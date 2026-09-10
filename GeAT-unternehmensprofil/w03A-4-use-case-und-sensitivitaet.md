---
artefakt: Prüfung der Plattformentscheidung — Use Case aus dem Datenbestand und Sensitivitätsprobe
kette: W03 A · KI-Analyse — Glied 4 von 6
baut_auf: w03A-3-ki-analyse-fassung-2-gueltig.md (Gewichtung und Scores, unverändert übernommen)
basis_fuer: w03A-5-entscheidungsvorlage.md (Handlungsempfehlung) · w03A-6-pitch-c-level.md (Sprechfassung)
woche: 03
datum: 2026-09-10
status: Prüfergebnis. Die Matrix vom Montag wird nicht ersetzt, sondern geprüft. Keine Gewichtsänderung
zweck: die zwei Schritte nachziehen, die in der Analyse fehlten — ein Use Case, der aus dem Datenbestand und nicht aus dem Sieger abgeleitet ist, und die Sensitivitätsprobe
bezug: w03A-1-ki-analyse-fassung-1.md, w03A-2-ki-analyse-review.md, w03C-1-plattformkriterien-kennzahlen-stakeholder.md, daten/
aufbau: je Abschnitt zuerst eine kurze Zusammenfassung, dann die ausführliche Fassung, dann Belege und Quellen
herkunft: Die Sensitivitätsrechnung ist arithmetisch aus den Scores der Fassung 2 abgeleitet und reproduzierbar (Abschnitt 5). Der Use Case ist aus dem Datenbestand abgeleitet, jede Zahl mit Kurzzitat
---

# Prüfung der Plattformentscheidung

> **Was dieses Dokument ist.** Der Prüfauftrag lautet: *keine zweite Matrix bauen, die erste prüfen.*
> Genau das steht hier. **Kein Gewicht ist geändert**, kein Score ist angefasst. Ergänzt sind die
> zwei Schritte, die in der Analyse fehlten: ein Use Case, der **vor** dem Blick auf den Sieger
> geschrieben ist, und die Sensitivitätsprobe.
>
> **Aufbau jedes Abschnitts:** *Kurz* — *Ausführlich* — *Belege und Quellen.*

---

## 1 · Die Antwort auf den Prüfauftrag

**Kurz.** Die Plattformwahl vom Montag hält. Beide Sieger sind gegen Gewichtsverschiebungen
robuster als erwartet — und genau das ist der eigentliche Befund: **die Gewichtung entscheidet
hier fast nichts.** Der Sieger steht schon durch die Scores fest.

**Ausführlich.**

| Prüfschritt | Ergebnis |
|---|---|
| Use Case aus dem Datenbestand geschrieben | steht in Abschnitt 2 — und er schließt zwei der fünf Optionen aus, bevor gerechnet wird |
| Plattformauswahl daran geprüft | **hält.** Option A für Stufe 1, Option F für Stufe 4 |
| Score nachgerechnet | **stimmt.** 3,49 / 3,09 / 1,78 / 2,32 / 2,32 in Matrix A, 3,56 für F in Matrix B |
| Sensitivität | Sieger hält in **allen 30** geprüften Varianten. Kippschwellen in Abschnitt 4 |
| Finale Empfehlung | unverändert gegenüber Fassung 2 — aber jetzt mit einem Satz begründet, der nicht der Score ist |

> **Die finale Empfehlung in einem Satz:** *Stufe 1 auf der EU-Plattform mit 20 Seats, weil sie das
> einzige Kriterium gewinnt, das eine Zutrittsbedingung ist — und Stufe 4 als regelbasierter Filter,
> weil unser Datenbestand die Voraussetzung für alles andere nicht hergibt.*

**Belege und Quellen.** Alle Scores unverändert aus
[`w03A-3-ki-analyse-fassung-2-gueltig.md`](w03A-3-ki-analyse-fassung-2-gueltig.md), Matrix A
(Abschnitt 5) und Matrix B (Abschnitt 7). Die Nachrechnung ist in Abschnitt 5 dieses Dokuments
reproduzierbar.

---

## 2 · Der Use Case — aus dem Datenbestand, nicht aus dem Sieger

**Kurz.** Der Use Case ist **vor** dem Blick in die Matrix geschrieben und ausschließlich aus dem
Datenbestand abgeleitet. Das ist die Reihenfolge, die die Methode verlangt: wer den Use Case im
Wissen um den Gewinner schreibt, schreibt einen, den der Gewinner erfüllt.

**Ausführlich.**

### Was die Plattform mit unserem Datenbestand leisten soll

> **In einem Satz:** Aus 41.000 Bewerberprofilen, von denen 63 Prozent kein strukturiertes Können
> enthalten, soll die Plattform **auf strukturierten Feldern** eine nachvollziehbare Vorauswahl
> vorbereiten und deren Begründung formulieren — ohne Personen zu ranken und ohne
> Lebenslauf-Volltexte in den Modellkontext zu nehmen.

Drei Leistungen, absteigend nach Machbarkeit auf dem heutigen Bestand:

| # | Leistung | Voraussetzung im Bestand | Heute erfüllt? |
|---:|---|---|---|
| **1** | **Formulieren** — Anzeigentexte, Profilzusammenfassungen für die Kundenunterlage | ein Mensch fügt den Text selbst ein. Keine Systemanbindung | **ja** — deshalb ist Stufe 1 sofort möglich |
| **2** | **Filtern auf Feldern** — Kandidaten finden, die eine Anforderung nachweislich erfüllen (Berufsfeld, Schein, Verfügbarkeit, Niederlassung) | strukturierte Pflichtfelder, Qualifikationskatalog mit einer Schreibweise, Gültigkeitsdatum bei Nachweisen | **nein** — 63 % ohne strukturiertes Können, kein Gültigkeitsdatum für Nachweise |
| **3** | **Suchen im Volltext** — Lebenslauf-PDFs durchsuchbar machen | Texterkennung, Textindex, offene Schnittstelle | **nein** — keines der drei vorhanden |

### Was der Use Case ausschließt, bevor gerechnet wird

Das ist der Teil, der die Prüfung überhaupt zu einer Prüfung macht:

1. **Keine Rangfolge von Personen nach Erfolgsprognose.** Die Zielgröße dafür existiert erst seit
   der Spalte `hauptgrund_nichtbesetzung` und hat keine Historie. Ein Modell auf vergangenen
   Besetzungen sortiert die Gruppen aus, die 28,8 bzw. 20,4 Prozent des Marktes ausmachen.
2. **Kein RAG über den Bewerberbestand.** Leistung 3 hat keine Voraussetzung. Wer sie jetzt kauft,
   bezahlt eine Funktion, deren Grundlage 12 bis 18 Monate entfernt ist.
3. **Keine tiefe Integration in das heutige Kernsystem.** Es wird in Q1/2027 ersetzt.

**Damit fallen zwei der fünf Optionen aus dem Use Case, unabhängig von jedem Score:** Option C
(Eigenbau) verlangt Kapazität, die es nicht gibt, und Option B (Copilot) erreicht den relevanten
Bestand nicht, weil die 41.000 Profile nicht in M365 liegen.

> **Der Prüfsatz, der daraus folgt:** Der Use Case und die Matrix kommen unabhängig voneinander zum
> selben Ausschluss. Das ist der stärkste Hinweis darauf, dass die Auswahl vom Montag trägt — und
> er ist stärker als der Score, weil er nicht von Gewichten abhängt.

**Belege und Quellen.**

| Aussage | Güte | Kurzzitat |
|---|---|---|
| 41.000 Profile, 63 % ohne strukturiertes Können | `angenommen` | *„41.000 Bewerberprofile, 63 Prozent ohne strukturierte Qualifikationsfelder — der Lebenslauf liegt als PDF-Anhang, das Können steht im Freitext."* — `profil.md` |
| Keine offene Schnittstelle, kein Textindex | `Fakt im Fall` | *„ohne offene API im Bestandsvertrag und ohne Textindex"* — `w03A-1-ki-analyse-fassung-1.md`, Kontextzeile 9 |
| Kein Gültigkeitsdatum für Qualifikationsnachweise | **gemessen 2026-09-10** | 437 von 1.473 Profilen nennen einen nachweispflichtigen Schein, keines ein Ablaufdatum — [`w03B-2-agent-neubewertung-nach-bereinigung.md`](w03B-2-agent-neubewertung-nach-bereinigung.md) |
| Kernsystemwechsel Q1/2027 | `Fakt im Fall` | *„Das Kernsystem wird in Q1/2027 ersetzt. Anbieterauswahl läuft."* — Kontextzeile 6 |
| Graph erreicht die Profile nicht | `abgeleitet` | *„Microsoft Graph erreicht die 41.000 Bewerberprofile nicht, weil sie nicht in M365 liegen."* — `w03A-1-ki-analyse-fassung-1.md`, Empfehlung 3 |
| 28,8 % / 20,4 % | **`öffentlich`** | GVP 2025, siehe [`w03C-2-dsgvo-ai-act-auszug.md`](w03C-2-dsgvo-ai-act-auszug.md) Abschnitt 7 |

---

## 3 · Der Score, nachgerechnet

**Kurz.** Nachgerechnet, nicht neu gewichtet. Beide Matrizen stimmen zellenweise mit Fassung 2
überein. Kein Rechenfehler.

**Ausführlich.**

**Matrix A · Stufe 1** — Gewichte K1 25, K2 20, K3 17, K4 15, K5 11, K6 6, K7 4, K8 2

| Option | Score | Rang |
|---|---:|---:|
| **A · EU-Plattform** | **3,49** | 1 |
| B · Copilot | 3,09 | 2 |
| D · Branchensoftware 2027 | 2,32 | 3 |
| E · Nullvariante | 2,32 | 3 |
| C · Cloud-ML | 1,78 | 5 |

Abstand Erster zu Zweiter: **0,40.**

**Matrix B · Stufe 4** — Gewichte L0 20, L1 25, L2 18, L3 17, L4 10, L5 6, L6 4

| Option | Score | Rang |
|---|---:|---:|
| **F · Regelbasierter Filter** | **3,56** | 1 |
| E · Nullvariante | 2,86 | 2 |
| A · EU-Plattform | 2,61 | 3 |
| C · Cloud-ML | 2,42 | 4 |
| D · Branchensoftware | 2,36 | 5 |
| B · Copilot | 1,68 | 6 |

Abstand Erster zu Zweiter: **0,70.**

> **Beide Abstände sind größer als das Rauschen.** Die Regel des Kurses lautet: 3,8 gegen 3,7 ist
> kein Ergebnis. 0,40 und 0,70 sind es — aber das begründet die Empfehlung noch nicht, siehe
> Abschnitt 4.

**Belege und Quellen.** Zellenwerte unverändert aus
[`w03A-3-ki-analyse-fassung-2-gueltig.md`](w03A-3-ki-analyse-fassung-2-gueltig.md), Abschnitte 5
und 7. Nachrechnung reproduzierbar über das Skript in Abschnitt 5.

---

## 4 · Sensitivitätsprobe — und der unbequeme Befund

**Kurz.** Jedes Gewicht um ±10 Prozentpunkte verschoben, Rest proportional: **der Sieger hält in
allen 30 Varianten.** Das klingt nach einem starken Ergebnis, ist aber auch ein Befund gegen die
Methode — **wenn das Ergebnis von den Gewichten nicht abhängt, war die Gewichtung Dekoration.**

**Ausführlich.**

### Die Probe

| Matrix | geprüfte Varianten | Sieger kippt |
|---|---:|---|
| A · Stufe 1 | 16 (8 Kriterien, je ±10) | **in keiner** |
| B · Stufe 4 | 14 (7 Kriterien, je ±10) | **in keiner** |

Härtere Probe — das schwerste Kriterium bis auf null herunterziehen:

| Probe | Ergebnis |
|---|---|
| Matrix A: K1 Compliance von 25 % auf **0 %** | Option A gewinnt weiter |
| Matrix B: L1 Betreiberfähigkeit von 25 % auf **0 %** | Option F gewinnt weiter |
| Matrix B: L0 Leitkennzahl von 20 % auf **0 %** | Option F gewinnt weiter |
| **Gleichgewichtsprobe:** alle Kriterien gleich schwer | A gewinnt mit 3,50 vor B mit 2,88 · F gewinnt mit 3,57 vor E mit 3,14 |

### Wo der Sieger tatsächlich kippt

Der Grund für die Robustheit: **jeder Sieger unterliegt in genau einer Zelle.**

| Matrix | Sieger | unterliegt nur bei | kippt, wenn dieses Kriterium steigt auf |
|---|---|---|---|
| A | Option A | **K3** Adoption, Einführungsaufwand, Support (Score 2 gegen 4 bei Copilot) | **31 %** — dann gewinnt Option B |
| B | Option F | **L5** Betriebsaufwand (Score 3 gegen 4 bei der Nullvariante) | **45 %** — dann gewinnt Option E |

**Das sind die beiden Sätze für den Pitch**, und sie sind belastbarer als jeder Gesamtscore:

> *„Unsere Empfehlung für Stufe 1 kippt erst, wenn Adoption und Einführungsaufwand von 17 auf 31
> Prozent steigen. Dann wäre Copilot richtig — und das ist eine Diskussion, die wir führen können.
> Bis dahin ist es keine."*

> *„Für Stufe 4 kippt sie erst, wenn Betriebsaufwand von 6 auf 45 Prozent steigt. Dann wäre gar
> nichts zu bauen richtig. Wer das für plausibel hält, argumentiert gegen das Vorhaben, nicht gegen
> die Option."*

### Der Befund gegen die eigene Methode

`abgeleitet` — und er gehört in den Pitch, nicht in eine Fußnote.

Option A ist in Matrix A bei **sechs von acht** Kriterien beste oder gleichbeste Option, Option F in
Matrix B bei **sechs von sieben**. Bei so einem Muster entscheidet nicht die Gewichtung, sondern das
Scoring. Zwei Folgen:

1. **Die eigentliche Angriffsfläche sind die Scores, nicht die Gewichte.** Wer die Empfehlung
   kippen will, muss zeigen, dass eine 4 eine 2 ist — nicht, dass ein Gewicht falsch ist. Und
   Fassung 2 sagt selbst: *„Die Zeile ‚unabhängig belegt?' steht bei jeder Spalte auf nein oder
   teilweise."*
2. **Ein Kriterium, das die Kandidaten nicht trennt, hätte nie ein großes Gewicht bekommen dürfen** —
   das war die Begründung für Deployment mit 2 % und ist konsistent. Aber die Umkehrung gilt auch:
   wenn *kein* Gewicht das Ergebnis dreht, ist die Matrix eine Dokumentation der Entscheidung, nicht
   ihre Herleitung. Das ist bei fünf bzw. sechs Optionen und diesem Scoreabstand ein ehrliches
   Ergebnis — und es entwertet die Matrix nicht, es begrenzt nur ihre Aussage.

**Belege und Quellen.** Alle Werte dieses Abschnitts sind arithmetisch aus den Scores der Fassung 2
gerechnet, nicht geschätzt. Das Skript steht in Abschnitt 5. Herkunft der Eingangswerte:
Fassung 2, Matrix A und B — dort selbst gekennzeichnet als *„Einschätzungen auf
Herstellerunterlagen"*, nicht als Messwerte.

---

## 5 · Reproduktion der Rechnung

**Kurz.** Wer die Zahlen prüfen will, braucht dieses Skript und die beiden Matrizen der Fassung 2.
Die Gewichte werden bei jeder Verschiebung proportional normiert, damit die Summe 100 Prozent
bleibt.

**Ausführlich.**

```python
A_gew = {"K1":25,"K2":20,"K3":17,"K4":15,"K5":11,"K6":6,"K7":4,"K8":2}
A_sc  = {"K1":[4,3,3,2,2], "K2":[4,3,1,1,2], "K3":[2,4,1,3,2], "K4":[3,3,1,3,3],
         "K5":[4,3,1,4,3], "K6":[4,2,3,1,4], "K7":[4,3,4,3,1], "K8":[3,2,3,2,1]}

B_gew = {"L0":20,"L1":25,"L2":18,"L3":17,"L4":10,"L5":6,"L6":4}
B_sc  = {"L0":[3,1,3,2,1,3], "L1":[2,2,2,2,4,4], "L2":[2,1,2,3,1,3],
         "L3":[3,2,4,2,4,4], "L4":[3,2,1,3,4,4], "L5":[3,3,1,4,4,3], "L6":[4,2,3,1,4,4]}

def score(gew, sc, n):
    return [sum(gew[k]/100*sc[k][i] for k in gew) for i in range(n)]

def setz(gew, sc, ziel, neu):          # ein Gewicht setzen, Rest proportional
    rest = sum(v for k, v in gew.items() if k != ziel)
    f = (100 - neu) / rest
    g = {k: (neu if k == ziel else v*f) for k, v in gew.items()}
    return score(g, sc, len(next(iter(sc.values()))))
```

Spaltenreihenfolge Matrix A: A, B, C, D, E. Matrix B: A, B, C, D, E, F.

**Belege und Quellen.** Die Eingangswerte sind zellenweise aus Fassung 2 übernommen; die Kontrolle
ist, dass `score(A_gew, A_sc, 5)` die dort tabellierten 3,49 / 3,09 / 1,78 / 2,32 / 2,32 ergibt.

---

## 6 · Was der Prüfauftrag nicht abdeckt

**Kurz.** Der Auftrag verlangt Use Case, Prüfung, Nachrechnung, Empfehlung. Drei Dinge fehlen darin
und entscheiden trotzdem mit.

**Ausführlich.**

1. **Die Reihenfolge des Auftrags ist umgekehrt.** Der Use Case wird geschrieben, **nachdem** der
   Sieger bekannt ist. Das ist die Bestätigungsfalle, vor der das Kursmaterial selbst warnt. Ich
   habe sie umgangen, indem der Use Case in Abschnitt 2 ausschließlich aus dem Datenbestand
   abgeleitet ist — prüfbar daran, dass er zwei Optionen **ohne** Rückgriff auf Scores ausschließt.
2. **„Keine zweite Matrix" und „bezieht die Vormittagsanalysen ein" widersprechen sich.** Eine
   Datenqualitätsanalyse kann Scores treffen (erlaubt: nachrechnen) **und** Gewichte (verboten:
   zweite Matrix). Hier ist kein Gewicht geändert; wo eines nicht zu halten wäre, gehört es als
   datierter Änderungsvermerk hin, nicht in eine stille Anpassung.
3. **Aus einem Score folgt keine Empfehlung.** Die Sensitivität fehlt im Auftrag vollständig. Sie
   steht in Abschnitt 4, und ihr Ergebnis ist der eigentliche Ertrag der Prüfung — nicht die
   Bestätigung des Siegers, sondern die Erkenntnis, dass er nicht an der Gewichtung hängt.

**Belege und Quellen.** *„Wer die Gewichte setzt, nachdem er die Scores kennt, hat keine
Entscheidungsgrundlage gebaut, sondern eine nachträgliche Begründung"* und *„Ein Gesamtscore von
3,8 gegen 3,7 ist kein Ergebnis, sondern Rauschen"* — beide
[`bibliothek/vendor-evaluation.md`](#bibliothek/vendor-evaluation.md), Abschnitte 1 und 3.

---

## 7 · Gegenargumente

**Kurz.** Vier Einwände. Der erste ist der ernsteste und betrifft nicht die Rechnung, sondern ihre
Eingangswerte.

**Ausführlich.**

1. **Die Sensitivität prüft die Gewichte, aber die Schwäche liegt bei den Scores.** Alle Scores sind
   Einschätzungen auf Herstellerunterlagen; die Zeile *„unabhängig belegt?"* steht bei jeder Spalte
   auf nein oder teilweise. Eine perfekt robuste Gewichtung über unbelegten Scores ist Präzision an
   der falschen Stelle.
2. **Ein Sieger, der auch bei Gewicht null gewinnt, ist verdächtig.** Entweder ist er wirklich
   überlegen, oder das Scoring hat einen Halo-Effekt: wer einmal als beste Option gilt, bekommt
   überall die höhere Zahl. Prüfbar nur durch fremdes Nachscoren, nicht durch mich.
3. **Der Use Case ist von derselben Person geschrieben wie die Matrix.** Dass er zum selben
   Ausschluss kommt, ist deshalb ein schwächerer Beleg als eine unabhängige Prüfung. Er ist
   nachprüfbar, weil er nur auf Feldern und Zahlen des Bestands beruht — aber er ist nicht
   unabhängig.
4. **Option F ist nicht beziffert.** Sie gewinnt Matrix B mit dem größten Abstand beider Matrizen,
   und niemand weiß, was sie kostet. Fassung 2 nennt das selbst ihre schwächste Stelle. Eine
   Sensitivitätsprobe ändert daran nichts.

---

## 8 · Offene Punkte

**Kurz.** Fünf. Zwei sind terminkritisch, einer lässt sich nur von außen beantworten.

**Ausführlich.**

| # | Frage | Wer | Warum sie zählt |
|---:|---|---|---|
| 1 | Scort jemand anderes die Matrix nach? | Peer oder Rolle 12 | Der einzige Weg, Gegenargument 2 zu prüfen. Kostet eine Stunde |
| 2 | Was kostet Option F? | Rolle 12, künftiger Anbieter | Sie gewinnt Teil B und ist unbeziffert |
| 3 | Ist die Migrationsausschreibung noch offen? | Rolle 2 | Entscheidet, ob die Anbieterpflichten ins Lastenheft können. **Terminkritisch** |
| 4 | Trägt die Auswahl über einen deterministischen Filter die Ausnahme nach Art. 6 Abs. 3? | **Rolle 8** | Entscheidet über die Machbarkeit von Option F. **Terminkritisch** |
| 5 | Steigt K3 auf über 31 %, wenn der Einführungsaufwand von Option A einmal beziffert ist? | Rolle 12 | Die einzige Kippschwelle in realistischer Reichweite |

**Belege und Quellen.** Punkt 5 folgt aus der Kippschwelle in Abschnitt 4; Punkte 2 und 4 sind
offene Punkte der Fassung 2 und hier unverändert übernommen.

## Änderungsvermerk

| Datum | Was |
|---|---|
| 2026-09-10 | angelegt als Prüfung der Plattformentscheidung. Use Case aus dem Datenbestand, Score nachgerechnet, Sensitivität über 30 Varianten plus Kippschwellen und Gleichgewichtsprobe. **Kein Gewicht und kein Score geändert** |
