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

## How phrases get made

**Determinism:** a closed pack per shard (`dataset/packs/s01.json`…`s24.json`) — nouns/verbs/adjs sliced from teach, plus frame ids, theme, tags, level, `n=42`.

**Intelligence:** 24 Pi **phraser** subagents. Each reads **one** pack and writes **one** shard of spoken sentences. They choose which snaps are sayable. They do not see the whole lexicon.

Do **not** let one Pi write all 1000 lines. That run was junk (10 min dumping dictionaries, zero files).

Rebuild packs: `.venv/bin/python pipeline/make_packs.py`

## Launch (next session)

1. Confirm no leftover `pi --mode json`.
2. Parent Pi only orchestrates:

```
pi-live start -C /root/LearnDutch --approve "Call the subagent tool with workflowScriptPath pipeline/workflow-phrases.js and cwd /root/LearnDutch. concurrency 5 if the tool allows it. Do not write sentences yourself. 24 phraser children, then merge worker. If agent phraser is missing, use worker."
```

3. Workflow: `pipeline/workflow-phrases.js` — `runs.all` of s01–s24 (`agent: phraser`), then `merge` worker runs `pipeline/merge.py` + `pipeline/validate.py`.
4. Phraser agent: `.pi/agents/phraser.md`
5. Health: process alive, `n` increasing **or** `dataset/shards/s*.json` appearing. RAM on this 1 GB VPS: keep **≤5 concurrent** children. Kill if 7 min stuck with no new shard.
6. Success: `dataset/sentences.json` with 1000 rows and `python3 pipeline/validate.py` prints OK. Then `git push`.

`pi-subagents` is already in `~/.pi/agent/settings.json` packages.

## Layout

```
data/frequency.json teach.json SOURCES.md
dataset/occupations.json frames.json
dataset/packs/s01.json … s24.json
dataset/shards/            ← empty until phrasers
dataset/sentences.json     ← missing
pipeline/README.md
pipeline/workflow-phrases.js
pipeline/make_packs.py merge.py validate.py build_dicts.py
.pi/agents/phraser.md
docs/index.html            ← mock on GH Pages
```

## Mock / product notes for later

- Typeahead job, not four chips.
- Harder drill = assemble the line in order.
- Level inferred from sentence ids, not asked.
- Next: feed `sentences.json` into the mock.
