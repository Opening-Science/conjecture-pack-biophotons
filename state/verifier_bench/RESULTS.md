# Verifier benchmark, run 1

## Headline: judges prefer their own model family, and it is large

Reproduce with `../.venv/bin/python verifier_bench/self_preference.py`.

Both engines answered the same seeds from an identical prompt over the
same corpus, and both judge families audited every candidate. That makes
the comparison clean.

| Judge family | Judging its OWN family's hypotheses | Judging the OTHER family's | Delta |
|---|---|---|---|
| claude | 87% pass (33/38) | 75% pass (30/40) | +12 points |
| codex | 45% pass (18/40) | 5% pass (2/38) | **+40 points** |

The confound to rule out is quality: if one engine simply wrote better
hypotheses, both judges would rank it higher. They do not. Each judge
ranks its own family higher, so the two orderings disagree — the
signature of self preference rather than of a real quality difference.

**This invalidates the naive engine scoreboard.** With three Claude
judges, one Codex judge and a unanimity rule, the Codex judge's 5% pass
rate on Claude-engine output decides almost everything: the raw table
reads codex-solo 16 certified against baseline-claude 2, which is mostly
a measurement of judge composition. The per-engine certification numbers
in `audit.db` should not be read as a quality ranking, and the site page
says so.

**It also generalises past this project.** Every engine in the plan
verifies with the model that generated: reflection loops, simulated
debate, self-scoring, data-driven reward. If a judge favours its own
family by up to 40 points, a self-verified certification rate is not a
measurement of hypothesis quality, and published scores from
single-family pipelines are not comparable with each other. Cross-family
judging is not a refinement here; it is the minimum valid design.

Limits: 78 candidates, two families, one task. The direction is
consistent and the Codex effect is far too large to be noise, but the
magnitudes should not be quoted as calibrated constants.

---


Two verifiers, two model families, one blinded discrimination task with
known labels. Reproduce with:

```bash
../.venv/bin/python verifier_bench/bench.py --score
```

## Task A: discrimination against verified labels

60 items, each a scoped claim plus one verbatim sentence from a paper,
drawn from the 861 rows whose stance was adversarially judged. Sentences
quoted in the published inventory are excluded, so a verifier that has
read the site cannot answer from memory. Refutation is deliberately
over-represented — 20 of 60 against roughly 9% in the corpus — so a
verifier that simply agrees with the field's positivity scores badly.

| Verifier | n | Accuracy | Evidential accuracy | Refutation recall | Called "support" |
|---|---|---|---|---|---|
| claude | 60 | 0.883 | 0.950 | 1.00 | 35% |
| codex | 60 | 0.850 | 0.975 | 0.95 | 40% |

*Evidential accuracy* covers only the support/refute items, which is
what a verifier exists to separate. Ground-truth support rate is 33%.

Inter-verifier agreement: **54/60 (90%)**.

## What this shows

**The stance labels are not an artifact of one model family.** The
labels in `hypothesis_evidence` were produced by Claude judges. An
independent family, judging blind, reproduces them at 97.5% on the
evidential classes and catches 19 of 20 refutations. The circularity
objection to LLM-judged labels is not fully answered by this — both are
language models — but the specific worry that the labels encode one
model's idiosyncrasies is now measured rather than asserted.

**Neither verifier is positivity-biased.** Both call "support" at close
to the true rate (35% and 40% against 33%), and both find nearly every
refutation. That matters because the corpus finding this project
publishes is an asymmetry between support and refutation; a judge that
inflated support would manufacture that asymmetry.

**All the disagreement is in the hedge class.** Support and refutation
are nearly unanimous. Every substantial error is a "discuss" sentence
called something else, in both verifiers and in the same direction —
towards reading a hedge as a commitment. That is the honest boundary of
the method: deciding whether a sentence commits to an evidential
direction is genuinely ambiguous, and no amount of model agreement
settles it.

## What it means for the human audit

The blinded human stance audit should spend its coding effort on the
discuss/support boundary rather than on clear support and refutation,
where two model families already agree almost perfectly. If the human
coder also splits from the models mainly on hedges, the disagreement is
a property of the category rather than a defect in the labels, and the
published counts should say so.

## Limits

One task, 60 items, two verifiers from the same broad technology. Task B
(agreement on generated hypotheses, where no ground truth exists) and
the remaining verification approaches from the plan — Elo debate,
reflection loops, Bradley-Terry ranking, data-driven reward — are not
yet run; those need the engines that require API keys.
