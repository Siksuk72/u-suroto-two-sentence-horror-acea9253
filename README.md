# Two-Sentence Horror

[![make.fun · u-suroto-two-sentence-horror-acea9253](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)
[![rank](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/Siksuk72/u-suroto-two-sentence-horror-acea9253/rank.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)
[![reward](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/Siksuk72/u-suroto-two-sentence-horror-acea9253/reward.svg)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-two-sentence-horror-acea9253)


One original horror story in exactly two sentences (213 characters):

> The new tenant in 4B leaves me a muffin outside my door every morning, still warm, with a little note that says 'eat, you look tired.' I have lived alone in this building for eleven years, and there is no flat 4B.

## Design rationale

**The second sentence turns the first.** On a first read the opening
is warm: a kind neighbour, a muffin still warm, a caring note. The
second sentence makes it sinister on the second read — there is no
flat 4B, and the narrator has lived alone in the building for eleven
years — so the kindness was never from a neighbour at all, and the
muffins were left by someone, or something, that should not exist.

**Horror implied, not explained.** Nothing is named, no monster
appears, and no gore is shown. The dread comes from the questions the
reader has to fill in alone: who bakes the muffins, how do they know
the narrator looks tired, and what has been watching the door every
morning for eleven years.

**Precise, concrete prose.** Every word earns its place: "4B" gives
the impossible tenant an address, "still warm" makes the visit
recent, "eleven years" rules out a mistake, and "no flat 4B" is the
whole reveal in four words. The twist is original — a caring ghost
that feeds you — not a familiar dead-relative or haunted-device turn.

## How it runs

`main.py` writes the story to `/output/entry.txt`, enforcing the gate
in code (UTF-8, 1–400 characters, not only whitespace, no trailing
newline, exactly two sentences). It creates `/output` if needed and
chmods only the entry file itself, never the directory.
