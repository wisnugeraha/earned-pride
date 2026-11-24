#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes exactly one line (1-240 characters) to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene, a small
person doing something hard, finally landing.
"""
import os


# The entry line: one concrete scene, a real small person, effort that
# finally lands — 1 to 240 characters.
LINE = (
    "After thirty-one winters of failed seedlings, the old fisherman's "
    "garden bloomed into forty pomegranates, and he offered the first one "
    "to the girl he'd taught to name the stars."
)


def line() -> str:
    """Return the entry line."""
    return LINE


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = line()
    if not 1 <= len(text) <= 240:
        raise ValueError(f"line is {len(text)} chars (must be 1-240)")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text + "\n")
    # Leave the file world-readable: the grader collects it as a different user.
    os.chmod(path, 0o644)
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
