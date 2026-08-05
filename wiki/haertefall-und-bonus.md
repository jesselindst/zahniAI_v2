---
titel: Härtefall und Bonus
aliase: [Bonusheft, Härtefallregelung, gleitende Härtefallregelung, Eigenanteil, Zuschussstufen]
labels: [Abrechnung, Regulatorik]
quellen: [raw/FZ-RL_2025-12-05_iK-2026-01-01.pdf, kataloge/fz_2026_v1.json, raw/recherche-2026-08/festzuschuss.md]
stand: 2026-08-05
gueltig_von: 2020-10-01
gueltig_bis:
---

Die Prozentstufen des Festzuschusses und ihre Wirkung auf den Eigenanteil. Ohne diese Angaben lässt sich der Eigenanteil aus einem Kostenvoranschlag nicht herleiten.

## Die vier Stufen

| Stufe | Voraussetzung | Grundlage |
|---|---|---|
| 60 Prozent | Grundfall | § 55 Abs. 1 Satz 2 SGB V |
| 70 Prozent | Untersuchungen in den letzten fünf Kalenderjahren lückenlos wahrgenommen | § 55 Abs. 1 Sätze 3 und 4 SGB V |
| 75 Prozent | dasselbe über zehn Kalenderjahre | § 55 Abs. 1 Satz 5 SGB V |
| 100 Prozent | Härtefall: 60 Prozent zuzüglich eines weiteren Betrags von 40 Prozent | § 55 Abs. 2 SGB V |

Vor dem 18. Lebensjahr sind halbjährliche, danach mindestens jährliche Untersuchungen nachzuweisen. Seit dem Gesundheitsversorgungsweiterentwicklungsgesetz 2021 ist in begründeten Ausnahmefällen eine Unterbrechung unschädlich; für 2020 galt eine Sonderregel.

Die Stufen 60, 70 und 75 Prozent gelten seit 01.10.2020. Zuvor lagen sie bei 50, 60 und 65 Prozent.

Härtefallkriterien sind geringe Bruttoeinnahmen unterhalb der Bezugsgrößengrenze sowie der Bezug von Sozialhilfe, Bürgergeld oder Leistungen nach dem Bundesausbildungsförderungsgesetz (§ 55 Abs. 2 Satz 2 ff. SGB V). Dazu tritt die gleitende Härtefallregelung nach § 55 Abs. 3 SGB V.

## Der Härtefall wirkt je nach Versorgungsform verschieden

Das ist die Stelle, an der Eigenanteilsrechnungen regelmäßig falsch werden.

Bei einer tatsächlich durchgeführten Regelversorgung gewähren die Kassen den weiteren Betrag von 40 Prozent „angepasst an die Höhe der für die jeweilige Regelversorgungsleistung tatsächlich anfallenden Kosten, höchstens jedoch in Höhe der … entstandenen Kosten" (FZ-RL, Teil A Nr. 4). Die Kasse trägt die Regelversorgung damit vollständig; es bleibt kein Eigenanteil. Ausgenommen sind Mehrkosten für Edelmetall oder Reinmetall statt Nichtedelmetall.

Bei gleichartiger oder andersartiger Versorgung leisten die Kassen laut FZ-RL, Teil A Nr. 5, „nur den Festzuschuss nach § 55 Absatz 1 Satz 2 SGB V und den Betrag in Höhe von 40 Prozent der … festgesetzten Beträge für die jeweilige Regelversorgung". Das ist der feste Tabellenbetrag ohne Anpassung an die tatsächlichen Regelversorgungskosten. Alle Mehrkosten trägt der Versicherte.

| | Härtefall bei Regelversorgung | Härtefall bei gleich- oder andersartiger Versorgung |
|---|---|---|
| Kasse trägt | tatsächliche Kosten der Regelversorgung | festen 100-Prozent-Betrag der Tabelle |
| Eigenanteil | keiner, außer Edelmetallmehrkosten | Gesamtkosten abzüglich des festen Betrags |

Die Protokollnotiz zu Teil A Nr. 4 hält fest, dass Festzuschüsse auch bei Nicht-Härtefällen höchstens in Höhe der entstandenen Kosten gewährt werden. Die Deckelung gilt also nicht nur im Härtefall.

Härtefall bedeutet damit nicht in jedem Fall Zuzahlungsfreiheit.

## Rechenweg

```
Regelversorgung
  Eigenanteil = tatsächliche Kosten (BEL und BEMA) − Festzuschuss
  Härtefall:    Eigenanteil = 0, ausgenommen Edelmetallmehrkosten

gleichartig
  Eigenanteil = Regelversorgungsanteil − Festzuschuss + Mehrkosten nach GOZ

andersartig
  Eigenanteil = Gesamtrechnung − erstatteter Festzuschuss
```

## Kontrollfall

Befund 1.1 mit Zuschlag 1.3, verblendete Krone im Verblendbereich.

| Lage | Leistung der Kasse |
|---|---|
| metallische Krone, vestibulär verblendet, kein Bonus | 60 Prozent zu 1.1 und 1.3 |
| dieselbe Krone, Bonusheft über zehn Jahre | 75 Prozent |
| dieselbe Krone, Härtefall | tatsächliche Kosten der Regelversorgung, Eigenanteil null |
| vollverblendete Zirkonkrone, Härtefall | fester 100-Prozent-Betrag zu 1.1 und 1.3; die Differenz zur Zirkonkrone trägt der Versicherte |

Der Befundkatalog führt je Befund sechs Beträge: die Bestandteile Honorar nach § 57 Abs. 1 SGB V und Material und Labor nach § 57 Abs. 2 SGB V, deren Summe der Härtefallbetrag ist, sowie die drei Abstaffelungen. Die Werte für 2026 stehen in [[festzuschussbetraege-2026]], für 2025 in [[festzuschussbetraege-2025]].

Ein mit Zahlen durchgerechneter Fall — dreigliedrige Brücke mit einmal 2.1 und dreimal 2.7 über alle vier Stufen, einschließlich der Deckelung im Härtefall — steht auf der Jahrgangsseite [[festzuschussbetraege-2026]]. Diese Seite bleibt betragsfrei, weil die Beträge jährlich wechseln.

## Offen

Die gleitende Härtefallregelung nach § 55 Abs. 3 SGB V ist oben nur benannt. Ihre Mechanik — Einkommensgrenzen, Berechnung des erhöhten Zuschusses im Grenzbereich — ist im Repository nirgends belegt; die Rechercheberichte nennen die Regelung nur in einer Aufzählung, ohne Grenzwerte und ohne Formel. Für eine Eigenanteilsberechnung im Grenzbereich reicht das nicht. Schließbar allein durch den Normtext des § 55 SGB V, der nicht vorliegt.

Verwandt: [[festzuschuss]] · [[versorgungsform]] · [[festzuschuss-befundklassen]] · [[festzuschussbetraege-2026]] · [[quelle-fz-rl-2026]]
