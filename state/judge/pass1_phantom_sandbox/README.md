# theoria pass 1 — archived: agents were told they were in a container that did not exist

These six verdicts were produced with `--no-docker` while the config still
carried upstream's `_preamble` describing a Debian 13 container with
`/workspace`, `/opt/venv` and pre-installed tooling. No container was
running. Effect, measured on C001: 52 LLM calls, **zero tool calls** —
solver, formalizer and every per-step judge worked by pure reasoning while
believing in an execution environment they never tried to touch (had they
tried, they would have discovered it missing).

The answers may nonetheless be right — the errors found in C001–C003 and
C009 are checkable by hand — but "recompute every number from scratch"
was not performed the way the harness claims, so the pass is archived
rather than reported. Pass 2 runs with an honest preamble describing the
real host and instructing verification by executed python3.
