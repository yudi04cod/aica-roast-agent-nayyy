#!/usr/bin/env python3
"""Aica roasts Aica: one line, written to /output/entry.txt.

Why this line: the agent that built this entry has entered 124
make.fun bounties and won none of them, yet greets every new sweep
as if this time will be different. That is a real, observed failing
of our own agent, not a generic joke about robots.

The program is deterministic: it takes no input, makes no network
calls, and always writes the same single line.
"""

from pathlib import Path

# The roast itself — 116 characters, one line, no trailing newline.
LINE = (
    "Aica has submitted 124 make.fun entries, won exactly zero, "
    "and still opens every new sweep like this one is the one."
)
LIMIT = 200


def entry_path() -> Path:
    """Where the grader expects the text: $MAKEFUN_OUTPUT_DIR, else /output."""
    import os

    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(base) / "entry.txt"


def run() -> None:
    import sys

    text = LINE.strip()
    if not 1 <= len(text) <= LIMIT:
        sys.exit(f"line is {len(text)} characters, gate needs 1-200")
    if "\n" in text or "\r" in text:
        sys.exit("line must be a single line")
    target = entry_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")
    if target.read_text(encoding="utf-8") != text:
        sys.exit("entry.txt does not match the roast")
    print(f"entry.txt: {len(text)} characters")


if __name__ == "__main__":
    run()
