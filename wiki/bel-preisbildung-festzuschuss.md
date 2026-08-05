# BEL II – Preisarten und Festzuschuss-Kopplung

Warum ein BEL-Preis im Katalog nicht derselbe ist wie der in Vereinbarungen genannte Preis.
Quellen: [[quelle-aenderungsvereinbarung-bel-ii-2023]] · § 57 Abs. 2 SGB V ·
Bundesmittelpreisliste 2026 (`raw/_inbox/BMP_2026_Leistungen_Regelversorgung.pdf`).

## Drei verschiedene Zahlen zur selben L-Nr.
| Zahl | Wer legt sie fest | Wozu |
|---|---|---|
| Bundeseinheitlicher Preis / Bundesmittelpreis | VDZI ↔ GKV-Spitzenverband, bundesweit, jährlich zum 30.09. (§ 57 Abs. 2 S. 1 SGB V) | Rechengröße für die Festzuschüsse des G-BA und Bezugsgröße der regionalen Vereinbarungen |
| Vereinbarter Vergütungspreis | regional: Landesverbände der Kassen ↔ Innungsverbände (§ 57 Abs. 2 S. 3, § 88 Abs. 2 SGB V) | was das Labor tatsächlich abrechnet |
| Katalogpreis im Repo | `kataloge/bel.json`, je L-Nr. Gewerbelabor / Praxislabor | Preisbasis der KV-Generierung |

Für den KV gilt der Katalogpreis, nicht der Bundesmittelpreis.

## § 57 Abs. 2 SGB V — die Mechanik

Der Wortlaut war bis zum 05.08.2026 ungeprüft und klärt drei Fragen auf einmal:

| Satz | Regelung |
|---|---|
| Satz 1 | GKV-Spitzenverband und VDZI vereinbaren jeweils zum 30. September die Veränderung der erstmals für 2005 ermittelten bundeseinheitlichen durchschnittlichen Preise |
| Satz 3 | Die regional vereinbarten Höchstpreise dürfen die bundeseinheitlichen Preise um **bis zu 5 %** unter- oder überschreiten |
| Satz 5 | Für die Festzuschussfestsetzung werden die bundeseinheitlichen Preise summiert und um **5 % gemindert**, soweit die Leistungen von Zahnärzten erbracht werden |

Damit ist geklärt, was frühere Fassungen dieser Seite offengelassen hatten: Der Bundeswert ist
eigenständig vereinbart, nicht aus regionalen Werten gemittelt. Die Kausalität läuft
umgekehrt — der Bundeswert ist die Bezugsgröße, aus der die regionalen Preise in einem
5-%-Korridor abgeleitet werden.

## Was `kataloge/bel.json` abbildet

Abgleich der 117 Positionen der Bundesmittelpreisliste 2026 gegen den Repo-Katalog
(eigene Auswertung, 05.08.2026):

| Kennzahl | Wert |
|---|---|
| Positionen im Katalog | 175 |
| davon in der BMP-Liste 2026 (= Regelversorgung) | 117 |
| Abweichung Gewerbelabor gegenüber BMP 2026, Median | +0,21 % |
| innerhalb des 5-%-Korridors nach § 57 Abs. 2 S. 3 | 113 von 117 |
| Verhältnis Praxislabor zu Gewerbelabor | exakt 95 % bei 171 von 175 Positionen |

Zwei Befunde folgen daraus:

1. Der Katalog ist nicht die Bundesmittelpreisliste, liegt aber nahe daran und verhält sich
   wie eine regionale Höchstpreisliste auf dem Preisstand 2026. Keine Position ist exakt
   deckungsgleich mit dem Bundeswert.
2. Die Praxislabor-Spalte ist rechnerisch der um 5 % geminderte Gewerbelabor-Preis. Das
   entspricht der Minderung nach § 57 Abs. 2 S. 5 SGB V. Ausnahmen sind 933 0, 933 5, 933 8
   und 970 0, die Praxis- und Gewerbelabor gleich ausweisen — bei den Versandpositionen ist der
   Praxislabor-Preis ohnehin gegenstandslos → [[bel-gruppe-zuschlaege-versand]].

Vier Positionen fallen aus dem 5-%-Korridor, alle nach unten. Es sind Grundeinheiten mit hoher
Ansatzhäufigkeit, ein Fehler wirkt sich deshalb auf viele KV aus:

| L-Nr. | Kurztext | BMP 2026 | Katalog Gewerbelabor | Abweichung |
|---|---|---:|---:|---:|
| 801 0 | Grundeinheit ZE | 27,19 € | 23,40 € | −13,9 % |
| 801 8 | Grundeinheit Instandsetzung ZE/implantatgest. | 27,19 € | 23,40 € | −13,9 % |
| 301 0 | Aufstellung, Grundeinheit | 41,38 € | 36,20 € | −12,5 % |
| 301 8 | Aufstellung, Grundeinheit bei Implantatversorgung | 41,38 € | 36,20 € | −12,5 % |

Ob es sich um einen abweichenden regionalen Wert, einen älteren Preisstand oder einen
Datenfehler handelt, ist offen. **VERIFIZIEREN**

Welchem KZV-Bereich und welchem Stichtag der Katalog zuzuordnen ist, ist im Repo weiterhin
nicht dokumentiert.

## Beispiel 005 1/2/3 — Preisart und Preisstand auseinanderhalten

| Wert | Betrag |
|---|---|
| Bundesmittelpreis ab 01.01.2023 | 16,62 € |
| Bundesmittelpreis 2026 | 18,94 € |
| Katalog `bel.json`, Gewerbelabor | 18,98 € |
| Katalog `bel.json`, Praxislabor | 18,03 € |

Der Abstand zwischen 16,62 € und 18,98 € ist überwiegend ein Zeitunterschied von drei Jahren,
kein Unterschied der Preisart. Jahresgleich verglichen liegen Bundesmittelpreis und Katalogwert
nur 0,04 € auseinander. Wer zwei Preisarten gegenüberstellt, muss sie deshalb im selben Jahr
vergleichen.

## Kopplung an die Festzuschüsse
Der G-BA legt die Festzuschuss-Richtlinie fest: Beträge nach § 57 Abs. 1 und Abs. 2
SGB V, Abstaffelungen nach § 55 Abs. 1 Sätze 2, 3, 5 und Abs. 2 SGB V (Bonusstufen).
In die Berechnung fließen die relativen Häufigkeiten der einzelnen L-Nrn. ein.
Details zur Richtlinie selbst: [[quelle-festzuschuss-richtlinie]]; zur Prozentmechanik:
[[festzuschuss-haertefall-bonus]].

Kalkulationsbasis 2026 (Kopf der GKV-SV-Betragstabelle, offiziell): bundeseinheitlicher
Zahnersatz-Punktwert 1,1844 € ab 01.01.2026; BEL-II-Preise nach Vereinbarung VDZI/GKV-SV
ab 01.01.2026 +4,78 % gegenüber 2025, zuzüglich „Modifikation Preisstruktur".

Daraus folgt ein Mechanismus, der bei jeder BEL-Änderung greift:

1. Leistungsinhalt oder Abrechnungsregel einer L-Nr. ändert sich
2. ihre relative Häufigkeit in der Versorgung ändert sich
3. die Festzuschussbeträge müssen angepasst werden (G-BA-Beschluss)
4. die Änderungsvereinbarung tritt zeitgleich mit diesem Beschluss in Kraft

Änderungsvereinbarung und G-BA-Beschluss sind deshalb immer datumsgleich zu lesen.

## Welche Positionen die Regelversorgung bilden

Die Bundesmittelpreisliste führt 117 L-Nrn. unter dem Titel „Leistungen für die
Regelversorgung". Nicht enthalten sind die Gruppen, für die es keinen Festzuschuss gibt:
Aufbissbehelfe (401 0 – 404 0), Kieferorthopädie (701 0 – 751 0) und der gesamte
UKPS-Leistungskreis. Das deckt sich mit [[bel-gruppe-aufbissbehelfe]] und [[bel-ii-ukps]].

Die Liste enthält keine Befundnummern. Die Zuordnung Befund → BEL-Positionen ist daraus
nicht zu gewinnen; sie steht im `regelversorgung`-Array des Festzuschusskatalogs
→ [[festzuschuss-befundklassen-referenz]].

## Kostenneutrale Einrechnung
Wird eine Position als eigenständig abrechenbare Leistung eingeschränkt, kann ihr Preisanteil
in die aufnehmende Position eingerechnet werden, statt ihn zu streichen. Beispiel 2023:
Der Preisanteil der 002 3 (Kunststoffsockel) wanderte in 005 1/2/3, deren Preis von
10,93 € auf 16,07 € stieg. Für die Kassen kostenneutral, für das Labor ein Nullsummenspiel —
aber nur, wenn 002 3 dort nicht weiter angesetzt wird. Doppelansatz wäre nach der
Einrechnung eine Überabrechnung. → [[bel-ausschlussregeln]]

## Offen
- Preisstand und Region des Katalogs `kataloge/bel.json` sind nicht dokumentiert.
- Die vier Positionen außerhalb des 5-%-Korridors (s. o.) sind ungeklärt. **VERIFIZIEREN**
- NEM-Verrechnungseinheiten sind regional: bei EM statt NEM in der Regelversorgung rechnet
  die KZV den BEL-Anteil über Verrechnungseinheiten an (z. B. KZV Berlin ab 01.01.2026:
  10,53 €/Einheit bei 60 %, 12,29 € bei 70 %, 13,16 € bei 75 %). Für andere KZV-Bereiche nicht
  erhoben, und auch für Berlin ohne hinterlegte Fundstelle — vor Verwendung bei der KZV
  verifizieren. → [[material-abrechnung-privat]] **VERIFIZIEREN**

## Verwandt
[[quelle-bel-ii-2014]] · [[quelle-festzuschuss-richtlinie]] · [[bel-ii-rechnungsstellung]] ·
[[bel-gruppe-arbeitsvorbereitung]] · [[festzuschuss-grundlagen]]
