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
   ------------------------------------------------------------------ */

var DOKUMENTE = [

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

];
