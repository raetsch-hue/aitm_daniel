---
artefakt: Entscheidungsvorlage — freigegebener KI-Zugang, Stufe 1
kette: W03 A · KI-Analyse — Glied 5 von 6
baut_auf: w03A-4-use-case-und-sensitivitaet.md (Prüfung) · w03A-3-ki-analyse-fassung-2-gueltig.md (Gewichtung und Scores)
basis_fuer: w03A-6-pitch-c-level.md
woche: 03
datum: 2026-09-10
status: Entwurf zur Vorlage in der Geschäftsführung. Nicht beschlossen
zweck: eine Handlungsempfehlung, die einer Entscheidungsträgerin hingelegt werden kann — zwei Seiten
adressat: Geschäftsführung (Rolle 1 und Rolle 2), zur Kenntnis Rolle 13
herkunft: abgeleitet. Alle Beträge sind `angenommen` oder `generiert`, alle Scores sind Einschätzungen auf Herstellerunterlagen. Kein Angebot liegt vor
---

# Entscheidungsvorlage: freigegebener KI-Zugang

**An:** Geschäftsführung · **Von:** Rolle 15 · **Datum:** 2026-09-10
**Entscheidungsbedarf:** Geschäftsführungsbeschluss, ≤ 9.000 € im Jahr — unter der
25.000-Euro-Grenze, also ohne Gesellschafterversammlung.

> **In einem Satz:** Wir beschaffen keine KI-Funktion, wir beenden eine laufende Verarbeitung ohne
> Rechtsgrundlage — neun Beschäftigte arbeiten heute mit privaten KI-Konten und Bewerberlebensläufen
> darin, ohne Auftragsverarbeitungsvertrag.

## 1 · Empfehlung, und woran wir sie gemessen haben

**Empfehlung:** integrierte EU-Plattform (Typ Langdock), Multi-Tenant SaaS, modellagnostisch —
**20 Seats über drei Standorte:** Recruiting Center Erfurt (9), Gotha (4), übrige Niederlassungen
und Innendienst (7). Beginnend mit den neun heutigen Schatten-Nutzern.

**Gemessen an acht Kriterien, gewichtet vor dem Bewerten und am 2026-09-07 fixiert:**

| Kriterium | Gewicht | Warum dieses Gewicht |
|---|---:|---|
| Compliance und AVV | **25 %** | Es wird kein Vorhaben reguliert, sondern ein laufender Zustand beendet |
| Verfügbarkeit gegen die Taktgrenze | **20 %** | Jeder Monat ohne Ersatz ist ein Monat Verarbeitung ohne AVV |
| Adoption, Einführungsaufwand, Support | **17 %** | Ein dokumentierter Adoptionsfehlschlag 2023 in genau dieser Werkzeugklasse |
| Kosten über drei Jahre | **15 %** | EBIT-Marge 2,6 %; freier Spielraum 185.000 €, nicht 280.000 |
| Betriebsaufwand bei 1,5 IT-Stellen | **11 %** | Beide Stellen sind bis Q1/2027 durch die Migration gebunden |
| Exit und Portabilität | **6 %** | Das Kernsystem wird Q1/2027 ersetzt |
| RAG und Integrationstiefe | **4 %** | Die Voraussetzung fehlt: 63 % der Profile ohne strukturiertes Können, keine offene API |
| Deployment-Flexibilität | **2 %** | Bei 20 Seats liefert jeder Anbieter dasselbe Multi-Tenant-SaaS — trennt nicht |

**Ergebnis:** EU-Plattform **3,49** · Microsoft Copilot for M365 **3,09** · Nullvariante **2,32** ·
Branchensoftware 2027 **2,32** · Google Vertex AI (Cloud-ML, Eigenbau) **1,78**.

**Und die Probe, die aus dem Score eine Empfehlung macht:** Jedes Gewicht um ±10 Prozentpunkte
verschoben — der Sieger hält in **allen 16 Varianten**, auch wenn Compliance auf null gesetzt wird.
Er kippt erst, wenn *Adoption und Einführungsaufwand* von 17 auf **31 %** steigen; dann wäre
Copilot richtig.

## 2 · Was dagegen spricht

| Einwand | Antwort |
|---|---|
| **„Wieder ein Werkzeug, das niemand benutzt."** 2023: 95.000 € über drei Jahre, 34 % Nutzung, erstmals 2026 gemessen — und nur wegen eines ISO-Audits | Der Einwand ist berechtigt und der stärkste hier. Zwei Unterschiede: **die neun Nutzer sind Nutzer, bevor etwas eingeführt wird** — es wird kein Bedarf geweckt, sondern ein bestehender legalisiert. Und es gibt ein Abbruchkriterium, vorher festgelegt: **nach drei Monaten null Lebensläufe in Diensten ohne AVV und mindestens zwei von drei Standorten in wöchentlicher Nutzung.** Sonst wird abgeschaltet und der Grund protokolliert |
| **„Keine zweite Baustelle vor der Migration."** Beide IT-Stellen sind bis Q1/2027 gebunden | Trifft den Betriebsaufwand, nicht den Aufbau: **maximal 10 Stunden IT**, kein Entwicklungsauftrag, keine Schnittstelle. Die Plattform hängt **nicht** an der Branchensoftware und überlebt den Systemwechsel — deshalb ist sie keine Altlast, sondern die einzige Option, die den Wechsel übersteht |
| **„Amortisation unter 24 Monaten oder wartet."** | Stufe 1 ist kein Investitionsfall. 9.000 € im Jahr beenden ein Rechtsrisiko — Amortisation ist hier die falsche Kennzahl. Die Amortisation wird an der **nächsten** Stufe nachgewiesen, an einem Posten, bei dem sie nicht bestritten werden kann. Wer sie schon hier verlangt, verschiebt den Rechtsverstoß um ein Quartal |
| **„Wir haben Microsoft 365 doch schon."** | Der vorhandene AVV ist ein echter Vorteil, und der Score von 3,09 ist nah dran. Aber: **Microsoft Graph erreicht die 41.000 Bewerberprofile nicht, weil sie nicht in M365 liegen** — der stärkste Punkt der Plattform greift bei unserem Bestand nicht. Und für alle 69 Stammkräfte kostet Copilot 24.840 € im Jahr: 160 € unter der Freigabegrenze und praktisch der gesamte Projektposten des IT-Budgets 2026 |

## 3 · Die ersten 90 Tage

| Feld | Was passiert | Beleg |
|---|---|---|
| **Einstiegsphase** | 20 Seats über drei Standorte, ≤ 9.000 €/Jahr. Drei Tore **vor** Vertragsschluss: AVV vorgelegt · Protokollierung begrenzbar, Betriebsvereinbarung mit dem Betriebsrat · EU-Verarbeitung und nachweisbare Löschung. Vergabebedingung: Modelle jederzeit auf dem Stand der öffentlich verfügbaren Spitzenmodelle — sonst wandert die Nutzung zurück | Stufe 1 mit 22.000 € im korrigierten Spielraum von 185.000 € (`gerechnet`, nach Abzug der 620.000 € Migrationsreserve) |
| **Datenarbeit** | **Löschung vor Extraktion:** die 18.000 Profile über der zugesagten Speicherdauer werden gelöscht, **bevor** irgendetwas strukturiert wird. Spart rund 24.000 € und verhindert, dass eine unzulässige Verarbeitung mit Budget unterlegt wird. Danach: Qualifikationskatalog mit einer Schreibweise, Pflichtfelder bei Neuanlage | 18.000 von 41.000 Profilen (`angenommen`, `profil.md`). Reihenfolgekorrektur aus der geprüften Fassung |
| **Fehlende Rolle** | **Ein Data Steward für Bewerber- und Kundendaten** — operative Datenverantwortung **mit Weisungsrecht in den Niederlassungen**, angesiedelt zwischen Recruiting, Vertrieb und IT. Ohne sie hat die RACI-Matrix an vier Stellen ein Accountable ohne Durchgriff | `raci-datenpflege.md`: *„Zeile 1 hat ein A ohne Weisungsrecht … Zeile 2 hat ein A ohne Durchgriff."* Ehrlich dazu: es ist eine Stelle, die kein Geld verdient |

**Was in den 90 Tagen ausdrücklich nicht passiert:** kein Besetzungsassistent, keine Rangfolge von
Personen, kein Zugriff auf Lebenslauf-Volltexte. Dafür fehlt die Datengrundlage — und das ist eine
Feststellung, keine Vorsichtsmaßnahme. Eine Messung von heute: **437 von 1.473 Profilen nennen
einen nachweispflichtigen Schein, und für keinen einzigen existiert ein Gültigkeitsdatum im
Datenmodell.**

## 4 · Was wir nicht wissen — und wie wir es klären

| # | Offene Frage | Klärung | Bis wann |
|---:|---|---|---|
| 1 | **Ist die Migrationsausschreibung noch offen?** Wenn ja, gehören drei Anforderungen ins Lastenheft: offene REST-API, Datenfeldarchitektur im Standard, Zeitnachweisformate der Kundenbetriebe | Rolle 2 fragen | **diese Woche** — danach ist es ein Änderungsauftrag ohne Wettbewerb |
| 2 | **Ist eine Datenschutz-Folgenabschätzung erforderlich, und trägt die Ausnahme nach Art. 6 Abs. 3?** | Externer Datenschutzbeauftragter, schriftlich. Nicht als Zusicherung, sondern als Dokument | vor dem ersten Lauf |
| 3 | **Was kostet der Einführungsaufwand der empfohlenen Plattform?** Neuer Lieferant, neue Oberfläche, neue Nutzerverwaltung | Angebot einholen. **Rechtfertigt er ein Gewicht über 31 % für Adoption, ist Copilot die richtige Wahl** — das ist die einzige Kippschwelle in Reichweite | vor Vertragsschluss |
| 4 | **Sind die Bewertungen unabhängig belegt?** Alle Scores beruhen auf Herstellerunterlagen; kein Angebot liegt vor | Zwei Referenzkunden im DACH-Raum unter 150 Beschäftigten als Ausschreibungsbedingung | vor Vertragsschluss |
| 5 | **Stimmt der Reifegrad, auf dem die Gewichtung aufbaut?** Er ist eine nicht validierte Einschätzung | Prozessdaten und Interviews statt Gruppenschätzung | vor der nächsten Stufe |

**Diese Vorlage hat Lücken, und sie sind benannt.** Die größte: der Einführungsaufwand der
empfohlenen Option ist unbeziffert — dieselbe Schwäche, die wir Copilot vorhalten.

## Beschlussvorschlag

1. Die Geschäftsführung beschließt den freigegebenen KI-Zugang für **20 Seats** über drei
   Standorte, **≤ 9.000 € im Jahr**, unter dem Vorbehalt der drei Tore aus Abschnitt 3.
2. Sie nimmt das **Abbruchkriterium** zur Kenntnis: nach drei Monaten null Lebensläufe in Diensten
   ohne AVV, mindestens zwei von drei Standorten in wöchentlicher Nutzung. Sonst Abschaltung.
3. Sie beauftragt die Klärung der offenen Frage 1 **in dieser Woche**.
4. Sie entscheidet **nicht** über einen Besetzungsassistenten. Für Stufe 4 gilt: kein
   Anbieterentscheid 2026. Bis dahin bleibt „nichts bauen" die zweitbeste bewertete Option — und
   besser als jedes der geprüften KI-Produkte.
