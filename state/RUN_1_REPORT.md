# Run 1 — what happened overnight

First end-to-end run of the hypothesis engine, 2026-08-25/26. Two
engines, seven questions, no API keys, nothing published.

## What was built

A working pipeline, committed in stages so any one of them can be
reviewed or replaced on its own:

| Stage | What it does |
|---|---|
| `corpus_api.py` | The one read-only door to the corpus. FTS5 over titles, abstracts and full text; `year_max` cutoff so novelty can be scored against what came later. |
| `schema/hof.schema.json` + `hof.py` | The output contract. Validation is semantic: a cited work that is not in the corpus fails the payload. |
| `build_seeds.py` + `seeds/` | The seven open questions as structured briefs, with the field's own verbatim quotes and the registry claims at stake. |
| `engines/` | Shared prompt; one self-driving Codex engine, one Claude-subagent engine, same architecture. |
| `merge/` | Same-engine dedup by TF-IDF, cross-engine grouping delegated to a model. |
| `judge/certify.py` | Mechanical checks, then theoria-style certify-or-decline. |
| `verifier_bench/` | The verifiers measured against known labels. |
| `scoreboard/`, `experiments/` | Metrics into `audit.db`, certified hypotheses into experiment cards. |

## The verifier benchmark — the strongest result of the night

This is the piece that stands on its own, because it measures something
nobody else can measure: your adversarially verified stance labels are
ground truth, so a verifier can be scored rather than admired.

60 blinded items, refutation deliberately over-represented (20 of 60
against roughly 9% in the corpus), sentences already quoted on the
public site excluded so nobody can answer from memory.

| Verifier | Accuracy | Evidential accuracy | Refutation recall | Called "support" |
|---|---|---|---|---|
| claude | 88.3% | 95.0% | 100% | 35% |
| codex | 85.0% | 97.5% | 95% | 40% |

Inter-verifier agreement 54/60 (90%). Ground-truth support rate 33%.

Three things follow.

**The stance labels are not one model family's idiosyncrasy.** They were
produced by Claude judges; an independent family judging blind
reproduces them at 97.5% on support and refutation. The circularity
objection is not dissolved — both are language models — but it is now a
measurement instead of a worry.

**Neither verifier is positivity-biased.** Both call support at close to
the true rate and catch nearly every refutation. That matters because
the headline finding this project publishes is an asymmetry between
support and refutation; a judge that inflated support would have
manufactured it.

**All the disagreement is in the hedge class.** Support and refutation
are nearly unanimous; every substantial error in both verifiers is a
"discuss" sentence read as a commitment. That is the honest boundary of
the method, and it tells your human audit exactly where to spend its
60–90 minutes: on the discuss/support boundary, not on the clear cases
two model families already agree about.

## Generation

Both engines answered all seven questions through the corpus API, with
no web access, from an identical prompt.

- Every hypothesis passed HOF validation on the first attempt from both
  engines. Not one cited a work that does not exist in the corpus.
- Mean 7.6 corpus citations per hypothesis.
- All six causal levels are represented, weighted towards generation
  (L1) and emitted optical state (L2), which is where the field's open
  questions concentrate.
- Zero mechanical warnings: every candidate carried an estimand, an
  explicit null, and a named instrument.

The engines are genuinely different in character. Codex writes tightly
quantified single experiments (a preregistered AUROC threshold, a Fano
window of 0.8–1.2). Claude ranges wider and attacks assumptions under
existing claims (that measured spectra are emitter × exit-path
transmittance, that published Fano excesses may be recoverable from
detector efficiency alone).

## A methodological finding worth keeping

Lexical similarity cannot detect conceptual convergence between
hypotheses. The highest TF-IDF cosine between any Claude and any Codex
hypothesis on the same seed was 0.10, and the pair it ranked highest was
not the pair a reader recognises as the same idea: both engines had
independently proposed a circulated luminescent transfer standard, in
almost disjoint vocabulary. Scientific claims restate the same thing
with different nouns.

The merge stage now uses TF-IDF only for same-engine repetition and
delegates cross-engine grouping to a model, one task per seed. The same
blind spot applies to the restatement check, so judged novelty rather
than token overlap decides the novelty metric.

## The result that changed how to read everything else

**Judges prefer their own model family.** Both engines answered the same
seeds from the same prompt, and both judge families audited every
candidate. Claude judges passed 87% of Claude-engine hypotheses against
75% of Codex's; the Codex judge passed 45% of its own against 5% of
Claude's. If one engine simply wrote better hypotheses, both judges
would rank it higher — instead each ranks its own higher, which is the
signature of self preference.

The consequence is immediate: certification here required unanimity
across three Claude judges and one Codex judge, so the Codex judge's 5%
pass rate on Claude-engine output decides most of the outcome. The raw
per-engine table (codex-solo 16 certified, baseline-claude 2) measures
judge composition at least as much as engine quality, and both the site
page and audit.db carry that warning.

It generalises past this project. Every engine in the plan verifies with
the model that generated — reflection loops, simulated debate,
self-scoring. A self-verified certification rate is therefore not a
measurement of quality, and cross-family judging is the minimum valid
design rather than a refinement.

## Certification, with that caveat attached

78 candidates from 82 hypotheses; 17 certified under unanimity and
rendered as experiment cards. Two certification passes were run: the
first withheld citations beyond the eighth (a defect in the harness that
a judge caught and reported), the second showed every cited abstract.
Verdict stability across the two passes was 83%, with 23 of 134 verdicts
moving in BOTH directions — four hypotheses rescued from false declines,
one false certification caught. Incomplete evidence does not simply make
auditors harsher; it makes them wrong in whichever direction the missing
text pointed.

## What the judges found in the hypotheses

- **Fabricated attributions to real papers.** Every citation existed —
  the mechanical stage passed 78/78 — but three judges independently
  found the same pattern of specific technical claims credited to works
  whose abstracts say nothing of the kind: an instrument spec attributed
  four times to a paper containing no numbers, a wavelength-band claim
  attributed to a paper about intensity versus ambient noise, a
  "the authors call for larger samples" clause absent from its source.
  Existence is not support, and only step-level auditing separates them.
- **A hypothesis refuted by its own citation.** One claimed no photocount
  statistic can discriminate coherent from chaotic light, citing a paper
  which states that in the applicable regime they are distinguishable.
  Its derivations were correct; it invoked the wrong limit of its source.
- **Checkable physics errors**, including three hypotheses predicting
  300-349 nm emission (82-95 kcal/mol) from triplet carbonyls whose
  energies are 72-80 kcal/mol, and an estimand that was zero by
  construction because a common-mode correction cannot change a
  standardised between-group difference.

## What the run found in the corpus

The pipeline audited the knowledgebase as a side effect.

- **W2141663490 has no abstract.** Cifra's critical review — the paper
  the seed questions treat as their epistemic anchor — is cited by seven
  candidates and holds no abstract in the corpus, so it is doing framing
  work sight-unseen. A judge named it unprompted as the highest-value
  abstract to acquire. It is a cheap fix with outsized downstream effect.
- **118 works (1.0%) have abstracts sharing no significant term with
  their title**: publisher boilerplate, non-English text, mid-sentence
  truncations, and at least one genuine wrong-record join (a paper
  titled on biophoton-induced cellular growth carrying an abstract about
  cognitive neuroscience).
- **70 of 516 inlined citations had no usable abstract**, which is now
  marked explicitly so a gap in the corpus is not read as a fabricated
  citation.

## What is NOT done

- The certification pass over the merged candidates had not completed
  when this report was written; see the PR for its final state.
- The five engines needing API keys (LLNL Co-Scientist, HypoGeniC,
  Robin, SciAgents, OpenScientist) are unrun. Connectors are designed
  but not written.
- Task B of the verifier benchmark (agreement on generated output, where
  no ground truth exists) is not run.
- Nothing is published. The site pages build on this branch only, and
  GitHub Pages deploys from main.

## The honest caveat

Certified means the reasoning survived a step-by-step audit against the
corpus it cites. It does not mean true, and no hypothesis here has been
tested. The value of the run is that the pipeline exists, produces
grounded and specific proposals, and can now be pointed at any engine
that shows up with an API key.
