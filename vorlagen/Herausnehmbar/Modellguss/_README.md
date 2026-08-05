# Modellguss — Versorgungsform-Entscheidung

Klammerverankerte Teilprothese mit gegossenem Metallgerüst.

## Festzuschuss-Befunde

| Befund | Situation |
|---|---|
| **3.1** | Alle zahnbegrenzten Lücken, die nicht 2.1–2.5 oder 4 entsprechen, **oder Freiendsituationen** (Lückensituation II) — **je Kiefer**. Das ist der tragende Modellguss-Befund; die Metallbasis (BEL 2010) ist im Leistungsumfang enthalten. |
| **+3.2** | Zuschlag bei verkürzter Zahnreihe (beidseitig bis Eckzahn/1. Prämolar bzw. einseitig), max. 2× je Kiefer |

**Nicht 2.7** — das ist der Verblendzuschuss je ersetztem Zahn im Verblendbereich und betrifft festsitzenden Zahnersatz, nicht das Modellgussgerüst.

**Achtung Abgrenzung:** Bei den Lückenbefunden **2.1–2.5** ist die Regelversorgung eine **Brücke**. Ein Modellguss ist dort fachlich **andersartig** — für diesen Fall existiert im Bestand noch keine Zielvorlage (`andersartig/` fehlt).

## Versorgungsform-Tabelle

| Versorgungsform | Material/Verfahren |
|---|---|
| `Regelversorgung/` | CoCr-Gerüst, gegossen (Standard-BEL) |
| `gleichartig/` | Titan-Gerüst, CAD-CAM gefrästes Gerüst |
| `Privatleistung/` | PKV, ohne HKP oder Komplett-Privatwunsch |

CAD-CAM-Fertigung ist gleichartig, weil BEL 2010 (Metallbasis) den Gussweg voraussetzt — bei gefrästem Gerüst entfallen die gussgebundenen BEL-Positionen, der Gerüstanteil läuft über BEB.

## Sattelform ist abrechnungsrelevant

- `Freiend` (free_end) — Lückensituation II, Befund 3.1
- `Schaltprothese` (switch) — nur Schaltlücken; bei 2.1–2.5 andersartig (s. o.)
- `Kombiniert` (combi) — Freiend + Schaltlücke

Pro Sattelform eine eigene Vorlage.

## Entscheidungsbaum

1. **PKV, kein HKP oder Komplett-Privatwunsch?** → `Privatleistung/`
2. **GKV mit HKP**:
   - **Lücke entspricht Befund 2.1–2.5 (Brücke wäre Regelversorgung)?** → andersartige Versorgung, Direktabrechnung GOZ, Kasse erstattet den Festzuschuss an den Versicherten
   - **Titan oder CAD-CAM-CoCr?** → `gleichartig/` (Festzuschuss 3.1 bleibt, Mehrkosten privat)
   - **CoCr gegossen?** → `Regelversorgung/{Sattelform}.md`
