# Totalprothese — Versorgungsform-Entscheidung

Komplettprothese im zahnlosen Kiefer (Befund 5.x).

## Versorgungsform-Tabelle

| Versorgungsform | Material/Verfahren |
|---|---|
| `Regelversorgung/` | PMMA-Kalt + Standard-Kunststoffzähne |
| `gleichartig/` | PMMA-Heiß, Premium-Kunststoffzähne, Gaumenfrei mit Bügel (ohne mediz. Indikation) |
| `Privatleistung/` | CAD-CAM gefräst, 3D-gedruckt, Keramikzähne, PMMA-Injekt |

**Keine andersartig**: Wenn statt Totalprothese ein Implantat-Prothese gewählt wird → `../ImplantatProthese/`.

## OK vs. UK

OK und UK sind getrennte Vorlagen — wegen Palatinalplatte (nur OK).

## Klassifizierungs-Regel: Metallbasis (Edge-Case)

Wenn Patient eine Metallbasis (Bügel, Platte) bekommt:

**Mit medizinischer Indikation** → bleibt **Regelversorgung**:
- Torus Palatinus (Knochenwucherung am Gaumen)
- Ausgeprägter Würgereiz
- Dokumentierte Allergie auf Acrylate
- Festzuschuss 4.5 + BEMA 98e
- Dokumentation der Indikation erforderlich

**Ohne medizinische Indikation** → **gleichartig** (`gleichartig/PMMA-heiss_Gaumenfrei-Buegel_OK.md`):
- Reiner Patientenwunsch nach gaumenfreier Gestaltung
- Festzuschuss in Höhe Regelversorgung-Totalprothese
- Mehrkosten privat

## Entscheidungsbaum

1. **PKV oder Privatwunsch?** → `Privatleistung/`
2. **GKV**:
   - **CAD-CAM, 3D-gedruckt, PMMA-Injekt, Keramikzähne?** → `Privatleistung/`
   - **Metallbasis mit medizinischer Indikation?** → bleibt `Regelversorgung/` (mit Festzuschuss 4.5 + BEMA 98e dokumentieren)
   - **Heißpolymerisation, Premium-Zähne ODER Metallbasis ohne Indikation?** → `gleichartig/`
   - **Standard PMMA-Kalt + Standard-Zähne?** → `Regelversorgung/`
