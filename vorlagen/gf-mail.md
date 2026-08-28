---
vorlage: Executive-Mail an die Geschäftsführung
zweck: Entscheidungsvorlage per Mail, maximal 180 Wörter
grundlage: kontext/organisation.md, kontext/vorhaben.md
---

# Vorlage: GF-Mail

Prompt für die Executive-Mail an die Geschäftsführung. Grundlage ist der Kontext in diesem Repository, nicht eine externe Datei.

## Prompt

```text
Du bist Digital Transformation Manager der Bundesagentur für Arbeit. Verfasse eine E-Mail an die zehnköpfige Geschäftsführung zur Vorbereitung des nächsten Geschäftsführungs-Meetings.

Grundlage ist die Reifegradanalyse in „kontext/organisation.md" sowie die Vorhabenbeschreibung in „kontext/vorhaben.md". Berichte über die wichtigste daraus abgeleitete Maßnahme: Der vorgeschlagene RPA-Pilot für standardisierte Änderungsmitteilungen sollte noch nicht freigegeben werden. Vorher ist eine belastbare Entscheidungsvorlage zu erstellen.

Schreibe im Executive Style:
- Formuliere die Kernaussage bereits im ersten Satz.
- Begründe sie anschließend in genau drei kurzen Absätzen:
  1. Die Reifegradbewertung beruht nur auf einer Gruppeneinschätzung und ist nicht ausreichend belegt.
  2. Für den RPA-Piloten fehlt ein vollständiger Business Case mit Fallzahlen, Einsparungen, Kosten und Amortisationszeit.
  3. RPA muss mit einer direkten Schnittstelle und einer Weiterentwicklung des Fachverfahrens verglichen werden.
- Schließe mit einer klaren Entscheidungsempfehlung und benenne, welche Unterlagen für die Freigabe benötigt werden.
- Formuliere kritisch, aber konstruktiv und lösungsorientiert.
- Verwende eine passende Betreffzeile und eine professionelle Anrede.
- Maximal 180 Wörter, sachlich, verständlich, keine Superlative und keine erfundenen Fakten.

Gib ausschließlich die fertige E-Mail aus.
```

## Prüfkriterien

- [ ] Kernaussage steht im ersten Satz, nicht erst im Schluss.
- [ ] Genau drei Begründungsabsätze, in der vorgegebenen Reihenfolge.
- [ ] Höchstens 180 Wörter (Betreff und Grußformel mitgezählt).
- [ ] Keine Zahl, die nicht aus `kontext/` stammt.
- [ ] Gruppeneinschätzung ist als solche benannt, nicht als Befund dargestellt.
- [ ] Die benötigten Unterlagen sind konkret aufgezählt.
- [ ] Ton kritisch, aber lösungsorientiert — keine Superlative.

## Ergebnis

Die erzeugte Mail ist ein Artefakt, keine Vorlage: ablegen unter `artefakte/woche-NN/`. Diese Datei bleibt unverändert.
