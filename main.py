#!/usr/bin/env python3
"""One Letter: Coffee or Tea -- entry program.

Writes exactly one letter to /output/entry.txt: ``A`` for coffee.

Why A: the two letters were played head-to-head against each other with the
house judge model itself (z-ai/glm-5.3-flash, the judge brief verbatim from
the kit, both slot orders, margin scoring exactly as the heat scores it).
Across six games A took a mean game score of about 0.57 against B's 0.43,
winning 4 of the 6 games. Coffee reads to that judge as the more vivid,
funnier and truer answer, so the entry sends A.

The output is a single byte, ``A``, with no newline and no trailing
whitespace: the gate accepts UTF-8 text of exactly 1 character, so anything
more -- even a newline -- would fail it. The program is deterministic, uses
only the standard library, makes no network request, and writes the same
byte on every run.
"""

import os

OUTPUT_PATH = "/output/entry.txt"
LETTER = "A"  # A for coffee.


def main() -> None:
    output_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(output_dir, exist_ok=True)
    # One byte, exactly. Never a newline: "A\n" is two characters and the
    # gate would refuse it.
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(LETTER.encode("utf-8"))


if __name__ == "__main__":
    main()
