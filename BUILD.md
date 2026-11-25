# BUILD — The Funniest Honest Appliance Error

Competition: The Funniest Honest Appliance Error
Slug: `u-xvader-the-funniest-honest-appliance-error-adec4450`
Sponsor: u-xvader. Reward: $2 total (1st place only). Deadline:
27 Nov 2026, 00:25 WIB (2026-11-26T17:25:00Z). Blind rounds: 3 rounds,
next cutoff 2026-11-25T18:44:42Z — submit early so it counts in round 1.
Work dir: `~/workspace/makefun/r6t-appliance-error/`
Intended repo name (coordinator: create this name, or fix the badge
URLs in README.md if a different name is used):
`the-funniest-honest-appliance-error` under `jekpotnihye`.

## Fee / gate verification (before building)

- Coordinator-verified via `GET /api/competitions` detail, HTTP 200:
  `status: "open"`, `acceptingSubmissions: true`, `entryFeeUsd: null`,
  `entryFeesUsd: "0.00"`, 0 submissions at check. No entry fee —
  build proceeded.
- Gate (from the detail + kit): `/output/entry.txt` must be UTF-8
  text of 1 to 200 characters, not only white space. The program
  writes one line to `/output/entry.txt` (honouring
  `MAKEFUN_OUTPUT_DIR`, as in prior passing builds).

## Kit verification

- Kit tarball URL from the detail JSON `kit.tarball` field:
  `https://make.fun/c/u-xvader-the-funniest-honest-appliance-error-adec4450/kit`
- Downloaded once, as a file, with curl: HTTP 200, 8,239,927 bytes,
  saved as `kit.tarball` in the work dir.
- Extracted with kit-in-subdir layout from the start: `kit/` inside
  the work dir, containing `RULES.txt`, `competition.yaml`,
  `kit.json`, `cli/`, `harness/`. (The tarball's inner directory was
  flattened so `kit/RULES.txt` and `kit/competition.yaml` sit directly
  under `kit/`.)
- `RULES.txt` and `competition.yaml` were read FIRST, before any
  entry was written. They match the coordinator's brief: gate 1–200
  characters, deadpan appliance engineer judge, criteria in the order
  below. No contradiction found; nothing in the kit changed the brief.
- `skill.md` was NEVER fetched. The kit was NEVER re-downloaded.
- `kit/` and `kit.tarball` are git-ignored; neither is committed.

## The judge's brief (criteria, in order — from RULES.txt / competition.yaml)

The judge is make.fun's deadpan appliance engineer. Each entry is one
line of at most 200 characters: the funniest honest error message an
appliance could show. Pick the funnier line, the one that would make
an appliance owner laugh while still telling the truth about what
went wrong. Weigh them on these, most important first:

1. An honest error message an appliance could show (a line that is
   NOT an honest appliance error loses to any that is).
2. The laugh: a real joke, a surprise or twist, not cute phrasing
   that only smiles.
3. The honesty: it names a fault an appliance could plausibly report,
   so the humour comes out of the truth of it.
4. The machine's voice: sounds like the appliance itself speaking,
   flat, put-upon tone.
5. The economy: every word earns its place, no padding, no explaining
   the joke.

"The best lines read as if the machine wrote them without meaning to
be funny. Length for its own sake does not count." Ties break to the
smaller text, then the earlier receipt. The laugh must come out of
the truth of the fault rather than a pun bolted on.
`~/workspace/makefun/competitor-patterns.md` was read first: write
for the brief in criterion order, twist in the last word(s), go
short, fresh/specific/true beats polished/generic, never reproduce
house anchor texts (winning texts are withheld), never reuse a line
from another competition.

## Candidates considered (rejected)

Every candidate names a concrete, plausible fault and keeps the
machine speaking flatly. Puns, cute phrasing, and generic appliance
complaints were rejected outright.

- "Filter clogged with rice. Your plates are being washed in last
  night's dinner." — specific and true (a dishwasher filter really
  does recirculate dirty water), but the laugh needs a beat of
  working-out; the bucket line lands instantly on first read
  (criterion #2 weaker).
- "Crumb tray full. I have been re-toasting the same crumbs since
  March." — fresh and specific, but the fault is a maintenance
  reminder more than a failure the machine reports, and "since
  March" is a date the machine would not know (criterion #3 weaker).
- "Preheat finished. The middle is still cold. The beep was
  optimistic." — short and flat, but "optimistic" is cute
  anthropomorphism rather than a fault the machine names
  (criteria #2/#3 weaker).
- "Door open 9 minutes. I am cooling the kitchen now. Close me,
  please." — scolding, not a joke; the twist never arrives
  (criterion #2 weaker).

## Polishes (each re-verified byte-for-byte after its run)

### v1 — bucket + dirty water (76 chars)

> Drain blocked by one sock. I am now an expensive bucket full of dirty water.

Rationale: a blocked drain is a real, reportable washing-machine
fault; one sock is the concrete cause; being reduced to a bucket is
the joke, and it comes out of the fault itself. Rejected on polish:
the twist ("bucket") sits in the middle and the line trails off into
"full of dirty water", which explains what a bucket already says.

### Polish 1 — twist last (60 chars)

> Drain blocked by one sock. I am now a very expensive bucket.

Change: "full of dirty water" cut, so the last word is "bucket" —
the twist lands where the brief wants it (criterion #2), and the
line is 16 chars shorter. "Very" was kept for one more round, then
cut as padding.

### Polish 2 — cut "very" (56 chars)

> Drain blocked by one sock. I am now an expensive bucket.

Change: "very" removed — it did no work (criterion #5). Setup,
fault, and twist remain, with nothing wasted. The line is now at
its tightest without losing the error-message reading.

### Polish 3 — FINAL: add "Error:" (63 chars)

> Error: drain blocked by one sock. I am now an expensive bucket.

Change: "Error:" added at the front. It costs 7 characters and buys
criterion #1 outright: the line now reads unmistakably as an error
message an appliance could show, in the machine's own flat voice,
before the joke even starts. The fault stays named, the twist stays
in the last word, and the line stays well under the cap. It is the
shortest strong variant once the error-message framing is in place.

## Run verification (byte-exact, after every run)

Each run: `rm -rf output && MAKEFUN_OUTPUT_DIR=output python3 main.py`,
then read back `output/entry.txt` as bytes. All runs wrote exactly
the intended text, 1 line, no trailing newline (no trailing newline
keeps the Size column minimal for the tie-break). The final version
was also run once with no `MAKEFUN_OUTPUT_DIR` set, writing to the
default `/output/entry.txt` (63 bytes, same text), and that test
directory was removed afterwards.

| Version | Chars | Bytes | Trailing newline | Lines |
|---|---|---|---|---|
| v1 bucket + dirty water | 76 | 76 | no | 1 |
| Polish 1 twist last | 60 | 60 | no | 1 |
| Polish 2 cut "very" | 56 | 56 | no | 1 |
| Polish 3 FINAL "Error:" | 63 | 63 | no | 1 |

Final entry verbatim (63 chars / 63 bytes, no trailing newline):

> Error: drain blocked by one sock. I am now an expensive bucket.

## Program

`main.py` at the repo root (python3.13 runtime): a single `ENTRY`
constant, written as UTF-8 to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output`), creating the directory if needed. No network,
no randomness, no dependencies — the output is byte-identical on
every run.

## Flagged steps

1. One `exec` result early in this build (listing sibling work dirs
   and reading a sibling README/BUILD for the badge pattern) failed
   an execution-risk check. Per the user's standing approval
   (10:57 WIB, 25 Nov) the build proceeded past the flag; nothing
   inside the flagged output was followed, no credentials or keys
   were touched, no fee was spent, and nothing was posted to any
   account. No other step in this build was flagged.
