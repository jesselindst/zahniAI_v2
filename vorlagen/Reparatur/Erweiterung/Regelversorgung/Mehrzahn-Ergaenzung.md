| Bereich | Autor | erstellt am | Version |
|--------|--------|--------|--------|
| Reparatur / Erweiterung / Regelversorgung | CLAUDE | 2026-04-27 | v1 |

# BEL-Positionen

| BEL | Leistung | Menge | Bemerkung |
|--------|--------|--------|--------|
| 0010 | Modell | 1 |  |
| 8010 | Grundeinheit ZE | 1 |  |
| 8023 | LE Einarbeiten Zahn | 2 | je Zahn (Beispielwert für 2 Zähne) |
| 8024 | LE Basisteil Kunststoff | 1 |  |
| 8130 | Auswechseln Konfektionsteil | 2 |  |
| 8027 | LE Kunststoffsattel | 1 | bei Sattelerweiterung |
| 9330 | Versandkosten | 2 |  |

# Basisleistungen

_Pflicht-Kern ist vollständig über BEL abgedeckt. Keine zusätzlichen BEB97-Basisleistungen erforderlich._

# Zusatzleistungen

## BEL-Zusatzleistungen

| BEL | Leistung | Menge | Bemerkung |
|--------|--------|--------|--------|
| 0023 | Verwendung von Kunststoff | 1 | bei Maßnahmen im Metallbereich (FZ-RL 6.5) |
| 0053 | Modell nach Überabdruck | 1 | bei Überabdruck-Technik |
| 0112 | Fixator | 1 | bei Bissfixierung |
| 0120 | Mittelwertartikulator | 1 | wenn Lateral-/Protrusionsbewegung erforderlich |
| 0201 | Basis für Vorbissnahme | 1 | bei Notwendigkeit der Bissnahme |
| 0213 | Basis für Bissregistrierung | 1 | bei Bissregistrierung |
| 0220 | Bisswall | 1 | bei Bissnahme |
| 3830 | Zahn zahnfarben hergestellt | je | wenn aus anatomischen Gründen kein Konfektionszahn verwendbar |
| 3840 | Zahn zahnfarben hinterlegen | je | OK nur bis Zahn 5 / UK nur bis Zahn 4 |
| 3800 | Einfache gebogene Halte-/Stützvorrichtung | je | bei Klammer am ergänzten Zahn |
| 3810 | Sonstige gebogene Halte-/Stützvorrichtung | je | bei aufwendiger Klammer |
| 8025 | LE Halte-/Stützvorrichtung einarbeiten | je | je eingearbeiteter Klammer (skalieren mit Klammeranzahl) |
| 8026 | LE Rückenschutzplatte einarbeiten | je | bei Rückenschutzplatte (Bedingung §12b: ungünstige Bissverhältnisse) |
| 8030 | Retention, gebogen | je | je Retention |
| 8040 | Retention, gegossen | je | bei gegossener Retention statt 8030 |
| 8060 | Gegossenes Basisteil | je | bei gegossener Basis-Erweiterung — nicht neben 8030/8040/8070 |
| 8070 | Metallverbindung bei Instandsetzung/Erweiterung | je | bei Lötverbindung im Metallbereich; Lot zu 75% abrechenbar (bel_kritische_regeln §17) |

## BEB-Zusatzleistungen

| BEB97 | Leistung | Menge | Bemerkung |
|--------|--------|--------|--------|
| 0732 | Desinfektion | 2 |  |
| 0710 | Eilterminzuschlag | 1 | bei urgency=express |
| 0721 | Zeiteinheit; Zahntechniker-Meister | je | bei Meister-Aufwand |
| 0722 | Zeiteinheit; Zahntechniker | je |  |
| 0723 | Zahnfarbenbestimmung I | 1 | bei abweichender Farbe |

# Material

| Material | Menge | Bemerkung |
|--------|--------|--------|
| Konfektionszahn (Kunststoff Standard) | 2 Stück | je Zahn |
| PMMA-Reparaturkunststoff | — |  |
| Modellgips (Hartgips) | — |  |
| Lotmaterial | — | bei 8070, zu 75% abrechenbar |

# Hinweise

Mehrere Zähne werden in vorhandene Prothese ergänzt — Regelversorgung. Mengen oben beispielhaft für 2 Zähne; bei mehr Zähnen die "je Zahn"-Positionen entsprechend skalieren. Bei größerer Erweiterung ggf. zusätzlich Sattelerweiterung (8027) und Klammern (8025).
- FZ-RL Befund 6.4 (je 1. Zahn) + 6.4.1 (je weiterer Zahn) bei Kunststoffmaßnahmen.
- Bei Metallbereichs-Maßnahmen FZ-RL 6.5 / 6.5.1 — dann zusätzlich 0023, 8070, ggf. 8060.
- 9330 nur für gewerbliche Labore (bel_kritische_regeln §19).
- 8070 NUR bei Lötung; bei Laser → BEB (Reparatur).
- Nicht-nebeneinander §4f: 8060 schließt 8010 aus; 8070 nicht neben 8030/8040/8060.