---
firma: Hellwig Fördertechnik (fiktiv)
stand: 2026-09-01
verwendung: Vorbereitung der Dozierenden
warnung: Enthält Lösungen. Nicht an Teilnehmende ausgeben.
---

# Dozentenhinweise

> **Spoilerwarnung.** Diese Datei enthält Referenzlösungen zu allen Übungen. Die Rohdaten in [`04_Change-Lage.md`](04_Change-Lage.md) sind absichtlich unbewertet; wer diese Datei vorher austeilt, macht die Übungen wertlos.

---

## 1. Kategorien-Lösungsschlüssel

| ID | Vorgeschlagen als | Richtig | Kernbegründung in einem Satz |
|---|---|---|---|
| V1 | GenAI | **RPA/OCR mit Regelwerk** für 68 % des Volumens, GenAI nur für die Restmenge | Regelhaft beschreibbare Aufgabe, stabile Formate, deterministisch prüfbar, keine Kosten je Vorgang |
| V2 | GenAI | **Zu 98 % kein KI-Vorhaben.** Berechtigung, Priorisierung, Datenpflege, Freigabegrenze — GenAI nur für die Teileidentifikation in Sonderfällen | 6,4 von 6,5 Tagen sind Liegezeit; und der sinnvolle KI-Anteil ist nicht der Angebotstext |
| V3 | Predictive ML | **Kategorie richtig, Voraussetzung fehlt** | Keine labelbare Zielgröße: Ausfälle stehen als Freitext, Zeitreihen erst ab 06/2023, Rohdaten bei Dritten |
| V4 | GenAI | **Compliance-Vorhaben**, nicht Effizienzprojekt | Verbindliche Auskunft nach außen; Haftung liegt beim Unternehmen |
| V5 | Agentic AI | **Nicht dieser Pfad.** Agent für Recherche und Entwurf, Freigabe beim Menschen | 11 Schritte, 0,95¹¹ ≈ 57 %; Fehler geht ungeprüft an den Kunden |
| V6 | „Statistik" | **Predictive ML — und das beste Vorhaben im Portfolio** | Einzige tragfähige Datenlage im Haus; 3,4 Mio. Bestand, 18 % Langsamdreher |
| V7 | GenAI | **GenAI mit Mensch dazwischen — der richtige Quick Win** | Einziges Vorhaben, das alle vier Kotter-Kriterien erfüllt |
| V8 | RPA | **RPA möglich, aber falsch** | Automatisiert eine Doppelpflege, die nicht existieren müsste; bricht bei jeder SAP-Änderung |
| V9 | Predictive ML | **Gar nicht** | Vergangenheit fortschreiben, wo geändert werden soll; zusätzlich Hochrisiko-Einordnung |
| V10 | RAG | **Erst kuratiert, dann Assistent** | Daten Stufe 2 und kein Berechtigungskonzept; 180 gültige Anleitungen statt 2.400 Dateien |

**Die drei heute machbaren und richtigen Vorhaben: V1 (umkategorisiert), V6, V7.** Keines war priorisiert, zwei enthielten das Wort KI nicht in der ursprünglichen Beschreibung.

### Die drei Fallen, in die Gruppen zuverlässig laufen

1. **V2 sauber einer Kategorie zuordnen.** Die Gruppe sucht die richtige KI-Kategorie und findet eine. Die Frage, die sie nicht stellt: *Welcher Bestandteil der Durchlaufzeit wird durch ein Sprachmodell kleiner?* Antwort: der mit 0,1 von 6,5 Tagen. Die zweite Frage, die noch seltener kommt: *Und wo im Prozess wäre GenAI dann wirklich richtig?* Antwort: Teileidentifikation in Sonderfällen, wo 90 % der Bearbeitungszeit liegen.
2. **V6 übergehen.** Es klingt nach Controlling. Wenn keine Gruppe es nennt, nicht auflösen, sondern fragen: *Welches Vorhaben hätte heute die Datenlage?*
3. **V10 ablehnen.** Fachlich korrekt, politisch teuer — es ist Semmlers einzige eigene Meldung. Wer sein Vorhaben ablehnt, verliert die Person, die man für Schritt 5 braucht. Die Nachfrage: *Was passiert mit Semmler, wenn wir sein Vorhaben absagen und seine Pilotteilnahme einfordern?*

---

## 2. ADKAR-Referenzbewertung

Bezugsvorhaben V2. Bewertung auf Basis der Aussagen in [`04_Change-Lage.md`](04_Change-Lage.md) Abschnitt 3. **Abweichungen von ±1 sind kein Fehler** — die Begründung zählt, nicht die Zahl.

| Stufe | A · Sachbearbeitung | B · Kowalczyk | C · Serviceleitung | D · IT |
|---|:---:|:---:|:---:|:---:|
| Awareness | 4 | 5 | 4 | 5 |
| Desire | **2 ⚠** | 5 | **2 ⚠** | 4 |
| Knowledge | 2 | 4 | 2 | **2 ⚠** |
| Ability | 1 | **2 ⚠** | 1 | 2 |
| Reinforcement | 1 | 1 | 1 | 2 |
| **Barrier Point** | **Desire** | **Ability** | **Desire** | **Knowledge** |

### Begründungen, die im Raum gesagt werden sollten

**Gruppe A · Desire 2.** *„Wenn der Automat die Standardfälle macht — was bleibt dann für neun Leute?"* plus *„Frau Kowalczyk sagt, es geht nicht um Stellen. Aber sie entscheidet das ja nicht."* Die Beschäftigungsfrage ist gestellt und nicht beantwortet. Awareness ist hoch (zwei Kunden haben es gesagt) — das ist die klassische Kombination, in der Kommunikation nichts mehr bewegt.
→ **Maßnahme:** schriftliche Aussage zur Beschäftigung mit Geltungszeitraum, von der Geschäftsführung, nicht von der Bereichsleitung. Dazu Beteiligung: zwei Sachbearbeitende legen mit fest, welche Fallgruppen der Assistent übernimmt.
→ **Nicht:** Schulung. Nicht Nutzungsquote als KPI.

**Gruppe B · Ability 2.** Awareness 5, Desire 5, Knowledge 4 — sie hat den Fall selbst gerechnet. Es fehlen Zugang (Vault-Leserecht) und Zeit (Bonus an Durchlaufzeit).
→ **Maßnahme:** Leserecht in derselben Woche, Zielvereinbarung für die Pilotdauer aussetzen oder Lernzeit separat buchbar machen.
→ **Der Lehrpunkt:** Das ist der teuerste Fall im Portfolio, weil hier eine vorhandene Bereitschaft verbrannt wird. Und der billigste zu lösen — zwei Entscheidungen, kein Budget.

**Gruppe C · Desire 2, mit Vorbehalt.** Hier wird im Kurs am meisten diskutiert, und zu Recht. Semmler *kann* Kapazität freigeben, tut es aber nicht — nach Modelllogik ist das Desire. **Die Ursache liegt vollständig im Umfeld:** Reaktionszeit ist seine Kennzahl, Pilotzeit belastet seine Kostenstelle, sechs Stellen sind unbesetzt, und sein eigener Vorschlag liegt seit Monaten unbearbeitet.
→ **Maßnahme:** Pilotzeit aus der Bereichskapazität herausrechnen, Kennzahl für die Pilotdauer aussetzen, V10 in kuratierter Fassung beauftragen.
→ **Wenn eine Gruppe „Ability" sagt:** nicht korrigieren, sondern zuspitzen. Beide Lesarten führen zur selben Maßnahme — und das ist eine bessere Einsicht als die richtige Stufenzuordnung.

**Gruppe D · Knowledge 2.** Desire 4, aber weder Berechtigungskonzept noch Folgenabschätzung noch Vorfallprozess. Die einzige Gruppe, für die Training richtig ist.
→ **Maßnahme:** Fachbegleitung für die Folgenabschätzung, nicht ein Prompting-Kurs.

### Die Pointe, die im Raum stehen muss

> Der Steuerkreis hat für Q4 **Schulungen** beschlossen. Sie treffen in einer von vier Gruppen. Drei Viertel des Budgets sind verbrannt, bevor es ausgegeben ist.

Das ist die stärkste Einzelaussage des Tages, und sie ist aus den Rohdaten hergeleitet, nicht behauptet.

---

## 3. Kraftfeld-Referenzbewertung

**Betrachtungsraum: Abteilung** (Innendienst, 14 Personen). Bei anderer Wahl verschieben sich Werte — insbesondere Nr. 16.

### Treibende Kräfte

| Nr. | Kraft | Cluster | Stärke |
|---:|---|---|---:|
| 5 | Auftragsquote von 47 % auf 34 % gefallen, Kunden nennen die Geschwindigkeit | Kontext | 4 |
| 1 | Zwei Großkunden haben Geschwindigkeit in die Lieferantenbewertung aufgenommen | Kontext | 4 |
| 3 | Zwei Wettbewerber bieten Angebote in unter zwei Stunden | Kontext | 4 |
| 7 | Kowalczyk hat den Fall selbst gemeldet und gerechnet | Mensch | 3 |
| 13 | Dr. Hellwig will bis Jahresende ein sichtbares Ergebnis | Kontext | 3 |
| 19 | Oberholz berichtet im Teams-Kanal von guten Erfahrungen | Mensch | 2 |
| | **Summe** | | **20** |

### Hemmende Kräfte

| Nr. | Kraft | Cluster | Stärke | Beeinflussbar | Maßnahme |
|---:|---|---|---:|:---:|---|
| 12 | Sorge um neun Stellen, keine schriftliche Aussage | Mensch | **5** | ja | Schriftliche Beschäftigungszusage mit Geltungszeitraum, von der GF |
| 14 | Keine Lernzeit im Kapazitätsplan des Innendienstes | Substanz | **5** | ja | 4 Std./Woche je Teilnehmender aus der Planung herausrechnen |
| 2 | Kowalczyks Bonus hängt an 5 AT Durchlaufzeit | Substanz | 4 | ja | Zielvereinbarung für die Pilotdauer aussetzen |
| 4 | Kein Vault-Leserecht, Klärung dauert 2,1 Tage | Substanz | 4 | ja | Leserecht für 3 Personen, eine Entscheidung von Beniers |
| 6 | 11 % der Positionen ohne Gewicht, kein Frachtpreis möglich | Substanz | 4 | ja | Gewichte der Top-500-Teile nachpflegen (deckt 71 % der Anfragen) |
| 8 | Unklar, welche Daten eingegeben werden dürfen; DSB nach 19 Tagen | Substanz | 4 | ja | Einseitiges Freigabeblatt mit Beispielen, einmalig durch DSB geprüft |
| 11 | Erinnerung an MES-Abbruch 2019 und Microsoft 2023 | Kontext | 4 | teilweise | Benennen statt übergehen; sichtbar anders machen, was damals fehlte |
| 10 | Preisfreigabe ab 10.000 EUR nur durch Brandtner | Substanz | 3 | ja | Vertretungsregel oder Grenze auf 25.000 EUR |
| 15 | Kein Ansprechpartner bei Problemen, IT 7 auf 512 | Substanz | 3 | ja | Zwei benannte Key User mit ausgewiesenem Zeitbudget |
| 18 | Beniers braucht dieselben IT-Kapazitäten für PDM | Kontext | 3 | teilweise | Priorisierungsentscheidung der GF, offen kommuniziert |
| 9 | Zwei Sachbearbeitende über 58, sehen den Sinn nicht | Mensch | 2 | teilweise | Nicht bearbeiten. Nicht zu Pilotteilnehmenden machen |
| 16 | Betriebsrat nicht eingebunden, Frage nach Leistungsdaten | Kontext | 2 | ja | Frühzeitige Information; **Stärke 5 bei Betrachtungsraum Gesellschaft** |
| 17 | Sonderfallwissen ist echt und wird nicht ersetzt | Mensch | 2 | **nein — zutreffend** | In die Lösung einbauen: Assistent nur für Standardfälle, Sonderfall bleibt beim Menschen |
| | **Summe** | | **45** | | |

### Die beiden Sonderfälle, nach denen [`04`](04_Change-Lage.md) fragt

- **Nr. 20** („Der Service trägt 80 % des EBIT, und dieses Vorhaben verbessert dort etwas Sichtbares") ist **keine Kraft.** Es ist ein Priorisierungsargument: es sagt, warum dieses Vorhaben wichtiger ist als ein anderes, wirkt aber auf das Verhalten der Beteiligten nicht. Gehört in die Vorhabenbegründung, nicht ins Kraftfeld.
- **Nr. 13** (Dr. Hellwigs Frist) **wirkt in beide Richtungen.** Auf Managementebene treibend, auf Arbeitsebene hemmend, weil der Zeitdruck genau die Vorleistungen verhindert — Datenpflege, Beteiligung, Freigabeblatt —, die das Vorhaben tragen. Beide Zuordnungen sind vertretbar, wenn die Begründung dabeisteht. Wer sie einfach als treibend notiert und weitergeht, hat den interessanteren Teil übersehen.

### Lesart der Zahlen

**45 zu 20** heißt: das Feld ist blockiert. Es heißt **nicht**, dass 25 Punkte fehlen.

Die entscheidenden Einzelwerte sind Nr. 12 und Nr. 14 — beide Stärke 5, beide beeinflussbar, beide **ohne Budget lösbar**. Eine schriftliche Zusage und eine Zeile im Kapazitätsplan senken die hemmende Seite um 10 Punkte. Mehr Kommunikation würde die treibende Seite auf vielleicht 23 heben und das Feld nicht bewegen.

**Von den zwölf Maßnahmen ist genau eine reine Kommunikation** — Nr. 11, und auch die ist eher ein Eingeständnis als eine Botschaft. Nr. 18 enthält Kommunikation, aber die Wirkung liegt in der Priorisierungsentscheidung, nicht in ihrer Bekanntgabe. Das ist der Prüfstein aus dem [Plattform-Beispiel](../coursebook/2.2/2.2_Ergaenzung-Force-Field-Analyse.md#46-das-beispiel-einführung-einer-kollaborationsplattform), und er hält.

### Die Nr. 9, an der sich zeigt, ob die Priorisierung verstanden wurde

Zwei Sachbearbeitende über 58, die den Sinn nicht sehen: schwach (2) und teilweise beeinflussbar. **Also nicht bearbeiten.** Gruppen widmen ihr regelmäßig die längste Diskussion, weil sie sich wie ein echtes Change-Problem anfühlt. Das ist das linke untere Feld der Matrix, und es kostet Zeit, die bei Nr. 12 und 14 fehlt.

---

## 4. Kotter: erwartete Ergebnisse

**Rückwärtsdiagnose:** Schritt 1 offen. Belege: 4 von 11 beim 75-Prozent-Test, 6 % Aufwandsanteil in den Schritten 1–4, zwei Freiwillige, keiner eingebunden, keine Planung für die Zeit nach dem Piloten.

**Vision, tragfähige Fassung** (eine von vielen; Maßstab ist nicht der Wortlaut):

> *„In zwei Jahren wartet bei uns kein Kunde mehr sechs Tage auf ein Ersatzteilangebot und niemand von uns sucht Informationen in vier Systemen zusammen. Was eine Maschine nachschlagen kann, schlägt die Maschine nach — was Erfahrung braucht, bleibt bei uns."*

Prüfung: in eigenen Worten wiedergebbar (ja), Zustand statt Projekt (ja), widersprechbar (ja — man kann finden, dass die Zusammenschau zur Qualitätssicherung gehört), Beschäftigungsfrage beantwortet (ja, im letzten Halbsatz), keine Prozentzahl (ja).

**Koalition, Mindestbesetzung:**

| Person | Bringt | Weshalb unverzichtbar |
|---|---|---|
| Dr. Hellwig | Autorität | Ohne sie bleibt jede Entscheidung Vorschlag |
| **Brandtner** | Reputation, Skepsis | Ohne ihn ist es eine Koalition der Überzeugten. Sein Einwand kommt sonst von außen, zum spätesten Zeitpunkt |
| **Semmler** | Autorität und Reputation im Bereich mit 80 % des EBIT | Ihn draußen zu lassen ist bequem und beendet das Vorhaben später |
| Ehrlicher | Expertise | Ohne ihn Pläne, die technisch nicht tragen |
| Kowalczyk | Fläche, Glaubwürdigkeit | Die einzige mit einem selbst gerechneten Fall |
| Reitmeier | Legitimität | Beteiligungspflicht; früh eingebunden ist sie eine treibende Kraft |
| Oberholz | Reichweite | 184 Zuhörer, die kein Newsletter erreicht |

Sieben Personen. Wer Brandtner oder Semmler weglässt, hat die Aufgabe nicht gelöst — auch wenn die Runde harmonischer aussieht.

**Quick Win: V7.** Erwartete Fehlwahl 1 ist V4 (nach außen sichtbar, für die Fläche wertlos, Haftungsfrage), Fehlwahl 2 ist V6 (bester ROI, für niemanden außerhalb des Controllings wahrnehmbar). Prüffrage: *Wessen Alltag wird spürbar besser, und wird diese Person davon erzählen?*

---

## 5. Zeitgerüst

| Block | Übung | Minuten |
|---|---|---:|
| 1.4 | Wellen-Diagnose | 20 |
| | Reifegrad lesen | 10 |
| | Kategorien zuordnen | 25 |
| | Auflösung und Diskussion | 20 |
| 1.5 | Kontextdatei destillieren | 30 |
| | GF-Mail mit Erfolgskriterien | 30 |
| | Gegenrede Brandtner | 20 |
| | Fremdmaterial / Injection | 15 |
| 2.1 | B = f(P, E) am Workshop 04/2026 | 15 |
| | Fall Kowalczyk | 10 |
| | ADKAR-Scoring vier Gruppen | 35 |
| | Auflösung | 20 |
| 2.2 | Rückwärtsdiagnose | 20 |
| | Vision umschreiben | 20 |
| | Koalition besetzen | 15 |
| | Quick Win wählen | 20 |
| | Blockierender Vorgesetzter | 15 |
| Mittwoch | Kraftfeld vollständig | 60 |

**Wenn die Zeit knapp wird**, zuerst kürzen: Wellen-Diagnose (auf 10 Min. im Plenum), Koalition besetzen (auf eine Namensliste ohne Begründung). **Nicht kürzen:** die Auflösung nach dem ADKAR-Scoring und die Maßnahmenzeile im Kraftfeld. Ohne sie bleibt in beiden Fällen ein Bild statt einer Erkenntnis.

---

## 6. Bewertungsraster

Für Abgaben zu Hellwig — Entscheidungsvorlage, Kraftfeld, ADKAR-Analyse, GF-Mail.

| Kriterium | 1 Punkt | 3 Punkte | 5 Punkte |
|---|---|---|---|
| **Trennung von Fakt, Annahme, Einschätzung** | vermischt | teilweise gekennzeichnet | jede Zahl mit Herkunft, Annahmen als solche benannt |
| **Engpassorientierung** | Mittelwert genannt | Profil beschrieben | die begrenzende Dimension benannt und die Maßnahme daraus abgeleitet |
| **Kategorienschärfe** | „KI" | Kategorie genannt | Kategorie genannt **und** begründet, warum nicht die billigere Nachbarkategorie |
| **Prüfbarkeit** | Adjektive | teils zählbar | jede Aussage entscheidbar, inklusive eines Negativkriteriums |
| **Gegenrede** | fehlt | im Anhang | im Text, mit dem stärksten Einwand und einer Antwort darauf |
| **Maßnahmen** | Kommunikation | gemischt | räumen Hindernisse weg, mit Wer / Bis wann / Woran erkennbar |

**Das trennscharfe Kriterium ist das letzte.** Eine Abgabe, deren Maßnahmen überwiegend aus Information, Kommunikation und Schulung bestehen, hat die Kernaussage der Woche nicht aufgenommen — unabhängig davon, wie gut sie geschrieben ist.

---

## 7. Fehler, die auf der Dozentenseite passieren

| Fehler | Wirkung | Gegenmittel |
|---|---|---|
| Die Firma zu früh vollständig ausgeben | Die Teilnehmenden lesen die Lösung, statt sie zu erarbeiten | Ausbaustufen aus [`05`](05_Kursverlauf-Ausbaustufen.md) einhalten |
| Kraftfeld vorbewertet zeigen | Sie lernen das Bild, nicht das Verfahren | Rohliste austeilen, Referenz erst danach |
| Semmler als Bremser einführen | Beendet die Ursachenanalyse, bevor sie beginnt | Ihn als rational handelnden Bereichsleiter einführen — Kennzahl, Kostenstelle, sechs offene Stellen |
| Die Zahlen als belastbar behandeln | Teilnehmende zitieren sie später | Bei jeder Nennung: erfunden, konstruiert für dieses Beispiel |
| Injects chronologisch spielen wollen | Zeitdruck, halbe Diskussionen | Jedes Inject steht allein. Zwei pro Block genügen |
| V2 als KI-Vorhaben behandeln | Der wichtigste Befund des Kurses geht verloren | Immer die Zerlegung zeigen: 6,4 von 6,5 Tagen sind Liegezeit |

---

## 8. Konsistenzprüfung beim Erweitern

Wer Material ergänzt, prüft diese sechs Größen — an ihnen hängt der Rest:

| Größe | Wert | Steht in |
|---|---:|---|
| Beschäftigte Stammsitz / Konzern | 512 / 1.380 | `00` |
| Reifegrad Daten | 2 | `01` |
| Eingangsrechnungen pro Monat / stabile Lieferanten | 2.050 / 61 | `00`, `material/M2` |
| Ersatzteilanfragen pro Jahr | 12.400 | `00`, `material/M2` |
| Netto-Bearbeitung / Durchlaufzeit Angebot | 47 Min. / 6,5 AT | `00` |
| Nutzung nach dem Prompting-Workshop | 8 % | `00`, `04` |

Eine geänderte Zahl in dieser Liste macht mehrere Übungen falsch. Zahlen außerhalb der Liste sind frei ergänzbar.
