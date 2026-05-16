# S016 Tech Development SQL Tuning Comparison

Date: 2026-05-16

Workspace: `/home/et16/AID`

## Requirement And Boundary

S016 performs a semantic-unit audit for the Altibase Development Guide, SQL Tuning Guide, and Altibase/Oracle comparison technical documents.

Scoped Korean sources and English targets:

- `DOCK/Home/36. Altibase 개발가이드__7341274.md` -> `arch/Home/Altibase Development Guide__14058519.md`; `arch/Home/Altibase Development Guide/**`
- `DOCK/Home/37. Altibase SQL 튜닝 가이드__19333563.md` -> `arch/Home/Altibase SQL Tuning Guide__22643010.md`
- `DOCK/Home/39. Altibase, Oracle 비교 자료__14058137.md` -> `arch/Home/Altibase_Oracle Comparison__16875638.md`

This job does not run the `llm-reference` consolidation workflow, does not edit Korean source documents, and does not delete or move English source documents.

## Required Reading

Reviewed before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/prompts/S016.md`
- `semantic-coverage/doc-mapping.tsv`
- The three Korean source documents and mapped English target documents listed above

Previous J/P workflow reports were used only as orientation. Coverage decisions in `semantic-coverage/matrices/S016-tech-development-sql-tuning-comparison.tsv` are based on direct inspection of the scoped Korean and English files.

## Pre-Edit State

- Branch: `combine`
- Initial `git status --short` showed only `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` modified inside the workflow runtime area as `S016` moved to `Progress`.
- No uncommitted project files outside the workflow runtime area were present before S016 edits.

## Design Note

S016 adds semantic evidence only:

- Adds `semantic-coverage/matrices/S016-tech-development-sql-tuning-comparison.tsv`
- Adds `semantic-coverage/notes/S016-tech-development-sql-tuning-comparison.md`
- Updates S016 workflow status in `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv`

The product documentation structure is unchanged. No English `arch/` page required edits in this job, so `manifest.json` metadata was not changed.

The matrix records 599 semantic units covering Development Guide overview/support/reference links, design-stage replication/HA/backup/table/partition/hardware guidance, development-stage connection/thread/resource/timeout/cursor/error/LOB/prepared-statement/tuning/bulk-change guidance, trace-log classification and message rows, client application error sections, SQL Tuning Guide version and attachment rows, and Altibase/Oracle comparison table rows including the full Built-In Function table.

## Audit Summary

### D036 Altibase Development Guide

The split English Development Guide preserves:

- the Korean-source overview, ten related technical document links, support portal route, support center number, and nontechnical legal/intellectual-property notices;
- design guidance for network-based replication, Lazy/Eager replication behavior, conflict-prevention design, log-based replication, Off-Line replicator limitations, HA raw-data policy, archive/cold/iLoader/incremental backup choices, table storage placement, HPT, native/non-native type choices, partition table limitations as of `7.3.0`, hardware/network/disk planning, redo log capacity planning, and DBMS conversion references;
- development guidance for `CONNTYPE`, `AUTO_COMMIT`, `ALTER SESSION SET AUTOCOMMIT = FALSE`, `ALTER SYSTEM`, threaded protocol sequence, connection-pool concurrency, resource cleanup, `SQLFreeStmt`, timeout policies, `altibase_boot.log`, cursor handling, SQL error checking, LOB auto-commit handling, `ClientSide_Auto_Commit`, prepared statement reuse, execution-plan checks, and bulk-change risks;
- trace-log classification for all Korean-source log names and detailed message/action rows for `altibase_boot.log`, `altibase_sm.log`, `altibase_qp.log`, `altibase_rp.log`, `altibase_rp_conflict.log`, `altibase_dk.log`, and `altibase_error.log`;
- client application error coverage for connection, communication, stack, conversion, cursor, literal, data-length, indicator, host-variable, space, lock-timeout, `TRX_UPDATE_MAX_LOGSIZE`, truncation, overflow, and open-statement errors.

The Korean source contains two Development Guide PDF links exported as `#` placeholders. S016 records them as `source_limitation` and confirms the English target preserves the exact legacy filenames without inventing a URL.

### D037 Altibase SQL Tuning Guide

The English SQL Tuning Guide preserves the Korean-source purpose, support route, support center, legal notices, `Altibase v5` basis, and URL-backed `D68_Altibase_SQL_Tuning_Guide.pdf` attachment. The English page also has its own English-space attachment URL; S016 separately verified that the Korean-source URL under attachment id `19333563` is preserved in the `Korean Source Attachments` section.

### D039 Altibase/Oracle Comparison

The English comparison document preserves:

- the `Altibase v7.1 or later` versus `Oracle 12c` scope, support route, support center, and nontechnical legal/intellectual-property notices;
- model comparison rows for architecture, logical structure, physical structure, and numeric/object-count considerations;
- feature comparison rows for supported functions, tools, partition table capabilities, partition operation details, and backup/recovery;
- development support comparison rows for SQL support, data types, APIs, and the complete Built-In Function table.

The matrix records the Built-In Function table at row level: 262 Korean data rows are represented by 262 English data rows. It also records the Korean export artifact in the Oracle `MOVE SUBPARTITION` row and the `CERATE TABLE AS SELECT` source typo as covered because the English target preserves the intended technical identifiers.

The URL-backed `ALTIBASE_ORACLE_비교자료.pdf` source attachment is preserved in the English `Korean Source Attachments` section.

## Attachment And Link Evidence

URL-backed document-format attachments in this scope:

- `D68_Altibase_SQL_Tuning_Guide.pdf`: Korean-source URL preserved in `arch/Home/Altibase SQL Tuning Guide__22643010.md`
- `ALTIBASE_ORACLE_비교자료.pdf`: Korean-source URL preserved in `arch/Home/Altibase_Oracle Comparison__16875638.md`

Source-limited filename-only references:

- `ALTIBASE_개발가이드.pdf`: Korean source uses a legacy `#` placeholder with no downloadable URL.
- `ALTIBASE_개발가이드_5.3.pdf`: Korean source uses a legacy `#` placeholder with no downloadable URL and labels it `ALTIBASE v5.3`.

## Self-Review

- Scope checked: S016 changed only S016 evidence files and S016 workflow status.
- Korean authority checked: all three scoped Korean source files were inspected directly with line-numbered reads.
- English target checked: all mapped English parent/split pages and single-page targets were inspected directly.
- Matrix checked: the S016 matrix uses the exact required TSV header, one physical row per matrix unit, allowed status values only, and no `missing`, `unverified`, or `recheck_required` rows.
- Terminology checked: `Lazy`, `Eager`, `Off-Line replicator`, `Hybrid Partitioned Table (HPT)`, `Partitioned Local Index`, `Non-Partitioned Global Index`, `CONNTYPE`, `AUTO_COMMIT`, `SQLFreeStmt`, `QUERY_TIMEOUT`, `FETCH_TIMEOUT`, `UTRANS_TIMEOUT`, `ClientSide_Auto_Commit`, `TRX_UPDATE_MAX_LOGSIZE`, trace log names, client error messages, Oracle/Altibase comparison identifiers, and exact attachment filenames/URLs are preserved.
- Product docs checked: no scoped English `arch/` Markdown page changed, so no manifest metadata refresh was required.

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
| S016 TSV header and column-count check | Passed: 599 data rows, 15 columns each |
| S016 coverage status check | Passed: 591 `covered`, 6 `not_applicable`, 2 `source_limitation` |
| S016 unresolved-status scan | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Full matrix unresolved-status scan over `semantic-coverage/matrices` | Passed with exit code 1, meaning no `missing`, `unverified`, or `recheck_required` rows |
| Scoped English empty-link and macro-artifact scan, including S016 evidence files | Passed with exit code 1, meaning no matches |
| Scoped stale-pattern scan for `CERATE TABLE`, malformed `MOVE S[UB]`, and broken scoped attachment links | Passed with exit code 1, meaning no matches |
| Scoped residual Korean scan in English targets | Passed with expected matches only for preserved Korean-source attachment filenames: `ALTIBASE_ORACLE_비교자료.pdf`, `ALTIBASE_개발가이드.pdf`, and `ALTIBASE_개발가이드_5.3.pdf` |
| Scoped document-format attachment preservation script | Passed: 2 URL-backed source attachments and 2 legacy placeholders preserved |
| Altibase/Oracle Built-In Function identifier/table-row comparison | Passed: 262 Korean rows align with 262 English rows by Oracle/Altibase identifier tokens |
| `bash -n .codex-jobs/ko-en-semantic-coverage-audit/run-all.sh` | Passed |
| `bash -n .codex-jobs/ko-en-semantic-coverage-audit/run_all.sh` | Passed |

## Decision

S016 final decision: `COMPLETE`.
