# S026 FAQ Monitoring Semantic Coverage Audit

## Requirement And Boundary

- Job: `S026`
- Scope: audit only `faq/Home/08. 모니터링/**` against `FAQE/Home/08. Monitoring/**`.
- Required workflow: `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`.
- Final decision: `COMPLETE`.

This job did not run the `llm-reference` consolidation workflow and did not edit Korean source documents. It changed only scoped English monitoring FAQ pages, `manifest.json`, this note, the S026 matrix, and the S026 workflow status.

## Required Reading And Preflight

Read before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- Scoped Korean and English monitoring FAQ documents listed in `semantic-coverage/doc-mapping.tsv` rows `F08-01` through `F08-12`.

The required handoff check was run before editing:

```bash
git status --porcelain --untracked-files=all -- . ":(exclude).codex-jobs" ":(exclude).codex-jobs/**"
```

Result: no output. The only pre-existing status change was the orchestrator's `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` runtime/status update.

## Design Note

S026 does not change documentation architecture or file organization. The documentation behavior change is limited to correcting scoped English FAQ wording that obscured or misspelled Korean-source identifiers:

- `System information by OS__16876206.md`: corrected Linux command labels from `iogstat` to `iostat` and from `inconfig` to `ifconfig`.
- `How to determine which queries are being rolled back__16876296.md`: corrected `don not use` to `do not use`.
- `Disk tablespace usage/ALTIBASE HDB 5.3.3, 5.3.5__16876253.md`: clarified BUG-31372 wording.
- `Disk table and index usage/ALTIBASE HDB 5.1.5.x__16876234.md`: clarified the DELETE/free-space limitation.
- `Disk table and index usage/ALTIBASE HDB 5.3.x, 5.5.1, 6.1.1, 6.3.1__16876240.md`: clarified BUG-31372 wording and the DELETE/USED behavior.

`manifest.json` metadata was updated for all five changed English Markdown pages.

## Direct Inspection Summary

- Korean source files inspected: 19 Markdown pages under `faq/Home/08. 모니터링/**`.
- English target files inspected: 19 Markdown pages under `FAQE/Home/08. Monitoring/**`.
- Matrix rows: 115.
- Status distribution:
  - `covered`: 90
  - `added`: 6
  - `not_applicable`: 19
  - `source_limitation`: 0
  - `missing`: 0
  - `unverified`: 0
  - `recheck_required`: 0

The audit covered headings, overview paragraphs, version conditions, SQL and command blocks, configuration properties, output examples, warnings, troubleshooting procedures, and URL-backed attachments. Long SQL and output blocks are summarized in the TSV with exact identifiers and line ranges; each corresponding Korean and English block was inspected directly.

## Source Coverage Notes

- `altiProfile`: English preserves `QUERY_PROF_FLAG`, `TIMED_STATISTICS`, `QUERY_PROF_LOG_DIR`, `V$SESSTAT`, `V$SYSSTAT`, `V$MEMSTAT`, binary profile conversion, `-stat` options, and production/disk-usage warnings.
- Lock monitoring: English preserves `v$lock`, `v$lock_statement`, `v$lock_wait`, `ALTER DATABASE ... SESSION CLOSE`, and client PID/session lookup SQL.
- OS system information: English preserves Linux, Sun, AIX, and HP-UX commands and examples. This job corrected the Linux disk/network command labels so they match the Korean source identifiers.
- Windows monitoring tool: English preserves the `altimon_for_windows.zip` URL-backed attachment, configuration settings, execution modes, termination steps, and log path.
- Disk table/index usage: English preserves version-specific `V$USAGE`, `V$SEGMENT`, `X$SEGMENT`, aging warnings, DELETE behavior, table/index count SQL, and BUG-31372 version conditions. This job clarified unclear English wording for Korean-source DELETE and BUG-31372 semantics.
- Disk tablespace usage: English preserves version-specific queries, `V$DISK_UNDO_USAGE`, `SYS_UNDO_TBS_EXTENT_SIZE`, BUG-39985, `REUSABLE_EXT_CNT`, and output examples. This job clarified one BUG-31372 applicability sentence.
- Rollback monitoring: English preserves LSN-based rollback detection and `v$transaction.status=4`; this job corrected the status-code wording for `COMMIT_IN_MEMORY`.
- Memory table/index and tablespace usage: English preserves `V$MEMTBL_INFO`, `GETCOUNT`, `V$MEM_BTREE_HEADER`, `V$VOL_TABLESPACES`, and memory/volatile tablespace SQL.
- altimon: English preserves the `ALTIMON_USER_GUIDE.pdf` URL-backed attachment, setup files, manual references, install/copy steps, connection properties, OS query settings, start command, and log location. The Korean source includes a legacy local `#` label before the actual PDF URL; the URL-backed PDF is preserved in English.
- Undo monitoring: English preserves `V$DISK_UNDO_USAGE`, `TX_EXT_CNT`, `USED_EXT_CNT`, `UNSTEALABLE_EXT_CNT`, `REUSABLE_EXT_CNT`, `TOTAL_EXT_CNT`, the 5.3.3+ transaction/undo SQL, all diagnostic scenarios, corrective actions, `UTRANS_TIMEOUT`, Java/APRE examples, and the `SQLFreeLob()` warning.
- Table/column definitions: English preserves version-specific table and column definition SQL, including `V$DBMS_STATS`, `NUM_ROW`, `CHECK_CONDITION`, and 4.3.9 system-table variants.

## Attachment And Link Evidence

URL-backed document-format attachments in scope:

- `altimon_for_windows.zip`
  - Korean: `faq/Home/08. 모니터링/08-04. Windows 용 모니터링 툴__7340488.md`
  - English: `FAQE/Home/08. Monitoring/Monitoring Tools for Windows__16876220.md`
- `ALTIMON_USER_GUIDE.pdf`
  - Korean: `faq/Home/08. 모니터링/08-10. 알티몬(altimon) 설정 및 실행 방법__6979592.md`
  - English: `FAQE/Home/08. Monitoring/How to set up and execute altimon__16876266.md`

No URL-backed document-format attachment gap remains in this scoped category.

## Self-Review

- Rechecked all `added` rows against the Korean source lines and the edited English target lines.
- Rechecked scoped English for Korean residue, empty links, macro-rendering artifacts, and legacy hash-anchor link patterns.
- Rechecked the matrix for invalid row widths and forbidden successful-job statuses.
- Rechecked edited-page `manifest.json` metadata against the file deltas for `body_chars` and `word_count`.
- Rechecked that no Korean source document was edited and no unrelated user change was reverted.

## Verification

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK/Home -type f -name '*.md' | wc -l` | Passed: 51 |
| `find faq/Home -type f -name '*.md' | wc -l` | Passed: 115 |
| `find arch/Home -type f -name '*.md' | wc -l` | Passed: 181 |
| `find FAQE/Home -type f -name '*.md' | wc -l` | Passed: 241 |
| S026 matrix TSV shape/status validation | Passed: 115 rows, 15 columns; `not_applicable` 19, `covered` 90, `added` 6 |
| Scoped English bad-link/macro/Korean-residue grep | Passed: no matches, `rg` exit code 1 |
| Scoped evidence bad-link/macro grep | Passed: no matches, `rg` exit code 1 |
| Scoped stale wording grep | Passed: no matches for corrected stale strings, `rg` exit code 1 |
| Scoped attachment preservation grep | Passed: four matches; both URL-backed attachments present in Korean and English |
| Scoped English code-fence balance check | Passed: 19 files checked, no odd fence counts |
| Edited-page manifest metadata comparison | Passed for all five edited English pages |
| Full semantic matrix unresolved-status grep | Passed: no `missing`, `unverified`, or `recheck_required` statuses, `rg` exit code 1 |

## Final Decision

`COMPLETE`: all in-scope Korean semantic units are covered by the English monitoring FAQ targets or intentionally excluded as export metadata. No `missing`, `unverified`, or `recheck_required` rows remain in the S026 matrix.
