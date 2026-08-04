| Bereich | Autor | erstellt am | Version |
|--------|--------|--------|--------|
| Reparatur / Unterfütterung / Regelversorgung | CLAUDE | 2026-04-27 | v1 |

# BEL-Positionen

| BEL | Leistung | Menge | Bemerkung |
|--------|--------|--------|--------|
| 0010 | Modell | 1 | Gegenbiss-/Konter-/Unterfütterungsmodell; je Kontrollmodell zusätzlich abrechenbar |
| 0018 | Modell bei Implantatversorgung | 1 | alternativ zu 0010 bei implantatgestützter Prothese (Nr. 36b ZE-RL) |
| 0023 | Verwendung von Kunststoff | 1 | bei Sonderdarstellung individueller Primärteile / Zahnfleischpartien (max. 3×); aus FZ-RL 6.6/6.7 |
| 0211 | Individueller Löffel | 1 | alternativ zu 0212 bei >3 Restzähnen oder ohne Funktionsabformung |
| 0212 | Funktionslöffel | 1 | bei funktioneller Randgestaltung (zahnloser Kiefer oder ≤3 Restzähne) |
| 0112 | Fixator | 1 | je Unterfütterung; Bisslagen-Fixierung (Artikulator 012 0 NICHT abrechenbar bei Unterfütterung) |
| 8010 | Grundeinheit ZE | 1 | NUR wenn gleichzeitig zur Unterfütterung weitere Instandsetzung erbracht wird — Unterfütterung selbst löst KEINE 8010 aus |
| 8090 | Vollständige Unterfütterung | 1 | je Prothese; alternative Abrechnung bei weichbleibender Vollunterfütterung an Bestandsbasis (zzgl. 3821) |
| 8098 | Vollständige Unterfütterung/implantatgestützte Basis | 1 | alternativ zu 8090 bei implantatgestützter Basis (auch Nr. 36 b ZE-RL) |
| 8100 | Prothesenbasis erneuern | 1 | **Hauptposition** bei weichbleibender Vollunterfütterung (BEL II 810 0 beschreibt explizit "vollständige weichbleibende Unterfütterung") oder Rebasierung |
| 8108 | Prothesenbasis erneuern/Implantatversorgung | 1 | alternativ zu 8100 bei implantatgestützter Prothese (Nr. 36 b ZE-RL) |
| 3821 | Weichkunststoff | 1 | je Prothese; Pflicht-Folgeleistung zu 8090/8098/8100/8108 bei Verarbeitung von Weichkunststoff |
| 3822 | Sonderkunststoff | 1 | je Prothese; alternativ zu 3821 bei zahnärztlicher Indikationsstellung für Sonderkunststoff statt Weichkunststoff |
| 9330 | Versandkosten | 2 | je Versandgang (nur gewerbliche Labore); Hin-/Rückversand |

# Basisleistungen

_Pflicht-Kern ist vollständig über BEL abgedeckt. Keine zusätzlichen BEB97-Basisleistungen erforderlich._

# Zusatzleistungen

| BEB97 | Leistung | Menge | Bemerkung |
|--------|--------|--------|--------|
| 0732 | Desinfektion | 2 | je Vorgang (Eingang/Ausgang) |
| 0706 | Foto- oder Video-Dokumentation | 1 | bei Bedarf (postop. Verlauf, Atrophie-Dokumentation) |
| 0710 | Eilterminzuschlag | 1 | bei urgency=urgent/express |
| 0721 | Zeiteinheit; Zahntechniker-Meister | je | je 15 Min für nicht in BEB erfasste Leistungen |
| 0722 | Zeiteinheit; Zahntechniker | je | je 15 Min für nicht in BEB erfasste Leistungen |

# Material

| Material | Menge | Bemerkung |
|--------|--------|--------|
| Weichbleibender Kunststoff (z.B. Mollosil) | — | für sensible Schleimhaut |
| Modellgips (Hartgips) | — | für Modell und Konter |
| Funktionslöffel-Kunststoff | — | nur bei 0211/0212 |
| Desinfektionsmittel | — | nach Herstelleranweisung |

# Hinweise

Vollständige Unterfütterung mit weichbleibendem Material — Regelversorgung. Indikation: sensible Schleimhaut, postoperativ (z.B. nach Extraktionen, Implantatchirurgie), dünner Alveolarkamm. Hinweis: Weichkunststoff hat kürzere Lebensdauer als Heiß-/Kaltpolymerisat (typisch 6-12 Monate).

**Festzuschuss:** Befund **6.7** "Verändertes Prothesenlager bei erhaltungswürdigem totalem Zahnersatz oder schleimhautgetragener Deckprothese, je Kiefer" (FZ-RL 2024-11-21) bzw. **6.6** bei Teil-Zahnersatz. Beide Befunde listen 8080/8090/8100 + 3821/3822 + 0010/0112/9330 explizit unter `regelversorgung_zahntechnik`.

**BEL-Regeln (kritisch):**
- **BEL 810 0 (Prothesenbasis erneuern)** beschreibt **explizit** "vollständige weichbleibende Unterfütterung" — primäre Position. Alternativ BEL 8090 + 3821 bei weichbleibender Vollunterfütterung an Bestandsbasis.
- BEL 3821 (Weichkunststoff) ist **je Prothese 1×** Folgeleistung zu 8090/8098/8100/8108.
- BEL 3822 (Sonderkunststoff) alternativ zu 3821 nur bei zahnärztlicher Indikationsstellung; je Prothese 1×.
- BEL 0023 (Verwendung von Kunststoff) max. 3× pro Fall.
- Alle Unterfütterungspositionen je Prothese / je Kiefer **nur 1×** abrechenbar.
- **Fixator (0112) ist** bei Unterfütterung **abrechenbar**, **Artikulator (012 0/5/8) NICHT**.
- BEL **8010 (Grundeinheit ZE)** ist nur abrechenbar bei zusätzlicher Instandsetzung — nicht für die Unterfütterung selbst.
- BEL 0212 nur bei zahnlosem Kiefer / ≤3 Restzähne; sonst BEL 0211.
- BEL 9330 nur für gewerbliche Labore.
- Bei implantatgestützter Prothese: BEL 0018 statt 0010, BEL 8098/8108 statt 8090/8100.