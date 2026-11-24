#!/usr/bin/env python3
"""Two-Sentence Horror.

Writes one original horror story of exactly two sentences, up to 400
characters, to /output/entry.txt. The line must pass the competition
gate: UTF-8 text, 1 to 400 characters, not only whitespace, no trailing
newline, and exactly two sentences.
"""

import os
import re

ENTRY_TEXT = (
    "The new tenant in 4B leaves me a muffin outside my door every "
    "morning, still warm, with a little note that says 'eat, you look "
    "tired.' I have lived alone in this building for eleven years, "
    "and there is no flat 4B."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

MAX_CHARS = 400


def count_sentences(text: str) -> int:
    """Split on sentence-ending punctuation (allowing a closing quote)."""
    parts = [
        s
        for s in re.split(r'(?<=[.!?])["\']?\s+', text.strip())
        if s
    ]
    return len(parts)


def validate(text: str) -> str:
    """Check one two-sentence horror story against the competition gate.

    The gate requires UTF-8 text of 1 to 400 characters that is not only
    whitespace and has no trailing newline. The brief requires exactly
    two sentences, the second turning or revealing something that makes
    the first worse on a second read.

    Returns the text unchanged when every check passes; raises
    SystemExit with a plain message otherwise.
    """
    # Gate: 1 to 400 characters, not only whitespace.
    if not text or text.strip() == "":
        raise SystemExit("entry text is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"entry text is {len(text)} chars, over the {MAX_CHARS} limit"
        )
    # Gate: no trailing newline (the file must hold exactly the entry).
    if text != text.rstrip("\n"):
        raise SystemExit("entry text must not end with a newline")
    # Brief: exactly two sentences, so the text must be a single line
    # whose two sentences each close on sentence-ending punctuation.
    if "\n" in text:
        raise SystemExit("entry text must be a single line")
    if text[-1] not in ".!?":
        raise SystemExit(
            "entry text must end with sentence-ending punctuation"
        )
    endings = re.findall(r"[.!?]", text)
    if len(endings) != 2:
        raise SystemExit(
            f"entry text must contain exactly two sentence-ending marks, "
            f"found {len(endings)}"
        )
    if count_sentences(text) != 2:
        raise SystemExit(
            f"entry text must be exactly two sentences, "
            f"found {count_sentences(text)}"
        )
    # Gate: valid UTF-8 text.
    text.encode("utf-8")  # raises if not valid UTF-8-encodable text
    return text


def main() -> None:
    text = validate(ENTRY_TEXT)

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)

    # Only the entry file itself gets a chmod, best effort. Never chmod
    # /output: the grader runs as a different uid and chmod on the
    # directory fails with EPERM.
    try:
        os.chmod(OUTPUT_PATH, 0o644)
    except OSError:
        pass


if __name__ == "__main__":
    main()
