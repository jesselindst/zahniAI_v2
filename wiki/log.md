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
- **Sachfehler in `bel-ii-grundlagen` korrigiert**: Die Seite sagte, gleichartige *und*
  andersartige Versorgungen würden „für den über die Regelversorgung hinausgehenden Anteil"
  nach BEB abgerechnet. Bei **andersartig** läuft die gesamte Leistung über GOZ/BEB, und die
  Kasse erstattet den Festzuschuss an den Versicherten (§ 55 Abs. 5 SGB V). Die alte Aussage
  ist auf der Seite als Korrekturhinweis stehengeblieben, nicht still ersetzt.

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

## [2026-08-04] lint | Vollprüfung des Wikis (32 Seiten, 2 979 Zeilen)

Geprüft: Widersprüche zwischen Seiten, Aussagen ohne Quellverweis, verwaiste Seiten, Aussagen
auf überholten Quellen. Zusätzlich alle quantitativen Behauptungen gegen die Repo-Artefakte
(`kataloge/bel.json`, `kataloge/beb97_zahniAI.json`, `raw/review-2026-08/findings_register.json`,
`vorlagen/`) nachgerechnet. **25 Findings, nichts gefixt.**

**Sauber verifiziert (keine Abweichung):** die 33 BEL↔BEB-Kollisionen 1:1 gegen beide Kataloge ·
135 Überschneidungen von 175 L-Nrn. · 1103 BEB-Positionen · 32 doppelte BEB-Kurztexte ·
642 Befunde / 252 hoch · 228 Vorlagen · 2027/2028 nur im BEL, 0105 nur im BEB ·
401 0 = mit / 402 0 = ohne adjustierte Oberfläche · Preise 005 1/2/3 18,98/18,03 ·
keine verwaisten Seiten, keine toten `[[…]]`-Links.

**Hoch**
1. `beb97-grundlagen:69` + `haeufige-abrechnungsfehler:36` zitieren **§ 3 Abs. 3 BEL II** für
   „Leistungsbestandteile sind abgegolten". § 3 Ziff. 3 regelt die Rechnungs-Pflichtangaben
   (`bel-ii-rechnungsstellung:6`, bestätigt in `raw/…/beb_stand.md:47`). Tragende Grundlage ist
   § 2 Ziff. 4 + die Positionstexte.
2. `bel-ii-ukps:12` „nur die 5er-Varianten und die 5xx-Positionen" — widerlegt durch die eigenen
   Tabellen (021 7, 850 0, 851 1–851 4) und `bel-gruppe-reparatur-erweiterung:16`.
3. **Festzuschusskatalog** ist tragende Quelle in vier Seiten, existiert aber nicht im Repo und
   fehlt in der Artefaktliste des index. Register verweist auf `reference/festzuschuss_befunde.json`
   — ebenfalls nicht vorhanden.
4. `haeufige-abrechnungsfehler:109` Versandgang-/Leerfahrten-Regel ohne Fundstelle; laut
   `raw/…/bel2_stand.md:82` nur portal-/fachliteraturbelegt (gRS 11.07.2016, Volltext nicht
   zugänglich) — steht im Widerspruch zur eigenen Regel in `quelle-review-vorlagen-2026-08:50`.
5. Vollständigkeit der **Änderungsvereinbarungen nach 01.01.2023** seit `log:97` (03.08.2026)
   ungeprüft; der Ingest vom 04.08. hat das nicht geschlossen. Stärkste Quellengattung.

**Mittel**
6. BEB-Hauptgruppen **HG8 (64 Pos.) und HG9 (3 Pos.)** fehlen in `quelle-beb97:38` und
   `beb97-grundlagen:27`, obwohl beide Seiten die Regel „falsche Hauptgruppe = Abrechnungsfehler"
   tragen. `quelle-beb97:35` sagt selbst „HG0–HG9".
7. **38 von 171 Kurztexten** in den BEL-Gruppenseiten weichen von `kataloge/bel.json` ab, obwohl
   `bel-ii-rechnungsstellung:15` die wörtliche Übernahme vorschreibt (u. a. 164 0/165 0
   „Komposit" vs. „Komposite", 384 0 „hinterlegt" vs. „hinterlegen").
8. Verteilungstabelle `haeufige-abrechnungsfehler:9` summiert auf 631/250 statt 642/252 —
   Zeile „sonstiges" (11 Befunde, 2 hoch) fehlt.
9. Zwei Zählweisen (Befunde aus dem Register vs. Vorlagen aus dem BEFUNDBERICHT) unmarkiert
   nebeneinander: 81 vs. 189, 27 vs. 137, 54 vs. 114. Dazu drei „häufigster …"-Superlative.
10. Belegtypen [Q]/[P]/[E] laut `quelle-review-vorlagen-2026-08:17` „durchgängig beibehalten" —
    tatsächlich in 9 der 11 abgeleiteten Seiten praktisch nicht verwendet.
11. Gemeinsame Rundschreiben weiterhin ohne Quellenseite, ihre Inhalte fließen aber bereits an
    drei Stellen ein (Adhäsivbrücke, Versandgang, Gesichtsbogen).
12. `bel.json` führt Praxislabor-Preise für 933 0/5/8, obwohl das Wiki den Ansatz im Praxislabor
    ausschließt.
13. KZBV-FZ-Kompendium Stand 01.01.2025 trägt die 50-%-Regel und die Härtefallwege, während die
    FZ-RL auf Stand 01.01.2026 ist — Versatz nicht vermerkt.
14. Regionale €-Werte (KZV Hamburg/Bayern/Berlin) als „offiziell" bezeichnet, ohne Dokument/Datum.
15. BEB-97-Marktaussage stützt sich auf eine Spitta-Quelle von 2016; Marktanteile selbst UNBELEGT.
16. `___ 8`-Systematik (`bel-ii-grundlagen:72`) erfasst 021 6 und 102 6 nicht.
17. `raw/_inbox/BMP_2026_Leistungen_Regelversorgung.pdf` seit drei Ingests offen — hätte die
    Zuordnung Befund → BEL-Positionen.

**Niedrig**
18. `quelle-festzuschuss-richtlinie:58` „Klasse 1–7" vs. Seitentitel/index „1–8".
19. `quelle-review-vorlagen-2026-08:12`: 536 + 110 = 646 > 642 — orthogonale Dimensionen
    (Schnittmenge 86) als Aufteilung dargestellt.
20. `bel-gruppe-herausnehmbarer-zahnersatz:12`: „(Implantat: 302 8)" steht hinter 303 0 statt 302 0.
21. `beb97-grundlagen:45` nennt BEB 2603 „PMMA-spezifisch"; Katalogtext lautet „Verblendschale aus
    Kunststoff", kein Beleg auf der Seite.
22. `bel-ii-rechnungsstellung:47` „das ist der übliche Weg" — Praxisaussage ohne Marker.
23. `festzuschuss-befundklassen-referenz:52` „6.8.1 eingeführt zum 01.01.2019" ohne Fundstelle.
24. `log.md` ist im index nicht gelistet, obwohl der index „Katalog aller Wiki-Seiten" sein soll.
25. `log:48` nennt die Inbox-Datei ohne `_inbox/`-Pfad, spätere Einträge mit.

## [2026-08-04] fix | Umsetzung aller 25 Lint-Findings

Nachlauf zum Lint-Eintrag oben: alle 25 Findings abgearbeitet, **25 Seiten geändert**
(+255/−76 Zeilen). Keine Seite neu angelegt, keine gelöscht, keine Links gebrochen.

**Sachliche Korrekturen (Regel war falsch oder unvollständig)**
- **§ 3 Abs. 3 → § 2 Ziff. 4**: Die Rechtsgrundlage gegen BEL+BEB-Doppelabrechnung war in
  `beb97-grundlagen` und `haeufige-abrechnungsfehler` falsch zitiert. § 3 Ziff. 3 regelt die
  Rechnungs-Pflichtangaben; „abgegolten" folgt aus § 2 Ziff. 4 und den Positionstexten. Der
  Ein-Rechnung-Grundsatz aus § 3 Ziff. 3 ist als *zusätzliches* Argument erhalten.
- **UKPS-Leistungskreis**: „nur 5er-Varianten und 5xx" war falsch — 021 7, 850 0 und 851 1–851 4
  gehören dazu. In `bel-ii-ukps` durch eine Tabelle mit allen drei Nummerngruppen ersetzt.
- **`___ 5`/`___ 8` sind Faustregeln**, keine Systematik: 021 6 und 102 6 sind Implantatpositionen
  mit Endziffer 6. In `bel-ii-grundlagen` und im index kenntlich gemacht.
- **BEB-Hauptgruppen HG8 und HG9 ergänzt** (Instandsetzung 8001–8851; Zuschläge 9330/9700/9850) —
  67 der 1103 Positionen fehlten in beiden BEB-Seiten, bei zugleich geltender Regel „falsche
  Hauptgruppe = Abrechnungsfehler". Katalogfeld `type` ergänzt.
- **38 Kurztexte** in den BEL-Gruppenseiten wörtlich an `kataloge/bel.json` angeglichen
  (u. a. 164 0/165 0 „Komposite", 384 0 „hinterlegen", 134 9 „Wiederbefestigung Sekundärteil").
  Jetzt 171/171 identisch — maschinell geprüft.
- `quelle-festzuschuss-richtlinie`: „Klasse 1–7" → „Klassen 1–8".
- `bel-gruppe-herausnehmbarer-zahnersatz`: 302 8 stand hinter 303 0, gehört zu 302 0; 303 0 hat
  keine Implantatvariante.

**Belege nachgetragen oder Aussagen zurückgenommen**
- **Versandgang** (`haeufige-abrechnungsfehler`) stand ohne Fundstelle. Herleitung jetzt auf der
  zuständigen Seite `bel-gruppe-zuschlaege-versand`: gRS 11.07.2016, Volltext nicht zugänglich;
  Hin-/Rückweg fachliteraturbelegt [Q], Leerfahrten/Anprobe nur portalbelegt [P] → VERIFIZIEREN.
- **Belegtypen-Anspruch korrigiert**: `quelle-review-vorlagen-2026-08` behauptete, [Q]/[P]/[E]
  seien „durchgängig beibehalten". Tatsächlich fehlen sie in 4 von 11 abgeleiteten Seiten ganz.
  Ersetzt durch eine ehrliche Bestandsaufnahme mit der Warnung, dass ein fehlender Marker **nicht**
  „quellenbelegt" bedeutet. Marker wurden **nicht** nachträglich erfunden.
- **Regionale €-Werte** (KZV Hamburg/Bayern/Berlin) waren als „offiziell" ausgewiesen, ohne
  Dokument oder Datum — jetzt als unbelegt markiert, in `material-abrechnung-privat` und
  `bel-preisbildung-festzuschuss`.
- BEB-97-Verbreitungsaussage: Alter der Quelle (Spitta 2016, zehn Jahre) offengelegt.
- KZBV-Kompendium Stand 01.01.2025 gegen FZ-RL 01.01.2026: Standversatz vermerkt.
- BEB 2603 „PMMA-spezifisch" war durch den Katalogtext nicht gedeckt → VERIFIZIEREN.
- 6.8.1 „eingeführt 01.01.2019" und die Konformitätserklärungs-Praxis als unbelegt gekennzeichnet.

**Der wichtigste Befund dieses Durchgangs**
Bei der Recherche zum fehlenden „Festzuschusskatalog" stellte sich heraus: Er ist **kein
Repo-Artefakt**, sondern die DB-Tabelle `catalog_festzuschussbefund` — und stand laut
`BEFUNDBERICHT.md` beim Review auf **Stand 2025**, während seit 01.01.2026 neue Beträge gelten
(1.1 ohne Bonus 229,25 € → 239,03 €). Das Wiki verwies bis jetzt beiläufig auf „den
Festzuschusskatalog" als Betragsquelle, ohne beides zu sagen. Jetzt an vier Stellen als
VERIFIZIEREN markiert: **jeder Eigenanteil, der ungeprüft aus dieser Tabelle gerechnet wird,
ist ein Jahr zu alt.**

**Offene Punkte sichtbar gemacht statt nur im Log versteckt**
`quelle-bel-ii-2014` hat einen Aktualitätsvorbehalt erhalten: Die Vollständigkeit der
**Änderungsvereinbarungen nach 01.01.2023** ist seit dem ersten Ingest ungeprüft — bei der
obersten Stufe der Quellenrangfolge und inzwischen über drei Jahren Abstand. Dazu die drei
bereits verwendeten, aber nie ingesteten **Rundschreiben** mit Datum und Fundstelle. Der index
führt beides plus das offene `BMP_2026`-PDF in einer eigenen Tabelle „Noch nicht ingestete
Quellen". `log.md` ist jetzt im index verlinkt.

**Nicht geändert (bewusst)**
- `kataloge/bel.json` (Praxislabor-Preis bei 933 0/5/8) und `findings_register.json` — Artefakte
  außerhalb des Wikis. Die Falle ist stattdessen im Wiki dokumentiert
  (`bel-gruppe-zuschlaege-versand`, index).
- **Log-Eintrag vom 03.08.2026**, der die Inbox-Datei ohne `_inbox/`-Pfad nennt: `log.md` ist
  append-only, historische Einträge werden nicht umgeschrieben. Korrekt ist
  `raw/_inbox/BMP_2026_Leistungen_Regelversorgung.pdf` (Finding 25).
- Der `BMP_2026`-Ingest selbst — das ist ein Ingest, kein Lint-Fix, und gehört in einen eigenen
  Durchgang mit `ingest_to_wiki`.

## [2026-08-05] lint | Vollprüfung mit den neuen Stilregeln (32 Seiten)

Zweiter Lint-Durchgang, einen Tag nach dem ersten. Neu gegenüber dem 04.08.: die Stilregeln
(neutral, deklarativ, Formatierung nur wo Struktur ist) und die Regel zur Konsolidierung echter
Duplikate. Alle Findings wurden direkt auf den Seiten behoben; 31 Seiten geändert, keine Seite
neu angelegt, keine gelöscht, keine Links gebrochen.

### Recherche: zwei lange offene Punkte geschlossen

Vollständigkeit der Änderungsvereinbarungen. Seit dem ersten Ingest (03.08.) stand im Wiki der
Vorbehalt, es sei nie geprüft worden, ob nach dem 01.01.2023 weitere Änderungsvereinbarungen
zum BEL II hinzugekommen sind — bei der obersten Stufe der Quellenrangfolge. Die
Dokumentenübersicht des GKV-Spitzenverbands als Vertragspartei führt genau zwei: UKPS
(22.11.2021, i. K. 01.01.2022, in der Repo-Fassung bereits enthalten) und Modellherstellung
(14.11.2022, i. K. 01.01.2023, im Wiki abgebildet). Nach 2023 keine weitere. Der Vorbehalt in
`quelle-bel-ii-2014` ist durch eine Tabelle mit Prüfdatum und Fundstelle ersetzt, der Hinweis
im `index` entsprechend. Die Prüfung ist bei jedem Jahreswechsel zu wiederholen.

Gemeinsame Rundschreiben. Dieselbe Übersicht führt vier Rundschreiben GKV-SV ↔ VDZI
(19.03.2014, 29.02.2016, 18.12.2019, 27.09.2021) und die Gesichtsbogen-Erklärung zum Download.
Das Wiki behandelte sie bisher als nicht vorliegend. Datum und Verfügbarkeit stehen jetzt in
`quelle-bel-ii-2014`, mit der Abgrenzung zu den zwei Rundschreiben KZBV ↔ GKV-SV
(Adhäsivbrücke 28.06.2016, Versandkosten 11.07.2016), deren Volltext weiterhin fehlt. Der
Ingest selbst bleibt offen — das ist ein Ingest, kein Lint-Fix.

### Sachliche Korrekturen

`raw/_inbox/BMP_2026_Leistungen_Regelversorgung.pdf` falsch beschrieben. Der `index` behauptete
über drei Ingests hinweg, die Datei enthalte die Zuordnung Befund → BEL-Positionen. Die Prüfung
der Datei zeigt: Sie ist die Liste der bundeseinheitlichen durchschnittlichen Netto-Preise nach
§ 57 Abs. 2 Satz 1 SGB V, gültig 01.01.–31.12.2026, und enthält keine einzige Befundnummer. Was
sie tatsächlich liefert, sind die 117 L-Nrn., die die Zahnersatz-Regelversorgung bilden, mit
ihrem Bundesmittelpreis. Beschreibung im `index` korrigiert, Auswertung in
`bel-preisbildung-festzuschuss` ergänzt.

§ 57 Abs. 2 SGB V war seit dem Ingest vom 03.08. als ungeprüft markiert. Der Wortlaut klärt
drei Fragen: Satz 1 (GKV-SV und VDZI vereinbaren die bundeseinheitlichen Durchschnittspreise
jährlich zum 30.09., erstmals ermittelt für 2005), Satz 3 (regionale Höchstpreise dürfen davon
um bis zu 5 % nach oben oder unten abweichen), Satz 5 (Minderung um 5 %, soweit Zahnärzte die
Leistung erbringen). Damit ist belegt, was das Wiki bisher nur vermutete: Der Bundeswert ist
eigenständig vereinbart und ist die Bezugsgröße der regionalen Preise, nicht ihr Mittelwert.

Preisstruktur von `kataloge/bel.json` erstmals vermessen (117 Positionen gegen die BMP-Liste
2026): Median-Abweichung +0,21 %, 113 von 117 innerhalb des 5-%-Korridors nach § 57 Abs. 2
Satz 3. Der Katalog verhält sich damit wie eine regionale Höchstpreisliste auf Preisstand 2026,
ist aber nicht die Bundesmittelpreisliste — keine Position ist deckungsgleich. Die
Praxislabor-Spalte ist bei 171 von 175 Positionen exakt der um 5 % geminderte
Gewerbelabor-Preis, was der Minderung nach § 57 Abs. 2 Satz 5 entspricht; Ausnahmen sind
933 0/5/8 und 970 0 mit gleichem Wert. Vier Positionen fallen aus dem Korridor, alle nach unten:
801 0 und 801 8 mit −13,9 %, 301 0 und 301 8 mit −12,5 %. Es sind Grundeinheiten mit hoher
Ansatzhäufigkeit; als VERIFIZIEREN vermerkt.

Beispiel 005 1/2/3 war irreführend. `bel-preisbildung-festzuschuss` stellte den
Bundesmittelpreis 2023 (16,62 €) dem Katalogwert (18,98 €) gegenüber, um zwei Preisarten zu
belegen. Der Abstand ist überwiegend ein Zeitunterschied von drei Jahren: jahresgleich
verglichen liegen BMP 2026 (18,94 €) und Katalog 0,04 € auseinander. Beispiel durch eine Tabelle
mit beiden Preisständen ersetzt und um die Regel ergänzt, Preisarten nur jahresgleich zu
vergleichen.

Fehlerklasse falsch benannt. `haeufige-abrechnungsfehler` überschrieb Abschnitt 1 mit
„Doppelabrechnung — die größte Fehlerklasse (198 Befunde / 190 Vorlagen)". Die 198 sind aber die
Registerkategorie `positionen` insgesamt, die laut `BEFUNDBERICHT.md` „Falsche/unzulässige
Positionen" heißt und neben der Doppelabrechnung auch die falsche Hauptgruppe umfasst —
Abschnitt 2 derselben Seite speist sich aus derselben Kategorie. Nachgezählt: nur 55 der 198
Befundtexte nennen überhaupt eine Doppelabrechnung. Überschrift korrigiert, Zugehörigkeit von
Abschnitt 2 kenntlich gemacht. Dieselbe Überattribution stand in `beb97-grundlagen` unter der
Komplettpositions-Tabelle und ist dort ebenso korrigiert. In `quelle-review-vorlagen-2026-08`
ist neu eine Tabelle aller elf Registerkategorien mit ihren Befundzahlen hinterlegt, damit die
Bezeichnungen nachschlagbar sind.

Kaputte Tabelle in `bel-ii-grundlagen`. Die Nummernkreis-Tabelle (001–032 bis 933/970) hatte
ihren Kopf verloren: Zwischen Tabellenkopf und Zeilen stand eine Aufzählung, die Zeilen liefen
danach als nackte Pipe-Zeilen weiter und wurden nicht als Tabelle gerendert. In zwei getrennte
Tabellen (Nummernkreise, Endziffern-Muster) mit eigenen Köpfen aufgeteilt.

### Stil

85 Warnsymbole auf 30 Seiten entfernt, dazu zwei Ausrufezeichen
(`bel-ii-implantatversorgung`, `bel-mengenregeln`) und die Symbole der Verblendbarkeits-Matrix
in `bel-gruppe-festsitzender-zahnersatz`, ersetzt durch „ja"/„nein"/„nicht genannt". Fettung
außerhalb von Tabellen durchgängig aufgelöst, auch in wörtlichen Zitaten — dort war sie
hinzugefügte Betonung, keine Struktur. Cliffhanger und wertende Zuspitzungen
(„die gefährlichste Fehlerquelle", „leicht zu übersehen, spürbar im Geld", „Die Zahl",
„Das ist die Stelle, an der …") in sachliche Formulierungen überführt.

Beibehalten: Fettung innerhalb von Tabellenzellen, die Statusmarker VERIFIZIEREN und UNBELEGT
sowie die Belegtypen [Q]/[P]/[E] — sie sind Struktur, keine Betonung, und der Agent liest sie
als Flags.

### Querverweise ergänzt

`bel-ii-ukps`, `bel-gruppe-kieferorthopaedie` und `bel-gruppe-aufbissbehelfe` verweisen jetzt
auf `bel-preisbildung-festzuschuss`: Alle drei Gruppen fehlen in der BMP-Regelversorgungsliste,
was ihre Sonderstellung ohne Festzuschuss unabhängig bestätigt. Dazu
`bel-gruppe-modellguss` → `cadcam-digitale-verfahren` (Gussweg bei 201 0),
`bel-gruppe-festsitzender-zahnersatz` → `cadcam-digitale-verfahren`,
`bel-gruppe-zuschlaege-versand` → `festzuschuss-versorgungsformen` (9700 nie bei EM) und
`bel-gruppe-aufbissbehelfe` → `quelle-bel-ii-2014` (Gesichtsbogen-Erklärung).

### Nicht geändert (bewusst)

- Die bewusste Redundanz zwischen `haeufige-abrechnungsfehler` und den Fachseiten. Sie ist als
  Prüfliste vor der KV-Ausgabe angelegt (Ingest-Eintrag 04.08.) und damit kein echtes Duplikat
  im Sinne der Konsolidierungsregel. Statt zu konsolidieren, sind die Zahlen beider Seiten
  aufeinander abgeglichen.
- `log.md` ist append-only; die Fettung in den Einträgen vom 03. und 04.08. bleibt stehen. Die
  neuen Stilregeln gelten ab diesem Eintrag.
- `kataloge/bel.json` — die vier Positionen außerhalb des 5-%-Korridors sind im Wiki
  dokumentiert, der Katalog selbst nicht angefasst.
- Der Ingest von `BMP_2026_Leistungen_Regelversorgung.pdf` und der Rundschreiben. Beides ist
  jetzt inhaltlich beschrieben, aber ein Ingest gehört in einen eigenen Durchgang mit
  `ingest_to_wiki`.

### Offen

- 110 VERIFIZIEREN-Punkte aus dem Review vom 04.08.
- Preisstand und KZV-Bereich von `kataloge/bel.json` weiterhin nicht dokumentiert; die vier
  Korridor-Ausreißer ungeklärt.
- Festzuschusskatalog `catalog_festzuschussbefund` weiterhin auf Stand 2025, soweit bekannt.
