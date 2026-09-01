---
ordner: training-company
firma: Hellwig Fördertechnik (fiktiv)
stand: 2026-09-01
typ: Lehrmaterial — vollständig erfunden
status: nicht als Beleg verwendbar
---

# Trainingsfirma: Hellwig Fördertechnik

**Ein fiktives Unternehmen als roter Faden für den ganzen Kurs.** Alle Modelle aus dem [Coursebook](../coursebook/0/00_Index-und-Gewichtung.md) werden an derselben Firma erklärt, geübt und gebrochen — statt an vier unverbundenen Beispielen.

---

## Warnhinweis, der vor allem anderen kommt

> **Jede Zahl in diesem Ordner ist erfunden.** Umsätze, Reifegrade, Kennzahlen, Personen, Zitate, Vorgeschichte — alles konstruiert, damit es zu den Modellen des Kurses passt.
>
> Diese Zahlen dürfen **nie** in ein Artefakt über die Bundesagentur für Arbeit wandern, nie in eine Entscheidungsvorlage, nie in eine Quellenangabe. `CLAUDE.md` verlangt, Fakten, Annahmen und Einschätzungen getrennt auszuweisen — dieser Ordner ist eine vierte Kategorie: **Lehrfiktion**.
>
> Umgekehrt gilt: Anders als in `kontext/` sind hier **Personen mit Namen** geführt. Das ist zulässig, weil es niemanden gibt. Für echte Stakeholder bleibt die Rollenregel aus `CLAUDE.md` in Kraft.

---

## Warum ausgerechnet diese Firma

Das Coursebook benutzt an vier Stellen einen anonymen Beispielfall, ohne ihn zu benennen:

| Coursebook-Stelle | Was dort steht | Bei Hellwig |
|---|---|---|
| [1.4 · 8.5 Kategorienfehler](../coursebook/1.4/1.4_Vier-Wellen-KI-Kategorien-Hype-Cycle.md) | „mittelständischer Maschinenbauer, rund 500 Mitarbeitende, SAP-ERP, Daten Stufe 2, 2.000 Eingangsrechnungen, 60 Lieferanten" | Stammsitz, 512 Beschäftigte, SAP ECC, Daten Stufe 2 — Vorhaben **V1** |
| [1.5 · 11.1 Prompt C](../coursebook/1.5/1.5_Strategisches-Prompt-Engineering.md) | „Maschinenbau, 500 Mitarbeitende, SAP-ERP … Rechnungsprüfung per RPA, 40 Personentage" | derselbe Fall, dieselben 40 Personentage |
| [2.1 · 9.4 Ability-Fehler](../coursebook/2.1/01_Change-Management-Lewin-ADKAR.md) | „Maschinenbauunternehmen schult 120 Mitarbeitende … Nutzung 8 %" | Prompting-Workshop 04/2026, Messung 06/2026 |
| [2.2 · 8.5 Vision](../coursebook/2.2/2.2_Kotter-8-Schritte-Modell.md) | „Bis Ende 2027 sind unsere Kernprozesse … 25 % Effizienzsteigerung" | wörtlich der Vision-Satz aus dem Steuerkreisprotokoll |

Dazu die [Kollaborationsplattform aus der Ergänzung zu 2.2](../coursebook/2.2/2.2_Ergaenzung-Force-Field-Analyse.md): Hellwig hat sie 2023 eingeführt, und sie ist halb gescheitert — genau mit den dort genannten Kräften.

**Die Firma ist also keine Erfindung neben dem Kurs, sondern die Zusammenfassung seiner eigenen Beispiele in einer Organisation.** Wer die Kursbeispiele kennt, erkennt sie wieder. Wer mit der Firma arbeitet, arbeitet an den Kursbeispielen.

Zur Größenangabe: Die 500er-Zahl des Coursebooks bezieht sich auf die Gesellschaft am Stammsitz (512 Beschäftigte). Die Konzernzahl 1.380 umfasst die Auslandsgesellschaften und wird gebraucht, sobald Reifegradunterschiede zwischen Standorten Thema werden.

---

## Die Dateien

| Datei | Enthält | Ab Kurstag |
|---|---|---|
| [`00_Firmenprofil.md`](00_Firmenprofil.md) | Profil, Zahlen, Systemlandschaft, Historie, Organisation | immer |
| [`01_Reifegrad-und-Wellen.md`](01_Reifegrad-und-Wellen.md) | Sechs Dimensionen IST/ZIEL mit prüfbaren Nachweisen, Wellen-Diagnose, Engpasslesung | 1.4 |
| [`02_Stakeholder.md`](02_Stakeholder.md) | Zwölf Personen mit Interesse, Haltung und Originalzitat | 1.4 |
| [`03_Vorhabenportfolio.md`](03_Vorhabenportfolio.md) | Zehn Vorhaben, teils absichtlich falsch kategorisiert | 1.4 |
| [`04_Change-Lage.md`](04_Change-Lage.md) | ADKAR-Rohmaterial, Kraftfeld-Rohdaten, Kotter-Stand, Vorgeschichte | 2.1 / 2.2 |
| [`05_Kursverlauf-Ausbaustufen.md`](05_Kursverlauf-Ausbaustufen.md) | Was wann freigegeben wird, mit Aufgabe und erwartetem Ergebnis | Planung |
| [`06_Sonderfaelle-und-Injects.md`](06_Sonderfaelle-und-Injects.md) | Dreizehn Störereignisse zum Vertiefen | ab 1.4 |
| [`07_Dozentenhinweise.md`](07_Dozentenhinweise.md) | Lösungen, Fallen, Bewertungsraster — **enthält Spoiler** | Vorbereitung |
| [`material/`](material/) | Rohmaterial: Mails, Protokoll, Kennzahlen, Tickets, Interviews, Fremddokument | ab 1.5 |

### Die Trennung, auf die es ankommt

`00` bis `04` sind **Zustand** — sie beschreiben die Firma, wie sie ist. `05` bis `07` sind **Didaktik** — sie beschreiben, was man damit macht. `material/` ist **Rohmaterial** — unaufbereitet, wie es in einer echten Organisation herumliegt.

Wer die Firma als Kontext in einen Prompt gibt, hängt Dateien aus der ersten Gruppe an. Nie den ganzen Ordner: [Context Rot](../coursebook/1.5/1.5_Strategisches-Prompt-Engineering.md#8-context-rot-warum-mehr-kontext-nicht-besser-ist) gilt hier genauso wie im eigenen Repo. Zwölf Dateien à 400 Wörter sind kein Ordnungsproblem, sondern der Grund, warum das über Wochen funktioniert.

---

## Drei Verwendungsarten

**1. Als Anschauungsmaterial im Vortrag.** „Reifegrad Daten Stufe 2" ist eine Behauptung. „11 % der Ersatzteilpositionen haben keine Gewichtsangabe, deshalb kann kein Frachtpreis automatisch berechnet werden" ist ein Argument. Alle Nachweise in `01` sind so gebaut.

**2. Als Übungsgegenstand.** Die Kraftfelder in `04` sind **unbewertet**, die ADKAR-Scores **nicht gesetzt** — nur Interviewaussagen liegen vor. Die Teilnehmenden bewerten selbst; die Referenzbewertung steht in `07`.

**3. Als Kontext für Prompt-Übungen.** `00` bis `03` haben genau das Format, das [Tag 1.5](../coursebook/1.5/1.5_Strategisches-Prompt-Engineering.md#9-wo-der-inhalt-wohnt-die-ablage-entscheidung) für Kontextdateien fordert: kurz, datiert, jeder Absatz entscheidungsrelevant. Sie sind gleichzeitig Inhalt und Formatbeispiel.

---

## So wächst die Firma mit dem Kurs

Jeder Kurstag legt eine Schicht auf denselben Sachverhalt, statt ein neues Beispiel zu öffnen:

```
Tag 1.4   Wo steht die Firma?          → Reifegrad, Wellen, Kategorien
Tag 1.5   Wie beschreibe ich sie?      → Kontextdateien, GF-Mail, Prompt-Härtung
Tag 2.1   Warum bewegt sich niemand?   → B = f(P, E), ADKAR, erstes Kraftfeld
Tag 2.2   Was ist als Nächstes zu tun? → Kotter-Rückwärtsdiagnose, Vision, Quick Win
Mittwoch  Was hält uns?                → Kraftfeld vollständig, mit Maßnahmenzeile
danach    Was passiert, wenn es läuft?  → Governance, Business Case, Rückfall, Nachfolge
```

Der Nutzen dieser Bauweise zeigt sich erst ab Tag 2.1: Wenn der Widerstand bei einer Person auftritt, die die Teilnehmenden schon aus Tag 1.4 als Befürworterin kennen, ist die Diskussion eine andere. Details in [`05_Kursverlauf-Ausbaustufen.md`](05_Kursverlauf-Ausbaustufen.md).

---

## Erweitern

Kommt ein neuer Kurstag dazu, wird **keine neue Firma erfunden**. Stattdessen:

1. Prüfen, welches der zehn Vorhaben in `03` das neue Thema am besten trägt.
2. Fehlende Fakten in `00` bis `04` **ergänzen, nicht anhängen** — der geltende Stand bleibt kurz, überholte Stände wandern raus.
3. Eine Ausbaustufe in `05` anlegen, mit Aufgabe und erwartetem Ergebnis.
4. Wenn das Thema einen Konflikt braucht: einen Inject in `06` schreiben, nicht eine Person umcharakterisieren.

Die Konsistenzregel: **Eine Zahl steht an genau einer Stelle.** Kennzahlen in `material/M2_Kennzahlen.md`, Bewertungen in `01`, alles andere verweist darauf.
