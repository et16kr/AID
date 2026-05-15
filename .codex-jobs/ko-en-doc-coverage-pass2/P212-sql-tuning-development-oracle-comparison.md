# P212 SQL Tuning, Development, and Oracle Comparison Audit

Date: 2026-05-16

## Scope

P212 audited the Korean Altibase Development Guide, SQL Tuning Guide, and Altibase/Oracle Comparison documents against their English `arch` targets.

| Korean source | English target |
| --- | --- |
| `DOCK/Home/36. Altibase 개발가이드__7341274.md` | `arch/Home/Altibase Development Guide__14058519.md`; `arch/Home/Altibase Development Guide/**` |
| `DOCK/Home/37. Altibase SQL 튜닝 가이드__19333563.md` | `arch/Home/Altibase SQL Tuning Guide__22643010.md` |
| `DOCK/Home/39. Altibase, Oracle 비교 자료__14058137.md` | `arch/Home/Altibase_Oracle Comparison__16875638.md` |

The Korean sources were treated as authoritative. No Korean source documents were edited.

## Boundary

- Completed only P212.
- Preserved the existing English parent/split-page structure for the Development Guide.
- Did not enter migration/conversion, VC guides, Docker/GeoServer/SQuirrel, FAQ, attachment-wide revalidation, or final LLM consolidation jobs.
- The pre-existing pass2 `jobs.tsv` status change for P212 was inside the workflow runtime area and did not block execution.

## Design Note

No product behavior or repository architecture changed. Documentation structure changes were limited to restoring Korean-source overview/contact/legal text, turning flattened examples into fenced code blocks, restoring a missing trace-log subsection, and repairing exported table-row structure in the Altibase/Oracle comparison page.

## Findings And Updates

- Restored Korean-source overview material in the Development Guide and SQL Tuning Guide, including related technical document references, support portal route, support center number, and informational/legal disclaimer text.
- Corrected Development Guide design guidance for Lazy/Eager replication, conflict-prevention references, Off-Line replicator conditions, backup method descriptions, HPT/table-design wording, redo log capacity considerations, and DBMS conversion reference links.
- Corrected Development Guide development-stage content for `CONNTYPE`, `AUTO_COMMIT`, `ALTER SYSTEM`, threaded connection protocol order, CLI/ODBC resource release, timeout examples, `altibase_cli.ini`, prepared statement examples, execution-plan examples, and bulk-change replication wording.
- Corrected Development Guide trace-log content for `$ALTIBASE_HOME/trc`, `altibase_boot.log`, `$ALTIBASE_HOME/msg/`, `altibase_sm.log`, `DB` property logging, `altibase_rp.log`, the missing `altibase_rp_conflict.log` section, replication conflict meanings, and abnormal termination support guidance.
- Corrected client application error content for `Communication link failure`, `Conversion not applicable`, `Invalid cursor state`, `Not defined cursor`, `PREPARE -> BINDING -> EXECUTE`, `TRX_UPDATE_MAX_LOGSIZE`, the 50 MB session example, and the `09-18. ERR-11118` reference link.
- Corrected Altibase/Oracle comparison content for support/legal overview text, deadlock detection wording, Altibase tablespace count `65,536`, DBMS Watcher, partition operation tables, recovery labels, `CONNECT_BY_ISCYCLE`, `CREATE TABLE AS SELECT`, `Parallel Select` support, binary data type row alignment, `CLI`, and `manifest.json` metadata.
- Rebuilt the Altibase/Oracle Built-In Function table at identifier level so blank category cells, Oracle/Altibase function names, unsupported markers, added rows, and misspelled identifiers match the Korean source semantics. Examples include `REPLACE2`, `REGEXP_COUNT`, `BASE64_DECODE_STR`, `BASE64_ENCODE`, `ROWIDTONCHAR`, `TO_BINARY_DOUBLE`, `LAST_VALUE`, `LEAD`, `PREDICTION_PROBABILITY`, `XMLCOLATTVAL`, and `PERCENTILE_DISC`.
- Preserved non-conflicting English-only clarification where useful, including the `REP1` example-name note and the English-only `Invalid character in use` client error section.
- Updated `manifest.json` metadata for all 7 edited English Markdown pages.

## Attachment And Link Evidence

- Scoped Korean source pages contain 4 document-format references:
  - `ALTIBASE_개발가이드.pdf`
  - `ALTIBASE_개발가이드_5.3.pdf`
  - `D68_Altibase_SQL_Tuning_Guide.pdf`
  - `ALTIBASE_ORACLE_비교자료.pdf`
- All 4 filenames or source URLs are preserved in the scoped English target set.
- The Development Guide PDFs are Korean-source legacy placeholders without downloadable URLs, so the English page records the exact Korean filenames as placeholders.
- Scoped grep found no empty links, Confluence macro errors, malformed support links, invalid `http://altibase_env.mk` links, or checked stale export typo patterns.

## Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/p212-manifest.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK -type f -name '*.md' \| wc -l` | 51 |
| `find faq -type f -name '*.md' \| wc -l` | 115 |
| `find arch -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE -type f -name '*.md' \| wc -l` | 241 |
| Scoped grep for empty links, Confluence macro errors, malformed support links, invalid local links, and stale typo patterns | Passed |
| Scoped document-format attachment preservation script | Passed, 4 Korean source references preserved |
| Altibase/Oracle Built-In Function identifier/table-row comparison | Passed, 262 Korean data rows matched 262 English data rows |
| Edited-page manifest metadata comparison (`body_chars`, `word_count`) | Passed for all 7 edited English pages |

## Remaining Risk

- External HTTP availability was not tested; P212 used grep-based source-link and attachment preservation checks.
- The Korean source contains legacy `#` placeholders for Development Guide PDFs; the English target preserves the exact filenames but cannot add download URLs that the Korean source does not provide.
- The Altibase/Oracle comparison document remains a feature comparison against Oracle 12c and keeps legacy product/version context where the Korean source keeps it.
