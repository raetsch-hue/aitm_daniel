# Lerntagebuch

**AI and Digital Transformation Management** · neue fische × SPICED, 2026
**Stand:** nach Tag 2.2 (Mittwoch, Woche 2) · angelegt 2026-09-01

Dieses Tagebuch fasst zusammen, was bis einschließlich Tag 2.2 durchgenommen wurde — Inhalt, Gewichtung, Belege — und lässt an jeder Stelle Platz für das, was *ich* daraus mitgenommen habe. Es folgt dem Prinzip der Bibliothek: **ergänzen, nicht ersetzen.** Neue Fassungen kommen unter die alte, damit der Lernweg nachvollziehbar bleibt.

Gewichtung wie im [Kursindex](#l1): ●●● frei erklären können · ●● wissen, dass es existiert und wo es steht · ● einmal gelesen, nachschlagbar.

**Inhalt:** [0 Mein Vorhaben](#l0) · [1 Die neun Sätze](#l1) · [2 Woche 1: Grundlagen](#l2) · [3 Tag 1.4](#l3) · [4 Tag 1.5](#l4) · [5 Tag 2.1](#l5) · [6 Tag 2.2](#l6) · [7 Querverbindungen](#l7) · [8 Selbsttest](#l8) · [9 Kompetenzstand](#l9) · [10 Offene Fragen](#l10) · [11 Meine Artefakte](#l11) · [12 Fortschreiben](#l12)

---

<a id="l0"></a>
## 0. Mein Vorhaben — der Kontext, auf den alles angewendet wird

Alle Methoden dieses Kurses werden an einem eigenen Vorhaben geübt. Aus meinen Bibliothekseinträgen lässt sich der Stand so zusammenfassen:

- **Organisation:** Behörde
- **Vorhaben:** RPA-Pilot auf einem Fachverfahren, Sonderfälle bleiben bei den Mitarbeitenden
- **Messgrößen definiert:** Bearbeitungszeit, Fehlerquote — *„Messbarkeit ist noch keine Wirtschaftlichkeit"*
- **Reifegradprofil** (Gruppeneinschätzung vom 27.08.2026): Kultur **1** (niedrigste Stufe des Profils), Technologie **2** neben Private Cloud, Data Warehouse und KI-Kompetenzzentrum — erklärungsbedürftig
- **Stakeholder:** Finanzleitung (Freigabe), Sachbearbeitung (Betroffene), Personalvertretung (benannt, **nicht beteiligt**)
- **Größte Bremse (Stärke 5):** kein vollständiger Business Case — ein Tor, keine Stimmung

_Eigene Ergänzung / Korrektur (Stand heute):_

> _…_

<sub>[↑ Inhalt](#l0)</sub>

---

<a id="l1"></a>
## 1. Die neun Sätze — der ganze Stoff bis 2.2

Der Kursindex verdichtet alles auf neun Sätze. Sie sind die Rückgratliste: wenn ich einen davon nicht in eigenen Worten erklären kann, weiß ich, wo ich nachlesen muss.

| # | Satz | Wo er herkommt |
|---|---|---|
| 1 | **Die Kategorie entscheidet, nicht die Technologie.** RPA, Predictive ML, GenAI und Agentic AI lösen verschiedene Probleme — der häufigste teure Fehler ist die falsche Kategorie, nicht der falsche Anbieter. | [1.4](#l3) |
| 2 | **Der Reifegrad begrenzt, was möglich ist.** Nicht der Durchschnitt zählt, sondern die schwächste relevante Dimension. | [1.4](#l3) |
| 3 | **Adoption ist nicht Wertschöpfung.** 72 % nutzen GenAI, 30 % sind mit dem ROI zufrieden. Die Lücke dazwischen ist Change Management. | [1.4](#l3) |
| 4 | **B = f(P, E): Verhalten ändert sich über das Umfeld, nicht über Überzeugung.** Widerstand ist keine Personeneigenschaft. | [2.1](#l5) |
| 5 | **Die ADKAR-Reihenfolge ist die ökonomische Aussage.** Training vor gelöstem Desire ist verbranntes Budget. Der erste Score ≤ 3 ist der Ansatzpunkt. | [2.1](#l5) |
| 6 | **Was das Modell nicht wissen kann, erfindet es** — plausibel genug, dass es niemand merkt. Kontext und prüfbares Erfolgskriterium sind die beiden Schrauben mit dem größten Hebel. | [1.5](#l4) |
| 7 | **Alles, was du zweimal tippst, gehört nicht in den Prompt.** Kontext gehört in Dateien, nicht in Chatverläufe. | [1.5](#l4) |
| 8 | **Die Vorbereitung ist die halbe Veränderung.** Vier von Kotters acht Schritten liegen vor der ersten sichtbaren Änderung — und dort scheitern die meisten Vorhaben. | [2.2](#l6) |
| 9 | **Hemmende Kräfte abbauen schlägt treibende verstärken.** Eine weitere Mail ist eine treibende Kraft; ein weggeräumtes Hindernis bewegt mehr — und ein Kraftfeld ohne Maßnahmenzeile hat gar nichts bewegt. | [2.2 Ergänzung](#l6) |

_Welchen dieser neun Sätze kann ich noch **nicht** frei erklären?_

> _…_

<sub>[↑ Inhalt](#l0)</sub>

---

<a id="l2"></a>
## 2. Woche 1 — Grundlagen und Handwerk

*Rekonstruiert aus den Repo-Aufträgen der Woche 2; für die Tage 1.1 bis 1.3 liegt mir keine Langfassung vor. Hier gehört meine eigene Erinnerung hinein.*

**Was entstanden ist**

| Artefakt | Was es leistet | Ablage |
|---|---|---|
| Repository-Setup | Alles an einem Ort, versionierbar. Am Montag ist dafür die Zeit draufgegangen — laut Kurs richtig so | Repo-Wurzel |
| Manual of Me | Wie ich arbeite, für andere lesbar | `artefakte/woche-01/` |
| Lernziele | Was ich in diesem Kurs erreichen will | `artefakte/woche-01/` |
| Die Gegenrede | Eine Position bewusst gegen den Strich gebürstet | `artefakte/woche-01/` |
| Unternehmensprofil | Der Kontext meines Vorhabens — Grundlage für alles Weitere | `artefakte/woche-01/` |
| `kompetenzen.md` | Ein Satz nach dem Muster **„Ich kann X, nachgewiesen durch Y in Kontext Z"** | Repo-Wurzel |
| `bibliothek/prompting.md` | RTCO, die sechs Stellschrauben, wo Kontext wohnt — in eigenen Worten, ohne auf die Folien zu schauen | `bibliothek/` |

**Das Prinzip dahinter** ●●●
*Was du nicht ohne Folie hinschreibst, weißt du noch nicht.* Deshalb entstehen die Bibliothekseinträge aus dem Gedächtnis und werden danach korrigiert — nicht abgeschrieben.

_Was ich aus Woche 1 tatsächlich mitgenommen habe:_

> _…_

_Was noch offen ist (fehlende Artefakte, halbe Einträge):_

> _…_

<sub>[↑ Inhalt](#l0)</sub>

---

<a id="l3"></a>
## 3. Tag 1.4 — Vier Wellen, KI-Kategorien, Hype Cycle

Langfassung: `coursebook/1.4/1.4_Vier-Wellen-KI-Kategorien-Hype-Cycle.md`

### Die vier Kategorien ●●●
Jede Vorhabenbewertung beginnt hier — mit Voraussetzung, ROI-Klarheit und Hauptrisiko je Kategorie:

| Frage | Antwort | Kategorie |
|---|---|---|
| Ist die Aufgabe **regelhaft beschreibbar**? | ja | **RPA** |
| Geht es um eine **Zahl aus historischen Mustern**? | ja | **Predictive ML** |
| Geht es um **Sprache, Variabilität, Entwurf**? | ja | **GenAI** |
| Braucht es **mehrere Schritte mit eigener Planung**? | ja | **Agentic AI** — und dann klein anfangen |

**Für mein Vorhaben relevant:** Ein RPA-Pilot auf strukturierten, wiederkehrenden Vorgängen ist genau der Fall, in dem GenAI die falsche Wahl wäre — deterministisch, prüfbar, ohne API-Kosten pro Vorgang, ohne Datenschutzfrage.

### Reifegrad als Engpass, nicht als Note ●●●
Zwei Firmen mit Mittelwert 3,0 brauchen völlig verschiedene Maßnahmen. Es zählt die **schwächste relevante** Dimension, nicht der Durchschnitt.
**Mein Fall:** Kultur 1 ist die schwächste Dimension des Profils — und Kultur ist für einen Pilot mit Betroffenen relevant, also begrenzt sie.

### Die drei Framing-Fragen ●●●
Die Standardreaktion auf jeden KI-Vorschlag: **Welle · Gap · Kategorie.**

### Weitere Punkte
- **Warum keine Welle übersprungen wird** ●● — Solow-Paradox und Produktivitäts-J-Kurve. Das Argument, mit dem Vorleistungen ins Budget kommen.
- **Der Hype Cycle und seine Grenzen** ●● — als Kommunikationswerkzeug stark, als Rechengrundlage wertlos. **Der Trough ist eine Verzweigung, keine Durchgangsstation.**
- **Fehlerfortpflanzung bei Agentic AI** ●● — 95 % je Schritt sind bei zehn Schritten 60 % gesamt. Erklärt, warum Demos laufen und Produktion nicht.
- **Das Wellenmodell selbst** ● — Ordnungsraster ohne kanonische Quelle: nützlich zum Erklären, nicht zum Zitieren.

### Die vier Fälle
| Fall | Wofür er steht | Gewicht |
|---|---|---|
| **Klarna** | Effizienz gemessen, Qualität nicht — Peak und Korrektur in 18 Monaten | ●●● |
| **Zillow Offers** | Prognosemodell driftet still, 420 Mio. USD in einem Quartal | ●● |
| **Air Canada** | Du haftest für das, was dein Chatbot sagt | ●● |
| **Amazon Recruiting** | ML schreibt die Vergangenheit fort — auch die unerwünschte | ● |

Details und Quellen: `examples/fallbeispiele.md`

_Mein Mitnahmesatz aus 1.4:_

> _…_

_Wo ich das schon angewendet habe:_

> _…_

<sub>[↑ Inhalt](#l0)</sub>

---

<a id="l4"></a>
## 4. Tag 1.5 — Strategisches Prompt Engineering

Langfassung: `coursebook/1.5/1.5_Strategisches-Prompt-Engineering.md`

### Die vier ●●●-Punkte

**Kontext: was das Modell nicht weiß, erfindet es.** Ursache Nummer eins für unbrauchbare Ergebnisse. Prüffrage: *Woher soll es das wissen?*

**Erfolgskriterium: was du nicht nachzählen kannst, ist geschätzt.** Ohne Kriterium ist auch die Selbstprüfung wertlos — und eine Aufgabe ohne Kriterium ist nicht automatisierbar.

**Wo der Inhalt wohnt: Prompt, Datei, Projektanweisung.** Die Schraube mit dem größten Hebel über die Zeit. *Das ist der Übergang vom Prompten zum Bauen.*

**Die Diagnoseliste.** Sieben Symptome, sieben Ursachen — das Blatt, das beim Arbeiten daneben liegt.

### Was ich mir am ehesten falsch merke ●●
- **„Denke Schritt für Schritt" ist überholt.** Bei Reasoning-Modellen wirkt nicht die Denkaufforderung, sondern eine **inhaltliche Prüfanweisung**: *„Prüfe vor der Empfehlung, ob unser Reifegrad in der Dimension Daten die Voraussetzung erfüllt. Wenn nicht, sag das zuerst."*
- **Selbstprüfung funktioniert nur gegen prüfbare Formkriterien** — Länge, Struktur, geforderte Bestandteile, Abgleich mit mitgegebenem Material. Gegen faktische Richtigkeit ohne externe Quelle bringt sie wenig bis nichts: ein Modell, das eine Falschaussage erzeugt hat, hält sie für richtig. Wer das verwechselt, baut sich eine Selbstbestätigungsmaschine.
- **Context Rot:** mehr Kontext wird schlechter, nicht besser. Information an den Rändern langer Eingaben wird zuverlässiger genutzt als in der Mitte.
- **Struktur:** XML-Tags, Material oben, Frage unten. Eine der wenigen Regeln mit belegter Zahl (bis zu 30 % bessere Antwortqualität).
- **Beispiele schlagen Beschreibungen** — und ein Gegenbeispiel mit Begründung wirkt stärker als ein viertes gutes.
- **Prompt Injection:** Fremdmaterial ausdrücklich als Daten deklarieren, niemals als Anweisung, und nie ungeprüft handeln lassen.
- **RTCO** ● ist ein Merkraster, kein Verfahren: mehrere Aufgaben gehören in mehrere Prompts.

### Die praktische Konsequenz für dieses Tagebuch
Der KI-Gegenprobe-Prompt aus Woche 2 lebt genau von diesen Regeln:
> *„Bau daraus einen kurzen Fall … **Nimm nur, was in der Datei steht. Ergänze nichts aus deinem eigenen Wissen.**"*
Ohne den letzten Satz füllt das Modell die Lücken selbst — und die Prüfung prüft nichts.

_Mein Mitnahmesatz aus 1.5:_

> _…_

_Welche Stellschraube merke ich am ehesten, wenn sie fehlt?_

> _…_

<sub>[↑ Inhalt](#l0)</sub>

---

<a id="l5"></a>
## 5. Tag 2.1 — Lewin und ADKAR

Langfassung: `coursebook/2.1/01_Change-Management-Lewin-ADKAR.md` · Eigener Eintrag: `bibliothek/lewin-adkar.md`

### B = f(P, E) ●●●
Verhalten ist eine Funktion von Person **und** Umfeld. Der Merksatz verschiebt den Blick vom Individuum aufs System — und damit die Maßnahme. **B = f(P, E) ist in erster Linie ein Auftrag an die Führung, nicht an die Mitarbeitenden.**

Beispiel aus dem Kurs: Ein Team nutzt ein neues Tool nicht. Naheliegende Erklärung „Widerstand" (P). Tatsächlich: die Bearbeitungszeit ist als KPI hinterlegt · der Hinweis „keine Kundendaten eingeben" macht den Hauptanwendungsfall unmöglich · die Teamleitung nutzt es selbst nicht. Alle drei sind E-Faktoren, keiner ist durch ein Training behebbar.

### ADKAR: Reihenfolge und Barrier Point ●●●
Awareness · Desire · Knowledge · Ability · Reinforcement. Jede Stufe pro Person oder Gruppe 1–5 bewerten; **der erste Wert ≤ 3 ist der Barrier Point.** Alles danach ist wirkungslos, solange er nicht gelöst ist.

**Knowledge kann Desire nicht ersetzen** ●●● — Schulungsbudget vor gelöstem Desire ist verloren. Der teuerste Standardfehler bei KI-Rollouts.

**Die Integration** ●●● — *Lewin sagt wann, ADKAR sagt was.* Zusammen ergibt es eine Interventionslogik.

### Die Kraftfeldanalyse ●●
Praktisch stärker als das 3-Stufen-Modell. Jede Situation ist ein Quasi-Gleichgewicht aus treibenden und hemmenden Kräften. Lewins übersehener Befund: **hemmende Kräfte abbauen wirkt stärker als treibende verstärken.** Eine weitere All-Hands-Mail ist eine treibende Kraft; eine freigegebene, datenschutzkonform geprüfte Tool-Instanz mit klarer Richtlinie räumt eine hemmende weg.

### Was ich mir zur Glaubwürdigkeit merken muss ●●
- **Unfreeze ohne Angst:** Dringlichkeit statt Druck.
- **Refreeze ist Struktur, nicht Kommunikation:** Solange der alte SOP gilt, gewinnt der alte SOP. **Der Projektabschluss ist der Moment mit dem höchsten Rückfallrisiko**, nicht der Moment des Erfolgs.
- **Der Burnes-Vorbehalt:** Lewin hat das 3-Stufen-Modell nie so veröffentlicht. Vier Wörter Vorsicht schützen die eigene Glaubwürdigkeit.
- **Die 70-Prozent-Zahl:** als Dringlichkeitssignal brauchbar, als Business Case nicht.

### Die zwei Studien, die den Kern belegen
| Studie | Kernbefund | Gewicht |
|---|---|---|
| **Lewin, Food Habits (1943)** | Vortrag 3 %, Gruppendiskussion 32 % — bei identischem Informationsgehalt | ●●● |
| **Coch & French (1948)** | Widerstand ist eine Funktion des Beteiligungsgrades, keine Eigenschaft der Belegschaft | ●● |

_Mein Mitnahmesatz aus 2.1:_

> _…_

_Mein Barrier Point je Gruppe im eigenen Vorhaben (Sachbearbeitung / Teamleitung / IT / Finanzleitung):_

> _…_

<sub>[↑ Inhalt](#l0)</sub>

---

<a id="l6"></a>
## 6. Tag 2.2 — Kotters acht Schritte und das Kraftfeld als Werkzeug

Langfassungen: `coursebook/2.2/2.2_Kotter-8-Schritte-Modell.md` und `coursebook/2.2/2.2_Ergaenzung-Force-Field-Analyse.md` · Eigener Eintrag: `bibliothek/kotter-forcefield.md`

### Die acht Schritte und ihre typischen Fehler ●●●
Die einzige Handlungsanleitung im Werkzeugkasten — sie sagt, was als Nächstes zu tun ist.

### Die Rückwärtsdiagnose ●●●
**Stockt es, ist fast immer ein *früherer* Schritt offen.** So wird das Modell im Alltag benutzt, nicht als Checkliste von vorn.

### Schritte 1–4 sind die halbe Veränderung ●●●
Vier von acht Schritten liegen vor der ersten sichtbaren Änderung. In der Praxis kehrt sich die Verteilung um: der Löwenanteil des Budgets liegt in Schritt 5 und 6 (Werkzeuge, Schulungen, Piloten), die Schritte 1 bis 4 werden in einem Kick-off abgehandelt. **Das ist der Standardaufbau eines Vorhabens, das später als „Widerstand in der Organisation" scheitert.**

### Zu früh den Sieg erklären ●●●
Der einzige Fehler, den man **im Moment des Erfolgs** macht — deshalb schützt Erfahrung nicht davor. Die Siegeserklärung ist kein Kommunikationsfehler, sondern ein **Ressourcenereignis**: sie beendet Aufmerksamkeit, Budget und Rollen.

### Die vier Zahlen aus dem Original ●●
Über 50 % scheitern in Phase 1 · 75 % des Managements müssen überzeugt sein · die Vision wird um den **Faktor 10** unterkommuniziert · die Verankerung dauert 5 bis 10 Jahre. Aus Beratungsbeobachtung an über 100 Unternehmen — als Muster aussagekräftig, als Statistik nicht.

### Weitere Punkte ●●
- **Kotter × ADKAR:** *Kotter ist der Kompass, ADKAR das Thermometer.* Den größten Zusatznutzen bringt ADKAR bei Schritt 4 und 5.
- **Vision, 5-Minuten-Test:** In eigenen Worten wiedergebbar? Zustand oder Projekt? Könnte man widersprechen? Drei Fragen, die 90 % aller „Visionen" als Projektpläne entlarven.
- **Der blockierende Vorgesetzte** ist nicht nur ein Hindernis, sondern ein Beweis, dass es nicht ernst gemeint ist.
- **Quick Wins werden geplant:** Die Auswahl entscheidet, nicht die Ausführung. Prüffrage nicht „können wir das schnell?", sondern ***wessen* Alltag wird spürbar besser, und wird diese Person davon erzählen?**
- **Die Datenlage:** **Die 70-Prozent-Zahl stammt nicht von Kotter.** Wer sie ihm zuschreibt, ist bei der ersten Nachfrage angreifbar.
- **Dual Operating System** ● — Hierarchie und freiwilliges Netzwerk parallel; die Antwort auf den Refreeze-Einwand. Funktioniert nur mit echter Freiwilligkeit.

### Das Kraftfeld als Arbeitswerkzeug (Ergänzung) ●●●
Acht Verfahrensschritte von Ist/Soll bis Maßnahmenplan. Die Punkte, die zählen:

- **Ansatzpunkte wählen: stark UND beeinflussbar.** Der Schritt, der am häufigsten übersprungen wird — *Arbeit an schwachen, leicht beeinflussbaren Kräften fühlt sich wie Fortschritt an und bewegt nichts.*
- **Kotter-Schritt 5 = Force-Field-Analyse.** Kotter sagt „remove obstacles" und lässt offen, welche. Das Kraftfeld liefert die Rangfolge.
- **Drei Kraftcluster:** Substanz und Prozess · menschliche Seite · Kontext und Umfeld. **Der dritte wird regelmäßig vergessen — und enthält die stärksten Kräfte.**
- **Bewerten ohne Scheingenauigkeit:** Summen sind Vergleiche, keine Messungen. **Eine einzelne 5 schlägt drei Zweien.**
- **Die Analyse-Falle:** Wer mit dem Bild aufhört, hat nichts getan. Ein Kraftfeld ohne Maßnahmenzeile hat nichts bewegt.
- **Kraftfeld → ADKAR-Übersetzung:** jede hemmende Kraft einer ADKAR-Stufe zuordnen — Rangfolge nach Wirkung *und* nach Zielgruppe.
- **Die letzte Spalte macht den Unterschied:** „Schulung durchgeführt" ist kein Ergebnis; „drei von fünf Teams haben in der Folgewoche mindestens einmal ohne Aufforderung genutzt" ist eines.

### Die drei Fälle
| Fall | Wofür er steht | Gewicht |
|---|---|---|
| **Kodak** | Technologie, Prognose und Zeit vorhanden — nur keine Dringlichkeit. Erfunden 1975, insolvent 2012 | ●●● |
| **Ford / Mulally** | Koalition entsteht durch Format und psychologische Sicherheit, nicht durch Benennung | ●● |
| **Kotters 12 Projekte** | Sieg erklärt, Veränderung zwei Jahre später verschwunden | ●● |

### Was ich in meinem eigenen Eintrag schon erarbeitet habe
Drei Bremskräfte mit Stärke und Abbaupfad — fehlender Business Case (5) · unbeantwortete Rollenfrage plus nicht beteiligte Personalvertretung (4) · angreifbare Reifegradgrundlage (4). Dazu die bewusste Entscheidung, den technischen Einwand *„direkte Schnittstelle wäre stabiler als RPA auf einer Oberfläche"* **nicht** ins Kraftfeld zu schreiben: er ist ein offener Sachvergleich, kein Hindernis. Ihn als Kraft zu führen, würde ihn zu etwas erklären, das wegzuräumen ist — und das wäre der Fehler.
→ Das ist genau der Gedanke, den Tag 2.4 später als „Widerstand, der recht hat" systematisiert. Notiz an mich: **der Punkt war vor der Lektüre schon da.**

_Mein Mitnahmesatz aus 2.2:_

> _…_

<sub>[↑ Inhalt](#l0)</sub>

---

<a id="l7"></a>
## 7. Querverbindungen — hier entsteht der eigentliche Wert

Die Tage sind kein Nebeneinander. Diese Verbindungen tragen den Kurs:

| Verbindung | Was sie bedeutet |
|---|---|
| **Reifegrad (1.4) → Barrier Point (2.1)** | Beides sind Engpassanalysen: 1.4 fragt, was die *Organisation* blockiert, 2.1, was die *Person* blockiert. Ein Vorhaben braucht beide Antworten |
| **Adoption ≠ Wertschöpfung (1.4) → Change Management (2.1)** | Die Lücke zwischen 72 % Nutzung und 30 % ROI-Zufriedenheit ist keine Technikfrage. Sie ist die Existenzberechtigung dieser Rolle |
| **Erfolgskriterium (1.5) → Reifegraddefinition (1.4)** | „Daten: Stufe 3" ist wertlos, „Stammdaten zentral gepflegt, nicht validiert, kein dokumentiertes Regelwerk" ist prüfbar. Dieselbe Regel, zwei Kontexte |
| **Kontext ins Repo (1.5) → alles Weitere** | Organisation, Reifegrad und Pilot aus 1.4 sind der Kontext, mit dem 1.5 arbeitet. Wer 1.4 vage lässt, kann 1.5 nicht nutzen |
| **Kotter Schritt 4+5 (2.2) → ADKAR Barrier Point (2.1)** | Kotter sagt, dass Freiwillige zu gewinnen und Hindernisse zu beseitigen sind — nicht, *bei wem welches* liegt. Das ADKAR-Scoring liefert genau das |
| **Blockierender Vorgesetzter (2.2) → Kraftfeld (2.1)** | Derselbe Befund in zwei Sprachen: die stärkste hemmende Kraft abbauen schlägt jede zusätzliche treibende |
| **Refreeze (2.1) = Schritt 8 (2.2) — und beide brechen bei KI** | Verankern setzt einen stabilen Endzustand voraus, den es bei KI nicht gibt. Beide Male lautet der Ausweg: **die Fähigkeit verankern, nicht das Werkzeug** |
| **Die 70-Prozent-Zahl (2.1) und ihre Zuschreibung (2.2)** | Dieselbe Zahl, zweimal unbelegt — einmal in der Herkunft, einmal in der Urheberschaft. Ein Muster dafür, wie Kennzahlen im Change-Diskurs entstehen |
| **B = f(P, E) (2.1) → „E-Mail geht schneller" (Ergänzung 2.2)** | Eine Überzeugung wird nicht durch Argumente gewonnen, sondern durch eine geänderte Vereinbarung, die ihr den Gegenstand nimmt |

_Eine Verbindung, die ich selbst gesehen habe und die hier nicht steht:_

> _…_

<sub>[↑ Inhalt](#l0)</sub>

---

<a id="l8"></a>
## 8. Selbsttest — die ●●●-Punkte ohne Vorlage

Erst antworten, dann aufklappen. Was ich nicht ohne Blick in die Datei beantworte, weiß ich noch nicht.

**1.** Welche vier KI-Kategorien gibt es, und mit welcher Frage entscheide ich zwischen ihnen?
<details><summary>Antwort</summary>

RPA (regelhaft beschreibbar) · Predictive ML (Zahl aus historischen Mustern) · GenAI (Sprache, Variabilität, Entwurf) · Agentic AI (mehrere Schritte mit eigener Planung, klein anfangen).
</details>

**2.** Warum ist der Durchschnitt eines Reifegradprofils nutzlos?
<details><summary>Antwort</summary>

Weil die schwächste **relevante** Dimension begrenzt, was möglich ist. Zwei Organisationen mit Mittelwert 3,0 brauchen völlig verschiedene Maßnahmen — das Profil entscheidet, nicht die Note.
</details>

**3.** Was sagt B = f(P, E), und was folgt daraus für die Maßnahme?
<details><summary>Antwort</summary>

Verhalten ist eine Funktion von Person und Umfeld. Folge: Umfeldfaktoren sind durch Managemententscheidungen veränderbar, Personeneigenschaften nicht durch Training. Widerstand ist keine Personeneigenschaft.
</details>

**4.** Was ist der Barrier Point, und was folgt daraus fürs Budget?
<details><summary>Antwort</summary>

Der erste ADKAR-Wert ≤ 3. Alles danach ist wirkungslos, solange er nicht gelöst ist — Training vor gelöstem Desire ist verbranntes Budget.
</details>

**5.** Warum reicht Knowledge nicht, wenn Desire fehlt?
<details><summary>Antwort</summary>

Wissen auf einen fehlenden Willen gestapelt erzeugt Compliance, nicht Verhalten. Bei Selbstwirksamkeitszweifeln verstärkt eine Schulung das Problem zunächst, weil sie den Abstand sichtbar macht. Belegt durch Lewin 1943: 3 % gegen 32 % bei identischem Informationsgehalt.
</details>

**6.** Wie benutze ich Kotters Modell, wenn ein Vorhaben stockt?
<details><summary>Antwort</summary>

Rückwärtsdiagnose: es ist fast immer ein *früherer* Schritt offen. Nicht von vorn abarbeiten, sondern zurückgehen bis zum ersten Schritt, der nicht wirklich erledigt ist.
</details>

**7.** Was sind die drei Prüffragen an eine Vision?
<details><summary>Antwort</summary>

In eigenen Worten wiedergebbar? Beschreibt sie einen Zustand oder ein Projekt? Könnte man ihr widersprechen? Wer alle drei mit Nein beantwortet, hat einen Projektplan mit einer Prozentzahl.
</details>

**8.** Warum ist der Moment des Erfolgs der gefährlichste?
<details><summary>Antwort</summary>

Weil die Siegeserklärung ein Ressourcenereignis ist: sie beendet Aufmerksamkeit, Budget und Rollen. Die alten Strukturen waren nie weg, sie hatten nur weniger Raum. Es ist der einzige Fehler, gegen den Erfahrung nicht schützt.
</details>

**9.** Warum wirkt das Lösen einer Bremse stärker als mehr Druck?
<details><summary>Antwort</summary>

Mehr Druck erhöht die Spannung im System (mehr Widerstand, höhere Rückfallwahrscheinlichkeit), ohne das Gleichgewicht aufzulösen. Eine gelöste Bremse verändert das Gleichgewicht selbst.
</details>

**10.** Was macht einen Ansatzpunkt zu einem Ansatzpunkt?
<details><summary>Antwort</summary>

Stark **und** beeinflussbar. Nur stark heißt handlungsunfähig, nur beeinflussbar heißt Beschäftigung. Und ohne Maßnahmenzeile mit Verantwortlichkeit, Datum und Erkennungsmerkmal ist auch der richtige Ansatzpunkt nichts wert.
</details>

**11.** Zwei Schrauben mit dem größten Hebel beim Prompten — und die Prüffrage dazu?
<details><summary>Antwort</summary>

Kontext („Woher soll es das wissen?") und prüfbares Erfolgskriterium („Was du nicht nachzählen kannst, ist geschätzt"). Was das Modell nicht wissen kann, erfindet es — plausibel genug, dass es niemand merkt.
</details>

**12.** Wann funktioniert Selbstprüfung durch das Modell, und wann nicht?
<details><summary>Antwort</summary>

Gegen prüfbare Formkriterien und gegen mitgegebenes Material: ja. Gegen faktische Richtigkeit ohne externe Quelle: nein — ein Modell, das eine Falschaussage erzeugt hat, hält sie für richtig.
</details>

_Welche Frage habe ich nicht beantwortet?_

> _…_

<sub>[↑ Inhalt](#l0)</sub>

---

<a id="l9"></a>
## 9. Mein Kompetenzstand

Muster aus Woche 1: **„Ich kann X, nachgewiesen durch Y in Kontext Z."** Nachweis heißt Artefakt, nicht Gefühl.

| Ich kann … | nachgewiesen durch … | im Kontext … | Stand |
|---|---|---|---|
| ein Vorhaben einer KI-Kategorie zuordnen und die Wahl begründen | _…_ | _…_ | ☐ |
| ein Reifegradprofil als Engpassanalyse lesen statt als Note | Reifegradbewertung vom 27.08.2026 (mit benannter Schwäche der Erhebung) | RPA-Pilot Fachverfahren | ☑ teilweise |
| wiederverwendbaren Kontext von Ergebnissen trennen | Repo-Struktur aus Woche 1 | Kursarbeit | ☐ |
| einen ADKAR-Score je Stakeholder-Gruppe erstellen und den Barrier Point begründen | _…_ | _…_ | ☐ |
| ein Kraftfeld herstellen, bewerten und zwei Ansatzpunkte begründen | `bibliothek/kotter-forcefield.md`, drei Bremskräfte mit Stärke und Abbaupfad | RPA-Pilot Fachverfahren | ☑ |
| unterscheiden, ob ein Einwand eine Bremskraft oder ein offener Sachvergleich ist | die bewusst nicht mitgebrachte „vierte Kraft" (Schnittstelle vs. RPA) | RPA-Pilot Fachverfahren | ☑ |
| eine Kennzahl formulieren, die widersprechen kann | _…_ | _…_ | ☐ |

_Der eine Satz, der heute in `kompetenzen.md` steht:_

> _…_

<sub>[↑ Inhalt](#l0)</sub>

---

<a id="l10"></a>
## 10. Offene Fragen und bekannte Lücken

**Aus dem Stoff**
- Wenn es keinen stabilen Endzustand gibt: Was tritt an die Stelle von Refreeze? *(Antwort kommt am Tag 2.3: kein Endzustand, sondern eine zweite Struktur — Kotters Dual Operating System.)*
- Weder Lewin noch ADKAR haben einen eingebauten Mechanismus, um im laufenden Prozess die Richtung zu korrigieren. Was setzt man daneben — einen Regelkreis, oder ein Modell, das von informeller Adoption ausgeht?
- Die 70-Prozent-Zahl: unbelegt in der Herkunft, falsch zugeschrieben in der Urheberschaft. Wie zitiere ich sie, ohne angreifbar zu sein?

**Aus dem eigenen Vorhaben**
- Der Business Case ist die stärkste Bremse (5) und liegt bei mir. Bis wann steht die Amortisationsrechnung mit offen ausgewiesenen Annahmen — inklusive der Variante, dass sich der Pilot nicht rechnet?
- Die Personalvertretung ist benannt, aber nicht beteiligt. Beteiligung **vor** der Entscheidungsvorlage ist der Abbaupfad — wer macht den ersten Schritt, und wann?
- Kultur 1 bei einem Piloten mit Betroffenen: begrenzt das den Piloten, oder ist es genau das, was der Pilot verändern soll?

_Eigene offene Fragen:_

> _…_

<sub>[↑ Inhalt](#l0)</sub>

---

<a id="l11"></a>
## 11. Meine Artefakte — was wo liegt

| Datei / Ordner | Inhalt | Stand |
|---|---|---|
| `bibliothek/lewin-adkar.md` | Lewin und ADKAR: Behauptungen, eigene Erfahrung, Kritik | angelegt |
| `bibliothek/kotter-forcefield.md` | Acht Schritte, drei eigene Bremskräfte mit Stärke, Kotter-Kritik | angelegt |
| `bibliothek/prompting.md` | RTCO, sechs Stellschrauben, wo Kontext wohnt | ☐ prüfen |
| `bibliothek/widerstand.md` | vier Typen, drei Taktiken, ein berechtigter Einwand | ☐ ab 2.3 |
| `kompetenzen.md` | „Ich kann X, nachgewiesen durch Y in Kontext Z" | ☐ prüfen |
| `artefakte/woche-01/` | Manual of Me, Lernziele, Gegenrede, Unternehmensprofil | ☐ prüfen |
| `artefakte/woche-02/` | ADKAR-Scoring, Kraftfeld, Key Learnings | ☐ ab 2.4 |
| `examples/fallbeispiele.md` | alle 20 Fallbeispiele des Kurses mit Quellen und Belastbarkeit | angelegt |
| `coursebook/2.3/`, `coursebook/2.4/` | Analysen der Folien mit Lücken und Beispielen | angelegt |
| `lerntagebuch/lerntagebuch.md` | diese Datei | angelegt |

<sub>[↑ Inhalt](#l0)</sub>

---

<a id="l12"></a>
## 12. Wie ich das fortschreibe

**Nach jedem Kurstag drei Zeilen**, mehr nicht:

1. **Ein Satz**, den ich behalten will — in eigenen Worten, nicht abgeschrieben.
2. **Eine Stelle**, an der es in meinem Vorhaben greift.
3. **Ein Zweifel** oder eine offene Frage.

**Am Wochenende**: die Einträge der Woche in die entsprechenden Abschnitte oben einsortieren und den Selbsttest laufen lassen. Falsche oder zu grobe Stellen **nicht überschreiben** — die neue Fassung kommt darunter, mit Datum. So bleibt sichtbar, was sich verändert hat.

**Die Gegenprobe**, wenn ein Abschnitt fertig aussieht:

> Lies diesen Abschnitt. Bau daraus einen kurzen Fall, maximal 200 Wörter, aus einer anderen Branche als meiner: eine Ausgangslage und eine Frage, in der genau diese Methode gebraucht wird. Nenne die Lösung nicht.
> Danach: Welche Angaben haben gefehlt, um den Fall zu bauen? An welcher Stelle gebe ich die Methode falsch oder zu grob wieder?
> **Nimm nur, was in der Datei steht. Ergänze nichts aus deinem eigenen Wissen.**

---

### Revisionen

| Datum | Was geändert wurde |
|---|---|
| 2026-09-01 | Angelegt, Stand nach Tag 2.2 |
| _…_ | _…_ |

<sub>[↑ Inhalt](#l0)</sub>
