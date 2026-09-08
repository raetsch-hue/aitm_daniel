---
titel: Vergleich Datenqualitätsberichte mit Auflösung
datum: 2026-09-08
basis:
  - bericht-bewerber.txt
  - bericht-kunden.txt
  - AUFLOESUNG-datenqualitaet.md
fokus: Eingebaute Fehler und Strukturprobleme, die von den Berichten nicht oder nicht ausdrücklich erkannt wurden
---

# Vergleich der Datenqualitätsberichte mit der Auflösung

# Trefferquote auf einen Blick

| Datei | Eingebaute Fehler laut Auflösung | Explizit als beabsichtigter Fehler erkannt | Nur indirekt auffällig | Komplett nicht erkannt |
|---|---:|---:|---:|---:|
| `bewerberdatenbank.csv` | **79** | **49 von 79 = 62,0 %** | 7 | 23 |
| `kundendatenbank.csv` | **57** | **33 von 57 = 57,9 %** | 14 | 10 |
| **Gesamt** | **136** | **82 von 136 = 60,3 %** | **21** | **33** |

**Kurz gesagt:**  
- Bewerberdatei: **49 von 79 eingebauten Fehlern klar erkannt**. Werden die 7 nur indirekt sichtbaren Fälle mitgezählt, wurden **56 von 79 zumindest technisch auffällig**.  
- Kundendatei: **33 von 57 eingebauten Fehlern klar erkannt**. Werden die 14 nur indirekt sichtbaren Fälle mitgezählt, wurden **47 von 57 zumindest technisch auffällig**.  
- Über beide Dateien hinweg wurden damit **82 von 136 Fehlern eindeutig erkannt**; **103 von 136** wurden zumindest direkt oder indirekt sichtbar.

> „Explizit erkannt“ bedeutet: Der Bericht benennt den tatsächlich eingebauten Fehler bzw. dieselbe fachliche Regel.  
> „Nur indirekt auffällig“ bedeutet: Der Datensatz taucht zwar in einer allgemeineren Prüfung auf, die eigentliche fachliche Fehlerlogik wird aber nicht erkannt.

---

## Kurzfazit

Die beiden automatischen Berichte erkennen einen großen Teil der **formal leicht prüfbaren** Probleme zuverlässig: leere Felder, ID-Lücken, falsche Datumsformate, vierstellige PLZ, Zeichensatzfehler, Zukunftsdaten, abgelaufene Einwilligungen und Kundendubletten.

Schwächer sind sie dort, wo **fachlicher Kontext**, **Beziehungen zwischen mehreren Feldern** oder **eine externe Erwartung an den Datenbestand** nötig sind.

Im direkten Abgleich mit der Auflösung ergeben sich:

- **33 eingebaute Fehlerinstanzen, die nicht erkannt wurden**
  - Bewerberdatenbank: **23**
  - Kundendatenbank: **10**
- zusätzlich **21 Fehlerinstanzen, die nur indirekt als allgemeine Auffälligkeit auftauchen**, aber nicht als der eigentlich eingebaute fachliche Fehler erkannt werden
  - Bewerberdatenbank: **7**
  - Kundendatenbank: **14**
- außerdem bleiben **4 strukturelle Befunde aus S3–S5 und S7–S8** ganz bzw. überwiegend unentdeckt; S8 wird nur indirekt berührt.

> Die Zählung unterscheidet bewusst zwischen **„nicht gefunden“** und **„indirekt gefunden“**.  
> Beispiel: Ein leeres Qualifikationsfeld wird technisch gezählt. Die fachliche Regel  
> „Status X darf nicht ohne Qualifikation vorkommen“ wird dadurch aber noch nicht erkannt.

---

# Teil A – Bewerberdatenbank

## 1. Nicht gefundene eingebaute Fehler

### Vollständigkeit

#### Platzhalter in der Qualifikation nicht erkannt – 2 Fälle

Der Bericht erkennt nur `BW-01990` mit „wird nachgereicht“.

Nicht erkannt wurden:

- `BW-01341` – Qualifikation mit Platzhalter `n.n.`
- `BW-01464` – Qualifikation mit Platzhalter `n.n.` bzw. entsprechender eingebauter Platzhaltervariante

**Ursache:** Die Platzhalterliste des Prüfers ist zu eng.

---

### Konsistenz

#### Abweichende Niederlassungsbezeichnung nicht vollständig erkannt – 2 Fälle

Von drei eingebauten Fällen wird nur `BW-01472` („Heilbad Heiligenst.“) als Schreibvariante erkannt.

Nicht erkannt wurden:

- `BW-01159`
- `BW-01773`

Beide gehören laut Auflösung zur eingebauten Abweichung der Niederlassungsbezeichnung.

**Ursache:** Die Prüfung erkennt nur Ähnlichkeiten zu häufigen vorhandenen Werten, aber keine verbindliche Soll-Werteliste der Niederlassungen.

---

#### Schreibvarianten von „Staplerschein“ nur teilweise erkannt – 7 Fälle

Die Auflösung enthält 10 bewusst eingebaute Varianten. Der Bericht erkennt nur:

- `BW-01944`
- `BW-02017`
- `BW-02125`

Nicht erkannt wurden:

- `BW-01242` – `Staplerf.`
- `BW-01280` – `Gabelstapler`
- `BW-01360` – `Flurfördermittelschein`
- `BW-01687` – `Staplerausweis`
- `BW-01797` – `Stapler-Führerschein`
- `BW-02031` – `Fahrerlaubnis Flurförderzeuge`
- `BW-02213` – `FFZ-Schein`

**Ursache:** Ein reiner Ähnlichkeitsvergleich erkennt Synonyme und fachliche Abkürzungen nicht zuverlässig.

---

#### Gedrehte Namensreihenfolge vollständig übersehen – 3 Fälle

Nicht erkannt wurden:

- `BW-01250` – `Claudia Groß`
- `BW-01525` – `Holger Lang`
- `BW-01633` – `Dirk Lange`

**Ursache:** Es fehlt eine Regel für das erwartete Namensformat `Nachname, Vorname`.

---

### Aktualität / zeitliche Konsistenz

#### Letzter Kontakt liegt vor Bewerbungseingang – 3 Fälle

Nicht erkannt wurden:

- `BW-01347`
- `BW-02047`
- `BW-02198`

**Ursache:** Der Bericht prüft einzelne Datumsfelder auf Alter, Zukunft und Format, aber nicht die **Reihenfolge zweier Datumsfelder innerhalb derselben Zeile**.

---

### Genauigkeit

#### PLZ passt nicht zum Ort – 3 Fälle

Nicht erkannt wurden:

- `BW-01223` – PLZ `07545`
- `BW-01358` – PLZ `99880`
- `BW-01753` – PLZ `07973`

**Ursache:** Die Prüfung kontrolliert nur die Länge der PLZ, nicht die fachliche Beziehung zwischen `plz` und `ort`.

---

#### Syntaktisch gültige, aber fachlich falsche E-Mail-Domain – 2 Fälle

Nicht erkannt wurden:

- `BW-01313` – `nico.voigt@gmial.com`
- `BW-02261` – `mario.roth@gmial.com`

**Ursache:** Der Regex prüft nur die formale Struktur. `gmial.com` ist syntaktisch eine gültige Domain und wird deshalb nicht beanstandet.

---

#### Auffällige Telefonnummer nicht erkannt – 1 Fall

Nicht erkannt:

- `BW-02070` – `0361 12345`

**Ursache:** Die Nummer erfüllt offenbar die Mindestanzahl an Ziffern bzw. fällt nicht unter die verwendete Regel, obwohl sie laut Lösungsblatt bewusst als unbrauchbar oder abweichend formatiert eingebaut wurde.

---

## 2. Nur indirekt gefunden, aber fachlich nicht erkannt

### Kein Kontaktweg vorhanden – 2 Fälle

- `BW-02038`
- `BW-02280`

Die leeren Einzelzellen werden durch V1 mitgezählt. Der Bericht erkennt aber nicht die fachliche Kombination:

> **E-Mail UND Telefonnummer fehlen gleichzeitig → Bewerber ist nicht kontaktierbar.**

---

### Status ohne Qualifikationsangabe – 2 Fälle

- `BW-01423`
- `BW-02008`

Die leeren Qualifikationsfelder werden in V1 gezählt, aber die fachliche Regel „dieser Status ohne Qualifikation ist inkonsistent“ fehlt.

---

### Status „Im Einsatz“, letzter Kontakt aus 2023 – 3 Fälle

- `BW-01822`
- `BW-02144`
- `BW-02242`

Die alten Kontaktdaten können in A1 als „älter als 730 Tage“ auftauchen. Nicht erkannt wird aber der entscheidende Widerspruch:

> **Aktueller Status „Im Einsatz“ passt nicht zu einem seit 2023 nicht aktualisierten Kontaktstand.**

---

## 3. Bewerber – Zusammenfassung

| Art | Nicht erkannt | Nur indirekt erkannt |
|---|---:|---:|
| Vollständigkeit | 2 | 2 |
| Konsistenz | 12 | 2 |
| Aktualität | 3 | 3 |
| Genauigkeit | 6 | 0 |
| **Summe** | **23** | **7** |

Damit werden **30 der 79 eingebauten Bewerber-Fehler nicht ausdrücklich als der beabsichtigte Fehler erkannt**. Davon sind 23 komplett verpasst und 7 nur über allgemeinere Prüfungen sichtbar.

---

# Teil B – Kundendatenbank

## 1. Nicht gefundene eingebaute Fehler

### Konsistenz

#### Abweichender Betreuername nur teilweise erkannt – 1 Fall

Erkannt werden:

- `KD-0108` – `MARX`
- `KD-0141` – `HILLE`

Nicht erkannt:

- `KD-0047` – `Steinbrück Nicole`

**Ursache:** Groß-/Kleinschreibungsvarianten werden gefunden, eine gedrehte Namensreihenfolge aber nicht.

---

#### Branchen-Kurzformen vollständig übersehen – 4 Fälle

Nicht erkannt wurden:

- `KD-0143`
- `KD-0687`
- `KD-0779`
- `KD-0877`

Eingebaute Kurzformen sind u. a.:

- `Elektro`
- `Logistik`
- `Metall`

**Ursache:** Ohne verbindliche Branchen-Werteliste kann der Prüfer nicht entscheiden, dass eine formal plausible Kurzform fachlich unerwünscht ist.

---

### Genauigkeit

#### PLZ passt nicht zum Ort – 3 Fälle

Nicht erkannt wurden:

- `KD-0170` – PLZ `99885`
- `KD-0921` – PLZ `99310`
- `KD-0949` – PLZ `99098`

**Ursache:** Wie bei den Bewerbern wird nur das PLZ-Format geprüft, nicht die Zuordnung zum Ort.

---

#### Freemail-Adresse ohne Bezug zum Unternehmen – 2 Fälle

Nicht erkannt wurden:

- `KD-0689` – `kontakt@web.de`
- `KD-0701` – `buchhaltung@gmx.de`

**Ursache:** Die Adressen sind formal gültig. Für den Fehler braucht es eine fachliche Plausibilitätsregel, z. B. „Unternehmensadresse sollte zur Firmen-Domain passen“ bzw. eine Kennzeichnung von Freemail-Domains.

---

## 2. Nur indirekt gefunden, aber fachlich nicht erkannt

### Rahmenvertrag vorhanden, aber Verrechnungssatz fehlt – 4 Fälle

- `KD-0591`
- `KD-0667`
- `KD-0904`
- `KD-1049`

Der Bericht meldet insgesamt **222 leere Verrechnungssätze**. Das ist technisch korrekt, aber viel zu unspezifisch.

Der eigentliche eingebaute Fehler lautet:

> **Rahmenvertrag vorhanden → Verrechnungssatz muss gepflegt sein.**

Diese fachliche Abhängigkeit wird nicht geprüft.

---

### Status „Aktiv“, aber letzte Anfrage lange vor 2025 und keine Aktivität 2025 – 8 Fälle

- `KD-0026`
- `KD-0352`
- `KD-0431`
- `KD-0497`
- `KD-0674`
- `KD-0740`
- `KD-0827`
- `KD-0893`

A1 meldet generell 399 alte `letzte_anfrage`-Werte. Dadurch werden die Zeilen vermutlich technisch mit erfasst, aber die relevante Kombination wird nicht erkannt:

> **kundenstatus = Aktiv** + **alte letzte Anfrage** + **keine Anfrage 2025**

---

### Interessent ohne Anfrage und mit sehr altem Stand – 2 Fälle

- `KD-0447`
- `KD-0727`

Auch diese Zeilen fallen wahrscheinlich unter die allgemeine Altersprüfung A1. Die fachliche Kombination aus Interessentenstatus, fehlender Aktivität und sehr altem Datum wird jedoch nicht geprüft.

---

## 3. Kunden – Zusammenfassung

| Art | Nicht erkannt | Nur indirekt erkannt |
|---|---:|---:|
| Vollständigkeit | 0 | 4 |
| Konsistenz | 5 | 0 |
| Aktualität | 0 | 10 |
| Genauigkeit | 5 | 0 |
| **Summe** | **10** | **14** |

Damit werden **24 der 57 eingebauten Kunden-Fehler nicht ausdrücklich als der beabsichtigte Fehler erkannt**. Davon sind 10 komplett verpasst und 14 nur indirekt über allgemeinere Prüfungen sichtbar.

---

# Teil C – Strukturelle Fehler „nur an der Lücke“

Die Auflösung enthält zusätzlich acht Befunde S1–S8, die nicht zwingend in einer einzelnen Zeile stecken.

| Befund | Status im Bericht | Bewertung |
|---|---|---|
| **S1 – Niederlassung Aschersleben fehlt in Bewerberdaten** | **gefunden** | V5.2 meldet Aschersleben als fehlende Niederlassung |
| **S2 – laufende IDs fehlen** | **gefunden** | V4 findet 27 fehlende Bewerber-IDs und 18 fehlende Kunden-IDs |
| **S3 – Spalte Verfügbarkeit fehlt** | **nicht gefunden** | Keine Prüfung der Feldliste gegen den Kernprozess |
| **S4 – Quelle der Bewerbung fehlt** | **nicht gefunden** | Keine Prüfung gegen Marketing-/Attributionsbedarf |
| **S5 – Grund der Nichtbesetzung fehlt** | **nicht gefunden** | Die 1.860 nicht besetzten Anfragen werden nicht als fehlende Ziel-/Erklärvariable erkannt |
| **S6 – Bewerbungseingänge fehlen über mehrere Wochen** | **gefunden** | A4 erkennt die Zeitlücke (40 Tage) |
| **S7 – öffentliche Auftraggeber fehlen vollständig** | **nicht gefunden** | Vergleich mit dem Unternehmensprofil / erwarteten Kundengruppen fehlt |
| **S8 – Auszug deckt nur ca. 23 Monate ab** | **nur indirekt** | A1 erkennt alte Datensätze, aber nicht, dass der Export nur einen kleinen und ungekennzeichneten Ausschnitt des Gesamtbestands darstellt |

## Wichtigste strukturelle Lücken

Besonders relevant für eine spätere KI-/RAG-Nutzung sind die nicht gefundenen Punkte:

1. **Verfügbarkeit fehlt** – damit ist keine belastbare Disposition für kommende Zeiträume möglich.
2. **Bewerbungsquelle fehlt** – damit lässt sich die Wirkung des Anzeigenbudgets nicht messen.
3. **Nichtbesetzungsgrund fehlt** – damit fehlt eine zentrale Ziel-/Erklärvariable für Besetzungswahrscheinlichkeit.
4. **Kundengruppe „öffentliche Auftraggeber“ fehlt** – der Datenbestand bildet die beschriebene Organisation nicht vollständig ab.
5. **Exportumfang ist nicht dokumentiert** – ein Teilauszug kann fälschlich als Gesamtbestand interpretiert werden.

---

# Teil D – Auffälligkeiten des automatischen Prüfberichts selbst

Neben den verpassten Fehlern erzeugen die Berichte auch Befunde, die **nicht als eingebaute Fehler in der Auflösung vorgesehen sind**.

## 1. Kundendaten: 222 fehlende Verrechnungssätze

Der Bericht behandelt alle 222 leeren Werte als Vollständigkeitsbefund.

Die Auflösung markiert jedoch nur **4 Fälle** als tatsächlichen Fehler, nämlich dort, wo ein Rahmenvertrag vorhanden ist und deshalb ein Verrechnungssatz erwartet wird.

**Lehre:** Leere Werte sind nicht automatisch Datenfehler. Es braucht fachliche Konditionen.

---

## 2. Kundendaten: K4 erzeugt 33 vermeintliche E-Mail-Schreibvarianten

Beispiele wie

- `info@elektromontage.de` vs. `office@elektromontage.de`
- `hr@anlagenbau.de` vs. `info@anlagenbau.de`

sind nicht automatisch Schreibfehler. Es können unterschiedliche, völlig legitime Funktionspostfächer sein.

Keiner dieser 33 Befunde ist im Lösungsblatt als eingebauter Fehler ausgewiesen.

**Lehre:** Fuzzy Matching auf kompletten E-Mail-Adressen produziert hier viele Fehlalarme.

---

## 3. Allgemeine Altersprüfung ist zu breit

Bei den Kunden meldet A1 **399 alte Datensätze**. Die eingebauten Fehler betreffen dagegen nur bestimmte fachliche Kombinationen, z. B. „Aktiv, aber seit Jahren ohne Anfrage“.

**Lehre:** Eine starre Altersschwelle erkennt technische Auffälligkeiten, ersetzt aber keine Statuslogik.

---

## 4. Zeitlücken in Kundenanfragen

Der Bericht meldet zahlreiche 14- bis 28-tägige Lücken und fehlende Monate in `letzte_anfrage`. Diese sind im Lösungsblatt nicht als eingebaute Fehler definiert.

**Lehre:** Eine Zeitlücke ist nur dann ein Datenqualitätsproblem, wenn fachlich eine kontinuierliche Ereignisfolge zu erwarten wäre.

---

# Gesamtbewertung

Der automatische Prüfer ist **gut bei syntaktischer und technischer Datenqualität**, aber deutlich schwächer bei **semantischer und fachlicher Datenqualität**.

## Gut erkannt

- leere Einzelwerte
- ID-Lücken
- vierstellige PLZ
- Zeichensatzfehler
- einfache E-Mail-Syntaxfehler
- Datumsformatabweichungen
- Zukunftsdaten
- abgelaufene Einwilligungen
- Dubletten über normalisierte Firmennamen
- einfache Zahlen-/Spaltenregeln wie `besetzungen <= anfragen`

## Nicht ausreichend erkannt

- Synonyme und fachliche Schreibvarianten
- verbindliche Wertelisten
- Namensformat
- Beziehungen zwischen PLZ und Ort
- Beziehungen zwischen Status und Aktualität
- Beziehungen zwischen Rahmenvertrag und Verrechnungssatz
- Reihenfolge mehrerer Datumsfelder
- fehlende Prozessfelder
- fehlende Kundengruppen
- unvollständiger Exportumfang
- semantisch plausible, aber fachlich falsche Werte

## Schlussfolgerung

Für einen belastbaren Datenqualitätscheck reicht ein generischer technischer Prüfer nicht aus. Er sollte um drei Ebenen ergänzt werden:

1. **Fachliche Regeln über mehrere Felder**  
   Beispiel: `rahmenvertrag = Ja → verrechnungssatz_std muss gefüllt sein`.

2. **Referenz- und Sollwertwissen**  
   Beispiel: gültige Niederlassungen, Branchen, PLZ-Ort-Zuordnung, Freemail-Domains.

3. **Prozess- und Vollständigkeitsprüfung des Datenmodells**  
   Beispiel: Sind Verfügbarkeit, Bewerbungsquelle und Nichtbesetzungsgrund überhaupt als Felder vorhanden?

Erst diese Kombination aus **technischer Prüfung + Fachregeln + Kontextwissen** deckt die im Lösungsblatt eingebauten Datenqualitätsprobleme weitgehend ab.
