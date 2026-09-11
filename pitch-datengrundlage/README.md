# pitch-datengrundlage

**Kein Bestandteil von `GeAT-unternehmensprofil/`.** Dieses Verzeichnis enthält die Methode und die Datengrundlage zum C-Level-Pitch — beides so aufbereitet, dass Dritte damit arbeiten können.

| Datei | Was drin ist |
|---|---|
| [`skill-c-level-pitch.md`](skill-c-level-pitch.md) | **Die Methode** — kein installierter Skill, sondern eine Anleitung zum Lesen und Anwenden. Beginnt mit einem **Fragenkatalog: zwölf Fragen als Auswahl oder freie Antwort**, mit Voreinstellung bei Verfahrensfragen und ohne bei Sachfragen. Vier davon haben bewusst keine Voreinstellung — dort hält die Arbeit an, statt zu raten. Dann zwölf Pflichtwerte, Zuschnitt unter die Freigabegrenze, Kriterien herleiten, gewichten, Sensitivität, verbindliches Ausgabeformat, 14 Folien, Sprechunterlagen, Datenblatt |
| [`vorlage-praesentation.html`](vorlage-praesentation.html) | **Die leere Präsentation.** Dieselbe Gestaltung und Steuerung, 14 Folien mit Platzhaltern, jede mit ihrer Aufgabe im Kommentar |
| [`GeAT-datengrundlage-plattformfreigabe.md`](GeAT-datengrundlage-plattformfreigabe.md) | **Das durchgerechnete Beispiel.** Alle Werte, die in die GeAT-Präsentation eingegangen sind, mit Herkunftskennzeichen und Folien-Zuordnung |
| [`GeAT-kurzuebersicht.md`](GeAT-kurzuebersicht.md) | **Gefühl für die Firma in fünf Minuten.** Nur aus dem Datenblatt abgeleitet; zwölf fehlende Themen ausdrücklich markiert |
| [`GeAT-datenpruefung-verwendeter-umfang.md`](GeAT-datenpruefung-verwendeter-umfang.md) | **Die Datenqualitätsprüfung, im verwendeten Umfang.** Eine Messung ging in die Entscheidung ein; was gemessen, aber nicht verwendet wurde, steht getrennt dabei |

## Anwendung

Jemand übergibt ein Unternehmensprofil als Markdown-Datei. Ergebnis sind vier Dateien: Präsentation, Sprechzettel, Volltext, Datenblatt.

```
skill-c-level-pitch.md  +  fremdes-firmenprofil.md
        │
        └─►  pitch-datengrundlage/<Firma>/
                 <Firma>-pitch-praesentation.html
                 <Firma>-pitch-sprechzettel.md
                 <Firma>-pitch-sprechfassung-volltext.md
                 <Firma>-datengrundlage-<vorhaben>.md
```

Alle vier tragen den **Präfix der Firma**, für die sie gebaut wurden, und liegen in einem eigenen Unterverzeichnis. Nichts davon wird im fremden Unternehmensprofil abgelegt: es sind Ergebnisse, keine Quellen.

Das durchgerechnete Beispiel folgt dieser Benennung noch nicht vollständig — es ist vor der Festlegung entstanden. `GeAT-datengrundlage-plattformfreigabe.md` trägt den Präfix, die drei GeAT-Sprechunterlagen liegen weiterhin unter `GeAT-unternehmensprofil/` mit ihrem Ketten-Präfix `w03A-6-`.

Die Methode liegt bewusst **hier** und nicht unter `.claude/skills/` — sie ist kein aufrufbarer Skill. Wer ihn in Claude Code aufrufbar machen will, kopiert ihn als `SKILL.md` nach `.claude/skills/c-level-pitch/` — das Frontmatter ist bereits dafür gebaut.

## Vorbehalt

Die Zahlen im Beispiel stammen aus einem konstruierten Fall. Das Unternehmen existiert, die Hülle ist belegt, der Kern ist abgeleitet. **Die Struktur der Rechnung ist übertragbar, die absoluten Werte sind es nicht.** Der vollständige Vorbehalt steht im Kopf des Datenblatts.
