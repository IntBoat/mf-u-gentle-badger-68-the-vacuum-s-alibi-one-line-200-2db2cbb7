#!/usr/bin/env python3
"""The Vacuum's Alibi: One Line, 200 Characters (make.fun).

Writes the entry -- one line in which a robot vacuum explains why it
missed a spot -- to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = "Log 04:12: the spot under the sofa was not missed; it was classified as a protected habitat for a dust bunny I have grown fond of."

# Gate: the entry must be 1-200 characters of UTF-8 text, no trailing newline.
assert 1 <= len(TEXT) <= 200 and TEXT == TEXT.strip()


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
