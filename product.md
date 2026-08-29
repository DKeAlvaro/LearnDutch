# Product

updated: 2026-08-29

How it looks, how you use it, the dataset, the Android stack. Identity is still `vision.md`.

Interactive mock: https://dkealvaro.github.io/LearnDutch/

## How the user uses it

Daily use is building sentences. Setup is typing who you are, once.

### First open

**What do you do?** One line. Options are **already in the dataset**. Type `stu` → Student. Type `enfer` → Nurse. English and Spanish aliases both match. You must pick a stored job; you cannot invent one.

That job is a tag weight, not an account. Tap the name at the top to type again.

Do **not** ask for level.

### Every other time

1. English is the prompt. Dutch is empty slots, one per word.
2. Chips are the words of that sentence plus a few decoys, shuffled. Tap the next word. Wrong: the chip dies, stay. Right: it snaps into the line.
3. Full line → Next and speaker unlock. Speaker is IAP. No spoiler before you finish.
4. Next. The pool is phrases at or below the current cap, biased to the job’s tags.

Level lives on **each phrase** (`A0`, `A1`, …). Cap starts at A0. A short streak of hits raises it. Failures reset the streak, not the whole app.

### What they never do

Rate Again/Good/Easy. Type the Dutch (chips only). Speak into a mic. Read a grammar note. Pick a CEFR from a menu.

## How it looks

One column, phone. Big Dutch, small English, slot chips, speaker, Next. Paper background, one accent colour. No tabs, no streak flame, no XP.

The mock is type-who-you-are plus the builder.

## Dataset format

Occupations are data, not UI hardcode. Bricks snap into frames at build (legos). Each resulting phrase has a level.

`occupations.json` — what the typeahead searches. Aliases in EN and ES.

```json
{
  "id": "student",
  "label": "Student",
  "aliases": ["student", "estudiante", "uni", "universidad"],
  "tags": ["student"]
}
```

`bricks.json` — lego pieces (lemma + article + tags + level).

`frames.json` — a pattern of parts, some of them slots:

```json
{
  "id": "ik_wil",
  "level": "A0",
  "tags": ["home", "out"],
  "parts": ["Ik", "wil", "{drink}"],
  "en": "I want {drink}."
}
```

`sentences.json` — cartesian snaps that are legal. This is the player deck. **Each row has `level`.**

```json
{
  "id": "ik_wil__koffie",
  "frame": "ik_wil",
  "level": "A0",
  "tags": ["home", "out"],
  "en": "I want coffee.",
  "parts": ["Ik", "wil", "koffie"],
  "audio": "audio/ik_wil__koffie.mp3"
}
```

Build explodes frames × bricks. TTS every shipped `parts` line. The phone only walks this list. Job tags bias which rows you see; `level` is the gate, not a question.

v1: ~40 frames, ~300 bricks, a few thousand snaps. Start the cap at A0.

Player state: `{ jobId, cap: "A0", seen: {} }`.

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
