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

## [2026-08-04] ingest | Vorlagenreview + Primärquellenrecherche Juli/August 2026

Quelle: `raw/review-2026-08/` — 7 Rechercheberichte (670 Zeilen, jede Aussage mit URL,
Abrufdatum und Quellentyp), `findings_register.json` (642 Befunde), `BEFUNDBERICHT.md`.
Keine externe Publikation, sondern eine **eigene Auswertung**: vollständige fachliche Prüfung
aller 228 ZahniAI-Abrechnungsvorlagen (9 608 Positionszeilen) gegen BEL II, BEB 97, FZ-RL und
ZE-RL, begleitet von einer Recherche zum Rechtsstand 2026.

**Angelegt: 11 Seiten**
- Quellen (4): `quelle-festzuschuss-richtlinie`, `quelle-zahnersatz-richtlinie`,
  `quelle-beb97`, `quelle-review-vorlagen-2026-08`
- Festzuschuss (4): `festzuschuss-grundlagen`, `festzuschuss-versorgungsformen`,
  `festzuschuss-haertefall-bonus`, `festzuschuss-befundklassen-referenz`
- Privatabrechnung (3): `beb97-grundlagen`, `beb-bel-nummernkollisionen`,
  `material-abrechnung-privat`
- Querschnitt (2): `cadcam-digitale-verfahren`, `haeufige-abrechnungsfehler`

**Aktualisiert: 4 Seiten** — `bel-preisbildung-festzuschuss` (Kalkulationsbasis 2026, offene
Frage zu § 57 Abs. 2 teilgeklärt), `bel-ii-zusatzkosten-material` (Umkehrschluss: was abgegolten
ist), `bel-gruppe-aufbissbehelfe` (digitale Fertigung, kein Festzuschussbereich), `index`.

**Aufteilungslogik.** Das Wiki deckte bisher ausschließlich das BEL II ab — also die GKV-Seite
der Regelversorgung. Es fehlte damit alles, was einen KV überhaupt erst rechenbar macht: das
Festzuschusssystem, die private Abrechnungsschiene und die Einstufungsfrage
Regelversorgung/gleichartig/andersartig. Der Ingest folgt deshalb nicht der Struktur der
Quelldokumente (die sind thematisch quer), sondern den drei Entscheidungen, die ein KV-Agent
nacheinander treffen muss:

1. **Welcher Befund?** → Festzuschuss-Block (4 Seiten). Die Trennung zwischen `grundlagen`
   (Systematik), `befundklassen-referenz` (Nachschlagen) und `haertefall-bonus` (Rechnen) ist
   bewusst: Der Agent braucht selten alles drei gleichzeitig.
2. **Welche Versorgungsform?** → `festzuschuss-versorgungsformen`. Eigene Seite, weil sie die
   Weiche zwischen BEL- und GOZ/BEB-Welt stellt und von beiden Seiten aus verlinkt wird.
3. **Welcher Katalog, welche Position?** → BEB-Block (3 Seiten) als Gegenstück zu den
   bestehenden BEL-Gruppenseiten.

`haeufige-abrechnungsfehler` ist bewusst redundant zu den Fachseiten — als Prüfliste vor der
KV-Ausgabe, analog zu `bel-ausschlussregeln` und `bel-mengenregeln`.

**Der wichtigste neue Befund: BEL ↔ BEB-Nummernkollisionen.** Eigene Auswertung von
`kataloge/bel.json` gegen `kataloge/beb97_zahniAI.json`: **135 der 175 BEL-Nummern kommen auch
im BEB vor**, bei **33 davon bedeutet die Nummer etwas völlig anderes** — 0213 ist im BEL
„Basis für Bissregistrierung", im BEB „Ausblocken eines Stumpfes". **1360/1370 sind schlicht
vertauscht** (beide Leistungen existieren in beiden Katalogen unter der jeweils anderen
Nummer). Eine reine Existenzprüfung fängt davon nichts ab, weil die Nummer ja gültig ist.
Das war vor diesem Ingest nirgends dokumentiert.

**Belegtypen beibehalten.** Die Rechercheberichte trennen [Q] Quelle / [P] Praxis / [E] eigene
Einschätzung und markieren Unbelegtes als UNBELEGT. Diese Trennung ist in den Wiki-Seiten
erhalten — insbesondere bei der privaten Materialabrechnung, wo vieles gängige Praxis ohne
Normtext ist (Kalkulationsfreiheit des Labors).

**Konflikte / Korrekturen am Bestand:**
- `bel-preisbildung-festzuschuss` ließ offen, ob der Bundesmittelpreis aus regionalen
  Vereinbarungen gemittelt wird. Die GKV-SV-Betragstabelle 2026 nennt ausdrücklich
  „BEL-II-Preise **nach Vereinbarung VDZI/GKV-SV**" — der Bundeswert ist also eigenständig
  vereinbart. Vermutung als hinfällig markiert, der § 57 Abs. 2-Wortlaut bleibt ungeprüft.
- `bel-gruppe-aufbissbehelfe` führte die Gruppe rein positionsseitig. Ergänzt: Für
  Aufbissbehelfe existiert **kein Festzuschussbefund**, folglich gibt es dort auch keine
  „gleichartige" Versorgung — die in `vorlagen/Schienen/` verwendete Achse
  `Regelversorgung/` ↔ `gleichartig/` ist dort systematisch unpassend. **Nicht** im
  Vorlagenbestand geändert, nur als Befund notiert.
- Die verbreitete Merkregel „Adhäsivbrücke nur 14.–21. Lebensjahr" gilt seit dem
  G-BA-Beschluss vom 18.02.2016 **nur noch** für zwei nebeneinander fehlende Schneidezähne.

**Nicht ins Wiki übernommen (bewusst):**
- **Die 642 Einzelbefunde.** Sie sind vorlagenspezifisch, nicht verallgemeinerbares Regelwissen.
  Ins Wiki gewandert ist nur das Muster dahinter. Register bleibt unter
  `raw/review-2026-08/findings_register.json`.
- **Festzuschuss-Beträge in €.** Sie werden jährlich neu festgesetzt (1.1 ohne Bonus: 2025 =
  229,25 €, 2026 = 239,03 €). Im Wiki stehen Befund und Prozentmechanik; die Beträge kommen aus
  dem Festzuschusskatalog.
- **Legierungs-Tagespreise** außer als Größenordnung (125–150 €/g für hochgoldhaltig, Stand
  20.07.2026) — sie ändern sich täglich.

**Offen / nächste Schritte:**
- `raw/_inbox/BMP_2026_Leistungen_Regelversorgung.pdf` weiterhin nicht ingested. Nach dieser
  Runde besonders interessant: Er müsste die Zuordnung Befund → BEL-Positionen enthalten, die
  hier nur über das `regelversorgung`-Array des Festzuschusskatalogs erschlossen ist.
- **Gemeinsame Rundschreiben** des BEL-Ausschusses weiterhin nicht im Wiki. Das Rundschreiben
  vom 19.03.2014 und das zu Adhäsivbrücken vom 28.06.2016 sind in der Recherche bereits
  ausgewertet und wären ein lohnender eigener Ingest.
- **110 VERIFIZIEREN-Punkte** aus dem Review sind offen, u. a.: GOZ-Nummernzuordnung für den
  laborgefertigten Stiftaufbau, Mengenlogik BEB 0918, Würgereiz/Acrylat-Allergie als
  Metallbasis-Indikation (in der ZE-RL so nicht benannt).
- **Katalogpflege**: 32 doppelt vergebene BEB-Kurztexte, kritisch 0917/2848 (textgleich,
  HG0/40 min vs. HG2/45 min) — für einen Agenten nicht unterscheidbar.
- BEB-Volltext ist ein VDZI-Lizenzprodukt und nicht frei zugänglich; Aussagen zur BEB-Binnenlogik
  stützen sich auf den Repo-Katalog und Fachliteratur, nicht auf einen amtlichen Text.
