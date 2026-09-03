# Ereignisse: GeAT mbH

Was sich im Kursverlauf am Unternehmen geändert hat. Eine Zeile je Änderung, mit der Woche und der betroffenen Datei. Änderungen werden hier festgehalten, nicht still in den anderen Dateien überschrieben — das hält das Profil über elf Wochen widerspruchsfrei.

| Woche | Was sich geändert hat | Warum | Betroffene Datei |
|---|---|---|---|
| 2.3 | Profil angelegt: sechs Profildateien plus Recherche, für GeAT mbH als `typ: real` | Start. Wechsel vom Musterprofil (Mustermann Antriebstechnik) auf den eigenen Fall | alle |
| 2.3 | Recherche durchgeführt: Firma, Sitz, Gründung, Leistungen, Beschäftigte 2018 und 2021, Zertifikate, Aufsicht und sieben Branchenbenchmarks als `öffentlich` belegt | Stufe 1 des Feldkatalogs | `recherche.md` |
| 2.3 | Umsatz, Ergebnis und alle Prozesskosten als `angenommen` gesetzt, weil zur Ertragslage nichts öffentlich ist | Stufe 2. Der Vorbehalt steht im Kopf von `zahlen.md` | `zahlen.md` |
| 2.3 | Reifegradbewertung mit prüfbarem Nachweis je Dimension angelegt, Wellen-Diagnose ergänzt — übernommen aus der Bauweise der Trainingsfirma in `training-company/` | Nachweise statt Adjektive. „Daten: 2" ist eine Behauptung, „63 Prozent der Profile ohne strukturierte Qualifikationsfelder" ein Argument | `profil.md` |
| 2.3 | EU AI Act als **voraussichtlich Hochrisiko** eingeordnet (Annex III Nr. 4), mit Prüfung der Ausnahme nach Art. 6 Abs. 3 | Bewerberauswahl ist in Annex III genannt; entscheidend bleibt, ob das System die Auswahl materiell beeinflusst. Unterscheidet diesen Fall vom Musterprofil und von der Trainingsfirma | `profil.md`, `vorhaben.md` |
| 2.3 | Pilotkennzahl von Besetzungsdauer auf **gesendete Profile je Besetzung** geändert | Von 11 Tagen Besetzungsdauer sind 0,4 Tage Arbeit. Die Profilzahl ist die einzige Größe, auf die der Assistent direkt wirkt | `vorhaben.md`, `zahlen.md` |
| 2.4 | Drei Persona-Gespräche zum KI-Kern (Stufen 1, 3, 4) geführt und ausgewertet: grundsätzliche Ablehnung (Rehberg), Zögern (neue Figur aus der Disposition), berechtigter Einwand (Marnitz) | Methode Woche 12 gegen das Profil laufen lassen. Ergebnis: elf Nachbesserungen am Transformationsvorschlag, darunter drei Fehler im eigenen Papier — Reihenfolge 3c vor 3b, Pilotstart zwei Monate vor Fertigstellung der Gültigkeitsfelder, und der nicht belegte AÜG-Satz | `Gespraeche/` (neu), Nachbesserungen offen in `transformationsvorschlag.md` |
| 2.4 | **Rolle 15 eingeführt: AI and Digital Transformation Manager**, Stelle im Mai 2026 neu geschaffen, bei der Geschäftsführung angesiedelt, Macht 2, Interesse 5, kein Gremium und kein eigenes Budget. **Erste und einzige reale Person im Profil** (der Fallbearbeiter selbst) | Die Gespräche haben gezeigt, dass der „Ich" des Vorhabens ohne Verankerung nicht führbar ist: Mandat, Dienstjahre und fehlendes Gremium tragen in allen drei Gesprächen mit. Bis dahin war die Rolle unbemerkt erzeugt und nicht gekennzeichnet | `menschen.md` (Kopf, Gremien, Rolle 15, Segmente), `profil.md` (Frontmatter, Leseanweisung) |
| 2.4 | Nachweis für Reifegrad **Strategie** ausgetauscht: „Keine Rolle für Digitalisierung oder KI im Organigramm" → „Rolle existiert seit vier Monaten, ohne Budgetposten, ohne Gremium, ohne Weisungsrecht". Nachweis **People** entsprechend präzisiert | Der alte Nachweis war mit Rolle 15 nicht mehr wahr. **Die Stufe bleibt bei 2** — eine Stelle ohne Budget und Gremium ist kein Beleg für „definiert" | `profil.md`, Reifegrad |
| 2.4 | Zahlen nachgezogen: Stammpersonal 68 → **69**, Personalaufwand Stammpersonal 4,6 → **4,695 Mio**, EBIT 0,9 → **0,805 Mio**, EBIT-Marge 2,9 → **2,6 Prozent**, Mitarbeitende 708 → **709** | Die Stelle ist als zusätzlicher Kopf gesetzt, nicht als Umwidmung. 95.000 Euro Vollkosten (`generiert`) | `zahlen.md`, `profil.md`, `menschen.md` (Rolle 10) |
| 2.4 | **Offener Punkt notiert, nicht entschieden:** der Investitionsspielraum von 900.000 Euro ist aus EBIT 0,9 Mio abgeleitet. Bei 0,805 Mio trägt dieselbe Ableitung nur 805.000, es blieben 185.000 statt 280.000 — und die Stufen 1 bis 5 kosten 240.000 | Bewusst nicht still nachgerechnet: der Wert trägt die gesamte Taktung des Transformationsvorschlags. Eine Korrektur würde eine Stufe streichen, das ist eine Entscheidung für Woche 6 und keine Rechenkorrektur | `zahlen.md` (Hinweis eingefügt), `transformationsvorschlag.md` (betroffen, unverändert) |

## Zu erwartende Ereignisse

Nicht eingetreten, nur absehbar. Beim Eintreten in die Tabelle oben verschieben, nicht hier abhaken.

| Voraussichtlich | Was | Warum es das Profil verändert |
|---|---|---|
| Woche 3 bis 5 | Branchensoftware identifiziert (offene Frage 3 aus `recherche.md`) | Entscheidet über Schnittstellenfähigkeit und damit über zwei Drittel des Pilotaufwands. `systeme-daten.md` wird an mehreren Stellen von `angenommen` auf `öffentlich` wechseln |
| Woche 5 | Stellungnahme des Datenschutzbeauftragten zur Hochrisiko-Einordnung | Kann den Zuschnitt des Piloten ändern, nicht nur seine Dokumentation |
| Woche 6 | Business Case gerechnet; die `generiert`-Kostenwerte müssen bestätigt oder gestrichen werden | Siehe [`generierte-werte.md`](generierte-werte.md) |
| Woche 6 oder 7 | **Investitionsspielraum entscheiden.** 900.000 halten und begründen, oder auf rund 805.000 korrigieren und eine Stufe des Transformationsvorschlags streichen | Die härteste Folge der Rolle 15. Ändert `zahlen.md` und die Taktung in `transformationsvorschlag.md` |
| Woche 11 | Entscheidung zur Reihenfolge Datenstrukturierung / Softwaremigration | Programmthema, keine technische Frage. Ändert `vorhaben.md`, parallele Initiativen |
