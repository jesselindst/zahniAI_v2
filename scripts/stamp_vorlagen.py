#!/usr/bin/env python3
"""Einmalige Migration: stempelt jede Vorlage mit ihrer Katalog-Herkunft.

Liest die Spaltenkoepfe der Positionstabellen (BEB97, BEL), leitet daraus die
verwendeten Kataloge ab und schreibt ein Frontmatter mit den aktiven
Katalogdateien zum Stempelzeitpunkt. Die Tabellen bleiben unangetastet —
das Kuerzel traegt der Spaltenkopf, nicht die Zelle.

Das Frontmatter ist der Anker fuer Fassungswechsel: Eine Aenderungsmatrix
2026 -> 2027 trifft genau die Vorlagen, deren 'kataloge:' noch auf eine
2026er-Datei zeigt. Nach dem Nachziehen wird die Fassung hochgestempelt.

Vorlagen, die schon ein Frontmatter tragen, werden uebersprungen.

Aufruf aus dem Repo-Wurzelverzeichnis:
    python3 scripts/stamp_vorlagen.py --dry-run
    python3 scripts/stamp_vorlagen.py
"""

import datetime
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graph import load_kataloge  # noqa: E402

BASIS = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                      ".."))
VORLAGEN = os.path.join(BASIS, "vorlagen")

KOPF = re.compile(r"^\|\s*(BEB97|BEL|BEBZT|GOZ|BEMA)\s*\|", re.IGNORECASE)


def main():
    dry = "--dry-run" in sys.argv
    _, fassungen = load_kataloge()
    aktiv = {k: liste[0]["datei"] for k, liste in fassungen.items()}
    heute = datetime.date.today().isoformat()

    gestempelt, uebersprungen, ohne = 0, 0, []
    for pfad in sorted(glob.glob(os.path.join(VORLAGEN, "**", "*.md"),
                                 recursive=True)):
        if os.path.basename(pfad).startswith("_"):
            continue
        with open(pfad, encoding="utf-8") as fh:
            text = fh.read()
        if text.startswith("---"):
            uebersprungen += 1
            continue

        praefixe = sorted({m.group(1).lower()
                           for m in (KOPF.match(z) for z in text.split("\n"))
                           if m})
        rel = os.path.relpath(pfad, BASIS)
        dateien = [aktiv[p] for p in praefixe if p in aktiv]
        if not dateien:
            ohne.append(rel)
            continue

        fm = ("---\n"
              f"kataloge: [{', '.join(dateien)}]\n"
              f"stand: {heute}\n"
              "---\n\n")
        gestempelt += 1
        print(f"{rel}: {', '.join(dateien)}")
        if not dry:
            with open(pfad, "w", encoding="utf-8") as fh:
                fh.write(fm + text)

    modus = "wuerde stempeln" if dry else "gestempelt"
    print(f"\n{modus}: {gestempelt}, schon mit Frontmatter: {uebersprungen}")
    if ohne:
        print("ohne Positionstabelle (nicht gestempelt):")
        for r in ohne:
            print(f"  {r}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
