# GPTs Knowledge Packaging Recommendations

Date: 2026-05-17

## Purpose

This document records the recommended packaging strategy for using the generated Altibase LLM reference package as GPTs Knowledge.

The operational constraint is that original source documents under `arch/`, `FAQE/`, `DOCK/`, and `faq/` cannot be uploaded to GPTs. The GPT must be able to answer from the newly generated `llm-reference/` documents only. GPTs also have a limited number of Knowledge file slots, and some slots may be needed for separate manual files.

## Current GPTs Knowledge Constraint

OpenAI Help Center guidance checked on 2026-05-17 says GPTs Knowledge supports up to 20 attached files per GPT, with large per-file limits. Text-forward files are preferred because GPTs process uploaded files by chunking text and retrieving relevant chunks at answer time.

Reference pages:

- `https://help.openai.com/en/articles/8843948-knowledge-in-gpts`
- `https://help.openai.com/en/articles/8555545-file-uploads-faq`

Because the generated Altibase reference package is small enough to fit into one large Markdown file, file count is the binding constraint, not file size.

## Recommendation

Create GPT-upload-specific bundle files instead of uploading the current individual `llm-reference/*.md` files one by one.

Recommended upload set:

1. `Altibase_GPT_Knowledge_Full.md` - required
2. `Altibase_GPT_Knowledge_Audit.md` - optional, internal-review use only

If only one GPTs Knowledge slot is available for this project, upload only `Altibase_GPT_Knowledge_Full.md`.

## Required Bundle: `Altibase_GPT_Knowledge_Full.md`

This file should be the primary customer-answer knowledge file. It should be built from the generated documents only.

Include these files in this order:

1. `llm-reference/README.md`
2. `llm-reference/source-index.md`
3. `llm-reference/00-source-classification.md`
4. `llm-reference/01-installation-upgrade-platform.md`
5. `llm-reference/02-architecture-storage-concepts.md`
6. `llm-reference/03-operation-administration-security.md`
7. `llm-reference/04-backup-recovery.md`
8. `llm-reference/05-replication-ha.md`
9. `llm-reference/06-monitoring-diagnostics.md`
10. `llm-reference/07-troubleshooting-error-messages.md`
11. `llm-reference/08-sql-performance-tuning.md`
12. `llm-reference/09-development-client-api.md`
13. `llm-reference/10-application-framework-integration.md`
14. `llm-reference/11-migration-conversion-tools.md`
15. `llm-reference/12-terminology-multilingual-preservation.md`
16. The GPT usage guidance from `llm-reference/HANDOFF.md`

Do not include full coverage TSV ledgers in the customer-answer bundle. They are useful for audit, but they add retrieval noise for normal customer questions.

## Optional Bundle: `Altibase_GPT_Knowledge_Audit.md`

Create this only when at least one additional GPTs Knowledge slot is available for internal or technical-review use.

Include:

- `llm-reference/LLM_REFERENCE_BUILD_REPORT.md`
- `llm-reference/HANDOFF.md`
- `llm-reference/coverage/README.md`
- A compact summary of coverage status distributions
- A compact summary of accepted risk labels
- A compact source-to-topic index if source traceability is needed

Avoid including full `semantic-unit-coverage.tsv`, `attachment-diagram-register.tsv`, or `answerability-backtest.tsv` unless the GPT is specifically for internal audit. These ledgers are large and may reduce answer quality for customer-facing GPTs.

## GPT Instructions To Use With The Bundle

Use the following instruction text, or a close variant, in the GPT configuration:

```text
Use Altibase_GPT_Knowledge_Full.md as the primary source for Altibase answers.
Answer from the uploaded knowledge file before relying on general knowledge.
Prefer exact commands, SQL, file paths, configuration properties, system views, error codes, class names, version strings, and package filenames from the knowledge file.
Answer in the user's language, but keep product names, SQL, commands, paths, properties, error codes, class names, filenames, URLs, and version strings exactly as written.
When source confidence matters, preserve labels such as English-only source, english_only_auxiliary, legacy_no_downloadable_url, legacy_attachment_label_only, diagram_unavailable, not_document_format, accepted_source_limitation, and accepted_english_only_auxiliary.
Do not invent content from unavailable diagrams, missing attachments, or legacy attachment labels with no downloadable URL.
If the knowledge file does not contain enough information to answer safely, say that the available Altibase reference does not contain the required detail.
```

## Why This Is Better Than Uploading Individual Topic Files

Uploading all current `llm-reference/*.md` files would consume most of the available GPTs Knowledge slots before separate manual files are added. A single bundle preserves the same answer content while leaving file slots for manual work.

The generated topic files are already organized with clear headings, `Source paths`, and `Terminology` sections. Combining them into one text-forward Markdown file should preserve retrieval quality while reducing file-slot pressure.

## What The Bundle Can Replace

For GPTs answer generation, `Altibase_GPT_Knowledge_Full.md` can replace direct upload of the original source tree.

It is suitable for:

- Customer-facing Altibase Q&A
- GPTs Knowledge upload
- Codex or assistant reference during support-answer drafting
- Multilingual answer generation from the English canonical reference

## What The Bundle Should Not Replace

The bundle should not be treated as a legal archive or word-for-word substitute for the original source files.

The original source trees remain necessary for:

- Source cleanup work
- Korean-English discrepancy review
- Attachment or diagram investigation
- Legal or historical preservation
- Regenerating or auditing the LLM reference package

## Packaging Validation Checklist

Before uploading the bundle to GPTs:

- Confirm the bundle contains only generated `llm-reference/` content.
- Confirm all topic files `01` through `12` are included.
- Confirm `README.md`, `source-index.md`, and `00-source-classification.md` are included.
- Confirm the GPT usage guidance from `HANDOFF.md` is included.
- Confirm exact identifiers are preserved without translation or normalization.
- Confirm coverage TSV files are omitted from the customer-answer bundle unless intentionally building an audit GPT.
- Confirm the final bundle is clear Markdown text, not PDF or presentation format.

