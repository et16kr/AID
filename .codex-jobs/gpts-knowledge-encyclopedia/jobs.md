# GPTs knowledge encyclopedia packaging

- Kind: `mixed`
- Status values: `ToDo`, `Progress`, `Done`, `Fail`
- User-run command: `./run-all.sh` from this directory
- Codex workdir: repository root by default, override with `CODEX_WORKDIR=/path`
- Default behavior: continue through all jobs until completion or failure
- Optional single-job mode: `RUN_ONE=1 ./run-all.sh`
- Handoff gate: uncommitted project files stop the workflow before the next job starts
- Commit gate: each successful job must pass review and create a focused commit
- Status gate: after each successful job, `jobs.tsv` status is amended into that job commit

## Completion Standard

This workflow is complete only when the repository contains GPTs upload artifacts that can be attached without the original source trees.

Required customer-facing upload file:

- `llm-reference/gpts-upload/Altibase_GPT_Knowledge_Encyclopedia.md`

Optional internal-review upload file:

- `llm-reference/gpts-upload/Altibase_GPT_Knowledge_Audit.md`

The required encyclopedia file must include the full generated `llm-reference` topic corpus, preserve exact identifiers and source-path traceability, and state clearly that original `arch/`, `FAQE/`, `DOCK/`, and `faq/` files are not GPT answer-time dependencies.

## Jobs

| ID | Status | Title | Goal |
| --- | --- | --- | --- |
| `G001` | `ToDo` | GPTs upload requirements and corpus gate | Confirm the GPTs-only answer target, verify the current llm-reference corpus is the source boundary, and create the upload workflow requirements. |
| `G002` | `ToDo` | Bundle generator and encyclopedia artifact | Implement the repeatable bundle generator and create the one-file GPTs encyclopedia from the full llm-reference topic corpus. |
| `G003` | `ToDo` | GPT retrieval hardening and answer routing | Improve the encyclopedia bundle for GPTs retrieval with front matter, routing index, exact-identifier guidance, and self-contained answer rules without removing source traceability. |
| `G004` | `ToDo` | Optional audit bundle and upload handoff | Create the optional second audit bundle plus upload instructions, manifest, and GPT configuration text for customer-facing use. |
| `G005` | `ToDo` | Final GPTs readiness validation | Run final validation proving the generated 1-2 files are complete, self-contained, source-traceable, and ready for GPTs upload. |

## Resume Rules

- `Fail`: stop before starting later jobs.
- Dirty project files: stop before starting or advancing to another job.
- `Progress`: preserve interruption evidence, set the job back to `ToDo`, then rerun only when project files are clean.
- `Done`: skip.
- Nonzero `codex exec` exits leave the job as `Progress` by default; the next manual run stops if project files are dirty, or resets runtime state and retries when clean.

## Acceptance Checklist

- Each job has a matching prompt in `prompts/`.
- Each job has concrete acceptance criteria.
- Each successful job leaves project files clean and advances HEAD with a commit.
- `bash -n run-all.sh` passes.
- `bash -n run_all.sh` passes.
- `workflow-requirements.md` defines required outputs, source boundary, bundle policy, and final readiness criteria.
- The final report decision is `GPTS_UPLOAD_READY` unless a real blocker is recorded as `GPTS_RECHECK_REQUIRED`.
