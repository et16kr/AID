# Shared Exhaustive LLM Reference Consolidation Requirements

Every job in this workflow must follow `.codex-jobs/llm-reference-consolidation/workflow-requirements.md`.

## Required Reading

- `AGENTS.md`
- `.codex-jobs/llm-reference-consolidation/workflow-requirements.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `source-stabilization/validation-report.md`
- `source-stabilization/source-classification.tsv`
- `source-stabilization/legacy-attachments.tsv`
- `source-stabilization/url-backed-attachments.tsv`
- The source documents listed for the current job in `workflow-requirements.md`

## Global Rules

- Korean source documents under `DOCK/` and `faq/` remain authoritative. Do not delete, move, or rewrite them.
- Original English source documents under `arch/` and `FAQE/` are not deleted, moved, or renamed.
- Consolidated LLM output goes under `llm-reference/`.
- Use `git status --porcelain --untracked-files=all -- . ":(exclude).codex-jobs" ":(exclude).codex-jobs/**"` for the blocking preflight check.
- Do not treat `.codex-jobs/llm-reference-consolidation/jobs.tsv`, `logs/`, `rollbacks/`, or `.runtime/` as blocking project changes.
- Do not manually advance `jobs.tsv` statuses. The orchestrator owns job state transitions and will record the active job's final status after your commit.
- This is an exhaustive reference package. Do not produce only FAQ-style summaries or representative examples.
- Keep source traceability. Each consolidated document must include a `Source paths` section with actual source paths.
- Every source file and semantic unit owned by the job must be represented in the coverage TSVs.
- Mark English-only auxiliary material as `English-only source` or `english_only_auxiliary` when used.
- Do not invent missing attachment URLs. For legacy `#` source labels, record `no downloadable URL in source`.
- Preserve exact product names, SQL, commands, configuration properties, paths, error codes, class names, attachment filenames, and source URLs.
- Preserve distinct version, OS, license, restart, mode, output, and failure-condition variants. Do not collapse them unless the coverage row names the canonical duplicate target.
- If a new Korean-English semantic discrepancy is found, record it as a risk and fix the English source only when the job scope explicitly allows source cleanup.

## Required Job Method

1. Reconfirm the active job id, title, and job-specific requirements from `jobs.tsv` and `workflow-requirements.md`.
2. Inspect all source paths listed for the current job.
3. Extract or verify semantic units: concepts, procedures, SQL, commands, configuration, paths, warnings, version conditions, troubleshooting, errors, attachments, and sample code.
4. Draft or update the target topic document with enough detail for answer generation.
5. Update `llm-reference/coverage/semantic-unit-coverage.tsv` for the job-owned source units.
6. Update related coverage files when source paths, attachments, diagrams, risks, or answerability checks are in scope.
7. Self-review for omissions, unsupported claims, broken links, source-label mistakes, and unclear wording.
8. Run the targeted checks and the standard checks that match the job scope.
9. Fix failures and rerun relevant checks.
10. Review the final diff.
11. Commit the completed job with a focused message. Do not report success without a commit.

## Standard Consolidated Document Shape

Use this structure unless the job-specific topic needs a small adjustment:

```markdown
# <Topic title>

## Source paths

## Source coverage notes

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

For expected-no-match scans, `rg` exit code 1 is a passing no-match result. Exit code 2 or higher is a command error.
