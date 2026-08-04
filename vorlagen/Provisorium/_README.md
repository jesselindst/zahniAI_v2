# Provisorium — Übersicht

Vorübergehende Versorgungen während HKP-Behandlung oder bei Implantat-Einheilung.

## Wann diese Hauptkategorie?

Im Konfigurator: `supplyCategory = 'provisional'` (ProvisionalConfig.tsx).

## Versorgungstypen → Sub-Ordner

| Sub-Ordner | Wann? |
|---|---|
| `Einzelzahn/` | Provisorische Krone, HKP-begleitend |
| `Bruecke/` | Provisorische Brücke, HKP-begleitend |
| `Langzeit/` | Tragzeit > 6 Monate (z.B. Implantat-Einheilung) |
| `ProvKroneLabor/` | Laborgefertigte Provisorische Krone (höherwertig als chairside) |
| `Tabletop/` | Bisshebung-Provisorium auf Okklusalfläche |

## Versorgungsform-Logik

**Provisorium während HKP-Behandlung** (kurze Tragzeit, PMMA-Standard):
- `Einzelzahn/Regelversorgung/` und `Bruecke/Regelversorgung/` (BEMA + BEL)

**Höherwertige Provisorien** (CAD-CAM, PEEK, Metallarmiert):
- `Privatleistung/` (BEB / GOZ)

**Langzeitprovisorium** (>6 Monate):
- Immer Privatleistung (GKV deckt Langzeit-Lösung nicht)

**Tabletop**: immer Privatleistung (Bisshebung ist nicht GKV-Standard).
