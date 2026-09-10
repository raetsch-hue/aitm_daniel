---
ordner: GeAT-unternehmensprofil
firma: GeAT – Gesellschaft für Arbeitnehmerüberlassung Thüringen mbH, Erfurt
typ: real (Hülle belegt, Kern konstruiert)
stand: 2026-09-10
verwendung: Übungsfall für alle Methoden bis Kurswoche 12
---

# Unternehmensprofil GeAT mbH

Der durchgehende Fall für alle Methoden des Kurses bis Woche 12: Change Management, Stakeholder-Analyse, Plattformwahl, Governance, Business Case, Datenstrategie, Skalierung, Programm-Management. Gebaut nach dem Feldkatalog `unternehmensprofil.md` aus dem geteilten Kursprojekt „Werkbank: Unternehmensprofile".

## Der Hinweis, der vor allem anderen kommt

> **GeAT existiert.** Firma, Sitz, Gründungsjahr, Leistungen, Zertifikate und die Aufsichtsbehörde sind belegt und stehen mit Quelle und Abrufdatum in [`recherche.md`](recherche.md).
>
> **Alles andere ist konstruiert.** Umsatz, Ergebnis, Prozesskosten, Datenqualität, Systemlandschaft, Vorgeschichte, Kultur — dazu ist nichts öffentlich, und ein Modell erfindet es überzeugend. Jeder Wert trägt deshalb ein Kennzeichen: `öffentlich`, `angenommen` oder `generiert`.
>
> **Alle Personen sind erfunden — außer einer.** Die Geschäftsführung der GeAT ist im Impressum und im Handelsregister öffentlich benannt. Dieser Name kommt in diesem Profil nicht vor, und das ist Absicht. **Die Ausnahme ist Rolle 15 in `menschen.md`:** der AI and Digital Transformation Manager ist der Fallbearbeiter selbst und trägt Herkunft `real`. Die Stelle ist im Fall im Mai 2026 neu geschaffen; ihre Haltung und ihr Nachtgedanke sind ein Vorschlag und vom Fallbearbeiter zu bestätigen.
>
> **Nichts aus diesem Ordner gehört in ein Artefakt über eine reale Organisation.** Weder eine Zahl noch ein Zitat noch eine Einschätzung.

## Warum GeAT

Der Kernprozess des Unternehmens **ist** der KI-Fall. Bei einem Maschinenbauer hängt man KI an einen Prozess an; bei einem Personaldienstleister ist die Auswahl von Menschen für Stellen das Geschäft selbst. Daraus folgen drei Dinge, die kein anderer Fall in dieser Schärfe liefert:

1. **EU AI Act Annex III, Nummer 4 — voraussichtlich Hochrisiko.** Filterung und Bewertung von Bewerbungen sind ausdrücklich gelistet. Art. 6 Abs. 3 enthält eng begrenzte Ausnahmen für Systeme ohne erheblichen Einfluss auf die Entscheidung; ein menschlicher Klick allein genügt dafür nicht. Gerade diese Abgrenzung macht den Fall didaktisch wertvoll.
2. **Bias mit Zahlen statt mit Beispielen.** 28,8 Prozent der Zeitarbeitnehmer in Deutschland haben keinen Berufsabschluss, 20,4 Prozent waren zuvor langzeitarbeitslos oder noch nie beschäftigt, und Zeitarbeit trägt 10,8 Prozent der Übergänge aus Langzeitarbeitslosigkeit in Beschäftigung — alles belegt (GVP 2025). Ein auf Erfolgswahrscheinlichkeit trainiertes Modell sortiert genau diese Gruppen zuerst aus. Das ist keine Übungsaufgabe, das ist eine Rechnung.
3. **Die Aufsichtsbehörde ist die Bundesagentur für Arbeit** (belegt, Impressum). Sie erteilt die Erlaubnis, von der das Geschäftsmodell abhängt, und ist im Vermittlungsmarkt selbst Akteur. Für einen Digital Transformation Manager in der öffentlichen Arbeitsverwaltung ist das der Fall von der anderen Seite des Tisches.

Dazu passt der Reifegrad: Die Branche liegt bei 46 Prozent regelmäßiger KI-Nutzung (Lünendonk 2025, belegt). Ein Personaldienstleister mit Daten auf Stufe 2 ist deshalb glaubwürdig — anders als eine E-Commerce-Firma, bei der ein niedriger Reifegrad die ganze Engpass-Pointe zerstören würde.

## Die Dateien

| Datei | Enthält | Braucht ab |
|---|---|---|
| [`recherche.md`](recherche.md) | Was öffentlich belegbar ist, mit Quelle und Abrufdatum. Branchenbenchmarks. Offene Fragen | immer |
| [`profil.md`](profil.md) | Identität, Geschäftsmodell, fünf Kernprozesse, Reifegrad mit prüfbarem Nachweis, Wellen-Diagnose, drei brennende Probleme, Vorgeschichte, Marktumfeld, Regulatorik, Reibungsliste | W1, W3, W5 |
| [`zahlen.md`](zahlen.md) | GuV-Skelett, Rohertrag je Überlassungsstunde, Personalkosten je Bereich, IT-Budget, Pilotprozess mit Zerlegung der Durchlaufzeit, Investitionsspielraum, Rechenproben | W6, W7 |
| [`menschen.md`](menschen.md) | Sechs Gremien, 15 Rollen mit Macht, Interesse, Haltung und Zitat (Rolle 15 ist der Fallbearbeiter, `real`), sechs Segmente, fünf Kulturmerkmale mit Beleg | W2, W4, W12 |
| [`systeme-daten.md`](systeme-daten.md) | Systemlandschaft, Datenbestände mit Qualitätsbefund, Wissensquellen, Schatten-IT, Auftragsverarbeiter | W3, W5, W8 |
| [`datenverantwortung.md`](datenverantwortung.md) | Wer für welchen Datenbestand accountable ist (formal: niemand), kritische Befunde priorisiert, Data-Owner-Vorschlag, Sofortmaßnahmen ohne Beschluss | W3, W5, W8 |
| [`vorhaben.md`](vorhaben.md) | Der Pilot, Workflows heute und im Ziel, Risikoeinschätzung nach EU AI Act, parallele Initiativen, Eskalationsweg | W2, W6, W9, W11 |
| [`ereignisse.md`](ereignisse.md) | Was sich im Kursverlauf geändert hat, je Zeile eine Woche | laufend |
| [`w03A-4-use-case-und-sensitivitaet.md`](w03A-4-use-case-und-sensitivitaet.md) | **Kette W03 A, Glied 4.** Prüfung der Plattformentscheidung: Use Case aus dem Datenbestand, Score nachgerechnet, Sensitivität über 30 Varianten plus Kippschwellen. Ändert kein Gewicht | W3, W6 |
| [`w03A-5-entscheidungsvorlage.md`](w03A-5-entscheidungsvorlage.md) | **Kette W03 A, Glied 5.** Handlungsempfehlung für die Geschäftsführung, zwei Seiten: Empfehlung mit Maßstab, vier entkräftete Gegenargumente, die ersten 90 Tage mit Beleg, fünf offene Fragen, Beschlussvorschlag | W3, W6 |
| [`w03A-6-pitch-c-level.md`](w03A-6-pitch-c-level.md) | **Kette W03 A, Glied 6. ✔ GELTENDE FASSUNG (2).** Sprechfassung für das C-Level: BLUF vorn, 7 Minuten Kern. Offene Punkte als drei Gates plus Zweitbeschluss. Mit Zeitkontrolle und Notfallkürzung | W3 |
| [`w03B-1-agent-konzept-bestandswaechter.md`](w03B-1-agent-konzept-bestandswaechter.md) | **Kette W03 B, Glied 1.** Agent-Konzept auf den bereinigten Beständen: was empfohlen wird, was nicht, und warum kein Assistent für alle 69 | W3, W8, W10 |
| [`w03A-1-ki-analyse-fassung-1.md`](w03A-1-ki-analyse-fassung-1.md) | **Kette W03 A, Glied 1. ⚠ ÜBERHOLT.** Erstfassung der Plattform- und Werkzeugwahl. Nur noch für den Fassungsvergleich lesen | — |
| [`w03A-2-ki-analyse-review.md`](w03A-2-ki-analyse-review.md) | **Kette W03 A, Glied 2.** Review der Erstfassung: sachliche Fehler, methodische Schwächen, budgetäre Widersprüche | W3 |
| [`w03A-6-pitch-c-level-fassung-1.md`](w03A-6-pitch-c-level-fassung-1.md) | **Kette W03 A, Glied 6, Fassung 1. ⚠ ÜBERHOLT.** Erstfassung des Pitch, vier Abschnitte, 7–10 Minuten. Inhaltlich unverändert gültig, aber nicht auf ein sofortiges Go gebaut. Nur noch für den Fassungsvergleich lesen | — |
| [`w03A-6-pitch-c-level-review.md`](w03A-6-pitch-c-level-review.md) | **Kette W03 A, Glied 6, Zwischenglied.** Review des Pitch auf ein sofortiges Go: BLUF, Kürzung von Abschnitt 2, offene Punkte als Gates. Mit Gegenprüfung — vier Vorschläge wurden abgewandelt statt übernommen | W3 |
| [`w03A-3-ki-analyse-fassung-2-gueltig.md`](w03A-3-ki-analyse-fassung-2-gueltig.md) | **Kette W03 A, Glied 3. ✔ GELTENDE FASSUNG.** Gewichtung K1–K8 und L0–L6, sechs Optionen. **Hieraus zitieren, nicht aus Glied 1** | W3, W6, W7 |
| [`w03B-2-agent-neubewertung-nach-bereinigung.md`](w03B-2-agent-neubewertung-nach-bereinigung.md) | **Kette W03 B, Glied 2.** Messung der sechs Agentenregeln gegen die bereinigten Bestände: fünf finden null. Empfiehlt einen Fristenwächter statt des Bestandswächters | W3, W8 |
| [`w03C-1-plattformkriterien-kennzahlen-stakeholder.md`](w03C-1-plattformkriterien-kennzahlen-stakeholder.md) | **Kette W03 C, Glied 1.** Die sechs Plattformkriterien für das Kursboard: je Kriterium Kennzahlen, Stakeholder-Anforderungen und Belege. Konsolidiert die vier verstreuten Kennzahlen-Tabellen und weist fünf Widersprüche aus | W3, W6 |
| [`w03C-2-dsgvo-ai-act-auszug.md`](w03C-2-dsgvo-ai-act-auszug.md) | **Kette W03 C, Glied 2.** Auszug aus Glied 1, Kriterium 1 allein vortragbar: AI-Act-Einordnung, Anbieter-Betreiber-Unterscheidung, Bias-Rechnung. Kein eigenständiges Ergebnis | W3, W5 |
| [`w03C-3-reifegradstufe-building-pilots.md`](w03C-3-reifegradstufe-building-pilots.md) | **Kette W03 C, Glied 3.** Reifegradstufe für das zweite Kursboard: warum Stufe 2 nachgeholt und nicht erreicht wird, die vier Eintrittskarten aus Glied 2, und warum GeAT in keine Zeitkategorie des MIT-Modells fällt | W3, W6 |
| [`raci-datenpflege.md`](raci-datenpflege.md) | RACI-Matrix für fünf Datenpflege-Aufgaben, je Zeile genau ein Accountable, plus die Rolle, die dafür fehlt | W3, W5, W8 |
| [`daten/`](daten/) | Zwei generierte Übungsdatensätze als CSV (Bewerber, Kunden) mit eingebauten Datenqualitätsproblemen, dazu Datenblatt, Prüfskript, RAG-Erläuterung und separates Lösungsblatt | W3, W5, W8 |
| [`generierte-werte.md`](generierte-werte.md) | Alle 19 `generiert`-Werte, sortiert nach der Woche, die sie zuerst braucht — plus die `angenommen`-Werte, die trotzdem geprüft werden müssen | jeden Freitag |
| `Gespraeche/` | Drei Persona-Gespräche zum KI-Kern mit Auswertung (Typ, Barriere, Berechtigung des Einwands, Prüfweg) und Kennzeichnung des Generierten | W12 |

Zwei Referenzen liegen absichtlich **nicht** in diesem Ordner, weil sie zum Kurs gehören und nicht zum Fall: der **Feldkatalog** (`unternehmensprofil.md`) und das **Musterprofil** der fiktiven Mustermann Antriebstechnik GmbH. Beide stehen im geteilten Projekt „Werkbank: Unternehmensprofile". Der Feldkatalog liegt zusätzlich im Projektwissen dieses Falls, damit ein Modell die Feldstruktur ohne Umweg kennt.

**Nie den ganzen Ordner in einen Prompt geben.** Der Feldkatalog verteilt das Profil auf sechs Dateien, damit ein Modell nur die liest, die es braucht. Für eine Stakeholder-Analyse reichen `profil.md` und `menschen.md`; für den Business Case `zahlen.md` und `vorhaben.md`.

## Dokumentketten

**Hier wird nachgehalten, welches Dokument auf welchem aufbaut.** Ein Ergebnis, das ein anderes
voraussetzt, steht sonst im luftleeren Raum: man liest es, ohne zu wissen, dass seine Zahlen
woanders begründet sind — und ändert es, ohne das Vorgängerdokument mitzuändern.

### Die Regel

| | |
|---|---|
| **Dateiname** | `wNN` Kurswoche · `A/B/C` Kette innerhalb der Woche · `-N-` Position. Alphabetisch sortiert steht damit jede Kette in ihrer Lesereihenfolge |
| **Frontmatter** | jedes Glied trägt `kette:`, `baut_auf:`, `basis_fuer:`. `basis_fuer: offen` heißt: letztes Glied, hier geht es weiter |
| **Überholte Glieder** | bleiben liegen und werden **im Namen und im Frontmatter** als überholt gekennzeichnet. Nicht löschen — der Fassungsvergleich ist der Lernertrag |
| **Änderungen** | wandern ins **früheste** betroffene Glied. Wer ein Auszugsdokument korrigiert, ohne das Elterndokument zu korrigieren, erzeugt zwei Wahrheiten |
| **Auszüge** | tragen oben einen Kennzeichnungskasten: Herkunft, führende Quelle, „keine neuen Zahlen" |
| **Eintragung hier** | jede Kette bekommt eine Zeile unten. Ein Glied ohne Eintrag gilt als vergessen, nicht als eigenständig |

### Kette W03 A · KI-Analyse — die Plattform- und Werkzeugwahl

```
profil · zahlen · systeme-daten · menschen · vorhaben · transformationsvorschlag   (Bestand)
   └─ w03A-1-ki-analyse-fassung-1.md              Erstfassung  ⚠ ÜBERHOLT
        └─ w03A-2-ki-analyse-review.md            Review gegen die Erstfassung
             └─ w03A-3-ki-analyse-fassung-2-gueltig.md   ✔ GELTENDE FASSUNG
                  └─ w03A-4-use-case-und-sensitivitaet.md   Prüfung: Use Case + Sensitivität
                       ├─ w03A-5-entscheidungsvorlage.md      2 Seiten für die Geschäftsführung
                       └─ w03A-6-pitch-c-level-fassung-1.md   Sprechfassung  ⚠ ÜBERHOLT
                            └─ w03A-6-pitch-c-level-review.md      Review: BLUF, Kürzung, Gates
                                 └─ w03A-6-pitch-c-level.md            ✔ GELTENDE FASSUNG (2)
```

**Wer Gewichte oder Scores zitiert, zitiert `w03A-3`.** Glied 4 prüft, ändert aber nichts: es
liefert den Use Case aus dem Datenbestand und die Sensitivitätsprobe, die in `w03A-3` fehlte.
Glieder 5 und 6 sind die Ausgabeformate derselben Prüfung: Vorlage und Pitch.

**Der Pitch hat seit dem 10.09.2026 zwei Fassungen, nach demselben Muster wie Glied 1 bis 3:**
Fassung 1 → Review → geltende Fassung. **Wer den Pitch hält, hält `w03A-6-pitch-c-level.md`.**
Geändert haben sich Reihenfolge und Form, **nicht die Zahlen** — jede Zahl aus Fassung 1 gilt
weiter und ist in `w03A-3` bis `w03A-5` nachgewiesen. `basis_fuer: offen` — das nächste Glied wäre der Business Case in W06.

**Wer Gewichte oder Scores zitiert, zitiert `w03A-3`.** Fassung 2 hat vier Gewichte geändert, MCP
als Kriterium gestrichen, einen Rechenfehler der Erstfassung korrigiert und eine sechste Option
(Option F) ergänzt, die Teil B gewinnt.

### Kette W03 B · Agent auf den bereinigten Beständen

```
w03A-3 (Plattformwahl) · raci-datenpflege · daten/
   └─ w03B-1-agent-konzept-bestandswaechter.md    Konzept: der Bestandswächter
        └─ w03B-2-agent-neubewertung-nach-bereinigung.md   Messung gegen die bereinigten Daten
```

**Glied 1 gilt weiter, seine Begründung nicht.** Auf dem bereinigten Bestand finden fünf der sechs
Regeln null Fälle; Glied 2 empfiehlt stattdessen einen Fristenwächter mit zwei Regeln. Glied 1
trägt dazu einen Nachtrag. `basis_fuer: offen` — das nächste Glied wäre die zweite Prüfmessung.

### Kette W03 C · Plattformkriterien und Reifegrad (Kursboards)

```
w03A-3 (geltende Gewichtung K1–K8)
   └─ w03C-1-plattformkriterien-kennzahlen-stakeholder.md   Board 1: sechs Kriterien
        └─ w03C-2-dsgvo-ai-act-auszug.md                    Auszug: Kriterium 1 allein
             └─ w03C-3-reifegradstufe-building-pilots.md     Board 2: Stufe 2 Building Pilots
```

`basis_fuer: offen` — das nächste Glied wäre der Business Case in W06.

### Kette · Datenqualitätsübung

```
daten/README.md → daten/pruefe_datenqualitaet.py → daten/AUFLOESUNG-datenqualitaet.md
   → daten/KORREKTUR-dokumentation.md → *-korrigiert.csv
```

Abgeschlossen. Beide korrigierten Bestände bestehen 23 von 24 Prüfungen; der Rest ist Prüfung A1
und fachlich richtig.

### Noch ohne Präfix, weil die Kurswoche nicht deklariert ist

Diese vier bilden nachweislich eine Kette — die Reihenfolge steht in ihren eigenen
`bezug:`-Angaben —, tragen aber kein `woche:` im Frontmatter. Ein Präfix wäre hier geraten, nicht
belegt:

```
transformationsvorschlag.md
   ├─ widerstandsmuster.md
   │    └─ board-widerstandsanalyse.md
   └─ storyline-stufe-3-datenfundament.md
        └─ storyline-stufe-3-kurzfassung.md
```

**Offen:** Sobald die Kurswoche für diese vier feststeht, werden sie zu `wNN…` umbenannt und hier
als eigene Kette geführt.

### Bestandsdateien — keine Kettenglieder

`recherche.md` · `profil.md` · `zahlen.md` · `menschen.md` · `systeme-daten.md` · `vorhaben.md` ·
`datenverantwortung.md` · `raci-datenpflege.md` · `ereignisse.md` · `generierte-werte.md`

Sie werden **fortgeschrieben, nicht abgeleitet**, und tragen deshalb kein `kette:`. Wer aus ihnen
ein datiertes Ergebnis zieht, beginnt eine neue Kette — und trägt sie hier ein.

## Die Reibung, die eingebaut ist

Ein Profil ohne Widersprüche liefert bei jeder Methode glatte Ergebnisse. Sechs Pflichtreibungen nach Feldkatalog, plus zwei an unüblicher Stelle:

| Reibung | Wo |
|---|---|
| Zwei Rollen mit unvereinbaren Zielen: Recruiting Center gegen Niederlassungsleitung Gotha | `menschen.md`, Rollen 4 und 5 |
| Gescheiterte Vorgängerinitiative: Bewerbermanagement-Modul 2023, 34 Prozent Nutzung, nie ausgewertet | `profil.md`, Vorgeschichte |
| System ohne Schnittstelle: Multiposting ↔ Bewerbermanagement, jede Anzeige zweimal gepflegt | `systeme-daten.md` |
| Datenbestand mit Mangel: 41.000 Profile, 63 Prozent ohne strukturiertes Können, 18.000 über die Speicherfrist | `systeme-daten.md` |
| Parallele Initiative um dieselben Leute: Migration der Branchensoftware 2027 | `vorhaben.md` |
| Zahl, die wehtut: 280.000 Euro Spielraum, Freigaben über 25.000 nur quartalsweise | `zahlen.md` |
| **Unüblich:** der Engpass der Fakturierung ist der Papier-Stundenzettel, und die Person, die ihn beherrscht, kommt im Vorhaben nicht vor | `menschen.md` Rolle 11, `systeme-daten.md` |
| **Unüblich:** das Anzeigenbudget von 480.000 Euro ist größer als das gesamte IT-Budget — und liegt im Vertrieb | `zahlen.md` |

## Woher die Bauweise kommt

Die Struktur folgt dem Feldkatalog des Kurses. Drei Elemente sind aus der Trainingsfirma in [`../training-company/`](../training-company/) (Hellwig Fördertechnik) übernommen, weil sie dort besser gelöst sind als in der Vorlage:

- **Prüfbarer Nachweis je Reifegradstufe.** Nicht „Daten: 2", sondern der einzelne Befund, den man bestreiten kann.
- **Wellen-Diagnose** als eigener Abschnitt in `profil.md`, mit einem Satz, der die Diagnose zusammenfasst.
- **Die Zerlegung der Durchlaufzeit** in `zahlen.md`. Bei Hellwig stehen 47 Minuten Arbeit gegen 6,5 Tage Durchlauf; bei GeAT 3,4 Stunden gegen 11 Tage. Beide Male ist die Rechnung der Lehrpunkt — mit dem Unterschied, dass bei GeAT genau ein Wartezeitblock durch bessere Vorschläge kürzer wird. Das macht den Fall entscheidbar statt entlarvend.

Was **nicht** übernommen wurde: Hellwigs Didaktikteil (Ausbaustufen, Injects, Dozentenhinweise). Dieses Profil ist ein Übungsfall für eine Person, kein Kursmaterial für einen Raum.

## Nächste Schritte

1. Die vier offenen Fragen aus `recherche.md` abarbeiten, mit Priorität auf der Branchensoftware.
2. Die 19 `generiert`-Werte durchgehen. Wert 4 (Eigentümerstruktur) zuerst — er hängt an Wert im Frontmatter und verändert den Tonfall des ganzen Falls. Wert 18 (Haltung und Nachtgedanke der Rolle 15) kann nur der Fallbearbeiter selbst bestätigen. Wert 19 (95.000 Euro für die neue Stelle) entscheidet über den Investitionsspielraum und damit darüber, ob die Stufen 1 bis 5 des Transformationsvorschlags noch hineinpassen.
3. Stufe 3 des Feldkatalogs: die erste Methode gegen das Profil laufen lassen und die Lücken nachtragen.
