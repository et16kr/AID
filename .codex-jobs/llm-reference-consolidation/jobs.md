# LLM Reference Consolidation

- Kind: `docs`
- Status values: `ToDo`, `Progress`, `Done`, `Fail`
- User-run command: `./run-all.sh` from this directory
- Default behavior: continue through all jobs until completion or failure
- Optional single-job mode: `RUN_ONE=1 ./run-all.sh`
- Handoff gate: uncommitted project files stop the workflow before the next job starts
- Commit gate: each successful job must pass review and create a focused commit
- Detailed source boundaries and output file names: `workflow-requirements.md`
- Shared prompt instructions appended at runtime: `prompt-addendum.md`
- Previous completed workflow scripts were intentionally removed from `.codex-jobs/` before creating this workflow.

## Jobs

| ID | Status | Title | Goal |
| --- | --- | --- | --- |
| `L001` | `ToDo` | Source readiness cleanup | Clean residual source issues before consolidation, especially real untranslated Korean in English auxiliary sources, and verify baseline counts. |
| `L002` | `ToDo` | Package scaffold and source index | Create the llm-reference package scaffold, source classification policy, and source index used by later jobs. |
| `L003` | `ToDo` | Installation upgrade platform reference | Build the installation, upgrade, database creation, platform setup, and Docker reference document. |
| `L004` | `ToDo` | Architecture storage concepts reference | Build the architecture, memory and disk DBMS concepts, storage, WAL, and disk I/O reference document. |
| `L005` | `ToDo` | Operation administration security reference | Build the operation, administration, startup shutdown, configuration, user, security, password, charset, and resource reference document. |
| `L006` | `ToDo` | Backup recovery reference | Build the backup policy, online cold logical incremental backup, recovery, log, and validation reference document. |
| `L007` | `ToDo` | Replication HA reference | Build the replication, HA, conflict, gap monitoring, constraints, and operational caution reference document. |
| `L008` | `ToDo` | Monitoring diagnostics reference | Build the monitoring queries, system views, OS utility, CPU overload, memory growth, and diagnostic collection reference document. |
| `L009` | `ToDo` | Troubleshooting error messages reference | Build the failure response, troubleshooting patterns, and error message reference document. |
| `L010` | `ToDo` | SQL performance tuning reference | Build the SQL tuning, optimizer, index, partition, query, and performance reference document. |
| `L011` | `ToDo` | Development client API reference | Build the development, precompiler, APRE, C/C++, Java, JDBC, ODBC, ADO.NET, PHP, and client API reference document. |
| `L012` | `ToDo` | Application framework integration reference | Build the Tomcat, JEUS, JBoss, WebLogic, WebSphere, Spring, iBATIS, MyBatis, and Hibernate integration reference document. |
| `L013` | `ToDo` | Migration conversion tools reference | Build the Oracle/MSSQL conversion, Altibase migration, Migration Center, GeoServer, SQuirrel, VC guides, and tool reference document. |
| `L014` | `ToDo` | FAQ integration and dedupe pass | Integrate Korean-source verified FAQ knowledge into the topic documents, reduce duplication, and keep source notes. |
| `L015` | `ToDo` | Terminology and multilingual preservation guide | Create the glossary and multilingual answer-stability rules for product names, commands, SQL, parameters, paths, and error codes. |
| `L016` | `ToDo` | Cross-reference consistency pass | Review all llm-reference documents for consistent headings, source classifications, links, attachment labels, and no unsupported claims. |
| `L017` | `ToDo` | Final validation and report | Run final validation checks and create a concise build report with coverage, risks, and verification evidence. |
| `L018` | `ToDo` | Final packaging review | Perform final diff review, check commits and clean handoff state, and ensure the package is ready for user review. |

## Resume Rules

- `Fail`: stop before starting later jobs.
- Dirty project files: stop before starting or advancing to another job.
- `Progress`: preserve interruption evidence, set the job back to `ToDo`, then rerun only when project files are clean.
- `Done`: skip.
- Nonzero `codex exec` exits leave the job as `Progress` by default; the next manual run stops if project files are dirty, or resets runtime state and retries when clean.

## Acceptance Checklist

- Each job has a matching prompt in `prompts/`.
- Each job has concrete acceptance criteria.
- `workflow-requirements.md` defines the job-specific output file, source paths, and acceptance criteria.
- `run-all.sh` appends `prompt-addendum.md` to each runtime prompt.
- Each successful job leaves project files clean and advances HEAD with a commit.
- `bash -n run-all.sh` passes.
