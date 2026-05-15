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

## P202 Tech audit: installation core and database creation

### Scope

P202 audited Korean installation, quick install, troubleshooting, database creation, and configuration core documents against their English `arch` targets. The Korean sources remained authoritative and were not edited.

| Korean source | English target |
| --- | --- |
| `DOCK/Home/20. Altibase 설정 파일 가이드__13437165.md` | `arch/Home/Altibase Configuration File Guide__22642991.md` |
| `DOCK/Home/25. Altibase 데이터베이스 생성 가이드__13436812.md` | `arch/Home/Creating ALTIBASE Database__22643020.md` |
| `DOCK/Home/31. Altibase 설치가이드__11698403.md` | `arch/Home/Altibase Installation Guide__14647632.md`; `arch/Home/Altibase Installation Guide/1. Altibase HDB package installer__14647639.md`; `arch/Home/Altibase Installation Guide/2. Product Installation using the Package Installer__14647653.md`; `arch/Home/Altibase Installation Guide/3. License Key Request__14647666.md` |
| `DOCK/Home/41. Altibase Quick Install & Start for UNIX__13436834.md` | `arch/Home/Altibase Quick Install & Start for UNIX__16875604.md` |
| `DOCK/Home/42. Altibase 설치 시 발생할 수 있는 문제상황과 조치__13437056.md` | `arch/Home/Troubleshooting Altibase Installation Problems__15138879.md` |

### Findings And Updates

- Added missing Korean-source configuration semantics to the English configuration guide:
  - `?` in `altibase.properties` means `$ALTIBASE_HOME`.
  - `AUTO_COMMIT` session settings take precedence over `altibase.properties`.
  - Changing DB-creation-time immutable properties requires migration and DB recreation.
  - `altibase_boot.log`, `LF_PREPARE_WAIT_COUNT`, and `v$lfg` were corrected for exact searchable identifiers.
- Corrected EOS wording in both database creation and quick install documents. The Korean source says versions earlier than `Altibase ver. 6` are EOS targets; the English database creation document incorrectly included `Altibase ver. 6`.
- Fixed malformed support portal/manual links and an invalid `altibase_env.mk` URL in scoped English documents.
- Corrected installation guide details:
  - test environment version `Altibase v7.1.0`.
  - `Windows 7, 8` support table wording.
  - property-configuration step explanation.
  - post-install list of two shell scripts plus one SQL script.
  - malformed MAC address lookup table export.
- Corrected Quick Install and troubleshooting wording where Korean-source semantics or identifiers were unclear in English, including `PATH`, `altibase_boot.log`, shutdown wait behavior, iSQL utility wording, license reissue, and listener/replication port bind resolutions.
- No English change was needed for `arch/Home/Altibase Installation Guide/1. Altibase HDB package installer__14647639.md`; its APatch, patchinfo, backup, rollback, and command examples already matched the Korean source semantically.

### Attachment And Link Evidence

- Configuration, database creation, quick install, and troubleshooting PDF attachment links from Korean source pages remain preserved in the English targets.
- The scoped installation guide uses embedded image links rather than document-format attachments.
- Grep checks found no scoped `[]()`, `Error rendering macro`, `Unknown macro`, malformed `support.altibase.com/en/)]`, or invalid `http://altibase_env.mk` references after edits.

### Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p202-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK/Home -type f -name '*.md' \| wc -l` | 51 |
| `find faq/Home -type f -name '*.md' \| wc -l` | 115 |
| `find arch/Home -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE/Home -type f -name '*.md' \| wc -l` | 241 |
| Scoped grep for malformed support links, invalid `http://altibase_env.mk`, export artifacts, and corrected typo patterns | Passed, no matches |
| Scoped PDF attachment preservation grep | Passed, 5 preserved links |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 7 edited English pages |

### Remaining Risk

- P202 did not add broad Korean legal boilerplate to split English installation pages because the job focused on technical installation, database creation, configuration, command, warning, version, attachment, and link semantics.
- External HTTP availability was not tested; P202 used grep-based source-link and attachment preservation checks.
