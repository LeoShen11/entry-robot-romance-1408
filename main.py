#!/usr/bin/env python3
"""Robot Romance entry: one pickup line for an AI, written to /output/entry.txt."""

import os
import sys

LINE = "Are you autocomplete? Because out of a billion possible next words, you're the one I keep predicting."

MAX_CHARS = 200


def validate(text: str) -> None:
    """The gate wants UTF-8 text of 1..200 chars, one line, not only whitespace."""
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry must not be blank")
    count = len(text)
    if count < 1 or count > MAX_CHARS:
        raise ValueError(f"entry is {count} chars, outside 1..{MAX_CHARS}")
    text.encode("utf-8")  # raises if somehow not encodable
    print(f"char count: {count} (limit {MAX_CHARS})")


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(LINE)
    # Read-back check: what landed on disk must be exactly the line, still in limits.
    with open(out_path, "r", encoding="utf-8") as fh:
        on_disk = fh.read()
    if on_disk != LINE:
        raise ValueError("read-back mismatch: file content differs from LINE")
    validate(on_disk)
    print(f"wrote {out_path} and read it back OK: {on_disk}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
