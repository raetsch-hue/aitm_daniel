# Datenqualitätsbericht — `kundendatenbank.csv`

1040 Datensätze, 15 Spalten, Trennzeichen `;`, Kodierung utf-8-sig, Stichtag 2026-09-08, Altersschwelle 730 Tage.

## Vollständigkeit

| Code | Prüfung | Treffer | Betroffene Zeilen |
|---|---|---:|---:|
| V1 | Fehlende Werte je Spalte | 233 | 231 |
| V2 | Platzhalter statt Inhalt | 0 | 0 |
| V3 | Zeilen mit mehreren Lücken | 0 | 0 |
| V4 | Lücken in der laufenden Nummerierung (`kunde_id`) | 18 | 0 |

**[V1] Fehlende Werte je Spalte** — leere Zellen, spaltenweise gezählt

- Spalte `verrechnungssatz_std`: 222 leer (21,3 %), z. B. KD-0006 (Z7), KD-0009 (Z10), KD-0010 (Z11)
- Spalte `ansprechpartner`: 6 leer (0,6 %), z. B. KD-0060 (Z61), KD-0440 (Z441), KD-0531 (Z532)
- Spalte `email`: 5 leer (0,5 %), z. B. KD-0025 (Z26), KD-0163 (Z164), KD-0272 (Z273)

**[V4] Lücken in der laufenden Nummerierung (`kunde_id`)** — erwartet 1058 Datensätze zwischen der kleinsten und der größten Nummer, vorhanden 1040

- KD-0834 bis KD-0851 fehlen (18 Nummern)

## Konsistenz

| Code | Prüfung | Treffer | Betroffene Zeilen |
|---|---|---:|---:|
| K1 | Exakte Dubletten | 0 | 0 |
| K2 | Unscharfe Dubletten | 6 | 6 |
| K3 | Schreibvarianten desselben Werts | 2 | 2 |
| K4 | Schreibvarianten in Freitextfeldern | 33 | 33 |
| K5 | Gemischte Schreibweisen bei Datum und Zahl | 3 | 3 |
| K6 | Mehrfach vergebene Nummern (`kunde_id`) | 0 | 0 |
| K7.1 | Fachliche Regel `besetzungen_2025<=anfragen_2025` | 2 | 2 |

**[K2] Unscharfe Dubletten** — derselbe Betrieb oder dieselbe Person zweimal, mit abweichender Schreibweise (Vergleich ohne Groß-/Kleinschreibung, Umlaute, Sonderzeichen und Leerzeichen, Rechtsform bleibt erhalten; zusätzlich Ähnlichkeit ab 95 Prozent bei gleicher Rechtsform). Gezählt wird nur, wenn mindestens zwei weitere unterscheidungskräftige Felder übereinstimmen — Spalten mit wenigen Ausprägungen zählen dabei nicht

- KD-0212 (Z213): „Zimmermann Offsetdruck GmbH & Co. KG“ ↔ KD-0631 (Z632): „Zimmermann Offsetdruck GmbH & Co KG“
- KD-0277 (Z278): „Elektrotechnik Beck eK“ ↔ KD-0301 (Z302): „Elektrotechnik Beck e.K.“
- KD-0318 (Z319): „Jenaer Umschlaglager GmbH & Co KG“ ↔ KD-1001 (Z984): „Jenaer Umschlaglager GmbH & Co. KG“
- KD-0423 (Z424): „Bad Langensalzaer Backwaren GmbH“ ↔ KD-1046 (Z1029): „Bad Langensalzaer Backwaren GmbH.“
- KD-0436 (Z437): „Becker Schaltanlagen GmbH & Co. KG“ ↔ KD-0493 (Z494): „Becker Schaltanlagen GmbH & Co KG“

**[K3] Schreibvarianten desselben Werts** — kategoriale Spalten: Werte, die nach Faltung zusammenfallen (Groß-/Kleinschreibung, Umlaute, Satzzeichen, Leerzeichen)

- Spalte `betreuer`: Einzelwert „MARX“ ähnelt einem häufigen Wert — z. B. KD-0108 (Z109)
- Spalte `betreuer`: Einzelwert „HILLE“ ähnelt einem häufigen Wert — z. B. KD-0141 (Z142)

**[K4] Schreibvarianten in Freitextfeldern** — Freitext an Trennzeichen zerlegt; seltene Bausteine, die einem häufigen Baustein ähneln (Ähnlichkeit ab 82 Prozent)

- Spalte `email`: „info@elektromontage.de“ (2x) neben „office@elektromontage.de“ (6x) — z. B. KD-0084 (Z85), KD-0170 (Z171)
- Spalte `email`: „hr@verpackungswer.de“ (2x) neben „info@verpackungswer.de“ (5x) — z. B. KD-0130 (Z131), KD-0554 (Z555)
- Spalte `email`: „hr@logistikzentru.de“ (2x) neben „info@logistikzentru.de“ (7x) — z. B. KD-0234 (Z235), KD-0251 (Z252)
- Spalte `email`: „info@anlagenbau.de“ (2x) neben „hr@anlagenbau.de“ (8x) — z. B. KD-0267 (Z268), KD-0680 (Z681)
- Spalte `email`: „personal@berger.de“ (1x) neben „personal@thueringer.de“ (5x) — z. B. KD-0308 (Z309)

**[K5] Gemischte Schreibweisen bei Datum und Zahl** — je Spalte das häufigste Format als Leitformat, alles andere als Abweichung

- Spalte `verrechnungssatz_std`: Komma und Punkt als Dezimaltrennzeichen gemischt (815 zu 3) — z. B. KD-0283 (Z284) = 32.88; KD-0446 (Z447) = 26.35

**[K7.1] Fachliche Regel `besetzungen_2025<=anfragen_2025`** — vorgegebene Regel, zeilenweise geprüft

- KD-0295 (Z296): besetzungen_2025 = 8, anfragen_2025 = 7
- KD-0380 (Z381): besetzungen_2025 = 15, anfragen_2025 = 13

## Aktualität

| Code | Prüfung | Treffer | Betroffene Zeilen |
|---|---|---:|---:|
| A1 | Datumsfelder älter als die Schwelle | 399 | 399 |
| A2 | Datum in der Zukunft | 2 | 2 |
| A3 | Abgelaufene Fristen | 0 | 0 |
| A4 | Zeitliche Lücken in der Reihe | 18 | 0 |

**[A1] Datumsfelder älter als die Schwelle** — Ereignis- und Kontaktdaten (`letzte_anfrage`) vor dem 2024-09-08, also älter als 730 Tage bezogen auf den Stichtag 2026-09-08

- Spalte `letzte_anfrage`: 399 Werte vor 2024-09-08 (38,4 %), ältester 2019-04-09 bei KD-0447 (Z448)

**[A2] Datum in der Zukunft** — Ereignisfelder (kein Fristfeld) mit einem Datum nach dem Stichtag

- KD-0175 (Z176): `letzte_anfrage` = 2027-08-14 liegt nach dem Stichtag
- KD-0768 (Z769): `letzte_anfrage` = 2027-07-15 liegt nach dem Stichtag

**[A4] Zeitliche Lücken in der Reihe** — Monate ohne Eintrag innerhalb des dicht belegten Zeitraums (ältestes Zwanzigstel abgeschnitten) und Abstände von mindestens 14 Tagen zwischen zwei aufeinanderfolgenden Einträgen

- Spalte `letzte_anfrage`: 13 Monate ohne Eintrag mitten in der Reihe (04/2025, 08/2025, 09/2025, 10/2025, 10/2026, 11/2026)
- Spalte `letzte_anfrage`: 25 Tage ohne Eintrag zwischen 2020-05-21 und 2020-06-15
- Spalte `letzte_anfrage`: 14 Tage ohne Eintrag zwischen 2020-10-02 und 2020-10-16
- Spalte `letzte_anfrage`: 14 Tage ohne Eintrag zwischen 2020-10-16 und 2020-10-30
- Spalte `letzte_anfrage`: 19 Tage ohne Eintrag zwischen 2021-03-26 und 2021-04-14
- Spalte `letzte_anfrage`: 15 Tage ohne Eintrag zwischen 2021-07-29 und 2021-08-13

## Genauigkeit

| Code | Prüfung | Treffer | Betroffene Zeilen |
|---|---|---:|---:|
| G1 | Zahlen außerhalb des plausiblen Bereichs | 2 | 2 |
| G2 | Postleitzahlen mit falscher Länge | 3 | 3 |
| G3 | Unbrauchbare E-Mail-Adressen | 0 | 0 |
| G4 | Telefonnummern mit zu wenigen Ziffern | 0 | 0 |
| G5 | Unplausible Datumswerte | 0 | 0 |
| G6 | Zeichensatzschäden | 2 | 2 |
| G7 | Überzählige Leerzeichen | 0 | 0 |

**[G1] Zahlen außerhalb des plausiblen Bereichs** — Grenzen aus den Daten selbst: bei Messgrößen unteres und oberes Quartil ± dreifacher Quartilsabstand, bei Zählgrößen das Dreifache des 99er-Perzentils

- Spalte `verrechnungssatz_std`: 2 Werte außerhalb [14.55; 44.20] — z. B. KD-0336 (Z337) = 2,95; KD-0808 (Z809) = 2,95

**[G2] Postleitzahlen mit falscher Länge** — fünf Ziffern erwartet; vier Ziffern deuten auf eine verlorene führende Null

- KD-0138 (Z139): `plz` = „6484“ ist keine fünfstellige Postleitzahl
- KD-0456 (Z457): `plz` = „7318“ ist keine fünfstellige Postleitzahl
- KD-0782 (Z783): `plz` = „6449“ ist keine fünfstellige Postleitzahl

**[G6] Zeichensatzschäden** — Zeichenfolgen wie Ã¼ oder â€ — ein Umlaut, der einmal falsch kodiert gespeichert wurde

- KD-0110 (Z111): `firmenname` = „FlÃ¤ischwerk Apolda e.K.“
- KD-0712 (Z713): `firmenname` = „Ludwig PrÃ¤zisionsteile GmbH“

## Zusammenfassung

Datensätze mit mindestens einem Befund: **598 von 1040 = 57,50 Prozent**.

Ein Befund ist noch kein Fehler: V1 und A1 treffen auch Zeilen, in denen das Fehlen fachlich richtig ist. Der Bericht zählt, die Bewertung bleibt fachlich.
