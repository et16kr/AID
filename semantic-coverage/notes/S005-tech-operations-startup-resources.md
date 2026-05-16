# S005 Tech Operations Startup Resources

Date: 2026-05-16

Workspace: `/home/et16/AID`

## Requirement And Boundary

S005 performs a semantic-unit audit for failure response, startup and shutdown, system resource sizing, OS utility, UNIX memory, and operation-related configuration documents.

Scoped Korean sources and English targets:

- `DOCK/Home/20. Altibase 설정 파일 가이드__13437165.md` -> `arch/Home/Altibase Configuration File Guide__22642991.md`
- `DOCK/Home/26. Altibase 기본적인 장애대응 절차__13435879.md` -> `arch/Home/Responding to Failures Guide for Altibase__15138818.md`; `arch/Home/Responding to Failures Guide for Altibase/1. Classification by type of failure__15138822.md`; `arch/Home/Responding to Failures Guide for Altibase/2. Procedure by type of failure__15138835.md`; `arch/Home/Responding to Failures Guide for Altibase/3. References__15138869.md`
- `DOCK/Home/43. Altibase STARTUP _ STOP 과정의 이해__13434993.md` -> `arch/Home/Understanding the Altibase Start_Shut down Process__14909450.md`; `arch/Home/Understanding the Altibase Start_Shut down Process/1. Starting Altibase__14909452.md`; `arch/Home/Understanding the Altibase Start_Shut down Process/2. Shutting Altibase Down__14909483.md`
- `DOCK/Home/45. Altibase 운영을 위한 시스템 리소스 용량산정 가이드__14057887.md` -> `arch/Home/System Data Capacity Estimation Guide for Altibase Operations__22643042.md`
- `DOCK/Home/47. 문제분석을 위한 OS별 유틸리티 사용 가이드__13436866.md` -> `arch/Home/Utility Guide for each OS for Problem Analysis__16875587.md`
- `DOCK/Home/48. UNIX Memory Management__13436842.md` -> `arch/Home/UNIX Memory Management__16875572.md`

`DOCK/Home/20. Altibase 설정 파일 가이드__13437165.md` is primarily owned by S003. S005 therefore adds only operation-specific cross-reference rows for D020, not a second full audit.

This job does not run the `llm-reference` consolidation workflow, does not edit Korean source documents, and does not delete or move English source documents. No English source document changes were required after direct comparison, so `manifest.json` metadata was not changed.

## Required Reading

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/prompts/S005.md`
- `semantic-coverage/README.md`
- `semantic-coverage/doc-mapping.tsv`
- The six Korean source documents and eleven English target documents listed above

Previous J/P workflow reports were used only as orientation. Coverage decisions in `semantic-coverage/matrices/S005-tech-operations-startup-resources.tsv` are based on direct inspection of the scoped Korean and English files.

## Pre-Edit State

- Branch: `combine`
- `git status --short` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified from `S005 ToDo` to `S005 Progress`.
- `git status --short --untracked-files=all -- . ':(exclude).codex-jobs' ':(exclude).codex-jobs/**'` produced no output, so there were no uncommitted project files outside the workflow area before S005 edits.
- S005 owns the full audit for D026, D043, D045, D047, and D048. D020 is cross-reference only because S003 owns the full audit.

## Design Note

S005 adds the semantic matrix and per-job note for the operations/startup/resource group:

- `semantic-coverage/matrices/S005-tech-operations-startup-resources.tsv`
- `semantic-coverage/notes/S005-tech-operations-startup-resources.md`

The product documentation structure is unchanged. The matrix records semantic units by topic section, compact table group, procedure, SQL block, command block, warning, external reference, attachment, and source limitation. Long command and SQL examples are summarized in the matrix while preserving exact commands, paths, error codes, system views, property names, and version numbers.

Export metadata, Confluence TOCs, contact-only support boilerplate, and legal/warranty boilerplate are recorded as `not_applicable` because they do not change the technical operation baseline. Broken Gliffy placeholders in the Korean STARTUP/STOP source are recorded as `source_limitation`; the surrounding technical text is covered separately, and the English target already carries corresponding English diagrams/log images where available.

## Audit Summary

### D020 Configuration Cross-References

S005 added operation-specific cross-reference rows only. The English configuration guide covers the Korean source semantics for:

- Altibase 7.1.0/7.3.0 basis and cross-links to system resource sizing and replication configuration
- capacity and startup connection properties such as `MEM_MAX_DB_SIZE`, `BUFFER_AREA_SIZE`, `PORT_NO`, `SQL_PLAN_CACHE`, and `REPLICATION_PORT_NO`
- session operation properties `MAX_CLIENT` and `MULTIPLEXING_THREAD_COUNT`
- resource-limit properties and errors including `TRX_UPDATE_MAX_LOGSIZE`, `PREPARE_STMT_MEMORY_MAXIMUM`, `EXECUTE_STMT_MEMORY_MAXIMUM`, `QUERY_TIMEOUT`, `FETCH_TIMEOUT`, `UTRANS_TIMEOUT`, and `IDLE_TIMEOUT`
- disk I/O and checkpoint properties including `PREPARE_LOG_FILE_COUNT`, `LF_PREPARE_WAIT_COUNT`, `v$lfg`, `CHECKPOINT_BULK_WRITE_PAGE_COUNT`, and `DIRECT_IO_ENABLED`
- PBT properties `QP_MSGLOG_FLAG`, `RP_CONFLICT_MSGLOG_FLAG`, and `TIMED_STATISTICS`

### D026 Failure Response

The split English failure-response guide covers the Korean source semantics for:

- urgent versus non-urgent failure definitions and maintenance-contract support
- required failure information: system logs, all files under `$ALTIBASE_HOME/trc`, and failure-time observations
- urgent user procedure: process check, local `isql` connection check, support request, support center contact, `server kill`, and `server start`
- connection failure categories and exact errors including `ERR-01052`, `ERR-71016`, `ERR-50032`, `ERR-31010`, `ERR-4102E`, `ERR-31370`, and `ERR-410E3`
- first-response checks for `ulimit -n`, `PORT_NO`, `netstat`, `ftp`/`telnet`, `df`/`bdf`, and the warning not to delete online log files
- OS-specific Hang information collection with `pstack` and `procstack`
- insufficient tablespace diagnosis and actions, including `ALTER TABLESPACE`, `MEM_MAX_DB_SIZE`, `DELETE`, `TRUNCATE`, and `ALTER TABLE ... COMPACT`
- physical disk shortage and physical memory shortage behavior, including the `V$MEMSTAT` query
- MVCC/Garbage Data impact from bulk changes or long-running queries, including `V$STATEMENT`, `V$TRANSACTION`, and `V$MEMGC` queries
- system problem errors and OS log locations
- replication failure checks, `V$REPSENDER`, `V$REPRECEIVER`, `altibase_rp.log`, `V$REPGAP`, Altibase 6.5.1-or-earlier `REP_GAP` formula, conflict logs, and conflict error codes
- technical support system, trace-log file descriptions, and basic monitoring items

### D043 Startup And Shutdown

The English startup/shutdown guide covers the Korean source semantics for:

- startup/shutdown overview and Altibase 7.1.0 example basis
- four startup stages: `PROCESS`, `CONTROL`, `META`, and `SERVICE`
- `STARTUP` use through iSQL with `SYSDBA` privileges and forward-only transitions
- PROCESS stage boot logging through `$ALTIBASE_HOME/trc/altibase_boot.log`, module initialization, property changes, performance views, and transition to higher stages
- SERVICE stage user access, listener startup, DB-service module initialization, Meta DB checks, replication manager startup, heartbeat manager startup, and iSQL success messages
- shutdown overview, `SHUTDOWN` through iSQL `-sysdba`, `NORMAL`, `IMMEDIATE`, `ABORT`, SERVICE-only restrictions for `NORMAL`/`IMMEDIATE`, and install OS account restriction
- `NORMAL` waiting for client disconnection and orderly module termination
- `IMMEDIATE` session disconnection, transaction rollback, `SERVER STOP` equivalence, reverse-order module shutdown, resource release, table compaction, dirty-page flush, checkpoint, and increased wait time
- `ABORT` as a `kill -9` shutdown and its recovery consequence
- the Korean-source legacy startup/stop PDF attachment

The Korean STARTUP/STOP source contains broken Gliffy placeholders in several diagram/log positions. Those placeholder units are recorded as `source_limitation`. The English target contains corresponding English diagram/log images where available, but the exact missing Korean Gliffy content cannot be independently inferred from the Korean export.

### D045 System Resource Sizing

The English resource sizing guide covers the Korean source semantics for:

- Altibase 7.1.0-or-higher basis and the need to determine server storage before a project
- memory sizing factors: memory DB size, disk DB buffer size, and query execution memory
- 32 KB memory table pages, slots, `V$MEMTBL_INFO`, memory index pointer sizing, 30-50% margin, `SYSTEM_.SYS_COLUMNS_`, and volatile tablespace inclusion
- disk DB buffer recommendation of at least 10% of frequently accessed disk DB size
- query execution plan memory, `SQL_CACHE`, temporary memory, disk temporary tablespaces, and MVCC margin formulas
- memory sizing example DDL, record-length SQL, 8-byte alignment rule, and 34 GB total memory example
- disk capacity factors: checkpoint image files, transaction log file space, estimated disk DB space, and backup space
- checkpoint image sizing at twice memory DB capacity
- WAL and online log file sizing, replication/log retention cases, load-test sizing, and minimum 50 GB recommendation when testing is difficult
- disk DB page-based sizing with `PCTFREE`, `PCTUSED`, 8,192-byte pages, header sizes, 3,551 MB example, and 30-50% margin
- undo and temporary tablespace sizing, including 1 TB worst-case update and 30% largest-table guidance
- backup and archive log sizing, including daily example and previous-backup retention
- `iloader` delimiter capacity formula and compression-ratio caveat
- final 1,720 GB disk capacity example and legacy resource sizing PDF attachment

### D047 OS Utility Guide

The English OS utility guide covers the Korean source semantics for:

- OS commands as supplements to Altibase performance views during problem analysis
- common `netstat -in` and `vmstat 1 5` usage and indicator interpretation
- Linux thread CPU checks with `top -H` and `ps -LFm -p`, `pstack` stack interpretation, `/proc/<process id>/fd`, and `/var/log/messages`
- Solaris `prstat`, `pstack -F ... | c++filt`, `pfiles -F`, and `/var/adm/messages.*`
- AIX `ps -mo THREAD`, `procstack`, `pfiles -n`, and `errpt -a`
- HP-UX `glance`, `pstack`, `pfiles`, and `/var/adm/syslog/syslog.log`
- the Korean-source legacy OS utility PDF attachment

### D048 UNIX Memory Management

The English UNIX memory guide covers the Korean source semantics for:

- UNIX/Linux process memory management overview
- Solaris reserved swap allocation, `swap -s`, VSZ/swap example, `lotsfree`, `vmstat` `sr`/`fr`, swapping, and `pmap -F`
- AIX memory classifications, `svmon -G`, page-unit interpretation, file-cache stealing, `MAXPERM`, `MINPERM`, `NUMPERM`, `MAXCLIENT`, `stric_maxperm`, `lru_file_repage`, `svmon -P`, and `ps v`
- HP arena allocation, `_M_ARENA_OPT=16:8`, default `8:32`, Glance, `pmap`, and file-cache settings `dbc_max_pct` and `dbc_min_pct`
- Linux swappiness, `/proc/sys/vm/swappiness`, `sysctl`, default 60%, MySQL `0` reference, RHEL6 arena notes, `MALLOC_ARENA_TEST`, `MALLOC_ARENA_MAX`, `top`, `pmap`, and VSZ/free behavior
- the Korean-source legacy UNIX Memory Management PDF attachment

## Attachment Evidence

URL-backed document-format attachments in this scope:

- `ALTIBASE_STARTUP_STOP_과정의이해.pdf`: preserved in `arch/Home/Understanding the Altibase Start_Shut down Process__14909450.md` and `arch/Home/Understanding the Altibase Start_Shut down Process/1. Starting Altibase__14909452.md`
- `ALTIBASE_운영을_위한_시스템_리소스_용량산정_가이드.pdf`: preserved in `arch/Home/System Data Capacity Estimation Guide for Altibase Operations__22643042.md`
- `ALTIBASE_문제분석을_위한_OS별_유틸리티_사용_가이드.pdf`: preserved in `arch/Home/Utility Guide for each OS for Problem Analysis__16875587.md`
- `UNIX_Memory_Management.pdf`: preserved in `arch/Home/UNIX Memory Management__16875572.md`
- D020 configuration guide attachments are primarily audited by S003/S019, but the English target still preserves both Korean-source PDF URLs.

D026 has embedded support/reference images but no URL-backed document-format attachments.

## Self-Review

- Scope checked: only S005 evidence files and S005 workflow status files were changed.
- Korean authority checked: all six Korean source files were inspected directly with line-numbered reads.
- English target checked: all eleven English target files were inspected directly with line-numbered reads.
- Duplicate source ownership checked: D020 rows are cross-reference only and name S003 as primary owner in the matrix notes.
- Matrix checked: the S005 matrix uses the exact required TSV header, one physical row per matrix unit, allowed status values only, and no `missing`, `unverified`, or `recheck_required` rows.
- Coverage checked: commands, SQL, system views, file paths, property names, version conditions, warnings, error codes, external links, and PDF attachment links were included in matrix evidence.
- Product docs checked: no English source change was needed, so `manifest.json` metadata remained valid and unchanged.
- Source limitations checked: broken Gliffy placeholders in the Korean STARTUP/STOP source are explicitly marked as `source_limitation`, and the surrounding technical text is covered separately.

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
| S005 TSV header and column-count check | Passed: 109 data rows, 15 columns each |
| S005 coverage status check | Passed: 97 `covered`, 8 `not_applicable`, 4 `source_limitation` |
| S005 unresolved-status scan | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Full matrix unresolved-status scan over `semantic-coverage/matrices` | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Scoped empty-link and macro-artifact scan over S005 English targets and evidence | Passed with exit code 1, meaning no matches |
| `semantic-coverage` empty-link and macro-artifact scan | Passed with exit code 1, meaning no matches |
| Scoped attachment preservation grep | Passed: 7 preserved English URL hits for 6 Korean-source PDF links, with the STARTUP/STOP PDF preserved in both parent and starting pages |

## Decision

S005 is complete for its scoped semantic-unit audit.

S005 final decision: `COMPLETE`.
