#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Baut das Inhaltsverzeichnis der Artefakte neu.

  python coursetools/inhalt-bauen.py

Erzeugt zwei Dinge, beide vollstaendig automatisch:

  1. artefakte/INHALT.md
     Ein Verzeichnis aller Markdown-Dateien unterhalb von artefakte/, mit
     Sprunglinks auf jede Ueberschrift der Ebenen 2 und 3. Die Linkform
     "#artefakte/datei.md#ueberschrift" ist die, die viewer.html versteht.

  2. Der Block ARTEFAKTE in coursebook/dateien.js
     Alles zwischen den beiden Marker-Kommentaren wird ersetzt. Ausserhalb
     der Marker bleibt die Datei unberuehrt.

Aufruf von ueberall: das Skript findet das Repo-Wurzelverzeichnis selbst
(eine Ebene ueber dem eigenen Ordner).

Warum ein Skript und keine Handarbeit: Ueberschriften aendern sich, und ein
Verzeichnis mit toten Sprungzielen ist schlechter als keines. Nach jeder
Aenderung an einem Artefakt einmal laufen lassen - oder push.bat ruft es auf.
"""

import re
import sys
import datetime
from pathlib import Path

# ---------------------------------------------------------------- Einstellung

# Ueberschriften bis zu dieser Ebene kommen ins Verzeichnis (2 = nur "##").
MAX_EBENE = 3

# Anzeigetitel im Viewer. Steht eine Datei hier nicht drin, wird der Titel
# aus Ordner und Frontmatter zusammengesetzt (siehe titel_bauen).
# Sortiert wird im Viewer alphabetisch nach diesem Titel.
TITEL = {
    "INHALT.md":                            "Alle Themen · Inhaltsverzeichnis",
    "checkliste.md":                        "Checkliste · Wissensüberprüfung (laufend)",
    "extra/README.md":                      "Extra · 0 Übersicht",
    "extra/01_modelle-und-verfahren.md":    "Extra · 1 Modelle und Verfahren, die nur genannt wurden",
    "extra/02_zahlen-und-befunde.md":       "Extra · 2 Zahlen und Befunde, die nicht behandelt wurden",
    "extra/03_spannungen-und-blinde-flecken.md": "Extra · 3 Spannungen und blinde Flecken",
}

# Reihenfolge der Gruppen im Inhaltsverzeichnis. Ordner, die hier nicht
# stehen, kommen alphabetisch hinten dran.
GRUPPEN = [
    ("",         "Übergreifend"),
    ("woche-01", "Woche 01 · KI-Vorhaben bewerten und mit dem Modell arbeiten"),
    ("woche-02", "Woche 02 · Change Management"),
    ("extra",    "Extra · was nicht behandelt wurde"),
]

MARKER_AUF = "/* >>> ARTEFAKTE-ANFANG"
MARKER_ZU  = "/* <<< ARTEFAKTE-ENDE"

# ---------------------------------------------------------------- Werkzeuge

def slug(text, vergeben):
    """Ankername wie marked.js 4.x ihn erzeugt.

    Muss zeichengenau mit dem Renderer uebereinstimmen, sonst zeigt der Link
    ins Leere. Reihenfolge wie im Original: kleinschreiben, trimmen, HTML-Tags
    raus, unerwuenschte Zeichen raus, Leerraum zu Bindestrich. Doppelte
    Ueberschriften bekommen -1, -2 ... angehaengt.
    """
    s = text.lower().strip()
    s = re.sub(r"<[!/a-z].*?>", "", s, flags=re.I)
    s = re.sub(r"[ -⁯⸀-⹿\\'!\"#$%&()*+,./:;<=>?@\[\]^`{|}~]", "", s)
    s = re.sub(r"\s", "-", s)
    n = vergeben.get(s, 0)
    vergeben[s] = n + 1
    return s if n == 0 else "%s-%d" % (s, n)


def linktext(s, in_tabelle=False):
    """Text, der als Linkbeschriftung sicher ist. Eckige Klammern kommen in
    Ueberschriften vor ("[Verweis]") und wuerden den Link zerlegen; in einer
    Tabellenzelle ist zusaetzlich der senkrechte Strich gefaehrlich."""
    s = s.replace("[", "\\[").replace("]", "\\]")
    return s.replace("|", "\\|") if in_tabelle else s


def frontmatter(zeilen):
    """YAML-Kopf als flaches dict. Nur Schluessel: Wert, mehr braucht es hier."""
    if not zeilen or zeilen[0].strip() != "---":
        return {}, 0
    daten = {}
    for i in range(1, len(zeilen)):
        z = zeilen[i].rstrip("\n")
        if z.strip() == "---":
            return daten, i + 1
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", z)
        if m:
            daten[m.group(1)] = m.group(2).strip().strip('"').strip("'")
    return daten, 0


def ueberschriften(zeilen, ab):
    """(Ebene, Text, Anker) je Ueberschrift. Codebloecke werden uebersprungen -
    eine Zeile '# ...' in einem Beispiel ist keine Ueberschrift."""
    treffer, im_code, vergeben = [], False, {}
    for z in zeilen[ab:]:
        if z.lstrip().startswith("```"):
            im_code = not im_code
            continue
        if im_code:
            continue
        m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", z)
        if not m:
            continue
        ebene, roh = len(m.group(1)), m.group(2)
        # Inline-Auszeichnung entfernen, wie der Renderer es tut
        text = re.sub(r"`([^`]*)`", r"\1", roh)
        text = re.sub(r"\*\*(.*?)\*\*|\*(.*?)\*|__(.*?)__|_(.*?)_",
                      lambda m: next(g for g in m.groups() if g is not None), text)
        text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
        anker = slug(text, vergeben)
        if 2 <= ebene <= MAX_EBENE:
            treffer.append((ebene, text, anker))
    return treffer


def titel_bauen(rel, fm, h1):
    """Anzeigetitel fuer den Viewer, wenn die Datei nicht in TITEL steht."""
    if rel in TITEL:
        return TITEL[rel]
    name = fm.get("artefakt") or h1 or Path(rel).stem
    ordner = str(Path(rel).parent).replace("\\", "/")
    if ordner.startswith("woche-"):
        return "Woche %s · %s" % (ordner.split("-", 1)[1], name)
    if ordner == "extra":
        return "Extra · %s" % name
    return name


def gruppenname(ordner):
    for schluessel, beschriftung in GRUPPEN:
        if schluessel == ordner:
            return beschriftung
    return ordner or "Übergreifend"


def gruppenrang(ordner):
    for i, (schluessel, _) in enumerate(GRUPPEN):
        if schluessel == ordner:
            return i
    return len(GRUPPEN)

# ---------------------------------------------------------------- Einlesen

def einlesen(wurzel):
    basis = wurzel / "artefakte"
    if not basis.is_dir():
        sys.exit("Ordner artefakte/ nicht gefunden unter %s" % wurzel)

    dokumente = []
    for pfad in sorted(basis.rglob("*.md")):
        rel = pfad.relative_to(basis).as_posix()
        if rel == "INHALT.md":
            continue
        zeilen = pfad.read_text(encoding="utf-8").splitlines()
        fm, ab = frontmatter(zeilen)
        h1 = next((re.sub(r"^#\s+", "", z).strip()
                   for z in zeilen[ab:] if z.startswith("# ")), "")
        dokumente.append({
            "rel": rel,
            "ordner": str(Path(rel).parent).replace("\\", "/").replace(".", ""),
            "titel": titel_bauen(rel, fm, h1),
            "h1": h1,
            "stand": fm.get("stand") or fm.get("datum") or "",
            "status": fm.get("status", ""),
            "thema": fm.get("thema", ""),
            "zweck": fm.get("zweck", ""),
            "kapitel": ueberschriften(zeilen, ab),
        })

    dokumente.sort(key=lambda d: (gruppenrang(d["ordner"]), d["titel"]))
    return dokumente

# ---------------------------------------------------------------- Ausgabe 1

def inhalt_schreiben(wurzel, dokumente):
    heute = datetime.date.today().isoformat()
    z = []
    z.append("---")
    z.append("artefakt: Inhaltsverzeichnis")
    z.append("stand: %s" % heute)
    z.append("status: automatisch erzeugt von coursetools/inhalt-bauen.py")
    z.append("zweck: alle Themen der Artefakte an einer Stelle, mit Sprung zur Überschrift")
    z.append("---")
    z.append("")
    z.append("# Inhaltsverzeichnis · Artefakte")
    z.append("")
    z.append("Alle Dokumente unterhalb von `artefakte/`, aufgeschlüsselt bis zur dritten "
             "Überschriftenebene. Ein Klick springt im Viewer direkt an die Stelle.")
    z.append("")
    z.append("> Diese Datei wird erzeugt, nicht gepflegt. Änderungen hier gehen beim "
             "nächsten Lauf von `coursetools/inhalt-bauen.py` verloren — die Überschriften "
             "ändert man im jeweiligen Dokument. Die Sprunglinks funktionieren im Viewer; "
             "auf github.com bleiben sie wirkungslos, dort ist die Dateiliste der Weg.")
    z.append("")

    # Kurzübersicht
    z.append("| Dokument | Stand | Abschnitte |")
    z.append("|---|---|---:|")
    for d in dokumente:
        z.append("| [%s](#artefakte/%s) | %s | %d |"
                 % (linktext(d["titel"], True), d["rel"], d["stand"] or "—", len(d["kapitel"])))
    z.append("")
    z.append("---")
    z.append("")

    letzte_gruppe = None
    for d in dokumente:
        if d["ordner"] != letzte_gruppe:
            letzte_gruppe = d["ordner"]
            z.append("## %s" % gruppenname(letzte_gruppe))
            z.append("")

        z.append("### [%s](#artefakte/%s)" % (linktext(d["titel"]), d["rel"]))
        z.append("")
        beschreibung = d["thema"] or d["zweck"]
        if beschreibung:
            z.append("*%s*" % beschreibung)
            z.append("")
        z.append("`artefakte/%s`%s" % (d["rel"], (" · Stand %s" % d["stand"]) if d["stand"] else ""))
        z.append("")
        if not d["kapitel"]:
            z.append("Keine Zwischenüberschriften.")
            z.append("")
            continue
        for ebene, text, anker in d["kapitel"]:
            einzug = "  " * (ebene - 2)
            z.append("%s- [%s](#artefakte/%s#%s)" % (einzug, linktext(text), d["rel"], anker))
        z.append("")

    z.append("---")
    z.append("")
    z.append("*Erzeugt am %s aus %d Dokumenten. Neu erzeugen: "
             "`python coursetools/inhalt-bauen.py`*" % (heute, len(dokumente)))
    z.append("")

    ziel = wurzel / "artefakte" / "INHALT.md"
    ziel.write_text("\n".join(z), encoding="utf-8", newline="\n")
    return ziel

# ---------------------------------------------------------------- Ausgabe 2

def dateien_js_schreiben(wurzel, dokumente):
    ziel = wurzel / "coursebook" / "dateien.js"
    if not ziel.is_file():
        print("  Hinweis: coursebook/dateien.js nicht gefunden, Block nicht erneuert.")
        return None

    text = ziel.read_text(encoding="utf-8")
    i = text.find(MARKER_AUF)
    j = text.find(MARKER_ZU)
    if i < 0 or j < 0 or j < i:
        print("  Hinweis: Marker in dateien.js nicht gefunden, Block nicht erneuert.")
        print("  Erwartet werden die Zeilen '%s ...' und '%s ...'." % (MARKER_AUF, MARKER_ZU))
        return None

    eintraege = ["      Automatisch erzeugt von coursetools/inhalt-bauen.py.",
                 "      Nicht von Hand aendern - Aenderungen gehen beim naechsten Lauf",
                 "      verloren. Anzeigetitel stellt man im Skript unter TITEL ein.  */",
                 ""]
    # Das Inhaltsverzeichnis selbst zuerst, dann die Dokumente
    alle = [{"rel": "INHALT.md", "titel": TITEL["INHALT.md"]}] + dokumente
    for d in alle:
        eintraege.append('  { datei: "../artefakte/%s",' % d["rel"])
        eintraege.append('    titel: "%s",' % d["titel"].replace('"', '\\"'))
        eintraege.append('    bereich: "artefakte" },')
        eintraege.append("")

    neu = (text[:i]
           + MARKER_AUF + " (%d Dokumente, %s)\n" % (len(alle), datetime.date.today().isoformat())
           + "\n".join(eintraege)
           + "  " + MARKER_ZU
           + text[j + len(MARKER_ZU):])
    ziel.write_text(neu, encoding="utf-8", newline="\n")
    return ziel

# ---------------------------------------------------------------- Hauptlauf

def main():
    wurzel = Path(__file__).resolve().parent.parent
    dokumente = einlesen(wurzel)

    a = inhalt_schreiben(wurzel, dokumente)
    b = dateien_js_schreiben(wurzel, dokumente)

    kapitel = sum(len(d["kapitel"]) for d in dokumente)
    print("Inhaltsverzeichnis erneuert.")
    print("  %d Dokumente, %d Abschnitte" % (len(dokumente), kapitel))
    print("  geschrieben: %s" % a.relative_to(wurzel))
    if b:
        print("  aktualisiert: %s (Block ARTEFAKTE)" % b.relative_to(wurzel))
    ohne = [d["rel"] for d in dokumente if not d["kapitel"]]
    if ohne:
        print("  ohne Zwischenüberschriften: %s" % ", ".join(ohne))


if __name__ == "__main__":
    main()
