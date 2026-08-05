---
name: ingest_to_wiki
description: Neue Quellen aus raw/_inbox/ ins Wiki einarbeiten — lesen, in Wissensseiten zerlegen, Positionen und Kanten setzen, mit dem Bestand verknüpfen, INDEX.md und LOG.md nachziehen. Nutze diesen Skill immer, wenn eine neue Quelle, ein Dokument, ein Katalog oder ein Rundschreiben ins Wiki soll — auch wenn das Wort "ingest" nicht fällt.
---

# Ingest

Verarbeite $ARGUMENTS (ohne Argument: alles in `raw/_inbox/`), eine Quelle nach der anderen. Jede Quelle vollständig abschließen — inklusive INDEX, LOG und Verschieben — bevor die nächste beginnt. Sonst entstehen Seiten ohne Index-Eintrag, und der nächste Lauf erkennt nicht, was schon da ist.

Schichten:

- `raw/` — unveränderlich, nur lesen
- `kataloge/*.json` — Positionslisten, werden nicht ins Wiki abgeschrieben. Benennung `<präfix>[_<label>]_<jahr>[_v<n>].json`, also `bel_2026_v1.json` → Präfix `bel`, Fassung 2026 v1. Fassungen liegen nebeneinander, die höchste ist die aktive; `graph.py` prüft gegen sie und weist die Vorgängerdatei als Diff-Grundlage aus
- `wiki/` — gehört dir
- `wiki/GRAPH.md` — abgeleitet, erzeugt von `scripts/graph.py`
- `vorlagen/` — eigene Schicht, wird **nicht** ins Wiki ingestiert. Vorlagen sind Kompositionen (angewandte Regeln je Falltyp), kein Regelwissen; das Kürzel je Zeile trägt der Tabellen-Spaltenkopf (`BEB97`, `BEL`), die Katalog-Herkunft samt Fassung das Frontmatter (`kataloge: [bel_2026_v1.json]`). Verbindung zum Wiki über `vorlagen/_REGISTER.md` (abgeleitet, Position → Vorlagen) und die Graph-Befunde. Regelwissen, das in Vorlagen-Bemerkungen wiederkehrt, gehört einmal ins Wiki, nicht 200-mal in die Vorlagen.

## 1. Orientieren

`INDEX.md` lesen (welche Seiten gibt es) und `GRAPH.md` (welche Position hat eine zuständige Seite). Ohne das entstehen Dubletten unter anderem Namen.

## 2. Lesen und gliedern

Quelle vollständig lesen, bevor du schreibst. Aussagen einordnen:

- **abrechnungsrelevant** — Positionsnummern, Leistungsinhalte, Bedingungen, Ausschlüsse, Kombinierbarkeit
- **fachlich einordnend** — Werkstoffe, Herstellungsschritte, Begriffe

Festhalten, was schon existiert, was neu entsteht, was zu aktualisieren ist. Gliederung vorlegen bei der ersten Quelle eines Laufs und bei unklarem Zuschnitt.

Ist die Quelle eine **neue Fassung eines Regelwerks, das schon im Wiki steht**, gilt Abschnitt 11 statt der Abschnitte 3 bis 9.

Patientendaten, Fallnummern und andere personenbezogene Angaben kommen nicht ins Wiki.

## 3. Seiten schreiben

**Schnitt.** Eine Seite pro Ding, auf das andere Seiten verlinken werden — nicht eine Seite pro Kapitel der Quelle. Die Seitenzahl folgt aus dem Inhalt. Ein Ingest berührt mehr bestehende Seiten, als er neue anlegt; ist es umgekehrt, hast du an Vorhandenem vorbeigeschrieben.

**Benennung.** Fachbegriff, Singular, wie in der Quelle. Synonyme und Abkürzungen als `aliase`, nie als eigene Seite.

**Belege.** Quellen im Frontmatter, Fundstelle in Klammern am Satzende: `(BEL II, Nr. 201 0)`. Positionsnummern, Beträge und Leistungsbeschreibungen exakt zitieren — Umformulieren ist hier ein Fehler.

**Stil.** Neutral, deklarativ, kurze Sätze. Fettung und Symbole nur bei echter Struktur: Tabellen, Kennzahlen, Formeln. Keine Ausrufezeichen, keine Emoji, keine Anmoderation.

**Nicht ins Wiki:**

- Was anderswo schon steht — verlinken statt neu ausschreiben
- Katalogtabellen. Nur die Konsequenz aufschreiben, auf den Katalog verlinken
- Zahlen mit Ablaufdatum. Ausnahme: reine Jahrgangsseiten mit `gueltig_von`/`gueltig_bis`
- BEB-Preise. Der BEB kennt nur Minutenwerte; der Preis ist laborspezifisch und wäre auf einer Wissensseite für alle anderen Kunden falsch
- Prozess-Metadaten des Ingests — die gehören auf die Quellseite

## 4. Positionen

Format `katalog:nummer`, also `bel:2010`. Im Fließtext bleibt die Schreibweise der Quelle (`201 0`).

Das Präfix ist Pflicht: 135 der 175 BEL-Nummern kommen im BEB97 mit anderer Bedeutung vor. Ohne Präfix sähe eine Kante richtig aus und der Kostenvoranschlag wäre falsch.

Neue Kataloge vor dem Ingest in `KATALOGE` in `scripts/graph.py` eintragen. Das Skript prüft jede ID gegen die aktive Fassung des Katalogs.

Jede Position hat **höchstens eine** zuständige Seite — die mit ihrer Regel. Vollabdeckung ist kein Ziel: BEB97 hat 1103 Positionen, die meisten tragen nur Name und Minutenwert und bekommen keine Seite.

## 5. Kanten

| Typ | Bedeutung | Katalog |
|---|---|---|
| `schliesst_aus` | A ist neben B nicht abrechenbar | innerhalb |
| `enthalten_in` | A ist Bestandteil von B | innerhalb |
| `alternativ_zu` | A und B decken denselben Zweck, nur eines je Bezugsgröße | innerhalb |
| `ersetzt_durch_bei` | statt A ist unter einer Bedingung B abzurechnen | innerhalb |
| `entspricht` | A deckt dieselbe Leistung wie B im anderen Katalog | übergreifend |

Format: `Position | Gegenposition | Geltung | Seite-mit-Prosa`.

- Nur setzen, wenn die Beziehung in der Quelle ausgesprochen ist. „Hängt thematisch zusammen" ist ein `[[Link]]`, keine Kante.
- **Geltung ist Pflicht** — „derselbe Zahn", „dasselbe Modellpaar", „immer". Ohne sie wird aus einem bedingten Ausschluss ein absoluter.
- Ausschlüsse über Katalogränder sind ein Fehler. Nur `entspricht` verbindet Kataloge; `entspricht` innerhalb eines Katalogs ist falsch, dafür ist `alternativ_zu` da.
- `alternativ_zu` mitsetzen, wo die Quelle Alternativen benennt. Ohne diese Kante sieht ein Paar wie 0310/0320 bei jeder Prüfung wie ein Verstoß aus — im Test gegen die 289 Vorlagen entstanden so 162 falsche Treffer.
- Ist eine `entspricht`-Zuordnung nicht 1:1, gehört das in die Geltung (`zusammen mit bebzt:xxxx`), nicht in mehrere unabhängige Kanten. Sonst geht bei einer Umschreibung eine Position verloren.
- Fehlt ein Äquivalent, ist das eine Aussage, keine Lücke — sonst verschwindet die Position stillschweigend und der Kostenvoranschlag wird zu billig. Begründung ist Pflicht.

## 6. Frontmatter

```yaml
---
titel: BEL-Gruppe Modellguss
aliase: [Modellguss, Metallbasis]
labels: [Abrechnung, BEL, Herstellung]
positionen: [bel:2010, bel:2021, bel:2026, bel:2050]
quellen: [raw/BEL_II_01_01_2022.pdf]
stand: 2026-08-05
gueltig_von: 2022-01-01
gueltig_bis:
schliesst_aus:
  - "bel:2010 | bel:8060 | immer | nebeneinander-ausschluesse-bel"
enthalten_in:
  - "bel:2026 | bel:2050 | Ney-Stiel ist Bestandteil der Bonwillklammer | nebeneinander-ausschluesse-bel"
entspricht:
  - "bel:2010 | beb97:0801 | 1:1 | beb97-modellguss"
kein_aequivalent:
  - "bel:2120 | beb97 | Zuschlag existiert dort nicht"
---
```

`stand` = Bearbeitungsdatum, `gueltig_von`/`gueltig_bis` = Geltungszeitraum des Regelwerks. Bei Abrechnung ist „was galt zum Leistungsdatum" die häufigere Frage.

Labels: `Abrechnung`, `BEB97`, `BEBZT`, `BEL`, `Herstellung`, `Material`, `Preise`, `Regulatorik`, `Quelle`. Ein neues Label lohnt ab absehbar 5–10 Seiten.

## 7. Verbinden

Links von den bestehenden Seiten ergänzen, die das neue Konzept erwähnen. Dann `python3 scripts/graph.py` und die Befunde beheben, bevor der Ingest als abgeschlossen gilt.

Die Textprüfung des Skripts erkennt nur `201 0` mit Leerzeichen. Bei BEB-Seiten trägt allein das Frontmatter die Wahrheit.

Widerspricht Neues dem Bestand: Konflikt auf beiden Seiten sichtbar machen, mit beiden Aussagen und Quellen. Ist die neue Quelle die jüngere Fassung derselben Regelung, zusätzlich `ersetzt_durch:` auf der alten und `ersetzt:` auf der neuen Seite. Der alte Wortlaut bleibt stehen — Altfälle brauchen ihn.

## 8. Quellseite

Titel, Herausgeber, Stand, Ablageort, zwei bis drei Sätze zum Inhalt, Liste der entstandenen Seiten, Prozess-Metadaten, und ein Abschnitt „Offene Punkte" mit den Regelwerken, auf die die Quelle verweist, ohne sie zu enthalten.

## 9. INDEX und LOG

`INDEX.md`, je neue und geänderte Seite:

| Seite | Inhalt | Meta |
|---|---|---|
| [BEL-Gruppe Modellguss](bel-gruppe-modellguss.md) | 201 0 – 212 0: Metallbasis, gegossene Halte- und Stützelemente, Klammerzuschlag | 2026-08-05 · BEL_II_01_01_2022.pdf |

Der Einzeiler ist das Suchfeld des nächsten Ingests. Er muss die Seite unterscheidbar machen, nicht den Titel wiederholen.

`LOG.md`, ein Eintrag je Quelle:

```
## [2026-08-05] ingest | BEL II, Stand 01.01.2022
7 neue Seiten, 12 bestehende um Querverweise ergänzt, 23 Kanten gesetzt.
Konflikt zur Kombinierbarkeit von 008 0 und 010 3 auf beiden Seiten vermerkt.
```

## 10. Quelle verschieben

Erst wenn alles steht, aus `raw/_inbox/` an ihren Platz unter `raw/`. Was im Inbox liegt, ist offen.

## 11. Neue Fassung eines bekannten Regelwerks

Der Ingest erzeugt hier keine Wissensseiten, sondern **eine Änderungsmatrix**. Angewendet wird sie vom Lint-Lauf.

**Leserichtung umdrehen.** Ein normaler Ingest liest von der Quelle ins Wiki und findet dabei Änderungen und Ergänzungen — aber nie ein Fehlen. Eine gestrichene Regel äußert sich in der neuen Fassung durch nichts. Deshalb gehst du zusätzlich rückwärts: jede Aussage der betroffenen Seiten gegen die neue Fassung prüfen. Schweigen ist ein Befund, keine Bestätigung.

**Zwei Herkünfte, beide nötig.**

- Katalog-Diff (Vorgängerfassung gegen aktive Fassung unter `kataloge/`): neu, entfallen, umbenannt. Deterministisch. Beide Dateien liegen nebeneinander, `GRAPH.md` benennt unter „Fassungen", welche welche ist. Fehlt die Vorgängerdatei, ist der Diff nicht zu haben — dann Abbruch und melden, statt die Matrix nur aus der Quelle zu bauen.
- Quelle (das PDF): geänderte Erläuterungen zur Abrechnung. Gleiche Nummer, gleicher Kurztext, andere Regel — das sieht kein Diff, und es sind meist die meisten Änderungen.

Eine Matrix nur aus dem Katalog sieht vollständig aus und ist inhaltlich blind. Je Zeile die Herkunft vermerken.

**Auslegung als solche kennzeichnen.** Dass 0021 entfällt und 0029 neu ist, sagt der Diff. Dass das eine das andere ersetzt, sagt nur die Quelle. Ohne Beleg lautet die Art `offen`, nicht `ersetzt_durch`.

**Format** — eine Wiki-Seite je Fassungswechsel:

```yaml
---
titel: Änderungsmatrix BEB97 2025 → 2026
labels: [Abrechnung, BEB97, Matrix]
quellen: [raw/beb97_2026.pdf, kataloge/beb97_zahniAI_2026_v1.json]
stand: 2026-08-05
von_fassung: 2025
nach_fassung: 2026
angewendet: nein
---
```

| alt | neu | Art | Herkunft | Beleg | Wirkung |
|---|---|---|---|---|---|
| beb97:0021 | beb97:0029 | ersetzt_durch | Quelle | BEB97 2026, Vorbem. Nr. 3 | 2 Seiten, 3 Kanten |
| — | beb97:0916 | neu | Katalog | — | — |
| beb97:0801 | — | entfallen | Katalog | — | 1 Seite, 1 Kante |
| beb97:0055 | beb97:0055 | regel_geaendert | Quelle | BEB97 2026, Nr. 0055 | 1 Seite |
| beb97:0051 | beb97:0051 | unveraendert_geprueft | Quelle | — | — |

Arten: `neu`, `entfallen`, `umbenannt`, `ersetzt_durch`, `regel_geaendert`, `unveraendert_geprueft`, `offen`.

`unveraendert_geprueft` gehört mit hinein. Sonst ist nicht unterscheidbar, was gleich geblieben ist und was niemand angesehen hat.

Die Spalte „Wirkung" füllst du aus `GRAPH.md` und `vorlagen/_REGISTER.md`: betroffene Seiten laut Positionsregister, betroffene Kanten laut Kantentabelle, betroffene Vorlagen laut Register.

**Danach.** Die neue Katalogdatei kommt als weitere Fassung unter `kataloge/` dazu, die abgelöste bleibt liegen — sie ist die Diff-Grundlage des nächsten Wechsels und der Beleg dafür, welche Fassung eine entfallene Position zuletzt kannte. Nie überschreiben, nie löschen. Danach `python3 scripts/graph.py`: die Tabelle „Fassungen" muss die neue Datei als aktiv und die alte als Vorgänger zeigen. Quellseite für die neue Fassung anlegen, die abgelöste bekommt `gueltig_bis`. Matrix in `INDEX.md` und `LOG.md` eintragen. `angewendet: nein` bleibt stehen — die Anwendung ist Sache des Lint-Laufs, und die Matrix wird vorher angesehen.