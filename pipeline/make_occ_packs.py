#!/usr/bin/env python3
"""Occupation packs: tag slices + counts. No job titles in this file."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dataset" / "occ_packs"

# Closed tag set from the product, not a job list.
PACKS = (
    [("work",)] * 6
    + [("student",)]
    + [("home",)]
    + [("out",)]
    + [("health",)]
)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (ROOT / "dataset" / "occ_shards").mkdir(parents=True, exist_ok=True)
    for i, tags in enumerate(PACKS, 1):
        n = 70 if tags == ("work",) else 50
        pack = {"id": f"o{i:02d}", "n": n, "tags": list(tags)}
        (OUT / f"{pack['id']}.json").write_text(
            json.dumps(pack, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    print("occ_packs", len(PACKS))


if __name__ == "__main__":
    main()
