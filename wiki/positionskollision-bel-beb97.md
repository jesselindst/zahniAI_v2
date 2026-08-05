---
titel: Positionskollision BEL und BEB 97
aliase: [Nummernkollision, gleiche Nummer andere Leistung, Katalogverwechslung]
labels: [Abrechnung, BEL, BEB97]
quellen: [kataloge/bel_2026_v1.json, kataloge/beb97_zahniAI_2026_v1.json]
stand: 2026-08-05
---

135 der 175 BEL-Nummern kommen auch im BEB 97 vor. Bei 33 davon bezeichnet dieselbe Nummer eine völlig andere Leistung. Zwei Nummern sind gegeneinander vertauscht. Ermittelt durch Abgleich der beiden Katalogdateien im Repository.

Eine Prüfung, die nur fragt, ob eine Nummer existiert, erkennt davon nichts: Die Nummer ist gültig, nur im falschen Katalog. Deshalb trägt jede Positions-ID im Wiki ein Katalogpräfix, siehe [[positionssystematik-bel]].

## Prüfregel

1. Steht die Position in der BEL- oder in der BEB-Tabelle des Kostenvoranschlags?
2. Stimmt der Leistungstext mit dem Kurztext genau dieses Katalogs überein?
3. Weicht er ab: Meint der Text die gleichnamige Position des anderen Katalogs?

Schritt 2 ist der eigentliche Test. Er erfasst alle 33 Fälle, weil sich die Kurztexte unterscheiden. Schritt 1 allein genügt nicht.

## Die 33 Kollisionen

| Nummer | BEL | BEB 97 |
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
| 2031 | Zweiarmige gegossene Haltevorrichtung | Individuellen Implantataufbau für Kronen oder Brückenpfeiler herstellen |
| 4010 | Aufbissbehelf mit adjustierter Oberfläche | Silberzinnbasis |
| 7110 | Abschirmelement | Haltesporn |
| 7121 | Weichkunststoff (KFO) | Dorn |
| 7122 | Sonderkunststoff (KFO) | Auflage |
| 7410 | Verbindungselemente/intermaxillär | Außenbogen |
| 8024 | LE Basisteil Kunststoff | Leistungseinheit, Erneuerung Zahn |
| 8030 | Retention, gebogen | Leistungseinheit, Kunststoffsattel lösen und wiederbefestigen |
| 8040 | Retention, gegossen | Leistungseinheit Basis vergrößern |
| 8208 | Instandsetzung Krone/implantatgestützt | Leistungseinheit, Nachbereiten Keramikverblendung |

## Vertauscht: 1360 und 1370

| Nummer | BEL | BEB 97 |
|---|---|---|
| 1360 | Gefrästes Lager | Schubverteilungsarm |
| 1370 | Schubverteilungsarm | Gefrästes Lager |

Beide Leistungen existieren in beiden Katalogen, jeweils unter der Nummer der anderen. Ein Katalogwechsel ohne Nummernprüfung dreht hier die Leistung um, ohne dass Kurztext oder Plausibilität auffallen.

## 0023 als folgenreichster Fall

002 3 ist im BEL Verwendung von Kunststoff, höchstens dreimal je Modell, und seit 01.01.2023 ausdrücklich nicht für Stümpfe und Sockel. Im BEB 97 trägt 0023 den Kurztext Modell für Einzelstümpfe, also genau den Zweck, für den die BEL-Position nicht mehr gilt. Wer aus der BEB-Bedeutung auf die BEL-Position schließt, landet unmittelbar in diesem Fehler. Siehe [[bel-gruppe-arbeitsvorbereitung]].

## Nummern, die nur ein Katalog kennt

| Nummer | BEL | BEB 97 |
|---|---|---|
| 0105 | existiert nicht | Stumpf aus Kunststoff |
| 2027 | Auflage | existiert nicht |
| 2028 | Umgehungsbügel bei Diastema | existiert nicht |

Beide Richtungen sind in Abrechnungsvorlagen aufgetreten. Die BEB-Entsprechung einer Auflage ist 3805 Auflage in HG3, nicht 2027 und nicht 7122; letzteres ist die kieferorthopädische Auflage in HG7.

Verwandt: [[beb97]] · [[bel-ii]] · [[positionssystematik-bel]]
