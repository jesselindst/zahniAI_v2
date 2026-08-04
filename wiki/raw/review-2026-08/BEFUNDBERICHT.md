# Befundbericht: Abrechnungsvorlagen in der Produktionsdatenbank

Stand: 04.08.2026. Prüfung **vollständig** (alle 228 Vorlagen, 22 Gruppen + 5 Querschnittsanalysen),
Drafts für alle 228 Vorlagen angelegt.
Beleg-Typen durchgängig getrennt: **[Q]** offizielle Quelle/Katalogfeld, **[P]** gängige Laborpraxis,
**[E]** eigene Einschätzung.

## Kernaussage

Die Wissensbasis hat **flächendeckende fachliche Substanzprobleme**, nicht nur Formatschwächen.
642 Befunde, davon **252 mit hoher Schwere**. Die hohen Befunde betreffen **223 der 228 Vorlagen**.
83 % aller Befunde (536) sind mit einem konkreten Katalog- oder Bestimmungszitat belegt;
110 bewusst als VERIFIZIEREN markiert statt geraten.

Die vier häufigsten Fehlerklassen mit hoher Schwere:

| Klasse | betroffene Vorlagen | typischer Fall |
|---|---|---|
| Falsche/unzulässige Positionen | 190 | Doppelabrechnung Komplettposition + Einzelschritte; falsche Hauptgruppe |
| Festzuschuss falsch/fehlend | 189 | fehlende Verblendzuschüsse 1.3/2.7/4.7; falscher Lückenbefund |
| Härtefall/Bonus fehlt | 137 | 60/70/75/100-%-Mechanik nirgends hinterlegt → Eigenanteil nicht berechenbar |
| Material falsch abgegrenzt | 114 | abgegoltenes Material als berechenbar geführt; EM ohne Gewicht/Tagespreis |

## 1. Systembefunde (Datenbank/Infrastruktur)

1. **FZ-Katalog veraltet** [Q]: `catalog_festzuschussbefund` steht auf Stand 2025. Seit 01.01.2026
   gelten neue Beträge (G-BA 05.12.2025, BAnz AT 04.02.2026 B3; z. B. 1.1 ohne Bonus 229,25 → 239,03 €).
2. **`materials_material` ist leer** [Q]: Der Agent bekommt laut Systemprompt die Labor-Materialliste —
   ohne Einträge kein `material_id`-Match; Materialzeilen laufen nur über Freitext.
3. **6 Vorlagen: `node.content` ≠ aktive Version** [Q] (Herausnehmbar/ImplantatProthese): Dort wurde an
   der Versionierung vorbei editiert. `read_template` liefert `node.content` — bei der nächsten
   Aktivierung gehen diese Direkt-Edits verloren.
4. **Kein Agent-Tool für Festzuschussbefunde** [E]: Die FZ-Tabelle existiert, ist dem Abrechnungsagenten
   aber nicht zugänglich. Empfehlung: `read_festzuschuss`-Tool; bis dahin tragen die Vorlagen
   Befund + Mechanik ohne €-Beträge.
5. **BEL-Preisstand prüfen** [E]: DB-Preise nahe BMP 2026, Herkunft/Region unklar.
6. **Mehrfach vergebene BEB-Kurztexte** [Q, eigene Auswertung]: 32 der 1103 Kurztexte doppelt.
   Kritisch bei identischem Text und abweichender Kalkulation: **0917 vs. 2848** „Konstruktion
   CAD-Krone zur Verblendung" (HG0/40 min vs. HG2/45 min) — für den Agenten nicht unterscheidbar.
   Weitere: 0909/2840, 3805/4122/4421/7122, 1360/3215.
7. **BEB-Positionen mit BEL-identischen Nummern** [Q, eigene Auswertung]: **135 der 175
   BEL-Nummern kommen auch im BEB 97 vor**; bei **33 davon bedeutet die Nummer etwas völlig
   anderes** — 0213 ist im BEL „Basis für Bissregistrierung", im BEB „Ausblocken eines Stumpfes";
   0023 im BEL „Verwendung von Kunststoff", im BEB „Modell für Einzelstümpfe". **1360 und 1370
   sind vertauscht**: beide Leistungen (Gefrästes Lager / Schubverteilungsarm) existieren in
   beiden Katalogen unter der jeweils anderen Nummer. Eine reine Existenzprüfung fängt davon
   nichts ab — die Nummer ist ja gültig. Prüfen muss man Nummer **und** Katalogzugehörigkeit
   **und** Leistungstext; `validate_drafts.py` tut das seit 04.08. Vollständige Liste:
   `wiki/beb-bel-nummernkollisionen.md` im Repo zahniAI_v2.

## 2. Mechanische Befunde (deterministischer Cross-Check, 9 608 Positionszeilen)

1. **BEB 2815 als „Okklusaler Stop" in 21 Vorlagen** [Q]: 2815 ist „CAD/CAM-Brückenglied, vollständig
   verblendet"; korrekt wäre **2915**.
2. **BEL 0105 existiert nicht** [Q]: Kunststoff-/Frässtumpf ist „ggf."-Bestandteil der Kronenpositionen.
3. **15 Doppelnennungen** [Q]: v. a. 0701 in Basis UND Zusatz (12 Vorlagen).
4. Alle übrigen 9 590+ Nummern existieren; Leistungsnamen weichen in 99 von 618 Codes ab.

## 3. Recherche-Kernkorrekturen (Primärquellen, Details in research/*.md)

1. **BEL II-2014**, konsolidiert Stand 01.01.2022, zuletzt geändert 01.01.2023 (Modellherstellung:
   Sockel in 0051/0052/0053 inkludiert; 0023 nicht für Stümpfe/Sockel) [Q].
2. **9700 nur NEM**, je Einheit nach abschließender Liste; **keine EM-/Titan-Zuschläge im BEL** [Q].
3. **Material GKV abschließend** (§ 2 Nr. 4): gesondert nur EM-Legierungen, künstliche Zähne,
   Konfektionsfertigteile, Implantatteile, Sonder-/Weichkunststoffe, UKPS-Elemente. NEM, Zirkon-/
   LiSi-Blanks, Gips abgegolten [Q]. Privat: Nachweis Legierung/Gewicht/Tagespreis (§ 10 GOZ) [Q].
4. **Festzuschuss**: 60/70/75 % (§ 55 Abs. 1), Härtefall § 55 Abs. 2 = +40 %. Wirkung differenziert:
   echte Regelversorgung → tatsächliche Kosten voll (Eigenanteil 0); gleich-/andersartig → nur fixer
   100-%-Betrag [Q]. Zusatzbefunde 1.3/2.7/4.7 je Verblendung im Bereich OK 15–25/UK 34–44 [Q].
   Klasse 7 nur Erneuerung/Wiederherstellung von Suprakonstruktionen [Q].
5. **Adhäsivbrücke**: Befunde 2.1/2.2 + 2.7 — **nicht 1.4/1.5** (das sind Stiftaufbauten). Bei EINEM
   Schneidezahn seit 04.05.2016 **ohne Altersgrenze**; „14.–21. Lj." nur bei zwei nebeneinander
   fehlenden Zähnen; Keramikgerüst = gleichartig [Q].
6. **Stiftaufbau**: 1.4 = konfektioniert (adhäsiv), 1.5 = gegossen (zementiert). Nicht-metallische
   Stifte (Glasfaser/Zirkon/Carbon) und Titanstifte sind bei GKV-Patienten **gleichartig mit FZ 1.4**,
   nicht „Privatleistung ohne Festzuschuss" [Q].
7. **CAD/CAM**: Gefräste Kronen/Brücken → gleichartig, weil die BEL-Kronenpositionen Gusstechnik
   voraussetzen (nicht „BEL II 2014 sagt immer") [Q]. Schienen 4010/4020 verfahrensoffen, regionale
   KZV-Unterschiede real [Q/P]. 3D-gedruckte Modelle nicht über 0010/005x [Q].
8. **UKPS**: GKV seit 2022, nur UKPS-gekennzeichnete BEL-Positionen + BEMA UP1–UP6 [Q].
9. **BEB 97**: weiterhin gängigste Privatbasis; Nachfolger „BEB Zahntechnik" 4. Aufl. 2023 mit
   153 Digitalpositionen — Basiswechsel nicht nötig, maßgeblich ist der DB-Katalog [Q/P].

## 4. Systematische Vorlagen-Befunde

1. **Härtefall/Bonus fehlt flächendeckend** [Q] — kein Agent kann Eigenanteile herleiten (137 Vorlagen).
2. **Verblend-Zusatzbefunde fehlen** [Q]: 1.3 (Krone), 2.7 (Brücke/Adhäsivbrücke), 4.7 (Teleskop).
3. **Doppelabrechnung Komplettposition + Einzelschritte** [Q]: „vollständig verblendet"-Positionen
   (2807/2810/2815/2829, 2552–2554, 2844–2846, 2613, 2653) neben separater Verblendung (2612/2616).
4. **BEL/BEB-Mix rechnet dieselbe Leistung doppelt** [Q] (1024+1620 BEL UND 2122/2314/2612 BEB).
5. **0023-Fehlverwendung für Stümpfe/CAD-CAM-Stumpfmodelle** [Q] (≥18 Vorlagen).
6. **Falsche Hauptgruppen-Positionen** [Q]: 6411 „Spezialpressverfahren" (HG6 Prothesen) für
   LiSi-Pressen; 2515 Kunststoff- statt Komposit-Onlay; 2603 PMMA-only.
7. **Erfundene Rechtsgrundlagen** [Q]: Alle 13 Teleskopkronen-Vorlagen zitieren nicht belegbare
   BEL-Paragraphen und leiten daraus falsche Regeln ab (z. B. „Mengen-Limit: max. 3 Teleskope").
8. **Falsche Leistungsausschlüsse zulasten der Patienten** [Q]: Valplast-Vorlagen behaupten pauschal
   „kein Festzuschuss" (Flexprothese ist gleichartig mit Zuschussanspruch); Stiftaufbau-Analogie.
9. **Fehlende Kernleistungen** [Q]: In allen drei Locator-Vorlagen fehlt das Einarbeiten der
   Matrizengehäuse; in allen vier Steg-Vorlagen fehlt das Sekundärteil (nur als Material geführt);
   drei Steg-Vorlagen enthalten überhaupt keine Steg-Position.
10. **Falsche Lückenbefunde mit Geldwirkung** [Q]: Implantat-Brücke 3-gliedrig mit 2.1 statt 2.3,
    4-gliedrig mit 2.2 statt 2.4/3.1.
11. **Strukturproblem Aufbissschienen** [Q]: Für Aufbissbehelfe existiert **kein** Festzuschuss-Befund
    — die Ordnerachse `Regelversorgung/` vs. `gleichartig/` ist dort systematisch unpassend. Die Drafts
    tragen einen ausdrücklich negativen FZ-Block, damit der Agent die %-Mechanik nicht anwendet;
    sauber wäre, `gleichartig/` dort in „Wahlleistung/Privatvereinbarung" zu überführen.
12. README-Fehler [Q]: Adhäsivbrücke „Befund 1.4"; Teilkrone „nicht in BEL" (1022 existiert);
    Root-README veraltet (Status „Files leer", tote Verweise, falsche Bayern-Regel).

Kontrollrechnungen (findings/kontrollrechnungen*.md) bestätigen die Geldwirkung: fehlender
1.3-Zuschuss ≈ 80–130 € je verblendeter Krone; Prothesenzähne bei Totalprothese fehlten als
gesondert berechenbares Material.

## 5. Format/Token

**Ausgangsbefund**: Kopfzeilen-Tabelle 100 % redundant (~38k Zeichen); Hinweise zu 91 % Fließtext;
Standard-Zusatzblock in 61 Varianten; 13 Überschriften-Ausreißer; Mischspalten „BEL/BEB" in
6 Vorlagen (Parser-Risiko). Das Zielschema v2 (ZIELSCHEMA.md) behält den Parsing-Vertrag des
Agenten bei und ergänzt den `# Festzuschuss`-Block.

### 5.1 Parsebarkeit: Ziel erreicht

| Merkmal | alt | Drafts |
|---|---|---|
| Fließtext in `# Hinweise` | 110 973 Zeichen (91 % der Sektion) | **0** |
| Kopfzeilen-Tabelle | 38 156 Zeichen | 261 Zeichen |
| Sektionsnamen außerhalb des Schemas | 6 Varianten | 0 |
| Mischspalten „BEL/BEB" | 6 Vorlagen | 0 |

Jede Zeile ist jetzt Tabellenzeile oder Bullet, Sektionsreihenfolge und Trigger-Präfixe sind
korpusweit kanonisch (`bei …`, `je <Einheit>: …`, `alternativ zu <Nr>`, `nur <…>`, `statt <Nr> bei <…>`).

### 5.2 Umfang: Ziel **verfehlt** — Korrektur einer früheren Aussage

Ich hatte im Zwischenstand „~30 % kürzer" berichtet. Die Messung über den Gesamtkorpus
(`measure_tokens.py`, 231 gegenüberstellbare Vorlagen) widerlegt das:

```
Altbestand gesamt: 1 041 513 Zeichen
Drafts gesamt:     1 781 437 Zeichen   (+71,0 %)
```

| Sektion | alt | neu | Delta |
|---|---:|---:|---:|
| Zusatzleistungen | 526 553 | 856 719 | +330 166 |
| Hinweise | 122 114 | 391 083 | +268 969 |
| Festzuschuss | 0 | 115 828 | +115 828 |
| Basisleistungen | 148 406 | 192 202 | +43 796 |
| Material | 83 850 | 101 351 | +17 501 |
| BEL-Positionen | 91 150 | 100 523 | +9 373 |
| Kopfzeilen | 38 156 | 261 | −37 895 |

**Ursache** (nicht Redundanz, sondern Inhalt): der neue `# Festzuschuss`-Block war ausdrücklich
beauftragt; die Zusatzleistungs-Tabellen wuchsen von 6 251 auf 8 002 Positionszeilen, weil fehlende
Leistungen ergänzt und Trigger-Bedingungen ausgeschrieben wurden; die Hinweise tragen die
Härtefall-/Bonus-Mechanik, die vorher nirgends stand, plus die nach Regelwerk-Punkt 24 verpflichtende
Benennung jeder entfallenen Position. Der Redundanzanteil blieb dabei praktisch unverändert
(34,7 % → 34,8 %); auch dedupliziert wächst der Korpus von 679 678 auf 1 162 369 Zeichen. Der
Zuwachs ist also Inhalt, kein Geschwätz — aber er ist eben auch nicht das, was du bestellt hattest.

### 5.3 Der ungenutzte Hebel (Empfehlung, nicht umgesetzt)

`analyze_bloat.py` beziffert den wortgleich wiederholten Standardblock:

- `# Zusatzleistungen`: 8 281 Tabellenzeilen, davon nur 2 579 verschieden →
  **543 483 Zeichen wortgleiche Wiederholung** (30 % des gesamten Draft-Korpus).
  Spitzenreiter: `0710 Eilterminzuschlag` (174×), `0702 Sonderversand` (170×),
  `0706 Foto-/Video-Dokumentation` (161×), `0732 Desinfektion` (160×).
- `# Hinweise`: weitere **75 585 Zeichen** wiederholte Standardbullets.

Zusammen **619 068 Zeichen = 35 % des Korpus**, verlustfrei auslagerbar. Verlagert man den
Standardblock in `sys_prompt_v2.md`, liegt der Korpus bei ~1,16 Mio. Zeichen — also **+11,6 %
statt +71 %** gegenüber dem Altbestand, bei allem fachlichen Zugewinn.

Ich habe das **nicht** umgesetzt, weil es kein Vorlagen-, sondern ein Laufzeit-Eingriff ist:
`sys_prompt_v2.md` bestimmt, wie der produktive Abrechnungsagent Positionen setzt. In ZIELSCHEMA.md
steht es deshalb unter „Nicht-Ziele". Vor einer Umsetzung ist eine Designfrage zu klären:
vorlagenspezifische **Abweichungen** vom Standardblock (z. B. Menge 1 statt 2 bei 0732, oder
Vorlagen, in denen 0710 nicht zulässig ist) müssen weiterhin ausdrückbar bleiben — nötig wäre also
ein Standardblock **plus** Override-/Ausschlussliste je Vorlage, nicht ein ersatzloses Streichen.

## 6. Qualitätssicherung der Drafts

Zwei deterministische Prüfungen sind Pflichtgate vor jedem DB-Schreibvorgang:
- `validate_drafts.py` — Schema, Existenz jeder Positionsnummer im DB-Katalog, Regelwerk-Stichproben.
- `check_infoloss.py` — jede entfallene Position/jedes Material muss im Draft oder in der
  `change_summary` wiederauffindbar sein („0 unbegründete Streichungen").

Beide fanden echte Fehler, auch in meinen eigenen Drafts (BEL 0320 Formteil war im Muster-Draft
verloren gegangen). **Selbstkorrektur am Werkzeug**: Der Validator wandte die Regel „BEL 0105
existiert nicht" zunächst auch auf BEB-Tabellen an — BEB 0105 „Stumpf aus Kunststoff" existiert
aber und ist bei Inlays zusatzabrechenbar. Seit 31.07. auf BEL beschränkt.

**Nachgerüstet am 04.08.** (nach dem Werkzeugfehler aus Abschnitt 8): Der Validator prüft jetzt
nicht mehr nur, *ob* eine Nummer existiert, sondern ob sie in der **richtigen Katalogtabelle**
steht. Nötig, weil rund 10 Nummern in BEL und BEB mit völlig verschiedener Bedeutung existieren —
0213 ist im BEL „Basis für Bissregistrierung", im BEB „Ausblocken eines Stumpfes". Eine reine
Existenzprüfung lässt so etwas durch; verglichen wird deshalb der Leistungstext gegen den
Katalogkurztext. Gegen den Altbestand gehalten findet die neue Regel 21 Textabweichungen und
keine Fehlplatzierung, gegen die Drafts nach der Korrektur beides null.

## 7. Stand der Umsetzung

- **Prüfung**: vollständig (22 Gruppen + 5 Querschnitte), 642 Befunde in `findings_register.json`.
- **Drafts**: **alle 228 Vorlagen** überarbeitet, dazu 4 Ordner-READMEs (Root, Adhäsivbrücke,
  Totalprothese, Modellguss). Jeder Draft hat `validate_drafts.py` und `check_infoloss.py` bestanden.
- **In der DB**: 266 Drafts über 226 Knoten (`status='draft'`, `source='agent'`). 38 Knoten tragen
  mehr als einen Draft — den ursprünglichen und den Rebase-Nachtrag aus Abschnitt 8; zwei davon
  zusätzlich die Korrektur des Werkzeugfehlers. **Maßgeblich ist immer die höchste Draft-Version.**
  Gelöscht wurde nichts, weil du das ausgeschlossen hattest. Die restlichen 6 überarbeiteten
  Knoten tragen keinen Draft mehr, weil du sie bereits **aktiviert** hast (Root-README,
  Adhäsivbrücken-README, beide Adhäsivbrücken-Regelversorgungen, beide Einzelkronen-Regelversorgungen).
- **Aktive Versionen: 289** — Stand unverändert. Nichts überschrieben, nichts gelöscht, kein Draft
  von mir veröffentlicht. Der Schreibpfad ist rein additiv (`INSERT … SELECT max(version)+1`) und
  prüft nach jedem Insert, dass `active_version` und die MD5 der aktiven Version sowie von
  `node.content` unverändert sind.
- Die 57 Knoten ohne Draft sind reine Ordner-Platzhalter (`source='seed'`, kein Inhalt).

Jeder Draft trägt seine Begründung in `change_summary` — was geändert wurde und woraus es folgt
(Katalogfeld, Richtlinie, Review-Befund). Für die 38 Vorlagen aus Abschnitt 8 existiert eine zweite
Draft-Fassung mit dem Nachtrag vom 04.08.; maßgeblich ist jeweils die höchste Draft-Version.

**Betriebshinweis zur Umgebung**: Die Läufe brachen regelmäßig ab, aus drei Gründen — (a) der
Container wird recycelt (`uptime` zeigte 5 min nach einem stillen Abbruch), (b) der
Parallelitätsdeckel liegt bei 2 Agenten (4 CPU-Kerne), sodass große Batches über eine Stunde
laufen, (c) Kontingentlimits (2–3 Mio. Subagent-Tokens je Lauf). Gegenmaßnahme seit 03.08.:
Batches von max. 4 Vorlagen je Agent, sofortiges Persistieren in die DB nach jedem Batch,
aktives Nachprüfen statt Warten auf Abschlussmeldungen.

## 8. Parallele Produktionsänderungen — Rebase der Drafts

Beim Abschluss-Check ist aufgefallen: **In der Produktion wurde während des Reviews
weitergearbeitet.** 52 aktive Fassungen tragen ein `updated_at` nach meinem Export vom 20.07.:
8 sind inhaltsgleich, 4 sind meine eigenen, von dir aktivierten Drafts — und **40 sind fremde
Änderungen** (28.07.–03.08., `source='agent'`), die meine Drafts nicht kannten.

Ohne Gegenmaßnahme hätte eine Aktivierung meiner Drafts diese Ergänzungen zurückgedreht.
`check_stale_baseline.py` hat je Vorlage aufgelistet, welche Positionen und Materialien betroffen
sind; 38 Vorlagen hatten echten Handlungsbedarf. Nachgetragen bzw. begründet abgelehnt wurde:

| Position | Vorlagen | Behandlung |
|---|---|---|
| BEB 0221 Hilfsteil in Abdruck | 24 | als Zusatzleistung ergänzt, `je Implantat`, „entfällt bei rein digitaler Abformung" |
| BEB 0223 Zahnfleischmaske, abnehmbar | 4 | ergänzt, mit Abgrenzung zu 0863 (gedrucktes Modell) |
| BEB 3301/3221/3321 individuelles Sekundärteil/Steggeschiebe | 7 | ergänzt — meine Drafts kannten nur den konfektionierten Weg (3621/3622), nicht den gefrästen |
| BEL 0213 + 0220 Bissregistrierung | 2 | ergänzt; **eigener Folgefehler behoben**: eine Schwestervorlage führte 0220 ohne Basis, was BEL II nicht zulässt |
| BEB 0210 Basis Autopolymerisat | 1 | ergänzt (Privatvorlage: BEL 0213 wäre dort systemfremd) |
| BEB 1640 Vestibuläre Verblendung Komposit | 1 | ergänzt |
| BEB 2010 + 5308 Modellguss-Tertiärgerüst | 1 | **nicht** übernommen, als vierte Tertiärvariante im Hinweis mit VERIFIZIEREN benannt |
| BEB 0221/0223 in reiner Regelversorgung | 1 | **nicht** übernommen — BEB in der Regelversorgung macht die Versorgung gleichartig; im Hinweis benannt |
| CoCr-Gerüst/Dubliermasse bei Locator | 2 | die aktive Fassung rechnet eine Metallbasis-Variante, meine Vorlage die Kunststoffvariante — als VERIFIZIEREN benannt |

**Neuer Befund dabei**: `Herausnehmbar/ImplantatProthese/andersartig/Teleskop_4-Implantate` führt in
der aktiven Fassung eine Position **2027 „Auflage" in der BEB97-Tabelle**. Im BEB97 existiert 2027
nicht (2026 = Ney-Stiel; 2027/2028 fehlen) — es ist eine **BEL-Nummer im BEB-Block**: BEL 2027
„Auflage" (Modellguss) gibt es sehr wohl. Die BEB-Entsprechung ist **3805 „Auflage" (HG3)**, nicht
7122 (KFO-Auflage, HG7). Im Draft entsprechend vermerkt.

Das ist zugleich ein Beispiel für eine größere, erst danach vermessene Fehlerklasse: **135 der 175
BEL-Nummern kommen auch im BEB 97 vor, bei 33 davon mit völlig anderer Bedeutung**; 1360/1370 sind
vertauscht. Eine reine Existenzprüfung fängt davon nichts ab — die Nummer ist ja gültig.

**Drei Fehler in meinem eigenen Werkzeug**, bei diesem Durchgang gefunden und behoben:

1. `check_stale_baseline.py` suchte entfallene Nummern zunächst nur in der `change_summary` statt
   im gesamten Draft und meldete dadurch 22 Nummern als verloren, die im Hinweisblock ausdrücklich
   benannt sind.
2. Der Materialabgleich verglich Zeichenketten exakt — „Zirkon-Blank" gegen „CAD/CAM Block Zirkon"
   zählte als Verlust. Beides korrigiert, bevor irgendetwas geändert wurde.
3. `merge_live_changes.py` traf im ersten Lauf die falsche Tabelle: Enthält ein Abschnitt erst eine
   BEL- und dann eine BEB97-Tabelle, lief die Suche bis zum Abschnittsende durch und hängte die
   BEL-Zeile unten an die BEB97-Tabelle. Das ist **einmal in die Datenbank gelangt** (Draft-Lauf
   vom 04.08., betroffen: die beiden `Bruecke/gleichartig/…EM_voll_3gliedrig`). Korrigiert und mit
   einer neuen, höheren Draft-Version überschrieben — aktiv wurde die fehlerhafte Fassung nie.
   Aufgefallen ist es nur, weil ich nach dem Merge stichprobenartig in die Datei gesehen habe;
   `validate_drafts.py` prüft Tabellenzugehörigkeit bisher nicht.

**Konsequenz für die Praxis**: Solange parallel an den Vorlagen gearbeitet wird, ist jeder Draft nur
so frisch wie sein Snapshot. `check_stale_baseline.py` sollte vor jeder Aktivierungsrunde erneut
laufen.

## 9. Offene Punkte / VERIFIZIEREN

**Vor Aktivierung fachlich freizugeben:**

- `Herausnehmbar/Modellguss/Privatleistung/CAD-CAM_CoCr_Freiend` — BEL 2010/2041 entfernt (gefrästes
  Gerüst erfüllt die Gusstechnik-Voraussetzung nicht). Verschiebt BEL-Anteil und Eigenanteil
  spürbar; bitte gegen die Hauspraxis prüfen, bevor der Draft aktiv wird.
- 110 Befunde mit VERIFIZIEREN-Flag (Details im Register), u. a. GOZ-Nummernzuordnung für den
  laborgefertigten Stiftaufbau (2180/2190/2195/2197), Mengenlogik von BEB 0918, sowie Würgereiz und
  Acrylat-Allergie als Metallbasis-Indikation (in der ZE-Richtlinie so nicht benannt).
- Versandgang-Definition (gRS 11.07.2016) nur fachliteraturbelegt.

**Hausentscheidungen, die ich bewusst nicht getroffen habe** (Struktur/Katalog, nicht Vorlageninhalt):

1. **Aufbissschienen**: `gleichartig/` auflösen — für Aufbissbehelfe existiert kein
   Festzuschuss-Befund, die Achse Regelversorgung/gleichartig ist dort systematisch falsch.
   Sauber wäre „Wahlleistung/Privatvereinbarung".
2. **Modellguss**: Ordner `andersartig/` fehlt im Bestand — bei Lückenbefunden 2.1–2.5 ist die
   Brücke Regelversorgung, ein Modellguss dort andersartig; für diesen realen Fall gibt es keine
   Zielvorlage.
3. **LiSi-Inlay-Reihe**: gefräst 2551–2554 vs. CAD/CAM 2844–2846 — Hausfestlegung nötig.
4. **Sinterhilfsmittel** korpusweit einheitlich regeln.
5. **Katalogpflege**: 32 doppelt vergebene BEB-Kurztexte, kritisch 0917/2848 (textgleich, HG0/40 min
   vs. HG2/45 min). Für den Agenten nicht unterscheidbar — Kurztext schärfen.
6. **Token-Hebel** aus 5.3: Standardblock nach `sys_prompt_v2.md` auslagern (35 % Korpusersparnis),
   sobald das Override-Design steht.

Zu 1.–6. liegen keine Änderungen in den Drafts, weil sie Ordnerstruktur, Katalog bzw. Systemprompt
betreffen — und dort hätte ich Bestand verändert statt Drafts angelegt.
