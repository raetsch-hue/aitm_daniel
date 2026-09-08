#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Datenqualitätsprüfung für eine CSV-Datei — Bericht je Dimension.

Prüft Vollständigkeit, Konsistenz, Aktualität und Genauigkeit und gibt je Prüfung
aus: was geprüft wurde, wie viele Treffer es gibt und welche Zeilen als Beispiel.

Nur Standardbibliothek, keine Installation nötig. Spaltentypen (Datum, Zahl,
Kategorie, Freitext, laufende Nummer) werden aus den Daten erkannt, nicht
vorgegeben — das Skript ist damit nicht auf die GeAT-Datensätze festgelegt.

Aufrufe
-------
    python3 pruefe_datenqualitaet.py bewerberdatenbank.csv
    python3 pruefe_datenqualitaet.py kundendatenbank.csv --markdown > bericht.md
    python3 pruefe_datenqualitaet.py kundendatenbank.csv \
        --regel "besetzungen_2025<=anfragen_2025"
    python3 pruefe_datenqualitaet.py bewerberdatenbank.csv \
        --vergleich kundendatenbank.csv --vergleich-spalten niederlassung

Was jeder Befund für ein RAG-System bedeutet, steht in
ERLAEUTERUNG-pruefungen-und-rag.md — je Prüfung ein Satz.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import difflib
import json
import re
import statistics
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass, field

# --------------------------------------------------------------------------- #
# Konfiguration
# --------------------------------------------------------------------------- #

PLATZHALTER = {
    "-", "--", "---", ".", "..", "?", "k.a.", "ka", "kein", "keine", "keins",
    "n.a.", "na", "n/a", "n.n.", "nn", "null", "none", "unbekannt", "unbenannt",
    "leer", "entfällt", "entfaellt", "tbd", "offen", "siehe lebenslauf",
    "siehe anhang", "siehe cv", "wird nachgereicht", "nachreichen", "x", "xxx",
    "0000", "00000", "test",
}

DATUMSFORMATE = ["%Y-%m-%d", "%d.%m.%Y", "%d.%m.%y", "%Y/%m/%d", "%d/%m/%Y",
                 "%Y-%m-%dT%H:%M:%S", "%d.%m.%Y %H:%M"]

# Spaltennamen-Stichwörter, an denen fachliche Prüfungen andocken
STICH_FRIST = ("bis", "frist", "ablauf", "gueltig", "gültig", "verfall", "loesch", "lösch")
# Felder, die planmäßig in der Zukunft liegen dürfen und kein Fristende sind:
# ein Verfügbarkeitsdatum ist weder veraltet noch abgelaufen, wenn es vorbei ist.
STICH_ZUKUNFT = ("verfuegbar", "verfügbar", "beginn", "eintritt", "start")
STICH_GEBURT = ("geburt", "gebdat", "geboren")
STICH_PLZ = ("plz", "postleitzahl", "zip")
STICH_MAIL = ("mail",)
STICH_TEL = ("tel", "fon", "mobil", "handy")

# Spalten, die zwar aus Ziffern bestehen, aber keine Messgrößen sind
STICH_KENNUNG = STICH_PLZ + STICH_TEL

# Spalten, in denen Namen stehen: dort ist ein seltener, ähnlicher Wert ein anderer
# Mensch und kein Schreibfehler — Prüfung K4 lässt sie deshalb aus
STICH_NAME = ("name", "vorname", "nachname", "firma", "ansprechpartner", "kontaktperson",
              "betreuer", "person")

# Rechtsformen: nur für die Frage, ob zwei ähnliche Namen dieselbe Rechtsform tragen
RECHTSFORMEN = ("gmbhcokg", "gmbhundcokg", "gmbh", "mbh", "ag", "kgaa", "kg", "ohg",
                "ek", "gbr", "ug", "se", "eg", "ev")


def rechtsform(schluessel: str) -> str:
    """Rechtsform am Ende des Vergleichsschlüssels, sonst leer."""
    for rf in sorted(RECHTSFORMEN, key=len, reverse=True):
        if schluessel.endswith(rf):
            return rf
    return ""


MOJIBAKE = re.compile(r"Ã.|Â.|â€|ï»¿")
MAIL_OK = re.compile(r"^[^@\s]+@[^@\s.]+\.[A-Za-z]{2,}$")
ID_MUSTER = re.compile(r"^(?P<pre>[A-Za-zÄÖÜäöü_\-]*?)(?P<num>\d+)$")


# --------------------------------------------------------------------------- #
# Datenhaltung
# --------------------------------------------------------------------------- #

@dataclass
class Befund:
    """Ergebnis einer einzelnen Prüfung."""
    code: str
    dimension: str
    pruefung: str
    beschreibung: str
    treffer: int
    grundmenge: str
    beispiele: list[str] = field(default_factory=list)
    zeilen: set[int] = field(default_factory=set)   # 0-basierte Datensatzindizes

    @property
    def ok(self) -> bool:
        return self.treffer == 0


@dataclass
class Tabelle:
    pfad: str
    spalten: list[str]
    zeilen: list[dict[str, str]]
    trennzeichen: str
    kodierung: str

    def spalte(self, name: str) -> list[str]:
        return [z.get(name, "") for z in self.zeilen]

    @property
    def n(self) -> int:
        return len(self.zeilen)


# --------------------------------------------------------------------------- #
# Einlesen und Typerkennung
# --------------------------------------------------------------------------- #

def lese_csv(pfad: str) -> Tabelle:
    """Liest die Datei ohne jede Umwandlung: alle Werte bleiben Text."""
    rohdaten, kodierung = None, None
    for kod in ("utf-8-sig", "utf-8", "cp1252", "latin-1"):
        try:
            with open(pfad, "r", encoding=kod, newline="") as f:
                rohdaten = f.read()
            kodierung = kod
            break
        except UnicodeDecodeError:
            continue
    if rohdaten is None:
        raise SystemExit("Datei %s ist mit keiner der geprüften Kodierungen lesbar." % pfad)

    kopf = rohdaten.split("\n", 1)[0]
    trenn = max({",": kopf.count(","), ";": kopf.count(";"), "\t": kopf.count("\t"),
                 "|": kopf.count("|")}.items(), key=lambda x: x[1])[0]
    leser = csv.DictReader(rohdaten.splitlines(), delimiter=trenn)
    spalten = list(leser.fieldnames or [])
    zeilen = [{k: (v if v is not None else "") for k, v in z.items() if k is not None}
              for z in leser]
    return Tabelle(pfad, spalten, zeilen, trenn, kodierung)


def als_datum(wert: str):
    w = (wert or "").strip()
    if not w:
        return None
    for f in DATUMSFORMATE:
        try:
            return dt.datetime.strptime(w, f).date()
        except ValueError:
            continue
    return None


def datumsformat(wert: str):
    w = (wert or "").strip()
    for f in DATUMSFORMATE:
        try:
            dt.datetime.strptime(w, f)
            return f
        except ValueError:
            continue
    return None


def als_zahl(wert: str):
    w = (wert or "").strip().replace(" ", "").replace(" ", "")
    if not w:
        return None
    # deutsche und englische Schreibweise zulassen
    if "," in w and "." in w:
        w = w.replace(".", "").replace(",", ".")
    else:
        w = w.replace(",", ".")
    try:
        return float(w)
    except ValueError:
        return None


def leer(wert: str) -> bool:
    return (wert or "").strip() == ""


def platzhalter(wert: str) -> bool:
    w = (wert or "").strip().lower().rstrip(".")
    return bool(w) and (w in PLATZHALTER or w.rstrip(".") in PLATZHALTER)


def falte(s: str) -> str:
    """Vergleichsform: klein, ohne Umlaute, ohne Sonderzeichen, ohne Mehrfachleerzeichen."""
    s = (s or "").strip().lower()
    s = (s.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
          .replace("ß", "ss").replace("é", "e").replace("è", "e"))
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def bezeichnerschluessel(s: str) -> str:
    """Vergleichsform für Firmen- und Personennamen.

    Die Rechtsform wird *nicht* entfernt: „Kunststofftechnik Ohrdruf GmbH" und
    „Kunststofftechnik Ohrdruf OHG" sind zwei Rechtsträger, keine Dublette. Durch
    das Entfernen aller Leerzeichen fallen dagegen die Schreibvarianten derselben
    Rechtsform zusammen — „GmbH & Co. KG" und „GmbH & Co KG" ergeben denselben
    Schlüssel, ebenso „e.K." und „eK".
    """
    return re.sub(r"\s+", "", falte(s))


def typisiere(t: Tabelle) -> dict[str, str]:
    """Ordnet jeder Spalte einen Typ zu: id, datum, zahl, kategorie, text."""
    typen = {}
    for s in t.spalten:
        werte = [w for w in t.spalte(s) if not leer(w)]
        if not werte:
            typen[s] = "leer"
            continue
        probe = werte if len(werte) <= 400 else werte[:400]
        anteil = lambda f: sum(1 for w in probe if f(w)) / len(probe)

        ids = [ID_MUSTER.match(w.strip()) for w in probe]
        ist_id = (all(ids) and len({m.group("pre") for m in ids}) == 1
                  and len(set(werte)) / len(werte) > 0.98)
        if ist_id and ("id" in s.lower() or "nummer" in s.lower() or "nr" in s.lower()
                       or len(set(werte)) == t.n):
            typen[s] = "id"
        elif anteil(lambda w: als_datum(w) is not None) >= 0.7:
            typen[s] = "datum"
        elif any(x in s.lower() for x in STICH_KENNUNG):
            typen[s] = "kennung"
        elif anteil(lambda w: als_zahl(w) is not None) >= 0.9:
            typen[s] = "zahl"
        elif len(set(werte)) <= max(40, 0.05 * len(werte)):
            typen[s] = "kategorie"
        else:
            typen[s] = "text"
    return typen


# --------------------------------------------------------------------------- #
# Hilfen für den Bericht
# --------------------------------------------------------------------------- #

class Kontext:
    def __init__(self, t: Tabelle, typen: dict[str, str], id_spalte: str | None,
                 stichtag: dt.date, max_alter: int, n_beispiele: int):
        self.t, self.typen = t, typen
        self.id_spalte = id_spalte
        self.stichtag, self.max_alter = stichtag, max_alter
        self.n_beispiele = n_beispiele

    def kennung(self, i: int) -> str:
        """Zeilenbezeichnung für den Bericht: Datensatz-ID plus CSV-Zeilennummer."""
        if self.id_spalte:
            return "%s (Z%d)" % (self.t.zeilen[i].get(self.id_spalte, "?"), i + 2)
        return "Zeile %d" % (i + 2)

    def bsp(self, paare) -> list[str]:
        """paare: Iterable von (index, text). Gibt bis n_beispiele Einträge zurück."""
        out = []
        for i, txt in paare:
            out.append("%s: %s" % (self.kennung(i), txt))
            if len(out) >= self.n_beispiele:
                break
        return out


def pz(x: float, stellen: int = 2) -> str:
    """Prozentwert in deutscher Schreibweise."""
    return ("%.*f" % (stellen, x)).replace(".", ",")


def kurz(wert: str, n: int = 60) -> str:
    w = (wert or "").replace("\n", " ")
    return w if len(w) <= n else w[: n - 1] + "…"


# --------------------------------------------------------------------------- #
# Dimension 1: Vollständigkeit
# --------------------------------------------------------------------------- #

def pruefe_vollstaendigkeit(k: Kontext, regeln) -> list[Befund]:
    t, out = k.t, []

    # V1 — fehlende Werte je Spalte
    treffer, beispiele, zeilen, je_spalte = 0, [], set(), []
    for s in t.spalten:
        idx = [i for i, w in enumerate(t.spalte(s)) if leer(w)]
        if idx:
            je_spalte.append((s, len(idx), idx))
            treffer += len(idx)
            zeilen.update(idx)
    je_spalte.sort(key=lambda x: -x[1])
    for s, n, idx in je_spalte[: k.n_beispiele]:
        beispiele.append("Spalte `%s`: %d leer (%s %%), z. B. %s"
                         % (s, n, pz(100 * n / t.n, 1),
                            ", ".join(k.kennung(i) for i in idx[:3])))
    out.append(Befund("V1", "Vollständigkeit", "Fehlende Werte je Spalte",
                      "leere Zellen, spaltenweise gezählt",
                      treffer, "%d Zellen" % (t.n * len(t.spalten)), beispiele, zeilen))

    # V2 — Platzhalter, die wie ein gepflegter Wert aussehen
    treffer, beispiele, zeilen = 0, [], set()
    fund = defaultdict(list)
    for s in t.spalten:
        for i, w in enumerate(t.spalte(s)):
            if platzhalter(w):
                fund[s].append((i, w))
                treffer += 1
                zeilen.add(i)
    for s, lst in sorted(fund.items(), key=lambda x: -len(x[1]))[: k.n_beispiele]:
        beispiele.append("Spalte `%s`: %d Platzhalter, z. B. %s"
                         % (s, len(lst), "; ".join("%s = „%s“" % (k.kennung(i), w)
                                                   for i, w in lst[:3])))
    out.append(Befund("V2", "Vollständigkeit", "Platzhalter statt Inhalt",
                      "Werte wie „k.A.“, „-“, „siehe Lebenslauf“ — Feld gefüllt, Aussage keine",
                      treffer, "%d Zellen" % (t.n * len(t.spalten)), beispiele, zeilen))

    # V3 — Zeilen mit auffällig vielen Lücken
    grenze = max(2, int(0.25 * len(t.spalten)))
    lueckig = []
    for i, z in enumerate(t.zeilen):
        n_leer = sum(1 for s in t.spalten if leer(z.get(s, "")) or platzhalter(z.get(s, "")))
        if n_leer >= grenze:
            lueckig.append((i, n_leer))
    lueckig.sort(key=lambda x: -x[1])
    out.append(Befund("V3", "Vollständigkeit", "Zeilen mit mehreren Lücken",
                      "Datensätze mit mindestens %d leeren oder Platzhalter-Feldern" % grenze,
                      len(lueckig), "%d Datensätze" % t.n,
                      k.bsp((i, "%d von %d Feldern ohne Inhalt" % (n, len(t.spalten)))
                            for i, n in lueckig),
                      {i for i, _ in lueckig}))

    # V4 — Lücken in der laufenden Nummerierung
    for s in [s for s in t.spalten if k.typen.get(s) == "id"]:
        werte = [w.strip() for w in t.spalte(s) if not leer(w)]
        treffer_m = [ID_MUSTER.match(w) for w in werte]
        if not all(treffer_m):
            continue
        nummern = sorted(int(m.group("num")) for m in treffer_m)
        breite = len(treffer_m[0].group("num"))
        praefix = treffer_m[0].group("pre")
        fehlend, luecken = [], 0
        for a, b in zip(nummern, nummern[1:]):
            if b - a > 1:
                luecken += 1
                fehlend.extend(range(a + 1, b))
        beispiele = []
        if fehlend:
            gruppen, lauf = [], [fehlend[0]]
            for x in fehlend[1:]:
                if x == lauf[-1] + 1:
                    lauf.append(x)
                else:
                    gruppen.append(lauf); lauf = [x]
            gruppen.append(lauf)
            for g in gruppen[: k.n_beispiele]:
                fmt = lambda x: "%s%0*d" % (praefix, breite, x)
                beispiele.append("%s fehlt" % fmt(g[0]) if len(g) == 1
                                 else "%s bis %s fehlen (%d Nummern)"
                                      % (fmt(g[0]), fmt(g[-1]), len(g)))
        out.append(Befund("V4", "Vollständigkeit",
                          "Lücken in der laufenden Nummerierung (`%s`)" % s,
                          "erwartet %d Datensätze zwischen der kleinsten und der größten "
                          "Nummer, vorhanden %d" % (nummern[-1] - nummern[0] + 1, len(nummern)),
                          len(fehlend), "%d Nummern im Wertebereich"
                          % (nummern[-1] - nummern[0] + 1), beispiele, set()))

    # V5 — Werte, die nur in der Vergleichsdatei vorkommen
    for b in regeln.get("vergleich", []):
        out.append(b)
    return out


# --------------------------------------------------------------------------- #
# Dimension 2: Konsistenz
# --------------------------------------------------------------------------- #

def pruefe_konsistenz(k: Kontext, regeln) -> list[Befund]:
    t, out = k.t, []
    inhalt = [s for s in t.spalten if k.typen.get(s) != "id"]

    # K1 — exakte Dubletten über alle Inhaltsspalten
    schluessel = defaultdict(list)
    for i, z in enumerate(t.zeilen):
        schluessel[tuple(z.get(s, "").strip() for s in inhalt)].append(i)
    dubl = {sch: idx for sch, idx in schluessel.items() if len(idx) > 1}
    zeilen = {i for idx in dubl.values() for i in idx[1:]}
    out.append(Befund("K1", "Konsistenz", "Exakte Dubletten",
                      "Datensätze, die in allen Feldern außer der Nummer übereinstimmen",
                      len(zeilen), "%d Datensätze" % t.n,
                      k.bsp((idx[1], "identisch zu %s" % k.kennung(idx[0]))
                            for idx in dubl.values()), zeilen))

    # K2 — unscharfe Dubletten in bezeichnenden Textspalten
    kandidaten = [s for s in t.spalten
                  if k.typen.get(s) == "text"
                  and len({falte(w) for w in t.spalte(s) if not leer(w)}) > 0.5 * t.n]
    MIN_STUETZEN = 2
    # Eine Spalte stützt nur, wenn sie überhaupt unterscheidet. `anfragen_2025` mit
    # fünfzehn verschiedenen Werten tut das nicht: dass zwei Kunden je drei Anfragen
    # hatten, ist Zufall und kein Hinweis auf denselben Betrieb.
    MIN_AUSPRAEGUNGEN = max(20, int(0.05 * t.n))
    stuetzbar = {sp for sp in t.spalten
                 if k.typen.get(sp) not in ("id", "kategorie", "leer")
                 and len({w.strip() for w in t.spalte(sp) if not leer(w)}) >= MIN_AUSPRAEGUNGEN}

    def stuetzt(s_name: str, i: int, j: int) -> bool:
        """Zwei Zeilen gelten nur als Dublette, wenn neben der Bezeichnung mindestens
        MIN_STUETZEN weitere belegte Felder übereinstimmen. Ohne diese Bedingung wären
        zwei Menschen mit demselben Namen eine Dublette, und das sind sie nicht."""
        gleich = 0
        for sp in stuetzbar:
            if sp == s_name:
                continue
            a_, b_ = t.zeilen[i].get(sp, "").strip(), t.zeilen[j].get(sp, "").strip()
            if a_ and b_ and falte(a_) == falte(b_):
                gleich += 1
        return gleich >= MIN_STUETZEN

    treffer, beispiele, zeilen = 0, [], set()
    for s in kandidaten:
        gruppen = defaultdict(list)
        for i, w in enumerate(t.spalte(s)):
            if not leer(w):
                gruppen[bezeichnerschluessel(w)].append(i)
        # gleicher Schlüssel = Dublette trotz abweichender Schreibweise
        for sch, idx in gruppen.items():
            if len(idx) > 1 and sch and stuetzt(s, idx[0], idx[1]):
                treffer += len(idx) - 1
                zeilen.update(idx[1:])
                if len(beispiele) < k.n_beispiele:
                    beispiele.append("%s: „%s“ ↔ %s: „%s“"
                                     % (k.kennung(idx[0]), kurz(t.zeilen[idx[0]][s]),
                                        k.kennung(idx[1]), kurz(t.zeilen[idx[1]][s])))
        # ähnliche, nicht identische Schlüssel — blockweise, damit es bei großen Dateien trägt
        bloecke = defaultdict(list)
        for sch in gruppen:
            if sch:
                bloecke[sch[:4]].append(sch)
        for blk in bloecke.values():
            if len(blk) < 2 or len(blk) > 60:
                continue
            for a_i in range(len(blk)):
                for b_i in range(a_i + 1, len(blk)):
                    a, b = blk[a_i], blk[b_i]
                    if rechtsform(a) != rechtsform(b):
                        continue      # verschiedene Rechtsform = verschiedener Rechtsträger
                    if (difflib.SequenceMatcher(None, a, b).ratio() >= 0.95
                            and stuetzt(s, gruppen[a][0], gruppen[b][0])):
                        i, j = gruppen[a][0], gruppen[b][0]
                        treffer += 1
                        zeilen.update({i, j})
                        if len(beispiele) < k.n_beispiele:
                            beispiele.append("%s: „%s“ ≈ %s: „%s“"
                                             % (k.kennung(i), kurz(t.zeilen[i][s]),
                                                k.kennung(j), kurz(t.zeilen[j][s])))
    out.append(Befund("K2", "Konsistenz", "Unscharfe Dubletten",
                      "derselbe Betrieb oder dieselbe Person zweimal, mit abweichender "
                      "Schreibweise (Vergleich ohne Groß-/Kleinschreibung, Umlaute, "
                      "Sonderzeichen und Leerzeichen, Rechtsform bleibt erhalten; zusätzlich "
                      "Ähnlichkeit ab 95 Prozent bei gleicher Rechtsform). "
                      "Gezählt wird nur, wenn mindestens zwei weitere unterscheidungs"
                      "kräftige Felder übereinstimmen — Spalten mit wenigen Ausprägungen "
                      "zählen dabei nicht",
                      treffer, "Spalten: %s" % (", ".join("`%s`" % s for s in kandidaten) or "keine"),
                      beispiele, zeilen))

    # K3 — Schreibvarianten desselben Werts in kategorialen Spalten
    treffer, beispiele, zeilen = 0, [], set()
    for s in [s for s in t.spalten if k.typen.get(s) in ("kategorie", "zahl", "datum")
              or k.typen.get(s) == "text"]:
        if k.typen.get(s) not in ("kategorie",):
            continue
        haeufig = Counter(w.strip() for w in t.spalte(s) if not leer(w))
        gruppen = defaultdict(list)
        for w in haeufig:
            gruppen[falte(w)].append(w)
        for sch, varianten in gruppen.items():
            if len(varianten) > 1:
                leit = max(varianten, key=lambda v: haeufig[v])
                neben = [v for v in varianten if v != leit]
                n = sum(haeufig[v] for v in neben)
                treffer += n
                idx = [i for i, w in enumerate(t.spalte(s)) if w.strip() in neben]
                zeilen.update(idx)
                if len(beispiele) < k.n_beispiele:
                    beispiele.append("Spalte `%s`: „%s“ (%dx) auch als %s — z. B. %s"
                                     % (s, leit, haeufig[leit],
                                        ", ".join("„%s“ (%dx)" % (v, haeufig[v]) for v in neben),
                                        ", ".join(k.kennung(i) for i in idx[:2])))
        # Werte, die nur einmal vorkommen, während ein ähnlicher Wert dominiert
        gemeldet = {v for varianten in gruppen.values() if len(varianten) > 1
                    for v in varianten}
        selten = [w for w, n in haeufig.items()
                  if n <= max(1, 0.002 * t.n) and w not in gemeldet]
        for w in selten:
            nah = difflib.get_close_matches(falte(w), [falte(x) for x in haeufig
                                                       if haeufig[x] > 10 * max(1, haeufig[w])],
                                            n=1, cutoff=0.8)
            if nah:
                idx = [i for i, v in enumerate(t.spalte(s)) if v.strip() == w]
                treffer += len(idx)
                zeilen.update(idx)
                if len(beispiele) < k.n_beispiele:
                    beispiele.append("Spalte `%s`: Einzelwert „%s“ ähnelt einem häufigen Wert "
                                     "— z. B. %s" % (s, w, ", ".join(k.kennung(i) for i in idx[:2])))
    out.append(Befund("K3", "Konsistenz", "Schreibvarianten desselben Werts",
                      "kategoriale Spalten: Werte, die nach Faltung zusammenfallen "
                      "(Groß-/Kleinschreibung, Umlaute, Satzzeichen, Leerzeichen)",
                      treffer, "%d Datensätze" % t.n, beispiele, zeilen))

    # K4 — Schreibvarianten in Freitextfeldern, tokenweise
    treffer, beispiele, zeilen = 0, [], set()
    # Kennungen sind kein Freitext: „info@…" und „office@…" sind zwei Postfächer
    # derselben Firma, keine zwei Schreibweisen desselben Werts.
    for s in [s for s in t.spalten if k.typen.get(s) == "text"
              and not any(x in s.lower() for x in STICH_NAME + STICH_MAIL + STICH_TEL)]:
        token = defaultdict(list)
        for i, w in enumerate(t.spalte(s)):
            for teil in re.split(r"[;,/|]| und ", w or ""):
                teil = teil.strip(" .()")
                if 4 <= len(teil) <= 45:
                    token[teil].append(i)
        if not token:
            continue
        haeufig = {tk: len(idx) for tk, idx in token.items()}
        gross = [tk for tk, n in haeufig.items() if n >= max(3, 0.004 * t.n)]
        klein = [tk for tk, n in haeufig.items() if n <= 2]
        for tk in klein:
            nah = difflib.get_close_matches(falte(tk), [falte(g) for g in gross],
                                            n=1, cutoff=0.82)
            if nah:
                leit = next(g for g in gross if falte(g) == nah[0])
                treffer += len(token[tk])
                zeilen.update(token[tk])
                if len(beispiele) < k.n_beispiele:
                    beispiele.append("Spalte `%s`: „%s“ (%dx) neben „%s“ (%dx) — z. B. %s"
                                     % (s, tk, haeufig[tk], leit, haeufig[leit],
                                        ", ".join(k.kennung(i) for i in token[tk][:2])))
    out.append(Befund("K4", "Konsistenz", "Schreibvarianten in Freitextfeldern",
                      "Freitext an Trennzeichen zerlegt; seltene Bausteine, die einem "
                      "häufigen Baustein ähneln (Ähnlichkeit ab 82 Prozent)",
                      treffer, "%d Datensätze" % t.n, beispiele, zeilen))

    # K5 — gemischte Datums- und Zahlenformate
    treffer, beispiele, zeilen = 0, [], set()
    for s in [s for s in t.spalten if k.typen.get(s) == "datum"]:
        formate = Counter()
        traeger = defaultdict(list)
        for i, w in enumerate(t.spalte(s)):
            f = datumsformat(w)
            if f:
                formate[f] += 1
                traeger[f].append(i)
        if len(formate) > 1:
            leit = formate.most_common(1)[0][0]
            for f, n in formate.items():
                if f == leit:
                    continue
                treffer += n
                zeilen.update(traeger[f])
                if len(beispiele) < k.n_beispiele:
                    beispiele.append("Spalte `%s`: %d Werte im Format %s statt %s — z. B. %s"
                                     % (s, n, f, leit,
                                        "; ".join("%s = %s" % (k.kennung(i), t.zeilen[i][s])
                                                  for i in traeger[f][:2])))
    for s in [s for s in t.spalten if k.typen.get(s) == "zahl"]:
        komma = [i for i, w in enumerate(t.spalte(s)) if "," in (w or "")]
        punkt = [i for i, w in enumerate(t.spalte(s)) if "." in (w or "")]
        if komma and punkt:
            neben = punkt if len(punkt) < len(komma) else komma
            treffer += len(neben)
            zeilen.update(neben)
            if len(beispiele) < k.n_beispiele:
                beispiele.append("Spalte `%s`: Komma und Punkt als Dezimaltrennzeichen "
                                 "gemischt (%d zu %d) — z. B. %s"
                                 % (s, len(komma), len(punkt),
                                    "; ".join("%s = %s" % (k.kennung(i), t.zeilen[i][s])
                                              for i in neben[:2])))
    out.append(Befund("K5", "Konsistenz", "Gemischte Schreibweisen bei Datum und Zahl",
                      "je Spalte das häufigste Format als Leitformat, alles andere als Abweichung",
                      treffer, "%d Datensätze" % t.n, beispiele, zeilen))

    # K6 — doppelte Datensatznummern
    for s in [s for s in t.spalten if k.typen.get(s) == "id"]:
        zaehler = Counter(w.strip() for w in t.spalte(s) if not leer(w))
        mehrfach = {w: n for w, n in zaehler.items() if n > 1}
        idx = {i for i, w in enumerate(t.spalte(s)) if w.strip() in mehrfach}
        out.append(Befund("K6", "Konsistenz", "Mehrfach vergebene Nummern (`%s`)" % s,
                          "dieselbe Datensatznummer in mehr als einer Zeile",
                          len(idx), "%d Datensätze" % t.n,
                          k.bsp((i, "Nummer %s kommt %dx vor"
                                 % (t.zeilen[i][s], mehrfach[t.zeilen[i][s].strip()]))
                                for i in sorted(idx)), idx))

    # K7 — fachliche Regeln aus der Kommandozeile
    for b in regeln.get("regeln", []):
        out.append(b)
    return out


# --------------------------------------------------------------------------- #
# Dimension 3: Aktualität
# --------------------------------------------------------------------------- #

def pruefe_aktualitaet(k: Kontext) -> list[Befund]:
    t, out = k.t, []
    datumsspalten = [s for s in t.spalten if k.typen.get(s) == "datum"]
    # Für die Frage „wie alt sind die Daten?" zählen Ereignis- und Kontaktdaten.
    # Ein Geburtsdatum ist immer alt, ein Fristende gehört zu Prüfung A3.
    verlaufsspalten = [s for s in datumsspalten
                       if not any(x in s.lower()
                                  for x in STICH_GEBURT + STICH_FRIST + STICH_ZUKUNFT)]
    grenze = k.stichtag - dt.timedelta(days=k.max_alter)

    # A1 — Datumswerte älter als die Schwelle
    treffer, beispiele, zeilen = 0, [], set()
    for s in verlaufsspalten:
        alt = [(i, als_datum(w)) for i, w in enumerate(t.spalte(s))
               if als_datum(w) and als_datum(w) < grenze]
        if alt:
            treffer += len(alt)
            zeilen.update(i for i, _ in alt)
            if len(beispiele) < k.n_beispiele:
                aeltestes = min(alt, key=lambda x: x[1])
                beispiele.append("Spalte `%s`: %d Werte vor %s (%s %%), ältester %s bei %s"
                                 % (s, len(alt), grenze.isoformat(), pz(100 * len(alt) / t.n, 1),
                                    aeltestes[1].isoformat(), k.kennung(aeltestes[0])))
    out.append(Befund("A1", "Aktualität", "Datumsfelder älter als die Schwelle",
                      "Ereignis- und Kontaktdaten (%s) vor dem %s, also älter als "
                      "%d Tage bezogen auf den Stichtag %s"
                      % (", ".join("`%s`" % s for s in verlaufsspalten) or "keine",
                         grenze.isoformat(), k.max_alter, k.stichtag.isoformat()),
                      treffer, "%d Datumswerte"
                      % sum(1 for s in verlaufsspalten for w in t.spalte(s) if als_datum(w)),
                      beispiele, zeilen))

    # A2 — Datum in der Zukunft, wo keines sein darf
    treffer, beispiele, zeilen = 0, [], set()
    for s in datumsspalten:
        if any(x in s.lower() for x in STICH_FRIST + STICH_ZUKUNFT):
            continue                      # Fristen und Plandaten dürfen in der Zukunft liegen
        zu = [(i, als_datum(w)) for i, w in enumerate(t.spalte(s))
              if als_datum(w) and als_datum(w) > k.stichtag]
        if zu:
            treffer += len(zu)
            zeilen.update(i for i, _ in zu)
            if len(beispiele) < k.n_beispiele:
                beispiele.extend(k.bsp((i, "`%s` = %s liegt nach dem Stichtag"
                                        % (s, d.isoformat())) for i, d in zu))
    out.append(Befund("A2", "Aktualität", "Datum in der Zukunft",
                      "Ereignisfelder (kein Fristfeld) mit einem Datum nach dem Stichtag",
                      treffer, "%d Datensätze" % t.n, beispiele[: k.n_beispiele], zeilen))

    # A3 — überschrittene Fristen bei noch aktivem Datensatz
    treffer, beispiele, zeilen = 0, [], set()
    fristspalten = [s for s in datumsspalten if any(x in s.lower() for x in STICH_FRIST)
                    and not any(x in s.lower() for x in STICH_ZUKUNFT)]
    statusspalten = [s for s in t.spalten if k.typen.get(s) == "kategorie"
                     and any(x in s.lower() for x in ("status", "zustand", "kennzeichen"))]
    for s in fristspalten:
        ab = [(i, als_datum(w)) for i, w in enumerate(t.spalte(s))
              if als_datum(w) and als_datum(w) < k.stichtag]
        for i, d in ab:
            treffer += 1
            zeilen.add(i)
            if len(beispiele) < k.n_beispiele:
                st = ("Status „%s“" % t.zeilen[i][statusspalten[0]]) if statusspalten else "—"
                beispiele.append("%s: `%s` = %s abgelaufen, %s"
                                 % (k.kennung(i), s, d.isoformat(), st))
    out.append(Befund("A3", "Aktualität", "Abgelaufene Fristen",
                      "Spalten mit Fristbezug (%s), deren Datum vor dem Stichtag liegt"
                      % (", ".join("`%s`" % s for s in fristspalten) or "keine erkannt"),
                      treffer, "%d Datensätze" % t.n, beispiele, zeilen))

    # A4 — Lücken in der Zeitreihe, gemessen an der örtlichen Dichte
    treffer, beispiele = 0, []
    for s in verlaufsspalten:
        daten = sorted(als_datum(w) for w in t.spalte(s) if als_datum(w))
        if len(daten) < 30:
            continue
        abstaende = [(b - a).days for a, b in zip(daten, daten[1:])]
        luecken = []
        for n, d in enumerate(abstaende):
            if d < 14:
                continue
            # Ein dünn belegter Altbestand erzeugt große Abstände, ohne dass etwas
            # fehlt. Was ein Loch davon unterscheidet: bei einem Loch ist es auf
            # *beiden* Seiten dicht. Geprüft wird deshalb, ob die zehn Einträge
            # davor und die zehn danach jeweils in höchstens 30 Tagen liegen.
            vor, nach = daten[max(0, n - 9):n + 1], daten[n + 1:n + 11]
            if len(vor) < 5 or len(nach) < 5:
                continue
            if (vor[-1] - vor[0]).days > 30 or (nach[-1] - nach[0]).days > 30:
                continue
            dichte = ((vor[-1] - vor[0]).days + (nach[-1] - nach[0]).days) / \
                     (len(vor) + len(nach) - 2)
            luecken.append((daten[n], daten[n + 1], d, dichte))
        for a, b, d, dichte in luecken:
            treffer += 1
            if len(beispiele) < 2 * k.n_beispiele:
                monate = []
                cur = (a.year, a.month) if a.day > 25 else None
                m = (a.year, a.month)
                while True:
                    m = (m[0] + 1, 1) if m[1] == 12 else (m[0], m[1] + 1)
                    if (m[0], m[1]) >= (b.year, b.month):
                        break
                    monate.append(m)
                zusatz = (", darin ohne jeden Eintrag: %s"
                          % ", ".join("%02d/%d" % (x[1], x[0]) for x in monate)) if monate else ""
                beispiele.append("Spalte `%s`: %d Tage ohne Eintrag zwischen %s und %s "
                                 "— davor und danach liegen im Mittel %.1f Tage zwischen "
                                 "zwei Einträgen%s"
                                 % (s, d, a.isoformat(), b.isoformat(), dichte, zusatz))
    out.append(Befund("A4", "Aktualität", "Zeitliche Lücken in der Reihe",
                      "Abstände zwischen zwei aufeinanderfolgenden Einträgen, die mindestens "
                      "14 Tage betragen und auf beiden Seiten von dicht belegten "
                      "Zeiträumen eingefasst sind (je zehn Einträge innerhalb von 30 Tagen) "
                      "— ein dünner Altbestand ist damit keine Lücke, ein Loch in einer "
                      "laufenden Reihe schon",
                      treffer, "Zeitreihe je Datumsspalte", beispiele, set()))
    return out


# --------------------------------------------------------------------------- #
# Dimension 4: Genauigkeit
# --------------------------------------------------------------------------- #

def pruefe_genauigkeit(k: Kontext) -> list[Befund]:
    t, out = k.t, []

    # G1 — Zahlen außerhalb des plausiblen Bereichs
    treffer, beispiele, zeilen = 0, [], set()
    for s in [s for s in t.spalten if k.typen.get(s) == "zahl"]:
        werte = [(i, als_zahl(w)) for i, w in enumerate(t.spalte(s)) if als_zahl(w) is not None]
        if len(werte) < 20:
            continue
        zahlen = sorted(v for _, v in werte)
        ganzzahlig = all(float(v).is_integer() and v >= 0 for v in zahlen)
        if ganzzahlig:
            # Zählgrößen sind rechtsschief: der Quartilsabstand würde den gesamten
            # oberen Rand als Ausreißer melden. Deshalb ein Vielfaches des 99er-Perzentils.
            p99 = zahlen[min(len(zahlen) - 1, int(0.99 * len(zahlen)))]
            unten, oben = -0.5, max(3 * p99, p99 + 10)
        else:
            q1, q3 = statistics.quantiles(zahlen, n=4)[0], statistics.quantiles(zahlen, n=4)[2]
            iqr = q3 - q1
            unten, oben = q1 - 3 * iqr, q3 + 3 * iqr
        raus = [(i, v) for i, v in werte if v < unten or v > oben]
        if raus:
            treffer += len(raus)
            zeilen.update(i for i, _ in raus)
            if len(beispiele) < k.n_beispiele:
                beispiele.append("Spalte `%s`: %d Werte außerhalb [%.2f; %.2f] — z. B. %s"
                                 % (s, len(raus), unten, oben,
                                    "; ".join("%s = %s" % (k.kennung(i), t.zeilen[i][s])
                                              for i, _ in raus[:3])))
    out.append(Befund("G1", "Genauigkeit", "Zahlen außerhalb des plausiblen Bereichs",
                      "Grenzen aus den Daten selbst: bei Messgrößen unteres und oberes "
                      "Quartil ± dreifacher Quartilsabstand, bei Zählgrößen das Dreifache "
                      "des 99er-Perzentils",
                      treffer, "%d Datensätze" % t.n, beispiele, zeilen))

    # G2 — Postleitzahlen
    treffer, beispiele, zeilen = 0, [], set()
    for s in [s for s in t.spalten if any(x in s.lower() for x in STICH_PLZ)]:
        falsch = [(i, w) for i, w in enumerate(t.spalte(s))
                  if not leer(w) and not re.fullmatch(r"\d{5}", w.strip())]
        if falsch:
            treffer += len(falsch)
            zeilen.update(i for i, _ in falsch)
            beispiele.extend(k.bsp((i, "`%s` = „%s“ ist keine fünfstellige Postleitzahl"
                                    % (s, w)) for i, w in falsch))
    out.append(Befund("G2", "Genauigkeit", "Postleitzahlen mit falscher Länge",
                      "fünf Ziffern erwartet; vier Ziffern deuten auf eine verlorene führende Null",
                      treffer, "%d Datensätze" % t.n, beispiele[: k.n_beispiele], zeilen))

    # G3 — E-Mail-Adressen
    treffer, beispiele, zeilen = 0, [], set()
    for s in [s for s in t.spalten if any(x in s.lower() for x in STICH_MAIL)]:
        falsch = [(i, w) for i, w in enumerate(t.spalte(s))
                  if not leer(w) and not MAIL_OK.fullmatch(w.strip())]
        treffer += len(falsch)
        zeilen.update(i for i, _ in falsch)
        beispiele.extend(k.bsp((i, "`%s` = „%s“" % (s, w)) for i, w in falsch))
    out.append(Befund("G3", "Genauigkeit", "Unbrauchbare E-Mail-Adressen",
                      "genau ein @, Punkt in der Domain, keine Leerzeichen",
                      treffer, "%d Datensätze" % t.n, beispiele[: k.n_beispiele], zeilen))

    # G4 — Telefonnummern
    treffer, beispiele, zeilen = 0, [], set()
    for s in [s for s in t.spalten if any(x in s.lower() for x in STICH_TEL)]:
        falsch = [(i, w) for i, w in enumerate(t.spalte(s))
                  if not leer(w) and len(re.sub(r"\D", "", w)) < 9]
        treffer += len(falsch)
        zeilen.update(i for i, _ in falsch)
        beispiele.extend(k.bsp((i, "`%s` = „%s“ hat %d Ziffern"
                                % (s, w, len(re.sub(r"\D", "", w)))) for i, w in falsch))
    out.append(Befund("G4", "Genauigkeit", "Telefonnummern mit zu wenigen Ziffern",
                      "mindestens neun Ziffern erwartet (Vorwahl plus Rufnummer)",
                      treffer, "%d Datensätze" % t.n, beispiele[: k.n_beispiele], zeilen))

    # G5 — unplausible Geburtsdaten und Datumswerte außerhalb jedes sinnvollen Bereichs
    treffer, beispiele, zeilen = 0, [], set()
    for s in [s for s in t.spalten if k.typen.get(s) == "datum"]:
        ist_geburt = any(x in s.lower() for x in STICH_GEBURT)
        for i, w in enumerate(t.spalte(s)):
            d = als_datum(w)
            if not d:
                continue
            grund = None
            if ist_geburt:
                alter = (k.stichtag - d).days / 365.25
                if alter < 15:
                    grund = "Alter %.0f Jahre — unter 15" % alter
                elif alter > 75:
                    grund = "Alter %.0f Jahre — über 75" % alter
            elif d.year < 1990 or d.year > k.stichtag.year + 10:
                grund = "Jahr %d außerhalb des sinnvollen Bereichs" % d.year
            if grund:
                treffer += 1
                zeilen.add(i)
                if len(beispiele) < k.n_beispiele:
                    beispiele.append("%s: `%s` = %s, %s" % (k.kennung(i), s, w, grund))
    out.append(Befund("G5", "Genauigkeit", "Unplausible Datumswerte",
                      "Geburtsdatum: Alter zwischen 15 und 75 Jahren; sonstige Datumsfelder "
                      "zwischen 1990 und Stichtag plus zehn Jahre",
                      treffer, "%d Datensätze" % t.n, beispiele, zeilen))

    # G6 — Zeichensatzschäden
    treffer, beispiele, zeilen = 0, [], set()
    for s in t.spalten:
        for i, w in enumerate(t.spalte(s)):
            if w and MOJIBAKE.search(w):
                treffer += 1
                zeilen.add(i)
                if len(beispiele) < k.n_beispiele:
                    beispiele.append("%s: `%s` = „%s“" % (k.kennung(i), s, kurz(w)))
    out.append(Befund("G6", "Genauigkeit", "Zeichensatzschäden",
                      "Zeichenfolgen wie Ã¼ oder â€ — ein Umlaut, der einmal falsch "
                      "kodiert gespeichert wurde",
                      treffer, "%d Zellen" % (t.n * len(t.spalten)), beispiele, zeilen))

    # G7 — Leerzeichen- und Formatschäden in Textfeldern
    treffer, beispiele, zeilen = 0, [], set()
    for s in t.spalten:
        for i, w in enumerate(t.spalte(s)):
            if not w:
                continue
            if w != w.strip() or "  " in w:
                treffer += 1
                zeilen.add(i)
                if len(beispiele) < k.n_beispiele:
                    beispiele.append("%s: `%s` = „%s“ (Leerzeichen am Rand oder doppelt)"
                                     % (k.kennung(i), s, kurz(w)))
    out.append(Befund("G7", "Genauigkeit", "Überzählige Leerzeichen",
                      "Werte mit Leerzeichen am Anfang oder Ende oder mit doppeltem "
                      "Leerzeichen — für jeden exakten Vergleich ein anderer Wert",
                      treffer, "%d Zellen" % (t.n * len(t.spalten)), beispiele, zeilen))
    return out


# --------------------------------------------------------------------------- #
# Zusatzprüfungen aus der Kommandozeile
# --------------------------------------------------------------------------- #

VERGLEICHE = {"<=": lambda a, b: a <= b, ">=": lambda a, b: a >= b,
              "<": lambda a, b: a < b, ">": lambda a, b: a > b,
              "==": lambda a, b: a == b, "!=": lambda a, b: a != b}


def pruefe_regel(k: Kontext, ausdruck: str, nr: int) -> Befund:
    """Fachliche Regel der Form spalte_a <= spalte_b (auch mit Zahl auf einer Seite)."""
    for op in ("<=", ">=", "!=", "==", "<", ">"):
        if op in ausdruck:
            links, rechts = [x.strip() for x in ausdruck.split(op, 1)]
            break
    else:
        raise SystemExit("Regel „%s“ enthält keinen der Vergleiche <= >= < > == !=" % ausdruck)

    def wert(seite, i):
        if seite in k.t.spalten:
            return als_zahl(k.t.zeilen[i][seite])
        return als_zahl(seite)

    verstoss = []
    for i in range(k.t.n):
        a, b = wert(links, i), wert(rechts, i)
        if a is None or b is None:
            continue
        if not VERGLEICHE[op](a, b):
            verstoss.append((i, "%s = %s, %s = %s" % (links, k.t.zeilen[i].get(links, a),
                                                      rechts, k.t.zeilen[i].get(rechts, b))))
    return Befund("K7.%d" % nr, "Konsistenz", "Fachliche Regel `%s`" % ausdruck,
                  "vorgegebene Regel, zeilenweise geprüft",
                  len(verstoss), "%d Datensätze" % k.t.n,
                  k.bsp(verstoss), {i for i, _ in verstoss})


def pruefe_vergleich(k: Kontext, andere: Tabelle, spalten: list[str], nr: int) -> list[Befund]:
    """Werte, die in der einen Datei vorkommen und in der anderen fehlen."""
    out = []
    for j, s in enumerate(spalten):
        if s not in k.t.spalten or s not in andere.spalten:
            continue
        hier = {w.strip() for w in k.t.spalte(s) if not leer(w)}
        dort = Counter(w.strip() for w in andere.spalte(s) if not leer(w))
        fehlt = sorted(set(dort) - hier)
        beispiele = ["„%s“ kommt in %s %dx vor, in dieser Datei nie"
                     % (w, andere.pfad.split("/")[-1], dort[w]) for w in fehlt]
        out.append(Befund("V5.%d" % (nr + j), "Vollständigkeit",
                          "Fehlende Ausprägungen in `%s` gegenüber %s"
                          % (s, andere.pfad.split("/")[-1]),
                          "Werteliste beider Dateien vergleichen: was steht dort und hier nicht?",
                          len(fehlt), "%d Ausprägungen in der Vergleichsdatei" % len(dort),
                          beispiele[: k.n_beispiele], set()))
    return out


# --------------------------------------------------------------------------- #
# Bericht
# --------------------------------------------------------------------------- #

DIMENSIONEN = ["Vollständigkeit", "Konsistenz", "Aktualität", "Genauigkeit"]


def bericht_text(t: Tabelle, typen, befunde: list[Befund], k: Kontext) -> str:
    z = []
    strich = "=" * 78
    z.append(strich)
    z.append("DATENQUALITÄTSBERICHT")
    z.append(strich)
    z.append("Datei          : %s" % t.pfad)
    z.append("Datensätze     : %d" % t.n)
    z.append("Spalten        : %d (%s)" % (len(t.spalten), ", ".join(t.spalten)))
    z.append("Format         : Trennzeichen „%s“, Kodierung %s"
             % (t.trennzeichen, t.kodierung))
    z.append("Spaltentypen   : %s" % ", ".join("%s=%s" % (s, typen[s]) for s in t.spalten))
    z.append("Stichtag       : %s, Altersschwelle %d Tage"
             % (k.stichtag.isoformat(), k.max_alter))
    z.append("")

    for dim in DIMENSIONEN:
        teil = [b for b in befunde if b.dimension == dim]
        if not teil:
            continue
        z.append("-" * 78)
        z.append("%s — %d Prüfungen, %d mit Treffern"
                 % (dim.upper(), len(teil), sum(1 for b in teil if not b.ok)))
        z.append("-" * 78)
        for b in teil:
            marke = "OK  " if b.ok else "!!  "
            z.append("%s[%s] %s" % (marke, b.code, b.pruefung))
            z.append("      Prüfung : %s" % b.beschreibung)
            z.append("      Treffer : %d von %s" % (b.treffer, b.grundmenge))
            if b.zeilen:
                z.append("      Zeilen  : %d betroffene Datensätze (%s %% der Datei)"
                         % (len(b.zeilen), pz(100 * len(b.zeilen) / t.n)))
            for e in b.beispiele:
                z.append("      · %s" % e)
            if not b.beispiele and not b.ok:
                z.append("      · (keine Beispiele darstellbar)")
            z.append("")

    betroffen = set()
    for b in befunde:
        betroffen |= b.zeilen
    z.append(strich)
    z.append("ZUSAMMENFASSUNG")
    z.append(strich)
    z.append("%-18s %8s %10s %s" % ("Dimension", "Treffer", "Zeilen", "Prüfungen mit Befund"))
    for dim in DIMENSIONEN:
        teil = [b for b in befunde if b.dimension == dim]
        if not teil:
            continue
        zl = set()
        for b in teil:
            zl |= b.zeilen
        z.append("%-18s %8d %10d %s"
                 % (dim, sum(b.treffer for b in teil), len(zl),
                    ", ".join(b.code for b in teil if not b.ok) or "—"))
    z.append("")
    z.append("Datensätze mit mindestens einem Befund: %d von %d = %s Prozent"
             % (len(betroffen), t.n, pz(100 * len(betroffen) / t.n)))
    z.append("")
    z.append("Ein Befund ist noch kein Fehler. V1 und A1 treffen auch Zeilen, in denen das")
    z.append("Fehlen fachlich richtig ist — ein Interessent hat keinen Verrechnungssatz, ein")
    z.append("inaktiver Kunde keine neue Anfrage. Der Bericht zählt, die Bewertung bleibt")
    z.append("fachlich und gehört zur Rolle, die für den Bestand einsteht.")
    z.append("")
    z.append("Zu lesen mit ERLAEUTERUNG-pruefungen-und-rag.md: dort steht je Prüfung in einem")
    z.append("Satz, was der Befund für ein RAG-System bedeutet.")
    z.append(strich)
    return "\n".join(z)


def bericht_markdown(t: Tabelle, typen, befunde: list[Befund], k: Kontext) -> str:
    z = ["# Datenqualitätsbericht — `%s`" % t.pfad.split("/")[-1], ""]
    z.append("%d Datensätze, %d Spalten, Trennzeichen `%s`, Kodierung %s, "
             "Stichtag %s, Altersschwelle %d Tage."
             % (t.n, len(t.spalten), t.trennzeichen, t.kodierung,
                k.stichtag.isoformat(), k.max_alter))
    z.append("")
    for dim in DIMENSIONEN:
        teil = [b for b in befunde if b.dimension == dim]
        if not teil:
            continue
        z.append("## %s" % dim)
        z.append("")
        z.append("| Code | Prüfung | Treffer | Betroffene Zeilen |")
        z.append("|---|---|---:|---:|")
        for b in teil:
            z.append("| %s | %s | %d | %d |" % (b.code, b.pruefung, b.treffer, len(b.zeilen)))
        z.append("")
        for b in teil:
            if b.ok:
                continue
            z.append("**[%s] %s** — %s" % (b.code, b.pruefung, b.beschreibung))
            z.append("")
            for e in b.beispiele:
                z.append("- %s" % e)
            z.append("")
    betroffen = set()
    for b in befunde:
        betroffen |= b.zeilen
    z.append("## Zusammenfassung")
    z.append("")
    z.append("Datensätze mit mindestens einem Befund: **%d von %d = %s Prozent**."
             % (len(betroffen), t.n, pz(100 * len(betroffen) / t.n)))
    z.append("")
    z.append("Ein Befund ist noch kein Fehler: V1 und A1 treffen auch Zeilen, in denen das "
             "Fehlen fachlich richtig ist. Der Bericht zählt, die Bewertung bleibt fachlich.")
    return "\n".join(z)


# --------------------------------------------------------------------------- #
# Einstieg
# --------------------------------------------------------------------------- #

def main(argv=None) -> int:
    p = argparse.ArgumentParser(
        description="Prüft eine CSV-Datei auf Datenqualität und schreibt einen Bericht.",
        epilog="Beispiel: python3 pruefe_datenqualitaet.py kundendatenbank.csv "
               "--regel \"besetzungen_2025<=anfragen_2025\"")
    p.add_argument("csv", help="Pfad zur zu prüfenden CSV-Datei")
    p.add_argument("--id-spalte", help="Spalte mit der laufenden Nummer (sonst automatisch)")
    p.add_argument("--stichtag", help="Bezugsdatum JJJJ-MM-TT (Vorgabe: heute)")
    p.add_argument("--max-alter-tage", type=int, default=730,
                   help="Schwelle für Prüfung A1 in Tagen (Vorgabe: 730)")
    p.add_argument("--beispiele", type=int, default=5,
                   help="Beispiele je Prüfung (Vorgabe: 5)")
    p.add_argument("--regel", action="append", default=[],
                   help="fachliche Regel, z. B. \"besetzungen_2025<=anfragen_2025\"; "
                        "mehrfach angebbar")
    p.add_argument("--vergleich", help="zweite CSV-Datei für den Wertelistenvergleich")
    p.add_argument("--vergleich-spalten",
                   help="Spalten für den Vergleich, mit Komma getrennt "
                        "(sonst alle gemeinsamen kategorialen Spalten)")
    p.add_argument("--markdown", action="store_true", help="Bericht als Markdown ausgeben")
    p.add_argument("--json", action="store_true", help="Befunde als JSON ausgeben")
    a = p.parse_args(argv)

    t = lese_csv(a.csv)
    if t.n == 0:
        print("Datei enthält keine Datensätze.", file=sys.stderr)
        return 1
    typen = typisiere(t)

    id_spalte = a.id_spalte or next((s for s in t.spalten if typen.get(s) == "id"), None)
    stichtag = dt.date.fromisoformat(a.stichtag) if a.stichtag else dt.date.today()
    k = Kontext(t, typen, id_spalte, stichtag, a.max_alter_tage, a.beispiele)

    zusatz = {"regeln": [], "vergleich": []}
    for nr, r in enumerate(a.regel, start=1):
        zusatz["regeln"].append(pruefe_regel(k, r, nr))
    if a.vergleich:
        andere = lese_csv(a.vergleich)
        if a.vergleich_spalten:
            spalten = [s.strip() for s in a.vergleich_spalten.split(",")]
        else:
            spalten = [s for s in t.spalten
                       if s in andere.spalten and typen.get(s) == "kategorie"]
        zusatz["vergleich"] = pruefe_vergleich(k, andere, spalten, 1)

    befunde = (pruefe_vollstaendigkeit(k, zusatz)
               + pruefe_konsistenz(k, zusatz)
               + pruefe_aktualitaet(k)
               + pruefe_genauigkeit(k))

    if a.json:
        print(json.dumps([{**b.__dict__, "zeilen": sorted(b.zeilen)} for b in befunde],
                         ensure_ascii=False, indent=1, default=list))
    elif a.markdown:
        print(bericht_markdown(t, typen, befunde, k))
    else:
        print(bericht_text(t, typen, befunde, k))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
