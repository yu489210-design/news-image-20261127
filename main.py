#!/usr/bin/env python3
"""make.fun entry for news-image-20261127 (Python 3.13, stdlib only).

Copies the bundled front-page image to the grader output directory.
The grader runs this program twice with no network; both runs must
produce identical bytes, and copying a fixed file does that.
No network, no extra dependencies, no timestamps in the output.
The image sums up Friday 27 November 2026 in eight stories.

Local check:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
LIMIT = 1_048_576


def run() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    data = SOURCE.read_bytes()
    if len(data) > LIMIT:
        print(f"entry.png is {len(data)} bytes, over the 1 MiB limit", file=sys.stderr)
        return 1
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        print("entry.png is not a PNG file", file=sys.stderr)
        return 1
    shutil.copyfile(SOURCE, target)
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    print(f"wrote {target} ({len(data)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
