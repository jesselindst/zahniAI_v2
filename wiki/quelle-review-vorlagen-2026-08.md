# Quelle: Systematische Prüfung der Abrechnungsvorlagen (Juli/August 2026)

Kein externes Dokument, sondern eine eigene Auswertung: vollständige fachliche Prüfung aller
228 ZahniAI-Abrechnungsvorlagen gegen BEL II, BEB 97, Festzuschuss- und Zahnersatz-Richtlinie,
begleitet von einer Primärquellen-Recherche.

| | |
|---|---|
| Zeitraum | 20.07. – 04.08.2026 |
| Gegenstand | 228 Vorlagen in 22 Gruppen + 5 Querschnittsanalysen; 9 608 Positionszeilen |
| Ergebnis | 642 Befunde, davon 252 mit hoher Schwere (betreffen 223 der 228 Vorlagen) |
| Belegquote | 536 von 642 mit Katalog- oder Bestimmungszitat (`beleg_typ = quelle`); 56 `praxis`, 50 `einschaetzung` |
| Offene Punkte | 110 Befunde mit `verifizieren`-Flag — eigene Dimension, keine Teilmenge der Belegquote: 86 davon sind zugleich quellenbelegt (belegt, aber noch zu bestätigen). Deshalb ergeben 536 + 110 mehr als 642. |
| Raw | `raw/review-2026-08/` — 7 Rechercheberichte, `findings_register.json`, `BEFUNDBERICHT.md` |

## Belegtypen

Im Register durchgängig getrennt gehalten (Feld `beleg_typ`):

| Marker | Bedeutung |
|---|---|
| [Q] | offizielle Quelle oder Katalogfeld — Zitat vorhanden |
| [P] | gängige Laborpraxis — plausibel, aber nicht normativ belegt |
| [E] | eigene Einschätzung — Schlussfolgerung, kein Beleg |
| VERIFIZIEREN | offen; bewusst nicht geraten (eigenes Feld `verifizieren`) |

In den abgeleiteten Wiki-Seiten sind diese Marker nur punktuell gesetzt — konsequent in
[[material-abrechnung-privat]] und [[cadcam-digitale-verfahren]], vereinzelt in
[[quelle-beb97]], [[haeufige-abrechnungsfehler]], [[festzuschuss-versorgungsformen]] und
[[festzuschuss-befundklassen-referenz]], gar nicht in [[festzuschuss-grundlagen]],
[[festzuschuss-haertefall-bonus]], [[beb97-grundlagen]] und [[beb-bel-nummernkollisionen]].

Ein fehlender Marker bedeutet daher nicht „quellenbelegt". Wer eine Aussage aus diesen Seiten
als Rechtsgrundlage in einen KV schreibt, muss sie am Register oder an der Primärquelle
gegenprüfen. Beim Ausbau der Seiten sind die Marker nachzuziehen.

## Kategorien des Registers

Die Befunde tragen im Register ein Feld `kategorie`. Die Bezeichnungen sind für das
Nachschlagen maßgeblich, weil sie breiter sind, als ihr jeweils typischer Fall vermuten lässt:

| `kategorie` | Befunde | umfasst |
|---|---:|---|
| `positionen` | 198 | falsche, unzulässige und doppelt angesetzte Positionen |
| `festzuschuss` | 81 | falscher oder fehlender Befund |
| `mengenlogik` | 64 | Menge und Bezugsgröße |
| `konsistenz` | 64 | Widersprüche zwischen Vorlagen |
| `basis_zusatz` | 59 | Zuordnung Basis-/Zusatzleistung |
| `material` | 54 | Materialabgrenzung |
| `fehlend` | 45 | fehlende Kernleistungen |
| `haertefall_bonus` | 27 | Prozentmechanik nicht hinterlegt |
| `format` | 21 | Parsebarkeit |
| `veraltet` | 18 | überholte Regel |
| `sonstiges` | 11 | — |

Auswertung dieser Kategorien: [[haeufige-abrechnungsfehler]].

## Die sieben Rechercheberichte

| Datei | Inhalt | Abruf |
|---|---|---|
| `festzuschuss.md` | FZ-RL/ZE-RL, § 55 SGB V, Härtefall, gleich-/andersartig, Adhäsivbrücke, Verblendgrenzen, Suprakonstruktionen | 20.07.2026 |
| `bel2_stand.md` | Gültige BEL-II-Fassung, Änderungsvereinbarung 2023, Rundschreiben, 9700, UKPS | 20.07.2026 |
| `beb_stand.md` | BEB 97 gegenüber BEB Zahntechnik 2023, Rechtscharakter, Digitalpositionen | 21.07.2026 |
| `materialabrechnung.md` | § 2 Ziff. 4 BEL II, § 9/§ 10 GOZ, Nachweispflichten, abgegoltene Materialien | 20.07.2026 |
| `cadcam_einstufung.md` | Einstufung gefräster/gedruckter Arbeiten, Schienenfertigung | 20.07.2026 |
| `neue_verfahren.md` | 3D-Druck, Monolithik, neue Materialien und ihre Abrechnungslage | 20.07.2026 |
| `verifikation_kernaussagen.md` | Gegenprüfung der Kernaussagen | 21.07.2026 |

Jede Aussage dort trägt Quelle (URL), Abrufdatum und Quellentyp
(offiziell / fachliteratur / portal). Nicht Belegbares ist als UNBELEGT markiert.

## Quellenhierarchie der Recherche

```
offiziell (KZBV · GKV-SV · G-BA · VDZI · KZVen · Gesetzestext)
   > Fachliteratur (Fachverlage, Kommentare)
      > Abrechnungsportale
```

Portale wurden nur ergänzend verwendet und sind als solche gekennzeichnet. Eine Aussage, die
*nur* auf Portalebene belegt war, ist nicht als gesichert übernommen worden.

## Was daraus ins Wiki eingeflossen ist

Nicht die 642 Einzelbefunde — die bleiben im `findings_register.json`. Ins Wiki gewandert ist
das verallgemeinerbare Regelwissen dahinter:

- [[festzuschuss-grundlagen]] · [[festzuschuss-versorgungsformen]] ·
  [[festzuschuss-haertefall-bonus]] · [[festzuschuss-befundklassen-referenz]]
- [[beb97-grundlagen]] · [[beb-bel-nummernkollisionen]] · [[material-abrechnung-privat]]
- [[cadcam-digitale-verfahren]] · [[haeufige-abrechnungsfehler]]

## Grenzen dieser Quelle

- Sie ist abgeleitet, nicht amtlich. Wo eine Aussage aus dieser Auswertung stammt und nicht
  aus einer Primärquelle, steht das an der Aussage.
- Der Prüfstand ist der 04.08.2026. Kataloge und Richtlinien ändern sich; die Betragstabellen
  jährlich.
- 110 Punkte sind ausdrücklich offen (VERIFIZIEREN), nicht entschieden. Sie sind im Register
  einzeln aufgeführt und in den Wiki-Seiten dort vermerkt, wo sie eine Regel betreffen.
