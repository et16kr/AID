# P224 FAQ Attachment Source English-Only and Export Revalidation

Date: 2026-05-16

## Scope

P224 revalidated FAQ document-format attachments, external source links, empty Markdown links, English-only `FAQE` classification candidates, legacy `#` labels, and export artifacts across `FAQE/Home`. Korean FAQ documents under `faq/Home` remained authoritative and were not edited.

## Boundary And Design Note

This job did not change product behavior, repository architecture, or the documentation hierarchy. Documentation edits were limited to correcting export-damaged references and missing-diagram placeholders in existing English FAQ pages. English-only `FAQE` pages were classified separately and are not described as Korean-source verified.

## Attachment Evidence

- Rechecked 7 URL-backed Korean FAQ document-format links with target extensions `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, and `.zip`.
- Confirmed all 7 exact URLs are preserved in `FAQE/Home`; missing count is 0.
- Preserved URL-backed links:

| Korean source attachment | Status |
| --- | --- |
| `D24_ALTIBASE_효율적인_이중화_가이드.pdf` | Preserved in `FAQE/Home/03. Replication/How to create_delete replication objects__16876082.md` |
| `D67_ALTIBASE_이중화_제약사항_가이드.pdf` | Preserved in `FAQE/Home/03. Replication/How to create_delete replication objects__16876082.md` |
| `LobSpringIbatisSample.zip` | Preserved in `FAQE/Home/07. Development and API/How to manage Spring+iBatis transaction__16876194.md` |
| `altimon_for_windows.zip` | Preserved in `FAQE/Home/08. Monitoring/Monitoring Tools for Windows__16876220.md` |
| `ALTIMON_USER_GUIDE.pdf` | Preserved in `FAQE/Home/08. Monitoring/How to set up and execute altimon__16876266.md` |
| `ALTIBASE_운영을_위한_HPUX_설정_가이드.pdf` | Preserved in `FAQE/Home/09. Error Messages/[Warning] Memory allocation failed__16876308.md` |
| `AdminCenter2.zip` | Preserved in `FAQE/Home/11. Utilities/AdminCenter2 execution file__16876465.md` |

## English-Only Classification

`FAQE/Home` contains 241 Markdown files. The 115 files under the Korean-core FAQ categories remain the Korean-source-verified target set. The remaining 126 files are English-only candidates:

| English-only candidate area | Files |
| --- | ---: |
| `ALTIBASE HDB Administration` | 7 |
| `ALTIBASE HDB Architecture` | 3 |
| `ALTIBASE HDB Performance Tuning` | 4 |
| `ALTIBASE HDB Replication` | 4 |
| `ALTIBASE HDB Troubleshooting` | 9 |
| `Altibase Error Messages` | 98 |
| `Altibase Error Messages__6979655.md` | 1 |

These pages may still be useful for LLM packaging, but they should be marked as English-only sources when used because this pass did not verify them against Korean FAQ source documents.

## Findings And Updates

- Replaced Confluence Gliffy placeholder artifacts in 7 English-only FAQE pages with explicit diagram-unavailable notes. No diagram content was inferred.
- Converted legacy `(#)` links in 7 English-only `Altibase Error Messages` pages to plain searchable error text while preserving exact error codes and messages.
- Corrected Java package/class names in `FAQE/Home/09. Error Messages/[Notify _ Fetch Timeout] Session Closed by Server__16876301.md` where the export had converted stack-trace identifiers such as `Altibase.jdbc.driver.cm`, `java.io`, `java.net`, and `sun.nio.ch` into fake HTTP links.
- Updated `manifest.json` metadata for all 15 edited English Markdown pages.

## Legacy Labels

- Korean FAQ source contains one non-downloadable legacy `#` attachment label: `total_memory_tablespaces_usage.txt` in `faq/Home/02. 운영 및 관리/02-12. MEM_MAX_DB_SIZE 프로퍼티 설정 변경__8454891.md`.
- This label has no URL-backed attachment to preserve and was not converted into an English download link.
- After cleanup, `FAQE/Home` contains no Markdown links with the exact `(#)` target.

## Self-Review

- Rechecked document-format attachment extraction using the target extensions `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, and `.zip`.
- Rechecked `FAQE/Home` for empty Markdown links, `(#)` links, `Error rendering macro`, `Unknown macro`, lowercase `unknown-macro` placeholder URLs, fake Java package HTTP links, and suspicious Markdown URL exports.
- Rechecked edited-page `manifest.json` `body_chars` and `word_count` against current file length and whitespace token counts.

## Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p224-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK/Home -type f -name '*.md' \| wc -l` | 51 |
| `find faq/Home -type f -name '*.md' \| wc -l` | 115 |
| `find arch/Home -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE/Home -type f -name '*.md' \| wc -l` | 241 |
| FAQ document-format attachment preservation script | Passed, 7 URL-backed links preserved and 0 missing |
| Legacy `#` FAQ attachment label inventory | Passed, 1 Korean-only non-downloadable label recorded; 0 `FAQE/Home` `(#)` links remain |
| `FAQE/Home` empty-link/export-artifact grep | Passed, no matches |
| Suspicious Markdown URL export scan | Passed, 0 suspicious links |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 15 edited English pages |
| `bash -n .codex-jobs/ko-en-doc-coverage-pass2/run_all.sh` and `bash -n .codex-jobs/ko-en-doc-coverage-pass2/run-all.sh` | Passed |

## Remaining Risk

- External HTTP availability was not tested; P224 used source-link preservation and grep-based validation.
- English-only `FAQE` pages remain outside Korean-source semantic verification unless a later job explicitly audits them.
- Replaced Gliffy placeholders identify missing diagrams but do not recreate diagram content.
