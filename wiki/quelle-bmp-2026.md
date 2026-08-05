---
titel: Quelle Bundesmittelpreise 2026
aliase: [BMP_2026_Leistungen_Regelversorgung.pdf]
labels: [Quelle, BEL, Preise]
quellen: [raw/BMP_2026_Leistungen_Regelversorgung.pdf]
stand: 2026-08-05
---

## Dokument

| | |
|---|---|
| Titel | Bundeseinheitliche durchschnittliche Netto-Preise nach § 57 Abs. 2 Satz 1 SGB V für BEL II – 2014, Leistungen für die Regelversorgung |
| Gültigkeit | 01.01.2026 – 31.12.2026 |
| Ursprungsdatei | BMP-2026-Preise_28-10-2025_Anlage.xlsx, als PDF gedruckt am 11.11.2025 |
| Umfang | 2 Seiten, 117 Positionen |
| Ablage | `raw/BMP_2026_Leistungen_Regelversorgung.pdf` |

Eine reine Preistabelle: BEL-Leistungsnummer, Kurzbezeichnung, Bundesmittelpreis in EUR. Das Dokument enthält keine Leistungsinhalte, keine Abrechnungsregeln und keinen erläuternden Text — diese stehen im BEL II, siehe [[quelle-bel-ii-2022]].

Ein Herausgeber ist im Dokument nicht ausgewiesen.

## Entstandene Wissensseiten

- [[bundesmittelpreis]] — Konzept, Rechtsgrundlage, Deckungsgrenzen, Preissystematik. Feste Anlaufstelle für alle Verweise aus dem übrigen Wiki.
- [[bundesmittelpreise-2026]] — das Zahlenwerk des Jahrgangs 2026.

## Aufbau für Jahreswechsel

Das Wiki trennt das Konzept vom Zahlenwerk. Alle Wissensseiten verlinken auf [[bundesmittelpreis]]; ausschließlich diese Seite verlinkt auf einen Jahrgang.

Erscheint eine neue Liste, sind zwei Schritte nötig und keine weiteren:

1. Jahrgangsseite `bundesmittelpreise-<Jahr>.md` anlegen, Aufbau wie [[bundesmittelpreise-2026]].
2. In [[bundesmittelpreis]] eine Zeile in die Jahrgangstabelle ergänzen.

Ältere Jahrgangsseiten bleiben stehen. Sie werden nicht gelöscht und nicht überschrieben, damit ein Vorgang aus einem früheren Jahr nachvollziehbar bleibt. Ihre Gültigkeit steht im Frontmatter unter `gueltig_von` und `gueltig_bis`.

## Prozess-Metadaten des Ingests

- Verarbeitet am 2026-08-05. Zwei neue Wissensseiten, neun bestehende Seiten um Querverweise ergänzt.
- Textextraktion mit `pdftotext -layout`. Das PDF ist unverschlüsselt und wurde aus einer Excel-Tabelle gedruckt; die zweispaltige Anordnung der Vorlage wurde beim Übertrag in eine einspaltige, nach BEL-Gruppen sortierte Darstellung aufgelöst.
- Alle 117 Positionen sind übernommen. Die Beträge wurden maschinell extrahiert und gegen den Rohtext abgeglichen.
- Die Deckungslücke gegenüber dem BEL II wurde durch Differenzbildung der Positionsnummern beider Quellen ermittelt: 58 BEL-Positionen ohne Bundesmittelpreis, vollständig aufgeführt in [[bundesmittelpreis]].
- Die Preisgleichheit von Implantatposition und Regelpendant wurde für alle 19 Paare geprüft und bestätigt.

## Offene Punkte

- **Verwendung des Bundesmittelpreises.** Die Quelle nennt § 57 Abs. 2 Satz 1 SGB V als Rechtsgrundlage, sagt aber nichts darüber, wie der Wert weiterverwendet wird. Der Zusammenhang mit den Festzuschüssen nach § 55 SGB V ist bislang unbelegt.
- **Regionale Preise.** Die tatsächlich abzurechnenden Vergütungen nach § 88 Abs. 2 SGB V sind nicht Gegenstand dieser Quelle und im Wiki weiterhin nicht abgebildet.
- **Herausgeber und Verbindlichkeit.** Aus dem Dokument selbst nicht ersichtlich.
- **Leistungen ohne Bundesmittelpreis.** Für Kieferorthopädie, Aufbissbehelfe und Unterkieferprotrusionsschienen fehlt jede Preisgrundlage im Wiki.
