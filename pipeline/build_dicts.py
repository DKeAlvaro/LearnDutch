#!/usr/bin/env python3
"""Build frequency.json and teach.json from published sources. Do not invent words."""
from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from wordfreq import top_n_list, zipf_frequency

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
UD_DIR = Path("/tmp/ud-nl")
WORD_OK = re.compile(r"^[a-zàáâäèéêëìíîïòóôöùúûüÿñçæœ\-']+$")

CONTENT = {"NOUN", "VERB", "ADJ"}
CLOSED = {"ADP", "DET", "PRON", "CCONJ", "SCONJ", "PART", "AUX", "PUNCT", "SYM", "X", "INTJ", "NUM"}


def parse_ud(path: Path):
    pos_c = defaultdict(Counter)
    gen_c = defaultdict(Counter)
    with path.open(encoding="utf-8") as f:
        for line in f:
            if not line.strip() or line.startswith("#"):
                continue
            cols = line.rstrip("\n").split("\t")
            if len(cols) < 6 or not cols[0].isdigit():
                continue
            lemma, upos, feats = cols[2].lower(), cols[3], cols[5]
            if not WORD_OK.match(lemma):
                continue
            pos_c[lemma][upos] += 1
            if upos == "NOUN" and feats and feats != "_":
                for kv in feats.split("|"):
                    if kv.startswith("Gender="):
                        gen_c[lemma][kv.split("=", 1)[1]] += 1
    return pos_c, gen_c


def merge_ud():
    pos, gen = defaultdict(Counter), defaultdict(Counter)
    for name in ("alpino-train.conllu", "lassy-train.conllu"):
        p, g = parse_ud(UD_DIR / name)
        for k, c in p.items():
            pos[k].update(c)
        for k, c in g.items():
            gen[k].update(c)
    return pos, gen


def article_of(lemma: str, gen) -> str | None:
    if lemma not in gen or not gen[lemma]:
        return None
    g, _ = gen[lemma].most_common(1)[0]
    if g == "Com":
        return "de"
    if g == "Neut":
        return "het"
    return None


def main():
    DATA.mkdir(parents=True, exist_ok=True)
    words = top_n_list("nl", 5000)
    freq = []
    for i, w in enumerate(words, 1):
        freq.append({"rank": i, "nl": w, "zipf": round(zipf_frequency(w, "nl"), 3)})
    pos, gen = merge_ud()

    teach = []
    for item in freq:
        w = item["nl"]
        if w not in pos:
            continue
        upos, n = pos[w].most_common(1)[0]
        closed_n = sum(pos[w][p] for p in CLOSED)
        verbish = pos[w]["VERB"] + pos[w]["AUX"]
        if upos == "NOUN":
            art = article_of(w, gen)
            if not art or n < 3:
                continue
            if verbish > n:
                continue
            glue = closed_n + pos[w]["ADV"]
            if glue > n:
                continue
        elif upos == "VERB":
            if n < 3 or closed_n > n:
                continue
            if not (w.endswith("en") or w in {"zijn", "doen", "gaan", "zien", "slaan", "staan"}):
                continue
        elif upos == "ADJ":
            if n < 3 or closed_n > n:
                continue
        else:
            continue
        row = {
            "nl": w,
            "pos": upos.lower(),
            "zipf": item["zipf"],
            "freq_rank": item["rank"],
            "ud_count": int(n),
        }
        if upos == "NOUN":
            row["article"] = article_of(w, gen)
        teach.append(row)

    nouns = [r for r in teach if r["pos"] == "noun"][:800]
    verbs = [r for r in teach if r["pos"] == "verb"][:400]
    adjs = [r for r in teach if r["pos"] == "adj"][:200]
    teach_out = nouns + verbs + adjs

    (DATA / "frequency.json").write_text(
        json.dumps(
            {
                "source": "wordfreq top_n_list('nl', 5000)",
                "license": "CC BY-SA 4.0 (wordfreq data) + Apache-2.0 (code)",
                "attribution": "Speer, Robyn (2018). wordfreq. https://github.com/rspeer/wordfreq",
                "n": len(freq),
                "words": freq,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    (DATA / "teach.json").write_text(
        json.dumps(
            {
                "source": (
                    "Intersection of wordfreq Dutch ranks with content-word UPOS "
                    "(NOUN/VERB/ADJ) in Universal Dependencies UD_Dutch-Alpino + "
                    "UD_Dutch-LassySmall train sets. Article from UD Gender."
                ),
                "license": "CC BY-SA 4.0 (UD treebanks + wordfreq data)",
                "attribution": [
                    "Speer, Robyn. wordfreq. https://github.com/rspeer/wordfreq",
                    "Universal Dependencies: UD_Dutch-Alpino, UD_Dutch-LassySmall (CC BY-SA 4.0)",
                ],
                "counts": {"noun": len(nouns), "verb": len(verbs), "adj": len(adjs)},
                "words": teach_out,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print("frequency", len(freq))
    print("teach", {k: v for k, v in json.loads((DATA / "teach.json").read_text())["counts"].items()})
    print("sample nouns", [r["nl"] for r in nouns[:15]])
    print("sample verbs", [r["nl"] for r in verbs[:10]])


if __name__ == "__main__":
    main()
