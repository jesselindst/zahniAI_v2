# Häufige Abrechnungsfehler — Prüfliste vor KV-Ausgabe

Destillat aus der systematischen Prüfung von 228 Abrechnungsvorlagen mit 9 608 Positionszeilen
→ [[quelle-review-vorlagen-2026-08]]. **642 Befunde**, davon 252 mit hoher Schwere.
Die Einzelbefunde stehen in `raw/review-2026-08/findings_register.json`.

## Verteilung

| Kategorie | Befunde | davon hoch |
|---|---:|---:|
| Positionen (falsch/unzulässig/doppelt) | 198 | 95 |
| Festzuschuss falsch oder fehlend | 81 | 52 |
| Mengenlogik | 64 | 15 |
| Konsistenz zwischen Vorlagen | 64 | 14 |
| Basis-/Zusatz-Zuordnung | 59 | 18 |
| Material falsch abgegrenzt | 54 | 17 |
| Fehlende Kernleistungen | 45 | 15 |
| Härtefall/Bonus nicht hinterlegt | 27 | 19 |
| Format/Parsebarkeit | 21 | — |
| Veraltete Regel | 18 | 5 |
| Sonstiges | 11 | 2 |
| **Summe** | **642** | **252** |

### ⚠️ Zwei Zählweisen — nicht vermischen

Die Zahlen dieser Seite und die im `BEFUNDBERICHT.md` messen **Verschiedenes**:

| | zählt | Beispiel Festzuschuss |
|---|---|---|
| `findings_register.json` (Tabelle oben) | **Befunde** — ein Befund kann viele Vorlagen betreffen | **81** Befunde |
| `BEFUNDBERICHT.md` | **betroffene Vorlagen** | **189** Vorlagen |

Beide Zahlen sind richtig. Weitere Paare: Positionen 198 Befunde / 190 Vorlagen · Härtefall 27 / 137
· Material 54 / 114. Wer sie nebeneinanderstellt, muss die Einheit dazusagen — sonst wirkt
dieselbe Fehlerklasse einmal klein und einmal groß.

**Deshalb gibt es hier auch nicht *den* häufigsten Fehler:** nach Befunden führen die
**Positionsfehler** (198), nach betroffenen Vorlagen ebenfalls (190) — dicht gefolgt vom
Festzuschuss (189 Vorlagen, aber nur 81 Befunde). Der Härtefall ist mit 27 Befunden klein und mit
137 Vorlagen der **flächendeckendste strukturelle** Mangel.

## 1. Doppelabrechnung — die größte Fehlerklasse (198 Befunde / 190 Vorlagen)

### Komplettposition **und** Einzelschritte

| angesetzt | zugleich angesetzt | Problem |
|---|---|---|
| 2807 / 2810 / 2815 / 2829 „… vollständig verblendet" | 2612 / 2616 separate Verblendung | Verblendung zweimal |
| 2552–2554, 2844–2846 (vollverblendete CAD/CAM-Einheiten) | separate Verblendung | dito |
| 2613, 2653 | dito | dito |

### BEL **und** BEB für dieselbe Arbeit

BEL 1024 (Krone für vestibuläre Verblendung) + 1620 (Verblendung Keramik) **und** zugleich
BEB 2122 / 2314 / 2612 — dieselbe Leistung aus zwei Katalogen.
Rechtsgrundlage der Kritik: **§ 2 Ziff. 4 der Einl. Best.** (abschließende Liste; alles Übrige ist
mit der Positionsvergütung abgegolten) und die Leistungstexte der Positionen selbst. Zusätzlich
verlangt **§ 3 Ziff. 3**, alle Leistungen in *einer* Rechnung zu führen — getrennte BEL- und
BEB-Rechnungen für dieselbe Arbeit sind damit ebenfalls ausgeschlossen.
→ [[bel-ii-zusatzkosten-material]], [[bel-ii-rechnungsstellung]]

### Leistungsbestandteile getrennt angesetzt

Pin, Sägeschnitt, Stumpf/Frässtumpf, Reponieren und Metallverbindungen sind bei den
Kronenpositionen bereits **Leistungsbestandteil**. → [[bel-ausschlussregeln]]

## 2. Falsche Position trotz passendem Kurztext

| angesetzt | richtig | Grund |
|---|---|---|
| **BEB 2815** „Okklusaler Stop" | **BEB 2915** | 2815 ist „CAD/CAM-Brückenglied, vollständig verblendet". Fehler in **21 Vorlagen** |
| **BEL 0105** | existiert nicht im BEL | Kunststoff-/Frässtumpf ist „ggf."-Bestandteil der Kronenpositionen. *BEB 0105 „Stumpf aus Kunststoff" existiert dagegen und ist bei Inlays zusatzabrechenbar* |
| **BEB 2027** „Auflage" | existiert nicht im BEB (BEL 2027 gibt es) | BEB-Entsprechung ist **3805** „Auflage" (HG3) → [[beb-bel-nummernkollisionen]] |
| **BEB 6411** „Spezialpressverfahren" für LiSi-Pressen | HG6 = Prothesen | falsche Hauptgruppe |
| **BEB 2515** Kunststoff-Onlay für ein Komposit-Onlay | materialgerechte Position | falsches Material im Leistungstext |
| **BEL 0023** für Stümpfe/CAD-CAM-Stumpfmodelle | — | seit 01.01.2023 ausdrücklich ausgeschlossen; ≥ 18 Vorlagen |

## 3. Festzuschuss

| Fehler | richtig |
|---|---|
| Verblend-Zusatzbefunde **1.3 / 2.7 / 4.7** vergessen | je Verblendung im Bereich OK 15–25 / UK 34–44; ca. **80–130 € je Krone** |
| Totalprothese mit Befund **5.x** | **4.2** (zahnloser OK) / **4.4** (zahnloser UK) — Klasse 5 ist die Interimsversorgung |
| Modellguss mit **2.7** | **3.1** je Kiefer (belegt über das `regelversorgung`-Array: 3.1 enthält BEL 2010 Metallbasis, 2.7 nicht — Katalog liegt nicht im Repo, s. [[festzuschuss-befundklassen-referenz]]) |
| Adhäsivbrücke mit **1.4** | **2.1/2.2 + 2.7** — 1.4/1.5 sind Stiftaufbauten |
| Dreigliedrige Implantatbrücke mit **2.1** | **2.3** (je Kiefer, nicht je Lücke) |
| Viergliedrig mit **2.2** | **2.4 / 3.1** |
| Klasse **7** bei einer Erstversorgung | Befund **vor** der Implantation; Klasse 7 nur für Erneuerung/Wiederherstellung |

→ [[festzuschuss-befundklassen-referenz]]

## 4. Falsche Leistungsausschlüsse — zulasten des Patienten

Diese Klasse wiegt schwer, weil dem Patienten ein Zuschuss entgeht, auf den er Anspruch hat:

| Behauptung in der Vorlage | tatsächlich |
|---|---|
| Flexible Klammerprothese (Valplast): „kein Festzuschuss" | **gleichartig**, Zuschuss bleibt |
| Nicht-metallische Stifte (Glasfaser/Zirkon/Carbon), Titanstifte: „Privatleistung ohne FZ" | **gleichartig mit FZ 1.4** |

## 5. Fehlende Kernleistungen

Nicht jeder Fehler ist eine zu viel angesetzte Position — es fehlten auch **tragende Leistungen**:

- In allen drei **Locator**-Vorlagen fehlte das Einarbeiten der **Matrizengehäuse**
- In allen vier **Steg**-Vorlagen fehlte das **Sekundärteil** (nur als Material geführt);
  drei enthielten überhaupt keine Steg-Position
- **BEL 0220 Bisswall ohne Basis 0213** — nach BEL II unzulässig
- Der **gefräste/individuelle** Weg beim Sekundärteil (3301/3221/3321) fehlte, obwohl der
  konfektionierte (3621/3622) geführt war

## 6. Erfundene Rechtsgrundlagen

Alle **13 Teleskopkronen-Vorlagen** zitierten nicht belegbare BEL-Paragraphen und leiteten
daraus Regeln ab — z. B. ein „Mengen-Limit: max. 3 Teleskope", das es nicht gibt.

⚠️ Merkregel: Eine Regel ohne auffindbare Fundstelle ist keine Regel. Lieber als
**VERIFIZIEREN** markieren als plausibel klingend behaupten.

## 7. Material

| Fehler | richtig |
|---|---|
| In der GKV **abgegoltenes** Material als berechenbar geführt (NEM, Zirkon-/LiSi-Blank, Gips) | § 2 Ziff. 4 BEL II ist **abschließend** → [[bel-ii-zusatzkosten-material]] |
| Edelmetall als Pauschalpreis | **Bezeichnung, Gewicht, Tagespreis** — § 10 Abs. 2 Nr. 5 GOZ → [[material-abrechnung-privat]] |
| Vorgefertigte Klammern/Labialbögen als Konfektionsfertigteile | sind **Halbfertigteile** und abgegolten |
| BEL 9700 in einer EM-Arbeit | 9700 gilt **nur für NEM** |

## 8. Mengen- und Bezugsgrößenfehler

- Bezugsgröße verwechselt: „je Kiefer" wie „je Lücke" behandelt (Befunde 2.3/2.4)
- Menge 0 oder fehlende Mengenlogik bei „je Zahneinheit"-Positionen
- **BEL 9330 je Versandgang**: ein Hin- und Rückweg = ein Gang, keine getrennte
  Hin-/Rückberechnung; Leerfahrten zählen nicht; **nur Gewerbelabor**.
  ⚠️ Nur mittelbar belegt (gRS 11.07.2016, Volltext nicht zugänglich); der Leerfahrten-Teil ist
  reine Portalquelle → Herleitung und Vorbehalt in [[bel-gruppe-zuschlaege-versand]].
  **VERIFIZIEREN**
- BEL 002 3 seit 01.01.2023: Bezugsgröße *je aufgefülltem Sekundärteil*, **max. 3× je Modell**

→ [[bel-mengenregeln]]

## 9. Struktur- und Konsistenzfehler

- Dieselbe Nummer in **Basis- und Zusatzleistungen** derselben Vorlage (u. a. 0701 in
  12 Vorlagen)
- Widersprüche zwischen Schwestervorlagen: dieselbe Leistung einmal über BEL, einmal über BEB
- READMEs mit falscher Befundklasse, während die Vorlagen darunter die richtige führen
- Vorlagen, deren aktive Fassung sich nach dem Snapshot geändert hat — vor jeder Aktivierung
  gegenprüfen

## Kurz-Checkliste

1. Jede Position: existiert sie **im angegebenen Katalog** und stimmt der Leistungstext?
   → [[beb-bel-nummernkollisionen]]
2. Keine Komplettposition **neben** ihren Einzelschritten, kein BEL **neben** BEB für dieselbe
   Arbeit
3. Befund + Bezugsgröße + Verblendzuschüsse vollständig? → [[festzuschuss-befundklassen-referenz]]
4. Versorgungsform bestimmt, und passen die Positionen dazu?
   → [[festzuschuss-versorgungsformen]]
5. Härtefall/Bonus hinterlegt, sodass der Eigenanteil rechenbar ist?
   → [[festzuschuss-haertefall-bonus]]
6. Material: GKV nur die abschließende Liste; privat Legierung mit Gewicht und Tagespreis
7. Jede zitierte Regel: gibt es dafür eine Fundstelle?
