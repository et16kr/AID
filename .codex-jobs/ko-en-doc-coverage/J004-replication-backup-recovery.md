# J004 Replication, Backup, and Recovery Review Note

Date: 2026-05-15

## Scope

J004 compared Korean DOCK replication, replication constraints, backup policy, failure response, and recovery-related technical documents against their English arch counterparts. Korean source documents remained authoritative and were not edited.

## Boundary

- Updated only scoped English technical Markdown documents, `manifest.json`, the review report, and workflow job tracking.
- Preserved the existing English split-page structure for the failure response, startup/shutdown, and backup policy documents.
- Did not enter FAQ coverage, development/API coverage, migration, final attachment-wide coverage, or final LLM consolidation work.

## Documentation Structure Impact

No architecture or product behavior change was introduced. The documentation-structure change was limited to normalizing malformed backup policy comparison tables so the Korean-source recovery-point, recovery-time, backup-time, transaction-impact, and summary relationships remain readable in English.

## Main Updates

- Rechecked the J004 mappings for failure response, replication configuration, replication constraints, backup policy, and startup/shutdown recovery procedures.
- Preserved J004 Korean source document-format attachment links in English counterparts; no missing `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, or `.zip` links remained.
- Corrected replication configuration wording for the Altibase `7.1.0` baseline, disk-sharing non-support, Lazy/Eager behavior, Off-Line Replicator use, HA standby shutdown state, N-way replication, `REPLICATION_MAX_LOGFILE`, bulk-change handling, and Parallel Applier DML processing.
- Corrected replication constraints for non-replicated columns, partitioned-table constraints, DDL constraints, memory/disk-table separation, the missing `ERR-61035` update-conflict error message, conflict-mitigation examples, and `RP_MSGLOG_FLAG` logging.
- Corrected backup policy recovery tables and summary tables so online backup, offline backup, logical backup, and incremental backup capabilities are distinguishable.
- Tightened failure-response and startup/shutdown recovery wording for `REP_GAP`, replication sender counts, SQL conflict tracing, selective recovery, and `kill -9`.

## Verification

Verification is recorded in `KO_EN_DOC_REVIEW_REPORT.md` for this job.
