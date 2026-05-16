# Exhaustive LLM Reference Consolidation

- Kind: `docs`
- Status values: `ToDo`, `Progress`, `Done`, `Fail`
- User-run command: `./run-all.sh` from this directory
- Default behavior: continue through all jobs until completion or failure
- Optional single-job mode: `RUN_ONE=1 ./run-all.sh`
- Handoff gate: uncommitted project files outside `.codex-jobs/` stop the workflow before the next job starts
- Commit gate: each successful job must pass review and create a focused commit
- Status gate: each successful job's `jobs.tsv` status is amended into that job commit so the final handoff can be clean
- Definition gate: workflow definition files must be committed before execution starts; runtime status-only changes in `jobs.tsv` are allowed
- Detailed source boundaries and output file names: `workflow-requirements.md`
- Shared prompt instructions appended at runtime: `prompt-addendum.md`

## Completion Standard

This workflow is designed around full source answerability, not a FAQ-only summary.

The final `llm-reference/` package must let an LLM answer questions grounded in every original English source document under `arch/Home` and `FAQE/Home`. The package may deduplicate repeated material, but every unique technical semantic unit must be covered in a topic document or explicitly classified in coverage evidence.

## Active Jobs

| ID | Status | Title | Goal |
| --- | --- | --- | --- |
| `R001` | `ToDo` | Interrupted run summary and phase gates | Preserve the interrupted L001 state, confirm Phase 2 readiness, and start the exhaustive Phase 3 evidence trail. |
| `R002` | `ToDo` | Package scaffold and exhaustive coverage ledgers | Create the llm-reference scaffold and initialize source inventory, coverage, attachment, answerability, and risk ledgers. |
| `R003` | `ToDo` | Full source inventory and source-to-topic map | Inventory every arch/Home and FAQE/Home Markdown source and map each source to a topic document and owner job. |
| `R004` | `ToDo` | Installation patch upgrade database creation | Build exhaustive installation, patch, upgrade, database creation, startup validation, and installation FAQ coverage. |
| `R005` | `ToDo` | Platform setup OS prerequisites Docker | Build exhaustive Linux, Solaris, HPUX, AIX, platform prerequisite, and Docker coverage. |
| `R006` | `ToDo` | Architecture storage disk concepts | Build exhaustive architecture, storage, WAL, checkpoint, disk configuration, and general concept coverage. |
| `R007` | `ToDo` | Configuration startup capacity OS utilities | Build exhaustive configuration, startup, shutdown, capacity sizing, OS utility, and memory management coverage. |
| `R008` | `ToDo` | Administration security sessions charset FAQ | Build exhaustive administration, security, session, client, charset, JOB, and operational FAQ coverage. |
| `R009` | `ToDo` | Backup recovery failure response | Build exhaustive backup, recovery, failure response, aexport, iloader, and validation coverage. |
| `R010` | `ToDo` | Replication and HA | Build exhaustive replication setup, constraints, HA, conflict, gap, GIVE-UP, and replication FAQ coverage. |
| `R011` | `ToDo` | Monitoring queries diagnostics | Build exhaustive monitoring SQL, system view, performance view, tablespace, session, lock, and monitoring FAQ coverage. |
| `R012` | `ToDo` | CPU memory OS evidence diagnostics | Build exhaustive CPU overload, memory growth, OS evidence, dump, log, and diagnostic decision coverage. |
| `R013` | `ToDo` | Troubleshooting Korean-source errors | Build exhaustive Korean-source-verified troubleshooting and error-message coverage. |
| `R014` | `ToDo` | English-only error troubleshooting catalog | Integrate or index English-only error and troubleshooting sources with explicit source labels. |
| `R015` | `ToDo` | SQL stored procedures query behavior | Build exhaustive SQL, stored procedure, query behavior, examples, limits, and FAQ coverage. |
| `R016` | `ToDo` | Performance tuning optimizer indexes | Build exhaustive tuning, optimizer, index, partitioning, HPT, and performance diagnostic coverage. |
| `R017` | `ToDo` | APRE precompiler C C++ development | Build exhaustive APRE, SES, precompiler, C/C++, Makefile, and sample-code coverage. |
| `R018` | `ToDo` | Java JDBC ODBC ADO.NET PHP API | Build exhaustive Java, JDBC, ODBC, unixODBC, ADO.NET, PHP, driver, connection, and API FAQ coverage. |
| `R019` | `ToDo` | WAS and framework integration | Build exhaustive Tomcat, JEUS, JBoss, WebLogic, WebSphere, Spring, iBATIS, MyBatis, and Hibernate coverage. |
| `R020` | `ToDo` | Migration conversion tools | Build exhaustive migration, Oracle/MSSQL conversion, Migration Center, VC, GeoServer, SQuirrel, and utility coverage. |
| `R021` | `ToDo` | English-only auxiliary corpus integration | Integrate or index English-only architecture, administration, performance, replication, and troubleshooting auxiliary sources. |
| `R022` | `ToDo` | FAQ exhaustive reconciliation | Reconcile every Korean-source-verified FAQE source against topic documents and coverage evidence. |
| `R023` | `ToDo` | Attachments diagrams external references | Register every attachment, legacy label, unavailable diagram, and external reference with preservation status. |
| `R024` | `ToDo` | Terminology multilingual preservation | Create the terminology and multilingual answer-stability guide for exact identifiers and translation boundaries. |
| `R025` | `ToDo` | Source semantic-unit coverage reconciliation | Reconcile source inventory, semantic-unit coverage, target sections, and accepted limitations. |
| `R026` | `ToDo` | Source-derived answerability backtest | Create source-derived answerability tests and fix or mark any not-answerable coverage. |
| `R027` | `ToDo` | Cross-reference unsupported-claim review | Normalize cross references, labels, links, terminology, and remove unsupported claims. |
| `R028` | `ToDo` | Final validation build report handoff | Run final validation, create the build report, and create the handoff document. |

## Resume Rules

- `Fail`: stop before starting later jobs.
- Dirty project files: stop before starting or advancing to another job.
- `Progress`: preserve interruption evidence, set the job back to `ToDo`, then rerun only when project files are clean.
- `Done`: skip.
- Nonzero `codex exec` exits leave the job as `Progress` by default; the next manual run stops if project files are dirty, or resets runtime state and retries when clean.

## Acceptance Checklist

- `run-all.sh` launches `codex exec` from the repository root, even when the user starts it from `.codex-jobs/llm-reference-consolidation/`.
- `run-all.sh` refuses uncommitted workflow definition changes while allowing runtime `jobs.tsv` status changes.
- `run-all.sh` records each `Done` status by amending the successful job commit.
- `workflow-requirements.md` defines exhaustive source coverage, semantic-unit evidence, answerability backtesting, output files, and final decision rules.
- Every job in `jobs.tsv` is covered by the shared prompt and by job-specific requirements in `workflow-requirements.md`.
- Phase 3 does not complete unless coverage evidence includes every `arch/Home` and `FAQE/Home` Markdown source.
- Final validation has zero unresolved `recheck_required` coverage or answerability rows unless the final decision is `RECHECK_REQUIRED`.
- `bash -n run-all.sh` passes.
- `bash -n run_all.sh` passes.
