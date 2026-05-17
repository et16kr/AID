# Shared GPTs Knowledge Encyclopedia Requirements

Every job in this workflow must follow `.codex-jobs/gpts-knowledge-encyclopedia/workflow-requirements.md`.

## Required Reading

- `AGENTS.md`
- `llm-reference/GPTS_KNOWLEDGE_PACKAGING_RECOMMENDATIONS.md`
- `llm-reference/LLM_REFERENCE_BUILD_REPORT.md`
- `llm-reference/HANDOFF.md`
- `.codex-jobs/gpts-knowledge-encyclopedia/jobs.tsv`
- `.codex-jobs/gpts-knowledge-encyclopedia/workflow-requirements.md`

## Global Rules

- The purpose is GPTs Knowledge upload, not another general handoff.
- The final GPTs answer artifact must be 1 required file plus at most 1 optional audit file.
- Original source trees `arch/`, `FAQE/`, `DOCK/`, and `faq/` must not be required at GPT answer time.
- Use only generated `llm-reference/` content as the source for the upload files.
- Preserve source paths as evidence labels and maintenance traceability, not as runtime dependencies.
- Include all 12 topic documents in full in the required encyclopedia bundle.
- Preserve exact product names, SQL, commands, paths, properties, system views, error codes, class names, driver names, package filenames, URLs, and version strings.
- Preserve accepted limitation labels and do not invent unavailable diagrams, attachments, or source content.
- Do not include full raw TSV ledgers in the customer-facing encyclopedia file unless explicitly changing the workflow requirement and documenting the retrieval risk.
- Do not manually advance `jobs.tsv` statuses. The orchestrator owns `Progress` and `Done` status transitions.
- Do not stage or commit `.codex-jobs/gpts-knowledge-encyclopedia/jobs.tsv`, logs, rollbacks, or `.runtime` files from inside a job.

## Standard Verification

Use relevant targeted checks for the job, and at minimum run:

```bash
python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json
git diff --check
```

For final bundle checks, the artifact scan must have no matches:

```bash
rg -n "\[\]\(|Error rendering macro|Unknown macro|unknown-macro|\]\(#\)" llm-reference/gpts-upload/Altibase_GPT_Knowledge_Encyclopedia.md
```

`rg` exit code 1 is the expected passing result for this no-match scan.
