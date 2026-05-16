# S001 Audit Method and Baseline

Date: 2026-05-16

Workspace: `/home/et16/AID`

## Requirement And Boundary

S001 defines the semantic-unit coverage method, confirms the repository baseline, creates the evidence structure, and records the workflow decision criteria.

This job is baseline-only. It does not audit product-document content, does not edit Korean source documents, does not edit English source documents under `arch/Home` or `FAQE/Home`, does not update `manifest.json`, and does not run the `llm-reference` consolidation workflow.

The current job scope has no assigned Korean source document and no assigned English target document. The S001 matrix is therefore a header-only schema artifact; source semantic-unit rows start in later scoped audit jobs.

## Required Reading

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/prompts/S001.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/prompt-addendum.md`

Korean source and English target product documents are not applicable to S001 because this baseline job has no product-document audit scope.

## Pre-Edit State

- Branch: `combine`
- Baseline HEAD before S001 edits: `131b19c`
- `git status --short` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified from `S001 ToDo` to `S001 Progress`.
- `git status --short --untracked-files=all -- . ':(exclude).codex-jobs' ':(exclude).codex-jobs/**'` produced no output, so there were no uncommitted project files outside the workflow area.
- Ignored workflow runtime files existed under `.codex-jobs/ko-en-semantic-coverage-audit/.runtime/` and `logs/`.

## Baseline Counts

| Area | Count |
| --- | ---: |
| `DOCK/Home` Markdown files | 51 |
| `faq/Home` Markdown files | 115 |
| `arch/Home` Markdown files | 181 |
| `FAQE/Home` Markdown files | 241 |

## Previous Report Relationship

`KO_EN_DOC_REVIEW_REPORT.md` and `PASS2_KO_EN_DOC_REVIEW_REPORT.md` record prior mapping, attachment, link, and scoped content review evidence. They are useful orientation for this workflow, but they are not accepted as proof that any current Korean semantic unit is covered.

`LLM_REFERENCE_REVIEW_PLAN.md` records the later source-stabilization and LLM consolidation gates. S001 keeps this workflow before consolidation and does not create `llm-reference/`.

## Design Note

S001 creates a new evidence structure under `semantic-coverage/`:

- `README.md` defines the method, schema, status values, duplicate ownership rule, and final decision criteria.
- `matrices/S001-audit-method-and-baseline.tsv` establishes the exact TSV header required by later jobs.
- `notes/S001-audit-method-and-baseline.md` records this baseline and verification evidence.
- `KO_EN_SEMANTIC_COVERAGE_REPORT.md` records the workflow-level method, baseline state, and current decision.

Later jobs must add source-specific matrix rows rather than relying on narrative reports.

## Self-Review

- Scope checked: S001 remains limited to baseline, evidence structure, and decision criteria.
- Product documents checked: no `DOCK/`, `faq/`, `arch/`, or `FAQE/` product files were edited.
- Terminology checked: the note uses the workflow status names and coverage status values from `workflow-requirements.md`.
- Matrix checked: the S001 matrix uses the exact required TSV header and intentionally contains no content rows.
- Link hygiene checked: repository paths are written as code-formatted paths rather than Markdown links, avoiding broken relative links.

## Verification

Verification results were recorded after drafting and self-review:

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK/Home -type f -name '*.md' \| wc -l` | 51 |
| `find faq/Home -type f -name '*.md' \| wc -l` | 115 |
| `find arch/Home -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE/Home -type f -name '*.md' \| wc -l` | 241 |
| S001 TSV header check | Passed |
| `bash -n .codex-jobs/ko-en-semantic-coverage-audit/run-all.sh` and `bash -n .codex-jobs/ko-en-semantic-coverage-audit/run_all.sh` | Passed |
| Empty-link and macro-artifact scan over `semantic-coverage` and `KO_EN_SEMANTIC_COVERAGE_REPORT.md` | Passed with exit code 1, meaning no matches |
| Matrix unresolved-status scan over `semantic-coverage/matrices` | Passed with exit code 1, meaning no unresolved S001 matrix rows |

## Decision

S001 is complete for its baseline scope.

The workflow-level decision remains `RECHECK_REQUIRED` because the source semantic-unit audits have not yet been completed. This is expected for S001 and is not a failure of this baseline job.
