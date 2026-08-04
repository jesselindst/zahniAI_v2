| Bereich | Autor | erstellt am | Version |
|--------|--------|--------|--------|
| festsitzender Zahnersatz / Brücke / Regelversorgung | CLAUDE | 2026-04-26 | v1 |

# BEL-Positionen

| BEL | Leistung | Menge | Bemerkung |
|--------|--------|--------|--------|
| 0010 | Modell | 2 | Arbeitsmodell + Gegenkiefermodell |
| 0023 | Verwendung von Kunststoff | 1 | für Stumpfmodelle |
| 0051 | Sägemodell | 1 |  |
| 0052 | Einzelstumpfmodell | je | je Pfeilerstumpf alternativ |
| 0053 | Modell nach Überabdruck | je | bei Reposition |
| 0120 | Mittelwertartikulator | 1 |  |
| 0240 | Übertragungskappe Kunststoff/Metall | je | je Pfeiler bei Stumpfreposition |
| 0310 | Provisorische Krone/Brückenglied | je | bei laborgefertigtem Provisorium |
| 1024 | Krone für vestibuläre Verblendung | 2 | je Anker; bei N-gliedrig: Anzahl Pfeilerzähne |
| 1100 | Brückenglied | 1 | je Zwischenglied; bei 4-gliedrig 2, bei N-gliedrig (N − Anzahl Anker) |
| 1550 | Konditionierung je Zahn/Flügel | je | bei Verblendung-Vorbereitung Komposit/Kunststoff |
| 1600 | Vestibuläre Verblendung Kunststoff | je | alternativ Kunststoffverblendung vestibulär |
| 1610 | Zahnfleisch Kunststoff | je | je Brückenglied Gingiva-Kunststoff alternativ zu Keramik |
| 1620 | Vestibuläre Verblendung Keramik | 3 | je Glied (Anker + Brückenglied) gesamt; alternativ BEL 1600 (Verblendung Kunststoff) |
| 1630 | Zahnfleisch Keramik | 1 | je Brückenglied (Gingiva-Anteil) |
| 1500 | Metallverbindung nach Brand | je | bei Lötstelle nach Brand |
| 9700 | Verarbeitungsaufwand NEM-Legierung | 3 | je Element (Anker + Brückenglied) |
| 9330 | Versandkosten | 2 | Hin- + Rückversand, entfällt bei Praxislabor |

# Basisleistungen

_Pflicht-Kern ist vollständig über BEL abgedeckt. Keine zusätzlichen BEB97-Basisleistungen erforderlich._

# Zusatzleistungen

| BEB97 | Leistung | Menge | Bemerkung |
|--------|--------|--------|--------|
| 0723 | Zahnfarbenbestimmung I | 1 | bei vestibulärer Verblendung |
| 0724 | Zahnfarbenbestimmung II | 1 | bei Schichtung/mehreren Farben |
| 0732 | Desinfektion | 2 | Eingangs- + Ausgangsdesinfektion |
| 0710 | Eilterminzuschlag | 1 | bei urgency=urgent/express |
| 0706 | Foto- oder Video-Dokumentation | 1 | bei Bedarf |
| 0721 | Zeiteinheit; Zahntechniker-Meister | je | bei Sonderaufwand |
| 0722 | Zeiteinheit; Zahntechniker | je | bei Sonderaufwand |
| 0701 | Versand je Versandgang | je | bei zusätzlichem Versandgang |
| 0907 | Digitaler Datenversand | je | bei digitaler Datenübermittlung |
| 0702 | Sonderversand oder Fahrtkosten | je | bei Sonderversand |
| 0731 | Individuelle Namenskennzeichnung I | 1 | bei Kennzeichnungspflicht |
| 2840 | Endkontrolle unter Stereomikroskop | je | bei höchsten Qualitätsanforderungen |

# Material

| Material | Menge | Bemerkung |
|--------|--------|--------|
| NEM-Legierung | ca. 8-12 g | für 3-gliedriges Gerüst (je nach Spannweite) |
| Verblendkeramik | — | je Glied, Schichtkeramik vestibulär; alternativ Verblendkunststoff bei BEL 1600 |
| Modellgips (Hartgips) | — | Arbeitsmodell + Gegenkiefermodell |
| Stumpf-Kunststoff | — | für Sägemodell-Stümpfe |
| Einbettmasse | — | für Gussvorgang |
| Konditionierer / Bonder | — | für Verblendung-Haftung |

# Hinweise

3-gliedrige NEM-Brücke vestibulär verblendet ist GKV-Regelversorgung innerhalb der Verblendgrenzen (OK 15-25, UK 34-44). Festzuschuss nach Befundklasse 2.x (Lückengebiss). Bei Mischbrücken über die Verblendgrenze hinaus wird BEL 1620 nur für Glieder innerhalb VG abgerechnet — die Molarenglieder werden unverblendet abgerechnet (vgl. `NEM_unverblendet_3gliedrig.md`). Bei größerer Spannweite (4+ Glieder) Mengen entsprechend skalieren: pro Anker `1024 +1`, pro Brückenglied `1100 +1`, pro Glied `1620 +1` und `9700 +1`. Wird die Brücke CAD-CAM gefräst, wechselt die Versorgung nach BEL II 2014 automatisch zu gleichartig (siehe `../gleichartig/`). Provisorische Versorgung wird separat aus `Provisorium/Bruecke/Regelversorgung/PMMA-Standard.md` kombiniert.