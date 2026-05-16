# S029 FAQ Error Messages 09-21 to 09-29 Semantic Coverage Audit

## Requirement And Boundary

- Job: `S029`
- Scope: audit only Korean FAQ error-message documents whose filenames begin with `09-21.` through `09-29.`, including nested Korean export paths such as `faq/Home/09. 에러메시지/Home/09. 에러메시지/**`, against `FAQE/Home/09. Error Messages/**`.
- Required workflow: `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`.
- Final decision: `COMPLETE`.

This job did not run the `llm-reference` consolidation workflow and did not edit Korean source documents. It did not require changes to English FAQ source pages; it added the S029 matrix and this note. Because no English Markdown page changed, `manifest.json` metadata did not need an update.

## Required Reading And Preflight

Read before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- Scoped Korean and English error-message FAQ documents listed in `semantic-coverage/doc-mapping.tsv` rows `F09-21` through `F09-29`.

The required handoff check was run before editing:

```bash
git status --porcelain --untracked-files=all -- . ":(exclude).codex-jobs" ":(exclude).codex-jobs/**"
```

Result: no output.

## Design Note

S029 does not change documentation behavior, architecture, or file organization. The audit keeps the existing English FAQ source pages as-is because direct semantic-unit inspection found that they already represent the Korean source content for this scoped range. The only structural note is evidence-related: `09-21. ERR-21010 Value overflow` is audited from its nested Korean export path, `faq/Home/09. 에러메시지/Home/09. 에러메시지/09-21. ERR-21010 Value overflow__6521028.md`, matching `semantic-coverage/doc-mapping.tsv`.

## Direct Inspection Summary

- Korean source files inspected: 9 Markdown pages under `faq/Home/09. 에러메시지/`, including the nested `09-21` export path.
- English target files inspected: 9 Markdown pages under `FAQE/Home/09. Error Messages/`.
- Matrix rows: 86.
- Status distribution:
  - `covered`: 77
  - `added`: 0
  - `not_applicable`: 9
  - `source_limitation`: 0
  - `missing`: 0
  - `unverified`: 0
  - `recheck_required`: 0

The audit covered headings, overview paragraphs, version conditions, symptoms, causes, SQL and command blocks, pseudo-code, output examples, configuration properties, errno values, reference links, warnings, notes, and generated export metadata. Long command, SQL, and output blocks are summarized in the TSV with exact identifiers and source line ranges.

## Source Coverage Notes

- `09-21 ERR-21010`: English preserves the all-version scope, INSERT/UPDATE symptom, `altierr 0x21010` output, `mtERR_ABORT_VALUE_OVERFLOW`, integer boundary example using `2147483648` and `2147483647`, remediation, and General Reference manual guidance. The Korean source is under a nested export path and was inspected directly.
- `09-22 ERR-21011`: English preserves the conversion-function, comparison-operator, automatic-casting causes, and all three examples: `UNION`, `TO_NUMBER('1-1')`, and `CHAR(1)` comparison cases including `'A'`, quoted comparison, blank string, and `TRIM(NO)`.
- `09-23 ERR-31283`: English preserves the `6.1.1 or earlier` version condition, partition-table PK/UNIQUE INDEX symptom, `altierr 0x31283`, global-index limitation, prefixed/nonprefixed uniqueness rationale, all three remediation options, the `REALSET_CONTENTS` SQL examples, and the partitioned-index support table.
- `09-24 ERR-41059`: English preserves the HDB 5+ scope, `ERR-91015` client symptom, `altibase_boot.log` messages, MAX_CLIENT/task/session relationship, service-thread and `TRANSACTION_TABLE_SIZE` causes, MAX_CLIENT/session/task checking procedures, OS commands (`netstat`, `lsof`, `ipcs`, `pfiles`), and MAX_CLIENT/application remediation guidance.
- `09-25 ERR-71018`: English preserves the TCP session-close overview, version-specific read/write message forms, session manager thread explanation, `ERR-71018` versus `ERR-71019` meanings, errno inference, `ECONNRESET` and `ETIMEDOUT` OS errno values, occurrence cases, no-server-action guidance, and replication `altibase_rp.log` note.
- `09-26 ERR-71019`: English preserves the Korean notice page as a redirect/reference to the corresponding English `ERR-71018` page. The Korean source contains only the notice and a legacy AID short link.
- `09-27 ERR-91015`: English preserves all-version scope, iSQL connection and connected-SQL symptoms, startup symptom, compatibility-policy cause, `altibase -v` and `apre -v` version checks, timeout-property causes, `altibase_boot.log` examples, property reference links, sysdba session-close cause, and startup property inspection targets.
- `09-28 Not found data`: English preserves the cursor FETCH workflow, versions `5.3.3`, `5.5.1`, and `6.1.1`, SESC loop and output examples, fetch-across-commit cause, communication-buffer timing, both application-change remedies, multi-connection code, LIMIT-based cursor reopening code, and version-difference table.
- `09-29 tablespace does not have enough free space`: English preserves the HDB 4+ scope, insufficient tablespace cause, usage-check and `ALTER TABLESPACE ... add datafile` action, monitoring reference, tablespace lock warning, and version-specific SELECT/DML blocking behavior.

## Attachment And Link Evidence

The scoped Korean `09-21` through `09-29` sources contain no URL-backed document-format attachments with extensions `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, or `.zip`.

Reference links inspected in scope include:

- `09-21` Korean support manual link. English uses the English Altibase manuals link plus the ALTIBASE Documents GitHub link.
- `09-24` legacy AID `MAX_CLIENT` considerations link. English uses the corresponding `docs.altibase.com` FAQE page.
- `09-26` legacy AID redirect link. English uses the corresponding `docs.altibase.com` FAQE page for `ERR-71018`.
- `09-27` session-property links for `FETCH_TIMEOUT`, `UTRANS_TIMEOUT`, and `IDLE_TIMEOUT`. English preserves the three reference slots with English FAQE pages.
- `09-28` legacy AID links for `ERR-4103C` and `ERR-410D2`. English uses the corresponding FAQE pages.
- `09-29` legacy AID monitoring category link. English uses the English FAQE monitoring category.

External HTTP availability was not tested; S029 used grep-based source-link and semantic target-preservation checks.

## Self-Review

- Rechecked all scoped Korean and English pages directly after drafting the matrix.
- Rechecked the nested `09-21` Korean path against the mapping row `F09-21`.
- Rechecked scoped English targets for Korean residue, empty Markdown links, macro-rendering artifacts, and legacy hash-anchor link patterns.
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
| S029 matrix TSV shape/status validation | Passed: 86 rows, 15 columns; `covered` 77, `not_applicable` 9 |
| Scoped English bad-link/macro grep | Passed: no matches, `rg` exit code 1 |
| Scoped English Korean-residue grep | Passed: no matches, `rg` exit code 1 |
| Scoped document-format attachment grep | Passed: no matches, `rg` exit code 1 |
| Scoped English code-fence balance check | Passed: 9 files checked, no odd fence counts |
| Full semantic matrix unresolved-status grep | Passed: no `missing`, `unverified`, or `recheck_required` statuses, `rg` exit code 1 |

## Final Decision

`COMPLETE`: all in-scope Korean semantic units are covered by the English error-message FAQ targets or intentionally excluded as export metadata/navigation. No `missing`, `unverified`, or `recheck_required` rows remain in the S029 matrix.
