# S020 - FAQ installation patch upgrade

## Requirement and boundary

S020 performs a semantic-unit audit for FAQ category `01. 설치, 패치, 업그레이드` against the Korean-core English FAQ category `01. Installation, Patch, Upgrade`.

Scoped Korean sources and English targets:

- `faq/Home/01. 설치, 패치, 업그레이드/01-01. Altibase HDB가 지원하는 플랫폼(OS)은__9110736.md` -> `FAQE/Home/01. Installation, Patch, Upgrade/What Platforms (OS) Altibase HDB supports__16875920.md`
- `faq/Home/01. 설치, 패치, 업그레이드/01-02. Unix 및 Linux 에서 알티베이스 서버 패치 절차__8454397.md` -> `FAQE/Home/01. Installation, Patch, Upgrade/Altibase Server Patch Procedure on Unix and Linux__16875922.md`
- `faq/Home/01. 설치, 패치, 업그레이드/01-03. 알티베이스 클라이언트 설치 방법(ALTIBASE HDB 5.5.1 부터)__8455011.md` -> `FAQE/Home/01. Installation, Patch, Upgrade/Altibase Client Installation/Starting from ALTIBASE HDB 5.5.1__16875941.md`
- `faq/Home/01. 설치, 패치, 업그레이드/01-04. 윈도우에서 알티베이스 설치 할 때 _이미 설치가 되었다_고 합니다__8454409.md` -> `FAQE/Home/01. Installation, Patch, Upgrade/What to do when installing Altibase on Windows, and it says _It has already been installed__16875943.md`

This job does not audit FAQ category 02, does not run the `llm-reference` consolidation workflow, does not edit Korean source documents, and does not delete or move English source documents.

## Required reading and direct inspection

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/prompts/S020.md`
- `semantic-coverage/doc-mapping.tsv`
- The four Korean source documents and four mapped English target documents listed above

Previous J/P reports were used only as orientation. Coverage decisions in `semantic-coverage/matrices/S020-faq-installation-patch-upgrade.tsv` are based on direct inspection of the scoped Korean and English files.

## Pre-edit state

- Branch: `combine`
- Initial `git status --short` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified inside the workflow area as `S020` was already in `Progress`.
- No uncommitted project files outside the workflow runtime area were present before S020 edits.

## Design note

S020 adds semantic evidence and one narrow English documentation correction:

- Adds `semantic-coverage/matrices/S020-faq-installation-patch-upgrade.tsv`
- Adds `semantic-coverage/notes/S020-faq-installation-patch-upgrade.md`
- Corrects the client-install FAQ label for the `ls -l` permission verification block from a repeated "change execution permission" label to "How to check file permission"
- Updates `manifest.json` metadata for the edited English FAQ page
- Updates S020 workflow status in `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv`

The documentation structure is unchanged.

## Audit summary

Matrix file: `semantic-coverage/matrices/S020-faq-installation-patch-upgrade.tsv`

Rows by coverage status:

- `covered`: 66
- `added`: 1
- `not_applicable`: 10

Rows by source:

- F01-01 platform support: 26 rows
- F01-02 Unix/Linux server patch procedure: 27 rows
- F01-03 client installation from ALTIBASE HDB 5.5.1: 18 rows
- F01-04 Windows already-installed registry cleanup: 6 rows

### Platform support

The English platform FAQ preserves the Korean-source platform tables for Altibase HDB `6.5.1`, `6.3.1`, and `6.1.1`, including OS names, CPU families, OS version constraints, server/client bitness, and the JDBC/JDK compatibility condition.

Key identifiers checked include `AIX`, `HP-UX`, `LINUX`, `SUN`, `Windows`, `PowerPC`, `IA64`, `PA-RISC`, `SPARC`, `i86PC`, `GNU glibc 2.12`, `GNU glibc 2.3.4`, `Windows 2003`, `Windows 2008`, `Windows 2012`, `Windows 7, 8`, `Altibase HDB 6`, `JDBC`, and `JDK 1.4`.

### Unix/Linux server patch procedure

The English patch FAQ preserves the Korean-source distinction between patch and upgrade, downtime requirement, pre-patch checks, current-version check, shutdown validation, backup procedures, package handling for `5.5.1` and later versus earlier releases, patch execution, version verification, script restoration after `sys` password changes, startup validation, meta-version warning, and the special `ALTIBASE HDB 4.3.9.1 ~ 4.3.9.50` to `4.3.9.51 ~` replication procedure.

Key identifiers checked include `altibase -v`, `server stop`, `server start`, `ps -ef | grep 'altibase -p' | grep -v grep`, `netstat -an | grep 20300`, `$ALTIBASE_HOME`, `bin.bak`, `lib.bak`, `msg.bak`, `conf.bak`, `include.bak`, `.run`, `.tgz`, `gzip -cd`, `tar xvf -`, `meta version`, `data files`, `log anchor files`, `log files`, `configuration files`, `PORT_NO`, `V$REPGAP`, `REP_GAP`, `aexport`, `SYS_CRT_REP.sql`, `SYSTEM_.SYS_REPLICATIONS_`, `ALTER REPLICATION`, `DROP REPLICATION`, `ALTER SYSTEM CHECKPOINT`, `CHECK_LOGFILE = 0`, `IMSI_T`, `IMSI_PROC`, `V$LFG`, `CUR_WRITE_LF_NO`, and `is -f SYS_CRT_REP.sql`.

One source wording inconsistency remains in the Korean and English patch FAQ startup verification step: the heading and example output show startup verification, but the source text also says "shutdown" and "no output". S020 records that risk in the matrix while treating the English target as semantically covering the Korean source state.

### Client installation

The English client-install FAQ preserves the Korean-source target OS list, support portal download/request path, upload procedure, permission change and verification commands, installer execution transcript, generated directory structure, shell initialization environment variables, shell-specific initialization filenames, environment application commands, and iSQL connection verification.

S020 changed one label in the English target so the `ls -l` verification block now matches the Korean-source meaning:

- Korean source: `파일 권한 확인 방법`
- English target after S020: `How to check file permission`

The long installer transcript and directory listing were checked for the required prompts, values, and identifiers, including `ALTIBASE_HOME`, `ALTIBASE_PORT_NO=20300`, `PATH`, `LD_LIBRARY_PATH`, `CLASSPATH`, `.bash_profile`, `.profile`, `Altibase.jar`, `isql`, `sys`, `manager`, `192.168.1.145`, and `SELECT PRODUCT_VERSION FROM V$VERSION`.

### Windows registry cleanup

The English Windows FAQ preserves the Korean-source symptom, cause, and registry cleanup procedure. It keeps the required registry key and screenshot evidence:

- `Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Altibase Corp.,`
- `altibase_registry.png`

The screenshot URL differs by Confluence export path between Korean and English spaces, but the filename and procedural evidence are represented.

## Attachment and link evidence

The scoped Korean FAQ category 01 source set contains 0 URL-backed document-format attachments with `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, or `.zip` extensions.

The scoped English FAQ category 01 target set also contains 0 URL-backed document-format attachments with those extensions.

Scoped support links were checked as source-link semantics rather than document attachments. The English client-install FAQ uses the corresponding English support URLs:

- `http://support.altibase.com/en/product`
- `http://support.altibase.com/en/`

## Self-review

- Scope checked: S020 changed only the scoped English client-install FAQ, `manifest.json`, S020 evidence files, and S020 workflow status.
- Korean authority checked: all four scoped Korean source files were inspected directly.
- English target checked: all four mapped English target files were inspected directly.
- Matrix checked: the S020 matrix uses the exact required TSV header, one physical row per matrix unit, allowed status values only, and no `missing`, `unverified`, or `recheck_required` rows.
- Terminology checked: product names, commands, SQL, property names, paths, version numbers, support URLs, and registry keys are preserved.
- Manifest checked: the edited English page metadata was updated from `body_chars: 8060` to `body_chars: 8054`; `word_count` remains `821`.

## Verification

Verification results after drafting, self-review, and fixes:

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK/Home -type f -name '*.md' \| wc -l` | 51 |
| `find faq/Home -type f -name '*.md' \| wc -l` | 115 |
| `find arch/Home -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE/Home -type f -name '*.md' \| wc -l` | 241 |
| S020 TSV header, field-count, and status validation | Passed: 77 data rows, 15 fields per row, statuses `covered: 66`, `added: 1`, `not_applicable: 10` |
| S020 scoped empty-link and macro-artifact grep | Passed with exit code 1, meaning no matches |
| S020 and full matrix unresolved-status grep | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Scoped document-format attachment grep for `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.zip` | Passed with exit code 1, meaning no URL-backed document-format attachments in scoped Korean or English category 01 files |
| Edited-page manifest metadata comparison | Passed: `body_chars` 8054 and `word_count` 821 match the edited English file |

## Final decision

S020 final decision: `COMPLETE`.
