# Coverage Ledgers

## Source paths

- `.codex-jobs/llm-reference-consolidation/workflow-requirements.md`
- `.codex-jobs/llm-reference-consolidation/jobs.tsv`
- `source-stabilization/source-classification.tsv`
- `source-stabilization/legacy-attachments.tsv`
- `source-stabilization/url-backed-attachments.tsv`

## Source coverage notes

R002 initializes the coverage ledger files with exact headers. Later jobs append rows. Empty data sections in these TSVs mean "not populated yet by the owning job", not "coverage complete".

The existing `interrupted-run-summary.md` is R001 narrative evidence. The TSV files are the machine-checkable ledgers for source inventory, topic mapping, semantic units, attachments, answerability, and risks.

## Scope and audience

Use these ledgers to prove that every source file and every answer-affecting source unit is either represented in a topic document or explicitly classified as an accepted limitation.

## Key facts

- `source-inventory.tsv` and `source-to-topic-map.tsv` must each contain exactly one row for every Markdown source file under `arch/Home` and `FAQE/Home` after R003.
- `semantic-unit-coverage.tsv` must include every answer-affecting concept, procedure, command, SQL statement, configuration item, path, warning, version condition, troubleshooting item, error, attachment, external reference, and sample code owned by later jobs.
- `attachment-diagram-register.tsv` must preserve URL-backed document-format attachments and accepted limitations.
- `answerability-backtest.tsv` must show source-derived answerability.
- `omissions-and-risks.tsv` must track accepted limitations, English-only auxiliary use, and any recheck risk.

## Procedures

1. Preserve the exact header line in every TSV.
2. Append rows with tab-separated fields only.
3. Escape literal tabs or newlines in field values as `\t` and `\n`.
4. Use the allowed status values from `workflow-requirements.md`.
5. Keep target document and section references specific enough for review.

## SQL, commands, and configuration

Header check:

```bash
head -n 1 llm-reference/coverage/source-inventory.tsv
head -n 1 llm-reference/coverage/source-to-topic-map.tsv
head -n 1 llm-reference/coverage/semantic-unit-coverage.tsv
head -n 1 llm-reference/coverage/attachment-diagram-register.tsv
head -n 1 llm-reference/coverage/answerability-backtest.tsv
head -n 1 llm-reference/coverage/omissions-and-risks.tsv
```

Inventory count check for later jobs:

```bash
find arch/Home FAQE/Home -type f -name '*.md' | wc -l
```

## Validation and troubleshooting

If a later job cannot cover a semantic unit, it must add a row with an accepted limitation or `recheck_required`. Final acceptance requires zero `recheck_required` rows unless the final report decision is `RECHECK_REQUIRED`.

If a source path in a coverage row no longer exists, R025 or R028 must either correct the path or document the source limitation.

## Version-specific notes

Coverage rows must preserve distinct version, OS, license, restart, mode, output, and failure-condition variants. Use `covered_by_canonical_duplicate` only when the canonical target section is named.

## Related errors

Error rows should preserve exact error codes and message text. English-only error rows must use an English-only source label or auxiliary status.

## Attachments and external references

Attachment rows must not invent missing URLs. Use `legacy_no_downloadable_url` for labels that do not have a downloadable URL in the source, and use `diagram_unavailable` when the source evidence says diagram content is unavailable.

## R022 FAQ reconciliation

R022 reconciled every Korean-source-verified FAQE source from `source-stabilization/source-classification.tsv` against the topic documents and `semantic-unit-coverage.tsv`.

- FAQE sources reconciled: 115 total, including 108 `Korean-source-verified` and 7 `Link-validated Korean-source-verified` sources.
- Pre-existing answer-affecting semantic rows checked for those sources: 555.
- R022 reconciliation marker rows added: 115 `source_metadata` rows with IDs `R022-FAQ-RECON-001` through `R022-FAQ-RECON-115`.
- Resulting scoped statuses: 645 `covered`, 4 `covered_by_canonical_duplicate`, 2 `legacy_attachment_label_only`, and 19 `not_document_format`.
- Reconciliation found no missing source-inventory rows, no missing source-to-topic-map rows, no missing source paths in topic documents, no `recheck_required` FAQ rows, and no covered FAQ rows with empty targets.

The reconciliation preserved source-specific version, OS, license where present, restart, backup/recovery mode, output, and failure-condition variants that already appear in the topic documents and semantic rows. Repetitive FAQ units are retained either as covered rows or as `covered_by_canonical_duplicate` rows with a named canonical target.

## R023 attachment, diagram, and external reference register

R023 rebuilt `attachment-diagram-register.tsv` from `source-stabilization/legacy-attachments.tsv`, `source-stabilization/url-backed-attachments.tsv`, and parsed HTTP(S) attachment or reference links in every Markdown source file under `arch/Home` and `FAQE/Home`. Source metadata lines (`source_url:` and the exported `Source:` line) are covered by the source inventory/source index and are not duplicated as external-reference rows.

- Registered rows: 825 across 184 source files.
- Preservation statuses: `diagram_unavailable` 14, `legacy_no_downloadable_url` 21, `not_document_format` 732, `preserved_url` 58.
- Kinds: `diagram` 14, `document_attachment` 58, `embedded_icon` 4, `embedded_image` 363, `external_reference` 332, `legacy_attachment_label` 21, `support_artifact` 33.
- URL-backed document-format rows from Phase 2 are represented with `preserved_url`; legacy labels are represented with `legacy_no_downloadable_url`; unavailable Gliffy exports are represented with `diagram_unavailable`; images, icons, support artifacts, and web/manual links are represented with `not_document_format`.
- R023 also appended matching `semantic-unit-coverage.tsv` rows for every register row, using `R023-ATT-*` and `R023-EXT-*` unit IDs.

## R025 source and semantic-unit coverage reconciliation

R025 reconciled the source inventory, topic map, semantic-unit ledger, topic source-path traceability, and accepted limitation rows after the topic and attachment consolidation jobs.

- Source tree count: `find arch/Home FAQE/Home -type f -name '*.md' | wc -l` returns 422.
- `source-inventory.tsv`: 422 unique source rows, 0 missing source files, 0 extra source files, 0 duplicate source paths; status distribution is `covered=296` and `covered_with_risk=126`.
- `source-to-topic-map.tsv`: 422 unique source rows, 0 missing source files, 0 extra source files, 0 duplicate source paths; status distribution is `mapped=296` and `mapped_with_risk=126`.
- Topic traceability: every source path in `source-to-topic-map.tsv` appears in its primary topic document, and every primary or secondary topic file referenced by the map exists.
- `semantic-unit-coverage.tsv`: every row has a non-empty `target_doc` and `target_section` unless the row has an accepted limitation status: `source_index_only`, `legacy_attachment_label_only`, `diagram_unavailable`, `not_document_format`, or `english_only_auxiliary`.
- Recheck status: all coverage TSVs contain 0 `recheck_required` rows, so no final `RECHECK_REQUIRED` decision is needed for R025.
- Accepted limitations remain explicit: `omissions-and-risks.tsv` records `accepted_source_limitation=25`, `accepted_english_only_auxiliary=5`, and `resolved=1`.

R025 also appended semantic-unit reconciliation evidence rows `R025-RECON-001` through `R025-RECON-005` so the global reconciliation itself is traceable from the ledger.

## R026 source-derived answerability backtest

R026 expanded `answerability-backtest.tsv` from the completed source inventory and semantic-unit coverage ledger.

- Existing backtest rows preserved: 289.
- R026-generated rows added: 333.
- Final backtest rows: 622 total, including 617 rows for the 422 `source-inventory.tsv` source files and 5 pre-existing rows for package or evidence sources.
- Inventory source coverage: 422 of 422 source files have at least one backtest row.
- Density coverage: 286 inventory sources have one row, 84 have two rows, and 52 have three or more rows.
- Result distribution for inventory sources: 480 `answerable` rows and 137 `answerable_with_source_label` rows.
- `not_answerable` rows: 0.
- `recheck_required` rows: 0.

The R026 generation read every source path in `source-inventory.tsv`, used `semantic-unit-coverage.tsv` as the source-derived unit list, and validated that each generated row's target document exists and keeps the source path traceable. Rows for English-only auxiliary material, canonical duplicates, parent index pages, and accepted attachment or diagram limitations use `answerable_with_source_label` so answers preserve the classification boundary instead of treating the source as Korean-source-verified.

## R027 cross-reference and unsupported-claim review

R027 normalized package cross references and source labels without changing original `arch/Home`, `FAQE/Home`, `DOCK/Home`, or `faq/Home` sources.

- Replaced wildcard-style source labels such as `FAQE/Home/ALTIBASE HDB Troubleshooting/**` with existing source directories in topic notes and risk evidence.
- Normalized the monitoring topic's `SQL, commands, and configuration` section heading to match the package document shape.
- Rechecked source-path traceability for top-level `llm-reference/*.md` Source paths sections and coverage TSV `source_path` values.
- Rechecked that English-only auxiliary material remains labeled as `English-only source` or `english_only_auxiliary` and is not described as Korean-source-verified.
- Rechecked that coverage status fields contain no `recheck_required` rows and that Markdown export-artifact scans return no live defects.

## R028 final validation and handoff

R028 created the final validation report and handoff:

- `llm-reference/LLM_REFERENCE_BUILD_REPORT.md`
- `llm-reference/HANDOFF.md`

Final validation confirmed expected output presence, source inventory reconciliation, source-to-topic reconciliation, coverage source-path existence, coverage target-document existence, attachment preservation, answerability results, accepted limitation labels, TSV column consistency, document count checks, manifest JSON validity, diff whitespace, and artifact scans.

R028 appended semantic-unit evidence rows `R028-FINAL-001` and `R028-HANDOFF-001` so the final report and handoff are traceable from `semantic-unit-coverage.tsv`.

## Ledger files

| File | Purpose | First row owner |
| --- | --- | --- |
| `source-inventory.tsv` | One row per source file with source class, owner job, counts, primary topic, and status | `R003` |
| `source-to-topic-map.tsv` | One row per source file with topic routing and owner job | `R003` |
| `semantic-unit-coverage.tsv` | One row per answer-affecting source unit or accepted limitation | Topic and reconciliation jobs |
| `attachment-diagram-register.tsv` | One row per attachment, diagram, or external reference in scope | `R023` |
| `answerability-backtest.tsv` | Source-derived question and answerability evidence | `R026` |
| `omissions-and-risks.tsv` | Accepted limitations, unresolved risks, and resolved omissions | Any job that finds a risk |

## Header contracts

`source-inventory.tsv`:

```text
source_path	source_class	owner_job	title	heading_count	code_block_count	attachment_count	primary_topic	coverage_status	notes
```

`source-to-topic-map.tsv`:

```text
source_path	source_class	primary_topic	secondary_topics	owner_job	mapped_status	notes
```

`semantic-unit-coverage.tsv`:

```text
source_path	source_heading	unit_id	unit_type	source_excerpt_or_identifier	coverage_status	target_doc	target_section	target_anchor	preservation_note	risk
```

`attachment-diagram-register.tsv`:

```text
source_path	label_or_url	kind	extension	source_class	target_doc	preservation_status	risk	notes
```

`answerability-backtest.tsv`:

```text
source_path	unit_id	question	expected_answer_basis	target_doc	target_section	result	risk	notes
```

`omissions-and-risks.tsv`:

```text
source_path	unit_id	issue_type	description	action	final_status	notes
```

## Terminology

- `covered`: The unit is represented in a topic document.
- `covered_by_canonical_duplicate`: The unit is duplicated and covered by a named canonical target.
- `source_index_only`: The item is source metadata only.
- `legacy_attachment_label_only`: The item is a non-downloadable legacy source label.
- `diagram_unavailable`: Diagram content is unavailable and not reconstructed.
- `english_only_auxiliary`: The item is useful auxiliary English-only material.
- `recheck_required`: Coverage cannot be verified and must be resolved before a complete final decision.
