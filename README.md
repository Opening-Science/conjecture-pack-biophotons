# Conjecture pack: biophotons

The first domain pack for **Conjecture: the Open Science Foundation
hypothesis hub** ([Opening-Science/conjecture](https://github.com/Opening-Science/conjecture)).
It hydrates the hub with one field: ultra-weak photon emission (UPE,
"biophotons") from living systems.

The hub is field-agnostic code: engines, judges, merge, scoreboard. This
pack is everything that makes it about biophotons: the corpus, the
field's open questions, the prompt framing, the claim register, and the
history of every run so far.

## What is in it

| Path | What it is |
|---|---|
| `pack.yaml` | The pack manifest the hub reads: corpus paths, questions and entry queries, prompt framing, causal levels, measurement areas, where outputs and state go. |
| `questions/open_research_questions.md` | The seven questions the field says it cannot answer, each stated in the literature's own words with sources. |
| `corpus/` | `fetch.py` downloads the corpus from this repository's release; `build_release.py` is how maintainers build it. |
| `state/` | Run state: seeds, engine runs, merge clusters, judge chunks and verdicts, `audit.db`, `scoreboard.json`, the verifier bench, and `RUN_1_REPORT.md`. |
| `outputs/` | Rendered results: the engine page, experiment cards, the claim inventory, open-question statements, the blinded stance audit. |

### The questions

1. What actually generates the photons, and why is the UV part still unexplained?
2. Is UPE coherent, and can photocount statistics ever decide?
3. Byproduct or signal? The functional-role question.
4. Does the brain's UPE mean anything, and can it be measured from outside the head?
5. The metrology hole: no calibration, no absolute units, no comparability.
6. Can UPE become a clinical biomarker?
7. Imaging: from counting to pictures.

### The corpus

18,357 works: the mapped field (18,355 works from OpenAlex) plus two
curated metrology references. The release contains metadata and
abstracts, the claim register (`hypotheses_v2`) with its verified
evidence, statements mined from full texts (short verbatim sentences
with page numbers), and citation edges.

It does **not** contain full-text bodies. They were mined in the
maintainers' workspace from papers that cannot be redistributed. Engines
therefore search titles and abstracts here, not full text. Every work
cited in the pack's runs is present, so every citation still resolves.

### Run 1

Two engines with the same architecture (single agent + corpus tools) on
two model families, over all seven questions. They produced 82
hypotheses; after merging, 78 candidates, audited certify-or-decline by
Claude and Codex judges:

| Engine | Candidates | Certified | Novel and certified |
|---|---|---|---|
| `codex-solo` | 40 | 16 | 15 |
| `baseline-claude` | 42 | 2 | 2 |

Certified means *the reasoning survived audit*, not *true*: every
hypothesis here is a proposal for an experiment. See
`state/RUN_1_REPORT.md` and `outputs/hypothesis_engine.md`.

## Using it

```bash
git clone https://github.com/Opening-Science/conjecture
git clone https://github.com/Opening-Science/conjecture-pack-biophotons
cd conjecture-pack-biophotons && python corpus/fetch.py && cd ..

cd conjecture
pip install -r requirements.txt
export CONJECTURE_PACK=../conjecture-pack-biophotons/pack.yaml
python -m unittest discover tests          # hub tests against this pack
python run_engine.py --list
python corpus_api.py search "delayed luminescence" --limit 5
```

`fetch.py` needs the GitHub CLI (`gh`), logged in with access to this
repository.

Rerunning `build_seeds.py` against the release corpus gives slightly
different entry-point snippets than the committed seeds, which were
built against the full-text corpus. The committed seeds are what run 1
was asked, so they stay as they are.

## Licence

The pack's own content (questions, claim register and curation, runs,
verdicts, outputs, code) is dedicated to the public domain under CC0
1.0; see `LICENSE`. Abstracts and metadata come from OpenAlex (CC0).
Statements and evidence sentences are short verbatim excerpts, quoted
with attribution to the work and page they come from; their copyright
stays with the original publishers.
