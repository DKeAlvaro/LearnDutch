# Phrase pipeline

updated: 2026-08-29

Mix **deterministic packs** with **phraser subagents**. One parent Pi must not write the 1000 sentences.

Full continue notes: `CONTINUE.md`.

## Deterministic

- `data/frequency.json` / `data/teach.json` — published sources, already built.
- `dataset/occupations.json` / `dataset/frames.json` — shared contract.
- `dataset/packs/s01.json` … `s24.json` — `make_packs.py`. Each pack is a closed bag of lemmas + frame ids + theme + tags + level + `n`.

## Intelligence

24 `phraser` children (`.pi/agents/phraser.md`). Each reads **one pack**, writes `dataset/shards/sXX.json` with `n` spoken sentences using **only** those words.

Then `worker` merge: `pipeline/merge.py` + `pipeline/validate.py` → `dataset/sentences.json` (1000).

## Run

Parent:

```
subagent({ workflowScriptPath: "pipeline/workflow-phrases.js", cwd: "/root/LearnDutch" })
```

Cap live children (~5) on this 1 GB VPS. 24 shards still run; they queue.

Do not dump dictionaries to stdout. Do not invent teach words.
