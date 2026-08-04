| Bereich | Autor | erstellt am | Version |
|--------|--------|--------|--------|
| Reparatur / Unterfütterung / Regelversorgung | CLAUDE | 2026-04-27 | v1 |

# BEL-Positionen

| BEL | Leistung | Menge | Bemerkung |
|--------|--------|--------|--------|
| 0010 | Modell | 1 | Gegenbiss-/Konter-/Unterfütterungsmodell (BEL II 001 0 explizit für Unterfütterung); ggf. 2× bei zusätzlichem Hilfsmodell / Kontrollmodell |
| 0018 | Modell bei Implantatversorgung | 1 | alternativ zu 0010 bei implantatgestützter Prothese (Nr. 36b ZE-RL) |
| 0023 | Verwendung von Kunststoff | 1 | bei Sonderdarstellung individueller Primärteile / Zahnfleischpartien (max. 3×); aus FZ-RL 6.6/6.7 |
| 0211 | Individueller Löffel | 1 | alternativ zu 0212 bei >3 Restzähnen oder ohne Funktionsabformung |
| 0212 | Funktionslöffel | 1 | bei funktioneller Randgestaltung (zahnloser Kiefer oder ≤3 Restzähne) |
| 0112 | Fixator | 1 | je Unterfütterung; Bisslagen-Fixierung mit Gegenbiss-Modell (Artikulator 012 0 NICHT abrechenbar bei Unterfütterung) |
| 8010 | Grundeinheit ZE | 1 | NUR wenn gleichzeitig zur Unterfütterung weitere Instandsetzung erbracht wird (Sprung/Bruch/Zahn ersetzen) — Unterfütterung selbst löst KEINE 8010 aus |
| 8090 | Vollständige Unterfütterung | 1 | je Prothese (bei bimaxillär: je Kiefer); Standardposition Heißpolymerisat |
| 8098 | Vollständige Unterfütterung/implantatgestützte Basis | 1 | alternativ zu 8090 bei implantatgestützter Basis; auch bei atrophiertem zahnlosen Kiefer (Nr. 36 b ZE-RL) |
| 8100 | Prothesenbasis erneuern | 1 | alternativ zu 8090 bei vollständigem Austausch der Kunststoffbasis (Rebasierung mit Heißpolymerisat) |
| 8108 | Prothesenbasis erneuern/Implantatversorgung | 1 | alternativ zu 8100 bei implantatgestützter Prothese (Nr. 36 b ZE-RL) |
| 3822 | Sonderkunststoff | 1 | je Prothese; bei zahnärztlicher Indikationsstellung für Sonderkunststoff zusätzlich zu 8090/8098/8100/8108 |
| 9330 | Versandkosten | 2 | je Versandgang (nur gewerbliche Labore); Hin-/Rückversand |

# Basisleistungen

_Pflicht-Kern ist vollständig über BEL abgedeckt. Keine zusätzlichen BEB97-Basisleistungen erforderlich._

# Zusatzleistungen

| BEB97 | Leistung | Menge | Bemerkung |
|--------|--------|--------|--------|
| 0732 | Desinfektion | 2 | je Vorgang (Eingang/Ausgang) |
| 0706 | Foto- oder Video-Dokumentation | 1 | bei Bedarf (Verlaufs-/Befunddokumentation) |
| 0710 | Eilterminzuschlag | 1 | bei urgency=urgent/express |
| 0721 | Zeiteinheit; Zahntechniker-Meister | je | je 15 Min für nicht in BEB erfasste Leistungen |
| 0722 | Zeiteinheit; Zahntechniker | je | je 15 Min für nicht in BEB erfasste Leistungen |

# Material

| Material | Menge | Bemerkung |
|--------|--------|--------|
| PMMA-Heißpolymerisat | — | dauerhaft, langlebig |
| Modellgips (Hartgips) | — | für Modell und Konter |
| Funktionslöffel-Kunststoff | — | nur bei 0211/0212 |
| Desinfektionsmittel | — | nach Herstelleranweisung |

# Hinweise

Vollständige Unterfütterung mit Heißpolymerisat — Regelversorgung. Indikation: Atrophie des Alveolarkamms, Druckstellen, Lockerung. Heißpolymerisation = höchste Stabilität, längste Lebensdauer.

**Festzuschuss:** Befund **6.7** "Verändertes Prothesenlager bei erhaltungswürdigem totalem Zahnersatz oder schleimhautgetragener Deckprothese, je Kiefer" (FZ-RL 2024-11-21) bzw. **6.6** bei Teil-Zahnersatz. Beide Befunde listen 8080/8090/8100 + 3821/3822 + 0010/0112/9330 explizit unter `regelversorgung_zahntechnik`.

**BEL-Regeln (kritisch):**
- BEL 809 0 (bzw. 809 8 / 810 0 / 810 8) ist je Prothese / je Kiefer **nur 1×** abrechenbar.
- **Fixator (0112) ist** bei Unterfütterung **abrechenbar**, **Artikulator (012 0/5/8) NICHT** (BEL II §5 + Erläuterungen zu 808 0/809 0).
- BEL **8010 (Grundeinheit ZE) ist KEINE eigenständige Leistung** zur Unterfütterung — nur abrechenbar, wenn zusätzlich eine Instandsetzung (Sprung/Bruch/Zahn ersetzen) erbracht wird.
- BEL 3822 (Sonderkunststoff) nur bei zahnärztlicher Indikationsstellung; je Prothese 1× zusätzlich zu 8090/8098/8100/8108.
- BEL 0023 (Verwendung von Kunststoff) max. 3× pro Fall.
- BEL 0212 (Funktionslöffel) nur bei zahnlosem Kiefer oder ≤3 Restzähnen; sonst BEL 0211 (Individueller Löffel).
- BEL 9330 (Versand) nur für gewerbliche Labore (Praxislabor: nicht abrechenbar).
- Bei implantatgestützter Prothese: BEL 0018 statt 0010 und BEL 8098 statt 8090 (bzw. 8108 statt 8100); zusätzliche Indikation Nr. 36 b ZE-RL (atrophierter zahnloser Kiefer).