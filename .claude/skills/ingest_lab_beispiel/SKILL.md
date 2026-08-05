---
name: ingest_lab_beispiel
description: Neues Abrechnungsbeispiel oder Abrechnungskatalog eines Labors einpflegen.Nutze wenn ein Labor eine neue Rechnung/KV-Beispiel schickt oder einen eigenen Katalog/eigene Positionen hochlädt.
---

## A) Neues Abrechnungsbeispiel (Auftrag + Kostenvoranschlag eines Labors)
1. Dokument transkribieren nach folgendem Muster: 
        '''
        # Kurze Beschreibung der Arbeit

        Auftraggeber: Dr. Carsten Rosenboom. Auftragsdatum 22.01.2026, Belegnummer 67736.

        ## Kontext

        | | |
        |---|---|
        | Patient |  |
        | Kasse |  |
        | Zahn | 36 |
        | Befund | SKM (implantatgetragene Suprakonstruktion), Krone, Brückenglied vorhanden an 26 |
        | Art der Arbeit | Zirkonkrone auf Implantat, vollverblendet |
        | Auftragstext | „Bitte um KV 36 SKM Zirkon Vollverblend. Nobel Biocare" |
        ... (je nach Auftrag weitere Kontextinformationen, z.B. Implantatsystem, etc.)

        ## Positionen

        | Nr. | Bezeichnung | Menge | Einzelpreis | Material | Leistung |
        |---|---|---:|---:|---:|---:|
        | 0002 | Modell aus Superhartgips | 2,00 | 9,68 | | 19,36 |
        ...

        ## Hinweise
        falls angebracht
        '''
2. Ablegen unter `customizing/vorlagen/<Labor>/`, Dateiname nach dem Fallbeispiel-Naming-Schema.
3. Nur die Positionen, die im Dokument tatsächlich vorkommen, gegen die ZahniAI-Kataloge prüfen (`kataloge/beb97_zahniAI.json`). Matched sie 1:1 (Nummer + Bezeichnung passt) → nichts weiter zu tun.
4. Matched sie nicht (fremde Nummer, anderer Name, anderer Preiszuschnitt) → in die Matrix unten. Nur Privatleistungen vergleichen, BEL Positionen sind gesetzlichvorgeschrieben, die schriebn wir nicht in id Matrix.

## B) Neuer eigener Katalog eines Labors

1. Katalog vollständig einlesen, ablegen unter `customizing/kataloge/<Labor>/`.
2. Jese Position im Katalog gegen `kataloge/beb97_zahniAI.json` prüfen.
3. Matched sie nicht → in die Matrix unten. Nur Privatleistungen vergleichen, BEL Positionen sind gesetzlich vorgeschrieben, die schreiben wir nicht in die Matrix.

## Matrix (für beide Fälle gleich)

Labore haben manchmal eigene Positionen. Wenn sie eigenen Katalog hochladen, dann erstelle eine Vergleichsmatrix zu den ZahniAI Positionen. Denn wir nutzen ja unsere Abrechnungsvorlagen, die eben nur die ZahniAi Positionn führen. Um weiterehin auf die Vorlagen zurückgreifen zu können, aber mit den individuellen Positionen abrechnen zu können, brauchen wir die Matrix. Gehe Positioon für Position durch. Ist sie: 
    1. ergänzend 
    oder
    2. ersetzend 
    oder
    3. nur anders benannt
Ergänzende Positionen musst du in der generieurng des KVs sematisch berücksichtigen. Passt sie zur Leistung? 
Ersetzende kannst du einfach am Ende vor ausgbae des finalen KVs austauschen. Zu beachten ist, dass ersetzen auch 1:n sein kann. Sprich manche labore fassen der einfachheit halber einfach mehrere Positionen zu einer zusammen. Das erkennst du entweder am Preis, oder am Namen. Hier gilt aber auch: wenn neue Position hinzugekommen ist in einer neu hochgeladenen Voralge oder Katalog und du kannst sie nicht interpretieren -> nachfragen und als Bemerkung hinter die Position in die Matrix schreiben. 
Umbenannte ebenso einfach austauschen. 

`positionsmatrix.md` je Labor: eine Tabelle, Spalten Fremd-Position | ZahniAI-Position | Klassifikation (ergänzend/ersetzend/umbenannt) | Bemerkung.
