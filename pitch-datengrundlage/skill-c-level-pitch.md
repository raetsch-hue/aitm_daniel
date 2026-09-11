---
name: c-level-pitch
description: Aus einem Unternehmensprofil eine C-Level-Pitch-Präsentation herleiten — Kriterien, Gewichtung, 14 Folien, Sprechunterlagen und Datenblatt. Für Beschaffungs- und Freigabeentscheidungen vor einem Gremium, das haftet.
typ: SKILL · Methodenbeschreibung, kein Bestandteil eines Unternehmensprofils
ablage: pitch-datengrundlage/ — bewusst nicht unter .claude/skills/. Wer ihn aufrufbar machen will, kopiert ihn als SKILL.md dorthin
datum: 2026-09-11
eingabe: eine Firmen-md beliebiger Struktur
ausgabe: vier Dateien mit Firmen-Präfix in pitch-datengrundlage/<Firma>/ — Präsentation (HTML), Sprechzettel, Volltext, Datenblatt
beispiel: pitch-datengrundlage/GeAT-datengrundlage-plattformfreigabe.md (durchgerechnet)
vorlage: pitch-datengrundlage/vorlage-praesentation.html
baut_auf: vorlagen/pitch-c-level.md (die zehn Prüfkriterien) · coursebook/3.4 (Vier-Abschnitts-Format)
---

# Skill: Vom Unternehmensprofil zum C-Level-Pitch

> **Was diese Methode leistet.** Jemand übergibt ein Unternehmensprofil als Markdown-Datei — beliebig aufgebaut, aus einem anderen Kurs, einer anderen Branche, einer anderen Größe. Ergebnis sind **vier Dateien mit dem Präfix dieser Firma**: eine Präsentation, ein Sprechzettel, eine Volltextfassung und ein Datenblatt. Was sie genau enthalten und wie sie heißen, steht im nächsten Abschnitt.
>
> **Was er nicht kann.** Er erfindet keine Zahlen. Fehlt ein Pflichtwert, wird er als Lücke ausgewiesen — im Ergebnis, nicht im Nebensatz. Eine Präsentation mit sichtbaren Lücken ist brauchbar; eine mit erfundenen Zahlen ist es nicht.
>
> **Zum Status.** Dies ist eine **Methodenbeschreibung**, kein installierter Skill. Sie liegt bewusst unter `pitch-datengrundlage/` und nicht unter `.claude/skills/` — sie wird gelesen und angewendet, nicht aufgerufen.
>
> **Und die Grundregel, die über allem steht: Was nicht im Datensatz steht, wird erfragt — nicht geraten.** Schritt 0 nennt die drei Punkte, die immer zu fragen sind; darüber hinaus gilt sie für jede Unklarheit.

> **Die Grundannahme.** Der Adressat ist eine **Freigabeinstanz, die haftet** — keine Peer-Gruppe. Daraus folgt alles Weitere: Beschluss nach vorn, Gegenargumente selbst nennen, offene Punkte als Bedingungen.

---

## Was am Ende entsteht — und wie es heißt

**Vier Dateien**, und sie tragen alle den **Präfix der Firma**, für die sie gebaut wurden. Der Präfix ist der Kurzname, wie die Firma sich selbst schreibt — `GeAT`, `Hellwig`, `Brehmer`.

| # | Datei | Was drin ist |
|---|---|---|
| 1 | `<Firma>-pitch-praesentation.html` | 14 Folien nach [`vorlage-praesentation.html`](vorlage-praesentation.html), Sprechernotiz je Folie |
| 2 | `<Firma>-pitch-sprechzettel.md` | Stichpunkte je Folie mit Zeitbudget, die Sätze die fallen müssen, vorbereitete Antworten, Notfallpfad |
| 3 | `<Firma>-pitch-sprechfassung-volltext.md` | Wort für Wort, mit Folienmarken, Pausen, Zeitmarken, Regieanweisungen |
| 4 | `<Firma>-datengrundlage-<vorhaben>.md` | alle verwendeten Werte mit Herkunftskennzeichen, Status quo, Roadmap, Bewertungsmatrix mit Begründungen, Folien-Zuordnung, „Was nicht belegt ist" |

**Ablage:** ein eigenes Unterverzeichnis je Firma, `pitch-datengrundlage/<Firma>/`. Der Präfix bleibt trotzdem am Dateinamen — die Dateien werden einzeln weitergegeben, und dann trägt nur der Name noch die Zuordnung.

> **Nichts in einem fremden Unternehmensprofil ablegen.** Die vier Dateien sind Ergebnisse, keine Quellen. Wer sie in das übergebene Profil legt, vermischt Bestand und Ableitung — und beim nächsten Stand weiß niemand mehr, was gepflegt wird und was einmal erzeugt wurde.

**Wohin die sechs Pflichtbestandteile aus dem [Ausgabeformat](#das-ausgabeformat-verbindlich) gehören:**

| Bestandteil | Datei |
|---|---|
| Bewertungstabelle, Gewichte auf Summe 100, gewichtetes Ergebnis | **Datenblatt**, verdichtet auf Folie 7 |
| Je Gewicht eine Begründungszeile | **Datenblatt** |
| Markierte Lücken mit dem gewählten Weg aus [0.3](#03-wie-eine-lücke-überbrückt-wird) | **Datenblatt**, dazu Folie 10 |
| Empfehlung in drei bis fünf Sätzen, zwei Gegenargumente | **Folien 6, 8, 9** und Volltext |
| Abschnitt „Offene Fragen" | **Folie 10** und Datenblatt |
| Die ersten 90 Tage mit Abbruchkriterium | **Folien 5, 10, 13** und Datenblatt |

> **Wenn der Auftrag kleiner ist**, etwa nur eine Bewertungstabelle ohne Vortrag: Datei 4 allein genügt. Sie enthält alle sechs Bestandteile. Die Folien sind die Darstellung, das Datenblatt ist die Substanz.

---

## Der Fragenkatalog — alles, was erfragt wird

**Zwölf Fragen. Sie stehen hier vollständig, damit keine vergessen wird.** Die ersten sieben werden **vor** dem Start gestellt, die restlichen fünf entstehen unterwegs.

**Zur Spalte „ohne Antwort":** Bei **Verfahrensfragen** gibt es eine Voreinstellung — die Arbeit soll nicht an einer Formsache stehenbleiben. Bei **Sachfragen** gibt es keine. *Was nicht im Datensatz steht und nicht beantwortet wird, wird nicht gesetzt, sondern als Lücke ausgewiesen — oder die Arbeit hält an.*

### A · Vor dem Start: Auftrag und Ergebnis

| # | Frage | Auswahl | Ohne Antwort |
|---:|---|---|---|
| 1 | **Welche sechs Gruppen sind gemeint?** Ausführlich in [0.1](#01-welche-sechs-gruppen-sind-gemeint) | ☐ nur **Reifegrad-Dimensionen** (Strategie · Technologie · Daten · Kultur · Prozesse · People) ☐ nur **Plattform-Kriterien** (DSGVO/AI Act · Deployment · RAG · MCP · Preis/Lock-in · Adoption) ☐ **beide** | Voreinstellung: **beide** — der vollständige Weg, wird im Ergebnis vermerkt |
| 2 | **Welcher Ergebnisumfang?** | ☐ **ganzes Paket** (4 Dateien) ☐ Präsentation + Sprechzettel ☐ nur Präsentation ☐ **nur Datenblatt** | Voreinstellung: **ganzes Paket** |
| 3 | **Firmenkurzname für den Präfix?** — wie die Firma sich selbst schreibt | *freie Antwort* | Voreinstellung: der Name aus dem Frontmatter des Profils |
| 4 | **Wie heißt das Vorhaben?** — für den Dateinamen des Datenblatts | *freie Antwort* | Voreinstellung: aus dem Beschlussgegenstand abgeleitet |

### B · Vor dem Start: der Gegenstand

| # | Frage | Auswahl | Ohne Antwort |
|---:|---|---|---|
| 5 | **Woher kommen die Plattformen?** Ausführlich in [0.2](#02-woher-kommen-die-plattformen) | ☐ **vorgegeben** — welche? ☐ **Recherche** — gibt es gesetzte oder ausgeschlossene Kandidaten? | **keine Voreinstellung.** Ohne Antwort wird nicht bewertet |
| 6 | **Was ist der Beschlussgegenstand, und welcher Betrag?** Pflichtwert 1 | *freie Antwort* | **keine.** Ohne diese Angabe gibt es keinen Pitch — [Schritt 1](#schritt-1--datenaufnahme--die-zwölf-pflichtwerte) |
| 7 | **Wer entscheidet — welches Gremium, welche Freigabegrenze, welcher Tagungsrhythmus?** Pflichtwert 2 | *freie Antwort* | **keine.** Davon hängt der Zuschnitt ab — [Schritt 2](#schritt-2--der-zuschnitt--der-schritt-den-alle-überspringen) |

### C · Wenn Pflichtwerte fehlen

| # | Frage | Auswahl | Ohne Antwort |
|---:|---|---|---|
| 8 | **Der Anlass ist im Profil nicht erkennbar** — was ist das Problem, seit wann, woran messbar? Pflichtwert 4 | *freie Antwort* | **keine.** Arbeit hält an |
| 9 | **Es gibt keine Vorgängerinitiative mit Zahl** — gab es ein früheres Vorhaben, das gescheitert oder gelungen ist? Pflichtwert 7 | ☐ ja, welches ☐ nein, es gibt keine | Wird als Lücke ausgewiesen. **Der Pitch verliert seinen stärksten Teil** und wird deutlich schwächer |
| 10 | **Ein Kriterium hat im Datensatz keinen Beleg** — welcher der drei Wege? Ausführlich in [0.3](#03-wie-eine-lücke-überbrückt-wird) | ☐ **Annahme** mit Kennzeichnung ☐ **Recherche** mit Quelle ☐ **offene Frage** mit Zuständigkeit und Frist | Voreinstellung: **offene Frage** — die ehrlichste der drei. Stillschweigend füllen ist nie zulässig |

### D · Unterwegs

| # | Frage | Auswahl | Ohne Antwort |
|---:|---|---|---|
| 11 | **Die beiden besten Gesamtscores liegen unter 0,3 auseinander** — das ist kein Ergebnis, sondern unentschieden. Welches Kriterium fehlt? | *freie Antwort* | Wird als **unentschieden** ausgewiesen, keine Empfehlung ausgesprochen — [Schritt 5](#schritt-5--scoring-sensitivität-kippschwelle) |
| 12 | **Das Vorhaben passt nicht unter die Freigabegrenze** — kleiner zuschneiden oder Gremiumsvorlage? | ☐ **kleiner zuschneiden** ☐ **Gremiumsvorlage** vorbereiten, mit Sitzungstermin | Voreinstellung: **kleiner zuschneiden**, solange der Zweck erhalten bleibt — [Schritt 2](#schritt-2--der-zuschnitt--der-schritt-den-alle-überspringen) |

> **Die Fragen 5 bis 8 haben bewusst keine Voreinstellung.** Es sind die vier, bei denen eine gesetzte Antwort das Ergebnis unbrauchbar macht statt nur ungenau. Wer sie überspringt, baut eine Präsentation über eine Entscheidung, die niemand getroffen hat.

---

## Schritt 0 · Die drei Fragen im Detail

**Diese Methode rät nicht. Sie fragt.** Der vollständige Katalog steht oben; hier sind die drei Fragen erläutert, bei denen die Antwort allein nicht genügt — man muss wissen, was aus ihr folgt.

### 0.1 Welche sechs Gruppen sind gemeint?

In den Kursunterlagen gibt es **zwei verschiedene Sechsergruppen**. Sie werden regelmäßig verwechselt, und die Verwechslung kostet die halbe Bewertung:

| | Gruppe | Die sechs |
|---|---|---|
| **1** | **Reifegrad-Dimensionen** | Strategie · Technologie · Daten · Kultur · Prozesse · People |
| **2** | **Plattform-Kriterien aus Tag 3.1** | DSGVO/AI Act · Deployment · RAG · MCP · Preis/Lock-in · Adoption |

Die erste beschreibt, **wo die Organisation steht**. Die zweite, **woran die Kandidaten gemessen werden**. Das eine ist die Begründung, das andere die Bewertung.

> **Frage stellen, bevor irgendetwas gebaut wird:**
> *„Sollen die sechs **Reifegrad-Dimensionen** durchgespielt werden (1), die sechs **Plattform-Kriterien** (2) — oder **beide**?"*

| Antwort | Was daraus folgt |
|---|---|
| **nur 1** | Das Ergebnis ist eine **Standortbestimmung**. Die Bewertungsmatrix baut darauf auf, ersetzt sie aber nicht. Jede Dimension bekommt eine Zeile, auch die ohne Datenlage |
| **nur 2** | Das Ergebnis ist eine **Bewertungsmatrix**. Die sechs Kriterien sind gesetzt und werden nur gewichtet, nicht hergeleitet — Schritt 3 entfällt weitgehend |
| **beide** | Der vollständige Weg: erst Standort, dann Bewertung. Die Reifegrad-Dimensionen **begründen** die Gewichte der Plattform-Kriterien. **Das ist der Weg des durchgerechneten Beispiels** |

**Wichtig bei Antwort 1 oder „beide":** Es werden **alle sechs Dimensionen durchgespielt, auch die ohne Datenlage.** Eine Dimension ohne Beleg wird nicht weggelassen, sondern markiert — siehe [0.3](#03-wie-eine-lücke-überbrückt-wird).

> **Und der Widerspruch, der dabei auffallen wird:** Schritt 3 dieser Methode sagt *„was nicht trennt, bekommt kein Gewicht"* und wirft Kriterien ohne begründenden Satz heraus. Anforderung 1 verlangt das Gegenteil: Vollständigkeit. **Beides ist richtig, für verschiedene Dinge.** Die Reifegrad-Dimensionen werden **vollständig** durchgespielt, weil sie eine Bestandsaufnahme sind. Die Bewertungskriterien werden **auf Trennschärfe geprüft**, weil sie eine Entscheidung tragen. Wer das vermischt, bekommt entweder eine lückenhafte Standortbestimmung oder eine aufgeblähte Matrix.

### 0.2 Woher kommen die Plattformen?

Auch das ist zu fragen und nicht zu setzen:

| Weg | Wann | Was zu tun ist |
|---|---|---|
| **Vorgabe** | Die zu vergleichenden Plattformen sind in der Aufgabe oder im Profil genannt | Übernehmen, unverändert. Auch dann die **Nullvariante ergänzen**, wenn sie fehlt |
| **Recherche** | Es gibt keine Vorgabe | Kandidaten selbst bestimmen — **je einer aus jeder Kategorie**, die für die Organisation in Frage kommt. **Jeder Kandidat mit Quelle**, und die Auswahl wird begründet: warum diese drei und nicht andere |

**Immer zu ergänzen, unabhängig vom Weg:** die **Nullvariante** und, falls vorhanden, **hausinterne Alternativen** — die Funktionen eines Systems, das ohnehin kommt. Beide stehen in keiner Marktübersicht und entscheiden trotzdem mit.

> **Frage stellen:** *„Sind die Plattformen vorgegeben — oder soll ich sie recherchieren?"* Bei Recherche zusätzlich: *„Gibt es Kandidaten, die gesetzt sind oder ausgeschlossen?"*

### 0.3 Wie eine Lücke überbrückt wird

Fehlt eine Angabe, gibt es **genau drei zulässige Wege** — und einen unzulässigen:

| Weg | Wie es aussieht |
|---|---|
| **Annahme mit Kennzeichnung** | Der Wert wird gesetzt, als `Annahme` markiert und begründet. Im Ergebnis erkennbar, nicht im Fließtext versteckt |
| **Recherche mit Quelle** | Der Wert wird beschafft und mit Fundstelle belegt |
| **Offene Frage mit Zuständigkeit** | Der Wert bleibt offen — mit **Name der Rolle**, die ihn beantworten kann, und **Frist** |

> **Stillschweigend füllen ist keiner der drei Wege.** Eine Zahl ohne Kennzeichen ist eine Behauptung, und sie fällt genau dann auf, wenn es teuer wird — im Gremium.

**Ein Kriterium ohne Beleg im Datensatz wird markiert, nicht weggelassen.** Die Markierung gehört in die Bewertungstabelle selbst, nicht in eine Fußnote.

---

## Schritt 1 · Datenaufnahme — die zwölf Pflichtwerte

Lies das übergebene Profil und trage diese zwölf Angaben zusammen. **Erfinde nichts.** Was fehlt, kommt in die Fehlliste am Ende dieses Schritts.

| # | Was gebraucht wird | Wofür im Pitch |
|---:|---|---|
| 1 | **Der Beschlussgegenstand und sein Betrag** | Folie 2 |
| 2 | **Freigabegrenzen, Gremien und ihr Tagungsrhythmus** | Folie 2 — bestimmt den Zuschnitt, siehe Schritt 2 |
| 3 | **Investitionsspielraum**, und ob im Haus eine andere Zahl umläuft | Folie 4 |
| 4 | **Der Anlass:** was ist das Problem, seit wann, woran erkennbar | Folie 3 |
| 5 | **Mengengerüst der Betroffenen:** Personen, Bestände, Standorte | Folien 3 und 4 |
| 6 | **Umsetzungskapazität und ihre Bindungen** (IT-Stellen, laufende Großvorhaben) | Folien 4 und 9 |
| 7 | **Eine Vorgängerinitiative mit Zahl** — bevorzugt eine gescheiterte | Folie 8. **Der wichtigste Einzelwert** |
| 8 | **Bestands- und Qualitätszahlen**, soweit ein Kriterium daran hängt | Folien 6 und 12 |
| 9 | **Die Optionen**, einschließlich Nullvariante und hausinterner Alternativen. Fehlen sie im Profil: [0.2](#02-woher-kommen-die-plattformen) | Folie 6 |
| 10 | **Regulatorische Lage** (Datenschutz, Branchenrecht, Mitbestimmung) | Folie 10 |
| 11 | **Wer im Raum sitzt und welche Kennzahl diese Person verlangt** | Folien 8 und 14 |
| 12 | **Was nicht bekannt ist** — ausdrücklich abgefragt | Folien 10 und 11 |

**Übernimm die Herkunftskennzeichen des Profils.** Hat es keine, führe sie selbst ein: `belegt` · `angenommen` · `gerechnet` · `unbekannt`. Ohne diese Trennung ist das spätere Datenblatt wertlos.

> **Fehlliste.** Fehlt Nr. 1, 2, 4 oder 9, brich ab und frage nach — ohne sie gibt es keinen Pitch. Fehlt Nr. 7, sag es deutlich: der Pitch verliert seinen stärksten Teil und wird deutlich schwächer. Alles andere lässt sich mit einer benannten Lücke bauen.

---

## Schritt 2 · Der Zuschnitt — der Schritt, den alle überspringen

**Bevor** irgendetwas bewertet wird: Finde die Grenze, unterhalb derer das anwesende Gremium **allein** entscheiden kann, und prüfe, ob das Vorhaben darunter passt.

Das ist keine Formalie. In dem durchgerechneten Beispiel entscheidet die Geschäftsführung wöchentlich bis 25.000 €, darüber die Gesellschafterversammlung — quartalsweise. Ein Vorhaben über der Grenze verliert bis zu drei Monate. Der Betrag wurde deshalb bewusst darunter zugeschnitten, und **genau das ist ein Argument, kein Zufall.**

| Lage | Konsequenz für den Pitch |
|---|---|
| Vorhaben passt unter die Grenze | Sag es auf Folie 2: *„Sie entscheiden allein."* Und sag, dass der Zuschnitt Absicht war |
| Vorhaben passt nicht darunter | Dann ist dies **nicht** der Pitch, sondern die Vorbereitung einer Gremiumsvorlage. Ändere das Ziel: nicht Freigabe, sondern Auftrag zur Vorlage — und nenne den Sitzungstermin |
| Es gibt keine Grenze / kein Gremium | Kläre, wer unterschreibt. Ohne Adressat ist jeder Pitch an die falsche Person gerichtet |

**Zweite Frage in diesem Schritt:** Hat die vortragende Rolle ein eigenes Budget? Wenn nein, gehört das in den ersten Satz — es erklärt, warum überhaupt jemand fragen muss.

---

## Schritt 3 · Kriterien herleiten, nicht übernehmen

**Übernimm keine Kriterienliste.** Die acht aus dem Beispiel gelten für dieses Unternehmen, nicht allgemein — „Verfügbarkeit gegen die Taktgrenze" existiert nur, weil dort ein Gremium quartalsweise tagt.

Drei Regeln:

**Regel 1 — Jedes Kriterium braucht einen Satz über *diese* Organisation.** Kein Satz, kein Kriterium. Der Satz muss aus dem Profil stammen, nicht aus der Technik. *„Compliance wiegt schwer, weil Datenschutz wichtig ist"* ist kein Satz — das sagt jeder. *„Compliance wiegt schwer, weil sie hier der Zweck der Beschaffung ist und nicht eine Zulassungsfrage für später"* ist einer.

**Regel 2 — Was nicht trennt, bekommt kein Gewicht.** Prüfe jedes Kriterium: Bewerten sich die Optionen darin unterschiedlich? Wenn alle gleich abschneiden, kostet es Gewicht und bewegt die Entscheidung nicht. Im Beispiel bekam „Deployment-Flexibilität" deshalb 2 %.

**Regel 3 — Ausschlusskriterien gehören *vor* die Matrix, nicht hinein.** „Rechtskonform: 4" ist unsinnig. Eine Bedingung ist erfüllt oder nicht. Ziehe sie heraus und nenne sie auf Folie 10 als Bedingung.

> **Prüffrage für die fertige Liste:** Kannst du jedes Gewicht auf einen Satz über die Organisation zurückführen? Geht das bei einem nicht, ist es entweder falsch gewichtet oder gar kein Kriterium.

**Wie das im Beispiel aussah** — zur Orientierung, nicht zur Übernahme:

| Kriterium | Gewicht | Der Satz, der es begründet |
|---|---:|---|
| Compliance und AVV | 25 % | Es ist der **Zweck** der Beschaffung, nicht eine Zulassungsfrage |
| Verfügbarkeit gegen die Taktgrenze | 20 % | Jeder Monat ohne zulässigen Ersatz ist ein weiterer Monat ohne Vertrag |
| Adoption und Einführungsaufwand | 17 % | Das letzte Werkzeug liegt bei 34 % Nutzung |
| Kosten über drei Jahre | 15 % | EBIT-Marge 2,6 %, Gesellschafter erwarten Ausschüttung |
| Betriebsaufwand | 11 % | 1,5 IT-Stellen, bis Q1/2027 gebunden |
| Exit und Portabilität | 6 % | Systemwechsel steht bevor |
| RAG und Integrationstiefe | 4 % | **63 % der Profile sind unstrukturiert — die Voraussetzung fehlt** |
| Deployment-Flexibilität | 2 % | Bei dieser Größe gibt es faktisch nur eine Variante — trennt nicht |

Die letzten beiden Zeilen sind die lehrreichen: **ein Kriterium abzuwerten, das im Lehrbuch schwer wiegt, ist eine Leistung — wenn man es begründen kann.**

---

## Schritt 4 · Gewichten

- **Summe 100 %.** Fünf bis acht Kriterien. Mehr kann niemand verteidigen.
- **Reihenfolge einhalten: Kontext → Gewichtung → Scoring.** Die Gewichte werden **schriftlich fixiert, bevor** gescort wird. Wer das Ergebnis kennt und dann gewichtet, baut eine nachträgliche Begründung und merkt es selbst nicht.
- **Jede spätere Änderung wird als Änderung ausgewiesen**, mit Grund. Nicht still verschieben.
- Bei einer **öffentlichen Vergabe** ist das keine Disziplin, sondern Pflicht: Zuschlagskriterien und Gewichtung werden vorab bekanntgegeben und sind danach nicht mehr änderbar.

**Drei Faustregeln, die sich bewährt haben:**
1. Der **Zweck** der Beschaffung bekommt das höchste Gewicht.
2. Was die Organisation **nicht betreiben kann**, bekommt viel — nicht wenig.
3. Was die Kandidaten **nicht trennt**, bekommt wenig — unabhängig davon, wie wichtig es klingt.

---

## Schritt 5 · Scoring, Sensitivität, Kippschwelle

**Scores 1–5, mit Ankern.** Ohne Ankerdefinition erzeugen zwei Bearbeiter zwei Skalen. Vorschlag: *5 = erfüllt belegbar und vertraglich · 4 = erfüllt, Belege öffentlich · 3 = teilweise, mit Aufwand herstellbar · 2 = nur auf Roadmap · 1 = nicht vorgesehen.*

**Jede Zahl braucht eine Begründung mit Quelle.** Und eine Zeile *„unabhängig belegt? ja / nein / teilweise"* — bei Herstellerunterlagen lautet die Antwort *nein*, und das gehört sichtbar in die Matrix.

**Sensitivitätsprobe:** jedes Gewicht um ±10 Prozentpunkte verschieben, Rest proportional, neu rechnen. Das ergibt **2 × Anzahl der Kriterien** Durchläufe. Zwei Ergänzungen:
- **Härtere Probe:** das schwerste Kriterium auf null ziehen.
- **Gleichgewichtsprobe:** alle Kriterien gleich schwer. Die ist am überzeugendsten, weil sie die Gewichtung ganz aus dem Spiel nimmt.

**Dann die Kippschwelle suchen** — das Kriterium, in dem der Sieger als einziges unterliegt, und den Gewichtswert, ab dem er verliert. **Dieser Wert gehört auf die Folie.** Er ist der einzige Satz, mit dem der Vortragende benennt, unter welcher Bedingung er falsch liegt, und er erzeugt mehr Vertrauen als jeder Gesamtscore.

> **Zwei Ehrlichkeiten, die dazugehören.** Bei Kriterien unter 10 % ist die Variante „−10" faktisch eine Null-Probe. Und wenn die stärkste Variante nahe an die Kippschwelle heranreicht, sag es: *„n von n halten — die knappste Variante liegt x Punkte darunter."*
>
> **Und die Abbruchregel:** Liegen die beiden besten Gesamtscores weniger als **0,3** auseinander, ist das kein Ergebnis, sondern unentschieden. Dann entscheidet ein Kriterium, das noch fehlt — such es, statt die Differenz zu verteidigen.

---

## Schritt 6 · Die vierzehn Folien

Benutze `vorlage-praesentation.html`. Jede Folie trägt ihre Aufgabe im Kommentar. **Die Reihenfolge ist das Argument** — nicht umstellen:

| # | Folie | Aufgabe | Pflicht |
|---:|---|---|---|
| 1 | Titel | Rahmen setzen | kein Wort über Technik |
| 2 | **Beschluss** | BLUF: Betrag, Umfang, Freigabekompetenz | warum überhaupt gefragt wird, und warum der Betrag so zugeschnitten ist |
| 3 | Der Grund | Problem mit Mengengerüst | der Satz *„Wir beschaffen kein X, wir beenden Y"*; kein Vorwurf an Betroffene |
| 4 | Wie es geht | beweist: das Vorhaben ist klein | drei Kacheln, ein Gedanke |
| 5 | Wann und Stop | Start plus **Abbruchkriterium vor dem Beschluss** | positiv formuliert, beide Bedingungen messbar |
| 6 | Alternativen | Ausschlusslogik statt Punktetabelle | Nullvariante **und** eine Ergebniszeile |
| 7 | Robustheit | Sensitivität und Kippschwelle | Skala nennen („von 5"), Kippschwelle aussprechen |
| 8 | Gegenargument | das stärkste, möglichst das eigene | mit Zahl. Dem Einwand zuerst recht geben |
| 9 | Diesmal anders | **Kontraste** zu Folie 8 | jede Zeile ein Gegensatz, keine Aufzählung |
| 10 | Bedingungen | offene Punkte als Bedingungen | eine echte Lücke offen benennen |
| 11 | Zweitbeschluss | aus einer Wissenslücke wird ein Auftrag | kein Geld; terminkritisch |
| 12 | Reihenfolge | Governance vor Werkzeug | optional, entfällt bei Zeitnot |
| 13 | Beschlussantrag | genau drei Punkte | wer, was, bis wann |
| 14 | Zustimmung | beide Ausgänge tragbar zeigen | die Frage stellen, dann still sein |

**Sechs Sprachregeln, die sich als nötig erwiesen haben:**
1. **Keine Anglizismen für Beschlusssachen.** „Bedingung", nicht „Gate". „Bedingte Freigabe", nicht „bedingtes Go". „Zugänge" oder „Lizenzen", nicht „Seats". Und nicht „Hinderungsgrund" — das dreht die Aussage um: eine Bedingung muss erfüllt werden, damit es losgeht, ein Hinderungsgrund spricht dagegen.
2. **Den Anbieter beim Namen nennen**, mit dem Zusatz, ob ein Angebot vorliegt. Gattungsbegriffe klingen nach Ausweichen.
3. **Ein Kachel-Label sagt, was die Zahl ist — nicht, was sie nicht ist.** Korrekturen gehören in den Mund, nicht auf die Folie.
4. **Kein Satz über den Vortrag.** „Ich fasse mich kurz" ist nicht kurz. Der erste Satz trägt Inhalt oder entfällt.
5. **Keine doppelten Verneinungen** in Abbruchbedingungen. Positiv formulieren.
6. **Keine Fachsprache ohne Übersetzung.** „Wird berichtet, nicht verrechnet" versteht niemand. „Es verschwindet nicht in einer anderen Position" schon.

**Und eine Warnung, die Geld kostet:** Sag **nicht** „Sie haben null Risiko". Wenn der Pitch selbst offene Punkte nennt — und er soll —, ist der Satz widerlegbar, und zwar von jemandem im Raum. Sag stattdessen, worauf das Risiko **begrenzt** ist: Betrag und Zeitraum.

**Sprechernotizen (`data-notes`) sind Pflicht auf jeder Folie.** Sie tragen, was gesagt und was **nicht** gesagt wird.

---

### Das Ausgabeformat, verbindlich

Unabhängig davon, ob zusätzlich Folien gebaut werden — **diese sechs Bestandteile gehören in jedes Ergebnis:**

1. **Die Bewertungstabelle:** alle Kriterien, ihre Gewichte mit **Summe 100**, alle Plattformen, je Zelle ein Score, je Spalte das **gewichtete Ergebnis**.
2. **Je Gewicht eine Begründungszeile** — ein Satz über *diese* Organisation, nicht über die Technik.
3. **Markierte Lücken** in der Tabelle selbst: welches Kriterium hat im Datensatz keinen Beleg, und über welchen der drei Wege aus [0.3](#03-wie-eine-lücke-überbrückt-wird) wurde es überbrückt.
4. **Die Empfehlung in drei bis fünf Sätzen**, mit **mindestens zwei Gegenargumenten**.
5. **Ein Abschnitt „Offene Fragen"** — mit Zuständigkeit und Frist, nicht als Aufzählung von Zweifeln.
6. **Die ersten 90 Tage:** was konkret passiert, welche Bedingungen vor dem ersten Euro erfüllt sein müssen, und das **Abbruchkriterium** mit seinen messbaren Bedingungen.

> **Punkt 6 wird am häufigsten vergessen und am häufigsten verlangt.** Eine Empfehlung ohne die ersten 90 Tage ist eine Meinung darüber, was man kaufen sollte — keine Entscheidungsvorlage. Und ein 90-Tage-Plan ohne Abbruchkriterium ist ein Zeitplan, keine Absicherung.

---

## Schritt 7 · Die beiden Sprechunterlagen

**Sprechzettel** — ein Blatt, Stichpunkte, für die Hand am Rednerpult. Je Folie ein Block mit Zeitbudget. Fett = muss fallen. Dazu zwei Teile, die sich bewährt haben: **die vier Sätze, die auf keinen Fall fehlen dürfen**, und eine Tabelle **vorbereiteter Antworten** auf die Rückfragen, die kommen werden (*„warum nicht abwarten?", „warum nicht verbieten?", „Amortisation?", „und wenn der Anbieter übernommen wird?"*).

**Volltext** — zum Üben, nicht zum Vorlesen. Mit Folienwechseln als `▶ FOLIE n`, Pausenmarken, Zeitmarken und Regieanweisungen in Klammern. Dazu ein **Notfallpfad**: welche Folien bleiben, wenn die Sitzung auf ein Drittel zusammenschrumpft.

---

## Schritt 8 · Das Datenblatt

Eine Datei mit allen Werten, die in die Präsentation eingegangen sind, damit ein Dritter sie prüfen kann. Vier Pflichtbestandteile:

1. **Die Einschränkung des Quellprofils, wörtlich und ganz oben.** Wenn dort steht, dass die Zahlen nicht außerhalb verwendbar sind, steht das auch hier — an erster Stelle, nicht im Anhang.
2. **Herkunftskennzeichen an jedem Wert**, mit Lesehilfe.
3. **Eine Zuordnung Folie → benötigte Werte.** Das ist der Teil, der die Datei benutzbar macht statt nur lesbar.
4. **Ein Abschnitt „Was nicht belegt ist"** mit dem Hinweis, dass diese Lücken Teil des Arguments sind und nicht Nachlässigkeit.

**Keine personenbezogenen Namen.** Alle Beteiligten als Rollen führen.

---

## Prüfliste vor der Abgabe

Die zehn Kriterien aus [`vorlagen/pitch-c-level.md`](../vorlagen/pitch-c-level.md) durchgehen — Ein-Satz-Test · Freigabekompetenz · Nullvariante mit Preis · stärkstes Gegenargument selbst genannt · Herleitung statt Scores · Ausschlusskriterien vorab · Sensitivität · die verlangte Zahl mit Herkunft · nächster Schritt mit Abbruchkriterium · offene Fragen als Bedingungen.

Dazu fünf, die erst beim Bauen aufgefallen sind:

- [ ] Steht der Beschluss in den ersten 45 Sekunden?
- [ ] Trägt jede Zeile auf Folie 9 einen **Kontrast**, keine Aussage?
- [ ] Ist die Kippschwelle genannt — also der Punkt, an dem die Empfehlung falsch wäre?
- [ ] Ist mindestens eine eigene Lücke offen benannt, ohne Beschönigung?
- [ ] Gibt es einen **Zweitbeschluss** — etwas, das nur das Gremium erledigen kann?

---

## Was dieser Skill bewusst nicht tut

**Er baut keinen Business Case.** Eine Freigabe unter einer Gremiengrenze und ein Business Case über 100.000 € sind zwei verschiedene Gattungen mit zwei verschiedenen Adressaten. Wer beides mischt, verliert beide.

**Er bewertet nicht, ob das Vorhaben sinnvoll ist.** Er vertritt eine Empfehlung, die jemand anderes hergeleitet hat — und er macht ihre Schwachstellen sichtbar, statt sie zu verstecken.

**Er ersetzt keine Rechtsberatung.** Regulatorische Aussagen gehören als Bedingung formuliert und von der zuständigen Stelle schriftlich bestätigt.

---

## Anhang · Das durchgerechnete Beispiel

[`GeAT-datengrundlage-plattformfreigabe.md`](GeAT-datengrundlage-plattformfreigabe.md) enthält denselben Weg mit echten Werten: zwölf Pflichtwerte gefüllt, acht Kriterien hergeleitet, fünf Optionen bewertet, sechzehn Sensitivitätsvarianten, Kippschwelle bei 31 %, vier offene Punkte.

**Lies es als Beispiel für die Form, nicht als Vorlage für die Zahlen.** Die Zahlen gelten für ein Unternehmen mit 709 Beschäftigten, sechs Standorten, 1,5 IT-Stellen und einer quartalsweise tagenden Gesellschafterversammlung. Ändert sich eine dieser vier Größen, ändert sich die halbe Gewichtung.
