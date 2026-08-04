# Wiki – Index

Katalog aller Wiki-Seiten. **Bei jedem Ingest mitpflegen.**
Einstieg für eine Abrechnungsfrage: erst hier die passenden Seiten wählen, dann nur diese
öffnen.

## Quellen
| Seite | Inhalt | Stand |
|---|---|---|
| [quelle-bel-ii-2014](quelle-bel-ii-2014.md) | BEL II – 2014, Bundeseinheitliches Verzeichnis abrechnungsfähiger zahntechnischer Leistungen (§ 88 Abs. 1 SGB V). Vertragsparteien, Aufbau, Verbindlichkeit. **Bei 002 3 und 005 1/2/3 überholt.** Raw: `raw/BEL_II_01_01_2022.pdf` | 01.01.2022 |
| [quelle-aenderungsvereinbarung-bel-ii-2023](quelle-aenderungsvereinbarung-bel-ii-2023.md) | Änderungsvereinbarung VDZI ↔ GKV-SV vom 14.11.2022: Neufassung 002 3 und 005 1/2/3, Bundesmittelpreis. **Geht dem BEL II 01.01.2022 vor.** Raw: `raw/VDZI - Verband Deutscher Zahntechniker-Innungen.pdf` | 01.01.2023 |

*Noch nicht ingested (liegt in `raw/_inbox/`):* `BMP_2026_Leistungen_Regelversorgung.pdf`

## Grundlagen & Konzepte
| Seite | Inhalt |
|---|---|
| [bel-ii-grundlagen](bel-ii-grundlagen.md) | Wann gilt BEL II? Regelversorgung/KFO/Aufbissbehelfe/UKPS, Kompatibilitäts-Grundregel, Informationspflicht des Zahnarztes, Systematik der L-Nummern (`___ 5` = UKPS, `___ 8` = Implantat) |
| [bel-ii-rechnungsstellung](bel-ii-rechnungsstellung.md) | Pflichtangaben (L-Nr. + Kurztext), Herstellungsort, Fremdleistungen, arbeitsteilige Fertigung, Konformitätserklärung nach VO (EU) 2017/745, Aufbewahrungsfristen |
| [bel-ii-zusatzkosten-material](bel-ii-zusatzkosten-material.md) | Was **neben** den Leistungen abrechenbar ist: Konfektionsfertigteile vs. konfektionierte Hilfsteile, EM-Legierungen, Lote (75 %-Regel), Registrierbesteck |
| [bel-ii-implantatversorgung](bel-ii-implantatversorgung.md) | Die `___ 8`-Positionen, Nr. 36 a (Einzelzahnlücke) vs. Nr. 36 b (atrophierter zahnloser Kiefer), Bestätigungspflicht des Zahnarztes |
| [bel-ii-ukps](bel-ii-ukps.md) | Unterkieferprotrusionsschiene: geschlossener Leistungskreis, vollständige Positionsliste, feste Mengenobergrenzen |
| [bel-preisbildung-festzuschuss](bel-preisbildung-festzuschuss.md) | Drei Preisarten je L-Nr. (Bundesmittelpreis / regionale Vergütung / `bel.json`) — welche in den KV gehört; Kopplung an die G-BA-Festzuschuss-Richtlinie, kostenneutrale Einrechnung |

## Leistungsgruppen (Verzeichnisteil)
| Seite | L-Nr. |
|---|---|
| [bel-gruppe-arbeitsvorbereitung](bel-gruppe-arbeitsvorbereitung.md) | 001 0 – 032 0 · Modelle, Bisslagefixierung, Basen/Löffel, Registrierung, Provisorien |
| [bel-gruppe-festsitzender-zahnersatz](bel-gruppe-festsitzender-zahnersatz.md) | 101 3 – 165 0 · Kronen, Brückenglieder, Teleskope, Geschiebe/Anker, Verblendungen |
| [bel-gruppe-modellguss](bel-gruppe-modellguss.md) | 201 0 – 212 0 · Metallbasis, gegossene Halte-/Stützelemente, Rückenschutzplatte |
| [bel-gruppe-herausnehmbarer-zahnersatz](bel-gruppe-herausnehmbarer-zahnersatz.md) | 301 0 – 384 0 · Aufstellung/Fertigstellung, gebogene Halteelemente, Sonderkunststoffe |
| [bel-gruppe-aufbissbehelfe](bel-gruppe-aufbissbehelfe.md) | 401 0 – 404 0 · Schienen mit/ohne adjustierte Oberfläche, Umarbeiten, semipermanente Schiene |
| [bel-gruppe-kieferorthopaedie](bel-gruppe-kieferorthopaedie.md) | 701 0 – 751 0 · Basen, Schrauben, Bögen, Federn, Verbindungs-/Halteelemente |
| [bel-gruppe-reparatur-erweiterung](bel-gruppe-reparatur-erweiterung.md) | 801 0 – 870 0 · Grundeinheiten + Leistungseinheiten, Unterfütterung, Basiserneuerung |
| [bel-gruppe-zuschlaege-versand](bel-gruppe-zuschlaege-versand.md) | 933 0/5/8, 970 0 · Versandkosten, NEM-Verarbeitungsaufwand |

## Querschnitt-Regeln (Prüflisten vor KV-Ausgabe)
| Seite | Inhalt |
|---|---|
| [bel-ausschlussregeln](bel-ausschlussregeln.md) | Alle „nicht nebeneinander / nur wenn / stattdessen"-Regeln: gegenseitige Ausschlüsse, Grundeinheit-vs-Unterfütterung, Artikulator-Verbote, Umleitungsregeln, Praxis-/Gewerbelabor |
| [bel-mengenregeln](bel-mengenregeln.md) | Wie oft ansetzbar — sortiert nach Bezugsgröße (je Zahn / je Kiefer / je Werkstück / je Vorgang), Stützstiftregistrierung, UKPS-Obergrenzen |

## Zugehörige Repo-Artefakte (nicht im Wiki gespiegelt)
- `kataloge/bel.json` — L-Nr., Kurztext, **Preise** (Gewerbelabor / Praxislabor), 9 Gruppen
- `kataloge/beb97_zahniAI.json` — BEB 97
- `vorlagen/` — Abrechnungsvorlagen je Konfigurator-Bereich
