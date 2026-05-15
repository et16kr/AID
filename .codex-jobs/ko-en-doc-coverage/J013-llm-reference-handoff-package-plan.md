# J013 LLM Reference Handoff Package Plan Note

Date: 2026-05-16

## Scope

J013 is limited to the handoff plan for consolidating the reviewed English documents into GPTs, Codex, and other LLM reference documents. It does not rewrite Korean source documents, English source documents under `arch/Home` or `FAQE/Home`, attachment URLs, or `manifest.json`.

## Initial Git State

Before J013 edits, the only dirty tracked file was `.codex-jobs/ko-en-doc-coverage/jobs.tsv`, where the workflow runner had changed J013 from `ToDo` to `Progress`.

No project documentation files under `DOCK/`, `arch/`, `faq/`, `FAQE/`, `manifest.json`, `KO_EN_DOC_REVIEW_REPORT.md`, or `LLM_REFERENCE_REVIEW_PLAN.md` were dirty before editing.

## Design Note

J013 changes the planned documentation structure for the next phase only. The added plan defines a future `llm-reference/` package layout with topic-based output documents, source-path traceability rules, duplicate handling rules, and multilingual terminology preservation rules.

The plan keeps the source hierarchy intact:

- Korean documents remain authoritative.
- Original English documents remain in place for review and traceability.
- Consolidated LLM reference documents should be generated as new files in a separate output directory.
- English-only `FAQE` extras must be labeled and separately reviewed if included because they are outside the Korean-source core coverage set.

## Documents Updated

- `LLM_REFERENCE_REVIEW_PLAN.md`
- `.codex-jobs/ko-en-doc-coverage/J013-llm-reference-handoff-package-plan.md`
- `.codex-jobs/ko-en-doc-coverage/jobs.md`
- `.codex-jobs/ko-en-doc-coverage/jobs.tsv`

## Self-Review Result

- The package plan includes concrete topic groups, proposed output filenames, and source paths.
- The plan preserves the J002-J012 coverage boundary and does not mark English-only `FAQE` extras as Korean-source verified.
- Multilingual rules explicitly preserve product names, commands, SQL, system views, properties, file paths, error codes, versions, attachments, and URLs.
- No original Korean or English source document is deleted, moved, or rewritten by this job.

## Verification

The following checks passed during J013:

- `python3 -m json.tool manifest.json > /tmp/aid_manifest_j013.json`
- `git diff --check`
- `bash -n .codex-jobs/ko-en-doc-coverage/run_all.sh`
- `bash -n .codex-jobs/ko-en-doc-coverage/run-all.sh`
- Document counts:
  - `DOCK`: 51 Markdown files
  - `faq`: 115 Markdown files
  - `arch`: 181 Markdown files
  - `FAQE`: 241 Markdown files
- Planned source-path validation:
  - 101 `arch/Home` and `FAQE/Home` source path patterns were checked.
  - Missing source path patterns: 0.
- Markdown consistency check:
  - Empty Markdown links in changed planning files: 0.
  - Unresolved placeholder markers in changed planning files: 0.
