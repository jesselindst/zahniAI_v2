# Vorlagen — Abrechnungs-Vorlagen für ZahniAI

Generische Abrechnungsvorlagen für die KI-gestützte Kostenvoranschlag-Erstellung, strukturiert als Decision-Tree: Jede Ordnerebene hat eine `_README.md` als Entscheidungshilfe; Klassifizierung (Regelversorgung/gleichartig/andersartig/Privatleistung) passiert in den READMEs VOR der Wahl der konkreten Vorlage. Die Vorlagen selbst enthalten nur Abrechnungsinhalt (Festzuschuss-Block, BEL-/BEB-Tabellen, Material, Hinweise).

## Hauptkategorien (Top-Level)

| Hauptkategorie | Wann? |
|---|---|
| `Festsitzend/` | Krone, Brücke, Inlay/Onlay/Veneer, Teleskop, Stiftaufbau, Adhäsivbrücke |
| `Herausnehmbar/` | Total-/Teilprothese, Modellguss, Kombi-Versorgung, Implantat-Prothese |
| `Implantat/` | Suprakonstruktionen (Krone, Brücke, Locator, Steg) |
| `Schienen/` | Aufbiss-, Schnarcher-/UKPS-, Bleaching-, Sport-, Retainer-, CMD-Schiene |
| `Reparatur/` | Prothesen-/Klammerreparatur, Erweiterung, Unterfütterung, Reinigung |
| `Provisorium/` | Einzelzahn-, Brücken-, Langzeit-, Tabletop-Provisorium |

## Versorgungsformen

| Form | BEL? | BEB? | Festzuschuss |
|---|:-:|:-:|---|
| `Regelversorgung/` | ✅ | ❌ | 60 % (Bonus 70/75 %; Härtefall: tatsächliche RV-Kosten voll) |
| `gleichartig/` | ✅ (RV-Anteil) | ✅ (Mehrleistung) | wie Regelversorgung; Mehrkosten privat (§ 9 GOZ) |
| `andersartig/` | ❌ | ✅ | FZ-Erstattung an Versicherten; Direktabrechnung GOZ |
| `Privatleistung/` | ❌ | ✅ (oder GOZ) | kein Festzuschuss-Antrag |
| `Sonderfaelle/` | ✅ | je nach Fall | Suprakonstruktion als RV nur in ZE-RL-36-Fällen |

## Schlüssel-Klassifizierungs-Regeln (Quick-Reference)

| Regel | Konsequenz |
|---|---|
| **CAD-CAM gefräste Krone/Brücke** | gleichartig — BEL-Kronen-/Brückenpositionen setzen Gusstechnik voraus (gRS zum BEL II-2014); gilt NICHT für Schienen |
| **Verblendgrenzen** OK 15–25, UK 34–44 (ZE-RL Nr. 20/25) | innerhalb vestibulär verblendet = Regelversorgung (+Zusatzbefund 1.3/2.7/4.7); außerhalb oder vollverblendet = gleichartig |
| **Inlay/Onlay/Veneer** | Privatleistung; kein ZE-Festzuschuss (ggf. Kassenanteil in Höhe der Regel-Füllung über KCH-Mehrkostenregelung) |
| **Stiftaufbau** | gegossen metallisch = Regelversorgung (Befund 1.5); konfektioniert metallisch = Regelversorgung (Befund 1.4); Glasfaser = gleichartig; Zirkon/Carbon = Privatleistung |
| **Adhäsivbrücke** (Befunde 2.1/2.2 + 2.7) | Metallgerüst, einspannig, Schneidezahnersatz: 1 Zahn = Regelversorgung ohne Altersgrenze; 2 nebeneinander fehlende Zähne = Regelversorgung nur 14.–20. Lj.; Keramikgerüst = gleichartig |
| **Aufbissschiene** BEL 4010 (adjustiert) / 4020 (nicht adjustiert) | verfahrensoffen (Tiefziehen, CAD-CAM, 3D-Druck) — aber regionale KZV-Unterschiede beachten (z. B. Berlin restriktiv; Bayern mit Vermerk „digitale Abformung", dann ohne Modellpositionen) |
| **UKPS** (Schlafapnoe) | GKV-Leistung (G-BA 2021), abrechenbar seit 01.01.2022 als Zweitlinie nach CPAP; NUR UKPS-gekennzeichnete BEL-Positionen (0015 … 9335) + BEMA UP1–UP6 |
| **Implantat-Suprakonstruktion** | grundsätzlich andersartig; Regelversorgung nur ZE-RL Nr. 36 (zahnbegrenzte Einzelzahnlücke → Krone; atrophierter zahnloser Kiefer → Totalprothesen-Niveau); Befundklasse 7 NUR für Erneuerung/Wiederherstellung |
| **Freiendbrücke** | andersartig (Regelversorgung wäre Modellguss) |
| **3D-gedruckte/gefräste Modelle** | nicht über BEL 0010/005x (Gips vorausgesetzt) — bei Intraoralscan-Route modellfrei oder privat |

## Naming-Schema (Filename)

`{Material}_{Verfahren}_{Verblendung}_{Region/Kiefer}_{Spannweite}_{Besonderheit}.md`

- Ordner kodieren Hauptkategorie/Versorgungstyp/Versorgungsform — nicht im Filename wiederholen
- Nur abrechnungsrelevante Permutationen; Spannweiten als Repräsentanten (3-, 4-, grossspannig, Freiend) — Agent leitet konkrete Spannweite ab
- OK/UK nur wenn abrechnungsrelevant verschieden

**Kanonische Terme:** `NEM`, `EM`, `Zirkon`, `LiSi`, `VMK-EM`, `VMK-NEM`, `CAD-CAM`, `OK`/`UK`, `3D-gedruckt`, `mit-Geschiebe`. Trenner `_`, innerhalb Tokens ASCII-Hyphen, keine Spaces/Doppel-`_`.
