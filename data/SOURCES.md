# Dictionary sources

- `frequency.json` — wordfreq `top_n_list('nl', 5000)` + zipf. Data CC BY-SA 4.0. Speer, Robyn. https://github.com/rspeer/wordfreq
- `teach.json` — those ranks whose dominant UPOS in UD_Dutch-Alpino + UD_Dutch-LassySmall train is NOUN, VERB, or ADJ. Article from UD Gender. Treebanks CC BY-SA 4.0.

Rebuild: `.venv/bin/python pipeline/build_dicts.py` (needs the UD train conllu files in `/tmp/ud-nl`).
