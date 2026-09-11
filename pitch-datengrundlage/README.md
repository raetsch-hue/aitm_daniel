# pitch-datengrundlage

**Kein Bestandteil von `GeAT-unternehmensprofil/`.** Dieses Verzeichnis enthält die Methode und die Datengrundlage zum C-Level-Pitch — beides so aufbereitet, dass Dritte damit arbeiten können.

| Datei | Was drin ist |
|---|---|
| [`skill-c-level-pitch.md`](skill-c-level-pitch.md) | **Die Methode** — kein installierter Skill, sondern eine Anleitung zum Lesen und Anwenden. Beginnt mit **Schritt 0: drei Dinge, die erfragt und nicht geraten werden** (welche sechs Gruppen, woher die Plattformen, wie Lücken überbrückt werden). Dann zwölf Pflichtwerte, Zuschnitt unter die Freigabegrenze, Kriterien herleiten, gewichten, Sensitivität, verbindliches Ausgabeformat, 14 Folien, Sprechunterlagen, Datenblatt |
| [`vorlage-praesentation.html`](vorlage-praesentation.html) | **Die leere Präsentation.** Dieselbe Gestaltung und Steuerung, 14 Folien mit Platzhaltern, jede mit ihrer Aufgabe im Kommentar |
| [`GeAT-datengrundlage-plattformfreigabe.md`](GeAT-datengrundlage-plattformfreigabe.md) | **Das durchgerechnete Beispiel.** Alle Werte, die in die GeAT-Präsentation eingegangen sind, mit Herkunftskennzeichen und Folien-Zuordnung |

## Anwendung

Jemand übergibt ein Unternehmensprofil als Markdown-Datei. Ergebnis sind vier Dateien: Präsentation, Sprechzettel, Volltext, Datenblatt.

```
skill-c-level-pitch.md  +  fremdes-firmenprofil.md   →   vier Dateien
```

Die Methode liegt bewusst **hier** und nicht unter `.claude/skills/` — sie ist kein aufrufbarer Skill. Wer ihn in Claude Code aufrufbar machen will, kopiert ihn als `SKILL.md` nach `.claude/skills/c-level-pitch/` — das Frontmatter ist bereits dafür gebaut.

## Vorbehalt

Die Zahlen im Beispiel stammen aus einem konstruierten Fall. Das Unternehmen existiert, die Hülle ist belegt, der Kern ist abgeleitet. **Die Struktur der Rechnung ist übertragbar, die absoluten Werte sind es nicht.** Der vollständige Vorbehalt steht im Kopf des Datenblatts.
