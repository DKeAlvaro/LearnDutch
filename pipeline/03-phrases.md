# 03 Phrases

Do **not** write `sentences.json` yourself. Do not explode the whole lexicon in one agent.

Packs are already sliced from `teach.json` (`pipeline/make_packs.py`). Launch 24 `phraser` children via `pipeline/workflow-phrases.js`. Each child reads one pack and writes `dataset/shards/sXX.json`. Then `pipeline/merge.py` + `pipeline/validate.py` → `dataset/sentences.json` (1000).

Schema of each row:

```json
{
  "id": "ik_wil__koffie",
  "frame": "ik_wil",
  "level": "A0",
  "tags": ["home"],
  "en": "I want coffee.",
  "parts": ["Ik", "wil", "koffie"],
  "audio": null
}
```
