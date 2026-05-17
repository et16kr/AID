# GPTs Knowledge Validation Process

Date: 2026-05-17

## Purpose

This document separates automated validation from human review for the Altibase GPTs Knowledge upload artifacts.

Human review must not start until the final automated gate passes. The final automated gate is implemented by:

```bash
python3 llm-reference/gpts-upload/validate-gpts-knowledge.py --mode final
```

Before GPTs upload bundles exist, use source-corpus preflight:

```bash
python3 llm-reference/gpts-upload/validate-gpts-knowledge.py --mode preflight
```

## Automated Validation Scope

The automated script can verify structural completeness, source inclusion, generated-file readiness, and known blocking patterns.

Automated checks include:

- Required `llm-reference/` source files exist.
- Inventory and map ledgers contain no `pending` rows.
- Coverage ledgers contain no status-field `recheck_required` rows.
- `answerability-backtest.tsv` contains no `not_answerable` rows.
- GPTs upload files exist after bundle generation.
- The human review checklist exists for the manual pass.
- No more than two Altibase GPTs upload files are required.
- `Altibase_GPT_Knowledge_Encyclopedia.md` exists.
- All 12 topic documents are included exactly once.
- Required full-text source documents match the source files between `BEGIN INCLUDED DOCUMENT` and `END INCLUDED DOCUMENT` markers.
- Required GPTs front matter exists.
- `COMPLETE_REFERENCE_PACKAGE` exists in the bundle.
- Routing terms for major question areas appear near the top of the bundle.
- Accepted limitation labels are present.
- The bundle explicitly says original source files are not GPT answer-time dependencies.
- Source-path traceability is preserved.
- Known export artifact patterns are absent.
- Full raw coverage TSV files are not embedded in the customer-facing encyclopedia bundle.
- File sizes are below configured GPTs per-file limits.
- `UPLOAD_MANIFEST.tsv` has the required structure and marks exactly one customer-required upload file.
- `GPTS_INSTRUCTIONS.txt` contains core answer rules.

## Automated Validation Commands

Before bundle generation:

```bash
python3 llm-reference/gpts-upload/validate-gpts-knowledge.py --mode preflight
```

After bundle generation, before the final readiness report:

```bash
python3 llm-reference/gpts-upload/validate-gpts-knowledge.py --mode full
```

After `GPTS_READINESS_REPORT.md` is created, and before human review:

```bash
python3 llm-reference/gpts-upload/validate-gpts-knowledge.py --mode final \
  --write-report llm-reference/gpts-upload/GPTS_AUTOMATED_VALIDATION_REPORT.md
```

The human review process may start only when the final automated decision is:

```text
GPTS_AUTOMATED_PASS
```

If the script reports:

```text
GPTS_AUTOMATED_RECHECK_REQUIRED
```

the bundle must be fixed before human review starts.

## Human Review Scope

Human review remains necessary for judgment that cannot be reduced safely to file checks.

Human review should check:

- Customer-facing clarity.
- Whether the GPT answers feel like natural support documentation rather than ledger text.
- Whether representative GPT answers are complete and not overly verbose.
- Whether source path references are useful and not confusing to customers.
- Whether the GPT refuses or qualifies answers correctly when the bundle lacks detail.
- Whether multilingual answers preserve product names, SQL, commands, paths, properties, error codes, class names, filenames, URLs, and version strings.
- Whether GPTs UI behavior with uploaded files matches the intended instructions.

Use the HTML checklist for the manual pass:

```text
llm-reference/gpts-upload/HUMAN_REVIEW_CHECKLIST.html
```

## Manual Review Sample Set

After automated validation passes, test representative questions from these areas:

- Installation, patch, upgrade, and database creation.
- OS prerequisites and Docker.
- Architecture, storage, checkpoint, and log concepts.
- Administration, security, sessions, charset, and configuration.
- Backup, recovery, and failure response.
- Replication and HA.
- Monitoring, diagnostics, CPU, memory, locks, and system views.
- Troubleshooting and error messages.
- SQL, stored procedures, optimizer, indexing, partitioning, and performance.
- APRE, JDBC, ODBC, ADO.NET, PHP, and client APIs.
- WAS and framework integration.
- Migration, conversion, and tooling.
- Terminology and multilingual answer preservation.

## Final Policy

Use this decision order:

1. Run automated validation.
2. If automated validation fails, fix the bundle and rerun.
3. If automated validation passes, start human review.
4. If human review passes, mark the upload package ready for GPTs.
5. If human review fails, fix the bundle or GPT instructions and rerun automated validation before another human review pass.
