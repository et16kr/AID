# GPTs Readiness Report

Report date: 2026-05-17

## Final Decision

`GPTS_UPLOAD_READY`

Automated validation decision: `GPTS_AUTOMATED_PASS`.

The Altibase GPTs upload package is ready for GPTs Knowledge upload after automated validation. Human review starts only after automated validation passes with `GPTS_AUTOMATED_PASS`; human review should use `llm-reference/gpts-upload/HUMAN_REVIEW_CHECKLIST.html`.

## Expected Outputs Reconfirmed

The expected outputs from `.codex-jobs/gpts-knowledge-encyclopedia/workflow-requirements.md` are present:

- `llm-reference/gpts-upload/build-gpts-knowledge-bundles.py`
- `llm-reference/gpts-upload/validate-gpts-knowledge.py`
- `llm-reference/gpts-upload/VALIDATION_PROCESS.md`
- `llm-reference/gpts-upload/HUMAN_REVIEW_CHECKLIST.html`
- `llm-reference/gpts-upload/Altibase_GPT_Knowledge_Encyclopedia.md`
- `llm-reference/gpts-upload/README.md`
- `llm-reference/gpts-upload/GPTS_INSTRUCTIONS.txt`
- `llm-reference/gpts-upload/UPLOAD_MANIFEST.tsv`
- `llm-reference/gpts-upload/GPTS_READINESS_REPORT.md`

Optional/internal audit output is also present:

- `llm-reference/gpts-upload/Altibase_GPT_Knowledge_Audit.md`

## Exact GPTs Upload File List

| Status | File | Purpose |
| --- | --- | --- |
| Required customer-facing upload | `llm-reference/gpts-upload/Altibase_GPT_Knowledge_Encyclopedia.md` | Self-contained Altibase GPTs Knowledge encyclopedia for customer and support answers. Upload this as the required Altibase reference file. |
| Optional/internal only | `llm-reference/gpts-upload/Altibase_GPT_Knowledge_Audit.md` | Optional validation, coverage, packaging, and traceability evidence. Do not require this file for normal customer answers. |

The upload manifest contains two Altibase GPTs Knowledge rows, with exactly one customer-required row. No more than two Altibase GPTs upload files are required.

## Validation Command Results

| Check | Command or Evidence | Result |
| --- | --- | --- |
| Manifest JSON parse | `python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json` | Passed |
| Diff whitespace check | `git diff --check` | Passed |
| Generator rerun | `python3 llm-reference/gpts-upload/build-gpts-knowledge-bundles.py` | Passed; generated encyclopedia and audit bundle |
| Required output presence | `test -f ...` for all required workflow outputs | Passed |
| Included document boundary count | `rg -c "^BEGIN INCLUDED DOCUMENT:" llm-reference/gpts-upload/Altibase_GPT_Knowledge_Encyclopedia.md` | Passed; 18 included document boundaries |
| Topic file inclusion | `rg -n "BEGIN INCLUDED DOCUMENT: llm-reference/(0[1-9]\|1[0-2])-.*\\.md" ...` plus automated validator | Passed; all 12 topic files are included exactly once |
| Supporting document inclusion | `rg -n "^BEGIN INCLUDED DOCUMENT: llm-reference/(README\|source-index\|00-source-classification\|HANDOFF\|LLM_REFERENCE_BUILD_REPORT\|coverage/README)\\.md" ...` | Passed |
| Source package decision marker | `rg -n "COMPLETE_REFERENCE_PACKAGE" llm-reference/gpts-upload/Altibase_GPT_Knowledge_Encyclopedia.md` | Passed |
| Coverage blocker scan | Status-field blocker `rg` scan over `llm-reference/coverage/*.tsv` | Passed; no matches, exit code 1 as expected |
| Artifact scan | Standard artifact `rg` scan over `Altibase_GPT_Knowledge_Encyclopedia.md` | Passed; no matches, exit code 1 as expected |
| Upload manifest count | `awk -F '\\t' ... llm-reference/gpts-upload/UPLOAD_MANIFEST.tsv` | Passed; 2 rows, 1 customer-required row |
| Full automated validation | `python3 llm-reference/gpts-upload/validate-gpts-knowledge.py --mode full` | Passed; final automated decision `GPTS_AUTOMATED_PASS` |
| Final automated validation | `python3 llm-reference/gpts-upload/validate-gpts-knowledge.py --mode final` | Passed; final automated decision `GPTS_AUTOMATED_PASS` |

## Size Summary

| File | Bytes | Rough token estimate |
| --- | ---: | ---: |
| `Altibase_GPT_Knowledge_Encyclopedia.md` | 1,030,415 | 257,603 |
| `Altibase_GPT_Knowledge_Audit.md` | 50,124 | 12,531 |
| Total | 1,080,539 | 270,134 |

Both generated upload files are below the configured GPTs per-file limit used by the validator.

## Completeness And Traceability

- The encyclopedia includes all 12 topic documents in full.
- The encyclopedia includes `llm-reference/README.md`, `llm-reference/source-index.md`, `llm-reference/00-source-classification.md`, `llm-reference/HANDOFF.md`, `llm-reference/LLM_REFERENCE_BUILD_REPORT.md`, and `llm-reference/coverage/README.md`.
- The validator confirmed 15 full-text included documents match their source files.
- The validator confirmed source-path traceability with 18 `Source paths` sections and 628 source references.
- The encyclopedia contains `COMPLETE_REFERENCE_PACKAGE`.

Original source trees `arch/`, `FAQE/`, `DOCK/`, and `faq/` are not GPT answer-time dependencies. Source paths retained in the generated files are evidence labels and maintenance traceability only.

## Remaining Accepted Limitations

These are accepted limitations, not blockers:

- `English-only source`
- `english_only_auxiliary`
- `legacy_no_downloadable_url`
- `legacy_attachment_label_only`
- `diagram_unavailable`
- `not_document_format`
- `accepted_source_limitation`
- `accepted_english_only_auxiliary`

The GPT must not invent unavailable diagrams, missing attachments, synthetic URLs, or source content absent from the encyclopedia. If the encyclopedia lacks enough detail to answer safely, the GPT should say that the available Altibase GPT knowledge does not contain the required detail.

## Human Review Boundary

Human review starts only after automated validation passes with `GPTS_AUTOMATED_PASS`. Automated validation has passed, so the next step is human review using `llm-reference/gpts-upload/HUMAN_REVIEW_CHECKLIST.html` before customer deployment.
