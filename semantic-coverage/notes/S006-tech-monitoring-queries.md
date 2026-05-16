# S006 Tech Monitoring Queries

Date: 2026-05-16

Workspace: `/home/et16/AID`

## Requirement And Boundary

S006 performs a semantic-unit audit of the Korean monitoring queries guide against the English split monitoring guide. The scoped Korean source is authoritative and was not edited.

Scoped Korean source and English targets:

- `DOCK/Home/59. Altibase 모니터링 쿼리 가이드__10060431.md` -> `arch/Home/Altibase Monitoring Queries Guide__14058229.md`; `arch/Home/Altibase Monitoring Queries Guide/**`

This job covers only S006. It does not run the `llm-reference` consolidation workflow, does not edit Korean source documents, and does not delete or move English source documents. Direct comparison found no English source change was required, so `manifest.json` metadata was not changed.

## Required Reading

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/prompts/S006.md`
- `semantic-coverage/README.md`
- `semantic-coverage/doc-mapping.tsv`
- The Korean source document and all English monitoring-guide parent and child pages listed in the mapping

Previous J/P workflow reports were used only as orientation. Coverage decisions in `semantic-coverage/matrices/S006-tech-monitoring-queries.tsv` are based on direct inspection of the scoped Korean and English files.

## Pre-Edit State

- Branch: `combine`
- `git status --short` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified from `S006 ToDo` to `S006 Progress`.
- `git status --short --untracked-files=all -- . ':(exclude).codex-jobs' ':(exclude).codex-jobs/**'` produced no output, so there were no uncommitted project files outside the workflow area before S006 edits.

## Design Note

S006 adds the semantic matrix and per-job note for the monitoring query guide:

- `semantic-coverage/matrices/S006-tech-monitoring-queries.tsv`
- `semantic-coverage/notes/S006-tech-monitoring-queries.md`

The product documentation structure is unchanged. The Korean source is a single large page, while the English target is split into parent, overview, meta/performance-view, and query-category child pages. The matrix therefore records coverage by exported metadata, overview sections, meta-table/performance-view groups, monitoring query category headings, individual query IDs, SQL blocks, version/use caveats, column/output tables, and the legacy PDF attachment. Long SQL blocks are summarized in matrix rows while preserving exact query IDs, system views, properties, column identifiers, version conditions, and warnings.

## Audit Summary

### Overview And Meta/Performance Views

The English monitoring guide preserves the Korean source semantics for:

- the three-part guide structure, General Reference recommendation, monitoring-query shortcut, and CA ERwin IDEF1X ERD note;
- internal/external/trace-log monitoring categories and the internal-monitoring scope of this guide;
- meta table and performance view definitions, including `SYSTEM_`, read-only `SELECT`, and the `V$` performance-view prefix;
- ERD notation caveats, version-dependent meta/performance-view changes, and terminology for session, statement/query, MVCC, memory DB GC, and `Ager`;
- session/query/transaction/lock/service-thread/memory-DB-GC views, including `TIMED_STATISTICS`, `V$STATEMENT`, `V$SQLTEXT`, `V$PLANTEXT`, `V$SERVICE_THREAD`, `V$TRANSACTION`, `V$MEMGC`, `V$LOCK`, `V$LOCK_WAIT`, and `V$LOCK_STATEMENT`;
- tablespace/table/column/index/constraint metadata and performance views, including `TABLE_ID`, `TABLE_OID`, `V$SEGMENT`, 16-byte memory-index estimation, `SEG_PID`, and `INDEX_SEG_PID`;
- statistical views and caveats, including `V$PROPERTY`, `V$SYSTEM_WAIT_CLASS`, `V$SYSTEM_EVENT`, `V$SESSION_EVENT`, `V$SESSION_WAIT`, `V$SYSSTAT`, `V$SESSTAT`, `V$FILESTAT`, `V$MEMSTAT`, `V$BUFFPOOL_STAT`, `V$LFG`, `LF_PREPARE_WAIT_COUNT`, and `PREPARE_LOG_FILE_COUNT`;
- replication metadata and runtime views, including `SYS_REPL_ITEMS_`, `V$REPSENDER`, `V$REPGAP`, `V$REPRECEIVER`, `V$REPSENDER_TRANSTBL`, and `V$REPRECEIVER_TRANSTBL`;
- tablespace access, privilege, PSM, and view metadata, including `SYS_TBS_USERS_`, `SYS_PRIVILEGES_`, `SYS_GRANT_SYSTEM_`, `SYS_GRANT_OBJECT_`, `SYS_VIEWS_`, `SYS_VIEW_PARSE_`, `SYS_PROCEDURES_`, and `SYS_PROC_PARSE_`.

### Query ID Coverage

Direct query inventory found 72 Korean query IDs and 72 matching English query IDs with no missing or extra IDs.

Covered query groups:

- `SS01`-`SS03`: session counts, session details, SYSDBA sessions, `CLIENT_APP_INFO` v5/v4 caveat.
- `ST01`-`ST10`: statement counts, query details, active queries, long-running queries, full scans, per-session statement counts, `TIMED_STATISTICS`, `CLIENT_APP_INFO`, `V$SESSIONMGR`, and transaction timing caveats.
- `SV01`-`SV02`: service-thread status and contention, including Altibase v5+ and Altibase v4 variants where the Korean source provides them.
- `TL01`, `LO01`-`LO02`, `GC01`-`GC02`, `MS01`-`MS02`, and `DB01`: transaction/lock, redo log, GC, memory, and disk-buffer monitoring.
- `TS01`-`TS14`: memory/disk/undo/temp tablespace usage, data files, file I/O, checkpoint paths, overall status, and all Korean-source version variants.
- `OB01`-`OB20`: memory and disk objects, partition tables, sequences, synonyms, PSM, views, packages, triggers, jobs, users, and tablespace lists, including older-version variants and object timestamp/access caveats.
- `PV01`-`PV05`: system/object privileges, role creation, users granted roles, privilege types, and role-filter semantics.
- `CT01`-`CT04`: full constraints, PK/FK/UNIQUE relationships, composite index columns, index summary, and `CHECK_CONDITION`.
- `RP01`-`RP06`: replication sender/receiver/gap/status/log-buffer/table-list queries, including `REPL_MODE`, `START_FLAG`, `V$REPGAP`, and the Korean-source `STAUS` alias in `RP01`.

### Attachment Evidence

The Korean source contains one URL-backed document-format attachment:

- `ALTIBASE_모니터링_쿼리_가이드.pdf`

The English monitoring guide preserves this PDF URL in both:

- `arch/Home/Altibase Monitoring Queries Guide__14058229.md`
- `arch/Home/Altibase Monitoring Queries Guide/1. Altibase Server Monitoring Overview__14058232.md`

## Self-Review

- Scope checked: only S006 evidence files and S006 workflow status files were changed.
- Korean authority checked: the Korean monitoring guide was inspected directly with line-numbered reads.
- English target checked: the parent and all 21 split English monitoring guide pages were inspected directly.
- Matrix checked: the S006 matrix uses the exact required TSV header, one physical row per matrix unit, allowed status values only, and no `missing`, `unverified`, or `recheck_required` rows.
- Query IDs checked: all 72 Korean query IDs are present in the English targets.
- SQL/code checked: SQL block counts balance at 88 Korean blocks and 88 English blocks when indented fences are counted; per-query block counts match for the 72 query sections.
- Terminology checked: system views, meta tables, properties, paths, column names, query IDs, and version conditions are preserved as technical identifiers.
- Product docs checked: no English source change was needed, so `manifest.json` metadata remained valid and unchanged.
- Source typos checked: apparent Korean-source typos such as `STAUS` in `RP01` were preserved in the English target because the Korean source is authoritative for this audit.

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
| S006 TSV header and column-count check | Passed: 113 data rows, 15 columns each |
| S006 coverage status check | Passed: 111 `covered`, 2 `not_applicable` |
| S006 unresolved-status scan | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Full matrix unresolved-status scan over `semantic-coverage/matrices` | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Scoped empty-link and macro-artifact scan over S006 English targets and evidence | Passed with exit code 1, meaning no matches |
| Scoped query ID comparison | Passed: 72 Korean query IDs and 72 English query IDs; no missing or extra IDs |
| Scoped SQL/code block inventory | Passed: 88 Korean SQL/code blocks and 88 English SQL/code blocks; per-query block counts match |
| Scoped monitoring guide PDF attachment preservation grep | Passed: 2 preserved English URL hits for the Korean-source PDF link |
| High-risk identifier grep for `TIMED_STATISTICS`, `CLIENT_APP_INFO`, `REPL_MODE`, `START_FLAG`, `CHECK_CONDITION`, `STAUS`, `LF_PREPARE_WAIT_COUNT`, `PREPARE_LOG_FILE_COUNT`, and `V$REPGAP` | Passed: identifiers found in scoped English targets |
| Scoped residual Korean text scan over S006 English targets | Passed with exit code 1, meaning no Korean text remains in the English monitoring guide |

## Decision

S006 is complete for its scoped semantic-unit audit after verification passes.

S006 final decision: `COMPLETE`.
