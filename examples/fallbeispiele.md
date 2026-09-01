# Fallbeispiele im Kurs — Übersicht

**Stand:** 2026-09-01 · **Quelle:** lokale Kursdokumente in `coursebook/` (Tag 1.4, 1.5, 2.1, 2.2) sowie die veröffentlichte Course-Book-Website für die späteren Wochen.

**Inhalt:** [Kurzübersicht aller Fälle](#uebersicht) · [1.4 Vier Wellen](#fall-1) · [2.1 Lewin & ADKAR](#fall-6) · [2.2 Kotter](#fall-14) · [Anhang: späte Wochen](#anhang) · [Quellen](#quellen)

Zwei Hinweise vorweg:

1. Die **Langfassungen im Repo** (`coursebook/*.md`) enthalten die ausgearbeiteten Fälle. Die Website-Fassung der Lektüren ist gekürzt — Kodak und Ford stehen dort **nicht**, weshalb man sie online nicht findet.
2. Die Kursdokumente unterscheiden selbst zwischen **öffentlich dokumentierten Fällen** und **typisierten Praxisszenarien** (Muster, keine Fallstudie eines namentlichen Unternehmens). Diese Unterscheidung ist hier durchgehend übernommen — sie ist wichtig, wenn du einen Fall im Steuerkreis zitierst.

---

<a id="uebersicht"></a>
## Kurzübersicht

| § | Fall | Wofür er steht | Modell / Schritt | Belastbarkeit | Quelle im Web |
|---|---|---|---|---|---|
| [14](#fall-14) | [**Kodak**](#fall-14) | Technologie, Prognose und Zeit vorhanden — nur keine Dringlichkeit | Kotter Schritt 1 | dokumentiert | [Kodak](https://en.wikipedia.org/wiki/Kodak) · [Steven Sasson](https://en.wikipedia.org/wiki/Steven_Sasson) |
| [15](#fall-15) | [**Ford / Alan Mulally**](#fall-15) | Koalition entsteht durch Format und psychologische Sicherheit, nicht durch Benennung | Kotter Schritte 2 + 5 | dokumentiert (eine Episode aus zweiter Hand) | [Alan Mulally](https://en.wikipedia.org/wiki/Alan_Mulally) |
| [16](#fall-16) | [**Kotters zwölf Reengineering-Projekte**](#fall-16) | Sieg zu früh erklärt, Veränderung zwei Jahre später verschwunden | Kotter Schritt 7 | Kotters eigene Beobachtung, keine Erhebung | [HBR 1995: Leading Change](https://hbr.org/1995/05/leading-change-why-transformation-efforts-fail-2) (Paywall) |
| [6](#fall-6) | [**Lewins Food-Habits-Studie (1943)**](#fall-6) | Wissen ändert kein Verhalten, eigene Entscheidung in der Gruppe schon (3 % vs. 32 %) | Lewin / ADKAR: Desire | dokumentiert (Originalstudie) | Originalzitat in §6; Hintergrund: [Kurt Lewin](https://en.wikipedia.org/wiki/Kurt_Lewin) |
| [7](#fall-7) | [**Coch & French, Harwood (1948)**](#fall-7) | Widerstand ist eine Funktion des Beteiligungsgrades, keine Eigenschaft der Leute | Lewin: B = f(P, E) | dokumentiert (Originalstudie) | [Human Relations 1(4), DOI](https://journals.sagepub.com/doi/10.1177/001872674800100408) |
| [1](#fall-1) | [**Klarna**](#fall-1) | Hype Cycle in 18 Monaten; gemessen wurde Durchsatz, nicht Qualität | KI-Kategorien / Hype Cycle | dokumentiert | [Klarna (Wikipedia, mit Belegen)](https://en.wikipedia.org/wiki/Klarna) |
| [2](#fall-2) | [**Zillow Offers**](#fall-2) | Prognosemodell driftet still weiter — Rückkopplungszeit ist die kritische Größe | Predictive ML | dokumentiert | [Zillow](https://en.wikipedia.org/wiki/Zillow) |
| [3](#fall-3) | [**Air Canada**](#fall-3) | Wer haftet, wenn das Sprachmodell plausibel Falsches sagt: du | GenAI / Compliance | dokumentiert (Gerichtsentscheid) | [Moffatt v. Air Canada, 2024 BCCRT 149 — Analyse](https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot) |
| [4](#fall-4) | [**Amazon Recruiting**](#fall-4) | Predictive ML schreibt die Vergangenheit fort und objektiviert sie dabei | Predictive ML / Bias | dokumentiert | [Reuters, 10.10.2018](https://www.reuters.com/article/world/insight-amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK0AG/) |
| [5](#fall-5) | [Kategorienfehler: GenAI, wo RPA gereicht hätte](#fall-5) | Falsche Werkzeugkategorie frisst die Ersparnis in der Kontrolle auf | KI-Kategorien | typisiertes Szenario | [Kurs, Tag 1.4](https://neuefische-teaching.github.io/AIDTM/coursebook/1.4/index.html) |
| [8](#fall-8) | [Desire-Fehler beim Versicherer](#fall-8) | Ein Satz über „30 % Effizienz" kostet den Rollout | ADKAR: Desire | typisiertes Szenario | [Kurs, Lektüre Lewin/ADKAR](https://neuefische-teaching.github.io/AIDTM/coursebook/woche-2/lektuere-change-lewin-adkar-w2.html) |
| [9](#fall-9) | [Ability-Fehler im Maschinenbau](#fall-9) | Schulung top, Nutzung 8 % — die Ursachen liegen am Arbeitsplatz | ADKAR: Ability | typisiertes Szenario | [Kurs, Lektüre Lewin/ADKAR](https://neuefische-teaching.github.io/AIDTM/coursebook/woche-2/lektuere-change-lewin-adkar-w2.html) |
| [10](#fall-10) | [Reinforcement-Fehler in der Behörde](#fall-10) | Nutzung 60 % → 25 % nach Projektende | ADKAR: Reinforcement / Refreeze | typisiertes Szenario | [Kurs, Lektüre Lewin/ADKAR](https://neuefische-teaching.github.io/AIDTM/coursebook/woche-2/lektuere-change-lewin-adkar-w2.html) |
| [17](#fall-17) | [Der Quick Win, der keiner war](#fall-17) | Erfolg nur im Steuerkreis sichtbar = keine Bewegung in der Fläche | Kotter Schritt 6 | typisiertes Szenario | [Kurs, Lektüre Kotter/Force Field](https://neuefische-teaching.github.io/AIDTM/coursebook/woche-2/lektuere-change-kotter-forcefield-w2.html) |
| [18](#fall-18) | [Die Vision, die ein Projektplan war](#fall-18) | Zielsatz mit Prozentzahl erzeugt keine Freiwilligen | Kotter Schritt 3 | typisiertes Szenario | [Kurs, Lektüre Kotter/Force Field](https://neuefische-teaching.github.io/AIDTM/coursebook/woche-2/lektuere-change-kotter-forcefield-w2.html) |
| [11](#fall-11) | [Das E-Problem hinter dem P-Problem](#fall-11) | „Widerstand" entpuppt sich als KPI, Compliance-Hinweis und Vorbildverhalten | Lewin: B = f(P, E) | typisiertes Szenario | [Kurs, Tag 2.1](https://neuefische-teaching.github.io/AIDTM/coursebook/2.1/index.html) |
| [12](#fall-12) | [Beispiel-Kraftfeld: GenAI im Kundenservice](#fall-12) | Hemmende Kräfte abbauen wirkt stärker als treibende verstärken | Lewin: Kraftfeldanalyse | Kursbeispiel | [Kurs, Tag 2.1](https://neuefische-teaching.github.io/AIDTM/coursebook/2.1/index.html) |
| [13](#fall-13) | [Beispiel-Scorecard, 200 Betroffene](#fall-13) | Drei Gruppen, zwei Maßnahmenpakete — der erste Wert ≤ 3 ist der Barrier Point | ADKAR: Diagnose | Kursbeispiel | [Kurs, Lektüre Lewin/ADKAR](https://neuefische-teaching.github.io/AIDTM/coursebook/woche-2/lektuere-change-lewin-adkar-w2.html) |
| [19](#fall-19) | [Toolsheros „Jeffrey"](#fall-19) | Gegenstück: ein Beispiel, in dem jeder Schritt gelingt — also keine Fallstudie | Kotter (Toolshero) | Illustration, kein Fall | [Toolshero: Kotter's 8 Step Change Model](https://www.toolshero.com/change-management/8-step-change-model-kotter/) |
| [20](#fall-20) | [Toolsheros Kollaborationsplattform](#fall-20) | Die Spalte „woran erkennbar" macht aus dem Diagramm einen Maßnahmenplan | Lewin: Kraftfeldanalyse | Illustration, kein Fall | [Toolshero: Force Field Analysis](https://www.toolshero.com/change-management/force-field-analysis-lewin/) |

> Hinweis zu den Links: Wo die Originalquelle hinter einer Paywall liegt oder nicht frei abrufbar ist (Klarna-Pressemitteilung, HBR 1995, Bloomberg-Interview 2025), ist eine belegte Sekundärquelle verlinkt. Die Kurs-Links zeigen auf die **gekürzte Website-Fassung** — die ausgearbeiteten Fälle stehen nur in den lokalen Langfassungen unter `coursebook/`.

---

## 1.4 — Vier Wellen, KI-Kategorien, Hype Cycle

<a id="fall-1"></a>
### 1. Klarna: der Hype Cycle in Reinform, in 18 Monaten

**Peak (Feb. 2024):** Klarna meldet, ein KI-Assistent auf OpenAI-Basis erledige im Kundenservice die Arbeit von rund **700 Vollzeitkräften** — zwei Drittel aller Servicechats, Lösungszeit von 11 auf unter 2 Minuten, erwarteter Gewinnbeitrag ca. **40 Mio. USD**.
**Trough (2025):** CEO Sebastian Siemiatkowski korrigiert öffentlich: man sei zu weit gegangen, die **Servicequalität habe gelitten**, es werden wieder Menschen eingestellt — Kundinnen sollen immer einen Menschen erreichen können.
**Der Punkt:** Beide Aussagen sind wahr. Was 2024 fehlte, war nicht Technologie, sondern die **Messgröße** — gemessen wurde Durchsatz, nicht Ergebnisqualität.
**Transfer:** Jeder GenAI-Pilot im Kundenkontakt braucht eine Qualitätskennzahl, **die widersprechen kann** (Erstkontakt-Lösungsquote, Wiederkontaktquote, Zufriedenheit nach Abschluss).
*Quellen: Klarna-Pressemitteilung vom 27.02.2024 („Klarna AI assistant handles two-thirds of customer service chats in its first month"); zur Kurskorrektur das Bloomberg-Interview mit Siemiatkowski, Mai 2025 — beide nicht frei abrufbar, belegte Zusammenfassung mit Einzelnachweisen: [Klarna auf Wikipedia](https://en.wikipedia.org/wiki/Klarna).*

<sub>[↑ zurück zur Kurzübersicht](#uebersicht)</sub>

<a id="fall-2"></a>
### 2. Zillow Offers: wenn ein Prognosemodell still driftet

2018 startet Zillow das iBuying: Häuser algorithmisch bewerten, ankaufen, renovieren, verkaufen. Am **2. November 2021** wird das Geschäft eingestellt — allein Q3/2021 ca. **420 Mio. USD** Verlust, rund **7.000 Häuser** im Bestand, **25 %** der Belegschaft entlassen.
**Mechanismus:** Das Modell war nicht falsch programmiert, sondern auf einem Markt kalibriert, den es nicht mehr gab — und lieferte weiter Preise mit unveränderter Zuversicht. Zwischen Vorhersage und Überprüfung lagen Wochen; in dieser Zeit kaufte der Algorithmus weiter.
**Prüffrage:** *Wie schnell würden wir merken, dass es falsch liegt — und wie viel Schaden entsteht bis dahin?*
*Quelle: Ankündigung von Zillow Group am 02.11.2021; Zahlen belegt in der [Zillow-Übersicht mit Einzelnachweisen](https://en.wikipedia.org/wiki/Zillow).*

<sub>[↑ zurück zur Kurzübersicht](#uebersicht)</sub>

<a id="fall-3"></a>
### 3. Air Canada: die Haftungsfrage bei GenAI

Ein Chatbot auf der Airline-Website gibt eine falsche Auskunft zu Trauerfalltarifen. Im **Februar 2024** entscheidet das kanadische Civil Resolution Tribunal gegen Air Canada; das Argument, der Chatbot sei eine eigenständige Entität, wird zurückgewiesen.
**Folge:** Jeder GenAI-Einsatz mit verbindlichen Auskünften an Kundinnen ist ein **Compliance-Vorhaben**, kein Effizienzprojekt — mit Freigabe, Protokollierung und Rückfallpfad zum Menschen.
*Quelle: Moffatt v. Air Canada, 2024 BCCRT 149, entschieden am 19.02.2024 — [Analyse mit Fundstelle](https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot).*

<sub>[↑ zurück zur Kurzübersicht](#uebersicht)</sub>

<a id="fall-4"></a>
### 4. Amazons Recruiting-Modell: der Bias-Fall

Ab 2014 entwickelt Amazon ein ML-Modell zur Bewerbungsvorauswahl, trainiert auf zehn Jahren Lebensläufen. 2018 wird bekannt, dass es eingestellt wurde: Bewerbungen von Frauen wurden systematisch benachteiligt, „Frauen-" im Lebenslauf wirkte negativ.
**Der Punkt:** Das Modell funktionierte technisch einwandfrei — es sagte präzise voraus, wen Amazon *früher* eingestellt hätte. **Predictive ML extrapoliert die Vergangenheit.**
**Prüffrage:** *Wollen wir die Vergangenheit fortschreiben oder ändern?* Nachfrageprognose → fortschreiben, ML richtig. Personalauswahl, Kredit, Leistungsbewertung → ändern, historisch trainiertes Modell falsch.
*Quelle: [Reuters, 10.10.2018 — „Amazon scraps secret AI recruiting tool that showed bias against women"](https://www.reuters.com/article/world/insight-amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK0AG/).*

<sub>[↑ zurück zur Kurzübersicht](#uebersicht)</sub>

<a id="fall-5"></a>
### 5. Der Kategorienfehler: GenAI, wo RPA gereicht hätte *(typisiert)*

Maschinenbauer, ~500 Mitarbeitende, SAP-ERP, Datenreifegrad Stufe 2, ca. **2.000 Eingangsrechnungen/Monat** von rund **60 Lieferanten** in stabilen Formaten. Entschieden wird ein „KI-Projekt" mit Sprachmodell. Ergebnis: bei ~2 % der Rechnungen plausibel erfundene Werte, API-Kosten pro Vorgang, Prüfaufwand frisst die Ersparnis, Datenschutzbewertung nötig.
**Richtig gewesen wäre** RPA/OCR mit Regelwerk; das Sprachmodell lohnt sich für die Restmenge (~5 %).
**Kategorienfrage in einem Satz:** regelhaft beschreibbar → RPA · Zahl aus historischen Mustern → Predictive ML · Sprache, Variabilität, Entwurf → GenAI · mehrere Schritte mit eigener Planung → Agentic AI, klein anfangen.


<sub>[↑ zurück zur Kurzübersicht](#uebersicht)</sub>

---
## 1.5 — Strategisches Prompt Engineering

Enthält **keine Unternehmensfälle**, sondern drei technische Beispielfälle (Abschnitt 11): der Vorher-Nachher-Vergleich eines Prompts, „wenn die Selbstprüfung das Falsche prüft", und „der Kontext, der zu groß wurde" (Context Rot). Für eine Fallbeispiel-Sammlung nur der Vollständigkeit halber erwähnt.

---

## 2.1 — Change Management: Lewin und ADKAR

<a id="fall-6"></a>
### 6. Lewins eigenes Experiment: die Food-Habits-Studie (1943)

Im Zweiten Weltkrieg sollte in den USA der Verbrauch von Innereien gesteigert werden. Zwei Bedingungen: **Gruppe A** hörte einen guten Vortrag über Nährwert, Sparsamkeit, Patriotismus samt Rezepten. **Gruppe B** führte eine moderierte Gruppendiskussion, erörterte selbst die Hindernisse („mein Mann isst das nicht", „der Geruch") und traf am Ende eine offene Entscheidung.
**Ergebnis:** Vortragsgruppe ca. **3 %**, Diskussionsgruppe ca. **32 %** hatten die neuen Gerichte zubereitet — etwa das Zehnfache.
**Warum das der stärkste Change-Fall ist:** Der Informationsgehalt war praktisch identisch. Unterschiedlich war nur, ob die Teilnehmerinnen selbst zu einer Entscheidung kamen und diese in der Gruppe sichtbar wurde. In ADKAR: A bekam **Knowledge**, B bekam **Desire plus soziale Verbindlichkeit**.
**Transfer:** Das Prompting-Webinar für 200 Personen ist Gruppe A. Der 90-Minuten-Workshop, in dem ein Team eigene zeitraubende Aufgaben aufschreibt, eine gemeinsam mit KI löst und verbindlich festlegt, wer bis wann was ausprobiert, ist Gruppe B. Gleicher Aufwand, eine Größenordnung Wirkung.
*Quelle: Lewin, K. (1943): Forces Behind Food Habits and Methods of Change. Bulletin of the National Research Council, 108, 35–65. (Keine frei zugängliche Online-Fassung verifiziert — Hintergrund zur Person und zur Kraftfeldanalyse: [Kurt Lewin](https://en.wikipedia.org/wiki/Kurt_Lewin).)*

<sub>[↑ zurück zur Kurzübersicht](#uebersicht)</sub>

<a id="fall-7"></a>
### 7. Autonomie als Umfeldfaktor: Coch & French, Harwood (1948)

In der Harwood-Textilfabrik in Virginia führte jede Ablaufänderung zu Produktivitätseinbruch, Beschwerden und Fluktuation. Drei Gruppen bei identischer technischer Änderung: (1) keine Beteiligung, (2) Beteiligung über Vertreter, (3) volle Beteiligung.
**Ergebnis:** Gruppe 1 erreichte das alte Niveau nie wieder (Beschwerden, Kündigungen), Gruppe 2 nach etwa zwei Wochen, Gruppe 3 übertraf es deutlich — ohne Fluktuation.
**Lehre:** Widerstand war keine Eigenschaft der Belegschaft (P), sondern eine Funktion des Beteiligungsgrades (E). Dieselben Menschen, dieselbe Änderung, drei Ergebnisse. **B = f(P, E) im Experiment.**
**Transfer:** Ein Anwendungsfall, den die Fachabteilung selbst benannt hat, wird genutzt; derselbe Fall von der IT ausgewählt und ausgerollt nicht. Der Unterschied liegt nicht im Tool.
*Quelle: [Coch, L. & French, J. R. P. (1948): Overcoming Resistance to Change. Human Relations, 1(4), 512–532](https://journals.sagepub.com/doi/10.1177/001872674800100408) (DOI 10.1177/001872674800100408).*

<sub>[↑ zurück zur Kurzübersicht](#uebersicht)</sub>

<a id="fall-8"></a>
### 8. Der Desire-Fehler: eine Formulierung, die einen Rollout kostet *(typisiert)*

Versicherer, GenAI-Assistent in der Schadensachbearbeitung, **180 Betroffene**. Kick-off-Botschaft: „Mit dem neuen Assistenten heben wir Effizienzpotenziale von rund 30 Prozent."
**Folge:** Awareness steigt, **Desire fällt**. „30 Prozent" wird als Personalabbau gelesen; es entsteht die stille Norm, das Tool nicht zu benutzen, Frühnutzer gelten als illoyal. ADKAR: Awareness 5, Desire 1 → Barrier Point Desire; die geplanten Schulungen treffen die falsche Stufe.
**Korrektur (nichts davon technisch):** verbindliche schriftliche Aussage zur Beschäftigungssicherung mit Geltungszeitraum · Umformulierung von Kostenseite auf Arbeitsinhalt („der Assistent übernimmt die Standardfälle, ihr bekommt Zeit für die komplexen — die, für die ihr eingestellt wurdet") · zwei Sachbearbeitende je Team definieren mit, welche Fallgruppen der Assistent übernimmt.
**Lehre:** Effizienzargumente adressieren die Organisation, Desire entsteht bei der Person. Dieselbe Wahrheit baut Desire auf oder zerstört es, je nachdem, ob sie in Kosten oder in Arbeitsinhalt formuliert ist.

<sub>[↑ zurück zur Kurzübersicht](#uebersicht)</sub>

<a id="fall-9"></a>
### 9. Der Ability-Fehler: Schulung erledigt, Nutzung bei null *(typisiert)*

Maschinenbauunternehmen, **120 Geschulte** aus Vertrieb und Technik, halbtägiger Prompting-Workshop, Feedback sehr gut, Anwendungsfall vom Vertrieb selbst vorgeschlagen. Sechs Wochen später: Nutzung bei ca. **8 %**.
**Was fehlte — nicht Knowledge, sondern die Ability-Bedingungen:** kein Zugang zu den eigenen Angebotsdokumenten im Tool · keine Freigabe, welche Kundendaten eingegeben werden dürfen · kein Ansprechpartner bei Fehlern · kein Zeitpuffer bei unveränderten Vertriebszielen.
**Korrektur statt Nachschulung:** dokumentierte Freigabeliste mit Beispielen, zwei benannte Key User je Standort mit Zeitbudget, Anbindung der Angebotsdatenbank, wöchentliche 30-Minuten-Sprechstunde über acht Wochen.
**Prüffrage vor jeder Nachschulung:** *Könnte die Person es unter ihren realen Bedingungen tun, wenn sie wollte?*

<sub>[↑ zurück zur Kurzübersicht](#uebersicht)</sub>

<a id="fall-10"></a>
### 10. Der Reinforcement-Fehler: der Rückfall nach Projektende *(typisiert)*

Behörde, KI-gestützte Textbausteine für Bescheide. Nach vier Monaten **60 % Nutzung** — Projektteam aufgelöst, Vorhaben als Erfolg abgeschlossen. Drei Monate später: **25 %**.
**Drei Reinforcement-Lücken:** die Verfahrensanweisung beschrieb weiterhin den alten Weg (im Zweifel gewinnt das dokumentierte Verfahren) · die Qualitätssicherung prüfte weiter nur den alten Prozessschritt (was nicht geprüft wird, wird nicht gemacht) · die Key User waren ohne Nachfolge zurück in Fachaufgaben.
**Korrektur:** Verfahrensanweisung anpassen (wirksamster Einzelhebel), neuen Schritt in die QS aufnehmen, Key-User-Rolle mit 10 % Zeitanteil dauerhaft verankern, quartalsweise Kurzretrospektive.
**Lehre:** Refreeze ist eine Struktur- und Dokumentationsaufgabe, keine Kommunikationsaufgabe. Der Projektabschluss ist der Moment mit dem **höchsten** Rückfallrisiko.

<sub>[↑ zurück zur Kurzübersicht](#uebersicht)</sub>

<a id="fall-11"></a>
### 11. Das E-Problem hinter einem scheinbaren P-Problem *(typisiert)*

Ein Sachbearbeitungsteam nutzt ein neues KI-Tool nicht. Naheliegende Erklärung: „Widerstand" (P). Tatsächlich: die Bearbeitungszeit ist als KPI hinterlegt (Ausprobieren kostet in der Statistik) · der Compliance-Hinweis „keine Kundendaten eingeben" macht den Hauptanwendungsfall unmöglich · die Teamleitung nutzt das Tool selbst nicht.
Alle drei sind E-Faktoren, alle durch Managemententscheidungen veränderbar, keiner durch ein Training.

<sub>[↑ zurück zur Kurzübersicht](#uebersicht)</sub>

<a id="fall-12"></a>
### 12. Beispiel-Kraftfeld: GenAI-Assistent im Kundenservice

Treibende Kräfte (mit Stärke 1–5): Wettbewerbsdruck 4 · Ziel im Vorstandsprogramm 4 · spürbare Entlastung bei Standardanfragen 3 · einzelne Early Adopters 2.
Hemmende Kräfte und wodurch abbaubar: Sorge um Arbeitsplatzsicherheit 5 (verbindliche Aussage, Rollenbild „komplexe Fälle") · Bearbeitungszeit-KPI bestraft die Lernphase 4 (KPI 8 Wochen aussetzen) · Unklarheit über erlaubte Daten 4 (einseitiges Do/Don't-Blatt) · Betriebsrat nicht eingebunden 3 · kein Ansprechpartner 2.
**Lewins übersehener Befund dazu:** hemmende Kräfte abbauen wirkt besser als treibende verstärken. Eine weitere All-Hands-Mail ist eine treibende Kraft; eine freigegebene, datenschutzkonforme Tool-Instanz mit klarer Richtlinie räumt eine hemmende weg.

<sub>[↑ zurück zur Kurzübersicht](#uebersicht)</sub>

<a id="fall-13"></a>
### 13. Beispiel-Scorecard (Kursszenario, 200 Betroffene)

| Stufe | Teamleitung | Frontline | IT |
|---|---|---|---|
| Awareness | 4 | 4 | 5 |
| Desire | 3 ⚠ | **2 ⚠** | 4 |
| Knowledge | 2 | 1 | **3 ⚠** |
| Ability | 2 | 1 | 3 |
| Reinforcement | 1 | 1 | 2 |
| **Barrier Point** | **Desire** | **Desire** | **Knowledge** |

Regel: der erste Wert ≤ 3 ist der Barrier Point; alles danach ist wirkungslos, solange er nicht gelöst ist. Drei Gruppen, zwei völlig verschiedene Maßnahmenpakete — ein Plan mit einheitlichem Schulungsangebot trifft in zwei von drei Fällen daneben.


<sub>[↑ zurück zur Kurzübersicht](#uebersicht)</sub>

---
## 2.2 — Kotters 8 Schritte

<a id="fall-14"></a>
### 14. Kodak: Dringlichkeit, die nie entstand (Schritt 1)

**Ausgangslage:** 1975 entwickelte der Kodak-Ingenieur **Steven Sasson** die erste batteriebetriebene digitale Handkamera — ein Prototyp mit 10.000 Bildpunkten. Die Technologie, die Kodaks Geschäftsmodell zerstören würde, entstand im eigenen Haus, 37 Jahre vor dem Ende.
**Was die Führung tat:** Sie zögerte beim Umschwenken — hohe Investitionen für einen damals sehr kleinen Markt. Diese Einschätzung war **zum Zeitpunkt der Entscheidung wirtschaftlich nicht falsch**. 1979 sagte der Mitarbeiter Larry Matteson den vollständigen Übergang zur Digitalfotografie bis 2010 voraus. Gehandelt wurde nicht.
**Ergebnis:** Am **19. Januar 2012** meldete Kodak Chapter 11 an.
**Warum das der lehrreichste Urgency-Fall ist:** Kodak fehlte weder Technologie noch Information noch Prognose. Es fehlte die **geteilte Überzeugung, dass jetzt gehandelt werden muss** — zu einem Zeitpunkt, als das Kerngeschäft hervorragend lief. Genau das ist Kotters Punkt: Dringlichkeit ist am schwersten zu erzeugen, wenn es der Organisation gut geht, und genau dann am wertvollsten.
**Transfer auf KI:** Eine Organisation, deren Zahlen stimmen, nimmt eine KI-Analyse zur Kenntnis und ändert nichts. „Wir haben eine Studie" ist keine Dringlichkeit. Prüffrage: *Was in unserem Geschäft würde in drei Jahren nicht mehr funktionieren, und woran würden wir das heute schon merken?*
*Belastbarkeit: hoch — Sasson-Prototyp 1975, Matteson-Prognose 1979, Chapter-11-Antrag 19.01.2012, alles öffentlich dokumentiert. Belege: [Kodak](https://en.wikipedia.org/wiki/Kodak) (Chapter 11 am 19.01.2012, Sasson-Prototyp 1975) · [Steven Sasson](https://en.wikipedia.org/wiki/Steven_Sasson) (100 × 100 Pixel = 10.000 Bildpunkte, 3,6 kg, Speicherung auf Kassettenband).*

<sub>[↑ zurück zur Kurzübersicht](#uebersicht)</sub>

<a id="fall-15"></a>
### 15. Ford unter Alan Mulally: Koalition und Handlungsfreiheit (Schritte 2 und 5)

**Ausgangslage:** Mulally wurde am **5. September 2006** CEO von Ford — ein Branchenfremder aus der Luftfahrt, in einem Konzern mit massiven Verlusten und schrumpfendem Marktanteil. 2006 sicherte er einen Kredit über **23,6 Mrd. USD** durch Verpfändung von Unternehmenswerten.
**Mechanismus:** wöchentliche **Business Plan Reviews** — jeden Donnerstag 7 Uhr, dieselbe Runde, dieselben Kennzahlen, bewertet als grün, gelb oder rot.
**Was daran Kotter ist:** Die BPR sind Schritt 2 und Schritt 5 in einem Format — eine dauerhafte Führungskoalition (dieselben Personen, jede Woche, geteilte Verantwortung für dasselbe Bild) und Handlungsfreiheit, weil Probleme sichtbar werden, bevor sie eskalieren.
**Die Voraussetzung, an der es fast scheiterte:** Nach Bryce Hoffman (*American Icon*) zeigten die Führungskräfte über Wochen ausschließlich grüne Kennzahlen — bei einem Konzern, der Milliarden verlor. Erst als **Mark Fields** als Erster einen Punkt auf Rot setzte und Mulally applaudierte statt zu sanktionieren, änderte sich das Verhalten. *(Journalistisch belegt, Darstellung aus zweiter Hand — als Illustration geeignet, nicht als Beleg zitierbar.)*
**Ergebnis:** Ford überstand die Krise 2008/09 als einziger der drei großen US-Hersteller **ohne staatliche Rettung**.
**Lehre:** Eine Führungskoalition entsteht nicht durch Benennung, sondern durch ein **Format mit Taktung und psychologischer Sicherheit**. Schritt 5 beginnt nicht bei Budget und Werkzeugen, sondern bei der Frage, ob Probleme benannt werden dürfen. Übertragen: Wenn ein Pilot nur Erfolgsmeldungen produziert, misst du nicht den Piloten, sondern die Angst im Team.
*Belege: [Alan Mulally](https://en.wikipedia.org/wiki/Alan_Mulally) — Amtszeit ab 2006, 23,6-Mrd.-USD-Kredit gegen Verpfändung aller Vermögenswerte, BPR jeden Donnerstag 7 Uhr, Ford als einziger der Detroit Three ohne Staatskredit. Die Fields-Episode: Bryce Hoffman, *American Icon* (2012).*

<sub>[↑ zurück zur Kurzübersicht](#uebersicht)</sub>

<a id="fall-16"></a>
### 16. Kotters zwölf Reengineering-Projekte: zu früh gefeiert (Schritt 7)

In zwölf beobachteten Vorhaben wurde nach zwei bis drei Jahren der Sieg erklärt; innerhalb von zwei weiteren Jahren verschwanden die Veränderungen wieder, in zwei von zehn Fällen waren Spuren praktisch nicht mehr nachweisbar.
**Mechanismus:** Die Siegeserklärung ist kein Kommunikationsfehler, sondern ein **Ressourcenereignis** — sie beendet Aufmerksamkeit, Budget und Rollen. Die alten Strukturen waren nie weg, sie hatten nur weniger Raum.
**Warum das zählt:** Es ist der einzige Fehler, den man **im Moment des Erfolgs** macht — deshalb schützt Erfahrung nicht davor.
**Gegenmaßnahme:** schon bei der Planung festlegen, was *nach* dem erfolgreichen Piloten passiert (welche Rollen bleiben, welcher Prozess ändert sich, wann wird nachgemessen).
*Belastbarkeit: Kotters eigene Fallbeobachtung, keine unabhängige Erhebung — als Muster aussagekräftig, als Statistik nicht. Original: [Kotter, J. P. (1995): Leading Change: Why Transformation Efforts Fail, HBR März–April 1995](https://hbr.org/1995/05/leading-change-why-transformation-efforts-fail-2) (Paywall).*

<sub>[↑ zurück zur Kurzübersicht](#uebersicht)</sub>

<a id="fall-17"></a>
### 17. Der Quick Win, der keiner war (Schritt 6) *(typisiert)*

Versicherer, erster sichtbarer Erfolg: ein Dokumentenklassifikationsmodell, technisch anspruchsvoll, nach zehn Wochen fertig, **94 % Genauigkeit**, im Steuerkreis beklatscht. In der Organisation kommt nichts an — die Klassifikation lief vorher in einem Schritt mit, den niemand als Aufwand wahrnahm; keine einzige Anfrage aus anderen Bereichen.
**Diagnose:** drei der vier Kotter-Kriterien erfüllt (eindeutig, terminiert, anerkannt) — **sichtbar war es nicht**, jedenfalls nicht für die Menschen, deren Freiwilligkeit man gewinnen wollte.
**Korrektur:** als zweiter Quick Win automatisch vorbefüllte Antwortentwürfe für Standardfälle — technisch einfacher, fachlich unspektakulär; danach meldeten sich drei Abteilungen von selbst.
**Prüffrage:** nicht „können wir das schnell?", sondern *wessen* Alltag wird spürbar besser, und wird diese Person davon erzählen?

<sub>[↑ zurück zur Kurzübersicht](#uebersicht)</sub>

<a id="fall-18"></a>
### 18. Die Vision, die ein Projektplan war (Schritt 3) *(typisiert)*

Maschinenbauer, KI-Vision: „Bis Ende 2027 sind unsere Kernprozesse in Vertrieb, Service und Buchhaltung KI-gestützt, mit einer Effizienzsteigerung von 25 %." Der Satz steht auf jeder Folie. Nach vier Monaten kann in drei Teams niemand sagen, was sich für die eigene Arbeit ändern soll; zwei Personen lesen Stellenabbau heraus; keine Freiwilligenmeldung.
**An Kotters drei Prüffragen:** in eigenen Worten wiedergebbar? Nein, es wird die Zahl wiederholt. Zustand oder Projekt? Projekt. Könnte man widersprechen? Nein — niemand ist gegen Effizienz, deshalb sagt der Satz nichts.


<sub>[↑ zurück zur Kurzübersicht](#uebersicht)</sub>

---
## 2.2 Ergänzung — Force-Field-Analyse

<a id="fall-19"></a>
### 19. Toolsheros Fallbeispiel „Jeffrey" — als Gegenstück
*Quelle: [Toolshero — Kotter's 8 Step Change Model: the Basics and Examples](https://www.toolshero.com/change-management/8-step-change-model-kotter/)*

Jeffrey leitet ein Unternehmen mit rund 100 Beschäftigten und verliert Umsatz an Wettbewerber, die in neue Technologie investieren. Er arbeitet die acht Schritte der Reihe nach ab — und **jeder Schritt gelingt**. Kein Unternehmen, keine Zahlen, kein Zeitraum, kein Ergebnis: **keine Fallstudie**, im Gegensatz zu den drei Fällen im Hauptdokument, die ausgewählt wurden, weil dort etwas schiefging.
**Wozu es trotzdem taugt:** als **Format** (acht Absätze, ein Vorhaben, ein Schritt pro Absatz) für das eigene Vorhaben — und als Übung, es zu brechen: bei jedem Schritt fragen, was passiert, wenn er misslingt (Schritt 1 → [Kodak](#fall-14); Schritt 2 → die Runde besteht aus Überzeugten, der respektierte Skeptiker fehlt; Schritt 3 → der Satz enthält eine Prozentzahl; Schritt 4 → es wird gesendet, die Führung verhält sich gegenteilig, es entsteht Zynismus; Schritt 5 → „Dialog" ersetzt die Entscheidung, wenn eine Führungskraft blockiert).

<sub>[↑ zurück zur Kurzübersicht](#uebersicht)</sub>

<a id="fall-20"></a>
### 20. Toolsheros Beispiel: Einführung einer Kollaborationsplattform
*Quelle: [Toolshero — Force Field Analysis: The Basics and an Example](https://www.toolshero.com/change-management/force-field-analysis-lewin/)*

Toolshero führt das Kraftfeld-Verfahren an einer Plattformeinführung vor — nah genug an einem KI-Rollout, dass sich alles übertragen lässt. Merksatz aus der Vorlage: die letzte Spalte („woran erkennbar") macht den Unterschied. „Schulung durchgeführt" ist kein Ergebnis; „drei von fünf Teams haben in der Folgewoche mindestens einmal ohne Aufforderung genutzt" ist eines.


<sub>[↑ zurück zur Kurzübersicht](#uebersicht)</sub>

---
<a id="anhang"></a>
## Anhang: Fälle in späteren Wochen (aus der Course-Book-Website)

Diese liegen noch nicht als lokale Langfassung im Repo, tauchen aber auf den Tagesseiten auf:

| Fall | Wo (Link) | Inhalt in einem Satz |
|---|---|---|
| **Deutsche Telekom** | [Tag 3.3](https://neuefische-teaching.github.io/AIDTM/coursebook/3.3/index.html) · [Tag 8.1](https://neuefische-teaching.github.io/AIDTM/coursebook/8.1/index.html) | Plattformwahl nach Governance-Anforderungen und Reifegrad statt nach technischer Überlegenheit; später zentralisiertes Top-Down-Data-Governance-Modell mit Qualitäts-KPIs und Datenkatalog. |
| **Bosch** | [Tag 9.1](https://neuefische-teaching.github.io/AIDTM/coursebook/9.1/index.html) | Systematischer KI-Rollout 2020–2024 über mehrere hundert Werke, zentrale KI-Plattform, Hub-and-Spoke (zentrale Methodik, lokale Umsetzung). |
| **Bosch** | [Tag 5.3](https://neuefische-teaching.github.io/AIDTM/coursebook/5.3/index.html) | Governance-Transformation: gewachsene Datensilos, ein Rechtsbereich, der Datenschutz kannte und den AI Act nicht, Mitbestimmung von Anfang an in der RACI. |
| **Bosch** | [Tag 6.2](https://neuefische-teaching.github.io/AIDTM/coursebook/6.2/index.html) | Beschaffung je Anwendungsfall statt nach einer Regel: HR-Dokumentenverarbeitung als Kaufsoftware, Predictive Maintenance und Bildprüfung als Partnermodell. |
| **Siemens** | [Tag 4.3](https://neuefische-teaching.github.io/AIDTM/coursebook/4.3/index.html) | Erste Kommunikationswelle nur Effizienzgewinne → Ingenieure fragen sich, ob Stellen wegfallen; erst die zweite Welle mit Entwicklungspfaden verbessert das Engagement. |
| **Siemens** | [Tag 7.2](https://neuefische-teaching.github.io/AIDTM/coursebook/7.2/index.html) | Smart Factory Nanjing, 2021 live: ca. 20 % Produktivitätssteigerung, 20 % Kostenreduktion gegenüber traditionellen Werken. |
| **Siemens Industrial Copilot / Moody's / Canadian Tire** | [Tag 4.4](https://neuefische-teaching.github.io/AIDTM/coursebook/4.4/index.html) | Referenzbeispiele im Executive Briefing: über 50 aktive Kunden · 25 % Zeitersparnis bei 14.000 Nutzenden · Nicht-Tech-Referenz. |
| **Hofmann Personal** | [Tag 7.1](https://neuefische-teaching.github.io/AIDTM/coursebook/7.1/index.html) · [Tag 7.3](https://neuefische-teaching.github.io/AIDTM/coursebook/7.3/index.html) | 2024 Langdock für CV-Verarbeitung eingeführt: 10–30 Min. auf 1–2 Min. pro CV, laut Unternehmen ca. 25.000 eingesparte Arbeitsstunden/Jahr (ROI-Rechenbeispiel). |
| **HaTL — Hartmann Transport & Logistik GmbH** | [Woche 13](https://neuefische-teaching.github.io/AIDTM/coursebook/woche-13/index.html) ff. | Kein realer Fall, sondern das durchgängige fiktive Simulationsunternehmen der Abschluss-Simulation (Wochen 13–16). |

Externe Belege zu diesen Fällen sind auf den Kursseiten selbst nur teils angegeben (Bosch verweist z. B. auf den Geschäftsbericht 2024, Hofmann Personal auf eine Langdock-Case-Study 2024, Ref. CL-012). Vor einer Verwendung nach außen also am Tag selbst nachsehen, welcher Beleg dort steht.

---

## Wie man diese Fälle benutzt

- **Zitierfähig ohne Einschränkung:** [Kodak](#fall-14), [Ford](#fall-15) (außer der Fields-Episode), [Klarna](#fall-1), [Zillow](#fall-2), [Air Canada](#fall-3), [Amazon](#fall-4), [Lewin 1943](#fall-6), [Coch & French 1948](#fall-7).
- **Nur als Muster verwendbar:** alles mit *(typisiert)* markierte — [§5](#fall-5), [§8](#fall-8), [§9](#fall-9), [§10](#fall-10), [§11](#fall-11), [§17](#fall-17), [§18](#fall-18) — sowie [Kotters zwölf Projekte](#fall-16). Diese Fälle bilden dokumentierte Fehlermuster ab, sind aber keine Fallstudien namentlicher Unternehmen — in einer Vorlage für Entscheider also als Szenario kennzeichnen.
- **Die drei Fälle, die man laut Kursindex parat haben sollte:** [Kodak](#fall-14) (●●●), [Ford / Mulally](#fall-15) (●●), [Kotters zwölf Projekte](#fall-16) (●●).

---

<a id="quellen"></a>
## Quellen im Überblick

**Primär- und Belegquellen zu den Fällen**

- Kodak / Steven Sasson: [Kodak](https://en.wikipedia.org/wiki/Kodak) · [Steven Sasson](https://en.wikipedia.org/wiki/Steven_Sasson)
- Ford / Alan Mulally: [Alan Mulally](https://en.wikipedia.org/wiki/Alan_Mulally); Fields-Episode aus Bryce Hoffman, *American Icon* (2012)
- Kotters zwölf Projekte: [HBR, März–April 1995 — Leading Change: Why Transformation Efforts Fail](https://hbr.org/1995/05/leading-change-why-transformation-efforts-fail-2) (Paywall)
- Coch & French (1948): [Human Relations 1(4), 512–532](https://journals.sagepub.com/doi/10.1177/001872674800100408)
- Lewin (1943), Food Habits: Bulletin of the National Research Council 108, 35–65 — keine frei zugängliche Fassung verifiziert; Hintergrund [Kurt Lewin](https://en.wikipedia.org/wiki/Kurt_Lewin)
- Klarna: [Klarna (Wikipedia, mit Einzelnachweisen zur Pressemitteilung 27.02.2024)](https://en.wikipedia.org/wiki/Klarna); Kurskorrektur laut Bloomberg-Interview, Mai 2025
- Zillow Offers: [Zillow](https://en.wikipedia.org/wiki/Zillow)
- Air Canada: [Moffatt v. Air Canada, 2024 BCCRT 149 (19.02.2024) — juristische Analyse](https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot)
- Amazon Recruiting: [Reuters, 10.10.2018](https://www.reuters.com/article/world/insight-amazon-scraps-secret-ai-recruiting-tool-that-showed-bias-against-women-idUSKCN1MK0AG/)

**Die Pflichtlektüren des Kurses (Originale)**

- [Toolshero — Lewin Change Model](https://www.toolshero.com/change-management/lewin-change-model/)
- [Toolshero — ADKAR Model](https://www.toolshero.com/change-management/adkar-model/)
- [Toolshero — Kotter's 8 Step Change Model](https://www.toolshero.com/change-management/8-step-change-model-kotter/)
- [Toolshero — Force Field Analysis](https://www.toolshero.com/change-management/force-field-analysis-lewin/)

**Course Book (gekürzte Website-Fassung)**

- [Woche 2 — Übersicht](https://neuefische-teaching.github.io/AIDTM/coursebook/woche-2/)
- [Lektüre: Warum Veränderung scheitert — Lewin und ADKAR](https://neuefische-teaching.github.io/AIDTM/coursebook/woche-2/lektuere-change-lewin-adkar-w2.html)
- [Lektüre: Acht Fehler, und ein Werkzeug dagegen — Kotter und Force-Field-Analyse](https://neuefische-teaching.github.io/AIDTM/coursebook/woche-2/lektuere-change-kotter-forcefield-w2.html)
- [Lektüre: Widerstand ist eine Information, nicht ein Hindernis](https://neuefische-teaching.github.io/AIDTM/coursebook/woche-2/lektuere-change-widerstand-w2.html)
- [Tag 1.4](https://neuefische-teaching.github.io/AIDTM/coursebook/1.4/index.html) · [Tag 2.1](https://neuefische-teaching.github.io/AIDTM/coursebook/2.1/index.html) · [Tag 2.2](https://neuefische-teaching.github.io/AIDTM/coursebook/2.2/index.html)

**Lokale Langfassungen (die eigentliche Quelle dieser Sammlung)**

- `coursebook/1.4/1.4_Vier-Wellen-KI-Kategorien-Hype-Cycle.md` — Abschnitt 8
- `coursebook/2.1/01_Change-Management-Lewin-ADKAR.md` — Abschnitt 9
- `coursebook/2.2/2.2_Kotter-8-Schritte-Modell.md` — Abschnitt 8
- `coursebook/2.2/2.2_Ergaenzung-Force-Field-Analyse.md` — Abschnitte 3.3 und 4.6
- `coursebook/0/00_Index-und-Gewichtung.md` — Gewichtung der drei Kernfälle
