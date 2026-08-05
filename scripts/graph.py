#!/usr/bin/env python3
"""Erzeugt wiki/GRAPH.md aus den Wiki-Seiten.

Rein ableitend: liest wiki/*.md, schreibt genau eine Datei.
Aendert niemals eine Wissensseite. Wird von den Skills ingest, lint und
query zu Beginn ihres Laufs aufgerufen.
"""

import os
import re
import sys
import json
import glob
import datetime
from collections import defaultdict

WIKI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "wiki")
WIKI = os.path.normpath(WIKI)
KATALOGE_DIR = os.path.normpath(os.path.join(WIKI, "..", "kataloge"))
OUT = os.path.join(WIKI, "GRAPH.md")
SKIP = {"INDEX.md", "LOG.md", "GRAPH.md"}

# Kanten innerhalb eines Katalogs. 'entspricht' steht bewusst nicht dabei:
# es verbindet Kataloge und wird getrennt geprueft.
KANTEN = ["schliesst_aus", "enthalten_in", "alternativ_zu", "ersetzt_durch_bei"]
KANTEN_ALLE = KANTEN + ["entspricht"]

# Positions-ID: katalog:nummer, z. B. bel:0021. Ohne Praefix ist eine Nummer
# mehrdeutig — 135 der 175 BEL-Nummern kommen im BEB97 mit anderer Bedeutung vor.
# Praefix = erstes Segment des Dateinamens unter kataloge/. Nummernformat je
# Katalog, damit ein Tippfehler auffaellt statt durchzurutschen. Neuen Katalog
# hier eintragen, bevor er ingestiert wird.
KATALOGE = {
    "bel": r"\d{4}",
    "beb97": r"\d{4}",
    "bebzt": r"[\d.]{4,8}",   # Format ungeprueft, bei erstem Ingest verifizieren
    "goz": r"\d{4}",
    "bema": r"[A-Za-z0-9]{1,5}",
}
POS = re.compile(r"^(%s)$" % "|".join(
    f"{k}:{v}" for k, v in KATALOGE.items()))


# ---------------------------------------------------------------- Frontmatter

def parse_frontmatter(text):
    """Minimaler YAML-Parser fuer das hier verwendete Schema.

    Unterstuetzt: 'key: wert', 'key: [a, b]' und Blocklisten mit '  - eintrag'.
    Bewusst kein PyYAML, damit das Skript ohne Installation laeuft.
    """
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    block = text[3:end]
    rest = text[end + 4:]

    data, key = {}, None
    for line in block.split("\n"):
        if not line.strip() or line.strip().startswith("#"):
            continue
        item = re.match(r"\s+-\s+(.*)$", line)
        if item and key:
            data.setdefault(key, [])
            if isinstance(data[key], list):
                data[key].append(item.group(1).strip().strip("\"'"))
            continue
        kv = re.match(r"([A-Za-z_]+):\s*(.*)$", line)
        if not kv:
            continue
        key, val = kv.group(1), kv.group(2).strip()
        if val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            data[key] = [v.strip().strip("\"'") for v in inner.split(",") if v.strip()]
        elif val == "":
            data[key] = []
        else:
            data[key] = val.strip("\"'")
    return data, rest


def dateiname_teile(stem):
    """Praefix und Fassung aus einem Katalogdateinamen.

    Schema: <praefix>[_<label>]_<jahr>[_v<n>], das Label ist frei.
    Die Fassung sortiert die Dateien eines Praefix; die hoechste ist die
    aktive, die naechstniedrigere ist die Diff-Grundlage der Aenderungsmatrix.

        bel_2026                -> ('bel', (2026, 1))
        beb97_zahniAI_2026      -> ('beb97', (2026, 1))
        beb97_zahniAI_2026_v2   -> ('beb97', (2026, 2))
        bel                     -> ('bel', (0, 0))   ohne Fassung

    (0, 0) sortiert unter jede echte Fassung. Eine Datei ohne Fassung ist
    zulaessig, solange sie die einzige ihres Praefix ist — sonst waere die
    Reihenfolge geraten. Der Fall wird als Befund gemeldet.
    """
    teile = stem.split("_")
    praefix = teile[0].lower()
    jahr, v = 0, 0

    rest = teile[1:]
    if rest and re.fullmatch(r"[vV]\d+", rest[-1]) and len(rest) >= 2 \
            and re.fullmatch(r"\d{4}", rest[-2]):
        jahr, v = int(rest[-2]), int(rest[-1][1:])
    elif rest and re.fullmatch(r"\d{4}", rest[-1]):
        jahr, v = int(rest[-1]), 1

    return praefix, (jahr, v)


def load_kataloge():
    """Positionsnummern je Katalog und Fassung aus kataloge/*.json.

    Kataloge liegen versioniert nebeneinander. Eine neue Fassung kommt als
    weitere Datei dazu, die alte bleibt liegen — sie ist die Grundlage des
    Katalog-Diffs beim naechsten Fassungswechsel und der Beleg dafuer, welche
    Fassung eine entfallene Position zuletzt kannte.

    Rueckgabe:
        aktiv     praefix -> Nummernmenge der hoechsten Fassung
        fassungen praefix -> Liste aller Fassungen, absteigend, je Eintrag
                            {'datei', 'fassung', 'nummern'}
    """
    aktiv, fassungen = {}, defaultdict(list)
    if not os.path.isdir(KATALOGE_DIR):
        return aktiv, fassungen

    for pfad in sorted(glob.glob(os.path.join(KATALOGE_DIR, "*.json"))):
        datei = os.path.basename(pfad)
        praefix, fassung = dateiname_teile(datei[:-5])
        nummern = set()

        def walk(o):
            if isinstance(o, dict):
                for k, v in o.items():
                    if k.lower() in ("l_nr", "nr", "nummer", "position") \
                            and isinstance(v, str):
                        nummern.add(v.strip())
                    else:
                        walk(v)
            elif isinstance(o, list):
                for v in o:
                    walk(v)

        try:
            with open(pfad, encoding="utf-8") as fh:
                walk(json.load(fh))
        except Exception:
            continue
        if nummern:
            fassungen[praefix].append(
                {"datei": datei, "fassung": fassung, "nummern": nummern})

    for praefix, liste in fassungen.items():
        liste.sort(key=lambda e: e["fassung"], reverse=True)
        aktiv[praefix] = liste[0]["nummern"]

    return aktiv, fassungen


def fassung_str(f):
    jahr, v = f
    if jahr == 0:
        return "ohne Fassung"
    return f"{jahr}" if v <= 1 else f"{jahr} v{v}"


def zuletzt_in(fassungen, kat, nr):
    """Juengste Fassung unterhalb der aktiven, die 'nr' noch kennt."""
    for e in fassungen.get(kat, [])[1:]:
        if nr in e["nummern"]:
            return e["datei"]
    return None


def as_list(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


# ---------------------------------------------------------------- Einlesen

def load():
    seiten = {}
    for fn in sorted(os.listdir(WIKI)):
        if not fn.endswith(".md") or fn in SKIP:
            continue
        with open(os.path.join(WIKI, fn), encoding="utf-8") as fh:
            raw = fh.read()
        fm, body = parse_frontmatter(raw)
        seiten[fn[:-3]] = {
            "fm": fm,
            "body": body,
            "links": [m.split("#")[0].strip()
                      for m in re.findall(r"\[\[([^\]|]+)", body)],
        }
    return seiten


def kante_teile(s):
    """'2010 | 8060 | immer | nebeneinander-ausschluesse-bel' -> 4 Felder."""
    t = [x.strip() for x in s.split("|")]
    while len(t) < 4:
        t.append("")
    return t[:4]


# ---------------------------------------------------------------- Auswertung

def build(seiten):
    backlinks = defaultdict(set)
    kaputt = defaultdict(set)
    for name, s in seiten.items():
        for ziel in s["links"]:
            if ziel in seiten:
                backlinks[ziel].add(name)
            else:
                kaputt[name].add(ziel)

    pos2seite = defaultdict(set)
    for name, s in seiten.items():
        for p in as_list(s["fm"].get("positionen")):
            if POS.match(p):
                pos2seite[p].add(name)

    quelle2seite = defaultdict(set)
    for name, s in seiten.items():
        for q in as_list(s["fm"].get("quellen")):
            quelle2seite[q].add(name)

    kanten = defaultdict(list)
    for name, s in seiten.items():
        for typ in KANTEN_ALLE:
            for eintrag in as_list(s["fm"].get(typ)):
                a, b, geltung, prosa = kante_teile(eintrag)
                kanten[typ].append((a, b, geltung, prosa, name))

    label2seite = defaultdict(set)
    for name, s in seiten.items():
        for l in as_list(s["fm"].get("labels")):
            label2seite[l].add(name)

    # "hat im Zielkatalog kein Aequivalent" — eine positive Aussage, damit eine
    # Umschreibung die Luecke sieht, statt die Position stillschweigend zu
    # verlieren. Format: "beb97:0001 | bebzt | Begruendung"
    fehlt = []
    for name, s in seiten.items():
        for e in as_list(s["fm"].get("kein_aequivalent")):
            teil = [x.strip() for x in e.split("|")]
            while len(teil) < 3:
                teil.append("")
            fehlt.append((teil[0], teil[1], teil[2], name))

    return backlinks, kaputt, pos2seite, quelle2seite, kanten, label2seite, fehlt


def befunde(seiten, backlinks, kaputt, pos2seite, kanten, kataloge, fassungen,
            fehlt):
    f = []

    # Zwei Dateien mit derselben Fassung — welche die aktive ist, entschiede
    # die Sortierung des Dateinamens. Das darf nicht dem Zufall ueberlassen
    # sein, sonst prueft der Lauf still gegen den falschen Katalog.
    doppelt, ohne_fassung = [], []
    for kat, liste in sorted(fassungen.items()):
        gesehen = defaultdict(list)
        for e in liste:
            gesehen[e["fassung"]].append(e["datei"])
        for fa, dateien in sorted(gesehen.items()):
            if len(dateien) > 1:
                doppelt.append(f"{kat} {fassung_str(fa)}: {', '.join(sorted(dateien))}")
        if len(liste) > 1:
            ohne_fassung += [f"{kat}: {e['datei']}" for e in liste
                             if e["fassung"] == (0, 0)]
    if doppelt:
        f.append(("Katalogdateien mit gleicher Fassung (Reihenfolge nicht "
                  "bestimmbar)", doppelt))
    if ohne_fassung:
        f.append(("Katalogdatei ohne Fassung im Namen, obwohl der Katalog "
                  "mehrere Fassungen hat (erwartet <praefix>[_<label>]_<jahr>"
                  "[_v<n>].json)", ohne_fassung))

    verwaist = sorted(n for n in seiten if not backlinks.get(n))
    if verwaist:
        f.append(("verwaiste Seiten (keine eingehenden Links)", verwaist))

    kaputte = sorted(f"{a} -> [[{z}]]" for a, zs in kaputt.items() for z in zs)
    if kaputte:
        f.append(("Wikilinks ins Leere", kaputte))

    # Positionen, die irgendwo im Text vorkommen, fuer die aber keine Seite
    # zustaendig ist. Eine Seite darf Positionen erwaehnen, ohne sie zu fuehren —
    # Querschnittsseiten tun das notwendigerweise.
    # Nur die BEL-Schreibweise "201 0" ist im Text eindeutig einem Katalog
    # zuzuordnen. BEB-Nummern im Text erkennt diese Pruefung nicht — dafuer
    # traegt die Seite ihr Frontmatter.
    erwaehnt = defaultdict(set)
    for n, s in seiten.items():
        if "bel" not in [k.split(":")[0] for k in as_list(s["fm"].get("positionen"))] \
                and as_list(s["fm"].get("positionen")):
            continue
        for a, b in re.findall(r"\b(\d{3}) (\d)\b", s["body"]):
            erwaehnt["bel:" + a + b].add(n)
    ohne_zustaendige = sorted(f"{p} (genannt auf: {', '.join(sorted(v))})"
                              for p, v in erwaehnt.items() if p not in pos2seite)
    if ohne_zustaendige:
        f.append(("Positionen ohne zustaendige Seite", ohne_zustaendige))

    mehrfach = sorted(f"{p}: {', '.join(sorted(v))}"
                      for p, v in pos2seite.items() if len(v) > 1)
    if mehrfach:
        f.append(("Position von mehreren Seiten beansprucht "
                  "(genau eine Seite muss zustaendig sein)", mehrfach))

    ohne_praefix = sorted(f"{n}: {p}" for n, s in seiten.items()
                          for p in as_list(s["fm"].get("positionen"))
                          if not POS.match(p))
    if ohne_praefix:
        f.append(("Positionen ohne Katalog-Praefix (erwartet katalog:nnnn)",
                  ohne_praefix))

    # Jede Positions-ID gegen die aktive Fassung des Rohkatalogs pruefen. Eine
    # ID, die es dort nicht gibt, ist ein Tippfehler, eine erfundene Position
    # oder eine mit dem Fassungswechsel entfallene — beides faellt sonst erst
    # im Kostenvoranschlag auf. Kannte eine aeltere Fassung die Nummer, steht
    # sie dabei: dann ist es kein Tippfehler, sondern eine Matrixzeile.
    nicht_im_katalog = []
    for p in sorted(pos2seite):
        kat, nr = p.split(":", 1)
        if kat in kataloge and nr not in kataloge[kat]:
            alt = zuletzt_in(fassungen, kat, nr)
            herkunft = f", zuletzt in {alt}" if alt else ""
            nicht_im_katalog.append(
                f"{p} (zustaendig: {', '.join(sorted(pos2seite[p]))}{herkunft})")
    if nicht_im_katalog:
        f.append(("Positionen, die es in der aktiven Katalogfassung nicht gibt",
                  nicht_im_katalog))

    unbekannt, fremd, gleich = [], [], []
    for typ, eintraege in kanten.items():
        for a, b, geltung, prosa, quelle in eintraege:
            for p in (a, b):
                if POS.match(p):
                    # Eine 'entspricht'-Kante darf auf eine Katalogposition
                    # ohne eigene Wiki-Seite zeigen — die meisten Positionen
                    # tragen keine Regel und bekommen keine Seite. Fuer die
                    # anderen Kantentypen ist die zustaendige Seite Pflicht,
                    # weil dort die Prosa zur Regel steht.
                    if typ != "entspricht" and p not in pos2seite:
                        unbekannt.append(
                            f"{quelle} [{typ}]: {p} hat keine zustaendige Seite")
                    kat, nr = p.split(":", 1)
                    if kat in kataloge and nr not in kataloge[kat]:
                        alt = zuletzt_in(fassungen, kat, nr)
                        herkunft = f" (zuletzt in {alt})" if alt else ""
                        unbekannt.append(
                            f"{quelle} [{typ}]: {p} steht nicht in der aktiven "
                            f"Katalogfassung{herkunft}")
                elif p:
                    unbekannt.append(
                        f"{quelle} [{typ}]: '{p}' ist keine gueltige Positions-ID")
            if POS.match(a) and POS.match(b):
                ka, kb = a.split(":")[0], b.split(":")[0]
                if ka != kb and typ != "entspricht":
                    fremd.append(f"{quelle} [{typ}]: {a} -> {b}")
                if ka == kb and typ == "entspricht":
                    gleich.append(f"{quelle}: {a} -> {b}")
            if not geltung:
                unbekannt.append(
                    f"{quelle} [{typ}]: {a} -> {b} ohne Geltung im dritten Feld")
            if prosa and prosa not in seiten:
                unbekannt.append(
                    f"{quelle} [{typ}]: Prosaverweis '{prosa}' existiert nicht")
    if unbekannt:
        f.append(("Kanten mit unaufloesbarem Ziel oder fehlender Geltung",
                  sorted(set(unbekannt))))
    if fremd:
        f.append(("Kanten zwischen verschiedenen Katalogen — nur 'entspricht' "
                  "darf das", sorted(set(fremd))))
    if gleich:
        f.append(("'entspricht' innerhalb desselben Katalogs — dafuer ist "
                  "'alternativ_zu' da", sorted(set(gleich))))

    for pos, ziel, grund, quelle in fehlt:
        if not grund:
            f.append(("'kein_aequivalent' ohne Begruendung",
                      [f"{quelle}: {pos} -> {ziel}"]))
            break

    ohne_stand = sorted(n for n, s in seiten.items() if not s["fm"].get("stand"))
    if ohne_stand:
        f.append(("Seiten ohne 'stand:'", ohne_stand))

    return f


# ---------------------------------------------------------------- Ausgabe

def render(seiten, backlinks, kaputt, pos2seite, quelle2seite, kanten,
           label2seite, kataloge, fassungen, fehlt):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    L = []
    L.append("# Graph")
    L.append("")
    L.append(f"Generiert am {ts} aus {len(seiten)} Seiten. Abgeleitet, nicht "
             "Quelle: jede Aenderung von Hand geht beim naechsten Lauf verloren. "
             "Neu erzeugen mit `python3 scripts/graph.py`.")
    L.append("")

    fnd = befunde(seiten, backlinks, kaputt, pos2seite, kanten, kataloge,
                  fassungen, fehlt)
    L.append("## Befunde")
    L.append("")
    if not fnd:
        L.append("Keine.")
    for titel, eintraege in fnd:
        L.append(f"**{titel}**")
        L.append("")
        for e in eintraege:
            L.append(f"- {e}")
        L.append("")
    L.append("")

    L.append("## Backlinks")
    L.append("")
    L.append("| Seite | ein | aus | eingehend von |")
    L.append("|---|---|---|---|")
    for n in sorted(seiten):
        ein = sorted(backlinks.get(n, []))
        aus = len([z for z in seiten[n]["links"] if z in seiten])
        L.append(f"| {n} | {len(ein)} | {aus} | {', '.join(ein) if ein else '—'} |")
    L.append("")

    L.append("## Positionsregister")
    L.append("")
    if pos2seite:
        L.append("| Position | zustaendige Seite |")
        L.append("|---|---|")
        for p in sorted(pos2seite):
            L.append(f"| {p} | {', '.join(sorted(pos2seite[p]))} |")
    else:
        L.append("Leer — keine Seite fuehrt bisher `positionen:` im Frontmatter.")
    L.append("")

    L.append("## Kanten")
    L.append("")
    if not any(kanten.values()):
        L.append("Leer — keine Seite fuehrt bisher Kanten im Frontmatter.")
    for typ in KANTEN_ALLE:
        eintraege = kanten.get(typ)
        if not eintraege:
            continue
        L.append(f"### {typ}")
        L.append("")
        L.append("| von | nach | Geltung | Prosa auf | eingetragen auf |")
        L.append("|---|---|---|---|---|")
        for a, b, g, prosa, quelle in sorted(eintraege):
            L.append(f"| {a} | {b} | {g or '—'} | {prosa or '—'} | {quelle} |")
        L.append("")

        gegen = defaultdict(list)
        for a, b, g, _, _ in eintraege:
            gegen[b].append((a, g))
        L.append(f"Gegenrichtung: " + " · ".join(
            f"{b} ← {', '.join(a for a, _ in v)}" for b, v in sorted(gegen.items())))
        L.append("")

    L.append("## Katalogabdeckung")
    L.append("")
    if kataloge:
        L.append("| Katalog | aktive Fassung | Datei | Positionen | "
                 "davon mit zustaendiger Wiki-Seite |")
        L.append("|---|---|---|---|---|")
        for kat in sorted(kataloge):
            akt = fassungen[kat][0]
            gesamt = len(kataloge[kat])
            gedeckt = len([p for p in pos2seite if p.split(":")[0] == kat])
            L.append(f"| {kat} | {fassung_str(akt['fassung'])} | "
                     f"{akt['datei']} | {gesamt} | {gedeckt} |")
        L.append("")
        L.append("Geprueft wird gegen die aktive Fassung. Vollabdeckung ist "
                 "kein Ziel. Eine Wiki-Seite entsteht fuer regeltragende "
                 "Positionen; der Rest steht im Rohkatalog.")
        L.append("")

        L.append("### Fassungen")
        L.append("")
        L.append("| Katalog | Fassung | Datei | Positionen | Rolle |")
        L.append("|---|---|---|---|---|")
        for kat in sorted(fassungen):
            for i, e in enumerate(fassungen[kat]):
                if i == 0:
                    rolle = "aktiv"
                elif i == 1:
                    rolle = "Vorgaenger — Diff-Grundlage"
                else:
                    rolle = "Archiv"
                L.append(f"| {kat} | {fassung_str(e['fassung'])} | {e['datei']} "
                         f"| {len(e['nummern'])} | {rolle} |")
        L.append("")
        L.append("Eine neue Fassung kommt als weitere Datei dazu, die alte "
                 "bleibt liegen. Der Diff aktive gegen Vorgaengerfassung ist "
                 "die deterministische Haelfte der Aenderungsmatrix; die "
                 "andere Haelfte steht nur in der Quelle.")
    else:
        L.append("Keine Katalogdateien unter kataloge/ gefunden.")
    L.append("")

    ents = kanten.get("entspricht", [])
    if ents or fehlt:
        L.append("## Katalogzuordnung")
        L.append("")
        paare = defaultdict(int)
        for a, b, _, _, _ in ents:
            if POS.match(a) and POS.match(b):
                paare[(a.split(":")[0], b.split(":")[0])] += 1
        for (ka, kb), n in sorted(paare.items()):
            offen = len([p for p in pos2seite if p.split(":")[0] == ka]) - n
            L.append(f"- {ka} -> {kb}: {n} zugeordnet, {offen} ohne Zuordnung")
        if fehlt:
            L.append("")
            L.append("Ausdruecklich ohne Aequivalent:")
            L.append("")
            L.append("| Position | Zielkatalog | Begruendung | vermerkt auf |")
            L.append("|---|---|---|---|")
            for pos, ziel, grund, quelle in sorted(fehlt):
                L.append(f"| {pos} | {ziel} | {grund or '—'} | {quelle} |")
        L.append("")

    L.append("## Quellen")
    L.append("")
    L.append("| Quelle | abhaengige Seiten |")
    L.append("|---|---|")
    for q in sorted(quelle2seite):
        s = sorted(quelle2seite[q])
        L.append(f"| {q} | {len(s)}: {', '.join(s)} |")
    L.append("")

    L.append("## Labels")
    L.append("")
    L.append("| Label | Seiten |")
    L.append("|---|---|")
    for l in sorted(label2seite):
        L.append(f"| {l} | {len(label2seite[l])} |")
    L.append("")

    return "\n".join(L) + "\n"


def main():
    try:
        seiten = load()
        if not seiten:
            raise RuntimeError(f"Keine Wiki-Seiten in {WIKI} gefunden")
        kataloge, fassungen = load_kataloge()
        data = build(seiten)
        text = render(seiten, *data[:-1], kataloge, fassungen, data[-1])
    except Exception as exc:  # Fehler in die Datei schreiben, nicht nur nach stderr
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        text = (f"# Graph\n\nFEHLER beim Erzeugen am {ts}: {exc}\n\n"
                "Der Graph ist unbrauchbar, bis das behoben ist. "
                "Nicht als Grundlage fuer Antworten verwenden.\n")
        sys.stderr.write(f"graph.py: {exc}\n")

    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())