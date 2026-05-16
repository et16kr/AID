# KO to EN Semantic Coverage Report

Report date: 2026-05-16

Workspace: `/home/et16/AID`

Current workflow decision: `RECHECK_REQUIRED`

Reason: S003-S031 source-audit and attachment/classification matrices are merged through S032 with zero `missing`, `unverified`, or `recheck_required` rows, S033 source stabilization has passed, and S034 independent matrix challenge review found no sampled false-positive coverage row. The workflow still requires S035 final decision before this report can become `COMPLETE`.

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

S002 created the mapping inventory and matrix scaffold:

- `semantic-coverage/doc-mapping.tsv`
- `semantic-coverage/matrices/S002-mapping-inventory-and-unit-matrix-scaffold.tsv`
- `semantic-coverage/notes/S002-mapping-inventory-and-unit-matrix-scaffold.md`

S003-S031 added per-scope semantic-unit, attachment, link, and classification rows and notes under `semantic-coverage/matrices/` and `semantic-coverage/notes/`. S032 added aggregate closure evidence:

- `semantic-coverage/matrices/S032-unresolved-coverage-closure.tsv`
- `semantic-coverage/notes/S032-unresolved-coverage-closure.md`

S033 added source-stabilization evidence:

- `semantic-coverage/matrices/S033-source-stabilization-after-coverage-fixes.tsv`
- `semantic-coverage/notes/S033-source-stabilization-after-coverage-fixes.md`

S034 added independent challenge evidence:

- `semantic-coverage/matrices/S034-independent-matrix-challenge-review.tsv`
- `semantic-coverage/notes/S034-independent-matrix-challenge-review.md`

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

The current workflow decision remains `RECHECK_REQUIRED` because the final decision job is still pending. S035 must replace or confirm this decision after S034 completes.

## S001 Result

S001 completed the baseline method and evidence setup. The S001 matrix is header-only because this job has no product-document source scope.

Verification evidence is recorded in `semantic-coverage/notes/S001-audit-method-and-baseline.md`.

## S002 Result

S002 completed the KO-to-EN mapping inventory and evidence scaffold.

The mapping inventory contains 166 Korean source rows:

| Area | Source rows |
| --- | ---: |
| `DOCK/Home` technical documents | 51 |
| `faq/Home` Korean FAQ documents | 115 |

S002 validated that every Korean source path in `semantic-coverage/doc-mapping.tsv` exists and that every listed English target path exists. The S002 matrix is header-only because this job has no product-document semantic-unit audit scope.

Verification evidence is recorded in `semantic-coverage/notes/S002-mapping-inventory-and-unit-matrix-scaffold.md`.

## S003-S031 Source Audit Results

S003-S018 audited Korean technical documents under `DOCK/Home` against their mapped English `arch/Home` targets. S020-S030 audited Korean FAQ documents under `faq/Home` against the Korean-core English `FAQE/Home` targets. S019 and S031 closed attachment, source-link, legacy-label, export-artifact, and English-only classification evidence for the technical and FAQ sets.

Each source-audit job created a TSV matrix and Markdown note under `semantic-coverage/matrices/` and `semantic-coverage/notes/`. The direct Korean-source and English-target inspection evidence stays in those per-job files.

Status before S032 closure:

| Status | Rows |
| --- | ---: |
| `covered` | 4,665 |
| `added` | 70 |
| `not_applicable` | 290 |
| `source_limitation` | 78 |
| `missing` | 0 |
| `unverified` | 0 |
| `recheck_required` | 0 |

The 78 `source_limitation` rows are recorded limitations such as legacy non-downloadable `#` attachment labels, broken source export artifacts, or source links where no safe English content can be inferred.

## S032 Result

S032 merged and validated the existing coverage matrices.

Aggregate closure evidence:

| Check | Result |
| --- | --- |
| Prior matrix files checked | 31 |
| Prior matrix rows checked | 5,103 |
| Header or row-shape errors | 0 |
| `semantic-coverage/doc-mapping.tsv` rows | 166 |
| Mapped Korean sources without any matrix row | 0 |
| Missing KO or EN paths in `doc-mapping.tsv` | 0 |
| `missing` rows after S032 | 0 |
| `unverified` rows after S032 | 0 |
| `recheck_required` rows after S032 | 0 |

S032 did not edit `DOCK/`, `faq/`, `arch/`, `FAQE/`, or `manifest.json` because the merged matrix evidence showed no remaining safe source coverage fix to apply. The S032 matrix has 31 aggregate rows: 29 `covered` rows for source-audit/attachment matrices and 2 `not_applicable` rows for the header-only S001/S002 baseline and mapping matrices.

Verification evidence is recorded in `semantic-coverage/notes/S032-unresolved-coverage-closure.md`.

## S033 Result

S033 ran source-stabilization checks after coverage fixes.

Stabilization evidence:

| Check | Result |
| --- | ---: |
| Manifest page entries checked | 588 |
| Manifest missing paths after normalization | 0 |
| Manifest metadata mismatches after normalization | 0 |
| Live English residual Korean classes | intended filenames, URLs, legacy labels, and data examples only |
| Live/evidence stale artifact grep | expected no-match |
| Matrix `missing` rows after S033 | 0 |
| Matrix `unverified` rows after S033 | 0 |
| Matrix `recheck_required` rows after S033 | 0 |
| Mapping rows revalidated | 166 |
| Missing KO or EN paths in `doc-mapping.tsv` | 0 |

S033 fixed two residual Korean findings in English source files:

- `arch/Home/Altibase Oracle Conversion Guide/2. Environment Setting/2-2 SQL Conversion__14647324.md`
- `arch/Home/Altibase Oracle Conversion Guide/2. Environment Setting/2-3 Stored Procedure _ Function Conversion__14647326.md`

S033 also normalized `manifest.json` `body_chars` and `word_count` values to the current Markdown files and rephrased historical macro-export wording in semantic evidence so the required artifact scan is clean. It did not run the `llm-reference` consolidation workflow.

Verification evidence is recorded in `semantic-coverage/notes/S033-source-stabilization-after-coverage-fixes.md`.

## S034 Result

S034 independently challenged sampled `covered` matrix rows by inverse-searching required identifiers in English target files and re-reading the scoped Korean and English context directly.

Challenge evidence:

| Check | Result |
| --- | ---: |
| Covered rows with required identifiers scanned for weak exact-hit evidence | 4,665 S003-S031 covered rows considered; 170 weak exact-hit candidates surfaced |
| Manual challenge sample rows | 24 |
| S034 matrix rows | 25 |
| Sampled false-positive covered rows | 0 |
| English source files changed by S034 | 0 |
| `manifest.json` changes required by S034 | 0 |
| S034 `missing`, `unverified`, or `recheck_required` rows | 0 |

The manual sample covered installation/license tables, platform Direct I/O tables, monitoring SQL, replication conflicts, backup/recovery policy, APRE errors, client API configuration, conversion tables, Migration Center GUI semantics, Docker command output, FAQ platform support, operation properties, replication DDL steps, backup SQL, ODBC INI samples, monitoring SQL, error-message resolutions, utility command output, and attachment preservation.

S034 found weak exact-search cases caused by whitespace around configuration assignments, Markdown emphasis around placeholders, comma-formatted numeric limits, translated prose, and Migration Center screenshot condensation. Direct context review confirmed those sampled rows still preserve the Korean-source semantics in English. No source edit was required.

Verification evidence is recorded in `semantic-coverage/notes/S034-independent-matrix-challenge-review.md`.
