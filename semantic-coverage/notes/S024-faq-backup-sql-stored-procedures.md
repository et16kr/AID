# S024 - FAQ backup SQL stored procedures

## Requirement and boundary

S024 performs a semantic-unit audit for FAQ categories `04. 백업 및 복구`, `05. SQL`, and `06. Stored Procedures` against the Korean-core English targets under `FAQE/Home/04. Backup and Recovery`, `FAQE/Home/05. SQL`, and `FAQE/Home/06. Stored Procedure`. The Korean source documents are authoritative.

Scoped Korean sources and English targets:

- `faq/Home/04. 백업 및 복구/04-01. aexport 및 iloader 이용__7341694.md` -> `FAQE/Home/04. Backup and Recovery/Using aexport and iloader__16876103.md`
- `faq/Home/04. 백업 및 복구/04-01. aexport 및 iloader 이용/04-01-01. aexport, iloader 란__7341696.md` -> `FAQE/Home/04. Backup and Recovery/Using aexport and iloader/What is aexport, iloader__16876105.md`
- `faq/Home/04. 백업 및 복구/04-01. aexport 및 iloader 이용/04-01-02. aexport 를 이용한 데이터베이스 객체 백업__7341698.md` -> `FAQE/Home/04. Backup and Recovery/Using aexport and iloader/Database object backup using aexport__22642949.md`
- `faq/Home/04. 백업 및 복구/04-01. aexport 및 iloader 이용/04-01-03. iloader 를 이용한 데이터 다운로드__7341700.md` -> `FAQE/Home/04. Backup and Recovery/Using aexport and iloader/Data download using iloader__16876147.md`
- `faq/Home/04. 백업 및 복구/04-01. aexport 및 iloader 이용/04-01-04. 데이터베이스 객체 생성 및 데이터 업로드__7341702.md` -> `FAQE/Home/04. Backup and Recovery/Using aexport and iloader/Create database object and upload data__16876145.md`
- `faq/Home/04. 백업 및 복구/04-02. Cold Backup한 것을 Directory 경로변경 하여 복구하는 방법__9110699.md` -> `FAQE/Home/04. Backup and Recovery/How to recover cold backup by changing directory path__16876133.md`
- `faq/Home/04. 백업 및 복구/04-03. Online Backup 및 Time Based Recovery 방법__9110695.md` -> `FAQE/Home/04. Backup and Recovery/Online Backup and Time Based Recovery__16876135.md`
- `faq/Home/05. SQL/05-01. varchar, char 타입 비교__9110650.md` -> `FAQE/Home/05. SQL/Comparison between VARCHAR and CHAR types__16876151.md`
- `faq/Home/05. SQL/05-02. 객체에 부여된 권한을 확인하는 방법__8454634.md` -> `FAQE/Home/05. SQL/How to check the privileges granted to an object__16876153.md`
- `faq/Home/06. Stored Procedures/06-01. Stored Procedure 내에서 DML 로 영향 받은 레코드 수 확인 방법__8454526.md` -> `FAQE/Home/06. Stored Procedure/How to check the number of records affected by DML within the stored procedure__16876157.md`
- `faq/Home/06. Stored Procedures/06-02. 저장 프로시저 내용 확인 방법__9110656.md` -> `FAQE/Home/06. Stored Procedure/How to check the contents of stored procedure__16876159.md`

This job does not audit FAQ category `03. 이중화`, FAQ category `07. 개발 및 API`, technical guides under `DOCK/Home`, English-only `FAQE` material, or the `llm-reference` consolidation workflow. Korean source files were not edited, and no English source document was deleted or moved.

## Required reading and direct inspection

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv`
- `semantic-coverage/doc-mapping.tsv`
- `semantic-coverage/notes/S023-faq-replication.md`
- The 11 Korean source documents and 11 mapped English target documents listed above

Previous J/P reports were used only for orientation. Coverage decisions in `semantic-coverage/matrices/S024-faq-backup-sql-stored-procedures.tsv` are based on direct inspection of the scoped Korean and English files.

## Pre-edit state

- Branch: `combine`
- Required handoff check command:

```bash
git status --porcelain --untracked-files=all -- . ":(exclude).codex-jobs" ":(exclude).codex-jobs/**"
```

- Result: no output. No uncommitted project files outside the workflow runtime area were present before S024 edits.
- `git status --short --branch` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified by the active workflow state with `S024` marked `Progress`.

## Design note

S024 adds semantic evidence only:

- Adds `semantic-coverage/matrices/S024-faq-backup-sql-stored-procedures.tsv`
- Adds `semantic-coverage/notes/S024-faq-backup-sql-stored-procedures.md`
- Updates S024 workflow status in `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv`

No English Markdown source file required a content edit, so `manifest.json` metadata did not require updates for this job. The documentation structure is unchanged.

## Audit summary

Matrix file: `semantic-coverage/matrices/S024-faq-backup-sql-stored-procedures.tsv`

Rows by coverage status:

- `covered`: 82
- `not_applicable`: 11

Rows by source:

- F04-01 parent `aexport`/`iloader`: 3 rows
- F04-01-01 `aexport`, `iloader` definitions: 5 rows
- F04-01-02 database object backup using `aexport`: 10 rows
- F04-01-03 data download using `iloader`: 14 rows
- F04-01-04 database object creation and data upload: 11 rows
- F04-02 cold backup restore with directory path changes: 9 rows
- F04-03 online backup and time based recovery: 14 rows
- F05-01 `VARCHAR`/`CHAR` comparison: 6 rows
- F05-02 object privilege query: 5 rows
- F06-01 `SQL%ROWCOUNT` in stored procedures: 4 rows
- F06-02 stored procedure content inspection: 12 rows

### Backup and recovery coverage

The `aexport` and `iloader` pages preserve the Korean-source utility definitions, extracted object list, separator settings, `$ALTIBASE_HOME/conf/aexport.properties` preparation, generated script names, `aexport` prompt behavior, `run_il_out.sh` download flows, `run_il_in.sh` upload flows, environment variables `ALTIBASE_NLS_USE` and `ILO_DATEFORM`, character-set verification through `V$NLS_PARAMETERS`, and log/error checks for `download.out`, `upload.out`, `*.fmt`, `*.log`, `*.dat`, and `Error Row Count`.

The cold-backup restore page preserves the path-change rules for memory DB, disk DB, logs, and loganchor files, `$ALTIBASE_HOME/conf/altibase.properties` properties (`MEM_DB_DIR`, `DEFAULT_DISK_DB_DIR`, `LOGANCHOR_DIR`, `LOG_DIR`, `ARCHIVE_DIR`), `CONTROL` startup, `ALTER DATABASE RENAME DATAFILE`, and final service startup output.

The online-backup and time-based recovery page preserves the archive-log-mode precondition, `V$ARCHIVE` check, `ALTER DATABASE ARCHIVELOG`, database/tablespace/loganchor online backup SQL, DBA tablespace backup with `V$STABLE_MEM_DATAFILES`, `ALTER SYSTEM SWITCH LOGFILE`, archive-log range identification through `V$LFG` and `altibase_sm.log`, `SYS_TBS_DISK_TEMP` recreation, `ALTER DATABASE RECOVER DATABASE UNTIL TIME`, `META RESETLOGS`, and the required full backup after log reset.

### SQL and stored procedure coverage

The SQL pages preserve the `VARCHAR`/`CHAR` comparison examples and the rule that `CHAR` comparison pads with `0x20` while `CHAR`/`VARCHAR` comparison uses valid `VARCHAR` data up to `0x00`. The SESC initialization guidance is preserved. The object privilege page preserves the full object-privilege query over `SYSTEM_.SYS_USERS_`, `SYSTEM_.SYS_GRANT_OBJECT_`, `SYSTEM_.SYS_PRIVILEGES_`, and `SYSTEM_.SYS_TABLES_`, including selected aliases and the grantable flag.

The stored procedure pages preserve `SQL%ROWCOUNT`, the `proc1` example, and the `SP_DML_RECORD_COUNT.txt` attachment. The stored procedure content page preserves both inspection approaches: helper procedures over `SYSTEM_.SYS_PROCEDURES_` and `SYSTEM_.SYS_PROC_PARSE_`, and `aexport`-based extraction through `ALL_CRT_PROC.sql`, user-specific `aexport`, and object-specific `aexport -object user_name.procedure_name` available from `ALTIBASE HDB 5.5.1`.

## Attachment and link evidence

The scoped S024 Korean source set contains one URL-backed text attachment:

- `SP_DML_RECORD_COUNT.txt` in `faq/Home/06. Stored Procedures/06-01. Stored Procedure 내에서 DML 로 영향 받은 레코드 수 확인 방법__8454526.md`

The exact filename and `docs.altibase.com/download/attachments/8454526` URL are preserved in `FAQE/Home/06. Stored Procedure/How to check the number of records affected by DML within the stored procedure__16876157.md`.

The scoped Korean source set contains no URL-backed document-format attachments with `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, or `.zip` extensions. The scoped document-format attachment preservation check therefore has no required document-format URLs to match.

Non-document links were checked as source-link semantics:

- The Korean parent `aexport`/`iloader` manual link is represented by the corresponding English manual page and GitHub manual link in the English target.
- Other scoped sources do not introduce URL-backed document-format attachments.

## Self-review

- Scope checked: S024 changed only S024 evidence files and the S024 workflow status.
- Korean authority checked: all 11 scoped Korean source files were inspected directly.
- English target checked: all 11 mapped English target files were inspected directly.
- Matrix checked: the S024 matrix uses the exact required TSV header, one physical row per matrix unit, allowed status values only, and no `missing`, `unverified`, or `recheck_required` rows.
- Terminology checked: product names, utility names, SQL, commands, properties, paths, version numbers, error codes, system views, and attachment filenames are preserved.
- Manifest checked: no English source Markdown was edited, so no `manifest.json` metadata update was required.

## Verification

Verification results after drafting, self-review, and fixes:

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json` | Pass |
| `git diff --check` | Pass |
| `find DOCK/Home -type f -name '*.md' \| wc -l` | Pass, `51` |
| `find faq/Home -type f -name '*.md' \| wc -l` | Pass, `115` |
| `find arch/Home -type f -name '*.md' \| wc -l` | Pass, `181` |
| `find FAQE/Home -type f -name '*.md' \| wc -l` | Pass, `241` |
| S024 TSV header, field-count, and status validation | Pass, 15 fields, 93 rows: `covered` 82, `not_applicable` 11 |
| S024 allowed-status validation | Pass |
| S024 scoped empty-link and macro-artifact grep | Pass, `rg` exit 1 expected no matches |
| S024 and full matrix unresolved-status grep | Pass, `rg` exit 1 expected no matches |
| Scoped document-format attachment preservation grep for `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.zip` | Pass, `rg` exit 1 expected no scoped document-format attachments |
| Scoped text attachment and manual-link grep | Pass, `SP_DML_RECORD_COUNT.txt` preserved; Korean manual link represented by English manual/GitHub links |

## Final decision

S024 final decision: `COMPLETE`.
