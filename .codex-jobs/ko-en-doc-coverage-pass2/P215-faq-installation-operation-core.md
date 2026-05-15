# P215 FAQ Installation and Operation Core Audit

Date: 2026-05-16

## Scope

P215 audited Korean FAQ category `01. 설치, 패치, 업그레이드` and the core category `02. 운영 및 관리` operation/security/user/session/client-configuration documents against the corresponding English `FAQE` targets. Korean FAQ pages remained authoritative and were not edited.

| Korean source | English target |
| --- | --- |
| `faq/Home/01. 설치, 패치, 업그레이드/01-01. Altibase HDB가 지원하는 플랫폼(OS)은__9110736.md` | `FAQE/Home/01. Installation, Patch, Upgrade/What Platforms (OS) Altibase HDB supports__16875920.md` |
| `faq/Home/01. 설치, 패치, 업그레이드/01-02. Unix 및 Linux 에서 알티베이스 서버 패치 절차__8454397.md` | `FAQE/Home/01. Installation, Patch, Upgrade/Altibase Server Patch Procedure on Unix and Linux__16875922.md` |
| `faq/Home/01. 설치, 패치, 업그레이드/01-03. 알티베이스 클라이언트 설치 방법(ALTIBASE HDB 5.5.1 부터)__8455011.md` | `FAQE/Home/01. Installation, Patch, Upgrade/Altibase Client Installation/Starting from ALTIBASE HDB 5.5.1__16875941.md` |
| `faq/Home/01. 설치, 패치, 업그레이드/01-04. 윈도우에서 알티베이스 설치 할 때 _이미 설치가 되었다_고 합니다__8454409.md` | `FAQE/Home/01. Installation, Patch, Upgrade/What to do when installing Altibase on Windows, and it says _It has already been installed__16875943.md` |
| `faq/Home/02. 운영 및 관리/02-03. Database 를 stop 하고 start 하는 방법__9764972.md` | `FAQE/Home/02. Operation and Management/How to start and stop the database__22642937.md` |
| `faq/Home/02. 운영 및 관리/02-04. Database 의 db name을 바꾸는 방법__10059840.md` | `FAQE/Home/02. Operation and Management/How to change the database's db name__16875966.md` |
| `faq/Home/02. 운영 및 관리/02-06. DB 이름 변경 후 server create 오류발생시__8454421.md` | `FAQE/Home/02. Operation and Management/When server create errors occur after DB name change__16875972.md` |
| `faq/Home/02. 운영 및 관리/02-09. IPC 통신을 위한 알티베이스 서버 설정__9110665.md` | `FAQE/Home/02. Operation and Management/Altibase Server Configuration for IPC Communication__22642933.md` |
| `faq/Home/02. 운영 및 관리/02-10. LOCK TIMEOUT 발생 시 조치 방법__9110702.md` | `FAQE/Home/02. Operation and Management/How to resolve when LOCK TIMEOUT occurs__16875984.md` |
| `faq/Home/02. 운영 및 관리/02-11. Lock 잡고 있는 세션을 강제로 종료하는 방법__9110706.md` | `FAQE/Home/02. Operation and Management/How to forcefully close a session that is being locked__16875986.md` |
| `faq/Home/02. 운영 및 관리/02-15. sys 유저 패스워드 변경 방법__6521708.md` | `FAQE/Home/02. Operation and Management/How to change sys user password__16876004.md` |
| `faq/Home/02. 운영 및 관리/02-17. TRANSACTION_TABLE_SIZE 변경 시 고려사항__7341337.md` | `FAQE/Home/02. Operation and Management/Notes_Considerations when changing TRANSACTION_TABLE_SIZE__16876013.md` |
| `faq/Home/02. 운영 및 관리/02-18. 데이터베이스 보안 점검 체크리스트__6521702.md` | `FAQE/Home/02. Operation and Management/Database Security Checklist__22642935.md` |
| `faq/Home/02. 운영 및 관리/02-19. 동시 접속 세션 수(MAX_CLIENT) 증가 시 고려사항__7341076.md` | `FAQE/Home/02. Operation and Management/Notes_Considerations when increasing the number of concurrent connection sessions (MAX_CLIENT)__16876028.md` |
| `faq/Home/02. 운영 및 관리/02-21. 사용자 생성(CREATE USER) 및 패스워드 변경(ALTER USER) 방법__9110757.md` | `FAQE/Home/02. Operation and Management/How to create a user (CREATE USER) and change a password (ALTER USER)__16876036.md` |
| `faq/Home/02. 운영 및 관리/02-22. 사용자 패스워드 길이 제약 - 버전 별 차이__7341322.md` | `FAQE/Home/02. Operation and Management/User password length limitation - Differences by version__22642941.md` |
| `faq/Home/02. 운영 및 관리/02-27. OS시간과 DB시간이 맞질 않습니다__22642857.md` | `FAQE/Home/02. Operation and Management/The OS time and the DB time do not match__22642939.md` |

## Boundary And Design Note

This job did not change product behavior, architecture, or the documentation hierarchy. The existing FAQE file structure was preserved. Documentation-structure edits were limited to restoring missing Korean-source semantic units inside existing English pages, including the client-install directory listing and the security checklist `ACCESS_LIST` example.

P216 scope was left untouched: remaining category 02 storage, log, tablespace, job, resource, auto-start, character-set, and operational-change FAQ pages were not audited in this job.

## Findings And Updates

- No English change was needed for the platform support, `CREATE USER`/`ALTER USER`, or OS/DB time FAQ pages; their English content already matched the Korean-source meaning for the scoped semantic units.
- Corrected the Unix/Linux server patch FAQ for patch-vs-upgrade wording, 5.5.1 version boundaries, `$ALTIBASE_HOME`, replication gap wording, step references, `CHECK_LOGFILE = 0`, SQL comments, and replication start/drop wording.
- Restored the missing client-install directory structure block and clarified OS-user upload, installer prompts, shell initialization files, and connection-test placeholders.
- Clarified the Windows registry cleanup path and final installation-retry sentence.
- Corrected start/stop output examples and wording for `server start`, `isql -sysdba`, listener ports, IPC listener output, `Command executed successfully.`, and the `ERR-4107A` message.
- Clarified DB-name recreation data-loss wording and converted the server-create error script example to a searchable code block.
- Corrected IPC communication wording for Unix Domain Socket (UDS), version scope, and AIX/Windows recommendation grammar.
- Corrected lock/session FAQs so `ALTER DATABASE ... SESSION CLOSE` guidance refers to sessions that hold locks, target-session impact, wrong-session risk, and rollback/session-close behavior.
- Improved SYS password troubleshooting by making the `altipasswd` role explicit and formatting the `server` script password check as code.
- Clarified `TRANSACTION_TABLE_SIZE` offline-change wording, `ALTER SYSTEM` read-only behavior, step 2 backup reload wording, and the memory-usage heading.
- Updated the security checklist for Korean-source defaults and examples: `sys`/`manager`, `ALTER USER sys`, shell-history permission checks, `6.3.1 and all later versions`, `ACCESS_LIST` remote-access examples, audit wording, and the patch-note link.
- Corrected MAX_CLIENT guidance for `TRANSACTION_TABLE_SIZE`, shell `ulimit` commands, and Linux root-user resource configuration.
- Corrected password-length terminology from "digits" to "characters" and clarified that older versions stored only the first 8 characters.
- Updated `manifest.json` metadata for all 14 edited English Markdown pages.

## Attachment And Link Evidence

- The scoped Korean source set contains no URL-backed document-format attachments with `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, or `.zip` extensions.
- The scoped English target set also contains no URL-backed document-format attachments with those extensions.
- Image links, `docs.altibase.com` source URLs, support/manual links, and internal FAQ references were preserved or corrected only where the Korean-source meaning required it.

## Self-Review

- Rechecked commands, SQL, properties, file paths, environment variables, versions, error codes, and URLs in the edited pages against Korean source meaning.
- Ran grep checks for stale export artifacts and known bad patterns in edited English pages: empty Markdown links, `Error rendering macro`, `Unknown macro`, `ATLIBASE`, `craete`, `replicaiton`, stale version-boundary wording, stale table/file terms, and stale command-output text.
- Rechecked edited-page `manifest.json` metadata against current file length and whitespace token counts.

## Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p215-manifest.json` | Passed |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`, and lock-session title) | Passed for all 14 edited English pages |
| Scoped grep for empty links, export artifacts, stale typo patterns, stale command output, and residual Korean text in edited pages | Passed, no matches |
| Scoped document-format attachment grep in Korean source set | Passed, 0 URL-backed document-format attachments |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |

## Remaining Risk

- External HTTP availability was not tested; this job used source-link preservation and grep-based link checks.
- Some legacy FAQE pages in this scope still preserve Confluence-exported one-line command output blocks where the Korean source has the same export shape. This job corrected semantic drift and unclear text without broadly reformatting every legacy output block.
