# Altibase LLM Reference Package

## Source paths

This package is built from the stabilized English source set and the workflow evidence below.

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

The source corpus for answer content is the Markdown set under `arch/Home` and `FAQE/Home`. Korean documents under `DOCK/Home` and `faq/Home` remain the authoritative source for source cleanup decisions, but the consolidated LLM package is written from the stabilized English source files.

## Source coverage notes

This is an exhaustive reference package for GPTs, Codex, and other LLMs. It is not a FAQ-only package and it is not a summary-only package.

R002 initializes the package structure and coverage ledgers. R003 and later jobs populate source inventory rows, source-to-topic mappings, semantic-unit coverage rows, attachment rows, answerability rows, and omission or risk rows.

Coverage ledgers live in `llm-reference/coverage/`. A source item is complete only when its row is covered in the appropriate ledger or has an accepted limitation such as `legacy_attachment_label_only`, `diagram_unavailable`, `not_document_format`, or `english_only_auxiliary`.

## Scope and audience

Use this package as the English reference base for Altibase answer generation. The package is intended for:

- LLM knowledge files for GPTs and assistants.
- Codex reference material while editing Altibase documentation.
- Human review of which source paths, attachments, risks, and answerability tests were included.

The package must preserve exact product names, commands, SQL, configuration properties, paths, class names, error codes, version conditions, attachment filenames, and source URLs.

## Key facts

- Phase 2 final decision: `READY_FOR_LLM_CONSOLIDATION`.
- Phase 1 semantic coverage decision recorded by Phase 2: `COMPLETE`.
- Source corpus boundary: `arch/Home/**/*.md` and `FAQE/Home/**/*.md`.
- Phase 2 baseline counts: `arch/Home` has 181 Markdown files and `FAQE/Home` has 241 Markdown files.
- English-only auxiliary material must be labeled as `English-only source` or `english_only_auxiliary`.
- Hash-only legacy attachment labels must be recorded as having no downloadable URL in the source.
- Missing diagrams or exported diagram placeholders must not be reconstructed from guesswork.

## Procedures

1. Read `source-index.md` to find the target topic document and owning job for a source area.
2. Use `00-source-classification.md` to apply source class labels correctly.
3. Use the topic documents `01` through `12` for answer generation after their owning jobs are complete.
4. Use the coverage TSVs to audit whether a source file, semantic unit, attachment, or answerability question is covered.
5. Treat any `recheck_required` row as blocking unless the final build report explicitly decides `RECHECK_REQUIRED`.

## SQL, commands, and configuration

Standard verification for this package starts with:

```bash
python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json
git diff --check
find DOCK/Home -type f -name '*.md' | wc -l
find faq/Home -type f -name '*.md' | wc -l
find arch/Home -type f -name '*.md' | wc -l
find FAQE/Home -type f -name '*.md' | wc -l
```

Run the export-artifact scan pattern from `workflow-requirements.md` against `llm-reference`, `arch/Home`, and `FAQE/Home`. For that scan, exit code 1 is a passing no-match result. Exit code 2 or higher is a command error.

## Validation and troubleshooting

If a source file is missing from `source-inventory.tsv` or `source-to-topic-map.tsv`, R003 or R025 must add or reconcile it. If a source unit is not answerable from a topic document, R026 must either fix the topic document or record the accepted limitation.

Do not fix newly discovered Korean-English source discrepancies directly in consolidated topic text unless the active job explicitly allows source cleanup. Record the risk and return to the English source document cleanup path.

## Version-specific notes

Version, OS, license, restart, mode, output, and failure-condition variants must stay distinct unless a coverage row names the canonical duplicate target.

## Related errors

Error code coverage is split by source class:

- Korean-source-verified error and troubleshooting material is owned by R013.
- English-only error catalog material is owned by R014 and must keep an explicit `English-only source` label.

## Attachments and external references

Attachments and external references are governed by `source-stabilization/legacy-attachments.tsv`, `source-stabilization/url-backed-attachments.tsv`, and the Phase 3 attachment register.

Do not invent URLs for labels where the source provides no downloadable URL. Preserve original `docs.altibase.com` URLs and filenames when they are available.

## Expected package files

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
- `llm-reference/HANDOFF.md`
- `llm-reference/coverage/README.md`
- `llm-reference/coverage/interrupted-run-summary.md`
- `llm-reference/coverage/source-inventory.tsv`
- `llm-reference/coverage/source-to-topic-map.tsv`
- `llm-reference/coverage/semantic-unit-coverage.tsv`
- `llm-reference/coverage/attachment-diagram-register.tsv`
- `llm-reference/coverage/answerability-backtest.tsv`
- `llm-reference/coverage/omissions-and-risks.tsv`

## Job map

`jobs.tsv` is the source of truth for runtime status. This map lists every R-series job and its expected output ownership.

| Job | Title | Expected output ownership |
| --- | --- | --- |
| `R001` | Interrupted run summary and phase gates | `llm-reference/coverage/interrupted-run-summary.md` |
| `R002` | Package scaffold and exhaustive coverage ledgers | `README.md`, `source-index.md`, `00-source-classification.md`, `coverage/README.md`, coverage TSV headers |
| `R003` | Full source inventory and source-to-topic map | `coverage/source-inventory.tsv`, `coverage/source-to-topic-map.tsv` |
| `R004` | Installation patch upgrade database creation | `01-installation-upgrade-platform.md` |
| `R005` | Platform setup OS prerequisites Docker | `01-installation-upgrade-platform.md` |
| `R006` | Architecture storage disk concepts | `02-architecture-storage-concepts.md` |
| `R007` | Configuration startup capacity OS utilities | `03-operation-administration-security.md` |
| `R008` | Administration security sessions charset FAQ | `03-operation-administration-security.md` |
| `R009` | Backup recovery failure response | `04-backup-recovery.md` |
| `R010` | Replication and HA | `05-replication-ha.md` |
| `R011` | Monitoring queries diagnostics | `06-monitoring-diagnostics.md` |
| `R012` | CPU memory OS evidence diagnostics | `06-monitoring-diagnostics.md` |
| `R013` | Troubleshooting Korean-source errors | `07-troubleshooting-error-messages.md` |
| `R014` | English-only error troubleshooting catalog | `07-troubleshooting-error-messages.md` |
| `R015` | SQL stored procedures query behavior | `08-sql-performance-tuning.md` |
| `R016` | Performance tuning optimizer indexes | `08-sql-performance-tuning.md` |
| `R017` | APRE precompiler C C++ development | `09-development-client-api.md` |
| `R018` | Java JDBC ODBC ADO.NET PHP API | `09-development-client-api.md` |
| `R019` | WAS and framework integration | `10-application-framework-integration.md` |
| `R020` | Migration conversion tools | `11-migration-conversion-tools.md` |
| `R021` | English-only auxiliary corpus integration | Relevant topic documents and coverage rows |
| `R022` | FAQ exhaustive reconciliation | Relevant topic documents and coverage rows |
| `R023` | Attachments diagrams external references | `coverage/attachment-diagram-register.tsv` |
| `R024` | Terminology multilingual preservation | `12-terminology-multilingual-preservation.md` |
| `R025` | Source semantic-unit coverage reconciliation | Coverage TSV reconciliation and topic fixes |
| `R026` | Source-derived answerability backtest | `coverage/answerability-backtest.tsv` |
| `R027` | Cross-reference unsupported-claim review | Cross-reference and wording fixes across `llm-reference/*.md` |
| `R028` | Final validation build report handoff | `LLM_REFERENCE_BUILD_REPORT.md`, `HANDOFF.md` |

## Terminology

- `Korean-source-verified`: English source content audited against Korean source material and usable as primary Phase 3 input.
- `Link-validated Korean-source-verified`: Korean-source-verified material whose links or attachments were validated in Phase 2.
- `English-only source`: Auxiliary English material that must not be presented as Korean-source-verified.
- `legacy_attachment_label_only`: A source limitation where the source has only a legacy label and no downloadable URL.
- `diagram_unavailable`: A source limitation where diagram content is unavailable and must not be recreated.
- `recheck_required`: A blocking status unless the final decision explicitly accepts `RECHECK_REQUIRED`.
