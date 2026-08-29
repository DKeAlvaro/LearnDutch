#!/usr/bin/env python3
"""Frame packs + glue.json from frequency.json. No templates in this file."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DS = ROOT / "dataset"
OUT = DS / "frame_packs"
GLUE_RANK = 200
N_PACKS = 12
N_EACH = 30
TAGS = ["student", "work", "home", "out", "health"]
LEVELS = ["A0", "A1"]
SLOT_SETS = [["{noun}"], ["{noun}", "{adj}"], ["{noun}", "{verb}"]]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (DS / "frame_shards").mkdir(parents=True, exist_ok=True)
    freq = json.loads((DATA / "frequency.json").read_text(encoding="utf-8"))["words"]
    glue = [w for w in freq if w["rank"] <= GLUE_RANK]
    (DS / "glue.json").write_text(
        json.dumps({"source": "frequency.json", "rank_max": GLUE_RANK, "words": glue}, ensure_ascii=False, indent=2)
        + "\n",
        encoding="utf-8",
    )
    for i in range(N_PACKS):
        pack = {
            "id": f"f{i + 1:02d}",
            "n": N_EACH,
            "level": LEVELS[i % len(LEVELS)],
            "tags": [TAGS[i % len(TAGS)], TAGS[(i + 2) % len(TAGS)]],
            "slots": SLOT_SETS[i % len(SLOT_SETS)],
        }
        (OUT / f"{pack['id']}.json").write_text(
            json.dumps(pack, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    print("frame_packs", N_PACKS, "glue", len(glue))


if __name__ == "__main__":
    main()
