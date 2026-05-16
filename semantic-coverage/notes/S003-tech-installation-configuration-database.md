# S003 Tech Installation Configuration Database

Date: 2026-05-16

Workspace: `/home/et16/AID`

## Requirement And Boundary

S003 performs a semantic-unit audit for configuration, database creation, installation, quick start, and installation troubleshooting technical documents.

Scoped Korean sources and English targets:

- `DOCK/Home/20. Altibase 설정 파일 가이드__13437165.md` -> `arch/Home/Altibase Configuration File Guide__22642991.md`
- `DOCK/Home/25. Altibase 데이터베이스 생성 가이드__13436812.md` -> `arch/Home/Creating ALTIBASE Database__22643020.md`
- `DOCK/Home/31. Altibase 설치가이드__11698403.md` -> `arch/Home/Altibase Installation Guide__14647632.md`; `arch/Home/Altibase Installation Guide/1. Altibase HDB package installer__14647639.md`; `arch/Home/Altibase Installation Guide/2. Product Installation using the Package Installer__14647653.md`; `arch/Home/Altibase Installation Guide/3. License Key Request__14647666.md`
- `DOCK/Home/41. Altibase Quick Install & Start for UNIX__13436834.md` -> `arch/Home/Altibase Quick Install & Start for UNIX__16875604.md`
- `DOCK/Home/42. Altibase 설치 시 발생할 수 있는 문제상황과 조치__13437056.md` -> `arch/Home/Troubleshooting Altibase Installation Problems__15138879.md`

This job does not run the `llm-reference` consolidation workflow, does not edit Korean source documents, and does not delete or move English source documents. No English source document changes were required after direct comparison, so `manifest.json` metadata was not changed.

## Required Reading

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/prompts/S003.md`
- `semantic-coverage/README.md`
- `semantic-coverage/doc-mapping.tsv`
- The five Korean source documents and eight English target documents listed above

Previous J/P workflow reports were used only as orientation. Coverage decisions in `semantic-coverage/matrices/S003-tech-installation-configuration-database.tsv` are based on direct inspection of the scoped Korean and English files.

## Pre-Edit State

- Branch: `combine`
- `git status --short` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified from `S003 ToDo` to `S003 Progress`.
- `git status --short --untracked-files=all -- . ':(exclude).codex-jobs' ':(exclude).codex-jobs/**'` produced no output, so there were no uncommitted project files outside the workflow area before S003 edits.
- S003 owns the full audit for `DOCK/Home/20. Altibase 설정 파일 가이드__13437165.md`; later S005 rows for that source must be operation-specific cross-reference rows only.

## Design Note

S003 adds the first product-document semantic matrix in this workflow:

- `semantic-coverage/matrices/S003-tech-installation-configuration-database.tsv`
- `semantic-coverage/notes/S003-tech-installation-configuration-database.md`

The product documentation structure is unchanged. The matrix records semantic units by topic, command block, SQL block, property table row, warning/note, external reference, and attachment. Repeated installer transcripts and long startup/shutdown output blocks are summarized as single command-output semantic units when the transcript serves one procedural purpose; key identifiers from those blocks are preserved in the matrix evidence.

Korean legal/warranty boilerplate and export metadata are recorded as `not_applicable` because this workflow targets technical source coverage and those statements are not part of the English technical procedure baseline. URL-backed PDF attachments are recorded as `covered` because each is preserved in the English target.

## Audit Summary

### D020 Configuration File Guide

The English configuration guide covers the Korean source semantics for:

- `altibase.properties` purpose and Altibase `7.1.0`/`7.3.0` basis
- support portal and technical support center contact information
- property lookup through `SELECT name, value1 FROM v$property`
- hidden-property limitation of file lookup
- DCL property changes with `ALTER SYSTEM` and `ALTER SESSION`
- read-only property error `ERR-0104E`
- the `?` placeholder meaning `$ALTIBASE_HOME`
- DB-creation-time property recommendations, immutable properties, path properties, session properties, resource limits, disk I/O properties, and PBT properties
- references to system resource, replication, disk I/O, concurrent session, and General Reference documentation
- both Korean-source configuration PDF attachments

### D025 Database Creation Guide

The English database creation guide covers the Korean source semantics for:

- Altibase `7.1.0 or higher` basis
- EOS wording: versions earlier than `Altibase ver. 6` are EOS targets
- `DB_NAME` checking and `server` script update
- `server create UTF8 UTF16` and `isql -u sys -p manager -sysdba` creation methods
- database and national character set meanings
- archive log mode conversion at `startup control`
- immutable `DB_NAME` recreation/migration requirement
- drop-database file checks using `v$tablespaces`, `v$mem_tablespace_checkpoint_paths`, `v$datafiles`, and `LOG_DIR`
- `drop database mydb` command flow
- Korean-source version-specific database creation PDF attachment for Altibase 3, 4, and 5

### D031 Installation Guide

The split English installation guide covers the Korean source semantics across the parent and three child pages:

- overview, native compiler scope, Altibase `v7.1.0`, and Linux `2.6.32-504.el6.x86_64` test environment
- Java-based package installer, Altibase home directory, and APatch directory details
- `patchinfo`, `pkg_patch_0_0_0_0.txt`, `pkg_patch_0_0_0_10.txt`, `altibase_base_install.log`, backup, rollback, and uninstall semantics
- HP platform backup/rollback limitation and backup scope limitation
- Unix/Linux installation assumptions, memory, CPU, hard disk, and network requirements
- installer workflow, pre-checks, package download naming, OS/CPU/version support table, and SUN/Windows support cutoff from Altibase `7.1`
- text/GUI installer modes, `DISPLAY` hang mitigation, `chmod +x`, and `.run` execution
- property steps, database character set and national character set options, database directory settings, and `altibase.properties` manual editing
- property review, product install, license entry methods, quick setup guide, `pre_install.sh`, `post_install.sh`, `catproc.sql`, post-install tasks, license purchase, and MAC address lookup rows for Linux, Solaris, AIX, HP-UX, and Windows
- embedded installer screenshots are represented in the English split page with corresponding image references

### D041 Quick Install And Start

The English quick install guide covers the Korean source semantics for:

- preparation account, package download/upload, version/OS/MAC/license checks, support URL, and package filename examples
- EOS wording: versions earlier than `Altibase ver. 6` are EOS targets
- package permission, installer run, full/patch choice, kernel guide, DB name, port, `MEM_MAX_DB_SIZE`, `BUFFER_AREA_SIZE`, DB creation, archive mode, character set, national character set, and directory prompts
- property review, install, license registration, quick setting guide, `post_install.sh`, database creation output, environment setup, resulting `altibase.properties`, created data/log files, and `.bash_profile`/`altibase_user.env`
- directory component table including `admin`, `bin`, `include`, `install`, `lib`, `sample`, `trc`, `conf`, `logs`, `dbs`, `arch_logs`, `altiComp`, and `msg`
- 32-bit package/client-package considerations and support contact
- database creation guide link
- startup prerequisites, `server start`, iSQL `startup service`, startup failure examples, `altibase_boot.log`, and `No valid license present!`
- `server stop`, iSQL shutdown methods, shutdown option semantics for `abort`, `immediate`, and `normal`, plus the `normal` wait caution
- SQL92 note, manual reference, iSQL examples and options, `ALTIBASE_NLS_USE=MS949` character set handling, user creation/drop, tablespace creation/drop, table creation/drop, and the Korean-source Altibase v5 quick-install PDF attachment

### D042 Installation Troubleshooting

The English troubleshooting guide covers the Korean source semantics for:

- Altibase `6.5 or later` scope and `support@altibase.com` trace-log escalation
- binary/CPU mismatch with `cannot execute binary file`
- missing `ALTIBASE_HOME` with `ERR-91003`
- sysdba file-ownership/privilege failure with `ERR-9100B`
- missing `altibase.properties`
- missing, wrong, or expired `license`
- property range, conversion, and duplicate-value errors
- file write failure with `ERR-0103C`
- skipped database creation with missing log anchor and `ERR-91015`
- listener and replication port bind failures
- Korean-source Altibase `v5.3.3` troubleshooting PDF attachment

## Attachment Evidence

URL-backed document-format attachments in this scope:

- `202312_Altibase_설정_파일_가이드.pdf`: preserved in `arch/Home/Altibase Configuration File Guide__22642991.md`
- `201003_ALTIBASE_설정_파일_가이드.pdf`: preserved in `arch/Home/Altibase Configuration File Guide__22642991.md`
- `ALTIBASE_버전별_DB_생성_가이드.pdf`: preserved in `arch/Home/Creating ALTIBASE Database__22643020.md`
- `ALTIBASE_Quick_Install_Start_for_UNIX.pdf`: preserved in `arch/Home/Altibase Quick Install & Start for UNIX__16875604.md`
- `ALTIBASE_설치_시_발생할_수_있는_문제상황과_조치.pdf`: preserved in `arch/Home/Troubleshooting Altibase Installation Problems__15138879.md`

The scoped installation guide page has embedded screenshots but no URL-backed document-format attachment. The split English installation pages retain corresponding embedded screenshot references.

## Self-Review

- Scope checked: only S003 evidence files and the S003 workflow status were changed.
- Korean authority checked: all five Korean source files were inspected directly with line-numbered reads.
- English target checked: all eight English target files were inspected directly with line-numbered reads.
- Matrix checked: the S003 matrix uses the exact required TSV header, one physical row per matrix unit, allowed status values only, and no `missing`, `unverified`, or `recheck_required` rows.
- Coverage checked: commands, SQL, property names, version numbers, paths, error codes, support links, and PDF attachment links were included in matrix evidence.
- Product docs checked: no English source change was needed, so `manifest.json` metadata remained valid and unchanged.
- Known source quirks handled: Korean legal/warranty boilerplate and Confluence export metadata are `not_applicable`; Korean typos such as `altibase.propertites` and `PAHT` were considered source typos already normalized in English to the intended technical identifiers.

## Verification

Verification results after drafting and self-review:

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK/Home -type f -name '*.md' \| wc -l` | 51 |
| `find faq/Home -type f -name '*.md' \| wc -l` | 115 |
| `find arch/Home -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE/Home -type f -name '*.md' \| wc -l` | 241 |
| S003 TSV header and column-count check | Passed |
| S003 coverage status check | Passed: only `covered` and `not_applicable` rows |
| S003 unresolved-status scan | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Scoped empty-link and macro-artifact scan over S003 English targets and evidence | Passed with exit code 1, meaning no matches |
| Scoped attachment preservation grep | Passed: 5 URL-backed PDF attachment links preserved |

## Decision

S003 is complete for its scoped semantic-unit audit.

S003 final decision: `COMPLETE`.
