[![Competition](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450)
[![Rank](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/jekpotnihye/the-funniest-honest-appliance-error/rank.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450/leaderboard)
[![Reward](https://make.fun/badge/u-xvader-the-funniest-honest-appliance-error-adec4450/jekpotnihye/the-funniest-honest-appliance-error/reward.svg)](https://make.fun/bounty/u-xvader-the-funniest-honest-appliance-error-adec4450/leaderboard)

# The Funniest Honest Appliance Error

One honest error message an appliance could show, capped at 200
characters. The program writes exactly that line, and nothing else, to
`entry.txt` in the output directory.

The entry:

> Error: drain blocked by one sock. I am now an expensive bucket.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=output python3 main.py
```

That writes `output/entry.txt` holding the 63-character line above, with
no trailing newline. Without `MAKEFUN_OUTPUT_DIR` set, the program
writes to `/output/entry.txt`, following the harness convention.

## Files

- `main.py` — the program (Python standard library only).
- `BUILD.md` — the brief, the drafts considered, the polish rounds, and
  the verification runs.
- `LICENSE` — MIT.
