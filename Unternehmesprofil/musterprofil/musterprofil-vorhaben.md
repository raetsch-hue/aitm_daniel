# Vorhaben: Mustermann Antriebstechnik GmbH

## Das Vorhaben

**Assistent für die Angebotsvorbereitung bei Sonderanfertigungen.** Aus einer Kundenanfrage, dem Angebotsarchiv und den Stücklisten vergleichbarer Antriebe erzeugt ein Assistent einen Angebotsentwurf: drei bis fünf Referenzangebote mit Abweichungen, einen Kalkulationsvorschlag auf Basis der gültigen Vorlage und einen Textentwurf. Die Konstruktion prüft und entscheidet, der Innendienst schickt. Kein Angebot verlässt das Haus ohne Freigabe eines Menschen (angenommen, aus Auftrag 2 von Tag 1.4).

Der Pilot wurde auf Tag 1.4 gegen den Reifegrad gewählt: Daten 2 und Kultur 2 schließen einen Assistenten aus, der selbst entscheidet. Ein Assistent, der Referenzen findet und vorrechnet, funktioniert auf dem gemessenen Stand, wenn das Angebotsarchiv vorher aufbereitet wird.

| Angabe | Wert | Herkunft |
|---|---|---|
| Betroffene Prozesse | Angebot Sonderanfertigung, nachgelagert Konstruktion | angenommen |
| Betroffene Rollen | 28 Innendienst, 45 Konstruktion, davon zunächst 6 Innendienst und 8 Konstruktion im Pilot | angenommen |
| Ziel in einem Jahr: Durchlaufzeit | 6 Arbeitstage auf 3 | angenommen |
| Ziel in einem Jahr: Konstruktionsaufwand je Angebot | 3,5 Stunden auf 2 | angenommen |
| Ziel in einem Jahr: Nacharbeit | 18 Prozent auf 10 | angenommen |
| Nicht Ziel | Erfolgsquote. Sie hängt auch am Preis, und den macht der Pilot nicht | angenommen |
| Pilotdauer | 6 Monate, danach Entscheidung über Ausweitung auf alle Kundengruppen | generiert |

## Workflows

### Anfrage bis Angebot (heute)

| Schritt | Wer | Auslöser und Ergebnis | Volumen | Schnittstelle | Freigabe | Was ein Fehler kostet | Herkunft |
|---|---|---|---|---|---|---|---|
| 1 Anfrage erfassen | Innendienst | Mail oder Anruf des Kunden, Anlage im CRM oder Excel | 2.400 pro Jahr | CRM, Mail | | Doppelerfassung, verlorene Anfrage | angenommen |
| 2 Sichtung | Innendienst mit Konstruktion | Machbar oder nicht, 500 werden abgelehnt | 2.400 | keine, Zuruf | | Abgelehnte Anfrage, die machbar gewesen wäre: ein verlorener Auftrag, 60.000 Euro | angenommen |
| 3 Technische Bewertung | Konstruktion | Referenz suchen (Archiv, Kopf), Auslegung grob, Stückliste ableiten | 1.900 | PDM lesen, Archiv suchen | | 3,5 Stunden, bei falscher Referenz Nacharbeit 380 Euro | angenommen |
| 4 Kalkulation | Innendienst | Excel-Vorlage, Zuschläge, Preis | 1.900 | keine, Excel | | Falsche Vorlage: Angebot mit altem Materialpreis, im Mittel 4 Prozent zu billig | angenommen |
| 5 Freigabe | Vertriebsleiter über 50.000 Euro, GF über 250.000 Euro | Unterschrift | rund 900 über 50.000 | Mail | ja | Wartezeit 1 bis 3 Tage | angenommen |
| 6 Versand und Nachfassen | Innendienst | PDF an Kunden, Ablage im Archiv, Nachfassen nach 10 Tagen | 1.900 | Mail, Laufwerk | | Angebot ohne Metadaten im Archiv, für die nächste Anfrage nicht auffindbar | angenommen |

### Mit Assistent (Ziel)

Schritt 3 wird zu: Assistent liefert Referenzen und Kalkulationsvorschlag, Konstruktion prüft in 2 Stunden statt 3,5. Schritt 4 nutzt den Vorschlag, die Vorlage wird auf eine gültige Version gezwungen. Schritt 6 legt das Angebot mit Metadaten ab, damit das Archiv besser wird, je länger der Assistent läuft. Schritte 1, 2 und 5 bleiben unverändert: die Freigabe durch einen Menschen ist der Kontrollpunkt (angenommen).

## Risikoeinschätzung nach EU AI Act

Erste Einordnung, für Woche 5 zu prüfen (angenommen):

- **Der Assistent selbst:** begrenztes oder minimales Risiko. Er bereitet ein B2B-Angebot vor, entscheidet nicht über Personen, und ein Mensch gibt frei.
- **Was das Risiko erhöht:** sobald das System auswertet, welcher Konstrukteur wie schnell oder wie oft korrigiert, wird es zu einem System, das Leistung von Beschäftigten bewertet. Das ist der Bereich, den Annex III nennt, und der Punkt, an dem der Betriebsrat eine Betriebsvereinbarung verlangt. Das Vorhaben schließt solche Auswertungen aus, und das muss in der Vereinbarung stehen.
- **Datenschutz:** Kundenanfragen enthalten Ansprechpartner. Der Anbieter des Assistenten wird Auftragsverarbeiter, die private KI-Nutzung im Innendienst hört mit dem Pilot auf, weil es dann einen erlaubten Weg gibt.

## Parallele Initiativen

| Initiative | Verantwortlich | Status | Budget | Konkurriert um | Herkunft |
|---|---|---|---|---|---|
| ERP-Upgrade 2027 | GF Technik | Anbieterauswahl läuft, Start Q1 2027 | 1,8 Mio | die drei IT-Leute, die Arbeitsvorbereitung, die Aufmerksamkeit des Beirats | angenommen |
| Halle 3 in Ostrava | Werksleiter Ostrava | genehmigt, Bau ab Q4 2026 | 2,4 Mio (Kredit, außerhalb des Spielraums) | Aufmerksamkeit der GF-Runde | angenommen |
| CRM-Neustart | Vertriebsleiter | ruht seit 2024, kein Budget | 0 | denselben Innendienst, dasselbe Reizwort | angenommen |
| Nachfolge Konstruktion | Personalleitung | Konzept in Arbeit, kein Beschluss | 0 | die beiden Senior-Konstrukteure, deren Zeit auch der Pilot braucht | angenommen |
| ISO 9001 Rezertifizierung | Qualitätsmanagement | Audit Q4 2026 | 40.000 | Prozessbeschreibungen: der Angebotsprozess muss dokumentiert werden, so wie er ist, nicht wie er wird | generiert |

## Eskalationsweg

Wer entscheidet, wenn der Assistent etwas Falsches liefert, in drei Stufen (angenommen):

1. **Falsche Referenz oder Kalkulation im Entwurf:** die prüfende Konstrukteurin oder der Innendienst korrigiert und meldet den Fall in einer Liste. Kein Angebot geht ungeprüft raus, also kein Schaden beim Kunden.
2. **Gehäufte Fehler oder ein Angebot, das trotz Prüfung falsch rausging:** Vertriebsleiter und Konstruktionsleiter gemeinsam, innerhalb von zwei Tagen. Sie entscheiden, ob der Assistent für eine Kundengruppe pausiert.
3. **Schaden beim Kunden, Datenabfluss oder Streit zwischen Stufe 2:** GF-Runde am nächsten Montag, mit Betriebsrat, wenn Beschäftigtendaten betroffen sind.

Offen für Woche 11: Stufe 2 setzt voraus, dass die beiden Rollen mit den unvereinbaren Zielen gemeinsam entscheiden. Das ist Absicht und ein Risiko.
