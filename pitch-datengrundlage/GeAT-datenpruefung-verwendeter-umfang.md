---
artefakt: GeAT — Datenqualitätsprüfung, verwendeter Umfang
typ: DATENSATZ · Auszug, kein Bestandteil des Unternehmensprofils
quelle: GeAT-unternehmensprofil/daten/ — Prüfskript, Auflösung, Korrekturdokumentation
datum: 2026-09-11
umfang: ausschließlich das, was tatsächlich in die Plattformentscheidung eingegangen ist
regel: Was gemessen, aber nicht verwendet wurde, steht in Abschnitt 3 — als Bestand, nicht als Beleg
---

# GeAT — Datenqualitätsprüfung, verwendeter Umfang

> **Warum dieser Auszug getrennt geführt wird.** Die Prüfung ist erheblich umfangreicher als das, was in die Plattformentscheidung eingeflossen ist. **Aufgenommen ist hier nur der verwendete Teil.** Alles Übrige ist in [Abschnitt 3](#3--gemessen-aber-nicht-verwendet) benannt, damit ein Dritter weiß, dass es existiert — ohne dass es als Begründung erscheint, die es nie war.
>
> **Die Prüfung ist maschinell erfolgt**, über ein Prüfskript mit 24 Einzelprüfungen gegen zwei Bestände. Sie ist reproduzierbar.

---

## 1 · Was verwendet wurde

**Genau eine Messung**, und sie trägt in der Entscheidung eine tragende Aussage:

| Messung | Wert | Datum |
|---|---|---|
| Profile mit nachweispflichtigem Schein | **437 von 1.473** | gemessen **2026-09-10** |
| davon mit Gültigkeitsdatum im Datenmodell | **keines** | — |

> **Wofür sie gebraucht wird.** Sie belegt, dass die Grenze nicht bei der Datenqualität liegt, sondern beim **Datenmodell**: Es gibt kein Feld für die Gültigkeit eines Qualifikationsnachweises. Das lässt sich nicht durch bessere Pflege beheben, sondern nur durch eine Änderung am Zielsystem — und genau das begründet, warum die Anforderung **vor** der Migrationsausschreibung formuliert werden muss und nicht danach.
>
> **Und es ist die einzige Zahl im ganzen Vorhaben, die weder `angenommen` noch `gerechnet` ist, sondern gemessen.** Das macht sie im Gremium besonders belastbar — und es lohnt, sie als solche zu kennzeichnen.

**Das Mengengerüst dazu**, weil die 1.473 sonst nicht einzuordnen sind:

| Bestand | Ausgangszustand | Nach Bereinigung |
|---|---:|---:|
| Bewerberdatenbank | 1.284 Zeilen, 14 Spalten | **1.473 Zeilen, 16 Spalten** |
| Kundendatenbank | 1.040 Zeilen, 15 Spalten | 1.078 Zeilen, 17 Spalten |

> **Warum die korrigierte Fassung mehr Zeilen hat.** Sie ist **keine Zeile-für-Zeile-Reparatur**: Neben behobenen Einzelfehlern sind fehlende Datensätze ergänzt und Spalten hinzugefügt worden, die es vorher nicht gab. Wer die Dateien gegeneinanderstellt, vergleicht deshalb nicht zwei Fassungen derselben Menge. Die Nummern der übernommenen Datensätze sind stabil geblieben.
>
> **Die 437 sind am Zielzustand gemessen**, also am bereinigten Bestand von 1.473. Das ist der strengere Fall: Selbst nach der Bereinigung fehlt das Gültigkeitsdatum vollständig.

---

## 2 · Was daraus im Pitch steht

| Ort | Verwendung |
|---|---|
| **Datenblatt**, Abschnitt 4 „Datenbestand" | die Messung als Zeile, mit Herkunft „gemessen am Übungsbestand" |
| **Entscheidungsvorlage** `w03A-5`, Abschnitt 3 | als Beleg für den Satz, dass in den ersten 90 Tagen **kein Besetzungsassistent** gebaut wird — dafür fehlt die Datengrundlage, und das ist eine Feststellung, keine Vorsichtsmaßnahme |
| **Präsentation** | **kommt nicht vor.** Die Messung ist zu fein für 14 Folien; sie trägt die Vorlage, nicht den Vortrag |

> **Das ist eine bewusste Auslassung, keine Lücke.** Wer im Gremium nach der Datengrundlage gefragt wird, hat die Zahl parat — auf der Folie würde sie Platz kosten und nichts entscheiden.

---

## 3 · Gemessen, aber nicht verwendet

**Diese Werte existieren und sind belastbar. Sie sind in die Plattformentscheidung nicht eingegangen** und stehen hier nur, damit niemand sie später für unterschlagen hält.

| Befund | Wert |
|---|---|
| Zeilen mit Befund, Ausgangsbestand | **6,15 %** (Bewerber) · **5,48 %** (Kunden) |
| Zeilen mit Befund, Zielzustand | **0,68 %** (Bewerber) · 33,40 % (Kunden) — letztere ausschließlich aus der Aktualitätsprüfung A1 |
| Prüfungen ohne Treffer | vorher 15 bzw. 14 von 24 · nachher **23 von 24** in beiden Beständen |
| Fehlerinstanzen je Kategorie | Bewerber: Vollständigkeit 20 · Konsistenz 23 · Aktualität 16 · Genauigkeit 20 |
| | Kunden: Vollständigkeit 15 · Konsistenz 18 · Aktualität 12 · Genauigkeit 12 |
| Einzelfehlerlisten, Prüfrezepte, Reproduktionsanleitung | vollständig vorhanden in `GeAT-unternehmensprofil/daten/` |

> **Warum sie nicht verwendet wurden.** Die Fehlerquoten beschreiben einen **Übungsbestand**, nicht den Produktivbestand von 41.000 Profilen. Sie auf die Plattformentscheidung zu beziehen, hieße von 1.284 Zeilen auf 41.000 zu schließen — und genau das ist nicht zulässig. Die Messung aus [Abschnitt 1](#1--was-verwendet-wurde) ist anders gelagert: Sie betrifft das **Datenmodell**, und ein fehlendes Feld fehlt unabhängig von der Bestandsgröße.
>
> **Wer die Quoten trotzdem verwenden will**, muss den Übertrag begründen — und sollte wissen, dass ihn ein aufmerksames Gremium als Ersten angreift.

---

## 4 · Was die Prüfung nicht hergibt

- **Keine Aussage über den Produktivbestand.** Geprüft wurden zwei erzeugte Übungsbestände, nicht die 41.000 Profile.
- **Keine Aussage über Repräsentativität.** Die Fehler wurden eingebaut, nicht gefunden — die Verteilung ist eine Setzung (Ziehung ohne Schichtung, fester Startwert).
- **Keine Aussage über Ursachen.** Die Prüfung misst Zustände, nicht wie sie entstanden sind.
