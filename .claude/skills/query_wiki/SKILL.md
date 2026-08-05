---
name: query_wiki
description: Fragen aus dem Wiki beantworten — Seiten über index.md finden, Antwort mit Belegen bis zur Originalquelle synthetisieren, Lücken und Konflikte benennen, wertvolle Antworten ins Wiki zurückschreiben. Nutze diesen Skill für jede inhaltliche Frage zu Abrechnung, Positionen, Werkstoffen oder Verfahren — auch wenn nicht ausdrücklich nach dem Wiki gefragt wird.
---

# Query

Beantworte aus dem Wiki: $ARGUMENTS

## 1. Suchen

Lies `index.md` und wähle daraus die einschlägigen Seiten, dann lies diese vollständig — nicht nur den Treffer-Absatz. Der Nachbarkontext auf einer Seite entscheidet oft, ob eine Aussage überhaupt für den Fall gilt.

Folge von dort den Querverweisen. Antworten zur Abrechnung hängen fast immer an mehr als einer Seite: Position, Leistungsinhalt, Ausschlüsse, Kombinierbarkeit.

Suche auch unter Synonymen, Abkürzungen und den `aliase`-Einträgen im Frontmatter. Wer nach "Modellgussbasis" fragt, meint die Seite "Modellguss-Basis". Bringt der Index nichts, grepe über `wiki/`, bevor du eine Lücke meldest.

## 2. Antwort bilden

Trenne sichtbar, was belegt ist, von dem, was du erschließt:

- **Belegt** — steht so auf einer Wiki-Seite, die ihrerseits eine Quelle nennt.
- **Abgeleitet** — ergibt sich aus der Kombination mehrerer Seiten. Kennzeichne das und schreibe dazu, aus welchen Seiten. Hier entstehen die Fehler, und bei Abrechnungsfragen kosten sie Geld.

Belegformat: Wiki-Seite und Originalquelle, z. B. `→ [Modellguss-Basis](wiki/modellguss-basis.md), BEL II Nr. 001 0`. Ohne die Originalquelle ist die Antwort nicht prüfbar, ohne die Wiki-Seite nicht weiterverfolgbar.

**Konflikte** stehen im Wiki bewusst offen. Trägst du auf einen, gibst du beide Aussagen mit ihren Quellen wieder und entscheidest nicht selbst.

**Alter prüfen.** Vergleiche das `stand:`-Feld der genutzten Seiten mit der Frage. Bei Regelwerken, die jährlich fortgeschrieben werden, weise auf den Stand hin.

**Tagesaktuelle Zahlen** stehen absichtlich nicht im Wiki. Fragt jemand nach Preisen oder aktuellen Beträgen, verweist du auf die hinterlegte Quelle in `raw/`, statt eine Lücke zu melden.

## 3. Wenn das Wiki es nicht hergibt

Suche liefert immer Treffer. Dass Seiten gefunden wurden, heißt nicht, dass die Antwort darin steht. Prüfe vor dem Schreiben: Beantwortet eine konkrete Aussage auf einer dieser Seiten die Frage — oder klingt das Gefundene nur ähnlich?

Im Zweifel: "Das Wiki beantwortet das nicht." Dann nennst du, welche Quelle eingepflegt werden müsste, und wenn möglich, wo sie zu finden ist. Nie raten, nie aus schwach passenden Treffern synthetisieren.

Eine solche Antwort wird nie ins Wiki zurückgeschrieben — sonst wird die Vermutung beim nächsten Mal zur Quelle.

Teilantworten sind der Normalfall: Beantworte, was gedeckt ist, und benenne die Lücke genau, statt beides zu vermischen.

## 4. Zurückschreiben

Antworten, die echte Synthese enthalten — ein Vergleich, eine Ableitung über mehrere Seiten, ein Zusammenhang, den vorher niemand aufgeschrieben hatte — gehören ins Wiki, sonst verschwinden sie im Chatverlauf und werden beim nächsten Mal neu erarbeitet.

Zurückgeschrieben wird, was belegt ist und über eine Einzelseite hinausgeht. Nicht zurückgeschrieben wird das reine Vorlesen einer vorhandenen Seite, Abgeleitetes ohne tragende Belege und alles aus Abschnitt 3.

Beim Zurückschreiben gelten dieselben Regeln wie beim Ingest: Frontmatter mit Labels und Quellen, Belege im Text, Rückverlinkung von den beteiligten Seiten, Eintrag in `index.md` und in `log.md` mit Präfix `## [Datum] query | Titel`.

## 5. Form

Prosa als Standard. Tabelle, wenn mehrere Positionen gegen dieselben Kriterien verglichen werden. Die Antwort ist so lang wie nötig — bei einer Ja/Nein-Frage zur Abrechenbarkeit sind zwei Sätze und ein Beleg die vollständige Antwort.