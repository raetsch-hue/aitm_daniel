# Systeme und Daten: GeAT mbH

> Anbieternamen sind weggelassen, weil sie nicht belegbar sind. Welche Branchensoftware GeAT tatsächlich einsetzt, ist die wertvollste offene Rechercheposition (siehe [`recherche.md`](recherche.md), Punkt 4): Sie entscheidet über Schnittstellenfähigkeit und damit über zwei Drittel des Pilotaufwands. Alle Angaben dieser Datei tragen `angenommen` oder `generiert`.

## Systeme

| System | Zweck | Seit | Betrieb | Schnittstellen | Herkunft |
|---|---|---|---|---|---|
| **Branchensoftware Personaldienstleistung** | Bewerber, Kunden, Einsätze, Zeiterfassung, Lohnabrechnung, Fakturierung — das führende System | 2013, mehrfach erweitert | beim Anbieter gehostet | Datenexport nach Excel; **keine offene API im Bestandsvertrag**. Ablösung bzw. Versionswechsel für 2027 beschlossen | angenommen |
| **Bewerbermanagement-Modul (ATS)** | strukturierte Qualifikationsfelder, Bewerberportal, Statusverfolgung | 2023 | Modul der Branchensoftware | intern verbunden. **Keine** Verbindung zum Multiposting-Werkzeug | angenommen |
| **Multiposting für Stellenanzeigen** | Anzeigen gleichzeitig an Jobbörsen und Website | 2021 | Cloud | **keine.** Jede Anzeige wird zweimal gepflegt, Bewerbungen kommen ohne Quellenkennung zurück | angenommen |
| Microsoft 365 (Mail, Teams, Dateiablage) | Kommunikation, Dokumente, Videogespräche | 2020 | Cloud | keine zur Branchensoftware | angenommen |
| Zeiterfassung Zeitarbeitnehmer | Nachweis geleisteter Stunden je Einsatz | — | **Papier** | Stundenzettel werden abgetippt. 22 Prozent nachträglich korrigiert | angenommen |
| Lohnsteuer- und Meldewesen | Meldungen, Bescheinigungen | — | Modul plus Steuerberatung für den Jahresabschluss | Datei-Übergabe monatlich | angenommen |
| Website mit Jobportal | Anzeigen, Initiativbewerbung | laufend gepflegt | Cloud, Agentur | Bewerbung kommt als E-Mail mit PDF an | angenommen |
| CRM | **existiert nicht.** Kundenkontakte liegen in der Branchensoftware, Historie und Absprachen in persönlichen Outlook-Ordnern | | | angenommen |
| Business Intelligence / Data Warehouse | **existiert nicht.** Alle Auswertungen sind Excel-Exporte, 14 Berichte im Monatsrhythmus, je Niederlassung teils eigene Fassungen | | | angenommen |

**Der Exportdateien-Test:** 14 von 14 steuerungsrelevanten Auswertungen beruhen auf einem manuellen Export. Damit ist die Frage nach der Cloud-/API-Welle entschieden, unabhängig davon, wie viele Cloud-Lizenzen im Haus sind.

## Datenbestände

| Bestand | System | Verantwortliche Rolle | Qualitätsbefund (ein konkreter Mangel) | Personenbezogen | Herkunft |
|---|---|---|---|---|---|
| **Bewerberprofile** | Branchensoftware / ATS | niemand formal. Faktisch das Recruiting Center | **41.000 Profile, 63 Prozent ohne strukturierte Qualifikationsfelder.** Das Können steht im PDF-Lebenslauf im Freitext. Die Qualifikation „Staplerschein" existiert in elf Schreibweisen | ja | angenommen |
| **Speicherfristen Bewerberdaten** | Branchensoftware | Datenschutzbeauftragter (extern, beratend) | **18.000 Profile sind älter als die den Bewerbern zugesagte Speicherdauer.** Ein Löschkonzept liegt als Dokument vor und ist nicht in Betrieb | ja | angenommen |
| Qualifikationsnachweise | Papierakte, Netzlaufwerk, teils ATS | Niederlassung | Schweißerprüfungen, Staplerscheine, Führerscheine, Gesundheitsnachweise als Scan ohne Ablaufdatum im Feld. Gültigkeit wird beim Einsatz telefonisch erfragt | ja, teils Gesundheitsdaten | angenommen |
| Kundendaten und Anforderungshistorie | Branchensoftware plus persönliche Outlook-Ordner | Vertrieb | Rund die Hälfte der Absprachen zu Anforderungsprofilen liegt nur im Postfach der zuständigen Person. Bei Personalwechsel geht sie verloren | ja, Ansprechpartner | angenommen |
| Einsatz- und Zeitdaten | Branchensoftware, Papierzettel, Messenger-Fotos | Sachbearbeitung Einsatz | 22 Prozent der Zeitnachweise werden nachträglich korrigiert. Vier Tage Klärungsaufwand pro Monat | ja, Zeitarbeitnehmer | angenommen |
| Besetzungshistorie | Branchensoftware | Controlling | Vorhanden und datiert, aber **ohne Grund der Nichtbesetzung**. Für ein Modell, das aus Erfolg und Misserfolg lernen soll, fehlt damit die Zielgröße | ja | angenommen |
| Anzeigenwirkung | Multiposting-Werkzeug, getrennt | Vertrieb | Keine Zuordnung zwischen Anzeigenquelle und Besetzung, weil die Bewerbung ohne Quellenkennung im System landet. 480.000 Euro ohne Wirkungsnachweis | nein | angenommen |
| Personalakten Stammpersonal | Branchensoftware, Papierakte | internes Personal | vollständig | ja, Beschäftigte | angenommen |

**Der Bestand, der den Piloten gefährdet, ist nicht der größte, sondern der leere:** Die Besetzungshistorie enthält, wer besetzt wurde, aber nicht, warum die anderen 1.860 Anfragen nicht besetzt wurden. Ohne diese Zielgröße kann kein Modell Besetzungswahrscheinlichkeit lernen — es kann nur Ähnlichkeit zu früheren Besetzungen messen. Das ist ein anderer Gegenstand, und es ist der Grund, warum das Vorhaben mit strukturierter Erfassung anfangen muss und nicht mit einem Modell.

## Wissensquellen

Was ein Assistent lesen müsste, um eine Anfrage zu besetzen — und in welchem Zustand es ist.

| Quelle | Inhalt | Zustand | Herkunft |
|---|---|---|---|
| Bewerberprofile im ATS | 41.000 Profile, davon 15.000 mit strukturierten Feldern | siehe oben: 63 Prozent unstrukturiert, Schreibweisen uneinheitlich | angenommen |
| Lebenslauf-PDF | der eigentliche Inhalt: Tätigkeiten, Branchen, Maschinen, Schichtbereitschaft | 41.000 Dateien, kein Textindex, gescannte Dokumente teils ohne Texterkennung | angenommen |
| Anforderungsprofile der Kunden | was ein Kundenbetrieb tatsächlich braucht, jenseits der Stellenbezeichnung | in Postfächern und in Köpfen. Kein Feld im System | angenommen |
| Kandidatenlisten der Niederlassungen | wer gerade verfügbar ist, wer wo schon war, wer mit wem nicht kann | sieben Excel-Dateien, sieben Formate, kein Zugriff über Standortgrenzen | angenommen |
| Köpfe | Kenntnis der Kundenbetriebe: Meister, Schichtklima, Anforderungen zwischen den Zeilen | vier Senior-Disponenten, zwei über 58 | angenommen |
| Pinnwand-Ausdruck in der Sachbearbeitung | welcher Kundenbetrieb welches Zeitnachweis-Format akzeptiert | eine Person, ein Ausdruck, keine Kopie | angenommen |
| Prompt-Sammlung einer Recruiterin | funktionierende Textbausteine für Anzeigen und Profilzusammenfassungen | privat, außerhalb des Unternehmens, nicht geteilt | angenommen |

## Schatten-IT

| Was | Wer | Warum | Herkunft |
|---|---|---|---|
| **Privater KI-Zugang für Anzeigentexte und Profilzusammenfassungen** | neun Personen im Recruiting und Innendienst, überwiegend unter 35 | schneller als die Textbausteine. Niemand hat es verboten, niemand hat es erlaubt. **Lebensläufe werden dabei eingefügt** | angenommen |
| Sieben Kandidatenlisten in Excel | Niederlassungen | „Das System zeigt nicht, wer nächste Woche frei ist." Die Verfügbarkeit steht nirgends als Feld | angenommen |
| WhatsApp-Gruppen je Niederlassung, mit Zeitarbeitnehmern darin | Disponenten und rund 300 Zeitarbeitnehmer | einziger Kanal, der zuverlässig ankommt. Darin: Einsatzabsprachen, Fotos von Stundenzetteln, gelegentlich Krankmeldungen | angenommen |
| Persönliche Outlook-Ordner als Kundenhistorie | Vertrieb, Niederlassungsleitungen | es gibt kein CRM | angenommen |
| Kalkulations-Excel für Verrechnungssätze | Vertrieb, Niederlassungsleitungen | fünf Fassungen im Umlauf, keine als gültig gekennzeichnet | generiert |

Die erste und die dritte Zeile sind derselbe Befund in zwei Formen: personenbezogene Daten verlassen das Unternehmen über Kanäle, für die es keinen Auftragsverarbeitungsvertrag gibt. Das ist der Punkt, an dem das Vorhaben von einem Effizienzthema zu einem Compliance-Thema wird — und der Punkt, an dem es leichter zu begründen ist, weil ein erlaubter Weg den unerlaubten ersetzt.

## Auftragsverarbeiter

| Dienst | Verarbeitet | Vertrag zur Auftragsverarbeitung | Herkunft |
|---|---|---|---|
| Anbieter der Branchensoftware (Hosting) | Bewerber-, Beschäftigten- und Kundendaten vollständig | ja | angenommen |
| Multiposting-Anbieter | Anzeigendaten, Bewerberkontakte im Rücklauf | ja | angenommen |
| Jobbörsen und Indeed | Bewerberkontakte | ja, über die jeweiligen Nutzungsbedingungen | angenommen |
| Microsoft 365 | Mail, Dokumente, Ansprechpartnerdaten | ja | angenommen |
| Arbeitsmedizinischer Dienst | Gesundheitsdaten der Zeitarbeitnehmer | ja | angenommen |
| Steuerberatung | Lohn- und Beschäftigtendaten | ja | angenommen |
| Website-Agentur | Bewerbungen über das Jobportal | unklar, nie geprüft | generiert |
| **Privater KI-Zugang der Beschäftigten** | Lebensläufe mit Namen, Anschrift, Qualifikation | **nein.** Das ist der Befund für Woche 5 | angenommen |
| **WhatsApp-Gruppen** | Kontaktdaten und Gesundheitsangaben von rund 300 Zeitarbeitnehmern | **nein** | angenommen |
