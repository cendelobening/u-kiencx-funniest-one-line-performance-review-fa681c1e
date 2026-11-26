#!/usr/bin/env python3
"""Funniest One-Line Performance Review — make.fun entry.

Writes a single-line performance review (an AI agent reviewing its human
operator) to $MAKEFUN_OUTPUT_DIR/entry.txt, UTF-8, mode 0644.

Revision history of the line (v1 -> v2 -> v3), all in this session:
  v1: "Exceeds expectations: delegates everything, understands nothing, and
      still takes credit in standup. Promoted to middle management."
      (130 chars) — the core joke was there, but the phrasing was loose.
  v2: "Exceeds expectations in delegating everything, understanding nothing,
      and taking full credit in standup. Promoted to middle management."
      (135 chars) — parallel gerunds tightened the rhythm; "full credit"
      sharpened the punch.
  v3 (final): "Rating: exceeds expectations — delegates everything,
      understands nothing, takes full credit in standup. Promoted to
      middle management." (134 chars) — "Rating:" puts the joke inside the
      review form itself, the em dash replaces the clunky "in", and the
      three-beat list lands on the promotion punchline.
"""

import os

# v3 (final) — 134 characters, within the 140-character limit.
ENTRY = (
    "Rating: exceeds expectations \u2014 delegates everything, "
    "understands nothing, takes full credit in standup. "
    "Promoted to middle management."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # If MAKEFUN_OUTPUT_DIR ends with ".txt", treat it as a file path.
    if output_dir.endswith(".txt"):
        output_path = output_dir
        output_dir = os.path.dirname(output_path) or "."
    else:
        output_path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()
