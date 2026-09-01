---
firma: Hellwig Fördertechnik (fiktiv)
stand: 2026-09-01
verwendung: Vertiefung, ab Tag 1.4 einsetzbar
prinzip: Die Lage ändert sich, nicht die Personen.
---

# Sonderfälle und Injects

Dreizehn Ereignisse, die in die laufende Firmengeschichte eingespielt werden können. Jedes ist so gebaut, dass es **ein** Modell auf die Probe stellt und **eine** unbequeme Entscheidung erzwingt.

**Einsatzweise:** Ein Inject wird vorgelesen oder als Kurztext ausgegeben, dann läuft eine Diskussion oder eine Kurzaufgabe. Sie sind nicht chronologisch zu spielen — jedes funktioniert allein. Die Zeitangaben sind Vorschläge für eine gedachte Zukunft ab 09/2026.

**Zwei Regeln:** Kein Inject widerspricht einem anderen. Und keines verlangt, dass eine Person aus [`02_Stakeholder.md`](02_Stakeholder.md) sich anders verhält als beschrieben.

---

## I1 · Semmler setzt eine Kennzahl auf Rot

**Ereignis (10/2026).** In der Serviceleitungsrunde stellt Semmler erstmals seit sechs Sitzungen eine Kennzahl auf Rot: die Ersatzteil-Reaktionszeit. Er begründet: sechs unbesetzte Stellen, zwei Langzeitkranke. Dr. Hellwig ist anwesend.

**Was auf dem Spiel steht:** Ihre Reaktion. Wenn sie nachfragt, warum das erst jetzt kommt, sind die nächsten sechs Sitzungen wieder grün.

**Prüft:** Kotter Schritt 2 und 5, psychologische Sicherheit, [Ford / Mulally](../coursebook/2.2/2.2_Kotter-8-Schritte-Modell.md#82-ford-unter-alan-mulally-koalition-und-handlungsfreiheit-schritte-2-und-5).
**Aufgabe (10 Min.):** Formuliere Dr. Hellwigs Antwort in zwei Sätzen. Und: Was muss danach passieren, damit die zweite rote Zahl leichter fällt als die erste?
**Der Lehrpunkt:** Eine Koalition entsteht durch ein Format mit Taktung und Straffreiheit, nicht durch Benennung. Wenn ein Pilot nur Erfolgsmeldungen produziert, misst man nicht den Piloten.

---

## I2 · Der Chatbot sagt einen Liefertermin zu

**Ereignis (01/2027).** V4 ist seit sechs Wochen live. Ein Kunde fragt nach der Verfügbarkeit eines Antriebs, der Chatbot nennt „Lieferung innerhalb von 5 Werktagen". Tatsächlich sind es 14 Wochen — das Teil ist abgekündigt. Der Kunde hat auf dieser Basis eine Anlagenumstellung geplant und fordert **41.000 EUR** Vertragsstrafe aus dem Rahmenvertrag. Der Chatbot-Anbieter verweist auf seine AGB.

**Prüft:** [Air Canada](../coursebook/1.4/1.4_Vier-Wellen-KI-Kategorien-Hype-Cycle.md#83-air-canada-die-haftungsfrage-bei-genai), die Grenze zwischen Effizienz- und Compliance-Vorhaben.
**Aufgabe (15 Min.):** Drei Fragen. Wer haftet? Was hätte im Vorhaben von Anfang an anders sein müssen? Und: Gibt es eine Fassung von V4, die diesen Fall ausschließt und trotzdem Nutzen bringt?
**Erwartet:** Haftung liegt bei Hellwig. Verbindliche Auskünfte nach außen brauchen Freigabe, Protokollierung und einen Rückfallpfad zum Menschen — damit ist V4 ein Compliance-Vorhaben mit anderem Aufwandsprofil. Die tragfähige Fassung nennt Verfügbarkeiten nur als „unverbindlich, Angebot folgt" und übergibt bei Abkündigung an einen Menschen.
**Die harte Nachfrage:** Wer hat die 25 Personentage geschätzt, und war die Protokollierung darin?

---

## I3 · Der Wissensassistent zitiert die Gehaltsliste

**Ereignis (11/2026).** Ein Prototyp von V10 läuft mit Leserecht auf `N:\`. In einer Demo fragt Brandtner: „Was verdient ein Servicetechniker bei uns?" Der Assistent antwortet korrekt, mit Quellenangabe: `N:\Personal\Gehaltsrunde_2025_final.xlsx`, Zeile 34. Im Raum sitzen neun Personen, darunter zwei Techniker.

**Prüft:** Berechtigungen als Voraussetzung, nicht als Nachgedanke. Reifegrad Daten Stufe 2 in seiner unangenehmsten Form.
**Aufgabe (10 Min.):** Was ist jetzt zu tun — in dieser Reihenfolge? Und was folgt daraus für den Aufwand von V10?
**Erwartet:** Sofort Zugriff sperren, Vorfall dokumentieren, Betriebsrat und DSB informieren (bevor es jemand anders tut). Dann: V10 ist ohne Berechtigungsinventur nicht machbar, und die Inventur ist kein KI-Aufwand — sie hätte auch ohne KI schon fehlen dürfen.
**Der zweite Lehrpunkt:** Ein Assistent hat keine eigenen Rechte. Er erbt die Rechte seines Zugangs. Das ist keine KI-Eigenschaft, sondern eine Berechtigungsfrage, die nur durch KI sichtbar wird.

---

## I4 · Das Wartungsmodell driftet still

**Ereignis (05/2027).** V3 läuft seit sieben Monaten und hat elf Ausfälle korrekt vorhergesagt. Im März 2027 hat der Gateway-Hersteller eine neue Firmware ausgerollt; seither liefern zwei Sensortypen andere Skalierungen. Das Modell prognostiziert weiter, mit unveränderter Zuversicht. Im Mai fällt eine Anlage bei einem Großkunden aus, den das Modell als unkritisch geführt hat. Stillstandskosten beim Kunden: 210.000 EUR.

**Prüft:** [Zillow](../coursebook/1.4/1.4_Vier-Wellen-KI-Kategorien-Hype-Cycle.md#82-zillow-offers-wenn-ein-prognosemodell-still-driftet), Rückkopplungszeit, Modellmonitoring.
**Aufgabe (15 Min.):** Wie lange hätte der Zustand unbemerkt bleiben können? Welche zwei Kennzahlen hätten ihn gemeldet? Und warum hat es niemand gemerkt, obwohl elf Vorhersagen richtig waren?
**Erwartet:** Die Rückkopplungszeit bei Wartungsprognosen ist lang — ein Modell kann Monate falsch liegen, bevor ein Ausfall es beweist. Nötig sind Eingangsdatenüberwachung (Verteilungsverschiebung je Sensor) und eine laufende Trefferquote gegen tatsächliche Ausfälle. Die elf Treffer sind kein Gegenargument: sie liegen vor dem Firmware-Update.
**Die Verbindungsfrage:** Wer im Haus wäre für dieses Monitoring zuständig? Antwort: niemand. Die Rolle existiert nicht.

---

## I5 · Schatten-KI wird sichtbar

**Ereignis (09/2026).** Kai Oberholz postet im Teams-Kanal „Service Talk" (184 Mitglieder) einen Screenshot: ein abfotografierter Schaltplan der Anlage eines Kunden, daneben die KI-Antwort mit der richtigen Fehlerursache. Kommentar: *„Drei Minuten. Vorher eine halbe Stunde telefonieren."* 31 Reaktionen, 9 zustimmende Kommentare. Reitmeier sieht den Post.

**Prüft:** Governance, B = f(P, E), die Frage, ob Verbot oder Rahmen die Antwort ist.
**Aufgabe (20 Min., Gruppen):** Zwei Reaktionen ausformulieren — eine, die Oberholz zum Regelverstoß macht, und eine, die ihn zum Freiwilligen macht. Dann entscheiden und begründen.
**Erwartet:** Der Schaltplan ist Kundeneigentum, das ist ein echter Verstoß und muss adressiert werden. Aber: Es gab keine Regel, kein freigegebenes Werkzeug und keine Ansprechperson. Eine Sanktion ohne vorherigen Rahmen erzeugt einen Zyniker mit 184 Zuhörern. Die tragfähige Reaktion benennt den Verstoß, schafft in derselben Woche einen erlaubten Weg und macht Oberholz zum Key User — mit ausgewiesener Zeit.
**Der Nebenbefund:** 34 von 512 nutzen private Konten. Ein Verbot verlagert das ins Unsichtbare, es beendet es nicht.

---

## I6 · Brandtner verlangt einen Business Case

**Ereignis (10/2026).** Vor der Budgetrunde: *„Ich gebe für kein KI-Vorhaben Geld frei, dessen Amortisation über 18 Monaten liegt. Und ich will die Wartungskosten drin sehen, nicht nur die Einführung."*

**Prüft:** Wirtschaftlichkeitsrechnung, die versteckte Wartungslast von RPA, den Unterschied zwischen Einsparung und Ergebniswirkung.
**Aufgabe (30 Min., Gruppen):** Für V1 einen Business Case rechnen — mit Zahlen aus [`material/M2`](material/M2_Kennzahlen.md). Beide Varianten: deterministisch und GenAI. Jede Annahme kennzeichnen.
**Erwartet:** Die deterministische Variante amortisiert; die GenAI-Variante scheitert an laufenden Aufrufkosten plus vollständiger Nachkontrolle, weil unbekannt ist, welche 2 % betroffen sind. Und: eine jährliche Wartungsquote für die RPA-Strecke (Erfahrungswerte 15–25 % der Einführungskosten) gehört hinein, sonst ist die Rechnung falsch.
**Die unbequeme Zeile:** 0,6 FTE eingesparte Arbeit ist keine Kosteneinsparung, solange niemand die Stelle streicht. Ergebniswirksam ist sie erst, wenn die freie Kapazität etwas erzeugt oder eine Nachbesetzung entfällt. Das ehrlich hinzuschreiben, ist die Übung.

---

## I7 · Der Seniorgesellschafter stoppt V3

**Ereignis (11/2026).** Im Gesellschafterausschuss lehnt Jürgen Hellwig das Datenpaket des Gateway-Anbieters ab (68.000 EUR/Jahr): *„Unsere Anlagendaten gehen nicht in eine amerikanische Wolke."* Der Ausschuss folgt ihm. V3 ist damit ohne Rohdaten.

**Prüft:** Nicht beeinflussbare Kräfte, das rechte obere Feld der [Priorisierungsmatrix](../coursebook/2.2/2.2_Ergaenzung-Force-Field-Analyse.md#45-von-der-analyse-zur-maßnahme).
**Aufgabe (15 Min.):** Drei Optionen entwickeln, von denen keine „Herrn Hellwig überzeugen" ist.
**Erwartet:** Ein Vorhaben um die Kraft herum planen. Optionen: On-Premise-Datenerfassung für eine Teilflotte; das Vorhaben auf die 71 Anlagen mit eigener Steuerung begrenzen; V3 zurückstellen und V6 vorziehen, das keine externen Daten braucht.
**Der Lehrpunkt, der im Kurs am meisten Widerstand erzeugt:** Manche Kräfte werden nicht bearbeitet. Die Zeit, die in ihre Bearbeitung fließt, fehlt bei den starken **und** beeinflussbaren.

---

## I8 · Der Sieg wird zu früh erklärt

**Ereignis (02/2027).** V7 läuft seit zehn Wochen im 1st-Level. Erstreaktionszeit von 9,2 auf 3,1 Stunden, Erstlösungsquote von 71 auf 76 %. Dr. Hellwig stellt das im Company Meeting vor, nennt drei Namen, es gibt Applaus. Danach: Das Projektteam wird aufgelöst, der externe Dienstleister abgemeldet, Ehrlichers halbe Stelle für das Vorhaben endet. Drei Bereiche melden sich, ob sie auch dürfen.

**Prüft:** [Kotters Schritt 7](../coursebook/2.2/2.2_Kotter-8-Schritte-Modell.md#83-kotters-zwölf-reengineering-projekte-zu-früh-gefeiert-schritt-7), Konsolidierung als Ressourcenereignis.
**Aufgabe (15 Min.):** Was ist an diesem Ereignis richtig und was ist gefährlich? Welche drei Dinge müssten in derselben Woche entschieden werden?
**Erwartet:** Richtig ist alles bis zum Applaus — es ist ein Quick Win, der Freiwillige erzeugt hat, genau wie geplant. Gefährlich ist die Auflösung. Nötig: Kapazität für die drei anfragenden Bereiche, eine dauerhafte Key-User-Rolle mit Zeitanteil, ein Nachmesstermin.
**Der Satz, der geübt wird:** *„Der Pilot ist erfolgreich. Wir sind bei Schritt 6 von 8."*

---

## I9 · Der Rückfall nach Projektende

**Ereignis (06/2027).** Vier Monate nach I8: Nutzung von V7 ist von 62 % auf 27 % gefallen. Ursachen, in der Nachschau:

- Verfahrensanweisung VA-12 „Ticketbearbeitung 1st Level" beschreibt weiter den alten Weg.
- Die Qualitätsstichprobe prüft weiter nur die Reaktionszeit, nicht die Nutzung des Entwurfs.
- Die drei benannten Key User sind zurück im Tagesgeschäft, ohne Nachfolge.
- Ein ungelöster Fehlerfall (falsche Ersatzteilnummer in einem Entwurf, ging an einen Kunden) machte im Team die Runde. Erfolgsgeschichten machten das nicht.

**Prüft:** [Reinforcement](../coursebook/2.1/01_Change-Management-Lewin-ADKAR.md#95-der-reinforcement-fehler-der-rückfall-nach-projektende), Refreeze als Strukturaufgabe.
**Aufgabe (20 Min.):** Vier Maßnahmen in der Reihenfolge ihrer Wirkung. Und: Welche wäre vor Projektbeginn möglich gewesen?
**Erwartet:** Stärkster Einzelhebel ist VA-12. Dann Qualitätssicherung, dann Key-User-Rolle mit 10 % Zeitanteil, dann Fehlerfälle als Support-Anlass behandeln statt als Beweis. Alle vier wären vorab planbar gewesen — Refreeze wird vor dem Change entschieden, nicht danach.
**Die Anschlussfrage:** Wer im Haus darf eine Verfahrensanweisung ändern? Antwort: die Qualitätsleitung, die in keinem Vorhaben eingebunden ist.

---

## I10 · Die Trägerin wird abgeworben

**Ereignis (03/2027).** Nina Kowalczyk legt ein Angebot eines Wettbewerbers vor: gleiche Position, 18 % mehr, Titel „Leitung Digital Sales". Sie sagt, sie würde bleiben, wenn es „hier eine Perspektive in dieser Richtung" gäbe.

**Prüft:** [Kotters Schritt 8](../coursebook/2.2/2.2_Kotter-8-Schritte-Modell.md#3-die-acht-schritte-im-detail) und das Nachfolgerisiko. „Was passiert, wenn die drei Tragenden morgen gehen?"
**Aufgabe (15 Min.):** Die Frage beantworten — für V2 konkret. Dann: Was ist die richtige Reaktion, und was ist die teure?
**Erwartet:** V2 endet mit ihr, weil sie die Zahlen, den Prozess und die Beziehung zu den zwei Großkunden hält. Die teure Reaktion ist eine Gehaltsanpassung ohne Strukturänderung. Die tragfähige verankert die Fähigkeit: eine benannte Rolle, ein zweiter Kopf, dokumentierte Auswertung.
**Der Punkt, der bleibt:** Ein Vorhaben, das an einer Person hängt, ist nicht verankert — unabhängig davon, wie gut die Zahlen heute aussehen.

---

## I11 · Der Wettbewerber liefert in zwei Stunden

**Ereignis (12/2026).** Der größte Wettbewerber schaltet ein Ersatzteilportal mit Sofortangebot frei. Ein Großkunde (8 % des Serviceumsatzes) kündigt an, ab 2027 „bevorzugt dort" zu bestellen. Dr. Hellwig fordert in der Steuerkreissitzung „bis Ende Q1 eine Antwort".

**Prüft:** [Kodak](../coursebook/2.2/2.2_Kotter-8-Schritte-Modell.md#81-kodak-dringlichkeit-die-nie-entstand-schritt-1) und den Unterschied zwischen Dringlichkeit und Panik. Amaras Gesetz als Gegengewicht.
**Aufgabe (20 Min.):** Die Dringlichkeit ist jetzt da. War das gut? Und: Was ist in einem Quartal machbar, ohne Schritte zu überspringen?
**Erwartet:** Dringlichkeit, die erst durch einen verlorenen Kunden entsteht, ist zu spät — das ist Kodak, nur schneller. Machbar in einem Quartal: die drei nicht-KI-Engpässe von V2 (Vault-Leserecht, Gewichtsdaten für die Top-500-Teile, Freigabegrenze). Nicht machbar: ein Portal. Die ehrliche Antwort im Steuerkreis nennt beides.
**Die Formulierungsübung:** Wie sagt man „das dauert länger" ohne das Wort „aber"?

---

## I12 · AI Act trifft das HR-Vorhaben

**Ereignis (01/2027).** Die Personalleitung hat einen Anbieter für V9 ausgewählt und will unterschreiben. Lindqvist weist darauf hin, dass Systeme zur Bewerbervorauswahl als Hochrisiko-Anwendungen einzuordnen sind, mit Anforderungen an Risikomanagement, Datenqualität, Protokollierung, menschliche Aufsicht und Transparenz gegenüber Betroffenen. Der Anbieter liefert dazu ein zweiseitiges Merkblatt.

**Prüft:** Regulierung als Kraft im Cluster Kontext, den Unterschied zwischen Zulässigkeit und Sinnhaftigkeit.
**Aufgabe (15 Min.):** Zwei Ebenen trennen. Erstens: Was wäre nötig, um es zulässig zu machen? Zweitens: Wollen wir es dann?
**Erwartet:** Die zweite Frage entscheidet, und sie ist keine Rechtsfrage. Bei 19 % Frauenanteil in technischen Rollen lautet die Absicht „ändern", nicht „fortschreiben" — und ein historisch trainiertes Modell schreibt fort. Der Compliance-Aufwand ist dann Aufwand für ein Vorhaben, das man auch bei bestandener Prüfung nicht will.
**Der Transfer:** *Wollen wir die Vergangenheit fortschreiben oder ändern?* ist die billigere Prüfung, und sie kommt vor der juristischen.

---

## I13 · Effizienz gemessen, Qualität nicht

**Ereignis (04/2027).** V7 ist auf drei Bereiche skaliert. Berichtete Zahlen: Erstreaktionszeit von 9,2 auf 2,4 Stunden, bearbeitete Tickets je Person +38 %. Im Steuerkreis gefeiert. Nicht berichtet, weil nicht erhoben: Die Erstlösungsquote ist von 76 % auf **58 %** gefallen, die Wiederkontaktquote von 19 % auf 34 %. Zwei Servicetechniker berichten, dass sie zunehmend Zweitanfragen zu Themen erhalten, die das 1st-Level „schon beantwortet" hat.

**Prüft:** [Klarna](../coursebook/1.4/1.4_Vier-Wellen-KI-Kategorien-Hype-Cycle.md#81-klarna-der-hype-cycle-in-reinform-in-18-monaten). Eine Kennzahl, die widersprechen kann.
**Aufgabe (20 Min.):** Welche Kennzahl hätte von Anfang an mitlaufen müssen — und wer hätte sie festgelegt? Dann: Wie berichtet man das im Steuerkreis, ohne den Piloten zu beenden?
**Erwartet:** Beide Aussagen stimmen gleichzeitig. Nötig ist mindestens eine Qualitätskennzahl, die dem Effizienzargument widersprechen kann: Erstlösungsquote, Wiederkontaktquote oder Zufriedenheit nach abgeschlossenem Vorgang. Wer nur Durchsatz misst, optimiert Durchsatz — auch dort, wo es schadet.
**Die härtere Frage:** Die Zahlen lagen im Ticketsystem vor. Nicht erheben war keine technische, sondern eine Auswahlentscheidung. Wer trifft solche Entscheidungen bei Hellwig? Niemand benannt.

---

## Zuordnung: Inject zu Modell

| Inject | Kurstag | Modell oder Werkzeug |
|---|---|---|
| I1 Rote Kennzahl | 2.2 | Kotter 2 und 5, psychologische Sicherheit |
| I2 Chatbot-Zusage | 1.4 | Haftung bei GenAI, Kategorie vs. Compliance |
| I3 Gehaltsliste | 1.4 / Governance | Reifegrad Daten, Berechtigungen |
| I4 Modelldrift | 1.4 | Predictive ML, Rückkopplungszeit |
| I5 Schatten-KI | 2.1 | B = f(P, E), Governance, Freiwillige |
| I6 Business Case | 1.4 / Wirtschaftlichkeit | Kategorienkosten, RPA-Wartungslast |
| I7 Gesellschafter stoppt | Mittwoch | Kraftfeld, nicht beeinflussbare Kräfte |
| I8 Zu früh gefeiert | 2.2 | Kotter 7 |
| I9 Rückfall | 2.1 / 2.2 | Reinforcement, Refreeze, Kotter 8 |
| I10 Abwerbung | 2.2 | Kotter 8, Nachfolgerisiko |
| I11 Wettbewerber | 2.2 | Kotter 1, Kodak, Amaras Gesetz |
| I12 AI Act | 1.4 / Governance | Bias, Regulierung als Kontextkraft |
| I13 Qualität nicht gemessen | 1.4 / 2.2 | Klarna, Quick-Win-Kennzahlen |

**Für einen kurzen Block:** I5, I8 und I13 tragen am meisten Diskussion pro Minute. **Für einen langen Block:** I2 und I6 zusammen, weil sie dieselbe Fehlentscheidung von zwei Seiten zeigen — einmal juristisch, einmal kaufmännisch.
