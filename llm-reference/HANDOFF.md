# LLM Reference Handoff

## Source paths

- `llm-reference/README.md`
- `llm-reference/source-index.md`
- `llm-reference/00-source-classification.md`
- `llm-reference/01-installation-upgrade-platform.md`
- `llm-reference/02-architecture-storage-concepts.md`
- `llm-reference/03-operation-administration-security.md`
- `llm-reference/04-backup-recovery.md`
- `llm-reference/05-replication-ha.md`
- `llm-reference/06-monitoring-diagnostics.md`
- `llm-reference/07-troubleshooting-error-messages.md`
- `llm-reference/08-sql-performance-tuning.md`
- `llm-reference/09-development-client-api.md`
- `llm-reference/10-application-framework-integration.md`
- `llm-reference/11-migration-conversion-tools.md`
- `llm-reference/12-terminology-multilingual-preservation.md`
- `llm-reference/LLM_REFERENCE_BUILD_REPORT.md`
- `llm-reference/coverage/README.md`

## Source coverage notes

This handoff is for the completed exhaustive LLM reference package. The source corpus remains the stabilized English Markdown under `arch/Home` and `FAQE/Home`; Korean documents under `DOCK/Home` and `faq/Home` remain authoritative for future source cleanup decisions and must not be deleted or rewritten as part of using this package.

Use `llm-reference/LLM_REFERENCE_BUILD_REPORT.md` for final validation results and `llm-reference/coverage/` for machine-checkable traceability.

## Package use

For GPTs, Codex, or another LLM knowledge base, load the package in this order:

1. `llm-reference/README.md`
2. `llm-reference/source-index.md`
3. `llm-reference/00-source-classification.md`
4. Topic files `llm-reference/01-*.md` through `llm-reference/12-*.md`
5. `llm-reference/LLM_REFERENCE_BUILD_REPORT.md`
6. `llm-reference/coverage/README.md` and TSV ledgers when traceability or audit evidence is needed

The topic files are intended for answer generation. The coverage ledgers are intended for audit, source tracing, and risk-label checks.

## Codex use

When editing Altibase documentation, use the topic files to locate the consolidated English guidance, then use each topic's `Source paths` section to return to the original `arch/Home` or `FAQE/Home` source. If a Korean-English conflict is found in future work, treat the Korean source under `DOCK/Home` or `faq/Home` as authoritative and record the discrepancy before changing English source documentation.

Do not use `llm-reference/` as a replacement for the original source tree when source cleanup is required. It is a consolidated reference package with traceability back to the source files.

## GPTs and LLM knowledge-file use

Use the package as an English canonical reference for multilingual answers. The LLM may answer in Turkish, Arabic, German, French, Thai, Chinese, Japanese, Korean, or English, but the following must remain exact:

- Product and component names such as `Altibase`, `ALTIBASE HDB`, `APRE`, `iSQL`, `aexport`, `iloader`, `altimon`, and `Migration Center`.
- SQL, system views, performance views, commands, configuration properties, file paths, error codes, class names, JDBC URLs, DSNs, filenames, and source URLs.
- Version, OS, restart, license, archive/noarchive, and failure-condition variants.

When a topic says material is `English-only source`, answer with that label when source confidence matters. Do not describe English-only auxiliary content as Korean-source-verified.

## Risk labels to preserve

The final package has no unresolved `recheck_required` status rows. The remaining labels are accepted limitations:

| Label | Meaning |
| --- | --- |
| `English-only source` | Auxiliary English material outside Korean-source verification. |
| `english_only_auxiliary` | Semantic-unit coverage from English-only auxiliary material. |
| `legacy_no_downloadable_url` | The source has an attachment label but no downloadable URL. |
| `legacy_attachment_label_only` | Semantic-unit coverage for a legacy attachment label with no downloadable URL. |
| `diagram_unavailable` | The exported source says diagram content is unavailable; do not reconstruct it. |
| `not_document_format` | The link or artifact is outside the document-format attachment gate. |
| `accepted_source_limitation` | The source limitation is documented and accepted. |
| `accepted_english_only_auxiliary` | English-only auxiliary limitation is documented and accepted. |

## Verification status

Final R028 validation decision: `COMPLETE_REFERENCE_PACKAGE`.

The final validation passed manifest JSON parsing, diff whitespace checks, source document counts, artifact scans, source inventory reconciliation, source-to-topic reconciliation, coverage source-path checks, coverage target-document checks, attachment preservation checks, answerability checks, and TSV column-width checks.

## Terminology

- Keep source labels and coverage statuses untranslated when they are evidence labels.
- Keep Korean attachment filenames, encoded Korean URLs, and Korean sample data exactly as source identifiers.
- Keep SQL, commands, properties, paths, error codes, class names, and version strings in source spelling even when the surrounding answer is translated.
