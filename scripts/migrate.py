#!/usr/bin/env python3
"""Einmalige Migration: setzt das Katalog-Praefix 'bel:' vor alle Positions-IDs.

Aendert ausschliesslich das Frontmatter — 'positionen:' und die Positionsfelder
in den Kanteneintraegen. Der Fliesstext bleibt unangetastet, dort steht weiter
die Schreibweise der Quelle (201 0).

Laeuft nur, solange das Wiki ausschliesslich BEL-Positionen kennt. Danach ist
die Zuordnung nicht mehr eindeutig ableitbar und muss beim Ingest entstehen.

Aufruf aus dem Repo-Wurzelverzeichnis:
    python3 scripts/migrate_praefix.py --dry-run
    python3 scripts/migrate_praefix.py
"""

import os
import re
import sys

WIKI = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     "..", "wiki"))
SKIP = {"INDEX.md", "LOG.md", "GRAPH.md"}
KANTEN = ["schliesst_aus", "enthalten_in", "alternativ_zu", "ersetzt_durch_bei",
          "entspricht"]
KATALOG = "bel"   # einziger Katalog im Bestand zum Migrationszeitpunkt

nackt = re.compile(r"^\d{4}$")


def migriere_frontmatter(fm_text):
    zeilen = fm_text.split("\n")
    aus, aktiv, n = [], None, 0

    for zeile in zeilen:
        key = re.match(r"([A-Za-z_]+):", zeile)
        if key:
            aktiv = key.group(1)

        # positionen: [0010, 0021] — Inline-Liste
        if aktiv == "positionen" and "[" in zeile:
            def ersetze(m):
                return f"{KATALOG}:{m.group(0)}"
            neu = re.sub(r"(?<![\w:])\d{4}(?![\w:])", ersetze,
                         zeile[zeile.index("["):])
            n += len(re.findall(r"(?<![\w:])\d{4}(?![\w:])",
                                zeile[zeile.index("["):]))
            zeile = zeile[:zeile.index("[")] + neu

        # Kanteneintrag: "0021 | 2010 | Geltung | seite"
        elif aktiv in KANTEN and re.match(r"\s+-\s", zeile):
            m = re.match(r"(\s+-\s+)([\"']?)(.*?)([\"']?)\s*$", zeile)
            if m:
                pre, q1, inhalt, q2 = m.groups()
                teile = [t.strip() for t in inhalt.split("|")]
                for i in (0, 1):
                    if i < len(teile) and nackt.match(teile[i]):
                        teile[i] = f"{KATALOG}:{teile[i]}"
                        n += 1
                zeile = f'{pre}{q1}{" | ".join(teile)}{q2}'

        aus.append(zeile)
    return "\n".join(aus), n


def main():
    dry = "--dry-run" in sys.argv
    gesamt, dateien = 0, 0

    for fn in sorted(os.listdir(WIKI)):
        if not fn.endswith(".md") or fn in SKIP:
            continue
        pfad = os.path.join(WIKI, fn)
        with open(pfad, encoding="utf-8") as fh:
            text = fh.read()
        if not text.startswith("---"):
            continue
        ende = text.find("\n---", 3)
        if ende == -1:
            continue

        fm, rest = text[3:ende], text[ende:]
        neu_fm, n = migriere_frontmatter(fm)
        if n == 0:
            continue

        gesamt += n
        dateien += 1
        print(f"{fn}: {n} IDs")
        if not dry:
            with open(pfad, "w", encoding="utf-8") as fh:
                fh.write("---" + neu_fm + rest)

    modus = "wuerde aendern" if dry else "geaendert"
    print(f"\n{modus}: {gesamt} IDs in {dateien} Dateien")
    if not dry:
        print("Jetzt 'python3 scripts/graph.py' laufen lassen und die Befunde pruefen.")
    return 0


if __name__ == "__main__":
    sys.exit(main())