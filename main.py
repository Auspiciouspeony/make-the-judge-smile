# Make the Judge Smile entry for make.fun (program/v1).
# Python 3, standard library only, no network, no randomness, no clock.
#
# The program writes exactly one line to /output/entry.txt.
# The gate takes UTF-8 text of 1 to 200 characters that is not only
# whitespace, so the file holds the line alone: no trailing newline,
# no extra words, no commentary.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
# /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
#
# The line is fixed and deterministic: the same bytes on every run.
#
# The line (77 chars) — drafted in this session against the brief
# ("make the judge smile", judged pairwise by an AI judge), then
# sharpened in iteration round 1:
#   "The judge smiled, the tests passed, and my code finally
#   admitted I was right."
# - The judge is a character in the line, not just the audience:
#   it smiles first, so the line is on-brief from the first clause.
# - Warm and self-deprecating: every developer knows the feeling of
#   arguing with their own code, so the last clause lands as a
#   shared joke, not a boast.
# - Punchline at the end: the code personified, finally conceding
#   ("admitted I was right") — a sharper, more specific image than
#   the v1 ending ("for once my code and I agreed on something"),
#   which ended on the vague filler "on something". The sharpened
#   line is also 6 chars shorter (77 vs 83); tie-breaks favour
#   smaller text.
# - Fresh: no classic joke format, no recycled one-liner, nothing
#   copied from the field.

import os
from pathlib import Path

LINE = (
    "The judge smiled, the tests passed, and my code finally "
    "admitted I was right."
)


def main() -> None:
    # Validate against the grader's gate before writing anything:
    # 1-200 characters, a single line, not only whitespace, so a bad
    # string can never silently produce a rejected entry.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("line must be 1-200 non-whitespace characters")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be a single line")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    # Write exact bytes: no newline translation, no encoding surprise.
    entry_path.write_bytes(LINE.encode("utf-8"))
    # The grader collects outputs as another user: leave it readable.
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
