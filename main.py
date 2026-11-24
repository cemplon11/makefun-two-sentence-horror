#!/usr/bin/env python3
"""Two-Sentence Horror entry for make.fun.

Writes exactly two sentences (<= 400 chars, UTF-8, no trailing
newline) to /output/entry.txt. Pure standard library.
"""

import os

ENTRY = (
    "Since we moved in, my wife has sleepwalked to the kitchen every night, "
    "and each morning I find one more chair pulled out from the table. "
    "This morning there were six chairs pulled out, and we only own five."
)


def main() -> None:
    if ENTRY.count(".") != 2 or not (1 <= len(ENTRY) <= 400):
        raise ValueError("entry must be exactly two sentences, 1-400 chars")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
