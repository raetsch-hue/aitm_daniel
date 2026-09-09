# Vendor Evaluation: die gewichtete Bewertungsmatrix und ihre Verteidigung

**Bibliothekseintrag – Woche 3**
Quellen: Kursdokument [3.4 · Die Entscheidung vertreten](#3.4/3.4_Die-Entscheidung-vertreten.md) · [Foliensatz 3.4](https://neuefische-teaching.github.io/AIDTM/week03/3.4/slides.html) · [Tagesseite 3.4](https://neuefische-teaching.github.io/AIDTM/coursebook/3.4/index.html) · Kriterienkatalog aus [3.1 · KI-Plattformen im Vergleich](#3.1/3.1_KI-Plattformen-im-Vergleich.md) · [Hammond, Keeney & Raiffa (1998), *The Hidden Traps in Decision Making*](https://hbr.org/1998/09/the-hidden-traps-in-decision-making-2) · [Hattie & Timperley (2007), *The Power of Feedback*](https://conselhopedagogico.tecnico.ulisboa.pt/files/sites/32/hattie-and-timperley-2007.pdf)
Angelegt: 2026-09-09 · Status: **erste Fassung, noch nicht in eigene Worte gebracht** — Auftrag 2 des Tages verlangt genau das, und der Selbsttest in [6](#6-selbsttest) misst nur dann etwas
Bezugsvorhaben: **RPA-Pilot für standardisierte Änderungsmitteilungen**, Bundesagentur für Arbeit (`kontext/vorhaben.md`, `kontext/organisation.md`)
Vorgänger: `bibliothek/datenqualitaet-governance.md` (Accountable-Rolle, Air-Canada-Fall) · `bibliothek/widerstand.md` (Gegenposition als Information)

> **Arbeitsprinzip dieses Eintrags:** ergänzen, nicht ersetzen. Was nach dem Pitch und nach Tag 3.5 dazukommt, kommt **unter** die erste Fassung. Der Unterschied zwischen beiden Fassungen ist der Lernertrag.

**Inhalt:** [1 Was eine gewichtete Bewertungsmatrix leistet](#1-was-eine-gewichtete-bewertungsmatrix-leistet) · [2 Wie eine Empfehlung im Pitch verteidigt wird](#2-wie-eine-empfehlung-im-pitch-verteidigt-wird) · [3 Woran eine Matrix erkennbar nicht trägt](#3-woran-eine-matrix-erkennbar-nicht-trägt) · [4 Übertrag auf den RPA-Pilot](#4-übertrag-auf-den-rpa-pilot) · [5 Was ich noch nicht glaube](#5-was-ich-noch-nicht-glaube) · [6 Selbsttest](#6-selbsttest)

---

## 1. Was eine gewichtete Bewertungsmatrix leistet

Eine **Bewertungsmatrix** ist ein Werkzeug für Entscheidungen mit mehreren Kriterien: Kriterien in die Zeilen, Optionen in die Spalten, je Feld ein Score, je Zeile ein Gewicht. Score × Gewicht ergibt den Punktwert, die Summe den Gesamtscore.

Der Zweck steht im Glossar des Kurses, und der entscheidende Halbsatz wird leicht überlesen: die explizite Gewichtung macht die Entscheidung nachvollziehbar, **besonders gegenüber Menschen, die andere Prioritäten haben.** Damit ist auch gesagt, was die Matrix *nicht* leistet:

| Sie leistet | Sie leistet nicht |
|---|---|
| Die Entscheidung wird **verhandelbar**, weil die Prioritäten offenliegen statt im Bauch zu bleiben | Sie findet nicht heraus, welche Option die beste ist. Sie rechnet aus, was aus *meinen* Gewichten folgt |
| Sie trennt **zwei Streitgegenstände**: „ist der Score falsch" ist eine Faktenfrage, „ist das Gewicht falsch" eine Wertfrage | Sie macht keine Wertentscheidung objektiv. Zahlen ändern nichts daran, dass eine Gewichtung eine Setzung ist |
| Sie ist **prüfbar**: eine fremde Matrix lässt sich auf Herleitung der Gewichte abklopfen | Sie ist keine Rechnung. Ein Gesamtscore von 3,8 gegen 3,7 ist kein Ergebnis, sondern Rauschen |
| Sie erzwingt **Vollständigkeit**: was keine Zeile hat, wurde nicht bewertet — und das fällt auf | Sie erfasst nur, was als Kriterium formulierbar ist. Der Rest verschwindet, siehe [3](#3-woran-eine-matrix-erkennbar-nicht-trägt) |

**Die Reihenfolge ist der eigentliche Inhalt der Methode:** erst Kontext, dann Gewichtung, dann Scoring. Wer die Gewichte setzt, nachdem er die Scores kennt, hat keine Entscheidungsgrundlage gebaut, sondern eine nachträgliche Begründung — und merkt es selbst nicht, weil das Ergebnis hergeleitet aussieht. Hammond, Keeney und Raiffa führen genau das als Denkfalle: man sucht bestätigende Belege für die Option, die man ohnehin wollte. Die Matrix ist gegen diese Falle **nicht** immun, sie macht sie nur dokumentierbar.

Der Merksatz dazu, in der brauchbaren Fassung der Tagesseite:

> **Es gibt keine einzige richtige Matrix. Es gibt eine begründete und eine unbegründete.**
> Wer seine Gewichtung aus dem Unternehmenskontext ableiten kann, hat eine Entscheidungsgrundlage. Wer sie gesetzt hat, weil sie plausibel aussah, hat eine Liste.

Die Folie sagt inzwischen stattdessen „es gibt *situationsadäquate* Matrizen". Das ist eine Beschreibung, kein Maßstab — und wer nur diese Fassung mitnimmt, kann keine Matrix mehr kritisieren, auch nicht die eigene. Ich behalte die erste.

**Die Prüffrage, die ich mir merke:** *Kann ich jedes Gewicht auf einen Satz über die Organisation zurückführen?* Nicht auf ein Gefühl über die Technik. Geht das bei einem Kriterium nicht, ist es entweder falsch gewichtet oder gar kein Kriterium.

## 2. Wie eine Empfehlung im Pitch verteidigt wird

Ein **Pitch** ist keine Ergebnispräsentation. Er ist darauf angelegt, **Widerspruch zu erzeugen und ihn dann argumentativ aufzulösen** — ein *Entscheidungsangebot*, kein Vortrag. Daraus folgt ein ungewohntes Erfolgskriterium: ein Pitch, nach dem niemand widerspricht, hat nicht überzeugt, sondern nichts angeboten.

Die Struktur, vier Abschnitte in acht bis zehn Minuten:

| Abschnitt | Zeit | Was hier wirklich passiert |
|---|---|---|
| **Kontext** | max. 2 min | Die Grundlage der Gewichtung. Ohne ihn ist alles Folgende beliebig — und länger als zwei Minuten ist er Selbstzweck |
| **Matrix mit Gewichtung** | max. 3 min | Nicht die Scores vortragen, sondern die **Herleitung** der Gewichte. Die Scores sind nachlesbar, die Begründung nicht |
| **Empfehlung und Gegenargumente** | max. 3 min | Der Kern. Mindestens zwei Gegenargumente, selbst genannt |
| **Nächster Schritt** | max. 2 min | Was als Erstes passiert, wenn zugestimmt wird. Fehlt er, ist die Empfehlung eine Meinungsäußerung |

> **Eine Empfehlung ohne benannte Gegenposition ist keine Empfehlung, sondern eine Meinung.**

Vier Regeln, die ich für jede Entscheidungsvorlage übernehme:

1. **Die Gegenargumente vor die Empfehlung ziehen.** Der häufigste Fehler ist, dass sie hinten wegfallen, wenn die Zeit knapp wird. Wer erst zeigt, was gegen die eigene Wahl spricht, und dann empfiehlt, kann sie nicht mehr verlieren — und wirkt geprüft statt defensiv.
2. **Ein schwaches Gegenargument ist schlimmer als keines.** Es liest sich als Alibi und entwertet die übrigen. Das stärkste eigene Gegenargument selbst zu nennen nimmt der Gegenseite die Pointe.
3. **Vor jedem Nachbessern unterscheiden:** **Datenproblem** (eine Zahl fehlt oder ist unbelegt → recherchieren) oder **Argumentationsproblem** (die Zahlen stehen, die Schlussfolgerung trägt nicht → Gewichtung oder Empfehlung ändern). *Blindes Nachbessern trifft meist das falsche.* Und: hält die Begründung unter Druck nicht, ist das eine Erkenntnis, kein Versagen.
4. **Feedback ist kein Auftrag.** Was in mehreren Rückmeldungen steht, ist ein echtes Problem; was in einer steht, kann Geschmack sein. Man muss nicht jede umsetzen — man muss **begründen können, warum nicht.** Damit wird aus dem Umgang mit Feedback eine dokumentierte Entscheidung statt einer Fleißaufgabe.

**Der Selbsttest vorher**, und der letzte Halbsatz ist der wirksame Teil:
> *„Spiel den kritischen Stakeholder: Was würdest du mir entgegenhalten? Ich will die stärksten Gegenargumente hören, nicht freundliche Kritik."*

Ohne ihn liefert ein Modell Zustimmung mit Verbesserungsvorschlägen. Die Grenze: das Modell kennt die Organisation nicht und liefert die Einwände eines generischen Stakeholders. Zum Härten der Argumentation brauchbar, als Ersatz für die Frage, was *diese* Freigabeinstanz fragt, nicht.

**Und die Regel für Feedback, das ich selbst gebe** — der Befund von Hattie und Timperley, nicht Höflichkeit: Rückmeldungen zur Person wirken am schwächsten, zur Aufgabe und zum Vorgehen am stärksten. „Mehr Details" und „besser strukturieren" sind deshalb kein Feedback, sondern eine Vertagung. Brauchbar ist nur: **was genau, wo, wie.**

## 3. Woran eine Matrix erkennbar nicht trägt

Sechs Anzeichen. Die ersten drei kann man an der eigenen Matrix prüfen, die letzten drei fallen erst im Gespräch auf.

| Anzeichen | Warum es trägt | Was zu tun ist |
|---|---|---|
| **Die Gewichte lassen sich nicht auf den Kontext zurückführen** | Dann ist der Gesamtscore eine Zahl ohne Aussage | Je Gewicht ein Satz über die Organisation. Geht das nicht: Kriterium streichen |
| **Die Empfehlung kippt bei kleiner Änderung der Gewichte** | 3,8 gegen 3,7 ist keine Entscheidung | Sensitivität prüfen: wichtigstes Kriterium ±10 Prozentpunkte, Rest proportional. Ergebnis als Satz: *„stabil, solange X über 20 % gewichtet ist"* |
| **Es gibt keine Nullvariante** | „Nichts tun" ist die erste Rückfrage jeder Freigabeinstanz, und sie kostet null | Vierte Spalte: Status quo fortführen — mit seinen Kosten und Risiken, nicht als Strohmann |
| **Alle Beteiligten haben dieselben Prioritäten** | Dann ist die Matrix Aufwand ohne Ertrag; sie ist für den Dissens gebaut | Aufwand kürzen, Entscheidung direkt begründen |
| **Die Frage war falsch zugeschnitten** | Drei Optionen sauber verglichen, aber der Bedarf liegt in einer anderen Kategorie. Das ist weder Daten- noch Argumentationsproblem | Vor der Matrix: *ist die Aufgabe regelhaft beschreibbar?* Kategorie klären, dann bewerten |
| **Ein Kriterium ist eigentlich ein Ausschlusskriterium** | „DSGVO-konform: 4" ist unsinnig. Entweder liegt ein Auftragsverarbeitungsvertrag vor oder nicht | Als **K.-o.-Kriterium** vor die Matrix ziehen, nicht als Score hinein |

**Und die vier Größen, die keine Spalte misst** — sie gehören nicht in die Matrix, sondern in „Offene Fragen" und in den nächsten Schritt:

- **Eigentümerwechsel.** Bewertet wird der Anbieter von heute, gebunden wird man an den von morgen. Nach der Übernahme von VMware durch Broadcom (November 2023) endeten Perpetual-Lizenzen und Support-Verlängerungen; ein Großkunde klagte 2024 und bezifferte die geforderte Steigerung im Verfahren mit bis zu 1.050 % (Parteivortrag, kein festgestellter Sachverhalt). Konsequenz: Exit, Portabilität und Preisänderungsklauseln **verhandeln**, nicht bewerten.
- **Exit-Kosten.** Ein Score „Lock-in: 3" sagt nichts darüber, was ein Wechsel tatsächlich kostet. Gehört als offen ausgewiesene Schätzung in Personentagen daneben.
- **Einführungskosten.** Die Matrix vergleicht Produkte, Projekte scheitern aber teurer als Produkte. Bei Lidl waren rund 201 Mio. EUR geplant und etwa 500 Mio. verbraucht, bevor die Einführung 2018 abgebrochen wurde — der Anbieter war nicht das Problem, die **Passung** war es.
- **Durchsetzungsrisiko.** „DSGVO-konform: 5" verwechselt Zusage mit Nachweis. Die italienische Aufsicht sperrte ChatGPT 2023 vorläufig, verhängte Ende 2024 ein Bußgeld von 15 Mio. EUR, und ein Gericht in Rom hob es im März 2026 auf — **nicht in der Sache, sondern wegen Unzuständigkeit.** Wer auf die Aufsicht setzt, wartet Jahre auf eine Zuständigkeitsfrage. Konformität muss vertraglich gesichert sein.

**Der Fall, der mich am meisten überzeugt**, weil er nicht die Auswahl betrifft, sondern das Danach: Ein US-Krebszentrum beauftragte 2013 ein KI-Vorhaben über 2,4 Mio. USD und sechs Monate. Der Vertrag wurde **zwölfmal verlängert**; ein Prüfbericht hielt 2017 rund 62 Mio. USD Ausgaben fest, Honorare wiederholt knapp unter der Grenze, ab der das Aufsichtsgremium hätte zustimmen müssen, und ein Ergebnis, das nie in der Versorgung eingesetzt wurde. **Die Governance versagte nicht bei der Auswahl, sondern bei den Verlängerungen.** Deshalb gehört in jeden „nächsten Schritt" ein Pilot mit Abbruchkriterien und Kostendeckel je Verlängerung — nicht aus Vorsicht, sondern weil sonst niemand den Punkt bestimmt, an dem entschieden wird.

## 4. Übertrag auf den RPA-Pilot

**Fakt aus dem Vorhaben:** Offener Entscheidungspunkt 3 lautet „Technischer Vergleich: RPA, direkte Schnittstelle und Verbesserung des bestehenden Fachverfahrens" (`kontext/vorhaben.md`). Das ist genau die Aufgabe dieses Eintrags — drei Optionen, mehrere Kriterien, eine zu verteidigende Empfehlung. Und es ist in einem Punkt besser gestellt als die Kursübung: **die Nullvariante ist schon drin.** „Verbesserung des bestehenden Fachverfahrens" ist die Option, die in der Übung fehlte.

**Fakt:** Punkt 2 verlangt einen vollständigen Business Case mit Entwicklungs-, Lizenz- und Betriebskosten sowie Amortisationszeit. Damit sind die Einführungskosten aus [3](#3-woran-eine-matrix-erkennbar-nicht-trägt) formal abgedeckt — als Anforderung. Belegt sind sie nicht.

**Fakt:** Die Messgrößen des Pilots sind Bearbeitungszeit, Fehler- und Nachbearbeitungsquote, Anteil automatisch verarbeiteter Fälle, eingesparte Arbeitsschritte. Für keine liegt ein Ausgangswert vor. Ohne Ausgangswert kann keine dieser Größen einen Score begründen — sie sind Zielgrößen, keine Bewertungsgrundlage.

**Gruppeneinschätzung, unvalidiert:** Der Reifegrad (`kontext/organisation.md`) — Strategie 2, Technologie 2, Daten 2, Kultur 1, Prozesse 2, People 3. Jede Gewichtung, die ich daraus ableite, trägt diesen Vorbehalt mit: die Einschätzung ist nicht durch Interviews, Prozessdaten oder Systemanalysen geprüft, und besonders die Technologiebewertung von 2 verträgt sich schlecht mit einer eigenen Private Cloud, einem Data Warehouse und einem KI-Kompetenzzentrum. **Eine Matrix auf diesem Fundament ist begründet, aber nicht belastbar** — und genau so muss sie ausgewiesen werden.

**Meine Einschätzung, nicht belegt — was aus dem Reifegradprofil für die Gewichtung folgt:**

| Kriterium | Warum es hoch gewichtet gehört | Aus welcher Zeile des Profils |
|---|---|---|
| **Wartungsaufwand und Abhängigkeit von Oberflächen** | Steht im Vorhaben selbst als zentrales Risiko: RPA hängt an bestehenden Benutzeroberflächen | Technologie 2, viele getrennte Systeme |
| **Betreibbarkeit im Fachbereich** | Bei Kultur 1 und geringer Veränderungsbereitschaft entscheidet nicht die Funktion, sondern wer es im Alltag trägt | Kultur 1, People 3 |
| **Datenschutz und Protokollierung als K.-o.-Kriterium** | Personen-, Adress- und Bankdaten. Das ist kein Score, das ist eine Bedingung | Zentrales Risiko im Vorhaben |
| **Rückholbarkeit** | Ein ungeeigneter Prozess könnte dauerhaft festgeschrieben werden — das ist das Exit-Problem in Prozessform | Zentrales Risiko im Vorhaben, Prozesse 2 |

**Der Punkt, an dem sich die Kursmethode für eine Behörde ändert, und der wichtigste dieses Abschnitts:** Bei einer öffentlichen Beschaffung ist die Gewichtung nicht nur intern zu begründen. Zuschlagskriterien und ihre Gewichtung werden in den Vergabeunterlagen **vorab** bekanntgegeben und dürfen danach nicht mehr verändert werden. Damit ist die Reihenfolge „erst Kontext, dann Gewichtung, dann Scoring" hier nicht Methodendisziplin, sondern Voraussetzung — eine nachträglich verschobene Gewichtung ist im Kurs ein Denkfehler und in einem Verfahren ein Angriffspunkt. **Vorbehalt: das ist meine Einordnung, keine Rechtsauskunft; mit der Vergabestelle zu klären, bevor eine Matrix in eine Unterlage geht.**

**Was ich konkret vorschlagen würde:**
1. **Zwei K.-o.-Kriterien vor die Matrix:** Datenschutz- und Protokollierungsanforderungen aus dem Kontrollkonzept (Punkt 4). Erfüllt oder nicht — kein Score.
2. **Vier Kriterien mit Gewichten**, jedes mit einem Satz aus dem Organisationsprofil begründet, plus die Nullvariante als vierte Spalte.
3. **Ausgangswerte vor dem Pilot erheben** — sonst ist die Fehler- und Nachbearbeitungsquote als Kriterium nicht bewertbar. Das ist derselbe Befund wie in `bibliothek/datenqualitaet-governance.md`, Abschnitt 4.
4. **Sensitivität prüfen** und das Ergebnis als Satz in die Vorlage: bei welcher Gewichtung kippt die Empfehlung?
5. **Nächster Schritt mit Abbruchkriterien**, nicht mit einem Termin. Drei vorher festgelegte Bedingungen, bei denen der Pilot endet.

## 5. Was ich noch nicht glaube

- **Die Übung bewertet drei Plattformen, die Realität bewertet Optionen.** Im Pilot stehen RPA, Schnittstelle und Verfahrensverbesserung gegeneinander — drei verschiedene *Kategorien*, nicht drei Anbieter derselben Kategorie. Ob eine Matrix Kategorien überhaupt vergleichen kann, ist mir unklar: die Kriterien, die eine Schnittstelle auszeichnen, sind nicht die, an denen RPA gemessen wird. Verdacht: für Kategorienentscheidungen braucht es die Kategorienfrage aus 1.4, und die Matrix kommt erst **danach**, innerhalb der gewählten Kategorie.
- **Der Gesamtscore ist die schwächste Stelle der Methode und wird nirgends problematisiert.** Scores von 1 bis 5 werden multipliziert und addiert, als wären die Abstände gleich groß und die Kriterien unabhängig. Beides ist selten der Fall. Praktisch heißt das: knappe Ergebnisse nicht als Ergebnis lesen, sondern als „unentschieden" — und dann nach einem Kriterium entscheiden, das noch fehlt.
- **Fünf Kriterien sind wenig, und das ist eine Setzung ohne Begründung.** Der Kurs verlangt fünf Kernkriterien. Warum fünf, steht nirgends. Vermutlich Zeitgründe der Übung. Für eine echte Vorlage würde ich lieber sagen, was bewusst **nicht** bewertet wurde.
- **Peer-Feedback ohne Kalibrierung streut.** Topping zeigt, dass Peer-Feedback wirkt, wenn die Bewertenden vorher an einem Beispiel kalibriert wurden. Das passiert in der Übung nicht. Ich weiß deshalb nicht, wie viel die Rückmeldungen wert sind, die ich bekomme — und werde sie nach „mehrfach genannt / einmal genannt" sortieren müssen statt nach Überzeugungskraft.
- **Das Publikum sind Peers, nicht Entscheider.** Die Fragen, die tatsächlich kommen — was kostet es, wer betreibt es, wie lange dauert es, wer hat das schon gemacht — stellen Menschen mit demselben Wissensstand nicht. Meine Matrix wird in der Übung also an der falschen Härte geprüft. Gegenmittel bis Tag 3.5: die vier Fragen selbst an die eigene Matrix stellen.
- **Ich habe die Sensitivitätsprüfung noch nie gemacht.** Sie steht in diesem Eintrag als Empfehlung, nicht als Erfahrung. Bis ich sie einmal gerechnet habe, ist das übernommenes Wissen.

---

## 6. Selbsttest

*Noch offen.* Der Prompt aus Auftrag 2, wörtlich, gegen **diese** Datei zu laufen — und zwar erst, nachdem der Eintrag in eigenen Worten steht:

> *„Lies `bibliothek/vendor-evaluation.md`. Bau daraus einen kurzen Fall, maximal 200 Wörter, aus einer anderen Branche als meiner: eine Ausgangslage und eine Frage, in der genau diese Methode gebraucht wird. Nenne die Lösung nicht. Danach zwei Dinge: Welche Angaben haben in meinem Eintrag gefehlt, um den Fall zu bauen? An welcher Stelle gibt mein Eintrag die Methode falsch oder zu grob wieder?
> Nimm nur, was in der Datei steht. Ergänze nichts aus deinem eigenen Wissen."*

Die zwei Antworten kommen hierunter. Der Prompt funktioniert nur gegen einen selbst geschriebenen Text: er soll die Lücken **meines** Verständnisses zeigen, nicht die einer fremden Zusammenfassung.

---

## Nachtrag nach dem Pitch und nach Tag 3.5

*Noch offen.* Drei Fragen stehen an: Was hat der Pitch über die Matrix offenbart, das vorher nicht auffiel? Welches Gegenargument war am schwersten zu entkräften? Und was wäre noch offen, wenn die Matrix morgen einer echten Entscheidungsinstanz vorliegt?
