# S021 - FAQ operation core

## Requirement and boundary

S021 performs a semantic-unit audit for FAQ category `02. 운영 및 관리` operation-core topics: security, users, sessions, clients/IPC, startup, shutdown, SYS password, database name changes, and related administrative procedures.

Scoped Korean sources and English targets are the S021 rows in `semantic-coverage/doc-mapping.tsv`:

- `faq/Home/02. 운영 및 관리/02-01. [Linux] Altibase 서버 프로세스 자동 시작 스크립트 등록 방법__12517478.md` -> `FAQE/Home/02. Operation and Management/[Linux] How to register Altibase server process auto start script__16875947.md`
- `faq/Home/02. 운영 및 관리/02-03. Database 를 stop 하고 start 하는 방법__9764972.md` -> `FAQE/Home/02. Operation and Management/How to start and stop the database__22642937.md`
- `faq/Home/02. 운영 및 관리/02-04. Database 의 db name을 바꾸는 방법__10059840.md` -> `FAQE/Home/02. Operation and Management/How to change the database's db name__16875966.md`
- `faq/Home/02. 운영 및 관리/02-06. DB 이름 변경 후 server create 오류발생시__8454421.md` -> `FAQE/Home/02. Operation and Management/When server create errors occur after DB name change__16875972.md`
- `faq/Home/02. 운영 및 관리/02-08. HP-UX에서 부팅 시 알티베이스를 자동으로 시작(startup)하는 방법__9110724.md` -> `FAQE/Home/02. Operation and Management/How to startup Altibase automatically when booting from HP-UX__16875976.md`
- `faq/Home/02. 운영 및 관리/02-09. IPC 통신을 위한 알티베이스 서버 설정__9110665.md` -> `FAQE/Home/02. Operation and Management/Altibase Server Configuration for IPC Communication__22642933.md`
- `faq/Home/02. 운영 및 관리/02-10. LOCK TIMEOUT 발생 시 조치 방법__9110702.md` -> `FAQE/Home/02. Operation and Management/How to resolve when LOCK TIMEOUT occurs__16875984.md`
- `faq/Home/02. 운영 및 관리/02-11. Lock 잡고 있는 세션을 강제로 종료하는 방법__9110706.md` -> `FAQE/Home/02. Operation and Management/How to forcefully close a session that is being locked__16875986.md`
- `faq/Home/02. 운영 및 관리/02-13. PUBLIC SYNONYM 을 삭제해도 되나요__6520939.md` -> `FAQE/Home/02. Operation and Management/Can PUBLIC SYNONYM be dropped__16875993.md`
- `faq/Home/02. 운영 및 관리/02-14. Solaris에서 OS booting 시 자동 altibase startup__9110643.md` -> `FAQE/Home/02. Operation and Management/Automatic altibase startup during OS booting in Solaris__16875996.md`
- `faq/Home/02. 운영 및 관리/02-15. sys 유저 패스워드 변경 방법__6521708.md` -> `FAQE/Home/02. Operation and Management/How to change sys user password__16876004.md`
- `faq/Home/02. 운영 및 관리/02-18. 데이터베이스 보안 점검 체크리스트__6521702.md` -> `FAQE/Home/02. Operation and Management/Database Security Checklist__22642935.md`
- `faq/Home/02. 운영 및 관리/02-19. 동시 접속 세션 수(MAX_CLIENT) 증가 시 고려사항__7341076.md` -> `FAQE/Home/02. Operation and Management/Notes_Considerations when increasing the number of concurrent connection sessions (MAX_CLIENT)__16876028.md`
- `faq/Home/02. 운영 및 관리/02-21. 사용자 생성(CREATE USER) 및 패스워드 변경(ALTER USER) 방법__9110757.md` -> `FAQE/Home/02. Operation and Management/How to create a user (CREATE USER) and change a password (ALTER USER)__16876036.md`
- `faq/Home/02. 운영 및 관리/02-22. 사용자 패스워드 길이 제약 - 버전 별 차이__7341322.md` -> `FAQE/Home/02. Operation and Management/User password length limitation - Differences by version__22642941.md`
- `faq/Home/02. 운영 및 관리/02-27. OS시간과 DB시간이 맞질 않습니다__22642857.md` -> `FAQE/Home/02. Operation and Management/The OS time and the DB time do not match__22642939.md`

This job does not audit S022 storage/resource/log/JOB/charset operation topics, does not run the `llm-reference` consolidation workflow, does not edit Korean source documents, and does not delete or move English source documents.

## Required reading and direct inspection

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv`
- `semantic-coverage/doc-mapping.tsv`
- The 16 Korean source documents and 16 mapped English target documents listed above

Previous J/P reports were used only as orientation. Coverage decisions in `semantic-coverage/matrices/S021-faq-operation-core.tsv` are based on direct inspection of the scoped Korean and English files.

## Pre-edit state

- Branch: `combine`
- Initial `git status --short` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified inside the workflow area as `S021` was already in `Progress`.
- No uncommitted project files outside the workflow runtime area were present before S021 edits.

## Design note

S021 adds semantic evidence and one narrow English documentation correction:

- Adds `semantic-coverage/matrices/S021-faq-operation-core.tsv`
- Adds `semantic-coverage/notes/S021-faq-operation-core.md`
- Corrects the start/stop FAQ iSQL example from `SERVER = 127.0.0.1` to `SERVER = localhost` so it matches the Korean source output
- Updates S021 workflow status in `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv`

The documentation structure is unchanged. `manifest.json` did not require a content-metadata change for the edited start/stop page because the replacement has the same character count and word count as the previous text; the manifest entry remains `body_chars: 13808` and `word_count: 1591`, matching the edited file.

## Audit summary

Matrix file: `semantic-coverage/matrices/S021-faq-operation-core.tsv`

Rows by coverage status:

- `covered`: 112
- `added`: 1
- `not_applicable`: 18

Rows by source:

- F02-01 Linux automatic startup: 14 rows
- F02-03 database start/stop: 10 rows
- F02-04 database name change: 7 rows
- F02-06 server create error after DB name change: 5 rows
- F02-08 HP-UX automatic startup: 9 rows
- F02-09 IPC server configuration: 9 rows
- F02-10 LOCK TIMEOUT handling: 7 rows
- F02-11 lock-holding session close: 5 rows
- F02-13 PUBLIC SYNONYM drop/create: 5 rows
- F02-14 Solaris automatic startup: 7 rows
- F02-15 SYS password change: 6 rows
- F02-18 database security checklist: 22 rows
- F02-19 MAX_CLIENT increase considerations: 9 rows
- F02-21 user creation/password change: 4 rows
- F02-22 password length by version: 6 rows
- F02-27 OS time vs DB time mismatch: 6 rows

### Startup and shutdown procedures

The Linux, HP-UX, and Solaris automatic startup pages preserve the Korean-source scripts and identifiers for `systemctl`, `chkconfig`, `altibased.service`, SELinux mode handling, HP-UX `/sbin/init.d` and `/sbin/rc2.d`, and Solaris `/etc/init.d` and `/etc/rc3.d` workflows.

The Solaris Korean source still contains Confluence `Unknown macro` export artifacts inside script blocks. The English target contains reconstructed shell blocks that preserve the recoverable identifiers and commands: `/etc/alti-conf.d/alti.conf`, `ALTIBASE_HOME`, `ALTIBASE_OWNER`, `START_ALTIBASE`, `isql -s 127.0.0.1 -u sys -p manager -sysdba`, `startup`, `shutdown immediate`, and `/etc/init.d/altibase <start|stop>`.

### Core administration

The start/stop, database name change, DB-name-related `server create` error, SYS password change, IPC configuration, MAX_CLIENT, user creation/password change, password length, and OS time mismatch FAQs preserve the Korean-source commands, SQL, property names, version conditions, and operational warnings.

S021 corrected one exact-output mismatch in the start/stop FAQ:

- Korean source: `ISQL_CONNECTION = TCP, SERVER = localhost, PORT_NO = 20370`
- English target before S021: `ISQL_CONNECTION = TCP, SERVER = 127.0.0.1, PORT_NO = 20370`
- English target after S021: `ISQL_CONNECTION = TCP, SERVER = localhost, PORT_NO = 20370`

### Security and sessions

The security checklist preserves the Korean-source checks and remediation steps for user inventory, default `sys/manager` password, system privileges, `WITH GRANT OPTION`, script/config/log file permissions, trace file permissions, shell history, public/private synonyms, account lockout, password complexity, password lifetime, `PORT_NO`, `IDLE_TIMEOUT`, auditing, `ACCESS_LIST`, `REMOTE_SYSDBA_ENABLE`, and patch-note references.

The session-related FAQs preserve the lock-timeout and session-close SQL using `SYSTEM_.SYS_TABLES_`, `V$LOCK`, `V$SESSION`, `V$STATEMENT`, `ALTER DATABASE mydb SESSION CLOSE`, and the rollback caution for sessions that cannot be disconnected until rollback completes.

## Attachment and link evidence

The scoped S021 Korean and English source files contain 0 URL-backed document-format attachments with `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, or `.zip` extensions.

Non-document operational links were checked as source-link semantics:

- Linux SELinux documentation is represented with the corresponding English Red Hat documentation URL.
- IPC, MAX_CLIENT, auditing, and security checklist manual references are represented with English support/manual or GitHub manual links.
- Korean cross-reference links to other FAQ pages are represented with corresponding English FAQE links where available.

## Self-review

- Scope checked: S021 changed only the scoped English start/stop FAQ, S021 evidence files, and S021 workflow status.
- Korean authority checked: all 16 scoped Korean source files were inspected directly.
- English target checked: all 16 mapped English target files were inspected directly.
- Matrix checked: the S021 matrix uses the exact required TSV header, one physical row per matrix unit, allowed status values only, and no `missing`, `unverified`, or `recheck_required` rows.
- Terminology checked: product names, commands, SQL, property names, paths, version numbers, error codes, support URLs, and system view names are preserved.
- Manifest checked: edited-page manifest metadata still matches the edited English file (`body_chars: 13808`, `word_count: 1591`).

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
| S021 TSV header, field-count, and status validation | Pass, 15 fields, 131 rows: `covered` 112, `added` 1, `not_applicable` 18 |
| S021 scoped empty-link and macro-artifact grep | Pass, `rg` exit 1 expected no matches |
| S021 and full matrix unresolved-status grep | Pass, `rg` exit 1 expected no matches |
| Scoped document-format attachment grep for `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.zip` | Pass, `rg` exit 1 expected no URL-backed document-format attachments |
| Edited-page manifest metadata comparison | Pass, manifest/file values match: `13808 13808 1591 1591` |

## Final decision

S021 final decision: `COMPLETE`.
