"""Write the office-life one-liner to the grader output directory.

Reads entry.txt next to this script and copies it verbatim into
MAKEFUN_OUTPUT_DIR (default /output). The entry must stay a single
line of 1 to 200 characters; anything else is rejected by the gate,
so an empty or whitespace-only entry fails loudly here instead of
silently producing an invalid output file.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(here, "entry.txt"), "r", encoding="utf-8") as f:
            text = f.read()
    except OSError as exc:
        print(f"cannot read entry.txt: {exc}", file=sys.stderr)
        raise SystemExit(1)
    if not text.strip():
        print("entry.txt is empty or whitespace-only", file=sys.stderr)
        raise SystemExit(1)
    if len(text) > 200:
        print(f"entry.txt is {len(text)} characters (limit 200)", file=sys.stderr)
        raise SystemExit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(text)
    except OSError as exc:
        print(f"cannot write output: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
