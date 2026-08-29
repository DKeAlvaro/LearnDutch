# Phrase pipeline

updated: 2026-08-29

Pi runs this. Human already built the two dictionaries. You write occupations, frames, then **1000 sentences**.

## Dictionaries (do not edit, do not invent)

| File | What | Source |
|---|---|---|
| `data/frequency.json` | Top 5000 Dutch wordforms by zipf | wordfreq `nl` (CC BY-SA 4.0) |
| `data/teach.json` | 800 nouns + verbs + adjectives | those ranks ∩ UD content UPOS (Alpino + LassySmall, CC BY-SA 4.0) |

Frequency is glue: *de, van, ik, op, niet*. Teach is chicha: *huis, vrouw, water, auto, school*.

Homographs exist (*meer, wil*). Prefer the concrete sense or skip.

## Order

1. `pipeline/01-occupations.md` → `dataset/occupations.json`
2. `pipeline/02-frames.md` → `dataset/frames.json`
3. `pipeline/03-phrases.md` → `dataset/sentences.json` (**1000** rows)
4. `pipeline/04-validate.md` → fix until it passes

Schema reminder: `product.md` (occupations, frames, sentences). Audio field may be `null` for now.

## Rules

- Every content lemma in a sentence must be in `teach.json` (or a closed function word from frequency ranks 1–80: ik, je, hij, ze, we, het, de, een, van, in, op, te, en, is, zijn, heb, hebt, heeft, wil, naar, met, voor, als, dat, die, dit, niet, geen, er, waar, hoe, wat).
- `parts` is the Dutch sentence split on spaces. No punctuation except `?` glued to the last word.
- `en` is natural English, same meaning.
- `level` is `A0` or `A1` on **each sentence**. About 700 A0, 300 A1.
- `tags` ⊂ occupation tags you defined (student, work, home, out, health, …).
- Short. Spoken. 2026 Dutch. No textbook names, no copyright lines.
- Combinations must be grammatical (*de*/*het* from teach `article`).
- Do not call APIs. Write files with the write/bash tools.
