#!/usr/bin/env python3
"""Invent a Word We Need — coins one new English word and defines it.

The program writes a single line to /output/entry.txt: the invented word
"draftloop" plus its one-line definition (102 characters, within the 140
character gate).
"""

import os

ENTRY = "Draftloop (n.): typing, deleting and retyping the same message until the moment to send it has passed."

# The gate: /output/entry.txt must be UTF-8 text of 1 to 140 characters,
# not only white space. Refuse to write anything that would fail it.
assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
assert ENTRY.strip(), "entry must not be only white space"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
