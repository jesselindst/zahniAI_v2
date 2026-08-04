# Modellguss — Versorgungsform-Entscheidung

Teilprothese mit Klammern, ≥4 Pfeilerzähne (Befund 2.x bei Freiend, 3.x bei Schaltgebiss).

## Versorgungsform-Tabelle

| Versorgungsform | Material/Verfahren |
|---|---|
| `Regelversorgung/` | CoCr-Gerüst (Standard-BEL) |
| `gleichartig/` | Titan-Gerüst, CAD-CAM gefrästes Gerüst |
| `Privatleistung/` | PKV oder Privatwunsch |

**Andersartig nur wenn ZE-Typ-Wechsel**: z.B. Brücke statt Modellguss = `Festsitzend/Bruecke/andersartig/Freiend...`.

## Saddle-Type ist abrechnungsrelevant

- `Freiend` (free_end) — Befundklasse 2.7
- `Schaltprothese` (switch) — Schaltlücke
- `Kombiniert` (combi) — Kombination Freiend + Schalt

Pro Saddle-Type eigene Vorlage.

## Entscheidungsbaum

1. **PKV oder Privatwunsch?** → `Privatleistung/`
2. **GKV**:
   - **Titan oder CAD-CAM-CoCr?** → `gleichartig/`
   - **CoCr Standard?** → `Regelversorgung/{SaddleType}.md`
