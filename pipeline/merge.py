#!/usr/bin/env python3
"""Merge dataset/shards/*.json → dataset/sentences.json (1000 rows)."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARDS = ROOT / "dataset" / "shards"
OUT = ROOT / "dataset" / "sentences.json"


def main():
    rows = []
    seen = set()
    for p in sorted(SHARDS.glob("s*.json")):
        data = json.loads(p.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            data = data.get("sentences") or data.get("rows") or []
        for s in data:
            i = s.get("id")
            if not i or i in seen:
                continue
            seen.add(i)
            s.setdefault("audio", None)
            rows.append(s)
    if len(rows) < 1000:
        raise SystemExit(f"only {len(rows)} unique sentences, need 1000")
    rows = rows[:1000]
    OUT.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", OUT, len(rows))


if __name__ == "__main__":
    main()
