# Continue here

updated: 2026-08-29

Previous chat hit context limit. Pi JSON runs were killed. **No `dataset/sentences.json` yet.**

## Product

Native Android app later. Web mock is the test field: https://dkealvaro.github.io/LearnDutch/

- Dumb player + curated phrase dataset. Not a textbook.
- First open: type **What do you do?** against `dataset/occupations.json` (EN/ES aliases).
- Drill: English prompt, build Dutch from word chips (legos).
- Do **not** ask CEFR. Each sentence has `level` (`A0`/`A1`).
- Audio baked later; IAP for hear. No accounts/SRS.

Specs: `vision.md`, `product.md`, `sources.md`.

## Dictionaries (done, do not invent words)

| File | What | Source |
|---|---|---|
| `data/frequency.json` | Top 5000 nl zipf | wordfreq (CC BY-SA 4.0) |
| `data/teach.json` | 800 nouns + verbs + adjs | those ranks ∩ UD Alpino+LassySmall content UPOS (CC BY-SA 4.0) |

Rebuild: `.venv/bin/python pipeline/build_dicts.py` (needs `/tmp/ud-nl/*.conllu`).

Frequency = glue (`de van ik`). Teach = chicha (`huis vrouw water`). Homographs (`meer`, `wil`) exist; skip the function-word sense.

## How data gets made

Python never lists Dutch jobs, frames, or fills. It slices `data/*.json`.

1. **Occupations** — 10 `jobs` children (`workflow-occupations.js`) → `occupations.json` (≥400). Typeahead, not the phrase lexicon.
2. **Frames** — glue from frequency rank ≤ 200; 12 `framer` children (`workflow-frames.js`) → `frames.json` (≥200).
3. **Phrases** — `make_packs.py` slices teach + those frames; 24 `phraser` children → `sentences.json` (1000).

Do **not** let one Pi write a whole file. Handwritten occupations/frames stay short and starve the app.

## Launch

One child at a time on this 1 GB VPS. Occupations first:

```
pi-live start -C /root/LearnDutch --approve "Call the subagent tool ONCE with workflowScriptPath pipeline/workflow-occupations.js and cwd /root/LearnDutch. async false. Do not write occupations yourself."
```

Then the same for `workflow-frames.js`, then `workflow-phrases.js`. Kill if 7 min stuck with no new shard.

`pi-subagents` is already in `~/.pi/agent/settings.json` packages.

## Layout

```
data/frequency.json teach.json SOURCES.md
dataset/occupations.json frames.json glue.json
dataset/occ_packs/ occ_shards/
dataset/frame_packs/ frame_shards/
dataset/packs/ shards/
dataset/sentences.json
pipeline/README.md
pipeline/workflow-occupations.js workflow-frames.js workflow-phrases.js
pipeline/make_occ_packs.py make_frame_packs.py make_packs.py
.pi/agents/jobs.md framer.md phraser.md
docs/index.html            ← mock on GH Pages
```

## Mock / product notes for later

- Typeahead job, not four chips.
- Harder drill = assemble the line in order.
- Level inferred from sentence ids, not asked.
- Next: feed `sentences.json` into the mock.
