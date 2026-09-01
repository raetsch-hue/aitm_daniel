# Weiterführende Quellen

**Höchstens drei pro Thema — nur was den Aufwand wirklich lohnt**
Kurs: AI and Digital Transformation Management · neue fische × SPICED, 2026
Geprüft am 01.09.2026 · umfasst die Tage 1.4, 1.5, 2.1, 2.2 und die Ergänzung zu 2.2

---

## Auswahlkriterium

Es gibt zu jedem dieser Themen hunderte Artikel und Videos. Die meisten wiederholen, was in den Folien steht. Aufgenommen ist nur, was **eine der drei Bedingungen** erfüllt:

- Es ist die **Primärquelle** zu etwas, das im Kurs nur als Behauptung auftaucht
- Es liefert die **Gegenposition**, die deine Argumentation belastbar macht
- Es ist **direkt anwendbar** — du kannst es morgen benutzen

Jeder Link wurde am 01.09.2026 geprüft. Paywalls und Sprache sind vermerkt.

---

## Tag 1.4 — Vier Wellen, KI-Kategorien, Hype Cycle

### 1. Die Produktivitäts-J-Kurve ●●●

**Brynjolfsson, Rock & Syverson (2021):** *The Productivity J-Curve: How Intangibles Complement General Purpose Technologies.* American Economic Journal: Macroeconomics.
🔗 https://www.aeaweb.org/articles?id=10.1257/mac.20180386 · Englisch, Fachaufsatz

**Warum diese Quelle:** Der Kurs behauptet, dass keine Welle übersprungen werden kann. Das hier ist der Beleg. Die Autoren zeigen, dass General Purpose Technologies erst dann Produktivität erzeugen, wenn die komplementären immateriellen Investitionen — Prozesse, Qualifikation, Daten — getätigt sind. Diese Investitionen kosten sofort und wirken erst Jahre später; die gemessene Produktivität sinkt also zunächst.

**Was du daraus mitnimmst:** Das Argument, mit dem du Vorleistungen ins Budget bekommst. „Wir sehen im ersten Jahr keinen Effekt" ist keine Ausrede, sondern der dokumentierte Normalfall bei dieser Technologieklasse.

**Wenn die Zeit knapp ist:** Abstract und Einleitung reichen für das Argument.

### 2. Gartner, Hype-Cycle-Methodik ●●

🔗 https://www.gartner.com/en/research/methodologies/gartner-hype-cycle · Englisch, frei

**Warum diese Quelle:** Wer den Hype Cycle im Steuerkreis benutzt, sollte die Originaldefinition der fünf Phasen kennen — nicht die Nacherzählung aus dritter Hand. Nebenbei sichtbar: Gartner selbst formuliert vorsichtiger, als die verbreitete Verwendung nahelegt, und gibt bewusst **keine Zeitachse** an.

**Was du daraus mitnimmst:** Saubere Phasenbezeichnungen und die Gewissheit, dass eine Zyklusposition keine Prognose ist. Das schützt vor dem häufigsten Fehler: aus „im Trough" ein Datum abzuleiten.

### 3. Carlota Perez — Vorträge und Aufsätze ●●

🔗 https://www.carlotaperez.org/ · Englisch, frei, Videos und PDFs

**Warum diese Quelle:** Die seriöse Alternative zum Hype Cycle. Perez beschreibt technologische Revolutionen als Abfolge von Installations- und Deploymentphase mit einer Krise dazwischen — hergeleitet aus fünf historischen Revolutionen statt aus einer Kurve ohne Datengrundlage. Die Aussage ist dieselbe wie „im Trough investieren", nur mit Mechanismus und Belegen.

**Was du daraus mitnimmst:** Deine Rückfallposition, wenn im Raum jemand den Hype Cycle als unwissenschaftlich angreift. Und ein besseres mentales Modell dafür, warum Wertschöpfung der Euphorie *nachläuft*.

**Zugang:** Auf der Seite gibt es aufgezeichnete Vorträge — für den Einstieg besser geeignet als die Aufsätze.

> **Wenn du nur eine Sache liest:** die J-Kurve. Sie stützt das zentrale Argument des Tages, und sie ist zitierfähig.

---

## Tag 1.5 — Strategisches Prompt Engineering

### 1. Anthropic, Prompting Best Practices ●●●

🔗 https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices · Englisch, frei

**Warum diese Quelle:** Die maßgebliche und laufend aktualisierte Referenz. Sie deckt genau die Schrauben ab, die im Kurs behandelt werden — XML-Struktur, 3 bis 5 Beispiele, „sag was zu tun ist statt was zu lassen" — und dokumentiert die Punkte, an denen ältere Ratgeber inzwischen falsch liegen: adaptives Denken statt manueller Denkbudgets, kein Prefill mehr bei aktuellen Modellen.

**Was du daraus mitnimmst:** Die konkreten Formulierungsmuster zum Übernehmen. Insbesondere der Abschnitt zu langem Kontext: Material nach oben, Frage nach unten, bis zu 30 % bessere Antwortqualität.

**Zusatz:** Die kürzere Schwesterseite zu langem Kontext lohnt die zehn Minuten:
🔗 https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/long-context-tips

### 2. Anthropic, Effective Context Engineering for AI Agents ●●●

🔗 https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents · Englisch, frei

**Warum diese Quelle:** Der Artikel hinter Stellschraube 6. Er erklärt, warum mehr Kontext ab einem Punkt schlechtere Ergebnisse liefert — *Context Rot*, das begrenzte Aufmerksamkeitsbudget — und wie man eine Systemanweisung auf die richtige Flughöhe bringt: spezifisch genug zum Steuern, offen genug für Heuristiken.

**Was du daraus mitnimmst:** Die Begründung dafür, warum deine `kontext/`-Dateien kurz und aktuell bleiben müssen statt vollständig zu werden. Das ist der Unterschied zwischen einem Repo, das nach acht Wochen noch trägt, und einem, das schlechter wird.

### 3. Anthropic Academy ●●

🔗 https://www.anthropic.com/learn · Englisch, Kurse mit Zertifikat

**Warum diese Quelle:** Die einzige Videoempfehlung der Liste. Strukturierte Kurse zu AI Fluency, Arbeiten mit der API und Model Context Protocol — deutlich näher an der Praxis als die üblichen Prompt-Tipp-Videos, die zu großen Teilen aus Ritualen bestehen, die im Kursdokument unter „Was nicht funktioniert" stehen.

**Was du daraus mitnimmst:** Systematik statt Tricks, und mit MCP ein Thema, das dir in Woche 3 bei den Plattformkriterien wieder begegnet.

> **Wenn du nur eine Sache liest:** die Best Practices. Sie sind die Quelle, aus der die sechs Stellschrauben des Kurstags stammen — und sie altern langsamer als jeder Blogartikel.

---

## Tag 2.1 — Change Management: Lewin & ADKAR

### 1. Prosci, ADKAR Model Overview ●●

🔗 https://www.prosci.com/methodology/adkar · Englisch, frei

**Warum diese Quelle:** Die Anbieterseite zum Modell, und damit der schnellste Weg zu sauberem Begriffsgebrauch, wenn du dein ADKAR-Scoring-Dokument schreibst. Dort findest du außerdem Fallstudien und das Assessment-Konzept hinter dem Barrier Point.

**Was du daraus mitnimmst:** Verlässliche Definitionen. **Mit einem Vorbehalt:** Das ist Produktdokumentation eines kommerziellen Anbieters, keine unabhängige Forschung. Für den Praxisgebrauch gut, in einer Arbeit entsprechend kennzeichnen.

### 2. Dent & Goldberg (1999): „Challenging ‚Resistance to Change'" ●●●

Journal of Applied Behavioral Science 35(1), 25–41. · Englisch, Fachaufsatz, meist kostenpflichtig

**Warum diese Quelle:** Der größte Ertrag pro investierter Stunde im ganzen Kursthema. Die Autoren zeigen, dass Lewin Widerstand im **System** verortete und dass die spätere Managementliteratur ihn in die **Person** verschoben hat. Diese Verschiebung ist folgenreich: „Die Belegschaft leistet Widerstand" führt zu Überzeugungsarbeit und Druck, „es gibt hemmende Kräfte im System" führt dazu, Barrieren abzubauen. Dieselbe Beobachtung, zwei völlig verschiedene Maßnahmen.

**Was du daraus mitnimmst:** Eine dauerhafte Änderung daran, wie du über Ablehnung sprichst und schreibst. Ersetze „Widerstand" durch die konkrete hemmende Kraft — das ist präziser, adressierbar, und es beschuldigt niemanden.

**Zugang:** Über Hochschulbibliotheken zugänglich. Falls du nicht herankommst: Der Kern steht in [2.1 · Kritik und Alternativen](#2.1/01_Change-Management-Lewin-ADKAR.md#10-kritik-grenzen-und-alternativen).

### 3. Burnes (2020): „The Origins of Lewin's Three-Step Model of Change" ●

Journal of Applied Behavioral Science 56(1), 32–59. · Englisch, Fachaufsatz, meist kostenpflichtig

**Warum diese Quelle:** Im Slide Deck zitiert, deshalb hier. Burnes zeichnet nach, dass Lewin das 3-Stufen-Modell nie als Modell veröffentlicht hat — es wurde nach seinem Tod 1947 aus seinen Texten zusammengestellt.

**Was du daraus mitnimmst:** Vor allem eine Sprachregelung: „das Modell, das üblicherweise Lewin zugeschrieben wird". Für die tägliche Arbeit reicht diese eine Einsicht; der volle Aufsatz lohnt nur, wenn du korrekt zitieren musst.

> **Wenn du nur eine Sache liest:** Dent & Goldberg. Es ändert etwas an deiner Praxis, nicht nur an deinem Wissen.

---

## Tag 2.2 — Kotters 8-Schritte-Modell

### 1. Kotter (1995): Leading Change — Why Transformation Efforts Fail ●●●

Harvard Business Review, Mai–Juni 1995.
🔗 https://hbr.org/1995/05/leading-change-why-transformation-efforts-fail-2 · Englisch, teilweise kostenpflichtig

**Warum diese Quelle:** Der Ursprungstext, aus dem die acht Schritte hervorgingen. Zwanzig Seiten, in einer Stunde gelesen, und er enthält beides — das Modell und die Fallbeobachtungen, aus denen es entstand.

**Was du daraus mitnimmst:** Vor allem zwei Dinge, die im Umlauf falsch wiedergegeben werden. Erstens den Satz, der das Modell trägt: *„Skipping steps creates only an illusion of speed and never produces a satisfying result."* Zweitens Kotters **tatsächliche** Aussage zur Erfolgsquote — qualitativ, vorsichtig, und ohne die 70-Prozent-Zahl, die ihm regelmäßig zugeschrieben wird.

**Vorbehalt:** Es ist eine Beratungsbeobachtung, keine kontrollierte Untersuchung. Das mindert den praktischen Wert nicht, aber es gehört bei jeder Zitierung dazu.

**Zugang:** Der Artikel liegt **hinter einer Bezahlschranke** — die Adresse steht oben, falls du über Hochschule oder Arbeitgeber Zugang hast. Falls nicht, ist nichts verloren: Die beiden Aussagen, auf die es ankommt — der Satz zum Überspringen von Schritten und Kotters *tatsächliche*, qualitative Formulierung zur Erfolgsquote — sind in [2.2 · Datenlage](#2.2/2.2_Kotter-8-Schritte-Modell.md#2-kotter-und-die-datenlage--was-belegt-ist-und-was-nicht) wörtlich zitiert und eingeordnet.

### 2. Kotter Inc., The 8 Steps for Leading Change ●●

🔗 https://www.kotterinc.com/methodology/8-steps/ · Englisch, frei

**Warum diese Quelle:** Weil die Schritte heute anders heißen als im Kurs. Aus „Vision kommunizieren" wurde **„Enlist a Volunteer Army"**, aus „Consolidate" wurde „Sustain Acceleration". Wer nur die Fassung von 1996 kennt, kommt in Gesprächen mit Beratungen ins Stolpern.

**Was du daraus mitnimmst:** Die Umbenennung von Schritt 4 ist die aufschlussreichste. Sie verschiebt das Erfolgsmaß von *gesendet* auf *gewonnen* — dieselbe Korrektur, die ADKAR bei *Awareness* vornimmt. Zehn Minuten für eine Einsicht, die deine Kommunikationsplanung ändert.

### 3. Kotter (2012): Accelerate! ●●

Harvard Business Review, November 2012.
🔗 https://hbr.org/2012/11/accelerate · Englisch, teilweise kostenpflichtig

**Warum diese Quelle:** Kotters eigene Korrektur an seinem Modell. Er beschreibt hier das Dual Operating System — Hierarchie und Netzwerk parallel — und räumt damit implizit ein, dass die strenge Schrittfolge von 1996 der Realität schnelllebiger Organisationen nicht standhält.

**Was du daraus mitnimmst:** Die Begründung dafür, warum KI-Vorhaben beides gleichzeitig brauchen: stabile Governance und schnelle Experimente. Und ein Modell dafür, wie das organisatorisch aussieht, ohne ein separates Innovation Lab zu bauen.

> **Wenn du nur eine Sache liest:** den Artikel von 1995. Er ist die Quelle, er ist kurz, und er immunisiert dich gegen die falschen Zahlen, die in seinem Namen kursieren.

---

## Ergänzung zu 2.2 — Force-Field-Analyse

> **Andere Rolle als die übrigen Abschnitte.** Diese drei Adressen sind nicht Vertiefung nach dem Block, sondern **Vorbereitung darauf**. Der Nachmittagsblock am Mittwoch ist der kürzeste der Woche, der Vormittag gehört dem Career Day. Wer die erste Quelle gelesen hat, spart im Block rund zwanzig Minuten. Aufbereitet und um das Verfahren, die Bewertungsregeln und eine Vorlage ergänzt steht alles in [Ergänzung 2.2](#2.2/2.2_Ergaenzung-Force-Field-Analyse.md) — die Quellen darunter sind das Original dazu.

### 1. Toolshero, Force Field Analysis (Lewin) ●●●

🔗 https://www.toolshero.com/change-management/force-field-analysis-lewin/ · Englisch, frei

**Warum diese Quelle:** Sie ist **direkt anwendbar** — das dritte Auswahlkriterium dieser Liste, und hier ist es wörtlich gemeint. Die Seite beschreibt die Kraftfeldanalyse als Verfahren in acht Schritten, von der Formulierung des Soll-Zustands bis zum Maßnahmenplan mit Verantwortlichen, dazu die Gliederung der Kräfte in drei Cluster, ein durchgerechnetes Beispiel (Einführung einer Kollaborationsplattform) und fünf ehrlich benannte Grenzen.

**Was du daraus mitnimmst:** Das Werkzeug für Mittwoch. Zwei Einsichten tragen den Rest: Kräfte werden **erst einzeln, dann gemeinsam** gesammelt, und ein Ansatzpunkt muss **stark und beeinflussbar** sein — beides gleichzeitig. Der zweite Satz erklärt, warum so viele Change-Maßnahmen fleißig und wirkungslos sind.

**Vorbehalt:** Lernplattform, also Sekundärdarstellung. Als Verfahren brauchbar, als Beleg nicht zitierfähig — die Primärquelle steht unter Nummer 3.

### 2. Toolshero, Kotter's 8 Step Change Model ●●

🔗 https://www.toolshero.com/change-management/kotter-8-step-change-model/ · Englisch, frei
*(Die zweite kursierende Adresse `/8-step-change-model/` führt auf denselben Artikel.)*

**Warum diese Quelle:** Nicht wegen der Genauigkeit — das Hauptdokument ist in jedem Punkt präziser. Sondern weil das hier die **verbreitetste** Kurzfassung ist: Wenn dir jemand im Steuerkreis Kotter erklärt, ist es mit hoher Wahrscheinlichkeit diese und nicht die von 1995. Sie benutzt noch die Bezeichnungen von 1996, ist durchgehend partizipativer formuliert als Kotters Original und illustriert das Modell an einem Durchlauf, in dem jeder Schritt gelingt.

**Was du daraus mitnimmst:** Vor allem die beiden Einwände am Ende der Seite — Veränderung verläuft eher organisch als linear, und das Modell berücksichtigt finanzielle und politische Kräfte nicht. Die dort gezogene Konsequenz ist genau der Grund, warum morgen beides zusammen dran ist: **Kotter mit der Force-Field-Analyse ergänzen.**

### 3. Lewin (1947): Frontiers in Group Dynamics ●

Human Relations 1(1), 5–41.
🔗 https://journals.sagepub.com/doi/10.1177/001872674700100103 · Englisch, Fachaufsatz, **kostenpflichtig**

**Warum diese Quelle:** Die Primärquelle zum Kraftfeld. Hier stehen die quasi-stationären Gleichgewichte im Original — und damit der Beleg für die Aussage, die der ganze Mittwoch trägt: dass ein Zustand von zwei gleich starken Kräftebündeln gehalten wird und dass das Lösen der hemmenden Seite andere Folgen hat als das Verstärken der treibenden.

**Was du daraus mitnimmst:** Für die praktische Arbeit nichts, was nicht auch in den ersten beiden Quellen steht. Relevant, wenn du korrekt zitieren musst — und als Beleg dafür, dass die Kraftfeldanalyse **tatsächlich** von Lewin stammt, anders als das 3-Stufen-Modell ([Burnes-Vorbehalt](#2.1/01_Change-Management-Lewin-ADKAR.md#2-kurt-lewin-person-werk-und-was-davon-wirklich-von-ihm-stammt)).

> **Wenn du nur eine Sache liest:** die Force-Field-Seite — und zwar heute, nicht nach dem Block. Sie ist die einzige Quelle dieser ganzen Liste, die morgen Nachmittag Zeit spart.

---

## Was hier bewusst nicht steht

**Keine Prompt-Tipp-Sammlungen und keine „50 besten Prompts"-Videos.** Ein großer Teil dieser Inhalte besteht aus Techniken, die bei Modellen mit adaptivem Denken wirkungslos sind — „denke Schritt für Schritt", Superlative in der Rolle, emotionaler Druck. Was davon gilt und was nicht, steht in [1.5 · Was nicht funktioniert](#1.5/1.5_Strategisches-Prompt-Engineering.md#12-was-nicht-funktioniert--und-sicherheit).

**Keine Beratungsstudien als Belege.** Die Zahlen aus McKinsey und ähnlichen Erhebungen stehen bereits in den Kursdokumenten. Es sind Umfragewerte, keine Messungen — als Größenordnung brauchbar, als Nachweis nicht. Sie noch einmal zu verlinken, macht sie nicht belastbarer.

**Keine Videos zu Lewin und ADKAR.** Es gibt viele, und die meisten geben das 3-Stufen-Modell unkritisch als Lewins Werk aus — also genau den Fehler, den der Kurstag korrigiert.

**Keine Erklärvideos zu Kotter.** Aus demselben Grund: Ein großer Teil davon führt die 70-Prozent-Zahl als Kotters Befund an. Sie stammt nicht von ihm, und wer sie so weitergibt, gerät bei der ersten Nachfrage in Erklärungsnot. Die Originalquelle ist kürzer als die meisten dieser Videos.

---

*Diese Liste wächst mit dem Kurs. Kommt ein neuer Foliensatz dazu, werden bis zu drei Quellen ergänzt — nach denselben Kriterien, mit geprüften Links.*
