#!/usr/bin/env python3
"""Slice teach.json + frames.json into 24 closed packs. Lexicon stays in those files."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DS = ROOT / "dataset"
PACKS = DS / "packs"

N_PACKS = 24
N_SENTENCES = 42
FRAMES_PER = 5


def split(seq, i, n):
    size, extra = divmod(len(seq), n)
    start = i * size + min(i, extra)
    end = start + size + (1 if i < extra else 0)
    return seq[start:end]


def main():
    PACKS.mkdir(parents=True, exist_ok=True)
    teach = json.loads((DATA / "teach.json").read_text(encoding="utf-8"))["words"]
    frames = json.loads((DS / "frames.json").read_text(encoding="utf-8"))
    if isinstance(frames, dict):
        frames = frames.get("frames") or []
    nouns = [w for w in teach if w["pos"] == "noun"]
    verbs = [w for w in teach if w["pos"] == "verb"]
    adjs = [w for w in teach if w["pos"] == "adj"]

    for i in range(N_PACKS):
        chosen = [frames[(i * FRAMES_PER + k) % len(frames)] for k in range(FRAMES_PER)]
        tags = [t for t, _ in Counter(t for f in chosen for t in (f.get("tags") or [])).most_common(2)]
        level = Counter(f.get("level") for f in chosen).most_common(1)[0][0]
        pack = {
            "id": f"s{i + 1:02d}",
            "n": N_SENTENCES,
            "level": level,
            "tags": tags,
            "frames": [f["id"] for f in chosen],
            "nouns": split(nouns, i, N_PACKS),
            "verbs": split(verbs, i, N_PACKS),
            "adjs": split(adjs, i, N_PACKS),
        }
        (PACKS / f"{pack['id']}.json").write_text(
            json.dumps(pack, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    print("packs", N_PACKS, "nouns", len(nouns), "verbs", len(verbs), "adjs", len(adjs), "frames", len(frames))


if __name__ == "__main__":
    main()
