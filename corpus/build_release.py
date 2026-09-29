# SPDX-License-Identifier: AGPL-3.0-or-later
"""Build the pack's distributable corpus from the full local knowledgebase.

Maintainers only: it needs the full knowledgebase and field map, which
live in the maintainers' workspace. Everyone else gets its output with
corpus/fetch.py.

The local knowledgebase holds full-text bodies of 4,533 works, much of
it publisher text that cannot be redistributed. The release keeps the
line the project's public site already draws (decided 2026-08-24): metadata, abstracts (OpenAlex,
CC0), the claim register and its verified evidence, and short verbatim
statements with their page, but no full-text bodies, no PDFs and no
local file names.

What changes for an engine: search runs over titles and abstracts
instead of titles, abstracts and bodies, so snippets come from abstracts.
Every work stays in the corpus, so every citation in the pack's runs
still resolves.

    python corpus/build_release.py --kb FULL_KB --fieldmap FULL_FIELDMAP
                                               # -> corpus/release/

Writes knowledgebase.sqlite, fieldmap.sqlite (citation edges only) and
SHA256SUMS; publish them as assets of a GitHub release of the pack repo,
and corpus/fetch.py downloads and verifies them.
"""
from __future__ import annotations

import argparse
import hashlib
import sqlite3
from pathlib import Path

HERE = Path(__file__).resolve().parent

# works columns that describe the local full-text holding, not the work
LOCAL_ONLY = {"fulltext_file", "n_pages", "n_chars", "fulltext_quality",
              "lang_guess"}
# copied as they are
TABLES = ["hypotheses", "hypotheses_v2", "hypothesis_evidence",
          "hypothesis_evidence_map", "hypothesis_worklevel", "authors",
          "work_authors"]


def columns(db: sqlite3.Connection, table: str, schema: str = "src") -> list:
    return [r[1] for r in db.execute(f"PRAGMA {schema}.table_info({table})")]


def build_kb(src: Path, out: Path) -> None:
    out.unlink(missing_ok=True)
    db = sqlite3.connect(f"file:{out}", uri=True)
    db.execute(f"ATTACH DATABASE 'file:{src}?mode=ro' AS src")
    keep = [c for c in columns(db, "works") if c not in LOCAL_ONLY]
    cols = ", ".join(f'"{c}"' for c in keep)
    db.execute(f"CREATE TABLE works AS SELECT {cols} FROM src.works")
    for t in TABLES:
        db.execute(f"CREATE TABLE {t} AS SELECT * FROM src.{t}")
    # statements: short verbatim sentences with page, minus local file name
    st = [c for c in columns(db, "statements") if c != "file"]
    db.execute("CREATE TABLE statements AS SELECT "
               + ", ".join(st) + " FROM src.statements")
    db.execute("ALTER TABLE statements ADD COLUMN file TEXT")
    # the search index the hub queries, with the body column left empty
    db.execute("CREATE VIRTUAL TABLE works_fts USING fts5("
               "work_id UNINDEXED, title, abstract, body, "
               "tokenize='porter unicode61')")
    db.execute("INSERT INTO works_fts (work_id, title, abstract, body) "
               "SELECT work_id, title, abstract, '' FROM src.works_fts")
    for sql in ("CREATE INDEX idx_w_id ON works(work_id)",
                "CREATE INDEX idx_st_w ON statements(work_id)"):
        db.execute(sql)
    db.commit()
    db.execute("DETACH DATABASE src")
    db.execute("VACUUM")
    db.close()


def build_fieldmap(src: Path, out: Path) -> None:
    out.unlink(missing_ok=True)
    db = sqlite3.connect(f"file:{out}", uri=True)
    db.execute(f"ATTACH DATABASE 'file:{src}?mode=ro' AS src")
    db.execute("CREATE TABLE citation_edges AS "
               "SELECT src_work_id, dst_work_id FROM src.citation_edges")
    db.execute("CREATE INDEX idx_edge_src ON citation_edges(src_work_id)")
    db.execute("CREATE INDEX idx_edge_dst ON citation_edges(dst_work_id)")
    db.commit()
    db.execute("DETACH DATABASE src")
    db.execute("VACUUM")
    db.close()


def check(out: Path) -> None:
    db = sqlite3.connect(out / "knowledgebase.sqlite")
    n_body = db.execute("SELECT COUNT(*) FROM works_fts "
                        "WHERE length(body) > 0").fetchone()[0]
    n = db.execute("SELECT COUNT(*) FROM works").fetchone()[0]
    assert n_body == 0, f"{n_body} full-text bodies leaked"
    leaked = LOCAL_ONLY & set(r[1] for r in
                              db.execute("PRAGMA table_info(works)"))
    assert not leaked, f"local columns leaked: {leaked}"
    assert not db.execute("SELECT COUNT(*) FROM statements "
                          "WHERE file IS NOT NULL").fetchone()[0]
    print(f"  {n} works, no full-text bodies, no local file names")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--kb", type=Path, required=True,
                    help="the full knowledgebase.sqlite")
    ap.add_argument("--fieldmap", type=Path, required=True,
                    help="the full fieldmap.sqlite")
    ap.add_argument("--out", type=Path, default=HERE / "release")
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)
    build_kb(a.kb.resolve(), a.out / "knowledgebase.sqlite")
    build_fieldmap(a.fieldmap.resolve(), a.out / "fieldmap.sqlite")
    check(a.out)
    sums = []
    for f in ("knowledgebase.sqlite", "fieldmap.sqlite"):
        h = hashlib.sha256((a.out / f).read_bytes()).hexdigest()
        size = (a.out / f).stat().st_size
        sums.append(f"{h}  {f}")
        print(f"  {f}: {size / 1e6:.1f} MB  sha256 {h[:16]}")
    (a.out / "SHA256SUMS").write_text("\n".join(sums) + "\n",
                                      encoding="utf-8")
    print("pin these in corpus/fetch.py (SHA256), with the new TAG:")
    for line in sums:
        h, f = line.split()
        print(f'    "{f}":\n        "{h}",')


if __name__ == "__main__":
    main()
