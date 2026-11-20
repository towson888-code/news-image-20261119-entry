#!/usr/bin/env python3
"""Entry point: write the 19 November 2026 front page to /output/entry.png.

The image is drawn by the build script and shipped in this repository as
entry.png; this program copies it to the output directory. Standard
library only, deterministic, no network, no clock.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
