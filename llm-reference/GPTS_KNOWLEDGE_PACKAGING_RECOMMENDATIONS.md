# GPTs Knowledge Packaging Requirements

Date: 2026-05-17

## Purpose

This document defines the requirements for creating GPTs Knowledge upload artifacts from the generated Altibase LLM reference package.

The target is not a general documentation handoff. The target is a GPTs attachment package that lets a GPT answer customer and support questions without uploading the original source trees under `arch/`, `FAQE/`, `DOCK/`, or `faq/`.

The final customer-facing GPTs answer target is exactly 1 required Knowledge file plus at most 1 optional audit file. The optional audit file is for validation and support traceability only; it must not be required for customer answers. This limit is intentional because other manual files may also need to use the GPTs file slots.

## Current Assessment

The existing `llm-reference/` topic documents are suitable source material for a GPTs Knowledge package, but the current individual files are not the final upload shape.

Uploading the individual `llm-reference/*.md` files would consume too many GPTs Knowledge slots. Uploading only a subset of the topic files would make the GPT incomplete. Uploading only `README.md`, `source-index.md`, or the build report would not provide enough answer content.

Therefore, the correct next step is to create one or two generated bundle files that concatenate and normalize the answer corpus for GPTs retrieval.

## Corpus Gate

Use only generated `llm-reference/` content as the source boundary for GPTs upload files. The original source trees `arch/`, `FAQE/`, `DOCK/`, and `faq/` are not GPTs upload inputs and are not GPT answer-time dependencies.

Source paths from those trees may remain in the generated upload files only as evidence labels and maintenance traceability. No generated upload file may imply that a GPT can open, inspect, or depend on those repository paths while answering a user.

Reject any proposed GPTs attachment artifact as incomplete if it requires any of the following for normal customer-answer generation:

- Direct upload of `arch/`, `FAQE/`, `DOCK/`, or `faq/`.
- Direct upload of individual topic files instead of the encyclopedia bundle.
- A subset of the 12 topic documents.
- The optional audit bundle as a runtime answer dependency.
- Full raw TSV ledgers in the customer-facing encyclopedia file.

## GPTs Knowledge Constraint

OpenAI Help Center guidance checked on 2026-05-17 says GPTs Knowledge supports up to 20 attached files per GPT, with large per-file limits. Text-forward files are preferred because GPTs process uploaded files by chunking text and retrieving relevant chunks at answer time.

Reference pages:

- `https://help.openai.com/en/articles/8843948-knowledge-in-gpts`
- `https://help.openai.com/en/articles/8555545-file-uploads-faq`

For this repository, file count is the binding constraint. The current generated Altibase reference Markdown corpus is small enough to fit into one GPTs Knowledge file.

## Required Output

Create a GPT-upload directory:

```text
llm-reference/gpts-upload/
```

Required file:

```text
llm-reference/gpts-upload/Altibase_GPT_Knowledge_Encyclopedia.md
```

Optional second file:

```text
llm-reference/gpts-upload/Altibase_GPT_Knowledge_Audit.md
```

If only one GPTs Knowledge slot can be used for Altibase reference content, upload only `Altibase_GPT_Knowledge_Encyclopedia.md`.

## Definition Of Complete For GPTs Upload

The GPTs upload artifact is complete only when all of the following are true:

- The GPT can answer from the generated upload file without requiring original `arch/`, `FAQE`, `DOCK`, or `faq` files.
- The required encyclopedia file includes the full text of every topic document `01` through `12`.
- The required encyclopedia file includes enough front matter and instructions for the GPT to know how to use the package.
- The required encyclopedia file includes source-path traceability so answers can refer back to source paths when needed.
- The required encyclopedia file preserves exact product names, commands, SQL, configuration properties, paths, class names, driver names, error codes, filenames, URLs, and version strings.
- The required encyclopedia file preserves accepted limitation labels, including `English-only source`, `english_only_auxiliary`, `legacy_no_downloadable_url`, `legacy_attachment_label_only`, `diagram_unavailable`, `not_document_format`, `accepted_source_limitation`, and `accepted_english_only_auxiliary`.
- The required encyclopedia file does not depend on full raw coverage TSV files for normal answer generation.
- The optional audit file, if created, contains validation evidence and coverage summaries for internal review.
- No generated upload file tells the GPT to open or inspect original source files as a requirement for answering. Source paths are evidence labels, not required runtime inputs.

## Required Encyclopedia Bundle

`Altibase_GPT_Knowledge_Encyclopedia.md` is the primary GPTs Knowledge file. It must be customer-answer ready and self-contained.

It must include these sections in this order:

1. `# Altibase GPT Knowledge Encyclopedia`
2. `## How To Use This Knowledge File`
3. `## Answering Rules For GPTs`
4. `## Source Package Status`
5. Full content of `llm-reference/README.md`
6. Full content of `llm-reference/source-index.md`
7. Full content of `llm-reference/00-source-classification.md`
8. Full content of `llm-reference/01-installation-upgrade-platform.md`
9. Full content of `llm-reference/02-architecture-storage-concepts.md`
10. Full content of `llm-reference/03-operation-administration-security.md`
11. Full content of `llm-reference/04-backup-recovery.md`
12. Full content of `llm-reference/05-replication-ha.md`
13. Full content of `llm-reference/06-monitoring-diagnostics.md`
14. Full content of `llm-reference/07-troubleshooting-error-messages.md`
15. Full content of `llm-reference/08-sql-performance-tuning.md`
16. Full content of `llm-reference/09-development-client-api.md`
17. Full content of `llm-reference/10-application-framework-integration.md`
18. Full content of `llm-reference/11-migration-conversion-tools.md`
19. Full content of `llm-reference/12-terminology-multilingual-preservation.md`
20. GPT usage guidance from `llm-reference/HANDOFF.md`
21. Compact final validation summary from `llm-reference/LLM_REFERENCE_BUILD_REPORT.md`
22. Compact accepted-risk and attachment-limitation summary from `llm-reference/coverage/README.md`

The topic documents must be included in full. Do not summarize or selectively copy the topic files into the encyclopedia bundle.

## Optional Audit Bundle

Create `Altibase_GPT_Knowledge_Audit.md` only when a second GPTs Knowledge slot is available for internal review or technical support validation.

It should include:

- Full `llm-reference/LLM_REFERENCE_BUILD_REPORT.md`
- Full `llm-reference/HANDOFF.md`
- Full `llm-reference/coverage/README.md`
- Full `llm-reference/GPTS_KNOWLEDGE_PACKAGING_RECOMMENDATIONS.md`
- Coverage status distributions
- Answerability status distributions
- Attachment and diagram preservation summary
- Source inventory and source-to-topic reconciliation summary

Do not include full `semantic-unit-coverage.tsv`, `attachment-diagram-register.tsv`, or `answerability-backtest.tsv` in the customer-facing encyclopedia file. These TSVs are audit evidence, not answer prose. They may be included in the optional audit file only if the GPT is for internal audit and the additional retrieval noise is acceptable.

## Why Full TSV Ledgers Are Not Required In The Answer Bundle

The goal is to preserve original technical meaning for GPT answers, not to force the GPT to read audit rows as user-facing documentation.

The consolidated topic documents already carry the answerable technical content extracted from the original source corpus. The coverage TSVs prove that extraction and classify limitations. For customer-answer GPTs, the answer bundle should include the full topic documents and compact risk summaries, while the full TSV ledgers remain in the repository for audit and regeneration.

If a future reviewer needs row-level proof, use the optional audit file or the repository copy of `llm-reference/coverage/`.

## Required Answering Rules For GPT Instructions

Use these instructions in the GPT configuration and also embed them near the top of `Altibase_GPT_Knowledge_Encyclopedia.md`:

```text
Use Altibase_GPT_Knowledge_Encyclopedia.md as the primary source for Altibase answers.
Answer from the uploaded knowledge file before relying on general knowledge.
Do not require access to original arch, FAQE, DOCK, or faq source files.
Prefer exact commands, SQL, file paths, configuration properties, system views, error codes, class names, driver names, package filenames, URLs, and version strings from the knowledge file.
Answer in the user's language, but keep product names, SQL, commands, paths, properties, error codes, class names, filenames, URLs, and version strings exactly as written.
When source confidence matters, preserve labels such as English-only source, english_only_auxiliary, legacy_no_downloadable_url, legacy_attachment_label_only, diagram_unavailable, not_document_format, accepted_source_limitation, and accepted_english_only_auxiliary.
Do not invent content from unavailable diagrams, missing attachments, or legacy attachment labels with no downloadable URL.
If the knowledge file does not contain enough information to answer safely, say that the available Altibase GPT knowledge does not contain the required detail.
```

## Bundle Generation Requirements

The bundle should be generated by a repeatable script, not by manual copy and paste.

Recommended script:

```text
llm-reference/gpts-upload/build-gpts-knowledge-bundles.py
```

The script must:

- Create `llm-reference/gpts-upload/` if needed.
- Generate `Altibase_GPT_Knowledge_Encyclopedia.md`.
- Optionally generate `Altibase_GPT_Knowledge_Audit.md`.
- Insert clear document-boundary markers before each included source document.
- Preserve Markdown code blocks and tables.
- Preserve all exact identifiers without translation or normalization.
- Add a generated-file warning that names the script and source files.
- Fail if any required source file is missing.
- Print output file sizes.

Use ASCII for generated control text unless source content already contains non-ASCII identifiers, filenames, URLs, or examples.

## Bundle Validation Requirements

Before the bundle is considered GPTs-ready, run validation checks that prove the output is self-contained and complete for the stated purpose.

Automated validation is defined in:

```text
llm-reference/gpts-upload/VALIDATION_PROCESS.md
llm-reference/gpts-upload/validate-gpts-knowledge.py
```

Human review must start only after the final automated validation script reports `GPTS_AUTOMATED_PASS`.

Required checks:

```bash
python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json
git diff --check
test -f llm-reference/gpts-upload/Altibase_GPT_Knowledge_Encyclopedia.md
rg -n "BEGIN INCLUDED DOCUMENT: llm-reference/(0[0-9]|1[0-2])-.*\\.md" llm-reference/gpts-upload/Altibase_GPT_Knowledge_Encyclopedia.md
rg -n "## Source paths|## Terminology" llm-reference/gpts-upload/Altibase_GPT_Knowledge_Encyclopedia.md
rg -n "\\[\\]\\(|Error rendering macro|Unknown macro|unknown-macro|\\]\\(#\\)" llm-reference/gpts-upload/Altibase_GPT_Knowledge_Encyclopedia.md
```

For the final `rg` artifact scan, exit code 1 is the passing no-match result.

Additional required validation:

- Confirm all 12 topic files are included exactly once.
- Confirm `README.md`, `source-index.md`, `00-source-classification.md`, `HANDOFF.md`, and `LLM_REFERENCE_BUILD_REPORT.md` content needed by the bundle are included.
- Confirm the bundle contains the final decision `COMPLETE_REFERENCE_PACKAGE`.
- Confirm the bundle states that original source files are not required at GPT answer time.
- Confirm the bundle states accepted limitation labels and tells the GPT not to invent missing diagrams or attachments.
- Confirm the bundle file size is well below GPTs per-file limits.
- Confirm there are zero status-field `recheck_required` rows in the repository coverage ledgers before generating the final bundle.
- Confirm the automated validation gate passes:

```bash
python3 llm-reference/gpts-upload/validate-gpts-knowledge.py --mode full
```

Before starting human review, run the final automated gate after `GPTS_READINESS_REPORT.md` exists:

```bash
python3 llm-reference/gpts-upload/validate-gpts-knowledge.py --mode final
```

Automated checks do not replace human review. Human review remains required for customer-facing clarity, representative GPT answer quality, and GPTs UI behavior.

## Acceptance Criteria

The GPTs upload packaging work is complete only when:

- `llm-reference/gpts-upload/Altibase_GPT_Knowledge_Encyclopedia.md` exists.
- The encyclopedia bundle is generated from the current committed `llm-reference/` documents.
- The encyclopedia bundle includes the full text of all 12 topic documents.
- The encyclopedia bundle is self-contained for GPT answer generation.
- The encyclopedia bundle is one file and can be uploaded to GPTs as a text-forward Knowledge file.
- If created, the audit bundle is the second and final Altibase GPTs upload file.
- No more than 2 Altibase GPTs Knowledge files are required.
- The validation checks pass.
- The final commit records the generated bundle and the bundle-generation script.

## What The GPTs Bundle Can Replace

For GPTs answer generation, `Altibase_GPT_Knowledge_Encyclopedia.md` can replace direct upload of the original source tree.

It is suitable for:

- Customer-facing Altibase Q&A
- GPTs Knowledge upload
- Codex or assistant reference during support-answer drafting
- Multilingual answer generation from the English canonical reference

## What The GPTs Bundle Should Not Replace

The bundle should not be treated as a legal archive or word-for-word historical substitute for the original source files.

The original source trees remain necessary for:

- Source cleanup work
- Korean-English discrepancy review
- Attachment or diagram investigation
- Legal or historical preservation
- Regenerating or auditing the LLM reference package
