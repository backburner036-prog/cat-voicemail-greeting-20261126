#!/usr/bin/env python3
"""Funniest Cat Voicemail Greeting entry: write one cat voicemail line to /output/entry.txt.

The greeting is fixed text -- deterministic, no randomness, no clock, no I/O
beyond the single output file. It runs in well under 60 seconds.
"""

import os

# The greeting text is fixed on purpose: the entry must be byte-identical on every run.
# D2 was chosen for TEXT: it won the proxy judge in both directions (D1 vs D2 and D2 vs D1).
TEXT = "Hi, it's Mochi. I'm ignoring you from inside the box. Leave a message — I'll sit on it until it's warm."


# Entry point: gate the text, then write it plus a newline and verify the round-trip.
def main() -> None:
    assert 1 <= len(TEXT) <= 200, "entry text out of range"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    with open(path, encoding="utf-8") as f:
        assert f.read() == TEXT + "\n", "round-trip mismatch"


if __name__ == "__main__":
    main()
