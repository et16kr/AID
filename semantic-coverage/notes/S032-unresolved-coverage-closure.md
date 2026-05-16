# S032 Unresolved Coverage Closure

## Requirement And Boundary

- Job: `S032`
- Scope: merge existing coverage-matrix evidence, fix any remaining source coverage issues where safe, and drive unresolved semantic differences to zero or explicit recheck risks.
- Required workflow: `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`.
- Final decision for this job: `COMPLETE`.

S032 is a closure job. It does not replace the direct Korean-source and English-target inspections performed by S003-S031. It validates that those matrices are structurally usable as a merged evidence set, that every mapped Korean source has at least one matrix row, and that no `missing`, `unverified`, or `recheck_required` rows remain after the source-audit and attachment/classification jobs.

This job did not run the `llm-reference` consolidation workflow and did not edit product source documents under `DOCK/`, `faq/`, `arch/`, or `FAQE/`. No `manifest.json` update was required because no English Markdown source page changed in S032.

## Required Reading And Preflight

Read before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- Existing coverage evidence under `semantic-coverage/matrices/` and `semantic-coverage/notes/`

The required handoff check was run before editing:

```bash
git status --porcelain --untracked-files=all -- . ":(exclude).codex-jobs" ":(exclude).codex-jobs/**"
```

Result: no output.

## Design Note

S032 does not change product documentation behavior, architecture, or source-document organization. It adds aggregate closure evidence:

- `semantic-coverage/matrices/S032-unresolved-coverage-closure.tsv`
- `semantic-coverage/notes/S032-unresolved-coverage-closure.md`
- an S032 closure section in `KO_EN_SEMANTIC_COVERAGE_REPORT.md`

The S032 matrix uses one aggregate row per prior matrix file. These rows are workflow-closure evidence, not new product semantic units. Product semantic-unit proof remains in S003-S031 matrices and notes.

## Aggregate Matrix Evidence

The merge validation covered 31 existing matrices, S001 through S031.

Summary:

- Prior matrix files checked: 31
- Prior matrix rows checked: 5,103
- Matrix header or row-shape errors: 0
- `missing` rows: 0
- `unverified` rows: 0
- `recheck_required` rows: 0
- Mapped Korean source rows in `semantic-coverage/doc-mapping.tsv`: 166
- Mapped Korean sources without any matrix row: 0
- Missing KO or EN paths in `semantic-coverage/doc-mapping.tsv`: 0

Merged status counts before adding the S032 closure matrix:

- `covered`: 4,665
- `added`: 70
- `not_applicable`: 290
- `source_limitation`: 78

S032 found no remaining source coverage issue requiring an English source edit.

## Closure Matrix

Matrix file: `semantic-coverage/matrices/S032-unresolved-coverage-closure.tsv`

Rows by unit type:

- `matrix_aggregate`: 31

Rows by coverage status:

- `covered`: 29
- `not_applicable`: 2
- `missing`: 0
- `unverified`: 0
- `recheck_required`: 0

The two `not_applicable` rows are S001 and S002 because those jobs intentionally created baseline and mapping scaffolds without product semantic-unit rows.

## Source Coverage Closure

The S032 merge check confirmed:

- S003-S018 and S020-S030 provide product semantic-unit evidence for the 166 Korean source files mapped in S002.
- S019 provides technical document attachment, legacy-label, source-link, and external-reference closure evidence.
- S031 provides FAQ attachment, legacy-label, source-link, export-artifact, and English-only classification closure evidence.
- Every `source_limitation` row has a recorded reason, such as a legacy `#` attachment label with no downloadable URL or a broken source export artifact.
- No prior matrix leaves a `missing`, `unverified`, or `recheck_required` coverage status.

The workflow-level decision remains `RECHECK_REQUIRED` until S033 source stabilization, S034 independent matrix challenge review, and S035 final decision are complete. S032 itself has no unresolved coverage blocker.

## Self-Review

Self-review checked that:

- The S032 matrix header matches the required TSV schema.
- Every S032 matrix row has exactly 15 TSV fields.
- Status values are workflow-approved.
- The aggregate merge validation covered S001-S031 and excluded S032 while calculating prior matrix totals.
- The aggregate merge validation did not hide unresolved rows: the unresolved-status grep over all current matrices still returns no matches.
- `semantic-coverage/doc-mapping.tsv` still contains 166 Korean source rows and every listed KO and EN path exists.
- No product Markdown file or `manifest.json` was edited in S032.

## Verification

Verification commands were run after edits.

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK/Home -type f -name '*.md' | wc -l` | Passed: 51 |
| `find faq/Home -type f -name '*.md' | wc -l` | Passed: 115 |
| `find arch/Home -type f -name '*.md' | wc -l` | Passed: 181 |
| `find FAQE/Home -type f -name '*.md' | wc -l` | Passed: 241 |
| Aggregate matrix validation over S001-S031 | Passed: 31 files, 5,103 rows, 0 shape/header errors, 0 unresolved rows |
| `semantic-coverage/doc-mapping.tsv` path validation | Passed: 166 mapping rows, 0 missing KO or EN paths |
| S032 matrix TSV shape/status validation | Passed: 31 rows, 15 fields per row; `covered` 29, `not_applicable` 2 |
| Full semantic matrix unresolved-status grep | Passed: expected-no-match grep exited 1 |
| Live source empty-link/export-artifact grep on `arch/Home FAQE/Home` | Passed: expected-no-match grep exited 1 |

The broader artifact grep including `semantic-coverage/` was inspected separately. It finds intentional historical evidence quotes in earlier notes/matrices, such as Korean-source macro export artifacts recorded by S021, so it is not used as a live-source failure for S032. The live source trees `arch/Home` and `FAQE/Home` passed the no-match check.

External HTTP availability was not tested; this closure job used path existence, source-link preservation evidence from S019/S031, and grep-based validation.

## Final Decision

`COMPLETE`: all merged matrix evidence is structurally valid, every mapped Korean source has matrix coverage, and there are zero `missing`, `unverified`, or `recheck_required` rows. No English source edit was required in S032.
