---
titel: KI-Analyse GeAT mbH — Plattform- und Werkzeugwahl
bezug: Coursebook 3.1 Abschnitt 6 (Bewertungsmatrix) gegen profil.md, zahlen.md, systeme-daten.md, menschen.md, vorhaben.md, transformationsvorschlag.md
typ: Analyse und Entscheidungsvorlage, nicht beschlossen
datum: 2026-09-07
woche: 03
status: Entwurf, zur Vorlage in der Geschäftsführung
verantwortlich: Rolle 15 (AI and Digital Transformation Manager) — Macht 2, kein Budget, kein Gremium
herkunft: abgeleitet — Gewichtungen sind begründete Setzungen, Scores sind Einschätzungen auf Herstellerunterlagen, Preise sind prüfpflichtige Listenwerte
---

# KI-Analyse GeAT mbH — welches Werkzeug, und warum nicht die anderen

> **Was diese Datei ist.** Die Bewertungsmatrix aus [Coursebook 3.1, Abschnitt 6](../coursebook/3.1/3.1_KI-Plattformen-im-Vergleich.md), angewendet auf GeAT statt auf einen Versicherer mit 1.200 Beschäftigten. Sie ergänzt den [`transformationsvorschlag.md`](transformationsvorschlag.md): dort steht die **Reihenfolge**, hier steht das **Werkzeug** für Stufe 1 und Stufe 4.
>
> **Wie sie zu lesen ist.** Drei Herkunftsarten, überall getrennt gehalten:
> `Fakt` = belegt oder aus dem Profil als `öffentlich` übernommen · `Annahme` = Setzung dieser Analyse, begründet · `Einschätzung` = mein Urteil, bestreitbar.
> **Kein Wert in dieser Datei ist ein Angebot.** Kein Anbieter wurde angefragt, kein AVV liegt vor, kein Preis ist verhandelt.
>
> **Warum ich sie selbst schreibe.** Die Stelle ist im Mai 2026 geschaffen worden, hat Macht 2 und kein Gremium ([`menschen.md`](menschen.md), Rolle 15). Ich bin damit der einzige Beteiligte, dessen Lage von dieser Entscheidung abhängt. Das gehört in die Vorlage, nicht in eine Fußnote: Wer eine Empfehlung von mir liest, liest die Empfehlung einer interessierten Partei. Die Gegenargumente in [Abschnitt 8](#8-gegenargumente-und-risiken) sind deshalb länger als die Empfehlung.

**Inhalt:** [1 Reihenfolge](#1-die-reihenfolge-die-eingehalten-wird) · [2 Kategorienfrage](#2-die-kategorienfrage-drei-bedarfe-eine-plattformfrage) · [3 Tore](#3-drei-tore-vor-der-matrix) · [4 Kontext A](#4-teil-a--kontext-stufe-1-der-freigegebene-zugang) · [5 Matrix A](#5-matrix-a--das-ergebnis) · [6 Teil B Stufe 4](#6-teil-b--stufe-4-dieselben-optionen-andere-gewichtung) · [7 Was kein Score misst](#7-was-kein-score-misst) · [8 Gegenargumente](#8-gegenargumente-und-risiken) · [9 Empfehlung](#9-die-empfehlung) · [10 Offene Punkte](#10-offene-punkte-und-prüffragen)

---

## 1. Die Reihenfolge, die eingehalten wird

Die Kursregel lautet: **erst Kontext festlegen, dann gewichten, dann scoren.** Ohne Kontext ist jede Gewichtung beliebig, und die Matrix wird zu einer Liste. Diese Datei hält die Reihenfolge ein und macht sie prüfbar.

Drei Vorkehrungen, alle aus den Mängeln, die das Coursebook selbst an der Beispielmatrix benennt (Abschnitt 9):

| Vorkehrung | Grund | Wo sie wirkt |
|---|---|---|
| **Skalenanker, vorher fixiert** | „Score 1 bis 5 mit Begründung" ohne Definition erzeugt so viele Skalen wie Bewerter | unten in dieser Tabelle |
| **Gewichtung schriftlich begründet, bevor gescort wird** | Wer das Wunschergebnis kennt, kann rückwärts gewichten (Hammond/Keeney/Raiffa, *The Hidden Traps in Decision Making*) | [Abschnitt 4](#4-teil-a--kontext-stufe-1-der-freigegebene-zugang), [Abschnitt 6](#6-teil-b--stufe-4-dieselben-optionen-andere-gewichtung) |
| **Spalte „unabhängig belegt"** | Alle verfügbaren Belege sind Herstellerangaben — die schwächste Belegform für eine Freigabeinstanz | in beiden Score-Tabellen |

**Die Anker, Fassung dieser Analyse** (`Annahme`, übernommen aus Coursebook 3.1 Abschnitt 9 Punkt 2):

| Wert | Bedeutung |
|---:|---|
| **5** | erfüllt, belegbar **und vertraglich zugesichert** |
| **4** | erfüllt, Belege öffentlich (Herstellerdokumentation, Zertifikat) |
| **3** | teilweise erfüllt, mit Aufwand herstellbar |
| **2** | nur auf der Roadmap oder nur behauptet |
| **1** | nicht vorgesehen |

> **Regel, die aus den Ankern folgt und die Matrix begrenzt:** Es gibt in dieser Analyse **keine 5**. Ein Wert 5 verlangt eine vertragliche Zusicherung; GeAT hat kein Angebot und keinen AVV auf dem Tisch. Wer in einer Vorbewertung ohne Ausschreibung eine 5 verteilt, hat den Anker nicht gelesen. Die Werte 5 werden in der Ausschreibung erreicht — oder eben nicht, und dann ist genau das das Ergebnis.

---

## 2. Die Kategorienfrage: drei Bedarfe, eine Plattformfrage

> **Nicht: „Welche Plattform ist die beste?" — sondern: „In welcher Kategorie liegt unser Bedarf?"**

GeAT hat drei offene Werkzeugbedarfe, und nur einer davon ist eine Plattformfrage. Wer sie vermischt, kauft ein Werkzeug für eine Aufgabe, die es nicht löst.

| Bedarf | Quelle | Kategorie | In dieser Matrix? |
|---|---|---|---|
| Freigegebener KI-Zugang für Anzeigentexte und Profilzusammenfassungen, 9.000 € | [Transformationsvorschlag](transformationsvorschlag.md), Stufe 1 | **Integrierte Enterprise-KI-Plattform** | **ja — Teil A** |
| Besetzungsassistent: Bestand und Lebenslauf-Dateien durchsuchen, drei bis fünf Kandidaten mit Begründung, 60.000 € | ebenda, Stufe 4 · [`vorhaben.md`](vorhaben.md) | **Integrierte Plattform mit RAG** oder Produktfunktion des Kernsystems | **ja — Teil B** |
| Schnittstelle Multiposting ↔ Bewerbermanagement, Quellenkennung im Rücklauf, 18.000 € | ebenda, Stufe 2 | **Workflow-Automatisierung** (n8n, Make, Zapier) oder Anbieterschnittstelle | **nein** |

**Warum der dritte Bedarf nicht in diese Matrix gehört.** Er ist kein KI-Fall. Eine Bewerbung braucht eine Quellenkennung, kein Sprachmodell. Keine der fünf Optionen unten löst ihn, und keine Plattformentscheidung ersetzt ihn. Er ist trotzdem der Posten mit der schnellsten Amortisation im ganzen Programm — zehn Prozent besser allokiertes Anzeigenbudget sind 48.000 € im Jahr, bei 480.000 € Gesamtbudget (`Fakt` im Fall: [`zahlen.md`](zahlen.md)). Er steht hier, damit er nicht in der Plattformdiskussion verschwindet.

Und damit ist der teure Fehler aus Coursebook 3.1 Abschnitt 8.1 benannt: **GenAI kaufen, wo eine Schnittstelle gereicht hätte.** Bei GeAT wäre er 18.000 € gegen einen Plattformvertrag.

---

## 3. Drei Tore vor der Matrix

Ein Kriterium, das man nicht aufgeben kann, ist kein Kriterium — es ist ein Tor. Wer es gewichtet, erlaubt, dass es überstimmt wird. Bei GeAT gibt es drei, und alle drei stehen **vor** dem Scoring.

| Tor | Grundlage | Prüffrage an den Anbieter | Wer entscheidet |
|---|---|---|---|
| **T1 · AVV vorgelegt** | Art. 28 DSGVO. Neun Stammkräfte fügen heute Lebensläufe in private KI-Konten ein, ohne Auftragsverarbeitungsvertrag (`Fakt` im Fall: [`systeme-daten.md`](systeme-daten.md)) | „Legen Sie den AVV vor, nicht die Aussage, dass Sie DSGVO-konform sind." | Marnitz (DSB), Achtelik |
| **T2 · Protokollierung so konfigurierbar, dass Leistungs- und Verhaltenskontrolle ausgeschlossen werden kann** | § 87 BetrVG. Der Betriebsrat hat 2023 beim ATS-Modul genau darauf bestanden (`Fakt` im Fall: [`menschen.md`](menschen.md), Rolle 9) | „Welche Nutzerprotokolle entstehen, wer kann sie einsehen, und lässt sich der Umfang vertraglich begrenzen?" | Nowak (Betriebsrat) |
| **T3 · Verarbeitung in der EU, Löschfristen technisch durchsetzbar** | Art. 9 DSGVO. Bewerberdaten enthalten teils Gesundheitsangaben aus der arbeitsmedizinischen Vorsorge; 18.000 Profile liegen über der zugesagten Speicherdauer (`Fakt` im Fall) | „Wo liegen die Daten, und wie löschen Sie auf Anforderung nachweisbar?" | Marnitz (DSB) |

> **Warum T2 ein Tor ist und kein Kriterium.** Das Coursebook nennt Mitbestimmung als fehlendes Kriterium und setzt hinzu: *„In einer Behörde ist das ein Tor, kein Kriterium unter vielen."* Bei GeAT gilt derselbe Satz aus einem anderen Grund. Der Betriebsrat ist hier nicht Gegner, sondern die einzige Instanz, die 2024 nach der Nutzung des Moduls gefragt hat. Und weil die verantwortliche Rolle kein Gremium hat, ist eine Betriebsvereinbarung die einzige Vereinbarung im ganzen Vorhaben, die meine Anwesenheit überdauert.

**Wirkung der Tore auf die fünf Optionen:** Keine wird vorab ausgeschlossen — bei keiner ist heute belegt, dass sie ein Tor **nicht** passiert. Die Tore sind deshalb Ausschreibungsanforderungen, keine Filter. Wer sie erst nach der Auswahl stellt, verhandelt ohne Alternative.

---

## 4. Teil A — Kontext Stufe 1: der freigegebene Zugang

### 4.1 Der Kontext, zehn Zeilen, vor jeder Gewichtung

| Nr | Kontextzeile | Herkunft |
|---:|---|---|
| 1 | **69 Seats, nicht 709.** 640 der 709 Beschäftigten sind Zeitarbeitnehmer in Kundenbetrieben, ohne Bildschirmarbeitsplatz bei GeAT | `Fakt` im Fall |
| 2 | **Der enge Zuschnitt sind 20 Seats:** Recruiting Center (9), Vertrieb und Innendienst — die Gruppe, in der die neun Schatten-Nutzer sitzen | `Annahme` dieser Analyse |
| 3 | **Reguliert, aber nicht wie eine Versicherung.** AÜG-Erlaubnis der Bundesagentur für Arbeit, ISO 9001, Art. 9 DSGVO, AGG, § 26 BDSG, § 87 BetrVG. Kein BaFin-Regime, keine aufsichtsrechtliche Auslagerungsanzeige | `Fakt` (Aufsicht) / `Einschätzung` (Vergleich) |
| 4 | **Der ungeregelte Zustand läuft heute.** Neun Personen, private KI-Konten, Lebensläufe darin, kein AVV. Dazu WhatsApp-Gruppen mit rund 300 Zeitarbeitnehmern, Kontakt- und Gesundheitsangaben, ebenfalls ohne Vertrag | `Fakt` im Fall |
| 5 | **1,5 IT-Stellen für sechs Niederlassungen plus Zentrale** — und beide vollständig durch die Migration 2027 gebunden | `Fakt` im Fall |
| 6 | **Das Kernsystem wird in Q1/2027 ersetzt.** Anbieterauswahl läuft. Jede tiefe Integration in die heutige Branchensoftware ist in sechs Monaten Altlast | `Fakt` im Fall |
| 7 | **Kein Data-Science-Team, keine Datenverantwortung, kein Digitalisierungsgremium.** Reifegrad 2,2 im Mittel, Daten und Kultur auf 2 — unvalidierte Gruppeneinschätzung | `Einschätzung`, ausdrücklich unvalidiert |
| 8 | **EBIT-Marge 2,6 %.** Freigabe der Geschäftsführung bis 25.000 €, darüber quartalsweise Gesellschafterversammlung. Stufe 1 setzt 9.000 € für den Zugang an | `Fakt` im Fall |
| 9 | **Die relevanten Daten liegen nicht in Microsoft 365.** 41.000 Bewerberprofile und 41.000 Lebenslauf-PDFs liegen in der Branchensoftware, ohne offene API im Bestandsvertrag und ohne Textindex | `Fakt` im Fall |
| 10 | **Ein Werkzeug, das keiner benutzt, gibt es hier schon.** ATS-Modul 2023, 95.000 € über drei Jahre, 34 % Nutzung, nie ausgewertet, intern „noch im Aufbau" | `Fakt` im Fall |

> **Die eine Kontextzeile, die die Gewichtung am stärksten dreht, ist Nummer 6.** Diese Plattformentscheidung fällt sechs Monate vor einem Kernsystemwechsel. Damit wird Integrationstiefe zum Risiko und Wechselfähigkeit zum Wert — die genaue Umkehrung der Kursmatrix.

### 4.2 Die Gewichtung A, begründet, vor dem Scoring

**Fixiert am 2026-09-07. Jede Änderung wird im Änderungsvermerk dokumentiert, nicht still vorgenommen.**

| Nr | Kriterium | Gewicht A | Begründung der Gewichtung | Kontextzeile |
|---:|---|---:|---|---:|
| K1 | **Compliance und AVV** | **25 %** | Der ungeregelte Zustand läuft. Die Plattform ersetzt keine Idee, sondern eine laufende Verarbeitung ohne Rechtsgrundlage. Compliance ist hier kein Zulassungsthema für später, sondern der Zweck der Beschaffung | 3, 4 |
| K2 | **Verfügbarkeit gegen die Taktgrenze** | **20 %** | Im Kurs nicht vorgesehen, bei GeAT entscheidend: Jeder Monat ohne freigegebenen Ersatz ist ein Monat Verarbeitung ohne AVV. Ein Werkzeug, das 2027 kommt, löst das Problem von 2026 nicht | 4, 6, 8 |
| K3 | **Adoptionspfad und Support** | **15 %** | Kulturmerkmal 1: „Der gute Disponent hat es im Kopf, nicht im System." Kulturmerkmal 2: „Was nicht gemessen wird, ist nicht gescheitert." Das Haus hat einen dokumentierten Adoptionsfehlschlag in genau dieser Werkzeugklasse | 10 |
| K4 | **Kosten über drei Jahre (TCO)** | **15 %** | Im Kurs mit 5 % und ohne Rechnung. Bei 2,6 % EBIT-Marge und 9.000 € Ansatz ist Preis ein Auswahlkriterium, nicht eine Randnotiz. Die Zeile wird gerechnet, nicht gescort — siehe 4.4 | 8 |
| K5 | **Betriebsaufwand bei 1,5 IT-Stellen** | **10 %** | „Support" misst den Anbieter. Diese Zeile misst GeAT: wer betreibt das, wenn es läuft, und woher kommt die Kapazität | 5 |
| K6 | **Exit, Portabilität, Anschlussfähigkeit (inkl. MCP)** | **10 %** | Im Kurs zweimal gerügt: Lock-in wird benannt, aber nicht geprüft; MCP steht mit 10 %. Bei GeAT operativ: das Kernsystem wechselt Q1/2027. Die Plattform muss den Wechsel überleben | 6 |
| K7 | **RAG und Integrationstiefe** | **3 %** | **Die stärkste Abweichung von der Kursmatrix (dort 20 %).** In Stufe 1 fügt ein Mensch den Lebenslauf selbst ein. RAG über den Bewerberbestand ist Stufe 4 und heute technisch unmöglich: keine offene API, kein Textindex, 63 % der Profile ohne strukturierte Felder. Wer RAG jetzt bezahlt, bezahlt eine Funktion, deren Voraussetzung 12 bis 18 Monate entfernt ist | 9 |
| K8 | **Deployment-Flexibilität** | **2 %** | **Die zweite große Abweichung (Kursmatrix 25 %).** Siehe Kasten | 1, 5 |
| | **Summe** | **100 %** | | |

> **Warum Deployment bei GeAT 2 % wiegt und beim Versicherer 25 %.** Der Versicherer mit 1.200 Beschäftigten hat Regulierungsdruck **und** Größe: er kann Single-Tenant oder Bring-your-own-Cloud fordern und erfüllt die Seat-Schwelle. GeAT hat den Regulierungsdruck, aber nicht die Größe. Bei 69 Seats liegt jede Enterprise-Plattform unterhalb der Schwellen für Single-Tenant (typisch ab 1.000 Seats) und On-Premise (typisch ab 5.000) — und es gibt keine 1,5 IT-Stellen, die einen Kubernetes-Cluster betreiben könnten. **Für GeAT ist Multi-Tenant SaaS in der EU die einzige verfügbare Option, bei jedem Anbieter.** Ein Kriterium, das die Kandidaten nicht trennen kann, bekommt ein kleines Gewicht, kein großes.
>
> Die Folge daraus ist kein Verzicht, sondern eine Verschiebung: Was der Versicherer **architektonisch** erfüllt, muss GeAT **vertraglich** erfüllen — über T1, T2, T3 und über die Prüffrage aus dem Coursebook, nach der fast niemand fragt: *„Können wir in 18 Monaten wechseln, wenn sich die Anforderungen verschärfen?"* Deshalb wandert das Gewicht nach K6, nicht ins Leere.

### 4.3 Die fünf Optionen

| Spalte | Option | Kategorie | Referenz |
|---|---|---|---|
| **A** | **Integrierte Enterprise-KI-Plattform, EU-Anbieter.** Multi-Tenant SaaS in der EU, mehrere Modelle austauschbar, REST und MCP, AVV als Standardangebot | Integrierte Plattform | Langdock-Typ |
| **B** | **Microsoft 365 Copilot.** Aufsatz auf den bestehenden M365-Vertrag von 2020, KI in Word, Outlook, Teams, Zugriff über Microsoft Graph | Integrierte Plattform | Copilot for M365 |
| **C** | **Cloud-ML-Plattform.** Eigener Aufbau: Modellzugang, Oberfläche, Authentifizierung, Protokollierung, Betrieb in Eigenregie | Cloud-ML | Vertex AI, Bedrock, Azure AI Foundry |
| **D** | **KI-Funktionen des Branchensoftware-Anbieters 2027.** Als Anforderung in die laufende Migrationsausschreibung geschrieben statt separat beschafft | Produktfunktion des Kernsystems | — |
| **E** | **Nullvariante.** Kein Plattformvertrag. Verbot der privaten Nutzung, Einzelfallfreigabe für zwei Personen, Rest über bestehende Textbausteine | keine | — |

> **Spalte D steht in keiner Kursmatrix, und sie ist bei GeAT die wichtigste.** Der Anbieterauswahlprozess für die Migration läuft **jetzt** ([`vorhaben.md`](vorhaben.md), parallele Initiativen). Eine Anforderung, die vor Vertragsschluss in der Ausschreibung steht, kostet Verhandlungsaufwand. Dieselbe Anforderung danach ist ein Change Request mit Anbietermonopol. Das ist keine technische, sondern eine Terminfrage — und sie hat ein Ablaufdatum.
>
> **Spalte E steht ebenfalls nicht in der Kursmatrix**, und das Coursebook rügt genau das (Abschnitt 9 Punkt 5). Eine Vorlage ohne Nullvariante zwingt das Gremium zu einem Kauf. In Teil B wird die Nullvariante zur zweitbesten Option — das wäre ohne die Spalte nicht sichtbar geworden.

### 4.4 Die Kostenzeile, gerechnet statt gescort

Coursebook 3.1 Abschnitt 9 Punkt 4: Preis steht mit 5 % in der Beispielmatrix — ohne TCO. Hier wird gerechnet. **Alle Preise sind Listenwerte nach meinem Kenntnisstand und ausdrücklich prüfpflichtig; kein Angebot liegt vor.**

| Option | Lizenz/Jahr, 20 Seats | Lizenz/Jahr, 69 Seats | Lizenz 3 Jahre, 20 Seats | Vorleistung, nicht in der Lizenz | Herkunft |
|---|---:|---:|---:|---|---|
| **A** EU-Plattform | 4.800 – 7.200 € | 16.560 – 24.840 € | 14.400 – 21.600 € | Nutzerverwaltung, Freigabe der Bausteine aus Hübners Prompt-Sammlung (2.000 € in Stufe 1 veranschlagt) | Bandbreite marktüblich 20–30 €/Seat/Monat, **kein Listenpreis öffentlich, Angebot einzuholen** |
| **B** M365 Copilot | **7.200 €** | **24.840 €** | 21.600 € | **Berechtigungsbereinigung in SharePoint — Aufwand unbeziffert.** Copilot zeigt, was die fragende Person sehen darf, und alles, was sie versehentlich sehen darf | Listenpreis ca. 30 €/Nutzer/Monat bei Jahresbindung, **Stand prüfen** |
| **C** Cloud-ML | Verbrauch, gering | Verbrauch, gering | — | **Der bestimmende Posten.** Oberfläche, Authentifizierung, Protokollierung, Betrieb. Ohne Angebot nicht seriös zu beziffern | **Lücke — und die Lücke ist selbst das Ergebnis** |
| **D** Branchensoftware 2027 | nicht separat | nicht separat | — | Verhandlungsaufwand in der laufenden Ausschreibung. Nach Vertragsschluss: Change Request | **Lücke, verhandelbar. 620.000 € sind für die Migration bereits reserviert** |
| **E** Nullvariante | 0 € | 0 € | 0 € | Kontrollaufwand plus DSB-Stunden (nach Stunden abgerechnet). Das Risiko der laufenden Verarbeitung ohne AVV ist nicht bezifferbar | **Lücke, nicht null** |

**Drei Rechnungen, die aus dieser Tabelle folgen:**

1. **Nur der enge Zuschnitt passt in Stufe 1.** 9.000 € sind angesetzt. 20 Seats passen bei A und B, 69 Seats bei keinem von beiden.
2. **Copilot für alle 69 Stammkräfte kostet 24.840 € im Jahr — so viel wie der gesamte Projektposten des IT-Budgets 2026 (25.000 €).** Beide Zahlen stehen im Fall, und sie treffen sich auf 160 €.
3. **Und hier ein Befund, der in keiner Anbieterunterlage steht:** 24.840 € liegen **160 € unter der Freigabegrenze der Geschäftsführung**. Über drei Jahre sind es 74.520 € — das Dreifache der Grenze. Wer die Maßnahme in Jahresraten vorlegt, hält die 25.000-Euro-Grenze formal ein und umgeht die Gesellschafterversammlung. Das ist kein Vorschlag, sondern eine Warnung: es wird jemand vorschlagen, und die Antwort muss vorher aufgeschrieben sein. **Die Freigabegrenze gilt für die Maßnahme, nicht für die Jahresrate.**

---

## 5. Matrix A — das Ergebnis

Rechenregel: **Score (1–4) × Gewichtung = gewichteter Punktwert**, Summe der Spalte = Gesamtscore.

| Kriterium | Gewicht | A · EU-Plattform | B · Copilot | C · Cloud-ML | D · Branchensw. 2027 | E · Nullvariante |
|---|---:|---:|---:|---:|---:|---:|
| K1 Compliance und AVV | 25 % | **4** → 1,00 | 3 → 0,75 | 3 → 0,75 | 2 → 0,50 | 2 → 0,50 |
| K2 Verfügbarkeit gegen die Taktgrenze | 20 % | **4** → 0,80 | 3 → 0,60 | 1 → 0,20 | 1 → 0,20 | 2 → 0,40 |
| K3 Adoptionspfad und Support | 15 % | 3 → 0,45 | **4** → 0,60 | 1 → 0,15 | 3 → 0,45 | 2 → 0,30 |
| K4 Kosten über drei Jahre | 15 % | 3 → 0,45 | 2 → 0,30 | 1 → 0,15 | **4** → 0,60 | 3 → 0,45 |
| K5 Betriebsaufwand bei 1,5 IT-Stellen | 10 % | **4** → 0,40 | 3 → 0,30 | 1 → 0,10 | **4** → 0,40 | 3 → 0,30 |
| K6 Exit, Portabilität, MCP | 10 % | **4** → 0,40 | 2 → 0,20 | 3 → 0,30 | 1 → 0,10 | **4** → 0,40 |
| K7 RAG und Integrationstiefe | 3 % | 4 → 0,12 | 3 → 0,09 | 4 → 0,12 | 4 → 0,12 | 1 → 0,03 |
| K8 Deployment-Flexibilität | 2 % | 3 → 0,06 | 2 → 0,04 | 3 → 0,06 | 2 → 0,04 | 1 → 0,02 |
| **Gesamtscore A** | **100 %** | **3,68** | **2,88** | **1,83** | **2,41** | **2,40** |
| *unabhängig belegt?* | | *nein* | *teilweise* | *teilweise* | *nein — Anbieter nicht ausgewählt* | *entfällt* |

### 5.1 Die Begründungen, auf die es ankommt

Der Score ist die Zusammenfassung. Entschieden wird über die Zellen.

**K1 Compliance — warum Copilot hier nur eine 3 bekommt, obwohl sein AVV schon existiert.** Das ist die unbequemste Zelle der Matrix, und sie muss erklärt werden. Copilot ist die **einzige** Option, deren Auftragsverarbeitungsvertrag heute vorliegt: der M365-Vertrag von 2020. Auf dem Teilaspekt „AVV" wäre das eine 5 nach den Ankern — vertraglich zugesichert. Trotzdem 3 auf das Kriterium, weil Copilots Compliance nicht im Vertrag entschieden wird, sondern in der Berechtigungsstruktur: die Plattform zeigt jeder fragenden Person alles, was sie sehen darf. Ob GeATs SharePoint-Berechtigungen dafür geprüft sind, ist **im Profil nicht dokumentiert** — in einem Haus, in dem Kundenhistorie in persönlichen Outlook-Ordnern liegt und jede Niederlassung eigene Excel-Listen führt, ist eine geprüfte Struktur unwahrscheinlich (`Einschätzung`, keine Feststellung). Nach den Ankern: „teilweise, mit Aufwand herstellbar" = 3. **Der vorhandene AVV bleibt trotzdem ein echter Vorteil, den die Zahl 3 nicht trägt. Genau das ist gemeint, wenn es heißt: im Plenum zählt nicht der Score, sondern die Begründung.**

**K2 Verfügbarkeit — die Zelle, die Spalte D in Teil A erledigt.** Die Branchensoftware-Option bekommt eine 1, nicht weil sie schlecht ist, sondern weil sie zwölf bis achtzehn Monate zu spät kommt. Der Umstieg ist Q1/2027; eine KI-Funktion darin ist danach. Bis dahin läuft die Verarbeitung ohne AVV weiter. Dieselbe Spalte gewinnt in Teil B, wo dieses Kriterium wegfällt.

**K3 Adoption — Spalte D bekommt eine 3, obwohl der Adoptionspfad strukturell der beste ist.** Eine Funktion im System, in dem die Disponenten seit 2013 arbeiten, ist der kürzeste Adoptionsweg überhaupt: kein neues Werkzeug, keine neue Anmeldung. Strukturell eine 4. Empirisch eine 2 — das ATS-Modul 2023 liegt in genau diesem System bei 34 % Nutzung, nach einer Schulung von einem halben Tag je Niederlassung. Ein Werkzeug im gewohnten System ist kein Adoptionsversprechen, wenn im gewohnten System schon ein ungenutztes Werkzeug liegt. 3, mit offengelegtem Widerspruch.

**K6 Exit — Spalte D bekommt eine 1, und das ist der Preis der günstigsten Option.** KI-Funktion und Kernsystem in einem Vertrag heißt: wer die KI wechseln will, wechselt das Kernsystem. Das ist exakt die Lage von 2013, die den Fall heute schwierig macht — ein Bestandsvertrag ohne offene Schnittstelle. Lock-in ist kein prinzipielles Problem, aber er muss **bewusst** eingegangen werden. Bewusst heißt hier: in der Ausschreibung 2026 mit einer Exit-Klausel, nicht 2028 mit einer Bitte.

**K7 RAG — die Zelle, in der Copilots größte Stärke wertlos wird.** In der Kursmatrix hat Copilot bei RAG eine 5, den Höchstwert der ganzen Tabelle. Bei GeAT liegen die relevanten Daten — 41.000 Profile, 41.000 Lebenslauf-PDFs — nicht in Microsoft 365, sondern in der Branchensoftware, ohne offene API. Microsoft Graph erreicht sie nicht. Die Fähigkeit bleibt hoch, ihre Reichweite ist null. Bei 3 % Gewicht macht die Differenz 0,03 Punkte aus. **Das ist der Beweis für die Kurspointe in einer Zelle: dieselbe Plattform, dieselbe Fähigkeit, ein anderer Kontext, und aus dem stärksten Argument des Anbieters wird eine Randnotiz.**

**C · Cloud-ML mit 1,83 — der Reifegradfehler, nicht ausgerechnet, sondern begründet.** Coursebook Abschnitt 4: *„Fehler Nr. 1: Eine Predictive-Plattform für eine Reactive-Organisation kaufen."* Und wörtlich zu Vertex AI: *„Eine Sachbearbeiterin arbeitet damit nicht."* Ich stütze den Ausschluss aber **nicht** auf die Reifegradverteilung — die Zahlen (6/14/42/25/13 %) stammen aus einer Erhebung von Juni 2021, vor ChatGPT, und tragen als Muster, nicht als aktuelle Verteilung. Der Ausschluss stützt sich auf zwei prüfbare Befunde aus dem Fall: **kein Data-Science-Team** und **1,5 IT-Stellen, beide durch die Migration gebunden**. Wer widersprechen will, bestreitet einen dieser zwei Befunde, nicht eine Prozentzahl von 2021.

**D 2,41 gegen E 2,40 — hier kann der Score nicht entscheiden.** Ein Hundertstel Differenz zwischen „auf das Kernsystem 2027 warten" und „nichts kaufen" ist keine Aussage, sondern ein Rundungsartefakt. Die beiden Optionen sind auf verschiedenen Wegen an derselben Stelle gelandet: D ist inhaltlich stark und terminlich unmöglich, E ist terminlich sofort und inhaltlich wirkungslos. **Was sie trennt, steht nicht in der Matrix:** die Nullvariante scheitert an dem Grund, der schon im Transformationsvorschlag steht — *ein Verbot ohne Ersatz. Wenn der freigegebene Zugang schlechter ist als das, was die neun Personen heute nutzen, wandert die Nutzung zurück und wird nur unsichtbarer.* Die Nullvariante bietet keinen Ersatz. Sie beendet den Zustand nicht, sie macht ihn unbeobachtbar.

### 5.2 Ergebnis Teil A

**Option A, die integrierte EU-Plattform, gewinnt mit 3,68 gegen 2,88 — und sie gewinnt nicht wegen der Modelle.** Sie gewinnt in drei Zellen, die alle aus dem GeAT-Kontext kommen und in keiner Anbieterbroschüre stehen:

1. **Sie ist in Wochen verfügbar** (K2, 20 %), und das ist bei einer laufenden Verarbeitung ohne AVV kein Komfort, sondern der Zweck.
2. **Sie hängt nicht am Kernsystem** (K6, 10 %), das in Q1/2027 ersetzt wird. Modellagnostisch und über MCP anschlussfähig heißt hier praktisch: sie überlebt die Migration, ohne mitzuwandern.
3. **Sie erzeugt keinen Betriebsaufwand** (K5, 10 %) bei 1,5 gebundenen IT-Stellen.

**Der Zuschnitt gehört zur Empfehlung:** 20 Seats, nicht 69. Nicht aus Sparsamkeit — die neun Schatten-Nutzer und ihre unmittelbaren Kolleginnen sind die Gruppe, die das Werkzeug bereits benutzt. **Das ist das erste Vorhaben in diesem Haus, dessen Nutzer schon Nutzer sind.** Nach dem Modul 2023, das 95.000 € kostete und bei 34 % Nutzung liegt, ist das das einzige Adoptionsargument, das in diesem Haus noch Kredit hat.

---

## 6. Teil B — Stufe 4: dieselben Optionen, andere Gewichtung

### 6.1 Was sich am Kontext ändert

| Kontextzeile | Teil A (Stufe 1) | Teil B (Stufe 4) |
|---|---|---|
| Gegenstand | Anzeigentexte, Profilzusammenfassungen | **Besetzungsvorschlag: drei bis fünf Kandidaten mit Begründung** |
| AI-Act-Einstufung | kein Bewerberauswahlsystem | **voraussichtlich Hochrisiko, Annex III Nr. 4** — rechtliche Arbeitshypothese, vor Einsatz zu dokumentieren |
| Datenzugang | Mensch fügt den Lebenslauf ein | **System durchsucht 41.000 Profile und 41.000 PDFs standortübergreifend** |
| Termin | sofort, GF-Beschluss, 9.000 € | **Q2/2027, Gesellschafterversammlung, 60.000 €** |
| Voraussetzungen | keine | **Stufe 1 bis 3 gelaufen:** Betriebsvereinbarung unterzeichnet, Qualifikationskatalog, Pflichtfelder, Nichtbesetzungsgrund, Löschkonzept in Betrieb, Migration abgeschlossen |
| Zwei nicht verhandelbare Konstruktionsregeln | — | **Begründung und nicht vorgeschlagene Kandidaten sichtbar** · **Rangfolge nach Erfüllungsgrad, nicht nach Erfolgsprognose** |

**Die Regel, die dahinter steht, und die im Kurs nicht vorkommt** (`rechtliche Arbeitshypothese`, von Marnitz zu prüfen): Wer ein Hochrisiko-KI-System unter eigenem Namen in Betrieb nimmt oder ein bestehendes wesentlich umzweckt, kann nach AI Act vom **Betreiber zum Anbieter** werden — mit Konformitätsbewertung, technischer Dokumentation, Registrierung und Herstellerhaftung. Baut GeAT den Besetzungsassistenten selbst auf einer generischen Plattform, trägt GeAT diese Pflichten. Kauft GeAT eine Produktfunktion, die der Anbieter als Hochrisikosystem in Verkehr bringt, bleibt GeAT Betreiber. **Das ist bei 69 Stammkräften und 1,5 IT-Stellen der Unterschied zwischen machbar und nicht machbar — und es ist der Punkt, an dem die Matrix kippt.**

### 6.2 Gewichtung B, begründet, vor dem Scoring

**Fixiert am 2026-09-07, unabhängig von Gewichtung A gesetzt.**

| Nr | Kriterium | Gewicht B | (A) | Begründung der Änderung |
|---:|---|---:|---:|---|
| L1 | **AI-Act-Betreiberfähigkeit** (Rollenverteilung, Protokollierung, technische Dokumentation, Konformitätsbewertung) | **30 %** | 25 % | Bei Annex III ist Datengovernance Zulassungsvoraussetzung, nicht Reifegradziel. Und die Frage, wer Anbieter ist, entscheidet über die Machbarkeit |
| L2 | **Zugang zu den Bewerberdaten und RAG-Tiefe** | **25 %** | 3 % | **Die größte Verschiebung.** Ohne Zugriff auf 41.000 Profile und PDFs gibt es keinen Assistenten. In Stufe 1 war das irrelevant, hier ist es der Gegenstand |
| L3 | **Nachvollziehbarkeit und wirksame menschliche Aufsicht** (Begründung, nicht vorgeschlagene Kandidaten, Rangfolgelogik steuerbar) | **20 %** | — | Neu. Der Disponent muss begründet abweichen **können**. Eine Liste ohne Begründung erfüllt das nicht, auch wenn ein Mensch bestätigt. Hier hängt auch der Bias-Fall: Rangfolge nach Erfüllungsgrad statt nach Erfolgsprognose muss steuerbar sein |
| L4 | **Kosten über drei Jahre** | **10 %** | 15 % | 60.000 € sind bereits in der Taktung eingeplant und gehen ohnehin durch die Gesellschafterversammlung. Der Preis entscheidet hier weniger als in Stufe 1 |
| L5 | **Betriebsaufwand** | **8 %** | 10 % | unverändert relevant, aber von L1 teilweise absorbiert |
| L6 | **Exit, Portabilität, MCP** | **5 %** | 10 % | Nach der Migration ist die Systemlandschaft für Jahre gesetzt. Der Wechselhorizont ist länger, das Gewicht kleiner |
| L7 | **Adoptionspfad und Support** | **2 %** | 15 % | Der Pilot umfasst sechs Disponenten aus zwei Niederlassungen und vier Recruiter — handverlesen, mit Rehberg als eingekauftem Pilotstandort (Stufe 5). **Adoption wird hier organisatorisch bezahlt, nicht beim Anbieter gekauft** |
| — | *Verfügbarkeit gegen die Taktgrenze* | **0 %** | 20 % | **Fällt weg.** Stufe 4 ist auf Q2/2027 terminiert. Es gibt keinen laufenden Rechtsverstoß zu beenden — Stufe 1 hat ihn beendet |
| — | *Deployment-Flexibilität* | **0 %** | 2 % | **Fällt weg.** Immer noch 69 Seats, immer noch SaaS als einzige verfügbare Option. Ein Kriterium ohne Trennschärfe wird gestrichen, nicht mitgeschleppt |
| | **Summe** | **100 %** | | |

### 6.3 Matrix B

| Kriterium | Gewicht | A · EU-Plattform | B · Copilot | C · Cloud-ML | D · Branchensw. 2027 | E · Nullvariante |
|---|---:|---:|---:|---:|---:|---:|
| L1 AI-Act-Betreiberfähigkeit | 30 % | 2 → 0,60 | 2 → 0,60 | 2 → 0,60 | **4** → 1,20 | **4** → 1,20 |
| L2 Zugang zu den Bewerberdaten, RAG | 25 % | 2 → 0,50 | 1 → 0,25 | 3 → 0,75 | **4** → 1,00 | 1 → 0,25 |
| L3 Nachvollziehbarkeit, menschliche Aufsicht | 20 % | 3 → 0,60 | 2 → 0,40 | **4** → 0,80 | 2 → 0,40 | **4** → 0,80 |
| L4 Kosten über drei Jahre | 10 % | 3 → 0,30 | 2 → 0,20 | 1 → 0,10 | **4** → 0,40 | **4** → 0,40 |
| L5 Betriebsaufwand | 8 % | 3 → 0,24 | 3 → 0,24 | 1 → 0,08 | **4** → 0,32 | **4** → 0,32 |
| L6 Exit, Portabilität, MCP | 5 % | **4** → 0,20 | 2 → 0,10 | 3 → 0,15 | 1 → 0,05 | **4** → 0,20 |
| L7 Adoptionspfad und Support | 2 % | 3 → 0,06 | **4** → 0,08 | 1 → 0,02 | 3 → 0,06 | **4** → 0,08 |
| **Gesamtscore B** | **100 %** | **2,50** | **1,87** | **2,50** | **3,43** | **3,25** |

### 6.4 Der Sieger wechselt — und die Nullvariante wird Zweite

| Option | Score A (Stufe 1) | Score B (Stufe 4) | Bewegung |
|---|---:|---:|---|
| **A** EU-Plattform | **3,68** · Platz 1 | 2,50 · Platz 3 | **−1,18** |
| **B** Copilot | 2,88 · Platz 2 | 1,87 · Platz 5 | −1,01 |
| **C** Cloud-ML | 1,83 · Platz 5 | 2,50 · Platz 3 | +0,67 |
| **D** Branchensoftware 2027 | 2,41 · Platz 3 | **3,43** · Platz 1 | **+1,02** |
| **E** Nullvariante | 2,40 · Platz 4 | **3,25** · Platz 2 | +0,85 |

**Dieselben fünf Optionen. Dieselbe Rechenregel. Dieselben Anker. Andere Gewichtung, anderer Sieger.** Das ist die Kurspointe, nicht als Beispiel, sondern am eigenen Fall — und sie fällt hier härter aus als beim Versicherer gegen das Handelsunternehmen, weil sich nicht der Kunde ändert, sondern nur der Verwendungszweck **innerhalb desselben Unternehmens, im Abstand von einem Jahr.**

**Drei Befunde, die aus der Bewegung folgen und wichtiger sind als die Zahlen:**

**Erstens: Spalte D gewinnt aus einem einzigen Grund, und der hat ein Ablaufdatum.** L1 mit 30 % — nur bei der Produktfunktion eines Branchenanbieters bleibt GeAT **Betreiber** statt **Anbieter** eines Hochrisikosystems. Diese 4 ist aber keine Feststellung, sondern eine Bedingung: sie gilt nur, wenn die Anbieterpflichten nach AI Act **in der Ausschreibung 2026 stehen**. Wer sie 2028 nachfragt, bekommt eine Roadmap und damit nach den Ankern eine 2 — und Spalte D fällt von 3,43 auf 2,83. Dieselbe Logik trägt L3: die 2 dort ist auf 4 hebbar, wenn „Rangfolge nach Erfüllungsgrad, nicht nach Erfolgsprognose" und „Begründung plus nicht vorgeschlagene Kandidaten sichtbar" als Ausschreibungsanforderungen formuliert werden. Nach Vertragsschluss ist beides ein Change Request bei einem Anbieter ohne Wettbewerb.

**Zweitens: A und C landen beide auf 2,50 — auf völlig verschiedenen Wegen.** Die EU-Plattform ist bequem, betriebsarm und erreicht die Daten nicht. Die Cloud-ML-Plattform erreicht die Daten, gibt volle Kontrolle über die Rangfolgelogik — der einzige Weg, den Bias-Fall wirklich zu messen statt zu behaupten — und ist mit 1,5 IT-Stellen nicht betreibbar. **Ein Gesamtscore, der zwei so unterschiedliche Optionen gleich bewertet, ist der Beweis dafür, dass der Score nicht die Entscheidung ist.** Wer nur die Zahl vorlegt, legt nichts vor.

**Drittens, und das ist der unbequemste Befund: die Nullvariante ist bei Stufe-4-Gewichtung mit 3,25 die zweitbeste Option** — besser als drei der vier Werkzeuge. Kein Hochrisikosystem, keine Konformitätspflicht, keine Anbieterrolle, vollständige menschliche Entscheidung, keine Kosten. Das ist **kein Argument gegen das Vorhaben.** Es ist die präzise Begründung dafür, warum Stufe 4 nicht 2026 als Plattformkauf entschieden wird, sondern 2026 als Ausschreibungsanforderung und 2027 als Pilot. **Wenn Spalte D wegfällt, ist „keinen Assistenten bauen" die beste verbleibende Option** — und dann ist das Vorhaben ein anderes. Diese Zeile gehört in die Vorlage, bevor jemand sie findet.

---

## 7. Was kein Score misst

Vier Dinge, die keine Zelle dieser Matrix erfasst und die trotzdem über den Erfolg entscheiden. Sie gehören in „Offene Fragen", nicht in eine Punktzahl.

**7.1 Haftung ist keine Plattformeigenschaft.** Am 19.02.2024 entschied das kanadische Civil Resolution Tribunal in *Moffatt v. Air Canada* gegen die Airline: das Unternehmen haftet für die Auskünfte auf seiner Website, unabhängig davon, welches System sie erzeugt. Für GeAT übersetzt: **das Kandidatenprofil, das an den Kundenbetrieb geht, ist die Auskunft.** 4,8 Profile je Besetzung, rund 6.000 im Jahr. Wenn eines eine Qualifikation ausweist, die im Lebenslauf nicht steht, haftet GeAT — und der Kunde erfährt es beim Einsatz, nicht beim Lesen. Daraus folgen zwei Anforderungen, die Plattformfunktionen sind und keine Zusatzwünsche: **Protokollierung jedes freigegebenen Profils** und ein **Rückfallpfad**, der ohne den Assistenten arbeitet.

**7.2 Kein Kriterium misst Maß.** Klarna, Februar 2024: der KI-Assistent erledigt die Arbeit von rund 700 Vollzeitkräften, zwei Drittel aller Servicechats, Lösungszeit von 11 auf unter 2 Minuten. 2025 korrigiert der CEO: man sei zu weit gegangen, die Servicequalität habe gelitten. Kein Kriterium der Matrix hätte das erfasst — sie bewertet Fähigkeiten, nicht Maß im Einsatz. **Bei GeAT hat dieser Fall einen Namen:** Regina Pfaff, 59, kennt in 40 Kundenbetrieben die Meister mit Vornamen und weiß, wer mit wem nicht kann. Wenn der Assistent trägt und die Zahlen stimmen, geht 2030 mit ihr das Wissen, aus dem er gelernt hat — und niemand merkt es, weil die Kennzahlen gut aussehen. Die Vorkehrung dagegen steht nicht in der Matrix, sondern in Stufe 5 des Transformationsvorschlags: Pfaffs Kundenbetriebswissen strukturiert erfassen, **bevor** der Assistent kommt.

**7.3 Alle Belege sind Herstellerangaben.** Deployment-Optionen, Compliance-Zusagen, MCP-Unterstützung, Preise — jede Quelle für diese Analyse ist eine Anbieterseite oder eine Anbieterdokumentation. Für eine Vorlage an die Gesellschafterversammlung ist „steht auf der Anbieterseite" die schwächste Belegform. Die Zeile *unabhängig belegt?* in Matrix A steht deshalb auf **nein** oder **teilweise**, bei jeder Spalte. Was fehlt und in die Ausschreibung gehört: **zwei Referenzkunden gleicher Größenordnung im DACH-Raum, davon einer aus der Personaldienstleistung**, mit Gesprächserlaubnis.

**7.4 Die Reifegradzahlen sind von 2021.** Die Verteilung 6/14/42/25/13 % stammt aus einer Erhebung von Juni 2021 (N = 1.500) — vor ChatGPT. Sie trägt im Kurs die Aussage „Fehler Nr. 1", und die Aussage bleibt plausibel; die Prozentzahlen sind es nach fünf Jahren nicht mehr. Ich zitiere sie deshalb als Muster mit Jahresangabe und stütze den Ausschluss von Spalte C auf zwei Befunde aus dem Fall, nicht auf die Tabelle ([5.1](#51-die-begründungen-auf-die-es-ankommt)). Dazu die zweite Einschränkung, die aus dem eigenen Haus kommt: **der GeAT-Reifegrad 2,2 ist selbst eine unvalidierte Gruppeneinschätzung.** Jede Aussage dieser Analyse, die darauf aufbaut, trägt diesen Vorbehalt mit.

---

## 8. Gegenargumente und Risiken

Nicht im Anhang, weil sie zum Ergebnis gehören. Sechs Einwände, jeder mit Rolle, weil jeder von jemandem kommen wird.

**8.1 Achtelik (GF Finanzen/IT, Macht 4): „Keine zweite Baustelle vor dem Umstieg."** Der Einwand ist berechtigt und trifft Empfehlung 1 nicht. Multi-Tenant SaaS mit 20 Seats bindet Nutzerverwaltung, keine Betriebskapazität — das ist die 4 in K5. Empfehlung 2 ist noch weniger eine zweite Baustelle: sie ist Migrationsarbeit, die ohnehin ansteht, nur mit drei zusätzlichen Anforderungen im Lastenheft. **Wo der Einwand trifft:** wenn die Plattform tatsächlich 69 Seats bekommt, ist Nutzerverwaltung über sechs Niederlassungen kein Nebenbei mehr. Das ist ein Grund für den engen Zuschnitt, kein Argument gegen ihn.

**8.2 Marnitz (DSB, extern): „Bewerberauswahl ist Annex III. Deployment mit 2 % ist zu leicht."** Der stärkste Einwand gegen diese Analyse. Zwei Antworten, und die erste ist eine Einschränkung. **Erstens:** Deployment mit 2 % gilt für Stufe 1 und beruht darauf, dass GeAT bei 69 Seats On-Premise gar nicht beziehen kann — nicht darauf, dass es unwichtig wäre. Wenn Marnitz On-Premise als Pflichtanforderung feststellt, ist die Konsequenz nicht ein anderes Gewicht, sondern **die Nullvariante**, weil dann keine Option verfügbar bleibt. Das gehört so vorgelegt. **Zweitens:** Stufe 1 ist kein Bewerberauswahlsystem — Anzeigentexte fallen nicht unter Annex III. Aber: eine **Profilzusammenfassung, die in die Kundenunterlage geht**, ist grenznah, und die Grenze verläuft bei „erheblichem Einfluss auf die Auswahlentscheidung" (Art. 6 Abs. 3). **Diese Abgrenzung ist vor Inbetriebnahme zu dokumentieren, nicht danach** — sie ist der erste Punkt für Marnitz und kein Nachgang zu dieser Analyse.

**8.3 Dr. Barth (Gesellschaftervertreterin, Macht 5): „Amortisation unter 24 Monaten oder wartet, bis die Software steht."** Der Einwand, dem diese Analyse **nicht** ausweicht: **Stufe 1 amortisiert sich nicht.** Sie senkt keine Kosten und verkürzt keinen Prozess. Sie beendet eine Verarbeitung ohne Rechtsgrundlage — und vermiedenes Risiko ist keine Zahl, jedenfalls keine, die ich seriös nennen kann. Wer eine Amortisation verlangt, bekommt sie aus **Stufe 2** (Quellenkennung, 48.000 € im Jahr bei zehn Prozent besserer Allokation des Anzeigenbudgets) — und deshalb steht Stufe 2 im Transformationsvorschlag **vor** dem teuren Stück. Der Rechenweg ist offengelegt, die Bezugsgröße von 480.000 € steht im Fall.

**8.4 Vollmer (Geschäftsführerin, Macht 5): „Ich habe 2023 schon einmal für ein Modul bezahlt, das keiner benutzt."** Der Einwand mit dem meisten Gewicht, weil er stimmt: 95.000 €, 34 % Nutzung, drei Jahre, nie ausgewertet. Die Antwort ist der Zuschnitt, nicht das Versprechen. **20 Seats, beginnend mit den neun Personen, die das Werkzeug seit einem Jahr benutzen — außerhalb des Hauses und ohne Vertrag.** Nutzung muss hier nicht erzeugt werden, sie muss legalisiert werden. Dazu die Vorkehrung, die 2023 gefehlt hat: eine Auswertung nach drei Monaten mit einem **vorher festgelegten Abbruchkriterium**. Wenn nach drei Monaten weniger als 15 der 20 Seats wöchentlich aktiv sind, wird der Vertrag nicht verlängert, sondern ausgewertet. `Annahme`, mit der Geschäftsführung zu bestätigen.

**8.5 Rehberg (NL Gotha, Macht 4, informeller Einfluss sehr hoch): „Wer mir vorschlagen will, wen ich schicke, hat noch nie in einer Werkhalle gestanden."** Trifft Stufe 1 nicht: der Zugang schlägt keine Kandidaten vor, er schreibt Texte. Das ist ein Vorteil des Zuschnitts und ein Grund, Stufe 1 und Stufe 4 in getrennten Vorlagen zu behandeln — wer beides zusammen vorlegt, holt sich Rehbergs Widerstand gegen den Assistenten in die Entscheidung über den Textbaustein. **Und der Einwand behält seine Kraft für Teil B**, wo er nicht durch Zuschnitt zu entschärfen ist, sondern nur durch Stufe 5: Rehberg als Pilotstandort einkaufen, nicht überzeugen.

**8.6 Der Einwand, der stimmt und den ich nicht beantworten kann.** Die gesamte Empfehlung 2 setzt voraus, dass die **Migrationsausschreibung noch offen ist**. Der Fall sagt „Anbieterauswahl läuft" — nicht, wie weit. Steht sie kurz vor Vertragsschluss, ist Spalte D tot: dann fällt die Stufe-4-Entscheidung zwischen A und C, beide bei 2,50, beide machen GeAT zum **Anbieter** eines Hochrisikosystems. **Und dann ist die Nullvariante mit 3,25 die beste verbleibende Option, und das Vorhaben, für das meine Stelle geschaffen wurde, ist ein anderes.** Das ist die wichtigste offene Frage dieser Analyse, sie ist terminkritisch, und ich kann sie nicht aus dem Profil beantworten — sie muss bei Achtelik gestellt werden, **diese Woche**.

---

## 9. Die Empfehlung

Nicht ein Werkzeug, sondern **zwei Entscheidungen mit unterschiedlichen Siegern und einem Termin dazwischen.**

### Empfehlung 1 · Jetzt: integrierte EU-Plattform, enger Zuschnitt

**Geschäftsführungsbeschluss, ≤ 9.000 € im Jahr, 20 Seats, unter der 25.000-Euro-Grenze — verliert also kein Quartal.**

| Was | Wert |
|---|---|
| Option | A · integrierte Enterprise-KI-Plattform, EU-Anbieter, Multi-Tenant SaaS |
| Score A | **3,68** von 4,00 möglichen |
| Zuschnitt | 20 Seats: Recruiting Center (9) plus Vertrieb und Innendienst, beginnend mit den neun heutigen Schatten-Nutzern |
| Verantwortlich | Balzer (IT), Kloß (Fachseite) — wie in Stufe 1 vorgesehen |
| Vor Vertragsschluss zu erfüllen | T1 AVV vorgelegt · T2 Protokollierung begrenzbar, Betriebsvereinbarung mit Nowak · T3 EU-Verarbeitung und nachweisbare Löschung |
| Abbruchkriterium, vorher festgelegt | Nach drei Monaten weniger als 15 der 20 Seats wöchentlich aktiv → auswerten, nicht verlängern |

**Die Begründung in drei Sätzen, für das Protokoll:** Sie ist die einzige Option, die den ungeregelten Zustand in Wochen beendet statt in Quartalen. Sie hängt nicht an der Branchensoftware, die in Q1/2027 ersetzt wird — sie überlebt die Migration, ohne mitzuwandern. Und sie ist die einzige, deren Nutzer schon Nutzer sind.

### Empfehlung 2 · Bis Q4/2026: die Stufe-4-Anforderungen in die Migrationsausschreibung

**Kostet keine Freigabe. Ist terminkritisch. Ist die eigentliche Entscheidung dieser Analyse.**

Spalte D gewinnt Teil B mit 3,43 — **aber nur, solange die Ausschreibung offen ist.** Sechs Anforderungen, die vor Vertragsschluss ins Lastenheft gehören:

| Nr | Anforderung | Wirkt auf |
|---:|---|---|
| 1 | **Anbieterpflichten nach EU AI Act beim Anbieter**, schriftlich: Konformitätsbewertung, technische Dokumentation, Registrierung. GeAT bleibt Betreiber | L1 · die 4, die Spalte D gewinnen lässt |
| 2 | **Rangfolge nach Erfüllungsgrad der Anforderung, nicht nach Erfolgsprognose.** Konfigurierbar und dokumentiert | L3 · hebt 2 auf 4 · Bias-Fall |
| 3 | **Begründung und nicht vorgeschlagene Kandidaten sichtbar** in der Oberfläche | L3 · wirksame menschliche Aufsicht |
| 4 | **Offene API** für Bewerberdaten und Anzeigen, mit Quellenkennung im Rücklauf | L2 · und Stufe 2, die daran heute scheitert |
| 5 | **Qualifikationskatalog, Pflichtfelder, Gültigkeitsdatum, Nichtbesetzungsgrund** als Felder im Zielsystem | Stufe 3a und 3d, ohne Nacharbeit |
| 6 | **Exit-Klausel und Datenportabilität:** in welchem Format, in welcher Zeit, zu welchem Preis | L6 · die 1, die der Preis dieser Option ist |
| — | **Und die Zeile, die nicht aus dieser Analyse kommt:** Doreen Ritschel in die Anforderungserhebung. Welcher Kundenbetrieb welches Zeitnachweis-Format akzeptiert, steht auf einem Pinnwand-Ausdruck und in keinem Lastenheft | 17.700 € im Jahr, kein KI-Fall |

**Warum das die eigentliche Entscheidung ist:** Anforderung 1 ist der einzige Grund, warum Stufe 4 für GeAT überhaupt machbar ist. Sie ist in der laufenden Ausschreibung Verhandlungsaufwand und danach ein Change Request bei einem Anbieter ohne Wettbewerb. **Wer Empfehlung 2 verpasst, entscheidet damit auch Stufe 4 — nur ohne es zu merken, und gegen 3,25 für „nichts bauen".**

### Empfehlung 3 · Nicht jetzt, und warum nicht

| Option | Score A / B | Warum nicht |
|---|---:|---|
| **B · Microsoft 365 Copilot** | 2,88 / 1,87 | Bei 69 Seats 24.840 € im Jahr — 160 € unter der Freigabegrenze, über drei Jahre 74.520 €. Die Vorleistung (Berechtigungsbereinigung in SharePoint) ist unbeziffert. Und der stärkste Punkt der Plattform greift nicht: **Microsoft Graph erreicht die 41.000 Bewerberprofile nicht, weil sie nicht in M365 liegen.** Nicht ausgeschlossen — der vorhandene AVV bleibt ein echter Vorteil, und nach der Migration ist die Zelle L2 neu zu bewerten. Aber nicht als Stufe-1-Werkzeug |
| **C · Cloud-ML-Plattform** | 1,83 / 2,50 | *„Fehler Nr. 1: Eine Predictive-Plattform für eine Reactive-Organisation kaufen."* Belegt an zwei Befunden aus dem Fall, nicht an einer Prozentzahl von 2021: kein Data-Science-Team, 1,5 IT-Stellen und beide durch die Migration gebunden. **Sie ist bei L3 die stärkste Option von allen** — volle Kontrolle über Rangfolgelogik und Bias-Messung — und scheitert an Kapazität, nicht an Funktion. Das gehört gesagt, damit es nicht als Vorurteil gelesen wird |
| **E · Nullvariante für Stufe 1** | 2,40 | Ein Verbot ohne Ersatz. Die Nutzung wandert zurück und wird nur unsichtbarer. Die Nullvariante beendet den Zustand nicht, sie beendet die Beobachtung. **Für Stufe 4 ist sie mit 3,25 die zweitbeste Option und bleibt in der Vorlage stehen** |
| **Ein Assistent auf Option A oder C** | 2,50 / 2,50 | Beide machen GeAT voraussichtlich zum **Anbieter** eines Hochrisikosystems nach Annex III — mit Konformitätsbewertung, technischer Dokumentation und Registrierung, bei 1,5 IT-Stellen. Das ist keine Budget-, sondern eine Machbarkeitsfrage (`rechtliche Arbeitshypothese`, von Marnitz zu prüfen) |

---

## 10. Offene Punkte und Prüffragen

### 10.1 Was diese Analyse nicht beantworten kann

| Nr | Offener Punkt | An wen | Bis wann | Was davon abhängt |
|---:|---|---|---|---|
| 1 | **Wie weit ist die Migrationsausschreibung?** Vor Vertragsschluss oder nach? | Achtelik | **diese Woche** | Empfehlung 2 vollständig. Fällt Spalte D weg, ist die Nullvariante die beste Stufe-4-Option |
| 2 | **Welche Branchensoftware ist es, und was kann der Nachfolger?** Die wertvollste offene Rechercheposition des ganzen Falls | Balzer, Achtelik | Q4/2026 | Spalte D ist ohne diese Antwort nicht scorebar — die 2 bei L1 in Matrix A ist bis dahin eine Platzhalterzahl |
| 3 | **Ist die Profilzusammenfassung für die Kundenunterlage schon Annex III?** Abgrenzung nach Art. 6 Abs. 3, vor Inbetriebnahme zu dokumentieren | Marnitz | vor Vertragsschluss Stufe 1 | Ob Empfehlung 1 überhaupt so zuschneidbar ist |
| 4 | **Sind die SharePoint-Berechtigungen geprüft?** Im Profil nicht dokumentiert | Balzer | vor jeder Copilot-Bewertung | Zelle K1/B — die 3 kann eine 4 oder eine 2 sein |
| 5 | **Stellt Marnitz On-Premise als Pflichtanforderung fest?** | Marnitz | vor der GF-Vorlage | Bei „ja" bleibt keine Option verfügbar, und die Vorlage lautet Nullvariante |
| 6 | **Trägt der Investitionsspielraum die Taktung noch?** 900.000 € sind aus einem EBIT von 0,9 Mio abgeleitet; bei 0,805 Mio bleiben nach der Migrationsreservierung 185.000 statt 280.000, und die Stufen 1 bis 5 kosten 240.000 | Ziegenhorn | Business Case Woche 6 | Nicht diese Analyse, aber die Reihenfolge, die sie voraussetzt |

### 10.2 Die Prüffragen für das Anbietergespräch

Nicht „sind Sie DSGVO-konform", sondern das Dokument. Rote Flagge: *„Wir sind DSGVO-konform"* ohne vorgelegten AVV — das ist eine Marketingaussage, keine Zusicherung.

1. **Legen Sie den AVV vor** — das Dokument, nicht die Aussage. Dazu ISO 27001 oder SOC 2, und wo genau die Daten verarbeitet werden.
2. **Welche Nutzerprotokolle entstehen, wer kann sie einsehen, und lässt sich der Umfang vertraglich begrenzen?** (Das ist Nowaks Frage, und sie entscheidet über die Betriebsvereinbarung.)
3. **Können wir in 18 Monaten wechseln, wenn sich die Anforderungen verschärfen?** Die Frage, nach der laut Coursebook fast niemand fragt.
4. **Wie bekommen wir unsere Daten und Prompts wieder heraus — in welchem Format, in welcher Zeit, zu welchem Preis?**
5. **Wie löschen Sie auf Anforderung nachweisbar?** (18.000 überfällige Profile sind der Anlass, nicht das Beispiel.)
6. **Nennen Sie zwei Referenzkunden im DACH-Raum unter 150 Beschäftigten, davon einen aus der Personaldienstleistung, mit Gesprächserlaubnis.** Herstellerangaben sind die schwächste Belegform.
7. **Wer trägt bei einem Hochrisikosystem nach Annex III welche Pflicht — Anbieter oder Betreiber?** Schriftlich, vor der Ausschreibung, nicht im Protokoll danach.

### 10.3 Was ich an dieser Analyse selbst nicht belastbar finde

Vier Stellen, an denen ich widersprechen würde, wenn jemand anders sie vorlegt:

1. **Gewichtung A ist meine Setzung.** K2 mit 20 % ist im Kurs nicht vorgesehen und entscheidet Teil A mit. Wer K2 auf 5 % senkt, weil ein Rechtsverstoß mit AVV-Lücke nicht als terminkritisch gilt, sieht ein anderes Ergebnis: dann rückt Copilot auf. Ich halte die 20 % für begründet, aber nicht für unbestreitbar.
2. **Spalte D wird auf einem nicht ausgewählten Anbieter gescort.** L1 = 4 ist eine Erwartung an einen Markt, kein Befund an einem Produkt. Das ist die schwächste Zelle der ganzen Analyse — und sie trägt die zweite Empfehlung.
3. **Die Anbieterrolle nach AI Act ist eine Arbeitshypothese**, keine geprüfte Rechtsauskunft. Sie ist das Scharnier von Teil B. Wenn Marnitz sie anders sieht, kippt Matrix B.
4. **Preise sind Listenwerte nach meinem Kenntnisstand, keine Angebote.** Die Bandbreite bei Option A ist marktüblich abgeleitet, nicht erhoben. Die 24.840 € bei Copilot sind gerechnet, aber der Listenpreis dahinter ist zu verifizieren.

---

## Änderungsvermerk

| Datum | Änderung | Grund |
|---|---|---|
| 2026-09-07 | Erstfassung. Gewichtung A und Gewichtung B fixiert, vor dem Scoring | — |

> **Regel für Änderungen an den Gewichtungen:** Wer sie verschiebt, trägt die Änderung hier ein, mit Grund und Datum. Eine nachträglich verschobene Gewichtung ohne Vermerk ist kein Nachjustieren, sondern ein rückwärts gerechnetes Ergebnis.

**Verwandte Dateien:** [`transformationsvorschlag.md`](transformationsvorschlag.md) (Reihenfolge und Taktung) · [`vorhaben.md`](vorhaben.md) (Gegenstand, AI-Act-Einschätzung, parallele Initiativen) · [`systeme-daten.md`](systeme-daten.md) (Schatten-IT, Auftragsverarbeiter, Datenzustand) · [`zahlen.md`](zahlen.md) (Budget, Freigabegrenzen, IT-Budget) · [`menschen.md`](menschen.md) (Rollen, Gremien, Kulturmerkmale) · [Coursebook 3.1](../coursebook/3.1/3.1_KI-Plattformen-im-Vergleich.md) (Methode und ihre Mängel)
