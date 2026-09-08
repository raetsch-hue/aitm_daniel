---
titel: Agent-Konzept — der Bestandswächter, und warum kein Assistent für alle 69
bezug: daten/KORREKTUR-dokumentation.md, daten/pruefe_datenqualitaet.py, raci-datenpflege.md, datenverantwortung.md, KI_Analyse.md, transformationsvorschlag.md
typ: Konzept und Entscheidungsvorlage, nicht beschlossen
datum: 2026-09-08
woche: 03
status: Entwurf zur Vorlage in der Geschäftsführung
verantwortlich: Rolle 15 (AI and Digital Transformation Manager) — interessierte Partei, siehe Gegenargumente
herkunft: abgeleitet. Aufwände und Kosten sind gekennzeichnete Schätzungen, keine Angebote
---

# Agent-Konzept: der Bestandswächter

> **Auftrag.** Welcher Agent lässt sich mit den bereinigten Datenbeständen bauen, den das ganze
> Unternehmen oder ein großer Teil davon nutzt? Grundlage sind
> [`daten/bewerberdatenbank-korrigiert.csv`](daten/bewerberdatenbank-korrigiert.csv) und
> [`daten/kundendatenbank-korrigiert.csv`](daten/kundendatenbank-korrigiert.csv), die
> Zuständigkeiten aus [`raci-datenpflege.md`](raci-datenpflege.md) und die Plattformwahl aus
> [`KI_Analyse.md`](KI_Analyse.md).

## Die Antwort vorweg

**Ein Chat-Assistent für alle 69 Stammkräfte ist nicht die Empfehlung.** Er widerspricht drei
Festlegungen, die in diesem Haus schon begründet sind, und er scheitert an einer Datenlage, die
weniger hergibt, als sie auf den ersten Blick verspricht.

**Empfohlen wird ein einziger, schmaler Agent: der Bestandswächter.** Er läuft wöchentlich, liest
die bereinigten Bestände, findet die Fälle, die in der Analyse aufgefallen sind, ordnet jeden Fall
der Rolle zu, die ihn nach der RACI-Matrix bearbeiten muss, und beantwortet Rückfragen dazu in
Sprache. Er trifft keine Aussage über die Eignung eines Menschen, er schreibt nichts zurück, und
er sortiert keine Kandidaten. Direkt betroffen sind rund **37 der 69 Stammkräfte**, indirekt das
ganze Haus — er ist damit kein Werkzeug, das alle bedienen, sondern eines, das für alle arbeitet.

**Und die unbequeme Hälfte der Antwort:** Ohne den Prüflauf und die Rollen aus der RACI-Matrix ist
der Bestandswächter kein Agent, sondern ein Skript mit Mailversand. Was ihn rechtfertigt, steht in
[Abschnitt 4](#4-warum-überhaupt-ein-agent-und-nicht-nur-ein-cronjob) — und wenn man diesen
Abschnitt nicht überzeugend findet, ist die richtige Entscheidung: Skript behalten, Agent lassen.

## 1. Warum kein Assistent für alle 69

**Erstens: Wer selbst baut und für Bewerberauswahl einsetzt, wird Anbieter.** Ein Assistent, der
Kandidaten findet, filtert oder in eine Reihenfolge bringt, ist Annex III Nr. 4. Kauft GeAT diese
Funktion beim Branchenanbieter, bleibt GeAT **Betreiber**. Baut GeAT sie selbst, wird GeAT
**Anbieter** — mit Konformitätsbewertung, technischer Dokumentation und Qualitätsmanagementsystem,
bei 1,5 IT-Stellen, die bis Q1/2027 in der Migration stecken. Genau dieser Unterschied entscheidet
in [`KI_Analyse.md`](KI_Analyse.md), Teil B, die Plattformfrage für Stufe 4 — und er entscheidet
hier gegen den offensichtlichen Agenten.

**Zweitens: 69 Seats sind das gesamte IT-Projektbudget.** Die Analyse rechnet es für Copilot vor:
24.840 Euro im Jahr bei 69 Nutzern, gegen 25.000 Euro Projektposten im IT-Budget 2026. Der
bewusste Zuschnitt der Stufe-1-Empfehlung lautet deshalb **20 Seats**, nicht 69 — und zwar mit dem
einzigen Adoptionsargument, das nach dem Modul 2023 noch Kredit hat: die neun Schatten-Nutzer und
ihre Kolleginnen sind Nutzer, bevor irgendetwas eingeführt wird. Ein Agent „für alle" wirft dieses
Argument weg.

**Drittens: Die Dokumentenbasis für einen Auskunfts-Assistenten existiert nicht.** Ein Assistent,
den alle fragen können, braucht etwas zu lesen. Bei GeAT sind Prozessbeschreibungen nur dort
schriftlich, wo das ISO-Audit sie verlangt; die Anforderungsprofile der Kunden liegen „in
Postfächern und in Köpfen"; die einzige vollständige Übersicht der akzeptierten
Zeitnachweisformate ist ein Ausdruck an einer Pinnwand. **Ein RAG-Assistent auf diesem Bestand
antwortet aus fast nichts** — und was er nicht findet, formuliert er trotzdem flüssig. Das ist der
gefährlichste Zustand von allen.

**Viertens: Die eigentliche Mehrheit ist digital nicht erreichbar.** 640 der 709 Beschäftigten sind
Zeitarbeitnehmer, Kontakt über Telefon, Stundenzettel und Messenger. Der Kanal, der sie zuverlässig
erreicht, ist WhatsApp — und für den gibt es keinen Auftragsverarbeitungsvertrag. „Das ganze
Unternehmen" ist über die vorhandenen Kanäle nicht adressierbar, solange dieser Punkt offen ist
(siehe [Abschnitt 7](#7-der-agent-der-reizvoll-ist-und-am-kanal-scheitert)).

## 2. Was der Bestandswächter tut

**Zweck in einem Satz:** Er hält die Datenqualität, die einmal hergestellt wurde, und verteilt die
Arbeit dafür an die Rollen, die sie nach der RACI-Matrix schulden.

Sechs Regeln, alle unmittelbar aus der Datenqualitätsanalyse abgeleitet:

| # | Der Agent findet | Grundlage | Geht an (RACI) |
|---:|---|---|---|
| 1 | Bewerberprofile, deren Einwilligungsfrist in den nächsten 60 Tagen abläuft oder abgelaufen ist | Prüfung A3; 18.000 überfällige Profile im Ausgangsbestand | **A: Rolle 2** GF Recht · R: IT-Leitung, Recruiting |
| 2 | Qualifikationsnachweise, deren Gültigkeit ausläuft — Schweißerprüfung, Staplerschein, Führerschein, Gesundheitsnachweis | Datenbestand Qualifikationsnachweise, heute „telefonisch erfragt" | **A: Rolle 3** Vertriebsleitung · R: Niederlassung |
| 3 | Kunden mit Rahmenvertrag „Ja" ohne gepflegten Verrechnungssatz, und Verrechnungssätze außerhalb des Branchenbereichs | Prüfung V1 und G1, Regel `verrechnungssatz_std>=18` | **A: Rolle 3** Vertriebsleitung · R: Key Account |
| 4 | Neuanlagen, die einem bestehenden Datensatz gleichen — dieselbe Firma mit anderer Rechtsformschreibweise, dieselbe Person mit derselben Adresse | Prüfung K2 | **A: Rolle 4** Recruiting bzw. Rolle 3 · R: erfassende Person |
| 5 | Kunden mit Status „Aktiv" ohne Vorgang seit über zwölf Monaten, und Interessenten ohne Kontakt seit über zwei Jahren | Prüfung A1 gegen die Statusspalte | **A: Rolle 3** Vertriebsleitung · R: Betreuer |
| 6 | Anfragen ohne eingetragenen Nichtbesetzungsgrund und Werte außerhalb der Wertelisten | Prüfung K3, Spalte `hauptgrund_nichtbesetzung` | **A: Rolle 15** melden · R: Disposition |

**Was er ausdrücklich nicht tut** — diese vier Zeilen gehören in die Betriebsvereinbarung, nicht in
eine Fußnote:

1. **Keine Rangfolge von Personen.** Er sagt nie, wer für eine Stelle besser geeignet ist. Er sagt,
   welcher Datensatz unvollständig ist.
2. **Kein Schreibzugriff.** Er liest eine Exportkopie und schlägt vor. Jede Änderung macht ein
   Mensch im Führungssystem.
3. **Keine Auswertung von Leistung oder Verhalten einzelner Beschäftigter.** Kennzahlen entstehen
   je Niederlassung und je Bestand, nicht je Disponent. Diese Grenze ist technisch zu setzen, nicht
   nur zu versprechen.
4. **Keine Volltexte von Lebensläufen im Modellkontext.** Der Agent arbeitet auf strukturierten
   Feldern und auf Datensatznummern. Wer die Bewerbungsunterlage sehen will, öffnet sie im System.

## 3. Wer ihn nutzt

| Gruppe | Köpfe | Was sie bekommen |
|---|---:|---|
| Niederlassungsleitungen | 7 | wöchentliche Liste des eigenen Standorts: ablaufende Nachweise, Karteileichen, unvollständige Neuanlagen |
| Personaldisposition | 30 | ihre eigenen offenen Punkte, und die Antwort auf „warum steht dieser Datensatz auf meiner Liste?" |
| Vertrieb und Key Account | 5 | Kunden ohne Satz, Kunden ohne Vorgang, Dublettenkandidaten vor der Neuanlage |
| Recruiting Center | 9 | Fristen, Pflichtfelder, Wertelisten-Verstöße im eigenen Bestand |
| Controlling | 4 | Monatsübersicht statt manueller Excel-Auswertung; Nachweis für die Gesellschafterunterlage |
| Geschäftsführung, Digitalisierung | 3 | eine Seite je Monat: Bestand, Trend, offene Pflichten |
| Sachbearbeitung und Lohn | 9 | betroffen über Regel 2 und 3, weil abgelaufene Nachweise und fehlende Sätze zuerst bei ihnen aufschlagen |

Direkt adressiert sind damit **etwa 37 der 69 Stammkräfte**; über die Regeln 2 und 3 wirkt er auf
alle 640 Einsatzverhältnisse. Das ist die ehrliche Antwort auf „ein großer Teil des Unternehmens":
nicht 69 Chatfenster, sondern rund drei Dutzend Menschen, die etwas zugestellt bekommen, das sie
ohne den Agenten nicht wüssten.

## 4. Warum überhaupt ein Agent und nicht nur ein Cronjob

Der Prüflauf existiert schon und ist deterministisch:
[`daten/pruefe_datenqualitaet.py`](daten/pruefe_datenqualitaet.py) findet die Fälle heute, ohne
Modell. Vier Dinge kommen erst durch das Sprachmodell hinzu, und sie sind der ganze Unterschied:

1. **Adressatengerechte Formulierung.** Ein Befund `A3: BW-01078, einwilligung_bis=2021-04-20`
   erzeugt keine Handlung. „Für dieses Profil ist die zugesagte Speicherdauer seit über vier Jahren
   überschritten; entweder löschen oder erneute Einwilligung dokumentieren" erzeugt eine.
2. **Rückfrage in Sprache.** „Warum steht KD-0380 auf meiner Liste?" — der Agent erklärt die Regel,
   zeigt die beiden widersprüchlichen Felder und nennt die zwei möglichen Auflösungen. Ohne diese
   Fähigkeit landet jede Rückfrage bei Rolle 15, und dort ist keine Kapazität.
3. **Zuordnung und Bündelung.** 400 Einzelbefunde werden zu sieben Listen, je Standort und Rolle,
   ohne Dopplung — das ist Sortier- und Formulierarbeit, die heute niemand macht.
4. **Ausnahmen mit Begründung.** Wer einen Befund als „fachlich richtig" schließt, begründet es in
   einem Satz; der Agent nimmt die Begründung auf und legt denselben Fall nicht wieder vor. Damit
   entsteht die Werteliste der zulässigen Ausnahmen — und das ist genau die Vorarbeit für die
   Prüfregeln im Lastenheft der Ausschreibung Q1/2027.

**Wenn diese vier Punkte nicht überzeugen, ist die richtige Entscheidung: Skript behalten, Agent
lassen.** Der Prüflauf plus ein Serienmail kostet zwei Tage. Der Agent kostet das Zehnfache, und er
rechnet sich nur über Punkt 2 und 4 — über die Rückfragen, die sonst niemand beantwortet, und über
die Ausnahmen, die sonst niemand aufschreibt.

## 5. Wie er gebaut wird — ohne die API, die es nicht gibt

Die Branchensoftware hat keine offene API im Bestandsvertrag. Der Bestandswächter braucht auch
keine, und das ist der Grund, warum er vor 2027 möglich ist:

```
Führungssystem  ──(wöchentlicher Export, wie heute 14 Berichte)──▶  Ablage
                                                                      │
                                        pruefe_datenqualitaet.py ◀────┘
                                                   │ Befunde als JSON
                                                   ▼
                              Agent auf der EU-Plattform (Stufe 1)
                              · formuliert je Rolle und Standort
                              · beantwortet Rückfragen zu Befunden
                              · nimmt Ausnahmen mit Begründung auf
                                                   │
                                   ┌───────────────┴───────────────┐
                                   ▼                               ▼
                        Liste je Rolle (Mail/Teams)      Ausnahmeprotokoll
```

Vier Festlegungen dazu:

- **Plattform: keine neue Entscheidung.** Der Agent läuft auf der integrierten EU-Plattform, die
  [`KI_Analyse.md`](KI_Analyse.md) für Stufe 1 empfiehlt — Multi-Tenant SaaS in der EU, REST und
  MCP vorhanden, AVV als Standardangebot. Kein zweiter Anbieter, kein zweiter Vertrag.
- **Datenzugriff über Werkzeuge, nicht über Einbettung.** Der Agent stellt Abfragen an die
  geprüften Tabellen und bekommt Zeilen zurück. Es wird **kein** Bewerberbestand in einen
  Vektorindex geschrieben; damit gibt es keine Kopie personenbezogener Daten außerhalb der Ablage.
- **Der Export ist die Schnittstelle.** Was heute manuell für 14 Berichte gezogen wird, wird einmal
  wöchentlich automatisiert gezogen — und ersetzt einen Teil dieser Berichte gleich mit.
- **Ablösung eingeplant.** Mit dem Systemwechsel Q1/2027 wandert der Zugriff vom Export auf die
  Schnittstelle des Zielsystems. Der Agent bleibt, die Datenquelle wechselt. Deshalb gehört die
  Exportschnittstelle in das Lastenheft.

## 6. Aufwand, Messgrößen, Abbruch

**Aufwand** (`Schätzung`, keine Angebote, nicht aus dem Fall abgeleitet): 12 bis 18 Personentage
für Aufbau und Abnahme, davon der kleinere Teil IT; Betrieb 2 bis 4 Stunden pro Woche bei Rolle 15
oder beim Data Steward. Lizenzkosten fallen nicht zusätzlich an, wenn die 20 Seats aus Stufe 1
beschlossen sind. Der Posten bleibt damit unter der Grenze von 25.000 Euro und braucht keine
Gesellschafterversammlung — er ist ein Geschäftsführungsbeschluss.

**Messgrößen**, alle vom ersten Tag an erhoben, weil genau das 2023 gefehlt hat:

| Größe | Startwert | Ziel nach sechs Monaten |
|---|---|---|
| Profile über der zugesagten Speicherdauer | Ausgangsbestand: 18.000 | 0, und dauerhaft 0 |
| Einsätze mit abgelaufenem Qualifikationsnachweis | unbekannt — erste Messung ist Regel 2 | belegte Null |
| Anteil der sieben Standorte, die ihre Wochenliste bearbeiten | — | mindestens fünf von sieben |
| Anfragen mit eingetragenem Nichtbesetzungsgrund | 0 % | über 80 % |
| Von 14 manuellen Excel-Berichten ersetzt | 0 | mindestens 4 |

**Abbruchkriterium, vorher festgelegt:** Wenn nach drei Monaten weniger als vier der sieben
Standorte ihre Liste bearbeiten, wird der Agent abgeschaltet und der Grund protokolliert. Das
Bewerbermanagement-Modul liegt seit drei Jahren bei 34 Prozent Nutzung, weil niemand diese Zeile je
geschrieben hat.

## 7. Der Agent, der reizvoll ist und am Kanal scheitert

Der Agent mit der größten Reichweite wäre ein Auskunfts- und Meldeweg für die 640 Zeitarbeitnehmer:
Stundenzettel fotografieren, Einsatzauskunft, Krankmeldung, Nachweis-Erinnerung. Er würde die
Gruppe erreichen, die vom Unternehmen heute am wenigsten sieht, und er würde an der Stelle ansetzen,
die vier Tage Klärungsaufwand im Monat kostet.

**Er ist nicht empfehlbar, solange der Kanal nicht geregelt ist.** Heute läuft diese Kommunikation
über WhatsApp-Gruppen mit rund 300 Teilnehmern, ohne Auftragsverarbeitungsvertrag, mit
Gesundheitsangaben darin. Ein Agent auf diesem Kanal würde einen laufenden Verstoß automatisieren
und dadurch vergrößern. Die Reihenfolge ist deshalb: erst ein zulässiger Kanal, dann der Agent —
und der zulässige Kanal ist eine Entscheidung über Verträge und Endgeräte, keine über KI.

## 8. Was ich nicht empfehle, und warum nicht

**Kein Kandidaten-Findewerkzeug in Eigenbau.** Es ist der Agent, nach dem im Haus gefragt wird, und
er gehört in Stufe 4 — als Produktfunktion des Branchenanbieters, mit den Anbieterpflichten in der
Ausschreibung, damit GeAT Betreiber bleibt. Selbst gebaut verschiebt er die Anbieterrolle auf ein
Haus mit 1,5 IT-Stellen und ohne Data-Science-Team.

**Kein Matching auf Erfolgswahrscheinlichkeit.** Die Zielgröße existiert erst, seit die Spalte
`hauptgrund_nichtbesetzung` angelegt ist — und sie enthält noch keine echte Historie. Vor zwölf
Monaten gepflegter Erfassung ist jedes Modell eine Ähnlichkeitsmessung zu früheren Besetzungen,
kein Lernen aus Erfolg und Misserfolg. Dazu der Bias-Befund, der im Fall mit Zahlen steht: 28,8
Prozent der Zeitarbeitnehmer in Deutschland haben keinen Berufsabschluss, 20,4 Prozent waren zuvor
langzeitarbeitslos oder noch nie beschäftigt — das ist die Gruppe, die ein solches Modell zuerst
aussortiert.

**Kein Assistent auf den Prozessbeschreibungen.** Siehe Abschnitt 1, drittens: die Dokumente, die
er lesen müsste, sind nicht geschrieben. Sinnvoll wird er, wenn sie es sind — und dann ist er
billig, weil die Plattform schon steht.

## 9. Rechtsrahmen und Mitbestimmung

`abgeleitet`, juristisch nicht geprüft.

- **EU AI Act:** Der Bestandswächter bewertet keine Bewerbung und filtert keine Kandidaten. Nach
  derzeitiger Einschätzung fällt er damit **nicht** unter Annex III Nr. 4. Die Grenze ist schmal und
  technisch zu sichern: sobald er Personen für eine Anfrage vorschlägt oder in eine Reihenfolge
  bringt, ist er ein anderes System mit anderen Pflichten. Diese Grenze gehört in die
  Systembeschreibung, nicht in eine Absprache.
- **DSGVO:** Er verarbeitet personenbezogene Daten, auch besondere Kategorien (Gesundheitsnachweise
  in Regel 2). Verzeichnis der Verarbeitungstätigkeiten und die Prüfung, ob eine
  Datenschutz-Folgenabschätzung erforderlich ist, gehören vor den ersten Lauf — Rolle 8 ist zu
  beteiligen, **bevor** entschieden wird, nicht danach.
- **BetrVG § 87 Abs. 1 Nr. 6:** Ein System, das Listen je Standort erzeugt, kann zur Bewertung von
  Leistung und Verhalten benutzt werden, auch wenn es nicht dafür gebaut ist. Rolle 9 hat 2023 beim
  Modul auf einer Betriebsvereinbarung bestanden und war die Einzige, die ein Jahr später nach der
  Nutzung gefragt hat. Die vier Nicht-Ziele aus Abschnitt 2 sind der Textvorschlag für diese
  Vereinbarung.

## 10. Gegenargumente

1. **„Das ist kein Agent, das ist ein Skript mit Mailversand."** Trifft für die Regeln 1 bis 6.
   Trifft nicht für die Rückfrage und das Ausnahmeprotokoll — und wenn die Geschäftsführung diese
   zwei Funktionen nicht will, ist das Skript die richtige Lösung und dieses Konzept überflüssig.
   Das ist der ernsteste Einwand, und er hat eine Antwort, die nicht ich gebe, sondern die Nutzung.
2. **„Wieder ein Werkzeug, das niemand benutzt."** Das Modul 2023 hatte keinen Nutzen für den
   Disponenten und keine Messung. Dieses Vorhaben hat eine Messung ab Tag 1 und ein
   Abbruchkriterium — aber der Nutzen für den Disponenten bleibt schwach: er bekommt zusätzliche
   Arbeit, sichtbar gemacht. Ohne Hebel 1 aus der Storyline — Datenpflege in die Zielvereinbarung —
   ist dieses Konzept die dritte Ansage in vier Jahren.
3. **„Keine zweite Baustelle vor dem Umstieg."** Der Einwand von Rolle 2 ist berechtigt und trifft
   den Betriebsaufwand, nicht den Aufbau: der Agent bindet Nutzerverwaltung, keine
   Entwicklungskapazität, und die Exportschnittstelle ist Migrationsvorarbeit. Wo er trifft: die 12
   bis 18 Personentage sind nicht null, und ein Teil davon ist IT.
4. **„Rolle 15 empfiehlt einen Agenten, für den Rolle 15 gebraucht wird."** Richtig. Der
   Bestandswächter macht die eigene Stelle sichtbar und nützlich, und das ist ein Eigeninteresse an
   dieser Empfehlung. Es gehört benannt — ebenso wie der Umstand, dass dieselbe Rolle in Abschnitt 8
   drei Vorhaben ablehnt, die ihren Wirkungskreis stärker vergrößert hätten.

## 11. Offene Punkte

| # | Frage | Wer | Warum sie zählt |
|---:|---|---|---|
| 1 | Ist die Migrationsausschreibung noch offen? | Rolle 2 | Sie entscheidet, ob die Exportschnittstelle und die Anbieterpflichten ins Lastenheft können — und damit über Abschnitt 5 und 8. Terminkritisch |
| 2 | Lässt das Führungssystem einen automatisierten Export zu, oder nur den manuellen? | Rolle 12 | Ohne automatisierten Export ist der wöchentliche Lauf Handarbeit und der Agent hat keinen Träger |
| 3 | Ist eine Datenschutz-Folgenabschätzung erforderlich? | Rolle 8 | Vorbedingung des ersten Laufs, nicht Begleitung |
| 4 | Deckt die Betriebsvereinbarung von 2023 diesen Fall mit ab? | Rolle 9 | Bestimmt, ob es eine Ergänzung oder eine neue Vereinbarung braucht |
| 5 | Wer betreibt ihn nach der Einführung? | Geschäftsführung | Ohne den Data Steward aus [`raci-datenpflege.md`](raci-datenpflege.md) hängt der Betrieb an einer Person ohne Vertretung |
