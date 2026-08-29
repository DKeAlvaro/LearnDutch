#!/usr/bin/env python3
"""Merge dataset/occ_shards/*.json → dataset/occupations.json."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARDS = ROOT / "dataset" / "occ_shards"
OUT = ROOT / "dataset" / "occupations.json"
MIN_N = 400
TAGS = {"student", "work", "home", "out", "health"}


def main():
    rows = []
    seen = set()
    for p in sorted(SHARDS.glob("o*.json")):
        data = json.loads(p.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            data = data.get("occupations") or data.get("rows") or []
        for s in data:
            i = s.get("id")
            if not i or i in seen:
                continue
            aliases = [a.strip().lower() for a in (s.get("aliases") or []) if a and str(a).strip()]
            tags = [t for t in (s.get("tags") or []) if t in TAGS]
            if not aliases or not tags or not s.get("label"):
                continue
            seen.add(i)
            rows.append({"id": i, "label": s["label"], "aliases": aliases, "tags": tags})
    if len(rows) < MIN_N:
        raise SystemExit(f"only {len(rows)} occupations, need {MIN_N}")
    OUT.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", OUT, len(rows))


if __name__ == "__main__":
    try:
        main()
    except SystemExit as e:
        print(e, file=sys.stderr)
        raise
