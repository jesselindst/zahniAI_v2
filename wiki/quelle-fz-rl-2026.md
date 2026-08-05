---
titel: Quelle Festzuschuss-Richtlinie, Fassung 2026
aliase: [FZ-RL 2026, FZ-RL_2025-12-05_iK-2026-01-01, fz_2026_v1.json]
labels: [Quelle, Regulatorik, Preise]
quellen: [raw/FZ-RL_2025-12-05_iK-2026-01-01.pdf, raw/2026-01-01-FZ-Betraege.pdf, kataloge/fz_2026_v1.json]
stand: 2026-08-05
gueltig_von: 2026-01-01
gueltig_bis:
ersetzt:
  - quelle-fz-rl-2025
---

## Dokument

| | |
|---|---|
| Titel | Richtlinie des Gemeinsamen Bundesausschusses zur Bestimmung der Befunde und der Regelversorgungsleistungen für die Festzuschüsse nach §§ 55, 56 SGB V sowie über die Höhe der auf die Regelversorgungsleistungen entfallenden Beträge nach § 56 Absatz 4 SGB V |
| Herausgeber | Gemeinsamer Bundesausschuss |
| Erstfassung | 03.11.2004, Bundesanzeiger 2004 S. 24 463, in Kraft 01.01.2005 |
| Zuletzt geändert | 05.12.2025, BAnz AT 04.02.2026 B3, in Kraft 01.01.2026 |
| Umfang | 57 Seiten |
| Ablage | `raw/FZ-RL_2025-12-05_iK-2026-01-01.pdf`, Katalog unter `kataloge/fz_2026_v1.json` |

Ergänzend die Servicetabelle des GKV-Spitzenverbands mit denselben Beträgen in kompakter Form, `raw/2026-01-01-FZ-Betraege.pdf`, 2 Seiten. Sie enthält die Klassen 1 bis 7; Klasse 8 fehlt dort, weil diese Befunde keinen eigenen Betrag tragen.

## Aufbau

| Teil | Inhalt |
|---|---|
| Präambel | Grundlage der Befundbestimmung, Bezug zur Zahnersatz-Richtlinie, Stellungnahmerecht des Verbands Deutscher Zahntechniker-Innungen |
| A. Allgemeines | neun Nummern mit den Anwendungsregeln, dazu drei Protokollnotizen |
| B. Befunde und zugeordnete Regelversorgungen | 54 Befunde in 8 Klassen, je mit zahnärztlichen und zahntechnischen Regelversorgungsleistungen und sechs Beträgen |
| C. Delegation der Bekanntmachung | Verfahren nach § 56 Abs. 4 SGB V |

Damit liegt erstmals Teil A vor. Die vorige Fassung im Wiki, [[quelle-fz-rl-2025]], enthielt nur den Befundkatalog.

## Was Teil A regelt

Die neun Nummern tragen die Anwendungsregeln, die zuvor nur mittelbar belegt waren:

| Nr. | Inhalt |
|---|---|
| 1 | Befunde nur ansetzbar, wenn die in der Beschreibung geregelten Voraussetzungen vorliegen. Funktionstüchtiger vorhandener Zahnersatz wird natürlichen Zähnen gleichgestellt |
| 2 | Festzuschüsse werden erst gewährt, wenn keine weitere Versorgungsnotwendigkeit besteht; bei Teilleistungen anteilig. „Festzuschüsse für Verblendungen werden immer dann gewährt, wenn die Regelversorgung diese vorsieht" |
| 3 | Es soll eine funktionell ausreichende Gegenbezahnung vorhanden sein oder hergestellt werden |
| 4 | Härtefall: zusätzlicher Betrag von 40 Prozent, angepasst an die tatsächlich anfallenden Kosten der Regelversorgung, höchstens in Höhe der entstandenen Kosten |
| 5 | Härtefall bei gleich- oder andersartiger Wahl: nur der Festzuschuss nach § 55 Abs. 1 Satz 2 SGB V und der feste 40-Prozent-Betrag |
| 6 | Suprakonstruktionen; bei Erstversorgung gilt die Befundsituation vor dem Setzen der Implantate. Festzuschüsse werden auch gewährt, wenn Suprakonstruktionen außerhalb der Fälle der Zahnersatz-Richtlinie gewählt werden |
| 7 | Für Implantate, Implantataufbauten und implantatbedingte Verbindungselemente sind keine Festzuschüsse ansetzbar, bei Erstversorgung wie bei Erneuerung und Wiederherstellung |
| 8 | Abrechnungsgrundlage: BEMA und BEL für die Regelversorgung, Gebührenordnung für Zahnärzte für gleichartige Mehrkosten und für andersartige Versorgung; in den Ausnahmefällen nach Nr. 36 der Zahnersatz-Richtlinie weiterhin BEMA und BEL |
| 9 | Begleitleistungen bleiben vertragszahnärztliche Leistungen, auch bei gleich- oder andersartiger Wahl |

Drei Protokollnotizen ergänzen: Therapieschritte in begründeten Ausnahmefällen mit Ermittlung auf Basis des Gesamtbefundes und Begutachtungsmöglichkeit der Kasse; die Begrenzung auf die entstandenen Kosten auch bei Nicht-Härtefällen; die Ankündigung einer Überprüfung der Auswirkungen.

Damit sind die Aussagen der Seiten [[festzuschuss]], [[haertefall-und-bonus]] und [[versorgungsform]] primärquellenbelegt. Sie stützten sich zuvor auf [[quelle-recherche-abrechnungsrahmen-2026]].

## Vier Zuschlagsbefunde sind Differenzbeträge

Teil B beschreibt vier Befunde nicht als eigene Leistung, sondern als Differenz zweier Positionen. Aus der Fassung 2025 war das nicht ersichtlich.

| Befund | Rechnung |
|---|---|
| 1.3 | 102 4 Krone für vestibuläre Verblendung abzüglich 102 1 Vollkrone Metall |
| 2.7 | 102 4 abzüglich 102 1 |
| 3.2 | Teleskopversorgung abzüglich 204 1 Zweiarmige Klammer mit Auflage |
| 4.5 | 303 0 Aufstellung Metall je Zahn abzüglich 302 0 Aufstellung Wachs je Zahn |

Das erklärt die geringe Höhe dieser Zuschläge und ist im Katalog im Feld `abzueglich` festgehalten.

## Neu im Katalog gegenüber 2025

Der Katalog `fz_2026_v1.json` führt zusätzlich zur Fassung 2025:

- `regelversorgung_zahnaerztlich` mit den BEMA-Positionen je Befund
- `abzueglich` bei den vier Differenzbefunden
- die Betragsbestandteile `honorar` und `material_labor` nach § 57 Abs. 1 und Abs. 2 SGB V
- `null` statt 0,00 bei den Befunden der Klasse 8, die keinen eigenen Betrag tragen

Die zahntechnischen Regelversorgungslisten sind aus der Fassung 2025 übernommen, nachdem der Abgleich gegen Teil B für alle 54 Befunde keine Abweichung ergeben hat.

## Fassungswechsel

Was sich geändert hat, steht in [[aenderungsmatrix-fz-rl-2025-2026]]. Kurz: kein Befund neu, keiner entfallen, keine Regelversorgungsliste geändert; 48 Befunde mit neuen Beträgen, Steigerung zwischen 3,03 und 9,39 Prozent bei einem Median von 4,78 Prozent.

## Offene Punkte

Die Richtlinie verweist in Teil A Nr. 8 auf das „bundeseinheitliche Verzeichnis der abrechnungsfähigen zahntechnischen Leistungen (BEL II – 2004)". Maßgeblich ist seit Langem das BEL II – 2014, siehe [[quelle-bel-ii-2022]]. Die Fundstelle ist im Richtlinientext nicht nachgeführt worden; sachlich ändert das nichts.

Die Zahnersatz-Richtlinie, auf die Teil A an mehreren Stellen verweist und die bestimmt, was für einen Befund Regelversorgung ist, liegt weiterhin nicht vor. Sie trägt insbesondere Nr. 36 zur Suprakonstruktion und Nr. 20 zum Verblendbereich.

Teil C regelt allein die Bekanntmachung und ist ohne Abrechnungsrelevanz.
