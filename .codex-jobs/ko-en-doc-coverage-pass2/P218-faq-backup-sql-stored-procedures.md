# P218 FAQ Backup, SQL, and Stored Procedures Audit

Date: 2026-05-16

## Scope

P218 audited Korean FAQ categories `04. 백업 및 복구`, `05. SQL`, and `06. Stored Procedures` against the corresponding English `FAQE` targets. Korean FAQ pages remained authoritative and were not edited.

| Korean source | English target |
| --- | --- |
| `faq/Home/04. 백업 및 복구/04-01. aexport 및 iloader 이용__7341694.md` | `FAQE/Home/04. Backup and Recovery/Using aexport and iloader__16876103.md` |
| `faq/Home/04. 백업 및 복구/04-01. aexport 및 iloader 이용/04-01-01. aexport, iloader 란__7341696.md` | `FAQE/Home/04. Backup and Recovery/Using aexport and iloader/What is aexport, iloader__16876105.md` |
| `faq/Home/04. 백업 및 복구/04-01. aexport 및 iloader 이용/04-01-02. aexport 를 이용한 데이터베이스 객체 백업__7341698.md` | `FAQE/Home/04. Backup and Recovery/Using aexport and iloader/Database object backup using aexport__22642949.md` |
| `faq/Home/04. 백업 및 복구/04-01. aexport 및 iloader 이용/04-01-03. iloader 를 이용한 데이터 다운로드__7341700.md` | `FAQE/Home/04. Backup and Recovery/Using aexport and iloader/Data download using iloader__16876147.md` |
| `faq/Home/04. 백업 및 복구/04-01. aexport 및 iloader 이용/04-01-04. 데이터베이스 객체 생성 및 데이터 업로드__7341702.md` | `FAQE/Home/04. Backup and Recovery/Using aexport and iloader/Create database object and upload data__16876145.md` |
| `faq/Home/04. 백업 및 복구/04-02. Cold Backup한 것을 Directory 경로변경 하여 복구하는 방법__9110699.md` | `FAQE/Home/04. Backup and Recovery/How to recover cold backup by changing directory path__16876133.md` |
| `faq/Home/04. 백업 및 복구/04-03. Online Backup 및 Time Based Recovery 방법__9110695.md` | `FAQE/Home/04. Backup and Recovery/Online Backup and Time Based Recovery__16876135.md` |
| `faq/Home/05. SQL/05-01. varchar, char 타입 비교__9110650.md` | `FAQE/Home/05. SQL/Comparison between VARCHAR and CHAR types__16876151.md` |
| `faq/Home/05. SQL/05-02. 객체에 부여된 권한을 확인하는 방법__8454634.md` | `FAQE/Home/05. SQL/How to check the privileges granted to an object__16876153.md` |
| `faq/Home/06. Stored Procedures/06-01. Stored Procedure 내에서 DML 로 영향 받은 레코드 수 확인 방법__8454526.md` | `FAQE/Home/06. Stored Procedure/How to check the number of records affected by DML within the stored procedure__16876157.md` |
| `faq/Home/06. Stored Procedures/06-02. 저장 프로시저 내용 확인 방법__9110656.md` | `FAQE/Home/06. Stored Procedure/How to check the contents of stored procedure__16876159.md` |

## Boundary And Design Note

This job did not change product behavior, architecture, or the documentation hierarchy. The existing FAQE category and child-page structure was preserved. Documentation edits were limited to Korean-source semantic corrections, missing version context, clearer command/result explanations, and natural technical English inside existing pages.

## Findings And Updates

- No English change was needed for the `Using aexport and iloader` parent page or the `What is aexport, iloader?` definition page; their overview, object list, version condition for `Materialized View`, and manual links already matched the Korean sources semantically.
- Corrected the `aexport` database-object backup page so `.sql` files and `.sh` files are described with their Korean-source roles: `.sql` files contain object creation statements, and `.sh` files execute those `.sql` files in one batch.
- Restored the Korean-source `ALTIBASE HDB version 5` availability condition for checking `NLS_USE` and `NLS_CHARACTERSET` in the `iloader` data download page.
- Clarified `run_il_out.sh`, `run_il_in.sh`, foreground/background execution, table-specific extraction, log-checking, and `DBUSER_TABLENAME.log`/`USERNAME_TABLENAME.dat` explanations while preserving the Korean-source commands.
- Clarified cold-backup path-change wording for `$ALTIBASE_HOME/conf/altibase.properties` and the iSQL datafile rename step.
- Clarified online backup and time-based recovery wording for `CONTROL`, `ALTER SYSTEM SWITCH LOGFILE`, Archivelog Mode recovery prerequisites, 10-minute-before-deletion recovery, and recreating the `SYS_TBS_DISK_TEMP` data file.
- Rewrote the `VARCHAR`/`CHAR` comparison explanation so the `0x20` padding and `0x00` valid-data comparison rules are explicit.
- Clarified SQL comments in the object privilege query without changing the SQL, system tables, or aliases.
- Added code formatting and clearer wording for `SQL%ROWCOUNT`, `SYSTEM_.SYS_PROCEDURES_`, `SYSTEM_.SYS_PROC_PARSE_`, `ALL_CRT_PROC.sql`, and `aexport` stored-procedure extraction options.
- Updated `manifest.json` metadata for all 9 edited English Markdown pages.

## Attachment And Link Evidence

- The scoped Korean source set contains 1 URL-backed attachment/reference with a document or text-file extension: `SP_DML_RECORD_COUNT.txt`.
- The exact `SP_DML_RECORD_COUNT.txt` URL is preserved in the scoped English target.
- Scoped backup/SQL/stored-procedure pages contain no missing empty Markdown links, `Error rendering macro`, or `Unknown macro` markers.

## Self-Review

- Rechecked all scoped Korean/English pairs by semantic unit, including headings, bullets, procedure steps, commands, SQL, configuration/environment variables, warning-style notes, version conditions, and attachment links.
- Rechecked changed English pages for residual Korean prose, stale export artifacts, unclear generated-script wording, and inconsistent technical terminology.
- Rechecked `manifest.json` `body_chars` and `word_count` against the edited English page contents.

## Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p218-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 9 edited English pages |
| Scoped document/text attachment preservation script | Passed, 1 Korean source attachment URL preserved |
| Scoped stale-pattern grep | Passed, no matches |

## Remaining Risk

- External HTTP availability was not tested; P218 used source-link preservation and grep-based checks.
- The Korean source preserves probable command/output typos such as `ls --l run_il_out.sh` and `tail -f download.d.out`. Because Korean source command text is authoritative for this audit, the English target preserves those commands and records this as a source-review risk rather than inferring corrections.
