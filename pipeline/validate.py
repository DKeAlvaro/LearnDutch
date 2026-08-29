#!/usr/bin/env python3
"""Check dataset/*.json against pipeline/04-validate.md."""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DS = ROOT / "dataset"
DATA = ROOT / "data"

FN = {
    "ik", "je", "jij", "hij", "ze", "zij", "we", "wij", "u", "het", "de", "een",
    "van", "in", "op", "te", "en", "is", "zijn", "heb", "hebt", "heeft", "wil",
    "wilt", "naar", "met", "voor", "als", "dat", "die", "dit", "niet", "geen",
    "er", "waar", "hoe", "wat", "mijn", "jouw", "haar", "zijn", "ons", "jullie",
    "een", "alstublieft", "alsjeblieft", "om", "tot", "bij", "aan", "uit",
}


def load(name):
    return json.loads((DS / name).read_text(encoding="utf-8"))


def main():
    occ = load("occupations.json")
    frames = load("frames.json")
    sents = load("sentences.json")
    teach = {w["nl"]: w for w in json.loads((DATA / "teach.json").read_text())["words"]}
    freq80 = {
        w["nl"]
        for w in json.loads((DATA / "frequency.json").read_text())["words"]
        if w["rank"] <= 80
    }
    allow = set(teach) | FN | freq80

    errors = []
    if not isinstance(occ, list):
        occ = occ.get("occupations", occ)
    if not isinstance(frames, list):
        frames = frames.get("frames", frames)
    if not isinstance(sents, list):
        sents = sents.get("sentences", sents)

    if len(sents) != 1000:
        errors.append(f"sentences count {len(sents)} != 1000")
    ids = [s.get("id") for s in sents]
    if len(ids) != len(set(ids)):
        errors.append("duplicate ids")
    frame_ids = {f.get("id") for f in frames}
    for i, s in enumerate(sents):
        if s.get("level") not in {"A0", "A1"}:
            errors.append(f"bad level {s.get('id')} {s.get('level')}")
        if s.get("frame") not in frame_ids:
            errors.append(f"unknown frame {s.get('id')} {s.get('frame')}")
        parts = s.get("parts") or []
        if not parts:
            errors.append(f"empty parts {s.get('id')}")
        for tok in parts:
            t = tok.rstrip("?.!")
            if t.lower() not in allow and t not in allow:
                errors.append(f"token not in dicts: {t!r} ({s.get('id')})")
                if len(errors) > 40:
                    break
        if len(errors) > 40:
            break

    print("occupations", len(occ) if isinstance(occ, list) else type(occ))
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
