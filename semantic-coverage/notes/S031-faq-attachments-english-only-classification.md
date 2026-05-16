# S031 FAQ Attachments and English-Only Classification

## Requirement And Boundary

- Job: `S031`
- Scope: revalidate FAQ attachments, legacy labels, source links, export artifacts, and English-only `FAQE` classification boundaries.
- Required workflow: `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`.
- Final decision: `COMPLETE`.

This job works only on FAQ link and classification evidence. It does not rerun body-level semantic audits already owned by S020-S030, does not run `llm-reference` consolidation, and does not edit Korean source documents.

## Required Reading And Preflight

Read before editing:

- `AGENTS.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `semantic-coverage/doc-mapping.tsv`
- FAQ source and target files reached by the S031 link/classification scan.

The required handoff check was run before editing:

```bash
git status --porcelain --untracked-files=all -- . ":(exclude).codex-jobs" ":(exclude).codex-jobs/**"
```

Result: no output.

## Design Note

S031 does not change documentation architecture or file organization. It adds the S031 matrix and this note, and it makes one scoped source-link correction in an English FAQ page: the `REPLICATION_GAP_UNIT` reference in `FAQE/Home/03. Replication/Replication monitoring query__22642947.md` now preserves the Korean-source GitHub manual URL. `manifest.json` metadata was updated for that edited page.

English-only `FAQE` pages remain auxiliary source candidates. They must not be used as Korean-source coverage proof unless a later job explicitly maps and audits them.

## Direct Inspection Summary

The S031 scan directly inspected the Korean FAQ tree, the mapped Korean-core English FAQ target set from `semantic-coverage/doc-mapping.tsv`, and the full `FAQE/Home` tree for English-only classification.

Matrix file: `semantic-coverage/matrices/S031-faq-attachments-english-only-classification.tsv`

Rows by unit type:

- `support_reference`: 32
- `external_reference`: 8
- `internal_cross_reference`: 31
- `export_artifact_link`: 34
- `legacy_hash_label`: 2
- `document_attachment`: 7
- `downloadable_support_artifact`: 12
- `english_only_classification`: 7

Rows by coverage status:

- `covered`: 86
- `added`: 1
- `not_applicable`: 11
- `source_limitation`: 35
- `missing`: 0
- `unverified`: 0
- `recheck_required`: 0

## Attachment Evidence

Seven Korean FAQ URL-backed document-format attachments were found and all exact URLs are preserved in the mapped English FAQ targets:

- `D24_ALTIBASE_효율적인_이중화_가이드.pdf`
- `D67_ALTIBASE_이중화_제약사항_가이드.pdf`
- `LobSpringIbatisSample.zip`
- `altimon_for_windows.zip`
- `ALTIMON_USER_GUIDE.pdf`
- `ALTIBASE_운영을_위한_HPUX_설정_가이드.pdf`
- `AdminCenter2.zip`

Twelve additional downloadable FAQ support artifacts were also checked and exactly preserved: `altimon.bat`, `altimon.vbs`, seven ALTIMON `.tar` files, two `altimon.conf` files, and `SP_DML_RECORD_COUNT.txt`.

## Legacy Labels And Export Artifacts

Two Korean FAQ `(#)` labels were classified:

- `ALTIMON USER GUIDE`: covered by the same-page English guide section and the preserved `ALTIMON_USER_GUIDE.pdf` link.
- `total_memory_tablespaces_usage.txt`: `source_limitation`; the Korean source has no downloadable URL, and the English target keeps the filename as plain text without inventing a link.

Export-generated fake HTTP links in Korean source examples were not propagated into `FAQE/Home`. These include Java package names (`java.io`, `java.net`, `sun.nio.ch`, `Altibase.jdbc.driver.cm`), ODBC library/path strings (`libaltibase_odbc-64bit-ul64.so`, `modules:...`), and the HP-UX `PATH` value. The English targets preserve these identifiers as text or code.

## Source Link Evidence

The scan checked support portal links, internal Confluence shortlinks, external references, and official source/manual links in Korean FAQ pages.

One English target was updated in this job:

- `faq/Home/03. 이중화/03-08. 이중화 모니터링 쿼리__9110681.md` line 176 links `REPLICATION_GAP_UNIT` to a GitHub manual anchor.
- `FAQE/Home/03. Replication/Replication monitoring query__22642947.md` line 175 now preserves that link.

Other localized or context-only source links were classified in the matrix as covered or not applicable according to whether the English target preserves the exact URL, an English equivalent, or only the technical reference context. Generic Korean support portal links were not treated as required downloadable source attachments.

## English-Only Classification

`semantic-coverage/doc-mapping.tsv` maps 115 Korean FAQ files to 115 Korean-core English FAQ targets. `FAQE/Home` contains 241 Markdown files, leaving 126 English-only candidate files.

English-only candidate areas:

- `ALTIBASE HDB Administration`: 7 files
- `ALTIBASE HDB Architecture`: 3 files
- `ALTIBASE HDB Performance Tuning`: 4 files
- `ALTIBASE HDB Replication`: 4 files
- `ALTIBASE HDB Troubleshooting`: 9 files
- `Altibase Error Messages`: 98 files
- `Altibase Error Messages__6979655.md`: 1 file

These pages can be used later only as labeled `English-only source` auxiliary material. They do not prove Korean-source semantic coverage.

## Self-Review

Self-review checked that:

- The matrix header matches the required TSV schema.
- Every matrix row has exactly 15 TSV fields.
- Status values are workflow-approved.
- The S031 matrix has no `missing`, `unverified`, or `recheck_required` rows.
- All 7 URL-backed FAQ document-format attachments are exact-preserved in mapped English targets.
- The one edited English FAQ page preserves the restored `REPLICATION_GAP_UNIT` source link and has updated `manifest.json` metadata.
- `FAQE/Home` has no empty Markdown links, macro rendering artifacts, lowercase macro placeholder URLs, or legacy hash-only links.
- English-only `FAQE` files are classified separately from Korean-core FAQ targets.

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
| S031 matrix TSV shape/status validation | Passed: 133 rows, 15 fields per row; `covered` 86, `added` 1, `not_applicable` 11, `source_limitation` 35 |
| FAQ document-format attachment preservation check | Passed: 7 document-format links preserved; 19 total `download/attachments` links preserved |
| English-only `FAQE` classification count | Passed: 115 mapped Korean-core FAQE targets, 241 total FAQE Markdown files, 126 English-only candidates |
| Source-tree empty-link/export-artifact grep on `arch/Home FAQE/Home` | Passed: expected-no-match grep exited 1 |
| `FAQE/Home` fake HTTP export-artifact grep | Passed: expected-no-match grep exited 1 |
| Full semantic matrix unresolved-status grep | Passed: expected-no-match grep exited 1 |
| Edited-page manifest metadata comparison | Passed: `FAQE/Home/03. Replication/Replication monitoring query__22642947.md` has `body_chars` 7422 and `word_count` 902 |

External HTTP availability was not tested; S031 used source-link preservation and grep-based validation.

The broader artifact grep including `semantic-coverage/` was not used as a pass/fail source-stability check for S031 because earlier matrices and notes intentionally quote Korean-source macro placeholder labels as evidence. The live source trees `arch/Home` and `FAQE/Home` passed the no-match artifact grep.

## Final Decision

`COMPLETE`: S031 found no unresolved FAQ attachment, legacy-label, export-artifact, or English-only classification blocker. The one missing source link found during direct inspection was restored in the mapped English FAQ target.
