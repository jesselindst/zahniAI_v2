# Festsitzend — Übersicht

Festsitzender Zahnersatz: alle Versorgungen, die fest am Zahn / Implantat verbleiben (nicht herausnehmbar).

## Wann diese Hauptkategorie?

Im Konfigurator: `supplyCategory = 'fixed'` (FixedConfig.tsx).

Befund-Trigger:
- Befund `k` (vorhandene Krone defekt) → Krone neu
- Befund `f` mit Schaltlücke + ausreichend Pfeilern → Brücke
- Befund `wf` (wurzelbehandelt) + zerstörter Zahn → Stiftaufbau + Krone
- Befund `r` / `w` (Wurzelrest) → Stiftaufbau + Krone (oder Extraktion + Brücke)

## Versorgungstypen → Sub-Ordner

| Sub-Ordner | Wann? |
|---|---|
| `Einzelkrone/` | Einzelner präparierter Zahn, Versorgung mit Vollkrone |
| `Teilkrone/` | Teilbedeckung des Zahns (kein voller Krone-Umfang) |
| `Inlay/` | Defekt mit Wandbeteiligung, gegossener/keramischer Einsatz |
| `Onlay/` | Höckerüberkronung ohne komplette Vollkrone |
| `Veneer/` | Verblendschale labial (rein ästhetisch, ggf. mediz. Indikation) |
| `Teleskopkrone/` | Pfeiler einer kombinierten Versorgung (siehe `Herausnehmbar/Kombinationsarbeit/`) |
| `Stiftaufbau/` | Vorbereitung wurzelbehandelter Zahn vor Krone |
| `Bruecke/` | Lückenversorgung über min. 2 Pfeilerzähne |
| `Adhaesivbruecke/` | Klebebrücke mit ein-/zweiflügeliger Anhaftung (meist Frontzahnbereich) |

## Klassifizierungs-Hinweise

Beim Auswählen des Versorgungstyps lies das jeweilige `_README.md` darin (z.B. `Einzelkrone/_README.md`) — dort ist die Versorgungsform-Logik beschrieben (Regelversorgung vs. gleichartig vs. andersartig vs. Privatleistung).

**Generelle Regel für Festsitzend bei GKV:**
- BEL-Standard (NEM, vestibulär verblendet innerhalb VG) = Regelversorgung
- Premium-Material/Verfahren (CAD-CAM, Zirkon, Galvano, EM) = gleichartig
- Anderer ZE-Typ als Befund vorgibt (Implantat statt Brücke, Freiendbrücke statt Modellguss) = andersartig
