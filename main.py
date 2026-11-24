#!/usr/bin/env python3
"""Cat Reviews Its Human - one-star review entry.

Writes a single-line, deadpan one-star review from a house cat about
its human to /output/entry.txt (under 200 characters, one line).
"""
import os
from pathlib import Path

REVIEW = (
    "One star. He refills my bowl only after I scream at the same empty bowl "
    "for twenty minutes, then acts shocked when his charger tastes like dinner."
)


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    text = REVIEW.strip()
    assert 1 <= len(text) < 200, len(text)
    assert "\n" not in text
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
