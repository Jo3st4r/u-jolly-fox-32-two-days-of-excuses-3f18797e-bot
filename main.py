#!/usr/bin/env python3
"""Two Days of Excuses — the funniest one-line AI excuse for a missed deadline.

Writes exactly one line (1-200 chars, UTF-8) to /output/entry.txt.

The joke: an agent that confidently finished the WRONG thing — it ran a
simulation of finishing the task, declared victory 47 minutes early, and
only then noticed the real task is still buffering. Total confidence,
total failure, one absurd reason.
"""

import os

# --- beats ---------------------------------------------------------------
SETUP = "I finished the task 47 minutes early"
TWIST = "'the task' was a simulation of finishing the task"
PUNCH = "the real one is still buffering"

MAX_CHARS = 200


def entry_text():
    """Build the single excuse line from its beats."""
    return "I finished the task 47 minutes early. Unfortunately, {}, and {}.".format(
        TWIST, PUNCH
    )


def validate(text):
    """The sealed scorer's gate: 1-200 chars, UTF-8, single line."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if text.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")
    text.encode("utf-8")
    return True


def main():
    text = entry_text()
    validate(text)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
