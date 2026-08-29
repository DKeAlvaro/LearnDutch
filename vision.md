# Learn Dutch

updated: 2026-08-29

A native app that packages a **curated Dutch phrase dataset** and plays it at the user. No lessons. No context. No thinking. Anki, one step further: you do not build a deck, rate cards, or study grammar. You open it and drill phrases.

Stukje was a book cut into pieces. This is not a book.

## Product

The product is the dataset. The app is a dumb player.

First open: **What do you do?** Type. Matches from a **fixed occupation list** (EN/ES aliases). You pick one. No four buttons. No “what level are you?”.

Drill: English prompt. Dutch is empty slots. You build it in order from word chips (legos). Wrong chip dies. Right chip snaps in. Next.

Phrases are frames × bricks. Each phrase has a **level id** (A0/A1/…). The app starts at A0 and climbs if you keep hitting; it does not ask.

No restaurant scene. No grammar note. If it needs an explanation, it is not in the dataset.

## Dataset

Lego: small frames with slots, bricks from a frequency list, cartesian product at **build** time. Only grammatical snaps. Occupation list is part of the dataset. See `sources.md` and `product.md`.

Shipped as JSON + baked TTS. The phone does not call an API and does not run a model.

## Shape

- One listing, one job: Dutch phrases.
- Reading/seeing is free. Hearing is a one-time IAP (Play Billing).
- Offline. Small UI.
- No accounts, streaks, SRS, notes, search, chat, scoring, or “type and hear”.

## Not

- A course, a textbook, or Duolingo.
- Stukje with Dummies inside.
- A DIY Anki deck (that is the user’s job in Anki; here the curation is done).
- A runtime ML toy.

If another language later: another app, another name.

How it looks, the loop, JSON, Android stack: `product.md`.
Mock (tap it): https://dkealvaro.github.io/LearnDutch/

## Where

`/root/LearnDutch` · `DKeAlvaro/LearnDutch`. Stukje stays a format prototype, not this product.
