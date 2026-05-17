# GPTs Knowledge Encyclopedia Workflow Requirements

## Purpose

Create the final GPTs Knowledge upload artifacts for Altibase from the generated `llm-reference/` package.

The goal is a self-contained GPTs encyclopedia that can answer customer and support questions without attaching the original source trees. The output must be suitable for GPTs Knowledge upload when only 1 or 2 file slots are available.

## Source Boundary

Allowed source material:

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
- `llm-reference/HANDOFF.md`
- `llm-reference/LLM_REFERENCE_BUILD_REPORT.md`
- `llm-reference/coverage/README.md`
- `llm-reference/GPTS_KNOWLEDGE_PACKAGING_RECOMMENDATIONS.md`

The original source trees `arch/`, `FAQE/`, `DOCK/`, and `faq/` are not upload inputs and are not runtime dependencies. Source paths from those trees may remain inside the generated bundle as evidence labels and maintenance traceability.

## Expected Outputs

Required:

- `llm-reference/gpts-upload/build-gpts-knowledge-bundles.py`
- `llm-reference/gpts-upload/validate-gpts-knowledge.py`
- `llm-reference/gpts-upload/VALIDATION_PROCESS.md`
- `llm-reference/gpts-upload/HUMAN_REVIEW_CHECKLIST.html`
- `llm-reference/gpts-upload/Altibase_GPT_Knowledge_Encyclopedia.md`
- `llm-reference/gpts-upload/README.md`
- `llm-reference/gpts-upload/GPTS_INSTRUCTIONS.txt`
- `llm-reference/gpts-upload/UPLOAD_MANIFEST.tsv`
- `llm-reference/gpts-upload/GPTS_READINESS_REPORT.md`

Optional but preferred when it fits as the second Altibase upload file:

- `llm-reference/gpts-upload/Altibase_GPT_Knowledge_Audit.md`

## Bundle Policy

`Altibase_GPT_Knowledge_Encyclopedia.md` is the required GPTs Knowledge file.

It must:

- Include all 12 topic documents in full.
- Include enough front matter for GPTs to know how to use the file.
- Include source-path traceability without implying the GPT can open source paths at answer time.
- Include exact identifier preservation rules.
- Include accepted limitation labels and instructions not to invent unavailable material.
- Include the final source package status, including `COMPLETE_REFERENCE_PACKAGE`.
- Be generated repeatably by script.

`Altibase_GPT_Knowledge_Audit.md` is optional and intended for internal traceability. It may include reports and compact coverage summaries. It should not be required for customer answers.

## Job Breakdown

### G001 - GPTs upload requirements and corpus gate

Goal: Confirm that the workflow target is a GPTs upload artifact and establish the exact source boundary, outputs, and validation gates.

Expected work:

- Review the current `llm-reference/` package and `GPTS_KNOWLEDGE_PACKAGING_RECOMMENDATIONS.md`.
- Update packaging requirements if any criterion still permits an incomplete GPTs upload artifact.
- Create or update `llm-reference/gpts-upload/README.md` with the target files, source boundary, and upload intent.
- Do not generate the final encyclopedia bundle in this job.

Acceptance:

- The GPTs upload target is documented as 1 required file plus at most 1 optional audit file.
- The original source trees are explicitly marked as non-runtime dependencies.
- The required source files and expected outputs are listed.
- Basic checks pass and the result is committed.

### G002 - Bundle generator and encyclopedia artifact

Goal: Implement the repeatable generator and create the initial one-file encyclopedia artifact.

Expected work:

- Create `llm-reference/gpts-upload/build-gpts-knowledge-bundles.py`.
- Generate `llm-reference/gpts-upload/Altibase_GPT_Knowledge_Encyclopedia.md`.
- Include all required source files in the order defined by `GPTS_KNOWLEDGE_PACKAGING_RECOMMENDATIONS.md`.
- Insert clear `BEGIN INCLUDED DOCUMENT` and `END INCLUDED DOCUMENT` markers.
- Preserve Markdown code blocks and tables.
- Fail when any required source file is missing.

Acceptance:

- The generator runs successfully from the repository root.
- The encyclopedia file exists.
- All 12 topic documents are included exactly once in full.
- The bundle contains `COMPLETE_REFERENCE_PACKAGE`.
- The bundle states that original source files are not required at GPT answer time.
- Basic checks and bundle-specific checks pass, and the result is committed.

### G003 - GPT retrieval hardening and answer routing

Goal: Improve answerability and retrieval quality of the one-file encyclopedia without dropping content.

Expected work:

- Add or generate front matter optimized for GPTs retrieval.
- Add an answer routing index that maps common Altibase question areas to the relevant sections.
- Add exact identifier preservation guidance near the top.
- Add accepted limitation and source-confidence guidance near the top.
- Keep all 12 topic documents in full.
- Do not remove source-path traceability.

Acceptance:

- The encyclopedia remains self-contained and includes all topic files in full.
- The top of the file clearly tells GPTs how to answer and when to avoid invention.
- The routing index covers installation, platform, architecture, administration, backup, replication, monitoring, troubleshooting, SQL/performance, development/API, framework integration, migration, and terminology.
- Basic checks and bundle-specific checks pass, and the result is committed.

### G004 - Optional audit bundle and upload handoff

Goal: Create upload support files and the optional audit bundle.

Expected work:

- Generate or update `llm-reference/gpts-upload/Altibase_GPT_Knowledge_Audit.md`.
- Create `llm-reference/gpts-upload/GPTS_INSTRUCTIONS.txt` with copy-paste GPT configuration instructions.
- Create `llm-reference/gpts-upload/UPLOAD_MANIFEST.tsv` listing generated upload files, purpose, required/optional status, and whether each should be uploaded to a customer-facing GPT.
- Ensure the customer-facing required upload remains one file.

Acceptance:

- `GPTS_INSTRUCTIONS.txt` is directly usable in GPT configuration.
- `UPLOAD_MANIFEST.tsv` clearly distinguishes required customer upload from optional audit upload.
- The optional audit bundle does not become a runtime dependency for customer answers.
- Basic checks pass and the result is committed.

### G005 - Final GPTs readiness validation

Goal: Prove the generated GPTs upload artifacts are complete and ready.

Expected work:

- Run final validation checks.
- Create `llm-reference/gpts-upload/GPTS_READINESS_REPORT.md`.
- Confirm all expected outputs exist.
- Confirm no more than 2 Altibase GPTs Knowledge upload files are required.
- Confirm the required encyclopedia file includes the full 12 topic documents exactly once.
- Confirm no unresolved status-field `recheck_required` rows exist in repository coverage ledgers.
- Confirm artifact scans have no matches.
- Confirm generated files are below GPTs file limits based on current OpenAI Help Center guidance recorded in the packaging requirements.
- Run `python3 llm-reference/gpts-upload/validate-gpts-knowledge.py --mode full`.
- Record that human review must not start until automated validation reports `GPTS_AUTOMATED_PASS`.
- Reference `llm-reference/gpts-upload/HUMAN_REVIEW_CHECKLIST.html` as the manual review checklist.

Acceptance:

- `GPTS_READINESS_REPORT.md` records a final decision of `GPTS_UPLOAD_READY` or `GPTS_RECHECK_REQUIRED`.
- A complete run should end with `GPTS_UPLOAD_READY`.
- The report lists the exact files to upload to GPTs.
- The report references the automated validation decision.
- Standard and targeted checks pass.
- The result is committed and the working tree is clean.
