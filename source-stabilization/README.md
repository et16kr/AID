# English Source Stabilization Evidence

Report date: 2026-05-16

Workspace: `/home/et16/AID`

Phase 2 job: `E001` - Phase 1 completion gate and baseline

## Purpose

This directory stores Phase 2 evidence for stabilizing the English source documents before any LLM reference consolidation work. Phase 2 checks whether `arch/Home` and `FAQE/Home` are safe source material for GPTs, Codex, and other LLM references after the Korean-to-English semantic coverage audit.

Phase 2 must not run the Phase 3 `.codex-jobs/llm-reference-consolidation/` workflow and must not create `llm-reference/`.

## Phase 1 Gate

`KO_EN_SEMANTIC_COVERAGE_REPORT.md` was read directly for the Phase 1 decision. That report records the final workflow decision as `COMPLETE`.

Stale runtime status values in `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` or `jobs.md` do not override `KO_EN_SEMANTIC_COVERAGE_REPORT.md`.

Phase 1 completion evidence:

- Final decision: `COMPLETE`
- Final validation rows with `missing`: `0`
- Final validation rows with `unverified`: `0`
- Final validation rows with `recheck_required`: `0`
- URL-backed document attachments: preserved according to the Phase 1 final report

## Baseline Repository State

The required handoff check was run from the repository root before E001 edits:

```bash
git status --porcelain --untracked-files=all -- . ":(exclude).codex-jobs" ":(exclude).codex-jobs/**"
```

Result: no output, so no project handoff files outside `.codex-jobs` blocked this job.

Current baseline:

| Field | Value |
| --- | --- |
| Branch | `combine` |
| HEAD | `d6547183af2b25bc98066506a87fe7dfac583c1c` |

Baseline Markdown counts:

| Area | Count |
| --- | ---: |
| `DOCK/Home` | 51 |
| `faq/Home` | 115 |
| `arch/Home` | 181 |
| `FAQE/Home` | 241 |

E001 did not edit product source documents under `DOCK/`, `faq/`, `arch/`, or `FAQE/`. E001 did not update `manifest.json` because no validation in this job proved metadata was stale.

## Evidence Files

E001 initialized the planned Phase 2 TSV evidence files with their required headers:

| Evidence file | Owner | Purpose | E001 state |
| --- | --- | --- | --- |
| `source-stabilization/residual-korean-classification.tsv` | E002 | Classify residual Hangul in English source documents. | Header-only |
| `source-stabilization/markdown-artifacts.tsv` | E003 | Track empty links, macro artifacts, unknown macro strings, and hash-only attachment links. | Header-only |
| `source-stabilization/legacy-attachments.tsv` | E004 | Inventory legacy attachment labels with no downloadable URL in source evidence. | Header-only |
| `source-stabilization/url-backed-attachments.tsv` | E005/E006 | Verify technical and FAQ document-format attachment URL preservation. | Header-only |
| `source-stabilization/source-classification.tsv` | E007 | Classify Korean-source-verified, link-validated, English-only, legacy attachment, and unavailable diagram sources. | Header-only |
| `source-stabilization/manifest-metadata.tsv` | E008 | Validate `manifest.json` metadata against current Markdown sources. | Header-only |

`source-stabilization/validation-report.md` is reserved for E009 final stabilization reporting and was not created by E001.

## Phase 2 Decision Rules

The final Phase 2 report must use exactly one decision:

- `READY_FOR_LLM_CONSOLIDATION`: Phase 1 is `COMPLETE`; English source defects are fixed or intentionally classified; URL-backed attachment omissions are zero; English-only FAQE sources are not mislabeled as Korean-source-verified; `manifest.json` and standard checks pass.
- `RECHECK_REQUIRED`: any source defect, classification gap, attachment uncertainty, metadata mismatch, or validation failure remains unresolved.

E001 is a baseline gate only. It does not make the final Phase 2 readiness decision; E009 owns that decision after E002-E008 evidence is complete.

## E001 Verification

Standard verification commands are recorded here for the baseline:

```bash
python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json
git diff --check
find DOCK/Home -type f -name '*.md' | wc -l
find faq/Home -type f -name '*.md' | wc -l
find arch/Home -type f -name '*.md' | wc -l
find FAQE/Home -type f -name '*.md' | wc -l
```

Results:

| Command | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json` | Pass |
| `git diff --check` | Pass |
| `find DOCK/Home -type f -name '*.md' \| wc -l` | 51 |
| `find faq/Home -type f -name '*.md' \| wc -l` | 115 |
| `find arch/Home -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE/Home -type f -name '*.md' \| wc -l` | 241 |

E001 did not run source-stability `rg` scans. No expected-no-match `rg` exit code was produced in this job.
