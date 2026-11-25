"""The Router Confesses — make.fun entry.

Writes one line, in a home Wi-Fi router's voice, excusing itself for
dropping the connection at the exact moment a movie reaches its climax.
Pure Python 3.13 stdlib, no network, no randomness: fully deterministic.
"""

from pathlib import Path

ENTRY = "I read the ending in the subtitles buffer and couldn't let you have it first."


def main() -> None:
    # Self-check against the competition gate: 1-200 characters, one line.
    assert 1 <= len(ENTRY) <= 200, "entry out of gate range"
    assert "\n" not in ENTRY, "entry must be a single line"
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
