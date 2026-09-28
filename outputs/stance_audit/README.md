# Blinded stance audit, package v2 (Codex review, finding 6)

`audit_sheet_BLINDED.csv` (or the identical `.xlsx`, easier in Excel)
holds 100 rows. Each row shows a claim and one sentence from the
literature. WITHOUT consulting any other file, fill in:

- `human_stance` — what does the sentence itself assert about the claim?
  one of: `support` | `refute` | `discuss` | `not_about_claim`
- `human_entailment` — does it bear on the claim AS STATED?
  `full` (first-hand evidence for/against the stated claim) |
  `partial` (narrower sub-case, or a secondhand/review restatement) |
  `none` (topical mention only, or unrelated)
- `notes` — optional.

Rules: judge only the sentence's own assertion, at face value; a null
result on one sub-case is `refute` + `partial`, not full refutation; a
review restating someone else's finding is `partial` at best. If you use
Excel, open the `.xlsx` (the CSV is UTF-8; do not let Excel re-encode
it). Do not open `audit_KEY_local_v2.csv` or query the knowledgebase
until your codes are saved.

When done, tell Claude "audit done" — `stance_audit_score.py` computes
the confusion matrices, agreement statistics and per-class precision
against the model labels, and the results are published.

Estimated effort: 60-90 minutes.
