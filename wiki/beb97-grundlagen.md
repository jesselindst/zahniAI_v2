# BEB 97 — Aufbau und Abrechnungslogik

Quelle: [[quelle-beb97]]; Katalog `kataloge/beb97_zahniAI.json` (1103 Positionen).
Auswertung aus [[quelle-review-vorlagen-2026-08]].

## Preisbildung: Zeit statt Preis

Der BEB-Katalog enthält keine Preise, sondern Planzeiten (`dauer_min`) und eine
Hauptgruppe (`hg`). Der Preis entsteht im Labor:

```
Position = dauer_min × Kostensatz(Hauptgruppe)
```

Der Kostensatz ist betriebsindividuell — deshalb ist die BEB nur Nomenklatur, keine
Gebührenordnung. Zwei Labore mit derselben BEB-Position kommen legitim zu verschiedenen Preisen.

Folge für die Vergleichsmatrix beim Labor-Customizing: Eine Labor-Position kann eine
ZahniAI-Position ersetzen, obwohl der Preis abweicht — maßgeblich ist der Leistungsinhalt,
nicht die Zahl.

## Hauptgruppen sind Abrechnungsinhalt, keine Sortierung

Die Hauptgruppe bestimmt den Kostensatz und damit den Preis. Sie sagt zugleich, für welche
Art von Arbeit die Position gedacht ist.

| HG | Bereich |
|---|---|
| HG0 | Arbeitsvorbereitung: Modelle, Stümpfe, Hilfsteile, Dokumentation, Zuschläge |
| HG1 | Kunststoff: Provisorien, Verblendungen, Basen |
| HG2 | Guss- und Frästechnik: Metallbasis, Modellguss, Kronen, Brückenglieder, CAD-Konstruktion |
| HG3 | Verankerung: Teleskope, Geschiebe, Stege, Sekundärteile |
| HG4 | Tertiärstrukturen, Passungen, Schienen |
| HG5 | Oberflächen: Konditionieren, Polieren, Nachbearbeiten |
| HG6 | Prothetik: Aufstellung, Fertigstellung, Sonderverfahren |
| HG7 | Kieferorthopädie |
| HG8 | Instandsetzung, Erweiterung, Unterfütterung (Grund-/Leistungseinheiten, 8001–8851) |
| HG9 | Zuschläge/Auslagen: 9330 Versand, 9700 NEM-Verarbeitungsaufwand, 9850 3D-Modell |

HG8 und HG9 fehlten in früheren Fassungen dieser Seite — zusammen 67 der
1103 Positionen. Wer Reparaturleistungen in HG2 oder HG6 sucht, findet dort nichts Passendes und
greift zur falschen Position.

Eine Position aus der falschen Hauptgruppe ist ein Abrechnungsfehler, auch wenn der
Kurztext passt. Belege aus dem Review:

| angesetzt | Problem |
|---|---|
| 6411 „Spezialpressverfahren" für eine gepresste Lithiumdisilikat-Krone | HG6 = Prothesen, nicht Kronen |
| 2515 „Kunststoff-Onlay" für ein Komposit-Onlay | falsches Material im Leistungstext |
| 2603 für eine nicht-PMMA-Arbeit | Katalogtext ist neutral („Verblendschale aus Kunststoff"); die PMMA-Einschränkung stammt aus dem Review, nicht aus dem Katalog. **VERIFIZIEREN** |

## Komplettpositionen und ihre Einzelschritte schließen sich aus

Der BEB kennt für dieselbe Arbeit oft beides: eine Komplettposition und die Einzelschritte.
Beide zusammen sind Doppelabrechnung.

| Komplettposition | schließt aus |
|---|---|
| 2807 / 2810 / 2815 / 2829 „… vollständig verblendet" | separate Verblendung 2612 / 2616 |
| 2552–2554, 2844–2846 (vollverblendete CAD/CAM-Einheiten) | dieselbe Verblendung nochmals |
| 2613, 2653 | dito |

Diese Doppelansätze sind der häufigste Einzelfall innerhalb der größten Befundkategorie des
Reviews (`positionen`: 198 Befunde in 190 der 228 Vorlagen). Die Kategorie umfasst daneben auch
falsche und unzulässige Positionen; die 198 sind ihr also nicht allein zuzurechnen.
Aufschlüsselung → [[haeufige-abrechnungsfehler]].

## BEL und BEB nicht für dieselbe Arbeit mischen

Ebenfalls Doppelabrechnung, und schwerer zu erkennen, weil zwei verschiedene Kataloge im Spiel
sind:

| BEL | zugleich angesetzt | Bewertung |
|---|---|---|
| 1024 Krone für vestibuläre Verblendung + 1620 Verblendung Keramik | BEB 2122 / 2314 / 2612 | dieselbe Leistung zweimal |

Rechtsgrundlage der Kritik: § 2 Ziff. 4 der Einleitenden Bestimmungen (abschließende Liste
des zusätzlich Abrechenbaren, alles Übrige ist mit der Positionsvergütung abgegolten) sowie die
Leistungstexte der jeweiligen Positionen, die die Teilschritte ausdrücklich einschließen
→ [[bel-ii-zusatzkosten-material]], [[bel-gruppe-festsitzender-zahnersatz]].

Nicht einschlägig ist § 3 Ziff. 3 — der regelt die Pflichtangaben der Rechnung, nicht die Frage,
was abgegolten ist ([[bel-ii-rechnungsstellung]]). Er wirkt hier nur mittelbar: Weil alle
erbrachten Leistungen in *einer* Rechnung stehen müssen, ist auch das Aufteilen derselben Arbeit
auf getrennte BEL- und BEB-Rechnungen unzulässig. → [[bel-ausschlussregeln]]

In einer reinen Regelversorgung hat der BEB nichts zu suchen: Jede angesetzte
BEB-Position macht die Versorgung gleichartig und löst die Mehrkostenvereinbarung aus.
→ [[festzuschuss-versorgungsformen]]

## Nummernfallen

- 135 Nummern existieren in beiden Katalogen, 33 davon mit völlig anderer Bedeutung, zwei
  vertauscht → [[beb-bel-nummernkollisionen]]
- 32 doppelt vergebene Kurztexte innerhalb des BEB; kritisch 0917/2848 (textgleich,
  HG0/40 min gegenüber HG2/45 min)
- Lücken in der Nummernfolge laden zu Erfindungen ein: 2026 existiert, 2027/2028 nicht

## Verwandt

- [[quelle-beb97]] · [[beb-bel-nummernkollisionen]]
- [[material-abrechnung-privat]] — was neben den BEB-Positionen berechnet wird
- [[haeufige-abrechnungsfehler]]
