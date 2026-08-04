# Bruecke Regelversorgung — Permutations-Auswahl

NEM-Brücke als BEL-Standard, Spannweite als Repräsentanten.

## Files in diesem Ordner

| File | Spannweite | Verblendung | Position |
|---|---|---|---|
| `NEM_vestibulaer_3gliedrig.md` | 3-gliedrig | vestibulär | innerhalb VG |
| `NEM_vestibulaer_4gliedrig.md` | 4-gliedrig | vestibulär | innerhalb VG |
| `NEM_unverblendet_3gliedrig.md` | 3-gliedrig | unverblendet | Molarenbereich |
| `NEM_unverblendet_grossspannig.md` | 5+gliedrig | unverblendet | Molarenbereich |

## Spannweite ableiten

Spannweiten >4-gliedrig: nutze `_grossspannig.md` als Basis und multipliziere Glieder-Positionen entsprechend Anzahl Brückenglieder.

## Verblendgrenzen-Logik

Bei Mischbrücken (z.B. 13-17 — vom Frontzahn bis Molar): innerhalb VG (13-15) vestibulär verblendet, außerhalb VG (16-17) unverblendet → kombinierte BEL-Positionen pro Glied. Wenn Patient Vollverblendung über alle Glieder wünscht → wechselt zu `gleichartig/Zirkon_voll_grossspannig.md` etc.
