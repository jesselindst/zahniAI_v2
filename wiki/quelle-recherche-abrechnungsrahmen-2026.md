---
titel: Quelle Recherche Abrechnungsrahmen 2026
aliase: [Vorlagenreview 2026, Rechercheberichte Juli 2026]
labels: [Quelle, Abrechnung, Regulatorik]
quellen: [raw/recherche-2026-08/festzuschuss.md, raw/recherche-2026-08/beb_stand.md, raw/recherche-2026-08/bel2_stand.md, raw/recherche-2026-08/materialabrechnung.md, raw/recherche-2026-08/cadcam_einstufung.md, raw/recherche-2026-08/neue_verfahren.md, raw/recherche-2026-08/verifikation_kernaussagen.md]
stand: 2026-08-05
---

## Dokument

| | |
|---|---|
| Titel | Recherche zum Abrechnungsrahmen 2026 und Prüfung der Abrechnungsvorlagen |
| Art | eigene Auswertung, kein externes Regelwerk |
| Zeitraum | 20.07. bis 04.08.2026 |
| Ablageort | `raw/recherche-2026-08/` |
| Umfang | sieben Rechercheberichte, dazu `findings_register.json` mit 642 Einzelbefunden |

Die Berichte schließen die Lücke zwischen dem BEL II und einem vollständigen Kostenvoranschlag: das Festzuschusssystem, die Einstufung der Versorgungsform, die private Abrechnungsschiene und die Einordnung digitaler Fertigungsverfahren. Grundlage sind Primärquellen des Gemeinsamen Bundesausschusses, der Kassenzahnärztlichen Bundesvereinigung, des GKV-Spitzenverbands, des Verbands Deutscher Zahntechniker-Innungen sowie die Gesetzestexte des SGB V und der GOZ.

Parallel wurden alle 228 Abrechnungsvorlagen des Konfigurators mit 9608 Positionszeilen gegen diese Quellen geprüft. Ergebnis sind 642 Befunde, davon 252 mit hoher Schwere.

## Berichte

| Datei | Inhalt | Abruf |
|---|---|---|
| `festzuschuss.md` | Festzuschuss-Richtlinie, Zahnersatz-Richtlinie, § 55 SGB V, Härtefall, Versorgungsformen, Adhäsivbrücke, Verblendgrenze, Suprakonstruktionen | 20.07.2026 |
| `bel2_stand.md` | gültige BEL-Fassung, Änderungsvereinbarung 2023, Rundschreiben, 970 0, UKPS | 20.07.2026 |
| `beb_stand.md` | BEB 97 gegen BEB Zahntechnik 2023, Rechtscharakter, Digitalpositionen | 21.07.2026 |
| `materialabrechnung.md` | § 2 Ziffer 4 BEL II, § 9 und § 10 GOZ, Nachweispflichten, abgegoltene Materialien | 20.07.2026 |
| `cadcam_einstufung.md` | Einstufung gefräster und gedruckter Arbeiten, Schienenfertigung, regionale Unterschiede | 20.07.2026 |
| `neue_verfahren.md` | 3D-Druck, Monolithik, digitale Totalprothetik, neue Werkstoffe | 20.07.2026 |
| `verifikation_kernaussagen.md` | Gegenprüfung der Kernaussagen | 21.07.2026 |

Jede Aussage in den Berichten trägt Quelle, Abrufdatum und Quellentyp. Die Hierarchie lautet: offizielle Körperschaft vor Fachliteratur vor Abrechnungsportal. Aussagen, die nur auf Portalebene belegt waren, sind nicht als gesichert übernommen. Nicht Belegbares ist als UNBELEGT markiert.

## Entstandene Seiten

| Seite | Herkunft |
|---|---|
| [[festzuschuss]] | `festzuschuss.md` |
| [[versorgungsform]] | `festzuschuss.md` |
| [[haertefall-und-bonus]] | `festzuschuss.md` |
| [[festzuschuss-befundklassen]] | `festzuschuss.md` |
| [[beb97]] | `beb_stand.md`, Katalogauswertung |
| [[positionskollision-bel-beb97]] | Abgleich der beiden Katalogdateien |
| [[material-privat-goz]] | `materialabrechnung.md` |
| [[cad-cam-einstufung]] | `cadcam_einstufung.md`, `neue_verfahren.md` |

Ergänzt wurden [[bel-ii]], [[verblendung-bel]], [[gesondert-abrechenbare-materialien-bel]], [[bel-gruppe-aufbissbehelfe]], [[implantatversorgung-bel]], [[bel-gruppe-modellguss]], [[bel-gruppe-arbeitsvorbereitung]] und [[bundesmittelpreis]].

## Nicht übernommen

Die 642 Einzelbefunde bleiben im Register. Sie sind vorlagenspezifisch; ins Wiki gehört das Regelwissen dahinter.

Festzuschussbeträge in Euro bleiben außen vor, weil sie jährlich neu festgesetzt werden. Legierungspreise ebenso, sie ändern sich täglich. BEB-Preise gehören nicht ins Wiki, weil der BEB nur Minutenwerte kennt und der Preis laborspezifisch ist.

## Offene Punkte

Die Quelle verweist auf Regelwerke, die im Wiki nicht als eigene Quelle vorliegen:

- Festzuschuss-Richtlinie des Gemeinsamen Bundesausschusses, Fassung mit Wirkung ab 01.01.2026
- Zahnersatz-Richtlinie in der Fassung vom 18.02.2016
- Festzuschuss-Kompendium der Kassenzahnärztlichen Bundesvereinigung
- Gemeinsames Rundschreiben zu Adhäsivbrücken vom 28.06.2016 sowie das Rundschreiben zum BEL II vom 19.03.2014
- Änderungsvereinbarung zum BEL II vom 14.11.2022, liegt als PDF in `raw/_inbox/`

Die Befundnummern des Festzuschusssystems sind keine Katalogpositionen und deshalb nicht als Positions-IDs geführt. Ein Katalog `fz` unter `kataloge/` würde sie prüfbar machen; er ist bislang nicht angelegt.

110 Punkte der Prüfung sind ausdrücklich offen. Dazu zählen die Zuordnung der GOZ-Nummern für den laborgefertigten Stiftaufbau, die Mengenlogik der BEB-Position 0918 und die Frage, ob ausgeprägter Würgereiz und Acrylatallergie als Indikation für eine Metallbasis gelten.
