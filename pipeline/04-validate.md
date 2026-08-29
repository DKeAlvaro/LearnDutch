# 04 Validate

Run checks. Fix the JSON until they pass. Do not lower the count below 1000.

- `occupations.json`, `frames.json`, `sentences.json` parse as JSON.
- `len(sentences) == 1000`.
- Every `id` unique.
- Every `level` in `A0`,`A1`.
- Every `frame` id exists in frames.json.
- Every token in `parts` is either a function word (pipeline README list / frequency rank ≤ 80) or a `nl` in teach.json (allow *de*/*het*/*een* and infinitives from teach verbs).
- Nouns after *de*/*het* match teach `article` when the article is present.
- No empty `parts`, no English inside `parts`.
- Print a short report: counts by level, by tag, 10 sample lines.
