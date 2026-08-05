---
titel: Positionssystematik BEL
aliase: [L-Nr., BEL-Nummer, Leistungsnummer]
labels: [Abrechnung, BEL]
quellen: [raw/BEL_II_01_01_2022.pdf]
stand: 2026-08-05
---

Jede BEL-Position trägt eine Leistungsnummer (L-Nr.) aus dreistelliger Basis und einstelligem Suffix, geschrieben mit Leerzeichen: `001 0`, `102 4`, `933 8`. In Rechnungen ist neben der Nummer der Kurztext aus Anlage 2 anzugeben, siehe [[rechnungsstellung-bel]].

## Nummernkreise

Die erste Stelle bestimmt die Gruppe (BEL II, Anlage 2):

| Kreis | Gruppe |
|---|---|
| 0xx | Arbeitsvorbereitung |
| 1xx | Festsitzender Zahnersatz |
| 2xx | Modellguss |
| 3xx | Herausnehmbarer Zahnersatz |
| 4xx | Aufbissbehelfe |
| 5xx | Unterkieferprotrusionsschienen |
| 7xx | Kieferorthopädie |
| 8xx | Reparatur und Erweiterung |
| 9xx | Versandkosten, Verarbeitungsaufwand |

6xx ist nicht belegt. Anlage 2 kennt nur die ersten acht als eigene Gruppenüberschrift; die Positionen des Kreises 9xx stehen dort unter Reparatur/Erweiterungen, obwohl sie gruppenübergreifend anwendbar sind (siehe [[bel-zuschlaege-versand]]). Die Gruppenzugehörigkeit sagt nichts über Kombinierbarkeit: Positionen verschiedener Gruppen sind grundsätzlich miteinander kompatibel, siehe [[mengen-und-bezugsgroessen-bel]].

## Suffixe als Versorgungsmarker

Das BEL führt für Implantatversorgung und für Unterkieferprotrusionsschienen eigene Positionen, die inhaltlich der Normalposition entsprechen, aber getrennt abgerechnet werden. Sie sind überwiegend am Suffix erkennbar. Das Muster ist eine Lesehilfe, keine Regel: maßgeblich bleibt immer die Erläuterung zur Abrechnung der konkreten Position.

**Implantatversorgung, überwiegend Suffix 8.** Die vollständige Liste der Positionen, die nur für eine Versorgung nach Nr. 36 der Zahnersatz-Richtlinie abrechenbar sind:

001 8 · 012 8 · 021 6 · 021 8 · 022 8 · 102 6 · 102 8 · 162 8 · 163 8 · 301 8 · 302 8 · 361 8 · 362 8 · 801 8 · 808 8 · 809 8 · 810 8 · 820 8 · 933 8

Zwei dieser Positionen brechen das Muster und tragen Suffix 6: `021 6` (Basis für Bissregistrierung) und `102 6` (Vollkrone/Metall). Einzelheiten in [[implantatversorgung-bel]].

**Unterkieferprotrusionsschiene, teils Suffix 5, teils eigener Nummernkreis.** Die vollständige Liste der mit UKPS gekennzeichneten Positionen:

001 5 · 002 5 · 011 5 · 012 5 · 020 5 · 021 7 · 501 0 · 502 0 · 510 0 · 511 0 · 520 0 · 521 0 · 808 5 · 850 0 · 851 1 · 851 2 · 851 3 · 851 4 · 933 5

`021 7` (Individueller Löffel UKPS) bricht das Suffix-Muster. Der Nummernkreis 5xx und die Reparaturpositionen 850 0 sowie 851 1–851 4 sind ohnehin eigenständig. Einzelheiten in [[unterkieferprotrusionsschiene]].

**Suffix 5 bedeutet nicht generell UKPS.** `005 5` (Fräsmodell), `021 5` (Basis für Aufstellung), `202 5` (Kralle) und `380 5` (Gebogene Auflage) tragen dasselbe Suffix ohne UKPS-Bezug. Wer vom Suffix auf die Versorgungsart schließt, rechnet hier falsch ab.

## Suffixe innerhalb einer Familie

Sonst unterscheidet das Suffix Varianten derselben Grundleistung. `021 1` bis `021 8` sind alle Basen aus Kunststoff, differenziert nach Zweck (individueller Löffel, Funktionslöffel, Bissregistrierung, Stützstiftregistrierung, Aufstellung). `802 1` bis `802 7` sind die Leistungseinheiten der Prothesen-Instandsetzung. Die Varianten einer Familie sind nicht automatisch gegeneinander ausgeschlossen, aber häufig durch eine ausdrückliche Regel begrenzt, siehe [[nebeneinander-ausschluesse-bel]].

Verwandt: [[bel-ii]]
