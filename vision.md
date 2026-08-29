# Learn Dutch

updated: 2026-08-29

A native app that packages a **curated Dutch phrase dataset** and plays it at the user. No lessons. No context. No thinking. Anki, one step further: you do not build a deck, rate cards, or study grammar. You open it and drill phrases.

Stukje was a book cut into pieces. This is not a book.

## Product

The product is the dataset. The app is a dumb player.

One phrase on screen. English is the prompt, Dutch has a hole, chips are the answer. After a hit, swap the slot to hear variants. Next. Frequency order, not chapters.

No restaurant scene. No “this is the accusative”. No can-do list. If it needs an explanation, it is not in the dataset.

## Dataset

Frames with slots, filled from a frequency list (wordfreq / OpenTaal), attested against real Dutch (Tatoeba as raw material, not as the deck). Combinations generated at **build** time. Only grammatical, frequent, short. See `sources.md`.

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
