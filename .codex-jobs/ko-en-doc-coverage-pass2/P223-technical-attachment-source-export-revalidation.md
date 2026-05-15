# P223 Technical Attachment Source and Export Revalidation

Date: 2026-05-16

## Scope

P223 revalidated document-format attachments, external source links, empty Markdown links, legacy `#` attachment labels, `Error rendering macro`, `Unknown macro`, and known export artifacts across technical `arch` documents. Korean technical documents under `DOCK/Home` remained authoritative and were not edited.

## Boundary And Design Note

This job did not change product behavior, architecture, or the documentation hierarchy. Documentation edits were limited to correcting export-damaged or malformed external references in existing English `arch` pages and refreshing `manifest.json` metadata for those edited pages.

## Attachment Evidence

- Rechecked 42 URL-backed Korean technical document-format links:
  - 41 `docs.altibase.com/download/attachments` document links.
  - 1 external GeoServer importer plug-in ZIP link: `https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.2/extensions/geoserver-2.16.2-importer-plugin.zip/download`.
- All 42 URL-backed links are preserved in `arch/Home`; missing count is 0.
- Recorded 6 Korean-source legacy attachment labels that still use `#` and therefore have no downloadable URL to preserve:

| Korean source | Legacy label |
| --- | --- |
| `DOCK/Home/36. Altibase 개발가이드__7341274.md:800` | `ALTIBASE_개발가이드.pdf` |
| `DOCK/Home/36. Altibase 개발가이드__7341274.md:802` | `ALTIBASE_개발가이드_5.3.pdf` |
| `DOCK/Home/40. Oracle to Altibase 변환가이드__7341605.md:1156` | `ALTIBASE_Oracle_변환_가이드.pdf` |
| `DOCK/Home/40. Oracle to Altibase 변환가이드__7341605.md:1158` | `ORACLE_to_ALTIBASE_변환_가이드_5.5.pdf` |
| `DOCK/Home/44. APRE_C_C++ New Features & 업그레이드 가이드__13435760.md:385` | `APRE_New_Features_업그레이드_가이드.pdf` |
| `DOCK/Home/65. MSSQL to Altibase 변환가이드__7341431.md:577` | `ALTIBASE_MSSQL_변환가이드.pdf` |

## Findings And Updates

- Corrected two concatenated support-portal export artifacts:
  - `arch/Home/Altibase Oracle Conversion Guide__14647316.md`
  - `arch/Home/Disk Configuration Guide for Altibase__14647508.md`
- Corrected three Hibernate links where the final period was exported inside the URL:
  - `arch/Home/Hibernate Integration Guide for Altibase__14058388.md`
- Corrected MyBatis source links:
  - Added readable separation between `http://blog.mybatis.org/` and `http://mybatis.github.io/mybatis-3/`.
  - Removed the final period from the `http://mybatis.github.io/mybatis-3/en/` URL.
- Updated `manifest.json` metadata for all 5 edited English Markdown pages.

## Self-Review

- Rechecked document-format attachment extraction using the target extensions `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, and `.zip`.
- Rechecked `arch/Home` for empty Markdown links, `Error rendering macro`, `Unknown macro`, lowercase `unknown-macro` placeholder URLs, concatenated support links, and the corrected Hibernate/MyBatis malformed URL patterns.
- Rechecked edited-page `manifest.json` `body_chars` and `word_count` against current file length and whitespace token counts.

## Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p223-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK/Home -type f -name '*.md' \| wc -l` | 51 |
| `find faq/Home -type f -name '*.md' \| wc -l` | 115 |
| `find arch/Home -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE/Home -type f -name '*.md' \| wc -l` | 241 |
| Technical document-format attachment preservation script | Passed, 42 URL-backed links preserved and 0 missing |
| Legacy `#` technical attachment label inventory | Passed, 6 labels recorded separately |
| `arch/Home` empty-link/export-artifact grep | Passed, no matches |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 5 edited English pages |
| `bash -n .codex-jobs/ko-en-doc-coverage-pass2/run_all.sh` and `bash -n .codex-jobs/ko-en-doc-coverage-pass2/run-all.sh` | Passed |

## Remaining Risk

- External HTTP availability was not tested; P223 used source-link preservation and grep-based validation.
- The six legacy `#` attachment labels remain non-downloadable because the Korean source does not provide URLs.
- P223 corrected link/export artifacts only. It did not perform another sentence-level Korean-to-English semantic audit of the edited English pages.
