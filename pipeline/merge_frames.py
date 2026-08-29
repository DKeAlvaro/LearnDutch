#!/usr/bin/env python3
"""Merge dataset/frame_shards/*.json → dataset/frames.json. Literals must be glue."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DS = ROOT / "dataset"
SHARDS = DS / "frame_shards"
OUT = DS / "frames.json"
MIN_N = 200
SLOTS = {"{noun}", "{adj}", "{verb}"}


def main():
    glue = {
        w["nl"]
        for w in json.loads((DS / "glue.json").read_text(encoding="utf-8"))["words"]
    }
    rows = []
    seen = set()
    dropped = 0
    for p in sorted(SHARDS.glob("f*.json")):
        data = json.loads(p.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            data = data.get("frames") or data.get("rows") or []
        for s in data:
            i = s.get("id")
            parts = s.get("parts") or []
            if not i or i in seen or not parts:
                continue
            bad = False
            has_slot = False
            for tok in parts:
                if tok in SLOTS:
                    has_slot = True
                    continue
                if tok.rstrip("?.!").lower() not in glue:
                    bad = True
                    break
            if bad or not has_slot or not s.get("en"):
                dropped += 1
                continue
            seen.add(i)
            rows.append(
                {
                    "id": i,
                    "level": s.get("level"),
                    "tags": s.get("tags") or [],
                    "parts": parts,
                    "en": s["en"],
                }
            )
    if len(rows) < MIN_N:
        raise SystemExit(f"only {len(rows)} frames, need {MIN_N} (dropped {dropped})")
    OUT.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", OUT, len(rows), "dropped", dropped)


if __name__ == "__main__":
    try:
        main()
    except SystemExit as e:
        print(e, file=sys.stderr)
        raise
