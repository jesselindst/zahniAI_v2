| Bereich | Autor | erstellt am | Version |
|--------|--------|--------|--------|
| Reparatur / Unterfütterung / Regelversorgung | CLAUDE | 2026-04-27 | v1 |

# BEL-Positionen

| BEL | Leistung | Menge | Bemerkung |
|--------|--------|--------|--------|
| 0010 | Modell | 1 | Gegenbiss-/Konter-Modell (Hilfsmodell für Unterfütterung); je Kontrollmodell zusätzlich abrechenbar |
| 0018 | Modell bei Implantatversorgung | 1 | alternativ zu 0010 bei implantatgestützter Prothese (Nr. 36b ZE-RL) |
| 0023 | Verwendung von Kunststoff | 1 | bei Sonderdarstellung individueller Primärteile / Zahnfleischpartien (max. 3×); aus FZ-RL 6.6/6.7 |
| 0112 | Fixator | 1 | je Unterfütterung; Bisslagen-Fixierung (Artikulator 012 0 NICHT abrechenbar bei Unterfütterung) |
| 8010 | Grundeinheit ZE | 1 | NUR wenn gleichzeitig zur Unterfütterung weitere Instandsetzung erbracht wird — Unterfütterung selbst löst KEINE 8010 aus |
| 8080 | Teilunterfütterung einer Basis | 1 | je Prothese (auch bei mehreren Bereichen nur 1×); lokale weichbleibende Anpassung |
| 8088 | Teilunterfütterung/implantatgest. | 1 | alternativ zu 8080 bei implantatgestützter Basis |
| 3821 | Weichkunststoff | 1 | je Prothese; Pflicht-Folgeleistung zu 8080/8088 bei Verarbeitung von Weichkunststoff |
| 3822 | Sonderkunststoff | 1 | je Prothese; alternativ zu 3821 bei zahnärztlicher Indikationsstellung für Sonderkunststoff statt Weichkunststoff |
| 9330 | Versandkosten | 2 | je Versandgang (nur gewerbliche Labore); Hin-/Rückversand |

# Basisleistungen

_Pflicht-Kern ist vollständig über BEL abgedeckt. Keine zusätzlichen BEB97-Basisleistungen erforderlich._

# Zusatzleistungen

| BEB97 | Leistung | Menge | Bemerkung |
|--------|--------|--------|--------|
| 0732 | Desinfektion | 2 | je Vorgang (Eingang/Ausgang) |
| 0706 | Foto- oder Video-Dokumentation | 1 | bei Bedarf |
| 0710 | Eilterminzuschlag | 1 | bei urgency=urgent/express |
| 0721 | Zeiteinheit; Zahntechniker-Meister | je | je 15 Min für nicht in BEB erfasste Leistungen |
| 0722 | Zeiteinheit; Zahntechniker | je | je 15 Min für nicht in BEB erfasste Leistungen |

# Material

| Material | Menge | Bemerkung |
|--------|--------|--------|
| Weichbleibender Kunststoff | — | für lokal sensible Schleimhaut |
| Modellgips (Hartgips) | — | für Modell und Konter |
| Desinfektionsmittel | — | nach Herstelleranweisung |

# Hinweise

Partielle weichbleibende Unterfütterung — Regelversorgung. Nur ein Bereich (lokale Schleimhaut-Empfindlichkeit).

**Festzuschuss:** Befund **6.6** "Verändertes Prothesenlager bei erhaltungswürdigem Teil-Zahnersatz, je Prothese" (FZ-RL 2024-11-21) bzw. **6.7** bei Total-/Deckprothese. Beide Befunde listen 8080 + 3821 + 0010/0112/9330 explizit unter `regelversorgung_zahntechnik`.

**BEL-Regeln (kritisch):**
- BEL 808 0 ist je Prothese / je Kiefer **nur 1×** abrechenbar — auch bei mehreren unterfütterten Bereichen.
- BEL 3821 (Weichkunststoff) ist **je Prothese 1×** Folgeleistung zu 8080/8088.
- BEL 3822 (Sonderkunststoff) alternativ zu 3821 nur bei zahnärztlicher Indikationsstellung; je Prothese 1×.
- BEL 0023 (Verwendung von Kunststoff) max. 3× pro Fall.
- **Fixator (0112) ist** abrechenbar, **Artikulator (012 0/5/8) NICHT** (BEL II §5 + Erläuterungen zu 808 0).
- BEL **8010 (Grundeinheit ZE)** nur bei zusätzlicher Instandsetzung — nicht für die Unterfütterung selbst.
- BEL 9330 nur für gewerbliche Labore.
- Bei implantatgestützter Prothese: BEL 0018 statt 0010 und BEL 8088 statt 8080.