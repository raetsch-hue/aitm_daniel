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

  // ---- Kurzfassungen ----
  { datei: "essentials/2.3_Essentials-Kraefte-sichtbar-machen.md",
    titel: "2.3 · Essentials: Kräfte sichtbar machen" },

  { datei: "essentials/2.4_Essentials-Widerstand.md",
    titel: "2.4 · Essentials: Widerstand ist eine Information" },

  { datei: "essentials/2.5_Essentials-Die-Woche-wird-ein-Plan.md",
    titel: "2.5 · Essentials: Die Woche wird ein Plan" },

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

  /* ================= BEISPIELE ================= */

  { datei: "../examples/fallbeispiele.md",
    titel: "Fallbeispiele im Kurs (Übersicht)",
    bereich: "examples" },

  /* ================= LERNTAGEBUCH ================= */

  { datei: "../lerntagebuch/lerntagebuch.md",
    titel: "Lerntagebuch (Stand 2.2)",
    bereich: "lerntagebuch" },

];
