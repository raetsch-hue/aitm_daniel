#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Macht die Offline-Kopie des Hugging-Face-MCP-Kurses im Viewer lesbar.

  python coursetools/mcp-course-aufbereiten.py

Ausgangslage: AI_Course/mcp-course/units/ enthaelt die Originalseiten als
.mdx. Der Viewer kann das nicht anzeigen - er rendert Markdown, und MDX
bringt Bausteine mit (<Question>, <hfoptions>, <Youtube>), die als roher
Text im Dokument stehen bleiben wuerden.

Das Skript erzeugt zwei Dinge, beide vollstaendig automatisch:

  1. AI_Course/mcp-course/viewer/*.md
     Je eine Markdown-Fassung pro Kursseite, in der Reihenfolge des
     offiziellen Inhaltsverzeichnisses (units/_toctree.yml) durchnummeriert.
     Umgebaut werden nur die MDX-Bausteine und die Bildpfade; der Fliesstext
     bleibt Wort fuer Wort stehen. Code-Bloecke bleiben unangetastet, sonst
     wuerde z. B. "<Tool ...>" in einem Beispiel-Log mit umgeschrieben.

  2. Der Block MCP-COURSE in coursebook/dateien.js
     Alles zwischen den beiden Marker-Kommentaren wird ersetzt. Ausserhalb
     der Marker bleibt die Datei unberuehrt.

Quelle der Wahrheit bleibt units/*.mdx. Die Dateien unter viewer/ sind
Ableitungen und werden bei jedem Lauf neu geschrieben - dort nichts von Hand
aendern. Nach einer Aktualisierung des Kurses (siehe
AI_Course/mcp-course/README.md) einmal laufen lassen.

Aufruf von ueberall: das Skript findet das Repo-Wurzelverzeichnis selbst
(eine Ebene ueber dem eigenen Ordner).
"""

import html
import re
import sys
import datetime
from pathlib import Path

# ---------------------------------------------------------------- Einstellung

QUELLE   = "AI_Course/mcp-course/units"
ZIEL     = "AI_Course/mcp-course/viewer"
LIVE     = "https://huggingface.co/learn/mcp-course/"

# Bildpfade in den .mdx sind relativ zur .mdx ("../../bilder/x.png").
# Gerendert wird aber in coursebook/viewer.html, also muss der Pfad von
# dort aus stimmen.
BILD_ALT = "../../bilder/"
BILD_NEU = "../AI_Course/mcp-course/bilder/"

MARKER_AUF = "/* >>> MCP-COURSE-ANFANG"
MARKER_ZU  = "/* <<< MCP-COURSE-ENDE"

# ---------------------------------------------------------------- Werkzeuge

def toc_lesen(pfad):
    """units/_toctree.yml ohne PyYAML lesen. Das Format ist flach und stabil:
    eine Liste aus Kapiteln mit 'title' und 'sections' (je 'local' + 'title').
    Ein eigener Mini-Parser spart die Abhaengigkeit."""
    kapitel, aktuell, eintrag = [], None, None
    for roh in pfad.read_text(encoding="utf-8").splitlines():
        z = roh.strip()
        if roh.startswith("- title:"):
            aktuell = {"titel": wert(z[len("- title:"):]), "seiten": []}
            kapitel.append(aktuell)
        elif z.startswith("- local:") and aktuell is not None:
            eintrag = {"local": wert(z[len("- local:"):]), "titel": ""}
            aktuell["seiten"].append(eintrag)
        elif z.startswith("title:") and eintrag is not None:
            eintrag["titel"] = wert(z[len("title:"):])
    return kapitel


def wert(s):
    s = s.strip()
    if len(s) > 1 and s[0] == s[-1] and s[0] in "\"'":
        s = s[1:-1]
    return s.strip()


def kapitelkuerzel(titel):
    """"3.1. Use Case: ..." -> "3.1". Ohne fuehrende Nummer: leer."""
    m = re.match(r"\s*(\d+(?:\.\d+)*)\.", titel)
    return m.group(1) if m else ""


def esc(s):
    return html.escape(s, quote=False)


# ---------------------------------------------------------------- MDX-Umbau

def frage_umbauen(block):
    """<Question choices={[...]} /> -> Antwortliste plus eingeklappte
    Aufloesung. Die Aufloesung steckt in <details>, damit die Frage zum
    Selbsttest taugt und die Antwort nicht schon daneben steht.
    Innerhalb von <details> steht bewusst HTML: marked rendert Markdown
    in einem HTML-Block nicht mit."""
    auswahl = []
    for roh in re.findall(r"\{[^{}]*\}", block):
        t = re.search(r'text:\s*"((?:[^"\\]|\\.)*)"', roh)
        e = re.search(r'explain:\s*"((?:[^"\\]|\\.)*)"', roh)
        if not t:
            continue
        auswahl.append({
            "text":    t.group(1).replace('\\"', '"'),
            "erklaer": (e.group(1).replace('\\"', '"') if e else ""),
            "richtig": bool(re.search(r"correct:\s*true", roh)),
        })
    if not auswahl:
        return ["*(Frage konnte nicht umgesetzt werden, siehe Original-.mdx)*", ""]

    # Liste, nicht nur Zeilen: aufeinanderfolgende Textzeilen wuerde Markdown
    # zu einem einzigen Absatz zusammenziehen.
    zeilen = []
    for i, a in enumerate(auswahl):
        zeilen.append("- **%s.** %s" % (chr(65 + i), a["text"]))
    zeilen.append("")

    d = ["<details><summary>Auflösung</summary>"]
    for i, a in enumerate(auswahl):
        marke = "✅ <b>%s (richtig)</b>" % chr(65 + i) if a["richtig"] else "· %s" % chr(65 + i)
        d.append("<p>%s — %s</p>" % (marke, esc(a["erklaer"])))
    d.append("</details>")
    zeilen.append("".join(d))
    zeilen.append("")
    return zeilen


def umbauen(text):
    """Zeilenweise, weil Code-Bloecke unberuehrt bleiben muessen."""
    zeilen = text.split("\n")
    raus, i, im_code = [], 0, False

    while i < len(zeilen):
        z = zeilen[i]

        if z.lstrip().startswith("```"):
            im_code = not im_code
            raus.append(z)
            i += 1
            continue
        if im_code:
            raus.append(z)
            i += 1
            continue

        if z.lstrip().startswith("<Question"):
            block, j = [], i
            while j < len(zeilen) and zeilen[j].strip() != "/>":
                block.append(zeilen[j])
                j += 1
            raus.extend(frage_umbauen("\n".join(block)))
            i = j + 1
            continue

        s = z.strip()
        if s.startswith("<hfoptions") or s in ("</hfoption>", "</hfoptions>"):
            i += 1
            continue

        m = re.match(r'<hfoption\s+id="([^"]+)"\s*>', s)
        if m:
            raus.extend(["", "**Variante: %s**" % m.group(1), ""])
            i += 1
            continue

        m = re.match(r'<Youtube\s+id="([^"]+)"\s*/?>', s)
        if m:
            raus.extend(["", "> 🎥 Video: <https://www.youtube.com/watch?v=%s>" % m.group(1), ""])
            i += 1
            continue

        raus.append(z.replace(BILD_ALT, BILD_NEU))
        i += 1

    # Mehr als eine Leerzeile hintereinander entsteht durch die entfernten
    # Bausteine; zusammenstreichen, damit das Dokument ruhig bleibt.
    sauber, leer = [], 0
    for z in raus:
        leer = leer + 1 if not z.strip() else 0
        if leer < 3:
            sauber.append(z)
    return "\n".join(sauber).strip() + "\n"


def kopf(kapitel, local):
    return (
        "> **Offline-Kopie** aus dem Hugging-Face-MCP-Kurs, Kapitel „%s“.\n"
        "> Original online: <%s%s> · Quelltext: `%s/%s.mdx`\n"
        "> Aufbereitet von `coursetools/mcp-course-aufbereiten.py` — MDX-Bausteine\n"
        "> wurden zu Markdown umgebaut, der Text ist unverändert.\n\n"
        % (kapitel, LIVE, local, QUELLE, local)
    )


# ---------------------------------------------------------------- Ausgabe

def seiten_schreiben(wurzel, kapitel):
    quelle = wurzel / QUELLE
    ziel = wurzel / ZIEL
    ziel.mkdir(parents=True, exist_ok=True)
    for alt in ziel.glob("*.md"):
        alt.unlink()

    dokumente, n = [], 0
    for kap in kapitel:
        kurz = kapitelkuerzel(kap["titel"])
        for seite in kap["seiten"]:
            src = quelle / (seite["local"] + ".mdx")
            if not src.is_file():
                print("  Hinweis: %s fehlt, uebersprungen." % src.relative_to(wurzel))
                continue
            n += 1
            name = "%02d_%s.md" % (n, seite["local"].replace("/", "-"))
            (ziel / name).write_text(
                kopf(kap["titel"], seite["local"]) + umbauen(src.read_text(encoding="utf-8")),
                encoding="utf-8", newline="\n")
            dokumente.append({
                "rel": name,
                "titel": "%02d · %s · %s" % (n, ("U" + kurz) if kurz else "—", seite["titel"]),
            })
    return dokumente


def dateien_js_schreiben(wurzel, dokumente):
    zieldatei = wurzel / "coursebook" / "dateien.js"
    if not zieldatei.is_file():
        print("  Hinweis: coursebook/dateien.js nicht gefunden, Block nicht erneuert.")
        return None

    text = zieldatei.read_text(encoding="utf-8")
    i = text.find(MARKER_AUF)
    j = text.find(MARKER_ZU)
    if i < 0 or j < 0 or j < i:
        print("  Hinweis: Marker in dateien.js nicht gefunden, Block nicht erneuert.")
        print("  Erwartet werden die Zeilen '%s ...' und '%s ...'." % (MARKER_AUF, MARKER_ZU))
        return None

    eintraege = ["      Automatisch erzeugt von coursetools/mcp-course-aufbereiten.py.",
                 "      Nicht von Hand aendern - Aenderungen gehen beim naechsten Lauf",
                 "      verloren.  */",
                 ""]
    eintraege.append('  { datei: "../AI_Course/mcp-course/README.md",')
    eintraege.append('    titel: "00 · Über diese Offline-Kopie",')
    eintraege.append('    bereich: "mcp-course" },')
    eintraege.append("")
    for d in dokumente:
        eintraege.append('  { datei: "../%s/%s",' % (ZIEL, d["rel"]))
        eintraege.append('    titel: "%s",' % d["titel"].replace('"', '\\"'))
        eintraege.append('    bereich: "mcp-course" },')
        eintraege.append("")

    neu = (text[:i]
           + MARKER_AUF + " (%d Dokumente, %s)\n" % (len(dokumente) + 1,
                                                     datetime.date.today().isoformat())
           + "\n".join(eintraege)
           + "  " + MARKER_ZU
           + text[j + len(MARKER_ZU):])
    zieldatei.write_text(neu, encoding="utf-8", newline="\n")
    return zieldatei


# ---------------------------------------------------------------- Hauptlauf

def main():
    wurzel = Path(__file__).resolve().parent.parent
    toc = wurzel / QUELLE / "_toctree.yml"
    if not toc.is_file():
        print("Nicht gefunden: %s" % toc)
        print("Ohne die Offline-Kopie des Kurses gibt es nichts aufzubereiten.")
        return 1

    kapitel = toc_lesen(toc)
    dokumente = seiten_schreiben(wurzel, kapitel)
    js = dateien_js_schreiben(wurzel, dokumente)

    print("MCP-Kurs aufbereitet.")
    print("  %d Kapitel, %d Seiten" % (len(kapitel), len(dokumente)))
    print("  geschrieben: %s/" % ZIEL)
    if js:
        print("  Block erneuert: %s" % js.relative_to(wurzel))
    return 0


if __name__ == "__main__":
    sys.exit(main())
