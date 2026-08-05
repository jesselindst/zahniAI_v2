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

| Hauptgruppe | Bereich | Positionen |
|---|---|---|
| HG0 | Arbeitsvorbereitung, Modelle, Stümpfe, Hilfsteile, Dokumentation, Scan und CAD-Auftragsanlage | 211 |
| HG1 | Kunststoffarbeiten, Provisorien, Verblendungen, Basen, Bisswälle | 105 |
| HG2 | Kronen, Brückenglieder, Inlays und Onlays, Schultern, CAD/CAM-Einheiten | 267 |
| HG3 | Verankerungselemente, Teleskope, Geschiebe, Stege, Riegel, Sekundärteile, Fertigstellung je Zahn | 127 |
| HG4 | Metallbasis, Klammern, Bügel, Rückenschutzplatten, Passungen | 82 |
| HG5 | Lötungen, lötfreie Verbindung und Laserschweißen, Vergoldung, Konditionieren | 37 |
| HG6 | Aufstellung, Fertigstellung, Basisteile, Gussgitter und Retentionen | 60 |
| HG7 | Kieferorthopädie, Schienen, Resektionsprothetik | 147 |
| HG8 | Instandsetzung, Unterfütterung, Erweiterung | 64 |
| HG9 | Versand, Verarbeitungsaufwand NEM, 3D-Modell-Material | 3 |

Eine Position aus der falschen Hauptgruppe ist ein Abrechnungsfehler, auch wenn der Kurztext passt. 6411 Spezialpressverfahren liegt in HG6 und deckt Prothesen ab; für eine gepresste Lithiumdisilikatkrone ist es die falsche Position. 2515 beschreibt ein Kunststoff-Onlay und trägt kein Komposit-Onlay.

## Komplettposition und Einzelschritte schließen einander aus

Der Katalog führt für dieselbe Arbeit vielfach beides: eine Komplettposition und die Einzelschritte. Beide zusammen sind Doppelabrechnung.

| Komplettposition | daneben nicht abrechenbar |
|---|---|
| 2807, 2810, 2815 vollständig verblendet | 2612, 2616 separate Verblendung |
| 2613, 2653 | dieselbe Verblendung erneut |

## BEL und BEB nicht für dieselbe Arbeit

Ebenfalls Doppelabrechnung, aber schwerer zu erkennen, weil zwei Kataloge im Spiel sind. 102 4 Krone für vestibuläre Verblendung zusammen mit 162 0 Vestibuläre Verblendung Keramik deckt dieselbe Leistung ab wie die BEB-Positionen 2121, 2313 und 2611 — die Teilverblendungsvarianten. Vestibulär ist Teilverblendung; 2122, 2314 und 2612 sind die Vollverblendungsvarianten und damit nicht deckungsgleich. Die Zuordnung ist aus den Kurztexten beider Kataloge erschlossen, ein Dokument, das BEB gegen BEL abbildet, liegt nicht vor.

Material ist mit den Vergütungen für die aufgeführten Leistungen abgegolten, soweit es nicht in der Liste der gesondert abrechenbaren Materialien steht (BEL II, Anlage 1, § 2 Ziffer 4). Welche Teilleistungen in einer Position eingeschlossen sind, ergibt sich aus ihrem Leistungsinhalt im Verzeichnisteil. Siehe [[nebeneinander-ausschluesse-bel]] und [[gesondert-abrechenbare-materialien-bel]].

In einer reinen Regelversorgung hat der BEB keinen Platz. Jede angesetzte BEB-Position macht die Versorgung gleichartig und löst die Mehrkostenvereinbarung aus, siehe [[versorgungsform]].

## Katalogschwächen

Der Katalog enthält 1103 Positionen: 779 als `standard`, 324 als `individuell`. Der Katalog erklärt die Typen nicht, drei Befunde grenzen ihre Bedeutung aber ein.

Erstens tragen ausschließlich die 324 `individuell`-Positionen ein Feld `quellen`, keine einzige `standard`-Position. Die Herkunftsschlüssel sind `intern` bei 210, `dent_content` bei 202 und `spitta` bei 136 Positionen, Mehrfachnennung möglich.

Zweitens sind von den 135 Nummern, die BEB und BEL gemeinsam haben, 101 `individuell` und die meisten davon praktisch textgleich mit dem BEL-Kurztext. Im `standard`-Bestand liegen nur 34 gemeinsame Nummern.

Drittens lassen sich drei Fälle einzeln nachweisen, in denen eine `individuell`-Position eine gespiegelte BEL-Position ist und die echte BEB-Position als `standard` in einer anderen Hauptgruppe steht: 1360 und 1370 gegen 3215, die Auflagen 3800 bis 3814 gegen 4118 bis 4421, und alle neun Positionen, die den 3D-Druck nennen.

Die Lesart ist damit belegt: `individuell` markiert nachträglich eingespiegelte Fremdpositionen, `standard` den originären Bestand. Endgültig entscheiden ließe sich das nur an einer Dokumentation des Katalog-Imports, die nicht im Repository liegt. Alle Aussagen dieser Seite und von [[positionskollision-bel-beb97]] hängen an dieser Unterscheidung.

Die erste Ziffer entspricht ausnahmslos der Hauptgruppe, bei allen 1103 Positionen ohne Abweichung. Die Nummernkreise: HG0 0001–0961, HG1 1001–1874, HG2 2001–2983, HG3 3001–3983, HG4 4001–4983, HG5 5001–5851, HG6 6001–6938, HG7 7001–7908, HG8 8001–8851, HG9 9330–9850.

Bekannte Schwächen, ermittelt aus `kataloge/beb97_zahniAI_2026_v1.json`:

- 32 Kurztexte sind doppelt vergeben. Kritisch bei identischem Text und abweichender Kalkulation: 0917 und 2848 tragen beide „Konstruktion CAD-Krone zur Verblendung", die eine in HG0 mit 40 Minuten, die andere in HG2 mit 45 Minuten. Weitere Paare sind 0909 und 2840, 3805 mit 4122, 4421 und 7122 sowie 1360 und 3215.
- Die Nummernfolge hat Lücken, die zu Erfindungen einladen. 2026 Ney-Stiel existiert, 2027 und 2028 nicht.
- Nummern, die auch im BEL vorkommen und dort etwas anderes bezeichnen, siehe [[positionskollision-bel-beb97]].

## Stand 2026

Die BEB 97 ist nach Fachverlagsangaben weiterhin die am häufigsten genutzte Liste. Inhaltlich gilt sie als veraltet, vor allem bei digitalen Verfahren; originäre Positionen für 3D-Druck oder Datensatzhandling enthält sie nicht. Die Datei führt solche Positionen durchaus — 0856, 0871, 0915, 0916, 0923, 0927, 0937, 0943 und 9850 nennen den Druck ausdrücklich —, aber alle davon sind `individuell`, also nachträglich ergänzt und nicht Teil des originären Bestands. Labore legen dafür eigene Nummern an und kalkulieren neu, siehe [[cad-cam-einstufung]].

Nachfolger ist die BEB Zahntechnik in der 4. Auflage 2023 mit rund 153 Digitalpositionen. Ein Wechsel ist nicht erzwungen; maßgeblich ist, welches Verzeichnis das Labor seiner Kalkulation zugrunde legt. Im Repository ist das die BEB 97.

Der BEB-Volltext ist ein Lizenzprodukt des Verbands und nicht frei zugänglich. Aussagen zur Binnenlogik auf dieser Seite stützen sich auf den Katalog im Repository und auf Fachliteratur, nicht auf einen amtlichen Text.

Verwandt: [[positionskollision-bel-beb97]] · [[material-privat-goz]] · [[versorgungsform]] · [[bel-ii]]
