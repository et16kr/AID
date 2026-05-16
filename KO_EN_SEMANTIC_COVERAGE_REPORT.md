# KO to EN Semantic Coverage Report

Report date: 2026-05-16

Workspace: `/home/et16/AID`

Current workflow decision: `RECHECK_REQUIRED`

Reason: S001 establishes the audit method and baseline only. The Korean source semantic-unit audits, closure, stabilization, independent challenge review, and final decision jobs are still pending.

## Authority And Boundary

Korean documents under `DOCK/Home` and `faq/Home` are the authority for this workflow. Korean-core English documents under `arch/Home` and `FAQE/Home` are the update targets.

This workflow does not delete, move, or rewrite Korean source documents. It also does not delete or move original English source documents. If an English source document is missing Korean-authoritative content, the scoped audit job must update the English source first and update `manifest.json` metadata for changed Markdown pages.

The `.codex-jobs/llm-reference-consolidation/` workflow is preserved but must not run until the semantic coverage and source-stabilization gates are complete.

## Baseline Repository State

S001 baseline was captured on branch `combine` at pre-edit HEAD `131b19c`.

Before S001 edits, there were no uncommitted project files outside the workflow area. The only tracked modification was `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv`, where the workflow runtime had marked S001 as `Progress`.

Baseline document counts:

| Area | Count |
| --- | ---: |
| `DOCK/Home` Markdown files | 51 |
| `faq/Home` Markdown files | 115 |
| `arch/Home` Markdown files | 181 |
| `FAQE/Home` Markdown files | 241 |

S001 did not edit product documentation under `DOCK/`, `faq/`, `arch/`, or `FAQE/`, and did not update `manifest.json`.

## Relationship To Previous Work

Previous reports remain useful orientation:

- `KO_EN_DOC_REVIEW_REPORT.md` records first-pass mapping, attachment, link, and scoped content fixes.
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md` records second-pass scoped checks, final validation, source classification, and remaining risks.
- `LLM_REFERENCE_REVIEW_PLAN.md` records source-readiness gates, source classes, consolidation rules, and multilingual terminology preservation rules.

Those reports are not sufficient proof for this workflow. Every scoped source audit job must inspect its assigned Korean source and English target files directly and must create semantic-unit matrix evidence.

## Evidence Structure

S001 created the baseline evidence structure:

- `semantic-coverage/README.md`
- `semantic-coverage/matrices/S001-audit-method-and-baseline.tsv`
- `semantic-coverage/notes/S001-audit-method-and-baseline.md`

S002 will create or update `semantic-coverage/doc-mapping.tsv`. Later jobs will add per-scope matrices and notes under `semantic-coverage/matrices/` and `semantic-coverage/notes/`.

## Semantic Unit Method

Audit by semantic unit, not visual line number. A semantic unit is the smallest independently meaningful content item, including headings, paragraphs, bullet or numbered steps, table rows, command blocks, SQL blocks, configuration items, warnings, notes, version conditions, limitations, error-code resolution items, attachments, and external references.

Each Korean semantic unit must be represented in the target English source, added to the English source, recorded as intentionally not applicable, recorded as a source limitation, or marked for recheck with a concrete blocker.

Matrix rows use this exact TSV header:

```text
job_id	ko_path	ko_start_line	ko_end_line	ko_unit_id	unit_type	ko_excerpt	required_identifiers	en_target_paths	en_start_line	coverage_status	action	evidence_excerpt	risk	notes
```

Allowed `coverage_status` values are `covered`, `added`, `not_applicable`, `source_limitation`, `missing`, `unverified`, and `recheck_required`.

Successful scoped jobs must not leave `missing` or `unverified` rows. `recheck_required` rows are allowed only when a concrete blocker is recorded and the workflow-level decision remains `RECHECK_REQUIRED`.

## Duplicate Source Ownership

Duplicate Korean source ownership follows `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`.

- `DOCK/Home/20. Altibase 설정 파일 가이드__13437165.md`: primary owner S003.
- `DOCK/Home/26. Altibase 기본적인 장애대응 절차__13435879.md`: primary owner S005.
- `DOCK/Home/43. Altibase STARTUP _ STOP 과정의 이해__13434993.md`: primary owner S005.

Later jobs that reference these sources add only topic-specific cross-reference rows and name the primary owner in `notes`.

## Decision Criteria

The final decision must be exactly one of:

- `COMPLETE`: all in-scope Korean semantic units are `covered`, `added`, `not_applicable`, or `source_limitation`; no `missing`, `unverified`, or `recheck_required` rows remain; English source fixes and `manifest.json` metadata are complete; URL-backed document attachments are preserved; validation passes.
- `RECHECK_REQUIRED`: any semantic unit remains uncertain, disputed, technically unsafe to translate, or blocked by insufficient source evidence.

S001 sets the current workflow decision to `RECHECK_REQUIRED` because source semantic-unit coverage has not yet been established. S035 must replace or confirm this decision after all scoped audit, closure, stabilization, and challenge-review jobs are complete.

## S001 Result

S001 completed the baseline method and evidence setup. The S001 matrix is header-only because this job has no product-document source scope.

Verification evidence is recorded in `semantic-coverage/notes/S001-audit-method-and-baseline.md`.
