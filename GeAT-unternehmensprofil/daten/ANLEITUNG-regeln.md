---
titel: Fachliche Regeln anwenden — die Option --regel
gehoert_zu: pruefe_datenqualitaet.py
datum: 2026-09-08
woche: 03
status: Anleitung
herkunft: Syntax und Verhalten am Skript geprüft; die Ergebniszahlen stammen aus einem Lauf gegen die beiden Übungsdateien mit Stichtag 2026-09-08
---

# Fachliche Regeln anwenden

> **Was diese Datei ist.** Eine Anleitung zur Option `--regel` von
> [`pruefe_datenqualitaet.py`](pruefe_datenqualitaet.py): Syntax, ein geprüfter Regelkatalog für
> beide Übungsdateien, ein Rezept für eigene Regeln und die Fallen. Was die übrigen Prüfungen
> bedeuten, steht in [`ERLAEUTERUNG-pruefungen-und-rag.md`](ERLAEUTERUNG-pruefungen-und-rag.md).

## Warum es diese Option gibt

Alle anderen Prüfungen des Skripts kommen ohne Fachwissen aus. Sie erkennen, was leer ist, was
doppelt ist, was unterschiedlich geschrieben ist, was aus dem Wertebereich fällt — alles Fragen, die
sich aus der Datei selbst beantworten lassen.

Ob 15 Besetzungen bei 13 Anfragen möglich sind, steht dagegen in keiner Spalte. Das weiß nur, wer
das Geschäft kennt. `--regel` ist die Stelle, an der dieses Wissen in eine prüfbare Form kommt: eine
Behauptung über jede einzelne Zeile, die das Skript nachrechnet, statt sie zu glauben.

Der Befund erscheint als `K7.n` in der Dimension **Konsistenz** — ein Widerspruch zwischen zwei
Feldern desselben Datensatzes.

## Syntax

```bash
python3 pruefe_datenqualitaet.py kundendatenbank.csv --regel "besetzungen_2025<=anfragen_2025"
```

| Bestandteil | Regel |
|---|---|
| Linke und rechte Seite | ein Spaltenname **oder** eine feste Zahl. Beide Seiten dürfen Spalten sein |
| Vergleich | `<=` `>=` `<` `>` `==` `!=` — sonst bricht das Skript mit einer Meldung ab |
| Werte | werden als Zahl gelesen, Komma und Punkt als Dezimaltrennzeichen sind beide erlaubt |
| Mehrfachnutzung | `--regel` beliebig oft angeben; jede Regel wird ein eigener Befund `K7.1`, `K7.2`, … |
| Anführungszeichen | **Pflicht.** Ohne sie deutet die Shell `<` und `>` als Umleitung und legt eine Datei namens `anfragen_2025` an |
| Leerzeichen | erlaubt: `"besetzungen_2025 <= anfragen_2025"` funktioniert genauso |

Zeilen, in denen eine der beiden Seiten leer ist oder keine Zahl enthält, werden **übersprungen** und
nicht als Verstoß gezählt. Das ist beabsichtigt — ein Interessent ohne Verrechnungssatz verstößt
gegen keine Regel, ihm fehlt ein Wert, und dafür ist Prüfung `V1` da.

## So liest sich das Ergebnis

```
!!  [K7.1] Fachliche Regel `besetzungen_2025<=anfragen_2025`
      Prüfung : vorgegebene Regel, zeilenweise geprüft
      Treffer : 2 von 1040 Datensätze
      Zeilen  : 2 betroffene Datensätze (0,19 % der Datei)
      · KD-0295 (Z296): besetzungen_2025 = 8, anfragen_2025 = 7
      · KD-0380 (Z381): besetzungen_2025 = 15, anfragen_2025 = 13
```

`KD-0295` ist die Kundennummer, `Z296` die Zeile in der CSV-Datei — damit findet man den Datensatz
im Editor wieder, ohne zu suchen.

## Regelkatalog Kundendatenbank

Alle Zeilen sind am Bestand vom 8. September 2026 durchgerechnet.

| Regel | Behauptung | Ergebnis |
|---|---|---:|
| `besetzungen_2025<=anfragen_2025` | Niemand besetzt mehr Stellen, als angefragt wurden | **2 Verstöße** |
| `verrechnungssatz_std>=18` | Kein Verrechnungssatz unter 18 Euro je Stunde — darunter wäre nicht einmal der Personalaufwand gedeckt | **2 Verstöße** |
| `verrechnungssatz_std<=60` | Kein Satz über 60 Euro; darüber liegt kein gewerblicher Einsatz mehr | 0 |
| `anfragen_2025>=0` | Keine negativen Zählwerte | 0 |
| `besetzungen_2025>=0` | Keine negativen Zählwerte | 0 |

Die erste Regel ist die wichtigste, weil aus diesen zwei Spalten die Besetzungsquote entsteht — die
Kennzahl, die im Fall von 48 auf 40 Prozent gefallen ist. Eine Zeile mit mehr Besetzungen als
Anfragen ergibt eine Quote über 100 Prozent und hebt die Gesamtquote an, ohne aufzufallen.

Die zweite Regel ist ein Beispiel für eine Grenze, die man setzen **muss**, weil die Daten sie nicht
hergeben: Prüfung `G1` leitet ihre Grenzen aus der Verteilung ab und findet deshalb nur, was weit
außen liegt. Wo genau die fachliche Untergrenze liegt, ist eine Entscheidung, keine Rechnung.

Als Kopiervorlage:

```bash
python3 pruefe_datenqualitaet.py kundendatenbank.csv --stichtag 2026-09-08 \
    --regel "besetzungen_2025<=anfragen_2025" \
    --regel "verrechnungssatz_std>=18" \
    --regel "verrechnungssatz_std<=60" \
    --regel "anfragen_2025>=0"
```

## Regelkatalog Bewerberdatenbank

**Hier greift `--regel` fast nicht — und das ist ein Befund, kein Mangel der Option.** Die Datei
enthält keine zwei Zählgrößen, die sich zueinander verhalten müssten. Die naheliegenden Regeln des
Bestands sind Reihenfolgen von Datumsfeldern:

- `letzter_kontakt` darf nicht vor `eingang_datum` liegen
- `einwilligung_bis` muss nach `eingang_datum` liegen
- `geburtsdatum` muss vor `eingang_datum` liegen

Diese Vergleiche kann `--regel` **nicht** ausdrücken, weil es nur numerisch vergleicht. Die erste
davon deckt die feste Prüfung `A1`/`A3`-Umgebung teilweise ab; vollständig geprüft wird sie derzeit
nicht. Das ist die deutlichste Lücke der Option.

Was in der Bewerberdatei stattdessen trägt, sind die festen Prüfungen: `A3` für abgelaufene
Einwilligungen, `G5` für unplausible Geburtsdaten, `G2` für Postleitzahlen, `K4` für die
Schreibvarianten der Qualifikationen.

## Eine eigene Regel in vier Schritten

1. **Behauptung als Satz formulieren.** „In keiner Zeile kann die Zahl der Besetzungen größer sein
   als die Zahl der Anfragen." Wer den Satz nicht sauber sagen kann, hat keine Regel, sondern ein
   Gefühl.
2. **Die zwei beteiligten Felder benennen.** Beide müssen Größen sein, die man sinnvoll vergleichen
   kann — keine Kennungen (siehe die Falle unten).
3. **In den Ausdruck übersetzen** und ausführen.
4. **Gegenprobe machen.** Die Regel umdrehen und erneut laufen lassen:
   `--regel "anfragen_2025>=besetzungen_2025"` muss dieselben zwei Zeilen liefern. Tut sie das nicht,
   stimmt etwas mit dem Spaltennamen oder dem Datentyp nicht.

## Zwei Fallen

**Falle 1: Ein Tippfehler im Spaltennamen sieht wie ein bestandener Test aus.** Wer sich verschreibt,
bekommt:

```
OK  [K7.1] Fachliche Regel `besetzungen_2025<=anfrage_2025`
      Treffer : 0 von 1040 Datensätze
```

Null Treffer, Häkchen, alles gut — und geprüft wurde nichts. Das Skript liest die unbekannte Seite
als Zahl, bekommt keine, überspringt jede Zeile. **Deshalb ist die Gegenprobe aus Schritt 4 nicht
optional.** Zwei Regeln, die sich widersprechen und beide null Treffer melden, sind der sichere
Hinweis darauf, dass gar nicht gerechnet wurde.

**Falle 2: Eine Regel kann laufen, richtig zählen und trotzdem falsch sein.** Beispiel:

```
!!  [K7.1] Fachliche Regel `plz>=10000`
      Treffer : 451 von 1284 Datensätze (35,12 %)
```

Der Gedanke war, die vierstelligen Postleitzahlen mit verlorener führender Null zu finden. Gefunden
wurden 451 Zeilen — darunter jede korrekte Postleitzahl aus Gera, Jena und Saalfeld, die in
Thüringen mit `07` beginnt. Eine Postleitzahl ist keine Zahl, sondern eine Kennung; sie ist nicht
größer oder kleiner, sie ist gleich oder verschieden. Für diesen Zweck ist `G2` zuständig, die auf
die Länge prüft und vier Treffer meldet.

**Die Lehre:** `--regel` gehört auf Größen — Mengen, Beträge, Zeiten. Nicht auf Postleitzahlen,
Telefonnummern, Kunden- oder Bewerbernummern.

## Was `--regel` nicht kann

| Gewünscht | Warum nicht | Was stattdessen greift |
|---|---|---|
| Datumsvergleiche (`letzter_kontakt>=eingang_datum`) | die Option vergleicht nur Zahlen | `A1`, `A2`, `A3` prüfen Alter, Zukunft und Fristen — die Reihenfolge zweier Datumsfelder derzeit nicht |
| Textvergleiche (`status=="Im Pool"`) | keine Textwerte | `K3` findet Schreibvarianten, `V1` leere Felder |
| Bedingte Regeln („wenn Rahmenvertrag `Ja`, dann Verrechnungssatz gepflegt") | keine Wenn-dann-Logik | im Bericht als Kombination von `V1` und der Spalte `rahmenvertrag` von Hand zu lesen |
| Summenregeln („Summe der Anfragen ergibt 3.100") | Regeln gelten zeilenweise, nicht über die Datei | eigene Auswertung; das Skript prüft keine Aggregate |

Die erste Zeile ist die, die am meisten fehlt. Wenn du willst, erweitere ich `--regel` so, dass sie
auch Datumsfelder vergleicht — der Eingriff ist klein, weil die Datumserkennung schon existiert.

## Der eigentliche Zweck: aus der Prüfregel wird eine Systemregel

Eine Regel, die am Bestand hält, ist mehr als ein Prüfergebnis. Sie ist eine **Anforderung an das
System**, das die Daten erfasst — und damit gehört sie in die Ausschreibung der neuen
Branchensoftware im ersten Quartal 2027, nicht in ein Skript, das jemand gelegentlich laufen lässt.
Drei Schritte, in dieser Reihenfolge:

1. **Regel formulieren und am Bestand prüfen** — hier, mit `--regel`.
2. **Regel als Validierung fordern.** Was heute ein Bericht meldet, muss das System morgen bei der
   Eingabe verhindern. Eine Besetzung, die es ohne Anfrage nicht geben kann, darf gar nicht
   erfassbar sein.
3. **Regel einer Rolle zuordnen.** Jede Regel braucht jemanden, der über Ausnahmen entscheidet.
   Wer das ist, steht in [`datenverantwortung.md`](../datenverantwortung.md), Abschnitt 5 — für
   Anfragen und Besetzungen die Leiterin Controlling, für Verrechnungssätze die Vertriebsleitung.

Eine Regel ohne zuständige Rolle wird beim ersten unbequemen Treffer stillgelegt. Das ist der Grund,
warum dieser Abschnitt zur Anleitung gehört und nicht zum Anhang.

## Grenzen und Gegenargumente

- **Ein Verstoß sagt nicht, welches Feld falsch ist.** Bei `KD-0380` kann die 15 zu hoch oder die 13
  zu niedrig sein. Das Skript zeigt den Widerspruch, die Klärung bleibt fachlich.
- **Zu viele Regeln erzeugen Alarmmüdigkeit.** Fünf Regeln, die jemand liest, sind mehr wert als
  dreißig, die niemand mehr ansieht. Bei GeAT reichen für den Anfang die vier aus dem Katalog oben.
- **Eine Regel prüft die Vergangenheit, nicht die Ursache.** Warum `KD-0380` widersprüchlich ist —
  Nachbuchung, Korrektur, Zahlendreher — steht nicht in der Datei, sondern nur in der Erinnerung der
  Person, die es erfasst hat. Deshalb ist die Klärung mit Abstand teurer als die Prüfung, und
  deshalb lohnt Schritt 2 oben mehr als jeder weitere Bericht.
