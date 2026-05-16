# S009 Tech Backup Recovery

Date: 2026-05-16

Workspace: `/home/et16/AID`

## Requirement And Boundary

S009 performs a semantic-unit audit for backup policy, recovery, archive/noarchive mode implications, failure response items that affect recoverability, and startup recovery behavior.

Scoped Korean sources and English targets:

- `DOCK/Home/50. Altibase 백업정책 결정을 위한 고려사항__14057586.md` -> `arch/Home/Considerations for Altibase Backup Policy__14647709.md`; `arch/Home/Considerations for Altibase Backup Policy/1. Backup Types__14647714.md`; `arch/Home/Considerations for Altibase Backup Policy/2. Considerations for Determining Backup Policy__14647722.md`; `arch/Home/Considerations for Altibase Backup Policy/3. Summary (Considerations for Altibase Backup Policy)__14647728.md`
- `DOCK/Home/26. Altibase 기본적인 장애대응 절차__13435879.md` -> `arch/Home/Responding to Failures Guide for Altibase/2. Procedure by type of failure__15138835.md`
- `DOCK/Home/43. Altibase STARTUP _ STOP 과정의 이해__13434993.md` -> `arch/Home/Understanding the Altibase Start_Shut down Process__14909450.md`; `arch/Home/Understanding the Altibase Start_Shut down Process/1. Starting Altibase__14909452.md`; `arch/Home/Understanding the Altibase Start_Shut down Process/2. Shutting Altibase Down__14909483.md`

`DOCK/Home/26. Altibase 기본적인 장애대응 절차__13435879.md` and `DOCK/Home/43. Altibase STARTUP _ STOP 과정의 이해__13434993.md` are primarily owned by S005. S009 therefore adds only backup/recovery-specific cross-reference rows for D026 and D043, not a second full audit.

This job does not run the `llm-reference` consolidation workflow, does not edit Korean source documents, and does not delete or move English source documents. Direct comparison found no English source change was required, so `manifest.json` metadata was not changed.

## Required Reading

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/prompts/S009.md`
- `semantic-coverage/README.md`
- `semantic-coverage/doc-mapping.tsv`
- The three Korean source documents and mapped English target documents listed above

Previous J/P workflow reports were used only as orientation. Coverage decisions in `semantic-coverage/matrices/S009-tech-backup-recovery.tsv` are based on direct inspection of the scoped Korean and English files.

## Pre-Edit State

- Branch: `combine`
- `git status --short` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified from `S009 ToDo` to `S009 Progress`.
- `git status --short --untracked-files=all -- . ':(exclude).codex-jobs' ':(exclude).codex-jobs/**'` produced no output, so there were no uncommitted project files outside the workflow area before S009 edits.
- D050 is fully owned by S009. D026 and D043 are cross-reference only because S005 owns their full audit.

## Design Note

S009 adds the semantic matrix and per-job note for the backup/recovery technical scope:

- `semantic-coverage/matrices/S009-tech-backup-recovery.tsv`
- `semantic-coverage/notes/S009-tech-backup-recovery.md`

The product documentation structure is unchanged. The matrix records the backup policy source by semantic units for metadata, overview, support contact, backup-type definitions, table rows, recovery-point/recovery-time policy, transaction impacts, retention guidance, disk partition guidance, summary comparison rows, references, and the legacy PDF attachment. Dense summary tables are split by backup method where one Korean row contains independent facts for multiple methods.

D026 and D043 rows are topic-specific cross-references only. S009 records failure-response online-log recoverability warnings, physical disk shortage behavior, MVCC online-log growth, staged startup recovery rationale, ABORT restart recovery, and startup/stop attachment preservation. The Korean D043 export exposes `CONTROL` and `META` recovery headings without body content; the matrix records this as `source_limitation` while noting that the English target contains recovery detail that cannot be independently verified from the exported Korean body.

## Audit Summary

### D050 Backup Policy

The English backup-policy parent and split pages preserve the Korean source semantics for:

- data-loss scenarios and backup policy scope, while excluding detailed commands/options;
- backup type classification: logical backup, physical online/offline backup, and incremental backup starting from `Altibase 6.3.1`;
- logical backup with `aexport` and `iLoader`, including `.sql`, `.sh`, FORM, and text data file outputs;
- physical backup of data files and log anchor files, online backup while Altibase is running, offline backup while Altibase is stopped, stable memory checkpoint image behavior, disk temporary tablespace exclusion for online backup, and full database restriction for offline backup;
- incremental backup, `Page Change Tracking`, level 0 baseline backups, level 1 differential backups, and level 1 cumulative backups;
- policy factors: backup target, recovery policy, backup type/cycle/time, retention period, and business/data-owner cooperation;
- recovery points: backup point, complete recovery, incomplete recovery, `UNTIL CANCEL`, `UNTIL TIME`, and backup-type-specific recovery availability;
- recovery time factors for `aexport`, `iLoader`, online backup, offline backup, and incremental backup;
- backup duration and transaction impact, including DDL restriction for `aexport`, Memory GC growth for `iLoader`, online-log growth during online/incremental backups, and service downtime for offline backup;
- retention of at least two backup copies and disk partition separation for backup files;
- summary comparison rows for characteristics, pros, cons, detailed recovery state, archive mode, archive log file management, `backupInfo`, and recovery targets;
- related manuals and the Korean-source legacy backup-policy PDF attachment.

### D026 Failure Response Cross-References

S009 added backup/recovery-specific cross-reference rows only. The English failure-response guide preserves the Korean source semantics for:

- the warning not to delete Altibase online log files because arbitrary deletion makes the database unrecoverable;
- physical disk shortage preventing online log and trace log writes, making the DB appear hung, and requiring disk space to be freed;
- MVCC Garbage Data from bulk changes or long-running queries increasing online log files or physical memory, with `V$STATEMENT`, `V$TRANSACTION`, and `V$MEMGC` diagnostic SQL identifiers preserved.

### D043 Startup Recovery Cross-References

S009 added recovery-specific cross-reference rows only. The English startup/shutdown guide preserves the Korean source semantics for:

- staged startup with `PROCESS`, `CONTROL`, `META`, and `SERVICE` to avoid restrictions on meta migration and recovery functions;
- `STARTUP` through iSQL with `SYSDBA` privileges and DBA tasks such as database creation, meta upgrade, and selective recovery;
- `ABORT` shutdown using `kill -9`, the database consistency caveat, and database recovery during the next startup;
- preservation of the legacy `ALTIBASE_STARTUP_STOP_과정의이해.pdf` source attachment.

The Korean D043 source has `CONTROL` and `META` headings without body content in the exported Markdown. S009 records that recovery-topic export gap as `source_limitation`; it is not treated as missing English content because no Korean body text is available to translate or compare.

## Attachment Evidence

URL-backed document-format attachments in this scope:

- `ALTIBASE_백업정책_결정을_위한_고려사항.pdf`: preserved in `arch/Home/Considerations for Altibase Backup Policy__14647709.md`
- `ALTIBASE_STARTUP_STOP_과정의이해.pdf`: preserved in `arch/Home/Understanding the Altibase Start_Shut down Process__14909450.md` and `arch/Home/Understanding the Altibase Start_Shut down Process/1. Starting Altibase__14909452.md`

D026 has embedded support/reference images but no URL-backed document-format attachments.

## Self-Review

- Scope checked: only S009 evidence files and the S009 workflow status file were changed.
- Korean authority checked: all three scoped Korean source files were inspected directly with line-numbered reads.
- English target checked: the mapped English backup-policy pages and recovery-related failure/startup target pages were inspected directly.
- Duplicate source ownership checked: D026 and D043 rows are cross-reference only and name S005 as primary owner in the matrix notes.
- Matrix checked: the S009 matrix uses the exact required TSV header, one physical row per matrix unit, allowed status values only, and no `missing`, `unverified`, or `recheck_required` rows.
- Terminology checked: `aexport`, `iLoader`, `Page Change Tracking`, `Archive mode`, `CONTROL stage`, `backupInfo`, `UNTIL CANCEL`, `UNTIL TIME`, online log files, log anchor files, `V$STATEMENT`, `V$TRANSACTION`, `V$MEMGC`, and `kill -9` are preserved as technical identifiers.
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
| S009 TSV header and column-count check | Passed: 72 data rows, 15 columns each |
| S009 coverage status check | Passed: 69 `covered`, 2 `not_applicable`, 1 `source_limitation` |
| S009 unresolved-status scan | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Full matrix unresolved-status scan over `semantic-coverage/matrices` | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Scoped empty-link and macro-artifact scan over S009 English targets and evidence | Passed with exit code 1, meaning no matches |
| Scoped attachment preservation grep | Passed: backup-policy PDF found in Korean source and English target; startup/stop PDF found in Korean source and two English targets |

## Decision

S009 final decision: `COMPLETE`.
