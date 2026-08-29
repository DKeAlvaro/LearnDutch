# 02 Frames

Do **not** write `frames.json` yourself. A short handwritten template list starves the phrasers.

Glue: `python3 pipeline/make_frame_packs.py` copies `frequency.json` (rank ≤ 200) to `dataset/glue.json` and writes 12 packs (level, tags, slots, `n`).
Then `pipeline/workflow-frames.js`: 12 `framer` children, each writes `dataset/frame_shards/fXX.json`.
Merge: `python3 pipeline/merge_frames.py` → `dataset/frames.json` (≥200). Drops rows whose literals are not in glue.

Schema:

```json
{
  "id": "ik_wil_noun",
  "level": "A0",
  "tags": ["home", "out"],
  "parts": ["Ik", "wil", "{noun}"],
  "en": "I want {noun}."
}
```

Slots only `{noun}`, `{adj}`, `{verb}` (teach.json POS). Literals only glue. Fill happens later in phrase packs.
