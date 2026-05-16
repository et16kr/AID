# Shared English Source Stabilization Requirements

Every job in this workflow must follow `.codex-jobs/english-source-stabilization/workflow-requirements.md`.

## Required Reading

- `AGENTS.md`
- `KO_EN_SEMANTIC_COVERAGE_REPORT.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `semantic-coverage/README.md`
- `.codex-jobs/english-source-stabilization/workflow-requirements.md`
- The Phase 2 evidence files relevant to the current job, if they already exist

## Global Rules

- Do not run `.codex-jobs/llm-reference-consolidation/run-all.sh`.
- Do not create `llm-reference/`.
- Do not delete, move, or rewrite Korean source documents under `DOCK/` or `faq/`.
- Do not delete, move, or rename English source documents under `arch/` or `FAQE/`.
- Preserve exact technical identifiers: product names, commands, SQL, properties, paths, error codes, class names, attachment filenames, and URLs.
- Fix English source text only when the current job identifies a real source-stability defect and the correction is safe from local context.
- If a finding cannot be resolved safely, record it as a concrete risk and let E008 decide `RECHECK_REQUIRED`.

## Worktree Handoff Check

Before editing, run this from the repository root:

```bash
git status --porcelain --untracked-files=all -- . ":(exclude).codex-jobs" ":(exclude).codex-jobs/**"
```

Stop if it prints output. Workflow runtime files under `.codex-jobs/english-source-stabilization/` are expected and are not project handoff files.

## Standard Verification

Run and record the relevant verification commands before committing:

```bash
python3 -m json.tool manifest.json >/tmp/aid-manifest-check.json
git diff --check
find DOCK/Home -type f -name '*.md' | wc -l
find faq/Home -type f -name '*.md' | wc -l
find arch/Home -type f -name '*.md' | wc -l
find FAQE/Home -type f -name '*.md' | wc -l
```

For source-stability scans, explain whether no-match `rg` exit code 1 is expected.

## Commit Requirement

A successful job must:

- review the final diff,
- create one focused git commit for that job,
- leave project files clean outside workflow runtime files.

## Workflow Definition Gate

`run-all.sh` refuses to start when workflow definition files are uncommitted. This is intentional so generated prompts, requirements, and scripts are not lost while `.codex-jobs` runtime files are excluded from project dirty checks. For `jobs.tsv`, status-only runtime changes are allowed, but uncommitted job definition changes are blocked. Runtime paths `logs/`, `rollbacks/`, and `.runtime/` are excluded.
