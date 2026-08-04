| Bereich | Autor | erstellt am | Version |
|--------|--------|--------|--------|
| festsitzender Zahnersatz / Teleskopkrone / gleichartig | CLAUDE | 2026-04-27 | v1 |

# BEL-Positionen

| BEL | Leistung | Menge | Bemerkung |
|--------|--------|--------|--------|
| 0010 | Modell | 2 | Arbeitsmodell + Gegenkiefermodell |
| 0023 | Verwendung von Kunststoff | 1 | je Stumpfmodell für CAD-CAM |
| 0051 | Sägemodell | 1 |  |
| 0120 | Mittelwertartikulator | 1 |  |
| 9330 | Versandkosten | 2 | Hin- + Rückversand, entfällt bei Praxislabor |
| 0052 | Einzelstumpfmodell | 1 | je Pfeiler, bei Einzelstumpfmodell-Anfertigung |
| 0055 | Fräsmodell | 1 | je Kiefer, für paralleles Gestalten |
| 0240 | Übertragungskappe Kunststoff/Metall | 1 | je Pfeiler, bei Stumpfreposition |
| 0310 | Provisorische Krone/Brückenglied | 1 | je Pfeiler, bei längerer Tragezeit Provisorium |

# Basisleistungen

| BEB97 | Leistung | Menge | Bemerkung |
|--------|--------|--------|--------|
| 0103 | Modellsegment sägen | 1 | je Pfeiler |
| 0212 | Dowel-Pin setzen | 1 | je Pfeiler |
| 0213 | Ausblocken eines Stumpfes | 1 | je Pfeiler |
| 0216 | Stumpf vorbereiten | 1 | je Pfeiler |
| 0301 | Zahn vermessen | 1 | je Pfeiler |
| 0850 | 3D-Auftragsanlage / CAD/CAM-Auftragsanlage | 1 | je Auftrag |
| 0891 | CAD/CAM Modell einscannen | 1 | je Kiefer-Modell |
| 0918 | CAD/CAM Konstruktionsgrenze festlegen | 1 | je Pfeiler |
| 3855 | CAD/CAM Primärkrone konstruieren | 1 | je Pfeiler, Zirkon-Primärteleskop |
| 3853 | CAD/CAM Nachbearbeitung Teleskopkrone, primär | 1 | je Pfeiler |
| 2863 | Mehraufwand Sintern, je Auftrag | 1 | je Auftrag, Zirkon-Sintervorgang |
| 0105 | Stumpf aus Kunststoff | 1 | je Pfeiler, für CAD-CAM (Sägemodell-Stumpf) |

# Zusatzleistungen

| BEB97 | Leistung | Menge | Bemerkung |
|--------|--------|--------|--------|
| 0223 | Zahnfleischmaske, abnehmbar | 1 | je Pfeiler, bei Ästhetik-Anspruch |
| 0302 | Modell vermessen | 1 | bei zusätzlicher Vermessung neben 0301 |
| 3106 | Bohrung und Fräsung für Friktionsstift | 1 | je Pfeiler, bei Friktionsstift im Primär |
| 2813 | CAD/CAM Zirkon anpassen, je Zahneinheit | 1 | bei Mehraufwand Anpassung |
| 2840 | Endkontrolle unter Stereomikroskop | 1 | je Pfeiler, bei höchsten Qualitätsanforderungen |
| 0732 | Desinfektion | 2 | Eingangs- + Ausgangsdesinfektion |
| 0710 | Eilterminzuschlag | 1 | bei urgency=urgent/express |
| 0706 | Foto- oder Video-Dokumentation | 1 | bei Bedarf |
| 0721 | Zeiteinheit; Zahntechniker-Meister | je | bei Sonderaufwand |
| 0722 | Zeiteinheit; Zahntechniker | je | bei Sonderaufwand |
| 0701 | Versand je Versandgang | je | bei zusätzlichem Versandgang |
| 0104 | Stumpf aus Superhartgips | 1 | je Pfeiler, alternative Stumpfvariante (Superhartgips) |
| 0115 | Zweitstumpf aus Kunststoff | 1 | je Pfeiler, bei Zweitstumpf-Bedarf (Kunststoff) |
| 0116 | Zweitstumpf aus Metall | 1 | je Pfeiler, bei Zweitstumpf-Bedarf (Metall) |
| 0303 | Modell ausblocken | 1 | je Pfeiler, bei Modell ausblocken |
| 0723 | Zahnfarbenbestimmung I | 1 | bei Bedarf (Zirkon-Eigenfarbe — Farbabstimmung wichtig) |

# Material

| Material | Menge | Bemerkung |
|--------|--------|--------|
| CAD/CAM Block Zirkon | 1 Stück | je Pfeiler, für Primärteleskop |
| Modellgips (Hartgips) | — | Arbeitsmodell + Gegenkiefermodell |
| Stumpf-Kunststoff | — | je Stumpf für CAD-CAM (Sägemodell) |
| Sintermasse / Sinterhilfsmittel | — | für Zirkon-Sintervorgang |

# Hinweise

Reine Zirkon-Primär-Vorlage — wenn nur das Primärteleskop CAD-CAM-gefräst aus Zirkon gefertigt wird und das Sekundärteleskop separat abgerechnet wird (typisch in Kombi mit `Galvano_sekundaer.md` oder `Zirkon_sekundaer.md`). CAD-CAM-Zirkon-Primär macht die Versorgung nach BEL II 2014 (§14 CAD/CAM-Ausschluss BEL) automatisch zu gleichartig — NICHT andersartig. Patient erhält Festzuschuss in Höhe der Regelversorgung (NEM-Teleskop, BEL 1200, Befunde 4.6/3.2) und trägt die Mehrkosten privat. Diese Vorlage dokumentiert nur den Primärteleskop-Anteil eines Pfeilers — der Agent kombiniert mit einer Sekundär-Vorlage und `Herausnehmbar/Kombinationsarbeit/` für die Gesamtversorgung. Bei mehreren Pfeilern multiplizieren sich die Mengen (BEB97 0850 und 2863 bleiben 1× je Auftrag). Mengen-Limit: max 3 Teleskope je Kiefer (BEL §16).