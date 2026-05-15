# Pass2 Korean-English Documentation Review Report

Review start date: 2026-05-16

Workspace: `/home/et16/AID`

## Summary

This report tracks the second-pass Korean-to-English documentation audit after J013. The pass2 goal is to make the English source set safer before GPTs, Codex, and other LLM reference packaging begins.

The second pass uses Korean `DOCK/Home` and `faq/Home` documents as authoritative sources. Later scoped jobs compare Korean and English content at sentence, bullet, table-row, command, SQL, configuration, warning, version, attachment, and link level, using semantic units when document structures differ.

P201 establishes the baseline and includes the newly generated pass2 workflow scaffold. It does not edit product documentation.

## P201 Baseline after J013

### Scope

P201 confirmed J013 completion, current git state, first-pass completion status, document counts, manifest validity, and pass2 audit boundaries before any pass2 product documentation editing.

### Evidence

- Current branch before P201 edits: `combine`.
- Initial dirty state: only untracked `.codex-jobs/ko-en-doc-coverage-pass2/` scaffold files.
- Latest first-pass commit before P201 edits: `dbac1de docs: complete J013 LLM handoff plan`.
- `.codex-jobs/ko-en-doc-coverage/jobs.tsv` showed `J001` through `J013` as `Done`.
- First-pass report and handoff evidence reviewed:
  - `KO_EN_DOC_REVIEW_REPORT.md`
  - `LLM_REFERENCE_REVIEW_PLAN.md`
  - `.codex-jobs/ko-en-doc-coverage/J012-final-coverage-validation.md`
  - `.codex-jobs/ko-en-doc-coverage/J013-llm-reference-handoff-package-plan.md`

### Baseline Counts

| Area | Count |
| --- | ---: |
| `DOCK/Home` Markdown files | 51 |
| `faq/Home` Markdown files | 115 |
| `arch/Home` Markdown files | 181 |
| `FAQE/Home` Markdown files | 241 |

### Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK/Home -type f -name '*.md' \| wc -l` | 51 |
| `find faq/Home -type f -name '*.md' \| wc -l` | 115 |
| `find arch/Home -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE/Home -type f -name '*.md' \| wc -l` | 241 |
| `bash -n .codex-jobs/ko-en-doc-coverage-pass2/run_all.sh` | Passed |
| `bash -n .codex-jobs/ko-en-doc-coverage-pass2/run-all.sh` | Passed |

The required baseline export-pattern scan was run:

```bash
rg -n "\[\]\(|Error rendering macro|Unknown macro" arch/Home FAQE/Home
```

It found four pre-existing `Unknown macro: {gliffy}` markers in `FAQE/Home/ALTIBASE HDB Troubleshooting/Cannot insert new records after deleting bulk records__2557870.md` at lines 29, 39, 55, and 101.

P201 did not edit that product documentation page because P201 is a baseline-only job. The finding is English-only `FAQE` material outside the Korean-core FAQ verification boundary and is recorded for later scoped export/link revalidation work.

### Changes Made

- Added `.codex-jobs/ko-en-doc-coverage-pass2/` workflow scaffold to version control.
- Added `.codex-jobs/ko-en-doc-coverage-pass2/P201-baseline-after-j013.md`.
- Added this `PASS2_KO_EN_DOC_REVIEW_REPORT.md`.
- Marked P201 as `Done` in pass2 workflow control files.

No product documentation files under `DOCK/`, `arch/`, `faq/`, or `FAQE/` were edited. `manifest.json` was not changed.

### Remaining Risk

- P201 is not a sentence-level product documentation audit; that work starts with later scoped jobs.
- The English-only `FAQE/Home/ALTIBASE HDB Troubleshooting/Cannot insert new records after deleting bulk records__2557870.md` page still contains four `Unknown macro: {gliffy}` markers.
- English-only `FAQE` extras remain outside Korean-source core verification unless later pass2 jobs explicitly classify and review them.
