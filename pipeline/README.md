# Phrase pipeline

updated: 2026-08-29

Subagents build the large JSON. Python only slices dictionaries and merges shards. One parent Pi must not write occupations, frames, or 1000 sentences.

## Order

1. Dictionaries already in `data/` (`build_dicts.py`).
2. Occupations: `make_occ_packs.py` → 10 `jobs` children → `merge_occupations.py`.
3. Frames: `make_frame_packs.py` → 12 `framer` children → `merge_frames.py`.
4. Phrases: `make_packs.py` slices teach + frames → 24 `phraser` children → `merge.py` + `validate.py`.

## Run

Occupations (first):

```
subagent({ workflowScriptPath: "pipeline/workflow-occupations.js", cwd: "/root/LearnDutch", async: false })
```

Then frames: `pipeline/workflow-frames.js`. Then phrases: `pipeline/workflow-phrases.js`.

One live child on this 1 GB VPS. Do not dump dictionaries. Do not invent teach words.
