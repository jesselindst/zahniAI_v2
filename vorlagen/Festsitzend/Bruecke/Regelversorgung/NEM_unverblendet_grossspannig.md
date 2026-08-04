| Bereich | Autor | erstellt am | Version |
|--------|--------|--------|--------|
| festsitzender Zahnersatz / Brücke / Regelversorgung | CLAUDE | 2026-04-27 | v1 |

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
| 1021 | Vollkrone/Metall | 2 | je Anker (bei mehr Pfeilern entsprechend skalieren) |
| 1100 | Brückenglied | 3 | je Zwischenglied; bei 5-gliedrig 3 Glieder, bei N-gliedrig (N − Anzahl Anker) |
| 1500 | Metallverbindung nach Brand | 1 | je Lötstelle, bei großspanniger Brücke meist 1-2 |
| 9700 | Verarbeitungsaufwand NEM-Legierung | 5 | je Element (Anker + Brückenglied) |
| 9330 | Versandkosten | 2 | Hin- + Rückversand, entfällt bei Praxislabor |

# Basisleistungen

_Pflicht-Kern ist vollständig über BEL abgedeckt. Keine zusätzlichen BEB97-Basisleistungen erforderlich._

# Zusatzleistungen

| BEB97 | Leistung | Menge | Bemerkung |
|--------|--------|--------|--------|
| 0732 | Desinfektion | 2 | Eingangs- + Ausgangsdesinfektion |
| 0710 | Eilterminzuschlag | 1 | bei urgency=urgent/express |
| 0706 | Foto- oder Video-Dokumentation | 1 | bei Bedarf |
| 0721 | Zeiteinheit; Zahntechniker-Meister | je | bei großspannigen Konstruktionen häufig erhöhter Aufwand |
| 0722 | Zeiteinheit; Zahntechniker | je | bei Sonderaufwand |
| 0701 | Versand je Versandgang | je | bei zusätzlichem Versandgang |
| 0907 | Digitaler Datenversand | je | bei digitaler Datenübermittlung |
| 0702 | Sonderversand oder Fahrtkosten | je | bei Sonderversand |
| 0731 | Individuelle Namenskennzeichnung I | 1 | bei Kennzeichnungspflicht |
| 2840 | Endkontrolle unter Stereomikroskop | je | bei höchsten Qualitätsanforderungen |

# Material

| Material | Menge | Bemerkung |
|--------|--------|--------|
| NEM-Legierung | ca. 15-25 g | für großspanniges Vollguss-Gerüst (5+gliedrig) |
| Modellgips (Hartgips) | — | Arbeitsmodell + Gegenkiefermodell |
| Stumpf-Kunststoff | — | für Sägemodell-Stümpfe |
| Einbettmasse | — | für Gussvorgang |
| Lot / Lötmittel | — | bei Lötstellen-Verbindung |
| Polierpaste / Hochglanzmittel | — | für Hochglanz-Politur |

# Hinweise

Großspannige NEM-Brücke unverblendet (5+gliedrig, z.B. 14-17 oder 34-37+) ist GKV-Regelversorgung im Molarenbereich außerhalb der Verblendgrenzen. Bei großer Spannweite oft Brückenteilung mit Lötstelle (BEL 1500) zur Spannungsreduktion. Mengen-Skalierung: pro Anker `1021 +1`, pro Brückenglied `1100 +1`, pro Element `9700 +1`, pro Lötstelle `1500 +1`. Festzuschuss nach Befundklasse 2.x kombiniert (Lückengebiss + Pfeilerzähne). Bei zusätzlichem Geschiebe oder Vollverblendung über alle Glieder → wechselt zu `gleichartig/` (Geschiebe = `Zirkon_voll_grossspannig_mit-Geschiebe.md`).