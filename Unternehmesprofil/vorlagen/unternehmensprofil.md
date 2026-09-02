# Dein Unternehmensprofil: der Fall für alle Methoden bis Woche 12

Das Unternehmen, das du auf Tag 1.4 gewählt hast, wird ab heute zum durchgehenden Fall. Jede Methode, die du in deine Bibliothek schreibst, wendest du auf dieses Unternehmen an: ADKAR, das Kraftfeld, die Stakeholder-Landkarte, die Vendor-Matrix, der Business Case, die Datenstrategie, das Programm. Ab Woche 13 wechselt ihr auf ein vorgegebenes Unternehmen. Bis dahin ist dieses Profil dein Übungsgelände.

Ein Profil, das nur Branche, Größe und Systeme auflistet, liefert bei jeder Methode glatte Ergebnisse. Deshalb enthält dieses Profil vor allem Spannungen: Personen mit unvereinbaren Zielen, eine gescheiterte Vorgängerinitiative, ein System ohne Schnittstelle, eine Zahl, die dem Piloten wehtut. Konflikt ist das wichtigste Datenfeld.

## Drei Regeln

**1. Jeder Wert trägt eine Herkunft.** Drei Kennzeichen, immer in Klammern hinter dem Wert oder als Spalte in der Tabelle:

| Kennzeichen | Bedeutung | Was du damit tun darfst |
|---|---|---|
| `öffentlich` | belegt, mit Quelle (Link, Datum) | in jedem Deliverable verwenden |
| `angenommen` | von dir gesetzt, plausibel, meist aus einem Branchenbenchmark abgeleitet | verwenden, in Deliverables als Annahme ausweisen |
| `generiert` | vom Modell vorgeschlagen, von dir noch nicht geprüft | nur als Platzhalter. Vor der Verwendung in einem Deliverable wird daraus `angenommen` oder es wird gestrichen |

`generiert` ist ein Zustand, kein Urteil. Es markiert, was du noch anfassen musst. Bei jedem Wochenmodul (siehe Stufe 3) gehst du die generierten Werte durch, die die Methode der Woche braucht.

**2. Keine realen Personen.** Auch bei einem realen Unternehmen: die Geschäftsführung, der Betriebsrat, die Leitung IT sind erfundene Rollen mit erfundenen Namen. Was ein echter Mensch denkt und will, steht in keiner Quelle, und ein Modell erfindet es überzeugend. Namen aus Presse und Impressum bleiben draußen.

**3. Keine nicht-öffentlichen Daten deines Arbeitgebers.** Die Regel aus Tag 1.5 gilt hier ohne Ausnahme: Kundendaten, interne Zahlen, Namen von Kolleginnen und Kollegen gehören nie ins Repo. Wer das eigene Unternehmen nimmt, verfremdet es: anderer Name, andere Stadt, Zahlen gerundet und verschoben, Personen erfunden. Kennzeichen dafür ist `typ: verfremdet` im Profil.

## Fiktiv, real oder verfremdet

| Typ | Was öffentlich trägt | Was du erfinden musst |
|---|---|---|
| **real** | Branche, Größe, Standorte, Geschäftsbericht, Jobanzeigen, Presse, Produkte | alles ab Woche 2: Haltungen, Kultur, Datenqualität, Budgetspielraum, Vorgeschichte |
| **fiktiv** | Branchenbenchmarks für Margen, Personalkosten, IT-Quote | alles, aber gestützt auf die Benchmarks |
| **verfremdet** | wie fiktiv | wie fiktiv, plus konsequente Verfremdung |

Ein reales Unternehmen liefert eine glaubwürdige Hülle. Den Kern, der die Methoden trägt, liefert es nicht, weil der nie öffentlich ist. Rechne bei allen drei Typen damit, dass die Hälfte des Profils `angenommen` trägt. Das ist in Ordnung, solange es dransteht.

**Größe.** 150 bis 800 Mitarbeitende, mindestens zwei Standorte oder Geschäftsbereiche, mindestens ein Gremium neben der Geschäftsführung. Unter 100 Personen gibt es keine Stakeholder-Landkarte und keine RACI-Matrix, über 5.000 wird alles abstrakt. Wenn dein Zielunternehmen größer ist, nimm einen Bereich oder eine Landesgesellschaft.

**Branche.** Nimm eine, in der du gearbeitet hast oder arbeiten willst. Das Profil begleitet dich 11 Wochen, und in einem Bewerbungsgespräch ist der Fall, den du kennst, ein Argument.

## Dateistruktur

Das Profil ersetzt `kontext/organisation.md` aus Tag 1.5 und verteilt sich auf sechs Dateien, weil sie in unterschiedlichen Wochen gebraucht werden und ein Modell nur die lesen soll, die es braucht.

```
kontext/unternehmen/
├── recherche.md       Quellen und Benchmarks aus Stufe 1, mit Datum
├── profil.md          Identität, Geschäftsmodell, Reifegrad, drei brennende Probleme, Vorgeschichte, Regulatorik
├── zahlen.md          GuV-Skelett, Personalkosten je Bereich, IT-Budget, Kosten des Pilotprozesses, Investitionsspielraum
├── menschen.md        Gremien, Rollen mit Haltung, Mitarbeitersegmente, Kulturmerkmale
├── systeme-daten.md   Systemlandschaft, Datenbestände mit Qualitätsbefund, Wissensquellen, Schatten-IT
├── vorhaben.md        das Vorhaben aus Tag 1.4, seine Workflows, parallele Initiativen, Eskalationsweg
└── ereignisse.md      was sich im Kursverlauf am Unternehmen geändert hat, je Zeile eine Woche
```

`organisation.md` bleibt als eine Zeile stehen, die auf `unternehmen/profil.md` zeigt, damit deine `CLAUDE.md` und die Verweise aus Woche 2 weiter stimmen. Änderungen am Unternehmen sind Ereignisse („Woche 6: neue CFO, will Zahlen sehen"), keine stillen Überschreibungen. Das hält das Profil über 11 Wochen widerspruchsfrei: der Umsatz aus Woche 1 muss zum Business Case in Woche 6 passen, die Rollen aus Woche 4 tauchen in Woche 10 wieder auf.

## Der Feldkatalog

Die Felder sind aus den Methoden des Kurses rückwärts abgeleitet. Ein Thema ohne Feld wäre eine Lücke, die dir spätestens in der betreffenden Woche auffällt. Die Spalte rechts sagt, welche Woche das Feld zuerst braucht.

### profil.md

Kopf als Frontmatter, feste Schlüssel, damit alle Profile im Kurs gleich lesbar sind:

```yaml
---
name: Mustermann Antriebstechnik GmbH
typ: fiktiv            # real | fiktiv | verfremdet
branche: Maschinenbau, Antriebskomponenten
rechtsform: GmbH
eigentuemer: Familie   # Familie | Konzern | Investor | öffentliche Hand
gruendung: 1968
mitarbeitende: 420
standorte: [Bielefeld, Ostrava]
umsatz_mio_eur: 68
stand: 2026-09-02
herkunft_kopf: angenommen   # gilt für alle Werte in diesem Kopf
---
```

| Abschnitt | Inhalt | Braucht |
|---|---|---|
| Geschäftsmodell | Was verkauft wird, an wen, mit welcher Marge. Drei größte Kundengruppen, größter Wettbewerber | W1, W6 |
| Fünf Kernprozesse | Je Prozess: was passiert, wer macht es, wo es hakt. Einer davon ist der Pilotprozess | W1, W9 |
| Reifegrad | Sechs Dimensionen (Strategie, Technologie, Daten, Kultur, Prozesse, People), IST und ZIEL in zwei Jahren, Skala 1 bis 5, je ein Satz Begründung | W1, W3 |
| Drei brennende Probleme | Je Problem: Symptom, Zahl, wer darunter leidet, was bisher versucht wurde | W2, W6, W12 |
| Vorgeschichte | Mindestens eine gescheiterte Änderung der letzten fünf Jahre: was, warum gescheitert, wer erinnert sich | W2, W10 |
| Regulatorik | Branchenaufsicht, Datenarten (Kunden, Beschäftigte, Gesundheit, Bonität), Bezug zu Annex III des EU AI Act ja oder nein mit Bereich, Betriebsrat ja oder nein | W5 |

### zahlen.md

Alle Tabellen mit einer Spalte Herkunft. Runde Zahlen, die sich gegenseitig stützen: Personalkosten geteilt durch Mitarbeitende muss zur Branche passen.

| Tabelle | Spalten | Braucht |
|---|---|---|
| GuV-Skelett | Umsatz, Materialaufwand, Personalaufwand, sonstige Kosten, EBIT, je mit Vorjahr | W6, W7 |
| Personalkosten je Bereich | Bereich, Köpfe, Kosten pro Jahr | W6, W10 |
| IT-Budget | Gesamt, davon Lizenzen, Betrieb, Projekte. IT-Quote in Prozent vom Umsatz | W3, W7 |
| Pilotprozess | Vorgänge pro Jahr, Minuten je Vorgang, beteiligte Rollen, Fehlerquote, Kosten je Fehler | W6, W9 |
| Investitionsspielraum | Was in den nächsten zwei Jahren frei ist, wer es freigibt, Diskontsatz für Barwertrechnung | W6, W7 |

### menschen.md

| Tabelle | Spalten | Braucht |
|---|---|---|
| Gremien | Name, Mitglieder (Rollen), Rhythmus, was dort entschieden wird | W4, W11, W12 |
| Rollen | 8 bis 12 Zeilen: Rolle, erfundener Name, Macht (1 bis 5), Interesse (1 bis 5), Haltung zum Vorhaben (ein Satz), informeller Einfluss, was diese Person nachts wach hält | W2, W4, W12 |
| Segmente | 4 bis 6 Mitarbeitergruppen: Bezeichnung, Anzahl, Tätigkeit, Altersstruktur, Digitalaffinität, Fluktuation | W2, W10 |
| Kulturmerkmale | 5 Beobachtungen mit Beleg: nicht „hierarchisch", sondern „Entscheidungen über 5.000 Euro gehen über den Schreibtisch der Inhaberin" | W2, W10 |

Mindestens zwei Rollen müssen einander widersprechen. Wenn alle das Vorhaben gut finden, gibt es nichts zu analysieren.

### systeme-daten.md

| Tabelle | Spalten | Braucht |
|---|---|---|
| Systeme | Name, Zweck, Einführungsjahr, Betrieb (Cloud, eigenes Rechenzentrum), Schnittstellen zu anderen Systemen, Anbieter | W3, W8, W9 |
| Datenbestände | Bezeichnung, System, Verantwortliche Rolle, Qualitätsbefund (ein konkreter Mangel), personenbezogen ja oder nein | W3, W5, W8 |
| Wissensquellen | Wo das Wissen liegt, das ein Assistent lesen müsste: Laufwerke, Wiki, Mails, Köpfe. Zustand jeder Quelle | W3, W8 |
| Schatten-IT | Excel-Listen, private Tools, inoffizielle KI-Nutzung: was, wer, warum | W8, W11 |
| Auftragsverarbeiter | Welche externen Dienste Personendaten verarbeiten | W5 |

Mindestens ein System ohne Schnittstelle. Mindestens ein Datenbestand, dessen Qualität den Piloten gefährdet.

### vorhaben.md

| Abschnitt | Inhalt | Braucht |
|---|---|---|
| Das Vorhaben | Der Pilot aus Tag 1.4: Ziel, Umfang, betroffene Prozesse und Rollen, was Erfolg in einem Jahr heißt | W2, W6 |
| Workflows | Je betroffener Workflow: Auslöser, Schritte, Volumen, Schnittstellen, Freigabepunkte, was ein Fehler kostet | W9 |
| Risikoeinschätzung | Erste Einordnung nach EU AI Act (minimal, begrenzt, hoch), mit dem Grund | W5, W9 |
| Parallele Initiativen | 3 bis 5 andere Projekte mit Status, Budget, Verantwortlichen. Mindestens eines konkurriert um dieselben Leute | W11 |
| Eskalationsweg | Wer entscheidet, wenn der Pilot etwas Falsches tut: drei Stufen | W5, W11 |

### ereignisse.md

Eine Tabelle: Woche, was sich geändert hat, warum, welche Datei betroffen ist. Am Anfang leer. Hier entsteht über den Kurs die Geschichte deines Unternehmens.

## Der Prompt in drei Stufen

Zwei Fassungen, wo es einen Unterschied macht. Die Repo-Fassung gilt, wenn Claude deinen Ordner lesen und schreiben kann. Die Browser-Fassung gilt, wenn du Inhalte einfügst.

### Stufe 1: Recherche

Für ein reales oder verfremdetes Unternehmen. Werkzeug: Perplexity oder Claude mit Websuche. Ergebnis wird `kontext/unternehmen/recherche.md`.

```
Ich baue ein Unternehmensprofil für ein Übungsprojekt. Unternehmen: [Name, Sitz].
Recherchiere ausschließlich öffentlich belegbare Angaben und gib zu jeder Angabe
die Quelle mit Link und Abrufdatum an. Was du nicht belegen kannst, lässt du weg
und nennst es am Ende als offene Frage.

Ich brauche:
1. Branche, Produkte, drei wichtigste Kundengruppen, wichtigster Wettbewerber
2. Mitarbeitende, Standorte, Rechtsform, Eigentümerstruktur, Gründungsjahr
3. Umsatz und, falls veröffentlicht, Ergebnis der letzten zwei Jahre
4. Aktuelle Stellenanzeigen: welche Rollen gesucht werden, welche Systeme darin
   genannt sind (ERP, CRM, Cloud-Anbieter)
5. Presse der letzten 24 Monate: Investitionen, Umbauten, Personalwechsel in der
   Führung, Krisen
6. Branchenbenchmarks für diese Größe: EBIT-Marge, Personalkostenquote, IT-Quote
   in Prozent vom Umsatz, übliche Fluktuation

Format: Markdown, eine Tabelle je Punkt, Spalten Angabe, Wert, Quelle, Datum.
```

Für ein fiktives Unternehmen entfallen die Punkte 1 bis 5. Punkt 6 bleibt Pflicht: ohne Benchmarks tragen die Zahlen in Woche 6 nicht.

### Stufe 2: Das Profil erzeugen

Vorher den Feldkatalog aus diesem Dokument (Abschnitt „Der Feldkatalog") als `vorlagen/unternehmensprofil.md` ins Repo legen, damit das Modell weiß, welche Dateien und Tabellen es schreiben soll.

Das Modell fragt, bevor es liefert. Ein Profil, das in einem Zug fertig kommt, ist ein Profil des Modells, nicht deins.

**Repo-Fassung**, im Ordner `aitm_vorname/`:

```
Lies kontext/person.md, kontext/organisation.md und kontext/unternehmen/recherche.md.
Wir bauen daraus das Unternehmensprofil in kontext/unternehmen/, nach dem
Feldkatalog in vorlagen/unternehmensprofil.md.

Schritt 1: Stell mir fünf Fragen, eine nach der anderen, und warte jeweils auf
meine Antwort:
  1. Wofür soll dieses Unternehmen in elf Wochen stehen: welche Art von Fall will
     ich lernen zu lösen?
  2. Welches Problem tut dem Unternehmen am meisten weh, und seit wann?
  3. Was wurde in den letzten Jahren schon versucht, und woran ist es gescheitert?
  4. Wer im Unternehmen will das Vorhaben, wer will es nicht, und warum?
  5. Welche Zahl darf ich nicht schönen?

Schritt 2: Schreib die sechs Dateien. Regeln dabei:
  - Jeder Wert trägt eine Herkunft: öffentlich (mit Quelle aus recherche.md),
    angenommen (aus meinen Antworten oder einem Benchmark abgeleitet, nenne den
    Benchmark) oder generiert (dein Vorschlag, den ich noch nicht bestätigt habe).
  - Erfinde keine Angaben über das reale Unternehmen, die nicht in recherche.md
    stehen. Alles darüber hinaus ist generiert.
  - Reale Personen kommen nicht vor. Rollen bekommen erfundene Namen.
  - Zahlen müssen sich gegenseitig stützen: Personalkosten geteilt durch
    Mitarbeitende, IT-Quote, EBIT-Marge im Rahmen der Benchmarks.
  - Baue Reibung ein und markiere sie in einer Liste am Ende von profil.md:
    zwei Rollen mit unvereinbaren Zielen, eine gescheiterte Vorgängerinitiative,
    ein System ohne Schnittstelle, ein Datenbestand mit einem Mangel, der den
    Piloten gefährdet, eine parallele Initiative, die um dieselben Leute
    konkurriert, und eine Zahl, die dem Piloten wehtut.

Schritt 3: Gib mir zum Schluss die Liste aller Werte mit Herkunft generiert,
sortiert nach der Woche, in der sie zuerst gebraucht werden.
```

**Browser-Fassung:** Denselben Text verwenden, die erste Zeile ersetzen durch „Ich füge dir drei Dinge ein: mein Kontext zur Person, mein bisheriges Organisationsprofil und die Recherche." und die Dateien nacheinander in den Chat einfügen. Statt „Schreib die sechs Dateien" gilt „Gib mir die sechs Dateien nacheinander als Markdown-Blöcke, ich lege sie selbst an."

### Stufe 3: Das Profil mit einer Methode prüfen

Das ist der Teil, den du jede Woche wiederholst, sobald ein neuer Bibliothekseintrag steht. Die Methode wird auf das Profil angewendet, und das Modell darf nichts erfinden. Wo es erfinden müsste, fehlt ein Feld. Wo es einen generierten Wert benutzt hat, steht eine Prüfung an.

```
Lies bibliothek/<methode>.md und alle Dateien in kontext/unternehmen/.
Wende die Methode aus dem Bibliothekseintrag auf dieses Unternehmen an, für das
Vorhaben in vorhaben.md.

Nimm nur, was in den Dateien steht. Ergänze nichts aus deinem eigenen Wissen,
weder zur Methode noch zum Unternehmen.

Danach drei Listen:
1. Welche Angaben haben im Profil gefehlt, um die Methode sauber anzuwenden?
   Je Angabe: in welche Datei sie gehört.
2. Welche Werte mit Herkunft generiert hast du verwendet? Die muss ich vor der
   Abgabe bestätigen oder ändern.
3. An welcher Stelle gibt mein Bibliothekseintrag die Methode zu grob wieder,
   sodass du sie auf dieses Unternehmen nicht anwenden konntest?
```

Liste 1 füllst du im Profil nach, mit Herkunft `angenommen`. Liste 2 arbeitest du ab: bestätigen heißt Kennzeichen ändern, ablehnen heißt streichen und in `ereignisse.md` festhalten. Liste 3 gehört unter den Bibliothekseintrag, wie beim Selbsttest mit dem generierten Fall.

Heute, Tag 2.3, ist die erste Prüfung das Kraftfeld: `bibliothek/kotter-forcefield.md` gegen das Profil. Rechne damit, dass die Bremskräfte aus der Ankommen-Runde in `menschen.md` und `systeme-daten.md` noch keine Entsprechung haben. Genau die trägst du nach.

## Musterprofil

Ein fertiges Profil einer fiktiven Firma liegt als Beispiel bereit: Mustermann Antriebstechnik GmbH, Maschinenbau, 420 Mitarbeitende in Bielefeld und Ostrava, sieben Dateien. Es zeigt, wie Reibung konkret aussieht, wie die Zahlen ineinandergreifen und wie die drei Herkunftskennzeichen im Text stehen. Einige Werte tragen dort absichtlich `generiert`, damit du siehst, wie ein offener Wert aussieht. Du findest es im geteilten Projekt im Teamspace und im Course Book auf der Seite zu Tag 2.3.

## Im Teamspace und im Browser

Im Teamspace gibt es ein geteiltes Projekt „Werkstatt Unternehmensprofil". Es enthält die Regeln als Projektanweisung, den Feldkatalog, die drei Prompts und das Musterprofil. Dort läuft Stufe 2 für alle, die im Browser arbeiten: Recherche und Antworten im Gespräch einfügen, das Ergebnis kommt als sechs Markdown-Blöcke zurück.

**Was du dort nie hochlädst: dein Profil.** Alles im Projektwissen eines geteilten Projekts sieht der ganze Kurs. Dein Profil und deine Recherche werden im Gespräch eingefügt und landen danach in deinem Repo. Das Projekt endet mit dem Team-Zugang, das Repo bleibt.

**Stufe 3 im Browser** braucht dein Profil und den Bibliothekseintrag als Kontext, beides privat. Dafür ist dein eigenes Projekt aus Tag 1.5 der Ort: die sechs Profildateien ins Projektwissen laden, den Bibliothekseintrag dazu, und bei jeder Änderung die betroffene Datei ersetzen. Das ist der Preis der Browser-Pflichtebene. Wer im Editor arbeitet, hat den Kontext ohnehin im Ordner.

## Wann was

| Wann | Was | Ergebnis |
|---|---|---|
| Heute, Hack Time | Stufe 1 und 2, danach Stufe 3 mit dem Kraftfeld | sechs Dateien, Liste der generierten Werte |
| Jeden Montag, Ankommen | Stufe 3 mit der Methode der Vorwoche, falls noch nicht geschehen | Lücken gefüllt, Ereignis eingetragen |
| Jeden Freitag, vor der Produktion | Alle generierten Werte, die das Artefakt der Woche braucht, bestätigen oder streichen | kein `generiert` im Artefakt |
| Woche 12 | Das Profil ist der Fall für die Strategie vor dem Steering Committee | vollständiges Profil ohne `generiert` |
| Woche 13 | Wechsel auf das vorgegebene Unternehmen. Dein Profil bleibt im Repo und ist ein Portfolio-Stück | |
