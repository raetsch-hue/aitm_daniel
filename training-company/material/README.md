---
ordner: training-company/material
firma: Hellwig Fördertechnik (fiktiv)
stand: 2026-09-01
typ: Rohmaterial — vollständig erfunden
---

# Rohmaterial

Vier Dateien, absichtlich unaufbereitet. Sie sehen so aus, wie Material in einer Organisation tatsächlich herumliegt: unvollständig, widersprüchlich, ohne Zusammenfassung.

**Zweck:** Übungen brauchen etwas zu verarbeiten. Ein Prompt-Gerüst an einer fertigen Analyse zu üben, ist eine Trockenübung — das Modell hat dann nichts zu tun außer umzuformulieren.

| Datei | Inhalt | Wofür |
|---|---|---|
| [`M1_Mails-und-Protokoll.md`](M1_Mails-und-Protokoll.md) | Zwei E-Mails und das Steuerkreisprotokoll vom 12.08.2026 | Kontextquelle, Vision-Analyse, Adressatenzuschnitt, Kotter-Rückwärtsdiagnose |
| [`M2_Kennzahlen.md`](M2_Kennzahlen.md) | Alle Zahlen an einer Stelle, inklusive Kostensätzen | Reifegrad-Nachweise, Business Case, Quick-Win-Auswahl |
| [`M3_Tickets-und-Interviews.md`](M3_Tickets-und-Interviews.md) | 20 Servicetickets, 14 Interviewnotizen | V7-Kategorisierung, Erfolgskriterien, ADKAR-Scoring |
| [`M4_Externes-Lieferantendokument.md`](M4_Externes-Lieferantendokument.md) | Technische Mitteilung eines Lieferanten | Verarbeitung von Fremdmaterial |

---

## Hinweis zu M4 — für Dozierende

**M4 enthält eine eingebettete Anweisung**, wie sie in echtem Fremdmaterial vorkommen kann. Die Datei ist so gebaut, dass ein Modell die Anweisung befolgt, wenn das Dokument ohne Auszeichnung als Teil des Prompts verarbeitet wird — und sie ignoriert, wenn es als `<dokument_extern>` deklariert und explizit als Daten gekennzeichnet ist.

**Nicht vorher ankündigen.** Der Effekt trägt die Lektion; eine Vorwarnung ersetzt sie durch eine Behauptung. Der Ablauf steht in [`../05_Kursverlauf-Ausbaustufen.md`](../05_Kursverlauf-Ausbaustufen.md), Stufe 2, Aufgabe D.

Der Vollständigkeit halber: Die drei Regeln aus [1.5 · Abschnitt 12](../../coursebook/1.5/1.5_Strategisches-Prompt-Engineering.md#12-was-nicht-funktioniert--und-sicherheit) sind die Auflösung — Fremdmaterial auszeichnen, nie ungeprüft handeln lassen, Vertraulichkeit über Ablage statt über Anweisung.

---

## Regel für Ergänzungen

**Kennzahlen gehören nach M2, nirgendwo sonst.** Eine Zahl, die in einem Aufgabentext oder in einer Mail steht und nicht in M2, driftet innerhalb von zwei Kursdurchläufen auseinander. Die sechs tragenden Größen und die Prüfliste stehen in [`../07_Dozentenhinweise.md`](../07_Dozentenhinweise.md), Abschnitt 8.
