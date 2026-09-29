# SPDX-License-Identifier: AGPL-3.0-or-later
"""Download the pack's corpus from its GitHub release and verify it.

The corpus is too large for git and is published as release assets
(built by build_release.py): knowledgebase.sqlite, fieldmap.sqlite and
SHA256SUMS. This fetches the release pinned below with the GitHub CLI
(`gh`, logged in) and refuses files whose checksums do not match.

The expected checksums are pinned here, in git, not read from the
release's own SHA256SUMS: whoever could replace a release asset could
replace that file too, but not this one without a reviewed commit.

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
# printed by build_release.py; bump together with TAG
SHA256 = {
    "knowledgebase.sqlite":
        "ff62f01d92a372883dfc7f9f6bab27ee5c4d2e56f635f64151bbf8a5708a4306",
    "fieldmap.sqlite":
        "1717b82b326ad594a9cc0997ddbc6711c88cd381546f79f49d2773d979505363",
}


def main() -> None:
    if shutil.which("gh") is None:
        sys.exit("needs the GitHub CLI (gh), logged in; or download the "
                 f"{TAG} release assets of {REPO} into {HERE} by hand")
    pats = [a for f in SHA256 for a in ("-p", f)]
    subprocess.run(["gh", "release", "download", TAG, "-R", REPO, *pats,
                    "-D", str(HERE), "--clobber"], check=True)
    for f, want in SHA256.items():
        got = hashlib.sha256((HERE / f).read_bytes()).hexdigest()
        if got != want:
            (HERE / f).unlink()
            sys.exit(f"{f}: checksum mismatch, deleted")
        print(f"  {f}: ok ({(HERE / f).stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
