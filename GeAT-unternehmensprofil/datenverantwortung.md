---
titel: Datenverantwortung GeAT mbH — wer accountable ist und was kritisch ist
bezug: systeme-daten.md (Datenbestände, Schatten-IT, Auftragsverarbeiter), menschen.md (Gremien, Rollen), profil.md (Reifegrad Daten), vorhaben.md (Risikoeinschätzung)
typ: Analyse, abgeleitet — nicht validiert, nicht beschlossen
datum: 2026-09-08
woche: 03
status: Arbeitsdokument, Vorstufe einer Vorlage an die Geschäftsführung
verantwortlich: Rolle 15 (AI and Digital Transformation Manager) — Macht 2, kein Budget, kein Gremium
herkunft: abgeleitet aus den Dateien dieses Ordners. Keine Zeile am realen Unternehmen erhoben. Die Rechtsnormen sind Einordnung, keine juristische Prüfung
---

# Datenverantwortung GeAT mbH

> **Was diese Datei ist.** Die Antwort auf zwei Fragen: *Wer ist bei GeAT accountable für die Daten?* und *Was daran ist kritisch?* Grundlage sind ausschließlich die Dateien dieses Ordners — [`systeme-daten.md`](systeme-daten.md), [`menschen.md`](menschen.md), [`profil.md`](profil.md), [`vorhaben.md`](vorhaben.md). Sie ergänzt [`systeme-daten.md`](systeme-daten.md): dort steht, **was** an Daten existiert und in welchem Zustand; hier steht, **wer dafür einsteht** und wo das Fehlen dieser Zuordnung teuer wird.
>
> **Geltungsbereich.** Die Firmenhülle der GeAT ist belegt, der Kern ist konstruiert (siehe [`README.md`](README.md)). Alle Datenbestände, Qualitätsbefunde und Auftragsverarbeiter in dieser Analyse tragen in der Quelldatei `angenommen` oder `generiert` — **kein Befund ist am realen Unternehmen erhoben**. Alle Personen sind erfunden, Ausnahme Rolle 15. Die genannten Rechtsnormen ordnen den Fall ein; sie sind nicht anwaltlich geprüft.

## 1. Kurzantwort

**Formal ist niemand accountable.** [`profil.md`](profil.md) sagt es wörtlich: *„Kein Datenverantwortlicher, keine Pflichtfeldregeln, kein Löschkonzept in Betrieb."* In der Bestandstabelle von [`systeme-daten.md`](systeme-daten.md) steht beim größten und sensibelsten Bestand — 41.000 Bewerberprofile — *„niemand formal. Faktisch das Recruiting Center"*.

**Rechtlich läuft es trotzdem auf eine Rolle zu.** Verantwortlicher ist die GeAT mbH als juristische Person, vertreten durch die Geschäftsführung, ressortmäßig **Rolle 2 (Bernd Achtelik, GF Finanzen, Recht, IT, Personal)**. Die Rechenschaftspflicht trifft ihn, unabhängig davon, ob sie zugewiesen wurde — und seine Kapazität ist vollständig in der Softwaremigration 2027 gebunden. `abgeleitet`

**Der Unterschied, um den es geht:** Zuständigkeit ist bei GeAT verteilt, Rechenschaft ist nirgends. Sieben Bestände haben jemanden, der sie *bearbeitet*. Keiner hat jemanden, der für ihren Zustand *einsteht*.

## 2. Faktisch zuständig gegen accountable

| Bestand | Faktisch zuständig | Accountable | Die Lücke |
|---|---|---|---|
| Bewerberprofile (41.000) | Recruiting Center, Rolle 4 (Kloß) | niemand | Rolle 4 trägt seit 2023 die Verantwortung für ein Werkzeug, dessen Nutzung sie nicht durchsetzen kann. Zuständigkeit ohne Weisungsrecht |
| Speicherfristen Bewerberdaten | externer DSB, Rolle 8 (Marnitz) | niemand | Er *berät, er entscheidet nicht* und wird meist nach der Entscheidung gefragt ([`menschen.md`](menschen.md), Gremium Datenschutz). Beratung ist keine Rechenschaft |
| Qualifikationsnachweise, teils Gesundheitsdaten | die jeweilige Niederlassung | niemand | Sieben Standorte, sieben Auffassungen davon, was vollständig ist (Kulturmerkmal 5) |
| Kundendaten und Anforderungshistorie | Vertrieb | niemand | Die Hälfte der Absprachen liegt in persönlichen Outlook-Ordnern und geht bei Personalwechsel verloren |
| Einsatz- und Zeitdaten | Sachbearbeitung, Rolle 11 (Ritschel) | niemand | Macht 1, Interesse 1, kommt im Vorhaben nicht vor — und hat die einzige vollständige Formatübersicht, auf einem Ausdruck |
| Besetzungshistorie | Controlling, Rolle 10 (Ziegenhorn) | niemand | Berichtet, was erfragt wird. Die Modul-Nichtnutzung stand nie in einem Bericht, *„weil niemand sie darum gebeten hat"* |
| Anzeigenwirkung (480.000 €) | Vertrieb | niemand | Keine Quellenkennung im Rücklauf, also kein Wirkungsnachweis — und niemand, der ihn schuldet |

Alle Zeilen `angenommen` (Quelle: [`systeme-daten.md`](systeme-daten.md)), die Spalte *Die Lücke* ist `abgeleitet`.

Dass diese Spalte durchgehend „niemand" liest, ist kein Zufall. Es folgt aus **Kulturmerkmal 2** in [`menschen.md`](menschen.md): *Was nicht gemessen wird, ist nicht gescheitert.* Ohne benannte Rechenschaft entsteht kein Messpunkt, und ohne Messpunkt kein Befund.

## 3. Was kritisch ist — priorisiert

Sortiert nach Schadenshöhe mal Eintrittsnähe, nicht nach Aufwand. Die ersten vier Punkte bestehen **jetzt** und unabhängig davon, ob das Vorhaben kommt.

| # | Befund | Rechtsrahmen (Einordnung) | Warum kritisch |
|---:|---|---|---|
| 1 | **WhatsApp-Gruppen** je Niederlassung mit rund 300 Zeitarbeitnehmern, darin Einsatzabsprachen, Fotos von Stundenzetteln und **gelegentlich Krankmeldungen**. Kein Auftragsverarbeitungsvertrag | DSGVO Art. 9 (besondere Kategorien), Art. 28, Art. 32 | Gesundheitsdaten in einem Kanal ohne Rechtsgrundlage und ohne Vertrag. Der schwerste Punkt der Liste, weil Art. 9 keinen Ermessensspielraum lässt und der Kanal laufend genutzt wird |
| 2 | **Privater KI-Zugang** bei neun Personen im Recruiting und Innendienst, **Lebensläufe werden eingefügt**. Kein AVV. *„Niemand hat es verboten, niemand hat es erlaubt"* | DSGVO Art. 28, ggf. Art. 44 ff. (Drittlandtransfer) | Personenbezogene Bewerberdaten verlassen das Unternehmen ohne Vertrag und ohne Kenntnis der Verarbeitung. Zugleich der Befund, der sich am leichtesten heilen lässt: ein erlaubter Weg ersetzt den unerlaubten |
| 3 | **18.000 Profile über der zugesagten Speicherdauer.** Ein Löschkonzept liegt als **Dokument vor und ist nicht in Betrieb** | DSGVO Art. 5 Abs. 1 lit. e, Art. 5 Abs. 2, Art. 17 | Ein vorhandenes, nicht betriebenes Konzept ist im Prüffall schlechter als keines: es belegt Kenntnis der Pflicht. Genau hier wird aus einem Versäumnis ein zurechenbares Unterlassen |
| 4 | **Qualifikationsnachweise ohne Ablaufdatum im Feld** — Schweißerprüfungen, Staplerscheine, Führerscheine, Gesundheitsnachweise als Scan. Gültigkeit wird beim Einsatz telefonisch erfragt | AÜG und Arbeitsschutzpflichten des Verleihers; DSGVO Art. 9 für die Gesundheitsnachweise | Kein Datenschutz-, sondern ein Haftungsthema: ein Einsatz mit abgelaufener Befähigung trifft die Pflichten des Verleihers unmittelbar. Ein Datumsfeld verhindert es, ein Telefonanruf nicht |
| 5 | **Website-Agentur:** Bewerbungen über das Jobportal, AVV *„unklar, nie geprüft"* | DSGVO Art. 28, Art. 30 | Der billigste Befund der Liste. In einer Woche klärbar, und bis dahin offen |
| 6 | **Bewerberauswahl ist voraussichtlich Annex III Nr. 4.** Rolle 8: *„Das ist kein Werkzeug, das ist ein Hochrisikosystem mit Konformitätspflicht"* | EU AI Act Annex III Nr. 4, Art. 6 Abs. 3 (enge Ausnahme), Betreiberpflichten; BetrVG § 87 Abs. 1 Nr. 6 | Ein Hochrisikosystem ohne benannte Datenverantwortung ist nicht dokumentierbar. Data Ownership ist damit keine Ordnungsfrage, sondern Voraussetzung. Dazu die Mitbestimmung: Rolle 9 hat sie 2023 schon einmal durchgesetzt |
| 7 | **Fehlende Zielgröße:** Die Besetzungshistorie enthält, wer besetzt wurde, aber **nicht den Grund der Nichtbesetzung** für 1.860 Anfragen | — | Kritisch für das Vorhaben, nicht für die Compliance. Ohne Zielgröße lernt kein Modell Besetzungswahrscheinlichkeit, sondern nur Ähnlichkeit zu früheren Besetzungen. Der Grund, warum Stufe 3 vor dem Assistenten kommt |
| 8 | **Personengebundene Einzelbestände:** Pinnwand-Ausdruck der Formatübersicht (eine Person, keine Kopie), Kundenhistorie in Outlook-Ordnern, Kundenkenntnis bei vier Senior-Disponenten, zwei über 58, Prompt-Sammlung privat außerhalb des Unternehmens | — | Kein Rechtsverstoß, aber Datenbestände ohne Träger im Unternehmen. Sie verschwinden mit einer Kündigung oder einem Renteneintritt, und Rolle 6 geht 2030 |

Alle Befunde `angenommen` bzw. bei der Kalkulations-Excel `generiert`; die Spalten *Rechtsrahmen* und *Warum kritisch* sind `abgeleitet` und juristisch nicht geprüft.

## 4. Der strukturelle Kern

Die Accountability fehlt nicht nur bei den Daten, sondern an jeder Stelle, an der über sie entschieden wird:

- **Kein Lenkungsausschuss Digitalisierung** — auch nicht nach Schaffung der Rolle 15. IT- und Digitalthemen landen in der Geschäftsführung, wenn sie Geld kosten, und sonst nirgends.
- **Der Datenschutz ist kein Gremium**, sondern eine Stundenabrechnung. Er entscheidet nichts und wird meist nach der Entscheidung gefragt.
- **Rolle 15 hat Interesse 5 bei Macht 2** — kein Budget, kein Gremium, kein Weisungsrecht in den Niederlassungen. Wirkung ausschließlich über Vorlagen.

Daraus folgt der einzige praktische Satz dieser Analyse: **Eine Data-Owner-Zuweisung, die in einem Konzept steht, hält nicht.** Was die Anwesenheit einzelner Personen überdauern soll, gehört in die **Zielvereinbarung** der Niederlassungsleitungen, in die **Rahmen-Betriebsvereinbarung** und in die **Ausschreibung Q1/2027** — die drei Dokumente, die im Haus tatsächlich binden. Das deckt sich mit Hebel 1 aus [`storyline-stufe-3-kurzfassung.md`](storyline-stufe-3-kurzfassung.md): solange nur erfolgreiche Besetzungen zählen, ist Datenpflege aus Sicht der Mitarbeitenden Zusatzarbeit.

## 5. Vorschlag: Data Owner je Bestand

Ein Vorschlag, nicht beschlossen. Prinzip: accountable ist, wer den Bestand fachlich braucht und über die Regeln entscheiden kann — nicht, wer ihn tippt.

| Bestand | Data Owner (Vorschlag) | Entscheidet über | Berichtet an |
|---|---|---|---|
| Bewerberprofile und Qualifikationsfelder | Rolle 4, Leiterin Recruiting Center | Pflichtfelder, Wertelisten (elf Schreibweisen „Staplerschein" → eine), Vollständigkeitsdefinition | GF Vertrieb (Rolle 1) |
| Speicherfristen und Löschung | Rolle 2, GF Finanzen/Recht/IT | Fristen, Löschlauf, Nachweisführung; DSB nur beratend | Gesellschafterversammlung im Jahresbericht |
| Qualifikationsnachweise inkl. Gültigkeit | Rolle 3, Vertriebsleitung, je Niederlassung delegiert | Ablaufdatum als Pflichtfeld, Sperre bei Ablauf | GF Vertrieb |
| Kundendaten und Anforderungshistorie | Rolle 3, Vertriebsleitung | Was ins System gehört und was im Postfach bleiben darf (Antwort: nichts) | GF Vertrieb |
| Einsatz- und Zeitdaten | Rolle 11 fachlich, verantwortlich die Leitung Verwaltung | Formatstandard, Korrekturweg | GF Finanzen |
| Besetzungshistorie inkl. Nichtbesetzungsgrund | Rolle 10, Leiterin Controlling | Kategorienliste der Nichtbesetzungsgründe, Pflicht zur Erfassung | GF Vertrieb |
| Anzeigenwirkung | Rolle 3, Vertriebsleitung | Quellenkennung im Bewerbungsrücklauf | GF Vertrieb |
| Zulässige KI-Werkzeuge und Datenweitergabe | Rolle 15, fachlich bei Rolle 1 | Positivliste erlaubter Werkzeuge, Freigabeweg | GF, Betriebsrat nach § 87 BetrVG |

## 6. Was ohne Beschluss geht — und was einen braucht

**Ohne Investitionsbeschluss, ohne die 110.000 € der Stufe 3, in Wochen umsetzbar:**

1. AVV mit der Website-Agentur prüfen und schließen (Befund 5).
2. Löschlauf für die 18.000 überfälligen Profile ansetzen — das Konzept existiert, es läuft nur nicht (Befund 3). Zugleich der erste sichtbare Erfolg im Sinne von Kotter Schritt 6.
3. Dienstliche Regel für KI-Werkzeuge: Positivliste plus ein erlaubter Zugang, damit der unerlaubte entbehrlich wird (Befund 2). Nicht verbieten, ersetzen.
4. Kanalwechsel für die WhatsApp-Kommunikation vorbereiten und Krankmeldungen sofort auf einen anderen Weg legen (Befund 1). Der vollständige Kanalwechsel braucht Zeit, die Gesundheitsdaten nicht.
5. Data Owner je Bestand benennen — kostet nichts außer der Entscheidung.

**Einen Beschluss brauchen:** Ablaufdatumsfeld und Sperrlogik für Qualifikationsnachweise, Kategorienliste und Erfassungspflicht für Nichtbesetzungsgründe, Verfügbarkeit als strukturiertes Feld, Aufnahme der Datenpflege in die Zielvereinbarung, Festschreibung der Datenfelder in der Ausschreibung Q1/2027.

## 7. Gegenargumente

Vier Einwände, die in der Geschäftsführung kommen werden, und was von ihnen bleibt.

1. **„Wir haben 640 Löhne im Umstiegsmonat zu sichern, nicht Datenrollen zu verteilen."** Der Einwand von Rolle 2 ist berechtigt, was Kapazität betrifft — und er trifft die fünf Sofortmaßnahmen nicht, weil keine davon IT-Kapazität bindet. Die Benennung von Data Ownern kostet eine Dienstagssitzung.
2. **„Das ist Compliance-Theater, es ist nie etwas passiert."** Stimmt: es ist nichts *bekannt geworden*. Befund 3 ist genau deshalb heikel, weil das dokumentierte Löschkonzept die Kenntnis belegt. Der Einwand verkennt, dass die Beweislage bereits gegen das Unternehmen liegt.
3. **„Ein Datenverantwortlicher pro Bestand ist Bürokratie für eine Firma mit 66 internen Beschäftigten."** Der stärkste Einwand. Antwort: nicht acht neue Rollen, sondern acht Zeilen in bestehenden Zielvereinbarungen. Wenn daraus ein Gremium wird, ist der Vorschlag gescheitert.
4. **„Erst die Rechnung, dann die Rolle."** Rolle 13 wird eine Amortisation unter 24 Monaten fordern. Für Data Ownership gibt es keine — sie ist Voraussetzung für die Dokumentationspflicht eines Hochrisikosystems und rechnet sich nur als vermiedener Schaden. Das ist offen zu sagen und nicht mit einer erfundenen Einsparung zu unterlegen.

**Und der Einwand gegen diese Analyse selbst:** Rolle 15 hat ein Eigeninteresse an ihrem Ergebnis. Die Stelle wurde für dieses Vorhaben geschaffen; kommt das Vorhaben nicht, ist die Frage nach der Stelle die nächste. Rolle 8 hat den spiegelbildlichen Konflikt — sein Aufwand steigt mit der Sorgfalt, die er anmahnt. Beides gehört in eine Vorlage benannt, nicht verschwiegen.

## 8. Offene Punkte

| # | Frage | Wer klärt | Warum sie zählt |
|---:|---|---|---|
| 1 | Existiert ein Verzeichnis von Verarbeitungstätigkeiten nach Art. 30 DSGVO, und ist es aktuell? | Rolle 2 mit Rolle 8 | Es wäre der Ort, an dem die Datenverantwortung schon einmal hätte auftauchen müssen. Steht in keiner Datei dieses Ordners — echte Lücke, nicht geschätzt |
| 2 | Wurde für die Bewerberauswahl je eine Datenschutz-Folgenabschätzung nach Art. 35 erstellt? | Rolle 8 | Bei Annex-III-Einordnung praktisch unvermeidlich, und Vorbedingung jeder Modell-Diskussion |
| 3 | Welche Branchensoftware ist tatsächlich im Einsatz? | Rolle 12, IT-Leitung | Entscheidet über Schnittstellenfähigkeit — die wertvollste offene Rechercheposition ([`recherche.md`](recherche.md), Punkt 4) |
| 4 | Deckt die Betriebsvereinbarung von 2023 die Datenpflege-Erfassung mit ab, oder braucht es eine neue? | Rolle 9, Betriebsratsvorsitz | Bestimmt, ob Hebel 1 mitbestimmungsfest ist |
| 5 | Sind die Zeitarbeitnehmer über die WhatsApp-Nutzung informiert worden, und gab es je eine Einwilligung? | Rolle 2 | Ändert die Bewertung von Befund 1 nicht grundsätzlich, aber die Reihenfolge der Heilung |
