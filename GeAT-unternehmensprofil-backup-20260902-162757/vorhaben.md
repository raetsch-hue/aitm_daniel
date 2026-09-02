# Vorhaben: GeAT mbH

## Das Vorhaben

**KI-gestützte Vorbereitung der Besetzung.** Aus einer Kundenanfrage, dem eigenen Bewerberbestand und den Lebenslauf-Dateien erzeugt ein Assistent einen Besetzungsvorschlag: drei bis fünf Kandidaten mit begründeter Passung und ausgewiesenen Lücken, ein Kandidatenprofil als Kundenunterlage, und einen Anzeigenentwurf für den Fall, dass der Bestand nicht trägt. **Der Personaldisponent entscheidet, wer vorgeschlagen wird — nicht der Assistent.** Kein Kandidat wird ohne Freigabe eines Menschen an einen Kunden gesendet, und keine Bewerbung wird ohne menschliche Sichtung abgelehnt (`angenommen`).

Der Pilot ist gegen den Reifegrad gewählt: Daten 2 und Kultur 2 schließen ein System aus, das selbst auswählt oder sortiert. Ein Assistent, der Kandidaten **findet und begründet**, funktioniert auf dem gemessenen Stand — aber nur, wenn die Qualifikationsdaten vorher strukturiert erfasst werden. Diese Vorleistung ist Teil des Vorhabens, nicht seine Voraussetzung.

| Angabe | Wert | Herkunft |
|---|---|---|
| Betroffene Prozesse | Anfrage bis Besetzung; nachgelagert Bewerbergewinnung | angenommen |
| Betroffene Rollen | 23 Disponenten, 9 Recruiter; im Pilot zunächst 6 Disponenten aus zwei Niederlassungen und 4 Recruiter | angenommen |
| Ziel in einem Jahr: Besetzungsdauer | Median 11 auf 7 Arbeitstage | angenommen |
| Ziel in einem Jahr: gesendete Profile je Besetzung | 4,8 auf 3,2 | angenommen |
| Ziel in einem Jahr: Besetzungsquote | 40 auf 45 Prozent | angenommen |
| Ziel in einem Jahr: Vollkosten je Besetzung | 815 auf 650 Euro | angenommen |
| Ziel in einem Jahr: Anteil strukturiert erfasster Profile | 37 auf 80 Prozent bei allen neu angelegten Profilen | angenommen |
| **Nicht Ziel** | Personalabbau in der Disposition. Und **nicht** die Abbruchquote der ersten vier Wochen: die hängt am Kundenbetrieb, nicht am Vorschlag | angenommen |
| Pilotdauer | 6 Monate, danach Entscheidung über die Ausweitung auf alle Niederlassungen | generiert |
| Budget | 180.000 Euro über zwei Jahre, davon rund zwei Drittel für Datenstrukturierung und Konformität, ein Drittel für das Modell und die Oberfläche | generiert |

Die Zielgröße, an der der Pilot gemessen wird, ist **nicht** die Besetzungsdauer, sondern die Zahl der gesendeten Profile je Besetzung. Sie ist die einzige Größe, auf die der Assistent direkt wirkt, sie ist wöchentlich messbar, und sie treibt die Besetzungsdauer über die Kundenentscheidung (3,1 von 11 Tagen). Wer die Besetzungsdauer selbst zur Pilotkennzahl macht, misst zu 96 Prozent Warteschleifen, die der Pilot nicht anfasst.

## Workflows

### Anfrage bis Arbeitsbeginn, heute

| Schritt | Wer | Auslöser und Ergebnis | Volumen | Schnittstelle | Freigabe | Was ein Fehler kostet | Herkunft |
|---:|---|---|---:|---|---|---|---|
| 1 Anfrage aufnehmen | Disponent | Anruf oder Mail des Kunden, Anlage in der Branchensoftware | 3.100/Jahr | Mail, Branchensoftware | | Anfrage liegt im Postfach; im Mittel 2,3 Tage, bis sie gesichtet ist | angenommen |
| 2 Anforderung klären | Disponent | Rückfrage beim Kunden: Qualifikation, Schicht, Dauer, Sonderbedarf | 3.100 | Telefon | | Unklares Profil führt zu Fehlvorschlägen; jede zusätzliche Runde kostet den Kunden Sichtungszeit | angenommen |
| 3 Bestand durchsuchen | Disponent | Suche im ATS, in der eigenen Excel-Liste, im Kopf | 3.100 | ATS, Excel, keine standortübergreifende Suche | | Bei einem Drittel der Anfragen wird der Bestand faktisch übersprungen; die Anzeige wird sofort geschaltet: 387 Euro je Besetzung Anzeigenanteil | angenommen |
| 4 Anzeige schalten | Recruiter | Multiposting, wenn der Bestand nicht trägt | ca. 2.000 | Multiposting, **keine** Verbindung zum ATS | | Anzeige zweimal gepflegt; Bewerbung kommt ohne Quellenkennung zurück | angenommen |
| 5 Ansprache und Erstgespräch | Recruiter, Disponent | Kandidaten kontaktieren, Verfügbarkeit klären | — | Telefon, WhatsApp | | 2,6 Tage Warten auf Rückmeldung. Wer zwei Tage später anruft, erreicht einen Kandidaten, der zugesagt hat | angenommen |
| 6 Profil erstellen und senden | Disponent | Kundenunterlage aus dem Lebenslauf, 4,8 Profile je Besetzung | ca. 6.000 Profile | Word, Mail | | Ein schlecht passendes Profil kostet 3,1 Tage Kundenentscheidung und Glaubwürdigkeit | angenommen |
| 7 Vorstellung und Zusage | Kunde, Disponent | Kundenentscheidung, teils Vorstellungsgespräch | 1.240 Besetzungen | Mail, Telefon | ja, beim Kunden | — | angenommen |
| 8 Vertrag, Vorsorge, Arbeitsbeginn | Sachbearbeitung, Arbeitsmedizin | Vertrag, Unterlagen, Vorsorgetermin, Einweisung | 1.240 | Papier, Fremddienst | ja, Disponent | 2,6 Tage. 6 Prozent erscheinen am ersten Tag nicht: 380 Euro je Fall | angenommen / generiert |

### Mit Assistent, Ziel

Schritt 3 wird zu: Der Assistent durchsucht Bestand **und** Lebenslauf-Dateien standortübergreifend, liefert drei bis fünf Kandidaten mit Begründung und ausgewiesenen Lücken. Der Disponent prüft, ergänzt aus seiner Kenntnis des Kundenbetriebs und entscheidet. Schritt 6 nutzt einen Profilentwurf aus dem Lebenslauf, geprüft und freigegeben durch den Disponenten. Schritt 4 fällt für einen Teil der Anfragen weg, weil der Bestand vorher gesehen wurde — das ist der Posten, der die 480.000 Euro Anzeigenbudget senkt.

Schritte 1, 2, 7 und 8 bleiben unverändert. **Das ist keine Lücke, sondern der Befund:** 4,9 von 11 Tagen liegen in Schritten, die der Assistent nicht berührt. Wer das nicht vorher sagt, erklärt es hinterher.

Und ein Nebeneffekt, der in keiner Anbieterunterlage steht: Der Assistent kann nur strukturierte Qualifikationen verwerten. Damit bekommt die Datenpflege aus Schritt 3 erstmals einen Nutzen für die Person, die sie leisten soll. Das ist der einzige mir bekannte Weg, den Zielkonflikt aus dem Modulversagen 2023 aufzulösen — und er funktioniert nur, wenn der Assistent den Disponenten spürbar entlastet, bevor er ihn zur Pflege auffordert.

## Risikoeinschätzung nach EU AI Act

**Einordnung: Hochrisiko.** Nicht grenzwertig, nicht auslegungsbedürftig, sondern im Kern der Liste (`angenommen`, für Woche 5 mit dem Datenschutzbeauftragten zu prüfen):

- **Annex III Nummer 4** erfasst KI-Systeme in Beschäftigung und Personalmanagement, ausdrücklich für die Suche und Auswahl von Bewerbern, die Filterung von Bewerbungen und die Bewertung von Kandidaten. Ein System, das Kandidaten für eine Stelle vorschlägt und dabei implizit alle anderen nicht vorschlägt, ist genau das.
- **Der menschliche Klick befreit nicht.** Wirksame menschliche Aufsicht im Sinne des AI Act verlangt, dass der Disponent den Vorschlag überprüfen und begründet abweichen **kann** — also die Begründung des Systems versteht und die nicht vorgeschlagenen Kandidaten sieht. Ein Assistent, der eine Liste ohne Begründung ausgibt, erfüllt das nicht, auch wenn ein Mensch bestätigt.
- **Pflichten, die daraus folgen:** Risikomanagementsystem, Datengovernance mit dokumentierter Repräsentativität der Trainingsdaten, technische Dokumentation, Protokollierung der Vorschläge, Transparenz gegenüber betroffenen Bewerbern, Registrierung, Konformitätsbewertung. Der Anbieter trägt einen Teil, GeAT als Betreiber den Rest — und die Aufteilung gehört in den Vertrag, nicht in ein Protokoll.
- **Daneben, unabhängig vom AI Act:** Art. 22 DSGVO bei automatisierten Einzelentscheidungen, § 26 BDSG, das AGG bei jeder Auswahlentscheidung, und § 87 BetrVG, weil ein System, das Vorschläge und Ablehnungen protokolliert, technisch geeignet ist, Verhalten und Leistung der Disponenten zu überwachen.
- **Der Bias-Fall ist konkret, nicht theoretisch:** 20,4 Prozent der neu eingestellten Zeitarbeitnehmer waren zuvor länger als ein Jahr arbeitslos oder noch nie beschäftigt, 28,8 Prozent haben keinen Berufsabschluss (`öffentlich`, GVP 2025). Ein Modell, das auf vergangene erfolgreiche Besetzungen optimiert, ordnet genau diese Gruppen nach unten — und reproduziert damit die Vorauswahl der Kundenbetriebe, statt sie zu prüfen. Zeitarbeit trägt 10,8 Prozent der Übergänge aus Langzeitarbeitslosigkeit in Beschäftigung. Was das Modell wegsortiert, ist der arbeitsmarktpolitische Beitrag des Geschäftsmodells.

**Die Doppelrolle der Aufsicht** gehört in dieselbe Einordnung: Die Erlaubnis zur Arbeitnehmerüberlassung erteilt und überwacht die Bundesagentur für Arbeit (`öffentlich`, Impressum). Dieselbe Organisation ist im Vermittlungsmarkt Akteur. Ein Konformitätsmangel bei einem Hochrisikosystem in der Bewerberauswahl ist damit nicht nur ein Bußgeldrisiko, sondern berührt die Erlaubnis, von der das gesamte Geschäft abhängt. Das ist das stärkste Argument im Business Case und wird in Anbietergesprächen nie erwähnt.

## Parallele Initiativen

| Initiative | Verantwortlich | Status | Budget | Konkurriert um | Herkunft |
|---|---|---|---:|---|---|
| **Migration der Branchensoftware 2027** | Geschäftsführer Finanzen/IT | Anbieterauswahl läuft, Umstieg Q1 2027 | 620.000 | die 1,5 IT-Stellen, die Sachbearbeitung Lohn, die Aufmerksamkeit der Gesellschafter — und dieselben Datenfelder, die der Pilot strukturieren will | angenommen |
| Eröffnung Niederlassung Halle (Saale) | Vertriebsleitung | genehmigt, Start Q2 2027 | 240.000 | Vertriebszeit und zwei Disponenten, die aus dem Bestand kommen sollen | generiert |
| Ausbau GeAT Academy | Leiterin Academy | Konzept in Arbeit, kein Budget | 0 | die Qualifizierungsargumentation, die auch der Pilot braucht | generiert |
| Nachfolge Niederlassungsleitung und Senior-Disposition | internes Personal | kein Beschluss | 0 | die vier Senior-Disponenten, deren Wissen auch der Pilot als Trainingsgrundlage braucht | angenommen |
| ISO 9001 Rezertifizierung und GVP-Audit | Qualitätsbeauftragte | Audit Q2 2027 | 30.000 | Prozessbeschreibungen: der Besetzungsprozess muss dokumentiert werden, wie er ist, nicht wie er werden soll | generiert |

**Die erste Zeile ist die harte.** Die Migration bindet nicht nur die Menschen, sie berührt denselben Datenbestand. Zwei Möglichkeiten, und beide sind vertretbar: die Qualifikationsfelder vor der Migration strukturieren, damit sauber übernommen wird — oder danach, damit nicht zweimal gearbeitet wird. Die Entscheidung ist ein Programmthema für Woche 11 und keine technische Frage.

## Eskalationsweg

Wer entscheidet, wenn der Assistent etwas Falsches tut (`angenommen`):

1. **Unpassender Vorschlag oder fehlerhaftes Profil im Entwurf.** Der prüfende Disponent korrigiert, gibt nicht frei und trägt den Fall in eine Fehlerliste ein. Der Kunde sieht nichts — die Freigabe ist der Kontrollpunkt. Wöchentliche Durchsicht der Liste durch die Leiterin Recruiting Center.
2. **Gehäufte Fehlvorschläge, ein Muster in der Fehlerliste, oder ein Verdacht auf systematische Benachteiligung einer Gruppe.** Vertriebsleitung und Leiterin Recruiting Center gemeinsam, innerhalb von zwei Arbeitstagen, unter Beteiligung des Datenschutzbeauftragten. Sie entscheiden, ob der Assistent für eine Berufsgruppe oder Niederlassung pausiert. **Ein Verdacht auf Diskriminierung führt zur Pause, nicht zur Prüfung mit laufendem Betrieb.**
3. **Beschwerde eines Bewerbers, Datenabfluss, Anfrage der Aufsicht, oder Uneinigkeit auf Stufe 2.** Geschäftsführung am nächsten Dienstag, mit Betriebsrat, sobald Beschäftigtendaten betroffen sind, und mit einer schriftlichen Stellungnahme des Datenschutzbeauftragten. Bei Berührung der Erlaubnis nach AÜG informiert die Geschäftsführung die Gesellschafterversammlung außerhalb des Turnus.

**Offen für Woche 11:** Stufe 2 setzt voraus, dass die beiden Rollen mit den unvereinbaren Zielen gemeinsam entscheiden — Rehberg ist nicht dabei, obwohl seine Niederlassung betroffen wäre. Das ist Absicht und ein Risiko. Und Stufe 1 verlässt sich darauf, dass ein Disponent einen Fehler des Systems einträgt, der ihm Arbeit macht und ihn nichts kostet, wenn er ihn nicht einträgt. Wer die Fehlerliste zur Pflicht macht, ohne sie zu belohnen, bekommt eine leere Liste und hält sie für ein gutes Ergebnis.
