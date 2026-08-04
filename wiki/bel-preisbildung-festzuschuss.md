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
  **bundeseinheitlichen** Preis. Beides ist vereinbar, wenn der Bundeswert ein aus den
  regionalen Vereinbarungen abgeleiteter Mittelwert ist — das ist hier jedoch **nicht belegt**.
  Klärung über den Gesetzestext oder einen G-BA-Beschluss wäre der nächste Schritt.
- Welche Preisart die Werte in `kataloge/bel.json` genau abbilden (regional welches Bundesland,
  welcher Stand), ist im Repo nicht dokumentiert.

## Verwandt
[[quelle-bel-ii-2014]] · [[bel-ii-rechnungsstellung]] · [[bel-gruppe-arbeitsvorbereitung]]
