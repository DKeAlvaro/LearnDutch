# 01 Occupations

Do **not** write `occupations.json` yourself. One agent listing jobs is a short handwritten list.

Packs: `python3 pipeline/make_occ_packs.py` (tags + `n` only).
Then `pipeline/workflow-occupations.js`: 10 `jobs` children, each writes `dataset/occ_shards/oXX.json`.
Merge: `python3 pipeline/merge_occupations.py` → `dataset/occupations.json` (≥400).

Schema of each row:

```json
{
  "id": "student",
  "label": "Student",
  "aliases": ["student", "estudiante", "uni", "universidad"],
  "tags": ["student"]
}
```

Tags closed: `student`, `work`, `home`, `out`, `health`. Typeahead is EN/ES. This file is not the Dutch phrase lexicon.
