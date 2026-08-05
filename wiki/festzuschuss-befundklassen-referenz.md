# Festzuschuss — Befundklassen 1 bis 8 im Einzelnen

Referenzliste mit Bezugsgrößen und den Verwechslungen, die im Vorlagenreview aufgetreten sind.
Quellen: [[quelle-festzuschuss-richtlinie]] Teil B; Befundtexte aus dem Festzuschusskatalog
(54 Befunde). Fehleinordnungen aus [[quelle-review-vorlagen-2026-08]].

Keine Beträge — die ändern sich jährlich. → [[festzuschuss-haertefall-bonus]]

> Wo der Festzuschusskatalog liegt, und warum er nicht genügt.
> Er ist kein Repo-Artefakt, sondern die Datenbanktabelle `catalog_festzuschussbefund`
> des ZahniAI-Systems (im `findings_register.json` als `reference/festzuschuss_befunde.json`
> exportiert). Unter `kataloge/` ist er nicht zu finden.
>
> Der Review vom 04.08.2026 hat ihn als veraltet befundet: Die Tabelle stand auf Stand 2025,
> während seit 01.01.2026 neue Beträge gelten (G-BA 05.12.2025 — Befund 1.1 ohne Bonus
> 229,25 € → 239,03 €). Ob das inzwischen behoben ist, ist nicht verifiziert.
>
> Für diese Seite heißt das: Die Befundsystematik und die Bezugsgrößen sind belegt, die
> Beträge nicht. Vor jedem KV den Katalogstand prüfen und im Zweifel gegen die
> GKV-SV-Betragstabelle des laufenden Jahres gegenrechnen
> ([[quelle-festzuschuss-richtlinie]]). **VERIFIZIEREN**

## Klasse 1 — Erhaltungswürdiger Zahn

| Nr. | Befund | Bezug |
|---|---|---|
| 1.1 | Weitgehende Zerstörung der klinischen Krone / unzureichende Retention | je Zahn |
| 1.2 | Große Substanzdefekte bei erhaltener vestibulärer und/oder oraler Substanz | je Zahn |
| 1.3 | wie 1.1, aber im Verblendbereich (15–25 / 34–44) — Zuschlag | je Verblendung |
| 1.4 | Endodontisch behandelter Zahn, konfektionierter metallischer Stiftaufbau | je Zahn |
| 1.5 | Endodontisch behandelter Zahn, gegossener metallischer Stiftaufbau | je Zahn |

1.4 gegenüber 1.5: konfektioniert (adhäsiv befestigt) gegen gegossen (zementiert). Beide setzen
einen endodontisch behandelten Zahn voraus.

1.4 und 1.5 sind nicht die Adhäsivbrücke. Diese Verwechslung stand in mehreren Vorlagen und
im README der Adhäsivbrücke. Die Adhäsivbrücke gehört zu 2.1/2.2 (+2.7).

Nicht-metallische Stifte (Glasfaser, Zirkon, Carbon) und Titanstifte sind bei
GKV-Versicherten gleichartig mit Festzuschuss 1.4, nicht „Privatleistung ohne Zuschuss".

## Klasse 2 — Zahnbegrenzte Lücken, Lückensituation I

Voraussetzung: höchstens vier fehlende Zähne je Kiefer, ansonsten geschlossene Zahnreihe,
keine Freiendsituation.

| Nr. | Befund | Bezug |
|---|---|---|
| 2.1 | ein fehlender Zahn | je Lücke |
| 2.2 | zwei nebeneinander fehlende Zähne | je Lücke |
| 2.3 | drei nebeneinander fehlende Zähne | je Kiefer |
| 2.4 | Frontzahnlücke mit vier nebeneinander fehlenden Zähnen | je Kiefer |
| 2.5 | unmittelbar angrenzende weitere zahnbegrenzte Lücke mit einem fehlenden Zahn | je Lücke |
| 2.6 | disparallele Pfeilerzähne bei festsitzendem ZE — Zuschlag | je Lücke |
| 2.7 | fehlender Zahn im Verblendbereich — Zuschlag | je Verblendung |

Der Wechsel der Bezugsgröße von je Lücke (2.1/2.2) auf je Kiefer (2.3/2.4) wird
regelmäßig übersehen. Im Review: dreigliedrige Implantatbrücken mit 2.1 statt 2.3,
viergliedrige mit 2.2 statt 2.4/3.1.

2.7 gilt für den *ersetzten* Zahn und für einen an die Lücke angrenzenden Brückenanker
im Verblendbereich, nicht pauschal für alle Anker.

Adhäsivbrücke: Regelversorgung mit Metallgerüst (BEL 1023 „Flügel für Adhäsivbrücke",
BEMA 93a/93b). Befunde 2.1 bzw. 2.2 + 2.7. Keramikgerüst ist gleichartig.
Wiederherstellung: Befund 6.8.1 je Flügel *(Einführung zum 01.01.2019 — ohne hinterlegte
Fundstelle,* **VERIFIZIEREN***)*.
Die Altersgrenze 14.–21. Lebensjahr gilt nur bei zwei nebeneinander fehlenden Schneidezähnen
→ [[quelle-zahnersatz-richtlinie]] Nr. 22/24.

## Klasse 3 — Lückensituation II

| Nr. | Befund | Bezug |
|---|---|---|
| 3.1 | alle zahnbegrenzten Lücken außerhalb 2.1–2.5 und 4 oder Freiendsituation | je Kiefer |
| 3.2 | verkürzte Zahnreihe (beidseitig bis Eckzahn/1. Prämolar bzw. einseitig) — Zuschlag | max. 2× je Kiefer |

3.1 ist der tragende Modellguss-Befund. Belegt über das `regelversorgung`-Array im
Festzuschusskatalog: 3.1 enthält BEL 2010 (Metallbasis), 2.7 nicht.
*(Beleg stammt aus dem Review-Stand des Katalogs; die Datei liegt nicht im Repo, siehe Hinweis
oben.)*

Im Review führten mehrere Modellguss-Vorlagen „2.7 bei Freiend". Das ist falsch: 2.7 ist der
Verblendzuschuss je ersetztem Zahn und gehört zum festsitzenden Zahnersatz.

Umgekehrt ist bei den Lückenbefunden 2.1–2.5 die Brücke Regelversorgung — ein
Modellguss ist dort andersartig.

## Klasse 4 — Restzahnbestand bis 3 Zähne oder zahnloser Kiefer

| Nr. | Befund | Bezug |
|---|---|---|
| 4.1 / 4.3 | Restzahnbestand bis 3 Zähne — OK / UK | je Kiefer |
| 4.2 / 4.4 | zahnloser OK / UK | je Kiefer |
| 4.5 | Notwendigkeit einer Metallbasis — Zuschlag | je Kiefer |
| 4.6 | Restzahnbestand ≤ 3 Zähne mit dentaler Verankerung (Kombiversorgung) | je Ankerzahn |
| 4.7 | Verblendung einer Teleskopkrone im Verblendbereich — Zuschlag | je Ankerzahn |
| 4.8 | dentale Verankerung durch Wurzelstiftkappen | je Ankerzahn |
| 4.9 | schwierig zu bestimmende Kieferlagebeziehung (Totalprothese/Deckprothese) | — |

Die Totalprothese gehört zu 4.2 / 4.4, nicht zu 5.x. Im Review führten die
Totalprothesen-Vorlagen durchgängig Klasse 5 — das hätte den Agenten auf einen deutlich
niedrigeren Zuschuss geführt.

Metallbasis (4.5): mit medizinischer Indikation bleibt die Versorgung Regelversorgung
(Zuschlag 4.5 + BEMA 98e, Indikation dokumentieren). Die ZE-RL nennt als Ausnahmefälle
insbesondere Torus palatinus und Exostosen. Ohne Indikation ist die Versorgung gleichartig.
*VERIFIZIEREN: Ausgeprägter Würgereiz und Acrylat-Allergie werden vielfach als Indikation
genannt, sind in der Richtlinie so aber nicht ausgewiesen.*

## Klasse 5 — Interimsversorgung

| Nr. | Befund | Bezug |
|---|---|---|
| 5.1 | Verlust von bis zu 4 Zähnen | je Kiefer |
| 5.2 | Verlust von 5 bis 8 Zähnen | je Kiefer |
| 5.3 | Verlust von über 8 Zähnen | je Kiefer |
| 5.4 | zahnloser OK oder UK | je Kiefer |

Voraussetzung durchgängig: eine endgültige Versorgung ist nicht sofort möglich.
Klasse 5 ist die Interimsversorgung, nicht die definitive Prothese.

## Klasse 6 — Wiederherstellung konventioneller Zahnersatz

Reparatur, Erweiterung, Unterfütterung. Die für die Zahntechnik wichtigsten:

| Nr. | Befund |
|---|---|
| 6.0 – 6.3 | wiederherstellungsbedürftige herausnehmbare/Kombinationsversorgung, gestaffelt |
| 6.4 / 6.4.1 / 6.5 / 6.5.1 | erweiterungsbedürftige Versorgung mit Befundveränderung |
| 6.6 | verändertes Prothesenlager bei Teil-Zahnersatz, je Prothese |
| 6.7 | verändertes Prothesenlager bei totalem ZE / Deckprothese, je Kiefer |
| 6.8 | wiederherstellungsbedürftiger festsitzender rezementierbarer ZE, je Zahn |
| 6.8.1 | je Flügel einer Adhäsivbrücke |
| 6.9 | wiederherstellungsbedürftige Facette/Verblendung im Verblendbereich |
| 6.10 | erneuerungsbedürftiges Primär- oder Sekundärteleskop, je Zahn |

## Klasse 7 — Suprakonstruktionen: nur Erneuerung und Wiederherstellung

| Nr. | Befund | Grenze |
|---|---|---|
| 7.1 | erneuerungsbedürftige Suprakonstruktion (Einzelzahnlücke), je implantatgetragene Krone | — |
| 7.2 | Erneuerung darüber hinaus, je Krone/Anker/Glied | max. 4× je Kiefer |
| 7.3 | Wiederherstellung (Facette), je Facette | — |
| 7.4 | Wiederbefestigung rezementierbar/verschraubbar, je Krone/Anker | — |
| 7.5 | erneuerungsbedürftige implantatgetragene Prothesenkonstruktion, je Konstruktion | — |
| 7.6 | Zuschlag je implantatgetragenem Konnektor bei atrophiertem zahnlosem Kiefer (nur zu 7.5) | max. 4× je Kiefer |
| 7.7 | Wiederherstellung / Umgestaltung einer vorhandenen Totalprothese zur Suprakonstruktion | — |

Bei Erstversorgung ist Klasse 7 immer falsch. Dort gilt der Befund vor der Implantation
(FZ-RL Teil A Nr. 6) → [[festzuschuss-grundlagen]].

## Klasse 8 — Nicht vollendete Behandlung

Teilleistungen, gestaffelt als Prozentsatz des jeweiligen Befundzuschusses:

| Nr. | Situation | Anteil |
|---|---|---|
| 8.1 | nach Präparation eines Zahnes / einer Teleskopkrone / Wurzelstiftkappe | 50 % |
| 8.2 | dito, wenn weitergehende Maßnahmen durchgeführt wurden | 75 % |
| 8.3 | nach Präparation der Ankerzähne einer Brücke | 50 % der Befunde 2.1 ff. |
| 8.4 | dito mit weitergehenden Maßnahmen | 75 % |
| 8.5 / 8.6 | nach Abformung und Bissermittlung für Teilprothese / Cover Denture | gestaffelt |

## Verwandt

- [[festzuschuss-grundlagen]] · [[festzuschuss-versorgungsformen]] ·
  [[festzuschuss-haertefall-bonus]]
- [[haeufige-abrechnungsfehler]]
