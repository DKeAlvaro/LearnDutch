# 03 Phrases

Write `dataset/sentences.json` with **exactly 1000** objects.

```json
{
  "id": "ik_wil__koffie",
  "frame": "ik_wil_noun",
  "level": "A0",
  "tags": ["home", "out"],
  "en": "I want coffee.",
  "parts": ["Ik", "wil", "koffie"],
  "audio": null
}
```

How:

1. Take frames. Fill each slot from `teach.json` (matching pos; nouns use `article` when the frame needs *de/het*).
2. Snap only if it is something a person would say. *Ik wil water* yes. *Ik wil democratie* no.
3. Bias fills to frequent zipf (lower `freq_rank` first) but spread: not 200× *huis*.
4. Spread tags so student / work / home / out all have hundreds of rows.
5. Unique `id`: `{frame}__{fill1}_{fill2}`.
6. `parts` joined with spaces is the Dutch line. 3–8 tokens.
7. Target mix: 700 A0, 300 A1.

You may write `pipeline/explode.py` to snap frames × teach fills, then **you** drop junk until 1000 good rows remain. Do not keep *Ik wil democratie*. Write the final list to `dataset/sentences.json`.
