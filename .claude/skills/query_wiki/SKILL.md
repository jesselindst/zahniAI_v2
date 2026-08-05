---
name: query_wiki
description: Fragen aus dem Wiki beantworten — Seiten über INDEX.md und GRAPH.md finden, Antwort mit Belegen bis zur Originalquelle, Lücken und Konflikte benennen, wertvolle Antworten zurückschreiben. Nutze diesen Skill für jede inhaltliche Frage zu Abrechnung, Positionen, Werkstoffen oder Verfahren — auch wenn nicht ausdrücklich nach dem Wiki gefragt wird.
---

# Query

Beantworte aus dem Wiki: $ARGUMENTS

## 1. Graph erzeugen

`python3 scripts/graph.py`. Seit dem letzten Lauf können Seiten geändert worden sein; ein veraltetes Positionsregister ist bei einer Abrechnungsfrage teurer als gar keins.

## 2. Katalog klären

Eine nackte Positionsnummer ist mehrdeutig: `0021` ist im BEL Doublieren, im BEB97 ein Modell für Sägesegmente. 135 der 175 BEL-Nummern sind doppelt belegt.

Geht der Katalog aus der Frage nicht hervor, frag nach. Nicht raten, auch nicht nach Wahrscheinlichkeit. Steht er fest, nenne ihn in der Antwort — die Nummer allein trägt ihn nicht.

## 3. Suchen

- Konkrete Position: Positionsregister in `GRAPH.md`, dort steht sie als `bel:2010` mit zuständiger Seite. Keine Seite heißt nicht, dass es die Position nicht gibt — die meisten BEB-Positionen tragen keine Regel. Dann gibt der Rohkatalog unter `kataloge/` die Auskunft — die aktive Fassung, benannt in der Tabelle „Fassungen" in `GRAPH.md`. Eine ältere Fassung nur heranziehen, wenn nach dem Stand zu einem vergangenen Leistungsdatum gefragt ist; dann die Fassung in der Antwort nennen.
- Sonst über `INDEX.md`.
- Gefundene Seiten vollständig lesen, nicht nur den Treffer-Absatz. Der Nachbarkontext entscheidet oft, ob eine Aussage für den Fall gilt.
- Querverweisen und der Backlink-Tabelle folgen. Abrechnungsantworten hängen fast immer an mehreren Seiten: Position, Leistungsinhalt, Ausschlüsse, Kombinierbarkeit.
- Auch unter Synonymen, Abkürzungen und `aliase` suchen. Bringt beides nichts, über `wiki/` grepen, bevor du eine Lücke meldest.

## 4. Kanten benutzen

Kanten sagen, wo du nachsehen musst — sie sind kein Beleg. Bevor ein Ausschluss oder eine Alternative in die Antwort eingeht, liest du die Prosa auf der verwiesenen Seite.

Die Geltung im dritten Feld ist Teil der Regel. „Nicht nebeneinander abrechenbar für denselben Zahn" ist etwas anderes als „nicht nebeneinander abrechenbar". Fällt sie weg, ist die Antwort falsch.

Eine Kante ohne passende Prosa auf der Zielseite ist ein Lint-Befund, keine Grundlage.

Ableitungen bleiben innerhalb eines Regelwerks. Die einzige Brücke ist `entspricht` — und sie sagt nur, dass zwei Positionen dieselbe Leistung decken, nicht dass die Regeln des einen Katalogs im anderen gelten.

## 5. Antwort bilden

Sichtbar trennen:

- **Belegt** — steht so auf einer Wiki-Seite, die eine Quelle nennt
- **Abgeleitet** — aus mehreren Seiten kombiniert. Kennzeichnen und dazuschreiben, aus welchen. Hier entstehen die Fehler, und sie kosten Geld.

Belegformat: `→ [[bel-gruppe-modellguss]], BEL II Nr. 201 0`. Ohne Originalquelle nicht prüfbar, ohne Wiki-Seite nicht weiterverfolgbar.

**Konflikte** stehen im Wiki bewusst offen: beide Aussagen mit Quellen wiedergeben, nicht selbst entscheiden.

**Geltungszeitraum.** Bei einer Frage zu einem Leistungsdatum gegen `gueltig_von`/`gueltig_bis` prüfen. Bei `ersetzt_durch:` gilt für heutige Fälle die Nachfolgerin, für Altfälle die alte Seite.

**Tagesaktuelle Zahlen** stehen absichtlich nicht im Wiki. Auf die Quelle in `raw/` oder die Jahrgangsseite verweisen, statt eine Lücke zu melden.

## 6. Wenn das Wiki es nicht hergibt

Suche liefert immer Treffer. Prüfe vor dem Schreiben: Beantwortet eine konkrete Aussage die Frage — oder klingt das Gefundene nur ähnlich?

Im Zweifel: „Das Wiki beantwortet das nicht", plus welche Quelle eingepflegt werden müsste und wo sie zu finden ist. Nie raten, nie aus schwachen Treffern synthetisieren. Solche Antworten werden nie zurückgeschrieben — sonst wird die Vermutung beim nächsten Mal zur Quelle.

Teilantworten sind der Normalfall: beantworten, was gedeckt ist, und die Lücke genau benennen.

## 7. Zurückschreiben

Zurückgeschrieben wird, was belegt ist und über eine Einzelseite hinausgeht — ein Vergleich, eine Ableitung, ein neu entdeckter Zusammenhang. Nicht zurückgeschrieben wird das Vorlesen einer Seite, Abgeleitetes ohne tragende Belege und alles aus Abschnitt 6.

Die Begründung mitschreiben, nicht nur das Ergebnis: warum diese Auslegung, was dagegen sprach.

Es gelten die Ingest-Regeln: Frontmatter mit `labels`, `positionen`, `quellen`, `stand`, Belege im Text, Rückverlinkung, Eintrag in `INDEX.md` und `LOG.md` mit Präfix `## [Datum] query | Titel`. Danach `graph.py` und Befunde prüfen.

## 8. Form

Prosa als Standard, Tabelle beim Vergleich mehrerer Positionen gegen dieselben Kriterien. Bei einer Ja/Nein-Frage zur Abrechenbarkeit sind zwei Sätze und ein Beleg die vollständige Antwort.