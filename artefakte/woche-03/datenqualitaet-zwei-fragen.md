---
artefakt: Zwei Fragen zu Datenqualität und Governance
woche: 03
datum: 2026-09-07
status: Diskussionsvorbereitung für Tag 3.2, unvalidiert
zweck: die beiden Leitfragen des Vormittags aus der Aktenlage beantworten, statt sie im Plenum zu improvisieren
---

# Zwei Fragen, aus der eigenen Praxis beantwortet

**Anlass:** Die Lektüre zu Tag 3.2 stellt zwei Fragen, die im Plenum aus der eigenen Praxis zu beantworten sind — nicht aus dem Text. Dieses Dokument ist meine Antwort darauf, vor der Diskussion festgehalten.

**Bezug:** RPA-Pilot für standardisierte Änderungsmitteilungen, Bundesagentur für Arbeit (`kontext/vorhaben.md`, `kontext/organisation.md`, `kontext/stakeholder.md`)
**Grundlage:** [`bibliothek/datenqualitaet-governance.md`](#bibliothek/datenqualitaet-governance.md) · [`coursebook/3.2`](#3.2/3.2_Data-Governance-und-RAG.md)

> **Belegstatus vorweg, weil er hier den Unterschied macht.** Ich habe für keine der beiden Fragen eine Messung. Was ich habe, ist eine **unvalidierte Gruppeneinschätzung** zum digitalen Reifegrad (Stand 2026-08-27) und die Dokumentation des Vorhabens. Alles unten ist entsprechend gekennzeichnet: **[Fakt]** aus den Unterlagen · **[Gruppeneinschätzung]**, nicht validiert · **[Ableitung]** von mir. Eine Zahl, die ich nicht habe, steht als Lücke da und wird nicht geschätzt.

**Inhalt:** [1 Frage 1: welche Dimension](#1-frage-1--welche-der-vier-dimensionen-trifft-uns-am-härtesten) · [2 Frage 2: wer ist Accountable](#2-frage-2--wer-ist-accountable-für-unsere-kritischste-datendomäne) · [3 Was ich mitbringe](#3-was-ich-in-die-diskussion-mitbringe) · [4 Belegübersicht](#4-belegübersicht)

---

## 1. Frage 1 — Welche der vier Dimensionen trifft uns am härtesten?

### Die Antwort in einem Satz

**Konsistenz.** Nicht, weil sie den größten Einzelschaden anrichtet — das tut Genauigkeit —, sondern weil sie **strukturell** ist: sie entsteht aus der Systemlandschaft und lässt sich durch Sorgfalt einzelner Beschäftigter nicht ausgleichen.

### Warum Konsistenz, aus der Aktenlage

**[Gruppeneinschätzung]** Drei der sechs Reifegrad-Dimensionen zeigen auf denselben Punkt:

| Dimension | IST | Begründung im Profil | Was das für Datenqualität heißt |
|---|---:|---|---|
| Technologie | 2 | „Viele, aber teilweise getrennte Systeme" | dieselbe Person, dieselbe Adresse, dieselbe Bankverbindung liegt mehrfach vor |
| Daten | 2 | „Große Datenmengen, eingeschränkte gemeinsame Nutzung" | die Bestände existieren, aber nicht als **ein** Bestand |
| Prozesse | 2 | „Medienbrüche und manuelle Bearbeitung" | jeder Medienbruch ist eine Stelle, an der zwei Fassungen auseinanderlaufen |

**[Fakt]** Dazu kommt aus dem Organisationsprofil: zahlreiche Fachverfahren, gesetzliche Vorgaben und eine dezentrale Struktur erschweren eine einheitliche Transformation — bei rund 116.000 Beschäftigten.

**[Ableitung]** Das ist exakt das Muster, das der Kurs am Bosch-Fall zeigt, nur in der Verwaltungsvariante: **nicht durch schlechte Entscheidungen entstanden, sondern durch eine organisch gewachsene Systemlandschaft.** Der Unterschied zu Bosch ist, dass unsere Entitäten keine Produkte sind, sondern Personen und Leistungsfälle — der Schaden einer Verwechslung ist dort größer.

### Woran wir es merken — und woran wir es nicht merken

**[Fakt]** Bemerkbar ist es heute an drei Stellen, alle im Vorhaben dokumentiert:
- **Medienbrüche und manuelle Nacherfassung** — dieselbe Angabe wird mehrfach eingegeben, das ist der Anlass des Pilots überhaupt.
- **Die Messgröße „Fehler- und Nachbearbeitungsquote"** steht bereits im Vorhaben. Sie ist der Ort, an dem Inkonsistenz sichtbar würde.
- **Sonderfälle**, die laut Zuschnitt bei den Mitarbeitenden verbleiben. Ein Teil davon dürfte gar kein fachlicher Sonderfall sein, sondern ein Datenproblem, das als Sonderfall behandelt wird.

**Und jetzt der unangenehme Teil der Frage.** *Woran merken wir es?* — Ehrlich beantwortet: **anekdotisch.** Wir merken es, wenn jemand es meldet.

**[Lücke, keine Schätzung]** Für keine der vier Dimensionen liegt ein Ausgangswert vor. Es gibt keine Dublettenrate, keine Vollständigkeitsquote der Pflichtfelder, keinen Anteil überalteter Einträge. Die Messgröße „Fehler- und Nachbearbeitungsquote" aus dem Vorhaben ist ohne diesen Ausgangswert **nach** dem Pilot nicht interpretierbar — man weiß dann nicht, ob eine Quote von x % gut oder schlecht ist.

Das ist der eigentliche Befund dieser Frage: **die härteste Dimension ist nicht die, die wir messen, sondern die, die wir bemerken, wenn jemand sich beschwert.**

### Der Gegenkandidat, den ich nicht wegdiskutiere

**[Fakt]** Das Vorhaben nennt als zentrales Risiko ausdrücklich: *Fehler bei Personen-, Adress- oder Bankdaten können erhebliche Folgen haben.* Das ist **Genauigkeit**, und es ist die Dimension mit dem höchsten Einzelschaden — eine Leistung auf ein falsches Konto ist kein Komfortproblem.

**[Ableitung]** Warum ich trotzdem bei Konsistenz bleibe: Genauigkeit ist im Pilot bereits als Risiko benannt und bekommt über das geforderte Kontrollkonzept eine Behandlung. Konsistenz hat **keinen Adressaten** in den vier offenen Entscheidungspunkten. Ungelöst ist damit nicht die gefährlichste, sondern die unbeaufsichtigte Dimension.

Ein weiterer Punkt für Konsistenz: RPA überträgt regelbasiert. **[Ableitung]** Regelbasierte Übertragung ist gegenüber Formatabweichungen und Schreibvarianten empfindlicher als ein Mensch, der „Str." und „Straße" stillschweigend gleichsetzt. Der Pilot verschärft die Konsistenzanforderung, statt sie zu entspannen.

### Was die Frage entscheiden würde

Vier Zahlen, alle mit Bordmitteln aus dem bestehenden Data Warehouse erhebbar, keine neue Technik nötig:

1. **Dublettenrate** im betroffenen Bestand — Konsistenz
2. **Vollständigkeitsquote** der Pflichtfelder für die Übertragung — Vollständigkeit
3. **Anteil Einträge mit Stand älter als X Monate** — Aktualität
4. **Anteil Datensätze, die eine einfache Regelprüfung verletzen** (Formatabweichung, unplausibler Wert) — Genauigkeit, maschinell prüfbarer Teil

**[Ableitung]** Diese vier Zahlen gehören **vor** die Freigabe, nicht in die Auswertung danach. Sie kosten wenig und beantworten die Frage, die dieses Dokument nur begründet vermutet.

---

## 2. Frage 2 — Wer ist Accountable für unsere kritischste Datendomäne?

### Die Antwort

**Niemand — jedenfalls ist niemand benannt.**

Die Lektüre nimmt dieser Antwort die Peinlichkeit: *Fällt auf die Frage kein Name ein, ist das die Antwort und keine Wissenslücke.* Ich halte sie deshalb genau so fest.

### Welche Domäne ich für die kritischste halte

**[Ableitung]** Die **Stammdaten der Leistungsberechtigten** — Person, Adresse, Bankverbindung. Begründung: das Vorhaben benennt genau diese drei Felder als die Stelle mit erheblichen Fehlerfolgen, und sie sind zugleich das, was der Pilot automatisiert überträgt. Kritisch ist eine Domäne dort, wo Fehlerfolge und Automatisierungsgrad zusammenfallen.

### Was stattdessen existiert

**[Fakt]** Die Stakeholder-Übersicht führt acht Rollen. In RACI-Begriffen gelesen:

| Rolle aus `stakeholder.md` | Lässt sich lesen als | Accountable für die Datendomäne? |
|---|---|---|
| IT-Systemhaus | **R** — Architektur, Integration, Betrieb, Wartung | nein, das ist der Betrieb der Technik, nicht die Richtigkeit des Inhalts |
| Fachbereich und Prozessverantwortliche | **C**, teils **R** — Anforderungen und Abnahme | am nächsten dran, aber auf den **Prozess** bezogen, nicht auf den **Datenbestand** |
| Datenschutz und Informationssicherheit | **C** — Prüfung vor Verarbeitung realer Fälle | nein, prüft Zulässigkeit, nicht Qualität |
| Geschäftsführung / Finanzleitung | **A** für die **Investitionsentscheidung** | ja — aber für das Vorhaben, nicht für die Daten |
| Sachbearbeitung | **R** im Tagesgeschäft | nein, behebt Einzelfälle ohne Mandat für den Bestand |
| Personalvertretung, Kundinnen und Kunden | **I** bzw. Betroffene | nein |

**[Ableitung]** Das Muster ist genau das, was der Kurs als Normalfall beschreibt: **Responsible ist mehrfach besetzt, Accountable gar nicht.** Es gibt mehrere Stellen, die einen gemeldeten Fehler beheben würden. Es gibt keine, die dafür geradesteht, dass der Bestand insgesamt stimmt.

**[Fakt]** Bestätigt wird das durch die vier offenen Entscheidungspunkte des Vorhabens: Reifegrad-Validierung, Business Case, technischer Vergleich, Kontrollkonzept. Das Kontrollkonzept regelt Datenschutz, Protokollierung und die Behandlung fehlerhafter Übertragungen — also **Meldung und Behebung**. Eine verantwortende Rolle für die Datendomäne kommt in keinem der vier Punkte vor.

### Wer es sein müsste

**[Ableitung]** Nach der Kurslogik eine **Fachrolle, keine IT-Rolle** — jemand aus dem Fachbereich, der die Bedeutung der Felder beurteilen kann. Das IT-Systemhaus kann nicht Accountable sein: es kann feststellen, dass eine Bankverbindung syntaktisch gültig ist, nicht, dass sie die richtige ist. *Wer Datenqualität an die IT delegiert, delegiert sie an Leute, die den Inhalt nicht beurteilen können.*

**Konkreter Vorschlag für das Kontrollkonzept — eine Zeile, kein Konzept:**

> Für die Stammdaten der Leistungsberechtigten ist **[eine benannte Fachrolle]** Accountable. Sie legt fest, was als Qualität gilt, entscheidet über Korrekturen und verantwortet, welche Bestände für die automatisierte Übertragung freigegeben sind — auch **nach** Projektende.

**[Ableitung]** Der Zusatz „auch nach Projektende" ist kein Detail. Aus dem Behördenbeispiel in Woche 2 ist der Verlauf bekannt: Nutzung fällt zurück, sobald das Projektteam aufgelöst ist und niemand die Pflege übernommen hat. Eine RACI-Skizze ohne die Zeile „wer pflegt das nach Projektende" beschreibt einen Zustand, der vier Monate hält.

### Der Prüfpunkt, den ich mitnehme

Die Frage stellt man nicht als Governance-Frage, sondern beiläufig: *Wenn morgen 200 Adressen falsch übertragen wurden — wen ruft man an?* **[Ableitung]** Kommt als Antwort eine Organisationseinheit statt einer Rolle, oder kommen mehrere Antworten, ist die Lücke bestätigt.

---

## 3. Was ich in die Diskussion mitbringe

**Zwei Antworten:**
1. **Konsistenz**, weil sie strukturell aus getrennten Fachverfahren entsteht und im Pilot keinen Adressaten hat — mit dem ausdrücklichen Zugeständnis, dass **Genauigkeit** den höheren Einzelschaden trägt.
2. **Kein Name**, und das ist der Befund. Responsible ist mehrfach besetzt, Accountable ist unbesetzt.

**Drei Fragen an die Runde**, weil ich sie selbst nicht beantworten kann:
- Wie benennt man eine Accountable-Rolle in einer **dezentralen** Organisation, in der eine Datendomäne über viele Dienststellen verteilt gepflegt wird? Eine Rolle je Dienststelle löst die Konsistenz nicht — eine zentrale Rolle hat keinen Zugriff auf die Pflegepraxis vor Ort.
- Reicht es, die vier Kennzahlen einmalig vor der Freigabe zu erheben, oder braucht es sie fortlaufend? **[Ableitung]** Ich vermute fortlaufend, weil die Rückkopplungszeit sonst unbekannt bleibt — belegen kann ich es nicht.
- Wie bekommt man eine Accountable-Rolle besetzt, ohne zusätzliche Stellen? Das ist bei uns die Frage, an der es scheitern wird, nicht die fachliche.

**Ein Argument, das ich für die Finanzleitung mitnehme:** Datenqualität hat bisher kein eigenes Budget. Ein Automatisierungsvorhaben ist oft die erste Gelegenheit, bei der sie eines bekommt — weil sie hier keine Hygienemaßnahme ist, sondern die Voraussetzung dafür, dass die Automatisierung überhaupt funktioniert. Das dreht Datenqualität von einem Kostenpunkt, der das Vorhaben teurer macht, in eine Begründung, die es trägt. **[Ableitung]** Diese Umkehrung ist der Hebel gegenüber einer Finanzleitung, die laut Stakeholder-Übersicht ohnehin erst bei belegtem Reifegrad und vollständigem Business Case zustimmen wird.

---

## 4. Belegübersicht

| Aussage | Typ | Quelle |
|---|---|---|
| ca. 116.000 Beschäftigte, zahlreiche Fachverfahren, dezentrale Struktur, Private Cloud, Data Warehouse, KI-Kompetenzzentrum | **Fakt** aus den Unterlagen | `kontext/organisation.md` |
| Reifegrad IST: Technologie 2, Daten 2, Prozesse 2, Kultur 1, Strategie 2, People 3 | **Gruppeneinschätzung**, Stand 2026-08-27, **nicht validiert** | `kontext/organisation.md`, `kontext/bundesagentur_reifegrad.md` |
| Fehler bei Personen-, Adress- oder Bankdaten können erhebliche Folgen haben | **Fakt** aus den Unterlagen | `kontext/vorhaben.md` |
| Vier offene Entscheidungspunkte, darunter das Kontrollkonzept | **Fakt** aus den Unterlagen | `kontext/vorhaben.md` |
| Acht Stakeholder-Rollen, Finanzleitung als kritische Instanz | **Fakt** aus den Unterlagen | `kontext/stakeholder.md` |
| Konsistenz ist die härteste Dimension | **Ableitung** von mir, aus Reifegrad und Systemlandschaft | dieses Dokument |
| Stammdaten der Leistungsberechtigten sind die kritischste Domäne | **Ableitung** von mir | dieses Dokument |
| Accountable ist unbesetzt | **Ableitung** aus der Aktenlage — belegt ist nur, dass die Rolle **nicht dokumentiert** ist | `kontext/vorhaben.md`, `kontext/stakeholder.md` |
| Dublettenrate, Vollständigkeitsquote, Überalterungsanteil, Regelverletzungsquote | **Lücke** — keine Werte vorhanden, bewusst nicht geschätzt | — |

> **Vorbehalt, der für das ganze Dokument gilt:** Der Reifegrad ist eine Gruppeneinschätzung und noch nicht durch Interviews, Prozessdaten oder Systemanalysen geprüft. Jede Aussage oben, die darauf aufbaut, trägt diesen Vorbehalt mit. Insbesondere ist die niedrige Technologiebewertung mit der tatsächlich vorhandenen IT-Infrastruktur abzugleichen — sie könnte zu pessimistisch sein, was die Begründung für „Konsistenz" schwächen würde.

---

## Nachtrag nach der Diskussion

*Noch offen — hier kommt hinein, was die Runde ergeben hat: welche Dimensionen die anderen genannt haben, ob jemand eine Accountable-Rolle benennen konnte, und was ich an meiner Antwort korrigiere.*
