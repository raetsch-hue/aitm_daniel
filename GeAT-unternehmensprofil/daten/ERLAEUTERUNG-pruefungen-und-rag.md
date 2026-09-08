---
titel: Was jeder Prüfbefund für ein RAG-System bedeutet
gehoert_zu: pruefe_datenqualitaet.py
datum: 2026-09-08
woche: 03
status: Erläuterung, keine Auflösung — enthält keine Angabe darüber, welche Fehler in den Übungsdateien stecken
herkunft: abgeleitet. Die Prüfungen sind im Skript nachlesbar, die Folgerungen für RAG sind begründete Setzungen
---

# Prüfungen und ihre Bedeutung für ein RAG-System

> **Was diese Datei ist.** Zu jeder Prüfung des Skripts
> [`pruefe_datenqualitaet.py`](pruefe_datenqualitaet.py) **ein Satz**: was der Befund für ein
> RAG-System bedeutet. Sie verrät nicht, welche Fehler in den Übungsdateien stecken — das steht
> in [`AUFLOESUNG-datenqualitaet.md`](AUFLOESUNG-datenqualitaet.md).

**RAG in einem Satz:** Retrieval Augmented Generation heißt, dass ein Sprachmodell eine Frage nicht
aus dem Gedächtnis beantwortet, sondern zuerst passende Datensätze aus dem eigenen Bestand sucht
(Retrieval) und die Antwort dann aus diesen Fundstellen formuliert (Generation).

**Warum Datenqualität dort härter wirkt als in einem Bericht.** Ein Auswertungsfehler in Excel ist
sichtbar: die Zahl ist auffällig, die Spalte ist leer, jemand fragt nach. Ein RAG-System dagegen
formuliert aus dem, was es findet, eine flüssige Antwort — und die sieht bei einem lückenhaften
Bestand genauso überzeugend aus wie bei einem vollständigen. Der Fehler verschwindet nicht, er wird
unsichtbar. Zwei Wirkungswege sind zu trennen:

- **Retrieval:** Was falsch geschrieben, leer, unformatiert oder gar nicht vorhanden ist, wird nicht
  gefunden. Der Datensatz existiert, kommt aber in keiner Antwort vor.
- **Generation:** Was gefunden wird, gilt. Das Modell prüft die Fundstelle nicht auf Plausibilität,
  sondern formuliert sie um.

Der zweite Weg ist der gefährlichere, weil er aus einem Datenfehler eine Aussage macht.

## Vollständigkeit

| Code | Prüfung | Bedeutung für ein RAG-System |
|---|---|---|
| **V1** | Fehlende Werte je Spalte | Ein leeres Feld wird zu keinem Text und damit zu keinem Suchsignal, weshalb der Datensatz für genau die Frage unauffindbar bleibt, die dieses Merkmal betrifft. |
| **V2** | Platzhalter statt Inhalt | „k.A." und „siehe Lebenslauf" werden wie echter Inhalt eingebettet und vom Modell wie eine Aussage gelesen, sodass der Assistent Bewerber mit der Qualifikation „wird nachgereicht" vorschlägt. |
| **V3** | Zeilen mit mehreren Lücken | Datensätze mit vielen Lücken ergeben kurze, inhaltsarme Textstücke, die in der Vektorsuche fast überall mittelmäßig gut passen und dadurch bessere Treffer aus der Ergebnisliste verdrängen. |
| **V4** | Lücken in der laufenden Nummerierung | Was nicht in der Datei ist, ist auch nicht im Index, und das RAG-System antwortet vollständig und falsch, weil es das Fehlen nicht bemerken kann. |
| **V5** | Fehlende Ausprägungen gegenüber einer zweiten Datei | Ein Standort ohne einen einzigen Datensatz erzeugt die Antwort „dort gibt es keine passenden Bewerber", die wie ein Befund über den Arbeitsmarkt klingt und ein Befund über den Export ist. |

## Konsistenz

| Code | Prüfung | Bedeutung für ein RAG-System |
|---|---|---|
| **K1** | Exakte Dubletten | Identische Textstücke besetzen mehrere Plätze der Trefferliste und lassen eine einzelne Quelle wie eine mehrfach bestätigte aussehen, während der verdrängte Inhalt in der Antwort fehlt. |
| **K2** | Unscharfe Dubletten | Zwei Datensätze desselben Betriebs verteilen seine Historie auf zwei Fundstellen, sodass keine von beiden die vollständige Antwort enthält und das Modell den Rest ergänzt. |
| **K3** | Schreibvarianten desselben Werts | Metadatenfilter arbeiten exakt, weshalb „im pool" bei einer Filterung auf „Im Pool" herausfällt: der Datensatz ist vorhanden und für die Abfrage trotzdem unsichtbar. |
| **K4** | Schreibvarianten in Freitextfeldern | Elf Schreibweisen desselben Scheins zerlegen einen Begriff in elf schwache Signale, weshalb die Suche nach „Staplerschein" einen Teil der Geeigneten nicht findet, obwohl sie im Bestand stehen. |
| **K5** | Gemischte Schreibweisen bei Datum und Zahl | Ein Datum im abweichenden Format lässt sich nicht als Zahl vergleichen, weshalb jeder Zeitfilter wie „Eingang in den letzten zwölf Monaten" diese Zeilen stillschweigend fallen lässt. |
| **K6** | Mehrfach vergebene Nummern | Ist die Datensatznummer nicht eindeutig, zeigt der Quellenverweis der Antwort auf den falschen Datensatz, und die Nachprüfbarkeit bricht genau dort, wo sie gebraucht wird. |
| **K7** | Fachliche Regel (z. B. Besetzungen ≤ Anfragen) | Einen Widerspruch in den Zahlen erkennt das Modell nicht als Widerspruch, sondern formuliert ihn als Tatsache — aus 15 Besetzungen bei 13 Anfragen wird eine Quote von 115 Prozent in einer Entscheidungsvorlage. |

## Aktualität

| Code | Prüfung | Bedeutung für ein RAG-System |
|---|---|---|
| **A1** | Datumsfelder älter als die Schwelle | Der Assistent unterscheidet nicht zwischen „gilt" und „galt", weshalb ein zwei Jahre alter Verfügbarkeitsstand mit derselben Selbstsicherheit ausgegeben wird wie der von gestern. |
| **A2** | Datum in der Zukunft | Ein Zukunftsdatum steht bei jeder Sortierung nach Aktualität ganz oben und verdrängt damit ausgerechnet die tatsächlich aktuellen Datensätze aus der Trefferliste. |
| **A3** | Abgelaufene Fristen | Ein Profil mit abgelaufener Einwilligung darf nicht mehr verarbeitet werden, steht aber im Index — und jede Antwort, die es heranzieht, ist eine erneute Verarbeitung. |
| **A4** | Zeitliche Lücken in der Reihe | Fünf Wochen ohne einen einzigen Datensatz erzeugen im Index ein Loch, das das Modell nicht anzeigt, sondern mit den Nachbarzeiträumen plausibel überbrückt. |

## Genauigkeit

| Code | Prüfung | Bedeutung für ein RAG-System |
|---|---|---|
| **G1** | Zahlen außerhalb des plausiblen Bereichs | Ein Verrechnungssatz von 2,95 Euro wandert unverändert in eine Preisauskunft, weil ein Sprachmodell Zahlen nicht auf Plausibilität prüft, sondern wiedergibt. |
| **G2** | Postleitzahlen mit falscher Länge | Eine vierstellige Postleitzahl fällt aus jedem Regionalfilter, weshalb der Datensatz bei der Frage nach Bewerbern im Umkreis von Gera nicht auftaucht. |
| **G3** | Unbrauchbare E-Mail-Adressen | Die fehlerhafte Adresse landet in einem generierten Kontaktvorschlag, den niemand mehr prüft, weil er aus dem System kommt. |
| **G4** | Telefonnummern mit zu wenigen Ziffern | Eine zu kurze Rufnummer sieht im formulierten Text wie eine gültige aus, und der Fehler fällt erst der Person auf, die anruft. |
| **G5** | Unplausible Datumswerte | Ein Geburtsjahr 1938 im Bestand führt zu Antworten über verfügbare Fachkräfte, die weder faktisch noch arbeitsrechtlich verfügbar sind. |
| **G6** | Zeichensatzschäden | „PrÃ¤zisionsteile" wird anders eingebettet als „Präzisionsteile", weshalb der Datensatz bei der Suche nach dem korrekt geschriebenen Namen nicht gefunden wird. |
| **G7** | Überzählige Leerzeichen | Für jeden exakten Vergleich ist „ Beck" ein anderer Wert als „Beck", wodurch Dublettenerkennung, Filter und die Verknüpfung beider Dateien unbemerkt auseinanderlaufen. |

## Was daraus für die Reihenfolge folgt

Vier Folgerungen, alle `abgeleitet`, alle vor dem ersten Assistenten fällig:

1. **Werteliste und Pflichtfelder vor dem Modell.** K3 und K4 sind mit keinem Prompt zu heilen: was
   in elf Schreibweisen im Bestand steht, muss einmal vereinheitlicht und danach beim Erfassen
   erzwungen werden.
2. **Löschlauf vor dem Index.** A3 wird durch die Indexierung nicht besser, sondern schlimmer, weil
   jede Antwort eine weitere Verarbeitung ist — überfällige Profile gehören gelöscht, bevor sie
   eingebettet werden.
3. **Metadatenfilter brauchen saubere Werte.** Niederlassung, Status und Datum sind die drei Filter,
   mit denen ein Assistent überhaupt brauchbar wird; K3, K5 und G2 machen genau diese drei unzuverlässig.
4. **Quellenverweise brauchen eindeutige Nummern.** Ohne K6 und V4 gibt es keine belastbare
   Rückverfolgung — und ohne Rückverfolgung keine Antwort, die man einer Kundin oder einem
   Prüfer vorlegen kann.

## Grenzen dieser Prüfungen

Vier Punkte, die man beim Lesen des Berichts wissen muss:

- **Ein Befund ist kein Fehler.** V1 und A1 treffen auch Zeilen, in denen das Fehlen fachlich richtig
  ist: ein Interessent hat keinen Verrechnungssatz, ein inaktiver Kunde keine neue Anfrage. Der
  Bericht zählt, die Bewertung bleibt fachlich.
- **Ähnlichkeit findet Tippfehler, keine Synonyme.** K4 erkennt „Staplerscheim" neben
  „Staplerschein", aber nicht, dass „FFZ-Schein" und „Fahrerlaubnis Flurförderzeuge" dasselbe
  bezeichnen. Dafür braucht es eine gepflegte Werteliste, kein besseres Textmaß.
- **Dublettenerkennung ist eine Abwägung.** K2 verlangt zwei übereinstimmende Nebenfelder, sonst
  wären zwei Menschen mit demselben Namen eine Dublette. Die Bedingung kostet Trefferquote: eine
  echte Doppelbewerbung, die sich in allen anderen Feldern unterscheidet, findet das Skript nicht.
- **Was nicht als Spalte existiert, prüft kein Skript.** Fehlende Felder — eine Verfügbarkeit, eine
  Quelle, ein Grund der Nichtbesetzung — fallen nur auf, wenn man die Spaltenliste gegen die eigene
  Frage hält. Diese Prüfung bleibt Handarbeit, und sie ist die wertvollste.
