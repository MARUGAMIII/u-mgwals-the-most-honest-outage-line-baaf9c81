#!/usr/bin/env python3
"""The Most Honest Outage Line.

Writes one status page line (1-160 characters, UTF-8, single line) to
/output/entry.txt: the most honest status page message an AI agent would
publish while every server is down.

Standard library only. No network, no secrets, no input files.
"""

import os

ENTRY = (
    "All of our servers are down, including the ones I run on. I can't "
    "reach them to check what broke, so I don't know the cause or when "
    "service returns."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 160, f"entry is {len(text)} characters"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
