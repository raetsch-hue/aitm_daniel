---
titel: AUFLÖSUNG — eingebaute Datenqualitätsprobleme in den Übungsdatensätzen
typ: Lösungsblatt
gehoert_zu: bewerberdatenbank.csv, kundendatenbank.csv
datum: 2026-09-08
woche: 03
status: Auflösung — erst nach der eigenen Analyse öffnen
herkunft: vollständig generiert. Kein Wert stammt aus einem realen System
---

# ⚠️ AUFLÖSUNG — vor der Übung nicht lesen

> **Diese Datei ist das Lösungsblatt.** Sie listet jeden eingebauten Fehler, seine Kategorie und die
> betroffenen Datensätze. Wer die Übung selbst machen will, analysiert zuerst
> [`bewerberdatenbank.csv`](bewerberdatenbank.csv) und [`kundendatenbank.csv`](kundendatenbank.csv)
> und vergleicht danach.
>
> **Herkunft.** Beide Datensätze sind vollständig **generiert**. Personen, Firmen, Adressen und Zahlen
> sind erfunden; Übereinstimmungen mit real existierenden Betrieben sind unbeabsichtigt. Die Struktur
> folgt [`systeme-daten.md`](../systeme-daten.md), das Mengengerüst [`zahlen.md`](../zahlen.md).
> Nichts aus diesen Dateien gehört in ein Artefakt über eine reale Organisation.

## Kennzahlen

| Datensatz | Zeilen | Zeilen mit Fehler | Anteil | Vollständigkeit | Konsistenz | Aktualität | Genauigkeit |
|---|---:|---:|---:|---:|---:|---:|---:|
| Bewerberdatenbank | 1.284 | 79 | 6,15 % | 20 | 23 | 16 | 20 |
| Kundendatenbank | 1.040 | 57 | 5,48 % | 15 | 18 | 12 | 12 |

Angegeben sind **Fehlerinstanzen** je Kategorie; eine Zeile trägt höchstens einen Fehler, deshalb liegt
die Summe der Instanzen über der Zahl betroffener Zeilen nur dann, wenn eine Zeile mehrfach markiert
wurde — das kommt hier nicht vor. Beide Werte liegen im vorgegebenen Fenster von 3 bis 8 Prozent, die
Verteilung über die Zeilen ist ungleichmäßig (Ziehung ohne Schichtung, Seed 20260908).

## Teil A · Bewerberdatenbank

**1.284 Zeilen, 79 davon mit mindestens einem eingebauten Fehler = 6,15 Prozent.** Verteilung der Fehlerinstanzen: Vollständigkeit 20, Konsistenz 23, Aktualität 16, Genauigkeit 20.

### Vollständigkeit

| Fehlerart | Zeilen | Betroffene Datensätze | Konkrete Werte |
|---|---:|---|---|
| Geburtsdatum fehlt | 1 | `BW-01126` | `(leer)` |
| E-Mail-Adresse fehlt | 7 | `BW-01130`, `BW-01296`, `BW-01389`, `BW-01602`, `BW-01970`, `BW-02022`, `BW-02148` | `(leer)` |
| Telefonnummer fehlt | 4 | `BW-01216`, `BW-01454`, `BW-01981`, `BW-02299` | `(leer)` |
| Platzhalter statt Qualifikation | 3 | `BW-01341`, `BW-01464`, `BW-01990` | `n.n.`; `wird nachgereicht` |
| Qualifikation leer | 3 | `BW-01596`, `BW-01654`, `BW-02133` | `(leer)` |
| kein Kontaktweg vorhanden | 2 | `BW-02038`, `BW-02280` | `(leer)` |

### Konsistenz

| Fehlerart | Zeilen | Betroffene Datensätze | Konkrete Werte |
|---|---:|---|---|
| abweichende Schreibweise der Niederlassung | 3 | `BW-01159`, `BW-01472`, `BW-01773` | `Erfurt Zentrale`; `Heilbad Heiligenst.` |
| Statuswert außerhalb der Werteliste | 2 | `BW-01240`, `BW-01385` | `IM POOL`; `im pool` |
| Schreibvariante der Qualifikation Staplerschein | 10 | `BW-01242`, `BW-01280`, `BW-01360`, `BW-01687`, `BW-01797`, `BW-01944`, `BW-02017`, `BW-02031`, `BW-02125`, `BW-02213` | `Helfer Kunststoffverarbeitung, Staplerf.`; `Lagerhelfer, Gabelstapler`; `Lagerhelfer, Flurfördermittelschein`; `Versandmitarbeiter, Staplerausweis`; `Fachlagerist, Stapler-Führerschein, Höhentauglichkeit G41`; `CNC-Fachkraft, Programmierkenntnisse, Stapler (Schein)`; `Fachlagerist, Staplerscheim`; `Lagerhelfer, Fahrerlaubnis Flurförderzeuge, Schichtbereitschaft`; `Sachbearbeitung Auftragsabwicklung, SAP, Gabelstaplerschein`; `Versandmitarbeiter, FFZ-Schein, Höhentauglichkeit G41` |
| Namensreihenfolge gedreht | 3 | `BW-01250`, `BW-01525`, `BW-01633` | `Claudia Groß`; `Holger Lang`; `Dirk Lange` |
| abweichendes Datumsformat im Feld eingang_datum | 2 | `BW-01336`, `BW-01675` | `21.6.2026`; `29.3.2025` |
| Status „…“ ohne jede Qualifikationsangabe | 2 | `BW-01423`, `BW-02008` | `(leer)` |
| abweichendes Datumsformat im Feld einwilligung_bis | 1 | `BW-01511` | `19.7.2029` |

### Aktualität

| Fehlerart | Zeilen | Betroffene Datensätze | Konkrete Werte |
|---|---:|---|---|
| Einwilligungsfrist abgelaufen, Profil weiter aktiv geführt | 10 | `BW-01078`, `BW-01272`, `BW-01311`, `BW-01475`, `BW-01611`, `BW-01901`, `BW-02048`, `BW-02059`, `BW-02264`, `BW-02297` | `2021-04-20`; `2024-07-17`; `2024-05-08`; `2021-07-16`; `2022-11-21`; `2022-04-10`; `2024-01-02`; `2024-12-18`; `2021-08-06`; `2021-04-04` |
| letzter Kontakt liegt vor dem Bewerbungseingang | 3 | `BW-01347`, `BW-02047`, `BW-02198` | `2024-12-01`; `2024-05-20`; `2024-05-30` |
| Status „Im Einsatz“, letzter Kontakt 2023 | 3 | `BW-01822`, `BW-02144`, `BW-02242` | `2023-08-06`; `2023-11-06`; `2023-01-18` |

### Genauigkeit

| Fehlerart | Zeilen | Betroffene Datensätze | Konkrete Werte |
|---|---:|---|---|
| führende Null der Postleitzahl verloren | 4 | `BW-01090`, `BW-01681`, `BW-01787`, `BW-02129` | `7407`; `7580`; `7318`; `7768` |
| überzählige Leerzeichen im Namensfeld | 2 | `BW-01110`, `BW-01779` | `Beck,  Erik`; `Martin,  Rene` |
| Postleitzahl passt nicht zum Ort | 3 | `BW-01223`, `BW-01358`, `BW-01753` | `07545`; `99880`; `07973` |
| unbrauchbare E-Mail-Adresse | 5 | `BW-01229`, `BW-01313`, `BW-01426`, `BW-02261`, `BW-02340` | `jens.dietrich@googlemailcom`; `nico.voigt@gmial.com`; `uwe.schreiber@webde`; `mario.roth@gmial.com`; `franziska.pohl.t-online.de` |
| unplausibles Geburtsdatum | 2 | `BW-01331`, `BW-01356` | `1938-11-09` |
| Zeichensatzfehler im Namen | 2 | `BW-01374`, `BW-02271` | `Schulz, LarsÃ¤`; `Vollmer, AnjaÃ¤` |
| Telefonnummer unbrauchbar oder abweichend formatiert | 2 | `BW-02045`, `BW-02070` | `keine`; `0361 12345` |

## Teil B · Kundendatenbank

**1.040 Zeilen, 57 davon mit mindestens einem eingebauten Fehler = 5,48 Prozent.** Verteilung der Fehlerinstanzen: Vollständigkeit 15, Konsistenz 18, Aktualität 12, Genauigkeit 12.

### Vollständigkeit

| Fehlerart | Zeilen | Betroffene Datensätze | Konkrete Werte |
|---|---:|---|---|
| keine E-Mail-Adresse hinterlegt | 5 | `KD-0025`, `KD-0163`, `KD-0272`, `KD-0902`, `KD-0948` | `(leer)` |
| kein Ansprechpartner hinterlegt | 6 | `KD-0060`, `KD-0440`, `KD-0531`, `KD-0722`, `KD-0865`, `KD-1023` | `(leer)` |
| Rahmenvertrag „…“, aber kein Verrechnungssatz gepflegt | 4 | `KD-0591`, `KD-0667`, `KD-0904`, `KD-1049` | `(leer)` |

### Konsistenz

| Fehlerart | Zeilen | Betroffene Datensätze | Konkrete Werte |
|---|---:|---|---|
| Betreuername abweichend erfasst | 3 | `KD-0047`, `KD-0108`, `KD-0141` | `Steinbrück Nicole`; `MARX`; `HILLE` |
| Branche als Kurzform erfasst | 4 | `KD-0143`, `KD-0687`, `KD-0779`, `KD-0877` | `Elektro`; `Logistik`; `Metall` |
| Dublette: derselbe Betrieb ein zweites Mal, mit eigener Kundennummer | 6 | `KD-0277`, `KD-0318`, `KD-0493`, `KD-0631`, `KD-0761`, `KD-1046` | `KD-0301 (Elektrotechnik Beck e.K.)`; `KD-1001 (Jenaer Umschlaglager GmbH & Co. KG)`; `KD-0436 (Becker Schaltanlagen GmbH & Co. KG)`; `KD-0212 (Zimmermann Offsetdruck GmbH & Co. KG)`; `KD-0633 (Präzisionstechnik Wolf GmbH)`; `KD-0423 (Bad Langensalzaer Backwaren GmbH)` |
| Dezimalpunkt statt Dezimalkomma im Verrechnungssatz | 3 | `KD-0283`, `KD-0446`, `KD-0933` | `32.88`; `26.35`; `28.14` |
| mehr Besetzungen als Anfragen | 2 | `KD-0295`, `KD-0380` | `8`; `15` |

### Aktualität

| Fehlerart | Zeilen | Betroffene Datensätze | Konkrete Werte |
|---|---:|---|---|
| Status „Aktiv“, letzte Anfrage lange vor 2025, kein Vorgang 2025 | 8 | `KD-0026`, `KD-0352`, `KD-0431`, `KD-0497`, `KD-0674`, `KD-0740`, `KD-0827`, `KD-0893` | `2021-07-22`; `2022-11-10`; `2022-11-21`; `2021-02-14`; `2023-04-24`; `2021-05-14`; `2022-12-11`; `2023-04-09` |
| letzte Anfrage liegt in der Zukunft | 2 | `KD-0175`, `KD-0768` | `2027-08-14`; `2027-07-15` |
| Interessent ohne jede Anfrage, letzter Kontakt vor 2022 | 2 | `KD-0447`, `KD-0727` | `2019-04-09`; `2021-11-06` |

### Genauigkeit

| Fehlerart | Zeilen | Betroffene Datensätze | Konkrete Werte |
|---|---:|---|---|
| Zeichensatzfehler im Firmennamen | 2 | `KD-0110`, `KD-0712` | `FlÃ¤ischwerk Apolda e.K.`; `Ludwig PrÃ¤zisionsteile GmbH` |
| führende Null der Postleitzahl verloren | 3 | `KD-0138`, `KD-0456`, `KD-0782` | `6484`; `7318`; `6449` |
| Postleitzahl passt nicht zum Ort | 3 | `KD-0170`, `KD-0921`, `KD-0949` | `99885`; `99310`; `99098` |
| unplausibler Verrechnungssatz | 2 | `KD-0336`, `KD-0808` | `2,95` |
| Freemail-Adresse ohne Bezug zum Firmennamen | 2 | `KD-0689`, `KD-0701` | `kontakt@web.de`; `buchhaltung@gmx.de` |

## Die Fehler, die man nur an der Lücke sieht

Diese acht Befunde stehen **nicht in einer Zeile**. Sie sind nur zu finden, wenn man die Datei gegen
eine Erwartung hält: gegen das Unternehmensprofil, gegen die eigene Feldliste oder gegen die zweite
Datei. Sie zählen deshalb nicht in die Prozentquote der betroffenen Zeilen.

| # | Befund | Wie man es sieht | Bezug zum Fall |
|---:|---|---|---|
| S1 | **Die Niederlassung Aschersleben kommt in der Bewerberdatenbank nicht ein einziges Mal vor.** In der Kundendatenbank hat sie 109 Kunden und 269 Anfragen im Jahr 2025 | `niederlassung` in beiden Dateien auszählen und gegen die sechs Standorte aus [`profil.md`](../profil.md) halten. Ein Standort, der Kunden und Anfragen hat, aber keinen einzigen Bewerber | Der Bestand einer Niederlassung ist im Auszug nicht enthalten. Wer die Besetzungsquote je Standort rechnet, teilt dort durch Null und merkt es nicht — die Standorte sind sieben Firmen (Kulturmerkmal 5) |
| S2 | **In der Bewerberdatenbank fehlen 27 laufende IDs**, verteilt über neun Lücken (`BW-01065`, `BW-01066`, `BW-01298`, `BW-01299` …). In der Kundendatenbank fehlt ein zusammenhängender Block von 18 IDs: `KD-0834` bis `KD-0851` | `max(id) - min(id) + 1` gegen die Zeilenzahl rechnen | Gelöschte oder nie migrierte Datensätze ohne jede Spur. Ein Löschlauf ohne Protokoll ist von einem Datenverlust nicht zu unterscheiden — genau der Punkt aus [`datenverantwortung.md`](../datenverantwortung.md), Befund 3 |
| S3 | **Es gibt keine Spalte für die Verfügbarkeit.** Das Feld, das die Disposition täglich braucht — wer ab wann frei ist — existiert im Datensatz nicht | Spaltenliste gegen die Frage halten: „Kann ich mit dieser Datei eine Anfrage für nächste Woche besetzen?" Antwort: nein | Wörtlich der Befund aus [`systeme-daten.md`](../systeme-daten.md), Schatten-IT Zeile 2: *„Das System zeigt nicht, wer nächste Woche frei ist."* Deshalb sechs Excel-Listen in sechs Formaten |
| S4 | **Es gibt keine Spalte für die Quelle der Bewerbung.** Weder Jobbörse noch Anzeige noch Empfehlung sind erfasst | Spaltenliste. Dann die Frage: welche der 480.000 Euro Anzeigenbudget haben gewirkt? | [`systeme-daten.md`](../systeme-daten.md): *„Bewerbungen kommen ohne Quellenkennung zurück. 480.000 Euro ohne Wirkungsnachweis"* |
| S5 | **Es gibt keine Spalte für den Grund der Nichtbesetzung.** Die Kundendatenbank weist 3.100 Anfragen und 1.240 Besetzungen aus. Die Differenz von **1.860 nicht besetzten Anfragen** ist im Datensatz vorhanden, ihre Ursache nicht | `sum(anfragen_2025) - sum(besetzungen_2025)` rechnen und dann nach der Spalte suchen, die erklärt, woran es lag | Der Befund, der den Piloten gefährdet: *„Die Besetzungshistorie enthält, wer besetzt wurde, aber nicht, warum die anderen 1.860 Anfragen nicht besetzt wurden."* Ohne diese Zielgröße lernt kein Modell Besetzungswahrscheinlichkeit |
| S6 | **In der Bewerberdatenbank fehlt ein Zeitraum vollständig:** zwischen dem **19.12.2025 und dem 26.01.2026** ist kein einziger Bewerbungseingang verzeichnet | `eingang_datum` nach Monat gruppieren und die Reihe ansehen. Fünf Wochen bei Null, davor und danach normal | Exportlücke oder Systemwechsel im Dezember. Wer Bewerbereingänge im Jahresverlauf auswertet, liest einen Einbruch, den es nicht gab |
| S7 | **In der Kundendatenbank gibt es keinen einzigen öffentlichen Auftraggeber**, obwohl [`profil.md`](../profil.md) sie als Kundengruppe nennt | Werteliste der Spalte `branche` gegen die Kundengruppen im Profil halten | Eine ganze Kundengruppe fehlt in den Daten, mit der sie in der Steuerung nicht vorkommt. Bei öffentlichen Auftraggebern hängen daran Vergabefristen und andere Preislogik |
| S8 | **Der Auszug endet bei 23 Monaten Bewerbungseingang** — abgesehen von den 10 Altfällen mit abgelaufener Einwilligung. Von den 41.000 Profilen des Falls ist damit nur ein Bruchteil enthalten, und die Datei sagt das nicht | `min(eingang_datum)` gegen die 41.000 Profile aus [`profil.md`](../profil.md) halten | Ein Auszug ohne Angabe des Filters wird als Gesamtbestand gelesen. Die 18.000 überfälligen Profile sind hier **nicht** enthalten — wer die Löschpflicht an dieser Datei prüft, hält sie für ein Randproblem |

## Prüfrezepte

Ein Weg, jeden Fehler zu finden, ohne die Auflösung zu kennen. Reihenfolge nach Ertrag.

| Schritt | Prüfung | Findet |
|---:|---|---|
| 1 | Zeilenzahl gegen `max(id) − min(id) + 1` | S2 |
| 2 | Spaltenliste gegen die eigene Frage: welche Felder bräuchte ich, um den Kernprozess zu steuern? | S3, S4, S5 |
| 3 | Häufigkeitstabelle je kategorialem Feld (`niederlassung`, `status`, `branche`, `betreuer`, `rahmenvertrag`) | Schreibvarianten, Werte außerhalb der Liste, **und** fehlende Werte wie S1 und S7 |
| 4 | Leer- und Platzhalterquote je Spalte, Platzhalter (`k.A.`, `-`, `siehe Lebenslauf`) mitzählen | alle Vollständigkeitsfehler |
| 5 | Datumsfelder auf Format prüfen, dann auf Reihenfolge (`letzter_kontakt` ≥ `eingang_datum`, kein Datum in der Zukunft) | Formatbrüche, Datumsdreher, Zukunftsdaten |
| 6 | Fristenprüfung: `einwilligung_bis < heute` bei aktivem Status | Aktualitätsfehler Bewerber |
| 7 | Histogramm `eingang_datum` je Monat | S6, S8 |
| 8 | Regelprüfungen über zwei Spalten: `besetzungen ≤ anfragen`, Rahmenvertrag `Ja` → Satz gepflegt, PLZ-Präfix passend zum Ort | Konsistenz- und Genauigkeitsfehler Kunden |
| 9 | Wertebereiche: Geburtsjahr, Verrechnungssatz, PLZ-Länge (fünf Zeichen) | unplausible Werte, verlorene führende Null |
| 10 | Dublettensuche über normalisierten Firmennamen (Kleinschreibung, Rechtsform und Leerzeichen entfernt) | Dubletten |
| 11 | Volltextsuche nach `Ã` in allen Feldern | Zeichensatzfehler |
| 12 | Regex auf `email`: genau ein `@`, Punkt in der Domain, keine Leerzeichen | unbrauchbare Adressen |

## Reproduzierbarkeit

Beide Dateien sind mit festem Seed erzeugt und identisch reproduzierbar: `SEED = 20260908`
(Bewerber) und `SEED + 1` (Kunden). Trennzeichen `;`, Kodierung UTF-8 ohne BOM,
Dezimaltrennzeichen Komma, Datumsformat ISO `JJJJ-MM-TT` — jeweils außer in den Zeilen, in denen
genau das der eingebaute Fehler ist. Die Generatorskripte liegen nicht im Repository, weil sie den
Zufall und damit die Lösung enthalten; die Auflösung hier ist aus ihrem Protokoll erzeugt, nicht
von Hand geschrieben.
