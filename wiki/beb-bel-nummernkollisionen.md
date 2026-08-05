# BEL und BEB: gleiche Nummer, andere Leistung

Eine Fehlerquelle beim Mischen der beiden Kataloge, die eine Existenzprüfung nicht abfängt.
Eigene Auswertung von `kataloge/bel.json` (175 L-Nrn.) gegen `kataloge/beb97_zahniAI.json`
(1103 Positionen), Stand 04.08.2026 → [[quelle-review-vorlagen-2026-08]].

## Der Umfang

135 der 175 BEL-Nummern kommen auch im BEB 97 vor. Bei rund 100 davon meint die Nummer in
beiden Katalogen ungefähr dasselbe (0051 Sägemodell, 1021 Vollkrone/Metall, 9700
Verarbeitungsaufwand NEM). Bei 33 Nummern bedeutet sie etwas völlig anderes.

Eine reine Existenzprüfung fängt das nicht ab. Die Nummer existiert ja, nur eben im
falschen Katalog. Wer prüft, ob „0213" ein gültiger Code ist, bekommt in beiden Fällen „ja".
Zu prüfen sind Nummer, Katalogzugehörigkeit und Leistungstext.

## Die 33 echten Kollisionen

| Nr. | BEL II | BEB 97 |
|---|---|---|
| 0010 | Modell | Spezialmodell |
| 0022 | Platzhalter einfügen | Okklusionsmodell für Sägesegmente |
| 0023 | Verwendung von Kunststoff | Modell für Einzelstümpfe |
| 0025 | Doublieren eines Modells UKPS | Dosierungsstumpf |
| 0030 | Set-up je Segment | Modell digitales Antagonistenmodell |
| 0112 | Fixator | Stumpf aus feuerfester Masse |
| 0115 | Fixator UKPS | Zweitstumpf aus Kunststoff |
| 0201 | Basis für Vorbissnahme | Stumpfabdruck galvanisieren |
| 0205 | Vorbereiten Bissgabel UKPS | Abdruck galvanisieren |
| 0211 | Individueller Löffel | Abdruckmanschette |
| 0212 | Funktionslöffel | Dowel-Pin setzen |
| 0213 | Basis für Bissregistrierung | Ausblocken eines Stumpfes |
| 0214 | Basis für Stützstiftregistrierung | Reponieren eines Stumpfes |
| 0215 | Basis für Aufstellung | Zweitstumpfübertragung in Arbeitsmodell |
| 0216 | Basis für Bissregistrierung bei Implantatversorgung | Stumpf vorbereiten |
| 0217 | Individueller Löffel UKPS | Stumpf unter Mikroskop vorbereiten |
| 0218 | Basis für Aufstellung bei Implantatversorgung | Vorbereiten eines Stumpfes zum direkten Aufgalvanisieren |
| 0310 | Provisorische Krone/Brückenglied | Modell ausblocken, digital |
| 1201 | Teleskopierende Primär- oder Sekundärkrone | Übertragungskappe aus Kunststoff |
| 1341 | Konfektions-Geschiebe | Walkhoffsche Tastkugel an Bissschablone |
| 1360 | Gefrästes Lager | Schubverteilungsarm |
| 1370 | Schubverteilungsarm | Gefrästes Lager |
| 2021 | Einarmige gegossene Haltevorrichtung | Galvano-Wurzelkappe |
| 2031 | Zweiarmige gegossene Haltevorrichtung | Individuellen Implantataufbau herstellen |
| 4010 | Aufbissbehelf mit adjustierter Oberfläche | Silberzinnbasis |
| 7110 | Abschirmelement | Haltesporn |
| 7121 | Weichkunststoff (KFO) | Dorn |
| 7122 | Sonderkunststoff (KFO) | Auflage |
| 7410 | Verbindungselemente/intermaxillär | Außenbogen |
| 8024 | LE Basisteil Kunststoff | LE Erneuerung Zahn |
| 8030 | Retention, gebogen | LE Kunststoffsattel lösen und wiederbefestigen |
| 8040 | Retention, gegossen | LE Basis vergrößern |
| 8208 | Instandsetzung Krone/implantatgestützt | LE Nachbereiten Keramikverblendung |

## Der Sonderfall 1360 / 1370: vertauscht

| | 1360 | 1370 |
|---|---|---|
| BEL | Gefrästes Lager | Schubverteilungsarm |
| BEB | Schubverteilungsarm | Gefrästes Lager |

Beide Leistungen gibt es in beiden Katalogen, unter vertauschten Nummern. Ein
Katalogwechsel ohne Nummernprüfung dreht hier die Leistung um, ohne dass Kurztext oder
Plausibilität auffallen.

## 0023 — die folgenreichste Kollision

BEL 0023 ist „Verwendung von Kunststoff", max. 3× je Modell, und seit der
Änderungsvereinbarung 2023 ausdrücklich nicht für Stümpfe und Sockel
→ [[quelle-aenderungsvereinbarung-bel-ii-2023]], [[bel-gruppe-arbeitsvorbereitung]].

BEB 0023 ist „Modell für Einzelstümpfe" — also genau das, wofür BEL 0023 nicht mehr gilt.

Im Vorlagenreview war „0023 für Stümpfe/CAD-CAM-Stumpfmodelle" in mindestens 18 Vorlagen
angesetzt. Wer aus der BEB-Bedeutung auf die BEL-Position schließt, landet in diesem
Fehler.

## Nummern, die es nur in einem Katalog gibt

Ebenso tückisch, weil sie beim Katalogwechsel verschwinden:

| Nr. | BEL | BEB 97 |
|---|---|---|
| 0105 | existiert nicht | „Stumpf aus Kunststoff" — bei Inlays zusatzabrechenbar |
| 2027 | „Auflage" (Modellguss) | existiert nicht |
| 2028 | „Umgehungsbügel bei Diastema" | existiert nicht |

Die BEB-Entsprechung für eine Auflage ist 3805 „Auflage" (HG3) — nicht 2027 und
nicht 7122, das ist die KFO-Auflage in HG7.

Beide Richtungen sind real aufgetreten: eine Vorlage nutzte „BEL 0105" (existiert nicht),
eine andere „BEB 2027" (existiert nicht, gemeint war die Auflage).

## Prüfregel für den KV

1. Steht die Position in der BEL- oder in der BEB-Tabelle?
2. Stimmt der Leistungstext mit dem Kurztext *dieses* Katalogs überein?
3. Bei Abweichung: Meint der Text die Position aus dem anderen Katalog?

Punkt 2 ist der eigentliche Test — er fängt alle 33 Fälle, weil sich die Texte unterscheiden.
Punkt 1 allein genügt nicht, Punkt 3 liefert die Diagnose.

## Kollisionen innerhalb des BEB

Zusätzlich zu den katalogübergreifenden gibt es 32 doppelt vergebene Kurztexte innerhalb des
BEB 97. Kritisch, wenn Text identisch und Kalkulation verschieden ist:
0917 gegenüber 2848 „Konstruktion CAD-Krone zur Verblendung" — HG0/40 min gegen HG2/45 min.
Weitere: 0909/2840, 3805/4122/4421/7122, 1360/3215. → [[quelle-beb97]]

## Verwandt

- [[quelle-beb97]] · [[beb97-grundlagen]] · [[haeufige-abrechnungsfehler]]
- [[bel-ausschlussregeln]] — was innerhalb des BEL nicht nebeneinander steht
