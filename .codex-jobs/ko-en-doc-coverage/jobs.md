# Korean-to-English complete documentation coverage

- Kind: `docs`
- Status values: `ToDo`, `Progress`, `Done`, `Fail`
- User-run command: `./run_all.sh` from this directory
- Compatibility command: `./run-all.sh` from this directory
- Default behavior: continue through all jobs until completion or failure
- Optional single-job mode: `RUN_ONE=1 ./run_all.sh`
- Handoff gate: uncommitted project files stop the workflow before the next job starts
- Commit gate: each successful job must pass review and create a focused commit
- Shared requirements: `.codex-jobs/ko-en-doc-coverage/workflow-requirements.md`

## Jobs

| ID | Status | Title | Goal |
| --- | --- | --- | --- |
| `J001` | `Done` | Baseline inventory and mapping | Confirm requirements, current git state, document counts, Korean-English mappings, FAQ category mappings, and attachment inventory before content review. |
| `J002` | `Done` | Technical docs: installation and platform setup | Compare Korean DOCK installation, platform setup, database creation, quick start, installation troubleshooting, and Linux/Unix setup documents against English arch documents, then update English from Korean where needed. |
| `J003` | `Done` | Technical docs: operations and administration | Compare Korean DOCK configuration, operation, startup/shutdown, system resource, memory, CPU, monitoring, and OS utility documents against English arch documents, then update English from Korean where needed. |
| `J004` | `Done` | Technical docs: replication, backup, and recovery | Compare Korean DOCK replication, replication constraints, backup policy, failure response, and recovery-related documents against English arch documents, then update English from Korean where needed. |
| `J005` | `ToDo` | Technical docs: development and API integrations | Compare Korean DOCK developer, precompiler, APRE, Java, ODBC, ADO.NET, Spring, iBATIS, MyBatis, Hibernate, PHP, WAS integration, and client tool documents against English arch documents, then update English from Korean where needed. |
| `J006` | `ToDo` | Technical docs: SQL, tuning, migration, conversion, and tools | Compare Korean DOCK development guide, SQL tuning, Oracle/MSSQL conversion, data migration, Docker, GeoServer, SQuirrel, VC guides, and Migration Center documents against English arch documents, then update English from Korean where needed. |
| `J007` | `ToDo` | FAQ docs: installation, operation, and management | Compare Korean faq categories 01 and 02 against the corresponding FAQE core categories, then update English from Korean where needed. |
| `J008` | `ToDo` | FAQ docs: replication, backup, SQL, stored procedures, and development API | Compare Korean faq categories 03, 04, 05, 06, and 07 against the corresponding FAQE core categories, then update English from Korean where needed. |
| `J009` | `ToDo` | FAQ docs: monitoring, error messages, utilities, others, and general | Compare Korean faq categories 08, 09, 11, 12, and 13 against the corresponding FAQE core categories, then update English from Korean where needed. |
| `J010` | `ToDo` | Attachment and source-link coverage | Recheck all Korean document-format attachment links and important source references against English counterparts; update English documents and manifest where needed. |
| `J011` | `ToDo` | English quality and LLM-readability pass | Review updated English documents for technical English quality, terminology consistency, LLM searchability, and preservation of non-translatable identifiers; make scoped improvements without changing meaning. |
| `J012` | `ToDo` | Final coverage validation and review report | Run final coverage checks, JSON/diff validation, document counts, and update the review report with all changes, remaining risks, and evidence. |
| `J013` | `ToDo` | LLM reference handoff package plan | Create or update the handoff plan for consolidating English documents into GPTs/Codex/LLM reference documents, including topic groups, source paths, and multilingual terminology rules. |

## Resume Rules

- `Fail`: stop before starting later jobs.
- Dirty project files: stop before starting or advancing to another job.
- `Progress`: preserve interruption evidence, set the job back to `ToDo`, then rerun only when project files are clean.
- `Done`: skip.
- Nonzero `codex exec` exits leave the job as `Progress` by default; the next manual run stops if project files are dirty, or resets runtime state and retries when clean.

## Acceptance Checklist

- Each job has a matching prompt in `prompts/`.
- Each job has concrete acceptance criteria.
- Each prompt reads the shared requirements before editing.
- Each successful job leaves project files clean and advances HEAD with a commit.
- `bash -n run-all.sh` and `bash -n run_all.sh` pass.
