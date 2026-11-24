#!/usr/bin/env python3
"""Two Days of Excuses — one-line AI excuse for a missed deadline.

Writes the entry to /output/entry.txt (the competition's gate reads it)
and prints it with its character count.
"""

from pathlib import Path

LINE = (
    "I handed your deadline to a sub-agent, who handed it to another "
    "sub-agent \u2014 the chain now holds its own standup meeting, and "
    "your deadline is still in the backlog."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"entry is {len(LINE)} chars, must be 1-200")
    if "\n" in LINE:
        raise SystemExit("entry must be a single line")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    print(f"{LINE} ({len(LINE)} chars)")


if __name__ == "__main__":
    main()
