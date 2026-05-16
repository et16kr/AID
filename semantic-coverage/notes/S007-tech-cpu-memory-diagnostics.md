# S007 Tech CPU Memory Diagnostics

Date: 2026-05-16

Workspace: `/home/et16/AID`

## Requirement And Boundary

S007 performs a semantic-unit audit of the Korean CPU overload and memory usage increase analysis guides against their English split `arch` targets. The scoped Korean sources are authoritative and were not edited.

Scoped Korean sources and English targets:

- `DOCK/Home/62. Altibase CPU 과부하 현상에 대한 분석가이드__11698396.md` -> `arch/Home/Altibase CPU Overload Analysis Guide__14647581.md`; `arch/Home/Altibase CPU Overload Analysis Guide/**`
- `DOCK/Home/63. Altibase Memory 사용량 증가 분석가이드__11698518.md` -> `arch/Home/Altibase Memory Usage Increase Analysis Guide__14647388.md`; `arch/Home/Altibase Memory Usage Increase Analysis Guide/**`

This job covers only S007. It does not run the `llm-reference` consolidation workflow, does not edit Korean source documents, and does not delete or move English source documents. Direct comparison found no English source change was required, so `manifest.json` metadata was not changed.

## Required Reading

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/prompts/S007.md`
- `semantic-coverage/README.md`
- `semantic-coverage/doc-mapping.tsv`
- The two Korean source documents and all split English CPU/memory guide target pages listed in the mapping

Previous J/P workflow reports were used only as orientation. Coverage decisions in `semantic-coverage/matrices/S007-tech-cpu-memory-diagnostics.tsv` are based on direct inspection of the scoped Korean and English files.

## Pre-Edit State

- Branch: `combine`
- `git status --short` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified from `S007 ToDo` to `S007 Progress`.
- `git status --short --untracked-files=all -- . ':(exclude).codex-jobs' ':(exclude).codex-jobs/**'` produced no output, so there were no uncommitted project files outside the workflow area before S007 edits.

## Design Note

S007 adds the semantic matrix and per-job note for the CPU and memory diagnostic guides:

- `semantic-coverage/matrices/S007-tech-cpu-memory-diagnostics.tsv`
- `semantic-coverage/notes/S007-tech-cpu-memory-diagnostics.md`

The product documentation structure is unchanged. Each Korean source is a single page, while the English targets are split by guide chapter. The matrix therefore records coverage by exported metadata, overview sections, routine checklist rows, command/SQL blocks, diagnostic procedure sections, summary numbered items, attachment rows, and source caveats. Long SQL and shell blocks are summarized in the matrix while preserving exact identifiers, view names, property names, command names, version conditions, and attachment URLs.

## Audit Summary

### CPU Overload Guide

The English CPU overload guide preserves the Korean source semantics for:

- the user/kernel CPU overview, Altibase transaction processing, client communication, replication, data-file disk I/O, prerequisite guide references, and Altibase 6-or-later Linux test environment;
- routine CPU history collection, including OS-based CPU usage, transaction throughput, service-thread/session counts, cumulative `EXECUTE COUNT`, the `gettps.sh` script, sample output, and TPS history table;
- general analysis flow for normal transaction growth, unverified long-running or bulk-change queries, newly added services, existing application problems exposed by data growth, optimizer statistics/plan-change risk, `V$PLANTEXT`, and the monitoring-guide shortcut;
- query-processing CPU cost, including the PVO process, repeated `PREPARE`, `V$SYSSTAT` prepare counts, `PLAN-CACHE`, and session/PID diagnosis through `V$SESSTAT` and `V$SESSION`;
- memory-table and disk-table scan cost, including 32 KB pages, slots, full scans, memory-index pointer behavior, file cache, Buffered I/O, Direct I/O, and CPU/performance trade-offs;
- other CPU cases, including `NLS_USE` mismatch, `Dedicated Thread`, `Select-Poll`, `MULTIPLEXING_POLL_TIMEOUT`, OS environment variables, repeated connect/disconnect, `QUERY_PROF_FLAG`, `*.prof`, `altiProfile`, and profiling cautions;
- the summary cause-analysis items and the OS utility guide reference for per-thread CPU diagnosis.

### Memory Usage Increase Guide

The English memory usage increase guide preserves the Korean source semantics for:

- the overview of application/user and memory-tablespace data growth, prerequisite guide references, and Altibase 7-or-later Linux test environment;
- OS memory/swap checks for AIX, HP-UX, and Linux, including AIX `svmon` field meanings, HP-UX `glance`, Linux `top`, `free -m`, and available-memory formulas;
- routine memory history collection, including Altibase process memory utilization, the memory-guide `V$MEMSTAT` SQL, service-thread/session counts, the `gettps.sh` CPU/memory script, and sample output;
- `V$MEMSTAT` module descriptions for `Query_Prepare`, `Query_Execute`, `Query_Binding`, `Storage_Memory_Manager`, `Index_Memory`, and `Storage_Disk_Buffer`;
- the four representative Altibase process memory increase causes: memory table data growth, executing SQL statement count growth, MVCC copy growth, and delayed aging target deletion;
- memory table usage SQL with `SYS_TABLES_` and `V$MEMTBL_INFO`, `Alloc`/`Used` semantics, the `1G`/`900M` scenario, OS reserved-memory behavior, table compaction, `ALTER TABLE table_name COMPACT;`, restart effects, and PM restart guidance;
- SQL object close handling, Java/JDBC `ps.close`, `Query_Prepare` retention, bind-variable parameterization of similar SQL, and current-version distinct-query memory allocation behavior;
- MVCC copy semantics, `LIMIT` batching, `Old Version`/`Garbage Data`, `V$MEMGC`, `ADD_OID_CNT`, `GC_OID_CNT`, unfinished transaction diagnosis with `V$TRANSACTION`, `V$STATEMENT`, `V$MEMGC`, and the memory-table-only limitation.

### Source Caveats Preserved

- The Korean CPU source has internally inconsistent optimizer-statistics version wording: one detailed section names `6.1.1.6.1` or later, while the summary names `6.1.1` or earlier. The English guide preserves the scoped meaning in each corresponding section.
- The Korean memory routine checklist pairs a transaction-throughput row with a `v$memstat` SQL example while the prose mentions `V$SYSSTAT`. The English guide clarifies the row around `V$MEMSTAT` because the page is the memory usage guide and the Korean SQL block selects from `v$memstat`.

### Attachment Evidence

The Korean CPU source contains one URL-backed document-format attachment:

- `ALTIBASE_CPU_PBT절차.pdf`

The English CPU guide preserves this PDF URL in:

- `arch/Home/Altibase CPU Overload Analysis Guide__14647581.md`
- `arch/Home/Altibase CPU Overload Analysis Guide/1. Routine Checklist__14647587.md`

The Korean memory source contains one URL-backed document-format attachment:

- `ALTIBASE_MEM_PBT절차.pdf`

The English memory guide preserves this PDF URL in:

- `arch/Home/Altibase Memory Usage Increase Analysis Guide__14647388.md`

## Self-Review

- Scope checked: only S007 evidence files and S007 workflow status files were changed.
- Korean authority checked: both scoped Korean diagnostic guides were inspected directly with line-numbered reads.
- English target checked: the CPU parent plus five child pages, and the memory parent plus two child pages, were inspected directly.
- Matrix checked: the S007 matrix uses the exact required TSV header, one physical row per matrix unit, allowed status values only, and no `missing`, `unverified`, or `recheck_required` rows.
- Code checked: CPU source and target sets both contain 20 fenced-code markers; memory source and target sets both contain 18 fenced-code markers.
- Terminology checked: system views, properties, paths, utilities, version conditions, and attachment filenames are preserved as technical identifiers.
- Product docs checked: no English source change was needed, so `manifest.json` metadata remained valid and unchanged.
- Source quirks checked: the CPU version-wording inconsistency and memory `V$SYSSTAT`/`V$MEMSTAT` prose/SQL mismatch are recorded in the matrix and this note.

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
| S007 TSV header and column-count check | Passed: 72 data rows, 15 columns each |
| S007 coverage status check | Passed: 68 `covered`, 4 `not_applicable` |
| S007 unresolved-status scan | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Full matrix unresolved-status scan over `semantic-coverage/matrices` | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Scoped empty-link and macro-artifact scan over S007 English targets and evidence | Passed with exit code 1, meaning no matches |
| Scoped residual Korean text scan over S007 English targets | Passed with exit code 1, meaning no Korean text remains in the English target pages |
| Scoped fenced-code balance check | Passed: CPU Korean/English both 20 fenced markers; memory Korean/English both 18 fenced markers |
| High-risk identifier grep for CPU diagnostics | Passed: `V$SYSSTAT`, `V$SERVICE_THREAD`, `V$SESSION`, `V$STATEMENT`, `V$PLANTEXT`, `V$SESSTAT`, `NLS_USE`, `MULTIPLEXING_POLL_TIMEOUT`, `TIMED_STATISTICS`, `QUERY_PROF_FLAG`, `altiProfile`, `PLAN-CACHE`, `Direct I/O`, and `Buffered I/O` found in scoped English targets |
| High-risk identifier grep for memory diagnostics | Passed: `V$MEMSTAT`, `Query_Prepare`, `Query_Execute`, `Query_Binding`, `Storage_Memory_Manager`, `Index_Memory`, `Storage_Disk_Buffer`, `V$MEMTBL_INFO`, `ALTER TABLE table_name COMPACT`, `V$STATEMENT`, `MVCC`, `LIMIT`, `V$MEMGC`, `ADD_OID_CNT`, `GC_OID_CNT`, `V$TRANSACTION`, and `MINMEMSCNINTXS` found in scoped English targets |
| Scoped CPU and memory PDF attachment preservation script | Passed: CPU attachment URL preserved twice; memory attachment URL preserved once |

## Decision

S007 final decision: `COMPLETE`.
