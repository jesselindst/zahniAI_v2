---
titel: BEB 97
aliase: [BEB, Bundeseinheitliche Benennungsliste, BEB Zahntechnik, Privatabrechnung Labor]
labels: [Abrechnung, BEB97]
quellen: [raw/recherche-2026-08/beb_stand.md, kataloge/beb97_zahniAI_2026_v1.json]
stand: 2026-08-05
gueltig_von: 1997-01-01
gueltig_bis:
---

Leistungsverzeichnis für private zahntechnische Leistungen, herausgegeben vom Verband Deutscher Zahntechniker-Innungen. 1996 entwickelt, 1997 veröffentlicht. Gegenstück zum [[bel-ii]] auf der privaten Seite. Einstiegsseite für alles BEB.

## Rechtscharakter

Die BEB 97 ist eine reine Benennungs- und Nomenklaturliste. Sie ist weder Preisliste noch Gebührenordnung. Eine staatliche Gebührenordnung für private zahntechnische Leistungen existiert nicht; jedes Labor kalkuliert und bepreist selbst.

Der GOZ-Kommentar der Bundeszahnärztekammer hält fest, dass BEB und BEL für die GOZ-Abrechnung keinen bindenden Rechtscharakter haben und nur als Berechnungsgrundlage genannt werden können.

Daraus folgt eine Ungenauigkeit, die verbreitet ist: Die Formulierung, Mehrkosten würden nach BEB abgerechnet, trifft normativ nicht zu. Genannt ist in den Richtlinien die GOZ; die BEB ist die übliche Kalkulationsgrundlage dafür. Siehe [[versorgungsform]] und [[material-privat-goz]].

## Preisbildung über Minuten

Der Katalog trägt keine Preise, sondern Planzeiten in Minuten und eine Hauptgruppe. Der Preis entsteht im Labor aus Planzeit mal betriebsindividuellem Kostensatz der Hauptgruppe.

Deshalb stehen BEB-Preise nicht im Wiki. Zwei Labore kommen mit derselben Position legitim zu verschiedenen Preisen; ein Preis auf einer Wissensseite wäre für jedes andere Labor falsch.

Für die Vergleichsmatrix beim Labor-Customizing folgt daraus: Eine Laborposition kann eine Katalogposition ersetzen, obwohl der Preis abweicht. Maßgeblich ist der Leistungsinhalt.

## Hauptgruppen

Die erste Ziffer der Positionsnummer folgt der Hauptgruppe. Die Hauptgruppe bestimmt den Kostensatz und sagt zugleich, für welche Art Arbeit die Position gedacht ist.

| Hauptgruppe | Bereich |
|---|---|
| HG0 | Arbeitsvorbereitung, Modelle, Stümpfe, Hilfsteile, Dokumentation, Zuschläge |
| HG1 | Kunststoffarbeiten, Provisorien, Verblendungen, Basen |
| HG2 | Guss- und Frästechnik, Metallbasis, Modellguss, Kronen, Brückenglieder, CAD-Konstruktion |
| HG3 | Verankerungselemente, Teleskope, Geschiebe, Stege, Sekundärteile |
| HG4 | Tertiärstrukturen, Passungen, Schienen |
| HG5 | Oberflächenbearbeitung, Konditionieren, Nachbearbeiten |
| HG6 | Prothetik, Aufstellung, Fertigstellung, Sonderverfahren |
| HG7 | Kieferorthopädie |

Eine Position aus der falschen Hauptgruppe ist ein Abrechnungsfehler, auch wenn der Kurztext passt. 6411 Spezialpressverfahren liegt in HG6 und deckt Prothesen ab; für eine gepresste Lithiumdisilikatkrone ist es die falsche Position. 2515 beschreibt ein Kunststoff-Onlay und trägt kein Komposit-Onlay.

## Komplettposition und Einzelschritte schließen einander aus

Der Katalog führt für dieselbe Arbeit vielfach beides: eine Komplettposition und die Einzelschritte. Beide zusammen sind Doppelabrechnung.

| Komplettposition | daneben nicht abrechenbar |
|---|---|
| 2807, 2810, 2815, 2829 vollständig verblendet | 2612, 2616 separate Verblendung |
| 2552 bis 2554 und 2844 bis 2846 vollverblendete CAD/CAM-Einheiten | dieselbe Verblendung erneut |
| 2613, 2653 | dieselbe Verblendung erneut |

## BEL und BEB nicht für dieselbe Arbeit

Ebenfalls Doppelabrechnung, aber schwerer zu erkennen, weil zwei Kataloge im Spiel sind. 102 4 Krone für vestibuläre Verblendung zusammen mit 162 0 Vestibuläre Verblendung Keramik deckt dieselbe Leistung ab wie die BEB-Positionen 2122, 2314 und 2612. Leistungsbestandteile sind mit der Position abgegolten (BEL II, Anlage 1, § 3 Ziffer 3), siehe [[nebeneinander-ausschluesse-bel]].

In einer reinen Regelversorgung hat der BEB keinen Platz. Jede angesetzte BEB-Position macht die Versorgung gleichartig und löst die Mehrkostenvereinbarung aus, siehe [[versorgungsform]].

## Katalogschwächen

Der Katalog enthält 1103 Positionen. Bekannte Schwächen, ermittelt aus `kataloge/beb97_zahniAI_2026_v1.json`:

- 32 Kurztexte sind doppelt vergeben. Kritisch bei identischem Text und abweichender Kalkulation: 0917 und 2848 tragen beide „Konstruktion CAD-Krone zur Verblendung", die eine in HG0 mit 40 Minuten, die andere in HG2 mit 45 Minuten. Weitere Paare sind 0909 und 2840, 3805 mit 4122, 4421 und 7122 sowie 1360 und 3215.
- Die Nummernfolge hat Lücken, die zu Erfindungen einladen. 2026 Ney-Stiel existiert, 2027 und 2028 nicht.
- 135 Nummern kommen auch im BEL vor, 33 davon mit anderer Bedeutung, siehe [[positionskollision-bel-beb97]].

## Stand 2026

Die BEB 97 ist nach Fachverlagsangaben weiterhin die am häufigsten genutzte Liste. Inhaltlich gilt sie als veraltet, vor allem bei digitalen Verfahren; originäre Positionen für 3D-Druck oder Datensatzhandling enthält sie nicht. Labore legen dafür eigene Nummern an und kalkulieren neu, siehe [[cad-cam-einstufung]].

Nachfolger ist die BEB Zahntechnik in der 4. Auflage 2023 mit rund 153 Digitalpositionen. Ein Wechsel ist nicht erzwungen; maßgeblich ist, welches Verzeichnis das Labor seiner Kalkulation zugrunde legt. Im Repository ist das die BEB 97.

Der BEB-Volltext ist ein Lizenzprodukt des Verbands und nicht frei zugänglich. Aussagen zur Binnenlogik auf dieser Seite stützen sich auf den Katalog im Repository und auf Fachliteratur, nicht auf einen amtlichen Text.

Verwandt: [[positionskollision-bel-beb97]] · [[material-privat-goz]] · [[versorgungsform]] · [[bel-ii]]
