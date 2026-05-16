# KO to EN Semantic Coverage Audit

- Kind: `docs`
- Status values: `ToDo`, `Progress`, `Done`, `Fail`
- User-run command: `./run-all.sh` from this directory
- Default behavior: continue through all jobs until completion or failure
- Optional single-job mode: `RUN_ONE=1 ./run-all.sh`
- Handoff gate: uncommitted project files stop the workflow before the next job starts
- Commit gate: each successful job must pass review and create a focused commit
- Shared requirements: `.codex-jobs/ko-en-semantic-coverage-audit/workflow-requirements.md`
- Runtime prompt addendum: `.codex-jobs/ko-en-semantic-coverage-audit/prompt-addendum.md`
- Audit standard: semantic-unit matrix coverage, not report-only review
- Final decision: exactly one of `COMPLETE` or `RECHECK_REQUIRED`

## Jobs

| ID | Status | Title | Goal |
| --- | --- | --- | --- |
| `S001` | `ToDo` | Audit method and baseline | Define semantic-unit coverage method, confirm current repository state, create evidence structure, and record the audit decision criteria. |
| `S002` | `ToDo` | Mapping inventory and unit matrix scaffold | Validate KO to EN document mappings, create the coverage matrix schema, and prepare per-job evidence files. |
| `S003` | `ToDo` | Tech installation configuration database | Semantic-unit audit configuration, database creation, installation, quick start, and installation troubleshooting technical documents. |
| `S004` | `ToDo` | Tech platform disk IO | Semantic-unit audit disk I/O, Solaris, HPUX, AIX, and Linux platform setup technical documents. |
| `S005` | `ToDo` | Tech operations startup resources | Semantic-unit audit failure response, startup shutdown, resource sizing, OS utility, UNIX memory, and operation configuration documents. |
| `S006` | `ToDo` | Tech monitoring queries | Semantic-unit audit the monitoring queries guide, including SQL IDs, system views, examples, and warnings. |
| `S007` | `ToDo` | Tech CPU memory diagnostics | Semantic-unit audit CPU overload and memory usage increase analysis guides. |
| `S008` | `ToDo` | Tech replication | Semantic-unit audit replication configuration and replication constraints technical documents. |
| `S009` | `ToDo` | Tech backup recovery | Semantic-unit audit backup policy, recovery, archive/noarchive, failure response, and startup recovery technical documents. |
| `S010` | `ToDo` | Tech C C++ APRE precompiler | Semantic-unit audit developer training, Precompiler, APRE Makefile, and APRE C/C++ upgrade documents. |
| `S011` | `ToDo` | Tech client APIs | Semantic-unit audit Java, unixODBC, Windows ODBC, ADO.NET, and PHP client API documents. |
| `S012` | `ToDo` | Tech WAS framework integration | Semantic-unit audit Tomcat, JEUS, JBoss, WebLogic, WebSphere, Spring, iBATIS, MyBatis, and Hibernate documents. |
| `S013` | `ToDo` | Tech development SQL tuning comparison | Semantic-unit audit Altibase Development Guide, SQL Tuning Guide, and Altibase/Oracle comparison documents. |
| `S014` | `ToDo` | Tech migration conversion VC | Semantic-unit audit Oracle conversion, MSSQL conversion, version migration, Migration Center, VC 2008, and VC 2010 documents. |
| `S015` | `ToDo` | Tech Docker GeoServer SQuirrel | Semantic-unit audit Docker, GeoServer, and SQuirrel SQL Client technical documents. |
| `S016` | `ToDo` | Technical attachments and source links | Verify technical document attachments, legacy labels, source links, and external references across all audited technical mappings. |
| `S017` | `ToDo` | FAQ installation patch upgrade | Semantic-unit audit FAQ category 01 against English core FAQ targets. |
| `S018` | `ToDo` | FAQ operation core | Semantic-unit audit FAQ category 02 operation core topics such as security, users, sessions, clients, startup, and configuration. |
| `S019` | `ToDo` | FAQ operation storage resources | Semantic-unit audit remaining FAQ category 02 topics such as logs, tablespaces, files, JOBs, resources, charset, and operational changes. |
| `S020` | `ToDo` | FAQ replication | Semantic-unit audit FAQ category 03 replication against English core FAQ targets. |
| `S021` | `ToDo` | FAQ backup SQL stored procedures | Semantic-unit audit FAQ categories 04, 05, and 06 against English core FAQ targets. |
| `S022` | `ToDo` | FAQ development API | Semantic-unit audit FAQ category 07 development and API against English core FAQ targets. |
| `S023` | `ToDo` | FAQ monitoring | Semantic-unit audit FAQ category 08 monitoring against English core FAQ targets. |
| `S024` | `ToDo` | FAQ error messages | Semantic-unit audit FAQ category 09 error messages against English core FAQ targets. |
| `S025` | `ToDo` | FAQ utilities others general | Semantic-unit audit FAQ categories 11, 12, and 13 against English core FAQ targets. |
| `S026` | `ToDo` | FAQ attachments English-only classification | Verify FAQ attachments, legacy labels, source links, export artifacts, and English-only FAQE classification boundaries. |
| `S027` | `ToDo` | Unresolved coverage closure | Merge all coverage matrices, fix remaining missing source coverage, and drive unresolved semantic differences to zero or explicit recheck risks. |
| `S028` | `ToDo` | Source stabilization after coverage fixes | Run source stability checks after all coverage fixes: manifest, counts, residual Korean classification, links, macro artifacts, and metadata. |
| `S029` | `ToDo` | Independent matrix challenge review | Challenge the coverage matrix by sampling and inverse-searching KO units marked covered to find false positives or weak evidence. |
| `S030` | `ToDo` | Final semantic coverage decision | Create the final semantic coverage report and decide exactly one outcome: COMPLETE or RECHECK_REQUIRED. |

## Resume Rules

- `Fail`: stop before starting later jobs.
- Dirty project files: stop before starting or advancing to another job.
- `Progress`: preserve interruption evidence, set the job back to `ToDo`, then rerun only when project files are clean.
- `Done`: skip.
- Nonzero `codex exec` exits leave the job as `Progress` by default; the next manual run stops if project files are dirty, or resets runtime state and retries when clean.

## Acceptance Checklist

- Each job has a matching prompt in `prompts/`.
- Each job has concrete acceptance criteria.
- Each prompt receives `prompt-addendum.md` at runtime.
- Each audit job writes a semantic coverage matrix under `semantic-coverage/matrices/`.
- Each audit job writes a note under `semantic-coverage/notes/`.
- The final report is `KO_EN_SEMANTIC_COVERAGE_REPORT.md`.
- Previous J/P reports may be used for orientation, but current jobs must inspect source files directly.
- Each successful job leaves project files clean and advances HEAD with a commit.
- `bash -n run-all.sh` passes.
