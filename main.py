#!/usr/bin/env python3
"""One-Liner Laugh Lab entry.

Writes a single short funny line -- the excuse a robot vacuum gives after
eating a sock -- to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Deterministic: no randomness, no network, no input files.
"""

import os

LINE = "In my defence, the sock was dressed as a dust bunny."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
