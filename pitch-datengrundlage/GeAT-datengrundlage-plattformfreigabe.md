---
artefakt: Datengrundlage zum C-Level-Pitch „Plattformfreigabe" — Auszug, für Dritte
typ: DATENBLATT · kein Bestandteil des Unternehmensprofils
gehoert_nicht_zu: GeAT-unternehmensprofil/ — diese Datei ist eine Ableitung daraus, keine Quelle darin
datum: 2026-09-11
woche: 03
status: Auszug. Enthält ausschließlich die Werte, die in die Präsentation eingegangen sind
zweck: einem Dritten ermöglichen, die Präsentation nachzuvollziehen, zu prüfen oder nachzubauen
quellen: GeAT-unternehmensprofil/{profil,zahlen,systeme-daten,menschen,vorhaben}.md sowie w03A-3 bis w03A-5
personenbezug: keiner — alle Beteiligten sind als Rollen geführt
---

# Datengrundlage · C-Level-Pitch „Plattformfreigabe statt KI-Experiment"

> ## ⚠ Was diese Datei ist — und was sie nicht ist
>
> **Sie ist ein Datenblatt.** Sie sammelt an einer Stelle alle Werte, die in die Präsentation `c_level_pitch_plattformfreigabe.html` eingegangen sind, damit ein Dritter sie prüfen oder nachbauen kann.
>
> **Sie ist ausdrücklich kein Teil des Unternehmensprofils.** Das Profil liegt unter `GeAT-unternehmensprofil/` und bleibt die einzige gepflegte Quelle. Diese Datei ist eine **Ableitung mit Stand 11.09.2026** und wird nicht mitgepflegt. Bei Abweichungen gilt das Profil.
>
> **Und die wichtigste Einschränkung, wörtlich aus der Quelldatei `zahlen.md`:**
>
> > *„Zu Umsatz, Ergebnis und Bilanz der GeAT ist nichts öffentlich verfügbar. Die Werte sind aus
> > den belegten Beschäftigtenzahlen und den Branchenbenchmarks abgeleitet und so gesetzt, dass sie
> > sich gegenseitig stützen. Die **Struktur** der Rechnung ist übertragbar, die absoluten Werte
> > sind es nicht. **Für ein Deliverable außerhalb dieses Kurses ist keine Zahl dieser Datei
> > verwendbar.**"*
>
> Wer diese Daten weiterverwendet, verwendet also ein **durchgerechnetes Lehrbeispiel**, keine Unternehmensauskunft. Das Unternehmen existiert; die Hülle ist belegt, der Kern ist konstruiert.

---

## 0 · Lesehilfe — die Herkunftskennzeichen

Jeder Wert unten trägt eines dieser fünf Kennzeichen. Sie stammen aus dem Profil und sind das Wichtigste an dieser Datei:

| Kennzeichen | Bedeutung |
|---|---|
| `öffentlich` | belegt, mit Quelle nachweisbar |
| `angenommen` | aus Recherche und Branchen-Benchmarks abgeleitet, begründet gesetzt |
| `gerechnet` | rechnerisch aus anderen Werten dieser Datei abgeleitet |
| `generiert` | frei gesetzt, um den Fall vollständig zu machen — die schwächste Kategorie |
| `real` | tatsächlich zutreffend |

**Faustregel für Dritte:** Alles, was nach Geld aussieht, ist `angenommen` oder `gerechnet`. `öffentlich` sind im Wesentlichen Firma, Sitz, Gründung, Standorte und zwei historische Beschäftigtenzahlen.

---

## 1 · Unternehmen

| Angabe | Wert | Herkunft |
|---|---|---|
| Firma | GeAT – Gesellschaft für Arbeitnehmerüberlassung Thüringen mbH | `öffentlich` |
| Branche | Personaldienstleistung: Überlassung, Vermittlung, Beratung, Qualifizierung | `öffentlich` |
| Rechtsform | mbH (bis 2025 AG) | `öffentlich` |
| Gründung | 1995 | `öffentlich` |
| Standorte | sechs: Aschersleben, Erfurt, Gera, Gotha, Heilbad Heiligenstadt, Jena | `öffentlich` |
| Eigentümer | Investor | `angenommen` |
| **Beschäftigte gesamt** | **709** | `angenommen` |
| davon Zeitarbeitnehmer (Jahresdurchschnitt) | **640** — im Einsatz bei Kunden | `angenommen` |
| davon Stammpersonal | **69** — die Bildschirmarbeitsplätze | `angenommen` |
| Umsatz 2025 | 31,0 Mio € | `angenommen` |
| EBIT 2025 | 0,805 Mio € = 2,6 % | `gerechnet` (Benchmark 2–5 %) |

> **Die Unterscheidung 709 / 69 / 640 trägt die Präsentation an zwei Stellen** — sie begründet, warum 20 Zugänge genügen, und sie verhindert den Einwand „nur 20 von 709?".

---

## 1a · Status quo — wo das Unternehmen steht

*Kurzorientierung. Kein Ersatz für das Profil, aber genug, um zu beurteilen, ob die Gewichtung in Abschnitt 8 plausibel ist.*

**Die Lage in vier Sätzen.** Ein Personaldienstleister mittlerer Größe in einem schrumpfenden Markt: Umsatz −5,5 %, EBIT-Marge von 4,6 auf 2,6 % gefallen, Besetzungsquote von 48 auf 40 % gesunken, Besetzungsdauer von 8 auf 11 Arbeitstage gestiegen. Digitalisiert wird bisher nicht aus Strategie, sondern weil die Branchensoftware ersetzt werden muss. Es gibt seit Mai 2026 erstmals eine Rolle für Digitalisierung und KI — ohne Budget, ohne Gremium, ohne Weisungsrecht. Und es gibt eine gescheiterte Vorgängerinitiative, die jede neue Zusage belastet.

**Digitaler Reifegrad**, Skala 1 = ad hoc bis 5 = optimiert. **Einschätzung mit Stand 09/2026, ausdrücklich nicht validiert:**

| Dimension | IST | ZIEL | Woran der IST-Wert hängt |
|---|:---:|:---:|---|
| Strategie | 2 | 4 | kein Digitalisierungsziel mit Budgetposten; die einzige beschlossene Maßnahme mit Geld ist der Systemwechsel 2027 |
| Technologie | 2 | 4 | Kernsystem seit 2013, **ohne offene Schnittstelle im Bestandsvertrag**; Multiposting ohne Verbindung zum Bewerbermanagement |
| Daten | 2 | 3 | 41.000 Profile, **63 % ohne strukturierte Qualifikationsfelder**, Können steht im Freitext |
| Kultur | 2 | 3 | die Einführung von 2023 wurde **nie ausgewertet**, obwohl die Nutzung bei 34 % liegt |
| Prozesse | 2 | 4 | der Kernprozess läuft über drei Systeme und **vier manuelle Übertragungen**; Stundenzettel auf Papier und als Foto im Messenger |
| People | 3 | 4 | hohe Fachkompetenz, im Mittel 14 Jahre im Haus — aber keine Kapazität für Automatisierung |

> **Zwei Dinge daran sind für die Bewertung der Empfehlung wichtig.** Erstens: **Daten und Kultur stehen auf ZIEL 3, nicht 4** — hier wird bewusst nicht das Maximum angestrebt. Zweitens: Der Reifegrad ist eine **Einschätzung, keine Messung**. Jede Gewichtung in Abschnitt 8, die darauf aufbaut, trägt diesen Vorbehalt mit. Das ist der wichtigste Prüfpunkt für einen Dritten.

**Warum das die Gewichtung erklärt:** Technologie 2 und Prozesse 2 begründen das hohe Gewicht auf Betriebsaufwand und Exit. Daten 2 begründet, warum RAG-Fähigkeit nur 4 % bekommt — die Voraussetzung fehlt. Kultur 2 begründet die 17 % auf Adoption. **Ohne diese Tabelle wirken die Gewichte gegriffen; mit ihr sind sie herleitbar.**

---

## 1b · Roadmap — wo dieser Beschluss hingehört

Der Pitch entscheidet **Stufe 1 von fünf**. Die übrigen sind hier nur so weit aufgeführt, dass die Einordnung stimmt.

| Stufe | Ziel | Zeit | Betrag | Freigabe |
|:---:|---|---|---:|---|
| **1** | **Regelwerk vor Werkzeug** — die laufende Verarbeitung ohne Rechtsgrundlage beenden | Monat 1–2 | 22.000 € | **Geschäftsführung ← hier** |
| 2 | Die 480.000 € Anzeigenbudget auswertbar machen: welche Quelle erzeugt welche Besetzung | Monat 1–4 | 30.000 € | Gesellschafterversammlung |
| 3 | Datenfundament — Qualifikationskatalog, Pflichtfelder, Nichtbesetzungsgrund | Monat 3–10 | 110.000 € | Gesellschafterversammlung |
| 4 | Der Assistent — **Findewerkzeug, nicht Sortierer** | Monat 8–14 | 60.000 € | Gesellschafterversammlung |
| 5 | Den Zielkonflikt bezahlen: Zeit für Datenpflege vergüten statt appellieren | durchgehend | 18.000 € | Geschäftsführung |

**Die Taktung gegen das Quartalsgremium** — der Grund, warum Stufe 1 klein zugeschnitten ist:

| Termin | Was beschlossen werden muss |
|---|---|
| **sofort, Geschäftsführung** | **Stufe 1 (dieser Pitch)**, Stufe 5 anlaufend |
| Q4/2026 | Stufe 2 und 3 gemeinsam — **als Migrationsvorbereitung begründet, nicht als KI-Vorhaben** |
| Q1/2027 | keine Vorlage: die Migration läuft, die IT ist gebunden |
| Q2/2027 | Stufe 4, Pilotstart, mit den Ergebnissen aus 2 und 3 als Nachweis |

> **Drei Einordnungen für einen Dritten.** Erstens: **Stufe 2 steht bewusst vor Stufe 3.** Das Anzeigenbudget ist der einzige Posten, der sich aus laufenden Kosten refinanziert — er liefert die Amortisation an einer unstrittigen Stelle, bevor über das teure Stück geredet wird. Zweitens: **Stufe 5 läuft durchgehend mit**, nicht am Ende — sonst ist es wieder eine Ansage statt einer Vereinbarung, und genau daran ist 2023 gescheitert. Drittens: **Der Assistent kommt zuletzt.** Ohne die Stufen davor liefert er dasselbe Ergebnis wie 2023.

---

## 2 · Entscheidungswege und Freigabegrenzen

Der Punkt, an dem der ganze Zuschnitt des Vorhabens hängt.

| Angabe | Wert | Herkunft |
|---|---|---|
| Freigabe **bis** 25.000 € | Geschäftsführung, tagt **wöchentlich** (dienstags) | `angenommen` |
| Freigabe **über** 25.000 € | Gesellschafterversammlung, tagt **quartalsweise** | `angenommen` |
| Lenkungsausschuss Digitalisierung | **existiert nicht** | `angenommen` |
| Die vortragende Rolle | Digitalisierung und KI, geschaffen Mai 2026 — **kein eigenes Budget, kein Gremium, kein Weisungsrecht in den Niederlassungen** | Stelle `real`, Ausstattung `angenommen` |

**Was die Freigabeinstanzen jeweils verlangen** — der Pflichtwert, ohne den die Gegenargumente im Pitch nicht zu verstehen sind:

| Rolle | Forderung | Herkunft |
|---|---|---|
| Geschäftsführung, Vertriebsseite | schnelle Besetzung; trägt zugleich die Erinnerung an 2023 | `angenommen` |
| Geschäftsführung, Finanz-/IT-Seite | **keine zweite Baustelle vor der Migration** — die Migration ist ihr Vorhaben | `angenommen` |
| Gesellschaftervertretung | **„Amortisation unter 24 Monaten oder wartet, bis die Software steht."** | `angenommen` |
| Externer Datenschutzbeauftragter | stuft Bewerberauswahl als Annex III ein; seine Stellungnahme geht an die Gesellschafter | `angenommen` |

> **Die Amortisationsforderung ist der dritte Einwand im Pitch** — und die Antwort darauf lautet nicht „doch, es amortisiert sich", sondern: *bei dieser Maßnahme ist Amortisation die falsche Kennzahl; 9.000 € beenden ein Rechtsrisiko. Wer sie hier verlangt, verschiebt den Verstoß um ein Quartal.* Ein Dritter sollte diese Forderung kennen, sonst wirkt der Einwand im Pitch erfunden.

> **Die Zeile aus `zahlen.md`, die das erklärt:** *„Das ist keine Budgetgrenze, sondern eine Taktgrenze — und sie entscheidet mehr über den Zeitplan als die Technik."* Ein Vorhaben, das die Quartalssitzung verpasst, verliert ein Quartal.

**Daraus folgen zwei Aussagen der Präsentation:** dass überhaupt eine Freigabe nötig ist (die Rolle hat kein Budget), und dass der Betrag bewusst unter 25.000 € zugeschnitten wurde (sonst Quartalstakt).

---

## 3 · Der Anlass: ungeregelte KI-Nutzung

| Angabe | Wert | Herkunft |
|---|---|---|
| Personen mit **privaten KI-Konten** | **neun** — Recruiting und Innendienst, überwiegend unter 35 | `angenommen` |
| Dauer | seit etwa **einem Jahr** | `angenommen` |
| Verarbeitete Inhalte | Anzeigentexte und **Profilzusammenfassungen**, darunter Bewerberlebensläufe | `angenommen` |
| Auftragsverarbeitungsvertrag | **keiner**. Kein Beschluss, keine Freigabe, keine Regel | `angenommen` |
| Branchenvergleich | 46 % regelmäßige Nutzung | `öffentlich` |

---

## 4 · Datenbestand

| Angabe | Wert | Herkunft |
|---|---|---|
| **Bewerberprofile** | **41.000** | `angenommen` |
| davon mit strukturierten Qualifikationsfeldern | 15.000 — also **63 % unstrukturiert** | `angenommen` |
| **Profile über der zugesagten Speicherdauer** | **18.000** — kein Löschlauf etabliert | `angenommen` |
| Lebenslauf-PDF | 41.000 Dateien, **kein Textindex**, teils ohne Texterkennung | `angenommen` |
| Nachweispflichtige Scheine | 437 von 1.473 Profilen genannt, **für keinen ein Gültigkeitsdatum im Datenmodell** | gemessen am Übungsbestand |
| Datenverantwortung | **niemand formal** — faktisch das Recruiting Center | `angenommen` |

**Die 63 % begründen in der Präsentation**, warum das Kriterium „RAG und Integrationstiefe" nur 4 % Gewicht bekommt: die Voraussetzung fehlt. **Die 18.000 begründen** die Reihenfolge *erst löschen, dann strukturieren* und die Ersparnis von rund 24.000 € Aufbereitungsaufwand.

---

## 5 · IT-Landschaft und Migration

| Angabe | Wert | Herkunft |
|---|---|---|
| IT-Personal | **2 Köpfe, 1,5 Vollzeitstellen** | `angenommen` |
| Bindung | **bis Q1/2027 vollständig durch die Softwaremigration gebunden** | `angenommen` |
| Bewerbermanagement-Modul (ATS) | seit 2023, Modul der Branchensoftware | `angenommen` |
| Multiposting für Stellenanzeigen | seit 2021, Cloud — **keine Verbindung zum Bewerbermanagement**, Bewerbungen kommen ohne Quellenkennung | `angenommen` |
| Microsoft 365 | vorhanden — **die 41.000 Bewerberprofile liegen nicht darin** | `angenommen` |

> Der letzte Punkt ist das Ausschlusskriterium für Microsoft Copilot: dessen stärkste Eigenschaft — Zugriff über Microsoft Graph — greift beim relevanten Bestand nicht.

---

## 6 · Budget und Investitionsspielraum

| Angabe | Wert | Herkunft |
|---|---:|---|
| IT-Budget 2026 gesamt | 410.000 € = 1,3 % vom Umsatz | `gerechnet` |
| davon Projekte | 25.000 € | `angenommen` |
| **Anzeigen- und Jobbörsenbudget** | **480.000 €** — größer als das gesamte IT-Budget, liegt im Vertrieb | `angenommen` |
| Investitionsspielraum zwei Jahre (Basis EBIT 0,9 Mio) | 900.000 € | `angenommen` |
| reserviert für die Migration 2027 | − 620.000 € | `angenommen` |
| = im Haus umlaufender Wert | **280.000 €** | `gerechnet` |
| **korrigierter Wert (Basis EBIT 0,805 Mio)** | **185.000 €** | `gerechnet` |

> **Die Korrektur 280.000 → 185.000 erklärt:** Die 900.000 € stammen aus einer Ableitung mit 0,9 Mio EBIT. Das tatsächlich angesetzte EBIT beträgt 0,805 Mio; dieselbe Ableitung ergibt dann rund 805.000 €, abzüglich der Migrationsreserve **185.000 €**. In `zahlen.md` ist der Wert 900.000 bewusst stehen geblieben, weil er die Taktung des Transformationsvorschlags trägt — die Korrektur ist also eine **bekannte, dokumentierte Abweichung**, kein Rechenfehler.

---

## 7 · Die Vorgeschichte, die jeden Adoptionsanspruch prüft

| Angabe | Wert | Herkunft |
|---|---|---|
| Bewerbermanagement-Modul, lizenziert | **2023**, rund **95.000 €** | `angenommen` |
| Nutzungsgrad | **34 %** | `angenommen` |
| Erstmals gemessen | **2026** — und nur, weil ein ISO-Audit anstand | `angenommen` |
| Ursache | Datenpflege war für die Disposition reine Zusatzarbeit; Erfolg wird an besetzten Stellen gemessen, nicht an gepflegten Feldern | `angenommen` |

---

## 8 · Die Bewertungsmatrix

**Fünf Optionen.** Zwei davon stehen in keinem Lehrbuch und sind für diesen Fall ergänzt worden: die KI-Funktionen der künftigen Branchensoftware, und die Nullvariante.

| Kürzel | Option | Was gemeint ist |
|---|---|---|
| **A** | **Langdock** | Integrierte EU-Plattform, modellagnostisch, browserbasiert. **Die Empfehlung** |
| **B** | Microsoft Copilot for M365 | In Word, Teams, Outlook integriert; Datenzugriff über Microsoft Graph |
| **C** | Cloud-ML-Plattform | Entwicklerplattform für eigene Modelle |
| **D** | KI-Funktionen der Branchensoftware 2027 | Produktfunktion des künftigen Kernsystems, existiert erst nach der Migration |
| **E** | **Nullvariante** | Nichts tun, Zustand fortführen |

**Skalenanker für die Scores 1–5**, im Quelldokument fixiert:
*5 = erfüllt belegbar und vertraglich · 4 = erfüllt, Belege öffentlich (Herstellerdoku, Zertifikat) · 3 = teilweise, mit Aufwand herstellbar · 2 = nur auf der Roadmap oder nur behauptet · 1 = nicht vorgesehen.*
Mit zwei Regeln: **keine 5 ohne Angebot und AVV**, und **keine 4 für ein Produkt, das niemand benennen kann.**

**Acht Kriterien mit Gewichtung** (Summe 100 %, fixiert am 07.09.2026):

| Nr | Kriterium | Gewicht |
|---|---|---:|
| K1 | Compliance und AVV | 25 % |
| K2 | Verfügbarkeit gegen die Taktgrenze | 20 % |
| K3 | Adoptionspfad, **Einführungsaufwand** und Support | 17 % |
| K4 | Kosten über drei Jahre | 15 % |
| K5 | Betriebsaufwand bei 1,5 IT-Stellen | 11 % |
| K6 | Exit und Portabilität | 6 % |
| K7 | RAG und Integrationstiefe | 4 % |
| K8 | Deployment-Flexibilität | 2 % |

**Scores 1–5 und gewichtete Punktwerte:**

| Kriterium | Gew. | A · EU-Plattform | B · Copilot | C · Cloud-ML | D · Branchensw. 2027 | E · Nullvariante |
|---|---:|---:|---:|---:|---:|---:|
| K1 Compliance und AVV | 25 % | **4** → 1,00 | 3 → 0,75 | 3 → 0,75 | 2 → 0,50 | 2 → 0,50 |
| K2 Verfügbarkeit | 20 % | **4** → 0,80 | 3 → 0,60 | 1 → 0,20 | 1 → 0,20 | 2 → 0,40 |
| K3 Adoption/Einführung | 17 % | 2 → 0,34 | **4** → 0,68 | 1 → 0,17 | 3 → 0,51 | 2 → 0,34 |
| K4 Kosten 3 Jahre | 15 % | 3 → 0,45 | 3 → 0,45 | 1 → 0,15 | 3 → 0,45 | 3 → 0,45 |
| K5 Betriebsaufwand | 11 % | **4** → 0,44 | 3 → 0,33 | 1 → 0,11 | **4** → 0,44 | 3 → 0,33 |
| K6 Exit und Portabilität | 6 % | **4** → 0,24 | 2 → 0,12 | 3 → 0,18 | 1 → 0,06 | **4** → 0,24 |
| K7 RAG und Integration | 4 % | **4** → 0,16 | 3 → 0,12 | **4** → 0,16 | 3 → 0,12 | 1 → 0,04 |
| K8 Deployment | 2 % | 3 → 0,06 | 2 → 0,04 | 3 → 0,06 | 2 → 0,04 | 1 → 0,02 |
| **Gesamtscore** | **100 %** | **3,49** | **3,09** | **1,78** | **2,32** | **2,32** |
| *unabhängig belegt?* | | *nein* | *teilweise* | *teilweise* | *nein* | *entfällt* |

### Warum A gewinnt — die vier entscheidenden Zellen

Aus dem Quelldokument, alle vier aus dem Organisationskontext abgeleitet, keine aus einer Broschüre:

| Zelle | Begründung |
|---|---|
| **K1 Compliance, 25 % · A = 4, B = 3** | Modellagnostische EU-Plattformen bieten AVV und EU-Verarbeitung als Standardangebot mit öffentlicher Dokumentation. Copilot bleibt bei 3, weil seine Compliance **nicht im Vertrag entschieden wird**, sondern an der Berechtigungsstruktur hängt |
| **K2 Verfügbarkeit, 20 % · A = 4, B = 3** | Beide sind schnell. A ist schneller, weil bei Copilot **die Berechtigungsprüfung davorliegt und die Basislizenz ungeklärt ist** |
| **K5 + K6, zusammen 17 % · A = 4/4, B = 3/2** | A **hängt nicht am Kernsystem**, das Q1/2027 ersetzt wird, und erzeugt keinen Betrieb im Haus. Copilot bringt Ecosystem-Bindung über Graph mit — kein prinzipielles Problem, aber sechs Monate vor einem Systemwechsel teuer |
| **K3 Adoption, 17 % · A = 2, B = 4** | **Was A verliert.** Neuer Lieferant, neue Oberfläche, neue Nutzerverwaltung über sechs Standorte — in einem Haus, dessen letztes Werkzeug bei 34 % Nutzung liegt. Im Quelldokument als *„die teuerste Zelle der Empfehlung"* bezeichnet |

**D und E liegen mit je 2,32 gleichauf.** Der Score kann sie nicht trennen, und das ist der Befund, nicht die Schwäche: die eine Option ist inhaltlich stark und terminlich unmöglich, die andere terminlich verfügbar und inhaltlich leer.

### Kostenzeile je Option

Alle Preise sind **Listenwerte, prüfpflichtig, kein Angebot liegt vor.**

| Option | 20 Zugänge/Jahr | 69 Zugänge/Jahr | 20 Zugänge über 3 Jahre | Vorleistung, nicht in der Lizenz |
|---|---:|---:|---:|---|
| **A** Langdock | 4.800 – 7.200 € | 16.560 – 24.840 € | 14.400 – 21.600 € | neuer Lieferant: AVV, SSO, Nutzerverwaltung über sechs Standorte, Schulung |
| **B** Copilot | 7.200 € | 24.840 € | 21.600 € | Berechtigungsstruktur in SharePoint prüfen, **Aufwand unbeziffert**; Basislizenz ungeprüft |
| **C** Cloud-ML | Verbrauch, gering | Verbrauch, gering | — | Oberfläche, Authentifizierung, Protokollierung, Betrieb — der bestimmende Posten, ohne Angebot nicht nennbar |
| **D** Branchensoftware | nicht separat | nicht separat | — | Verhandlungsaufwand, solange die Ausschreibung offen ist; danach Change Request |
| **E** Nullvariante | **0 €** | **0 €** | **0 €** | Kontrollaufwand plus Stunden des Datenschutzbeauftragten. **Risiko der laufenden Verarbeitung nicht bezifferbar** |

> **Die Kostenzeile der Nullvariante ist der ehrlichste Wert der ganzen Tabelle** — und der einzige, bei dem ein Dritter aufpassen muss. Nichts zu tun kostet **nachweisbar null Euro**; was es tatsächlich kostet, ist das Risiko der fortlaufenden Verarbeitung ohne Rechtsgrundlage, **und das ist in diesem Fall nicht beziffert worden.** Wer die Empfehlung prüft, prüft an dieser Stelle eine Einschätzung, keine Rechnung. Der Pitch argumentiert deshalb nicht über Kosten, sondern über Sichtbarkeit: *ein Verbot ohne Ersatz beendet nicht die Nutzung, nur die Beobachtung.*
>
> **Und eine Korrektur aus dem Quelldokument, die zum Zuschnitt gehört:** 20 Zugänge Copilot kosten 7.200 € und passen ebenfalls unter den Ansatz von 9.000 €. Der Kostenvorteil von A entsteht erst über drei Jahre und bei größerer Zahl. **Kosten sind hier also nicht das entscheidende Kriterium** — wer das behauptet, überzeichnet.

> **Die letzte Zeile der Matrix ist die wichtigste für einen Dritten.** Alle Bewertungen der empfohlenen Option beruhen auf **Herstellerunterlagen**; ein Angebot lag zum Zeitpunkt der Präsentation nicht vor. Das ist im Pitch als Bedingung ausgewiesen, nicht verschwiegen.

**Zwei Optionen scheiden vor der Bewertung aus, nicht über Punkte:** Cloud-ML, weil kein Data-Science-Team existiert · Copilot, weil der Bestand nicht in Microsoft 365 liegt.

---

## 9 · Sensitivität und Kippschwelle

| Angabe | Wert |
|---|---|
| Verfahren | jedes Gewicht um **±10 Prozentpunkte** verschoben, Rest proportional |
| Anzahl Durchläufe | **16** (8 Kriterien × 2 Richtungen) |
| Ergebnis | Sieger hält in **allen 16** |
| Härtere Probe | K1 Compliance auf **0 %** → Sieger hält |
| Gleichgewichtsprobe | alle Kriterien gleich schwer → 3,50 gegen 2,88, Sieger hält |
| **Einzige Kippschwelle** | **K3 über 31 %** → dann gewinnt Copilot |
| Abstand der Gesamtscores | 0,40 (in Fassung 1 noch 0,80) |

> **Zwei Präzisierungen, die ein Dritter kennen sollte.** Erstens: Bei K6 (6 %), K7 (4 %) und K8 (2 %) ist die Variante „−10" faktisch eine **Null-Probe**, weil 10 Punkte nicht abziehbar sind. Zweitens: Die stärkste K3-Variante erreicht **27 %**, die Kippschwelle liegt bei **31 %** — die Probe verfehlt den Kipppunkt also um vier Punkte. „16 von 16" stimmt, kommt der Grenze aber nahe.

---

## 10 · Der Beschlussgegenstand

| Angabe | Wert | Herkunft |
|---|---|---|
| Zugänge | **20**, über **drei** Standorte | `angenommen` |
| Kosten | **≤ 9.000 € im Jahr** | `angenommen`, kein Angebot |
| IT-Aufwand | **≤ 10 Stunden**, keine Schnittstelle, kein Entwicklungsauftrag | `angenommen` |
| Probezeit | **90 Tage** | gesetzt |
| Abbruchbedingung 1 | kein Lebenslauf mehr in einem privaten Konto | gesetzt |
| Abbruchbedingung 2 | mindestens **2 von 3** Standorten arbeiten wöchentlich damit | gesetzt |
| Folge bei Nichterfüllung | Kündigung zum Quartalsende, Grund protokolliert | gesetzt |
| **Empfohlene Option** | **Langdock** (Option A) — Angebot steht aus | Bewertung |
| Bedingung Datenschutz | schriftliche Freigabe, AV-Vertrag **vorgelegt**, Löschung nachweisbar | gesetzt |
| Bedingung Mitbestimmung | **Betriebsvereinbarung, die Leistungskontrolle ausschließt** | gesetzt |
| Bedingung Markt | **2 Referenzkunden im DACH-Raum unter 150 Beschäftigten** | gesetzt |
| Bedingung Einführung | Schulung durch die neun, keine externe Beratung | gesetzt |
| Ersparnis Löschung vor Strukturierung | rund **24.000 €** | `gerechnet` |

---

## 11 · Welche Folie welche Zahl braucht

Für einen Dritten, der die Präsentation nachbaut oder prüft:

| Folie | Benötigte Werte | Abschnitt hier |
|---|---|---|
| 2 · Beschluss | 9.000 € · 20 Zugänge · 3 Standorte · Grenze 25.000 € · quartalsweise | [2](#2--entscheidungswege-und-freigabegrenzen), [10](#10--der-beschlussgegenstand) |
| 3 · Der Grund | 9 Konten · 1 Jahr · 0 AV-Verträge | [3](#3--der-anlass-ungeregelte-ki-nutzung) |
| 4 · Wie es geht | ≤ 10 h IT · 0 Schnittstellen · 9.000 von 185.000 € · 69/709/640 · 1,5 IT-Stellen bis Q1/2027 | [1](#1--unternehmen), [5](#5--it-landschaft-und-migration), [6](#6--budget-und-investitionsspielraum) |
| 5 · Wann und Stop | 90 Tage · beide Abbruchbedingungen | [10](#10--der-beschlussgegenstand) |
| 6 · Alternativen | kein Data-Science-Team · 41.000 Profile nicht in M365 · Migration Q1/2027 · Nullvariante Platz 2 | [4](#4--datenbestand), [5](#5--it-landschaft-und-migration), [8](#8--die-bewertungsmatrix) |
| 7 · Robustheit | 3,49 / 3,09 von 5 · 16 Varianten · K3 17 % → 31 % | [8](#8--die-bewertungsmatrix), [9](#9--sensitivität-und-kippschwelle) |
| 8 · Gegenargument | 95.000 € · 34 % · 2026 · ISO-Audit | [7](#7--die-vorgeschichte-die-jeden-adoptionsanspruch-prüft) |
| 8 · Gegenargument, Einwand 3 | Amortisationsforderung der Gesellschaftervertretung | [2](#2--entscheidungswege-und-freigabegrenzen) |
| 10 · Bedingungen | AV-Vertrag · 2 Referenzkunden < 150 · Einführungsaufwand unbeziffert | [10](#10--der-beschlussgegenstand) |
| 11 · Zweitbeschluss | Stand der Migrationsausschreibung (**unbekannt**) | [12](#12--was-nicht-belegt-ist) |
| 12 · Reihenfolge | 18.000 Profile · rund 24.000 € | [4](#4--datenbestand), [10](#10--der-beschlussgegenstand) |

---

## 12 · Was nicht belegt ist

Vier Lücken, die in der Präsentation ausdrücklich als solche vorgetragen werden. Ein Dritter sollte sie nicht für Nachlässigkeit halten — sie sind Teil des Arguments:

1. **Der Einführungsaufwand der empfohlenen Option ist nicht beziffert.** Es ist zugleich die einzige Größe, die die Empfehlung umdrehen könnte (Kippschwelle 31 %).
2. **Es liegt kein Angebot vor.** Alle Bewertungen beruhen auf Herstellerunterlagen.
3. **Der Stand der Migrationsausschreibung ist unbekannt** und konnte von der vortragenden Rolle nicht selbst geklärt werden.
4. **Das Risiko der Nullvariante ist nicht beziffert.** Nichts zu tun kostet nachweisbar 0 € an Lizenz, Einführung und Betrieb; was die fortlaufende Verarbeitung ohne Rechtsgrundlage kostet, wurde nicht gerechnet. Die Empfehlung stützt sich an dieser Stelle auf eine **Einschätzung**, nicht auf eine Rechnung.
5. **Ob eine Datenschutz-Folgenabschätzung nötig ist, ist offen** — zu klären schriftlich, vor dem ersten Lauf.

Dazu eine fünfte, die weiter zurückreicht: **Der Reifegrad, auf dem die Gewichtung aufbaut, ist eine nicht validierte Einschätzung** — erhoben als Gruppenurteil, nicht über Prozessdaten oder Interviews. Jede Gewichtung, die darauf steht, trägt diesen Vorbehalt mit.

---

## 13 · Herkunft dieser Datei

Zusammengestellt am **11.09.2026** aus:

| Quelle | Was daraus stammt |
|---|---|
| `GeAT-unternehmensprofil/profil.md` | Stammdaten, Reifegrad, Vorgeschichte 2023, Investitionsspielraum |
| `GeAT-unternehmensprofil/zahlen.md` | GuV, IT-Budget, Anzeigenbudget, Freigabegrenzen, Vorbehalt |
| `GeAT-unternehmensprofil/systeme-daten.md` | Systemlandschaft, Bewerberbestand, private KI-Konten |
| `GeAT-unternehmensprofil/menschen.md` | Gremien, Tagungsrhythmus, Ausstattung der vortragenden Rolle |
| `GeAT-unternehmensprofil/w03A-3-…-gueltig.md` | Kriterien, Gewichte, Scores, Gesamtscores |
| `GeAT-unternehmensprofil/w03A-4-use-case-und-sensitivitaet.md` | Sensitivitätsprobe, Kippschwelle |
| `GeAT-unternehmensprofil/w03A-5-entscheidungsvorlage.md` | 90 Tage, Bedingungen, offene Fragen |

**Alle Beteiligten sind als Rollen geführt.** Im Unternehmensprofil stehen Namen; sie sind bis auf eine Ausnahme erfunden. In dieser Datei kommt keiner vor — sie ist für Dritte gedacht.

**Nicht enthalten:** Rohertrags- und Margenrechnung, Prozesskennzahlen im Detail, Stakeholder- und Widerstandsanalysen, die Ausgestaltung der Stufen 2 bis 5, die zweite Bewertungsmatrix für Stufe 4. Die Abschnitte [1a](#1a--status-quo--wo-das-unternehmen-steht) und [1b](#1b--roadmap--wo-dieser-beschluss-hingehört) geben eine **Kurzorientierung**, damit die Gewichtung beurteilbar ist — sie ersetzen das Profil nicht. Wer mit dem Unternehmen arbeiten will statt nur diese eine Entscheidung zu prüfen, arbeitet mit `GeAT-unternehmensprofil/`.
