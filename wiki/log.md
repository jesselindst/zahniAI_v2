# Wiki – Log

Chronologisch, append-only. Präfix: `## [YYYY-MM-DD] <aktion> | <titel>`

## [2026-08-03] ingest | BEL II – 2014 (Stand 01.01.2022)

Quelle: `raw/BEL_II_01_01_2022.pdf` (135 S.) — Bundeseinheitliches Verzeichnis der
abrechnungsfähigen zahntechnischen Leistungen nach § 88 Abs. 1 SGB V, VDZI ↔
GKV-Spitzenverband. Erster Ingest, Wiki war leer.

**Angelegt: 16 Seiten + index.md**
- Quelle: `quelle-bel-ii-2014`
- Grundlagen: `bel-ii-grundlagen`, `bel-ii-rechnungsstellung`,
  `bel-ii-zusatzkosten-material`, `bel-ii-implantatversorgung`, `bel-ii-ukps`
- Leistungsgruppen (8): `bel-gruppe-arbeitsvorbereitung`,
  `bel-gruppe-festsitzender-zahnersatz`, `bel-gruppe-modellguss`,
  `bel-gruppe-herausnehmbarer-zahnersatz`, `bel-gruppe-aufbissbehelfe`,
  `bel-gruppe-kieferorthopaedie`, `bel-gruppe-reparatur-erweiterung`,
  `bel-gruppe-zuschlaege-versand`
- Querschnitt: `bel-ausschlussregeln`, `bel-mengenregeln`

**Aufteilungslogik:** Der Verzeichnisteil ist nach Leistungsgruppen gegliedert (= 1 Seite je
Gruppe, deckungsgleich mit Anlage 2 und mit den 9 Komplexen in `kataloge/bel.json`). Die
Erläuterungen zur Abrechnung enthalten aber quer über alle Gruppen zwei wiederkehrende
Regeltypen — Kombinationsverbote und Mengengrenzen. Diese sind zusätzlich in zwei
Querschnittseiten zusammengezogen, weil ein KV-Agent sie **positionsübergreifend als
Prüfliste** braucht und sie sonst über 120 Seiten verstreut wären. Bewusste Redundanz:
Regeln stehen sowohl bei ihrer Gruppe als auch in der Querschnittseite.

**Nicht ins Wiki übernommen (bewusst):**
- **Preise** — stehen nicht im BEL II (regional vereinbart); liegen in `kataloge/bel.json`.
- **Kurztext-Liste Anlage 2** — vollständig in `kataloge/bel.json` vorhanden, dort mit L-Nr.
  und Preis. Verweis statt Kopie.
- Vertrags-§§ 1, 3, 6 (Gegenstand, Umsetzungsfrist bis 31.12.2013, Kündigungsmodalitäten) —
  ohne Abrechnungsrelevanz, nur als Rahmen in `quelle-bel-ii-2014` erwähnt.

**Konflikte / Unklarheiten in der Quelle:**
- **810 8** (Prothesenbasis erneuern bei Implantatversorgung): Der Text nennt für die
  Bisslagefixierung „die L-Nrn. 001 8 und 011 2, nicht jedoch nach L-Nr. **012 0**". Alle
  Parallelvorschriften (808 8, 809 8) nennen an dieser Stelle **012 8**. Vermutlich
  Redaktionsversehen im Original. In `bel-ii-implantatversorgung` als solches markiert, nicht
  still korrigiert.
- **402 0** nennt als zusätzlich abrechenbar nur Halte-/Stützvorrichtungen, während 401 0 und
  403 0 zusätzlich „weitere Funktionsaufbisse" nennen. In `bel-gruppe-aufbissbehelfe` als
  Wortlautunterschied kenntlich gemacht, ohne Analogieschluss.

**Offen / nächste Schritte:**
- `raw/BMP_2026_Leistungen_Regelversorgung.pdf` und `raw/VDZI - Verband Deutscher
  Zahntechniker-Innungen.pdf` noch nicht ingested.
- **Gemeinsame Rundschreiben** des BEL-Ausschusses sind laut § 4/§ 5 verbindlich und
  präzisieren die Leistungsinhalte. Bisher keine im Wiki — eigene Quellengattung, wäre der
  nächste sinnvolle Ingest.

## [2026-08-03] ingest | Änderungsvereinbarung zum BEL II – 2014 (in Kraft 01.01.2023)

Quelle: `raw/VDZI - Verband Deutscher Zahntechniker-Innungen.pdf` (7 S.) — Ausdruck der
VDZI-Website mit dem vollständigen Vereinbarungstext VDZI ↔ GKV-Spitzenverband vom 14.11.2022.

**Angelegt: 2 Seiten**
- Quelle: `quelle-aenderungsvereinbarung-bel-ii-2023`
- Konzept: `bel-preisbildung-festzuschuss`

**Aktualisiert: 5 Seiten** — `bel-gruppe-arbeitsvorbereitung` (002 3 und 005 1/2/3 neu gefasst),
`bel-mengenregeln` (neue Bezugsgröße + Obergrenze der 002 3), `bel-ausschlussregeln`
(Teilausschluss 002 3 ↔ 005 1/2/3), `quelle-bel-ii-2014` (Überholungshinweis, Quellen-Rangfolge),
`index`.

**Umfang bewusst klein gehalten.** 7 PDF-Seiten, davon ~1 Seite Substanz. Der Wert liegt nicht
in neuen Seiten, sondern in der **Korrektur bestehender** — das Wiki führte an drei Stellen eine
seit 2023 überholte Regel.

**Der inhaltliche Kern:** Das Wiki sagte bei 005 1/2/3 „bei Kunststoffmodell zusätzlich 002 3".
Seit 01.01.2023 ist der Gips-/Kunststoffsockel **Leistungsbestandteil** von 005 1/2/3
(Erläuterungen zur Abrechnung: „Keine."), und der Preisanteil der 002 3 wurde kostenneutral
eingerechnet (10,93 € → 16,07 €, seit 01.01.2023 16,62 €). Ein KV nach der alten Wiki-Regel
hätte 002 3 doppelt angesetzt → **Überabrechnung**. Neu bei 002 3 außerdem: Bezugsgröße
*je aufgefülltem Sekundärteil* und Obergrenze *höchstens 3× je Modell*.

**Neue Erkenntnis zur Quellenhierarchie:** Änderungsvereinbarungen sind eine **dritte
Quellengattung** und stärker als Rundschreiben — sie ändern den Vertragstext selbst, statt ihn
nur auszulegen. Rangfolge jetzt in `quelle-bel-ii-2014` festgehalten.

**Konflikte / Unklarheiten in der Quelle:**
- Ziff. V datiert die Preiserhöhung auf „das Jahr 2022", Ziff. VI und die Protokollnotiz legen
  das Inkrafttreten aber auf 01.01.2023 (dann 16,62 €). Als Wortlautwiderspruch markiert, nicht
  geglättet.
- Dokumentform ist ein Website-Ausdruck, kein unterzeichnetes Original. Vermerkt.

**Katalog-Abgleich (kein Handlungsbedarf):** `kataloge/bel.json` führt 005 1/2/3 mit 18,98 €
(Gewerbelabor) / 18,03 € (Praxislabor) — also bereits auf dem angehobenen Niveau und damit
post-2023. Kein Widerspruch zum Bundesmittelpreis von 16,62 €: verschiedene Preisarten
(→ `bel-preisbildung-festzuschuss`).

**Offen / nächste Schritte:**
- `raw/_inbox/BMP_2026_Leistungen_Regelversorgung.pdf` noch nicht ingested.
- Gemeinsame Rundschreiben des BEL-Ausschusses weiterhin nicht im Wiki.
- Ungeprüft: ob es **weitere Änderungsvereinbarungen** nach 01.01.2023 gibt. Da sie dem BEL II
  vorgehen, wäre eine Vollständigkeitsprüfung auf vdzi.de der nächste sinnvolle Schritt.
- Nicht verifiziert, welche Preisart/welchen Stand `kataloge/bel.json` genau abbildet.
