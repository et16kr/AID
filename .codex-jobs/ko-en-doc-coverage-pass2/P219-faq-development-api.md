# P219 FAQ Development API Audit

Date: 2026-05-16

## Scope

P219 audited Korean FAQ category `07. 개발 및 API` against the corresponding English `FAQE` targets. Korean FAQ pages remained authoritative and were not edited.

| Korean source | English target |
| --- | --- |
| `faq/Home/07. 개발 및 API/07-01. Connection 연결이 끊어지는 경우와 각 경우의 에러 코드 및 에러 메세지(APRE_C_C++, SQLCLI)__9110022.md` | `FAQE/Home/07. Development and API/Connection disconnection, error codes, and error messages in each case (APRE_C_C++, SQLCLI)__16876167.md` |
| `faq/Home/07. 개발 및 API/07-02. JDBC/07-02-01. Altibase JDBC에서 Fail-Over 사용하는 방법은__9110740.md` | `FAQE/Home/07. Development and API/JDBC/How to use Fail-Over in Altibase JDBC__16876173.md` |
| `faq/Home/07. 개발 및 API/07-02. JDBC/07-02-02. jdbc.trc 파일 생성 위치 변경 방법__8454703.md` | `FAQE/Home/07. Development and API/JDBC/How to change the jdbc.trc file creation location__16876175.md` |
| `faq/Home/07. 개발 및 API/07-02. JDBC/07-02-03. JDBC를 통한 서로 다른 Altibase 버전 동시 접속__22642863.md` | `FAQE/Home/07. Development and API/JDBC/Simultaneous connections to different Altibase versions via JDBC__22642951.md` |
| `faq/Home/07. 개발 및 API/07-03. ODBC/07-03-01. 64-bit Windows에서 32-bit ODBC 설치__9110670.md` | `FAQE/Home/07. Development and API/ODBC/32-bit ODBC installation on 64-bit Windows__22642957.md` |
| `faq/Home/07. 개발 및 API/07-03. ODBC/07-03-02. ODBC 함수, SQLFreeStmt__9110024.md` | `FAQE/Home/07. Development and API/ODBC/ODBC function, SQLFreeStmt__16876183.md` |
| `faq/Home/07. 개발 및 API/07-03. ODBC/07-03-03. unix_odbc와 연동하기__9110646.md` | `FAQE/Home/07. Development and API/ODBC/Integrating with unix_odbc__16876187.md` |
| `faq/Home/07. 개발 및 API/07-04. PHP/07-04-01. php 사용중인데 한글이 깨집니다__8454801.md` | `FAQE/Home/07. Development and API/PHP/Hangul is broken when using php__16876191.md` |
| `faq/Home/07. 개발 및 API/07-05. Spring+iBatis 트랜잭션 관리 방법__9109742.md` | `FAQE/Home/07. Development and API/How to manage Spring+iBatis transaction__16876194.md` |

## Boundary And Design Note

This job did not change product behavior, architecture, or the documentation hierarchy. The existing FAQE category and child-page structure was preserved. Documentation edits were limited to Korean-source link, command, and Java method casing corrections inside existing English pages.

## Findings And Updates

- No English change was needed for the connection-disconnection, JDBC Fail-Over, `jdbc.trc`, multi-version JDBC, 32-bit ODBC on 64-bit Windows, `SQLFreeStmt`, or PHP Hangul troubleshooting pages; their version conditions, commands, SQL, configuration names, error codes, and procedure semantics already matched the Korean sources.
- Corrected the unixODBC page to preserve the Korean-source download URL `http://www.unixodbc.org/`.
- Corrected the unixODBC configure command to preserve the Korean-source command text: `./configure -prefix=/home/wonsik/ODBC_HOME --enable-gui=no --enable-threads=yes`.
- Corrected the Spring+iBatis page from `SetAutoCommit(false)` to the exact Java method `setAutoCommit(false)`.
- Updated `manifest.json` metadata for both edited English Markdown pages.

## Attachment And Link Evidence

- The scoped Korean source set contains 1 URL-backed document-format attachment: `LobSpringIbatisSample.zip`.
- The exact `LobSpringIbatisSample.zip` URL is preserved in the scoped English target.
- Scoped Korean and English development/API pages contain no empty Markdown links, `Error rendering macro`, or `Unknown macro` markers.

## Self-Review

- Rechecked all scoped Korean/English pairs by semantic unit, including headings, bullets, procedure steps, code blocks, JDBC/ODBC/PHP examples, SQL, configuration/environment variables, version conditions, warning-style notes, and attachment links.
- Rechecked the edited English pages for stale command/link variants, residual Korean prose, malformed Confluence export links, and inconsistent technical identifiers.
- Rechecked `manifest.json` `body_chars` and `word_count` against the edited English page contents.

## Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p219-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for both edited English pages |
| Scoped document-format attachment preservation script | Passed, 1 Korean source ZIP link preserved |
| Scoped stale-pattern grep | Passed, no matches |

## Remaining Risk

- External HTTP availability was not tested; P219 used source-link preservation and grep-based checks.
- The Korean source uses `-prefix` in the unixODBC configure command. Because Korean source command text is authoritative for this audit, the English target preserves that spelling; a source owner may still want to validate whether the command should be `--prefix`.
