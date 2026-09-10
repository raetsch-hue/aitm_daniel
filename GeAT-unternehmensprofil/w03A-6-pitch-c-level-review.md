---
artefakt: Review des C-Level-Pitch, Fassung 1 — BLUF, Kürzung, Gates
kette: W03 A · KI-Analyse — Glied 6, Zwischenglied zwischen Fassung 1 und Fassung 2
baut_auf: w03A-6-pitch-c-level-fassung-1.md
basis_fuer: w03A-6-pitch-c-level.md (Fassung 2)
woche: 03
datum: 2026-09-10
status: eingearbeitet. Drei Befunde übernommen, vier Vorschläge abgewandelt — Begründung unten
zweck: die Fassung 1 auf ein sofortiges Go hin prüfen und den Umbau festhalten
herkunft: externes Review. Die Gegenprüfung in Abschnitt 3 ist eigene Einschätzung
---

# Review des Pitch, Fassung 1 — was das „Sofort" verhindert

> **Was diese Datei ist.** Das Review, das den Umbau von Fassung 1 auf Fassung 2 ausgelöst hat,
> plus die Prüfung, an welchen Stellen ich ihm **nicht** gefolgt bin und warum. Beide Teile gehören
> zusammen: ein Review ungeprüft zu übernehmen ist derselbe Fehler wie es zu ignorieren.

**Die Ausgangsfrage:** Wenn das Ziel nicht „eine gute Vorlage" ist, sondern **ein sofortiges Go**,
müssen WAS, WIE und WANN in den ersten 60 Sekunden stehen. Daran gemessen hat Fassung 1 drei
Schwachstellen.

---

## 1. Die drei Befunde

### 1.1 Das WAS kommt zu spät — erst in Minute 5
Fassung 1 startet mit dem Problem (Schatten-IT), erklärt dann drei Minuten Gewichtungsprozente
(25 % Compliance, 20 % Verfügbarkeit, 4 % RAG), und erst in Abschnitt 3 erfährt der Entscheider,
**was er beschließen soll.**

> **Die C-Level-Denkweise dahinter: BLUF — Bottom Line Up Front.** Ein Geschäftsführer muss in
> Sekunde 30 wissen, worum es geht. Sonst hört er den Rest mit der Frage im Hinterkopf: *„Worauf
> will er eigentlich hinaus?"*

### 1.2 Abschnitt 2 ist zu akademisch
Drei von neun Minuten für Gewichtungsprozente und Sensitivitätsanalysen.

> **Die C-Level-Realität: Dafür wurde die Rolle eingestellt.** Der Geschäftsführer will vertrauen,
> nicht Rechenschritte nachvollziehen.

Die Kurzform, die in **45 Sekunden** dasselbe leistet: *Vertex scheidet aus — keine Data
Scientists. Copilot scheidet aus — die Bewerberdaten liegen nicht in Microsoft 365. Übrig bleibt
eine EU-Plattform.*

### 1.3 Abschnitt 4 lädt zum Vertagen ein
Der Satz *„Ob eine Datenschutz-Folgenabschätzung nötig ist, weiß ich nicht — das muss der DSB
sagen"* **zwingt einen vorsichtigen Entscheider förmlich** zu der Antwort: *„Dann fragen Sie erst
den DSB, bevor wir Geld ausgeben."*

> **Die Lösung: aus Unwissenheit werden Gates.** Nicht „ich weiß es nicht", sondern eine
> **bedingte Freigabe** — heute beschlossen, unter der aufschiebenden Bedingung, dass der DSB
> zustimmt.

---

## 2. Der vorgeschlagene Umbau

**Die ersten 90 Sekunden:**

| Zeit | Inhalt |
|---|---|
| **0:00–0:45** | **BLUF: WAS & WARUM** — die Summe, das Haftungsrisiko, die neun Konten, die Freigabegrenze |
| **0:45–1:30** | **WIE** — 10 Stunden IT, kein Entwicklungsaufwand, keine Schnittstelle, migrationsfest; warum die Alternativen scheitern |
| **1:30–2:15** | **WANN + Abbruchkriterium** — Start nächste Woche, hartes Kriterium nach 90 Tagen |

**Die offenen Punkte als Go/No-Go-Gates statt als Zweifel:**

| Statt zu sagen | Sag lieber |
|---|---|
| „Ob eine DSFA nötig ist, weiß ich nicht." | **Gate 1:** Bevor der erste Mitarbeiter eingeloggt wird, liegt die schriftliche Freigabe des DSB auf dem Tisch. Gibt er sie nicht, fließt kein Euro |
| „Ich weiß nicht, wie weit die Ausschreibung ist." | **Zweitbeschluss:** Ich brauche heute den Auftrag an die IT-Leitung, die drei KI-Anforderungen ins Migrations-Lastenheft aufzunehmen, falls es noch offen ist |
| „Ich habe den Einführungsaufwand nicht beziffert." | **Einführungsrisiko:** Wir nutzen das bestehende Champions-Prinzip der neun Kollegen. Die schulen ihre Teams, nicht externe Berater |

**Der vorgeschlagene Ablauf:** Minute 1–2 WAS/WIE/WANN plus Schatten-IT-Schock · Minute 3–4 warum
die Alternativen scheitern und die Lehre aus 2023 · Minute 5–6 die drei Bedingungen · Minute 7 der
Beschlussantrag.

---

## 3. Gegenprüfung — vier Punkte, denen ich nicht gefolgt bin

*Einschätzung, bestreitbar. Alle vier betreffen Stellen, an denen der Umbau den Pitch angreifbarer
machen würde als Fassung 1.*

### 3.1 „Sie haben null Risiko" — nicht übernommen
Der Satz ist die stärkste Formulierung des Reviews und die einzige, die den Pitch **kippen** kann.
Fassung 1 nennt selbst vier offene Punkte, darunter einen, der die Empfehlung umdrehen würde
(unbezifferter Einführungsaufwand). Wer vor einer Geschäftsführung, die 2023 95.000 Euro für ein
Modul mit 34 Prozent Nutzung ausgegeben hat, „null Risiko" sagt, bekommt genau diese Akte zurück.
**Übernommen wird die Absicht, nicht der Satz:** *„Ihr Risiko ist auf 9.000 Euro und ein Quartal
begrenzt."* Das ist nachweisbar und leistet dasselbe.

### 3.2 Die Nullvariante darf im Kurzteil nicht wegfallen
Die 45-Sekunden-Fassung lässt beide Optionen weg, die Fassung 1 selbst hinzugefügt hat: die
KI-Funktionen des künftigen Kernsystems — und **nichts tun**. Die Nullvariante ist in der
Bewertung für die nächste Stufe die **zweitbeste** Option, besser als jedes geprüfte KI-Produkt.
*„Warum tun wir nicht einfach nichts?"* ist die erste Frage eines vorsichtigen Entscheiders. Wer
sie nicht selbst beantwortet, verliert die Minute, die er vorher gespart hat. **Sie bleibt — als
ein Satz.**

### 3.3 Sensitivität kürzen, nicht streichen
Das Ergebnis der Sensitivitätsprobe ist kein Rechenschritt, sondern der **einzige Punkt, an dem
der Vortragende benennt, unter welcher Bedingung er falsch liegt** (Adoptionsgewicht über
31 Prozent → Copilot wäre richtig). Genau das erzeugt bei einem skeptischen Gremium Vertrauen, und
es ist die Umsetzung der Regel aus Coursebook 3.4: *eine Empfehlung ohne benannte Gegenposition ist
eine Meinung.* **Ein Satz statt einer Minute — aber nicht null.**

### 3.4 Die 185.000 Euro gehören nicht in die BLUF
Im Review stehen sie als *„freier Spielraum: 185.000 € vorhanden"*. In Sekunde 40 löst dieser Satz
eine von zwei Reaktionen aus: *„dann nehmen Sie doch mehr"* oder *„dann ist es offenbar nicht
dringend"*. In Fassung 1 hatte die Zahl eine andere Funktion — sie **korrigierte** eine im Haus
umlaufende Zahl (280.000) nach unten und war damit ein Glaubwürdigkeitsbeleg. **Diese Funktion
bleibt, der Ort wechselt:** nicht in die BLUF, sondern in den WIE-Teil.

---

## 4. Was übernommen wurde

| Befund | Status |
|---|---|
| BLUF: WAS, WIE, WANN in den ersten 90 Sekunden | **übernommen**, Abschnitt 1 der Fassung 2 |
| Abschnitt 2 von 3 Minuten auf ~60 Sekunden | **übernommen** — mit Nullvariante und Kippschwelle als je einem Satz ([3.2](#31-sie-haben-null-risiko--nicht-übernommen), [3.3](#33-sensitivität-kürzen-nicht-streichen)) |
| Offene Punkte als Gates statt als Zweifel | **übernommen**, drei Gates in Abschnitt 4 |
| Zweitbeschluss zur Migrationsausschreibung | **übernommen** — die stärkste Einzelidee des Reviews: aus einer Frage, die der Vortragende nicht beantworten kann, wird ein Auftrag, den nur das Gremium erteilen kann |
| Champions-Prinzip gegen das Einführungsrisiko | **übernommen**, aber ohne die Beziffungslücke zu verdecken |
| „Sie haben null Risiko" | **abgewandelt** ([3.1](#31-sie-haben-null-risiko--nicht-übernommen)) |
| 185.000 € in der BLUF | **verschoben** ([3.4](#34-die-185000-euro-gehören-nicht-in-die-bluf)) |

**Und eine Präzisierung:** Das Review schreibt *„seit Monaten"* über die privaten KI-Konten. Belegt
ist **etwa ein Jahr**. Die längere Dauer ist das stärkere Argument — sie bleibt.
