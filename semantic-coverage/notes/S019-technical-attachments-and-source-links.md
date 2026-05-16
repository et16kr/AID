# S019 - Technical attachments and source links

## Scope and boundary

S019 revalidated technical-document attachments, legacy labels, source links, and external references across the technical mappings `D020` through `D070` in `semantic-coverage/doc-mapping.tsv`.

This job did not audit FAQ files; FAQ attachments and English-only FAQE classification are assigned to S031. This job also did not run the LLM reference consolidation workflow.

## Required reading and direct inspection

Required project instructions and orientation files were read before editing:

- `AGENTS.md`
- `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `semantic-coverage/doc-mapping.tsv`

The S019 evidence was not copied from prior J/P reports. The job directly scanned the Korean technical source files under `DOCK/Home` and the mapped English technical targets under `arch/Home`.

## Design note

No product-document behavior, architecture, or documentation structure changed in this job. S019 only adds a semantic evidence matrix and this note. No `DOCK/`, `arch/`, `FAQE/`, `faq/`, or `manifest.json` product metadata edits were required.

## Audit method

The scan included:

- URL-backed document-format links using `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, and `.zip`.
- The GeoServer importer plug-in ZIP download link, because the URL path includes a downloadable ZIP.
- Legacy `#` link labels, including both document attachment placeholders and non-document UI/error-code placeholders.
- Non-image HTTP/HTTPS source links and external references from Korean technical sources.

The scan excluded embedded screenshots/images and false URL artifacts that are code or library filenames rather than external references, such as `connect1.sc`, `altibase_env.mk`, `lib*.so`, local host/server examples, and Confluence `createpage.action` placeholders.

## Matrix summary

Matrix file: `semantic-coverage/matrices/S019-technical-attachments-and-source-links.tsv`

Rows by unit type:

- `external_reference`: 234
- `document_attachment`: 42
- `legacy_attachment_label`: 6
- `legacy_hash_label`: 13

Rows by coverage status:

- `covered`: 267
- `source_limitation`: 21
- `not_applicable`: 7

The 42 URL-backed technical document/ZIP links were found in the mapped English target set. No English source document change was needed.

## Source limitations and non-applicable rows

The six legacy document attachment labels remain source limitations because the Korean source uses `#` and provides no downloadable URL:

- `ALTIBASE_개발가이드.pdf`
- `ALTIBASE_개발가이드_5.3.pdf`
- `ALTIBASE_Oracle_변환_가이드.pdf`
- `ORACLE_to_ALTIBASE_변환_가이드_5.5.pdf`
- `APRE_New_Features_업그레이드_가이드.pdf`
- `ALTIBASE_MSSQL_변환가이드.pdf`

Thirteen additional non-document `#` labels were recorded as `source_limitation` because they are legacy UI/error-code placeholders and no real URL can be inferred safely.

Two external reference rows were recorded as `source_limitation`:

- `DOCK/Home/53. Windows 환경의 Altibase ODBC 개발 가이드__13436856.md` line 44 has a malformed export link `http://atc.altibase.com에서`; English preserves the usable support portal reference instead.
- `DOCK/Home/68. Altibase GeoServer 연동가이드__14058194.md` line 214 labels a link as `GeoServer Documentation` but points to a Red Hat CPU governor page; English does not propagate that mismatched URL.

Seven generic top-of-document Korean support-portal boilerplate rows were marked `not_applicable` where the English target omits the nontechnical boilerplate and no technical procedure, attachment, or source reference depends on that link.

## Self-review

Self-review checked that:

- The matrix header matches the required TSV schema.
- Every row has exactly 15 TSV fields.
- Status values are limited to the workflow-approved values.
- No S019 row uses `missing`, `unverified`, or `recheck_required`.
- URL-backed document-format links are represented as `covered`, not as legacy labels.
- Legacy `#` labels are not converted into invented URLs.
- Known fake source-export links are recorded as limitations or excluded when they are code/library filenames rather than external references.
- `manifest.json` was not updated because no English product Markdown file changed.

## Verification

Verification commands were run after creating the S019 matrix and note.

| Check | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK/Home -type f -name '*.md' \| wc -l` | 51 |
| `find faq/Home -type f -name '*.md' \| wc -l` | 115 |
| `find arch/Home -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE/Home -type f -name '*.md' \| wc -l` | 241 |
| Technical document-format attachment preservation check | Passed: 42 URL-backed technical document/ZIP links covered, 0 missing; 6 legacy document `#` labels and 13 non-document `#` labels recorded separately |
| S019 matrix field-count/status check | Passed: 295 rows, 15 fields per row, no `missing`, `unverified`, or `recheck_required` rows |
| Scoped empty-link/export-artifact grep | Passed: expected-no-match grep exited 1, meaning no matches |
| Coverage unresolved-status grep | Passed: expected-no-match grep exited 1, meaning no matches |

## Final decision

COMPLETE
