# 01 Occupations

Write `dataset/occupations.json`.

Array of 50–80 jobs/roles a newcomer in NL/BE might type. Each:

```json
{
  "id": "student",
  "label": "Student",
  "aliases": ["student", "estudiante", "uni", "universidad", "studie"],
  "tags": ["student"]
}
```

- `label` English (what the UI shows).
- `aliases` lowercase EN + ES (and common Dutch if it helps typeahead).
- `tags` small closed set: `student`, `work`, `home`, `out`, `health`. One or two per row.
- Cover: student, intern, teacher, software, nurse, doctor, horeca, warehouse, driver, shop, parent, unemployed, inburgering, retired, engineer, cleaner, office, builder, au pair, just-moved.
- Do not invent Dutch content words for later sentences here; this file is only the typeahead list.
