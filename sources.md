# Dataset sources

updated: 2026-08-29

The app ships a curated phrase dataset, not a curriculum. Raw material below. The deck itself is original (frames + fills generated at build).

## Frequency

- **wordfreq** (Dutch): ranks from subtitles, wiki, etc. Data **CC BY-SA 4.0**. Credit in About. Do not vendor the raw SUBTLEX-NL Excel (research / NC-SA traces); wordfreq is the allowed path.
- **OpenTaal** word list: **CC BY 3.0** / BSD. Valid lemmas, not ranks. https://github.com/OpenTaal/opentaal-wordlist

Local files: `data/frequency.json` (glue + everything) and `data/teach.json` (nouns/verbs/adjs with chicha). Rebuild: `pipeline/build_dicts.py`.

## Attested sentences

- **Tatoeba** Dutch: default **CC BY 2.0 FR**, commercial with attribution. Mine short patterns (`Ik wil …`, `Waar is …`). Do not ship the Tatoeba dump as the product. Skip their audio unless the clip is CC-BY/CC0; we TTS.

https://tatoeba.org

## Build (not on device)

1. Take top-N lemmas by frequency, tagged (noun / verb / place / drink / …) plus `de`/`het`.
2. Keep a small set of frames with one slot.
3. Fill only matching types. Drop junk (`Ik wil de democratie` at the start).
4. Stamp each snap with a level (`A0` / `A1` / …). Never ask the user their level; start at A0.
5. Keep a closed **occupation list** (labels + EN/ES aliases + tags) for the typeahead.
6. TTS every shipped sentence once. JSON + mp3 in the app.

A model may propose frames or rank “sounds natural” **at build**. The APK stays a box of files.

## Out

Textbooks, Wikibooks, DLI, Boom, Delft, Naar Nederland, NT2Lex (NC-SA). This product does not wrap a course.
