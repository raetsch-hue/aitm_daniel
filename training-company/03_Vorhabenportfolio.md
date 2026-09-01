---
firma: Hellwig Fördertechnik (fiktiv)
stand: 2026-09-01
verwendung: Tag 1.4 (Kategorien), 1.5 (Kontext), 2.2 (Quick Wins)
hinweis: Die Spalte "Vorgeschlagen als" enthält absichtlich Fehler. Auflösung in 07_Dozentenhinweise.md
---

# Vorhabenportfolio

Zehn Vorhaben, wie sie im Steuerkreis, in Bereichsrunden und in Flurgesprächen tatsächlich formuliert wurden. **Die Kategorienangabe in der Spalte „Vorgeschlagen als" ist die Angabe der Vorschlagenden — nicht die richtige.** Das ist der Übungsgegenstand.

---

## Die Liste

| ID | Vorhaben | Von wem | Vorgeschlagen als | Aufwandsschätzung | Status |
|---|---|---|---|---|---|
| **V1** | Eingangsrechnungen automatisch erfassen und verbuchen | Brandtner, nach Messebesuch | „KI-Projekt Rechnungsverarbeitung" | 40 PT | beauftragt |
| **V2** | Ersatzteilangebot in 4 Stunden statt 6,5 Tagen | Kowalczyk | GenAI-Assistent | offen | Pilot beschlossen |
| **V3** | Vorausschauende Wartung für die installierte Basis | Dr. Hellwig | Predictive ML | 180 PT | im Programm |
| **V4** | Chatbot auf der Website: Lieferzeiten und Verfügbarkeit | Vertrieb Anlagen | GenAI, „schneller Erfolg" | 25 PT | Angebot liegt vor |
| **V5** | Agent bearbeitet Servicetickets Ende zu Ende | Dr. Hellwig, nach Anbietertermin | Agentic AI | 220 PT | Vorstandswunsch |
| **V6** | Prognose des Ersatzteilbedarfs, Bestandsoptimierung | Controlling | „Statistik-Auswertung" | 35 PT | zurückgestellt |
| **V7** | Tickets kategorisieren und Antwortentwürfe vorbefüllen | Ehrlicher | GenAI | 30 PT | nicht priorisiert |
| **V8** | Stücklistenübergabe Inventor → SAP | Beniers | RPA | 45 PT | in Warteschlange |
| **V9** | Vorauswahl von Bewerbungen | Personalleitung | „KI-Screening" | 20 PT | Anbieter kontaktiert |
| **V10** | Wissensassistent auf Serviceberichte und `N:\` | Semmler *(einzige eigene Meldung)* | GenAI / RAG | 90 PT | im Programm |

---

## Die vier Vorhaben, an denen im Kurs gearbeitet wird

Die übrigen sechs sind Kontrastmaterial. Diese vier tragen den Kurs.

### V1 · Eingangsrechnungen — der Kategorienfehler

**Ausgangslage.** 2.050 Rechnungen im Monat von 1.240 Lieferanten. **61 Lieferanten** liefern in immer gleichen PDF-Formaten und machen **68 % des Belegvolumens** aus. Brandtner hat auf einer Messe einen Anbieter gesehen, der „KI-basierte Rechnungsverarbeitung" verkauft, und 40 Personentage freigegeben.

**Was zu prüfen ist.** Ob eine Aufgabe, die regelhaft beschreibbar ist, ein Sprachmodell braucht. Kostenrechnung: bei 2.050 Belegen im Monat je ein Modellaufruf gegen ein einmaliges Regelwerk. Prüfbarkeit: bei welchem Anteil erfindet ein Modell plausible Werte, und wer merkt das? Datenschutz: gehen Lieferantendaten an einen externen Dienst?

**Der Lehrpunkt.** Das ist [1.4 · Beispiel 8.5](../coursebook/1.4/1.4_Vier-Wellen-KI-Kategorien-Hype-Cycle.md#85-der-kategorienfehler-genai-wo-rpa-gereicht-hätte) mit Namen und Zahlen. Die richtige Antwort ist eine geteilte: deterministisch für die 68 %, Sprachmodell nur für die Restmenge — und die Restmenge ist der einzige Teil, für den das Wort KI fällt.

**Warum es trotzdem nicht einfach ist:** Die 32 % Restmenge enthält 1.179 Lieferanten mit je ein bis zwei Belegen pro Jahr. Ein Regelwerk dafür zu bauen ist teurer als das Abtippen. Das ist die Stelle, an der die Kategorienfrage aufhört, eine Ja-Nein-Frage zu sein.

### V2 · Ersatzteilangebot — der Fall, der alles enthält

**Ausgangslage.** 12.400 Anfragen im Jahr, 47 Minuten Arbeit, 6,5 Tage Durchlauf, Auftragsquote von 47 % auf 34 % gefallen. Kowalczyk hat den Fall selbst gemeldet, mit eigener Auswertung. Der Steuerkreis hat einen „GenAI-Assistenten für Angebote" beschlossen.

**Die fünf Bestandteile der Durchlaufzeit, nach Größe:**

| Bestandteil | Arbeitstage | Was ihn löst | KI-Kategorie |
|---|---:|---|---|
| Warten auf Zeichnungsklärung aus der Konstruktion | 2,1 | Leseberechtigung des Innendienstes auf Vault — eine Entscheidung von Beniers | **keine** |
| Liegen im Postkorb, bis der Vorgang dran ist | 2,0 | Priorisierungsregel: Standardfälle zuerst, oder Kapazität | **keine** |
| Warten auf Frachtpreis | 1,4 | Gewichtsangaben nachpflegen (11 % fehlen), dann Regelrechnung | **keine**, ein Datenprojekt |
| Warten auf Preisfreigabe ab 10.000 EUR | 0,9 | Freigabegrenze anheben oder Vertretungsregel | **keine**, eine Entscheidung |
| Tatsächliche Bearbeitung (47 Min.) | 0,1 | Textbausteine, GenAI, Teileidentifikation | teilweise GenAI |

**Der Lehrpunkt.** 6,4 von 6,5 Tagen sind Liegezeit. **Kein Sprachmodell macht davon einen einzigen Tag kürzer.** Die drei größten Blöcke werden durch eine Berechtigung, eine Priorisierungsregel und eine Datenpflege gelöst — zusammen rund 5,5 Tage, ohne Lizenzkosten.

**Und trotzdem ist V2 das beste KI-Vorhaben im Haus.** Zwei Gründe:

1. Die Datenpflege, die es erzwingt, ist die Voraussetzung für alles Weitere.
2. Der sinnvolle KI-Anteil liegt **nicht** dort, wo der Steuerkreis ihn vermutet. Nicht der Angebotstext — der ist in 20 Minuten mit Textbausteinen gelöst. Sondern die **Teileidentifikation in Sonderfällen**: Kundenangabe „Nummer 3390-08" zu einer Anlage von 2007, für die es drei Nachfolgestände gibt. Dort liegen 90 % der Bearbeitungszeit, dort ist die Aufgabe sprachlich und variabel, und dort ist GenAI die richtige Kategorie.

Das ist die Wellen-Aussage in einem Vorhaben: Wer bei V2 nur den vermuteten KI-Teil finanziert, finanziert 1,5 % der Durchlaufzeit und den falschen Anwendungsfall.

**Rollen und Konflikte:** Kowalczyk will, kann aber nicht (Bonus an Durchlaufzeit gekoppelt, kein Vault-Zugriff). Beniers muss Leserechte freigeben, hat aber ein konkurrierendes Vorhaben. Brandtner muss die Freigabegrenze anheben, was ein Kontrollverzicht ist.

### V7 · Tickets kategorisieren und Entwürfe vorbefüllen — der bessere Quick Win

**Ausgangslage.** 1.850 Tickets im Monat, 42 % Standardanfragen, Erstreaktion 9,2 Stunden. Ehrlicher hat das Vorhaben vorgeschlagen, es wurde nicht priorisiert, weil es „technisch unspektakulär" ist.

**Warum es im Kurs gebraucht wird.** Es ist der Gegenentwurf zu V4 und V5 und erfüllt [Kotters vier Quick-Win-Kriterien](../coursebook/2.2/2.2_Kotter-8-Schritte-Modell.md#3-die-acht-schritte-im-detail) als einziges Vorhaben vollständig: eindeutig messbar, sichtbar für die Betroffenen, in acht Wochen erreichbar, und die Beteiligten sind benennbar. Der Mensch bleibt dazwischen, also entsteht keine Haftungsfrage.

Es ist gleichzeitig das Vorhaben, das im Kurs am häufigsten übersehen wird — weil es in der Liste nach dem langweiligsten aussieht. Das ist die Übung.

### V10 · Wissensassistent — das Vorhaben, das nicht gehen kann

**Ausgangslage.** Semmlers einzige eigene Meldung. 19 Techniker gehen in fünf Jahren in Rente, ihr Wissen steckt in 2.400 PDF-Dateien, 11 Jahren Serviceberichten und in Köpfen. Ein Assistent soll es abrufbar machen.

**Warum es nicht geht — noch nicht:**

- Daten auf Stufe 2. `N:\` hat keine Struktur, keine Metadaten, keine Versionierung. Dieselbe Wartungsanleitung liegt in vier Fassungen, drei davon veraltet.
- **Es gibt kein Berechtigungskonzept.** Auf `N:\` liegen unter anderem `Gehaltsrunde_2025_final.xlsx`, Abmahnungen und Kundenkalkulationen. Ein Assistent mit Leserecht auf `N:\` hat Leserecht darauf.
- Serviceberichte sind Freitext, Ø 34 Wörter, mit Werkstattkürzeln. Für Retrieval bedeutet das: plausible Antworten aus unzuverlässiger Quelle, ohne dass ein Techniker vor Ort das prüfen kann.

**Der Lehrpunkt.** Das ist der stärkste fachliche Grund für ein KI-Vorhaben im ganzen Haus — und er ist nicht umsetzbar, weil eine Welle-1-Lücke im Weg steht. Die richtige Antwort ist nicht Ablehnung, sondern eine Reihenfolge: Berechtigungsinventur, dann ein abgegrenzter Dokumentenkorpus (die 180 gültigen Wartungsanleitungen, kuratiert), dann Assistent mit Quellenangabe je Antwort.

**Und:** Semmler hat es vorgeschlagen. Wer sein einziges eigenes Vorhaben ablehnt, verliert die Person, die man für Schritt 5 am dringendsten braucht. Die Umsetzungsreihenfolge ist hier auch eine Change-Entscheidung.

---

## Die sechs übrigen — kurz

| ID | Was daran zu lernen ist |
|---|---|
| **V3** Predictive Maintenance | Die Kategorie ist richtig, die Daten fehlen. Rohdaten liegen beim Gateway-Anbieter, konsistente Zeitreihen erst ab 06/2023, Ausfälle nur als Freitext dokumentiert — es gibt keine Zielgröße zum Lernen. Prüffrage: *Wie schnell würden wir merken, dass das Modell falsch liegt?* Bei Wartungsintervallen: nach Monaten. Siehe [Zillow](../coursebook/1.4/1.4_Vier-Wellen-KI-Kategorien-Hype-Cycle.md#82-zillow-offers-wenn-ein-prognosemodell-still-driftet) und [Inject I4](06_Sonderfaelle-und-Injects.md) |
| **V4** Website-Chatbot | Sieht aus wie ein Effizienzprojekt, ist ein **Compliance-Vorhaben**: verbindliche Aussagen zu Lieferterminen gegenüber Kunden. [Air Canada](../coursebook/1.4/1.4_Vier-Wellen-KI-Kategorien-Hype-Cycle.md#83-air-canada-die-haftungsfrage-bei-genai) beantwortet die Haftungsfrage. Auslöser von [Inject I2](06_Sonderfaelle-und-Injects.md) |
| **V5** Agentic Ende-zu-Ende | Der Ablauf hat 11 Schritte. Bei 95 % Zuverlässigkeit je Schritt: 0,95¹¹ ≈ **57 %** Gesamterfolg — und der Fehler geht ohne Zwischenprüfung an den Kunden. Nicht „nein", sondern „nicht dieser Pfad": Agent für Recherche und Entwurf, Freigabe beim Menschen |
| **V6** Bedarfsprognose | Der **beste ROI im Portfolio** und das einzige Vorhaben, dessen Datenlage trägt: Bewegungsdaten seit 2011, sauber und datiert. 3,4 Mio. EUR Bestand, 18 % Langsamdreher. Wurde zurückgestellt, weil es nicht nach KI klingt. Das ist der Befund, nicht der Zufall |
| **V8** Stücklistenübergabe | RPA ist technisch möglich. Die Königsfrage: *guter Prozess oder schlechter?* Die Doppelpflege existiert nur, weil Vault und SAP nie verbunden wurden. RPA würde diesen Zustand für zehn Jahre festschreiben — und bei jeder SAP-Oberflächenänderung brechen. Beniers' PDM-Ausbau ist teurer und richtig |
| **V9** Bewerbervorauswahl | *Wollen wir die Vergangenheit fortschreiben oder ändern?* Bei 512 Beschäftigten mit einem Frauenanteil von 19 % in technischen Rollen lautet die Antwort „ändern" — und dann ist ein historisch trainiertes Modell das falsche Werkzeug ([Amazon](../coursebook/1.4/1.4_Vier-Wellen-KI-Kategorien-Hype-Cycle.md#84-amazons-recruiting-modell-der-bias-fall)). Zusätzlich: Hochrisiko nach AI Act, siehe [Inject I12](06_Sonderfaelle-und-Injects.md) |

---

## Reifegrad-Engpass je Vorhaben

Die Anwendung der Engpassregel aus [`01_Reifegrad-und-Wellen.md`](01_Reifegrad-und-Wellen.md). Nicht der Mittelwert entscheidet, sondern die niedrigste relevante Dimension.

| Vorhaben | Engpassdimension | Stufe | Machbar heute? |
|---|---|---:|---|
| V1 Rechnungen | Prozesse | 2 | **Ja**, in der deterministischen Fassung |
| V2 Ersatzteilangebot | Daten | 2 | **Teilweise** — Datenpflege ist Teil des Vorhabens, nicht Vorbedingung |
| V3 Predictive Maintenance | Daten | 2 | **Nein** |
| V4 Chatbot | Prozesse + Governance | 2 | **Nein**, nicht ohne Rückfallpfad und Freigabe |
| V5 Agentic | Technologie + Kultur | 2–3 | **Nein** |
| V6 Bedarfsprognose | Daten *(hier ausreichend)* | 3+ | **Ja** |
| V7 Tickets | Daten *(nur Tickettexte nötig)* | 3 | **Ja** |
| V8 Stücklisten | Prozesse | 2 | **Ja**, aber falsche Lösung |
| V9 Bewerber | Strategie + Recht | 2 | **Nein** |
| V10 Wissensassistent | Daten | 2 | **Nein**, in kuratierter Teilfassung ja |

**Drei der zehn Vorhaben sind heute machbar und richtig: V1 (umkategorisiert), V6 und V7.** Keines davon war priorisiert. Zwei davon enthalten nicht das Wort KI in der ursprünglichen Beschreibung.

Das ist die Pointe des Portfolios, und sie hält im Kurs jedes Mal.
