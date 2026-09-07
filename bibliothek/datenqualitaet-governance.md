# Datenqualität, RAG und Data Governance

**Bibliothekseintrag – Woche 3**
Quellen: Lektüre [Zuverlässig falsch: Datenqualität, RAG und Governance](https://neuefische-teaching.github.io/AIDTM/coursebook/woche-3/lektuere-datenqualitaet-rag-governance-w3.html) · Kursdokument [3.2 · Data Governance und RAG](#3.2/3.2_Data-Governance-und-RAG.md) · [Foliensatz 3.2](https://neuefische-teaching.github.io/AIDTM/week03/3.2/slides.html) · DAMA International, *DAMA-DMBOK*, 2. Auflage · appliedAI Initiative, *Retrieval-Augmented Generation Realized*, Whitepaper 2024 (im Kurs nicht verlinkt) · [Moffatt v. Air Canada, 2024 BCCRT 149](https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot)
Angelegt: 2026-09-07 · Status: erste Fassung (vor der Diskussion am Vormittag 3.2)
Bezugsvorhaben: **RPA-Pilot für standardisierte Änderungsmitteilungen**, Bundesagentur für Arbeit (`kontext/vorhaben.md`, `kontext/organisation.md`)
Vorgänger: `bibliothek/lewin-adkar.md` (Desire-Lücke) · `bibliothek/widerstand.md` (Air-Canada-Fall)

> **Arbeitsprinzip dieses Eintrags:** ergänzen, nicht ersetzen. Die zweite Fassung nach der Diskussionsstunde kommt **unter** die erste, nichts oben wird gelöscht. Der Unterschied zwischen beiden Fassungen ist der Lernertrag.

**Inhalt:** [1 Was Datenqualität für KI bedeutet](#1-was-datenqualität-für-ki-bedeutet) · [2 Warum RAG an den Daten hängt](#2-warum-rag-an-den-daten-hängt-und-nicht-am-modell) · [3 Data Governance und die Accountable-Rolle](#3-data-governance-und-was-die-accountable-rolle-darin-tut) · [4 Übertrag auf den RPA-Pilot](#4-übertrag-auf-den-rpa-pilot) · [5 Was ich noch nicht glaube](#5-was-ich-noch-nicht-glaube)

---

## 1. Was Datenqualität für KI bedeutet

Datenqualität ist nicht Fehlerfreiheit. Sie ist das **Ausmaß, in dem Daten für einen bestimmten Zweck geeignet sind** — und daraus folgt der Satz, der mir am meisten gebracht hat: dieselben Daten können für eine Auswertung gut genug und für ein KI-System unbrauchbar sein. Es gibt also keinen allgemeingültigen Schwellwert für „gute Daten". Wer Qualitätsziele setzen will, muss zuerst den Zweck benennen, sonst ist keine Dimension messbar.

Vier Dimensionen zählen für KI:

| Dimension | Die Frage dahinter | Was schiefgeht |
|---|---|---|
| **Vollständigkeit** | Sind alle relevanten Informationen da? | Fehlt ein Dokument, antwortet das System trotzdem — aus seinem Allgemeinwissen, ohne Kennzeichnung. Der Fachbegriff dafür ist **„Not in Context"**, und das ist der gefährlichste der vier Fälle |
| **Konsistenz** | Stimmen Daten aus verschiedenen Quellen überein? | Derselbe Sachverhalt in drei Schreibweisen heißt: das System findet **ein Drittel** der einschlägigen Dokumente. Nicht ein Drittel schlechter — ein Drittel |
| **Aktualität** | Ist der Stand aktuell? | Ein überholtes Dokument wird als gültig zitiert, mit voller Konfidenz. Der technische Grund: eine Ähnlichkeitssuche hat **keine eingebaute Zeitdimension**. Ein Dokument von 2021 und eines von gestern sind gleichwertig, solange niemand Metadaten pflegt und die Filterung konfiguriert |
| **Genauigkeit** | Sind die Werte selbst korrekt? | Ein falscher Wert in einem sauber formatierten, aktuellen Dokument ist **maschinell nicht erkennbar**. Dagegen hilft keine Technik, sondern nur eine Person, die für die Domäne geradesteht |

Der Kern ist die Zuordnung, nicht das Finden: **jedes Datenproblem gehört zu genau einer dieser vier Dimensionen.** Das ist der Wert des Rasters — es zwingt zur Entscheidung, worin das Problem eigentlich besteht, und damit auch dazu, wer es beheben kann.

**Was ich als Ergänzung notiere, weil es der Kurs nicht nennt:** Ein Datensatz kann vollständig, konsistent, aktuell und genau sein und trotzdem eine unerwünschte Struktur der Vergangenheit fortschreiben. Für Auswahl- und Bewertungsentscheidungen fehlt eine fünfte Dimension, **Repräsentativität**. Für unseren RPA-Pilot ist sie nachrangig — dort werden Formularangaben übertragen, nicht Menschen bewertet.

## 2. Warum RAG an den Daten hängt und nicht am Modell

**RAG (Retrieval-Augmented Generation)** ist ein Architekturansatz, bei dem ein Sprachmodell seine Antwort aus Dokumenten erzeugt, die **erst zum Zeitpunkt der Frage** abgerufen werden. Der entscheidende Satz: **RAG trennt das Wissen von der Sprachfähigkeit.** Das Modell ändert sich nicht, wenn sich die Daten ändern.

Genau deshalb ist der Ansatz für Organisationen attraktiv — die Wissensbasis lässt sich pflegen, ohne ein Modell anzufassen. Und genau deshalb hängt alles an den Daten: **das Modell hat kein eigenes Wissen über unsere Domäne, mit dem es einen Datenfehler ausgleichen könnte.**

Der Prozess hat vier Stufen, und an jeder kann es schiefgehen, **ohne dass sich das System meldet**:

| Stufe | Was passiert | Was hier bricht |
|---|---|---|
| 1 Indexierung | Dokumente werden zerlegt und durchsuchbar gemacht | fehlende Dokumente, unbrauchbares Chunking, keine Metadaten |
| 2 Retrieval | zur Frage passende Abschnitte werden gesucht | uneinheitliche Benennung, keine Zeitfilterung, falsche Treffer |
| 3 Augmentation | die Treffer gehen als Kontext an das Modell | zu viel Kontext verwässert, zu wenig lässt Lücken |
| 4 Generation | das Modell formuliert die Antwort | die Antwort ist so gut wie der Kontext — und **klingt immer gut** |

Das ist der Unterschied zu einem Softwarefehler: **es gibt keine Fehlermeldung, nur eine Antwort, die falsch ist.** Und diese Antwort ist schwerer zu entdecken als eine Halluzination, denn eine Halluzination fällt auf, weil sie sich falsch anfühlt. Eine korrekt abgerufene, aber veraltete Information fühlt sich richtig an, ist mit Quelle belegt und wird geglaubt. Der Quellenverweis, der Vertrauen schaffen soll, macht den Fehler unsichtbar.

Der Ausdruck dafür ist **„zuverlässig falsch"**, und er ist der wichtigste Begriff des Tages: ein System, das erkennbar nicht funktioniert, ist harmloser als eines, das plausibel danebenliegt.

Zwei Begriffe, die dabei ständig fallen:
- **Chunking** — die Zerlegung in Abschnitte vor der Indexierung. Zu große Abschnitte verwässern den Abruf, zu kleine zerreißen den Zusammenhang.
- **Metadata Filtering** — die Einschränkung der Suche über Zusatzangaben wie Datum, Organisationseinheit oder Gültigkeit. Das ist das Gegenmittel gegen die fehlende Zeitdimension und laut appliedAI die **tief hängende Frucht**: einfach umzusetzen, hohe Wirkung.

**Und der Satz, an dem sich alles aufhängt:** diese Metadaten kommen nicht automatisch. Jemand muss sie pflegen, jemand muss den Standard definieren, jemand trägt die Verantwortung dafür. Damit ist man bei Governance, und zwar nicht als Anschlussprojekt.

## 3. Data Governance, und was die Accountable-Rolle darin tut

**Data Governance ist der Rahmen aus Rollen, Prozessen und Regeln**, der sicherstellt, dass Daten vollständig, konsistent, aktuell und zugänglich sind. Es ist Struktur, nicht Kontrolle — der Unterschied ist wichtig, weil „Governance" in einer Behörde sonst sofort als zusätzliche Prüfinstanz gelesen wird.

Der Merksatz taugt als Diagnosewerkzeug, weil er vier Bruchstellen benennt:

> Die richtigen Personen haben die richtigen Daten, in der richtigen Qualität, zum richtigen Zeitpunkt, aus den richtigen Gründen.

Fehlen die richtigen **Personen**, werden Fehler gesehen, aber nicht behoben. Fehlt die **Qualität**, gibt es keinen Standard und keine Validierungsregeln. Fehlt der **Zeitpunkt**, ist die Wissensbasis seit Monaten nicht aktualisiert. Fehlen die **Gründe**, fehlen die Zugriffskontrollen.

Der Standard dahinter ist das **DMBOK** (Data Management Body of Knowledge) der **DAMA** (Data Management Association). Es ist kein Gesetz, kein Werkzeug und keine Software, sondern eine geordnete Sammlung dessen, was sich bewährt hat. Sein praktischer Wert liegt nicht in der Vollständigkeit, sondern darin, dass er eine **gemeinsame Sprache** liefert: wer „Data Steward" sagt, muss gegenüber IT oder externer Beratung nicht erklären, was gemeint ist.

**Die RACI-Matrix im Datenkontext** — dieselbe aus Woche 2, nur auf Datendomänen angewandt:

| Rolle | Im Datenkontext | Typische Besetzung |
|---|---|---|
| **R**esponsible | führt die Aufgabe aus | die Person, die die Übertragung oder Pflege tatsächlich macht |
| **A**ccountable | verantwortet das Ergebnis | **Data Steward** der Datendomäne — eine **Fachrolle, keine IT-Rolle** |
| **C**onsulted | wird einbezogen, liefert Fachwissen | Fachaufsicht, Datenschutz, Compliance |
| **I**nformed | wird über Ergebnisse informiert | Leitung, Datenschutzbeauftragte |

**Was die Accountable-Rolle tut** — und das ist der Kern der Frage: sie **führt die Arbeit nicht aus**, sie **steht dafür gerade, dass eine Datendomäne stimmt.** Sie legt fest, was als Qualität gilt, entscheidet über Korrekturen, verantwortet, was in die Wissensbasis aufgenommen und was daraus entfernt wird, und sie ist ansprechbar, wenn etwas falsch ist. Sie ist ausdrücklich eine **Business-Rolle**, weil nur jemand aus dem Fach beurteilen kann, ob ein Wert inhaltlich richtig ist. *Wer Datenqualität an die IT delegiert, delegiert sie an Leute, die den Inhalt nicht beurteilen können.*

**Die häufigste Governance-Lücke ist genau diese Rolle.** Es gibt fast immer jemanden, der Fehler behebt, wenn er sie gemeldet bekommt — aber niemanden, der dafür einsteht, dass die Domäne insgesamt stimmt. Ergebnis: jeder sieht das Problem, niemand behebt es dauerhaft. Woran man das im Gespräch erkennt: **Responsible zu benennen fällt allen leicht. Accountable ist die Frage, bei der es still wird.**

Die Kontrollfrage, die ich mitnehme: *Wer ist Accountable für unsere kritischste Datendomäne?* Fällt darauf niemandem sofort ein Name ein, ist das die Antwort und keine Wissenslücke.

## 4. Übertrag auf den RPA-Pilot

Der Pilot überträgt Angaben aus Onlineformularen in ein Fachverfahren (`kontext/vorhaben.md`). Das ist kein RAG-System — aber drei Punkte des Tages treffen ihn direkt.

**Fakt aus dem Vorhaben:** Zu den zentralen Risiken zählt bereits, dass Fehler bei Personen-, Adress- oder Bankdaten erhebliche Folgen haben können. Das ist ein **Genauigkeitsproblem** im Sinne des heutigen Rasters — und genau die Dimension, die maschinell **nicht** erkennbar ist.

**Meine Einschätzung, nicht belegt:** Die vier offenen Entscheidungspunkte des Vorhabens enthalten kein Feld für die Accountable-Rolle der übertragenen Datendomäne. Das Kontrollkonzept (Punkt 4) regelt Protokollierung und Fehlerbehandlung, also **Responsible**. Wer dafür geradesteht, dass die übertragenen Bestände inhaltlich stimmen, ist nicht benannt.

**Was ich daraus vorschlagen würde:**
1. Eine **Accountable-Zeile** ins Kontrollkonzept, besetzt aus dem Fachbereich, nicht aus der IT.
2. Vier Kennzahlen als Ausgangswert **vor** dem Pilot, alle mit Bordmitteln erhebbar: Vollständigkeitsquote der Pflichtfelder · Dublettenrate · Anteil der Einträge mit Stand älter als X Monate · Anteil der Datensätze, die eine einfache Regelprüfung verletzen. Ohne Ausgangswert ist die Messgröße „Fehler- und Nachbearbeitungsquote" aus dem Vorhaben nicht interpretierbar.
3. Die **Rückkopplungsfrage** als Dauerpunkt: *Wie schnell würden wir merken, dass die Übertragung systematisch falsch liegt?*

**Das Argument, das ich mir für die Entscheidungsvorlage merke:** KI und Automatisierung machen schlechte Daten sichtbarer, nicht besser — und das ist auch eine Chance. Ein Digitalisierungsvorhaben ist oft die erste Gelegenheit, bei der Datenqualität überhaupt ein Budget bekommt. Das dreht Datenqualität von einer Vorbedingung, die das Vorhaben teurer macht, in eine Begründung, die es rechtfertigt.

**Und die Haftungsseite,** die aus `bibliothek/widerstand.md` schon bekannt ist: im Fall *Moffatt v. Air Canada* (19.02.2024) haftete die Organisation für eine plausible Falschauskunft ihres Systems, unabhängig davon, welche Technik sie erzeugt hat. Der teuerste Fehler ist nicht die fehlende Antwort, sondern die **plausible falsche**.

## 5. Was ich noch nicht glaube

- **Der Bosch-Fall ist im Kurs unbelegt.** Die Organisationszahlen sind öffentlich, die Beschreibung der internen Datensilos hat keine Fundstelle, kein Datum, kein Ergebnis. Als Muster einer organisch gewachsenen Systemlandschaft überzeugend — in einer Unterlage für Entscheider würde ich ihn als typisiertes Muster kennzeichnen und nicht als Fallstudie zitieren.
- **Die vier Dimensionen bleiben unquantifiziert.** Der Kurs benennt sie und misst sie nicht. Ein Governance-Vorschlag mit „Maßnahmen" ohne Ausgangswert ist eine Absichtserklärung — dieselbe Schwäche, die in Woche 2 schon aufgefallen ist.
- **Berechtigungen fehlen fast vollständig.** Zugriffsrechte kommen nur als Nebensatz vor („falsche Gründe: Zugriffskontrollen fehlen") und als Wort „zugänglich" in der Definition. In der Praxis ist das der Fehler mit dem größten Schaden: ein Dokument liegt in der Wissensbasis, die fragende Person hätte es nie sehen dürfen, und das System zitiert daraus — ohne dass jemand eine Regel gebrochen hat. Prüffrage, die ich künftig stelle: *Respektiert der Abruf die Berechtigungen der fragenden Person zur Laufzeit?*
- **Löschung kommt nicht vor.** Der Auftrag kennt „veraltete Einträge archivieren". Archivieren ist aber das Gegenteil von Löschen und für einen Löschanspruch die falsche Antwort. Offene Frage: verschwinden die abgeleiteten Repräsentationen eines Dokuments, wenn das Dokument gelöscht wird — und wie weist man das nach?
- **Es fehlt ein Testverfahren.** Die Fehlerkette wird erklärt, aber nicht, wie man sie misst. Naheliegend wäre ein Prüfset aus 15 bis 20 Fragen mit bekannter richtiger Antwort, das nach jeder größeren Änderung erneut läuft — einschließlich Fragen, deren Antwort **absichtlich nicht** in den Dokumenten steht. Ohne dieses Set ist jede Aussage über Abrufqualität ein Gefühl.

---

## Nachtrag nach der Diskussion (Vormittag 3.2)

*Noch offen — wird nach der Diskussionsstunde ergänzt. Zwei Fragen stehen dort an: welche der vier Dimensionen trifft uns am härtesten und woran merken wir das, und wer ist Accountable für unsere kritischste Datendomäne.*
