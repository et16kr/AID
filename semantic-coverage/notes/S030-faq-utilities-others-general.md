# S030 FAQ Utilities, Others, and General Semantic Coverage Audit

## Requirement And Boundary

- Job: `S030`
- Scope: audit only Korean FAQ categories `11. 유틸리티`, `12. 기타`, and `13. 일반` against the corresponding English FAQ targets under `FAQE/Home/11. Utilities`, `FAQE/Home/12. Others`, and `FAQE/Home/13. General`.
- Required workflow: `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`.
- Final decision: `COMPLETE`.

This job did not run the `llm-reference` consolidation workflow and did not edit Korean source documents. Direct semantic-unit inspection found that the scoped English FAQ pages already represent the Korean source content, so this job did not change English source pages or `manifest.json`.

## Required Reading And Preflight

Read before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- Scoped Korean and English FAQ documents listed in `semantic-coverage/doc-mapping.tsv` rows `F11-01` through `F13-03`.

The required handoff check was run before editing:

```bash
git status --porcelain --untracked-files=all -- . ":(exclude).codex-jobs" ":(exclude).codex-jobs/**"
```

Result: no output.

## Design Note

S030 does not change documentation behavior, architecture, or file organization. The audit keeps the existing English FAQ source pages as-is because direct semantic-unit inspection found that they already represent the Korean source content for utilities, miscellaneous operational/debugging topics, and general product concepts. The only new structure is evidence: the S030 matrix and this note.

## Direct Inspection Summary

- Korean source files inspected: 7 Markdown pages under `faq/Home/11. 유틸리티`, `faq/Home/12. 기타`, and `faq/Home/13. 일반`.
- English target files inspected: 7 Markdown pages under `FAQE/Home/11. Utilities`, `FAQE/Home/12. Others`, and `FAQE/Home/13. General`.
- Matrix rows: 68.
- Status distribution:
  - `covered`: 61
  - `added`: 0
  - `not_applicable`: 7
  - `source_limitation`: 0
  - `missing`: 0
  - `unverified`: 0
  - `recheck_required`: 0

The audit covered headings and sections, overview paragraphs, version conditions, commands, command output, utility names, property names, warnings, attachment links, image references, table rows, and failure-management rows. Long command/output blocks are summarized in the TSV with exact identifiers and source line ranges.

## Source Coverage Notes

- `11-01 AdminCenter2 execution file`: English preserves the last-version notice, ALTIBASE HDB 4 upper limit, ALTIBASE HDB 5 Ware Valley `Orange for Altibase` note, maintenance-ended support warning, exact `AdminCenter2.zip` URL, `AdminCenter.exe` launch procedure, `$ALTIBASE_HOME/lib/Altibase.jar`, and Help Contents manual note.
- `11-02-01 DOS-format iloader upload error`: English preserves the conversion requirement, `ERR-9102B`, CR+LF versus `%n`, `^M`, Windows UltraEdit conversion, `dos2unix`, `sed`, Ctrl+v+m input note, and the ALTIBASE HDB 5.5.1+ `%r%n` upload example.
- `12-01 Thread process debugging method`: English preserves the Unix CPU/hang diagnostic purpose, `pstack`, `dbx`, and `gdb` command procedures, detach warning, and command/output identifiers. The Korean source exports for `dbx` and `gdb` examples are collapsed single-line blocks; English preserves the identifiers in fenced blocks without inferring additional line breaks.
- `12-02 Building a Large-Scale DRDB Index`: English preserves the index read/sort/store description, parallel I/O and buffer-miss performance warning, version ranges `6.5.1~7.1.0` and `7.3.0 or later`, `BUFFER_AREA_SIZE`, `SORT_AREA_SIZE`, `DISK_INDEX_BUILD_SORT_AREA_SIZE`, `DISK_INDEX_BUILD_MERGE_PAGE_COUNT`, `INDEX_BUILD_THREAD_COUNT`, memory sizing, STARTUP-time tradeoffs, and the merge-page formula.
- `13-01 What interface does Altibase provide`: English preserves the Altibase HDB 6.1.1+ scope, ANSI SQL-1999 statement, client interface rows for ODBC, JDBC, SQLCLI, Embedded SQL, ADO.NET, Unix ODBC, PDO, Hibernate Support, and server interface rows for SQL, Built-in Function, Stored Procedure & Function, View, and Trigger.
- `13-02 In-memory versus disk-based DBMS`: English preserves the all-version scope, hybrid DBMS explanation, data-residency distinction, architecture image reference, 4-10x performance note, TPC-C transaction mix, performance graph reference, and TPC-C definition. The English page uses localized FAQE image paths and `.jpeg` filenames for the corresponding embedded images.
- `13-03 Memory data safety`: English preserves main-memory durability scope, all-version applicability, support-request link mapped to the English support portal, WAL/checkpoint recovery semantics, backup and complete/incomplete recovery support, and failure-management rows for Transaction Failure, System Failure, and Disk Failure.

## Attachment And Link Evidence

The scoped Korean source set contains one URL-backed document-format attachment:

- `AdminCenter2.zip`

The exact URL is preserved in `FAQE/Home/11. Utilities/AdminCenter2 execution file__16876465.md`.

Other scoped source links inspected include:

- Ware Valley download site: `http://www.warevalley.com`
- Korean support portal link in `13-03`, mapped to the English support portal in the English target.
- Embedded image links in `13-02`, represented by corresponding localized FAQE image embeds in the English target.

External HTTP availability was not tested; S030 used source-link preservation and grep-based checks.

## Self-Review

- Rechecked all scoped Korean and English pages directly after drafting the matrix.
- Rechecked `semantic-coverage/doc-mapping.tsv` rows `F11-01` through `F13-03` for path ownership and target paths.
- Rechecked scoped English targets for empty Markdown links, macro-rendering artifacts, legacy hash-anchor link patterns, and Korean residue.
- Rechecked the matrix for invalid row widths and forbidden successful-job statuses.
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
| S030 matrix TSV shape/status validation | Passed: 68 rows, 15 columns; `covered` 61, `not_applicable` 7 |
| Full semantic matrix unresolved-status grep | Passed: no `missing`, `unverified`, or `recheck_required` statuses, `rg` exit code 1 |
| Scoped English bad-link/macro grep | Passed: no matches, `rg` exit code 1 |
| Scoped English Korean-residue grep | Passed: no matches, `rg` exit code 1 |
| Scoped document-format attachment grep | Passed: exact `AdminCenter2.zip` URL appears in both Korean source and English target |
| Scoped English code-fence balance check | Passed: 7 files checked, no odd fence counts |

External HTTP availability was not tested.

## Final Decision

`COMPLETE`: all in-scope Korean semantic units are covered by the English FAQ targets or intentionally excluded as export metadata/navigation. No `missing`, `unverified`, or `recheck_required` rows remain in the S030 matrix.
