#!/usr/bin/env python3
"""Describe Your Ex in One Word.

Writes exactly one word -- the verdict on an ex -- to entry.txt.
The word is "knockoff": a cheap imitation of a real partner.
"""

import os

WORD = "knockoff"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # Never delete the output directory itself (it may be a mount point);
    # just make sure it exists and write the file inside it.
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
