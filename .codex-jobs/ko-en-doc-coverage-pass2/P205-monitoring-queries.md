# P205 Monitoring Queries Audit

Date: 2026-05-16

## Scope

P205 audited the Korean Altibase monitoring queries guide against the English split guide targets.

| Korean source | English targets |
| --- | --- |
| `DOCK/Home/59. Altibase 모니터링 쿼리 가이드__10060431.md` | `arch/Home/Altibase Monitoring Queries Guide__14058229.md`; `arch/Home/Altibase Monitoring Queries Guide/**` |

The Korean source was treated as authoritative. No Korean source documents were edited.

## Design Note

This job does not change behavior, architecture, or the documentation structure. The existing English split-page structure was preserved. The job updates English content inside the existing pages and refreshes `manifest.json` metadata for the edited pages.

## Findings And Updates

- Confirmed that the monitoring query IDs are semantically covered: the Korean source and scoped English targets both contain 72 unique query IDs from `SS01` through `RP06`.
- Restored Korean-source version conditions and alternative SQL blocks that were missing or unclear in English, including:
  - `SV01` Altibase v4 service-thread query.
  - `TS01` memory tablespace variants for Altibase v5.5.1+, v5.3.3, and v4.
  - `TS03` disk tablespace variants for Altibase v5.5.1+, v5.3.3/v5.3.5 with `BUG-31372`, v5.1.5, and v4.
  - `OB01`, `OB03`, `OB05`, `OB06`, and `OB09` older-version object queries.
- Restored or clarified Korean-source version warnings for `CLIENT_APP_INFO`, `TIMED_STATISTICS`, `START_FLAG`, `REPL_MODE`, role-related privilege filters, package/job columns, constraint `CHECK_CONDITION`, tablespace queries, redo log queries, GC queries, disk buffer queries, and object query columns.
- Corrected meta-table and performance-view references where the English text or SQL drifted from the Korean source, including `SYSTEM_.SYS_TABLES_`, `TABLE_OID`, `V$MEM_TABLESPACES`, `V$VOL_TABLESPACES`, `INDEX_SEG_PID`, `LF_PREPARE_WAIT_COUNT`, `PREPARE_LOG_FILE_COUNT`, and `V$REPGAP`.
- Preserved Korean-source SQL identifiers exactly where the source contains them, including the `STAUS` alias in `RP01`.
- Preserved the Korean-source monitoring guide PDF attachment URL in the English parent and overview pages.

## Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p205-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Scoped query ID comparison | Passed, 72 Korean IDs and 72 English IDs, with no missing or extra IDs |
| Scoped SQL/code block comparison | Passed, 88 Korean blocks and 88 English blocks using a line-based fenced-code parser |
| Scoped fenced-code balance check | Passed for all scoped English files |
| Scoped grep for residual Korean text, empty links, Confluence macro errors, and stale typo patterns | Passed; only the expected `INTERVAL` substring matched the broad `NTERVAL` typo pattern |
| Scoped monitoring guide PDF attachment preservation grep | Passed, 2 preserved English links |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 18 edited English pages |

## Remaining Risk

- External HTTP availability was not tested; P205 used source-link and attachment-preservation grep checks.
- The Korean source contains a few apparent source-level typos, including the `RP01` alias `STAUS` and the v5.1.5 `TS03` SQL expression structure. They were preserved in English because the Korean source is authoritative for this pass.
