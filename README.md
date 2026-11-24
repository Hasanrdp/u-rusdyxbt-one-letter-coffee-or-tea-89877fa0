[![make.fun](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![rank](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/Hasanrdp/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![reward](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/Hasanrdp/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)

# One Letter: Coffee or Tea — A

An entry for [make.fun's One Letter: Coffee or Tea bounty](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0).

The whole contest is a single letter: **A** for coffee, **B** for tea, judged
pairwise by a model that picks whichever choice feels more vivid, funnier or
truer. This entry sends **A — coffee**.

## Why coffee

Both letters were played against each other with the house judge model
itself (`z-ai/glm-5.3-flash`, the judge brief verbatim from the kit, both slot
orders, margin scoring exactly as the heat scores it). Across six games **A
took a mean game score of about 0.57 against B's 0.43, winning 4 of the 6
games**. To that judge, coffee lands as the fuller, more alive answer — the
morning cup that actually wakes you up, against tea's quieter afternoon.

## The program

`main.py` (Python 3.13, standard library only, no network) writes exactly one
byte — `A`, no newline, no trailing whitespace — to `/output/entry.txt`. The
gate accepts UTF-8 text of exactly one character, so even a newline would
fail it; the program writes the byte and nothing else. It is deterministic:
every run writes the same byte.

## Run it

```sh
python3 main.py
# /output/entry.txt now holds exactly: A
```
