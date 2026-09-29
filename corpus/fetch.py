# SPDX-License-Identifier: AGPL-3.0-or-later
"""Download the pack's corpus from its GitHub release and verify it.

The corpus is too large for git and is published as release assets
(built by build_release.py): knowledgebase.sqlite, fieldmap.sqlite and
SHA256SUMS. This fetches the release pinned below with the GitHub CLI
(`gh`, authenticated: the repository is private) and refuses files whose
checksums do not match.

    python corpus/fetch.py
"""
from __future__ import annotations

import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = "Opening-Science/conjecture-pack-biophotons"
TAG = "corpus-v1"
FILES = ("knowledgebase.sqlite", "fieldmap.sqlite")


def main() -> None:
    if shutil.which("gh") is None:
        sys.exit("needs the GitHub CLI (gh), logged in with access to "
                 f"{REPO}; or download the {TAG} release assets into "
                 f"{HERE} by hand")
    subprocess.run(["gh", "release", "download", TAG, "-R", REPO,
                    "-D", str(HERE), "--clobber"], check=True)
    want = dict(reversed(line.split()) for line in
                (HERE / "SHA256SUMS").read_text().splitlines() if line)
    for f in FILES:
        got = hashlib.sha256((HERE / f).read_bytes()).hexdigest()
        if got != want[f]:
            (HERE / f).unlink()
            sys.exit(f"{f}: checksum mismatch, deleted")
        print(f"  {f}: ok ({(HERE / f).stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
