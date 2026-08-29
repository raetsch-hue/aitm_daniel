# Weiterführende Quellen

**Höchstens drei pro Thema — nur was den Aufwand wirklich lohnt**
Kurs: AI and Digital Transformation Management · neue fische × SPICED, 2026
Geprüft am 28.08.2026

---

## Auswahlkriterium

Es gibt zu jedem dieser Themen hunderte Artikel und Videos. Die meisten wiederholen, was in den Folien steht. Aufgenommen ist nur, was **eine der drei Bedingungen** erfüllt:

- Es ist die **Primärquelle** zu etwas, das im Kurs nur als Behauptung auftaucht
- Es liefert die **Gegenposition**, die deine Argumentation belastbar macht
- Es ist **direkt anwendbar** — du kannst es morgen benutzen

Jeder Link wurde am 28.08.2026 geprüft. Paywalls und Sprache sind vermerkt.

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

## Was hier bewusst nicht steht

**Keine Prompt-Tipp-Sammlungen und keine „50 besten Prompts"-Videos.** Ein großer Teil dieser Inhalte besteht aus Techniken, die bei Modellen mit adaptivem Denken wirkungslos sind — „denke Schritt für Schritt", Superlative in der Rolle, emotionaler Druck. Was davon gilt und was nicht, steht in [1.5 · Was nicht funktioniert](#1.5/1.5_Strategisches-Prompt-Engineering.md#12-was-nicht-funktioniert--und-sicherheit).

**Keine Beratungsstudien als Belege.** Die Zahlen aus McKinsey und ähnlichen Erhebungen stehen bereits in den Kursdokumenten. Es sind Umfragewerte, keine Messungen — als Größenordnung brauchbar, als Nachweis nicht. Sie noch einmal zu verlinken, macht sie nicht belastbarer.

**Keine Videos zu Lewin und ADKAR.** Es gibt viele, und die meisten geben das 3-Stufen-Modell unkritisch als Lewins Werk aus — also genau den Fehler, den der Kurstag korrigiert.

---

*Diese Liste wächst mit dem Kurs. Kommt ein neuer Foliensatz dazu, werden bis zu drei Quellen ergänzt — nach denselben Kriterien, mit geprüften Links.*
