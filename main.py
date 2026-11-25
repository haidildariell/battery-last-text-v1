#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes the battery's last text message to /output/entry.txt.
One line of plain text, well under the 200-character gate.
No network, no dependencies, fully deterministic.
"""

import os

ENTRY_TEXT = (
    "You plugged me in for 40 seconds, called it charging, "
    "and walked away. I hope your alarm clock dies the same way."
)

MAX_CHARS = 200


def validate(text):
    """Gate check, mirroring the competition rules: 1-200 chars, not blank."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry text must not be only whitespace")
    if len(text) != len(stripped) or "\n" in text:
        raise ValueError("entry text must be a single line")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry text must be 1-200 characters")
    return text


def write_entry(text, path="/output/entry.txt"):
    validated = validate(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(validated + "\n")


def main():
    write_entry(ENTRY_TEXT)


if __name__ == "__main__":
    main()
