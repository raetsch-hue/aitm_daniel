---
ordner: GeAT-unternehmensprofil
firma: GeAT – Gesellschaft für Arbeitnehmerüberlassung Thüringen mbH, Erfurt
typ: real (Hülle belegt, Kern konstruiert)
stand: 2026-09-02
verwendung: Übungsfall für alle Methoden bis Kurswoche 12
---

# Unternehmensprofil GeAT mbH

Der durchgehende Fall für alle Methoden des Kurses bis Woche 12: Change Management, Stakeholder-Analyse, Plattformwahl, Governance, Business Case, Datenstrategie, Skalierung, Programm-Management. Gebaut nach dem Feldkatalog `unternehmensprofil.md` aus dem geteilten Kursprojekt „Werkbank: Unternehmensprofile".

## Der Hinweis, der vor allem anderen kommt

> **GeAT existiert.** Firma, Sitz, Gründungsjahr, Leistungen, Zertifikate und die Aufsichtsbehörde sind belegt und stehen mit Quelle und Abrufdatum in [`recherche.md`](recherche.md).
>
> **Alles andere ist konstruiert.** Umsatz, Ergebnis, Prozesskosten, Datenqualität, Systemlandschaft, Vorgeschichte, Kultur — dazu ist nichts öffentlich, und ein Modell erfindet es überzeugend. Jeder Wert trägt deshalb ein Kennzeichen: `öffentlich`, `angenommen` oder `generiert`.
>
> **Alle Personen sind erfunden.** Die Geschäftsführung der GeAT ist im Impressum und im Handelsregister öffentlich benannt. Dieser Name kommt in diesem Profil nicht vor, und das ist Absicht.
>
> **Nichts aus diesem Ordner gehört in ein Artefakt über eine reale Organisation.** Weder eine Zahl noch ein Zitat noch eine Einschätzung.

## Warum GeAT

Der Kernprozess des Unternehmens **ist** der KI-Fall. Bei einem Maschinenbauer hängt man KI an einen Prozess an; bei einem Personaldienstleister ist die Auswahl von Menschen für Stellen das Geschäft selbst. Daraus folgen drei Dinge, die kein anderer Fall in dieser Schärfe liefert:

1. **EU AI Act Annex III, Nummer 4 — Hochrisiko, nicht Randzone.** Bewerbersuche, Filterung und Bewertung sind ausdrücklich gelistet. Der Fall lässt sich nicht mit „ein Mensch klickt ja" auflösen, und genau daran lernt man, was wirksame menschliche Aufsicht heißt.
2. **Bias mit Zahlen statt mit Beispielen.** 28,8 Prozent der Zeitarbeitnehmer in Deutschland haben keinen Berufsabschluss, 20,4 Prozent waren zuvor langzeitarbeitslos oder noch nie beschäftigt, und Zeitarbeit trägt 10,8 Prozent der Übergänge aus Langzeitarbeitslosigkeit in Beschäftigung — alles belegt (GVP 2025). Ein auf Erfolgswahrscheinlichkeit trainiertes Modell sortiert genau diese Gruppen zuerst aus. Das ist keine Übungsaufgabe, das ist eine Rechnung.
3. **Die Aufsichtsbehörde ist die Bundesagentur für Arbeit** (belegt, Impressum). Sie erteilt die Erlaubnis, von der das Geschäftsmodell abhängt, und ist im Vermittlungsmarkt selbst Akteur. Für einen Digital Transformation Manager in der öffentlichen Arbeitsverwaltung ist das der Fall von der anderen Seite des Tisches.

Dazu passt der Reifegrad: Die Branche liegt bei 46 Prozent regelmäßiger KI-Nutzung (Lünendonk 2025, belegt). Ein Personaldienstleister mit Daten auf Stufe 2 ist deshalb glaubwürdig — anders als eine E-Commerce-Firma, bei der ein niedriger Reifegrad die ganze Engpass-Pointe zerstören würde.

## Die Dateien

| Datei | Enthält | Braucht ab |
|---|---|---|
| [`recherche.md`](recherche.md) | Was öffentlich belegbar ist, mit Quelle und Abrufdatum. Branchenbenchmarks. Offene Fragen | immer |
| [`profil.md`](profil.md) | Identität, Geschäftsmodell, fünf Kernprozesse, Reifegrad mit prüfbarem Nachweis, Wellen-Diagnose, drei brennende Probleme, Vorgeschichte, Marktumfeld, Regulatorik, Reibungsliste | W1, W3, W5 |
| [`zahlen.md`](zahlen.md) | GuV-Skelett, Rohertrag je Überlassungsstunde, Personalkosten je Bereich, IT-Budget, Pilotprozess mit Zerlegung der Durchlaufzeit, Investitionsspielraum, Rechenproben | W6, W7 |
| [`menschen.md`](menschen.md) | Sechs Gremien, 14 Rollen mit Macht, Interesse, Haltung und Zitat, sechs Segmente, fünf Kulturmerkmale mit Beleg | W2, W4, W12 |
| [`systeme-daten.md`](systeme-daten.md) | Systemlandschaft, Datenbestände mit Qualitätsbefund, Wissensquellen, Schatten-IT, Auftragsverarbeiter | W3, W5, W8 |
| [`vorhaben.md`](vorhaben.md) | Der Pilot, Workflows heute und im Ziel, Risikoeinschätzung nach EU AI Act, parallele Initiativen, Eskalationsweg | W2, W6, W9, W11 |
| [`ereignisse.md`](ereignisse.md) | Was sich im Kursverlauf geändert hat, je Zeile eine Woche | laufend |
| [`generierte-werte.md`](generierte-werte.md) | Alle 17 `generiert`-Werte, sortiert nach der Woche, die sie zuerst braucht — plus die `angenommen`-Werte, die trotzdem geprüft werden müssen | jeden Freitag |

Zwei Referenzen liegen absichtlich **nicht** in diesem Ordner, weil sie zum Kurs gehören und nicht zum Fall: der **Feldkatalog** (`unternehmensprofil.md`) und das **Musterprofil** der fiktiven Mustermann Antriebstechnik GmbH. Beide stehen im geteilten Projekt „Werkbank: Unternehmensprofile". Der Feldkatalog liegt zusätzlich im Projektwissen dieses Falls, damit ein Modell die Feldstruktur ohne Umweg kennt.

**Nie den ganzen Ordner in einen Prompt geben.** Der Feldkatalog verteilt das Profil auf sechs Dateien, damit ein Modell nur die liest, die es braucht. Für eine Stakeholder-Analyse reichen `profil.md` und `menschen.md`; für den Business Case `zahlen.md` und `vorhaben.md`.

## Die Reibung, die eingebaut ist

Ein Profil ohne Widersprüche liefert bei jeder Methode glatte Ergebnisse. Sechs Pflichtreibungen nach Feldkatalog, plus zwei an unüblicher Stelle:

| Reibung | Wo |
|---|---|
| Zwei Rollen mit unvereinbaren Zielen: Recruiting Center gegen Niederlassungsleitung Nordhausen | `menschen.md`, Rollen 4 und 5 |
| Gescheiterte Vorgängerinitiative: Bewerbermanagement-Modul 2023, 34 Prozent Nutzung, nie ausgewertet | `profil.md`, Vorgeschichte |
| System ohne Schnittstelle: Multiposting ↔ Bewerbermanagement, jede Anzeige zweimal gepflegt | `systeme-daten.md` |
| Datenbestand mit Mangel: 41.000 Profile, 63 Prozent ohne strukturiertes Können, 18.000 über die Speicherfrist | `systeme-daten.md` |
| Parallele Initiative um dieselben Leute: Migration der Branchensoftware 2027 | `vorhaben.md` |
| Zahl, die wehtut: 280.000 Euro Spielraum, Freigaben über 25.000 nur quartalsweise | `zahlen.md` |
| **Unüblich:** der Engpass der Fakturierung ist der Papier-Stundenzettel, und die Person, die ihn beherrscht, kommt im Vorhaben nicht vor | `menschen.md` Rolle 11, `systeme-daten.md` |
| **Unüblich:** das Anzeigenbudget von 480.000 Euro ist größer als das gesamte IT-Budget — und liegt im Vertrieb | `zahlen.md` |

## Woher die Bauweise kommt

Die Struktur folgt dem Feldkatalog des Kurses. Drei Elemente sind aus der Trainingsfirma in [`../training-company/`](../training-company/) (Hellwig Fördertechnik) übernommen, weil sie dort besser gelöst sind als in der Vorlage:

- **Prüfbarer Nachweis je Reifegradstufe.** Nicht „Daten: 2", sondern der einzelne Befund, den man bestreiten kann.
- **Wellen-Diagnose** als eigener Abschnitt in `profil.md`, mit einem Satz, der die Diagnose zusammenfasst.
- **Die Zerlegung der Durchlaufzeit** in `zahlen.md`. Bei Hellwig stehen 47 Minuten Arbeit gegen 6,5 Tage Durchlauf; bei GeAT 3,4 Stunden gegen 11 Tage. Beide Male ist die Rechnung der Lehrpunkt — mit dem Unterschied, dass bei GeAT genau ein Wartezeitblock durch bessere Vorschläge kürzer wird. Das macht den Fall entscheidbar statt entlarvend.

Was **nicht** übernommen wurde: Hellwigs Didaktikteil (Ausbaustufen, Injects, Dozentenhinweise). Dieses Profil ist ein Übungsfall für eine Person, kein Kursmaterial für einen Raum.

## Nächste Schritte

1. Die vier offenen Fragen aus `recherche.md` abarbeiten, mit Priorität auf der Branchensoftware.
2. Die 17 `generiert`-Werte durchgehen. Wert 4 (Eigentümerstruktur) zuerst — er hängt an Wert im Frontmatter und verändert den Tonfall des ganzen Falls.
3. Stufe 3 des Feldkatalogs: die erste Methode gegen das Profil laufen lassen und die Lücken nachtragen.
