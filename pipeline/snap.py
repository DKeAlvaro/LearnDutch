#!/usr/bin/env python3
"""Snap frames.json × teach.json → sentences.json. No invented lemmas."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DS = ROOT / "dataset"
OUT = DS / "sentences.json"
N = 1000
SLOT = re.compile(r"^\{(noun|adj|verb)\}$")


def load_list(path, key):
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return data
    return data.get(key) or []


def main():
    teach = json.loads((DATA / "teach.json").read_text(encoding="utf-8"))["words"]
    glue = {
        w["nl"]
        for w in json.loads((DS / "glue.json").read_text(encoding="utf-8"))["words"]
    }
    frames = load_list(DS / "frames.json", "frames")
    by_pos = {"noun": [], "adj": [], "verb": []}
    for w in teach:
        if w["pos"] in by_pos and w["nl"] not in glue:
            by_pos[w["pos"]].append(w)
    for pos in by_pos:
        by_pos[pos].sort(key=lambda w: w["freq_rank"])

    rows = []
    seen = set()
    used = {pos: 0 for pos in by_pos}
    articles = {w["article"] for w in teach if w.get("article")}
    # Round-robin frames so one template cannot eat the whole deck.
    guard = 0
    while len(rows) < N and guard < N * 20:
        guard += 1
        frame = frames[len(rows) % len(frames)]
        parts_t = frame.get("parts") or []
        slots = []
        for tok in parts_t:
            m = SLOT.match(tok)
            if m:
                slots.append(m.group(1))
        if not slots:
            continue
        mapping = {}
        ok = True
        parts_l = [t.lower() for t in parts_t]
        for si, pos in enumerate(slots):
            pool = by_pos.get(pos) or []
            if pos == "noun":
                # Honour de/het already in the frame template.
                ni = parts_l.index("{noun}") if "{noun}" in parts_l else -1
                prev = parts_l[ni - 1] if ni > 0 else ""
                if prev in articles:
                    pool = [w for w in pool if w.get("article") == prev]
            if not pool:
                ok = False
                break
            key = pos
            w = pool[used[key] % len(pool)]
            used[key] += 1
            mapping[pos] = w
        if not ok:
            continue
        fills = [mapping[s]["nl"] for s in slots]
        sid = frame["id"] + "__" + "_".join(fills)
        if sid in seen:
            continue
        parts = []
        en = frame.get("en") or ""
        for tok in parts_t:
            m = SLOT.match(tok)
            if not m:
                parts.append(tok)
                continue
            w = mapping[m.group(1)]
            parts.append(w["nl"])
            en = en.replace("{" + m.group(1) + "}", w["nl"], 1)
        if frame["en"].endswith("?") and parts and not parts[-1].endswith("?"):
            parts[-1] = parts[-1] + "?"
        seen.add(sid)
        rows.append(
            {
                "id": sid,
                "frame": frame["id"],
                "level": frame.get("level") or "A0",
                "tags": list(frame.get("tags") or []),
                "en": en,
                "parts": parts,
                "audio": None,
            }
        )
    if len(rows) < N:
        raise SystemExit(f"only {len(rows)} snaps, need {N}")
    OUT.write_text(json.dumps(rows[:N], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", OUT, len(rows[:N]), "frames", len(frames))


if __name__ == "__main__":
    main()
