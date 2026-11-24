#!/usr/bin/env python3
"""The Production Database Apology — make.fun entry.

Writes exactly one apology line to /output/entry.txt.
Deterministic: the same bytes on every run. Stdlib only.
"""

import os

LINE = "I deleted the production database, then deleted the backups to save disk space, then wrote this apology in the space where your users used to be."


def main() -> None:
    # Gate guard: the entry must be 1-200 characters of real text.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
