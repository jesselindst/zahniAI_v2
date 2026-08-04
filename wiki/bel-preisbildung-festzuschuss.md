# BEL II – Preisarten und Festzuschuss-Kopplung

Warum ein BEL-Preis im Katalog **nicht** derselbe ist wie der in Vereinbarungen genannte Preis.
Quelle: [[quelle-aenderungsvereinbarung-bel-ii-2023]].

## Drei verschiedene Zahlen zur selben L-Nr.
| Zahl | Wer legt sie fest | Wozu |
|---|---|---|
| **Bundeseinheitlicher Preis / Bundesmittelpreis** | VDZI ↔ GKV-Spitzenverband, bundesweit | Rechengröße für die **Festzuschüsse** des G-BA |
| **Vereinbarter Vergütungspreis** | regional: Landesverbände der Kassen ↔ Innungsverbände (§ 57 Abs. 2, § 88 Abs. 2 SGB V) | was das Labor tatsächlich abrechnet |
| **Katalogpreis im Repo** | `kataloge/bel.json`, je L-Nr. Gewerbelabor / Praxislabor | Preisbasis der KV-Generierung |

⚠️ **Nie den Bundesmittelpreis in einen KV schreiben.** Für den KV gilt der Katalogpreis.

Beleg am Beispiel 005 1/2/3: bundeseinheitlicher Preis **16,62 €** (ab 01.01.2023), Katalog
`bel.json` **18,98 €** Gewerbelabor / **18,03 €** Praxislabor. Kein Widerspruch — zwei
verschiedene Preisarten.

## Kopplung an die Festzuschüsse
Der **G-BA** legt die Festzuschuss-Richtlinie fest: Beträge nach **§ 57 Abs. 1 und Abs. 2
SGB V**, Abstaffelungen nach **§ 55 Abs. 1 Sätze 2, 3, 5 und Abs. 2 SGB V** (Bonusstufen).
In die Berechnung fließen die **relativen Häufigkeiten** der einzelnen L-Nrn. ein.
Details zur Richtlinie selbst: [[quelle-festzuschuss-richtlinie]]; zur Prozentmechanik:
[[festzuschuss-haertefall-bonus]].

**Kalkulationsbasis 2026** (Kopf der GKV-SV-Betragstabelle, offiziell): bundeseinheitlicher
Zahnersatz-Punktwert **1,1844 €** ab 01.01.2026; **BEL-II-Preise nach Vereinbarung VDZI/GKV-SV
ab 01.01.2026 +4,78 %** gegenüber 2025, zuzüglich „Modifikation Preisstruktur".

Daraus folgt ein Mechanismus, der bei jeder BEL-Änderung greift:

1. Leistungsinhalt oder Abrechnungsregel einer L-Nr. ändert sich
2. → ihre relative Häufigkeit in der Versorgung ändert sich
3. → die Festzuschussbeträge müssen angepasst werden (G-BA-Beschluss)
4. → die Änderungsvereinbarung tritt **zeitgleich mit** diesem Beschluss in Kraft

Deshalb sind Änderungsvereinbarung und G-BA-Beschluss immer datumsgleich zu lesen.

## Kostenneutrale Einrechnung
Wird eine Position als eigenständig abrechenbare Leistung eingeschränkt, kann ihr Preisanteil
in die aufnehmende Position **eingerechnet** werden, statt ihn zu streichen. Beispiel 2023:
Preisanteil der **002 3** (Kunststoffsockel) wanderte in **005 1/2/3**, deren Preis von
10,93 € auf 16,07 € stieg. Für die Kassen kostenneutral, für das Labor ein Nullsummenspiel —
**aber nur, wenn 002 3 dort nicht weiter angesetzt wird.** Doppelansatz wäre nach der
Einrechnung eine echte Überabrechnung. → [[bel-ausschlussregeln]]

## Offen / nicht aus dieser Quelle belegt
- [[quelle-bel-ii-2014]] führt **§ 57 Abs. 2 SGB V** als Grundlage der **regionalen**
  Vergütungsvereinbarungen an, diese Quelle denselben Absatz im Zusammenhang mit dem
  **bundeseinheitlichen** Preis.
  **Teilklärung (Recherche 20.07.2026, [[quelle-review-vorlagen-2026-08]]):** Die GKV-SV-Tabelle
  2026 nennt ausdrücklich „BEL-II-Preise **nach Vereinbarung VDZI/GKV-SV**" als Kalkulationsbasis.
  Der Bundeswert ist damit **eigenständig vereinbart**, nicht aus regionalen Werten gemittelt.
  Die Vermutung eines abgeleiteten Mittelwerts ist damit hinfällig — der Wortlaut des § 57 Abs. 2
  bleibt aber weiterhin ungeprüft.
- Welche Preisart die Werte in `kataloge/bel.json` genau abbilden (regional welches Bundesland,
  welcher Stand), ist im Repo weiterhin **nicht dokumentiert**.
- **NEM-Verrechnungseinheiten** sind regional: bei EM statt NEM in der Regelversorgung rechnet
  die KZV den BEL-Anteil über Verrechnungseinheiten an (z. B. KZV Berlin ab 01.01.2026:
  10,53 €/Einheit bei 60 %, 12,29 € bei 70 %, 13,16 € bei 75 %). Für andere KZV-Bereiche nicht
  erhoben. → [[material-abrechnung-privat]]

## Verwandt
[[quelle-bel-ii-2014]] · [[quelle-festzuschuss-richtlinie]] · [[bel-ii-rechnungsstellung]] ·
[[bel-gruppe-arbeitsvorbereitung]] · [[festzuschuss-grundlagen]]
