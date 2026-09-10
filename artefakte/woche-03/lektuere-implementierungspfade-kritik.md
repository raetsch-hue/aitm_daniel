---
artefakt: Kritik der Lektüre Implementierungspfade und Reifegrade
woche: 03
datum: 2026-09-10
status: Argumentationsgrundlage für die Empfehlungsverteidigung, Tag 3.3/3.4
zweck: die Lektüre gegen die betriebliche Realität im öffentlichen Dienst stellen und die angreifbaren Zahlen kennen, bevor sie im Plenum zitiert werden
bezug: coursebook/3.3/3.3_Implementierungspfade-und-Workspace.md
quelle: https://neuefische-teaching.github.io/AIDTM/coursebook/woche-3/lektuere-implementierungspfade-w3.html
herkunft: eigene Analyse. Die Gegenbelege (S&P Global, McKinsey State of AI, MIT CISR) sind benannt, aber nicht an der Primärquelle gegengeprüft — vor Verwendung im Plenum verifizieren
---

# Kritische Analyse: Wie KI in Produktion kommt — Implementierungspfade und Reifegrade

**Gegenstand:** Lektüre Woche 3, Tag 3.3 ([Course Book](https://neuefische-teaching.github.io/AIDTM/coursebook/woche-3/lektuere-implementierungspfade-w3.html))  
**Zweck:** Fundierte Gegenüberstellung der Lehrmaterialien mit der betrieblichen Realität (Konzern/Öffentlicher Dienst), Aufdeckung von methodischen Schwachstellen und Vorbereitung auf die Empfehlungsverteidigung am Donnerstag.

---

## Executive Summary: Kernergebnis auf einen Blick

Die Lektüre liefert eine gut lesbare und didaktisch eingängige Motivation für den Unterschied zwischen Experiment und Produktion. Sie schärft das Bewusstsein dafür, dass KI-Vorhaben primär an organisatorischen und planerischen Hürden scheitern.

Bei genauer fachlicher und methodischer Prüfung weist der Text jedoch **drei gravierende Schwachstellen** auf:

1. **Faktische und methodische Ungenauigkeiten:**
   - Ein mathematischer Logikfehler deklariert 42 % zur „Mehrheit“.
   - Die 42-%-Abbruchquote stammt originär von S&P Global Market Intelligence, wird im Text aber fälschlich McKinsey zugeschrieben.
   - Die Zahl „35 % weniger Probleme durch schrittweisen Rollout (McKinsey 2024)“ ist eine isolierte Scheingenauigkeit („Management-Mythos“) ohne methodische Belastbarkeit.
   - Zwei unvereinbare Zeitlogiken werden unkommentiert nebeneinandergestellt: Ein 90-Tage-SaaS-Lizenz-Rollout (OpenAI) kollidiert frontal mit einem 18- bis 36-monatigen Transformationsmodell (MIT CISR).

2. **Kritische inhaltliche Lücken:**
   - **Regulatorik & Mitbestimmung fehlen vollständig:** Kein Wort zum EU AI Act, zur DSGVO/Datensouveränität oder zur Beteiligung von Betriebs- bzw. Personalräten (§ 87 BetrVG / BPersVG). In Deutschland scheitern Rollouts regelmäßig hieran, nicht an der Technik.
   - **Worthülse „Produktionsreife“:** Der Text fordert die Unterscheidung zwischen Pilot und Produktion, benennt aber die konkreten Kriterien für den Produktivbetrieb nicht (NFRs, LLMOps, RBAC/Berechtigungen, FinOps, Security).
   - **Verengung und Überhöhung des Datenkatalogs:** Fokussierung auf klassische Tabellen-Metadaten ignoriert, dass moderne GenAI-Anwendungen primär unstrukturierte Dokumente (SharePoint, Wikis, PDFs) und granulare Zugriffsrechte (ACLs) erfordern.
   - **Inhaltsleeres Fallbeispiel Deutsche Telekom:** Es werden weder die gewählte Architektur noch konkrete Kriterien genannt; die Argumentation verbleibt in einer tautologischen Floskel („Entschieden für das, was passte“).

3. **Didaktische Diskrepanz:**
   - Ausgewiesene Lesezeit von **40 Minuten** bei einem Textumfang von lediglich ca. 850 Wörtern (reine Lesezeit ~4 Minuten).
   - Der Passwortschutz (`#aitm`) ist lediglich eine oberflächliche clientseitige CSS-/JS-Sperre; die Inhalte liegen unverschlüsselt im HTML-Quelltext.

---

## 1. Detailanalyse: Was ist ungenau oder sachlich fragwürdig?

### 1.1 Mathematischer Logikfehler & Quellen-Fehlzuordnung bei den Abbruchquoten

* **Textstelle:**  
  > *„42 Prozent der Unternehmen haben 2024 die meisten ihrer KI-Initiativen abgebrochen, bevor sie Produktion erreichten. Das ist keine Randnotiz, das ist die Mehrheit der Versuche.“* (Quellenangabe: *McKinsey & Company, The State of AI, 2024*)
* **Kritik:**
  - **Mathematischer Widerspruch:** 42 % sind mathematisch eine Minderheit, nicht die Mehrheit.
  - **Kategoriale Verwechslung:** Wenn 42 % der *Unternehmen* einen Großteil ihrer Projekte abbrechen, bedeutet das keineswegs, dass 42 % aller *Initiativen* abgebrochen wurden, noch dass dies die „Mehrheit der Versuche“ über alle Unternehmen hinweg darstellt.
  - **Quellen-Fehler:** Die vielzitierte Zahl von 42 % abgebrochenen Initiativen (und ~46 % verworfenen POCs) stammt aus dem Enterprise-Report von **S&P Global Market Intelligence (2024/2025)**. McKinsey berichtet im *State of AI (2024/2025)* stattdessen über das Phänomen der „Pilot Purgatory“ (nur ca. 39 % berichten von signifikantem EBIT-Impact, nur 6 % sind echte High Performer), nennt diese 42-%-Zahl aber so nicht.
* **Risiko für Donnerstag:** Wenn im Vorstand jemand nachrechnet oder die Quelle prüft, verliert der Pitch sofort an Glaubwürdigkeit.

---

### 1.2 Scheingenauigkeit: Die „35-Prozent-Regel“ von McKinsey

* **Textstelle:**  
  > *„schrittweise Rollouts reduzieren kritische Probleme um 35 Prozent gegenüber gleichzeitigen (McKinsey 2024). Das ist die Zahl, die man parat haben sollte, wenn jemand aus Ungeduld einen Big-Bang-Rollout vorschlägt.“*
* **Kritik:**
  - **Kontextlose Pseudo-Präzision:** Was ist ein „kritisches Problem“? Gegenüber welcher Baseline? In welchem Sektor? Bei welcher Systemkomplexität?
  - McKinsey publiziert regelmäßig Transformationsstatistiken (z. B. 70 % aller digitalen Transformationen verfehlen ihre Ziele), aber eine isolierte Kausalitätsmetrik von exakt „35 % weniger kritische Probleme bei stufenweisem KI-Rollout“ existiert als belastbare wissenschaftliche Kenngröße nicht. Häufig werden Zahlen aus Legacy-ERP-Rollouts oder IT-Performance-Indizes unreflektiert auf GenAI übertragen.
* **Risiko für Donnerstag:** Eine solche Zahl als Totschlagargument zu nutzen, wirkt vor einer IT-Leitung oder einem CFO angreifbar, sobald nach der Erhebungsmethode gefragt wird.

---

### 1.3 Konzeptueller Widerspruch der Zeithorizonte (OpenAI vs. MIT CISR)

Der Text stellt zwei Modelle direkt hintereinander:

| Dimension | Framework 1: OpenAI (4 Phasen) | Framework 2: MIT CISR (4 Stufen) |
|---|---|---|
| **Zeithorizont** | **0 bis 90+ Tage** (Taktung in 30-Tage-Schritten) | **18 bis 36 Monate** (Großunternehmen) / 6–12 Mon. (KMU) |
| **Fokus** | Tool-Adoption / SaaS-Lizenzierung (ChatGPT Enterprise) | Sozio-technische Transformation & Infrastruktur |
| **Scale-Definition** | Tag 90: „MVP, dann Pilot, dann Rollout“ | Ab Monat 24: „KI als reguläre Infrastruktur“ |

* **Kritik:**
  - Der Text unterschlägt, dass es sich um **völlig unterschiedliche Gegenstände** handelt.
  - OpenAI beschreibt ein **Hersteller-Playbook zur schnellen Software-Einführung** (Accounts verteilen, Champions schulen, Prompting üben). Das skaliert in 90 Tagen.
  - MIT CISR beschreibt die **strukturelle Transformation von Geschäftsprozessen und Architekturen**. Dies dauert Jahre.
  - Wer dem Vorstand suggeriert, man könne Phase 4 („Scale“) nach Tag 90 erreichen, erzeugt genau die unrealistischen Erwartungshaltungen, die der Text im ersten Absatz als Hauptgrund für das Scheitern benennt.

---

## 2. Was fehlt grundlegend? (Die blinden Flecken)

### 2.1 Regulatorik, Compliance & Mitbestimmung (Der deutsche/europäische Kontext)

Der Text erwähnt beiläufig „Governance-Anforderungen“, ignoriert jedoch die drei maßgeblichen Faktoren für Enterprise-KI im europäischen Raum:

1. **EU AI Act:**
   - Pflicht zur Risikoklassifizierung (Minimal, Spezifische Transparenz, Hochrisiko, Verboten).
   - Bei Hochrisiko-Systemen (z. B. HR-Scoring, Bonitätsprüfung, Leistungsverwaltung im Sozialrecht): Umfassende Dokumentations-, Test-, Logging- und Überwachungspflichten vor Produktivsetzung.
2. **Datenschutz (DSGVO) & Cloud-Souveränität:**
   - Verarbeitung von personenbezogenen Daten (PII) im Prompting/RAG.
   - Auftragsverarbeitungsverträge (AVV), Third-Country-Data-Transfers (Schrems II, EU-US Data Privacy Framework).
   - Notwendigkeit von On-Premise- bzw. souveränen Cloud-Instanzen (z. B. Azure EU Data Boundary, Delos Cloud).
3. **Betriebsrat / Personalrat (§ 87 BetrVG / § 80 BPersVG):**
   - In deutschen Großunternehmen und Behörden (wie Telekom, BA, Bahn) scheitern oder verzögern sich Rollouts primär an Mitbestimmungsverfahren bezüglich Überwachung von Leistung und Verhalten (§ 87 Abs. 1 Nr. 6 BetrVG).
   - **Ohne Betriebsvereinbarung kein produktiver Rollout.** Dieser Aspekt wird in angloamerikanischen Frameworks (OpenAI) systematisch ausgeblendet und fehlt auch in dieser Lektüre vollständig.

---

### 2.2 Fehlende Kriterien für „Produktionsreife“ (Non-Functional Requirements)

Der Text fordert zu Recht die Abgrenzung: *„Ein Pilot ist ein kontrolliertes Experiment... Produktion heißt regulärer Betrieb“*. Er lässt die Lernenden jedoch im Stich bei der Beantwortung der Kernfrage: **Was genau fehlt denn für die Produktion?**

Für eine Verteidigung am Donnerstag müssen folgende NFR-Dimensionen (Non-Functional Requirements) benannt werden:

```
                      +------------------------------------------+
                      |         PRODUKTIONSREIFE (NFRs)          |
                      +------------------------------------------+
                                           |
         +-----------------+---------------+----------------+-----------------+
         |                 |                                |                 |
         v                 v                                v                 v
   [ARCHITEKTUR &    [DATEN & RECHTE]                 [QUALITÄT &       [FINANZEN &
      BETRIEB]                                         SICHERHEIT]       PROZESSE]
  - Latenz (P95/P99) - Granulare ACLs/RBAC            - Halluzinations- - Token-Budget /
  - SLA (99.9%)        (Dokumentenberechtigung)         monitoring        FinOps
  - Fallback-Pfade   - Data Staleness / Update-Zyklen - Prompt Injection/ - Human-in-the-
  - Rate Limits &    - Anonymisierung / PII-Filter      Jailbreak Schutz  Loop Eskalation
    Load Balancing   - Data Lineage                   - Groundedness /  - Support- &
                                                        Eval-Frameworks   Schulungskonzept
```

1. **Rechte- und Rollensynchronisation (ACLs / RBAC):**  
   Im Piloten testen 10 Personen mit denselben Dokumenten. In Produktion darf Nutzer A in der semantischen RAG-Suche nur Dokumente finden, für die er im Quellsystem (SAP, SharePoint) leseberechtigt ist. Das Fehlen dieses Berechtigungskonzepts ist der häufigste Showstopper bei RAG-Systemen.
2. **LLMOps & Evaluation:**  
   Wie wird Drift überwacht? Welche Halluzinationsrate wird toleriert? Gibt es automatisierte Benchmarks (RAG Triad: Context Relevance, Groundedness, Answer Relevance)?
3. **Security & Guardrails:**  
   Schutz gegen Indirect Prompt Injection, Exfiltration vertraulicher Daten, Jailbreaking.
4. **FinOps:**  
   Vom Pauschaltarif des Piloten zu variablen Token-Kosten unter Last: Unkontrollierte Kostenexplosionen verhindern.

---

### 2.3 Überhöhung und Engführung des Datenkatalogs

* **Textstelle:**  
  > *„Der Datenkatalog ist das Inhaltsverzeichnis, nicht das Buch... Ohne Katalog beginnt jedes Projekt mit derselben Woche Suchen.“*
* **Kritik:**
  - Der Text tut so, als löse ein klassischer Enterprise Data Catalog (wie Collibra oder Alation) das Datenproblem für KI.
  - **Realität:** Klassische Datenkataloge verwalten **strukturierte Tabellen** (SQL-Datenbanken, Schemata, Data Warehouses). Moderne generative KI und RAG benötigen jedoch zu über 80 % **unstrukturierte Daten** (PDFs, Word-Dateien, Confluence-Wikis, E-Mails, Tickets).
  - Ein Datenkatalog sagt nichts über Formatierungschaos, widersprüchliche Dokumentversionen oder fehlende Berechtigungsstrukturen aus. Ein Datenkatalog ist nützlich, aber für GenAI-Implementierungen keineswegs die hinreichende Vorbedingung.

---

### 2.4 Inhaltsleere Fallstudie: Deutsche Telekom

* **Textstelle:**  
  > *„Der Weg der Telekom führte von verstreuten lokalen Lösungen zu einer konzernweiten KI-Plattform... es wurde nicht die technisch überlegenste Lösung gewählt. Entschieden wurde für die, die zu den Governance-Anforderungen und zum Reifegrad passte...“*
* **Kritik:**
  - Das Fallbeispiel bleibt vollkommen abstrakt. Weder wird die Plattform benannt (handelte es sich um Azure OpenAI Service, ein modulares LLM-Gateway, T-Systems Agentic Hub oder Aleph Alpha?), noch werden die tatsächlichen Kriterien oder Laufzeiten offengelegt.
  - Die Aussage *„Passung schlägt Funktionsumfang“* ist eine Binsenweisheit. Spannend und lehrreich wäre gewesen: **Welche Funktionen wurden bewusst abgewählt**, um Datenschutz, Mitbestimmung oder Betriebsrat zu genügen?

---

### 2.5 Differenzierung nach Use-Case-Typen fehlt

Der Text wirft alle KI-Vorhaben in einen Topf. In der Praxis verlaufen die Implementierungspfade jedoch je nach technologischem Archetyp fundamental verschieden:

```
+---------------------------+---------------------------+---------------------------+
| 1. SaaS Assistent         | 2. Enterprise RAG         | 3. Agentische Automation  |
| (z.B. Copilot / ChatGPT)  | (Wissensmanagement)       | (Prozesskette / API-Call) |
+---------------------------+---------------------------+---------------------------+
| Fokus: Change Management, | Fokus: Datenaufbereitung, | Fokus: Schnittstellen,    |
| Prompt-Schulungen, Lizenz-| Chunking, Vektordatenbank,| Error-Handling, Autonomie-|
| verteilung, Betriebsrat.  | ACLs/Rechte, Retrieval.   | grenzen, Transaktionslogik|
| Laufzeit: 1 - 3 Monate    | Laufzeit: 6 - 12 Monate   | Laufzeit: 12 - 24 Monate  |
+---------------------------+---------------------------+---------------------------+
```

---

## 3. Didaktische Schwachstellen im Kurskontext

1. **Diskrepanz Lesezeit vs. Textumfang:**
   - Angegeben: **40 Minuten Lesezeit**.
   - Tatsächlicher Umfang: **854 Wörter** (ca. 4 Minuten Lesezeit).
   - Selbst bei intensiver Reflexion ist der Text zu dünn, um 40 Minuten Lesezeit ohne zusätzliche Primärquellen zu rechtfertigen.
2. **Fehlleitung vor der Hack Time:**
   - Der Text suggeriert: Was man in einer 30-minütigen Hack Time tut (PDF hochladen, RAG-Antwort mit Quellenangabe erzeugen, Agent konfigurieren), entspreche der OpenAI-Phase *„Foundations“*.
   - **Tatsächlich:** Das Ausprobieren einer Web-Oberfläche ist ein unverbindlicher Spielwiesen-Test (MIT Stage 1 / Experiment). Phase 1 bei OpenAI erfordert die Definition des Geschäftsproblems, Governance-Klärung und Business-Impact-Analyse. Die Übung im Browser mit organisatorischen Foundations gleichzusetzen, verharmlost den Aufwand für Enterprise-KI.

---

## 4. Konkrete Argumentationshilfen für die Empfehlungsverteidigung (Donnerstag)

Wenn am Donnerstag die Plattform-Empfehlung im Rollenspiel oder vor dem Prüfungsgremium verteidigt werden muss, sollten folgende Punkte aus dieser Kritik aktiv eingebracht werden:

1. **Begründungslogik „Passung vor Funktion“ präzisieren:**
   - Nicht nur sagen: *„Weil es zum Reifegrad passt.“* (Das ist ein Zirkelschluss).
   - Sondern konkretisieren: *„Wir verzichten bewusst auf Feature X (z. B. autonome Agentenfunktionen oder Closed-Source-Modelle der US-Hyperscaler), weil unsere Datenlandschaft die nötigen Rechte-Synchronisationen noch nicht automatisiert unterstützt und die Mitbestimmung (Personalrat/Betriebsrat) hierfür aktuell keine Freigabe erteilt.“*
2. **Den Übergang von Pilot zu Produktion konkret beziffern:**
   - Auf die Frage: *„Warum dauert der Rollout nach dem erfolgreichen Piloten noch 12 Monate?“*
   - Antwort: *„Der Pilot hat die Machbarkeit mit bereinigten Daten und 20 geschulten Power-Usern bewiesen. Für die Produktion fehlen uns vier industrielle NFR-Bausteine: 1. RBAC-Berechtigungsfilter auf Dokumentenebene, 2. LLMOps-Monitoring für Halluzinationserkennung, 3. Dienstvereinbarung mit dem Personalrat zur Leistungsüberwachung, 4. Anbindung an das Ticketsystem mit definiertem Human-in-the-Loop-Fallback.“*
3. **Realistische Zeithorizonte einfordern:**
   - Nicht auf 90-Tage-Versprechen der SaaS-Anbieter hereinfallen. Klare Trennung im Pitch:
     - *Tool-Bereitstellung (SaaS-Accounts)*: 3 Monate.
     - *Integrierte Wertschöpfung & Prozessänderung (Ways of Working)*: 12 bis 24 Monate.

---

## 5. Fazit

Die Lektüre liefert wertvolle Impulse zur Vermeidung von voreiligem Technologie-Aktionismus. Sie bleibt jedoch in der Management-Oberfläche stecken, arbeitet mit teils schiefen oder pseudopräzisen Statistiken und blendet die härtesten Hürden des europäischen Marktes (EU AI Act, Mitbestimmung, granulare Zugriffsrechte und industrielle Non-Functional Requirements) vollständig aus.

Für einen angehenden Digital & AI Transformation Manager ist der Text als Einstiegsmotivation brauchbar, als fachliche Entscheidungsgrundlage für die Praxis jedoch unvollständig und in Teilen irreführend.
