# S008 Tech Replication

Date: 2026-05-16

Workspace: `/home/et16/AID`

## Requirement And Boundary

S008 performs a semantic-unit audit of the Korean replication configuration and replication constraints technical documents against their English `arch` targets. The scoped Korean sources are authoritative and were not edited.

Scoped Korean sources and English targets:

- `DOCK/Home/27. Altibase 이중화 구성 가이드__13828098.md` -> `arch/Home/Altibase Replication Configuration Guide__14647672.md`
- `DOCK/Home/49. Altibase 이중화 제약사항 가이드__19333729.md` -> `arch/Home/Altibase Replication Constraints Guide__22643008.md`

This job covers only S008. It does not run the `llm-reference` consolidation workflow, does not edit Korean source documents, and does not delete or move English source documents. Direct comparison found no English source change was required, so `manifest.json` metadata was not changed.

## Required Reading

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/prompts/S008.md`
- `semantic-coverage/README.md`
- `semantic-coverage/doc-mapping.tsv`
- The two Korean source documents and the two English target pages listed in the mapping

Previous J/P workflow reports were used only as orientation. Coverage decisions in `semantic-coverage/matrices/S008-tech-replication.tsv` are based on direct inspection of the scoped Korean and English files.

## Pre-Edit State

- Branch: `combine`
- `git status --short` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified from `S008 ToDo` to `S008 Progress`.
- `git status --short --untracked-files=all -- . ':(exclude).codex-jobs' ':(exclude).codex-jobs/**'` produced no output, so there were no uncommitted project files outside the workflow area before S008 edits.

## Design Note

S008 adds the semantic matrix and per-job note for the replication guides:

- `semantic-coverage/matrices/S008-tech-replication.tsv`
- `semantic-coverage/notes/S008-tech-replication.md`

The product documentation structure is unchanged. Both Korean sources are single-page guides, and each maps to one English `arch` page. The matrix records coverage by exported metadata, overview sections, heading-level concepts, paragraph groups, list items, table-row groups, image references, warnings, configuration properties, command/code blocks, and the legacy PDF attachment. Long tables and code blocks are summarized in the matrix while preserving exact identifiers, view-independent terms, property names, command text, version conditions, and attachment URLs.

## Audit Summary

### Replication Configuration Guide

The English replication configuration guide preserves the Korean source semantics for:

- high-availability options, `Node`, `Fail-over`, performance and downtime goals, disk-sharing limitations, network-replication performance, separate DB continuity, and the `Altibase v7.1.0` or later basis;
- the replication concept, `Storage-Manager`, `Sender`, `Receiver`, transaction-log flow, asynchronous log-based replication, PK requirement, and multiple-network option;
- Sender `xLog` contents, INSERT/UPDATE/DELETE sender-log contents, Lazy/Eager mode behavior, Receiver before-value comparison, acknowledgment handling, retransmission position tracking, and network-failure resend;
- data conflict and gap risks, same-PK update conflict, conflict types, PK-range Active/Active avoidance, and `REPLICATION_UPDATE_REPLACE` limitations;
- `Off-Line Replicator` behavior from `Altibase v5.3`, HA-solution Active/Standby service configuration, data-delay handling, per-session Lazy/Eager choices, Eager conflict behavior, and conflict-preventing service design;
- conflict mitigation options including `REPLICATION_UPDATE_REPLACE=1`, Master / Slave rules, and TimeStamp conflict handling;
- Active/Standby plus Off-Line Replicator consistency design, N-way replication up to 32 peer nodes, design-stage mode/solution choices, disk-capacity planning with `REPLICATION_MAX_LOGFILE`, bulk-change methods using `LIMIT` and `ALTER SESSION SET REPLICATION = FALSE;`, Sender monitoring, dedicated 1G-or-higher replication lines, Parallel Applier, Sequence Replication, and configuration constraints.

### Replication Constraints Guide

The English replication constraints guide preserves the Korean source semantics for:

- Altibase's network-only data synchronization method, network delay/disconnection constraints, and related replication configuration guide reference;
- independent DB storage, redo-log to `xlog` conversion by `Sender`, `Receiver` apply, and the need to understand network delay/conflict constraints;
- Lazy/Eager synchronization methods, performance versus consistency trade-offs, no absolute multi-store consistency guarantee, and session-level mode configuration;
- replication object constraints, PK and LOB key restrictions, matching column/PK/`NOT NULL` requirements, memory/disk `xLog` size limits, 32 connection maximum, character set/national character set matching from `Altibase v5.3.3`, non-replicated columns, partitioned tables, and `Replication_ddl_enable` DDL exceptions;
- Cross Active-Active, PK update prohibition with delete/insert workaround, Sequence Replication cautions, Gigabit NIC recommendation, and memory/disk replication object separation;
- asynchronous conflict risk, conflict type/error-code table, valid INSERT Conflict code flow, `$ALTIBASE_HOME/trc/altibase_rp_conflict.log`, redo-log rollback reason, recommended UPDATE-first code flow, UPDATE Conflict behavior, `REPLICATION_UPDATE_REPLACE=1`, conflict mitigation by workload and PK separation, and `RP_MSGLOG_FLAG` setup.

### Attachment Evidence

The replication configuration Korean source contains embedded image links but no URL-backed document-format attachments.

The replication constraints Korean source contains one URL-backed document-format attachment:

- `ALTIBASE_이중화_제약사항_가이드.pdf`

The English constraints guide preserves this PDF URL in:

- `arch/Home/Altibase Replication Constraints Guide__22643008.md`

## Self-Review

- Scope checked: only S008 evidence files and the S008 workflow status file were changed.
- Korean authority checked: both scoped Korean replication guides were inspected directly with line-numbered reads.
- English target checked: both mapped English replication guide target pages were inspected directly.
- Matrix checked: the S008 matrix uses the exact required TSV header, one physical row per matrix unit, allowed status values only, and no `missing`, `unverified`, or `recheck_required` rows.
- Terminology checked: `Sender`, `Receiver`, `xLog`, `Lazy`, `Eager`, `Off-Line Replicator`, `REPLICATION_UPDATE_REPLACE`, `REPLICATION_MAX_LOGFILE`, `ALTER SESSION SET REPLICATION = FALSE;`, `Parallel Applier`, `Replication_ddl_enable`, `RP_MSGLOG_FLAG`, and `$ALTIBASE_HOME/trc/altibase_rp_conflict.log` are preserved as technical identifiers.
- Product docs checked: no English source change was needed, so `manifest.json` metadata remained valid and unchanged.

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
| S008 TSV header and column-count check | Passed: 59 data rows, 15 columns each |
| S008 coverage status check | Passed: 55 `covered`, 4 `not_applicable` |
| S008 unresolved-status scan | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Full matrix unresolved-status scan over `semantic-coverage/matrices` | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Scoped empty-link and macro-artifact scan over S008 English targets and evidence | Passed with exit code 1, meaning no matches |
| Scoped residual Korean text scan over S008 English targets | Passed with exit code 1, meaning no Korean text remains in the English target pages |
| Scoped fenced-code balance check | Passed: D027 Korean/English both 0 fenced markers; D049 Korean/English both 6 fenced markers |
| High-risk identifier grep for replication configuration | Passed: `Altibase version 7.1.0`, `Sender`, `Receiver`, `xLog`, `Lazy`, `Eager`, `REPLICATION_UPDATE_REPLACE`, `Off-Line Replicator`, `Altibase v5.3`, `Active/Standby`, `REPLICATION_MAX_LOGFILE`, `LIMIT`, `ALTER SESSION SET REPLICATION = FALSE;`, `Parallel Applier`, `Sequence replication`, `N-way`, and `32` found in the English target |
| High-risk identifier grep for replication constraints | Passed: `Replication`, `Sender`, `Receiver`, `xlogs`, `Lazy`, `Eager`, `Altibase v5.3.3`, `128 KB`, `32`, `Replication_ddl_enable`, `Cross Active-Active`, `ERR-11058`, `ERR-61000`, `ERR-61035`, `REPLICATION_UPDATE_REPLACE`, `$ALTIBASE_HOME/trc/altibase_rp_conflict.log`, `RP_MSGLOG_FLAG`, `alter system set RP_MSGLOG_FLAG = 6`, and the preserved PDF filename URL token found in the English target |
| Scoped replication PDF attachment preservation check | Passed: the Korean source PDF URL is present in both the Korean source and English constraints target |

## Decision

S008 final decision: `COMPLETE`.
