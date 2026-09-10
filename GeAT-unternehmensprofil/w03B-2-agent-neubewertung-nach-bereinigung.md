---
artefakt: Neubewertung des Agent-Konzepts nach der Datenbereinigung
woche: 03
datum: 2026-09-10
status: Entwurf. Ersetzt die Begründung in w03B-1-agent-konzept-bestandswaechter.md, nicht das Konzept selbst. Nicht beschlossen
zweck: messen, welcher Agent auf den bereinigten Beständen noch begründbar ist, und den Engpass benennen, den die Bereinigung erst sichtbar gemacht hat
bezug: GeAT-unternehmensprofil/w03B-1-agent-konzept-bestandswaechter.md
grundlage: GeAT-unternehmensprofil/daten/bewerberdatenbank-korrigiert.csv und kundendatenbank-korrigiert.csv, geprüft mit pruefe_datenqualitaet.py, Stichtag 2026-09-10
herkunft: eigene Messung auf generierten Übungsdaten. Die Werte sind reproduzierbar (Abschnitt 9). Die Schlussfolgerung gilt für diese Dateien und ist für ein reales System nicht belegt. Aufwände sind gekennzeichnete Schätzungen, keine Angebote
kette: W03 B · Agent auf den bereinigten Bestaenden — Glied 2 von 2
baut_auf: w03B-1-agent-konzept-bestandswaechter.md
basis_fuer: offen — naechstes Glied waere die zweite Pruefmessung in vier Wochen
---

# Neubewertung: welcher Agent bleibt übrig, wenn die Daten sauber sind

> **Anlass.** Die korrigierten Fassungen beider Bestände sind fertig und bestehen 23 von 24
> Prüfungen. Damit ist die Voraussetzung eingetreten, unter der
> [`w03B-1-agent-konzept-bestandswaechter.md`](#GeAT-unternehmensprofil/w03B-1-agent-konzept-bestandswaechter.md)
> den Bestandswächter empfohlen hat. Dieses Dokument prüft, ob die Empfehlung diese Voraussetzung
> überlebt.

## Die Antwort vorweg

**Sie überlebt sie nicht in der vorliegenden Form.** Fünf der sechs Regeln des Bestandswächters
finden auf dem bereinigten Bestand null Fälle. Der Bestandswächter war eine Dauerlösung für ein
Einmalproblem — und das Einmalproblem ist gelöst.

**Was bleibt, ist ein kleinerer Agent: der Fristenwächter.** Zwei Regeln statt sechs, weil nur
Fristen weiterlaufen, egal wie sauber ein Bestand ist.

**Und der Befund, der wichtiger ist als der Agent:** Die Bereinigung hat den Engpass verschoben —
von der Datenqualität auf das Datenmodell. 437 von 1.473 Bewerberprofilen tragen einen
nachweispflichtigen Schein. Für keinen einzigen existiert ein Gültigkeitsdatum. Eine fehlende
Spalte lässt sich nicht putzen, und genau sie trägt das größte Risiko.

**Empfehlung: der Agent ist nicht der nächste Schritt.** Die nächsten Schritte sind das fehlende
Feld und eine zweite Messung. Beides zusammen unter vier Personentagen.

## 1. Die Messung

`Fakt`, gemessen am 2026-09-10 mit dem Prüfskript und den sechs Regeln aus Abschnitt 2 des
Konzepts. Reproduktion in Abschnitt 9.

| Regel des Bestandswächters | Ausgangsbestand | Zielzustand |
|---|---:|---:|
| R1 Einwilligung abgelaufen | 10 | **0** |
| R1 Einwilligung läuft in ≤ 60 Tagen ab | 40 | 41 |
| R2 Qualifikationsnachweis läuft ab | nicht messbar | **nicht messbar** |
| R3 Rahmenvertrag „Ja" ohne Verrechnungssatz | 4 | **0** |
| R3 Verrechnungssatz unter 18,00 € | 2 | **0** |
| R4 unscharfe Dubletten | Treffer (6 entfernt) | **0** |
| R5 Status „Aktiv" ohne Vorgang > 12 Monate | 8 | **0** |
| R6 Nichtbesetzung ohne eingetragenen Grund | Spalte existierte nicht | **0** |

Mengengerüst: Ausgangsbestand 1.284 Bewerber / 1.040 Kunden, Zielzustand 1.473 / 1.078.

**Befundquote des Prüfskripts:** 6,15 % bzw. 5,48 % im Ausgangsbestand, **0,68 % bzw. 33,40 %** im
Zielzustand. Die 33,40 % sind kein Rückschritt: sie stammen ausschließlich aus Prüfung A1
(Aktualität) und zerfallen so —

| A1-Treffer Kundenbestand | Anzahl | Bewertung |
|---|---:|---|
| Status „Inaktiv", kein Kontakt > 24 Monate | 305 | fachlich richtig, kein Fehler |
| Status „Interessent", kein Kontakt > 24 Monate | 55 | Kandidat für Bereinigung, kein Widerspruch |
| Status „Aktiv", kein Vorgang > 12 Monate | **0** | der einzige echte Widerspruch — tritt nicht auf |
| Summe | 360 von 1.078 | |

**Regel 6 ist vollständig gepflegt.** 510 Kunden hatten 2025 Anfragen, 461 davon Nichtbesetzungen,
und alle 461 tragen einen Grund aus der Werteliste:

| Anzahl | Hauptgrund der Nichtbesetzung |
|---:|---|
| 185 | kein passender Kandidat verfügbar |
| 90 | Preis abgelehnt |
| 69 | Kunde hat selbst besetzt |
| 45 | Termin zu kurzfristig |
| 42 | Anforderung unklar |
| 30 | Anfrage zurückgezogen |

## 2. Was die Messung mit dem Konzept macht

`abgeleitet`.

Dass fünf Regeln null finden, ist keine Panne. Die korrigierte Fassung wurde gegen dieselben
Prüfungen gebaut, aus denen die Regeln abgeleitet sind — sie *muss* bestehen. Genau deshalb ist der
Schluss belastbar und nicht trivial:

**Die Regeln R3, R4, R5 und R6 beschreiben Zustände, nicht Vorgänge.** Ein fehlender
Verrechnungssatz, eine Dublette, ein widersprüchlicher Status, ein leeres Pflichtfeld — jeder
dieser Fälle entsteht einmal und ist danach behoben. Ein Agent, der sie wöchentlich sucht, sucht
nach dem ersten Lauf nichts mehr.

**Nur R1 und R2 beschreiben Vorgänge.** Fristen laufen weiter. Ein Bestand, der heute vollständig
ist, hat in 60 Tagen 41 abgelaufene Einwilligungen — unabhängig davon, wie gut gepflegt er ist.
Das ist der einzige Teil des Konzepts, der eine Dauerlösung rechtfertigt.

Das Konzept hat diesen Unterschied nicht gemacht, weil es auf dem fehlerhaften Bestand
argumentiert hat. Dort sahen alle sechs Regeln gleich aus.

## 3. Der Agent, der übrig bleibt: der Fristenwächter

| | Bestandswächter (Konzept) | Fristenwächter (dieser Vorschlag) |
|---|---|---|
| Regeln | 6 | 2 (R1, R2) |
| Fallvolumen | einmalig hoch, dann null | dauerhaft ~41 je 60 Tage aus R1 |
| Zweck | Datenqualität herstellen | Fristen überwachen, die niemand überwacht |
| Baubar heute | ja | **R1 ja, R2 nein** — siehe Abschnitt 4 |

Alles andere aus dem Konzept bleibt unverändert gültig und wird hier nicht wiederholt: die vier
Nicht-Ziele, der Weg über den Export statt über eine API, die Plattformwahl, der Rechtsrahmen und
das Abbruchkriterium. Sie stehen in
[`w03B-1-agent-konzept-bestandswaechter.md`](#GeAT-unternehmensprofil/w03B-1-agent-konzept-bestandswaechter.md),
Abschnitte 2, 5, 9 und 6.

## 4. Der Engpass, der neu ist: das Datenmodell

`Fakt`: 437 der 1.473 Bewerberprofile nennen im Freitextfeld `qualifikation` einen
nachweispflichtigen Schein — Schweißerprüfung, Staplerschein, Führerschein, Kranschein,
Ladungssicherung, G25/G41, Gesundheitsnachweis.

`Fakt`: Weder `bewerberdatenbank-korrigiert.csv` (16 Spalten) noch
`kundendatenbank-korrigiert.csv` (17 Spalten) enthält ein Feld für die Gültigkeit dieser Nachweise.
Das Konzept selbst schreibt zu R2, dieser Bestand werde „telefonisch erfragt".

**Damit ist R2 die Regel mit dem höchsten Schaden und der einzigen unbehebbaren Datenlücke.** Ein
Einsatz mit abgelaufenem G25 oder abgelaufenem Staplerschein ist ein Haftungsfall, kein
Pflegemangel. Die Bereinigung hat daran nichts geändert und konnte es nicht: sie korrigiert Werte,
sie erfindet keine Spalten.

**Konsequenz für die Ausschreibung Q1/2027:** `nachweis_art` und `nachweis_gueltig_bis` gehören als
Pflichtfelder ins Lastenheft. Ohne sie kauft GeAT dieselbe Lücke neu ein — und der Fristenwächter
bleibt dauerhaft halb.

## 5. Warum der Agent trotzdem nicht der nächste Schritt ist

41 rollierende Fälle sind ein Cronjob mit Serienmail. `Schätzung`: zwei Personentage. Das trägt die
12 bis 18 Personentage aus Abschnitt 6 des Konzepts nicht.

Was sie trägt, sind die zwei Funktionen, die das Konzept selbst als Rechtfertigung benennt:
Rückfrage in Sprache und Ausnahmeprotokoll. Beide brauchen Fallvolumen. **Auf 41 Fällen je 60 Tage
entsteht kein Ausnahmenkatalog**, und die Rückfragen bleiben so selten, dass die betroffene Rolle
sie selbst beantwortet.

Der Satz aus Abschnitt 4 des Konzepts gilt damit gegen das Konzept: *„Wenn diese vier Punkte nicht
überzeugen, ist die richtige Entscheidung: Skript behalten, Agent lassen."*

## 6. Vorschlag: drei Schritte in dieser Reihenfolge

### Schritt 1 · Die fehlende Spalte, nicht der Agent

**Jetzt. `Schätzung` 3 Personentage, davon der größere Teil Erhebung, nicht IT.**

Zwei Felder anlegen (`nachweis_art`, `nachweis_gueltig_bis`) und für die 437 betroffenen Profile
erheben. Das ist Handarbeit und die einzige Handarbeit, die sich in diesem Vorhaben lohnt: sie
erzeugt eine Zielgröße, die heute nicht existiert. Parallel als Pflichtfeld ins Lastenheft.

**Träger:** nach [`raci-datenpflege.md`](#GeAT-unternehmensprofil/raci-datenpflege.md) accountable
Rolle 3, ausführend die Niederlassungen.

### Schritt 2 · Nullmessung protokollieren, bevor der Bestand wieder verfällt

**Jetzt. `Schätzung` 0,5 Personentage.**

Das Prüfskript mit `--json` gegen beide korrigierten Dateien laufen lassen und den Bericht mit
Datum ablegen. Das ist der Startwert, der beim Modul 2023 gefehlt hat. In vier Wochen dieselbe
Messung.

> **Die Verfallsrate zwischen den beiden Messungen ist die Zahl, die über den Agenten entscheidet.**
> Verfällt der Bestand messbar, trägt der Fristenwächter. Verfällt er nicht, war die Bereinigung
> die Lösung und der Agent ist überflüssig.

Zwei Messungen, ein Monat, ein halber Tag — die billigste belastbare Entscheidungsgrundlage im
ganzen Vorhaben. Sie ersetzt eine Diskussion, die sonst im Steuerkreis ohne Zahlen geführt wird.

### Schritt 3 · Erst dann der Agent, und dann als Fristenwächter

**Frühestens in vier bis sechs Wochen, abhängig von Schritt 2.**

Zwei Regeln, gegen die gemessene Verfallsrate gerechnet. Messgrößen und Abbruchkriterium wie in
Abschnitt 6 des Konzepts, mit einem korrigierten Startwert: nicht 18.000 überfällige Profile,
sondern 0 überfällige und 41 in Frist.

## 7. Was zusätzlich auf die Nein-Liste gehört

Das Konzept lehnt in Abschnitt 8 drei Vorhaben ab — Assistent für alle 69, Findewerkzeug in
Eigenbau, Matching auf Erfolgswahrscheinlichkeit. Diese Ablehnungen bleiben unverändert richtig.

**Neu hinzu: der Bestandswächter mit sechs Regeln.** Auf dem bereinigten Bestand ist er nicht mehr
begründbar. Er wäre ein Werkzeug, das wöchentlich läuft und wöchentlich nichts findet — und damit
das vierte Werkzeug in vier Jahren, das niemand benutzt, diesmal aus dem umgekehrten Grund.

## 8. Gegenargumente gegen diese Neubewertung

1. **Die korrigierte Fassung ist ein konstruierter Zielzustand.** Dass sie 23 von 24 Prüfungen
   besteht, ist ein Befund über ihre Konstruktion, nicht über GeAT. Der Schluss „der Agent hat
   nichts zu tun" gilt für diese Dateien und ist für ein reales Führungssystem **nicht belegt**.
   Das ist der ernsteste Einwand gegen dieses Dokument.
2. **Eine Verfallsrate lässt sich an einer statischen CSV nicht messen.** Es gibt keine zweite
   Zeitscheibe. Schritt 2 setzt voraus, dass ein zweiter Export entsteht — im Fall eine
   `Annahme`, und sie hängt an offener Frage 2 des Konzepts.
3. **Die Hochrechnung ist eine Rechnung, keine Messung.** 41 Fälle je 60 Tage ergeben rund 250 im
   Jahr nur unter der Annahme gleichmäßig verteilter Einwilligungsdaten. Bei 1.473 generierten
   Profilen mit synthetischem Eingangsdatum ist diese Annahme plausibel und im Realbestand
   unbelegt.
4. **Der Interessenkonflikt bleibt, er dreht sich nur.** Abschnitt 10 Punkt 4 des Konzepts hält
   fest, dass Rolle 15 einen Agenten empfiehlt, für den Rolle 15 gebraucht wird. Hier empfiehlt
   dieselbe Rolle weniger Agent und mehr Datenmodellarbeit — was den eigenen Wirkungskreis
   ebenfalls beschreibt, nur anders.
5. **R2 könnte außerhalb der beiden Dateien geführt werden.** Die Aussage „kein Gültigkeitsdatum
   vorhanden" gilt geprüft für die beiden CSV-Bestände. Ob im Führungssystem ein solches Feld
   existiert, das nur nicht exportiert wird, ist offene Frage 2 unten.

## 9. Reproduktion der Messung

```
cd GeAT-unternehmensprofil/daten
python pruefe_datenqualitaet.py bewerberdatenbank-korrigiert.csv --stichtag 2026-09-10
python pruefe_datenqualitaet.py kundendatenbank-korrigiert.csv  --stichtag 2026-09-10
```

Die Regelwerte aus Abschnitt 1 entstehen mit `--regel`, siehe
[`ANLEITUNG-regeln.md`](#GeAT-unternehmensprofil/daten/ANLEITUNG-regeln.md); R1, R2 und R5 wurden
zusätzlich per Auszählung über die Datumsspalten gegen denselben Stichtag geprüft.

## 10. Offene Punkte

| # | Frage | Wer | Warum sie zählt |
|---:|---|---|---|
| 1 | Wird Schritt 2 beauftragt, bevor über den Agenten entschieden wird? | Geschäftsführung | Ohne die zweite Messung ist jede Agentenentscheidung eine Meinung. Terminkritisch, weil der Startwert mit jedem Tag ungültiger wird |
| 2 | Führt das Führungssystem Gültigkeitsdaten für Qualifikationsnachweise, die nur nicht exportiert werden? | Rolle 12 | Entscheidet, ob Schritt 1 eine Erhebung oder nur eine Exporterweiterung ist — Faktor 3 im Aufwand |
| 3 | Sind `nachweis_art` und `nachweis_gueltig_bis` noch im Lastenheft unterbringbar? | Rolle 2 | Dieselbe Terminfrage wie offene Frage 1 des Konzepts |
| 4 | Wer trägt die 55 Interessenten ohne Kontakt seit über 24 Monaten aus? | Rolle 3 | Der einzige Bereinigungsrest, der noch offen ist — und er braucht keinen Agenten |
| 5 | Bleibt das Abbruchkriterium bei „vier von sieben Standorten", wenn der Agent nur zwei Regeln hat? | Geschäftsführung | Bei 41 Fällen je 60 Tage verteilt sich die Arbeit anders als bei 400 |

## Änderungsvermerk

| Datum | Was |
|---|---|
| 2026-09-10 | angelegt. Messung gegen beide korrigierten Bestände, Neubewertung des Agent-Konzepts vom 2026-09-08 |
