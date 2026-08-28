---
projekt: AITM 08/2026 DR
zweck: Projektanweisung für die Arbeit in diesem Repository
---

# Projektanweisung

Diese Datei steuert, **wie** in diesem Repository gearbeitet wird. Sie verweist auf den Kontext, sie wiederholt ihn nicht. Wenn eine Information schon in `kontext/` steht, wird hier nur darauf verlinkt.

## Kontext zuerst lesen

| Datei | Enthält | Wann heranziehen |
|---|---|---|
| [`kontext/person.md`](kontext/person.md) | Rolle, Sprache, Tonalität, Arbeitsprinzipien | immer |
| [`kontext/organisation.md`](kontext/organisation.md) | Organisationsprofil und digitaler Reifegrad | bei Einordnung und Begründung |
| [`kontext/vorhaben.md`](kontext/vorhaben.md) | RPA-Pilot: Ziel, Messgrößen, offene Punkte, Risiken | bei allem zum Pilot |
| [`kontext/stakeholder.md`](kontext/stakeholder.md) | Rollen, Interessen, Einbindung | bei Adressatenzuschnitt |

## Arbeitsweise

- Sprache und Tonalität richten sich nach `kontext/person.md`. Nicht hier duplizieren.
- **Fakten, Annahmen und Gruppeneinschätzungen immer getrennt ausweisen** und als solche kennzeichnen.
- Keine Zahlen erfinden. Fehlende Werte als Lücke benennen, nicht schätzen und dann wie belegt darstellen.
- Gegenargumente und Risiken gehören in jedes Ergebnis, nicht in einen Anhang.
- Der Reifegrad in `kontext/organisation.md` ist eine unvalidierte Gruppeneinschätzung. Jede Aussage, die darauf aufbaut, trägt diesen Vorbehalt mit.

## Ablage

| Was | Wohin |
|---|---|
| Wiederverwendbar, ändert sich selten | `kontext/` |
| Vorlage mit Beispiel und Prüfkriterien | `vorlagen/` |
| Datiertes Ergebnis, je Kurswoche | `artefakte/woche-NN/` |
| Nachweisbare Fähigkeiten | `kompetenzen.md` |

Jedes Artefakt trägt im Frontmatter `datum`, `woche` und `status`. Ein Ergebnis, das mehrfach gebraucht wird, wandert als Vorlage nach `vorlagen/` — mit Beispiel und Prüfkriterien, sonst ist es keine Vorlage.

## Was hier nicht passiert

- Kontext nicht in Ergebnisdokumente kopieren, sondern verlinken.
- Vorlagen nicht überschreiben, wenn ein konkreter Anwendungsfall entsteht — Vorlage bleibt, Ergebnis geht nach `artefakte/`.
- Keine personenbezogenen Namen; Stakeholder werden als Rollen geführt (siehe `kontext/stakeholder.md`).
