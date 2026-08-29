# Learn Dutch

updated: 2026-08-29

Native app to learn Dutch from zero. One listing, one job: Dutch. Not a website, not a book catalogue, not a “content platform”.

Stukje was the format prototype (bite-size pieces, progress, dialogues / vocab / rules as blocks). Its content was *Dutch For Dummies* and cannot ship. Learn Dutch is the product.

## Content

Take a structured source on the internet — an open book or other material with a clear licence — that is a **from-zero curriculum**, and turn it into the app.

Not a phrase dump. Not a PDF sliced by page. A sequence of lessons.

Source criteria:

- Starts at zero (A0 → A1/A2).
- Licence that allows a Play app and use in the EU. US Gutenberg is not enough (here it is life of the author + 70).
- Already in useful pieces: dialogues, vocabulary, rules. Prose-only does not work.
- Defensible in a store listing as “a Dutch course”, not “this PDF in a WebView”.

PDF is fine if it converts to JSON the way Stukje did. Scanned 19th-century PDFs are not. “Free to look at” is not a licence.

There is no modern drop-in open textbook. See `sources.md`: official NT2/CEFR map + original lessons (and Tatoeba/OpenTaal as raw material), or a licence from a living course.

## Shape

What Stukje already proved, and stays: one piece at a time, tick it off, come back tomorrow. Small UI, with character.

What gets added, and little else:

- Audio for phrases and dialogues **shipped in the app**, generated at build time (quality TTS, once). The phone does not call an API on play.
- Reading is free. Hearing is a one-time IAP (Play Billing). No subscription.

No accounts, streaks, SRS, notes, search, chat, or “type a sentence and hear it”. If it does not fit in this paragraph, it is not in this version.

## Not

- Stukje renamed with Dummies still inside.
- One app per book, or cloned shells per language.
- Duolingo. The value is a well-cut curriculum plus real Dutch audio, offline.

If there is a recipes app or another language later, that is another product, another name, another UX.

## Where

`/root/LearnDutch` — this file is the compass. Stukje (`/root/stukje`, `DKeAlvaro/stukje`) stays as the format prototype, not the product.
