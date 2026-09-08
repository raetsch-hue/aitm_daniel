---
ordner: GeAT-unternehmensprofil/daten
inhalt: zwei generierte Übungsdatensätze zur Datenqualität plus Auflösung
datum: 2026-09-08
woche: 03
status: einsatzbereit
herkunft: vollständig generiert. Kein Wert stammt aus einem realen System
---

# Übungsdatensätze GeAT mbH

> **Alles hier ist erfunden.** Personen, Firmen, Anschriften, Sätze und Mengen sind generiert.
> Übereinstimmungen mit real existierenden Betrieben sind unbeabsichtigt und ohne Bedeutung.
> Die **Struktur** der Dateien folgt [`systeme-daten.md`](../systeme-daten.md), das **Mengengerüst**
> [`zahlen.md`](../zahlen.md), die Standorte [`profil.md`](../profil.md). Nichts aus diesem Ordner
> gehört in ein Artefakt über eine reale Organisation.

## Die Dateien

| Datei | Inhalt | Zeilen | Spalten |
|---|---|---:|---:|
| [`bewerberdatenbank.csv`](bewerberdatenbank.csv) | Auszug aus dem Bewerberbestand der Branchensoftware / des ATS | 1.284 | 14 |
| [`kundendatenbank.csv`](kundendatenbank.csv) | Kundenstamm mit Betreuung, Rahmenverträgen und den Anfragen des Jahres 2025 | 1.040 | 15 |
| [`bewerberdatenbank-korrigiert.csv`](bewerberdatenbank-korrigiert.csv) | Zielzustand: bereinigt und ergänzt, 23 von 24 Prüfungen ohne Treffer | 1.473 | 16 |
| [`kundendatenbank-korrigiert.csv`](kundendatenbank-korrigiert.csv) | Zielzustand: bereinigt und ergänzt | 1.078 | 17 |
| [`KORREKTUR-dokumentation.md`](KORREKTUR-dokumentation.md) | Änderungsprotokoll der korrigierten Fassungen samt Nachweis | — | — |
| [`pruefe_datenqualitaet.py`](pruefe_datenqualitaet.py) | Prüfskript: 22 Prüfungen über die vier Dimensionen, Bericht als Text, Markdown oder JSON | — | — |
| [`ERLAEUTERUNG-pruefungen-und-rag.md`](ERLAEUTERUNG-pruefungen-und-rag.md) | Je Prüfung ein Satz: was der Befund für ein RAG-System bedeutet. Verrät die Lösung nicht | — | — |
| [`ANLEITUNG-regeln.md`](ANLEITUNG-regeln.md) | Anleitung zur Option `--regel`: Syntax, geprüfter Regelkatalog, Fallen, Weg von der Prüfregel zur Systemregel | — | — |
| [`AUFLOESUNG-datenqualitaet.md`](AUFLOESUNG-datenqualitaet.md) | **Lösungsblatt.** Erst nach der eigenen Analyse öffnen | — | — |

**Format.** Trennzeichen `;`, Kodierung UTF-8 ohne BOM, Dezimaltrennzeichen Komma,
Datumsangaben ISO `JJJJ-MM-TT`. In Excel über *Daten → Aus Text/CSV* öffnen und die Kodierung auf
UTF-8 stellen, nicht per Doppelklick — sonst entstehen zusätzliche Fehler, die nicht in den Daten
liegen. In pandas: `pd.read_csv(pfad, sep=";", dtype=str, keep_default_na=False)`. `dtype=str` ist
wichtig, sonst repariert und zerstört pandas beim Einlesen Werte, um die es in der Übung geht.

## Spalten Bewerberdatenbank

| Spalte | Bedeutung |
|---|---|
| `bewerber_id` | laufende Nummer, Format `BW-#####` |
| `name` | Nachname, Vorname |
| `geburtsdatum` | Geburtsdatum |
| `plz`, `ort` | Wohnort der Bewerberin oder des Bewerbers |
| `telefon`, `email` | Kontaktwege |
| `qualifikation` | Freitextfeld: Beruf, Maschinen, Scheine, Bereitschaften |
| `berufsfeld` | Zuordnung zu einem der zehn Berufsfelder des Hauses |
| `niederlassung` | betreuender Standort |
| `eingang_datum` | Eingang der Bewerbung |
| `letzter_kontakt` | letzter dokumentierter Kontakt |
| `einwilligung_bis` | Ende der den Bewerbern zugesagten Speicherdauer |
| `status` | Neu, Erstgespräch geführt, Im Pool, Im Einsatz, Vermittelt, Abgelehnt, Kein Interesse, Nicht erreichbar |

## Spalten Kundendatenbank

| Spalte | Bedeutung |
|---|---|
| `kunde_id` | laufende Nummer, Format `KD-####` |
| `firmenname` | Firmierung des Kundenbetriebs |
| `branche` | Branche des Kundenbetriebs |
| `plz`, `ort` | Sitz des Betriebs |
| `ansprechpartner` | Kontaktperson im Betrieb |
| `email` | Kontaktadresse |
| `niederlassung` | betreuender Standort |
| `betreuer` | zuständige Person im Vertrieb oder in der Disposition |
| `kundenstatus` | Aktiv, Inaktiv, Interessent |
| `rahmenvertrag` | Ja oder Nein |
| `verrechnungssatz_std` | vereinbarter Verrechnungssatz in Euro je Überlassungsstunde |
| `letzte_anfrage` | Datum der letzten Personalanfrage |
| `anfragen_2025` | Zahl der Personalanfragen im Jahr 2025 |
| `besetzungen_2025` | Zahl der daraus besetzten Stellen |

## Das Prüfskript

```bash
python3 pruefe_datenqualitaet.py bewerberdatenbank.csv --stichtag 2026-09-08
python3 pruefe_datenqualitaet.py kundendatenbank.csv --regel "besetzungen_2025<=anfragen_2025"
python3 pruefe_datenqualitaet.py bewerberdatenbank.csv     --vergleich kundendatenbank.csv --vergleich-spalten niederlassung
python3 pruefe_datenqualitaet.py kundendatenbank.csv --markdown > bericht.md
```

Nur Standardbibliothek, keine Installation. Trennzeichen, Kodierung und Spaltentypen erkennt das
Skript selbst; es ist damit auch auf andere CSV-Dateien anwendbar. `--max-alter-tage` setzt die
Aktualitätsschwelle (Vorgabe 730), `--beispiele` die Zahl der Beispielzeilen je Prüfung (Vorgabe 5),
`--json` gibt die Befunde maschinenlesbar aus. Was jeder Befund für ein RAG-System bedeutet, steht
in [`ERLAEUTERUNG-pruefungen-und-rag.md`](ERLAEUTERUNG-pruefungen-und-rag.md) — je Prüfung ein Satz.

**Das Skript ersetzt die eigene Analyse nicht.** Es findet, was sich als Regel formulieren lässt.
Fehlende Spalten, fehlende Kundengruppen und ein Standort ohne Datensätze findet es nur, wenn man
ihm die Frage stellt — bei `--vergleich` etwa den Abgleich beider Dateien.

## Die Aufgabe

In beiden Dateien stecken absichtlich eingebaute Datenqualitätsprobleme, verteilt über die vier
Dimensionen **Vollständigkeit, Konsistenz, Aktualität und Genauigkeit**. Betroffen sind jeweils
zwischen drei und acht Prozent der Zeilen, ungleichmäßig über die Datei verteilt.

Drei Hinweise, mehr nicht:

1. **Ein gefülltes Feld ist nicht automatisch ein brauchbares Feld.** Zählen Sie Platzhalter mit.
2. **Mindestens eine Fehlerart ist in keiner einzelnen Zeile zu sehen.** Sie zeigt sich nur, wenn man
   die Datei gegen eine Erwartung hält: gegen die Standorte und Kundengruppen aus dem
   Unternehmensprofil, gegen die eigene Liste der Felder, die man zur Steuerung des Kernprozesses
   bräuchte, oder gegen die jeweils andere Datei. Fragen Sie also auch, **was fehlt** — nicht nur,
   was falsch ist.
3. **Beide Dateien gehören zusammen.** Ein Teil der Befunde entsteht erst im Abgleich.

Ein Vorschlag für die Reihenfolge und ein Satz Prüfrezepte stehen am Ende der Auflösung — dort auch
die vollständige Liste mit den betroffenen Datensätzen.

## Wofür das im Fall gebraucht wird

Der Reifegrad **Daten: 2** in [`profil.md`](../profil.md) ist eine Behauptung, solange niemand sie an
Daten prüft. Diese beiden Dateien machen die Behauptung prüfbar: Sie sind die Grundlage für Stufe 3
des [`transformationsvorschlag.md`](../transformationsvorschlag.md) und für die Frage, die in
[`datenverantwortung.md`](../datenverantwortung.md) offen bleibt — wer für welchen Bestand einsteht.
Wer die Fehler gefunden hat, kann die Pflichtfelder, Wertelisten und Prüfregeln benennen, die in die
Ausschreibung Q1/2027 gehören. Das ist der eigentliche Zweck der Übung: nicht Fehler zählen, sondern
aus Fehlern Anforderungen ableiten.
