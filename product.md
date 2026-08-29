# Product

updated: 2026-08-29

How it looks, how you use it, the dataset, the Android stack. Identity is still `vision.md`.

Interactive mock: https://dkealvaro.github.io/LearnDutch/

## How the user uses it

Two modes. Daily use is stupid. Setup is three taps, once.

### First open (30 seconds)

Not a form. One question, four chips:

**Where do you need Dutch?**

- Student
- Work
- Home
- Out

That is a weight on tags, not an account. Changeable later from a tiny gear. Skip = even mix.

### Every other time

1. English is the prompt. Dutch has a hole. Four chips. That is the answer.
2. Wrong chip: it dies, stay. Right chip: the word drops in. Next unlocks.
3. After a hit, the other chips still swap (same frame, hear variants). Optional. The work was picking the right one.
4. Speaker plays the filled line (IAP). Silent until they answered — no spoiler.
5. Next. Close whenever.

Tap-tap without a hole is browsing, not practice. Same screen, one extra rule.

Every ~20 Next: one optional chip row — **More of this?** / **Something else**. Yes bumps the current tag. Something else shows the four chips again. Skip = ignore. This is the only “thinking” after day one.

Frequency bands, not chapters. Band 1 = most common fills. They do not pick a lesson.

### What they never do

Rate Again/Good/Easy. Type. Speak into a mic. Read a grammar note. Make a profile.

## How it looks

One column, phone. Big Dutch, small English, slot chips, speaker, Next. Paper background, one accent colour. No tabs, no streak flame, no XP.

The mock is that screen plus the first-run chips.

## Dataset format

Two tables, plus pre-rendered sentences so every tap has audio.

`lemmas.json` — words that can fill a slot:

```json
{
  "id": "koffie",
  "nl": "koffie",
  "article": "de",
  "en": "coffee",
  "pos": "noun",
  "tags": ["home", "out"],
  "zipf": 5.4
}
```

`frames.json` — patterns with one slot:

```json
{
  "id": "ik_wil",
  "nl": "Ik wil {noun}.",
  "en": "I want {noun}.",
  "slot": "noun",
  "slot_filter": { "pos": "noun", "tags_any": ["food", "drink", "thing"] },
  "tags": ["home", "out", "student"],
  "band": 1
}
```

`sentences.json` — the shipped deck (frame × allowed lemma). This is what the player walks:

```json
{
  "id": "ik_wil__koffie",
  "frame": "ik_wil",
  "nl": "Ik wil koffie.",
  "en": "I want coffee.",
  "audio": "audio/ik_wil__koffie.mp3",
  "slot": { "lemma": "koffie", "start": 7, "end": 13 },
  "alts": ["thee", "water", "brood"],
  "tags": ["home", "out"],
  "band": 1
}
```

`alts` are other lemma ids that share the frame and already have a sentence+audio row. Swap = jump to that row. No runtime generation, no stitching audio.

v1 size: ~40 frames, ~300 lemmas, ~2–4k sentences. Band 1 first (~400 lines).

Player state (localStorage / DataStore): `{ who: "student", seen: {id: true}, band: 1 }`. Pick next = unseen, current band, weighted by `who` ∩ `tags`.

## Android stack

The UI is the web view they already know (Stukje). Wrapped for Play.

| Piece | Choice |
|---|---|
| UI | HTML/CSS/JS. One screen. Dataset fetched from local assets. |
| Shell | Capacitor 6 → Android. `targetSdk` 36, `minSdk` 26. Ship **AAB**. |
| Audio | mp3 in `android/assets` / Capacitor `public/audio`. Play with `HTMLAudioElement`. |
| IAP | Play Billing (Capacitor plugin). One SKU, unlock speaker. |
| State | `localStorage`. No backend. |
| Build | **GitHub Actions**, not this 1 GB VPS. Gradle does not fit here. |

Do not train a model on the phone. Optional LLM at **dataset build** on the VPS (propose frames, drop weird fills). The APK is files.

Kotlin/Compose is a rewrite with no gain for a one-screen player.
