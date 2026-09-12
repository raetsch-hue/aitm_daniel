# Weiterführende Quellen

**Höchstens drei pro Thema — nur was den Aufwand wirklich lohnt**
Kurs: AI and Digital Transformation Management · neue fische × SPICED, 2026
Umfasst die Tage 1.4, 1.5, 2.1, 2.2, die Ergänzung zu 2.2, 3.3, 3.4 und 4.1 bis 4.5
Links der Tage 1.4 bis 2.2 geprüft am 01.09.2026, die der Tage 3.3 und 3.4 am 09.09.2026, die der Woche 4 am 12.09.2026

---

## Auswahlkriterium

Es gibt zu jedem dieser Themen hunderte Artikel und Videos. Die meisten wiederholen, was in den Folien steht. Aufgenommen ist nur, was **eine der drei Bedingungen** erfüllt:

- Es ist die **Primärquelle** zu etwas, das im Kurs nur als Behauptung auftaucht
- Es liefert die **Gegenposition**, die deine Argumentation belastbar macht
- Es ist **direkt anwendbar** — du kannst es morgen benutzen

Jeder Link wurde zum jeweils oben genannten Datum geprüft. Paywalls und Sprache sind vermerkt.

> **Grenze dieser Liste:** Sie deckt bisher nicht alle Kurstage ab. Die Dokumente der Wochen 3 und 4 führen ihre Quellen inzwischen selbst vollständig und kommentiert. Für 2.3 bis 3.2 und 3.5 stehen die kommentierten Quellen in den jeweiligen Tagesdokumenten, jeweils im letzten Abschnitt — sie sind hier noch nicht auf drei zusammengezogen und nicht gewichtet.

> **Zur Woche 4 gilt eine zusätzliche Regel:** Mehrere im Kurs genannte Zahlen halten der Prüfung nicht stand, und eine Fristenangabe ist überholt. Die unten aufgenommenen Quellen sind deshalb **die geprüften** — welche Kursangabe wo abweicht, steht in den Tagesdokumenten (`coursebook/woche-4/4.1/` Abschnitt 10, `4.2/` Abschnitt 10, `4.3/` Abschnitt 3, `4.4/` Abschnitt 5, `4.5/` Abschnitt 8).

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

**Zugang:** Über Hochschulbibliotheken zugänglich. Falls du nicht herankommst: Der Kern steht in [2.1 · Kritik und Alternativen](#woche-2/2.1/01_Change-Management-Lewin-ADKAR.md#10-kritik-grenzen-und-alternativen).

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

**Zugang:** Der Artikel liegt **hinter einer Bezahlschranke** — die Adresse steht oben, falls du über Hochschule oder Arbeitgeber Zugang hast. Falls nicht, ist nichts verloren: Die beiden Aussagen, auf die es ankommt — der Satz zum Überspringen von Schritten und Kotters *tatsächliche*, qualitative Formulierung zur Erfolgsquote — sind in [2.2 · Datenlage](#woche-2/2.2/2.2_Kotter-8-Schritte-Modell.md#2-kotter-und-die-datenlage--was-belegt-ist-und-was-nicht) wörtlich zitiert und eingeordnet.

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

> **Andere Rolle als die übrigen Abschnitte.** Diese drei Adressen sind nicht Vertiefung nach dem Block, sondern **Vorbereitung darauf**. Der Nachmittagsblock am Mittwoch ist der kürzeste der Woche, der Vormittag gehört dem Career Day. Wer die erste Quelle gelesen hat, spart im Block rund zwanzig Minuten. Aufbereitet und um das Verfahren, die Bewertungsregeln und eine Vorlage ergänzt steht alles in [Ergänzung 2.2](#woche-2/2.2/2.2_Ergaenzung-Force-Field-Analyse.md) — die Quellen darunter sind das Original dazu.

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

**Was du daraus mitnimmst:** Für die praktische Arbeit nichts, was nicht auch in den ersten beiden Quellen steht. Relevant, wenn du korrekt zitieren musst — und als Beleg dafür, dass die Kraftfeldanalyse **tatsächlich** von Lewin stammt, anders als das 3-Stufen-Modell ([Burnes-Vorbehalt](#woche-2/2.1/01_Change-Management-Lewin-ADKAR.md#2-kurt-lewin-person-werk-und-was-davon-wirklich-von-ihm-stammt)).

> **Wenn du nur eine Sache liest:** die Force-Field-Seite — und zwar heute, nicht nach dem Block. Sie ist die einzige Quelle dieser ganzen Liste, die morgen Nachmittag Zeit spart.

---

## Tag 3.3 — Implementierungspfade und Reifegrade

> **Vorbemerkung, die den Abschnitt erklärt.** Der Stoff des Tages steht seit dem Umbau in einer **Pflichtlektüre** — [Wie KI in Produktion kommt](https://neuefische-teaching.github.io/AIDTM/coursebook/woche-3/lektuere-implementierungspfade-w3.html). Sie ist keine weiterführende Quelle, sondern die Primärquelle; wer nur die Folien liest, hat den Tag nicht gehabt. Die drei Adressen hier sind das, was **hinter** der Lektüre liegt: einmal der Beleg für ihre Kernzahl, zweimal die Originale ihrer beiden Frameworks.

### 1. S&P Global Market Intelligence, Abbruchquoten bei KI-Initiativen ●●●

Erhebung 2025, über 1.000 Unternehmen in Nordamerika und Europa.
🔗 https://www.ciodive.com/news/AI-project-fail-data-SPGlobal/742590/ · Englisch, frei (Berichterstattung; die Erhebung selbst ist kostenpflichtig)

**Warum diese Quelle:** Sie erfüllt das erste Auswahlkriterium dieser Liste in Reinform — **Primärquelle zu etwas, das im Kurs nur als Behauptung auftaucht.** Die 42-%-Zahl trägt den ganzen Tag und war innerhalb von acht Tagen zwei verschiedenen Häusern zugeschrieben: erst einem Software-Anbieter, dann McKinsey. Belegt ist sie bei S&P Global — **und zwar für 2025.** Der Wert für 2024, den der Kurs nennt, lag bei **17 %**.

**Was du daraus mitnimmst:** Eine zitierfähige Fassung, die stärker ist als die falsche: *„42 % der Unternehmen haben 2025 die meisten ihrer KI-Initiativen abgebrochen — 2024 waren es 17 % (S&P Global Market Intelligence)."* Aus einem Standwert wird eine **Verdopplung in einem Jahr**, und das ist das bessere Argument. Zwei weitere Angaben aus derselben Erhebung, die der Kurs nicht nennt: im Schnitt **46 % der Proof-of-Concepts** verworfen, und als Haupthindernisse **Kosten, Datenschutz und Sicherheitsrisiken** — nicht fehlende Funktionen.

**Vorbehalt:** Umfragewerte, keine Messungen — wie bei allen Zahlen dieser Art. Als Größenordnung und als Trend brauchbar, als Nachweis nicht. Die verlinkte Seite ist Berichterstattung über die Erhebung; wer die Zahl in eine Vorlage schreibt, sollte die Fundstelle mit Erhebungsjahr angeben und nicht die Berichterstattung zitieren.

### 2. MIT Sloan Center for Information Systems Research (CISR) ●●

🔗 https://cisr.mit.edu · Englisch, frei

**Warum diese Quelle:** Das Reifegradmodell mit den vier Stufen **und ihren Zeiträumen** — 3–6, 6–12, 12–24, ab 24 Monate. Die Zeiträume sind der zitierfähige Teil und die Antwort auf die Frage, die in jedem Vorstandsgespräch kommt und auf die ein „das kommt darauf an" nicht reicht.

**Was du daraus mitnimmst:** Die Verteidigung gegen zu optimistische Roadmaps — und den Fehler, den das Modell sichtbar macht: *eine Plattform kaufen, die für eine Stufe gebaut ist, auf der man nicht steht.* Das ist der Kategorienfehler aus Tag 1.4, **zeitlich statt sachlich**, und er liegt genau wie jener **vor** der Bewertungsmatrix.

**Wenn die Zeit knapp ist:** Die Zeiträume und die Stufennamen stehen aufbereitet in [3.3, Abschnitt 4](#woche-3/3.3/3.3_Implementierungspfade-und-Workspace.md#f4). Die Seite selbst lohnt nur, wenn du korrekt zitieren musst.

### 3. OpenAI Enterprise, *AI in the Enterprise* (November 2025) ●●

**Warum diese Quelle:** Das Vier-Phasen-Framework mit den Fallbeispielen Figma und BBVA. Der Wert liegt nicht in der Phasenfolge, die ist naheliegend, sondern in den **typischen Fallen je Phase** — sie sind als Diagnoseliste verwendbar, und „Tool-first statt Problem-first" ist die Frage aus Tag 3.1, einen Schritt früher gestellt.

**Was du daraus mitnimmst:** Zwei Sätze, die im eigenen Vorhaben sofort greifen. Erstens: der Vorhabenname verrät die Falle — wer „RPA-Pilot" sagt, hat einen Werkzeugnamen, nicht ein Problem. Zweitens: **die Phasen überlappen sich**, das Champions-Netz muss weiter wachsen, sonst bricht die Adoption in Phase 4 ein.

**Vorbehalt:** **Anbieterpublikation** über die eigenen Unternehmenskunden. Die Fallzahlen sind benannt und damit nachprüfbar, die Auswahl der Fälle ist es nicht — es sind Erfolge. Wer daraus zitiert, sollte die Herkunft nennen; für eine Aussage über Scheiterquoten ist Quelle 1 zuständig.

> **Wenn du nur eine Sache liest:** die Pflichtlektüre — sie ist keine Empfehlung, sondern der Stoff. Und danach, wenn du die 42 % irgendwo verwenden willst: Quelle 1, fünf Minuten, und die Zahl hält.

---

## Tag 3.4 — Vendor Evaluation: die Entscheidung vertreten

> **Andere Rolle als die übrigen Abschnitte.** Der Kurstag bringt keinen neuen Stoff, sondern ein Verfahren. Diese drei Adressen liefern deshalb nicht Hintergrund zum Stoff, sondern die **Gegenprobe zum Verfahren**: eine gegen den Missbrauch der Gewichtung, eine gegen wirkungsloses Feedback, eine gegen die zu kurze Kriterienliste. Der Tagesseite sind fünf Quellen beigegeben; die beiden hier nicht aufgenommenen sind unter Nummer 2 vermerkt.

### 1. Hammond, Keeney & Raiffa (1998): The Hidden Traps in Decision Making ●●●

Harvard Business Review, September–Oktober 1998.
🔗 https://hbr.org/1998/09/the-hidden-traps-in-decision-making-2 · Englisch, teilweise kostenpflichtig

**Warum diese Quelle:** Sie beschreibt genau den Fehler, den die Kernaussage des Tages ermöglicht. Wenn die Gewichtung über die Empfehlung entscheidet, ist die Gewichtung auch die Stelle, an der sich unbemerkt manipulieren lässt — die Autoren führen das als *Confirming-Evidence-* und *Anchoring-*Falle: man setzt die Gewichte, bis das Ergebnis herauskommt, das man ohnehin wollte, und hält das Ergebnis anschließend für hergeleitet.

**Was du daraus mitnimmst:** Den Grund, warum eine Matrix ohne **Sensitivitätsprüfung** keine Absicherung ist, sondern eine Begründungsmaschine. Das Gegenmittel steht in [3.4 · Was fehlt](#woche-3/3.4/3.4_Die-Entscheidung-vertreten.md#g11): das wichtigste Kriterium um ±10 Prozentpunkte verschieben und prüfen, ob der Gewinner kippt. Zwei Minuten Arbeit, und aus einer Punktzahl wird eine Entscheidungsaussage.

**Vorbehalt:** Managementklassiker von 1998, keine empirische Arbeit — die einzelnen Fallen sind seither in der Entscheidungsforschung unterschiedlich gut bestätigt. Als Prüfraster brauchbar, als Beleg für einen Effektumfang nicht.

### 2. Hattie & Timperley (2007): The Power of Feedback ●●

Review of Educational Research 77(1), 81–112.
🔗 https://conselhopedagogico.tecnico.ulisboa.pt/files/sites/32/hattie-and-timperley-2007.pdf · Englisch, Fachaufsatz, frei

**Warum diese Quelle:** Die Grundlagenarbeit dazu, welches Feedback wirkt und welches nicht. Sie liefert die Begründung für die scheinbar kleinliche Regel im Feedback-Bogen des Tages: „mehr Details" und „besser strukturieren" sind kein Feedback. Feedback wirkt, wenn es die Lücke zwischen Ist und Soll **benennbar** macht — Rückmeldungen zur Person wirken am schwächsten, Rückmeldungen zur Aufgabe und zum Vorgehen am stärksten.

**Was du daraus mitnimmst:** Eine Sprachregelung für jedes Review, das du selbst gibst: die Stelle, das Soll, der nächste Schritt. Und die Einsicht, warum *„bezieht sich auf das Artefakt und nicht auf die Person"* im Glossar steht — das ist keine Höflichkeitsregel, sondern der Wirksamkeitsbefund.

**Zusatz, die vierte Quelle der Tagesseite:** Topping (2005), *Trends in Peer Learning* — 🔗 https://andymatuschak.org/files/2005%20Topping.pdf. Beantwortet die Anschlussfrage, **unter welchen Bedingungen Peer-Feedback scheitert**, und begründet die Lücke in [3.4 · Was fehlt, 11.5](#woche-3/3.4/3.4_Die-Entscheidung-vertreten.md#g11): Bewertende müssen vorher an einem Beispiel kalibriert werden, sonst streuen die Bögen mehr als sie zeigen.

### 3. TechnologyMatch: The Essential IT Vendor Selection Criteria and Checklist (2024) ●

🔗 https://technologymatch.com/blog/the-essential-it-vendor-selection-criteria-and-checklist · Englisch, frei

**Warum diese Quelle:** Sie ist **direkt anwendbar** — das dritte Auswahlkriterium dieser Liste. Neun Kriterienkategorien mit gewichteter Bewertung, und der Ertrag liegt nicht im Rahmen selbst, sondern im Abgleich: Die fünf oder sechs Kriterien des Kurses lassen sich daran auf Lücken prüfen, und die Lücken sind vorhersagbar dieselben — **Betrieb, Support, Exit**. Genau die Felder, die in [3.4 · Was eine Matrix nicht misst](#woche-3/3.4/3.4_Die-Entscheidung-vertreten.md#g10) als blinde Flecken stehen.

**Was du daraus mitnimmst:** Eine Checkliste für die halbe Stunde vor der Abgabe einer Vorlage. Nicht um die Matrix zu verlängern — sondern um zu entscheiden, was bewusst **nicht** bewertet wurde und in „Offene Fragen" gehört.

**Vorbehalt:** Anbieterblog, kein neutraler Rahmen und keine Primärquelle. Als Prüfliste brauchbar, in einer Arbeit nicht zitierfähig. Die fünfte Quelle der Tagesseite — der Research-In-Action-Report von 2021 — ist hier nicht aufgenommen: nur auf Anfrage erhältlich, fünf Jahre alt, und die Zahlen daraus stehen bereits in Tag 3.1.

> **Wenn du nur eine Sache liest:** Hammond, Keeney & Raiffa. Es ist der einzige Text, der die zentrale Aussage des Tages nicht bestätigt, sondern angreift — und deshalb der einzige, der die eigene Matrix belastbarer macht.

---

## Tag 4.1 — Stakeholder-Analyse und Power/Interest Grid

### 1. Die Normen, die den Gatekeeper erklären ●●●

**Arbeitnehmerkammer Bremen:** *Eine (betriebsverfassungs-)rechtliche Betrachtung von KI*
🔗 <https://www.arbeitnehmerkammer.de/betriebs-personalraete/digitalisierung/kuenstliche-intelligenz/eine-betriebsverfassungs-rechtliche-betrachtung-von-ki.html> · Deutsch, frei

**Warum diese Quelle:** Der Kurs sagt „§ 87 BetrVG" ohne Absatz. Das genügt für die eigene Rolle nicht — die Absatzangabe entscheidet darüber, **wann** eingebunden werden muss. Hier stehen die einschlägigen Normen im Zusammenhang: § 87 Abs. 1 Nr. 6 (Mitbestimmung bei Überwachungseignung), **§ 90 Abs. 1 Nr. 3** (Unterrichtung **bei der Planung**, KI seit 2021 ausdrücklich genannt), § 80 Abs. 3 S. 2 (Sachverständiger, Erforderlichkeit **unwiderleglich vermutet**), § 95 Abs. 2a (Auswahlrichtlinien).

**Was du daraus mitnimmst:** Die schärfere Diagnose zum Praxisfall des Tages. „Zu spät eingebunden" ist eine Prozessbeschreibung; **„Verstoß gegen § 90"** ist eine Auskunft — und sie verändert das Gespräch mit dem Sponsor, weil frühe Einbindung dann keine Höflichkeit mehr ist, sondern eine ohnehin bestehende Pflicht.

**Gelesen aus Sicht der Gegenseite** — genau deshalb lesenswert.

### 2. Die Gegenposition zum Kursfall ●●●

**Bird & Bird zu ArbG Hamburg, Beschluss vom 16.01.2024 (24 BVGa 1/24)**
🔗 <https://www.twobirds.com/de/insights/2024/germany/erstes-urteil-zu-rechten-des-betriebsrats-bei-einsatz-von-kuenstlicher-intelligenz> · Deutsch, frei

**Warum diese Quelle:** Der Kurs zeigt den Fall, in dem Mitbestimmung greift. Dies ist der dokumentierte Fall, in dem sie **nicht** greift — Browserzugriff, private Accounts, keine Unternehmenshardware, kein Zugriff auf Nutzungsdaten.

**Was du daraus mitnimmst:** Drei Prüffragen vor dem ersten Gespräch: *Läuft es auf unserer Hardware? Haben wir Zugriff auf die Nutzungsdaten? Entstehen personenbezogene Leistungsdaten?* Wer sie beantwortet hat, führt ein Fachgespräch statt einer Machtprobe.

**Vorbehalt:** erstinstanzlich, Eilverfahren, enge Konstellation.

### 3. Die Primärquelle zum Grid ●●

**Mendelow, A. (1981):** *Environmental Scanning — The Impact of the Stakeholder Concept.* ICIS 1981 Proceedings, Cambridge MA
🔗 <https://aisel.aisnet.org/icis1981/20/> · Englisch, frei, kurz

**Warum diese Quelle:** Weil der Kurs sie auf 1991 datiert und sich dabei selbst widerspricht (Tag 3.5 nennt 1981). Und weil sichtbar wird, dass die **vier Quadranten mit Handlungsanweisung** nicht von Mendelow stammen, sondern aus der Popularisierung durch Johnson & Scholes.

**Was du daraus mitnimmst:** Die Fähigkeit, korrekt zu zitieren — und zu wissen, dass „die Mendelow-Matrix" im Steuerkreis meistens die Johnson-Scholes-Fassung meint.

> **Wenn du nur eine Sache liest:** die Normenübersicht. Sie ist die einzige Quelle der Woche, die dir im realen Gespräch sofort nützt.

---

## Tag 4.2 — Key User und Champions-Programm

### 1. Der empirische Einwand gegen das Canvas ●●●

**Howell, J. M. & Higgins, C. A. (1990):** *Champions of Technological Innovation.* Administrative Science Quarterly 35(2), 317–341
🔗 <https://eric.ed.gov/?id=EJ411660> · Englisch, Fachaufsatz

**Warum diese Quelle:** Sie ist die einzige begutachtete Arbeit, die die Frage des Tages direkt beantwortet — *soll man Champions ernennen?* — und sie antwortet gegen den Kursvorschlag: **Eine formale Ernennung kann die intrinsische Motivation untergraben und den Erfolg gefährden.** 25 gematchte Paare, Fragebögen und Interviews.

**Was du daraus mitnimmst:** Die Trennung, die das Canvas brauchbar macht: **Zeit, Zugang, Kanal und Anerkennung formalisieren — die Tätigkeit nicht.** Und die Antwort auf den häufigsten Gegenvorschlag („dann benennen wir je Abteilung eine Person").

### 2. Die zitierfähigen Adoptionszahlen ●●●

**Microsoft & LinkedIn (2024):** *Work Trend Index — AI at Work Is Here. Now Comes the Hard Part.*
🔗 <https://www.microsoft.com/en-us/worklab/work-trend-index/ai-at-work-is-here-now-comes-the-hard-part> · Englisch, frei

**Warum diese Quelle:** Der Kurs stützt den Tag auf „68 gegen 23 Prozent" aus einer Quelle ohne Stichprobe und ohne Methode. Hier sind Stichprobe (31.000 Befragte, 31 Länder) und Fragestellung offengelegt: **75 % nutzen KI bei der Arbeit, 78 % davon mit eigenen Werkzeugen; 79 % der Führungskräfte halten Adoption für wettbewerbskritisch, 60 % sagen, es gebe weder Vision noch Plan.**

**Was du daraus mitnimmst:** Den Accountability Gap mit Zahl — und das stärkere Argument für das Programm: Es erzeugt nicht Nutzung, es macht **unkontrollierte Nutzung sichtbar.** Damit ist es zugleich eine Governance-Maßnahme.

**Vorbehalt:** Erhebung eines Anbieters, der KI-Werkzeuge verkauft. Richtung plausibel, Höhe interessengefärbt — und das gehört mitgesagt.

### 3. Das Dual Operating System im Original ●●

**Kotter, J. P. (2014):** *Accelerate: Building Strategic Agility for a Faster-Moving World.* Harvard Business Review Press · Englisch

**Warum diese Quelle:** Weil die Bedingung, unter der das Modell funktioniert — **echte Freiwilligkeit** —, in Nacherzählungen regelmäßig wegfällt. Genau diese Bedingung steht im Konflikt mit einem Canvas, das Auswahl, Rollenbeschreibung und Mandat festschreibt.

**Was du daraus mitnimmst:** Die Sprache, um den Widerspruch zu benennen, statt ihn zu übersehen.

> **Wenn du nur eine Sache liest:** Howell & Higgins. Vier Seiten Zusammenfassung genügen, und sie verändern, wie du Dimension 1 des Canvas ausfüllst.

---

## Tag 4.3 — Botschaft, Kanal und Kommunikationsplan

### 1. Die Absender-Regel, die im Kurs fehlt ●●●

**Prosci:** *Communications Checklist for Change Management*
🔗 <https://www.prosci.com/blog/communications-checklist-for-change-management> · Englisch, frei

**Warum diese Quelle:** Der Kurs ordnet **Kanäle** zu und lässt **Absender** aus. Prosci hat dazu die stabilste Aussage der Praxisliteratur: **Geschäftliche Gründe** wollen Beschäftigte von der **Führungsspitze** hören, **persönliche Auswirkungen** von der **direkten Führungskraft.**

**Was du daraus mitnimmst:** Eine zusätzliche Spalte im Engagement-Kalender und zwei vermiedene Standardfehler — die Projektleitung, die ankündigt, und die Townhall, die Jobfragen beantworten soll.

**Vorbehalt:** Beratungsforschung, Methodik nicht öffentlich. Über viele Erhebungswellen stabil.

### 2. Der belegte Ersatz für den Siemens-Fall ●●●

**Der Duolingo-Verlauf, April bis August 2025**
🔗 <https://www.prdaily.com/the-scoop-duolingo-ceo-walks-back-ai-first-memo/> · Englisch, frei

**Warum diese Quelle:** Der Siemens-Fall des Kurses ist ohne Quelle und ohne Messgröße. Dieser Verlauf ist mit Daten, Zitaten und der Korrektur durch die Unternehmensleitung dokumentiert — und er trägt dieselbe Lehre: **Die erste Botschaft war nicht falsch, sie beantwortete eine Frage, die niemand gestellt hatte.**

**Was du daraus mitnimmst:** Drei Lehren statt einer — interne KI-Kommunikation ist bei kundensichtbaren Produkten nicht intern; die Korrektur bestätigte die Diagnose aus dem Mund des Absenders; und gelöschte Beiträge sind selbst eine Botschaft.

### 3. Artikel 50 EU AI Act ●●

**Verordnung (EU) 2024/1689, Artikel 50 — Transparenzpflichten**
🔗 <https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32024R1689> · Deutsch, frei

**Warum diese Quelle:** Weil ein Teil dessen, was der Tag als Gestaltungsfrage behandelt, **seit dem 02.08.2026 Pflicht ist** — und diese Frist von der Verschiebung der Hochrisiko-Pflichten ausdrücklich **nicht** betroffen ist.

**Was du daraus mitnimmst:** Eine Kalenderzeile mit hartem Termin statt einer Tonempfehlung. Und einen Satz, der den Einwand *„müssen wir das so breit kommunizieren?"* nicht diskutiert, sondern erledigt.

> **Wenn du nur eine Sache liest:** die Prosci-Checkliste. Sie ist die einzige der drei, die jede künftige Kommunikation verbessert, nicht nur diese.

---

## Tag 4.4 — Executive Briefing

### 1. Die eine Quelle ohne Interessenlage ●●●

**McKinsey & Company:** *The State of AI*
🔗 <https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai> · Englisch, frei

**Warum diese Quelle:** Von den vier Belegen, die der Kurs für Block 3 anbietet, ist dies der einzige ohne Anbieterfinanzierung. Und er liefert die beiden Zahlen, die zwei der vier Einwände zugleich beantworten: **88 % der Organisationen setzen KI in mindestens einer Funktion ein (Vorjahr 78 %), 21 % haben dafür Arbeitsabläufe grundlegend verändert** — und diese Neugestaltung zählt zu den Faktoren mit dem stärksten Beitrag zur Ergebniswirkung.

**Was du daraus mitnimmst:** Wenn nur eine Zahl ins Deck darf, diese. Sie sagt, dass die Technologie nicht die Engstelle ist — und wohin das Geld gehört.

**Vorbehalt:** Beratungsbefragung, keine Messung. Als Größenordnung brauchbar, als Nachweis nicht.

### 2. Warum die Anordnung auf der Folie eine inhaltliche Entscheidung ist ●●●

**Columbia Accident Investigation Board (2003), Report Volume 1** — der Abschnitt zur technischen Kommunikation
🔗 <https://www.gocivilairpatrol.com/media/cms/Columbiapdf_5161B0B3295B0.pdf> · Englisch, frei

**Warum diese Quelle:** Sie ist der schärfste dokumentierte Beleg dafür, dass **Verdichtung Information verliert** — und dass die Überschrift im Kopf der Lesenden mehr Gewicht trägt als der Inhalt darunter. Das Board hielt fest, es sei leicht nachvollziehbar, dass eine leitende Führungskraft die betreffende Folie lese, ohne zu erkennen, dass es um eine lebensbedrohliche Lage gehe.

**Was du daraus mitnimmst:** Die Feedback-Dimension „Evidence" mit Nachdruck — *war die stärkste Zahl prominent oder vergraben?* Und die Regel: Eine Risikozeile in der Fußnote ist keine genannte Risikozeile.

### 3. Die Herkunft des Fünf-Block-Modells ●●

**Minto, B.:** *The Pyramid Principle* · Englisch

**Warum diese Quelle:** Das Modell des Tages ist nicht neu — es ist Mintos **Antwort-zuerst**-Aufbau mit SCQA-Eröffnung, seit den späten 1970er-Jahren in der Beratungspraxis. Wer die Herkunft kennt, kann die Reihenfolge **begründen**, statt sie zu behaupten — und das ist genau der Einwand, der im Raum kommt.

**Was du daraus mitnimmst:** Die ersten beiden Kapitel genügen. Dazu die Gegenposition zum Deck-Format überhaupt: In vielen Häusern fällt die Entscheidung **beim Lesen der Vorlage**, nicht im Meeting.

> **Wenn du nur eine Sache liest:** die zwei McKinsey-Zahlen. Sie sind der einzige Beleg des Tages, den du ohne Vorbehaltssatz vortragen kannst.

---

## Tage 4.5 — Synthese, Governance und die Fristen

### 1. Die aktuelle Fristenlage zum EU AI Act ●●●

**Gibson Dunn:** *EU AI Act Omnibus Agreement — Postponed High-Risk Deadlines and Other Key Changes*
🔗 <https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/> · Englisch, frei

**Warum diese Quelle:** Weil die Angabe des Kurses — *„erste Hochrisiko-Anforderungen ab August 2026"* — überholt ist. Hochrisiko nach **Anhang III jetzt 02.12.2027**, nach **Anhang I 02.08.2028**; **Artikel 50 unverändert seit 02.08.2026**; Reallabore 02.08.2027; Artikel 4 (KI-Kompetenz) abgeschwächt.

**Was du daraus mitnimmst:** Die Fähigkeit, dieselbe Empfehlung mit einer Begründung vorzutragen, die der Rechtslage standhält. **Eine überholte Frist im eigenen Vortrag beschädigt auch die richtigen Aussagen daneben.**

**Vorbehalt:** Kanzleianalyse, Stand Sommer 2026. Keine Rechtsberatung — vor einer Aussage mit Außenwirkung den aktuellen Stand prüfen.

### 2. Was ohne den AI Act schon heute gilt ●●●

**DSGVO, Artikel 22 und Artikel 35** (mit Art. 37–39 zur Datenschutzbeauftragten)
🔗 <https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679> · Deutsch, frei

**Warum diese Quelle:** Weil die Fristverschiebung den Kurzschluss nahelegt, man habe bis Ende 2027 Zeit. **Artikel 22** gibt das Recht, nicht einer ausschließlich automatisierten Entscheidung unterworfen zu werden, und den Anspruch auf **Eingreifen einer Person** — das ist Human Oversight, heute geltend. **Artikel 35** verlangt die Folgenabschätzung bei hohem Risiko.

**Was du daraus mitnimmst:** Den Argumentationswechsel für die zweite W5-Frage: **mit Artikel 22 DSGVO begründen, nicht mit Artikel 14 AI Act.** Aussage behalten, Beleg austauschen.

### 3. Eine RACI-Vorlage für KI-Governance ●●

**VerifyWise:** *AI Lifecycle RACI Framework*
🔗 <https://verifywise.ai/ai-governance-library/organizational-roles-and-processes/raci-matrix-ai-governance-template> · Englisch, frei

**Warum diese Quelle:** Die drei W5-Fragen enden in drei Zeilen eines RACI — DPO, Human Oversight, Compliance-Accountable. Hier gibt es die Vorlage dafür, statt sie neu zu erfinden.

**Was du daraus mitnimmst:** Ein Ausgangsraster, das in Woche 5 in ISO 42001 einsortiert wird.

> **Wenn du nur eine Sache liest:** die Fristenübersicht. Sie ist die einzige Korrektur dieser Woche, die dich unmittelbar vor einer falschen Aussage im Steuerkreis bewahrt.

---

## Was hier bewusst nicht steht

**Keine Prompt-Tipp-Sammlungen und keine „50 besten Prompts"-Videos.** Ein großer Teil dieser Inhalte besteht aus Techniken, die bei Modellen mit adaptivem Denken wirkungslos sind — „denke Schritt für Schritt", Superlative in der Rolle, emotionaler Druck. Was davon gilt und was nicht, steht in [1.5 · Was nicht funktioniert](#woche-1/1.5/1.5_Strategisches-Prompt-Engineering.md#12-was-nicht-funktioniert--und-sicherheit).

**Keine Beratungsstudien als Belege.** Die Zahlen aus McKinsey und ähnlichen Erhebungen stehen bereits in den Kursdokumenten. Es sind Umfragewerte, keine Messungen — als Größenordnung brauchbar, als Nachweis nicht. Sie noch einmal zu verlinken, macht sie nicht belastbarer.

**Keine Videos zu Lewin und ADKAR.** Es gibt viele, und die meisten geben das 3-Stufen-Modell unkritisch als Lewins Werk aus — also genau den Fehler, den der Kurstag korrigiert.

**Keine Erklärvideos zu Kotter.** Aus demselben Grund: Ein großer Teil davon führt die 70-Prozent-Zahl als Kotters Befund an. Sie stammt nicht von ihm, und wer sie so weitergibt, gerät bei der ersten Nachfrage in Erklärungsnot. Die Originalquelle ist kürzer als die meisten dieser Videos.

---

*Diese Liste wächst mit dem Kurs. Kommt ein neuer Kurstag dazu, werden bis zu drei Quellen ergänzt — nach denselben Kriterien, mit geprüften Links und mit dem Prüfdatum im Kopf.*
