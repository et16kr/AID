# P201 Baseline After J013

Date: 2026-05-16

## Scope

P201 confirms the starting point for Korean-to-English sentence-level audit pass 2 after J013. It does not edit product documentation under `DOCK/`, `arch/`, `faq/`, or `FAQE/`, and it does not change `manifest.json` product metadata.

The pass2 workflow scaffold under `.codex-jobs/ko-en-doc-coverage-pass2/` was untracked at the start of this job. The P201 contract allows the freshly generated scaffold to be included in the P201 commit together with this baseline note and `PASS2_KO_EN_DOC_REVIEW_REPORT.md`.

## Requirement And Boundary Reconfirmation

- Job id: `P201`.
- Goal: confirm J013 completion, git state, document counts, manifest validity, first-pass reports, and pass2 audit boundary before editing product documentation.
- Korean `DOCK/Home` and `faq/Home` documents remain authoritative.
- English update targets for later pass2 jobs are `arch/Home` and Korean-core `FAQE/Home` documents.
- P201 records baseline evidence only. Sentence-level product documentation edits begin in later P202-P224 jobs.
- English-only `FAQE` content is not Korean-source verified unless a later job explicitly reviews and labels it.

## Initial Git State

Initial `git status --short --branch --untracked-files=all` showed branch `combine` with only the untracked pass2 workflow scaffold:

```text
## combine
?? .codex-jobs/ko-en-doc-coverage-pass2/.gitignore
?? .codex-jobs/ko-en-doc-coverage-pass2/jobs.md
?? .codex-jobs/ko-en-doc-coverage-pass2/jobs.tsv
?? .codex-jobs/ko-en-doc-coverage-pass2/prompt-addendum.md
?? .codex-jobs/ko-en-doc-coverage-pass2/prompts/P201.md
...
?? .codex-jobs/ko-en-doc-coverage-pass2/workflow-requirements.md
```

No uncommitted project documentation files from a previous job were present outside the pass2 workflow scaffold.

## J013 Completion Evidence

`git log --oneline -15` showed J013 as the current `HEAD` before P201 edits:

```text
dbac1de docs: complete J013 LLM handoff plan
7fdd71b docs: complete J012 final coverage validation
ccc7b75 docs: complete J011 English readability pass
0501b1c docs: complete J010 attachment source links
14867ce Complete J009 FAQ coverage review
18dd83e Complete J008 FAQ KO-EN coverage
e4edc97 J007 update FAQ installation and operations docs
5a8a044 J006 update SQL migration and tool docs
12fda5f docs: complete J005 development API coverage
b302321 docs: complete J004 replication backup recovery coverage
37b2f47 docs: complete J003 operations administration coverage
d4bfa64 docs: complete J002 installation platform coverage
3ea8f0f J001 baseline inventory and mapping
c4e97a5 Update English Altibase docs from Korean sources
075f125 init
```

The first-pass `.codex-jobs/ko-en-doc-coverage/jobs.tsv` shows `J001` through `J013` as `Done`. The J013 note exists at `.codex-jobs/ko-en-doc-coverage/J013-llm-reference-handoff-package-plan.md`, and `LLM_REFERENCE_REVIEW_PLAN.md` contains the J013 LLM reference handoff package plan.

## Design Note

P201 adds pass2 control documentation and reporting only. This establishes the second-pass workflow boundary but does not change product behavior, source document hierarchy, English product documentation, Korean source documentation, or manifest metadata.

The pass2 workflow is stricter than the first pass: later jobs must compare scoped Korean and English material at sentence, bullet, table-row, command, SQL, configuration, warning, version, attachment, and link level. If Korean and English structure differ, later jobs compare semantic units rather than line numbers.

## Baseline Counts

| Area | Count |
| --- | ---: |
| `DOCK/Home` Markdown files | 51 |
| `faq/Home` Markdown files | 115 |
| `arch/Home` Markdown files | 181 |
| `FAQE/Home` Markdown files | 241 |

## Baseline Checks

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json` | Passed |
| `git diff --check` | Passed |
| `bash -n .codex-jobs/ko-en-doc-coverage-pass2/run_all.sh` | Passed |
| `bash -n .codex-jobs/ko-en-doc-coverage-pass2/run-all.sh` | Passed |
| Document counts for `DOCK/Home`, `faq/Home`, `arch/Home`, `FAQE/Home` | Passed: 51, 115, 181, 241 |
| First-pass `jobs.tsv` completion status | Passed: `J001`-`J013` all `Done` |

The required full-scope export-pattern scan was also run:

```bash
rg -n "\[\]\(|Error rendering macro|Unknown macro" arch/Home FAQE/Home
```

It found four pre-existing `Unknown macro: {gliffy}` markers in English-only `FAQE` material:

- `FAQE/Home/ALTIBASE HDB Troubleshooting/Cannot insert new records after deleting bulk records__2557870.md:29`
- `FAQE/Home/ALTIBASE HDB Troubleshooting/Cannot insert new records after deleting bulk records__2557870.md:39`
- `FAQE/Home/ALTIBASE HDB Troubleshooting/Cannot insert new records after deleting bulk records__2557870.md:55`
- `FAQE/Home/ALTIBASE HDB Troubleshooting/Cannot insert new records after deleting bulk records__2557870.md:101`

P201 records this as baseline evidence and does not fix it because P201 must not edit product documentation. The issue is outside the Korean-core FAQ coverage boundary and is appropriate for later English-only/export revalidation work, especially P224.

## Self-Review

- The baseline note records the required git, first-pass, count, manifest, diff, script, and export-pattern evidence.
- The pass2 boundary is explicit: Korean sources remain authoritative, and product documentation editing is deferred to later scoped jobs.
- The pre-existing English-only `Unknown macro` markers are recorded as remaining risk, not hidden as a clean full-scope result.
- No Korean source document or English product documentation file was changed by P201.

## Remaining Risk

- P201 is not a sentence-level audit of product documentation. It only establishes the pass2 starting point.
- The English-only `FAQE/Home/ALTIBASE HDB Troubleshooting/Cannot insert new records after deleting bulk records__2557870.md` page contains four `Unknown macro: {gliffy}` markers and needs later scoped handling.
- English-only `FAQE` content remains outside Korean-source core verification unless a later pass2 job explicitly classifies and reviews it.
