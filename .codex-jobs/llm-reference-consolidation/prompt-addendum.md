# Shared LLM Reference Consolidation Requirements

Every job in this workflow must follow `.codex-jobs/llm-reference-consolidation/workflow-requirements.md`.

## Required Reading

- `AGENTS.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- The source documents listed for the current job in `workflow-requirements.md`

## Global Rules

- Korean source documents under `DOCK/` and `faq/` remain authoritative. Do not delete, move, or rewrite them.
- Original English source documents under `arch/` and `FAQE/` are not deleted or moved.
- Consolidated LLM output goes under `llm-reference/`.
- Keep source traceability. Each consolidated document must include a `Source paths` section with actual source paths.
- Mark English-only auxiliary material as `English-only source` when used.
- Do not invent missing attachment URLs. For legacy `#` source labels, record `no downloadable URL in source`.
- Preserve exact product names, SQL, commands, configuration properties, paths, error codes, class names, and attachment filenames.
- If a new Korean-English semantic discrepancy is found, record it as a risk and fix the English source only when the job scope explicitly allows source cleanup.

## Standard Consolidated Document Shape

Use this structure unless the job-specific topic needs a small adjustment:

```markdown
# <Topic title>

## Source paths

## Scope and audience

## Key facts

## Procedures

## SQL, commands, and configuration

## Validation and troubleshooting

## Version-specific notes

## Related errors

## Attachments and external references

## Terminology
```

## Standard Verification

Run the checks that match the job scope and record results in the job's final message before committing:

```bash
python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json
git diff --check
find DOCK/Home -type f -name '*.md' | wc -l
find faq/Home -type f -name '*.md' | wc -l
find arch/Home -type f -name '*.md' | wc -l
find FAQE/Home -type f -name '*.md' | wc -l
rg -n "\[\]\(|Error rendering macro|Unknown macro|unknown-macro|\]\(#\)" llm-reference arch/Home FAQE/Home
```

The final `rg` command may find intentional examples or legacy labels. If so, explain each hit and narrow the scan until only intentional hits remain.
