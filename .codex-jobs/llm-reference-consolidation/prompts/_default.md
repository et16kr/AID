# Exhaustive LLM Reference Consolidation Job

## Goal

Complete the active job from `.codex-jobs/llm-reference-consolidation/jobs.tsv` according to the job-specific section in `.codex-jobs/llm-reference-consolidation/workflow-requirements.md`.

## Scope

- Work only on the active job id supplied by the orchestrator.
- Read the existing project instructions before editing.
- Do not revert unrelated user changes.
- Before editing, stop only if there are uncommitted project files outside `.codex-jobs` workflow runtime and status files.
- Do not treat `.codex-jobs/llm-reference-consolidation/jobs.tsv`, logs, rollbacks, or `.runtime` prompt files as blocking project changes.
- Complete the scoped job without asking for step-by-step confirmation unless blocked or unsafe.

## Required Steps

1. Reconfirm the active job requirement and boundary.
2. Inspect the relevant files and existing patterns.
3. Read every source path assigned to the job.
4. Extract semantic units that affect answerability.
5. Draft or edit the scoped `llm-reference/` documentation.
6. Update coverage evidence files required by the job.
7. Self-review for correctness, omissions, broken links, inconsistent terminology, unsupported claims, and source-label mistakes.
8. Apply fixes from the review.
9. Run documentation checks, link checks, formatting checks, or grep-based consistency checks appropriate for this job.
10. Run the targeted verification commands.
11. Fix failures and rerun the relevant checks.
12. Review the final diff after checks pass.
13. Commit the completed job with a focused message. Do not report success without a commit.

## Acceptance Criteria

- The active job's goal and acceptance criteria in `workflow-requirements.md` are complete.
- Every source and semantic unit owned by the job is represented in coverage evidence or has an accepted limitation.
- Relevant checks have passed or any skipped checks are explicitly explained.
- The final review passed.
- The job result is committed, and project files are clean after the commit.
