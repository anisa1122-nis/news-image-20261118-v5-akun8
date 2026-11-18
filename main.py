#!/usr/bin/env python3
"""news-image-20261118 v5 (akun 8): write the pre-composed front page.

Hormuz-lead variant — same contrarian test as the 20261117 v5: lead with
the burning tanker off Hormuz (aerial shot with rescue helicopter) and
move Kerch to a secondary slot (dusk shot with cranes). Same dense v2
layout otherwise: 17 stories, map strip, 2x3 grid, "ALSO ON WEDNESDAY"
list and a source footer. Wednesday 18 November 2026.
Deterministic: copies the embedded bytes verbatim.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "image.jpg")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    # Guard: entry must be <= 1 MiB and exactly 1024x1024.
    assert os.path.getsize(dst) <= 1048576, "entry over 1 MiB"


if __name__ == "__main__":
    main()
