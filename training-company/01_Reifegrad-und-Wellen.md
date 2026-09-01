---
firma: Hellwig Fördertechnik (fiktiv)
stand: 2026-09-01
bewertungstyp: Einschätzung des Transformation Managers nach 4 Wochen, unvalidiert
betrachtungsraum: Gesellschaft Iserlohn (512 Beschäftigte)
verwendung: Tag 1.4
---

# Digitaler Reifegrad und Wellen-Diagnose

> **Statusvorbehalt.** Diese Bewertung ist eine Einzeleinschätzung nach vier Wochen im Haus, gestützt auf 14 Gespräche, den Kennzahlenauszug in [`material/M2`](material/M2_Kennzahlen.md) und eigene Systemeinsicht. Sie ist **nicht** durch Interviews in der Breite, Prozessdaten oder eine Systemanalyse validiert. Vor Investitionsentscheidungen muss sie überprüft werden.
>
> Jede Stufe ist an einem **prüfbaren Nachweis** festgemacht — nach der Regel aus [1.4 · Abschnitt 4](../coursebook/1.4/1.4_Vier-Wellen-KI-Kategorien-Hype-Cycle.md#4-digital-maturity-die-logik-hinter-allen-modellen). Wer widersprechen will, kann jeden Nachweis einzeln bestreiten. Das ist der Punkt.

---

## Das Profil

**Skala:** 1 = ad hoc, 2 = ansatzweise, 3 = definiert, 4 = gesteuert, 5 = optimiert

| Dimension | IST | ZIEL 18 Mon. | Nachweis für den IST-Wert |
|---|---:|---:|---|
| **Strategie** | 2 | 4 | „Digitalisierungsprogramm 2027" existiert als 12-seitiges Papier, beschlossen 03/2026. Kein eigener Budgetposten im Wirtschaftsplan, keine benannte verantwortliche Person je Maßnahme, kein Meilenstein mit Datum. 2 von 9 Maßnahmen begonnen, 0 abgeschlossen. |
| **Technologie** | 3 | 4 | Drei Kernsysteme produktiv und im Support (SAP ECC, Dynamics, M365). Kein entschiedener S/4-Pfad. 4 Punkt-zu-Punkt-Schnittstellen, davon 2 als CSV-Nachtjob, keine API-Verwaltung, kein Schnittstellen-Monitoring. Fernwartungsdaten technisch vorhanden, aber im Zugriff eines Dritten. |
| **Daten** | **2** | 4 | Materialstamm zentral in SAP gepflegt, **ohne Validierungsregeln**: 11 % der Ersatzteilpositionen ohne Gewichtsangabe, 6 % ohne Maße. 2.400 Kundendubletten zwischen SAP und Dynamics. Keine dokumentierten Qualitätsregeln, kein Data Owner, kein Datenkatalog. Reporting über 23 manuelle Exporte. |
| **Kultur** | **2** | 3 | In 24 Monaten 2 von Fachabteilungen selbst begonnene Piloten; einer wurde ohne Auswertung beendet. In der monatlichen Serviceleitungsrunde waren in den letzten 6 Sitzungen **alle 5 Kennzahlen grün** — bei sinkender EBIT-Marge. Der Abbruch des MES-Projekts 2019 wurde nie ausgewertet. |
| **Prozesse** | **2** | 4 | Ersatzteilangebot durchläuft 4 Systeme und 3 manuelle Übertragungen. Stücklisten Inventor → SAP manuell, 1.150 pro Jahr. 6 % der Kundenaufträge kommen per Fax. Ticketsystem und SAP haben keine Verbindung; Ersatzteilnummern werden abgetippt. |
| **People** | 3 | 4 | Fachkompetenz hoch: Ø 14 Jahre Betriebszugehörigkeit im Service, Ø 11 im Innendienst. 1 Data Analyst (Controlling, 0,5 FTE für Auswertungen), **keine Rolle für Automatisierung oder KI**. Prompting-Workshop 04/2026 für 120 Personen, Nutzung nach 6 Wochen 8 %. 34 Personen nutzen private KI-Konten. |

**Mittelwert: 2,3.** Diese Zahl ist in diesem Dokument absichtlich klein gesetzt, weil sie nichts erklärt.

---

## Wie das Profil zu lesen ist

Die Firma ist **nicht gleichmäßig auf Stufe 2**. Technologie und People liegen auf 3, Daten, Kultur und Prozesse auf 2. Das ergibt eine spezifische Diagnose:

> **Hellwig hat Werkzeuge und Menschen, aber keine verlässlichen Daten, keine belastbaren Abläufe und keine Fehlerkultur.**

Für die Vorhabenauswahl heißt das dreierlei:

| Befund | Konsequenz |
|---|---|
| **Daten auf 2** | Kein GenAI-Vorhaben mit internem Wissen. RAG auf `N:\` erzeugt selbstbewusst falsche Antworten — und niemand merkt es, weil es keine Prüfinstanz gibt. Betrifft **V10** und die Datenteile von **V2** |
| **Prozesse auf 2** | Vor jeder Automatisierung die Königsfrage: guter Prozess oder schlechter? Betrifft **V8** unmittelbar, **V2** mittelbar |
| **Kultur auf 2** | Piloten werden Erfolg melden, gleichgültig wie sie laufen. Sechs Sitzungen mit fünf grünen Kennzahlen sind kein gutes Zeichen, sondern das Ford-Muster aus [2.2 · 8.2](../coursebook/2.2/2.2_Kotter-8-Schritte-Modell.md#82-ford-unter-alan-mulally-koalition-und-handlungsfreiheit-schritte-2-und-5) |

**Die Engpassregel:** Für ein Vorhaben zählt nicht der Mittelwert, sondern die niedrigste **für dieses Vorhaben relevante** Dimension. Der Engpass ist also je Vorhaben ein anderer. Die Zuordnung steht in [`03_Vorhabenportfolio.md`](03_Vorhabenportfolio.md).

### Der Zielwert, der bewusst nicht 4 ist

Kultur steht auf ZIEL 3, nicht 4. Begründung: Eine Organisation, die 2019 ein abgebrochenes Projekt nie ausgewertet hat und in der seit sechs Monaten alle Kennzahlen grün sind, springt in 18 Monaten nicht auf „gesteuert". Ein ZIEL von 4 wäre eine Absichtserklärung, kein Plan — und die erste Zahl, die im Steuerkreis niemand ernst nimmt.

Das ist der Unterschied zwischen einer Reifegradtabelle und einer Reifegradaussage.

---

## Wellen-Diagnose

| Welle | Zustand bei Hellwig | Belegt durch |
|---|---|---|
| **1 · Mainframe / ERP** | **weitgehend abgeschlossen, mit Altlast** | SAP ECC ist führendes System für Aufträge, Material, Finanzen. Aber: Datenqualität ohne Regelwerk — eine Welle-1-Schuld, die in Welle 4 sichtbar wird |
| **2 · Internet / Kundenschnittstelle** | **nicht abgeschlossen** | Kein Kundenportal. 6 % der Aufträge per Fax, 79 % per E-Mail. Keine digitale Transaktionsstrecke zum Kunden. Zwei Wettbewerber haben eine |
| **3 · Mobile & Cloud / APIs** | **unvollständig** | M365 in der Cloud, aber 23 von 23 kritischen Auswertungen über manuelle Exporte. 4 Punkt-zu-Punkt-Schnittstellen, keine API-Verwaltung. Fernwartungsdaten bei einem Dritten |
| **4 · AI & Data** | **nicht begonnen, aber schon beschlossen** | Steuerkreis 08/2026 hat eine „Pilotphase KI" beschlossen, inklusive eines Agentic-Vorhabens (V5) |

### Der Satz, der die Diagnose zusammenfasst

> **Hellwig will in Welle 4 einsteigen und hat Welle 2 nie abgeschlossen.** Das Ersatzteilgeschäft verliert Aufträge nicht, weil kein KI-Assistent Angebote schreibt, sondern weil es keinen Weg gibt, auf dem eine Anfrage digital hereinkommt und ein Angebot digital hinausgeht.

Das ist die unbequeme Version. Die bequeme wäre „wir brauchen eine KI-Strategie" — und sie würde 200.000 EUR kosten, ohne die Auftragsquote zu bewegen.

**Was daraus nicht folgt.** Es folgt nicht „erst Welle 2 fertig, dann KI". Die belastbare Aussage der Wellenlogik ist Komplementarität, nicht Reihenfolge: Wo eine Schicht fehlt, wird die darüberliegende teuer. Praktisch heißt das, die fehlende Vorleistung **im selben Budget** auszuweisen, statt sie später als Überraschung zu entdecken. Für V2 sind das der Portalzugang und die Datenpflege, zusammen rund zwei Drittel des Aufwands.

---

## Die Diagnosefrage, angewandt

> *Könnten wir die Frage, die wir der KI stellen wollen, mit unseren heutigen Daten überhaupt korrekt beantworten — von Hand, mit genug Zeit?*

| Vorhaben | Frage an die KI | Von Hand beantwortbar? |
|---|---|---|
| **V2** Ersatzteilangebot | „Was kostet Teil X inklusive Fracht?" | **Nein** — bei 11 % der Positionen fehlt das Gewicht. Kein Mensch und keine KI kann daraus einen Frachtpreis ableiten |
| **V3** Predictive Maintenance | „Welche Anlage fällt in den nächsten 30 Tagen aus?" | **Nein** — Ausfälle stehen als Freitext in Serviceberichten, nicht als datierte Ereignisse. Es gibt nichts zu lernen |
| **V6** Ersatzteilbedarf | „Wie viele Stück von Teil X brauchen wir im Q1?" | **Ja** — Bewegungsdaten liegen seit 2011 in SAP, sauber und datiert |
| **V10** Wissensassistent | „Wie tausche ich das Getriebe an Anlagentyp F-220?" | **Teilweise** — die Information existiert, verteilt über 2.400 PDF-Dateien auf `N:\` ohne Struktur und ohne Berechtigungskonzept |

**Zwei von vier sind Datenprojekte, die sich als KI-Projekte vorstellen.** Das ist der häufigste Befund einer solchen Prüfung, und er kostet nichts außer einer Stunde Nachdenken.

---

## Was zu tun ist, um die Bewertung belastbar zu machen

Die Bewertung oben ist eine Einschätzung. Sie wird zu einer Grundlage durch vier Schritte:

| # | Schritt | Aufwand | Ergebnis |
|---|---|---|---|
| 1 | Datenqualität messen statt schätzen: Vollständigkeitsquote je Pflichtfeld im Material- und Kundenstamm, per SQL auf dem SAP-Auszug | 2 Tage | Dimension Daten belegt oder widerlegt |
| 2 | Prozessaufnahme Ersatzteilangebot mit Zeitmessung, 40 Vorgänge, alle Liegezeiten getrennt erfasst | 5 Tage | Engpass belegt; Grundlage für jeden Business Case |
| 3 | 12 Interviews à 30 Minuten quer über Bereiche und Ebenen, nach dem [ADKAR-Leitfaden](../coursebook/2.1/01_Change-Management-Lewin-ADKAR.md#11-werkzeugkasten-für-den-transformation-manager) | 3 Tage | Dimensionen Kultur und People belegt |
| 4 | Schnittstellen- und Berechtigungsinventur, inklusive `N:\`-Struktur | 4 Tage | Dimension Technologie belegt; Voraussetzung für jede RAG-Entscheidung |

14 Tage. Das ist die Antwort auf die Frage, was der Transformation Manager in den ersten sechs Wochen tut — und sie ist im Steuerkreis unbeliebt, weil in diesen 14 Tagen nichts sichtbar entsteht.

**Die Formulierung, die hilft:** *„Ich kann in vier Wochen einen Piloten starten oder in zwei Wochen wissen, welcher Pilot der richtige ist. Das zweite ist billiger."*
