---
titel: Korrigierte Fassung beider Datensätze — was geändert wurde und warum
gehoert_zu: bewerberdatenbank-korrigiert.csv, kundendatenbank-korrigiert.csv
grundlage: AUFLOESUNG-datenqualitaet.md
datum: 2026-09-08
woche: 03
status: Zielzustand, vollständig geprüft
herkunft: generiert. Die Korrekturen folgen dem Fehlerprotokoll; ergänzte Datensätze sind neu erzeugt und als solche ausgewiesen
---

# Korrigierte Fassung beider Datensätze

> **Was diese Datei ist.** Das Änderungsprotokoll zu
> [`bewerberdatenbank-korrigiert.csv`](bewerberdatenbank-korrigiert.csv) und
> [`kundendatenbank-korrigiert.csv`](kundendatenbank-korrigiert.csv). Die fehlerhaften
> Ausgangsdateien bleiben unverändert im Verzeichnis liegen — sie sind die Übung, diese hier
> ist der Zielzustand.

## Überblick

| | fehlerhaft | korrigiert |
|---|---:|---:|
| Bewerberdatenbank | 1.284 Zeilen, 14 Spalten | **1.473 Zeilen, 16 Spalten** |
| Kundendatenbank | 1.040 Zeilen, 15 Spalten | **1.078 Zeilen, 17 Spalten** |
| Zeilen mit Befund (Prüfskript) | 6,15 % bzw. 5,48 % | **0,68 % bzw. 33,40 %** — ausschließlich Prüfung A1, siehe unten |
| Prüfungen ohne Treffer | 15 von 24 bzw. 14 von 24 | **23 von 24** in beiden Dateien |

**Die korrigierte Fassung ist keine Zeile-für-Zeile-Reparatur.** Neben den behobenen Einzelfehlern
sind Datensätze ergänzt worden, die fehlten, und Spalten, die es nie gab. Wer die Dateien
gegeneinander stellt, vergleicht deshalb nicht zwei Fassungen derselben Menge — die Nummern der
1.284 bzw. 1.034 übernommenen Datensätze sind aber stabil geblieben und in beiden Dateien
identisch adressierbar.

## Behobene Einzelfehler — Bewerberdatenbank

| Anzahl | Korrektur | Vorher |
|---:|---|---|
| 14 | E-Mail-Adresse aus dem Namen neu gebildet | fehlte oder war unbrauchbar (fehlendes @, `gmial.com`, Leerzeichen) |
| 10 | Qualifikation auf die Vorzugsbezeichnung „Staplerschein" gesetzt | zehn abweichende Schreibweisen desselben Scheins |
| 10 | Einwilligung nach dokumentiertem Wiederkontakt erneuert | Frist abgelaufen, Profil weiter aktiv geführt |
| 8 | Telefonnummer neu gesetzt | fehlte oder war unbrauchbar |
| 8 | Qualifikation aus dem Berufsfeld ergänzt | leer oder Platzhalter (`k.A.`, `siehe Lebenslauf`) |
| 6 | Letzten Kontakt auf ein Datum nach dem Eingang gesetzt | Kontakt lag vor der Bewerbung, oder Status „Im Einsatz" bei Kontakt 2023 |
| 4 | Führende Null der Postleitzahl wiederhergestellt | vierstellige Postleitzahl |
| 3 | Geburtsdatum auf einen plausiblen Wert gesetzt | fehlte oder ergab ein Alter unter 15 bzw. über 75 |
| 3 | Niederlassung auf die Vorzugsschreibweise gesetzt | `HBH`, `Heilbad Heiligenst.`, `Erfurt Zentrale` |
| 3 | Namensreihenfolge auf „Nachname, Vorname" gebracht | gedreht |
| 3 | Ort aus der Postleitzahl korrigiert | Postleitzahl und Ort passten nicht zusammen |
| 3 | Datum auf ISO-Format gebracht | `21.6.2026` statt `2026-06-21` |
| 2 | Status auf einen Wert der Werteliste gesetzt | `im pool`, `IM POOL` |
| 2 | Umlaut im Namen wiederhergestellt | Zeichensatzschaden (`Ã¤`) |
| 2 | Überzählige Leerzeichen entfernt | doppelte oder randständige Leerzeichen |

## Behobene Einzelfehler — Kundendatenbank

| Anzahl | Korrektur | Vorher |
|---:|---|---|
| 10 | Kundenstatus auf „Inaktiv" berichtigt | Status „Aktiv" bei letzter Anfrage 2021 bis 2023, oder Interessent ohne Kontakt seit 2019 |
| 7 | E-Mail-Adresse mit Bezug zum Firmennamen gesetzt | fehlte oder war eine Freemail-Adresse ohne Bezug |
| 6 | Ansprechpartner ergänzt | leer |
| 6 | Verrechnungssatz auf einen branchenüblichen Wert gesetzt | fehlte trotz Rahmenvertrag, oder war unplausibel (2,95 €) |
| 6 | Dublette entfernt, die Nummer mit einem eigenen Betrieb belegt | derselbe Betrieb zweimal, mit abweichender Rechtsformschreibweise |
| 4 | Branche auf die Vorzugsbezeichnung gesetzt | Kurzform (`Metall`, `Logistik`, `Elektro`) |
| 3 | Dezimalkomma hergestellt | Dezimalpunkt im Verrechnungssatz |
| 3 | Betreuername auf die Vorzugsschreibweise gesetzt | `MARX`, `hille`, `Steinbrück Nicole` |
| 3 | Ort aus der Postleitzahl korrigiert | Postleitzahl und Ort passten nicht zusammen |
| 3 | Führende Null der Postleitzahl wiederhergestellt | vierstellige Postleitzahl |
| 2 | Besetzungen auf die Zahl der Anfragen begrenzt | mehr Besetzungen als Anfragen |
| 2 | Datum der letzten Anfrage auf einen zulässigen Wert gesetzt | Datum in der Zukunft (2027) |
| 2 | Umlaut im Firmennamen wiederhergestellt | Zeichensatzschaden |
| 218 | fehlender Verrechnungssatz als branchenüblicher Angebotssatz ergänzt | bei Interessenten durchgängig leer |

Die letzte Zeile ist eine **Setzung, kein Fund**: ein Interessent hat noch keinen vereinbarten
Satz. Im Zielzustand steht dort der Angebotssatz, damit die Spalte durchgängig belegt ist. Wer die
Unterscheidung „vereinbart" gegen „angeboten" braucht, führt dafür eine eigene Spalte — das ist
eine Anforderung an die neue Branchensoftware, keine Datenkorrektur.

## Ergänzt, weil es fehlte

Diese acht Punkte sind die strukturellen Befunde aus [`AUFLOESUNG-datenqualitaet.md`](AUFLOESUNG-datenqualitaet.md).

| Befund | Was ergänzt wurde |
|---|---|
| **S1** Niederlassung Aschersleben fehlte in der Bewerberdatei | 150 Bewerberdatensätze in Aschersleben, Staßfurt, Bernburg und Quedlinburg, dazu 12 in Ohrdruf. Aschersleben liegt damit bei 153 Bewerbern zu 109 Kunden — eine plausible Relation. Umgekehrt 20 Kunden in Waltershausen, Ronneburg, Kahla und Dingelstädt, die bisher nur in der Bewerberdatei vorkamen |
| **S2** Lücken in der Nummerierung | 27 fehlende Bewerbernummern und 18 fehlende Kundennummern mit Datensätzen belegt. Beide Nummernfolgen sind jetzt lückenlos |
| **S3** keine Spalte für die Verfügbarkeit | neue Spalte `verfuegbar_ab`. Bei laufendem Einsatz das voraussichtliche Einsatzende, sonst das Datum, ab dem die Person zur Verfügung steht |
| **S4** keine Spalte für die Quelle der Bewerbung | neue Spalte `quelle` mit sieben Ausprägungen (Jobbörse, Anzeige Website, Multiposting-Portal, Initiativbewerbung, Empfehlung, Bundesagentur für Arbeit, Karrieremesse). Damit sind die 480.000 Euro Anzeigenbudget erstmals einer Wirkung zuzuordnen |
| **S5** kein Grund der Nichtbesetzung | neue Spalten `nicht_besetzt_2025` (Anfragen minus Besetzungen) und `hauptgrund_nichtbesetzung` mit sechs Ausprägungen. Die Zielgröße, ohne die kein Modell Besetzungswahrscheinlichkeit lernen kann, ist damit vorhanden |
| **S6** fünf Wochen ohne Bewerbungseingang | die ergänzten Datensätze tragen Eingangsdaten im Zeitraum 19.12.2025 bis 26.01.2026. Die Reihe ist geschlossen |
| **S7** keine öffentlichen Auftraggeber | 14 Kunden der Branche „Öffentlicher Auftraggeber" (Stadt- und Kreisverwaltungen, Stadtwerke, Klinikum, Zweckverband). Die Kundendatei hat jetzt zehn Branchen statt neun |
| **S8** Auszug ohne Angabe des Filters | **nicht behoben.** Die korrigierte Fassung bleibt ein Auszug von 1.473 statt 41.000 Profilen. Ein CSV kann seinen Filter nicht mitführen; das gehört in den Dateinamen, in ein Beiblatt oder in eine Spalte des Exportwerkzeugs — und ist genau deshalb hier vermerkt |

Zwei weitere Eingriffe betreffen die Zeitreihe der Kundenanfragen: 55 Inaktivkunden wurden in die
Monate August bis November 2025 eingeordnet und 9 weitere umdatiert, weil zwischen dem Aktiv- und
dem Inaktivbestand ein Loch von drei Monaten ohne einen einzigen Vorgang klaffte. Das war kein
eingebauter Fehler, sondern ein Nebeneffekt der Erzeugung — im Zielzustand hat er nichts zu suchen.

## Nachweis

```bash
python3 pruefe_datenqualitaet.py bewerberdatenbank-korrigiert.csv --stichtag 2026-09-08 \
    --vergleich kundendatenbank-korrigiert.csv

python3 pruefe_datenqualitaet.py kundendatenbank-korrigiert.csv --stichtag 2026-09-08 \
    --vergleich bewerberdatenbank-korrigiert.csv \
    --regel "besetzungen_2025<=anfragen_2025" \
    --regel "nicht_besetzt_2025>=0" \
    --regel "verrechnungssatz_std>=18"
```

Ergebnis in beiden Fällen: **23 der 24 Prüfungen ohne Treffer.** Ohne Befund sind alle
Vollständigkeits-, Konsistenz- und Genauigkeitsprüfungen, dazu A2, A3 und A4.

**Die eine verbleibende Meldung ist A1 und ist kein Fehler.**

- **Bewerberdatei, 10 Datensätze:** Bewerbungen aus den Jahren 2019 bis 2022, deren Einwilligung
  nach dokumentiertem Wiederkontakt erneuert wurde. Das Eingangsdatum bleibt alt — es ist die
  Historie des Vorgangs und nicht zu korrigieren.
- **Kundendatei, 360 Datensätze:** Kunden mit Status „Inaktiv", deren letzte Anfrage mehr als zwei
  Jahre zurückliegt. Genau das bedeutet „inaktiv". Diese Zeilen jünger zu machen wäre nicht die
  Korrektur eines Fehlers, sondern die Erfindung von Vorgängen.

A1 misst das Alter von Daten, nicht ihre Richtigkeit. Die Meldung ist **zu lesen und zu bewerten**,
nicht wegzuarbeiten — und sie ist ein gutes Beispiel dafür, warum am Ende jedes Prüfberichts eine
Rolle stehen muss, die entscheidet, und nicht nur eine Zahl.

## Was die korrigierte Fassung nicht ist

- **Kein realer Datenbestand.** Alles ist erfunden, auch die 189 bzw. 38 ergänzten Datensätze.
  Für ein Deliverable außerhalb dieses Kurses ist keine Zeile verwendbar.
- **Kein Beweis, dass die Daten stimmen.** Geprüft ist, dass sie *formal* stimmen: vollständig,
  widerspruchsfrei, im plausiblen Bereich. Ob der Verrechnungssatz eines Kunden der vereinbarte
  ist, kann kein Skript feststellen — das ist der Unterschied zwischen Datenqualität und
  Datenrichtigkeit, und die zweite braucht einen Menschen mit Zuständigkeit.
- **Kein Ersatz für Regeln im System.** Was hier von Hand korrigiert wurde, entsteht morgen wieder,
  solange die Erfassung es zulässt. Die Liste oben ist deshalb zugleich eine Liste von
  Pflichtfeldern, Wertelisten und Prüfregeln für die Ausschreibung im ersten Quartal 2027 — siehe
  [`ANLEITUNG-regeln.md`](ANLEITUNG-regeln.md), Abschnitt „Der eigentliche Zweck".
