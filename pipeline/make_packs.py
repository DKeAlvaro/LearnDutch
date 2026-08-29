#!/usr/bin/env python3
"""Slice teach.json into 24 closed packs. Deterministic. No invented words."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PACKS = ROOT / "dataset" / "packs"

THEMES = [
    ("s01", "A0", ["home"], "home: food drink kitchen", ["ik_wil", "ik_heb", "ik_koop", "er_is", "een_alsjeblieft"]),
    ("s02", "A0", ["home"], "home: house rooms family", ["dit_is_mijn", "waar_is", "de_is_adj", "het_is_adj", "ik_zoek"]),
    ("s03", "A0", ["out"], "out: cafe shop street", ["ik_wil", "een_alsjeblieft", "ik_koop", "ik_neem", "waar_is"]),
    ("s04", "A0", ["out"], "out: transport directions", ["ik_ga_naar", "waar_is", "ik_neem", "ik_zoek", "er_is"]),
    ("s05", "A0", ["work"], "work: office basics", ["ik_heb", "waar_is", "dit_is_mijn", "ik_zoek", "ik_zie"]),
    ("s06", "A0", ["student"], "student: school campus", ["ik_ga_naar", "waar_is", "ik_heb", "dit_is_mijn", "ik_zie"]),
    ("s07", "A0", ["health"], "health: body doctor", ["ik_heb", "ik_zoek", "waar_is", "ik_ga_naar", "er_is"]),
    ("s08", "A0", ["home"], "home: time week day", ["ik_heb", "er_is", "de_is_adj", "het_is_adj", "ik_wil"]),
    ("s09", "A0", ["work", "out"], "work: horeca warehouse shop", ["ik_neem", "ik_heb", "waar_is", "ik_zoek", "een_alsjeblieft"]),
    ("s10", "A0", ["out", "home"], "out: money papers phone", ["ik_heb", "ik_zoek", "dit_is_mijn", "waar_is", "ik_koop"]),
    ("s11", "A0", ["home", "out"], "home: clothes weather", ["ik_heb", "ik_wil", "de_is_adj", "ik_koop", "dit_is_mijn"]),
    ("s12", "A0", ["student", "work"], "people: jobs self", ["ik_ben", "ik_woon_in", "dit_is_mijn", "ik_heb", "ik_zie"]),
    ("s13", "A1", ["work"], "work: hours meetings", ["ik_werk_tot", "ik_moet_naar", "kun_je", "waar_is", "ik_heb"]),
    ("s14", "A1", ["student"], "student: study classes", ["ik_studeer", "kun_je", "ik_moet_naar", "hoe_laat", "ik_heb"]),
    ("s15", "A1", ["out"], "out: travel timetable", ["hoe_laat", "ik_moet_naar", "ik_ga_naar", "waar_is", "ik_neem"]),
    ("s16", "A1", ["health"], "health: appointment", ["ik_moet_naar", "kun_je", "ik_heb", "waar_is", "hoe_laat"]),
    ("s17", "A1", ["home"], "home: chores errands", ["ik_moet_naar", "ik_koop", "kun_je", "waar_is", "ik_zoek"]),
    ("s18", "A1", ["work", "out"], "work: gemeente papers", ["ik_moet_naar", "ik_heb", "kun_je", "waar_is", "dit_is_mijn"]),
    ("s19", "A0", ["out"], "out: food restaurant", ["ik_wil", "een_alsjeblieft", "ik_neem", "ik_koop", "er_is"]),
    ("s20", "A0", ["work", "student"], "tech: laptop mail", ["ik_heb", "dit_is_mijn", "ik_zoek", "waar_is", "ik_zie"]),
    ("s21", "A0", ["home"], "home: live city", ["ik_woon_in", "ik_ga_naar", "waar_is", "er_is", "dit_is_mijn"]),
    ("s22", "A1", ["student", "work"], "ask help borrow", ["kun_je", "ik_zoek", "ik_heb", "waar_is", "ik_moet_naar"]),
    ("s23", "A0", ["out", "home"], "out: looking around", ["ik_zie", "ik_zoek", "waar_is", "er_is", "ik_ga_naar"]),
    ("s24", "A1", ["out", "home"], "inburgering daily", ["ik_moet_naar", "ik_heb", "waar_is", "kun_je", "dit_is_mijn"]),
]


def main():
    PACKS.mkdir(parents=True, exist_ok=True)
    teach = json.loads((DATA / "teach.json").read_text(encoding="utf-8"))["words"]
    nouns = [w for w in teach if w["pos"] == "noun"]
    verbs = [w for w in teach if w["pos"] == "verb"][:80]
    adjs = [w for w in teach if w["pos"] == "adj"][:60]
    n = 24
    size = len(nouns) // n
    for i, (sid, level, tags, theme, frames) in enumerate(THEMES):
        chunk = nouns[i * size : (i + 1) * size]
        pack = {
            "id": sid,
            "n": 42,
            "level": level,
            "tags": tags,
            "theme": theme,
            "frames": frames,
            "nouns": chunk,
            "verbs": verbs[i * 3 : i * 3 + 12] or verbs[:12],
            "adjs": adjs[i * 2 : i * 2 + 8] or adjs[:8],
        }
        (PACKS / f"{sid}.json").write_text(
            json.dumps(pack, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    print("packs", n, "nouns_each", size)


if __name__ == "__main__":
    main()
