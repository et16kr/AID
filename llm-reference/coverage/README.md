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

- `source-inventory.tsv` and `source-to-topic-map.tsv` must each contain exactly one row for every `arch/Home/**/*.md` and `FAQE/Home/**/*.md` source file after R003.
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
