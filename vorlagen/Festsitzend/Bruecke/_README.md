# Bruecke — Versorgungsform-Entscheidung

Lückenversorgung über min. 2 Pfeilerzähne (oder Implantatpfeiler — siehe `Implantat/BrueckePfeiler/`).

## Versorgungsform-Tabelle

| Versorgungsform | Material/Konstruktion |
|---|---|
| `Regelversorgung/` | NEM-Gerüst (BEL), vestibulär verblendet (innerhalb VG) ODER unverblendet (außerhalb VG) |
| `gleichartig/` | Premium-Material (Zirkon, LiSi, EM, VMK, Galvano) ODER CAD-CAM ODER großspannig mit Geschiebe |
| `andersartig/` | ZE-Typ-Wechsel: Freiendbrücke statt Freiend-Modellguss |
| `Privatleistung/` | PKV oder Privatwunsch |

## Entscheidungsbaum

1. **PKV oder Privatwunsch?** → `Privatleistung/`
2. **Freiendsituation: Brücke statt Modellguss gewählt?** → `andersartig/` (ZE-Typ-Wechsel)
3. **GKV mit HKP**:
   - **CAD-CAM gefräst (egal welches Material)?** → `gleichartig/`
   - **Premium-Material (Zirkon, LiSi, EM, VMK, Galvano)?** → `gleichartig/`
   - **Großspannig (5+ Glieder) mit Geschiebe-Brückenteilung?** → `gleichartig/`
   - **NEM, vestibulär innerhalb VG (3-/4-gliedrig Schaltbrücke)?** → `Regelversorgung/NEM_vestibulaer_3gliedrig.md` (oder _4gliedrig)
   - **NEM, unverblendet im Molarenbereich?** → `Regelversorgung/NEM_unverblendet_3gliedrig.md`

## Klassifizierungs-Regel: Wann ist eine Brücke andersartig?

Eine Brücke ist andersartig, wenn die Regelversorgung-Definition für den Befund einen ANDEREN ZE-Typ vorsieht.

**Freiendbrücke** (einseitig nur Pfeiler, freies Ende ohne Pfeiler):
- Bei Freiendsituation ist die Regelversorgung der **Modellguss** (oder Implantat-Festzuschuss)
- Wird stattdessen eine Brücke gewählt → ZE-Typ-Wechsel → andersartig
- Patient erhält Festzuschuss in Höhe Regelversorgung-Modellguss
- Reine BEB-Abrechnung, kein BEL-Anteil

**Edge-Case: Großspannige Brücke mit Geschiebe**
- Wenn Befund Brücke vorgibt → gleichartig (siehe `gleichartig/Zirkon_voll_grossspannig_mit-Geschiebe.md`)
- Wenn Befund eigentlich Cover Denture/Modellguss vorgibt → andersartig (ZE-Typ-Wechsel)

## Verblendgrenzen GKV

OK 15-25, UK 34-44 (siehe `../Einzelkrone/_README.md` für Details). Bei Brücken auch Brückenglieder: Verblendgrenzen gelten pro Glied. Bei Mischbrücken (Front + Molar) → kombinierte BEL-Positionen pro Glied.

## Spannweite

Vorlagen sind als **Repräsentanten** angelegt: 3gliedrig, 4gliedrig, grossspannig, Freiend. Der Agent leitet spezifische Spannweiten (5-, 6-, ..., 14-gliedrig) selbst ab durch Multiplikation der Glieder-Positionen.
