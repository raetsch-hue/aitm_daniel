---
titel: RACI-Matrix Datenpflege — Bewerber- und Kundendatenbank
bezug: datenverantwortung.md, daten/AUFLOESUNG-datenqualitaet.md, daten/KORREKTUR-dokumentation.md, menschen.md
typ: Entwurf einer Zuständigkeitsregelung, nicht beschlossen
datum: 2026-09-08
woche: 03
status: Vorschlag zur Vorlage in der Geschäftsführung
verantwortlich: Rolle 15 (AI and Digital Transformation Manager)
herkunft: abgeleitet. Rollen und Gremien aus menschen.md, Befunde aus der Datenqualitätsanalyse; die Zuordnung ist eine begründete Setzung
---

# RACI-Matrix Datenpflege

> **Gegenstand.** Bewerberdatenbank und Kundendatenbank der GeAT mbH — Personaldienstleistung,
> 709 Beschäftigte, davon 69 Stammpersonal, sechs Niederlassungen plus Zentrale in Erfurt.
> Grundlage sind die Datenqualitätsanalyse in
> [`daten/AUFLOESUNG-datenqualitaet.md`](daten/AUFLOESUNG-datenqualitaet.md) und das
> Reparaturprotokoll in [`daten/KORREKTUR-dokumentation.md`](daten/KORREKTUR-dokumentation.md).
>
> **Geltungsbereich.** Alle Personen in [`menschen.md`](menschen.md) sind erfunden, Ausnahme
> Rolle 15. Die Zuordnung unten ist ein Vorschlag und nicht beschlossen.

## Lesart

| Buchstabe | Bedeutung | Regel |
|---|---|---|
| **A** — Accountable | steht dafür ein, entscheidet Ausnahmen, wird gefragt, wenn es schiefgeht | **genau eine Rolle je Zeile**, nie zwei |
| **R** — Responsible | führt die Aufgabe aus | mehrere möglich |
| **C** — Consulted | wird vorher gehört, hat kein Entscheidungsrecht | mehrere möglich |
| **I** — Informed | erfährt das Ergebnis, ohne mitzureden | mehrere möglich |

Der Unterschied, der in der Praxis über alles entscheidet: **A ist nicht die Person, die am meisten
weiß, sondern die, die eine Regel gegen Widerstand durchsetzen kann.** Wer keine Weisung erteilen
kann, kann kein A sein — sonst steht die Matrix auf dem Papier und im Alltag entscheidet die
Niederlassung.

## Die Matrix

| Aufgabe | **A** (genau eine) | R | C | I |
|---|---|---|---|---|
| **1. Neue Einträge aufnehmen** — Bewerberprofil oder Kundenbetrieb erstmals erfassen | **Rolle 4 · Leiterin Recherche und Recruiting Center** (Kloß) | Recruiting Center; Personaldisposition; Vertriebsinnendienst | Rolle 12 IT-Leitung (Feldlogik); Rolle 8 DSB (Pflichtangaben, Einwilligung) | Niederlassungsleitungen; Rolle 10 Controlling |
| **2. Fehler melden** — auffällige, fehlende oder widersprüchliche Werte weitergeben | **Rolle 15 · AI and Digital Transformation Manager** | alle Erfassenden; monatlicher Prüflauf `pruefe_datenqualitaet.py` | Rolle 4; Rolle 3 Vertriebsleitung; Rolle 11 Sachbearbeitung | Geschäftsführung; Niederlassungsleitungen |
| **3. Fehler beheben** — den fehlerhaften Datensatz berichtigen | **Rolle 3 · Vertriebsleitung** (Steinbrück) für Kundendaten, **Rolle 4** für Bewerberdaten — je Bestand genau eine, siehe Hinweis unten | Disponent oder Recruiter, der den Datensatz führt; Rolle 12 IT bei Massenkorrekturen | Rolle 11 Sachbearbeitung (Auswirkung auf Abrechnung); Rolle 12 IT | Rolle 15; Rolle 10 Controlling |
| **4. Veraltete Einträge archivieren** — Fristablauf, Löschkonzept, Statuswechsel auf inaktiv | **Rolle 2 · Geschäftsführer Finanzen, Recht, IT, Personal** (Achtelik) | Rolle 12 IT-Leitung (Löschlauf); Rolle 4 (Vorauswahl Bewerberprofile) | Rolle 8 DSB (Fristen und Nachweis); Rolle 9 Betriebsrat (soweit Beschäftigtendaten) | Rolle 15; Niederlassungsleitungen; Rolle 10 Controlling |
| **5. Reparaturen freigeben** — Massenkorrektur, Löschlauf oder Regeländerung wirksam schalten | **Rolle 2 · Geschäftsführer Finanzen, Recht, IT, Personal** (Achtelik) | Rolle 12 IT-Leitung (Durchführung); Rolle 15 (Vorlage und Nachweis) | Rolle 8 DSB; Rolle 9 Betriebsrat; Rolle 10 Controlling (Auswirkung auf Kennzahlen) | Geschäftsführung insgesamt; Niederlassungsleitungen; Rolle 13 Gesellschaftervertretung ab 25.000 Euro |

**Hinweis zu Zeile 3.** Die Vorgabe „genau eine Rolle als Accountable" ist eingehalten, aber nur,
weil der Bestand geteilt wird: Kundendaten haben ein A, Bewerberdaten haben ein A. Ein einziges A
über beide Bestände wäre entweder zu weit von der Arbeit entfernt (Geschäftsführung) oder ohne
Zugriff auf die halbe Datenmenge (Recruiting kennt die Kundenhistorie nicht). Wer die Matrix auf
eine Zeile mit einem A zwingen will, muss die neue Rolle aus dem nächsten Abschnitt schaffen — dann
und nur dann gibt es einen Kandidaten.

## Warum diese fünf A und keine anderen

**Zeile 1 an Rolle 4.** Die Erfassung ist der einzige Punkt, an dem Datenqualität ohne Nacharbeit
entsteht. Rolle 4 hat 2023 das Bewerbermanagement-Modul beantragt und trägt seither die Folgen
seiner Nichtnutzung — 34 Prozent nach drei Jahren. Sie ist die Einzige mit einem Eigeninteresse an
gepflegten Feldern. **Das Risiko:** ihr fehlt das Weisungsrecht gegenüber den Disponenten, die zwei
Drittel der Einträge anlegen. Ohne die Änderung der Zielvereinbarung ist ihr A nominell.

**Zeile 2 an Rolle 15.** Meldungen brauchen eine Stelle, die sammelt, doppelte Meldungen
zusammenführt und den Prüflauf verantwortet — und die kein Eigeninteresse daran hat, einen Befund
klein zu halten. Genau das trifft auf eine Rolle ohne eigenen Bestand zu. **Das Risiko:** Macht 2
bei Interesse 5. Wer nur melden darf und nichts entscheidet, wird nach dem dritten ignorierten
Bericht aufhören zu melden.

**Zeile 3 an Rolle 3 und Rolle 4.** Berichtigen muss, wer den Datensatz fachlich verantwortet, sonst
entstehen aus Korrekturen neue Fehler. Bei Kundendaten ist das der Vertrieb, bei Bewerberdaten das
Recruiting. **Das Risiko:** die Hälfte der Kundenabsprachen liegt in persönlichen Outlook-Ordnern.
Solange das so ist, kann auch der Vertrieb einen Widerspruch nur vermuten, nicht auflösen.

**Zeile 4 an Rolle 2.** Archivieren und Löschen ist keine Datenpflege, sondern die Erfüllung einer
Rechtspflicht. Verantwortlicher im Sinne der DSGVO ist die Gesellschaft, ressortmäßig der
Geschäftsführer für Recht — die 18.000 überfälligen Profile sind sein Thema und nicht das des
Recruiting. **Das Risiko:** seine Kapazität hängt vollständig an der Softwaremigration 2027. Ein A
ohne Zeit delegiert faktisch an niemanden.

**Zeile 5 an Rolle 2.** Eine Massenkorrektur ändert die Datenbasis aller Auswertungen, ein
Löschlauf ist unwiderruflich. Freigabe gehört auf dieselbe Ebene wie die Haftung. **Das Risiko:**
dieselbe Rolle trägt Zeile 4 und Zeile 5, prüft also die Freigabe ihrer eigenen Aufgabe. Deshalb
ist Rolle 15 dort als R für Vorlage und Nachweis gesetzt und Rolle 10 als C — das ersetzt keine
Funktionstrennung, macht sie aber nachvollziehbar.

## Die Rolle, die fehlt

**Es fehlt ein Data Steward für Bewerber- und Kundendaten:** eine benannte, operative
Datenverantwortung mit Weisungsrecht in den Niederlassungen, angesiedelt zwischen Recruiting,
Vertrieb und IT.

Woran man es in der Matrix oben sieht — an vier Stellen, alle dieselbe Ursache:

1. **Zeile 1 hat ein A ohne Weisungsrecht.** Rolle 4 leitet das Recruiting Center in Erfurt, nicht
   die Disposition in sechs Niederlassungen. Die Erfassungsregel, die sie durchsetzen soll, gilt
   überwiegend für Menschen, die ihr nicht unterstellt sind.
2. **Zeile 2 hat ein A ohne Durchgriff.** Melden ohne Entscheidungsrecht funktioniert genau so
   lange, wie jemand freiwillig zuhört.
3. **Zeile 3 brauchte eine Teilung des Bestands**, um die Ein-A-Regel zu erfüllen. Das ist ein
   Umweg um eine fehlende Rolle, keine Lösung.
4. **Zeilen 4 und 5 landen beide bei derselben Geschäftsführungsrolle**, weil unterhalb der
   Geschäftsführung niemand existiert, der eine bestandsübergreifende Entscheidung treffen darf.

**Was die Rolle konkret hätte:** Pflege der Wertelisten und Pflichtfelder, Triage der Meldungen aus
dem monatlichen Prüflauf, Freigabe von Einzelkorrekturen bis zu einer festgelegten Menge,
Fachverantwortung für die Datenfelder in der Ausschreibung Q1/2027, und — das Entscheidende — ein
schriftliches Weisungsrecht der Geschäftsführung für Datenregeln gegenüber allen Niederlassungen.

**Was sie kostet.** Rund 0,5 Stellen. Bei 4,695 Mio Euro Personalaufwand Stammpersonal auf 69
Köpfe sind das etwa 68.000 Euro je Kopf und Jahr, also **rund 34.000 Euro** (`gerechnet` aus
[`zahlen.md`](zahlen.md); der Personalaufwand selbst ist `angenommen`). Zum Vergleich: die
Nichtbesetzung von 1.860 Anfragen im Jahr 2025 steht in derselben Datei.

**Der Notbehelf, wenn die Stelle nicht kommt.** Die Aufgabe als benannten Teilauftrag an Rolle 4
geben — mit drei Bedingungen, ohne die es nicht funktioniert: ein schriftliches Weisungsrecht für
Datenregeln, eine Freistellung von mindestens einem Tag pro Woche, und die Aufnahme der Datenpflege
in die Zielvereinbarung der Niederlassungsleitungen. Fehlt eine der drei, ist es kein Notbehelf,
sondern eine zusätzliche Aufgabe für eine Person, die schon 2023 ein System einführen sollte, das
niemand gefüllt hat.

## Zwei weitere Lücken, die nicht Rollen sind

**Es gibt kein Gremium.** Der Lenkungsausschuss Digitalisierung existiert nicht; Vorlagen gehen
dienstags in die Geschäftsführung, alles über 25.000 Euro quartalsweise in die
Gesellschafterversammlung. Eine RACI-Matrix ohne Ort, an dem strittige Fälle entschieden werden,
verlagert jeden Konflikt in die Geschäftsführung — und die entscheidet ihn nach Dringlichkeit,
nicht nach Datenlogik. Ein monatlicher Termin von 30 Minuten mit Rolle 3, 4, 12 und 15 würde
reichen; er muss nur existieren und ein Protokoll haben.

**Es gibt keine Funktionstrennung bei der Freigabe.** Zeile 5 verlangt, dass jemand freigibt, der
die Reparatur nicht selbst gebaut hat. Bei 1,5 IT-Stellen und ohne Qualitätsfunktion ist das
organisatorisch nicht gedeckt. Der praktikable Ersatz: jede Massenkorrektur wird vorher als
Prüfbericht und nachher als zweiter Prüfbericht dokumentiert, beide gehen an Rolle 10 Controlling.
Das ist keine Trennung, aber es ist nachprüfbar — und nachprüfbar ist die Mindestanforderung.

## Gegenargumente

1. **„Fünf Aufgaben, vier verschiedene A — das ist Bürokratie für 69 Stammkräfte."** Der Einwand
   trifft, wenn daraus vier Gremien werden. Er trifft nicht, wenn es vier Zeilen in bestehenden
   Zielvereinbarungen sind. Der Aufwand liegt in der Entscheidung, nicht im Betrieb.
2. **„Der Data Steward ist eine Stelle, die kein Geld verdient."** Richtig, und ehrlich zu sagen:
   eine Amortisation lässt sich für diese Rolle nicht seriös rechnen. Sie ist Voraussetzung für die
   Dokumentationspflicht eines Hochrisikosystems und rechnet sich nur als vermiedener Schaden.
3. **„Rolle 15 hat ein Eigeninteresse an dieser Matrix."** Auch richtig. Die Rolle wurde für dieses
   Vorhaben geschaffen, und jede Zuständigkeitsregelung, die sie vorschlägt, vergrößert ihren
   Wirkungskreis. Das gehört in die Vorlage benannt, nicht verschwiegen — ebenso wie der
   spiegelbildliche Konflikt von Rolle 8, deren Aufwand mit der Sorgfalt steigt, die sie anmahnt.
