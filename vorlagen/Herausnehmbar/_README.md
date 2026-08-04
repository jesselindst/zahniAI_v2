# Herausnehmbar — Übersicht

Herausnehmbarer Zahnersatz: vom Patienten entnehmbar zur Reinigung, mehrere Konstruktionsformen.

## Wann diese Hauptkategorie?

Im Konfigurator: `supplyCategory = 'removable'` (RemovableConfig.tsx).

Befund-Trigger:
- Multiple `f` (fehlende Zähne), insbes. Freiendsituation
- Zahnloser Kiefer (alle `e` / `f`) → Totalprothese
- ≤3 Zähne pro Kiefer (Befund 4.x) → Cover Denture
- Restgebiss mit ≥4 Pfeilern (Befund 3.x) → Modellguss + Teleskope

## Versorgungstypen → Sub-Ordner

| Sub-Ordner | Wann? |
|---|---|
| `Totalprothese/` | Zahnloser Kiefer (Befund 5.x) |
| `Modellguss/` | Teilprothese mit Klammern, ≥4 Pfeiler (Befund 2.x bei Freiend, 3.x bei Schaltgebiss) |
| `Klammerprothese/` | Interim/Sofortprothese als Übergangslösung |
| `FlexibleProthese/` | Valplast etc. — kleinere Schaltlücken (Privat) |
| `Kombinationsarbeit/` | Modellguss/CoverDenture mit Teleskopen, Geschieben, Stegen — Befund 3.x/4.x |
| `ImplantatProthese/` | Deckprothese auf 2-4 Implantaten — Befund-abhängig andersartig |
| `Reiseprothese/` | Zweite Prothese als Reserve (Privat) |

## OK vs. UK Differenzierung

Bei Totalprothese und Cover Denture: OK hat Palatinalplatte → unterschiedliche Abrechnung als UK. Vorlagen sind OK / UK getrennt.
Bei Modellguss: kein abrechnungsrelevanter Unterschied → keine Kiefer-Trennung.
