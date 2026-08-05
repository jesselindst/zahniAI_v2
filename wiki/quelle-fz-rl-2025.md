---
titel: Quelle Festzuschuss-Richtlinie, Fassung 2025
aliase: [FZ-RL 2025, FZ-RL_2024-11-21_iK-2025-01-01, fz_2025_v1.json]
labels: [Quelle, Regulatorik, Preise]
quellen: [kataloge/fz_2025_v1.json]
stand: 2026-08-05
gueltig_von: 2025-01-01
gueltig_bis: 2025-12-31
ersetzt_durch:
  - quelle-fz-rl-2026
---

## Dokument

| | |
|---|---|
| Titel | Richtlinie des Gemeinsamen Bundesausschusses über die Festzuschüsse für zahntechnische Leistungen, Befundkatalog mit Beträgen |
| Herausgeber | Gemeinsamer Bundesausschuss |
| Beschluss | 21.11.2024 |
| Gültigkeit | 01.01.2025 bis 31.12.2025 |
| Ablage | `kataloge/fz_2025_v1.json` |
| Umfang | 8 Befundklassen, 54 Befunde |

Der Befundkatalog der Festzuschuss-Richtlinie in strukturierter Form. Je Befund enthält er die Nummer, die Beschreibung mit Bezugsgröße, die zahntechnischen Leistungen der Regelversorgung und die vier Beträge für ohne Bonus, Bonus über fünf Jahre, Bonus über zehn Jahre und Härtefall.

Damit ist er zugleich Quelle und Katalog: Die Befundnummern sind Positions-IDs mit dem Präfix `fz` und werden von `scripts/graph.py` gegen diese Datei geprüft.

## Abgelöst

Diese Fassung ist durch [[quelle-fz-rl-2026]] abgelöst, Beschluss vom 05.12.2025, in Kraft ab 01.01.2026. Der Wortlaut bleibt hier stehen, weil Altfälle ihn brauchen: Für Leistungen mit Leistungsdatum 2025 gelten diese Beträge.

Was sich geändert hat, steht in [[aenderungsmatrix-fz-rl-2025-2026]].

Die Abweichung ist erheblich. Befund 1.1 ohne Bonus lag 2025 bei 229,25 Euro und liegt 2026 bei 239,03 Euro, rund 4,3 Prozent höher. Die Steigerung ist je Befund verschieden; eine pauschale Fortschreibung ist nicht zulässig.

Ein Kostenvoranschlag mit den Beträgen dieser Seite ist für Leistungen ab 01.01.2026 falsch. Die Beträge stehen deshalb ausschließlich auf der Jahrgangsseite [[festzuschussbetraege-2025]], nicht auf den Konzeptseiten.

Die Fassung 2026 liegt als `kataloge/fz_2026_v1.json` daneben und ist die aktive; diese Datei bleibt als Diff-Grundlage liegen.

## Entstandene und ergänzte Seiten

| Seite | Rolle |
|---|---|
| [[festzuschussbetraege-2025]] | Jahrgangsseite, trägt die 216 Beträge |
| [[festzuschuss-befundklassen]] | zuständig für alle 54 Befundnummern, ergänzt um die zahntechnische Regelversorgung je Befund |
| [[festzuschuss]] | Quellenangabe und Verweis auf die Jahrgangsseite |
| [[haertefall-und-bonus]] | die vier Betragsspalten entsprechen den vier Stufen |

## Was der Katalog belegt

Die Liste der zahntechnischen Leistungen je Befund entscheidet Fragen, die zuvor nur mittelbar zu beantworten waren:

- 201 0 Metallbasis steht in den Befunden 3.1, 4.1, 4.3 und 4.5, nicht in 2.7. Der Modellguss gehört damit zu Klasse 3 oder 4, der Zuschlag 2.7 zum festsitzenden Zahnersatz.
- 102 3 Flügel für Adhäsivbrücke steht in 2.1 und 2.2, nicht in 1.4 oder 1.5.
- 162 0 Vestibuläre Verblendung Keramik steht in 1.3, 2.7, 6.9 und 7.3, nicht in 4.7. Die Teleskopverblendung nach 4.7 kennt nur 155 0, 160 0, 161 0, 164 0 und 165 0, also Kunststoff und Komposit. Das deckt sich mit dem BEL, wo 162 0 als Träger nur Krone und Brückenglied nennt, siehe [[verblendung-bel]].
- Befund 1.4 hat keine zahntechnische Leistung, sondern nur die Materialangabe Stift. Der konfektionierte Stiftaufbau ist Regelversorgung ohne Laboranteil, anders als der gegossene nach 1.5.

## Offene Punkte

Der Katalog enthält nur Teil B der Richtlinie. Teil A liegt seit dem Ingest der Fassung 2026 vor, siehe [[quelle-fz-rl-2026]].

Die Zahnersatz-Richtlinie, die definiert, was für einen Befund Regelversorgung ist, liegt ebenfalls nicht vor.

Acht Befunde führen keine zahntechnischen Leistungen: 1.4 nur Material, 6.0 keine, sowie 8.1 bis 8.6, die als Prozentsatz anderer Befunde definiert sind.
