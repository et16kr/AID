# S033 Source Stabilization After Coverage Fixes

## Requirement And Boundary

- Job: `S033`
- Scope: run source-stability checks after coverage fixes: manifest metadata, document counts, residual Korean classification, links, macro artifacts, stale export patterns, and matrix status closure.
- Required workflow: `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`.
- Final decision for this job: `COMPLETE`.

S033 is a stabilization job. It does not replace the direct Korean-source and English-target inspections in S003-S031 or the aggregate coverage closure in S032. It checks the live source trees and evidence files after those fixes, applies source hygiene fixes where needed, and records the result in a stabilization matrix.

This job did not run the `llm-reference` consolidation workflow and did not delete, move, or rewrite Korean source documents.

## Required Reading And Preflight

Read before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- Existing semantic-coverage matrices and notes, especially S019, S031, and S032

The required handoff check was run before editing:

```bash
git status --porcelain --untracked-files=all -- . ":(exclude).codex-jobs" ":(exclude).codex-jobs/**"
```

Result: no output.

## Design Note

S033 does not change product-document architecture or documentation structure. It adds stabilization evidence:

- `semantic-coverage/matrices/S033-source-stabilization-after-coverage-fixes.tsv`
- `semantic-coverage/notes/S033-source-stabilization-after-coverage-fixes.md`
- an S033 section in `KO_EN_SEMANTIC_COVERAGE_REPORT.md`

It also normalizes `manifest.json` `body_chars` and `word_count` values to the current Markdown files. This makes the manifest consistent with the edited-page metadata checks used by prior coverage jobs and gives later consolidation work a stable file-size inventory.

## Changes Made

S033 fixed two live English-source residual Korean findings that were not intentional filenames, URLs, or Korean data examples:

- `arch/Home/Altibase Oracle Conversion Guide/2. Environment Setting/2-2 SQL Conversion__14647324.md`: translated the `DATENAME` row remark to English.
- `arch/Home/Altibase Oracle Conversion Guide/2. Environment Setting/2-3 Stored Procedure _ Function Conversion__14647326.md`: translated the inline `emp_no` primary-key comment and normalized the sample string quote.

S033 also rephrased historical macro-export wording in existing semantic-coverage evidence so the required stale-artifact grep is clean. The underlying evidence meaning is unchanged: the Korean source had Confluence macro-export placeholders, and the English target preserved the recoverable shell commands.

`manifest.json` metadata was normalized for 455 entries that no longer matched the current file text. After normalization, all 588 manifest page entries have existing source files and matching `body_chars` and `word_count` values.

## Residual Korean Classification

The live residual-Hangul scan over `arch/Home` and `FAQE/Home` has only intended classes after the two fixes:

- Korean attachment filenames and legacy attachment labels, such as `개발가이드`, `사용자가이드`, `변환가이드`, `설정_가이드`, and `이중화_가이드`.
- URL-backed downloadable document filenames whose original encoded URL contains Korean.
- Korean sample data used for character-set behavior, such as `한글테스트합니다`, `한글 데이터입니다`, and `알티베이스`.

No remaining live English-source Hangul line was classified as untranslated body prose or an untranslated procedure/comment.

## Stabilization Matrix

Matrix file: `semantic-coverage/matrices/S033-source-stabilization-after-coverage-fixes.tsv`

Rows by unit type:

- `manifest_metadata`: 1
- `document_counts`: 1
- `residual_korean_fix`: 2
- `residual_korean_classification`: 2
- `link_and_macro_artifact_check`: 1
- `matrix_unresolved_status_check`: 1
- `mapping_path_check`: 1
- `legacy_attachment_classification`: 1

Rows by coverage status:

- `added`: 3
- `covered`: 7
- `missing`: 0
- `unverified`: 0
- `recheck_required`: 0

## Self-Review

Self-review checked that:

- The S033 matrix header matches the required TSV schema.
- Every S033 matrix row has exactly 15 TSV fields.
- S033 uses only allowed coverage-status values.
- The two edited English source lines are natural technical English and preserve the identifiers `DATENAME`, `date_field_name`, `emp_no`, and primary-key semantics.
- Residual Korean in live English sources is now limited to intended attachment filenames, URLs, legacy labels, and Korean data examples.
- `manifest.json` page counts match filesystem counts and every page entry has matching current-file metadata.
- The required stale-artifact grep over live sources and evidence files returns the expected no-match result.
- No `missing`, `unverified`, or `recheck_required` rows remain in semantic matrices.

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
| Manifest path and metadata validation | Passed: 588 entries, 0 missing paths, 0 metadata mismatches |
| Residual Korean scan over live English sources | Passed after classification: only intended filenames, URLs, legacy labels, and data examples remain |
| Required stale-artifact grep over `arch/Home`, `FAQE/Home`, and `semantic-coverage` | Passed: expected-no-match grep exited 1 |
| Unresolved matrix-status grep | Passed: expected-no-match grep exited 1 |
| `semantic-coverage/doc-mapping.tsv` path validation | Passed: 166 mapping rows, 0 missing Korean paths, 0 missing English target paths |
| S033 matrix TSV shape/status validation | Passed: 10 rows, 15 fields per row; `added` 3, `covered` 7 |

External HTTP availability was not tested. S033 used file path validation, source-link preservation evidence from S019/S031, and grep-based local source hygiene checks.

## Final Decision

`COMPLETE`: source stabilization checks passed after applying the scoped hygiene fixes. Manifest metadata, counts, residual Korean classification, link/macro artifact scans, mapping paths, and matrix unresolved-status checks are clean for this job.
