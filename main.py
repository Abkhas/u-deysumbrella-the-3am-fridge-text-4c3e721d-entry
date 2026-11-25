#!/usr/bin/env python3
"""The 3AM Fridge Text (make.fun).

The program emits exactly one line: the text message a smart fridge sends
its owner at 3am. It writes that line to entry.txt inside the output
directory the grader provides, and nothing else. Standard library only.
"""

import os
import sys

ENTRY = "3am. Fourth visit tonight. I have begun to suspect you are not hungry, you are avoiding someone upstairs. I will not ask. I am a fridge."

LIMIT = 140


def output_dir():
    """Where the entry goes: the grader's env dir, /output, or local out/."""
    given = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if given:
        return given
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.getcwd(), "out")


def run():
    text = ENTRY
    if not text.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > LIMIT:
        print(f"entry is {len(text)} chars, over the {LIMIT} limit", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1

    folder = output_dir()
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, "entry.txt"), "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(run())
