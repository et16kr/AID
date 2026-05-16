# S027 FAQ Error Messages 09-01 to 09-10 Semantic Coverage Audit

## Requirement And Boundary

- Job: `S027`
- Scope: audit only Korean FAQ error-message documents whose filenames begin with `09-01.` through `09-10.` against `FAQE/Home/09. Error Messages/**`.
- Required workflow: `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`.
- Final decision: `COMPLETE`.

This job did not run the `llm-reference` consolidation workflow and did not edit Korean source documents. It changed only two scoped English FAQ pages, `manifest.json`, this note, the S027 matrix, and the S027 workflow status.

## Required Reading And Preflight

Read before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- Scoped Korean and English error-message FAQ documents listed in `semantic-coverage/doc-mapping.tsv` rows `F09-01` through `F09-10`.

The required handoff check was run before editing:

```bash
git status --porcelain --untracked-files=all -- . ":(exclude).codex-jobs" ":(exclude).codex-jobs/**"
```

Result: no output. The only pre-existing status change was the orchestrator's `.codex-jobs/ko-en-semantic-coverage-audit/jobs.tsv` runtime/status update.

## Design Note

S027 does not change documentation architecture or file organization. The documentation behavior change is limited to aligning two scoped English cursor-error pages with Korean-source wording:

- `ERR-410D2 (266450) Fetch out of sequence__16876332.md`: changed the communication-buffer cause from "the first large amount of records" to "a certain amount of records ... during the first FETCH" and added the missing note that all three remedies require application changes.
- `ERR-4103C (266300) Request of fetching data to an unprepared SQL statement__16876347.md`: changed the same communication-buffer wording to match the Korean source.

`manifest.json` metadata was updated for both changed English Markdown pages.

## Direct Inspection Summary

- Korean source files inspected: 10 Markdown pages under `faq/Home/09. 에러메시지/`.
- English target files inspected: 10 Markdown pages under `FAQE/Home/09. Error Messages/`.
- Matrix rows: 78.
- Status distribution:
  - `covered`: 63
  - `added`: 3
  - `not_applicable`: 12
  - `source_limitation`: 0
  - `missing`: 0
  - `unverified`: 0
  - `recheck_required`: 0

The audit covered headings, overview paragraphs, version conditions, symptoms, causes, SQL and command blocks, stack-trace examples, cursor examples, error-code lookups, configuration properties, warnings, notes, reference links, and URL-backed attachments. Long collapsed output and code blocks are summarized in the TSV with exact identifiers and line ranges; each corresponding Korean and English block was inspected directly.

## Source Coverage Notes

- `09-01 [Notify : Fetch Timeout]`: English preserves server-side and client-side symptoms, version-specific log formats, Orange/iSQL/APRE/SQLCLI/ODBC/CAPI/SESC/JDBC examples, `FETCH_TIMEOUT` cause semantics, old-image resource-growth risk, application-logic examples, property-change procedures, and `V$SESSION`/`V$PROPERTY` verification SQL.
- `09-02 [Warning] Memory allocation failed`: English preserves OS memory-allocation scope, `altibase_boot.log`, `ERR-01051`, HP-UX `maxdsiz`/`maxdsiz_64bit`, `/usr/sbin/kctune`, 32-bit OS 2G limit, physical-memory checks, `SYS_TBS_MEM_DATA`, and the HP-UX setup guide PDF attachment.
- `09-03 TRY_COUNT, LOCK_COUNT, MISS_COUNT`: English preserves the reset mutex statistics message, `v$mutex` counter overflow explanation, version-specific `desc v$mutex` structures for `6.3.1 or earlier`, `6.5.1`, and `7.1.0 or later`, and the no-action-needed conclusion.
- `09-04 altibase_qp.log 8-digit errorcode`: English preserves the `6.1.1 or earlier` and `6.3.1 or later` version split, the decimal-to-hex conversion from `822329545` to `3103C0C9`, the `3103C` error code, and the `altierr 0x3103C` lookup.
- `09-05 Closed Socket by client is Detected`: English preserves the all-version scope, exact `altibase_boot.log` message, disconnect/network causes, no-server-action guidance, and ignore-if-no-service-problem note.
- `09-06 ERR-0109D Insufficient memory`: English preserves version caveats, setup SQL, `ERR-0109D`/`ERR-01067` version examples, `altierr 0x0109D`, memory-table temporary area behavior, `EXECUTE_STMT_MEMORY_MAXIMUM`, `V$PROPERTY`, `ALTER SYSTEM`, `altibase.properties`, and cautious sizing guidance.
- `09-07 ERR-311E0`: English preserves `6.1.1 or earlier` applicability, no error in `6.3.1 or later`, disk temp tablespace 8K page-size cause, approximate 3000-byte note, failing and succeeding examples, `TEMP_TBS_MEMORY`, and upgrade guidance.
- `09-08 ERR-410D2`: English preserves cursor workflow, `-266450 HY000` output, commit/rollback-after-open cause, communication-buffer behavior, three remedies, CONN1/CONN2 example, Altibase 5+ 32K buffer/LIMIT example, `CURSOR WITH HOLD`, version-difference table, and manual references. This job added the missing application-change note and corrected one cause sentence.
- `09-09 ERR-1105D`: English preserves `ERR-1105D` and `ERR-31386`, version-specific message formats, `altierr 0x1105D`, `altierr 0x31386`, SELECT-only function restrictions, and the failing/succeeding function examples.
- `09-10 ERR-4103C`: English preserves Altibase 4.3.9 scope, cursor workflow, `-266300` output, commit/rollback-after-open cause, two remedies, CONN1/CONN2 example, Altibase 4.3.9 64K buffer/LIMIT example, and version-difference table. This job corrected one cause sentence.

## Attachment And Link Evidence

URL-backed document-format attachments in scope:

- `ALTIBASE_운영을_위한_HPUX_설정_가이드.pdf`
  - Korean: `faq/Home/09. 에러메시지/09-02. [Warning] Memory allocation failed__9109748.md`
  - English: `FAQE/Home/09. Error Messages/[Warning] Memory allocation failed__16876308.md`

No URL-backed document-format attachment gap remains in this scoped range.

## Self-Review

- Rechecked all `added` rows against the Korean source lines and the edited English target lines.
- Rechecked scoped English for Korean residue, empty links, macro-rendering artifacts, and legacy hash-anchor link patterns.
- Rechecked the matrix for invalid row widths and forbidden successful-job statuses.
- Rechecked edited-page `manifest.json` metadata against `wc -m -w` for both edited English files.
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
| S027 matrix TSV shape/status validation | Passed: 78 rows, 15 columns; `not_applicable` 12, `covered` 63, `added` 3 |
| Scoped English bad-link/macro/Korean-residue grep | Passed: no matches, `rg` exit code 1 |
| Scoped evidence bad-link/macro grep | Passed: no matches, `rg` exit code 1 |
| Scoped stale wording grep | Passed: no matches for corrected stale strings, `rg` exit code 1 |
| Scoped attachment preservation grep | Passed: two matches; the URL-backed HP-UX PDF is present in Korean and English |
| Scoped English code-fence balance check | Passed: 10 files checked, no odd fence counts |
| Edited-page manifest metadata comparison | Passed for both edited English pages |
| Full semantic matrix unresolved-status grep | Passed: no `missing`, `unverified`, or `recheck_required` statuses, `rg` exit code 1 |

## Final Decision

`COMPLETE`: all in-scope Korean semantic units are covered by the English error-message FAQ targets, added in this job, or intentionally excluded as export metadata/empty headings. No `missing`, `unverified`, or `recheck_required` rows remain in the S027 matrix.
