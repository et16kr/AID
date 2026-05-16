# S002 Mapping Inventory and Unit Matrix Scaffold

Date: 2026-05-16

Workspace: `/home/et16/AID`

## Requirement And Boundary

S002 validates Korean-to-English document mappings, creates the mapping inventory schema, and prepares the per-job evidence files needed by later semantic-unit audit jobs.

This job is inventory-only. It does not audit product-document semantic units, does not edit Korean source documents, does not edit English source documents under `arch/Home` or `FAQE/Home`, does not update `manifest.json`, and does not run the `llm-reference` consolidation workflow.

The S002 matrix is header-only because this job has no assigned content-bearing Korean semantic units to mark as `covered`, `added`, `not_applicable`, `source_limitation`, or `recheck_required`. Semantic-unit rows begin in S003 and later scoped audit jobs.

## Required Reading

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/prompts/S002.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/prompt-addendum.md`
- Current Korean source inventory under `DOCK/Home` and `faq/Home`
- Current English target inventory under `arch/Home` and `FAQE/Home`

S002 inspected product-document scope at the inventory level: path existence, expected counts, assigned jobs, duplicate ownership, and target-path availability. It did not treat prior J/P reports as semantic-unit proof.

## Pre-Edit State

- Branch: `combine`
- `git status --short` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified from `S002 ToDo` to `S002 Progress`.
- No uncommitted project files existed outside the workflow status file before S002 edits.

## Design Note

S002 adds `semantic-coverage/doc-mapping.tsv` as the source-to-target inventory used by later semantic-unit jobs.

The mapping schema is:

```text
mapping_id	ko_path	source_type	en_target_paths	assigned_audit_job	primary_owner_job	supporting_jobs	previous_evidence_refs	path_validation	notes
```

Rules:

- `mapping_id` is stable and short enough for later note and matrix references.
- `source_type` is `technical_doc` for `DOCK/Home` rows and `faq` for Korean-core `faq/Home` rows.
- `en_target_paths` uses `; ` to separate multiple existing English target files when a Korean page maps to a split English guide.
- `assigned_audit_job` is the job responsible for the semantic-unit audit of that Korean source.
- `primary_owner_job` records duplicate-source ownership where applicable.
- `supporting_jobs` records cross-reference or attachment/link jobs, such as S019 for technical documents and S031 for FAQ documents.
- `previous_evidence_refs` points to prior J/P orientation evidence only; those references do not prove current semantic-unit coverage.
- `path_validation` is `exists` only after S002 path checks verify the Korean source and all listed English target paths exist.

## Mapping Coverage

S002 created one mapping row per Korean source Markdown file in the workflow authority scope.

| Area | Source files | Mapping rows |
| --- | ---: | ---: |
| `DOCK/Home` technical documents | 51 | 51 |
| `faq/Home` Korean FAQ documents | 115 | 115 |
| Total | 166 | 166 |

Duplicate ownership follows `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`:

- `DOCK/Home/20. Altibase 설정 파일 가이드__13437165.md`: full audit owner S003; S005 may add operation-specific cross-reference rows only.
- `DOCK/Home/26. Altibase 기본적인 장애대응 절차__13435879.md`: full audit owner S005; S009 may add backup/recovery-specific cross-reference rows only.
- `DOCK/Home/43. Altibase STARTUP _ STOP 과정의 이해__13434993.md`: full audit owner S005; S009 may add recovery-specific cross-reference rows only.

S002 also records S019 as the supporting technical attachment/link job and S031 as the supporting FAQ attachment/classification job. These supporting jobs do not replace the primary semantic-unit owner.

## Self-Review

- Scope checked: S002 stayed limited to mapping inventory, schema documentation, and evidence scaffolding.
- Product documents checked: no `DOCK/`, `faq/`, `arch/`, or `FAQE/` product files were edited.
- Mapping count checked: every `DOCK/Home` Markdown file and every `faq/Home` Markdown file has exactly one mapping row.
- Target path checked: every listed English target path exists.
- Duplicate ownership checked: duplicate technical sources use the primary-owner rule from the workflow requirements.
- Terminology checked: matrix status values and job IDs match the workflow requirements.
- Matrix checked: the S002 matrix uses the exact required TSV header and intentionally contains no content rows.

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
| `semantic-coverage/doc-mapping.tsv` TSV shape check | Passed: 166 data rows, 10 columns each |
| Source mapping count check | Passed: 51 `technical_doc` rows and 115 `faq` rows |
| Korean source path existence check | Passed: 166 listed Korean source paths exist |
| English target path existence check | Passed: all listed English target paths exist |
| Mapped file readability check | Passed: 447 unique mapped Korean and English files read with non-empty heading or content |
| Mapping completeness check against `DOCK/Home` and `faq/Home` inventories | Passed: no missing or extra Korean source rows |
| S002 TSV header check | Passed |
| `bash -n .codex-jobs/ko-en-semantic-coverage-audit/run-all.sh` and `bash -n .codex-jobs/ko-en-semantic-coverage-audit/run_all.sh` | Passed |
| Empty-link and macro-artifact scan over S002 evidence files | Passed with exit code 1, meaning no matches |
| Matrix unresolved-status scan over S002 matrix | Passed with exit code 1, meaning no unresolved S002 matrix rows |

## Decision

S002 is complete for its mapping-inventory and matrix-scaffold scope.

The workflow-level decision remains `RECHECK_REQUIRED` because the source semantic-unit audits have not yet been completed. This is expected for S002 and is not a failure of this inventory job.
