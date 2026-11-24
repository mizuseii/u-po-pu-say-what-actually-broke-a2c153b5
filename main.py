#!/usr/bin/env python3
"""Say What Actually Broke entry.

Writes the muted-mic error line to /output/entry.txt.
Deterministic: no network, no randomness, no time dependence.
"""

from pathlib import Path

LINE = "You're on mute. You've been talking for four minutes. Unmute and start over — everyone just nodded along."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    """Write the one-liner to /output/entry.txt with no trailing newline."""
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE, "entry must be a single line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
