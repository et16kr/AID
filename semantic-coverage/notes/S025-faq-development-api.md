# S025 - FAQ development API

## Requirement and boundary

S025 performs a semantic-unit audit for FAQ category `07. 개발 및 API` against the Korean-core English targets under `FAQE/Home/07. Development and API`. The Korean source documents are authoritative.

Scoped Korean sources and English targets:

- `faq/Home/07. 개발 및 API/07-01. Connection 연결이 끊어지는 경우와 각 경우의 에러 코드 및 에러 메세지(APRE_C_C++, SQLCLI)__9110022.md` -> `FAQE/Home/07. Development and API/Connection disconnection, error codes, and error messages in each case (APRE_C_C++, SQLCLI)__16876167.md`
- `faq/Home/07. 개발 및 API/07-02. JDBC/07-02-01. Altibase JDBC에서 Fail-Over 사용하는 방법은__9110740.md` -> `FAQE/Home/07. Development and API/JDBC/How to use Fail-Over in Altibase JDBC__16876173.md`
- `faq/Home/07. 개발 및 API/07-02. JDBC/07-02-02. jdbc.trc 파일 생성 위치 변경 방법__8454703.md` -> `FAQE/Home/07. Development and API/JDBC/How to change the jdbc.trc file creation location__16876175.md`
- `faq/Home/07. 개발 및 API/07-02. JDBC/07-02-03. JDBC를 통한 서로 다른 Altibase 버전 동시 접속__22642863.md` -> `FAQE/Home/07. Development and API/JDBC/Simultaneous connections to different Altibase versions via JDBC__22642951.md`
- `faq/Home/07. 개발 및 API/07-03. ODBC/07-03-01. 64-bit Windows에서 32-bit ODBC 설치__9110670.md` -> `FAQE/Home/07. Development and API/ODBC/32-bit ODBC installation on 64-bit Windows__22642957.md`
- `faq/Home/07. 개발 및 API/07-03. ODBC/07-03-02. ODBC 함수, SQLFreeStmt__9110024.md` -> `FAQE/Home/07. Development and API/ODBC/ODBC function, SQLFreeStmt__16876183.md`
- `faq/Home/07. 개발 및 API/07-03. ODBC/07-03-03. unix_odbc와 연동하기__9110646.md` -> `FAQE/Home/07. Development and API/ODBC/Integrating with unix_odbc__16876187.md`
- `faq/Home/07. 개발 및 API/07-04. PHP/07-04-01. php 사용중인데 한글이 깨집니다__8454801.md` -> `FAQE/Home/07. Development and API/PHP/Hangul is broken when using php__16876191.md`
- `faq/Home/07. 개발 및 API/07-05. Spring+iBatis 트랜잭션 관리 방법__9109742.md` -> `FAQE/Home/07. Development and API/How to manage Spring+iBatis transaction__16876194.md`

This job does not audit FAQ categories outside `07. 개발 및 API`, technical guides under `DOCK/Home`, English-only `FAQE` material, or the `llm-reference` consolidation workflow. Korean source files were not edited, and no English source document was deleted or moved.

## Required reading and direct inspection

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv`
- `semantic-coverage/doc-mapping.tsv`
- `semantic-coverage/notes/S024-faq-backup-sql-stored-procedures.md`
- The nine Korean source documents and nine mapped English target documents listed above

Previous J/P reports were used only for orientation. Coverage decisions in `semantic-coverage/matrices/S025-faq-development-api.tsv` are based on direct inspection of the scoped Korean and English files.

## Pre-edit state

- Branch: `combine`
- Required handoff check command:

```bash
git status --porcelain --untracked-files=all -- . ":(exclude).codex-jobs" ":(exclude).codex-jobs/**"
```

- Result: no output. No uncommitted project files outside the workflow runtime area were present before S025 edits.
- `git status --short --branch` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified by the active workflow state with `S025` marked `Progress`.

## Design note

S025 adds semantic evidence only:

- Adds `semantic-coverage/matrices/S025-faq-development-api.tsv`
- Adds `semantic-coverage/notes/S025-faq-development-api.md`
- Updates S025 workflow status in `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv`

No English Markdown source file required a content edit, so `manifest.json` metadata did not require updates for this job. The documentation structure is unchanged.

## Audit summary

Matrix file: `semantic-coverage/matrices/S025-faq-development-api.tsv`

Rows by coverage status:

- `covered`: 99
- `not_applicable`: 9

Rows by source:

- F07-01 connection disconnection and APRE/SQLCLI error codes: 18 rows
- F07-02-01 Altibase JDBC Fail-Over: 14 rows
- F07-02-02 `jdbc.trc` creation location: 9 rows
- F07-02-03 simultaneous JDBC connections to different Altibase versions: 8 rows
- F07-03-01 32-bit ODBC on 64-bit Windows: 10 rows
- F07-03-02 `SQLFreeStmt`: 9 rows
- F07-03-03 unixODBC integration: 17 rows
- F07-04-01 PHP Hangul troubleshooting: 10 rows
- F07-05 Spring+iBatis transaction management: 13 rows

### Connection, JDBC, and ODBC coverage

The connection-disconnection page preserves the Korean-source APRE*C/C++ and SQLCLI/ODBC diagnostic fields, connection-not-established causes, timeout behavior, error outputs, and final SQLSTATE/SQLCODE categories for `08001`, `08003`, and `08S01`.

The JDBC Fail-Over page preserves CTF/STF definitions, `AlternateServer`, `ConnectionRetryCount`, `ConnectionRetryDelay`, `LoadBalance`, `SessionFailOver`, `FailOver_Source`, `HealthCheckDuration`, version-specific SQLSTATE checks (`08F01`, `ES_08FO01`), the Java sample, and manual references.

The `jdbc.trc` page preserves creation timing, fail-over event-trace use, file names, version conditions, `$ALTIBASE_HOME/trc` location behavior, lock-file error guidance, and `ALTIBASE_JDBC_TRCLOG_DISABLE` methods by version.

The multiversion JDBC page preserves the Altibase 7.3 basis, `Altibase7_3.jar`, both driver class names, `$ALTIBASE_HOME/lib`, the `java -jar Altibase7_3.jar` version check, and the 7.1/7.3 simultaneous connection example.

The 32-bit Windows ODBC page preserves the support limit through Altibase 6.5.1, no 32-bit ODBC driver support from 7.1, installer filename examples, `C:\windows\sysWOW64\odbcad32.exe`, DSN creation, `PORT_NO`/`ALTIBASE_PORT_NO`, and SQL checks for `V$DATABASE` and `V$NLS_PARAMETERS`.

The `SQLFreeStmt` page preserves all four options (`SQL_CLOSE`, `SQL_DROP`, `SQL_UNBIND`, `SQL_RESET_PARAMS`) and the practical distinction between freeing a statement handle and closing a cursor for reuse.

### unixODBC, PHP, and Spring+iBatis coverage

The unixODBC page preserves the `http://www.unixodbc.org/` download URL, source-authoritative configure command `./configure -prefix=/home/wonsik/ODBC_HOME --enable-gui=no --enable-threads=yes`, option descriptions, `pthread_sigmask` error case, build/install commands, `dltest`, `odbc.ini`, `ODBCINI`, `odbc_config --ulen`, `isql` connection output, PHP/PERL integration, PHP environment variables, `SQLLEN`/`SQLULEN` checks, `LongDataCompat=ON`, PHP configure options, and `php.ini` settings.

The PHP Hangul troubleshooting page preserves unixODBC and Altibase ODBC driver architecture, the diagnostic order from unixODBC to PHP to web server/page charset, `NLS_USE`, the `odbc.ini` sample with `NLS_USE = MS949`, Windows `chcp 65001`, Secure CRT Unicode settings, and `odbc.defaultlrl` guidance for large `varchar`/`clob` output.

The Spring+iBatis page preserves BMT and CMT method categories, common `applicationContext.xml`, direct `DataSourceTransactionManager` use with exact `setAutoCommit(false)`, `TransactionTemplate`, `tx:advice`, `TransactionProxyFactoryBean`, `@Transactional(propagation=Propagation.REQUIRED)`, the `AltibaseClobStringTypeHandler` CLOB 0-byte note, and the `LobSpringIbatisSample.zip` attachment.

## Attachment and link evidence

The scoped S025 Korean source set contains one URL-backed document-format attachment:

- `LobSpringIbatisSample.zip` in `faq/Home/07. 개발 및 API/07-05. Spring+iBatis 트랜잭션 관리 방법__9109742.md`

The exact filename and `docs.altibase.com/download/attachments/9109742/LobSpringIbatisSample.zip` URL are preserved in `FAQE/Home/07. Development and API/How to manage Spring+iBatis transaction__16876194.md`.

The scoped Korean and English development/API pages contain no empty Markdown links or Confluence macro-rendering markers. Non-document links were checked as source-link semantics, including support portal/manual links, `http://www.unixodbc.org/`, the JDBC Fail-Over JBOSS integration reference, and the PHP integration guide reference.

## Self-review

- Scope checked: S025 changed only S025 evidence files and the S025 workflow status.
- Korean authority checked: all nine scoped Korean source files were inspected directly.
- English target checked: all nine mapped English target files were inspected directly.
- Matrix checked: the S025 matrix uses the exact required TSV header, one physical row per matrix unit, allowed status values only, and no `missing`, `unverified`, or `recheck_required` rows.
- Terminology checked: product names, API names, commands, SQL, configuration properties, paths, error codes, version numbers, Java/XML/PHP snippets, and attachment filenames are preserved.
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
| S025 TSV header, field-count, and status validation | Pass, 15 fields, 108 rows: `covered` 99, `not_applicable` 9 |
| S025 allowed-status validation | Pass |
| S025 scoped empty-link and macro-artifact grep on scoped product docs | Pass, `rg` exit 1 expected no matches |
| S025 and full matrix unresolved-status grep | Pass, `rg` exit 1 expected no matches |
| Scoped document-format attachment preservation grep for `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.zip` | Pass, `LobSpringIbatisSample.zip` preserved in Korean source and English target |
| Scoped source-link and attachment grep | Pass, checked `LobSpringIbatisSample.zip`, `http://www.unixodbc.org/`, `ALTIBASE_JDBC_TRCLOG_DISABLE`, `setAutoCommit(false)`, `08F01`, `ES_08FO01`, `SQLFreeStmt`, and `NLS_USE` |

## Final decision

S025 final decision: `COMPLETE`.
