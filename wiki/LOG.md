# Wiki-Log

Chronologisch, append-only. Ein Eintrag je Ingest, Query oder Lint-Lauf.

## [2026-08-05] ingest | BEL II, Stand 01.01.2022

Erster Ingest in ein leeres Wiki. 18 Wissensseiten neu angelegt, keine bestehenden zu aktualisieren. Sieben Querschnittsseiten (Systematik, Mengen, Ausschlüsse, Rechnungsstellung, Material, Qualitätssicherung, Hauptseite), drei zu Versorgungsformen (Implantat, UKPS, Verblendung), acht zu den Leistungsgruppen.

Die verstreuten Erläuterungen zur Abrechnung wurden zu zwei Querschnittsseiten zusammengezogen: [[nebeneinander-ausschluesse-bel]] für die Abrechnungsverbote, [[mengen-und-bezugsgroessen-bel]] für die Bezugsgrößen. Die Zuordnung der 8er-Positionen zu Nr. 36 a (zahnbegrenzte Einzelzahnlücke) und Nr. 36 b (atrophierter zahnloser Kiefer) wurde aus den Einzelerläuterungen rekonstruiert und ist in [[implantatversorgung-bel]] vollständig aufgeführt.

Kein Widerspruch zum Bestand, da kein Bestand vorhanden war. Zwei Beobachtungen sind als Fallstricke vermerkt: Suffix 5 bedeutet nicht generell UKPS (005 5, 021 5, 202 5, 380 5), und Keramikverblendung ist bei Teleskopkronen und Rückenschutzplatte im Verzeichnistext nicht als Träger genannt.

Anlage 2 wurde als reine Zuordnungstabelle nicht übernommen; Verweis auf die Quelle steht in [[rechnungsstellung-bel]] und [[quelle-bel-ii-2022]]. Offene Verweise auf Zahnersatz-Richtlinie Nr. 36, § 28 Abs. 2 Satz 9 SGB V und die Gemeinsamen Rundschreiben sind in [[quelle-bel-ii-2022]] als Wissenslücken festgehalten.

## [2026-08-05] ingest | Bundesmittelpreise 2026

Preisliste nach § 57 Abs. 2 Satz 1 SGB V, gültig 01.01.–31.12.2026, 117 Positionen. Zwei neue Seiten, neun bestehende um Querverweise ergänzt.

Zahlenwerk und Konzept sind bewusst getrennt: [[bundesmittelpreis]] trägt die Erklärung und ist der einzige Anlaufpunkt, auf den andere Seiten verlinken; [[bundesmittelpreise-2026]] trägt nur die Beträge und wird ausschließlich von der Hub-Seite verlinkt. Bei einer neuen Preisliste entsteht eine weitere Jahrgangsseite plus eine Zeile in der Hub-Seite — keine andere Wiki-Seite muss angefasst werden.

Zwei Muster durch Abgleich mit dem BEL II ermittelt. Erstens: 58 BEL-Positionen haben keinen Bundesmittelpreis, und zwar ausnahmslos alle für UKPS, Aufbissbehelfe und Kieferorthopädie samt der sechs KFO-gebundenen Positionen der Arbeitsvorbereitung. Zweitens: alle 19 Implantatpositionen tragen exakt den Preis ihres Regelpendants. Beides in [[bundesmittelpreis]], die betroffenen Gruppenseiten sind entsprechend ergänzt.

Kein Widerspruch zum Bestand. Der Preis-Abschnitt in [[bel-ii]] war zu unscharf und unterscheidet jetzt die bundeseinheitliche von der regionalen Ebene; der offene Punkt zu Preisen in [[quelle-bel-ii-2022]] ist zur Hälfte geschlossen, die regionalen Vergütungen nach § 88 Abs. 2 SGB V fehlen weiterhin.

## [2026-08-05] lint | ganzes Wiki

Geprüft: 22 Seiten, erster Lint-Lauf nach dem Neuaufbau. Graph: 0 verwaist, 0 Wikilinks ins Leere, 0 Seiten ohne `stand:`.

Behoben: `positionen:` auf 10 Seiten nachgetragen, alle 175 BEL-Positionen kollisionsfrei verteilt. Zuständig ist die Seite des Nummernkreises; Ausnahme sind die Verblendungspositionen 1500–1650, die zu [[verblendung-bel]] gehören, weil dort ihr Leistungsinhalt steht. 40 Kanten aus vorhandener Prosa gesetzt (36 `schliesst_aus`, 1 `enthalten_in`, 4 `ersetzt_durch_bei`), jeweils mit Geltung und Prosaverweis. Quelle `BMP_2026_Leistungen_Regelversorgung.pdf` lag wieder in `_inbox/`, obwohl ingestiert — nach `raw/` verschoben, damit die Frontmatter-Pfade von drei Seiten wieder auflösen. Nummernkreis 9xx in [[positionssystematik-bel]] präzisiert: Anlage 2 kennt ihn nicht als eigene Gruppe. Prosa zu 801 8 in [[bel-gruppe-reparatur-erweiterung]] vervollständigt, es fehlten 802 5 bis 802 7.

Vorgelegt: 006 0/007 0 in [[qualitaetssicherung-sonderanfertigung]] als „ausdrückliche Ausnahme" bezeichnet, obwohl zwei getrennte Positionen die Regel gerade bestätigen. Doppelte Prosa zu 802 4, zur Bisslagefixierung und zu „keine Instandsetzung im Sinne von" auf je zwei bis drei Seiten. Mengenangaben mehrfach ausformuliert, etwa die sechs Modelle je UKPS auf drei Seiten.

Bewusst so belassen: 10 Querschnitts- und Quellseiten nennen Positionen im Text, führen aber kein `positionen:`. Ein Eintrag dort würde den Befund „Position von mehreren Seiten beansprucht" auslösen, der schwerer wiegt. `graph.py` unterscheidet bisher nicht zwischen zuständig und erwähnend.

Offen: Zahnersatz-Richtlinie Nr. 36 trägt das gesamte Implantatfenster und ist nicht ingestiert. Für keine Leistung steht ein abrechenbarer Preis im Wiki, nur der bundeseinheitliche Durchschnitt. BEB und Festzuschüsse fehlen vollständig, obwohl der Agent Kostenvoranschläge erstellen soll. Gemeinsame Rundschreiben seit 01.01.2022 sind verbindlich und unbekannt.

## [2026-08-05] ingest | Recherche Abrechnungsrahmen 2026

8 neue Seiten, 8 bestehende ergänzt, 1 Quellseite. Keine Kanten gesetzt: Die Quelle spricht keine Beziehungen zwischen einzelnen Positionen aus, sondern regelt die Ebene darüber.

Die Quelle ist eine eigene Auswertung, kein externes Regelwerk: sieben Rechercheberichte zu Festzuschuss, BEB 97, Materialabrechnung und digitalen Verfahren, dazu die Prüfung aller 228 Abrechnungsvorlagen mit 9608 Positionszeilen. Sie schließt die Lücke zwischen dem BEL II und einem vollständigen Kostenvoranschlag.

Schnitt entlang der drei Entscheidungen, die vor jedem Kostenvoranschlag zu treffen sind: welcher Befund (festzuschuss, festzuschuss-befundklassen, haertefall-und-bonus), welche Versorgungsform (versorgungsform), welcher Katalog (beb97, positionskollision-bel-beb97, material-privat-goz). Dazu cad-cam-einstufung für die Frage, ob ein Fertigungsweg überhaupt regelversorgungsfähig ist.

Konflikt in bel-gruppe-arbeitsvorbereitung sichtbar gemacht: Die Seite führt nach der Fassung 01.01.2022 den Satz, zu 005 1 bis 005 3 sei bei Kunststoffmodell zusätzlich 002 3 abrechenbar. Die Änderungsvereinbarung Modellherstellung mit Wirkung ab 01.01.2023 hat den Sockel in die Modellpositionen eingerechnet; ein zusätzlicher Ansatz wäre danach Überabrechnung. Beide Aussagen stehen mit Quelle nebeneinander. Die Änderungsvereinbarung liegt als PDF in raw/_inbox und ist nicht ingestiert; erst dieser Ingest kann den Konflikt auflösen.

Aus dem Abgleich der beiden Katalogdateien: 135 der 175 BEL-Nummern kommen auch im BEB 97 vor, 33 davon mit anderer Bedeutung, 1360 und 1370 gegeneinander vertauscht. Das ist die Begründung für das Katalogpräfix an jeder Positions-ID und stand bisher nirgends im Wiki.

Nicht übernommen: die 642 Einzelbefunde (vorlagenspezifisch, bleiben im Register), Festzuschussbeträge in Euro (jährlich neu festgesetzt), Legierungspreise (täglich), BEB-Preise (laborspezifisch).

Die Befundnummern des Festzuschusssystems sind keine Katalogpositionen und deshalb nicht als Positions-IDs geführt. Ein Katalog fz unter kataloge/ würde sie prüfbar machen; er ist nicht angelegt.

## [2026-08-05] ingest | Festzuschuss-Richtlinie, Befundkatalog Fassung 2025

2 neue Seiten, 4 bestehende ergänzt, 1 neuer Katalog. graph.py meldet keine Befunde.

Die Quelle ist zugleich Katalog: `FZ-RL_2024-11-21_iK-2025-01-01.json` liegt jetzt als `kataloge/fz_2025_v1.json`. Präfix `fz` in scripts/graph.py registriert, Nummernformat `\d\.\d{1,2}(\.\d)?` wegen 6.10 und der dreistelligen Untergliederungen 6.4.1, 6.5.1 und 6.8.1. Die 54 Befundnummern sind damit prüfbare Positions-IDs; festzuschuss-befundklassen ist für sie zuständig. Der offene Punkt aus dem vorigen Ingest ist damit erledigt.

Beträge auf einer eigenen Jahrgangsseite festzuschussbetraege-2025, nach dem Muster von bundesmittelpreise-2026: nur von der Konzeptseite verlinkt, mit gueltig_von und gueltig_bis. Auf den Konzeptseiten steht kein Betrag.

Die Fassung ist nicht die aktuelle. Der Gemeinsame Bundesausschuss hat am 05.12.2025 neue Beträge festgesetzt, in Kraft ab 01.01.2026; sie liegen nicht vor. Befund 1.1 ohne Bonus: 229,25 Euro 2025 gegen 239,03 Euro 2026. Auf der Quellseite und der Jahrgangsseite vermerkt.

Das Feld regelversorgung_zahntechnik beantwortet Fragen, die vorher nur mittelbar zu klären waren, und wurde als Konsequenz aufgeschrieben statt als Tabelle kopiert:

- 201 0 Metallbasis steht bei 3.1, 4.1, 4.3 und 4.5, nicht bei 2.7. Bestätigt die Zuordnung des Modellgusses zu Klasse 3.
- 102 3 Flügel für Adhäsivbrücke steht bei 2.1 und 2.2, nicht bei 1.4 oder 1.5.
- 162 0 Verblendung Keramik steht bei 1.3, 2.7, 6.9 und 7.3, nicht bei 4.7. Der Teleskop-Verblendzuschlag kennt nur Kunststoff und Komposit. Deckt sich mit verblendung-bel, wo 162 0 als Träger nur Krone und Brückenglied nennt.
- Befund 1.4 führt keine Laborleistung, nur die Materialangabe Stift. Der konfektionierte Stiftaufbau ist Regelversorgung ohne zahntechnischen Anteil, anders als der gegossene nach 1.5.
- Acht Befunde ohne Laborleistung: 1.4, 6.0 und 8.1 bis 8.6.

Nicht enthalten: Teil A mit den Anwendungsregeln und Teil C mit dem Verfahren. Härtefallwirkung, Verblendbereich, Mischfallregel und Erstattungsweg stützen sich weiter auf quelle-recherche-abrechnungsrahmen-2026.

## [2026-08-05] ingest | Festzuschuss-Richtlinie, Fassung 2026 (Fassungswechsel)

3 neue Seiten, 5 bestehende ergänzt, 1 neuer Katalog. graph.py meldet keine Befunde. Zwei Quellen in einem Lauf, weil die Betragstabelle des GKV-Spitzenverbands denselben Beschluss in kompakter Form wiedergibt und keine eigene Seite trägt.

Nach Abschnitt 11 behandelt: Der Ingest erzeugt eine Änderungsmatrix, keine neuen Wissensseiten für den Befundkatalog. Beide Herkünfte geprüft — Katalog-Diff fz_2025_v1.json gegen fz_2026_v1.json und der Volltext von Teil B. Zusätzlich rückwärts gelesen: jede Aussage der vier Festzuschuss-Seiten gegen die neue Fassung.

Ergebnis: kein Befund neu, keiner entfallen, keine Regelversorgungsliste geändert. 48 Befunde mit neuen Beträgen, Steigerung 3,03 bis 9,39 Prozent, Median 4,78. Eine pauschale Fortschreibung des Vorjahresbetrags wäre also falsch gewesen.

Vier vermeintliche Streichungen aus dem ersten Parserlauf haben sich am Rohtext als Artefakte erwiesen: 1550, 0112, 0010, 8060, 2041, 3020 und 1024 stehen im PDF, nur nicht am Zeilenanfang oder hinter dem Wort abzüglich. Ohne die Gegenprobe wären sechs falsche Befunde in die Matrix gelangt.

Erstmals liegt Teil A vor. Die neun Anwendungsregeln waren bisher nur über den Recherchebericht belegt und stehen jetzt primärquellenbelegt auf festzuschuss, haertefall-und-bonus und versorgungsform. Neu aufgenommen: die Gleichstellung funktionstüchtigen Zahnersatzes mit natürlichen Zähnen (Nr. 1), die Gewährung erst bei abgeschlossener Versorgungsnotwendigkeit samt Therapieschritt-Protokollnotiz (Nr. 2), die Gegenbezahnung (Nr. 3) und die Deckelung auf die entstandenen Kosten auch bei Nicht-Härtefällen.

Fachlicher Fund aus Teil B: Vier Zuschlagsbefunde sind Differenzbeträge — 1.3 und 2.7 als 102 4 abzüglich 102 1, 3.2 als Teleskopversorgung abzüglich 204 1, 4.5 als 303 0 abzüglich 302 0. Das erklärt ihre geringe Höhe und war aus der Fassung 2025 nicht ersichtlich. Im Katalog als Feld abzueglich festgehalten.

Der Katalog 2026 führt zusätzlich die BEMA-Positionen je Befund, die Betragsbestandteile Honorar und Material/Labor nach § 57 Abs. 1 und 2 SGB V und null statt 0,00 bei den sechs Befunden der Klasse 8, die keinen eigenen Betrag tragen. Die zahntechnischen Listen sind aus 2025 übernommen, nachdem der Abgleich für alle 54 Befunde keine Abweichung ergab.

quelle-fz-rl-2025 trägt jetzt ersetzt_durch, quelle-fz-rl-2026 trägt ersetzt. Der Wortlaut der alten Fassung bleibt stehen; für Leistungsdatum 2025 gelten diese Beträge.

Widerspruch in der Quelle: Teil A Nr. 8 verweist auf das BEL II – 2004. Maßgeblich ist seit Langem das BEL II – 2014. Die Fundstelle ist im Richtlinientext nicht nachgeführt; auf der Quellseite vermerkt, nicht stillschweigend korrigiert.

Offen: Die Zahnersatz-Richtlinie liegt weiterhin nicht vor, obwohl Teil A an mehreren Stellen auf sie verweist und sie bestimmt, was für einen Befund Regelversorgung ist. Sie trägt insbesondere Nr. 36 zur Suprakonstruktion und Nr. 20 zum Verblendbereich. In raw/_inbox liegt weiter die Änderungsvereinbarung zum BEL II, die den Konflikt in bel-gruppe-arbeitsvorbereitung auflösen würde.

## [2026-08-05] lint | gesamtes Wiki

Geprüft: alle 36 Seiten nach fünf Themenclustern, jede Aussage gegen `raw/` und die aktive Katalogfassung. Graph: 0 Befunde vor und nach dem Lauf. Matrix FZ-RL 2025→2026 angewendet.

Behoben: 3 falsche Abrechnungsregeln, 6 unpräzise Bezugsgrößen oder Positionsangaben, 4 falsche Katalogaussagen, 5 veraltete Aussagen, 6 fehlende Regelkomplexe aus Teil B der Festzuschuss-Richtlinie, 15 Kanten, 8 Frontmatter-Quellen, 8 Meta-Zeilen in INDEX.md.

Der schwerste Fund ist eine falsche Abrechnungsregel, die auf zwei Seiten stand: „Eine dreigliedrige Brücke löst 2.3 aus." Der Befund richtet sich nach der Zahl der fehlenden Zähne, nicht nach Brückengliedern — eine dreigliedrige Brücke ersetzt einen Zahn und löst 2.1 aus. 2.3 verlangt drei nebeneinander fehlende Zähne und gilt je Kiefer. Der Fehler hätte den Festzuschuss um ein Mehrfaches zu hoch angesetzt.

Zweiter Fund mit unmittelbarer Wirkung: Für lückenangrenzende Zähne eines Befundes der Klasse 2 sind 1.1 bis 1.3 nicht ansetzbar. Dieser Ausschluss und vier weitere Regeln des Klasse-2-Kopftextes — wann eine Freiendsituation vorliegt, Zahn 8 als Anker, Weisheitszahn zählt nicht mit, nicht versorgungsbedürftige Freiendsituationen zählen bei der Zahl der fehlenden Zähne doch mit — fehlten vollständig. Sie entscheiden die Weiche zwischen Brücke und Modellguss und damit zwischen Regelversorgung und andersartig.

Dritter Fund: Die Sperren aus Unterfütterung und Basiserneuerung waren zu weit gefasst. 808 0 und 809 0 sperren sechs Positionen, 810 0 nur 801 0 und 802 1–802 7, 864 0 nur 861 0 bis 863 0. Nach der alten Formulierung wäre 861 0 neben 810 0 gesperrt gewesen und 801 0 neben 864 0. Jetzt als Tabelle je Position, dazu die zwei ausdrücklichen Zusatz-Erlaubnisse zu 802 4 und 851 3, die die Sperre begrenzen.

Klasse 6 und Klasse 8 der Befundklassen-Seite waren zu Sammelzeilen verdichtet, die die Befundwahl nicht mehr tragen. 6.0 bis 6.3 unterscheiden sich nach Abformung und Werkstoffbereich, und 6.0 ist der einzige Befund, der zahntechnische Leistungen ausdrücklich ausschließt — das erklärt sein leeres Regelversorgungs-Verzeichnis. Bei 8.1 bis 8.6 sind die Basisbefunde je Zeile abschließend aufgezählt; „50 Prozent der Befunde 2.1 ff." war zu weit, es sind 2.1 bis 2.5. 1.4 ist bei 8.1 kein Basisbefund.

Der Widerspruch um 002 3 neben 005 1 bis 005 3 ist inhaltlich geklärt, aber nicht eingearbeitet: Die Änderungsvereinbarung in `raw/_inbox/` fasst 005 1 bis 005 3 zum 01.01.2023 mit „einschließlich Gips- oder Kunststoffsockel" neu, ihre Erläuterung zur Abrechnung lautet seither „Keine". Ein zusätzlicher Ansatz von 002 3 wäre Überabrechnung, und die Preise der aktiven Katalogfassung enthalten den Anteil bereits. Einarbeiten ist Ingest, nicht Lint. Behoben wurde die interne Inkonsistenz: Die Tabellenzeilen trugen die aufgehobene Regel ohne Vorbehalt 14 Zeilen unter dem Konfliktabschnitt und sind jetzt als Fassung 2022 markiert. Korrigiert wurde außerdem die Bezugsgröße der 002 3 — sie hat zwei Zweige, und der Deckel „höchstens dreimal je Modell" gilt nur für die Zahnfleischpartien, nicht für die Sekundärteile.

Falsche Katalogaussagen: Auf drei Seiten stand, das BEL binde sechs Positionen der Arbeitsvorbereitung an die Kieferorthopädie. Es sind fünf; 002 1 nennt im Leistungsinhalt Kralle und Kappe, also Zahnersatz. Auf `bel-gruppe-arbeitsvorbereitung` widersprach sich die Seite dabei selbst. Auf `beb97` fehlten HG8 und HG9 ganz, und HG2, HG4 und HG5 waren falsch beschrieben — Metallbasis und Modellguss stehen in HG4, nicht HG2; HG5 sind Lötungen und Vergoldung, nicht Oberflächenbearbeitung. Die als vollverblendet geführten CAD/CAM-Einheiten 2552 bis 2554 und 2844 bis 2846 sind Inlays, und 2829 heißt „für keramische Vollverblendung", trägt sie also gerade nicht.

Die Positionskollision ist nachgerechnet: 135 gemeinsame Nummern bestätigt, aber 35 statt 33 mit anderer Bedeutung. 0021 und 8027 fehlten. 8027 ist die schärfere Falle, weil der BEB-Kurztext genau die Leistung benennt, die im BEL unter 8024 steht. Ergänzt wurde die belastbarere Kennzahl: im `standard`-Bestand liegen nur 34 gemeinsame Nummern, davon 29 mit anderer Bedeutung — die 135 messen überwiegend den Bau der Katalogdatei.

Nicht bestätigt und verworfen: zwei gemeldete Kantenfehler. `bel:7030 → bel:7100` ist korrekt, weil bei `ersetzt_durch_bei` das Ziel die Ersatzposition ist und 701 0 richtig in der Geltung steht; `bel:7500 → bel:3800` und `bel:7510 → bel:3810` stehen bereits als `ersetzt_durch_bei` und nicht als `schliesst_aus`.

Vorgelegt: Die Herkunft von `kataloge/bel_2026_v1.json` ist unbelegt. Die Datei ist im Graph als aktive BEL-Fassung geführt, trägt für alle 175 Positionen `Preis_Gewerbelabor` und `Preis_Praxislabor`, hat aber keine Metadaten — kein Stand, keine Quelle, kein Preisgebiet. Die Preise stimmen mit keiner Quelle in `raw/` überein: gegenüber dem Bundesmittelpreis 2026 liegt Gewerbelabor 0,2 bis 2,1 Prozent höher, Praxislabor durchgängig 5 Prozent unter Gewerbelabor, und 58 Positionen sind bepreist, die der Bundesmittelpreis nicht kennt. Solange das offen ist, kann keine Preisaussage belastbar verankert werden. Behoben wurde nur die Leseart: „kein Bundesmittelpreis" bedeutet nicht „kein Preis", und das steht jetzt dort, wo die Aussage fällt.

Ebenfalls vorgelegt: BEB 1360 und 1370 sind gegeneinander vertauscht. Die BEL-Seite ist über die Bundesmittelpreisliste zweitbelegt. Die Indizien sprechen für einen Importfehler der Katalogdatei — beide Einträge sind `individuell` mit Spitta-Herkunft und liegen in HG1 inmitten gespiegelter BEL-Nummern, während die echte BEB-Position für den Schubverteilungsarm als `standard` unter 3215 in HG3 steht. Ob die Datei zu korrigieren ist, ändert Kennzahlen auf zwei Seiten und ist nicht Lint-Sache. Der Abschnitt ist als Datenfehler umformuliert, nicht mehr als BEB-97-Falle.

Drittens vorgelegt: die Semantik von `type: standard` gegen `individuell` in der BEB-Datei. Sie trägt die Aussagekraft beider BEB-Seiten, ist aber nirgends dokumentiert. Ohne sie ist nicht entscheidbar, welche der 1103 Positionen originäre BEB 97 sind. Auf `beb97` als offener Punkt festgehalten.

Drei Einordnungen auf `versorgungsform` sind als unbelegt markiert statt gelöscht: flexible Klammerprothese und nicht-metallische Stifte finden in keiner Quelle eine Fundstelle, und bei Titanstiften spricht der Wortlaut des Befundes 1.4 — konfektionierter metallischer Stiftaufbau, Materialangabe nur „Stift" ohne Legierungsbeschränkung — gegen die Einstufung als gleichartig. Bei der flexiblen Klammerprothese widersprechen sich Wiki und Vorlagenbestand.

Bewusst belassen: die wertenden Sätze auf den Konzeptseiten („wird häufig übersehen", „die folgenreichste Weiche"). Sie tragen Information für den Abrechnungsagenten; Umschreiben wäre Umbau ohne Sachgewinn. Der nächste Lauf muss sie nicht erneut melden.

Nicht behoben, weil Ingest: die Änderungsvereinbarung zum BEL II. Sie bleibt der einzige unverarbeitete Posten in `raw/_inbox/`.

Offen: Woher kommt `bel_2026_v1.json`, und welcher der beiden Preissätze gilt wofür? Sollen BEB 1360 und 1370 in der Katalogdatei getauscht werden? Was bedeutet `type: individuell`? Die Zahnersatz-Richtlinie fehlt weiterhin und trägt vier Pinpoint-Zitate, deren Sachgehalt aber über BEL II und FZ-RL zweitbelegt ist. Der GOZ-Normtext fehlt vollständig und trägt `material-privat-goz` allein über Sekundärquellen.

## [2026-08-05] lint | Zusammenführung mit dem verworfenen Lint-Zweig

Zweiter Lauf am selben Tag. Zusätzliche Vergleichsgrundlage: der Commit `f6f0bf3` auf `origin/worktree-lint-wiki-2026-08-05`. Er trägt einen Lint-Lauf über 33 Seiten der Dateistruktur, die durch `d4a74bc` beim Neuaufbau ersetzt wurde, und war nie gemergt. Ein Merge ist nicht möglich: die Seitennamen existieren nicht mehr. Verglichen wurde deshalb inhaltlich, Seite gegen Seite.

Graph: 0 Befunde vor und nach dem Lauf. 40 Seiten, eine neu.

Wichtigstes Ergebnis vorab: Der verworfene Zweig war an fünf Stellen inhaltlich schlechter, und die heutige Fassung bleibt dort unangetastet. Er behauptete, eine dreigliedrige Brücke löse Befund 2.3 aus — genau der Fehler, den der erste Lauf heute behoben hat. Ebenso überholt: die Bezugsgröße „je Lücke" bei 2.5, die die Quelle nicht nennt; Titanstifte pauschal als gleichartig; die Aussage, die Festzuschuss-Richtlinie nenne keine zahntechnischen Positionen (Teil B nennt sie für alle 54 Befunde); die Materialliste des § 2 Ziffer 4 ohne Umkehrschluss-Vorbehalt. Wer den Zweig gemergt hätte, hätte drei heute behobene Fehler zurückgeholt.

Geschlossen wurde die größte offene Frage des ersten Laufs: die Herkunft der Katalogpreise. Der Zweig hatte `bel.json` gegen die Bundesmittelpreisliste vermessen; die Kennzahlen sind unabhängig nachgerechnet und bis auf zwei bestätigt. 117 überlappende Positionen, Median-Abweichung +0,21 Prozent, keine einzige exakte Übereinstimmung, 113 innerhalb von 5 Prozent. Korrigiert: `Preis_Praxislabor` ist bei 160 Positionen centgenau 95 Prozent des Gewerbelabor-Preises, mit Rundungstoleranz bei 171 — nicht bei 171 centgenau; und die Ausnahmen mit gleichem Preis sind vier, nicht drei, weil 970 0 dazugehört. Neu gefunden: drei Abweichungsgruppen bilden einen Fingerabdruck — zehn Positionen des festsitzenden Zahnersatzes bei +2,07 Prozent, drei der Aufstellung bei −4,85 und −4,36 Prozent, und vier Grundeinheiten bei −12,52 und −13,94 Prozent. 801 0, 801 8, 301 0 und 301 8 rechnen im Katalog zulasten des Labors, und alle vier haben hohe Ansatzhäufigkeit.

Nicht übernommen wurde die Rechtsnorm, mit der der Zweig das begründete. § 57 Abs. 2 SGB V ist im Repository widersprüchlich belegt: die Rechercheberichte nennen für dieselbe Regel Satz 3, Satz 7 und § 88 Abs. 3. Die Messung steht deshalb als Messung auf der Seite, nicht als Konformitätsurteil, und die Satznummer fehlt bewusst. Ein früherer Zwischenbericht dieses Laufs hatte Satz 3 genannt; das war eine ungeprüfte Übernahme und ist zurückgenommen.

Ein Fehler, den der erste Lauf heute ungeprüft aus dem alten Bestand übernommen hatte, ist behoben: Die BEB-Entsprechung einer gegossenen Auflage ist nicht 3805, sondern 4122 oder 4421. 3805 ist `individuell` mit Spitta-Herkunft in HG3 und trägt denselben Text wie BEL 380 5, gehört also zum gespiegelten BEL-Bestand der Datei; die originären Positionen stehen als `standard` in HG4 zwischen Ringklammer und Stiel. Dasselbe Muster bei der Doppelbogenklammer.

Damit ist auch die Semantik von `type` belegt statt vermutet. Das Feld `quellen` liegt ausschließlich auf den 324 `individuell`-Positionen, auf keiner einzigen `standard`-Position; von den 135 BEL-gemeinsamen Nummern sind 101 `individuell` und meist textgleich mit dem BEL; und drei Fälle sind einzeln nachweisbar. `individuell` markiert eingespiegelte Fremdpositionen, `standard` den originären Bestand.

Die Positionskollisionen sind erneut nachgerechnet: 37 statt 35. 8023 und 8026 fehlten in beiden Fassungen — BEL „LE Einarbeiten Zahn" gegen BEB „Wiederbefestigung Zahn", BEL „LE Rückenschutzplatte einarbeiten" gegen BEB „Regulierungselemente einarbeiten". 8021, 8022 und 8025 sind dagegen nur Formulierungsvarianten und bleiben draußen.

Ein interner Widerspruch aus dem ersten Lauf ist geschlossen: `bel-gruppe-reparatur-erweiterung` zog die Instandsetzungskreise weiter zusammen, obwohl die Ausschlussseite sie am Morgen differenziert bekam. Beide Seiten tragen die Tabelle jetzt gleich. Ebenso behoben: `festzuschuss-befundklassen` behauptete Titanstifte als gleichartig, während `versorgungsform` sie als offen führte.

Neu belegt aus der Festzuschuss-Richtlinie: 2.7 ist für Flügel einer Adhäsivbrücke ausdrücklich nicht ansetzbar — bei einer verblendeten Adhäsivbrücke entsteht der Zuschlag je ersetztem Schneidezahn, nicht je Flügel. Die Adhäsivbrücke ist nur bei 2.1 und 2.2 Regelversorgung. Die Altersgrenze 21 steht als Protokollnotiz zu 2.2 in der Richtlinie selbst und braucht die Zahnersatz-Richtlinie nicht mehr; die Untergrenze 14 dagegen bleibt unbelegt. Dazu die Protokollnotizen zur Klasse 2 und zu 4.6, und der Hinweis, dass 4.5 bei Befund 3.1 nicht ansetzbar ist, weil die Metallbasis dort schon Regelversorgung ist.

Neu angelegt: `quelle-zahnersatz-richtlinie` als Fremdquellenseite ohne Volltext. Zehn Seiten nahmen ZE-RL-Nummern in Anspruch, ohne dass irgendwo Fassung, Fundstelle oder Belegstatus stand. Die Seite trennt, was aus dem Repository heraus belastbar ist — Nummern 25, 30, 36 a/b und 38 — von dem, was nicht belegt ist, darunter die Definitionen gleichartig und andersartig in Nummer 5, auf denen `versorgungsform` beruht.

Die Rangfolge der Quellengattungen steht jetzt auf `quelle-bel-ii-2022`: Änderungsvereinbarung über Gemeinsames Rundschreiben über Fassung, weil Vereinbarungen den Vertragstext selbst neu fassen. Dazu eine Tabelle aller acht bekannten Fortschreibungen seit 2014 mit Regelungsinhalt. Dass nichts Neueres gelistet ist, bleibt ein Negativbeleg aus einem Webseitenabruf und ist bei jedem Jahreswechsel zu wiederholen.

Der durchgerechnete Härtefall steht jetzt auf der Jahrgangsseite 2026, nicht auf `haertefall-und-bonus` — die Konvention, dass Beträge nur auf Jahrgangsseiten stehen, gilt auch für Beispiele. Vier Stufen einer dreigliedrigen Brücke mit einmal 2.1 und dreimal 2.7, alle Werte gegen den Katalog nachgerechnet. Die gleitende Härtefallregelung nach § 55 Abs. 3 SGB V bleibt offen und ist als solche benannt; im ganzen Repository liegt dazu kein Grenzwert und keine Formel.

Ebenfalls zurückgeholt: die Definition des Versandgangs. Hin- und Rückweg derselben Beförderung sind ein Gang, Leerfahrten zählen nicht. Die Regel steht nicht im Verzeichnis, sondern im Gemeinsamen Rundschreiben vom 11.07.2016, und ist nur sekundär belegt.

Nicht zurückgeholt und begründet verworfen: die Seite `haeufige-abrechnungsfehler` in ihrer alten Form. Von ihren rund 30 Einzelfehlern sind etwa 20 heute abgedeckt, meist genauer; drei ihrer Positionslisten sind katalogwidrig, darunter Inlays als vollverblendete CAD/CAM-Einheiten und 2829, das gerade eine Krone für die Verblendung ist. Eine Prüfliste, die nur verweist statt zu wiederholen, wäre der sinnvolle Nachfolger und ist als offener Punkt vermerkt. Ebenso nicht zurückgeholt: `quelle-beb97`, weil die BEB 97 kein Dokument im Repository ist und die Seite das Feld `quellen` mit keinem Wort erwähnte — die heutige `beb97` ist an diesem Punkt weiter. Und die Log-Historie des Zweigs: 447 Zeilen mit sechs Einträgen vom 03. bis 05.08., die Seitennamen nennen, die es nicht mehr gibt. Historie steckt in git, hier im Commit `f6f0bf3`.

Offen: Welchem Preisgebiet und Stichtag `bel_2026_v1.json` zuzuordnen ist, bleibt ungeklärt — dafür fehlt eine regionale Preisliste als Gegenprobe. Der Normtext des § 57 SGB V würde die Messung zum Rechtsbefund machen. BEB 1360 und 1370 bleiben vertauscht; ein Tausch ändert Kennzahlen auf zwei Seiten. Die Änderungsvereinbarung zum BEL II in `raw/_inbox/` ist weiterhin der einzige unverarbeitete Posten, und ihr Ingest würde die Bezugsgröße der 002 3 und den Weg des Bundesmittelpreises in die Betragsfestsetzung primärquellenfest machen. Eine Prüfliste für den Kostenvoranschlag fehlt als Gattung.
