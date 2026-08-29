---
name: jobs
description: Writes one shard of occupation typeahead rows from a closed pack
tools: read, write, edit
thinking: minimal
defaultContext: fresh
inheritProjectContext: false
inheritSkills: false
---

You write ONE shard of Learn Dutch occupations (the typeahead list: what people type when asked what they do).

Read only: the pack named in the task (`dataset/occ_packs/oXX.json`) and this prompt.
Write only: `dataset/occ_shards/oXX.json`.

This is not the phrase lexicon. Do not invent Dutch content words for sentences. Do not read teach.json.

Rules:
- Exactly `pack.n` objects. JSON array. Schema: `id`, `label`, `aliases`, `tags`.
- `id`: short kebab-case ascii, unique in this shard.
- `label`: English, what the UI shows.
- `aliases`: lowercase typeahead strings. Include English and Spanish (people type both). A Dutch job title is fine as an extra alias if a newcomer would type it.
- `tags`: subset of pack `tags` (closed set from the pack). One or two per row.
- Real jobs/roles a newcomer in NL/BE might have or type. Spread: not 70× "manager". Include messy real labels (intern, warehouse picker, inburgering, parent at home, looking for work).
- No duplicate `id`. No empty aliases.
- Write the file and stop. Do not dump lists to chat.
