# Systeme und Daten: Mustermann Antriebstechnik GmbH

Anbieternamen sind weggelassen. In deinem Profil dürfen sie stehen, wenn sie öffentlich belegt sind (Stellenanzeigen nennen sie meist).

## Systeme

| System | Zweck | Seit | Betrieb | Schnittstellen | Anbieter | Herkunft |
|---|---|---|---|---|---|---|
| ERP | Auftrag, Disposition, Einkauf, Lager, Finanzbuchhaltung, Artikelstamm | 2009, stark angepasst | Rechenzentrum im Haus | zum Lohnsystem des Dienstleisters; **keine** zur Konstruktionsdatenverwaltung | deutscher Mittelstandsanbieter, Upgrade auf aktuelle Version für 2027 geplant | angenommen |
| Konstruktionsdatenverwaltung (PDM) mit CAD | Zeichnungen, Stücklisten, Freigaben | 2015 | im Haus | keine. Stücklisten werden nach Freigabe von Hand ins ERP übertragen, rund 40 Minuten je Sonderantrieb | CAD-Anbieter | angenommen |
| CRM | Kontakte, Besuchsberichte, Chancen | 2022 | Cloud | zum ERP nur Kundenstamm, einmal nachts | Cloud-Anbieter | angenommen |
| Zeiterfassung und Zutritt | Beschäftigtendaten | 2018 | im Haus | zum Lohnsystem | Spezialanbieter | angenommen |
| Bürosoftware mit Mail und Dateiablage | Mail, Dokumente, Videokonferenz | 2020 | Cloud | | großer Anbieter | angenommen |
| Dokumentenlaufwerk „Angebote" | Angebotsarchiv als PDF, je Kunde ein Ordner | seit 2011 | Dateiserver im Haus, seit 2020 teils in der Cloud-Ablage gespiegelt | keine | | angenommen |
| Ticketsystem Service | Störungen, Einsätze, Ersatzteile | 2021 | Cloud | keine zum ERP, Ersatzteile werden abgetippt | Cloud-Anbieter | generiert |
| Konstruktionswiki | Auslegungswissen, 80 Seiten | 2019, seit 2020 ungepflegt | im Haus | | Open-Source-Wiki | angenommen |

## Datenbestände

| Bestand | System | Verantwortliche Rolle | Qualitätsbefund (ein konkreter Mangel) | Personenbezogen | Herkunft |
|---|---|---|---|---|---|
| Artikelstamm | ERP | niemand formal. Faktisch Arbeitsvorbereitung | Geschätzt 12 Prozent Dubletten, weil Sonderteile bei jeder Anfrage neu angelegt werden, statt bestehende zu suchen | nein | generiert (Schätzung der IT-Leitung, nie gemessen) |
| Angebotsarchiv | Dokumentenlaufwerk | Vertriebsinnendienst | 14.000 PDF ohne Metadaten. Preisstände darin bis zu 14 Jahre alt, ohne Kennzeichnung, welcher Preis aktuell wäre. Für einen Assistenten, der Referenzangebote finden soll, ist das die Hauptquelle und das Hauptrisiko | Ansprechpartner der Kunden im Kopf jedes Angebots | angenommen |
| Stücklisten | PDM und ERP doppelt | Konstruktion (PDM), Arbeitsvorbereitung (ERP) | Versionsstand stimmt bei geschätzt jedem zehnten Sonderantrieb nicht überein, fällt in der Montage auf | nein | angenommen |
| Kundendaten | CRM und Excel-Listen des Außendiensts | Vertrieb | 30 Prozent im CRM gepflegt, der Rest in acht persönlichen Excel-Dateien, teils mit Privatnummern der Ansprechpartner | ja | angenommen |
| Zeiterfassung | Zeiterfassungssystem | Personal | vollständig, aber nur über den Dienstleister auswertbar | ja, Beschäftigte | angenommen |
| Serviceberichte | Ticketsystem und Messenger-Gruppe | Service | Freitext, Fotos im Messenger, nicht durchsuchbar | teils, Namen von Kundentechnikern | generiert |

## Wissensquellen

Was ein Assistent lesen müsste, um ein Angebot vorzubereiten, und in welchem Zustand es ist.

| Quelle | Inhalt | Zustand | Herkunft |
|---|---|---|---|
| Angebotsarchiv | 14.000 Angebote seit 2011 | siehe oben: keine Metadaten, alte Preise | angenommen |
| Kalkulationsvorlagen | Excel mit Makros, Zuschlagsätze, Stundensätze | Neun Versionen im Umlauf, keine als gültig gekennzeichnet | angenommen |
| Konstruktionswiki | 80 Seiten Auslegungsregeln | Stand 2020, teils überholt durch neue Lagerbaureihe | angenommen |
| Postfächer der beiden Senior-Konstrukteure | Anfragen, Rückfragen, Auslegungsentscheidungen der letzten 15 Jahre | vollständig, aber persönlich und nicht zugänglich | angenommen |
| Köpfe | Auslegungserfahrung, Kundenhistorie, „das haben wir 2014 schon einmal so gebaut" | Zwei Personen, Rente 2027 und 2028 | angenommen |

## Schatten-IT

| Was | Wer | Warum | Herkunft |
|---|---|---|---|
| Kalkulations-Excel in neun Versionen | Innendienst, Konstruktion | Die offizielle Vorlage im ERP kann keine Sonderpositionen | angenommen |
| Privater KI-Chat für Angebotstexte | Sachbearbeiterin Innendienst und vier weitere unter 35 | Schneller als die Textbausteine, niemand hat es verboten, niemand hat es erlaubt. Kundenanfragen werden dabei eingefügt | angenommen |
| Acht Excel-Listen mit Kundendaten | Außendienst | Das CRM „ist zu langsam unterwegs" | angenommen |
| Messenger-Gruppe Service | 40 Personen Service und Montage | Fotos von Typenschildern, Absprachen, schneller als das Ticketsystem | generiert |

## Auftragsverarbeiter

| Dienst | Verarbeitet | Vertrag zur Auftragsverarbeitung | Herkunft |
|---|---|---|---|
| Cloud-Bürosoftware | Mail, Dokumente, Ansprechpartnerdaten | ja | angenommen |
| CRM-Anbieter | Kundendaten mit Ansprechpartnern | ja | angenommen |
| Lohnabrechnung (Steuerberatung) | Beschäftigtendaten | ja | angenommen |
| Ticketsystem Service | Namen von Kundentechnikern in Freitexten | unklar, nie geprüft | generiert |
| Privater KI-Chat der Innendienstkräfte | Kundenanfragen mit Ansprechpartnern | nein. Das ist der Befund für Woche 5 | angenommen |
