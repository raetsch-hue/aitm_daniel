---
artefakt: Plattformkriterien GeAT — Kennzahlen, Stakeholder-Anforderungen und Belege
woche: 03
datum: 2026-09-10
status: Arbeitsgrundlage für das Kursboard (Spalte GeAT mbH). Konsolidiert die vier vorhandenen Kennzahlen-Tabellen und weist deren Widersprüche aus. Nicht beschlossen
zweck: Elevator Pitch für die Präsentation, je Boardzeile ein Satz zum Kopieren, darunter die ausführliche Fassung — und sichtbar machen, was die sechs Kriterien bei GeAT nicht erfassen
bezug: w03A-1-ki-analyse-fassung-1.md (Gewichtung K1–K8), zahlen.md, menschen.md, vorhaben.md, transformationsvorschlag.md, storyline-stufe-3-datenfundament.md, w03B-1-agent-konzept-bestandswaechter.md
grundlage: Kriterienkatalog aus coursebook/3.1, Methodik aus bibliothek/vendor-evaluation.md
herkunft: konsolidierend. Jede Zahl trägt ihre Herkunft aus dem Profil (`öffentlich`, `angenommen`, `generiert`, `gerechnet`, `Fakt im Fall`). Vier Benchmarks sind unbelegt und als Lücke ausgewiesen, nicht ersetzt. Keine Zahl ist für ein Deliverable außerhalb dieses Kurses verwendbar
kette: W03 C · Plattformkriterien und Reifegrad — Glied 1 von 3
baut_auf: w03A-3-ki-analyse-fassung-2-gueltig.md (Gewichtung K1-K8, geltende Fassung)
basis_fuer: w03C-2-dsgvo-ai-act-auszug.md · w03C-3-reifegradstufe-building-pilots.md
---

# Plattformkriterien GeAT mbH: Kennzahlen, Stakeholder, Belege

> **Was dieses Dokument ist.** Die Spalte **GeAT mbH** des Kursboards, ausgeschrieben. Das Board
> fragt je Kriterium nach drei Dingen: *Relevante Kennzahlen*, *Anforderungen von Key
> Stakeholder\*innen*, *Belege*. Die sechs Kriterien stehen in
> [`coursebook/3.1`](#3.1/3.1_KI-Plattformen-im-Vergleich.md), die eigene Gewichtung in
> [`w03A-1-ki-analyse-fassung-1.md`](w03A-1-ki-analyse-fassung-1.md) Abschnitt 4.2.

> **Aufbau.** Zuerst der Elevator Pitch für die Präsentation. Dann je Boardzeile **der eine Satz
> zum Kopieren**, darunter die ausführliche Fassung. Ab Abschnitt 3 stehen die sechs Kriterien
> einzeln, mit allen Zahlen und Herkunftskennzeichen.

---

## 1 · Elevator Pitch — 60 Sekunden

**Zum Sprechen:**

> GeAT ist ein Personaldienstleister mit 709 Beschäftigten, von denen 69 einen Bildschirmarbeitsplatz haben. Wir entscheiden über eine KI-Plattform **sechs Monate, bevor unser Kernsystem ersetzt wird** — und das dreht die Standardmatrix um.
>
> Deployment-Flexibilität wiegt bei uns **2 statt 25 Prozent**: bei 69 Seats liefert jeder Anbieter dasselbe Multi-Tenant-SaaS, das Kriterium trennt niemanden. RAG wiegt **4 statt 20 Prozent**, MCP **0 statt 10**: unsere 41.000 Lebensläufe haben keinen Textindex und keine offene Schnittstelle, die Voraussetzung ist 12 bis 18 Monate entfernt.
>
> Was stattdessen wiegt, ist **Compliance mit 25 Prozent** — denn neun Leute arbeiten heute mit privaten KI-Konten und Bewerberlebensläufen darin, ohne Auftragsverarbeitungsvertrag. **Wir beschaffen keine Idee. Wir ersetzen eine laufende Verarbeitung ohne Rechtsgrundlage.**
>
> Die Empfehlung: integrierte EU-Plattform, enger Zuschnitt auf 20 Seats, 9.000 Euro — unter der Freigabegrenze, also ohne verlorenes Quartal.
>
> Und das Gegenargument, das ich selbst mitbringe: dieses Haus hat 2023 ein Werkzeug für 95.000 Euro gekauft, das 34 Prozent nutzen und das drei Jahre lang niemand gemessen hat. Deshalb gehört zu dieser Empfehlung eine Nutzungsmessung ab Tag 1 und ein Abbruchkriterium, das **vorher** festgelegt wird.

**Die kürzeste Fassung, wenn nur ein Satz bleibt:**

```
Wir entscheiden sechs Monate vor dem Kernsystemwechsel — deshalb wiegt bei GeAT
Compliance 25 % und RAG nur 3 %, und deshalb beschaffen wir keine Funktion,
sondern eine Rechtsgrundlage für neun Leute, die längst KI nutzen.
```

---

## 2 · Die vier Haftzettel

### Zeile 1 · Kriterium

**Zum Kopieren:**

```
DSGVO / AI Act, 25 % — das schwerste Kriterium, weil bei GeAT keine Idee
reguliert wird, sondern eine laufende Verarbeitung ohne AVV ersetzt werden muss:
9 private KI-Konten mit Bewerberlebensläufen. Deployment fällt auf 2 %, RAG auf
4 %, MCP auf 0 %, weil keines davon bei 69 Seats und 1,5 IT-Stellen trennt.
```

**Ausführlich.** Die eigene Gewichtung hat acht Kriterien, nicht sechs — und die Reihenfolge weicht
an zwei Stellen stark von der Kursmatrix ab. Beide Abweichungen hängen an einer einzigen
Kontextzeile: **das Kernsystem wird in Q1/2027 ersetzt.** Damit wird Integrationstiefe zum Risiko
und Wechselfähigkeit zum Wert — die genaue Umkehrung der Lehrbuchgewichtung. Die vollständige
Zuordnung samt der 30 Prozent, für die das Board keine Zeile hat, steht in Abschnitt 3.

### Zeile 2 · Relevante Kennzahlen

**Zum Kopieren:**

```
Copilot für alle 69 Stammkräfte kostet 24.840 € im Jahr — 160 € unter der
Freigabegrenze der Geschäftsführung und praktisch der gesamte Projektposten des
IT-Budgets 2026 (25.000 €). Über drei Jahre: 74.520 €, das Dreifache der Grenze.
```

**Ausführlich.** Die tragfähigsten Zahlen des Falls sind die Budgetzahlen, nicht die
Prozesskennzahlen: 25.000 € Projektposten, 620.000 € Migrationsreserve, 95.000 € für das ATS-Modul
2023 bei 34 Prozent Nutzung — alle `Fakt im Fall`. Die Prozesskennzahlen (Besetzungsquote 40 %,
Vollkosten je Besetzung 815 €, Besetzungsdauer 11 Tage) sind `angenommen` oder aus `angenommen`
gerechnet. Je Kriterium ausgeschrieben ab Abschnitt 4, die Widersprüche zwischen den vier
Kennzahlen-Tabellen in Abschnitt 10.

### Zeile 3 · Anforderungen von Key Stakeholder\*innen

**Zum Kopieren:**

```
Drei Anforderungen entscheiden, keine davon technisch: AVV vorgelegt statt
zugesichert (Rolle 8, externer Datenschutzbeauftragter) · Betriebsvereinbarung,
die Leistungskontrolle ausschließt (Rolle 9, Betriebsrat) · Amortisation unter
24 Monaten (Rolle 13, Gesellschaftervertreterin, Macht 5).
```

**Ausführlich.** Die gefährlichste Rolle ist keine dieser drei, sondern **Rolle 5 (Rehberg,
Niederlassungsleiter Gotha) mit Macht 4 und Interesse 2** — der Quadrant, in dem niemand überzeugt
werden muss, aber jeder blockieren kann. Und die einzige Anforderung, die eine Zahl ist, kommt von
Rolle 13. Alle Anforderungen sind aus Haltungen in [`menschen.md`](menschen.md) **abgeleitet, nicht
erhoben** — kein Interview liegt vor. Vollständig je Kriterium ab Abschnitt 4.

### Zeile 4 · Belege

**Zum Kopieren:**

```
Der härteste Beleg im Haus belegt einen Fehlschlag: ATS-Modul 2023, 95.000 €,
34 % Nutzung, drei Jahre nicht gemessen. Öffentlich belegt sind nur AÜG-Erlaubnis
und ISO 9001; zur Ertragslage existiert kein einziger öffentlicher Wert, und vier
Benchmarks haben keine Quelle.
```

**Ausführlich.** Die Belegkette ist ungleich stark. `öffentlich` mit Quelle und Abrufdatum sind 24
Angaben, überwiegend Identität und Zertifikate. Alles Wirtschaftliche ist `angenommen`. Vier
Benchmarks — Besetzungsquote, Rohertragsmarge, EBIT-Marge, IT-Quote — tragen **keine Quelle** und
stützen trotzdem jede Rechnung; sie sind in Abschnitt 11 als Lücke ausgewiesen und nicht ersetzt.
Drei weitere Lücken sind selbst das Ergebnis: Exit-Kosten, Cloud-ML-Aufbaukosten und die Kosten der
Nullvariante.

---

## 3 · Die Gewichtung: die sechs Kriterien deckeln 70 Prozent

`abgeleitet` aus [`w03A-1-ki-analyse-fassung-1.md`](w03A-1-ki-analyse-fassung-1.md) Abschnitt 4.2.

Die eigene Gewichtung hat **acht** Kriterien, nicht sechs. Die Zuordnung:

| Boardkriterium | eigenes Kriterium | Gewicht (F2) | (F1) | Kursmatrix |
|---|---|---:|---:|---:|
| DSGVO / AI Act | K1 Compliance und AVV | **25 %** | 25 % | 25 % |
| Deployment Flexibility | K8 Deployment-Flexibilität | **2 %** | 2 % | 25 % |
| RAG-Fähigkeit | K7 RAG und Integrationstiefe | **4 %** | 3 % | 20 % |
| MCP-Kompatibilität | — **kein eigenes Kriterium mehr** | **0 %** | 10 % | 10 % |
| Preismodell / Lock-in | K4 TCO 15 % + K6 Exit und Portabilität 6 % | **21 %** | 25 % | 5 % |
| Adaptionspfad Support | K3 Adoptionspfad, **Einführungsaufwand** und Support | **17 %** | 15 % | 15 % |
| — **kein Boardkriterium** | K2 Verfügbarkeit gegen die Taktgrenze | **20 %** | 20 % | — |
| — **kein Boardkriterium** | K5 Betriebsaufwand bei 1,5 IT-Stellen | **11 %** | 10 % | — |
| | | **100 %** | | |

> **Warum hier zwei Gewichtsspalten stehen.** Die geltende Fassung ist
> [`w03A-3-ki-analyse-fassung-2-gueltig.md`](w03A-3-ki-analyse-fassung-2-gueltig.md); sie ersetzt
> die Erstfassung nach einem eigenen Review. **Vier Gewichte haben sich geändert**, und eines davon
> kippt eine Boardzeile: **MCP ist aus K6 herausgenommen und wiegt jetzt null.** Begründung im
> Wortlaut: *„Wer soll bei zwei IT-Personen ohne Entwicklungsauftrag einen MCP-Server bauen und
> betreiben? Portabilität bleibt, MCP fällt."*

> **Der Satz für das Board: 31 Prozent des Gewichts haben auf diesem Board keine Zeile — und eine
> Boardzeile hat kein Gewicht.** Die beiden
> fehlenden Kriterien sind bei GeAT nicht exotisch, sondern die zwei, die den Sieger drehen — die
> Terminfrage (das Kernsystem wird Q1/2027 ersetzt) und die Betriebsfrage (1,5 IT-Stellen, beide
> gebunden). Wer nur die sechs füllt, hat eine Matrix, die 70 Prozent der eigenen Entscheidung
> abbildet.

Drei Abweichungen, die ich vertreten muss: **Deployment 2 statt 25 Prozent**, **RAG 4 statt 20
Prozent** und **MCP 0 statt 10 Prozent**. Beide sind in `w03A-1-ki-analyse-fassung-1.md` begründet — kurz: bei 69 Seats gibt es keine
Deployment-Wahl (jeder Anbieter liefert Multi-Tenant SaaS), und RAG hat bei GeAT keine
Voraussetzung. Ein Kriterium, das die Kandidaten nicht trennt, bekommt kein großes Gewicht.

---

## 4 · DSGVO und AI Act — Gewicht 25 %

### Relevante Kennzahlen

| Kennzahl | Wert | Ziel | Herkunft |
|---|---:|---:|---|
| Personen mit privatem KI-Zugang, Lebensläufe darin, ohne AVV | **9** | 0 | `Fakt im Fall` |
| Zeitarbeitnehmer in Messenger-Gruppen ohne AVV, mit Gesundheitsangaben | ca. **300** | Kanal geregelt | **`generiert`** — rechtlich der schärfste erfundene Punkt des Profils |
| Bewerberprofile über der zugesagten Speicherdauer | **18.000 von 41.000 = 43,9 %** | 0 bis Monat 7 | `angenommen` |
| Auftragsverarbeiter mit geprüftem AVV | **Lücke** — Website-Agentur „unklar, nie geprüft" | vollständig | **`generiert`** |
| Anteil der Anfragen, für die eine Annex-III-Einordnung schriftlich vorliegt | **0 %** | 100 % vor Stufe 4 | `abgeleitet` |

### Anforderungen von Key Stakeholder\*innen

| Rolle | Macht / Interesse | Anforderung an die Plattform |
|---|---:|---|
| **Rolle 8 · Dr. Holger Marnitz**, externer DSB | 2 / 3 | **AVV vorgelegt, nicht zugesichert.** Annex-III-Einordnung schriftlich; Prüfung der DSFA-Pflicht **vor** dem ersten Lauf. Der einzige Beteiligte, der bisher nichts unterschrieben hat |
| **Rolle 9 · Silke Nowak**, Betriebsratsvorsitzende | 3 / 4 | Betriebsvereinbarung, die Leistungs- und Verhaltenskontrolle **ausschließt**. Ihre Zustimmung ist daran gebunden, nicht an die Technik. Hat 2023 beim ATS-Modul darauf bestanden |
| **Rolle 2 · Bernd Achtelik**, GF Finanzen, Recht, IT | 4 / 3 | Keine zweite Baustelle vor der Migration. Compliance ja — aber nicht als eigenes Projekt |
| **Rolle 1 · Katrin Vollmer**, Geschäftsführerin | 5 / 4 | Der ungeregelte Zustand muss aufhören, ohne dass das Haus einen zweiten Fehlschlag wie 2023 vorzuweisen hat |

### Belege

| Aussage | Beleg | Güte |
|---|---|---|
| AÜG-Erlaubnis wird von der Bundesagentur für Arbeit erteilt und überwacht | Impressum, [`recherche.md`](recherche.md) mit Abrufdatum | **`öffentlich`** |
| ISO 9001 seit 2004 | [`recherche.md`](recherche.md) | **`öffentlich`** |
| Neun Schatten-Nutzer mit Lebensläufen in privaten Konten | [`systeme-daten.md`](systeme-daten.md) | `Fakt im Fall` |
| 300 Messenger-Teilnehmer mit Gesundheitsangaben | [`generierte-werte.md`](generierte-werte.md) Nr. 9 | **`generiert` — vor Verwendung bestätigen** |
| 18.000 überfällige Profile | [`profil.md`](profil.md) | `angenommen` |

> **Die Doppelrolle der Aufsicht — und die Grenze der Aussage.** Die AÜG-Erlaubnis wird von der
> Bundesagentur für Arbeit erteilt und überwacht (`öffentlich`, Impressum), die zugleich Akteurin im
> Vermittlungsmarkt ist. **Daraus folgt aber nicht, dass ein AI-Act-Verstoß die Erlaubnis
> gefährdet, und die BA ist nicht die zuständige KI-Aufsichtsbehörde.**
> [`vorhaben.md`](vorhaben.md) nimmt diese Verknüpfung ausdrücklich zurück;
> [`transformationsvorschlag.md`](transformationsvorschlag.md) behauptet sie noch als „stärkstes
> Argument im Business Case". **Die schwächere Fassung gilt:** Compliance ist ein relevantes
> Risiko, die direkte Verbindung zur Erlaubnis wäre ohne Rechtsgrundlage zu stark. Details im
> Auszug [`w03C-2-dsgvo-ai-act-auszug.md`](w03C-2-dsgvo-ai-act-auszug.md), Abschnitt 8.

---

## 5 · Deployment Flexibility — Gewicht 2 % (Kursmatrix 25 %)

### Relevante Kennzahlen

| Kennzahl | Wert | Herkunft |
|---|---:|---|
| Seats im engen Zuschnitt | **20** | `Annahme` der Analyse |
| Stammpersonal insgesamt | **69** | `angenommen` (Fortschreibung belegter Zahlen 2018 → 2021) |
| Beschäftigte insgesamt | **709**, davon 640 ohne Bildschirmarbeitsplatz bei GeAT | `Fakt im Fall` / `angenommen` |
| IT-Kapazität | **1,5 Stellen**, beide bis Q1/2027 durch die Migration gebunden | `Fakt im Fall` |
| Marktschwelle Single-Tenant / On-Premise | typisch ab **1.000** bzw. **5.000** Seats | **`Einschätzung`, unbelegt — Lücke** |

### Anforderungen von Key Stakeholder\*innen

| Rolle | Macht / Interesse | Anforderung |
|---|---:|---|
| **Rolle 12 · Sven Balzer**, IT-Leitung | 2 / 2 | *„Zeigt mir, wer das betreibt, wenn es läuft, und wer haftet."* Kein selbst betriebener Cluster, keine Komponente, die 1,5 Stellen pflegen müssten |
| **Rolle 8 · Dr. Holger Marnitz** | 2 / 3 | Verarbeitung in der EU als **Pflicht**, nicht als Präferenz — eine Präferenz kann man aufgeben |

### Belege
1,5 IT-Stellen und die Bindung durch die Migration: `Fakt im Fall`
([`systeme-daten.md`](systeme-daten.md), [`vorhaben.md`](vorhaben.md)).
Die Seat-Schwellen sind **meine Marktkenntnis ohne Quelle** und damit die schwächste Aussage in
diesem Abschnitt. Sie tragen die 2-Prozent-Gewichtung — wer sie widerlegt, widerlegt die
Gewichtung.

> **Warum trotzdem nur 2 Prozent:** Bei 69 Seats liegt GeAT unter jeder Schwelle für Single-Tenant
> und On-Premise. Multi-Tenant SaaS in der EU ist die einzige verfügbare Option, bei jedem
> Anbieter. Das Kriterium kann die Kandidaten nicht trennen. Das Gewicht wandert nach K6 —
> was der Versicherer **architektonisch** löst, muss GeAT **vertraglich** lösen.

---

## 6 · RAG-Fähigkeit und Integrationstiefe — Gewicht 4 % (Kursmatrix 20 %)

### Relevante Kennzahlen

| Kennzahl | Wert | Ziel | Herkunft |
|---|---:|---:|---|
| Bewerberprofile im Bestand | **41.000** | — | `angenommen` |
| Lebenslauf-PDFs, ohne Textindex | **41.000** | indexiert = Stufe 4 | `angenommen` |
| Anteil strukturiert erfasster Profile | **37 %** | 80 % bei Neuanlage, Monat 10 | `angenommen` |
| Bestandsprofile mit ≥ 3 strukturierten Qualifikationen | **37 %** | 70 %, Monat 10 | `angenommen` |
| Offene API im Bestandsvertrag der Branchensoftware | **nein** | Anforderung ins Lastenheft Q1/2027 | `Fakt im Fall` |
| Datenqualität des bereinigten Auszugs | **23 von 24 Prüfungen ohne Treffer** | halten | **gemessen 2026-09-10**, siehe unten |

> **Zur letzten Zeile, weil sie leicht falsch gelesen wird.** Gemessen wurde der bereinigte
> Übungsauszug: 1.473 Bewerber- und 1.078 Kundendatensätze. Das sind **3,6 Prozent** der 41.000
> Profile. Der Auszug ist sauber, der Bestand ist es nicht — die 18.000 überfälligen Profile aus
> Kriterium 1 stehen dazu nicht im Widerspruch, sie beziehen sich auf eine andere
> Grundgesamtheit. Details in
> [`w03B-2-agent-neubewertung-nach-bereinigung.md`](w03B-2-agent-neubewertung-nach-bereinigung.md).

### Anforderungen von Key Stakeholder\*innen

| Rolle | Macht / Interesse | Anforderung |
|---|---:|---|
| **Rolle 4 · Yvonne Kloß**, Leiterin Recruiting Center | 3 / 5 | Der **eigene Bestand** muss erste Suchquelle werden — nur das senkt die Besetzungsdauer und rechtfertigt die 480.000 € Anzeigenbudget. Treiberin, und sie trägt seit 2023 ein Werkzeug, das niemand nutzt |
| **Rolle 6 · Regina Pfaff**, Senior-Disponentin | 2 / 2 | *„Frag mich, nicht das System."* Kein Werkzeug, das ihr Wissen ersetzt statt es zu ergänzen |
| **Rolle 14 · Anja Weiskopf**, Leiterin Academy | 1 / 4 | *„Wenn die Maschine vorschlägt, muss der Disponent begründen können, warum er ablehnt."* Erklärbarkeit als Qualifizierungsfrage |

### Belege
37 % / 63 %, 41.000 Profile: `angenommen`, abgeleitet aus dem Mengengerüst in
[`zahlen.md`](zahlen.md). Fehlende API und fehlender Textindex: `Fakt im Fall`
([`systeme-daten.md`](systeme-daten.md)). Die Datenqualitätsmessung ist reproduzierbar
(`daten/pruefe_datenqualitaet.py`, Stichtag 2026-09-10) — aber auf **generierten** Übungsdaten.

> **Warum nur 4 Prozent:** In Stufe 1 fügt ein Mensch den Lebenslauf selbst ein. RAG über den
> Bewerberbestand setzt API, Textindex und strukturierte Felder voraus — 12 bis 18 Monate entfernt.
> Wer RAG jetzt bezahlt, bezahlt eine Funktion, deren Voraussetzung noch nicht existiert.

---

## 7 · MCP-Kompatibilität — Gewicht 0 % (in Fassung 2 gestrichen)

### Relevante Kennzahlen

| Kennzahl | Wert | Herkunft |
|---|---:|---|
| Monate zwischen Plattformentscheidung und Kernsystemwechsel | **ca. 6** (Wechsel Q1/2027) | `Fakt im Fall` |
| Für die Migration reserviertes Budget | **620.000 €** | `Fakt im Fall` |
| Proprietäre Schnittstellen, die bei einem Wechsel neu zu bauen wären | **Lücke** | — |
| Exit-Kosten in Euro und Personentagen | **Lücke — und die Lücke ist selbst das Ergebnis** | [`bibliothek/vendor-evaluation.md`](#bibliothek/vendor-evaluation.md) |
| Personen, die einen MCP-Server bauen und betreiben könnten | **0** von 1,5 IT-Stellen | `Fakt im Fall` |

> **Warum dieses Kriterium in Fassung 2 auf null gesetzt ist.** MCP beantwortet die Frage, ob eine
> Plattform in Jahren noch anschlussfähig ist — und die bleibt richtig. Sie ist bei GeAT nur nicht
> **entscheidungsrelevant**: es gibt niemanden, der einen MCP-Server bauen und betreiben würde. Was
> bleibt, ist Portabilität, und die steht als K6 mit 6 Prozent bei Kriterium 5.
> **Auf dem Board bleibt die Zeile stehen — mit dem Wert null und dieser Begründung.** Ein
> Kriterium mit null zu gewichten und zu sagen warum, ist prüfbar; es weglassen ist es nicht.

### Anforderungen von Key Stakeholder\*innen

| Rolle | Macht / Interesse | Anforderung |
|---|---:|---|
| **Rolle 2 · Bernd Achtelik** | 4 / 3 | Die Plattform muss den Systemwechsel **überleben**. Die Migration ist sein Projekt; eine Plattform, die 2027 neu beschafft werden muss, ist für ihn ein Eigengoal |
| **Rolle 12 · Sven Balzer** | 2 / 2 | Keine proprietäre Integrationsschicht. Was 1,5 Stellen nicht pflegen können, wird nicht gekauft |
| **Rolle 13 · Dr. Simone Barth**, Gesellschaftervertreterin | 5 / 3 | *„Wartet, bis die Software steht"* — sie ist der Grund, warum Anschlussfähigkeit belegt werden muss und nicht behauptet |

### Belege
Q1/2027 und die 620.000 €: `Fakt im Fall` ([`vorhaben.md`](vorhaben.md)). Die Exit-Kosten sind
nicht beziffert, und das ist bewusst so ausgewiesen: ein Score „Lock-in: 3" sagt nichts darüber,
was ein Wechsel kostet. **Die Prüffrage für das Anbietergespräch:** *„Können wir in 18 Monaten
wechseln, wenn sich die Anforderungen verschärfen — und was kostet das in Euro und Personentagen?"*

---

## 8 · Preismodell und Lock-in — Gewicht 15 % (Kursmatrix 5 %)

Das Kriterium mit der größten Aufwertung gegenüber der Kursmatrix, und das einzige, das
**gerechnet statt gescort** wird.

### Relevante Kennzahlen

| Kennzahl | Wert | Herkunft |
|---|---:|---|
| Lizenz EU-Plattform, 20 Seats / Jahr | **4.800 – 7.200 €** | Listenwerte, **kein Angebot liegt vor** |
| Lizenz M365 Copilot, 20 Seats / Jahr | **7.200 €** | Listenpreis ca. 30 €/Nutzer/Monat, **Stand prüfen** |
| Lizenz M365 Copilot, 69 Seats / Jahr | **24.840 €** | gerechnet |
| Projektposten im IT-Budget 2026 | **25.000 €** | `Fakt im Fall` |
| **Differenz der beiden Zeilen darüber** | **160 €** | **gerechnet — und der Befund des Abschnitts** |
| Freigabegrenze der Geschäftsführung | **25.000 €**, darüber quartalsweise Gesellschafterversammlung | `Fakt im Fall` |
| Copilot 69 Seats über drei Jahre | **74.520 €** = **3× Freigabegrenze** | gerechnet |
| Ansatz Stufe 1 | **9.000 €** | `angenommen` |
| ATS-Modul 2023, Kosten / Nutzung | **95.000 € über 3 Jahre / 34 %** | `Fakt im Fall` |
| Vollkosten je Besetzung | **815 €** (2025), 606 € (2023) | `gerechnet` aus `angenommen`-Werten |
| EBIT-Marge | **2,6 %**, EBIT 0,805 Mio | `angenommen` |
| Investitionsspielraum | **900.000 €**, bei strenger Fortschreibung ca. 805.000 € | `angenommen` |

> **Die Warnung, die vor die Empfehlung gehört.** 24.840 € liegen **160 € unter** der
> Freigabegrenze. Über drei Jahre sind es das Dreifache. Wer die Maßnahme in Jahresraten vorlegt,
> hält die Grenze formal ein und umgeht die Gesellschafterversammlung. Das ist kein Vorschlag: es
> wird jemand vorschlagen, und die Antwort muss vorher aufgeschrieben sein. **Die Freigabegrenze
> gilt für die Maßnahme, nicht für die Jahresrate.**

### Anforderungen von Key Stakeholder\*innen

| Rolle | Macht / Interesse | Anforderung |
|---|---:|---|
| **Rolle 13 · Dr. Simone Barth** | **5 / 3** | **Amortisation unter 24 Monaten** — oder warten. Höchste Macht im Feld, und die einzige Anforderung, die eine Zahl ist |
| **Rolle 10 · Petra Ziegenhorn**, Leiterin Controlling | 2 / 4 | Will die Rechnung sehen, **bevor** sie das Vorhaben mag. Hat 2023 das Modulbudget freigegeben und die Nichtnutzung nie in einem Bericht gehabt |
| **Rolle 2 · Bernd Achtelik** | 4 / 3 | TCO über drei Jahre, nicht Jahreslizenz. Und die Vorleistungen, die nicht in der Lizenz stehen |
| **Rolle 1 · Katrin Vollmer** | 5 / 4 | *„Ich habe 2023 schon einmal bezahlt"* — kein zweites Werkzeug ohne Nutzungsnachweis |

### Belege

| Aussage | Güte |
|---|---|
| 25.000 € Projektposten, 620.000 € Migration, 95.000 € / 34 % ATS-Modul, Freigabegrenze | `Fakt im Fall` — die tragfähigsten Zahlen des Abschnitts |
| Alle Lizenzpreise | **Listenwerte nach Kenntnisstand, prüfpflichtig, kein Angebot liegt vor** |
| Vollkosten je Besetzung, EBIT-Marge, Investitionsspielraum | `angenommen` bzw. `gerechnet` aus `angenommen` |
| Exit-Kosten, Cloud-ML-Aufbaukosten, Kosten der Nullvariante | **Lücke, und in allen drei Fällen ist die Lücke selbst das Ergebnis** |

---

## 9 · Adoptionspfad, Einführungsaufwand und Support — Gewicht 17 %

Das Kriterium, für das GeAT den härtesten Beleg hat — einen dokumentierten Fehlschlag in genau
dieser Werkzeugklasse.

### Relevante Kennzahlen

| Kennzahl | Wert | Ziel | Herkunft |
|---|---:|---:|---|
| Nutzung des ATS-Moduls von 2023 | **34 %** | — | `Fakt im Fall` |
| Jahre bis zur ersten Nutzungsmessung | **3** — erstmals 2026, und nur wegen eines ISO-Audits | ab Tag 1 messen | `Fakt im Fall` |
| Ausgegebene Schatten-Konten / davon aktiv | **9 / 3** | — | `Fakt im Fall` |
| Niederlassungsleiterrunden ohne Aufruf der Besetzungsquote | **5 in Folge** | jede Runde | `Fakt im Fall` |
| Standorte, die ihre Wochenliste bearbeiten | — | **≥ 5 von 7** | `abgeleitet` |
| **Abbruchkriterium** | **< 4 von 7 nach 3 Monaten → abschalten** | — | vorher festgelegt |

### Anforderungen von Key Stakeholder\*innen

| Rolle | Macht / Interesse | Anforderung |
|---|---:|---|
| **Rolle 5 · Uwe Rehberg**, NL Gotha, seit 2004 im Haus | **4 / 2** | *„Meine Besetzungen kommen über Leute, nicht über Listen."* **Der gefährlichste Quadrant des ganzen Felds:** hohe Macht, niedriges Interesse. Er muss nicht überzeugt werden, er muss nicht blockieren |
| **Rolle 3 · Marcel Steinbrück**, Vertriebsleiter | 3 / 5 | Sponsor. Will *„Profil in 24 Stunden"* verkaufen können — verantwortet die Besetzungsquote |
| **Rolle 7 · Lena Hübner**, Recruiterin | 1 / 5 | Nutzt seit einem Jahr einen privaten Zugang. **Der freigegebene Ersatz darf nicht schlechter sein** — sonst wandert die Nutzung zurück und wird unsichtbarer |
| **Rolle 6 · Regina Pfaff** | 2 / 2 | Kein Werkzeug, das 40 Jahre Kundenkenntnis für ungültig erklärt |
| **Rolle 11 · Doreen Ritschel**, Sachbearbeitung Zeiterfassung | 1 / 1 | *„Ihr wollt schneller besetzen. Ich kläre jeden Monat vier Tage Stundenzettel."* Kommt im Vorhaben nicht vor und weiß das |

### Belege
34 % Nutzung, 9 Konten mit 3 aktiven Nutzern, fünf Runden ohne Kennzahlaufruf: alle `Fakt im Fall`
([`profil.md`](profil.md), [`menschen.md`](menschen.md) Kulturmerkmal 2). Das ist die **beste
Belegbasis aller sechs Kriterien** — und sie belegt einen Fehlschlag, nicht einen Erfolg.

> Kulturmerkmal 2 des Hauses lautet: **„Was nicht gemessen wird, ist nicht gescheitert."** Daraus
> folgt die einzige nicht verhandelbare Anforderung dieses Kriteriums: Nutzungsmessung ab Tag 1 und
> ein vorher festgelegtes Abbruchkriterium. Ohne beides ist jede Plattformwahl die vierte Ansage in
> vier Jahren.

---

## 10 · Konsolidierung: die Widersprüche zwischen den vier Kennzahlen-Tabellen

Die Kennzahlen stehen an vier Stellen im Fall. Sie stimmen **nicht** überein. Auflösung hier, damit
im Pitch nicht zwei Zahlen für dieselbe Größe genannt werden.

| Größe | Fundstellen | Widerspruch | Auflösung |
|---|---|---|---|
| **Gesendete Profile je Besetzung** | `vorhaben.md`: 4,8 → **3,2 in einem Jahr** · `transformationsvorschlag.md`: 4,8 → **3,2 nach 6 Pilotmonaten** | Derselbe Zielwert für zwei verschiedene Horizonte. Einer von beiden ist falsch | **3,2 ist das Pilotziel nach 6 Monaten** — dafür existiert das Abbruchkriterium (< 4,0 nach 3 Monaten). Das Jahresziel muss **unter** 3,2 liegen oder der Jahreshorizont wird gestrichen. **Offen, zu entscheiden** |
| **Besetzungsdauer** | `vorhaben.md`: 11 → **7 Tage** in einem Jahr · `transformationsvorschlag.md`: 11 → **8,5 Tage** nach 6 Monaten | Kein echter Widerspruch (zwei Horizonte), aber `vorhaben.md` erklärt die Besetzungsdauer gleichzeitig zur **Nicht**-Zielgröße | Als **Kontextgröße** führen, nicht als Ziel. 96 % der 11 Tage sind Warteschleifen, die der Assistent nicht anfasst |
| **Anfragen mit Nichtbesetzungsgrund** | `storyline-stufe-3`: 0 % → **> 90 %** in Monat 10 · `agent-konzept`: 0 % → **> 80 %** nach 6 Monaten | Zwei Zielwerte für eine Größe | Als **Stufenziel** schreiben: > 80 % nach 6 Monaten, > 90 % in Monat 10. Nicht als zwei Ziele |
| **Profile über der Speicherdauer** | `profil.md` / `storyline`: **18.000** von 41.000 · Messung 2026-09-10: **0 abgelaufen, 41 in Frist** | Scheinbarer Widerspruch | **Zwei Grundgesamtheiten.** 18.000 gilt für den Gesamtbestand (41.000), die Messung für den bereinigten Auszug (1.473 = 3,6 %). Nicht mischen, und im Pitch immer die Grundgesamtheit mitsagen |
| **Besetzungsquote** | `zahlen.md`: 40,0 % (2025) / 48,0 % (2023), `gerechnet` aus 1.240 / 3.100 | konsistent | Bleibt. Aber der **Benchmark** dazu ist unbelegt, siehe Abschnitt 8 |

---

## 11 · Die vier Benchmarks ohne Quelle

`recherche.md` führt vier Benchmarks **ohne Quellenangabe**. Sie werden hier **als Lücke
ausgewiesen und nicht ersetzt** — keine Ersatzrecherche, keine Schätzung, die dann wie belegt
aussieht.

| Benchmark | Wert im Fall | Was daran hängt |
|---|---|---|
| **Besetzungsquote** | 35 – 50 % | Die zentrale Kennzahl des Falls. Ob 40 % schlecht sind, ist ohne Quelle **nicht entscheidbar** |
| **Rohertragsmarge** | — | Trägt die gesamte GuV in `zahlen.md` |
| **EBIT-Marge** | 2,6 % | Trägt die Freigabelogik in Kriterium 5 und die Amortisationsforderung von Rolle 13 |
| **IT-Quote** | — | Trägt die Einordnung des IT-Budgets 2026 |

**Die Folge, die ich im Pitch selbst nenne, bevor sie jemand findet:** Die 2,6 % EBIT-Marge sind
`angenommen` und stützen sich auf einen Benchmark ohne Quelle. Jede Aussage der Form „bei dieser
Marge ist X nicht darstellbar" trägt diesen Vorbehalt mit. Wer die Lünendonk-Studie im Volltext
hat, kann drei der vier auf `öffentlich` heben — das ist ein Datenproblem, kein
Argumentationsproblem, und damit durch Recherche lösbar.

---

## 12 · Gegenargumente

1. **Die Gewichtung ist eine Setzung, keine Rechnung.** K7 von 20 auf 3 Prozent und K8 von 25 auf 2
   Prozent zu ziehen, ändert das Ergebnis stärker als jeder Score. Beide Abweichungen sind auf eine
   Kontextzeile zurückführbar — aber wer die Kontextzeile anders bewertet, bekommt eine andere
   Empfehlung, und das ist legitim. Die Gewichte sind am 2026-09-07 **vor** dem Scoring fixiert
   worden; das ist der einzige Schutz gegen die nachträgliche Begründung, und er ist prüfbar.
2. **Die belegbarste Kennzahl des ganzen Dokuments belegt einen Fehlschlag.** 34 Prozent
   Modulnutzung ist der härteste Wert im Fall. Er stützt das Adoptionskriterium — und er ist
   gleichzeitig das stärkste Argument **gegen** jede Plattformbeschaffung. Wer ihn zitiert, zitiert
   gegen sich selbst mit.
3. **Fast alle Geldbeträge sind `angenommen` oder Listenwerte.** Zur Ertragslage der GeAT gibt es
   **keinen einzigen** öffentlichen Wert. Die Struktur der Rechnung ist übertragbar, die absoluten
   Werte sind es nicht — und die Amortisationsforderung von Rolle 13 ist damit an Zahlen zu
   beantworten, die niemand geprüft hat.
4. **Rolle 15 bewertet die Plattform, für deren Einführung Rolle 15 geschaffen wurde.** Macht 2,
   Interesse 5 — die größte Lücke zwischen Wollen und Können im ganzen Feld. Das gehört in den
   Pitch, nicht in eine Fußnote.
5. **Die Stakeholder-Anforderungen sind aus Haltungen abgeleitet, nicht erhoben.** Kein einziges
   Interview liegt vor. Die Zitate stammen aus [`menschen.md`](menschen.md) und sind dort
   überwiegend `angenommen`; Haltung und Nachtgedanke von Rolle 15 sind `generiert`.

---

## 13 · Offene Punkte

| # | Frage | Wer | Warum sie zählt |
|---:|---|---|---|
| 1 | Gilt 3,2 gesendete Profile je Besetzung nach 6 oder nach 12 Monaten? | Rolle 3, Rolle 10 | Der Widerspruch aus Abschnitt 10. Er entscheidet, ob der Pilot sein Ziel erreicht oder verfehlt — bei identischer Leistung |
| 2 | Liegt für **eine** der fünf Optionen ein Angebot vor? | Rolle 2 | Ohne Angebot ist Kriterium 5 mit 15 % auf Listenwerte gewichtet |
| 3 | Was kostet ein Plattformwechsel in Euro und Personentagen? | Anbietergespräch | Die Exit-Lücke trägt K6 mit 10 % |
| 4 | Deckt die Betriebsvereinbarung von 2023 den Plattformzugang mit ab? | Rolle 9 | Bestimmt, ob Ergänzung oder Neuverhandlung — und damit den Termin |
| 5 | Lässt sich einer der vier Benchmarks belegen? | Rolle 15 | Ein Datenproblem, per Recherche lösbar. Solange es offen ist, trägt jede Margenaussage einen Vorbehalt |

## Änderungsvermerk

| Datum | Was |
|---|---|
| 2026-09-10 | Auf die geltende Fassung 2 der KI-Analyse umgestellt: K3 15→17 %, K5 10→11 %, K7 3→4 %, K6 10→6 % ohne MCP. **MCP wiegt jetzt 0 %** — Boardzeile bleibt, Gewicht entfällt. „30 Prozent ohne Boardzeile" korrigiert auf 31 |
| 2026-09-10 | Aussage zur AÜG-Erlaubnis auf die belegbare Fassung zurückgenommen (Widerspruch zwischen vorhaben.md und transformationsvorschlag.md, siehe Auszug) |
| 2026-09-10 | angelegt. Elevator Pitch, vier Haftzettel zum Kopieren, Boardzeilen für alle sechs Kriterien gefüllt, Zuordnung zu K1–K8, vier Kennzahlen-Tabellen konsolidiert und fünf Widersprüche ausgewiesen, vier Benchmarks als Lücke markiert |
