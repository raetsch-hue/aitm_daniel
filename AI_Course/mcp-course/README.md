---
datum: 2026-09-09
status: abgelegt
quelle: https://github.com/huggingface/mcp-course
stand: Commit e706ccc0d7abe73c31813979c3451c0e31c8a464 (2026-04-26)
lizenz: Apache-2.0 (siehe LICENSE)
---

# MCP Course (Hugging Face) — Offline-Kopie

Vollständige Offline-Ablage des Kurses *Model Context Protocol* von Hugging Face.
Kein `woche:`-Feld im Frontmatter: das hier ist Referenzmaterial, kein datiertes Kursartefakt.

## Warum der Share-Link 404 gab

Der Link
`https://huggingface.co/organizations/mcp-course/share/BcsYJAxCofWDZncivkBzafSjAcuAxOMWua`
ist **kein Kurslink**, sondern eine Einladung in die Hugging-Face-Organisation `mcp-course`.
Er leitet per HTTP 302 auf `/login?next=…` um; ohne angemeldeten Account endet das im Fehlerbild.

Der Kursinhalt selbst ist offen und liegt an zwei Stellen:

- gerendert: <https://huggingface.co/learn/mcp-course/unit0/introduction>
- Quelltext: <https://github.com/huggingface/mcp-course> ← davon ist diese Kopie gezogen

Die Org-Einladung bleibt trotzdem relevant, wenn du Zertifikat oder Quiz-Tracking willst — beides
läuft nur eingeloggt auf dem Hub, nicht offline.

## Struktur

| Pfad | Inhalt |
|---|---|
| `INHALT.md` | Inhaltsverzeichnis in offizieller Lesereihenfolge, verlinkt auf die Einzelseiten |
| `mcp-course-komplett.md` | alle 36 Seiten in einem Dokument, zum Durchlesen und Volltextsuchen |
| `units/` | Kursseiten als MDX, Originaldateien und -namen (Unit 0 bis 3.1) |
| `units/_toctree.yml` | offizielles Inhaltsverzeichnis, Grundlage der beiden Dateien oben |
| `projects/` | lauffähiger Beispielcode zu Unit 3 (`starter/` und `solution/`, Python + `pyproject.toml`) |
| `bilder/` | 26 gespiegelte Abbildungen, plus `quellen.tsv` mit Zuordnung lokal ↔ Original-URL |
| `README-upstream.md` | Original-README des Kurs-Repos |
| `LICENSE` | Apache-2.0 |

Die Bild-URLs in den MDX-Dateien wurden auf die lokalen Kopien in `bilder/` umgeschrieben.
Das ist die einzige inhaltliche Änderung gegenüber dem Original; `bilder/quellen.tsv` hält
jede Ersetzung nachvollziehbar.

## Einstieg

1. `INHALT.md` öffnen und der Reihenfolge folgen, oder
2. `mcp-course-komplett.md` am Stück lesen.

Praktischer Teil: `projects/unit3/build-mcp-server/starter/` ist der Startpunkt,
`…/solution/` die Musterlösung.

## Lücken und Vorbehalte

- **Zertifikat und Quiz-Auswertung funktionieren offline nicht.** Die Seiten `unit1/certificate.mdx`
  und `unit3/certificate.mdx` beschreiben nur den Weg; die Prüfung selbst läuft auf dem Hub.
- **Quizfragen sind lesbar, aber nicht interaktiv.** Im MDX steht das `<Question …>`-Element im
  Rohtext — inklusive `correct: true` und Erklärungen. Zum Selbsttest also vorher nicht mitlesen.
- **Unit 4 existiert nicht.** Die Live-Seite `learn/mcp-course/unit4/introduction` liefert
  „Coming Soon". Der Kurs endet inhaltlich mit Unit 3.1.
- **Ein Bild fehlt**, weil es schon an der Quelle tot ist (HTTP 404): die Playwright-Abbildung in
  `units/unit2/continue-client.mdx`. Die Original-URL steht dort unverändert.
- **Die vietnamesische Übersetzung** (`units/vi/` im Original-Repo) wurde nicht mitkopiert.
- Kurse veralten. Der Stand ist der Commit im Frontmatter, nicht „heute".
- **Größe: 31 MB**, davon 28 MB Bilder — allein 20 MB entfallen auf eine Bildschirmaufzeichnung
  (`bilder/raw.githubusercontent.com_…_recording.gif`, eingebunden in `units/unit2/lemonade-server.mdx`)
  und 2,6 MB auf ein weiteres GIF in `units/unit2/continue-client.mdx`. Wenn das Repository schlank
  bleiben soll: die beiden Dateien löschen und im MDX die Original-URL aus `bilder/quellen.tsv`
  wieder einsetzen. Der Text bleibt davon unberührt.

## Aktualisieren

```bash
curl -sSL -o /tmp/mcp-course.tar.gz \
  https://codeload.github.com/huggingface/mcp-course/tar.gz/refs/heads/main
```

Danach entpacken, `units/en/` und `projects/` ersetzen, Bilder erneut spiegeln und
`INHALT.md` / `mcp-course-komplett.md` neu erzeugen. Der Ablauf ist in der Sitzung vom
2026-09-09 dokumentiert.
