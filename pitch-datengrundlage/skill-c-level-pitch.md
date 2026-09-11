---
name: c-level-pitch
description: Aus einem Unternehmensprofil eine C-Level-Pitch-Präsentation herleiten — Kriterien, Gewichtung, 14 Folien, Sprechunterlagen und Datenblatt. Für Beschaffungs- und Freigabeentscheidungen vor einem Gremium, das haftet.
typ: SKILL · Methodenbeschreibung, kein Bestandteil eines Unternehmensprofils
ablage: pitch-datengrundlage/ — bewusst nicht unter .claude/skills/. Wer ihn aufrufbar machen will, kopiert ihn als SKILL.md dorthin
datum: 2026-09-11
eingabe: eine Firmen-md beliebiger Struktur
ausgabe: Präsentation (HTML) · Sprechzettel · Volltext · Datenblatt
beispiel: pitch-datengrundlage/GeAT-datengrundlage-plattformfreigabe.md (durchgerechnet)
vorlage: pitch-datengrundlage/vorlage-praesentation.html
baut_auf: vorlagen/pitch-c-level.md (die zehn Prüfkriterien) · coursebook/3.4 (Vier-Abschnitts-Format)
---

# Skill: Vom Unternehmensprofil zum C-Level-Pitch

> **Was dieser Skill kann.** Jemand übergibt ein Unternehmensprofil als Markdown-Datei — beliebig aufgebaut, aus einem anderen Kurs, einer anderen Branche, einer anderen Größe. Ergebnis sind vier Dateien: eine Präsentation, ein Sprechzettel, eine Volltextfassung und ein Datenblatt.
>
> **Was er nicht kann.** Er erfindet keine Zahlen. Fehlt ein Pflichtwert, wird er als Lücke ausgewiesen — im Ergebnis, nicht im Nebensatz. Eine Präsentation mit sichtbaren Lücken ist brauchbar; eine mit erfundenen Zahlen ist es nicht.
>
> **Die Grundannahme.** Der Adressat ist eine **Freigabeinstanz, die haftet** — keine Peer-Gruppe. Daraus folgt alles Weitere: Beschluss nach vorn, Gegenargumente selbst nennen, offene Punkte als Bedingungen.

---

## Schritt 1 · Datenaufnahme — die zwölf Pflichtwerte

Lies das übergebene Profil und trage diese zwölf Angaben zusammen. **Erfinde nichts.** Was fehlt, kommt in die Fehlliste am Ende dieses Schritts.

| # | Was gebraucht wird | Wofür im Pitch |
|---:|---|---|
| 1 | **Der Beschlussgegenstand und sein Betrag** | Folie 2 |
| 2 | **Freigabegrenzen, Gremien und ihr Tagungsrhythmus** | Folie 2 — bestimmt den Zuschnitt, siehe Schritt 2 |
| 3 | **Investitionsspielraum**, und ob im Haus eine andere Zahl umläuft | Folie 4 |
| 4 | **Der Anlass:** was ist das Problem, seit wann, woran erkennbar | Folie 3 |
| 5 | **Mengengerüst der Betroffenen:** Personen, Bestände, Standorte | Folien 3 und 4 |
| 6 | **Umsetzungskapazität und ihre Bindungen** (IT-Stellen, laufende Großvorhaben) | Folien 4 und 9 |
| 7 | **Eine Vorgängerinitiative mit Zahl** — bevorzugt eine gescheiterte | Folie 8. **Der wichtigste Einzelwert** |
| 8 | **Bestands- und Qualitätszahlen**, soweit ein Kriterium daran hängt | Folien 6 und 12 |
| 9 | **Die Optionen**, einschließlich Nullvariante und hausinterner Alternativen | Folie 6 |
| 10 | **Regulatorische Lage** (Datenschutz, Branchenrecht, Mitbestimmung) | Folie 10 |
| 11 | **Wer im Raum sitzt und welche Kennzahl diese Person verlangt** | Folien 8 und 14 |
| 12 | **Was nicht bekannt ist** — ausdrücklich abgefragt | Folien 10 und 11 |

**Übernimm die Herkunftskennzeichen des Profils.** Hat es keine, führe sie selbst ein: `belegt` · `angenommen` · `gerechnet` · `unbekannt`. Ohne diese Trennung ist das spätere Datenblatt wertlos.

> **Fehlliste.** Fehlt Nr. 1, 2, 4 oder 9, brich ab und frage nach — ohne sie gibt es keinen Pitch. Fehlt Nr. 7, sag es deutlich: der Pitch verliert seinen stärksten Teil und wird deutlich schwächer. Alles andere lässt sich mit einer benannten Lücke bauen.

---

## Schritt 2 · Der Zuschnitt — der Schritt, den alle überspringen

**Bevor** irgendetwas bewertet wird: Finde die Grenze, unterhalb derer das anwesende Gremium **allein** entscheiden kann, und prüfe, ob das Vorhaben darunter passt.

Das ist keine Formalie. In dem durchgerechneten Beispiel entscheidet die Geschäftsführung wöchentlich bis 25.000 €, darüber die Gesellschafterversammlung — quartalsweise. Ein Vorhaben über der Grenze verliert bis zu drei Monate. Der Betrag wurde deshalb bewusst darunter zugeschnitten, und **genau das ist ein Argument, kein Zufall.**

| Lage | Konsequenz für den Pitch |
|---|---|
| Vorhaben passt unter die Grenze | Sag es auf Folie 2: *„Sie entscheiden allein."* Und sag, dass der Zuschnitt Absicht war |
| Vorhaben passt nicht darunter | Dann ist dies **nicht** der Pitch, sondern die Vorbereitung einer Gremiumsvorlage. Ändere das Ziel: nicht Freigabe, sondern Auftrag zur Vorlage — und nenne den Sitzungstermin |
| Es gibt keine Grenze / kein Gremium | Kläre, wer unterschreibt. Ohne Adressat ist jeder Pitch an die falsche Person gerichtet |

**Zweite Frage in diesem Schritt:** Hat die vortragende Rolle ein eigenes Budget? Wenn nein, gehört das in den ersten Satz — es erklärt, warum überhaupt jemand fragen muss.

---

## Schritt 3 · Kriterien herleiten, nicht übernehmen

**Übernimm keine Kriterienliste.** Die acht aus dem Beispiel gelten für dieses Unternehmen, nicht allgemein — „Verfügbarkeit gegen die Taktgrenze" existiert nur, weil dort ein Gremium quartalsweise tagt.

Drei Regeln:

**Regel 1 — Jedes Kriterium braucht einen Satz über *diese* Organisation.** Kein Satz, kein Kriterium. Der Satz muss aus dem Profil stammen, nicht aus der Technik. *„Compliance wiegt schwer, weil Datenschutz wichtig ist"* ist kein Satz — das sagt jeder. *„Compliance wiegt schwer, weil sie hier der Zweck der Beschaffung ist und nicht eine Zulassungsfrage für später"* ist einer.

**Regel 2 — Was nicht trennt, bekommt kein Gewicht.** Prüfe jedes Kriterium: Bewerten sich die Optionen darin unterschiedlich? Wenn alle gleich abschneiden, kostet es Gewicht und bewegt die Entscheidung nicht. Im Beispiel bekam „Deployment-Flexibilität" deshalb 2 %.

**Regel 3 — Ausschlusskriterien gehören *vor* die Matrix, nicht hinein.** „Rechtskonform: 4" ist unsinnig. Eine Bedingung ist erfüllt oder nicht. Ziehe sie heraus und nenne sie auf Folie 10 als Bedingung.

> **Prüffrage für die fertige Liste:** Kannst du jedes Gewicht auf einen Satz über die Organisation zurückführen? Geht das bei einem nicht, ist es entweder falsch gewichtet oder gar kein Kriterium.

**Wie das im Beispiel aussah** — zur Orientierung, nicht zur Übernahme:

| Kriterium | Gewicht | Der Satz, der es begründet |
|---|---:|---|
| Compliance und AVV | 25 % | Es ist der **Zweck** der Beschaffung, nicht eine Zulassungsfrage |
| Verfügbarkeit gegen die Taktgrenze | 20 % | Jeder Monat ohne zulässigen Ersatz ist ein weiterer Monat ohne Vertrag |
| Adoption und Einführungsaufwand | 17 % | Das letzte Werkzeug liegt bei 34 % Nutzung |
| Kosten über drei Jahre | 15 % | EBIT-Marge 2,6 %, Gesellschafter erwarten Ausschüttung |
| Betriebsaufwand | 11 % | 1,5 IT-Stellen, bis Q1/2027 gebunden |
| Exit und Portabilität | 6 % | Systemwechsel steht bevor |
| RAG und Integrationstiefe | 4 % | **63 % der Profile sind unstrukturiert — die Voraussetzung fehlt** |
| Deployment-Flexibilität | 2 % | Bei dieser Größe gibt es faktisch nur eine Variante — trennt nicht |

Die letzten beiden Zeilen sind die lehrreichen: **ein Kriterium abzuwerten, das im Lehrbuch schwer wiegt, ist eine Leistung — wenn man es begründen kann.**

---

## Schritt 4 · Gewichten

- **Summe 100 %.** Fünf bis acht Kriterien. Mehr kann niemand verteidigen.
- **Reihenfolge einhalten: Kontext → Gewichtung → Scoring.** Die Gewichte werden **schriftlich fixiert, bevor** gescort wird. Wer das Ergebnis kennt und dann gewichtet, baut eine nachträgliche Begründung und merkt es selbst nicht.
- **Jede spätere Änderung wird als Änderung ausgewiesen**, mit Grund. Nicht still verschieben.
- Bei einer **öffentlichen Vergabe** ist das keine Disziplin, sondern Pflicht: Zuschlagskriterien und Gewichtung werden vorab bekanntgegeben und sind danach nicht mehr änderbar.

**Drei Faustregeln, die sich bewährt haben:**
1. Der **Zweck** der Beschaffung bekommt das höchste Gewicht.
2. Was die Organisation **nicht betreiben kann**, bekommt viel — nicht wenig.
3. Was die Kandidaten **nicht trennt**, bekommt wenig — unabhängig davon, wie wichtig es klingt.

---

## Schritt 5 · Scoring, Sensitivität, Kippschwelle

**Scores 1–5, mit Ankern.** Ohne Ankerdefinition erzeugen zwei Bearbeiter zwei Skalen. Vorschlag: *5 = erfüllt belegbar und vertraglich · 4 = erfüllt, Belege öffentlich · 3 = teilweise, mit Aufwand herstellbar · 2 = nur auf Roadmap · 1 = nicht vorgesehen.*

**Jede Zahl braucht eine Begründung mit Quelle.** Und eine Zeile *„unabhängig belegt? ja / nein / teilweise"* — bei Herstellerunterlagen lautet die Antwort *nein*, und das gehört sichtbar in die Matrix.

**Sensitivitätsprobe:** jedes Gewicht um ±10 Prozentpunkte verschieben, Rest proportional, neu rechnen. Das ergibt **2 × Anzahl der Kriterien** Durchläufe. Zwei Ergänzungen:
- **Härtere Probe:** das schwerste Kriterium auf null ziehen.
- **Gleichgewichtsprobe:** alle Kriterien gleich schwer. Die ist am überzeugendsten, weil sie die Gewichtung ganz aus dem Spiel nimmt.

**Dann die Kippschwelle suchen** — das Kriterium, in dem der Sieger als einziges unterliegt, und den Gewichtswert, ab dem er verliert. **Dieser Wert gehört auf die Folie.** Er ist der einzige Satz, mit dem der Vortragende benennt, unter welcher Bedingung er falsch liegt, und er erzeugt mehr Vertrauen als jeder Gesamtscore.

> **Zwei Ehrlichkeiten, die dazugehören.** Bei Kriterien unter 10 % ist die Variante „−10" faktisch eine Null-Probe. Und wenn die stärkste Variante nahe an die Kippschwelle heranreicht, sag es: *„n von n halten — die knappste Variante liegt x Punkte darunter."*
>
> **Und die Abbruchregel:** Liegen die beiden besten Gesamtscores weniger als **0,3** auseinander, ist das kein Ergebnis, sondern unentschieden. Dann entscheidet ein Kriterium, das noch fehlt — such es, statt die Differenz zu verteidigen.

---

## Schritt 6 · Die vierzehn Folien

Benutze `vorlage-praesentation.html`. Jede Folie trägt ihre Aufgabe im Kommentar. **Die Reihenfolge ist das Argument** — nicht umstellen:

| # | Folie | Aufgabe | Pflicht |
|---:|---|---|---|
| 1 | Titel | Rahmen setzen | kein Wort über Technik |
| 2 | **Beschluss** | BLUF: Betrag, Umfang, Freigabekompetenz | warum überhaupt gefragt wird, und warum der Betrag so zugeschnitten ist |
| 3 | Der Grund | Problem mit Mengengerüst | der Satz *„Wir beschaffen kein X, wir beenden Y"*; kein Vorwurf an Betroffene |
| 4 | Wie es geht | beweist: das Vorhaben ist klein | drei Kacheln, ein Gedanke |
| 5 | Wann und Stop | Start plus **Abbruchkriterium vor dem Beschluss** | positiv formuliert, beide Bedingungen messbar |
| 6 | Alternativen | Ausschlusslogik statt Punktetabelle | Nullvariante **und** eine Ergebniszeile |
| 7 | Robustheit | Sensitivität und Kippschwelle | Skala nennen („von 5"), Kippschwelle aussprechen |
| 8 | Gegenargument | das stärkste, möglichst das eigene | mit Zahl. Dem Einwand zuerst recht geben |
| 9 | Diesmal anders | **Kontraste** zu Folie 8 | jede Zeile ein Gegensatz, keine Aufzählung |
| 10 | Bedingungen | offene Punkte als Bedingungen | eine echte Lücke offen benennen |
| 11 | Zweitbeschluss | aus einer Wissenslücke wird ein Auftrag | kein Geld; terminkritisch |
| 12 | Reihenfolge | Governance vor Werkzeug | optional, entfällt bei Zeitnot |
| 13 | Beschlussantrag | genau drei Punkte | wer, was, bis wann |
| 14 | Zustimmung | beide Ausgänge tragbar zeigen | die Frage stellen, dann still sein |

**Sechs Sprachregeln, die sich als nötig erwiesen haben:**
1. **Keine Anglizismen für Beschlusssachen.** „Bedingung", nicht „Gate". „Bedingte Freigabe", nicht „bedingtes Go". „Zugänge" oder „Lizenzen", nicht „Seats". Und nicht „Hinderungsgrund" — das dreht die Aussage um: eine Bedingung muss erfüllt werden, damit es losgeht, ein Hinderungsgrund spricht dagegen.
2. **Den Anbieter beim Namen nennen**, mit dem Zusatz, ob ein Angebot vorliegt. Gattungsbegriffe klingen nach Ausweichen.
3. **Ein Kachel-Label sagt, was die Zahl ist — nicht, was sie nicht ist.** Korrekturen gehören in den Mund, nicht auf die Folie.
4. **Kein Satz über den Vortrag.** „Ich fasse mich kurz" ist nicht kurz. Der erste Satz trägt Inhalt oder entfällt.
5. **Keine doppelten Verneinungen** in Abbruchbedingungen. Positiv formulieren.
6. **Keine Fachsprache ohne Übersetzung.** „Wird berichtet, nicht verrechnet" versteht niemand. „Es verschwindet nicht in einer anderen Position" schon.

**Und eine Warnung, die Geld kostet:** Sag **nicht** „Sie haben null Risiko". Wenn der Pitch selbst offene Punkte nennt — und er soll —, ist der Satz widerlegbar, und zwar von jemandem im Raum. Sag stattdessen, worauf das Risiko **begrenzt** ist: Betrag und Zeitraum.

**Sprechernotizen (`data-notes`) sind Pflicht auf jeder Folie.** Sie tragen, was gesagt und was **nicht** gesagt wird.

---

## Schritt 7 · Die beiden Sprechunterlagen

**Sprechzettel** — ein Blatt, Stichpunkte, für die Hand am Rednerpult. Je Folie ein Block mit Zeitbudget. Fett = muss fallen. Dazu zwei Teile, die sich bewährt haben: **die vier Sätze, die auf keinen Fall fehlen dürfen**, und eine Tabelle **vorbereiteter Antworten** auf die Rückfragen, die kommen werden (*„warum nicht abwarten?", „warum nicht verbieten?", „Amortisation?", „und wenn der Anbieter übernommen wird?"*).

**Volltext** — zum Üben, nicht zum Vorlesen. Mit Folienwechseln als `▶ FOLIE n`, Pausenmarken, Zeitmarken und Regieanweisungen in Klammern. Dazu ein **Notfallpfad**: welche Folien bleiben, wenn die Sitzung auf ein Drittel zusammenschrumpft.

---

## Schritt 8 · Das Datenblatt

Eine Datei mit allen Werten, die in die Präsentation eingegangen sind, damit ein Dritter sie prüfen kann. Vier Pflichtbestandteile:

1. **Die Einschränkung des Quellprofils, wörtlich und ganz oben.** Wenn dort steht, dass die Zahlen nicht außerhalb verwendbar sind, steht das auch hier — an erster Stelle, nicht im Anhang.
2. **Herkunftskennzeichen an jedem Wert**, mit Lesehilfe.
3. **Eine Zuordnung Folie → benötigte Werte.** Das ist der Teil, der die Datei benutzbar macht statt nur lesbar.
4. **Ein Abschnitt „Was nicht belegt ist"** mit dem Hinweis, dass diese Lücken Teil des Arguments sind und nicht Nachlässigkeit.

**Keine personenbezogenen Namen.** Alle Beteiligten als Rollen führen.

---

## Prüfliste vor der Abgabe

Die zehn Kriterien aus [`vorlagen/pitch-c-level.md`](../vorlagen/pitch-c-level.md) durchgehen — Ein-Satz-Test · Freigabekompetenz · Nullvariante mit Preis · stärkstes Gegenargument selbst genannt · Herleitung statt Scores · Ausschlusskriterien vorab · Sensitivität · die verlangte Zahl mit Herkunft · nächster Schritt mit Abbruchkriterium · offene Fragen als Bedingungen.

Dazu fünf, die erst beim Bauen aufgefallen sind:

- [ ] Steht der Beschluss in den ersten 45 Sekunden?
- [ ] Trägt jede Zeile auf Folie 9 einen **Kontrast**, keine Aussage?
- [ ] Ist die Kippschwelle genannt — also der Punkt, an dem die Empfehlung falsch wäre?
- [ ] Ist mindestens eine eigene Lücke offen benannt, ohne Beschönigung?
- [ ] Gibt es einen **Zweitbeschluss** — etwas, das nur das Gremium erledigen kann?

---

## Was dieser Skill bewusst nicht tut

**Er baut keinen Business Case.** Eine Freigabe unter einer Gremiengrenze und ein Business Case über 100.000 € sind zwei verschiedene Gattungen mit zwei verschiedenen Adressaten. Wer beides mischt, verliert beide.

**Er bewertet nicht, ob das Vorhaben sinnvoll ist.** Er vertritt eine Empfehlung, die jemand anderes hergeleitet hat — und er macht ihre Schwachstellen sichtbar, statt sie zu verstecken.

**Er ersetzt keine Rechtsberatung.** Regulatorische Aussagen gehören als Bedingung formuliert und von der zuständigen Stelle schriftlich bestätigt.

---

## Anhang · Das durchgerechnete Beispiel

[`GeAT-datengrundlage-plattformfreigabe.md`](GeAT-datengrundlage-plattformfreigabe.md) enthält denselben Weg mit echten Werten: zwölf Pflichtwerte gefüllt, acht Kriterien hergeleitet, fünf Optionen bewertet, sechzehn Sensitivitätsvarianten, Kippschwelle bei 31 %, vier offene Punkte.

**Lies es als Beispiel für die Form, nicht als Vorlage für die Zahlen.** Die Zahlen gelten für ein Unternehmen mit 709 Beschäftigten, sechs Standorten, 1,5 IT-Stellen und einer quartalsweise tagenden Gesellschafterversammlung. Ändert sich eine dieser vier Größen, ändert sich die halbe Gewichtung.
