---
titel: KI-Analyse GeAT mbH — Plattform- und Werkzeugwahl, nachgebesserte Fassung
bezug: Erstfassung KI_Analyse.md · Review KI_Analyse_Review.md · Gespraeche/03-der-einwand-der-stimmt.md · ereignisse.md Woche 2.4 · profil.md, zahlen.md, systeme-daten.md, menschen.md, vorhaben.md, transformationsvorschlag.md
typ: Analyse und Entscheidungsvorlage, nicht beschlossen
datum: 2026-09-07
woche: 03
status: Fassung 2, ersetzt KI_Analyse.md
verantwortlich: Rolle 15 (AI and Digital Transformation Manager) — Macht 2, kein Budget, kein Gremium
herkunft: abgeleitet — Gewichtungen sind begründete Setzungen, Scores sind Einschätzungen auf Herstellerunterlagen, Preise sind prüfpflichtige Listenwerte, Rechtsaussagen sind Arbeitshypothesen
---

# KI-Analyse GeAT mbH — nachgebesserte Fassung

> **Was diese Datei ist.** Fassung 2 der Plattform- und Werkzeugwahl. Sie ersetzt [`KI_Analyse.md`](KI_Analyse.md) und arbeitet zwei Quellen ein, die in der Erstfassung fehlten: das Review in [`KI_Analyse_Review.md`](KI_Analyse_Review.md) und die **Nachbesserungen aus Woche 2.4**, die laut [`ereignisse.md`](ereignisse.md) offen sind und in [`Gespraeche/03-der-einwand-der-stimmt.md`](Gespraeche/03-der-einwand-der-stimmt.md) im Wortlaut stehen.
>
> **Das Ergebnis hat sich geändert, nicht nur die Begründung.** Teil A behält seinen Sieger mit deutlich kleinerem Abstand. **Teil B hat einen anderen Sieger** — und er kommt nicht aus dem Review, sondern aus dem Gespräch mit dem Datenschutzbeauftragten, das die Erstfassung nicht gelesen hatte.
>
> **Herkunftskennzeichen wie in Fassung 1:** `Fakt` = belegt oder im Profil als `öffentlich` geführt · `Annahme` = begründete Setzung dieser Analyse · `Einschätzung` = mein Urteil, bestreitbar · `Rechtshypothese` = von Marnitz **und** der Zweitkanzlei zu bestätigen, nicht von mir.

**Inhalt:** [0 Prüfprotokoll](#0-prüfprotokoll-zum-review) · [1 Methode](#1-methode-anker-tore-und-der-reihenfolge-schutz) · [2 Der Rechtsrahmen, korrigiert](#2-der-rechtsrahmen-korrigiert) · [3 Die Budgetwahrheit](#3-die-budgetwahrheit-185000-statt-280000) · [4 Teil A](#4-teil-a--stufe-1-der-freigegebene-zugang) · [5 Matrix A](#5-matrix-a-revidiert) · [6 Teil B](#6-teil-b--stufe-4-mit-der-sechsten-option) · [7 Matrix B](#7-matrix-b-revidiert-sechs-optionen) · [8 Was kein Score misst](#8-was-kein-score-misst) · [9 Gegenargumente](#9-gegenargumente-und-risiken) · [10 Empfehlung](#10-die-empfehlung) · [11 Offene Punkte](#11-offene-punkte-und-prüffragen)

---

## 0. Prüfprotokoll zum Review

Ich habe jeden Punkt des Reviews gegen die Primärdateien geprüft, bevor ich ihn übernommen habe. **Neun von zwölf Punkten sind berechtigt, drei sind es nicht.** Beides steht hier, weil eine Vorlage, die Kritik ungeprüft einarbeitet, genauso unbrauchbar ist wie eine, die sie ignoriert.

### 0.1 Übernommen

| Review-Punkt | Befund der Prüfung | Wo es in Fassung 2 wirkt |
|---|---|---|
| **Fehler 2** · Budgetäre Konsequenz nicht gezogen | **Berechtigt im Kern.** Die Erstfassung nannte die Zahlen, aber nur in der Tabelle „Offene Punkte" — und kürte in Teil B trotzdem einen Sieger für ein Vorhaben, das nicht finanziert ist | **Neuer [Abschnitt 3](#3-die-budgetwahrheit-185000-statt-280000)**, vor beiden Matrizen |
| **Fehler 3** · Bruch der eigenen Skalenanker bei Option D | **Vollständig berechtigt und der schwerste Einwand.** Score 4 für ein Produkt eines nicht ausgewählten Anbieters verletzt den Anker „Belege öffentlich" frontal. Die Erstfassung hat das in 10.3 zugegeben und in 6.3 trotzdem gewinnen lassen | Option D auf **2** bei L1, auf **3** bei L2 und L4 korrigiert. D fällt von Platz 1 auf Platz 5 |
| **Fehler 4** · Betreiberpflichten ausgeblendet | **Berechtigt, und im Fall schon nachgewiesen.** Marnitz hat sieben Pflichten aufgezählt und festgestellt: *„Keine dieser sieben Pflichten hat dort eine eigene Zeile."* Die Erstfassung hat „GeAT bleibt Betreiber" wie eine Entlastung behandelt | **Neuer [Abschnitt 2](#2-der-rechtsrahmen-korrigiert)** mit Pflichtenliste und Kostenfolge |
| **Schwäche 1** · Nullvarianten-Paradoxon | **Berechtigt.** Matrix B hat 73 % ihres Gewichts auf Risiko-, Kosten- und Aufwandsvermeidung gelegt und kein Kriterium für Wirkung. Eine Matrix, die Untätigkeit belohnt, ist falsch konstruiert | **Neues Kriterium L0** (20 %) in Matrix B |
| **Schwäche 2** · Zeitplan der Migrationsausschreibung | **Berechtigt.** Ein Go-Live Q1/2027 heißt, dass die Verträge im September 2026 geschlossen oder in der juristischen Endabstimmung sind. Sechs Anforderungen in Q4/2026 nachzuverhandeln ist keine Empfehlung, sondern eine Hoffnung | Empfehlung 2 auf **drei** Anforderungen reduziert, mit Entscheidungsregel für den Fall, dass die Ausschreibung zu ist |
| **Schwäche 3a** · Asymmetrische Kostendarstellung bei Copilot | **Berechtigt.** 20 Seats Copilot kosten 7.200 € und passen unter den Stufe-1-Ansatz von 9.000 €. Die Erstfassung hat den 69-Seat-Fall rhetorisch nach vorn gestellt | K4 bei Copilot von **2 auf 3** korrigiert. Abstand A zu B fällt von 0,80 auf **0,40** |
| **Schwäche 3b** · Einführungsaufwand von Option A ignoriert | **Berechtigt.** Neuer Lieferant, AVV, SSO, Nutzerverwaltung, Schulung auf eine neue Oberfläche — die Erstfassung hat das bei A nicht bewertet und bei B nur die Vorleistung gesehen | K3 bei A von **3 auf 2** korrigiert, Kriterium umbenannt in „Adoptionspfad, **Einführungsaufwand** und Support" |
| **Schwäche 3c** · M365-Basislizenz ungeprüft | **Berechtigt und eine echte Lücke.** Copilot setzt eine qualifizierende Basislizenz voraus. Welche M365-Pläne GeAT seit 2020 hat, steht nirgends im Profil | **Neuer offener Punkt 7** in 11.1 |
| **Schwäche 4** · RAG auf Altdaten | **Berechtigt.** Die Erstfassung hat Option D bei L2 eine 4 gegeben, weil „die Daten im System liegen". Im System liegen ≠ verwertbar: 63 % ohne strukturierte Felder, kein Textindex, Scans ohne Texterkennung, elf Schreibweisen für „Staplerschein" | L2 bei D auf **3** korrigiert, Kriterium umbenannt in „Zugang **und Verwertbarkeit**" |
| **Schwäche 5** · MCP bei 1,5 IT-Stellen | **Berechtigt.** MCP verlangt jemanden, der Server baut und betreibt. GeAT hat zwei Personen ohne Entwicklungsauftrag. Portabilität bleibt ein Kriterium, MCP war ein Kursreflex | K6/L6 umbenannt in „Exit und Portabilität", MCP herausgenommen, Gewicht von 10 % auf **6 %** |
| **Bedenken 1–4** · Stakeholder und Kultur | **Berechtigt.** Insbesondere: 20 Lizenzen nur für Erfurt verspielt Rehberg, bevor Stufe 5 ihn braucht | **Sitzverteilung geändert** ([10.1](#empfehlung-1--jetzt-integrierte-eu-plattform-20-seats-über-drei-standorte)), Abbruchkriterium ersetzt, Vorab-Koalition als Arbeitsschritt aufgenommen |

### 0.2 Zurückgewiesen — mit Nachweis

| Review-Punkt | Warum er nicht trägt |
|---|---|
| **Fehler 1** · „Der AÜG-Erlaubnis-Mythos steht in `KI_Analyse.md` Zeile 126–127" | **Fehlzuschreibung.** Der zitierte Satz steht nicht in `KI_Analyse.md`, sondern in [`transformationsvorschlag.md`](transformationsvorschlag.md) **Zeile 126** — das Review hat die Zeilennummer der falschen Datei gelesen. `KI_Analyse.md` nennt das AÜG genau einmal, in Kontextzeile 3, rein deskriptiv und ohne Kausalbehauptung. **Der Fehler ist echt, aber er steht in einer anderen Datei** — und er ist in [`ereignisse.md`](ereignisse.md) Woche 2.4 bereits als offene Nachbesserung vermerkt. [Abschnitt 2.3](#23-was-in-transformationsvorschlagmd-noch-zu-streichen-ist) liefert den Ersatztext, damit der Punkt nicht ein drittes Mal auftaucht |
| **Fehler 2, Teilbehauptung** · „Die Analyse kalkuliert mit einem Investitionsspielraum von 280.000 €" | **Falsch.** `KI_Analyse.md` nennt 280.000 € an genau einer Stelle — Zeile 364, im offenen Punkt 6, und dort ausdrücklich als den Wert, der auf 185.000 € zu korrigieren ist. Der Vorwurf lautet richtig: *die Konsequenz wurde benannt und nicht gezogen.* So steht er in 0.1 |
| **Fehler 3, Nachrechnung** · „Option D sinkt von 3,43 auf 2,23" | **Rechenfehler.** Setzt man L1, L2, L4 und L5 auf 2, ergibt die Gewichtung B der Erstfassung **1,97**, nicht 2,23. Die Richtung stimmt, die Zahl nicht. Fassung 2 rechnet neu und kommt bei anderer Korrektur auf **2,36** |
| **Fehler 4, Punkt 6** · „Art. 27 FRIA: GeAT muss eine Grundrechte-Folgenabschätzung durchführen" | **Trägt für GeAT nicht.** Die Pflicht nach Art. 27 richtet sich an Betreiber, die öffentliche Stellen sind oder öffentliche Dienste erbringen, sowie an Betreiber der Systeme nach Annex III Nr. 5 Buchst. b und c (Kreditwürdigkeit, Risikobewertung in der Lebens- und Krankenversicherung). GeAT ist ein privater Verleiher unter **Annex III Nr. 4**. Eine **Datenschutz-Folgenabschätzung nach Art. 35 DSGVO** ist dagegen fällig und in Fassung 2 aufgenommen (`Rechtshypothese`) |
| **Fehler 4, Nummerierung** · „Art. 26 Abs. 11a" | Existiert nicht. Die Unterrichtung der Arbeitnehmervertretung ist **Art. 26 Abs. 7**, die Information der betroffenen Personen **Art. 26 Abs. 11**. Korrigiert in [Abschnitt 2.1](#21-die-betreiberpflichten-die-in-keiner-kostenzeile-stehen) (`Rechtshypothese`) |
| **Schwäche 3, Teilbehauptung** · „Für Stufe 1 greift Copilot gar nicht auf SharePoint zu" | **Zu stark.** Der lizenzierte M365-Copilot ist über Microsoft Graph auf Unternehmensinhalte geerdet; das lässt sich konfigurativ eingrenzen, aber nicht wegdefinieren. Genau deshalb bleibt K1 bei **3** = „teilweise, mit Aufwand herstellbar" — das ist die Bewertung, die die Argumentation des Reviews selbst stützt, nicht eine 4 |
| **Redline 4** · „Kriterium L0: Beitrag zur Senkung der **Besetzungsdauer**" | **Richtige Idee, falsche Kennzahl.** [`vorhaben.md`](vorhaben.md) und [`zahlen.md`](zahlen.md) verwerfen die Besetzungsdauer als Pilotkennzahl ausdrücklich: von 11 Tagen sind 0,4 Tage Arbeit, 96 % sind Warteschleifen, die kein Werkzeug anfasst. Wer L0 auf die Besetzungsdauer legt, trägt genau den Fehler in die Matrix zurück, den das Profil in Woche 2.3 abgestellt hat. **L0 misst deshalb die Leitkennzahl: gesendete Profile je Besetzung (4,8 → 3,2)** |

### 0.3 Was das Review nicht gesehen hat — und was das Ergebnis dreht

Das Review prüft die Erstfassung gegen sich selbst. Es prüft sie nicht gegen [`Gespraeche/03-der-einwand-der-stimmt.md`](Gespraeche/03-der-einwand-der-stimmt.md) — und dort steht der Einwand, der Teil B entscheidet.

**Erstens: Marnitz hat Option D vorweg widerlegt, ein Jahr bevor ich sie zum Sieger erklärt habe.** Wörtlich:

> *„Eine Anforderung ist keine Klärung. Sie schreiben in eine Ausschreibung, dass ein Anbieter etwas tragen soll. Was er unterschreibt, wissen Sie in einem Jahr, und was er unterschreibt, wird weniger sein. Das ist keine Unterstellung, das ist der Markt: Anbieter von Personalsoftware verkaufen Ihnen ein Werkzeug und schreiben in die AGB, dass der Kunde für die Rechtmäßigkeit der Nutzung verantwortlich ist. **Sie werden Betreiber sein und einen Teil der Anbieterpflichten faktisch mittragen.**"*

Das ist die inhaltliche Begründung für dieselbe Korrektur, die das Review methodisch fordert — und sie ist die stärkere, weil sie nicht nur sagt, dass der Score unbelegt ist, sondern **warum er auch nach der Ausschreibung nicht zutreffen wird.** Option D fällt damit nicht auf 2, weil noch kein Anbieter feststeht, sondern weil der Markt so nicht liefert.

**Zweitens, und das ist die eigentliche Nachbesserung: Marnitz hat eine sechste Option genannt, die in keiner der beiden Matrizen vorkam.**

> *„Nach dem, was ich beurteilen kann: nur eine Konstruktion, in der die Auswahl über nachvollziehbare, dokumentierte Kriterien läuft und das Sprachmodell nur formuliert, was ohnehin schon entschieden ist. Filter über strukturierte Felder — Qualifikation, Gültigkeit, Verfügbarkeit, Entfernung. Das ist nachvollziehbar, das ist reproduzierbar, das können Sie einem Bewerber erklären und einer Aufsicht vorlegen."*

Diese Option — **regelbasierter Filter, Sprachmodell nur zur Formulierung** — steht in Fassung 2 als **Option F** und gewinnt Teil B mit deutlichem Abstand. Sie ist die einzige Option, die gleichzeitig die Budgetgrenze aus [Abschnitt 3](#3-die-budgetwahrheit-185000-statt-280000) einhält, das Einstufungsrisiko aus [Abschnitt 2](#2-der-rechtsrahmen-korrigiert) auflöst und das Nullvarianten-Paradoxon aus dem Review beendet — nicht durch ein zusätzliches Kriterium, sondern durch eine Option, die tatsächlich wirkt.

**Drittens: drei Nachbesserungen aus Woche 2.4 waren in der Erstfassung nicht eingearbeitet**, obwohl [`ereignisse.md`](ereignisse.md) sie als offen führt: die Reihenfolge **3c vor 3b** (spart gut 24.000 €), der Pilotstart vor Fertigstellung der Gültigkeitsfelder, und der AÜG-Satz. Alle drei sind hier berücksichtigt.

---

## 1. Methode: Anker, Tore und der Reihenfolge-Schutz

Unverändert gegenüber Fassung 1, weil das Review sie nicht bestreitet: **erst Kontext festlegen, dann gewichten, dann scoren.**

| Wert | Bedeutung |
|---:|---|
| **5** | erfüllt, belegbar **und vertraglich zugesichert** |
| **4** | erfüllt, Belege öffentlich (Herstellerdokumentation, Zertifikat) |
| **3** | teilweise erfüllt, mit Aufwand herstellbar |
| **2** | nur auf der Roadmap oder nur behauptet |
| **1** | nicht vorgesehen |

**Keine 5 ohne Angebot und AVV.** Und die Regel, die Fassung 1 gebrochen hat und die hier durchgehalten wird: **keine 4 für ein Produkt, das niemand benennen kann.** Wer einen Anker aufschreibt und ihn dann in der Spalte bricht, die gewinnen soll, hat nicht gewichtet, sondern gewünscht. Das ist der Grund, warum Option D in Fassung 2 verliert.

**Die drei Tore, unverändert vor dem Scoring:**

| Tor | Grundlage | Prüffrage | Wer entscheidet |
|---|---|---|---|
| **T1 · AVV vorgelegt** | Art. 28 DSGVO. Neun Stammkräfte fügen heute Lebensläufe in private Konten ein, ohne Vertrag | „Legen Sie den AVV vor, nicht die Aussage, dass Sie DSGVO-konform sind" | Marnitz, Achtelik |
| **T2 · Protokollierung begrenzbar, Leistungs- und Verhaltenskontrolle ausschließbar** | § 87 BetrVG. Der Betriebsrat hat 2023 beim ATS-Modul darauf bestanden | „Welche Nutzerprotokolle entstehen, wer sieht sie, lässt sich der Umfang vertraglich begrenzen?" | Nowak |
| **T3 · EU-Verarbeitung, Löschfristen technisch durchsetzbar** | Art. 9 DSGVO. Teils Gesundheitsangaben; 18.000 Profile über der zugesagten Speicherdauer | „Wo liegen die Daten, wie löschen Sie nachweisbar?" | Marnitz |

**Neu in Fassung 2, weil Marnitz darauf besteht:** Vor der Ausschreibung braucht es **drei Dokumente**, nicht drei Zusicherungen — eine dokumentierte Einstufungsentscheidung, eine namentliche Aufstellung der Betreiberpflichten mit Kosten, und ein Konzept zur Information der 41.000 Betroffenen. Siehe [2.2](#22-die-drei-dokumente-vor-der-ausschreibung).

---

## 2. Der Rechtsrahmen, korrigiert

> **Alles in diesem Abschnitt ist `Rechtshypothese`.** Ich bin nicht Jurist, die Artikelnummern sind von Marnitz **und** von der Zweitkanzlei zu bestätigen ([Abschnitt 3](#3-die-budgetwahrheit-185000-statt-280000), Position Zweitmeinung). Das Review hat hier zwei Fehler gemacht, ich hatte in Fassung 1 eine Lücke — der Punkt verträgt keine dritte Runde aus dem Gedächtnis.

### 2.1 Die Betreiberpflichten, die in keiner Kostenzeile stehen

Fassung 1 hat „GeAT bleibt Betreiber" behandelt, als wäre das die Entlastung. Es ist eine **Reduktion**, keine Befreiung: Die Konformitätsbewertung, die technische Dokumentation als Hersteller und die Registrierung entfallen — die eigenen Pflichten des Betreibers nicht.

| Pflicht | Fundstelle (`Rechtshypothese`) | Was sie bei GeAT konkret verlangt | Kostenzeile heute |
|---|---|---|---|
| **Menschliche Aufsicht mit Kompetenz** | Art. 26 Abs. 2 | Die Disponenten müssen den Vorschlag verstehen, prüfen und begründet abweichen können. **Kein Beschäftigter im Haus hat heute eine dokumentierte Qualifizierung im Umgang mit KI-Vorschlägen** (`Fakt` im Fall, Reifegrad People) | **keine** |
| **KI-Kompetenz der Belegschaft** | Art. 4 | Gilt für Betreiber unabhängig von der Risikoklasse. Das ist der Punkt, an dem Weiskopf (Rolle 14, Academy) aus einer Nebenrolle in die Pflicht rückt | **keine** |
| **Repräsentativität der Eingabedaten** | Art. 26 Abs. 4 | Soweit GeAT die Eingabedaten kontrolliert: 63 % der Profile ohne strukturierte Felder, 28,8 % der Zeitarbeitnehmer ohne Berufsabschluss. Das Risiko liegt bei GeAT, nicht beim Anbieter | **keine** |
| **Protokolle überwachen und aufbewahren** | Art. 26 Abs. 5 und 6 | Nicht nur speichern — auswerten, um systematische Benachteiligung zu erkennen. Aufbewahrung mindestens sechs Monate | **keine** |
| **Unterrichtung der Arbeitnehmervertretung** | Art. 26 Abs. **7** (nicht 11) | Vor Inbetriebnahme am Arbeitsplatz. Fällt bei GeAT mit § 87 BetrVG zusammen und ist über T2 abgedeckt | über Stufe 1 |
| **Information der betroffenen Personen** | Art. 26 Abs. **11** | Bewerber müssen erfahren, dass ein Hochrisikosystem an der Entscheidung mitwirkt. **41.000 Menschen im Bestand, keine Maßnahme im Plan** | **keine** |
| **Auskunft über die Einzelentscheidung** | Art. 86 | Ein abgelehnter Bewerber kann eine klare Erläuterung der Rolle des Systems verlangen. Das Review hat diese Pflicht nicht genannt; sie ist die praktisch teuerste, weil sie einzelfallbezogen ist | **keine** |
| **Datenschutz-Folgenabschätzung** | Art. 35 DSGVO, verknüpft über Art. 26 Abs. 9 | Bei Art.-9-Daten und Profilbildung im Beschäftigungskontext praktisch zwingend | **keine** |
| ~~Grundrechte-Folgenabschätzung~~ | ~~Art. 27~~ | **Trägt für GeAT nicht** — die Pflicht gilt für öffentliche Stellen, Erbringer öffentlicher Dienste und Annex III Nr. 5 b/c. GeAT fällt unter Nr. 4 | entfällt |

**Und der Termin, den weder Fassung 1 noch das Review genannt hat:** Nach dem Anwendungszeitplan der Verordnung gelten die Pflichten für Hochrisikosysteme nach **Annex III seit dem 2. August 2026** (`Rechtshypothese`, zu verifizieren). Diese Analyse datiert vom 7. September 2026. **Es gibt keine Übergangsfrist mehr, in die ein Pilotstart in Q2/2027 fallen könnte.** Wer bis dahin plant, plant im geltenden Recht, nicht davor.

**Die Kostenfolge, wörtlich von Marnitz:**

> *„Ich habe Ihre Kostenaufstellung durchgesehen: zweihundertvierzigtausend Euro über fünf Stufen. Keine dieser sieben Pflichten hat dort eine eigene Zeile. […] Und der Puffer, den Sie ausweisen — vierzigtausend —, ist die Größenordnung, in der eine Konformitätsbewertung allein liegen kann. Das ist die Zahl, die Sie in der Versammlung brauchen und nicht haben."*

Ich beziffere die Pflichten hier **nicht**, weil ich es nicht kann und eine erfundene Zahl schlechter ist als eine benannte Lücke. Was ich beziffern kann, steht in [Abschnitt 3](#3-die-budgetwahrheit-185000-statt-280000): Stufe 4 ist schon **ohne** diese Pflichten unterfinanziert.

### 2.2 Die drei Dokumente vor der Ausschreibung

| Dokument | Warum vor der Ausschreibung | Wer |
|---|---|---|
| **1 · Dokumentierte Einstufungsentscheidung** | *„Ihr Papier sagt ‚voraussichtlich Hochrisiko' und lässt es offen. Offen ist keine Einstufung."* Wer die Ausnahme nach Art. 6 Abs. 3 in Anspruch nehmen will, muss die Bewertung **vor** Inbetriebnahme aufgeschrieben haben. Ein menschlicher Klick trägt sie nicht | Marnitz, gegengelesen |
| **2 · Betreiberpflichten mit Namen und Kosten** | Aus [2.1](#21-die-betreiberpflichten-die-in-keiner-kostenzeile-stehen). Nicht als Aufzählung im Risikoteil, sondern als Zeilen in der Kalkulation | Marnitz, Ziegenhorn |
| **3 · Information der 41.000 Betroffenen** | Art. 26 Abs. 11. Und der Zusatz, der die Reihenfolge erzwingt: *„Achtzehntausend dieser Menschen dürfen Sie ohnehin nicht mehr im Bestand haben"* | Marnitz, Kloß |

**Die Vorkehrung gegen mich selbst**, ebenfalls aus dem Gespräch: Marnitz rechnet nach Stunden ab und hat den Interessenkonflikt selbst benannt. Seine Auflösung ist in Fassung 2 übernommen — **2.000 € für eine Zweitmeinung einer zweiten Kanzlei, vor der Ausschreibung.** *„Wenn ich falsch liege, kostet Sie das zweitausend Euro und Sie haben es schriftlich. Wenn ich richtig liege, gehen Sie mit zwei Unterschriften in die Gesellschafterversammlung statt mit einer."* Das ist der billigste Posten des Programms und der einzige, der Dr. Barth einen Einwand vorwegnimmt, statt ihn zu beantworten.

### 2.3 Was in `transformationsvorschlag.md` noch zu streichen ist

Nicht Gegenstand dieser Analyse, aber die Ursache für den Fehler, den das Review hier gesucht und dort gefunden hat. [`transformationsvorschlag.md`](transformationsvorschlag.md) Zeile 126 behauptet, ein Konformitätsmangel berühre die AÜG-Erlaubnis, und nennt das *„das stärkste Argument im Business Case"*. [`vorhaben.md`](vorhaben.md) sagt an derselben Sache ausdrücklich das Gegenteil, und zwar richtig.

**Ersatztext, wie von Marnitz vorgegeben:** Bußgeldrisiko nach DSGVO und AI Act · Untersagungsverfügung gegen das System · Schadensersatz · und ein AGG-Fall, in dem GeAT die Beweislast trägt. *„Das ist genug. Sie brauchen die Erlaubnis nicht dazu."*

Der Vorgang gehört in [`ereignisse.md`](ereignisse.md), nicht still in die Datei.

---

## 3. Die Budgetwahrheit: 185.000 statt 280.000

Fassung 1 hat diese Rechnung in die Tabelle „Offene Punkte" gestellt. Das war zu leise. Sie gehört vor die Matrizen, weil sie eine der beiden Empfehlungen erledigt.

| Position | Betrag | Herkunft |
|---|---:|---|
| Investitionsspielraum zwei Jahre, aus EBIT 0,9 Mio abgeleitet | 900.000 | `Annahme` im Fall |
| **Dieselbe Ableitung bei EBIT 0,805 Mio** | **805.000** | `gerechnet` — die 95.000 € der Stelle Rolle 15 drücken das EBIT |
| Reserviert für die Migration 2027 | − 620.000 | `Annahme` im Fall |
| **Freier Spielraum, korrigiert** | **185.000** | `gerechnet` |
| | | |
| Stufe 1 · Regelwerk und freigegebener Zugang | 22.000 | `generiert` |
| Stufe 2 · Quellenkennung und Anzeigenwirkung | 30.000 | `generiert` |
| Stufe 3 · Datenfundament, **nach 3c vor 3b** | **86.000** | 110.000 − 24.000, siehe unten |
| Stufe 5 · Zielkonflikt und Organisation | 18.000 | `generiert` |
| **Neu:** Zweitmeinung zweite Kanzlei | 2.000 | aus `Gespraeche/03` |
| **Zwischensumme unverzichtbare Vorleistungen** | **158.000** | `gerechnet` |
| **Bleibt für Stufe 4** | **27.000** | `gerechnet` |
| Stufe 4 veranschlagt | 60.000 | `generiert` |
| Die sieben Betreiberpflichten aus [2.1](#21-die-betreiberpflichten-die-in-keiner-kostenzeile-stehen) | **nicht beziffert** | Lücke, keine Schätzung |
| **Unterdeckung, mindestens** | **33.000** | `gerechnet` — real höher |

**Die eine Einsparung, bei der Sorgfalt billiger ist.** Marnitz hat in Woche 2.4 gefragt, in welcher Reihenfolge 3b (Extraktion aus 41.000 Lebenslauf-PDFs, 55.000 €) und 3c (Löschung der 18.000 überfälligen Profile, 12.000 €) laufen. Im Transformationsvorschlag laufen beide von Monat 3 bis 10, also parallel. Die Folge, wenn 3b zuerst fertig ist: *„Sie haben die unzulässige Verarbeitung dann nicht geerbt. Sie haben sie ausgeweitet, mit Budget und Beschluss."* Bei **3c vor 3b** wird aus 23.000 statt 41.000 Dateien extrahiert — *„es spart Ihnen gut vierundzwanzigtausend Euro von den fünfundfünfzig."* Diese Korrektur ist in der Tabelle oben eingerechnet und sonst nirgends.

**Die Konsequenz für Teil B, und sie ist hart:** Bei 27.000 € Rest ist ein Assistent für 60.000 € nicht finanzierbar — **egal welcher Anbieter gewinnt.** Damit ist die Frage in Teil B nicht mehr „welches Produkt", sondern „welche Konstruktion passt in 27.000 €". Genau das ist der Grund, warum Option F in [Abschnitt 7](#7-matrix-b-revidiert-sechs-optionen) nicht nur methodisch, sondern auch finanziell gewinnt.

**Drei Wege, die Unterdeckung zu schließen — alle drei gehören der Geschäftsführung, nicht mir:**

1. **Stufe 2 refinanziert sich lassen und den Ertrag reinvestieren.** Zehn Prozent besser allokiertes Anzeigenbudget sind 48.000 € im Jahr. Braucht eine Zusage, dass der Ertrag im Vorhaben bleibt, und zwei vollständige Quartale Nachweis.
2. **Den Investitionsspielraum bei 900.000 € halten und begründen.** Das ist die Entscheidung, die [`ereignisse.md`](ereignisse.md) für Woche 6 oder 7 vorsieht. Sie ist vertretbar, aber sie ist eine Entscheidung und keine Rechnung.
3. **Stufe 4 auf die Konstruktion zuschneiden, die in 27.000 € passt.** Das ist Option F, und es ist der einzige der drei Wege, den ich ohne fremde Zusage gehen kann.

---

## 4. Teil A — Stufe 1: der freigegebene Zugang

### 4.1 Kontext, unverändert bis auf zwei Zeilen

Die zehn Kontextzeilen aus Fassung 1 gelten weiter ([`KI_Analyse.md`](KI_Analyse.md), 4.1). Zwei kommen hinzu:

| Nr | Neue Kontextzeile | Herkunft |
|---:|---|---|
| 11 | **Welche M365-Pläne GeAT seit 2020 lizenziert hat, steht nirgends.** Copilot setzt eine qualifizierende Basislizenz voraus. Ohne diese Prüfung ist jede Copilot-Kostenzahl unbelegt | Lücke, aus dem Review |
| 12 | **Zwanzig Lizenzen nur für Erfurt sind ein politischer Preis.** Rehberg (Macht 4, informeller Einfluss sehr hoch, hat vier von sechs Niederlassungsleitungen eingearbeitet) sieht dann, dass die Zentrale ein Werkzeug bekommt und Gotha nicht — und Stufe 5 braucht ihn als Pilotstandort | `Einschätzung`, aus dem Review |

### 4.2 Gewichtung A, revidiert

**Fixiert 2026-09-07. Änderungen gegenüber Fassung 1 mit Grund ausgewiesen — nicht still verschoben.**

| Nr | Kriterium | Gewicht | (F1) | Änderung und Grund |
|---:|---|---:|---:|---|
| K1 | Compliance und AVV | 25 % | 25 % | unverändert |
| K2 | Verfügbarkeit gegen die Taktgrenze | 20 % | 20 % | unverändert |
| K3 | Adoptionspfad, **Einführungsaufwand** und Support | **17 %** | 15 % | **Umbenannt und erhöht.** Fassung 1 hat den Einführungsaufwand nur bei Copilot gesehen (SharePoint) und bei Option A nicht (neuer Lieferant, AVV, SSO, Nutzerverwaltung, Schulung) |
| K4 | Kosten über drei Jahre | 15 % | 15 % | unverändert, aber symmetrisch gerechnet |
| K5 | Betriebsaufwand bei 1,5 IT-Stellen | **11 %** | 10 % | +1, aus dem freigewordenen MCP-Gewicht |
| K6 | **Exit und Portabilität** (ohne MCP) | **6 %** | 10 % | **MCP herausgenommen.** Wer soll bei zwei IT-Personen ohne Entwicklungsauftrag einen MCP-Server bauen und betreiben? Portabilität bleibt: Datenexport, Modellwechsel, Vertragsende |
| K7 | RAG und Integrationstiefe | **4 %** | 3 % | +1, aus dem MCP-Gewicht |
| K8 | Deployment-Flexibilität | 2 % | 2 % | unverändert — bei 69 Seats ist SaaS EU die einzige verfügbare Option, das Kriterium trennt nicht |
| | **Summe** | **100 %** | | |

### 4.3 Die Kostenzeile, jetzt symmetrisch

**Alle Preise Listenwerte nach meinem Kenntnisstand, prüfpflichtig, kein Angebot liegt vor.**

| Option | 20 Seats/Jahr | 69 Seats/Jahr | 20 Seats über 3 Jahre | Vorleistung, nicht in der Lizenz |
|---|---:|---:|---:|---|
| **A** EU-Plattform | 4.800 – 7.200 € | 16.560 – 24.840 € | 14.400 – 21.600 € | **Neuer Lieferant:** AVV, SSO, Nutzerverwaltung über sechs Standorte, Schulung auf eine neue Oberfläche. Bausteine aus Hübners Prompt-Sammlung (2.000 € in Stufe 1) |
| **B** M365 Copilot | **7.200 €** | 24.840 € | 21.600 € | Berechtigungsstruktur in SharePoint prüfen und eingrenzen, Aufwand unbeziffert. **Basislizenz ungeprüft** |
| **C** Cloud-ML | Verbrauch, gering | Verbrauch, gering | — | Oberfläche, Authentifizierung, Protokollierung, Betrieb — der bestimmende Posten, ohne Angebot nicht nennbar |
| **D** Branchensoftware 2027 | nicht separat | nicht separat | — | Verhandlungsaufwand, solange die Ausschreibung offen ist. Danach Change Request |
| **E** Nullvariante | 0 € | 0 € | 0 € | Kontrollaufwand plus DSB-Stunden. Risiko der laufenden Verarbeitung nicht bezifferbar |

**Die Korrektur, die das Review erzwungen hat:** **20 Seats Copilot kosten 7.200 € im Jahr und passen unter den Stufe-1-Ansatz von 9.000 €.** Fassung 1 hat den 69-Seat-Fall nach vorn gestellt und damit einen Kostennachteil erzeugt, der bei dem Zuschnitt, den ich selbst empfehle, nicht existiert. K4 bei Copilot steigt deshalb von 2 auf 3.

**Was bestehen bleibt, weil es unabhängig davon gilt:** 69 Seats Copilot kosten 24.840 € im Jahr — 160 € unter der Freigabegrenze der Geschäftsführung, über drei Jahre 74.520 €. **Die Grenze gilt für die Maßnahme, nicht für die Jahresrate.** Wer in Jahresraten vorlegt, umgeht das Gremium. Das steht hier, weil es vorgeschlagen wird, nicht weil ich es vorschlage.

---

## 5. Matrix A, revidiert

| Kriterium | Gewicht | A · EU-Plattform | B · Copilot | C · Cloud-ML | D · Branchensw. 2027 | E · Nullvariante |
|---|---:|---:|---:|---:|---:|---:|
| K1 Compliance und AVV | 25 % | **4** → 1,00 | 3 → 0,75 | 3 → 0,75 | 2 → 0,50 | 2 → 0,50 |
| K2 Verfügbarkeit gegen die Taktgrenze | 20 % | **4** → 0,80 | 3 → 0,60 | 1 → 0,20 | 1 → 0,20 | 2 → 0,40 |
| K3 Adoption, Einführungsaufwand, Support | 17 % | 2 → 0,34 *(F1: 3)* | **4** → 0,68 | 1 → 0,17 | 3 → 0,51 | 2 → 0,34 |
| K4 Kosten über drei Jahre | 15 % | 3 → 0,45 | 3 → 0,45 *(F1: 2)* | 1 → 0,15 | 3 → 0,45 *(F1: 4)* | 3 → 0,45 |
| K5 Betriebsaufwand bei 1,5 IT-Stellen | 11 % | **4** → 0,44 | 3 → 0,33 | 1 → 0,11 | **4** → 0,44 | 3 → 0,33 |
| K6 Exit und Portabilität | 6 % | **4** → 0,24 | 2 → 0,12 | 3 → 0,18 | 1 → 0,06 | **4** → 0,24 |
| K7 RAG und Integrationstiefe | 4 % | **4** → 0,16 | 3 → 0,12 | **4** → 0,16 | 3 → 0,12 *(F1: 4)* | 1 → 0,04 |
| K8 Deployment-Flexibilität | 2 % | 3 → 0,06 | 2 → 0,04 | 3 → 0,06 | 2 → 0,04 | 1 → 0,02 |
| **Gesamtscore A** | **100 %** | **3,49** | **3,09** | **1,78** | **2,32** | **2,32** |
| *Fassung 1* | | *3,68* | *2,88* | *1,83* | *2,41* | *2,40* |
| *unabhängig belegt?* | | *nein* | *teilweise* | *teilweise* | *nein* | *entfällt* |

**Der Sieger bleibt, der Abstand halbiert sich: 0,40 statt 0,80.** Das ist die redliche Wirkung der berechtigten Review-Punkte, und sie gehört so vorgelegt. Copilot ist die zweitbeste Option und deutlich näher dran, als Fassung 1 behauptet hat.

**Warum Option A trotzdem gewinnt — vier Zellen, alle aus dem Kontext, keine aus einer Broschüre:**

1. **K1, Compliance (25 %).** Modellagnostische EU-Plattformen bieten AVV und EU-Verarbeitung als Standardangebot mit öffentlicher Dokumentation. Copilot bleibt bei 3, weil seine Compliance nicht im Vertrag entschieden wird — der liegt vor und ist ein echter Vorteil —, sondern in einer Berechtigungsstruktur, die bei GeAT ungeprüft ist. Das ist „mit Aufwand herstellbar", nicht „erfüllt".
2. **K2, Verfügbarkeit (20 %).** Beide sind schnell. A ist schneller, weil bei Copilot die Berechtigungsprüfung davorliegt und die Basislizenz ungeklärt ist.
3. **K5 und K6 zusammen (17 %).** A hängt nicht am Kernsystem, das in Q1/2027 ersetzt wird, und erzeugt keinen Betrieb im Haus. Copilot bringt Ecosystem-Bindung über Graph mit — kein prinzipielles Problem, aber sechs Monate vor einem Kernsystemwechsel die falsche Richtung.
4. **Was A verliert und Fassung 1 verschwiegen hat: K3 mit 2.** Ein neuer Lieferant, eine neue Oberfläche, eine neue Nutzerverwaltung über sechs Standorte — in einem Haus, dessen letztes Werkzeug bei 34 % Nutzung liegt. **Das ist die teuerste Zelle der Empfehlung, und sie ist der Grund, warum der Zuschnitt und das Abbruchkriterium in [10.1](#empfehlung-1--jetzt-integrierte-eu-plattform-20-seats-über-drei-standorte) zur Empfehlung gehören und nicht als Beiwerk.**

**D und E liegen erneut gleich, jetzt bei 2,32.** Der Score kann sie nicht trennen, und das ist keine Schwäche der Matrix, sondern ihr Befund: die eine Option ist inhaltlich stark und terminlich unmöglich, die andere terminlich sofort und wirkungslos. Was sie trennt, steht in Stufe 1 des Transformationsvorschlags: *ein Verbot ohne Ersatz — die Nutzung wandert zurück und wird nur unsichtbarer.*

**Option F kommt in Matrix A nicht vor**, weil sie eine Konstruktion für die Besetzungsvorbereitung ist und kein Werkzeug für Anzeigentexte. Sie wäre hier ein Kategorienfehler.

---

## 6. Teil B — Stufe 4, mit der sechsten Option

### 6.1 Was sich am Kontext ändert

| | Stufe 1 | Stufe 4 |
|---|---|---|
| Gegenstand | Anzeigentexte, Profilzusammenfassungen | Besetzungsvorschlag: drei bis fünf Kandidaten mit Begründung |
| Einstufung | kein Bewerberauswahlsystem | **Annex III Nr. 4, voraussichtlich Hochrisiko — seit 2. August 2026 im Anwendungsbereich** (`Rechtshypothese`) |
| Datenzugang | Mensch fügt den Lebenslauf ein | System durchsucht Bestand standortübergreifend |
| Budget | 9.000 € im Ansatz | **27.000 € verfügbar, 60.000 € veranschlagt** ([Abschnitt 3](#3-die-budgetwahrheit-185000-statt-280000)) |
| Voraussetzung | keine | Stufe 1 bis 3 gelaufen, **3c vor 3b**, Betriebsvereinbarung unterzeichnet, Migration abgeschlossen |

**Die Regel, die Teil B entscheidet** (`Rechtshypothese`): Nach Art. 25 Abs. 1 wird ein Betreiber zum **Anbieter**, wenn er ein Hochrisikosystem unter eigenem Namen in Verkehr bringt, es wesentlich verändert oder den Zweck eines Systems so ändert, dass es hochriskant wird. Baut GeAT auf einer generischen Plattform ein Auswahlsystem, trägt GeAT Anbieterpflichten — bei 69 Stammkräften und 1,5 IT-Stellen ist das der Unterschied zwischen machbar und nicht machbar.

Fassung 1 hat daraus geschlossen, dass eine Produktfunktion des Kernsystemanbieters die Lösung sei. **Marnitz hat diesen Schluss vorweg widerlegt** ([0.3](#03-was-das-review-nicht-gesehen-hat--und-was-das-ergebnis-dreht)): Der Markt schiebt die Rechtmäßigkeit der Nutzung per AGB an den Kunden zurück. Die Anbieterpflicht ist eine Erwartung, kein Befund.

### 6.2 Option F — die Konstruktion, die Fassung 1 nicht hatte

> **Regelbasierter Filter über strukturierte Felder, Sprachmodell nur zur Formulierung.**
>
> Die Auswahl läuft über dokumentierte, reproduzierbare Kriterien: Qualifikation, Gültigkeit des Nachweises, Verfügbarkeit, Entfernung. Der Disponent sieht die Trefferliste **und die Filterbedingung, die sie erzeugt hat**. Das Sprachmodell formuliert anschließend das Kandidatenprofil für die Kundenunterlage aus einem Lebenslauf, den ein Mensch ausgewählt hat. **Es rangiert nicht, es bewertet nicht, es lehnt nicht ab.**

Vier Eigenschaften, die keine der fünf anderen Optionen hat:

| Eigenschaft | Warum sie zählt |
|---|---|
| **Die Auswahl ist voraussichtlich kein KI-System** | Ein deterministischer Filter über strukturierte Felder trifft keine Inferenz und passt sich nicht an. Damit ist der Auswahlschritt voraussichtlich nicht vom AI Act erfasst, und der Formulierungsschritt ist KI, aber kein Auswahlsystem. **Stärkster Kandidat für Art. 6 Abs. 3** (`Rechtshypothese`, Dokument 1 aus [2.2](#22-die-drei-dokumente-vor-der-ausschreibung)) |
| **Sie ist dem Bewerber erklärbar** | Marnitz wörtlich: *„das können Sie einem Bewerber erklären und einer Aufsicht vorlegen."* Damit ist Art. 86 nicht ein Kostenrisiko je Einzelfall, sondern eine Standardauskunft |
| **Ihr Kostentreiber ist schon bezahlt** | Sie braucht genau die Felder, die Stufe 3a und 3d erzeugen — Qualifikationskatalog, Pflichtfelder, Gültigkeitsdatum, Nichtbesetzungsgrund. Sie braucht **keinen** Textindex, **keine** OCR über 41.000 Scans, **keine** Vektorisierung |
| **Sie wächst mit dem Datenfundament** | Heute trägt sie 37 % des Bestands, nach Stufe 3 zwischen 70 und 80 %. Alle anderen Optionen setzen das Datenfundament voraus; diese eine baut darauf auf, während es entsteht |

**Die Grenze, die dazugehört, und sie ist die Pointe des ganzen Falls.** Marnitz:

> *„Das ist ein deutlich kleineres System als das, was ich beantragt habe." — „Ja. Und es ist auch das, was Ihre eigene Datenlage erlaubt. Sie schreiben, 63 Prozent der Profile haben kein strukturiertes Können. Das heißt: Ihre nachvollziehbare Variante findet heute in 37 Prozent des Bestands. Das ist der wahre Grund, warum Sie die andere wollen — nicht Geschwindigkeit, sondern weil sie den Datenmangel überspielt."*

Ein Sprachmodell über 41.000 Freitext-PDFs ist nicht die leistungsfähigere Lösung. Es ist die, die den Datenmangel unsichtbar macht — und genau dadurch aus einem Werkzeugprojekt ein Konformitätsproblem.

**Was Option F kostet, sage ich nicht**, weil ich es nicht seriös kann: eine Abfrage über bestehende Felder plus ein Formulierungsschritt, ohne Angebot nicht bezifferbar. Was ich sagen kann: ihr Kostentreiber liegt in Stufe 3 und ist bereits in den 86.000 € enthalten. Sie ist damit die einzige der sechs Optionen, bei der 27.000 € Rest nicht von vornherein zu wenig sind.

### 6.3 Gewichtung B, revidiert

| Nr | Kriterium | Gewicht | (F1) | Änderung und Grund |
|---:|---|---:|---:|---|
| **L0** | **Wirkung auf die Leitkennzahl** — gesendete Profile je Besetzung 4,8 → 3,2, nachgelagert Besetzungsquote 40 → 45 % | **20 %** | — | **Neu, auf Anstoß des Reviews, mit korrigierter Kennzahl.** Nicht Besetzungsdauer: von 11 Tagen sind 0,4 Tage Arbeit, 96 % sind Warteschleifen, die kein Werkzeug anfasst |
| L1 | AI-Act-Betreiberfähigkeit und **Einstufungsrisiko** | **25 %** | 30 % | Erweitert um die Einstufungsfrage, Gewicht zugunsten von L0 gesenkt |
| L2 | Zugang zu den Bewerberdaten **und deren Verwertbarkeit** | **18 %** | 25 % | Umbenannt: „im System liegen" ist kein Zugang, solange 63 % unstrukturiert sind und Scans keine Texterkennung haben |
| L3 | Nachvollziehbarkeit und wirksame menschliche Aufsicht | **17 %** | 20 % | unverändert im Inhalt |
| L4 | Kosten über drei Jahre, **gegen 27.000 € Rest** | **10 %** | 10 % | Bezugsgröße korrigiert |
| L5 | Betriebsaufwand bei 1,5 IT-Stellen | **6 %** | 8 % | — |
| L6 | **Exit und Portabilität** (ohne MCP) | **4 %** | 5 % | MCP herausgenommen, siehe K6 |
| — | Adoption und Support | **0 %** | 2 % | Entfällt. Sechs Disponenten und vier Recruiter, handverlesen, Rehberg als eingekaufter Pilotstandort — **Adoption wird organisatorisch bezahlt (Stufe 5), nicht beim Anbieter gekauft** |
| | **Summe** | **100 %** | | |

---

## 7. Matrix B, revidiert: sechs Optionen

| Kriterium | Gew. | A · EU-Plattf. | B · Copilot | C · Cloud-ML | D · Branchensw. | E · Nullvar. | **F · Regelfilter** |
|---|---:|---:|---:|---:|---:|---:|---:|
| L0 Wirkung auf die Leitkennzahl | 20 % | 3 → 0,60 | 1 → 0,20 | 3 → 0,60 | 2 → 0,40 | 1 → 0,20 | **3** → 0,60 |
| L1 Betreiberfähigkeit, Einstufungsrisiko | 25 % | 2 → 0,50 | 2 → 0,50 | 2 → 0,50 | 2 → 0,50 *(F1: 4)* | **4** → 1,00 | **4** → 1,00 |
| L2 Datenzugang und Verwertbarkeit | 18 % | 2 → 0,36 | 1 → 0,18 | 2 → 0,36 | 3 → 0,54 *(F1: 4)* | 1 → 0,18 | 3 → 0,54 |
| L3 Nachvollziehbarkeit, Aufsicht | 17 % | 3 → 0,51 | 2 → 0,34 | **4** → 0,68 | 2 → 0,34 | **4** → 0,68 | **4** → 0,68 |
| L4 Kosten gegen 27.000 € | 10 % | 3 → 0,30 | 2 → 0,20 | 1 → 0,10 | 3 → 0,30 *(F1: 4)* | **4** → 0,40 | **4** → 0,40 |
| L5 Betriebsaufwand | 6 % | 3 → 0,18 | 3 → 0,18 | 1 → 0,06 | **4** → 0,24 | **4** → 0,24 | 3 → 0,18 |
| L6 Exit und Portabilität | 4 % | **4** → 0,16 | 2 → 0,08 | 3 → 0,12 | 1 → 0,04 | **4** → 0,16 | **4** → 0,16 |
| **Gesamtscore B** | **100 %** | **2,61** | **1,68** | **2,42** | **2,36** | **2,86** | **3,56** |
| *Fassung 1* | | *2,50* | *1,87* | *2,50* | ***3,43*** | *3,25* | *— nicht enthalten* |

### 7.1 Der Sieger wechselt zum zweiten Mal — und diesmal ist es kein Produkt

| Option | Score A | Score B | Fassung 1 B | Bewegung |
|---|---:|---:|---:|---|
| **F** Regelfilter + Formulierung | *(entfällt)* | **3,56** · Platz 1 | *nicht enthalten* | **neu** |
| **E** Nullvariante | 2,32 | 2,86 · Platz 2 | 3,25 · Platz 2 | −0,39 durch L0 |
| **A** EU-Plattform | **3,49** · Platz 1 | 2,61 · Platz 3 | 2,50 · Platz 3 | +0,11 |
| **C** Cloud-ML | 1,78 | 2,42 · Platz 4 | 2,50 · Platz 3 | −0,08 |
| **D** Branchensoftware 2027 | 2,32 | 2,36 · Platz 5 | **3,43** · Platz 1 | **−1,07 — von Platz 1 auf Platz 5** |
| **B** Copilot | 3,09 · Platz 2 | 1,68 · Platz 6 | 1,87 · Platz 5 | −0,19 |

**Vier Befunde, in der Reihenfolge ihrer Tragweite:**

**Erstens: Option D stürzt von Platz 1 auf Platz 5, und der Sturz ist selbstverschuldet.** Nicht das Review hat sie erledigt, sondern der eigene Anker plus ein Satz aus dem eigenen Fall. L1 von 4 auf 2, weil der Markt Anbieterpflichten per AGB zurückschiebt. L2 von 4 auf 3, weil „im System liegen" bei 63 % unstrukturierten Profilen kein Zugang ist. L4 von 4 auf 3, weil Grenzkosten in einer nicht geführten Verhandlung keine Kosten sind. **Fassung 1 hat in Abschnitt 10.3 selbst notiert, dass dies „die schwächste Zelle der ganzen Analyse" sei — und sie trotzdem gewinnen lassen. Das ist der Fehler, den diese Fassung korrigiert.**

**Zweitens: Option F gewinnt mit 3,56 und dem größten Abstand beider Matrizen (0,70).** Sie ist die einzige Option, die alle vier Engpässe des Falls gleichzeitig trifft: das Einstufungsrisiko (L1 = 4, weil der Auswahlschritt voraussichtlich kein KI-System ist), die Nachvollziehbarkeit (L3 = 4, weil ein Filter reproduzierbar und erklärbar ist), die Budgetgrenze (L4 = 4, weil ihr Kostentreiber in Stufe 3 liegt) und die Datenlage (L2 = 3, weil sie strukturierte Felder braucht statt eines Textindex). Sie ist gleichzeitig **die kleinste** — und das ist keine Einschränkung, sondern die Antwort auf die Frage, die Fassung 1 nicht gestellt hat: nicht „welches Werkzeug ist am stärksten", sondern „welche Konstruktion erlaubt unsere Datenlage".

**Drittens: das Nullvarianten-Paradoxon ist aufgelöst, ohne es zu unterdrücken.** Mit L0 fällt E von 3,25 auf 2,86 und von Platz 2 auf Platz 2 — **es bleibt zweitbeste Option.** Das ist der ehrliche Befund und das Gegenteil einer Panne: **Nichts zu bauen ist besser als jedes der vier KI-Produkte.** Nur die Konstruktion, die auf Nachvollziehbarkeit statt auf Modellstärke setzt, schlägt sie. Ein Entscheidungsgremium, dem man das nicht zeigt, kann die Empfehlung nicht prüfen.

**Viertens: A und C sind nicht mehr gleich, aber weiter dicht beieinander** (2,61 zu 2,42), auf verschiedenen Wegen. C ist bei L3 die stärkste Option von allen — volle Kontrolle über die Rangfolgelogik und damit der einzige Weg, den Bias-Fall zu **messen** statt zu behaupten — und scheitert an Kapazität und Kosten, nicht an Funktion. Das gehört gesagt, damit der Ausschluss nicht als Vorurteil gelesen wird.

---

## 8. Was kein Score misst

Unverändert gültig aus Fassung 1, um zwei Punkte ergänzt.

**8.1 Haftung ist keine Plattformeigenschaft.** *Moffatt v. Air Canada*, 19.02.2024: das Unternehmen haftet für die Auskünfte auf seiner Website, unabhängig davon, welches System sie erzeugt. Bei GeAT ist **das Kandidatenprofil, das an den Kundenbetrieb geht, die Auskunft** — rund 6.000 im Jahr. Folge: Protokollierung jedes freigegebenen Profils und ein Rückfallpfad ohne Assistent sind Plattformfunktionen, keine Zusatzwünsche. **Ergänzung für Option F:** weil dort ein Mensch den Kandidaten auswählt und die Maschine nur formuliert, ist der Kontrollpunkt eindeutig — die Freigabe. Bei einem rangierenden System ist er es nicht.

**8.2 Kein Kriterium misst Maß.** Klarna 2024: 700 Vollzeitkräfte ersetzt, Lösungszeit von 11 auf unter 2 Minuten; 2025 korrigiert der CEO, die Servicequalität habe gelitten. Bei GeAT hat das einen Namen: Regina Pfaff, 59, kennt in 40 Kundenbetrieben die Meister mit Vornamen. Wenn der Assistent trägt und die Zahlen stimmen, geht 2030 mit ihr das Wissen, aus dem er gelernt hat — und niemand merkt es, weil die Kennzahlen gut aussehen.

**8.3 Neu: die klügste Regel wird die erste sein, die verloren geht.** Marnitz zur Bias-Regel („keine Optimierung auf Erfolgswahrscheinlichkeit"):

> *„Das ist die klügste Entscheidung in dem ganzen Papier und sie wird die erste sein, die Sie verlieren. […] Jemand wird sagen: Wir haben die Daten jetzt, wir wissen, welche Besetzungen gehalten haben, warum nutzen wir das nicht. Und dann wird die Regel gestrichen, in einem Änderungsantrag, ohne dass ich gefragt werde. **Schreiben Sie die Regel in die Betriebsvereinbarung, nicht in Ihr Konzept. Ihr Konzept kann ein Nachfolger ändern. Die Betriebsvereinbarung nicht, ohne Frau Nowak.**"*

Das ist keine Score-Frage und die wichtigste Einzelmaßnahme dieser Analyse. Sie ist in [10.1](#empfehlung-1--jetzt-integrierte-eu-plattform-20-seats-über-drei-standorte) als Bedingung von Stufe 1 aufgenommen, nicht als Absicht von Stufe 4.

**8.4 Neu: der Einwand hängt an einer Person, und das ist ein Konstruktionsfehler des Vorhabens.** Marnitz: *„Ich habe genau einen Adressaten für alles, was ich Ihnen heute gesagt habe, und das sind Sie. […] Ein Einwand, der an einer Person hängt, verschwindet mit ihr."* Seine Konsequenz — seine Stellungnahme geht **schriftlich an die Geschäftsführung, mit Kopie an den Betriebsrat**, nicht an mich — ist in Fassung 2 übernommen, obwohl sie meine Steuerungsmöglichkeit verringert. *„Sie hat noch nie zu einem besseren Ergebnis geführt, nur zu einem glatteren Papier."*

**8.5 Alle Belege sind Herstellerangaben.** Die Zeile *unabhängig belegt?* steht bei jeder Spalte auf nein oder teilweise. In die Ausschreibung gehören zwei Referenzkunden im DACH-Raum unter 150 Beschäftigten, davon einer aus der Personaldienstleistung, mit Gesprächserlaubnis.

**8.6 Die Reifegradzahlen sind von 2021** (6/14/42/25/13 %, N = 1.500, vor ChatGPT). Als Muster zitierbar, nicht als Verteilung. Der Ausschluss von Option C stützt sich deshalb auf zwei prüfbare Befunde — kein Data-Science-Team, 1,5 IT-Stellen und beide durch die Migration gebunden —, nicht auf die Tabelle. Und: **der GeAT-Reifegrad 2,2 ist selbst eine unvalidierte Gruppeneinschätzung.**

---

## 9. Gegenargumente und Risiken

**9.1 Achtelik (Macht 4): „Keine zweite Baustelle vor dem Umstieg."** Berechtigt, und Fassung 2 gibt ihm mehr Recht als Fassung 1. Stufe 1 mit 20 Seats bindet Nutzerverwaltung, keine Betriebskapazität — **konkret zugesagt: maximal 10 Arbeitsstunden von Balzer für die Benutzeranlage.** Empfehlung 2 ist auf drei Anforderungen reduziert, damit sie in eine laufende Endverhandlung passt statt sie aufzuhalten. **Wo er weiter Recht hat:** wenn die Plattform doch 69 Seats bekommt, ist Nutzerverwaltung über sechs Standorte kein Nebenbei. Das ist ein Grund für den Zuschnitt.

**9.2 Marnitz: „Offen ist keine Einstufung."** Der Einwand, an dem Fassung 1 vorbeigeschrieben hat. Er ist nicht durch ein Gewicht zu beantworten, sondern durch Dokument 1 aus [2.2](#22-die-drei-dokumente-vor-der-ausschreibung) — und Option F ist die einzige Konstruktion, bei der die Einstufung nicht „voraussichtlich Hochrisiko mit Ausnahmeprüfung" lautet, sondern eine begründbare Position hat.

**9.3 Dr. Barth (Macht 5): „Amortisation unter 24 Monaten."** Fassung 2 weicht nicht aus und liefert zusätzlich die Zahl, die Fassung 1 nicht hatte: **Stufe 1 amortisiert sich nicht.** Sie beendet eine Verarbeitung ohne Rechtsgrundlage; vermiedenes Risiko ist keine Zahl, die ich seriös nenne. Die Amortisation kommt aus Stufe 2 (48.000 €/Jahr bei zehn Prozent besserer Allokation von 480.000 €). **Und der Punkt, der jetzt dazugehört:** Barth wird die 185.000 € finden. Es ist besser, sie stehen in Abschnitt 3 meiner Vorlage als in ihrer ersten Frage.

**9.4 Vollmer (Macht 5): „Ich habe 2023 schon einmal für ein Modul bezahlt, das keiner benutzt."** Der Einwand mit dem meisten Gewicht. Die Antwort ist der Zuschnitt plus zwei Vorkehrungen, die Fassung 1 nicht hatte: eine **Qualitätsschwelle** für den freigegebenen Zugang (siehe 9.5) und ein **wirkungsbezogenes** Abbruchkriterium statt eines Nutzungszählers.

**9.5 Neu, aus dem Review: der Rebound-Effekt bei den neun Schatten-Nutzern.** Berechtigt und die schärfste organisatorische Kritik. Die neun nutzen private Konten, weil sie schnell, unreglementiert und auf aktuellem Modellstand sind. Ein reglementierter Ersatz mit schwächeren Modellen führt nicht zur Adoption, sondern in die Unsichtbarkeit — genau der Scheiterungsgrund, der in Stufe 1 des Transformationsvorschlags steht. **Zwei Konsequenzen:**
- **Qualitätsschwelle als Vergabebedingung:** Der freigegebene Zugang muss jederzeit Modelle auf dem Stand der öffentlich verfügbaren Spitzenmodelle anbieten. Genau das ist der Grund, warum Modellagnostik bei Option A kein Komfort ist, sondern die Voraussetzung dafür, dass Stufe 1 funktioniert.
- **Das Abbruchkriterium aus Fassung 1 war falsch konstruiert.** „Nach drei Monaten weniger als 15 von 20 Seats wöchentlich aktiv → nicht verlängern" macht die Nutzungsquote zur Selbstabschuss-Klausel und misst das Falsche. Ersetzt in [10.1](#empfehlung-1--jetzt-integrierte-eu-plattform-20-seats-über-drei-standorte).

**9.6 Neu, aus dem Review: Rehberg wird in Stufe 1 verspielt.** Berechtigt. Zwanzig Lizenzen für Erfurt, während Gotha zusieht, macht aus dem Vorhaben ein Erfurter Projekt — bei einem Niederlassungsleiter mit Macht 4, den besten Zahlen im Haus und vier von sechs eingearbeiteten Kollegen. **Konsequenz:** die 20 Seats verteilen sich über drei Standorte, Gotha inbegriffen, und Rehberg ist in Stufe 1 Nutznießer, bevor er in Stufe 5 Pilotstandort werden soll.

**9.7 Neu, aus dem Review: Ritschel und der Papier-Stundenzettel.** Berechtigt als politischer Befund, nicht als Analysefehler. 22 % Nachkorrekturen, vier Tage Klärung im Monat, rund 17.700 € — größer als mehrere Positionen des Vorschlags, und kein KI-Fall. Fassung 1 hat es in einer Tabellenzeile erwähnt. **Fassung 2 macht daraus eine der drei Migrationsanforderungen**, weil es die einzige ist, die Achtelik und die Niederlassungsleitungen gleichzeitig gewinnt. Wer zehntausende Euro für Textgeneratoren fordert, während die Abrechnung auf Papier läuft, verliert das Mandat als Problemlöser.

**9.8 Der Einwand, der stimmt und den ich nicht beantworten kann — jetzt schärfer.** Fassung 1 hat gefragt, ob die Migrationsausschreibung noch offen ist. Das Review hat die Antwort wahrscheinlich gemacht: **bei einem Go-Live in Q1/2027 sind die Verträge im September 2026 geschlossen oder in der juristischen Endabstimmung.** Damit ist Empfehlung 2 keine Verhandlung, sondern eine Bitte — und Option D war in Fassung 1 nicht nur falsch gescort, sondern terminlich schon tot. **Die Frage an Achtelik bleibt und ist diese Woche zu stellen. Die Empfehlung ist so gebaut, dass sie auch bei der Antwort „zu" trägt** — weil Option F keinen Anbieter braucht, der etwas zusagt, sondern strukturierte Felder, die GeAT selbst erzeugt.

---

## 10. Die Empfehlung

Drei Entscheidungen, unterschiedliche Sieger, ein Termin dazwischen. **Geändert gegenüber Fassung 1: Empfehlung 2 ist kleiner, Empfehlung 3 ist neu und ersetzt die dortige Kür von Option D.**

### Empfehlung 1 · Jetzt: integrierte EU-Plattform, 20 Seats über drei Standorte

**Geschäftsführungsbeschluss, ≤ 9.000 € im Jahr, unter der 25.000-Euro-Grenze — verliert kein Quartal.**

| Was | Wert |
|---|---|
| Option | **A** · integrierte EU-Plattform, Multi-Tenant SaaS, **modellagnostisch** |
| Score A | **3,49** — vor Copilot mit 3,09 |
| **Zuschnitt, geändert** | 20 Seats über **drei** Standorte: Recruiting Center Erfurt (9), **Gotha (4)**, übrige Niederlassungen und Innendienst (7). Beginnend mit den neun heutigen Schatten-Nutzern |
| Verantwortlich | Balzer (IT, **max. 10 Stunden**), Kloß (Fachseite) |
| **Vergabebedingung, neu** | Modelle jederzeit auf dem Stand der öffentlich verfügbaren Spitzenmodelle. Ohne diese Zusage ist der Rebound aus 9.5 vorprogrammiert |
| Tore vor Vertragsschluss | T1 AVV vorgelegt · T2 Protokollierung begrenzbar, Betriebsvereinbarung mit Nowak · T3 EU-Verarbeitung und nachweisbare Löschung |
| **In die Betriebsvereinbarung, nicht ins Konzept** | Ausschluss von Leistungs- und Verhaltenskontrolle · Zweckbindung · **und die Bias-Regel: keine Optimierung auf Erfolgswahrscheinlichkeit** (siehe 8.3) |
| **Abbruchkriterium, ersetzt** | Nach drei Monaten: **null Lebensläufe in Diensten ohne AVV**, bestätigt durch die neun Nutzer, und mindestens zwei der drei Standorte in wöchentlicher Nutzung. Gemessen wird die Wirkung, nicht die Sitzplatzauslastung. Wird es verfehlt, wird ausgewertet und nicht verlängert |

**Begründung in drei Sätzen, für das Protokoll.** Sie ist die einzige Option, die den ungeregelten Zustand in Wochen beendet statt in Quartalen. Sie hängt nicht an der Branchensoftware, die in Q1/2027 ersetzt wird. Und ihre Modellagnostik ist nicht ein Feature, sondern die Bedingung dafür, dass die neun Personen sie dem behalten, was sie heute privat nutzen.

**Was Empfehlung 1 kostet und Fassung 1 nicht gesagt hat:** einen neuen Lieferanten, eine neue Oberfläche und eine neue Nutzerverwaltung in einem Haus mit einem dokumentierten Adoptionsfehlschlag. Das ist die 2 bei K3, und sie ist der Grund für Zuschnitt, Qualitätsschwelle und Abbruchkriterium.

### Empfehlung 2 · Diese Woche klären, dann drei Anforderungen — nicht sechs

**Kostet keine Freigabe. Ist terminkritisch. Und ist kleiner als in Fassung 1, weil sie sonst nicht durchgeht.**

**Schritt 1, diese Woche:** Achtelik fragen, wie weit die Ausschreibung ist. Bei Vertragsschluss oder juristischer Endabstimmung entfällt Schritt 2, und Empfehlung 3 trägt alleine.

**Schritt 2, wenn noch offen — drei Anforderungen, keine sechs:**

| Nr | Anforderung | Warum genau diese drei |
|---:|---|---|
| 1 | **Offene REST-API für Bewerber- und Auftragsdaten**, mit Quellenkennung im Rücklauf | Ohne sie ist jede spätere Werkzeugwahl vorentschieden — und Stufe 2 scheitert heute genau daran |
| 2 | **Datenfeldarchitektur im Standard:** Qualifikationskatalog mit einer Schreibweise, Pflichtfelder bei Neuanlage, Gültigkeitsdatum bei Nachweisen, **Nichtbesetzungsgrund** beim Schließen einer Anfrage | Das ist die Voraussetzung für Option F und für Stufe 3 — und mitmigriert billiger als nachgerüstet |
| 3 | **Die Zeitnachweisformate der Kundenbetriebe, erhoben mit Doreen Ritschel** | 17.700 € im Jahr, vier Tage Klärung im Monat, eine Person und ein Pinnwand-Ausdruck. Der teuerste vermeidbare Fehler des Programmjahres — und die Anforderung, die Achtelik und die Niederlassungsleitungen auf die Vorlage holt |

**Was gestrichen ist und warum:** Die AI-Act-Haftungsübernahme durch den Anbieter, die konfigurierbare Rangfolgelogik und die Exit-Klausel standen in Fassung 1 als Anforderungen 1, 2 und 6. Sie sind gestrichen, **weil Marnitz nachgewiesen hat, dass sie nicht kommen** — der Markt schiebt die Rechtmäßigkeit der Nutzung per AGB zurück. Eine Anforderung, deren Nichterfüllung man vorhersagen kann, in eine Endverhandlung zu tragen, kostet Glaubwürdigkeit bei Achtelik und bringt nichts. Die drei verbliebenen sind Datenanforderungen: sie hängen nicht davon ab, was ein Anbieter zusagt, sondern davon, was das Zielsystem an Feldern hat.

### Empfehlung 3 · Neu: Stufe 4 wird 2026 nicht als Produkt entschieden, sondern als Konstruktion vorbereitet

**Das ersetzt die Kür von Option D in Fassung 1.**

| Was | Wert |
|---|---|
| Kein Anbieterentscheid für Stufe 4 in 2026 | Score B trennt sechs Optionen um 1,88 Punkte, aber **keine** erreicht eine 4 bei L1 **und** L2 gleichzeitig — außer F, und deren Kosten sind nicht beziffert |
| **Vorzugsvariante zur Ausarbeitung** | **Option F** · regelbasierter Filter über strukturierte Felder, Sprachmodell nur zur Formulierung. Score B **3,56** |
| Was zu ihr fehlt | Eine Bezifferung. Sie ist in Q1/2027 mit Balzer und dem künftigen Anbieter zu erheben, gegen die 27.000 € aus [Abschnitt 3](#3-die-budgetwahrheit-185000-statt-280000) |
| Reihenfolge, korrigiert | **3c vor 3b.** Löschung der 18.000 überfälligen Profile **vor** der Extraktion. Spart gut 24.000 € und verhindert, dass eine unzulässige Verarbeitung mit Budget und Beschluss ausgeweitet wird |
| Pilotstart | **Nicht** vor Fertigstellung der Gültigkeitsfelder aus 3a. Das war der zweite der drei Fehler aus Woche 2.4 und ist hier nachgetragen |
| Bis dahin ausdrücklich | Die Nullvariante bleibt mit 2,86 die zweitbeste Option und steht in der Vorlage. **Nichts zu bauen ist besser als jedes der vier KI-Produkte** — nur die kleinere, nachvollziehbare Konstruktion ist besser als nichts zu bauen |

### Empfehlung 4 · Vor dem Geschäftsführungs-Dienstag: nicht allein einreichen

Aus Bedenken 1 des Reviews, und es ist der Punkt, an dem ich als Rolle 15 mit Macht 2 den Fehler von 2023 wiederholen würde.

| Mit wem | Was vorher vereinbart ist |
|---|---|
| **Nowak (Betriebsrat)** | Entwurf der Rahmen-Betriebsvereinbarung liegt der Vorlage bei, damit Tor T2 als erledigt vorgelegt wird und nicht als Absicht. Sie ist die Rolle, deren Zustimmung meine Anwesenheit überdauert |
| **Achtelik (GF Finanzen/IT)** | Zusage: max. 10 Stunden Balzer, Migration Q1/2027 unberührt, Empfehlung 2 auf drei Datenanforderungen reduziert |
| **Rehberg (NL Gotha)** | Vier der 20 Seats gehen nach Gotha. In Stufe 1 gibt es keine Kandidatenvorschläge. Die Hoheit über das Anforderungsprofil bleibt in der Niederlassung |
| **Marnitz (DSB)** | Seine Stellungnahme geht **an die Geschäftsführung mit Kopie an den Betriebsrat**, nicht an mich. Sein Interessenkonflikt steht mit einem Satz in der Vorlage. Die Zweitmeinung (2.000 €) ist beauftragt |
| **Ziegenhorn (Controlling)** | Abschnitt 3 ist mit ihr gerechnet, bevor Dr. Barth ihn liest |

---

## 11. Offene Punkte und Prüffragen

### 11.1 Was diese Analyse nicht beantworten kann

| Nr | Offener Punkt | An wen | Bis wann | Was davon abhängt |
|---:|---|---|---|---|
| 1 | **Wie weit ist die Migrationsausschreibung?** | Achtelik | **diese Woche** | Empfehlung 2 vollständig |
| 2 | **Welche Branchensoftware ist es, und was kann der Nachfolger?** | Balzer, Achtelik | Q4/2026 | Option D war ohne diese Antwort nie scorebar. Das gilt weiter |
| 3 | **Ist die Profilzusammenfassung für die Kundenunterlage schon Annex III?** Und: trägt die Auswahl über einen deterministischen Filter die Ausnahme nach Art. 6 Abs. 3? | Marnitz **plus** Zweitkanzlei | vor Vertragsschluss Stufe 1 | Der Zuschnitt von Empfehlung 1 **und** die L1-Bewertung von Option F |
| 4 | **Was kostet Option F?** | Balzer, künftiger Anbieter | Q1/2027 | Ob Stufe 4 in 27.000 € passt |
| 5 | **Was kosten die sieben Betreiberpflichten?** Namentlich, mit Zeilen | Marnitz, Ziegenhorn | vor der Ausschreibung | Die Zahl, die in der Gesellschafterversammlung gebraucht und nicht vorhanden ist |
| 6 | **Sind die SharePoint-Berechtigungen geprüft?** | Balzer | vor jeder Copilot-Bewertung | K1/B — die 3 kann eine 4 oder eine 2 sein |
| 7 | **Neu: Welche M365-Basislizenzen hat GeAT seit 2020?** | Balzer | vor jeder Copilot-Kostenzahl | Ob 7.200 € überhaupt der richtige Preis ist |
| 8 | **Stellt Marnitz On-Premise als Pflichtanforderung fest?** | Marnitz | vor der GF-Vorlage | Bei „ja" bleibt bei 69 Seats keine Option verfügbar, und die Vorlage lautet Nullvariante |
| 9 | **Trägt der Investitionsspielraum 900.000 € oder 805.000 €?** | Ziegenhorn, Gesellschafterversammlung | Woche 6 oder 7 | Die Unterdeckung von 33.000 € — und ob eine Stufe gestrichen wird |

### 11.2 Prüffragen für das Anbietergespräch

1. **Legen Sie den AVV vor** — das Dokument, nicht die Aussage. Dazu ISO 27001 oder SOC 2 und den Verarbeitungsort.
2. **Welche Nutzerprotokolle entstehen, wer sieht sie, lässt sich der Umfang vertraglich begrenzen?**
3. **Wie stellen Sie sicher, dass wir jederzeit auf dem Stand der öffentlich verfügbaren Spitzenmodelle arbeiten?** (Die Frage, die den Rebound verhindert.)
4. **Können wir in 18 Monaten wechseln, wenn sich die Anforderungen verschärfen?**
5. **Wie bekommen wir Daten und Prompts wieder heraus — Format, Zeit, Preis?**
6. **Wie löschen Sie auf Anforderung nachweisbar?**
7. **Zwei Referenzkunden im DACH-Raum unter 150 Beschäftigten, davon einer aus der Personaldienstleistung, mit Gesprächserlaubnis.**
8. **Wer trägt bei Annex III welche Pflicht?** Schriftlich vor der Ausschreibung — **und rechnen Sie damit, dass die Antwort „der Kunde" lautet.** Marnitz hat das vorhergesagt; die Antwort ist der Test, nicht die Zusicherung.

### 11.3 Was ich an dieser Fassung selbst nicht belastbar finde

1. **Option F ist nicht beziffert.** Sie gewinnt Teil B mit dem größten Abstand beider Matrizen, und ich kann nicht sagen, was sie kostet. Das ist die schwächste Stelle von Fassung 2 — genau wie Option D die von Fassung 1 war. Der Unterschied: ich küre sie nicht zum Beschluss, sondern zur Ausarbeitung (Empfehlung 3).
2. **Alle Rechtsaussagen in Abschnitt 2 sind Arbeitshypothesen.** Das Review hat hier zwei Fehler gemacht, ich hatte eine Lücke. Zwei Unterschriften sind der Grund, warum die 2.000 € der billigste Posten sind.
3. **L0 mit 20 % ist meine Setzung.** Das Review wollte 25 % auf die Besetzungsdauer. Ich halte die Kennzahl für falsch und das Gewicht für zu hoch — aber die Idee war richtig, und ohne sie hätte die Nullvariante Teil B gewonnen.
4. **Der Wechsel des Siegers zwischen zwei Fassungen im Abstand von Stunden ist selbst ein Befund.** Er zeigt, wie empfindlich eine Nutzwertanalyse gegen Gewichtung und Ankerdisziplin ist. Wer diese Vorlage liest, sollte den Score als das nehmen, was er ist: eine geordnete Begründung, kein Messwert. **Im Plenum zählt nicht der Score, sondern die Begründung — und in dieser Fassung zählt sie doppelt, weil sie einmal falsch war.**

---

## Änderungsvermerk

| Datum | Änderung | Grund |
|---|---|---|
| 2026-09-07 | Fassung 1 (`KI_Analyse.md`): Gewichtung A und B fixiert, vor dem Scoring | — |
| 2026-09-07 | **Fassung 2.** Gewichtung A: K3 +2, K5 +1, K6 −4 (MCP entfernt), K7 +1. Gewichtung B: L0 neu (20 %), L1 −5, L2 −7, L3 −3, L5 −2, L6 −1, Adoption gestrichen | Review `KI_Analyse_Review.md` Schwächen 1, 3b, 5 · Kennzahlkorrektur gegen `vorhaben.md` |
| 2026-09-07 | **Fassung 2.** Option D: L1 4→2, L2 4→3, L4 4→3, K7 4→3. Option A: K3 3→2. Option B: K4 2→3. **Option F neu aufgenommen** | Ankerdisziplin (Review Fehler 3) · `Gespraeche/03` (AGB-Argument, sechste Option) |
| 2026-09-07 | **Fassung 2.** Neue Abschnitte 2 (Rechtsrahmen), 3 (Budget), 0 (Prüfprotokoll). Abbruchkriterium ersetzt, Sitzverteilung auf drei Standorte, Empfehlung 2 von sechs auf drei Anforderungen, Empfehlung 3 und 4 neu | Review Fehler 2 und 4, Bedenken 1–4 · Nachbesserungen aus `ereignisse.md` Woche 2.4 |

> **Regel für Änderungen an den Gewichtungen:** Wer sie verschiebt, trägt die Änderung hier ein, mit Grund und Datum. Eine nachträglich verschobene Gewichtung ohne Vermerk ist kein Nachjustieren, sondern ein rückwärts gerechnetes Ergebnis. **Fassung 2 verschiebt sieben Gewichte und korrigiert sechs Scores — jede einzelne Änderung steht oben mit ihrer Quelle.**

**Noch offen, nicht in dieser Datei zu erledigen:** der AÜG-Satz in [`transformationsvorschlag.md`](transformationsvorschlag.md) Zeile 126 ([Abschnitt 2.3](#23-was-in-transformationsvorschlagmd-noch-zu-streichen-ist)), und der Eintrag dieser Fassung in [`ereignisse.md`](ereignisse.md).

**Verwandte Dateien:** [`KI_Analyse.md`](KI_Analyse.md) (Fassung 1, ersetzt) · [`KI_Analyse_Review.md`](KI_Analyse_Review.md) (Prüfbericht) · [`Gespraeche/03-der-einwand-der-stimmt.md`](Gespraeche/03-der-einwand-der-stimmt.md) (Quelle von Option F und der drei Dokumente) · [`transformationsvorschlag.md`](transformationsvorschlag.md) · [`vorhaben.md`](vorhaben.md) · [`systeme-daten.md`](systeme-daten.md) · [`zahlen.md`](zahlen.md) · [`menschen.md`](menschen.md) · [`ereignisse.md`](ereignisse.md) · [Coursebook 3.1](../coursebook/3.1/3.1_KI-Plattformen-im-Vergleich.md)
