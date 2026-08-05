---
name: lint_wiki
description: Health-Check des Wikis — findet Widersprüche, veraltete und unbelegte Aussagen, verwaiste Seiten, fehlende Querverweise, Duplikate und Wissenslücken. Mechanische Mängel werden direkt behoben, inhaltliche Eingriffe vorgelegt. Nutze diesen Skill immer, wenn es um Wiki-Pflege, Aufräumen, Konsistenz- oder Gesundheitsprüfung des Wikis geht — auch wenn das Wort "lint" nicht fällt.
---

# Lint

Ein Lint-Lauf ist eine Gesundheitsprüfung, kein Umbau. Er hält das Wiki konsistent, während es wächst.

Grundregel: Was mechanisch und umkehrbar ist, behebst du selbst. Was Bedeutung verändert — Widersprüche auflösen, Aussagen löschen, Seiten zusammenführen — legst du vor. Ein Lauf, der still Inhalte umschreibt, erzeugt genau die Drift, die er verhindern soll: Niemand merkt, dass eine Entscheidung getroffen wurde, und das Ergebnis wird beim nächsten Lauf zur Grundlage.

## 1. Umfang festlegen

Ohne Angabe: alle Seiten, die seit dem letzten `lint`-Eintrag in `LOG.md` geändert wurden, plus deren direkte Nachbarn (verlinkte und verlinkende Seiten). Dort haben frische Ingests Drift erzeugt.

Den letzten Lauf findest du mit `grep "^## \[" LOG.md | grep lint | tail -1`.

Ein vollständiger Lauf über das ganze Wiki nur auf ausdrückliche Ansage. Bei größeren Wikis lieber nach Themencluster als alles auf einmal — ein Lauf, der zu viel umfasst, wird oberflächlich.

## 2. Prüfen (nur lesen)

Sammle erst alle Befunde, ohne etwas zu ändern. Danach entscheidest du, was davon behoben und was vorgelegt wird.

| Befund | Woran erkennbar |
|---|---|
| Widerspruch | Zwei Seiten sagen Unvereinbares über denselben Sachverhalt |
| veraltete Aussage | Eine neuere Quelle in `raw/` überholt, was auf der Seite steht |
| unbelegte Aussage | Behauptung ohne Verweis auf eine Quelle in `raw/` |
| verwaiste Seite | Keine eingehenden Links |
| fehlender Querverweis | Eine Seite nennt ein Konzept mit eigener Seite, verlinkt aber nicht dorthin |
| fehlende Seite | Ein Konzept wird auf mehreren Seiten miterklärt, hat aber keine eigene Seite |
| Duplikat | Derselbe Sachverhalt an mehreren Stellen ausgeschrieben statt verlinkt |
| Lücke | Eine Frage, die das Wiki naheliegend beantworten sollte, aber nicht kann |
| Stilverstoß | siehe Abschnitt 6 |

Klärungsgrundlage ist immer `raw/`. Findet sich dort kein Beleg für eine Aussage, lautet der Befund "unbelegt" — nicht "stimmt". Wiki-Seiten belegen einander nicht gegenseitig, sonst zementiert sich ein früherer Fehler.

## 3. Direkt beheben

Diese Eingriffe ändern keine Aussage und sind leicht rückgängig zu machen:

- fehlende Querverweise ergänzen
- verwaiste Seiten von passenden Stellen aus verlinken
- Stilverstöße korrigieren
- kaputte Links, falsche Seitentitel, uneinheitliche Benennung

## 4. Vorlegen statt ausführen

Bei diesen Befunden beschreibst du das Problem, deine Empfehlung und die Belege aus `raw/` — und wartest auf Entscheidung:

- **Widerspruch.** Beide Formulierungen zitieren, die Quellenlage je Seite nennen, sagen welche du für richtig hältst und warum. Wenn `raw/` die Frage nicht entscheidet, ist das selbst das Ergebnis: dann bleibt der Widerspruch als offene Frage auf beiden Seiten vermerkt.
- **Unbelegte Aussage.** Nicht löschen. Als unbelegt markieren und vorlegen — eine Aussage ohne Beleg kann trotzdem stimmen und wertvoll sein, die Quelle wurde vielleicht nur nie eingepflegt.
- **Seiten zusammenführen.** Siehe Abschnitt 5.
- **Neue Seite anlegen.** Vorschlagen, mit Begründung, welche bestehenden Seiten dann dorthin verlinken würden.

## 5. Redundanz, aber ohne Informationsverlust

Redundanz beseitigen heißt: eine Tatsache steht an genau einer Stelle, alles andere verlinkt dorthin. Es heißt nicht, Text zu kürzen. Wortzahl ist kein Ziel — ein Wiki, das Information verliert, um kürzer zu werden, hat seinen Zweck verfehlt. Du entfernst die zweite Ausformulierung, nicht den zweiten Gedanken.

Zusammenführen nur bei echtem Duplikat: Übersetzung, Abkürzung, Synonym, dieselbe Sache anders benannt. Nicht bei verwandten Themen, nicht bei Eltern-Kind-Beziehungen. Im Zweifel getrennt lassen und verlinken — eine falsch zusammengeführte Seite kostet mehr Arbeit als ein fehlender Link.

## 6. Lücken und offene Fragen

Recherchiere Lücken im Web, aber schreibe das Ergebnis nicht direkt ins Wiki. Was du findest, gehört zuerst als Quelle nach `raw/`, dann wird daraus eine Wiki-Aussage mit Verweis. Andernfalls erzeugt der Lauf genau den Befund, den er beseitigen soll — Aussagen ohne Beleg —, und die Quellenschicht verliert ihre Rolle als einzige Grundlage.

Am Ende jedes Laufs: 2–5 offene Fragen nennen, die sich aus den Befunden ergeben, und Quellen, deren Suche sich lohnen würde. Das ist oft der wertvollste Teil — Lücken sieht man erst, wenn das Vorhandene geordnet ist.

## 7. Stil

- Neutral und deklarativ.
- Kurze Sätze, ein Gedanke pro Satz.
- Die Modelle, die das Wiki lesen, folgen Anweisungen zuverlässig; sie brauchen keine rhetorische Betonung. Fettung und Symbole nur, wo echte Struktur ist: Tabellen, Kennzahlen, Formeln.
- Keine Ausrufezeichen, keine Emoji, keine Cliffhanger, keine Anmoderation ("In diesem Abschnitt betrachten wir…"). Die Seite beginnt mit dem Inhalt.

## 8. Protokollieren

Ein Eintrag pro Lauf, nicht pro Korrektur — sonst ertrinkt `LOG.md` und die Zeitleiste wird unlesbar.

```
## [2026-08-05] lint | Themencluster Retrieval
Geprüft: 23 Seiten (seit letztem Lauf geändert + Nachbarn)
Behoben: 6 Querverweise, 2 verwaiste Seiten verlinkt, 4 Stilkorrekturen
Vorgelegt: Widerspruch bm25-scoring/hybrid-search (Recall-Zahl); Zusammenführung reranking + cross-encoder
Offen: Woher stammt die 84,8-%-Angabe auf evaluation.md? Quelle zu Chunk-Größen fehlt.
```

Vorgelegte Punkte trägst du erst nach der Entscheidung als behoben nach. Befunde, die bewusst so bleiben sollen, hältst du ebenfalls fest — sonst meldet sie der nächste Lauf erneut.