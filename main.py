#!/usr/bin/env python3
"""One-Line Laugh Sprint entry.

Writes a single original one-liner (at most 200 characters) about everyday
life to <MAKEFUN_OUTPUT_DIR>/entry.txt. The line is a fixed constant, so
every run produces byte-identical output.
"""

import os

LINE = (
    "I bought a standing desk to sit less, and now I just stand here "
    "scrolling my phone like a very healthy statue."
)


def main() -> None:
    if len(LINE) > 200:
        raise ValueError(
            f"One-liner exceeds the 200-character limit: {len(LINE)} chars"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
