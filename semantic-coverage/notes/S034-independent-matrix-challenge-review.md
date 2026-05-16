# S034 Independent Matrix Challenge Review

## Requirement And Boundary

- Job: `S034`
- Scope: challenge existing semantic-coverage matrix rows marked `covered`, especially high-risk, table-heavy, code-heavy, SQL-heavy, and attachment/link rows.
- Required workflow: `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`.
- Final decision for this job: `COMPLETE`.

S034 is an independent challenge pass over existing evidence. It does not replace S003-S031 direct source audits, S032 aggregate closure, or S033 source stabilization. It samples covered rows, inverse-searches key identifiers in the English target files, re-reads the Korean source and English target context directly, and records whether any covered row is a false positive or has weak evidence.

This job did not run the `llm-reference` consolidation workflow and did not edit product source documents under `DOCK/`, `faq/`, `arch/`, or `FAQE/`.

## Required Reading And Preflight

Read before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- Existing semantic-coverage matrices and notes, especially S032 and S033
- The Korean source and English target files for the challenged sample rows

The required handoff check was run before editing:

```bash
git status --porcelain --untracked-files=all -- . ":(exclude).codex-jobs" ":(exclude).codex-jobs/**"
```

Result: no output.

## Design Note

S034 does not change product-document behavior, architecture, or documentation structure. It adds independent challenge evidence:

- `semantic-coverage/matrices/S034-independent-matrix-challenge-review.tsv`
- `semantic-coverage/notes/S034-independent-matrix-challenge-review.md`
- an S034 section in `KO_EN_SEMANTIC_COVERAGE_REPORT.md`

No English Markdown source page changed, so `manifest.json` did not require metadata updates.

## Challenge Method

The challenge used two passes.

First, an automated inverse-search scan parsed S003-S031 `semantic-coverage/matrices/S*.tsv` rows with `coverage_status=covered` and non-empty `required_identifiers`. It searched the listed English target files for identifier hits, prioritizing rows with technical unit types and low exact-hit ratios. This considered 4,665 covered source-audit, attachment, and classification rows and produced 170 weak candidates. Those candidates were not treated as failures by themselves because exact-string search is sensitive to normal technical-document differences such as whitespace around `=`, Markdown emphasis around placeholders, translated prose, comma-formatted numbers, and intentionally condensed GUI screenshot rows.

Second, S034 manually sampled 24 rows from S003-S031. The sample intentionally covered:

- technical documents and FAQ documents;
- installation, platform setup, monitoring, replication, backup/recovery, development/API, conversion, Docker, error messages, utilities, and attachment/link evidence;
- tables, SQL blocks, command blocks, configuration snippets, error-code rows, and URL-backed attachments;
- low exact-hit candidates from the automated scan.

Each sampled row was checked by re-reading the scoped Korean source lines and the English target lines directly, then inverse-searching the important identifiers or whitespace-normalized equivalents in the English target.

## Challenge Results

Matrix file: `semantic-coverage/matrices/S034-independent-matrix-challenge-review.tsv`

Rows by unit type:

- `matrix_challenge`: 24
- `inverse_search_candidate_scan`: 1

Rows by coverage status:

- `covered`: 25
- `missing`: 0
- `unverified`: 0
- `recheck_required`: 0

No false-positive covered row was found in the sampled set. No English source edit was required.

## Sample Evidence

| S034 row | Original row | Area | Independent challenge result |
| --- | --- | --- | --- |
| `S034-C001` | `S003-D031-U025` | Installation license MAC lookup table | Passed: English preserves Linux `ifconfig`, AIX `lscfg`, HP-UX `lanscan`, Windows `ipconfig /all`, and physical-address guidance. |
| `S034-C002` | `S004-D021-U023` | Direct I/O mount option table | Passed: English preserves `convosync=direct`, ZFS unsupported, AIX `-o dio`, Windows, and Linux filesystem rows. |
| `S034-C003` | `S006-D059-U060` | Monitoring TS03 SQL | Passed: English preserves `[TS03]`, `V$TABLESPACES`, `V$DISK_UNDO_USAGE`, `SYS_UNDO_TBS_EXTENT_SIZE`, `V$UNDO_TBS`, and version-specific SQL variants. |
| `S034-C004` | `S008-D049-U018` | Replication conflict error table | Passed: English preserves `ERR-11058`, `ERR-61000`, `ERR-61035`, and the INSERT/DELETE/UPDATE conflict rows. |
| `S034-C005` | `S009-D050-U021` | Backup incomplete recovery table | Passed: English preserves incomplete recovery, `UNTIL CANCEL`, and `UNTIL TIME`. |
| `S034-C006` | `S010-D034-U040` | APRE error-message section | Passed: English preserves both SQLCODE pairs, invalid length/literal causes, `to_number` example, and corrective actions. |
| `S034-C007` | `S011-D066-U011` | PHP ODBC DSN block | Passed: English preserves `[Altibase]`, driver path, server IP, and port. Exact search needed whitespace-normalized key/value matching. |
| `S034-C008` | `S016-D036-U018` | Lazy/Eager synchronization comparison | Passed: English preserves the Lazy log-transfer-success semantics and the Eager peer-commit synchronization guarantee. |
| `S034-C009` | `S017-D040-U268` | Oracle-to-Altibase sequence conversion table | Passed: English preserves `MAXVALUE`, `NOMAXVALUE`, Oracle 28-digit limit, and Altibase sequence range with comma-formatted numbers. |
| `S034-C010` | `S017-D070-U190` | Migration Center GUI option row | Passed after weak-evidence review: English preserves the actionable `Migration > Migration Options`, `DB to DB`, and `DB to File` semantics. S017 documents that screenshot-only images are intentionally omitted from the condensed English guide. |
| `S034-C011` | `S018-D067-U020` | Docker install validation output | Passed: English preserves `docker version`, client/server `19.03.2`, API `1.40`, `containerd`, and `runc`. |
| `S034-C012` | `S019-D020-U007` | Technical PDF attachment | Passed: English preserves the exact 202312 configuration-guide PDF download URL. |
| `S034-C013` | `S020-F01-01-U016` | FAQ supported platform table | Passed: English preserves glibc `2.3.4`, Ubuntu/Redhat/CentOS/Fedora/openSUSE ranges, and Oracle Linux `7.1`. |
| `S034-C014` | `S021-F02-13-U004` | PUBLIC SYNONYM SQL syntax | Passed: English preserves `DROP PUBLIC SYNONYM`, `SYNONYM_NAME`, and `PRINTLN`. |
| `S034-C015` | `S022-F02-23-U013` | JOB property section | Passed: English preserves `JOB_THREAD_QUEUE_SIZE`, queue examples, default/minimum `64`, `Read-Only`, and `X$PROPERTY` verification. |
| `S034-C016` | `S023-F03-03-U007` | Replication DDL operation table | Passed: English preserves stop replication and drop-table-from-replication steps. Exact search needed to ignore Markdown emphasis around placeholders. |
| `S034-C017` | `S024-F04-03-U012` | Online backup and time-based recovery SQL | Passed: English preserves `SYS_TBS_DISK_TEMP`, `ALTER DATABASE CREATE DATAFILE`, recovery until `2015-07-23:14:01:00`, and `META RESETLOGS`. |
| `S034-C018` | `S025-F07-03-03-U010` | unixODBC INI sample | Passed: English preserves `[ODBC Data Sources]`, `[Altiodbc]`, `Port = 40501`, `FetchBufferSize = 64`, and `Trace = 0`. |
| `S034-C019` | `S026-F08-12-U006` | Table/column definition SQL | Passed: English preserves `CHECK_CONDITION`, `SYSTEM_.SYS_CONSTRAINTS_`, `C.COLUMN_ORDER`, and the 6.3.1-or-later SQL section. |
| `S034-C020` | `S027-F09-07-U006` | `ERR-311E0` solution | Passed: English preserves `TEMP_TBS_MEMORY`, the SELECT hint example, performance note, and 6.3.1-or-later upgrade guidance. |
| `S034-C021` | `S028-F09-17-U012` | `ERR-11075` replication cause | Passed: English preserves `REPLICATION_LOCK_TIMEOUT`, active/standby scenario, and `altibase_rp.log` behavior. |
| `S034-C022` | `S029-F09-24-U011` | `ERR-41059` OS fallback commands | Passed: English preserves `netstat`, `lsof`, `ipcs -m`, `ipcs -ma`, `NATTCH`, and OS-specific examples. |
| `S034-C023` | `S030-F11-02-01-U011` | iLoader CRLF upload command | Passed: English preserves `-r "%r%n"`, release `5.5.1.4.10`, and `Load Count  : 2(T)`. |
| `S034-C024` | `S031-L063` | FAQ ZIP attachment | Passed: English preserves the exact `altimon_for_windows.zip` download URL and adjacent support artifacts. |

## Weak Evidence Findings

The automated exact-match scan surfaced weak candidates, but manual inspection showed no coverage defect in the sample.

- Key/value configuration examples sometimes use spaces around `=`, so exact search for `Port=20300` misses `Port = 20300`.
- Placeholder SQL in English may use Markdown emphasis, so exact search for `ALTER REPLICATION rep_name STOP` misses `ALTER REPLICATION *rep_name* STOP`.
- Numeric limits may be comma-formatted in English, so exact search for `9223372036854775806` misses `9,223,372,036,854,775,806`.
- The Migration Center English guide intentionally condenses GUI screenshot tables into prose. The challenged sample preserved the actionable menu path and option semantics; screenshot-only rows are separately classified by S017.

These were recorded as weak evidence cases, not false positives.

## Self-Review

Self-review checked that:

- The S034 matrix header matches the required TSV schema.
- Every S034 matrix row has exactly 15 TSV fields.
- S034 uses only allowed coverage-status values.
- The sample includes both technical and FAQ coverage, high-risk subject areas, table/code-heavy pages, and attachment/link rows.
- The Korean and English files for every sampled row were read directly.
- No sampled `covered` row needed to become `missing`, `unverified`, or `recheck_required`.
- No English source document or `manifest.json` metadata changed.

## Verification

Verification commands were run after edits.

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK/Home -type f -name '*.md' | wc -l` | Passed: 51 |
| `find faq/Home -type f -name '*.md' | wc -l` | Passed: 115 |
| `find arch/Home -type f -name '*.md' | wc -l` | Passed: 181 |
| `find FAQE/Home -type f -name '*.md' | wc -l` | Passed: 241 |
| Required stale-artifact grep over `arch/Home`, `FAQE/Home`, and `semantic-coverage` | Passed: expected-no-match grep exited 1 |
| Unresolved matrix-status grep | Passed: expected-no-match grep exited 1 |
| S034 matrix TSV shape/status validation | Passed: 25 rows, 15 fields per row; `covered` 25 |

External HTTP availability was not tested. S034 used local source files, exact or normalized identifier searches, and direct Korean/English context inspection.

## Final Decision

`COMPLETE`: S034 independently challenged sampled `covered` matrix evidence and found no false-positive coverage row in the sampled set. The workflow-level decision remains `RECHECK_REQUIRED` until S035 creates the final semantic coverage decision.
