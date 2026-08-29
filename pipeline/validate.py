#!/usr/bin/env python3
"""Check dataset/*.json against pipeline/04-validate.md. Tokens from data files only."""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DS = ROOT / "dataset"
DATA = ROOT / "data"


def load(name):
    return json.loads((DS / name).read_text(encoding="utf-8"))


def as_list(obj, key):
    if isinstance(obj, list):
        return obj
    return obj.get(key) or []


def allowed(teach_words, freq_words, frames):
    allow = {w["nl"] for w in teach_words}
    allow.update(w["nl"] for w in freq_words if w["rank"] <= 80)
    for f in frames:
        for tok in f.get("parts") or []:
            if tok.startswith("{") and tok.endswith("}"):
                continue
            bare = tok.rstrip("?.!")
            allow.add(bare)
            allow.add(bare.lower())
    return allow


def main():
    occ = as_list(load("occupations.json"), "occupations")
    frames = as_list(load("frames.json"), "frames")
    sents = as_list(load("sentences.json"), "sentences")
    teach_words = json.loads((DATA / "teach.json").read_text(encoding="utf-8"))["words"]
    freq_words = json.loads((DATA / "frequency.json").read_text(encoding="utf-8"))["words"]
    teach = {w["nl"]: w for w in teach_words}
    allow = allowed(teach_words, freq_words, frames)
    articles = {w["article"] for w in teach_words if w.get("article")}
    ok_levels = {f.get("level") for f in frames}

    errors = []
    if len(sents) != 1000:
        errors.append(f"sentences count {len(sents)} != 1000")
    ids = [s.get("id") for s in sents]
    if len(ids) != len(set(ids)):
        errors.append("duplicate ids")
    frame_ids = {f.get("id") for f in frames}
    for s in sents:
        if s.get("level") not in ok_levels:
            errors.append(f"bad level {s.get('id')} {s.get('level')}")
        if s.get("frame") not in frame_ids:
            errors.append(f"unknown frame {s.get('id')} {s.get('frame')}")
        parts = s.get("parts") or []
        if not parts:
            errors.append(f"empty parts {s.get('id')}")
        for j, tok in enumerate(parts):
            t = tok.rstrip("?.!")
            tl = t.lower()
            if tl not in allow and t not in allow:
                errors.append(f"token not in dicts: {t!r} ({s.get('id')})")
            if tl in articles and j + 1 < len(parts):
                nxt = parts[j + 1].rstrip("?.!").lower()
                info = teach.get(nxt)
                if info and info.get("pos") == "noun" and info.get("article") and info["article"] != tl:
                    errors.append(
                        f"article {tl} {nxt} != {info['article']} ({s.get('id')})"
                    )
            if len(errors) > 40:
                break
        if len(errors) > 40:
            break

    print("occupations", len(occ))
    print("frames", len(frames))
    print("sentences", len(sents))
    print("by level", dict(Counter(s.get("level") for s in sents)))
    tags = Counter()
    for s in sents:
        for t in s.get("tags") or []:
            tags[t] += 1
    print("by tag", dict(tags))
    print("sample:")
    for s in sents[:8]:
        print(" ", s.get("level"), " ".join(s.get("parts") or []), "/", s.get("en"))
    if errors:
        print("ERRORS", len(errors))
        for e in errors[:25]:
            print(" -", e)
        sys.exit(1)
    print("OK")


if __name__ == "__main__":
    main()
