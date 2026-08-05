# Customizing / Vorlagen — Lab-Beispiele

Echte Abrechnungsbeispiele einzelner Labore (Stil + Preisniveau), kein Decision-Tree wie
`vorlagen/`. Pro Labor ein Unterordner (z. B. `Henjes/`). Bei KV-Generierung für ein Labor
gewinnt ein passendes Beispiel hier gegenüber der generischen ZahniAI-Vorlage (§15 CLAUDE.md).

Dateinamen folgen dem Fallbeispiel-Schema aus der Naming-Strategie:
`Versorgung_Material_Verfahren_Verblendung_Position_Besonderheit.md`.

Jede Datei transkribiert ein reales Auftrags-/KV-Dokument 1:1 (Positionen, Mengen, Preise) plus
kurzen Kontext (Zahnschema, Implantatsystem, Kasse) — keine Klassifizierungslogik, die steht in
`vorlagen/`.
