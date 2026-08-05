---
name: lint_wiki
description: Health-Check des Wikis — findet Widersprüche, veraltete und unbelegte Aussagen, verwaiste Seiten, fehlende Querverweise und Kanten, doppelte Prosa. Mechanisches wird behoben, Inhaltliches vorgelegt. Nutze diesen Skill immer, wenn es um Wiki-Pflege, Aufräumen, Konsistenz- oder Gesundheitsprüfung geht — auch wenn das Wort "lint" nicht fällt.
---

# Lint

Ein Lint-Lauf ist eine Gesundheitsprüfung, kein Umbau.

Grundregel: Du behebst, was du belegen kannst. Vorgelegt wird nur, wo keine Quelle entscheidet — dort wäre Ändern gleichbedeutend mit Erfinden.

Was du änderst, machst du nachvollziehbar: `LOG.md` je Lauf, `git diff` je Seite. Das ist die Kontrolle, nicht die Rückfrage.

Vergleichsgrundlagen sind `raw/`, `kataloge/*.json` und die Änderungsmatrizen im Wiki. Prüfst du nur gegen `raw/` und liegt dort eine abgelaufene Fassung, bestätigt der Lauf ein veraltetes Wiki als gesund.

## 1. Graph erzeugen

`python3 scripts/graph.py` ausführen, `wiki/GRAPH.md` lesen. Nichts anderes hält die Datei aktuell. `GRAPH.md` ist abgeleitet: kein Index-Eintrag, keine Handänderung, zählt nicht als verwaiste Seite.

Der Abschnitt „Befunde" nimmt dir die mechanische Prüfung ab — verwaiste Seiten, Links und Kanten ins Leere, Kanten ohne Geltung, doppelt beanspruchte Positionen, IDs ohne Entsprechung im Rohkatalog, Kataloggrenzen-Verstöße, `kein_aequivalent` ohne Begründung, fehlendes `stand:`.

„Katalogabdeckung" zeigt die Quote je Katalog; eine niedrige BEB-Quote ist richtig, nicht behebbar. „Katalogzuordnung" zeigt den Stand der `entspricht`-Kanten.

## 2. Umfang

Ohne Angabe: Seiten, die seit dem letzten `lint`-Eintrag in `LOG.md` geändert wurden, plus deren Nachbarn laut Backlink-Tabelle. Letzter Lauf: `grep "^## \[" wiki/LOG.md | grep lint | tail -1`.

Die Graph-Befunde gelten immer fürs ganze Wiki, sie sind billig. Nicht angewendete Änderungsmatrizen (`angewendet: nein`) gehören immer dazu, unabhängig vom gewählten Umfang.

Vollständiger inhaltlicher Lauf nur auf Ansage, bei größerem Umfang nach Themencluster. Ein Lauf, der zu viel umfasst, wird oberflächlich.

## 3. Prüfen (nur lesen)

Erst alle Befunde sammeln, ohne zu ändern.

| Befund | Woran erkennbar |
|---|---|
| Widerspruch | Zwei Seiten sagen Unvereinbares über denselben Sachverhalt |
| veraltete Aussage | Eine neuere Quelle in `raw/` überholt die Seite |
| unbelegte Aussage | Behauptung ohne Verweis auf `raw/` |
| Kante ohne Prosa | Die Kante verweist auf eine Seite, wo die Regel nicht ausformuliert ist |
| Position ohne Kante | Der Text nennt Ausschluss oder Alternative, das Frontmatter nicht |
| fehlende `alternativ_zu` | Text benennt Alternativen („alternativ zu", „je Arbeitsmodell genau eine") ohne Kante |
| `entspricht` ohne Kardinalität | Nicht-1:1-Zuordnung als mehrere unabhängige Kanten statt in der Geltung |
| fehlender Querverweis | Seite nennt ein Konzept mit eigener Seite ohne Link |
| fehlende Seite | Konzept wird auf mehreren Seiten miterklärt, hat keine eigene |
| Duplikat | Derselbe Sachverhalt mehrfach ausgeschrieben statt verlinkt |
| Lücke | Naheliegende Frage, die das Wiki nicht beantwortet |
| abgelaufene Quelle | Eine Quellseite trägt ein `gueltig_bis` in der Vergangenheit, die daran hängenden Seiten gelten unverändert weiter |
| offene Matrix | Eine Änderungsmatrix mit `angewendet: nein` |
| Stilverstoß | siehe Abschnitt 9 |

Klärungsgrundlage sind `raw/` und `kataloge/*.json`. Ohne Beleg dort lautet der Befund „unbelegt", nicht „stimmt" — Wiki-Seiten belegen einander nicht. Ausnahme sind Änderungsmatrizen: Sie sind belegtes, freigegebenes Wissen und dürfen als Grundlage dienen.

## 4. Ändern

- fehlende Querverweise, Links auf verwaiste Seiten
- fehlende `positionen:` — Nummern stehen im Text, das Präfix folgt aus der Quelle der Seite
- Kanten, deren Regel als Prosa bereits auf einer Seite steht, samt Geltung und Prosaverweis
- Stilverstöße, kaputte Links, uneinheitliche Benennung
- **Widerspruch**, wenn `raw/` ihn entscheidet. Vorher prüfen, ob beide recht haben: unterschiedliche Geltungsbereiche (Kasse gegen privat, Gewerbe- gegen Praxislabor) oder Stände sind kein Widerspruch, sondern eine fehlende Einschränkung — dann ergänzt du die Einschränkung, statt eine Seite zu korrigieren.
- **Veraltete Aussage.** Nicht überschreiben: `ersetzt_durch:` und `ersetzt:` setzen, alter Wortlaut bleibt stehen. Altfälle brauchen ihn.
- **Duplikate und Zusammenführungen**, wenn es sich um dieselbe Sache handelt (Abschnitt 8).

Nach jeder Runde `graph.py` erneut laufen lassen. Im Protokoll steht, was du geändert hast — nicht nur wie viel.

## 5. Vorlegen

Nur, wo keine Quelle entscheidet:

- **Widerspruch ohne Klärung in `raw/`.** Bleibt als offene Frage auf beiden Seiten vermerkt.
- **Unbelegte Aussage.** Nicht löschen, als unbelegt markieren. Sie kann stimmen; vielleicht wurde nur die Quelle nie eingepflegt.
- **Fehlendes Äquivalent.** `kein_aequivalent` trägst du nur ein, wenn die Quelle es hergibt. Eine Position, zu der du nichts findest, ist nicht dasselbe wie eine ohne Entsprechung.
- **Matrixzeilen der Art `offen`.** Siehe Abschnitt 6.

## 6. Änderungsmatrix anwenden

Trägt eine Matrix im Wiki `angewendet: nein`, ist das der Auftrag. Aufruf mit Matrixnamen, oder du findest sie beim Umfang-Schritt.

Je Zeile, außer `unveraendert_geprueft`:

1. Alte Position im Positionsregister von `GRAPH.md` nachschlagen — das gibt die zuständige Seite.
2. Über Backlinks und Volltext alle weiteren Fundstellen sammeln.
3. **Kanten nicht vergessen.** Jede Kante, die auf die alte Position zeigt, ist betroffen — sie steht im Frontmatter, nicht im Text, und fällt beim Lesen sonst durch.
4. Ändern nach Art der Zeile: `umbenannt` und `ersetzt_durch` → Referenzen umstellen, alte Seite bekommt `ersetzt_durch:`. `entfallen` → `gueltig_bis` setzen, Aussage bleibt stehen. `regel_geaendert` → neue Regel aus der Quelle einarbeiten, alte mit `gueltig_bis`.
5. Zeilen der Art `offen` nicht anwenden, sondern vorlegen.

Danach `angewendet: ja` in der Matrix und ein Protokolleintrag mit der Zahl geänderter Seiten und Kanten je Zeile. Eine halb angewendete Matrix ist schlimmer als eine unangewendete — läuft der Lauf nicht durch, bleibt `nein` stehen und du hältst im Protokoll fest, wie weit du gekommen bist.

## 7. Was Lint nicht tut

Lint erzeugt keine Abrechnungsartefakte. Aus `entspricht`-Kanten ließen sich Vorlagen für einen anderen Katalog ableiten — das ist Generierung mit eigener Prüfpflicht (jede Ausgangsposition abgehakt: abgebildet, aufgeteilt, zusammengefasst oder ohne Äquivalent) und gehört in einen eigenen Skill. Eine Vorlage ist zudem mehr als eine Positionsliste; Mengen, Bemerkungen und Hinweiszeilen tragen Bedingungen, die sich nicht mit den Nummern übersetzen.

Fällt dir eine mögliche Ableitung auf, vermerkst du sie unter den offenen Punkten.

## 8. Redundanz ohne Informationsverlust

Eine Tatsache steht an genau einer Stelle, alles andere verlinkt dorthin. Das heißt nicht kürzen: Wortzahl ist kein Ziel. Du entfernst die zweite Ausformulierung, nicht den zweiten Gedanken.

Zusammenführen nur bei echtem Duplikat — Übersetzung, Abkürzung, Synonym, dieselbe Sache anders benannt. Nicht bei verwandten Themen, nicht bei Eltern-Kind-Beziehungen. Im Zweifel getrennt lassen und verlinken.

## 9. Stil

Neutral, deklarativ, kurze Sätze. Fettung und Symbole nur bei echter Struktur: Tabellen, Kennzahlen, Formeln. Keine Ausrufezeichen, keine Emoji, keine Anmoderation.

## 10. Lücken

Recherchierte Ergebnisse nicht direkt ins Wiki schreiben. Fundstücke gehören als Quelle nach `raw/_inbox/` und dann durch den Ingest — sonst erzeugt der Lauf die unbelegten Aussagen, die er beseitigen soll.

Am Ende 2–5 offene Fragen nennen und Quellen, deren Suche sich lohnt.

## 11. Protokollieren

Ein Eintrag pro Lauf, nicht pro Korrektur:

```
## [2026-08-05] lint | Gruppenseiten BEL
Geprüft: 12 Seiten. Graph: 0 verwaist, 0 kaputte Links.
Behoben: positionen: auf 8 Seiten, 23 Kanten aus vorhandener Prosa, 6 Querverweise.
Matrix BEB97 2025→2026 angewendet: 14 Zeilen, 22 Seiten, 9 Kanten. 2 Zeilen offen.
Vorgelegt: doppelte Ausschlussprosa 2010/8060 auf drei Seiten.
Offen: Gilt der BEL-Stand 2022 noch? Rundschreiben nicht ingested.
```

Vorgelegtes erst nach der Entscheidung als behoben nachtragen. Befunde, die bewusst bleiben, ebenfalls festhalten — sonst meldet sie der nächste Lauf erneut.