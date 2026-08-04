# Reparatur — Übersicht

Reparaturen, Erweiterungen, Unterfütterungen und Reinigungen von herausnehmbarem ZE.

## Wann diese Hauptkategorie?

Im Konfigurator: `supplyCategory = 'repair'` (RepairConfig.tsx).

Patient hat eine bestehende Prothese, die instand gesetzt werden muss (nicht: Neuanfertigung).

## Versorgungstypen → Sub-Ordner

| Sub-Ordner | Wann? |
|---|---|
| `Prothesenreparatur/` | Bruch, Riss, Sprung der Prothesenbasis oder eines Zahns |
| `Klammerreparatur/` | Verbogene/abgebrochene Klammer neu anfertigen |
| `Erweiterung/` | Zusätzlichen Zahn ergänzen (z.B. nach Extraktion) |
| `Unterfuetterung/` | Spaltbildung Prothese-Schleimhaut (Atrophie) |
| `Reinigung/` | Maschinelle Reinigung + Politur |

## Versorgungsform-Logik

**Wenn Reparatur an GKV-Regelversorgung-Prothese**: `Regelversorgung/` (BEL).
**Wenn Reparatur an Privat-/PKV-Prothese**: `Privatleistung/` (BEB/GOZ).

**Hinweis**: Materialwahl bei Unterfütterung ist abrechnungsrelevant:
- Heißpolymerisation = dauerhaft, höher abrechenbar
- Kaltpolymerisation = Standard
- Weichbleibend = bei sensibler Schleimhaut

Auch Scope (Vollständig vs. Partiell) ist abrechnungsrelevant.
