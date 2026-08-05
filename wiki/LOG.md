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
