# Totalprothese — Versorgungsform-Entscheidung

Komplettprothese im zahnlosen Kiefer.

## Festzuschuss-Befunde

| Befund | Situation |
|---|---|
| **4.2** | Zahnloser Oberkiefer |
| **4.4** | Zahnloser Unterkiefer |
| **4.1 / 4.3** | Restzahnbestand bis 3 Zähne (OK / UK) — Zähne werden im Rahmen der Versorgung entfernt |
| **+4.5** | Zuschlag je Kiefer bei notwendiger Metallbasis |

Nicht 5.x — die Befundklasse 5 ist die **Interimsversorgung** bei Lückengebiss (5.1: bis 4 fehlende Zähne, 5.2: 5–8 fehlende Zähne je Kiefer), nicht die Totalprothese.

## Versorgungsform-Tabelle

| Versorgungsform | Material/Verfahren |
|---|---|
| `Regelversorgung/` | PMMA-Kalt + Standard-Kunststoffzähne |
| `gleichartig/` | PMMA-Heiß, Premium-Kunststoffzähne, Keramikzähne, PMMA-Injekt, CAD-CAM gefräst, 3D-gedruckt, Gaumenfrei mit Bügel ohne mediz. Indikation |
| `Privatleistung/` | nur bei PKV, ohne HKP oder ausdrücklichem Komplett-Privatwunsch |

**Wichtig:** CAD-CAM, 3D-Druck, PMMA-Injekt und Keramikzähne sind bei GKV-Versicherten mit Heil- und Kostenplan **gleichartige Versorgung mit Festzuschuss 4.2/4.4** — nicht automatisch Privatleistung. Die Privatleistungs-Vorlagen gelten nur ohne GKV-Anspruch.

**Keine andersartig**: Wenn statt Totalprothese eine Implantatprothese gewählt wird → `../ImplantatProthese/`.

## OK vs. UK

OK und UK sind getrennte Vorlagen — wegen Palatinalplatte (nur OK) und UK-Sonderregeln (Beschwerungseinlage statt Saugkammer).

## Klassifizierungs-Regel: Metallbasis

**Mit medizinischer Indikation** → bleibt **Regelversorgung**, Zuschlag Befund **4.5** je Kiefer + BEMA 98e, Indikation dokumentieren. Die Zahnersatz-Richtlinie nennt als Ausnahmefälle insbesondere Torus palatinus und Exostosen.
*(VERIFIZIEREN: Ausgeprägter Würgereiz und Acrylat-Allergie standen bisher als gesicherte Indikationen im README — in der Richtlinie sind sie so nicht benannt. Vor Aktivierung fachlich klären.)*

**Ohne medizinische Indikation** → **gleichartig** (`gleichartig/PMMA-heiss_Gaumenfrei-Buegel_OK.md`): Festzuschuss in Höhe der Regelversorgung, Mehrkosten privat.

## Entscheidungsbaum

1. **PKV, kein HKP oder Komplett-Privatwunsch?** → `Privatleistung/`
2. **GKV mit HKP**:
   - **Metallbasis mit medizinischer Indikation?** → `Regelversorgung/` (Befund 4.2/4.4 + 4.5, BEMA 98e dokumentieren)
   - **Heißpolymerisation, Premium-/Keramikzähne, PMMA-Injekt, CAD-CAM, 3D-Druck ODER Metallbasis ohne Indikation?** → `gleichartig/` (Festzuschuss 4.2/4.4 bleibt, Mehrkosten privat)
   - **Standard PMMA-Kalt + Standard-Zähne?** → `Regelversorgung/`
