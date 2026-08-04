# Kombinationsarbeit — Versorgungsform-Entscheidung

Kombi aus Modellguss/CoverDenture + Teleskopen/Geschieben/Stegen.

## Versorgungsform-Tabelle

| Versorgungsform | Konstruktion |
|---|---|
| `Regelversorgung/` | NEM-Teleskope + Modellguss (Befund 3.x) ODER NEM-Teleskope + CoverDenture (Befund 4.x) |
| `gleichartig/` | Premium-Material (Zirkon-Teleskop, Galvano), Geschiebe oder Steg auf nat. Zähnen |
| `Privatleistung/` | PKV oder Privatwunsch (Sekundärkonus etc.) |

**Andersartig nur bei Implantat-Versorgung**: Wenn statt Modellguss/CoverDenture eine Implantat-Prothese gewählt wird → `../ImplantatProthese/andersartig/`.

## Befundklassen-Mapping (Regelversorgung)

| Befund | Wann? | Versorgung |
|---|---|---|
| **3.x** | Restgebiss mit ≥4 Pfeilerzähnen | Modellguss + NEM-Teleskope |
| **4.x** | ≤3 Zähne pro Kiefer | Cover Denture + NEM-Teleskope/Wurzelstiftkappen |

## Klassifizierungs-Regel: CAD-CAM bei Teleskopen

**Zirkon-/CAD-CAM-Teleskope = automatisch gleichartig** (BEL II 2014: gefräste Versorgungen sind nicht-BEL).

## Klassifizierungs-Regel: Cover Denture mit Metallbasis (Edge-Case)

**Mit medizinischer Indikation** (Torus Palatinus, Würgereiz, Allergie) → Festzuschuss 4.5 + BEMA 98e → bleibt **Regelversorgung**.

**Ohne medizinische Indikation** (nur Patientenwunsch) → `gleichartig/`.

## Entscheidungsbaum

1. **PKV oder Privatwunsch?** → `Privatleistung/`
2. **Implantat-getragene Prothese statt nat. Pfeiler?** → `../ImplantatProthese/`
3. **GKV mit HKP**:
   - **Zirkon-Teleskop / Galvano-Teleskop?** → `gleichartig/`
   - **Geschiebe oder Steg auf natürlichen Zähnen?** → `gleichartig/`
   - **Cover Denture mit Metallbasis ohne med. Indikation?** → `gleichartig/`
   - **NEM-Teleskop + Modellguss (Befund 3.x)?** → `Regelversorgung/NEM_Teleskop_Modellguss_{OK|UK}.md`
   - **NEM-Teleskop + CoverDenture (Befund 4.x)?** → `Regelversorgung/NEM_Teleskop_CoverDenture_{OK|UK}.md`
