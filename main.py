#!/usr/bin/env python3
"""Two-line explanation of a toaster, for a 10-year-old.

Line 1 explains the everyday thing with one vivid analogy.
Line 2 says why the analogy works: what it maps and what it leaves out.

Writes exactly two lines of text to /output/entry.txt.
Deterministic: stdlib only, no input, no randomness, no time.
"""

import os

LINE_1 = (
    "A toaster is a tiny sunbed where bread lies down for a tan "
    "and pops up, brown and toasty, when its time is up."
)

LINE_2 = (
    "The sunbed maps heat slowly browning the bread, but it leaves out "
    "that bread never picks its tan \u2014 a spring, not the bread, "
    "decides when to pop up."
)

ENTRY = LINE_1 + "\n" + LINE_2 + "\n"


def main() -> None:
    lines = ENTRY.splitlines()
    assert len(lines) == 2, "entry must be exactly two lines"
    assert 1 <= len(ENTRY) <= 400, "entry must be 1-400 characters"
    assert all(line.strip() for line in lines), "no blank lines"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
