| Bereich | Autor | erstellt am | Version |
|--------|--------|--------|--------|
| Reparatur / Unterfütterung / Regelversorgung | CLAUDE | 2026-04-27 | v1 |

# BEL-Positionen

| BEL | Leistung | Menge | Bemerkung |
|--------|--------|--------|--------|
| 0010 | Modell | 1 | Gegenbiss-/Konter-Modell (Hilfsmodell für Unterfütterung); je Kontrollmodell zusätzlich abrechenbar |
| 0018 | Modell bei Implantatversorgung | 1 | alternativ zu 0010 bei implantatgestützter Prothese (Nr. 36b ZE-RL) |
| 0015 | Modell UKPS | 1 | alternativ zu 0010 bei Unterkieferprotrusionsschiene (max. 6) |
| 0023 | Verwendung von Kunststoff | 1 | bei Sonderdarstellung individueller Primärteile / Zahnfleischpartien (max. 3×); aus FZ-RL 6.6/6.7 |
| 0112 | Fixator | 1 | je Unterfütterung; Bisslagen-Fixierung (Artikulator 012 0 NICHT abrechenbar bei Unterfütterung) |
| 0115 | Fixator UKPS | 1 | alternativ zu 0112 bei UKPS |
| 8010 | Grundeinheit ZE | 1 | NUR wenn gleichzeitig zur Unterfütterung weitere Instandsetzung erbracht wird (Sprung/Bruch/Zahn) — Unterfütterung selbst löst KEINE 8010 aus |
| 8080 | Teilunterfütterung einer Basis | 1 | je Prothese (auch wenn mehrere Bereiche unterfüttert werden, nur 1×); nur ein Bereich (z.B. Sattel, lokale Druckstelle) |
| 8088 | Teilunterfütterung/implantatgest. | 1 | alternativ zu 8080 bei implantatgestützter Basis |
| 8085 | Teilunterfütterung einer Basis UKPS | 1 | alternativ zu 8080 bei Unterkieferprotrusionsschiene |
| 3822 | Sonderkunststoff | 1 | je Prothese; bei zahnärztlicher Indikationsstellung für Sonderkunststoff zusätzlich zu 8080/8088 |
| 9330 | Versandkosten | 2 | je Versandgang (nur gewerbliche Labore); Hin-/Rückversand |

# Basisleistungen

_Pflicht-Kern ist vollständig über BEL abgedeckt. Keine zusätzlichen BEB97-Basisleistungen erforderlich._

# Zusatzleistungen

| BEB97 | Leistung | Menge | Bemerkung |
|--------|--------|--------|--------|
| 0732 | Desinfektion | 2 | je Vorgang (Eingang/Ausgang) |
| 0706 | Foto- oder Video-Dokumentation | 1 | bei Bedarf (Druckstellen-Dokumentation) |
| 0710 | Eilterminzuschlag | 1 | bei urgency=urgent/express |
| 0721 | Zeiteinheit; Zahntechniker-Meister | je | je 15 Min für nicht in BEB erfasste Leistungen |
| 0722 | Zeiteinheit; Zahntechniker | je | je 15 Min für nicht in BEB erfasste Leistungen |

# Material

| Material | Menge | Bemerkung |
|--------|--------|--------|
| PMMA-Heißpolymerisat | — | dauerhaft, langlebig |
| Modellgips (Hartgips) | — | für Modell und Konter |
| Desinfektionsmittel | — | nach Herstelleranweisung |

# Hinweise

Partielle Unterfütterung mit Heißpolymerisat — Regelversorgung. Nur ein Bereich der Basis (z.B. lokale Druckstelle, einzelner Sattel). Geringerer Aufwand als Vollunterfütterung.

**Festzuschuss:** Befund **6.6** "Verändertes Prothesenlager bei erhaltungswürdigem Teil-Zahnersatz, je Prothese" (FZ-RL 2024-11-21) bzw. **6.7** bei Total-/Deckprothese. Beide Befunde listen 8080/8090/8100 + 3821/3822 + 0010/0112/9330 explizit unter `regelversorgung_zahntechnik`. Bei Teilunterfütterung Teilzahnersatz → 6.6, bei Teilunterfütterung Total/Deckprothese → 6.7.

**BEL-Regeln (kritisch):**
- BEL 808 0 ist je Prothese / je Kiefer **nur 1×** abrechenbar — selbst wenn mehrere Bereiche der Basis unterfüttert werden.
- **Fixator (0112) ist** bei Unterfütterung **abrechenbar**, **Artikulator (012 0/5/8) NICHT** (BEL II §5 + Erläuterungen zu 808 0).
- BEL **8010 (Grundeinheit ZE) ist KEINE eigenständige Leistung** zur Unterfütterung — nur abrechenbar, wenn zusätzlich eine Instandsetzung (Sprung/Bruch/Zahn ersetzen) erbracht wird.
- BEL 3822 (Sonderkunststoff) nur bei zahnärztlicher Indikationsstellung; je Prothese 1× zusätzlich zu 8080/8088.
- BEL 0023 (Verwendung von Kunststoff) max. 3× pro Fall; bei Härtefällen i.d.R. nicht abrechenbar.
- BEL 9330 (Versand) nur für gewerbliche Labore (Praxislabor: nicht abrechenbar).
- Bei implantatgestützter Prothese: BEL 0018 statt 0010 und BEL 8088 statt 8080.
- Bei UKPS (Unterkieferprotrusionsschiene): BEL 0015 statt 0010, 0115 statt 0112, 8085 statt 8080.