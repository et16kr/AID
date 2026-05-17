# GPTs Upload Workflow

This directory is for the Altibase GPTs Knowledge upload workflow. The target is a self-contained GPTs answer package, not another general handoff package and not a direct upload of the original documentation trees.

## Upload Target

Customer-facing GPTs upload requires exactly one Knowledge file:

```text
llm-reference/gpts-upload/Altibase_GPT_Knowledge_Encyclopedia.md
```

At most one optional audit file may be created:

```text
llm-reference/gpts-upload/Altibase_GPT_Knowledge_Audit.md
```

`Altibase_GPT_Knowledge_Encyclopedia.md` is the required answer file. It must contain all 12 topic documents in full and enough package status, source traceability, risk labels, and answering rules for GPTs to answer without any other Altibase source attachment.

`Altibase_GPT_Knowledge_Audit.md`, if created, is for internal validation and technical support traceability only. It is not required for customer answers and must not become a GPT runtime dependency.

## Upload Order

For a customer-facing GPT, upload only this Altibase reference file:

1. `llm-reference/gpts-upload/Altibase_GPT_Knowledge_Encyclopedia.md`

Do not upload `Altibase_GPT_Knowledge_Audit.md` for normal customer-answer deployments unless the GPT is also intended for internal validation.

For an internal support or audit GPT, upload no more than these two Altibase reference files:

1. `llm-reference/gpts-upload/Altibase_GPT_Knowledge_Encyclopedia.md`
2. `llm-reference/gpts-upload/Altibase_GPT_Knowledge_Audit.md`

The encyclopedia is the answer corpus. The audit bundle is validation evidence, coverage summary, package handoff, and upload-policy traceability.

## Source Boundary

Use only the generated `llm-reference/` corpus as source material for GPTs upload files:

```text
llm-reference/README.md
llm-reference/source-index.md
llm-reference/00-source-classification.md
llm-reference/01-installation-upgrade-platform.md
llm-reference/02-architecture-storage-concepts.md
llm-reference/03-operation-administration-security.md
llm-reference/04-backup-recovery.md
llm-reference/05-replication-ha.md
llm-reference/06-monitoring-diagnostics.md
llm-reference/07-troubleshooting-error-messages.md
llm-reference/08-sql-performance-tuning.md
llm-reference/09-development-client-api.md
llm-reference/10-application-framework-integration.md
llm-reference/11-migration-conversion-tools.md
llm-reference/12-terminology-multilingual-preservation.md
llm-reference/HANDOFF.md
llm-reference/LLM_REFERENCE_BUILD_REPORT.md
llm-reference/coverage/README.md
llm-reference/GPTS_KNOWLEDGE_PACKAGING_RECOMMENDATIONS.md
```

The original source trees are not GPTs upload inputs and are not GPT answer-time dependencies:

```text
arch/
FAQE/
DOCK/
faq/
```

Source paths from those trees are retained only as evidence labels and maintenance traceability. They help maintainers audit or regenerate the package, but they do not mean that a GPT can open those paths during an answer.

## Required Workflow Outputs

Later jobs in this workflow create or update these support files:

```text
llm-reference/gpts-upload/build-gpts-knowledge-bundles.py
llm-reference/gpts-upload/validate-gpts-knowledge.py
llm-reference/gpts-upload/VALIDATION_PROCESS.md
llm-reference/gpts-upload/HUMAN_REVIEW_CHECKLIST.html
llm-reference/gpts-upload/GPTS_INSTRUCTIONS.txt
llm-reference/gpts-upload/UPLOAD_MANIFEST.tsv
llm-reference/gpts-upload/GPTS_READINESS_REPORT.md
```

The customer-facing required upload remains `Altibase_GPT_Knowledge_Encyclopedia.md` even when these support files exist.

`GPTS_INSTRUCTIONS.txt` contains copy-paste GPT configuration text. `UPLOAD_MANIFEST.tsv` records upload priority, audience, required/optional status, purpose, and notes for each Altibase GPTs Knowledge upload file.

## Run Order

1. `G001` confirms the GPTs-only target, source boundary, non-runtime source-tree rule, and upload workflow requirements. It does not create the final encyclopedia bundle.
2. `G002` creates the repeatable bundle generator and initial `Altibase_GPT_Knowledge_Encyclopedia.md` from the full generated `llm-reference/` corpus.
3. `G003` hardens retrieval and answer routing while preserving the full topic content and source traceability.
4. `G004` creates upload support files and, when useful, the optional `Altibase_GPT_Knowledge_Audit.md` without making it a customer-answer dependency.
5. `G005` runs final readiness validation and records whether the upload package is `GPTS_UPLOAD_READY` or `GPTS_RECHECK_REQUIRED`.

The orchestrator owns `jobs.tsv` status transitions. Individual jobs must not manually advance workflow status rows.

## Bundle Generator

Run the generator from the repository root:

```bash
python3 llm-reference/gpts-upload/build-gpts-knowledge-bundles.py
```

The generator writes `Altibase_GPT_Knowledge_Encyclopedia.md` and the optional `Altibase_GPT_Knowledge_Audit.md`, preserves included Markdown documents between explicit `BEGIN INCLUDED DOCUMENT` and `END INCLUDED DOCUMENT` markers, and fails if a required `llm-reference/` source file is missing.

## Acceptance Gate

A GPTs upload package is acceptable only when:

- The required customer-facing GPT upload file is `Altibase_GPT_Knowledge_Encyclopedia.md`.
- Customer-facing upload requires no more than one Altibase reference file.
- Internal upload requires no more than two Altibase reference files.
- No more than one optional audit file is used for Altibase GPTs Knowledge upload.
- The encyclopedia includes all 12 topic documents in full.
- The encyclopedia is self-contained for GPT answer generation.
- The optional audit bundle is not required for normal customer answers.
- The original source trees are not required at GPT answer time.
- Source paths are preserved as evidence labels and maintenance traceability.
- Accepted limitation labels remain visible, and unavailable diagrams or missing legacy attachments are not invented.
- Standard validation passes, including `python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json` and `git diff --check`.
