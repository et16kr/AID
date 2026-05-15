# P210 Java ODBC ADO.NET PHP Client APIs Audit

Date: 2026-05-16

## Scope

P210 audited Korean Java, unixODBC, Windows ODBC, ADO.NET, and PHP client API documents against their English `arch` targets.

| Korean source | English target |
| --- | --- |
| `DOCK/Home/32. Altibase와 unixODBC 연동 가이드__11698379.md` | `arch/Home/Altibase and unixODBC Integration Guide__14647413.md`; `arch/Home/Altibase and unixODBC Integration Guide/**` |
| `DOCK/Home/51. Altibase window ADO.NET 개발 가이드__11698513.md` | `arch/Home/Altibase Window ADO.NET Development Guide__14647565.md`; `arch/Home/Altibase Window ADO.NET Development Guide/**` |
| `DOCK/Home/53. Windows 환경의 Altibase ODBC 개발 가이드__13436856.md` | `arch/Home/Altibase ODBC Development Guide in Windows Environment__15138911.md` |
| `DOCK/Home/56. JAVA 개발 가이드__14057500.md` | `arch/Home/JAVA Developer's Guide__16875544.md` |
| `DOCK/Home/66. Altibase PHP 연동가이드__7341461.md` | `arch/Home/PHP Integration Guide for Altibase__14647305.md`; `arch/Home/PHP Integration Guide for Altibase/**` |

The Korean sources were treated as authoritative. No Korean source documents were edited.

## Boundary

- Completed only P210.
- Preserved the existing English parent and split-page hierarchy.
- Did not enter WAS/framework, SQL/tuning, migration/conversion, FAQ, attachment-wide revalidation, or final LLM consolidation jobs.
- The pre-existing pass2 `jobs.tsv` status change for P210 was inside the workflow runtime area and did not block execution.

## Design Note

No product behavior or repository architecture changed. Documentation structure changes were limited to restoring one missing Java semantic heading for simultaneous connections to different Altibase versions and reformatting flattened command/output blocks so client API procedures are searchable. Existing English split pages and source attachment placement were preserved.

## Findings And Updates

- Corrected scoped technical-support portal links that were exported as broken `[/en/]` concatenations while preserving the Korean-source support route.
- Updated unixODBC pages for Korean-source compile and integration semantics, including native compiler assumptions, `SQLLEN`/`SQLULEN`, `BUILD_LEGACY_64_BIT_MODE=1`, exact `./configure --prefix=/home/unixODBC --disable-gui --enable-threads=yes`, driver selection by `SQLLEN`, `odbcinst -j` output, AIX `libodbcinst.so.1`, and `[ODBC]` trace configuration.
- Replaced fake exported local-library links such as `libaltibase_odbc-64bit-ul64.so`, `libaltibase_odbc-64bit-ul32.so`, `libaltibase_odbc.so`, and `libodbcinst.so` with code literals.
- Corrected ADO.NET setup and error pages for `Altibase.Data.AltibaseClient.dll`, Windows terminology, `.NET Framework`, ADO.NET provider requirements, malformed Q&A link, `odbccli_sl.dll`, bit-specific `altiadonetX.X.X.X_32bit.zip` and `altiadonetX.X.X.X_64bit.zip`, and the `System.BadImageFormatException` DLL cause.
- Corrected Windows ODBC guide details for the Altibase `7.1.0` Windows ODBC cutoff, support/download links, Windows Client installation wording, control-panel setting table order, C# section wording, and flattened BLOB insert/select code comments.
- Corrected Java guide details for CLASSPATH setup wording, `AltibaseConnectionPoolDataSource`, `ABPoolingDataSource`, XA wording, missing simultaneous-version heading, `sessionfailover` CTF/STF explanation, `AltibasePSMCall.java`, `PreparedStatement`, `executeBatch()`, `setFetchSize()` memory warning, exact LOB autocommit error text, LOB sample paths, and timeout error table headers/messages.
- Corrected PHP pages for support wording, Altibase product naming, `db.php`, ODBC Manager wording, `--prefix` configure option, library path environment variables, `odbc.ini`, and standard ODBC function wording.
- Updated `manifest.json` metadata for all 12 edited English Markdown pages.

## Attachment And Link Evidence

- Scoped Korean source pages contain 3 URL-backed document-format attachments:
  - ADO.NET legacy PDF.
  - Windows ODBC legacy PDF.
  - Java legacy PDF.
- All 3 Korean-source PDF URLs are preserved in the scoped English target set.
- Scoped grep found no empty links, Confluence macro error markers, malformed support links, fake unixODBC local-library links, stale typo patterns checked for this job, or residual visible Korean text.

## Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p210-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Scoped grep for empty links, Confluence macro errors, malformed support links, fake unixODBC local links, stale typo patterns, and residual Korean text | Passed |
| Scoped document-format attachment preservation script | Passed, 3 Korean source URLs preserved |
| Scoped fenced-code balance check | Passed for all scoped English files |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 12 edited English pages |

## Remaining Risk

- External HTTP availability was not tested; P210 used grep-based source-link and attachment preservation checks.
- The PHP Korean source configure command appears to use single-dash options, but the English page now uses standard unixODBC `./configure --prefix=... --enable-...` option spelling consistent with the scoped unixODBC guide and technical intent.
- The PHP split page path and source URL still contain the pre-existing `ODBC Manger` spelling because this job did not rename source-exported files or alter page identity metadata.
