# P207 Replication Configuration and Constraints Audit

Date: 2026-05-16

## Scope

P207 audited the Korean replication configuration and replication constraints guides against their English `arch` targets.

| Korean source | English target |
| --- | --- |
| `DOCK/Home/27. Altibase 이중화 구성 가이드__13828098.md` | `arch/Home/Altibase Replication Configuration Guide__14647672.md` |
| `DOCK/Home/49. Altibase 이중화 제약사항 가이드__19333729.md` | `arch/Home/Altibase Replication Constraints Guide__22643008.md` |

The Korean sources were treated as authoritative. No Korean source documents were edited.

## Design Note

This job does not change product behavior, architecture, or the documentation hierarchy. It updates English content inside the existing pages, normalizes exported table headers and one conflict-options table for readability, and refreshes `manifest.json` metadata for the edited English pages.

## Findings And Updates

- Corrected the replication configuration guide support portal link and normalized product naming to `Altibase` in edited passages.
- Corrected disk-sharing, Sender, Receiver, network-failure recovery, Update Conflict, and `REPLICATION_UPDATE_REPLACE` explanations so the English text preserves Korean-source transaction-log and before-value semantics.
- Clarified Off-Line Replicator behavior for Altibase v5.3 or later, including direct reads of failed-node transaction log files, shared-disk or FTP collection options, and HA script automation.
- Clarified HA solution limitations, Active/Standby shutdown meaning, Lazy/Eager session use, replication gap wording, and N-way recovery wording.
- Normalized table headers for high availability methods, xLog contents, sender logs, conflict examples, HA shared-disk layout, Lazy/Eager mode, service separation examples, and summary requirements.
- Split the exported conflict-function table so `REPLICATION_UPDATE_REPLACE=1`, Master / Slave, TimeStamp, and Master / Slave transaction behavior are searchable and unambiguous.
- Clarified disk-capacity guidance for `REPLICATION_MAX_LOGFILE`, bulk-change handling with `ALTER SESSION SET REPLICATION = FALSE;`, Parallel Applier wording, sequence replication wording, DDL constraints, trigger/foreign-key guidance, and memory/disk replication object separation.
- Added the Korean-source support portal and technical support center references to the English replication constraints guide and preserved the Korean-source PDF attachment.
- Clarified the replication constraints guide reference to the Replication Conflict section and marked `REPLICATION_UPDATE_REPLACE` as a literal configuration parameter.

## Attachment And Link Evidence

- `DOCK/Home/27. Altibase 이중화 구성 가이드__13828098.md` contains embedded image links but no URL-backed document-format attachments.
- `DOCK/Home/49. Altibase 이중화 제약사항 가이드__19333729.md` contains one URL-backed PDF attachment, and the same URL is preserved in `arch/Home/Altibase Replication Constraints Guide__22643008.md`.
- Scoped grep found no residual Korean text in the edited English pages and no empty links, Confluence macro errors, malformed support links, or stale typo patterns checked for this job.

## Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p207-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Scoped grep for residual Korean text, empty links, Confluence macro errors, malformed support links, and stale typo patterns | Passed, no matches |
| Scoped document-format attachment preservation grep | Passed, 1 Korean source PDF URL preserved |
| Scoped Markdown table pipe-count check | Passed |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for both edited English pages |

## Remaining Risk

- External HTTP availability was not tested; P207 used grep-based source-link and attachment preservation checks.
- Legal boilerplate beyond the technical support contact remained outside the content changes because this job focused on technical replication configuration, constraints, commands, settings, warnings, attachments, and links.
