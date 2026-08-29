# 02 Frames

Write `dataset/frames.json`. 40–60 patterns. These are the lego templates.

```json
{
  "id": "ik_wil_noun",
  "level": "A0",
  "tags": ["home", "out"],
  "parts": ["Ik", "wil", "{noun}"],
  "en": "I want {noun}."
}
```

Slots are `{noun}`, `{place}`, `{drink}`, `{food}`, `{time}`, `{thing}`, `{person}`, `{verb}` — only if you will fill them from `teach.json`.

- A0: ik wil, ik heb, ik ga naar, waar is, dit is mijn, ik ben, ik woon in.
- A1: ik werk tot, ik studeer, kun je …, hoe laat, ik moet naar.
- Mix je (informal). No long subordinates.
- `tags` = which occupations should see this frame.
