# P208 Backup Recovery and Failure Recovery Audit

Date: 2026-05-16

## Scope

P208 audited Korean backup policy, failure response recovery sections, and startup/shutdown recovery-related sections against their English `arch` targets.

| Korean source | English target |
| --- | --- |
| `DOCK/Home/26. Altibase 기본적인 장애대응 절차__13435879.md` | `arch/Home/Responding to Failures Guide for Altibase__15138818.md`; `arch/Home/Responding to Failures Guide for Altibase/1. Classification by type of failure__15138822.md`; `arch/Home/Responding to Failures Guide for Altibase/2. Procedure by type of failure__15138835.md`; `arch/Home/Responding to Failures Guide for Altibase/3. References__15138869.md` |
| `DOCK/Home/43. Altibase STARTUP _ STOP 과정의 이해__13434993.md` | `arch/Home/Understanding the Altibase Start_Shut down Process__14909450.md`; `arch/Home/Understanding the Altibase Start_Shut down Process/1. Starting Altibase__14909452.md`; `arch/Home/Understanding the Altibase Start_Shut down Process/2. Shutting Altibase Down__14909483.md` |
| `DOCK/Home/50. Altibase 백업정책 결정을 위한 고려사항__14057586.md` | `arch/Home/Considerations for Altibase Backup Policy__14647709.md`; `arch/Home/Considerations for Altibase Backup Policy/1. Backup Types__14647714.md`; `arch/Home/Considerations for Altibase Backup Policy/2. Considerations for Determining Backup Policy__14647722.md`; `arch/Home/Considerations for Altibase Backup Policy/3. Summary (Considerations for Altibase Backup Policy)__14647728.md` |

The Korean sources were treated as authoritative. No Korean source documents were edited.

## Boundary

- Completed only P208.
- Preserved the existing English split-page hierarchy.
- Did not enter replication guide, FAQ backup/recovery, attachment-wide revalidation, or final LLM consolidation work.
- The pre-existing pass2 `jobs.tsv` status change from `P208 ToDo` to `P208 Progress` was inside the workflow runtime area and did not block execution.

## Design Note

No product behavior or architecture changed. Documentation structure changes were limited to normalizing malformed backup-policy tables so backup category, method, description, and recovery-stage fields are searchable and unambiguous. The existing page hierarchy and source attachment placement were preserved.

## Findings And Updates

- Corrected the backup-policy parent support portal link so it no longer renders as a broken concatenated `/en/` link and preserves the Korean-source support portal route.
- Normalized backup-type tables for logical, physical, and incremental backup methods:
  - `aexport` and `iLoader` are now explicitly under `Logical backup`.
  - `Online backup` and `Offline backup` are now explicitly under `Physical backup`.
  - Level 1 differential and cumulative incremental backups are now explicitly under `Incremental backup`.
- Corrected online-backup recovery wording from "while the Altibase server is running" to recovery during the Altibase server startup process, matching the Korean source.
- Clarified the summary table recovery state for online and incremental backup as `Started to CONTROL stage`, preserving the Korean-source CONTROL-stage recovery condition.
- Clarified the failure-response warning that Altibase online log files must not be deleted because arbitrary deletion makes the database unrecoverable.
- Clarified `altibase_sm.log` checkpoint and online-log deletion monitoring by preserving the exact `Remove Online Log File at LFG [0]: File[11252 ~ 11253]` message as a code literal.
- Startup/shutdown recovery sections were audited for PROCESS/CONTROL/META/SERVICE recovery stages, incomplete recovery online-log reset guidance, META restart recovery, `SHUTDOWN IMMEDIATE`, and `ABORT`; no additional English edits were needed after the earlier pass2 corrections.

## Attachment And Link Evidence

- Scoped Korean source pages contain 2 unique URL-backed document-format attachments.
- Both Korean source PDF URLs are preserved in the scoped English target set.
- Scoped grep found no empty links, Confluence macro error markers, malformed `support.altibase.com/)[/en/]` links, residual Korean text, or stale recovery wording checked for this job after edits.

## Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p208-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Scoped grep for empty links, Confluence macro errors, malformed support links, stale recovery wording, known Korean-source typos, and residual Korean text | Passed, no matches |
| Scoped document-format attachment preservation grep | Passed, 2 Korean source PDF URLs preserved |
| Scoped Markdown table pipe-count check | Passed |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 6 edited English pages |

## Remaining Risk

- External HTTP availability was not tested; P208 used grep-based source-link and attachment preservation checks.
- Legal boilerplate beyond the technical support contact remained outside the content changes because this job focused on backup, recovery, failure response, startup recovery, archive log, online/offline/logical/incremental backup, warnings, attachments, and links.
