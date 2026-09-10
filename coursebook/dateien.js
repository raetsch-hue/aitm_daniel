/* ------------------------------------------------------------------
   Liste der Dokumente, die viewer.html anzeigt.

   Neue Datei?  Hier eine Zeile ergänzen.  Datei gelöscht?  Zeile raus.
   Das ist die EINZIGE Stelle, die gepflegt werden muss.

   - Pfade sind relativ zu viewer.html
   - Die Reihenfolge hier ist egal: der Viewer sortiert aufsteigend nach
     der Nummer im Pfad (1.4 < 1.5 < 1.10 < 2.1)
   - Beim Öffnen erscheint das zuletzt gelesene Dokument, beim ersten
     Besuch das erste der sortierten Liste
   - Ein Komma zu viel am Ende ist hier erlaubt (anders als in JSON)

   BEREICHE
   Der Viewer hat oben im Kopf einen Umschalter "Bereich". Zu welchem
   Bereich ein Dokument gehört, erkennt er am Pfad; "bereich" muss man
   also nur setzen, wenn der Pfad es nicht verrät.
   - coursebook: alles unterhalb von coursebook/  (Standard)
   - bibliothek: alles unterhalb von ../bibliothek/
   - artefakte:  alles unterhalb von ../artefakte/
   ------------------------------------------------------------------ */

var DOKUMENTE = [

  /* ================= COURSEBOOK ================= */

  // ---- Einstieg ----
  { datei: "0/00_Index-und-Gewichtung.md",
    titel: "0 · Index & Gewichtung" },

  { datei: "0/01_Weiterfuehrende-Quellen.md",
    titel: "0 · Weiterführende Quellen" },

  // ---- Woche 1 ----
  { datei: "1.4/1.4_Vier-Wellen-KI-Kategorien-Hype-Cycle.md",
    titel: "1.4 · Vier Wellen, KI-Kategorien, Hype Cycle" },

  { datei: "1.5/1.5_Strategisches-Prompt-Engineering.md",
    titel: "1.5 · Strategisches Prompt Engineering" },

  // ---- Woche 2 ----
  { datei: "2.1/01_Change-Management-Lewin-ADKAR.md",
    titel: "2.1 · Vertiefung: Lewin & ADKAR" },

  { datei: "2.2/2.2_Kotter-8-Schritte-Modell.md",
    titel: "2.2 · Kotters 8-Schritte-Modell" },

  { datei: "2.2/2.2_Ergaenzung-Force-Field-Analyse.md",
    titel: "2.2 · Werkzeug: Force-Field-Analyse (Ergänzung)" },

  { datei: "2.3/2.3_Kraefte-sichtbar-machen.md",
    titel: "2.3 · Kräfte sichtbar machen (Analyse)" },

  { datei: "2.4/2.4_Widerstand-ist-eine-Information.md",
    titel: "2.4 · Widerstand ist eine Information (Analyse)" },

  { datei: "2.5/2.5_Die-Woche-wird-ein-Plan.md",
    titel: "2.5 · Die Woche wird ein Plan (Analyse)" },

  // ---- Woche 3 ----
  { datei: "3.1/3.1_KI-Plattformen-im-Vergleich.md",
    titel: "3.1 · KI-Plattformen im Vergleich (Analyse)" },

  { datei: "3.2/3.2_Data-Governance-und-RAG.md",
    titel: "3.2 · Data Governance und RAG (Analyse)" },

  { datei: "3.3/3.3_Implementierungspfade-und-Workspace.md",
    titel: "3.3 · Implementierungspfade und Workspace (Analyse)" },

  { datei: "3.4/3.4_Die-Entscheidung-vertreten.md",
    titel: "3.4 · Die Entscheidung vertreten (Analyse)" },

  { datei: "3.5/3.5_Synthese-Plattform-Daten-Umsetzung.md",
    titel: "3.5 · Synthese: Plattform, Daten, Umsetzung (Analyse)" },

  // ---- Kurzfassungen ----
  { datei: "essentials/2.3_Essentials-Kraefte-sichtbar-machen.md",
    titel: "2.3 · Essentials: Kräfte sichtbar machen" },

  { datei: "essentials/2.4_Essentials-Widerstand.md",
    titel: "2.4 · Essentials: Widerstand ist eine Information" },

  { datei: "essentials/2.5_Essentials-Die-Woche-wird-ein-Plan.md",
    titel: "2.5 · Essentials: Die Woche wird ein Plan" },

  { datei: "essentials/3.0_Essentials-Woche-3.md",
    titel: "3.0 · Essentials: Woche 3 komplett" },

  /* ================= BIBLIOTHEK =================
     Eigene Nachschlage-Einträge aus ../bibliothek/.
     Pfad beginnt mit ../ , weil viewer.html in coursebook/ liegt.
     Sortiert wird hier alphabetisch nach Titel, nicht nach Nummer.  */

  { datei: "../bibliothek/lewin-adkar.md",
    titel: "Lewin & ADKAR",
    bereich: "bibliothek" },

  { datei: "../bibliothek/kotter-forcefield.md",
    titel: "Kotter & Force Field",
    bereich: "bibliothek" },

  { datei: "../bibliothek/widerstand.md",
    titel: "Widerstand",
    bereich: "bibliothek" },

  { datei: "../bibliothek/datenqualitaet-governance.md",
    titel: "Datenqualität, RAG & Governance",
    bereich: "bibliothek" },

  { datei: "../bibliothek/vendor-evaluation.md",
    titel: "Vendor Evaluation",
    bereich: "bibliothek" },

  /* ================= ARTEFAKTE =================
     Eigene Arbeitsergebnisse aus ../artefakte/.
     Der folgende Block wird von coursetools/inhalt-bauen.py erzeugt.  */

  /* >>> ARTEFAKTE-ANFANG (13 Dokumente, 2026-09-10)
      Automatisch erzeugt von coursetools/inhalt-bauen.py.
      Nicht von Hand aendern - Aenderungen gehen beim naechsten Lauf
      verloren. Anzeigetitel stellt man im Skript unter TITEL ein.  */

  { datei: "../artefakte/INHALT.md",
    titel: "Alle Themen · Inhaltsverzeichnis",
    bereich: "artefakte" },

  { datei: "../artefakte/checkliste.md",
    titel: "Checkliste · Wissensüberprüfung (laufend)",
    bereich: "artefakte" },

  { datei: "../artefakte/woche-01/gegenrede.md",
    titel: "Woche 01 · Gegenrede zum RPA-Pilot",
    bereich: "artefakte" },

  { datei: "../artefakte/woche-01/kursmaterial.md",
    titel: "Woche 01 · Kursmaterial",
    bereich: "artefakte" },

  { datei: "../artefakte/woche-01/lernziele.md",
    titel: "Woche 01 · Lernziele",
    bereich: "artefakte" },

  { datei: "../artefakte/woche-01/manual-of-me.md",
    titel: "Woche 01 · Manual of Me",
    bereich: "artefakte" },

  { datei: "../artefakte/woche-02/kursmaterial.md",
    titel: "Woche 02 · Kursmaterial",
    bereich: "artefakte" },

  { datei: "../artefakte/woche-03/lektuere-implementierungspfade-kritik.md",
    titel: "Woche 03 · Kritik der Lektüre Implementierungspfade und Reifegrade",
    bereich: "artefakte" },

  { datei: "../artefakte/woche-03/datenqualitaet-zwei-fragen.md",
    titel: "Woche 03 · Zwei Fragen zu Datenqualität und Governance",
    bereich: "artefakte" },

  { datei: "../artefakte/extra/README.md",
    titel: "Extra · 0 Übersicht",
    bereich: "artefakte" },

  { datei: "../artefakte/extra/01_modelle-und-verfahren.md",
    titel: "Extra · 1 Modelle und Verfahren, die nur genannt wurden",
    bereich: "artefakte" },

  { datei: "../artefakte/extra/02_zahlen-und-befunde.md",
    titel: "Extra · 2 Zahlen und Befunde, die nicht behandelt wurden",
    bereich: "artefakte" },

  { datei: "../artefakte/extra/03_spannungen-und-blinde-flecken.md",
    titel: "Extra · 3 Spannungen und blinde Flecken",
    bereich: "artefakte" },
  /* <<< ARTEFAKTE-ENDE */

  /* ================= BEISPIELE ================= */

  { datei: "../examples/fallbeispiele.md",
    titel: "Fallbeispiele im Kurs (Übersicht)",
    bereich: "examples" },

  /* ================= LERNTAGEBUCH ================= */

  { datei: "../lerntagebuch/lerntagebuch.md",
    titel: "Lerntagebuch (Stand 2.2)",
    bereich: "lerntagebuch" },

  /* ================= MCP-KURS =================
     Offline-Kopie des Hugging-Face-MCP-Kurses, aufbereitet aus
     ../AI_Course/mcp-course/units/*.mdx. Der folgende Block wird von
     coursetools/mcp-course-aufbereiten.py erzeugt.  */

  /* >>> MCP-COURSE-ANFANG (37 Dokumente, 2026-09-09)
      Automatisch erzeugt von coursetools/mcp-course-aufbereiten.py.
      Nicht von Hand aendern - Aenderungen gehen beim naechsten Lauf
      verloren.  */

  { datei: "../AI_Course/mcp-course/README.md",
    titel: "00 · Über diese Offline-Kopie",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/01_unit0-introduction.md",
    titel: "01 · U0 · Welcome to the MCP Course",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/02_unit1-introduction.md",
    titel: "02 · U1 · Introduction to Model Context Protocol (MCP)",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/03_unit1-key-concepts.md",
    titel: "03 · U1 · Key Concepts and Terminology",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/04_unit1-architectural-components.md",
    titel: "04 · U1 · Architectural Components",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/05_unit1-quiz1.md",
    titel: "05 · U1 · Quiz 1 - MCP Fundamentals",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/06_unit1-communication-protocol.md",
    titel: "06 · U1 · The Communication Protocol",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/07_unit1-capabilities.md",
    titel: "07 · U1 · Understanding MCP Capabilities",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/08_unit1-sdk.md",
    titel: "08 · U1 · MCP SDK",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/09_unit1-quiz2.md",
    titel: "09 · U1 · Quiz 2 - MCP SDK",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/10_unit1-mcp-clients.md",
    titel: "10 · U1 · MCP Clients",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/11_unit1-hf-mcp-server.md",
    titel: "11 · U1 · Hugging Face MCP Server",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/12_unit1-gradio-mcp.md",
    titel: "12 · U1 · Gradio MCP Integration",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/13_unit1-unit1-recap.md",
    titel: "13 · U1 · Unit 1 Recap",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/14_unit1-certificate.md",
    titel: "14 · U1 · Get Your Certificate!",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/15_unit2-introduction.md",
    titel: "15 · U2 · Introduction to Building an MCP Application",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/16_unit2-gradio-server.md",
    titel: "16 · U2 · Building the Gradio MCP Server",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/17_unit2-clients.md",
    titel: "17 · U2 · Using MCP Clients with Your Application",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/18_unit2-continue-client.md",
    titel: "18 · U2 · Using MCP in Your AI Coding Assistant",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/19_unit2-gradio-client.md",
    titel: "19 · U2 · Building an MCP Client with Gradio",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/20_unit2-tiny-agents.md",
    titel: "20 · U2 · Building Tiny Agents with MCP and the Hugging Face Hub",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/21_unit2-lemonade-server.md",
    titel: "21 · U2 · Local Tiny Agents with AMD NPU and iGPU Acceleration",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/22_unit3-introduction.md",
    titel: "22 · U3 · Building Custom Workflow Servers for Claude Code",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/23_unit3-build-mcp-server.md",
    titel: "23 · U3 · Module 1: Build MCP Server",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/24_unit3-github-actions-integration.md",
    titel: "24 · U3 · Module 2: GitHub Actions Integration",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/25_unit3-slack-notification.md",
    titel: "25 · U3 · Module 3: Slack Notification",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/26_unit3-build-mcp-server-solution-walkthrough.md",
    titel: "26 · U3 · Unit 3 Solution Walkthrough: Building a Pull Request Agent with MCP",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/27_unit3-certificate.md",
    titel: "27 · U3 · Get Your Certificate!",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/28_unit3-conclusion.md",
    titel: "28 · U3 · Unit 3 Conclusion",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/29_unit3_1-introduction.md",
    titel: "29 · U3.1 · Build a Pull Request Agent on the Hugging Face Hub",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/30_unit3_1-setting-up-the-project.md",
    titel: "30 · U3.1 · Setting Up the Project",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/31_unit3_1-creating-the-mcp-server.md",
    titel: "31 · U3.1 · Creating the MCP Server",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/32_unit3_1-quiz1.md",
    titel: "32 · U3.1 · Quiz 1 - MCP Server Implementation",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/33_unit3_1-mcp-client.md",
    titel: "33 · U3.1 · MCP Client",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/34_unit3_1-webhook-listener.md",
    titel: "34 · U3.1 · Webhook Listener",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/35_unit3_1-quiz2.md",
    titel: "35 · U3.1 · Quiz 2 - Pull Request Agent Integration",
    bereich: "mcp-course" },

  { datei: "../AI_Course/mcp-course/viewer/36_unit3_1-conclusion.md",
    titel: "36 · U3.1 · Conclusion",
    bereich: "mcp-course" },
  /* <<< MCP-COURSE-ENDE */

];
