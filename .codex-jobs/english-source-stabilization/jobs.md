# English Source Stabilization

- Kind: `docs`
- Status values: `ToDo`, `Progress`, `Done`, `Fail`
- User-run command: `./run-all.sh` from this directory
- Default behavior: continue through all jobs until completion or failure
- Optional single-job mode: `RUN_ONE=1 ./run-all.sh`
- Handoff gate: uncommitted project files stop the workflow before the next job starts
- Commit gate: each successful job must pass review and create a focused commit
- Definition gate: workflow definition files must be committed before execution starts
- Shared requirements: `.codex-jobs/english-source-stabilization/workflow-requirements.md`
- Runtime prompt addendum: `.codex-jobs/english-source-stabilization/prompt-addendum.md`
- Phase 1 source of truth: `KO_EN_SEMANTIC_COVERAGE_REPORT.md`
- Final Phase 2 decision: exactly one of `READY_FOR_LLM_CONSOLIDATION` or `RECHECK_REQUIRED`

## Jobs

| ID | Status | Title | Goal |
| --- | --- | --- | --- |
| `E001` | `ToDo` | Phase 1 completion gate and baseline | Confirm the semantic coverage workflow ended COMPLETE, record baseline counts and clean-state evidence, and create the Phase 2 evidence structure. |
| `E002` | `ToDo` | Residual Korean classification | Scan English source files for Hangul, classify every hit, and fix only real untranslated English-source residue. |
| `E003` | `ToDo` | Markdown artifact cleanup | Verify empty Markdown links, macro rendering artifacts, unknown macro strings, and hash-only Markdown attachment links are absent or explicitly classified. |
| `E004` | `ToDo` | Legacy attachment inventory | Build a complete inventory of legacy attachment labels with no downloadable source URL and record them as no downloadable URL in source. |
| `E005` | `ToDo` | Technical URL-backed attachment verification | Recheck technical document-format attachment links and confirm URL-backed technical attachment omissions remain zero. |
| `E006` | `ToDo` | FAQ URL-backed attachment verification | Recheck FAQ document-format attachment links and confirm URL-backed FAQ attachment omissions remain zero. |
| `E007` | `ToDo` | English-only FAQE classification | Classify English-only FAQE material separately from Korean-source-verified content for later consolidation. |
| `E008` | `ToDo` | Manifest and source metadata check | Validate manifest.json, update metadata only if source files changed, and verify source counts remain stable. |
| `E009` | `ToDo` | Final stabilization report | Create the final Phase 2 stabilization report with READY_FOR_LLM_CONSOLIDATION or RECHECK_REQUIRED and verification evidence. |

## Resume Rules

- `Fail`: stop before starting later jobs.
- Dirty project files: stop before starting or advancing to another job.
- `Progress`: preserve interruption evidence, set the job back to `ToDo`, then rerun only when project files are clean.
- `Done`: skip.
- Nonzero `codex exec` exits leave the job as `Progress` by default; the next manual run stops if project files are dirty, or resets runtime state and retries when clean.
- Workflow files under `.codex-jobs/english-source-stabilization/`, including `jobs.tsv`, logs, rollbacks, and `.runtime`, are status/runtime files and are not blocking project handoff changes.
- `run-all.sh` still refuses to start if workflow definition files such as prompts, requirements, or scripts are uncommitted. For `jobs.tsv`, runtime status-only changes are allowed, but uncommitted job definition changes are blocked.

## Acceptance Checklist

- Each job has a matching prompt in `prompts/`.
- Each job has concrete acceptance criteria.
- Each prompt receives `prompt-addendum.md` at runtime.
- `workflow-requirements.md` defines Phase 2 evidence outputs and final decision rules.
- Jobs must not create `llm-reference/` or run Phase 3.
- Phase 2 evidence is written under `source-stabilization/`.
- Each successful job leaves project files clean and advances HEAD with a commit.
- `bash -n run-all.sh` passes.
- `bash -n run_all.sh` passes.
