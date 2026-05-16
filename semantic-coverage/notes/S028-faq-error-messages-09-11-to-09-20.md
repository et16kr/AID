# S028 FAQ Error Messages 09-11 to 09-20 Semantic Coverage Audit

## Requirement And Boundary

- Job: `S028`
- Scope: audit only Korean FAQ error-message documents whose filenames begin with `09-11.` through `09-20.` against `FAQE/Home/09. Error Messages/**`.
- Required workflow: `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`.
- Final decision: `COMPLETE`.

This job did not run the `llm-reference` consolidation workflow and did not edit Korean source documents. It changed one scoped English FAQ page, added the S028 matrix and note, and advanced the S028 workflow status. `manifest.json` metadata was checked for the edited page; the edit did not change its `body_chars` or `word_count`, so no manifest value changed.

## Required Reading And Preflight

Read before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- Scoped Korean and English error-message FAQ documents listed in `semantic-coverage/doc-mapping.tsv` rows `F09-11` through `F09-20`.

The required handoff check was run before editing:

```bash
git status --porcelain --untracked-files=all -- . ":(exclude).codex-jobs" ":(exclude).codex-jobs/**"
```

Result: no output.

## Design Note

S028 does not change documentation architecture or file organization. The documentation behavior change is limited to aligning one subsection label in the English `ERR-11118` FAQ with the Korean source:

- `FAQE/Home/09. Error Messages/ERR-11118 ( 69912) The update log size '_' is bigger than TRX_UPDATE_MAX_LOGSIZE '_'__16876399.md`: changed `How to change property setting value` to `How to check property setting values` before the `V$PROPERTY` and `V$SESSION` verification SQL.

## Direct Inspection Summary

- Korean source files inspected: 10 Markdown pages under `faq/Home/09. 에러메시지/`.
- English target files inspected: 10 Markdown pages under `FAQE/Home/09. Error Messages/`.
- Matrix rows: 105.
- Status distribution:
  - `covered`: 93
  - `added`: 1
  - `not_applicable`: 11
  - `source_limitation`: 0
  - `missing`: 0
  - `unverified`: 0
  - `recheck_required`: 0

The audit covered headings, overview paragraphs, version conditions, symptoms, causes, SQL and command blocks, configuration properties, version-check procedures, screenshots, reference links, warnings, notes, and empty source headings. Long output, SQL, and table blocks are summarized in the TSV with exact identifiers and source line ranges.

## Source Coverage Notes

- `09-11 ERR-4109C`: English preserves client/server major and patch version mismatch cases, APRE/Altibase/isql examples, 5.5.1 and 6.1.1 JDBC/CLI thresholds, unknown server-property cause, remediation, server/client version commands, and the Korean-source ODBC screenshot URL.
- `09-12 ERR-5102E`: English preserves the HDB 4+ scope, HDB 4.3.9 documentation caveat, APRE/SESC and SQLCLI/ODBC symptoms, three cursor-reuse causes, code examples, and required CLOSE/exception-handling actions.
- `09-13 ERR-7101D`: English preserves all-version scope, `altibase_boot.log` symptom, `altierr 0x7101D`, incompatible-client cause, no-server-impact note, compatibility rules around `5.3.3` and `cm protocol version`, connection example table, and version-check commands.
- `09-14 ERR-11030`: English preserves the HDB 4 scope, AUTOEXTEND OFF/maxsize cause, `V$DATAFILES` query, AUTOEXTEND ON remediation, AUTOEXTEND OFF restrictions, HDB 4.3.9 versus HDB 5 behavior, and `ulimit -a` check.
- `09-15 ERR-11036`: English preserves all-version scope, `DROP DATAFILE` symptom, `altierr` cause, used-datafile deletion restriction, tablespace recreation steps, and intentionally omits the empty `참고 사항` heading.
- `09-16 ERR-11049`: English preserves `MEM_MAX_DB_SIZE` cause and definition, memory usage SQL with `V$DATABASE` and `V$MEMTBL_INFO`, restart requirement, stop/edit/start procedure, disk-space warning, Linux/Unix and AIX/HP-UX resource settings, and the local English reference link.
- `09-17 ERR-11075`: English preserves version-specific messages, DDL/memory-table/`SELECT FOR UPDATE`/replication symptoms, `altierr 0x11075`, `DDL_LOCK_TIMEOUT`, `LOCK_ESCALATION_MEMORY_SIZE`, `REPLICATION_LOCK_TIMEOUT`, and all remediation bullets.
- `09-18 ERR-11118`: English preserves the memory-table update-log symptom, version-specific `ERR-11118` and `ERR-110C3`, MVCC explanation, record-reduction examples, transaction-log estimation SQL, `LOCK_ESCALATION_MEMORY_SIZE` caution, session/system/property-file change methods, and related bug table. This job corrected the property-check subsection label.
- `09-19 ERR-11183`: English preserves the 6.3.1 through 7.1.0.5.0 scope and BUG-48369 note, SORT/HASH disk-table symptom, `TEMP_MAX_PAGE_COUNT` cause, diagnostic SQL, `TEMP_MAX_PAGE_COUNT` formula and examples, online/persistent property changes, related Work Area property calculations, memory-impact checks, and OS-specific `ps` commands.
- `09-20 ERR-11184`: English preserves the 6.3.1+ scope, Work Area cause, `TOTAL_WA_SIZE` solution, `V$PROPERTY` check, `ALTER SYSTEM` and `altibase.properties` update, version-specific `V$MEMSTAT` areas, and concurrency wait precautions.

## Attachment And Link Evidence

The scoped Korean `09-11` through `09-20` sources contain no URL-backed document-format attachments with extensions `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, or `.zip`.

Image/reference links inspected in scope include:

- `09-11` cause diagrams and ODBC screenshot. The English page has localized cause diagrams and preserves the Korean-source ODBC screenshot URL.
- `09-13` ODBC screenshot. The English page has the corresponding FAQE screenshot URL.
- Local English FAQ links for `MEM_MAX_DB_SIZE` and `ERR-11118` are preserved where Korean source used legacy AID links.

## Self-Review

- Rechecked the `added` row against Korean source lines 144-168 and the edited English target lines 139-160.
- Rechecked scoped English targets for Korean residue, empty Markdown links, macro-rendering artifacts, and legacy hash-anchor link patterns.
- Rechecked the matrix for invalid row widths and forbidden successful-job statuses.
- Rechecked edited-page `manifest.json` metadata against `wc -w -m`; it still matches `word_count: 1309` and `body_chars: 9938`.
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
| S028 matrix TSV shape/status validation | Passed: 105 rows, 15 columns; `not_applicable` 11, `covered` 93, `added` 1 |
| Scoped English bad-link/macro grep | Passed: no matches, `rg` exit code 1 |
| Scoped English Korean-residue grep | Passed: no matches, `rg` exit code 1 |
| Scoped document-format attachment grep | Passed: no matches, `rg` exit code 1 |
| Scoped English code-fence balance check | Passed: 10 files checked, no odd fence counts |
| Edited-page manifest metadata comparison | Passed: `word_count` 1309 and `body_chars` 9938 match manifest |
| Full semantic matrix unresolved-status grep | Passed: no `missing`, `unverified`, or `recheck_required` statuses, `rg` exit code 1 |

## Final Decision

`COMPLETE`: all in-scope Korean semantic units are covered by the English error-message FAQ targets, added in this job, or intentionally excluded as export metadata/empty headings. No `missing`, `unverified`, or `recheck_required` rows remain in the S028 matrix.
