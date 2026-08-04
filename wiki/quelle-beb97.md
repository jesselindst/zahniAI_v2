# Quelle: BEB 97 — Bundeseinheitliche Benennungsliste

Das Leistungsverzeichnis für **private** zahntechnische Leistungen. Gegenstück zum
[[quelle-bel-ii-2014]] auf der GKV-Seite.

| | |
|---|---|
| Herausgeber | **VDZI** (Verband Deutscher Zahntechniker-Innungen) |
| Entstehung | 1996 entwickelt, 1997 veröffentlicht |
| Rechtscharakter | **reine Benennungs-/Nomenklaturliste** — keine Preisliste, keine Gebührenordnung |
| Im Repo | `kataloge/beb97_zahniAI.json` — 1103 Positionen; Felder `nr`, `name`, `dauer_min` (Planzeit), `hg` (Hauptgruppe), `type` (`standard` 779 / `individuell` 324) |

## Der entscheidende Unterschied zum BEL II

Es gibt **keine staatliche Gebührenordnung für private zahntechnische Leistungen**. Jedes Labor
kalkuliert und bepreist selbst (freie Preisvereinbarung). Die BEB liefert nur *Nummer und
Benennung* — der Preis entsteht aus **Planzeit × betriebsindividuellem Kostensatz**.

| | BEL II | BEB 97 |
|---|---|---|
| Rechtsnatur | Vertrag nach § 88 Abs. 1 SGB V, verbindlich | privates Verzeichnis, unverbindlich |
| Preise | vereinbart, **Höchstpreise** (§ 88 Abs. 2 SGB V) | keine — Laborkalkulation |
| Katalogfeld | Preis Gewerbe-/Praxislabor | `dauer_min` (Planzeit) + `hg` |

Der BZÄK-GOZ-Kommentar hält fest: BEB und BEL haben für die GOZ-Abrechnung **„keinen bindenden
Rechtscharakter"**, sie können nur als Berechnungsgrundlage genannt werden
(`bzaek.de/goz/goz-kommentar/…/ersatz-von-auslagen-fuer-zahntechnische-leistungen.html`).

⚠️ Daraus folgt: Die verbreitete Formulierung „Mehrkosten werden nach BEB abgerechnet" ist
abrechnungsrechtlich ungenau. Normativ heißt es **GOZ** (§ 9 GOZ, Auslagen); die BEB ist nur die
*übliche Kalkulationsgrundlage* dafür. → [[material-abrechnung-privat]]

## Aufbau: Hauptgruppen

Die Nummernsystematik folgt den Hauptgruppen HG0–HG9. Die erste Ziffer der Positionsnummer
korrespondiert mit der Hauptgruppe:

| HG | Bereich | Nummernkreis (Beispiele) |
|---|---|---|
| HG0 | Arbeitsvorbereitung, Modelle, Hilfsteile | 0001–0999 |
| HG1 | Kunststoff-/Provisorienarbeiten, Verblendungen | 1000–1999 |
| HG2 | Metallbasis, Modellguss, Kronen/Brückenglieder gegossen | 2000–2999 |
| HG3 | Verankerungselemente, Teleskope, Geschiebe, Stege | 3000–3999 |
| HG4 | Tertiärstrukturen, Passungen, Schienen | 4000–4999 |
| HG5 | Oberflächenbearbeitung, Konditionieren | 5000–5999 |
| HG6 | Prothesen: Aufstellung, Fertigstellung, Sonderverfahren | 6000–6999 |
| HG7 | Kieferorthopädie | 7000–7999 |
| **HG8** | **Instandsetzung, Erweiterung, Unterfütterung** (Grund- und Leistungseinheiten) | 8001–8851 |
| **HG9** | **Zuschläge und Auslagen** — 9330 Versand, 9700 Verarbeitungsaufwand NEM, 9850 3D-Modell/Material | 9330–9850 |

Verteilung im Repo-Katalog: HG0 211 · HG1 105 · HG2 267 · HG3 127 · HG4 82 · HG5 37 · HG6 60 ·
HG7 147 · **HG8 64** · **HG9 3** = 1103.

⚠️ Die Hauptgruppe ist **nicht dekorativ**. Eine Position aus der falschen Hauptgruppe ist ein
Abrechnungsfehler, auch wenn der Kurztext passend klingt — z. B. 6411 „Spezialpressverfahren"
liegt in HG6 (Prothesen) und ist für das Pressen einer Lithiumdisilikat-Krone die falsche
Position. → [[haeufige-abrechnungsfehler]]

## Status 2026: BEB 97 vs. „BEB Zahntechnik"

- **BEB 97** ist nach Fachverlagsangaben weiterhin die am häufigsten genutzte Liste, gilt aber
  inhaltlich als veraltet — vor allem bei **digitalen Verfahren**.
  ⚠️ Die Verbreitungsaussage stützt sich auf einen **Spitta-Beitrag von 2016** — zum Prüfstand
  04.08.2026 also **zehn Jahre alt** und drei Jahre älter als die 4. Auflage der BEB Zahntechnik.
  Als Begründung für die Katalogwahl trägt sie nicht mehr. **VERIFIZIEREN**
- Nachfolger: **„BEB Zahntechnik"**, 4. Auflage 2023, mit rund **153 Digitalpositionen**.
- Ein Basiswechsel ist nicht erzwungen: Maßgeblich ist, welches Verzeichnis das Labor seiner
  Kalkulation zugrunde legt. Im Repo ist das die BEB 97 (`kataloge/beb97_zahniAI.json`).

*Quellen (Fachverlag): Spitta, „Abrechnungssystem BEB 97 oder BEB Zahntechnik" (09.06.2016);
Spitta Dentalwelt, „Die BEB Zahntechnik — das Update" (16.04.2025).*
**UNBELEGT:** belastbare Marktanteilszahlen BEB 97 vs. BEB Zahntechnik für 2025/2026.

## Bekannte Katalogschwächen

Aus der systematischen Auswertung des Katalogs → [[quelle-review-vorlagen-2026-08]]:

1. **Mehrfach vergebene Kurztexte** — 32 der 1103 Kurztexte kommen doppelt vor. Kritisch bei
   identischem Text und abweichender Kalkulation: **0917 vs. 2848** „Konstruktion CAD-Krone zur
   Verblendung" (HG0/40 min vs. HG2/45 min). Für einen Agenten nicht unterscheidbar.
   Weitere: 0909/2840, 3805/4122/4421/7122, 1360/3215.
2. **Lücken in der Nummernfolge**, die zu Erfindungen einladen: 2026 „Ney-Stiel" existiert,
   **2027 und 2028 nicht**.
3. **Nummernkollisionen mit dem BEL** → eigene Seite: [[beb-bel-nummernkollisionen]]

## Der BEB-Volltext ist nicht frei zugänglich

Er ist ein VDZI-Lizenzprodukt. Aussagen zur BEB-Binnenlogik in diesem Wiki stützen sich deshalb
auf den im Repo vorhandenen Katalog (`kataloge/beb97_zahniAI.json`, maßgeblich für die
Abrechnung hier) sowie auf Fachliteratur — **nicht** auf einen amtlichen Volltext. Wo das
relevant ist, steht es an der jeweiligen Aussage.

## Wird ausgewertet in

- [[beb97-grundlagen]] · [[beb-bel-nummernkollisionen]] · [[material-abrechnung-privat]]
- [[haeufige-abrechnungsfehler]]
