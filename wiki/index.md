# Wiki – Index

Katalog aller Wiki-Seiten. **Bei jedem Ingest mitpflegen.**
Einstieg für eine Abrechnungsfrage: erst hier die passenden Seiten wählen, dann nur diese
öffnen.

## Quellen
| Seite | Inhalt | Stand |
|---|---|---|
| [quelle-bel-ii-2014](quelle-bel-ii-2014.md) | BEL II – 2014, Bundeseinheitliches Verzeichnis abrechnungsfähiger zahntechnischer Leistungen (§ 88 Abs. 1 SGB V). Vertragsparteien, Aufbau, Verbindlichkeit. **Bei 002 3 und 005 1/2/3 überholt.** Raw: `raw/BEL_II_01_01_2022.pdf` | 01.01.2022 |
| [quelle-aenderungsvereinbarung-bel-ii-2023](quelle-aenderungsvereinbarung-bel-ii-2023.md) | Änderungsvereinbarung VDZI ↔ GKV-SV vom 14.11.2022: Neufassung 002 3 und 005 1/2/3, Bundesmittelpreis. **Geht dem BEL II 01.01.2022 vor.** Raw: `raw/VDZI - Verband Deutscher Zahntechniker-Innungen.pdf` | 01.01.2023 |
| [quelle-festzuschuss-richtlinie](quelle-festzuschuss-richtlinie.md) | **FZ-RL des G-BA** — Zuordnung Befund → Festzuschuss und Höhe der Beträge. Aufbau Teil A/B/C, Historie der Prozentsätze, Kalkulationsbasis 2026. Beträge ändern sich jährlich | i. K. 01.01.2026 |
| [quelle-zahnersatz-richtlinie](quelle-zahnersatz-richtlinie.md) | **ZE-RL des G-BA** — was für welchen Befund Regelversorgung ist. Nr. 5 (gleich-/andersartig), 20/25 (Verblendgrenze), 22/24 (Adhäsivbrücke), 36–39 (Suprakonstruktion) | i. K. 04.05.2016 |
| [quelle-beb97](quelle-beb97.md) | **BEB 97 des VDZI** — Nomenklaturliste für private Laborleistungen, keine Gebührenordnung. Hauptgruppen, Status 2026 vs. „BEB Zahntechnik", bekannte Katalogschwächen. Katalog: `kataloge/beb97_zahniAI.json` | 1997, Katalogstand 2026 |
| [quelle-review-vorlagen-2026-08](quelle-review-vorlagen-2026-08.md) | **Eigene Auswertung**: Prüfung aller 228 Abrechnungsvorlagen + Primärquellenrecherche. 642 Befunde, Belegtypen [Q]/[P]/[E]. Raw: `raw/review-2026-08/` | 04.08.2026 |

### Noch nicht ingestete Quellen

| Quelle | Warum ihr Fehlen ins Gewicht fällt |
|---|---|
| `raw/_inbox/BMP_2026_Leistungen_Regelversorgung.pdf` | Enthielte die Zuordnung **Befund → BEL-Positionen**, die derzeit nur mittelbar über das `regelversorgung`-Array erschlossen ist — und der zugehörige Katalog fehlt im Repo (s. u.). Seit drei Ingests offen. |
| **Gemeinsame Rundschreiben** des BEL-Ausschusses | Nach § 4/§ 5 verbindliche Quellengattung, **keine eigene Quellenseite im Wiki** — obwohl ihre Inhalte an drei Stellen bereits verwendet werden: Adhäsivbrücke (28.06.2016) in [[quelle-zahnersatz-richtlinie]], Versandgang (11.07.2016) in [[bel-gruppe-zuschlaege-versand]], Gesichtsbogen (10.10.2014) in [[bel-gruppe-aufbissbehelfe]]. |
| **Festzuschusskatalog** = DB-Tabelle `catalog_festzuschussbefund` (kein Repo-Artefakt) | Liefert Befundtexte, `regelversorgung`-Array und die **Beträge**. Beim Review auf **Stand 2025**, während seit 01.01.2026 neue Beträge gelten — vor jedem KV den Stand prüfen → [[festzuschuss-haertefall-bonus]]. |

⚠️ **Ungeprüft:** ob es nach dem 01.01.2023 **weitere Änderungsvereinbarungen** zum BEL II gibt.
Sie gehen allen anderen Quellen vor → [[quelle-bel-ii-2014]].

## Grundlagen & Konzepte
| Seite | Inhalt |
|---|---|
| [bel-ii-grundlagen](bel-ii-grundlagen.md) | Wann gilt BEL II? Regelversorgung/KFO/Aufbissbehelfe/UKPS, Kompatibilitäts-Grundregel, Informationspflicht des Zahnarztes, Systematik der L-Nummern (`___ 5` = UKPS, `___ 8` = Implantat — **Faustregeln mit Ausnahmen**) |
| [bel-ii-rechnungsstellung](bel-ii-rechnungsstellung.md) | Pflichtangaben (L-Nr. + Kurztext), Herstellungsort, Fremdleistungen, arbeitsteilige Fertigung, Konformitätserklärung nach VO (EU) 2017/745, Aufbewahrungsfristen |
| [bel-ii-zusatzkosten-material](bel-ii-zusatzkosten-material.md) | Was **neben** den Leistungen abrechenbar ist: abschließende Liste des § 2 Ziff. 4, Konfektionsfertigteile vs. Hilfsteile, EM-Legierungen, Lote (75 %-Regel) — und der Umkehrschluss, was abgegolten ist |
| [bel-ii-implantatversorgung](bel-ii-implantatversorgung.md) | Die `___ 8`-Positionen, Nr. 36 a (Einzelzahnlücke) vs. Nr. 36 b (atrophierter zahnloser Kiefer), Bestätigungspflicht des Zahnarztes |
| [bel-ii-ukps](bel-ii-ukps.md) | Unterkieferprotrusionsschiene: geschlossener Leistungskreis, vollständige Positionsliste, feste Mengenobergrenzen |
| [bel-preisbildung-festzuschuss](bel-preisbildung-festzuschuss.md) | Drei Preisarten je L-Nr. (Bundesmittelpreis / regionale Vergütung / `bel.json`) — welche in den KV gehört; Kopplung an die FZ-Richtlinie, kostenneutrale Einrechnung |

## Festzuschuss (GKV-Zahnersatz)
| Seite | Inhalt |
|---|---|
| [festzuschuss-grundlagen](festzuschuss-grundlagen.md) | Befundbezogenes System, die drei Fragen jedes KV, die acht Befundklassen im Überblick, Zusatzbefunde 1.3/2.7/4.7, Bezugsgrößen, was nie bezuschusst wird |
| [festzuschuss-versorgungsformen](festzuschuss-versorgungsformen.md) | **Regelversorgung / gleichartig / andersartig** — Definitionen, Abrechnungswege im Vergleich, 50-%-Regel bei Mischfällen, häufige Fehleinordnungen |
| [festzuschuss-haertefall-bonus](festzuschuss-haertefall-bonus.md) | 60/70/75/100 %, Bonusheft, **die unterschiedliche Härtefallwirkung** bei Regelversorgung vs. gleich-/andersartig, Rechenweg für den Eigenanteil |
| [festzuschuss-befundklassen-referenz](festzuschuss-befundklassen-referenz.md) | Klassen 1–8 im Einzelnen mit Bezugsgrößen und den real aufgetretenen Verwechslungen |

## Private Abrechnung (BEB / GOZ)
| Seite | Inhalt |
|---|---|
| [beb97-grundlagen](beb97-grundlagen.md) | Preisbildung über Planzeit × Kostensatz, Hauptgruppen als Abrechnungsinhalt, Komplettposition vs. Einzelschritte, BEL/BEB nicht mischen |
| [beb-bel-nummernkollisionen](beb-bel-nummernkollisionen.md) | **135 Nummern in beiden Katalogen**, 33 mit völlig anderer Bedeutung, 1360/1370 vertauscht. Prüfregel für den KV |
| [material-abrechnung-privat](material-abrechnung-privat.md) | § 9/§ 10 GOZ: Bezeichnung, Gewicht und Tagespreis der Legierung; KV-Pflicht ab 1.000 €; was gesondert ausgewiesen wird; Gegenprobe GKV ↔ privat |

## Leistungsgruppen (Verzeichnisteil BEL II)
| Seite | L-Nr. |
|---|---|
| [bel-gruppe-arbeitsvorbereitung](bel-gruppe-arbeitsvorbereitung.md) | 001 0 – 032 0 · Modelle, Bisslagefixierung, Basen/Löffel, Registrierung, Provisorien |
| [bel-gruppe-festsitzender-zahnersatz](bel-gruppe-festsitzender-zahnersatz.md) | 101 3 – 165 0 · Kronen, Brückenglieder, Teleskope, Geschiebe/Anker, Verblendungen |
| [bel-gruppe-modellguss](bel-gruppe-modellguss.md) | 201 0 – 212 0 · Metallbasis, gegossene Halte-/Stützelemente, Rückenschutzplatte |
| [bel-gruppe-herausnehmbarer-zahnersatz](bel-gruppe-herausnehmbarer-zahnersatz.md) | 301 0 – 384 0 · Aufstellung/Fertigstellung, gebogene Halteelemente, Sonderkunststoffe |
| [bel-gruppe-aufbissbehelfe](bel-gruppe-aufbissbehelfe.md) | 401 0 – 404 0 · Schienen mit/ohne adjustierte Oberfläche, Umarbeiten, semipermanente Schiene, digitale Fertigung, **kein Festzuschussbereich** |
| [bel-gruppe-kieferorthopaedie](bel-gruppe-kieferorthopaedie.md) | 701 0 – 751 0 · Basen, Schrauben, Bögen, Federn, Verbindungs-/Halteelemente |
| [bel-gruppe-reparatur-erweiterung](bel-gruppe-reparatur-erweiterung.md) | 801 0 – 870 0 · Grundeinheiten + Leistungseinheiten, Unterfütterung, Basiserneuerung |
| [bel-gruppe-zuschlaege-versand](bel-gruppe-zuschlaege-versand.md) | 933 0/5/8, 970 0 · Versandkosten, NEM-Verarbeitungsaufwand |

## Querschnitt-Regeln (Prüflisten vor KV-Ausgabe)
| Seite | Inhalt |
|---|---|
| [bel-ausschlussregeln](bel-ausschlussregeln.md) | Alle „nicht nebeneinander / nur wenn / stattdessen"-Regeln: gegenseitige Ausschlüsse, Grundeinheit-vs-Unterfütterung, Artikulator-Verbote, Umleitungsregeln, Praxis-/Gewerbelabor |
| [bel-mengenregeln](bel-mengenregeln.md) | Wie oft ansetzbar — sortiert nach Bezugsgröße (je Zahn / je Kiefer / je Werkstück / je Vorgang), Stützstiftregistrierung, UKPS-Obergrenzen |
| [haeufige-abrechnungsfehler](haeufige-abrechnungsfehler.md) | **Destillat aus 642 Befunden**: Doppelabrechnung, falsche Positionen trotz passendem Kurztext, Festzuschussfehler, falsche Leistungsausschlüsse, fehlende Kernleistungen, erfundene Rechtsgrundlagen. Mit Kurz-Checkliste |
| [cadcam-digitale-verfahren](cadcam-digitale-verfahren.md) | Warum das BEL nicht technikneutral ist; gefräst = gleichartig bei Kronen/Brücken, **nicht** bei Aufbissbehelfen; Modelle, Intraoralscan, Monolithik, digitale Totalprothetik |

## Wiki-Betrieb
- [log](log.md) — chronologisches Protokoll aller Ingests, Queries und Lint-Läufe (append-only)

## Zugehörige Repo-Artefakte (nicht im Wiki gespiegelt)
- `kataloge/bel.json` — 175 L-Nrn. in 9 Komplexen, **Preise** (Gewerbelabor / Praxislabor).
  Die Kurztexte dieses Katalogs sind für Rechnung und KV **maßgeblich**
  ([[bel-ii-rechnungsstellung]]); die BEL-Gruppenseiten geben sie wörtlich wieder.
  ⚠️ Der Katalog führt bei **933 0/5/8 auch einen Praxislabor-Preis**, obwohl Versandkosten im
  Praxislabor **nicht** abrechenbar sind → [[bel-gruppe-zuschlaege-versand]]. Preisfeld hier
  nicht ungeprüft übernehmen.
- `kataloge/beb97_zahniAI.json` — 1103 BEB-97-Positionen; Felder `nr`, `name`, `dauer_min`
  (Planzeit), `hg` (Hauptgruppe **HG0–HG9**), `type` (`standard` / `individuell`)
- `vorlagen/` — 228 Abrechnungsvorlagen je Konfigurator-Bereich, Schema:
  `# Festzuschuss` · `# BEL-Positionen` · `# Basisleistungen` · `# Zusatzleistungen` ·
  `# Material` · `# Hinweise`
- `raw/review-2026-08/findings_register.json` — die 642 Einzelbefunde. Achtung beim Zählen: das
  Register zählt **Befunde**, der `BEFUNDBERICHT.md` daneben **betroffene Vorlagen** — dieselbe
  Sache ergibt in beiden Systemen verschiedene Zahlen → [[haeufige-abrechnungsfehler]].
