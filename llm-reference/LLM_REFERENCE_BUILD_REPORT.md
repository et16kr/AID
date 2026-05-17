# LLM Reference Build Report

Report date: 2026-05-17

## Source paths

- `AGENTS.md`
- `.codex-jobs/llm-reference-consolidation/jobs.tsv`
- `.codex-jobs/llm-reference-consolidation/workflow-requirements.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `source-stabilization/validation-report.md`
- `source-stabilization/source-classification.tsv`
- `source-stabilization/legacy-attachments.tsv`
- `source-stabilization/url-backed-attachments.tsv`
- `llm-reference/README.md`
- `llm-reference/source-index.md`
- `llm-reference/coverage/README.md`
- `llm-reference/coverage/source-inventory.tsv`
- `llm-reference/coverage/source-to-topic-map.tsv`
- `llm-reference/coverage/semantic-unit-coverage.tsv`
- `llm-reference/coverage/attachment-diagram-register.tsv`
- `llm-reference/coverage/answerability-backtest.tsv`
- `llm-reference/coverage/omissions-and-risks.tsv`

## Source coverage notes

This report is the R028 final validation output for the exhaustive LLM reference consolidation workflow. R028 owns final validation, build-report generation, and handoff generation; it does not own any new `arch/Home` or `FAQE/Home` source-document extraction.

The active workflow row at validation time is `R028	Progress	docs	Final validation build report handoff`. Jobs R001 through R027 are `Done`; the orchestrator owns the final transition of R028 from `Progress` to `Done` after this committed result.

## Final decision

`COMPLETE_REFERENCE_PACKAGE`

The consolidated package is complete for the current workflow boundary. No coverage status field contains `recheck_required`, every inventoried source file is mapped, every coverage source path exists or is an accepted source limitation, and the remaining risk labels are documented rather than unresolved.

## Validation summary

| Check | Result |
| --- | --- |
| Expected top-level `llm-reference/` Markdown outputs | 17 of 17 present after R028 outputs |
| Expected coverage outputs | 8 of 8 present |
| `arch/Home` plus `FAQE/Home` source files | 422 |
| `source-inventory.tsv` rows | 422 rows, 422 unique paths, 0 missing, 0 extra |
| `source-to-topic-map.tsv` rows | 422 rows, 422 unique paths, 0 missing, 0 extra |
| Missing source paths in coverage ledgers | 0 |
| Missing target documents in coverage ledgers | 0 |
| TSV column-width consistency | Passed for all six TSV ledgers |
| Topic documents with `Source paths` and `Terminology` sections | Passed |
| Standard artifact scan | Passed; `rg` returned exit code 1 for no matches |
| Status-field `recheck_required` rows | 0 |

## Coverage ledger results

| Ledger | Rows | Status distribution |
| --- | ---: | --- |
| `source-inventory.tsv` | 422 | `covered=296`, `covered_with_risk=126` |
| `source-to-topic-map.tsv` | 422 | `mapped=296`, `mapped_with_risk=126` |
| `semantic-unit-coverage.tsv` | 2729 | `covered=1698`, `covered_by_canonical_duplicate=43`, `not_document_format=771`, `legacy_attachment_label_only=25`, `source_index_only=1`, `english_only_auxiliary=166`, `diagram_unavailable=25` |
| `attachment-diagram-register.tsv` | 825 | `not_document_format=732`, `preserved_url=58`, `diagram_unavailable=14`, `legacy_no_downloadable_url=21` |
| `answerability-backtest.tsv` | 622 | `answerable=485`, `answerable_with_source_label=137` |
| `omissions-and-risks.tsv` | 31 | `accepted_source_limitation=25`, `accepted_english_only_auxiliary=5`, `resolved=1` |

## Attachment and diagram preservation

`source-stabilization/url-backed-attachments.tsv` records 49 preserved URL-backed document-format attachments from the Korean-source validation gate: 42 technical rows and 7 FAQ rows. Final validation found 0 of those preserved URLs missing from `llm-reference/coverage/attachment-diagram-register.tsv`.

The attachment and diagram register contains 58 `preserved_url` rows because it also records source-corpus attachment coverage beyond the Phase 2 Korean-source URL-backed document-format subset. Remaining attachment and diagram limitations are explicit:

- `legacy_no_downloadable_url`: 21 register rows where the source has no downloadable URL.
- `diagram_unavailable`: 14 register rows where exported diagram content is unavailable and must not be reconstructed.
- `not_document_format`: 732 register rows for images, icons, web/manual references, or support artifacts outside the document-format preservation gate.

## Answerability and risk results

`answerability-backtest.tsv` has 622 answerability rows. All are `answerable` or `answerable_with_source_label`; there are no `not_answerable` or `recheck_required` rows.

Remaining risks are accepted and labeled, not unresolved:

- English-only auxiliary material remains labeled as `English-only source` or `english_only_auxiliary`.
- Legacy attachment labels remain labeled as `legacy_no_downloadable_url` or `legacy_attachment_label_only`; no synthetic URLs were introduced.
- Unavailable diagrams remain labeled as `diagram_unavailable`; no diagram content was reconstructed.
- Source limitations in `omissions-and-risks.tsv` remain accepted source limitations or accepted English-only auxiliary limitations.

## Verification commands

The following standard checks are required for this workflow and were run after R028 edits:

```bash
python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json
git diff --check
find DOCK/Home -type f -name '*.md' | wc -l
find faq/Home -type f -name '*.md' | wc -l
find arch/Home -type f -name '*.md' | wc -l
find FAQE/Home -type f -name '*.md' | wc -l
```

The workflow's standard artifact scan was also run against `llm-reference arch/Home FAQE/Home`.

Expected final results:

| Command | Result |
| --- | --- |
| `python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json` | Passed |
| `git diff --check` | Passed |
| `find DOCK/Home -type f -name '*.md' \| wc -l` | 51 |
| `find faq/Home -type f -name '*.md' \| wc -l` | 115 |
| `find arch/Home -type f -name '*.md' \| wc -l` | 181 |
| `find FAQE/Home -type f -name '*.md' \| wc -l` | 241 |
| Standard artifact scan over `llm-reference arch/Home FAQE/Home` | Passed with no matches; `rg` exit code 1 is expected for no-match scans |

Additional targeted validation was also run:

- Expected output presence check.
- Source inventory and source-to-topic map reconciliation against `find arch/Home FAQE/Home -type f -name '*.md'`.
- Coverage source-path existence check.
- Coverage target-document existence check.
- TSV column-width consistency check.
- Topic `Source paths` and `Terminology` heading check.
- Phase 2 preserved-URL attachment comparison against the final attachment register.

## Remaining risk labels

The package intentionally retains these labels for answer safety:

- `English-only source`: auxiliary English material that was not Korean-source verified.
- `english_only_auxiliary`: semantic units from English-only auxiliary material.
- `legacy_no_downloadable_url`: attachment label exists but the source has no downloadable URL.
- `legacy_attachment_label_only`: semantic-unit coverage for a legacy attachment label with no downloadable URL.
- `diagram_unavailable`: diagram content was unavailable in the export and must not be reconstructed.
- `not_document_format`: link or artifact is outside `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, and `.zip` document-format preservation scope.
- `accepted_source_limitation`: source limitation is documented and accepted.
- `accepted_english_only_auxiliary`: English-only auxiliary limitation is documented and accepted.

## Terminology

- Preserve exact product names, SQL, commands, properties, paths, error codes, class names, filenames, and URLs in downstream answers.
- Do not translate source labels such as `English-only source`, `legacy_no_downloadable_url`, `diagram_unavailable`, or `not_document_format` when the label itself is the evidence.
- Korean filenames, encoded Korean URL components, and Korean sample data remain source identifiers and should not be normalized into invented English names.
