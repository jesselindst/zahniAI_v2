# Implantat — Übersicht

Suprakonstruktionen auf Implantaten: einzelne Implantat-Kronen/-Brücken sowie Verbindungselemente (Locator, Steg, Teleskop) für Implantat-Prothesen.

## Wann diese Hauptkategorie?

Im Konfigurator: `supplyCategory = 'implant'` (ImplantConfig.tsx).

**Wichtig:** Diese Hauptkategorie deckt nur die SUPRAKONSTRUKTION ab. Implantatchirurgie (Insertion, Augmentation, Bohrschablone) ist separat über GOZ.

Befund-Trigger:
- `i` (Implantat vorhanden, ohne Suprakonstruktion)
- `f` mit Patientenwunsch Implantat statt Brücke/Prothese

## Versorgungstypen → Sub-Ordner

| Sub-Ordner | Wann? |
|---|---|
| `KroneVerschraubt/` | Krone direkt verschraubt mit Implantat (mit Schraubenkanal) |
| `KroneZementiert/` | Krone zementiert auf Abutment |
| `BrueckePfeiler/` | Implantat-Brücke mit ≥2 Implantatpfeilern |
| `Locator/` | Patrize zur Verankerung Deckprothese (siehe `Herausnehmbar/ImplantatProthese/`) |
| `Steg/` | Stegkonstruktion zwischen Implantaten |
| `TeleskopAufImplantat/` | Primär-/Sekundärteleskop auf Implantat |

## Versorgungsform-Logik (alle Implantat-Versorgungen)

**Standardfall** (häufigster Fall):
- Implantat-Suprakonstruktion = `andersartig`
- Patient bekommt Festzuschuss in Höhe Krone-/Brücke-Regelversorgung
- Implantat selbst privat (GOZ + Material)

**Ausnahmeindikationen** (5 Fälle nach §28 Abs.2 SGB V):
1. Größere Kiefer-/Gesichtsdefekte (Tumor-OP, Trauma)
2. Operationen nach großen Zysten (follikuläre, Keratozysten)
3. Operationen nach Osteopathien
4. Angeborene Kieferdefekte (LKG-Spalte, ektodermale Dysplasie)
5. Unfälle

→ Sub-Ordner `Sonderfaelle/` nutzen. Implantat als Sachleistung. Suprakonstruktion nach ZE-RL §36a/b als Regelversorgung oder gleichartig.

**Zusätzliche Bedingung Sonderfall**: konventioneller ZE NICHT möglich (Restkamm nicht belastbar).

**PKV oder Privatwunsch**: `Privatleistung/`.
