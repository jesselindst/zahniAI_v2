---
name: ingest_to_wiki
description: Neue Quellen aus raw/_inbox/ ins Wiki einarbeiten — lesen, analysieren, in Wissensseiten zerlegen, mit dem Bestand verknüpfen, INDEX.md und LOG.md nachziehen. Nutze diesen Skill immer, wenn eine neue Quelle, ein Dokument, ein Katalog oder ein Rundschreiben ins Wiki soll — auch wenn das Wort "ingest" nicht fällt.
---

# Ingest

Verarbeite $ARGUMENTS (ohne Argument: alles in `raw/_inbox/`), eine Quelle nach der anderen. Eine Quelle wird vollständig abgeschlossen — inklusive `INDEX.md`, `LOG.md` und Verschieben — bevor die nächste beginnt. Ein abgebrochener Lauf hinterlässt sonst Seiten ohne Index-Eintrag, und der nächste Lauf kann nicht erkennen, was schon da ist.

Der Ingest ist der einzige Schritt, an dem viel Aufwand pro Quelle gerechtfertigt ist. Was hier sauber zerlegt und verknüpft wird, muss später nie wieder aus dem Rohdokument rekonstruiert werden.

## 1. Orientieren

Lies zuerst `INDEX.md` vollständig. Ohne diesen Überblick entstehen Seiten, die es unter anderem Namen schon gibt — der teuerste Fehler beim Ingest, weil er sich mit jeder weiteren Quelle vervielfacht.

## 2. Quelle lesen und Gliederung erstellen

Lies die Quelle vollständig, bevor du irgendetwas schreibst. Ordne dann jede relevante Aussage einer der beiden Kategorien zu:

- **abrechnungsrelevant** — Positionsnummern, Leistungsinhalte, Abrechnungsbedingungen, Ausschlüsse, Kombinierbarkeit
- **fachlich einordnend** — Werkstoffe, Herstellungsschritte, Begriffe, Zusammenhänge, die das Verständnis der Abrechnung tragen

Halte fest, welche Konzepte im Wiki schon eine Seite haben, welche neu angelegt werden und welche bestehenden Seiten aktualisiert werden müssen. Diese Gliederung legst du bei der ersten Quelle eines Laufs kurz vor, ebenso bei jeder Quelle, deren Zuschnitt unklar ist. Danach kannst du durchlaufen.

## 3. Seiten schreiben

**Seitenschnitt.** Eine Seite pro Ding, über das man eigenständig eine Frage stellen würde und auf das andere Seiten verlinken werden. Nicht eine Seite pro Kapitel der Quelle — die Struktur des Dokuments ist nicht die Struktur des Wikis. Ein Katalog mit vielen eigenständigen Positionen kann 15 Seiten ergeben, ein zweiseitiges Rundschreiben eine einzige. Die Zahl folgt aus dem Inhalt, sie ist kein Ziel: Seiten aufzuteilen, um auf eine Zahl zu kommen, erzeugt Fragmente, die einzeln nichts beantworten.

Ein Ingest berührt in der Regel mehr bestehende Seiten, als er neue anlegt. Wenn das umgekehrt ist, prüfe, ob du an Vorhandenem vorbeigeschrieben hast.

**Benennung.** Fachbegriff im Singular, ausgeschrieben, wie er in den Quellen steht. Abkürzungen nur, wenn sie die übliche Bezeichnung sind (BEL, BEB). Synonyme und Abkürzungen bekommen keine eigene Seite, sondern werden im Frontmatter als `aliase` geführt — sonst laufen zwei Seiten für dieselbe Sache nebeneinander her.

**Belegpflicht.** Jede Aussage ist auf ihre Quelle zurückführbar. Quellen stehen im Frontmatter, im Text folgt die konkrete Fundstelle in Klammern am Satzende, z. B. `(BEL II, Nr. 001 0)`. Positionsnummern, Beträge und Wortlaute von Leistungsbeschreibungen zitierst du exakt — hier ist Umformulieren ein Fehler, kein Stil.

**Stil.**
- Neutral und deklarativ.
- Kurze Sätze, ein Gedanke pro Satz.
- Die Modelle, die das Wiki lesen, folgen Anweisungen zuverlässig; sie brauchen keine rhetorische Betonung. Fettung und Symbole nur, wo echte Struktur ist: Tabellen, Kennzahlen, Formeln.
- Keine Ausrufezeichen, keine Emoji, keine Anmoderation. Die Seite beginnt mit dem Inhalt.

**Was nicht ins Wiki kommt.**
- Aussagen, die anderswo schon stehen — verlinken, nicht neu ausschreiben. Eine Tatsache lebt an genau einem Ort.
- Reine Katalogtabellen. Wäre ein Modell mit dem Rohdokument selbst darauf gekommen (reiner Diff, reine Gruppierung, keine Interpretation), schreibst du nur die Konsequenz auf und verlinkst auf die Quelle.
- Zahlen mit Ablaufdatum: Tagespreise, jährliche Beträge, Regionalsätze. Verweise auf die Quelle statt sie festzuschreiben — eine falsch gewordene Zahl im Wiki ist schlechter als gar keine.
- Prozess-Metadaten über den Ingest selbst (Belegquote, Zählweisen, Marker-Abdeckung). Die gehören auf die Quellseite.

## 4. Mit dem Bestand verbinden

Neue Seiten sind wertlos, solange nichts auf sie zeigt. Ergänze auf den bestehenden Seiten, die das neue Konzept erwähnen, die Links dorthin. Sonst entstehen verwaiste Seiten, die der Lint-Lauf später aufräumen muss.

Widerspricht Neues dem Bestand, machst du den Konflikt auf beiden Seiten sichtbar — mit beiden Aussagen und ihren Quellen — statt still zu überschreiben. Auflösen ist Sache des Lint-Laufs oder einer ausdrücklichen Entscheidung.

## 5. Frontmatter

Jede Seite bekommt maschinenlesbaren Kopf, damit später Graph-Traversierung möglich ist:

```yaml
---
titel: Modellguss-Basis
aliase: [Modellgussbasis]
labels: [Abrechnung, BEL]
quellen: [raw/kassen/bel-ii-2024.pdf]
stand: 2026-08-05
---
```

Labels: `Abrechnung`, `BEB`, `BEL`, `Herstellung`, `Material`, `Regulatorik` — du bist nicht darauf beschränkt. Ein neues Label lohnt sich nur, wenn absehbar 5–10 Seiten es tragen werden. Der Lint-Lauf ergänzt Labels bei Bedarf nach, du kannst also konservativ bleiben.

## 6. Quellseite anlegen

Pro Quelle eine Seite unter den Quellseiten: Titel, Herausgeber, Stand, Ablageort in `raw/`, zwei bis drei Sätze worum es geht, und die Liste der Wissensseiten, die daraus entstanden sind. Hierhin gehören auch die Prozess-Metadaten des Ingests.

Damit lässt sich später beantworten, was aus einer Quelle geworden ist — und wenn eine Quelle veraltet, welche Seiten davon betroffen sind.

## 7. `INDEX.md` aktualisieren

Bei jedem Ingest, für jede neue und jede geänderte Seite:

| Seite | Inhalt | Meta |
|---|---|---|
| [Modellguss-Basis](wiki/modellguss-basis.md) | Abrechnungsposition und Leistungsinhalt der Basis beim Modellguss | 2026-08-05 · bel-ii-2024.pdf |

Der Einzeiler unter "Inhalt" ist das, wonach beim nächsten Ingest gesucht wird. Er muss die Seite unterscheidbar machen, nicht nur ihren Titel wiederholen.

## 8. `LOG.md` ergänzen

Ein Eintrag pro Quelle, 1–2 Sätze, was übernommen wurde:

```
## [2026-08-05] ingest | BEL II, Stand 2024
7 neue Seiten zu Modellguss-Positionen, 12 bestehende Seiten um Querverweise ergänzt. Konflikt zur Kombinierbarkeit von 008 0 und 010 3 auf beiden Seiten vermerkt.
```

## 9. Quelle verschieben

Erst wenn alles davon steht, verschiebst du die Quelle aus `_inbox/` an ihren Platz unter `raw/`. Das Verschieben ist die Bestätigung, dass der Ingest abgeschlossen ist — was noch im Inbox liegt, ist noch offen.