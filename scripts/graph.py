#!/usr/bin/env python3
"""Erzeugt wiki/GRAPH.md aus den Wiki-Seiten.

Rein ableitend: liest wiki/*.md, schreibt genau eine Datei.
Aendert niemals eine Wissensseite. Wird von den Skills ingest, lint und
query zu Beginn ihres Laufs aufgerufen.
"""

import os
import re
import sys
import datetime
from collections import defaultdict

WIKI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "wiki")
WIKI = os.path.normpath(WIKI)
OUT = os.path.join(WIKI, "GRAPH.md")
SKIP = {"INDEX.md", "LOG.md", "GRAPH.md"}

KANTEN = ["schliesst_aus", "enthalten_in", "alternativ_zu", "ersetzt_durch_bei"]


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
            if re.fullmatch(r"\d{4}", p):
                pos2seite[p].add(name)

    quelle2seite = defaultdict(set)
    for name, s in seiten.items():
        for q in as_list(s["fm"].get("quellen")):
            quelle2seite[q].add(name)

    kanten = defaultdict(list)
    for name, s in seiten.items():
        for typ in KANTEN:
            for eintrag in as_list(s["fm"].get(typ)):
                a, b, geltung, prosa = kante_teile(eintrag)
                kanten[typ].append((a, b, geltung, prosa, name))

    label2seite = defaultdict(set)
    for name, s in seiten.items():
        for l in as_list(s["fm"].get("labels")):
            label2seite[l].add(name)

    return backlinks, kaputt, pos2seite, quelle2seite, kanten, label2seite


def befunde(seiten, backlinks, kaputt, pos2seite, kanten):
    f = []

    verwaist = sorted(n for n in seiten if not backlinks.get(n))
    if verwaist:
        f.append(("verwaiste Seiten (keine eingehenden Links)", verwaist))

    kaputte = sorted(f"{a} -> [[{z}]]" for a, zs in kaputt.items() for z in zs)
    if kaputte:
        f.append(("Wikilinks ins Leere", kaputte))

    ohne_pos = sorted(n for n, s in seiten.items()
                      if not as_list(s["fm"].get("positionen"))
                      and re.search(r"\b\d{3} \d\b", s["body"]))
    if ohne_pos:
        f.append(("Seiten nennen Positionen im Text, fuehren aber kein "
                  "'positionen:' im Frontmatter", ohne_pos))

    mehrfach = sorted(f"{p}: {', '.join(sorted(v))}"
                      for p, v in pos2seite.items() if len(v) > 1)
    if mehrfach:
        f.append(("Position von mehreren Seiten beansprucht "
                  "(genau eine Seite muss zustaendig sein)", mehrfach))

    unbekannt = []
    for typ, eintraege in kanten.items():
        for a, b, _, prosa, quelle in eintraege:
            for p in (a, b):
                if re.fullmatch(r"\d{4}", p) and p not in pos2seite:
                    unbekannt.append(f"{quelle} [{typ}]: {p} hat keine zustaendige Seite")
            if prosa and prosa not in seiten:
                unbekannt.append(f"{quelle} [{typ}]: Prosaverweis '{prosa}' existiert nicht")
    if unbekannt:
        f.append(("Kanten mit unaufloesbarem Ziel", sorted(set(unbekannt))))

    ohne_stand = sorted(n for n, s in seiten.items() if not s["fm"].get("stand"))
    if ohne_stand:
        f.append(("Seiten ohne 'stand:'", ohne_stand))

    return f


# ---------------------------------------------------------------- Ausgabe

def render(seiten, backlinks, kaputt, pos2seite, quelle2seite, kanten, label2seite):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    L = []
    L.append("# Graph")
    L.append("")
    L.append(f"Generiert am {ts} aus {len(seiten)} Seiten. Abgeleitet, nicht "
             "Quelle: jede Aenderung von Hand geht beim naechsten Lauf verloren. "
             "Neu erzeugen mit `python3 scripts/graph.py`.")
    L.append("")

    fnd = befunde(seiten, backlinks, kaputt, pos2seite, kanten)
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
    for typ in KANTEN:
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
        data = build(seiten)
        text = render(seiten, *data)
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