# Korean-to-English sentence-level documentation audit pass 2

- Kind: `docs`
- Status values: `ToDo`, `Progress`, `Done`, `Fail`
- User-run command: `./run-all.sh` from this directory
- Default behavior: continue through all jobs until completion or failure
- Optional single-job mode: `RUN_ONE=1 ./run-all.sh`
- Handoff gate: uncommitted project files stop the workflow before the next job starts
- Commit gate: each successful job must pass review and create a focused commit
- Shared requirements: `.codex-jobs/ko-en-doc-coverage-pass2/workflow-requirements.md`
- Audit level: sentence, bullet, table-row, command, SQL, configuration, warning, version, attachment, and link level
- Required report: `PASS2_KO_EN_DOC_REVIEW_REPORT.md`

## Jobs

| ID | Status | Title | Goal |
| --- | --- | --- | --- |
| `P201` | `Done` | Baseline after J013 | Confirm J013 completion, git state, document counts, manifest validity, first-pass reports, and pass2 sentence-level audit boundary before editing product documentation. |
| `P202` | `Done` | Tech audit: installation core and database creation | Sentence-level audit Korean installation guide, quick install, troubleshooting, database creation, and configuration core sections against English arch targets; update English from Korean where needed. |
| `P203` | `Done` | Tech audit: OS platform and disk I/O setup | Sentence-level audit Korean Linux, Solaris, HPUX, AIX, and disk I/O setup documents against English arch targets; update English from Korean where needed. |
| `P204` | `Done` | Tech audit: operations failure startup resource utilities | Sentence-level audit Korean failure response, startup/shutdown, system resource sizing, OS utility, UNIX memory, and operation-related configuration sections against English arch targets; update English from Korean where needed. |
| `P205` | `Done` | Tech audit: monitoring queries | Sentence-level audit the Korean Altibase monitoring queries guide, including section IDs, SQL, meta tables, performance views, examples, and warnings against English arch targets; update English from Korean where needed. |
| `P206` | `Done` | Tech audit: CPU and memory analysis | Sentence-level audit Korean CPU overload and memory usage increase analysis guides against English arch targets; update English from Korean where needed. |
| `P207` | `Done` | Tech audit: replication configuration and constraints | Sentence-level audit Korean replication configuration and replication constraints guides against English arch targets; update English from Korean where needed. |
| `P208` | `Done` | Tech audit: backup recovery and failure recovery | Sentence-level audit Korean backup policy, failure response recovery sections, and startup/shutdown recovery-related sections against English arch targets; update English from Korean where needed. |
| `P209` | `Done` | Tech audit: C C++ precompiler APRE developer basics | Sentence-level audit Korean developer training, Precompiler, APRE Makefile, and APRE C/C++ upgrade documents against English arch targets; update English from Korean where needed. |
| `P210` | `Done` | Tech audit: Java ODBC ADO.NET PHP client APIs | Sentence-level audit Korean Java, unixODBC, Windows ODBC, ADO.NET, and PHP documents against English arch targets; update English from Korean where needed. |
| `P211` | `Done` | Tech audit: WAS and framework integrations | Sentence-level audit Korean TOMCAT, JEUS, JBoss, WebLogic, WebSphere, Spring, iBATIS, MyBatis, and Hibernate integration documents against English arch targets; update English from Korean where needed. |
| `P212` | `Done` | Tech audit: SQL tuning development and Oracle comparison | Sentence-level audit Korean development guide, SQL tuning guide, and Altibase Oracle comparison documents against English arch targets; update English from Korean where needed. |
| `P213` | `Done` | Tech audit: migration conversion and VC guides | Sentence-level audit Korean Oracle conversion, MSSQL conversion, Altibase version migration, Migration Center, VC 2008, and VC 2010 documents against English arch targets; update English from Korean where needed. |
| `P214` | `Done` | Tech audit: Docker GeoServer and SQuirrel tools | Sentence-level audit Korean Docker, GeoServer, and SQuirrel SQL Client documents against English arch targets; update English from Korean where needed. |
| `P215` | `Done` | FAQ audit: installation and operation core | Sentence-level audit Korean FAQ category 01 and core category 02 operation/security/user/session/client configuration documents against English FAQE targets; update English from Korean where needed. |
| `P216` | `Done` | FAQ audit: operation storage logs jobs and resources | Sentence-level audit remaining Korean FAQ category 02 operation/management documents for logs, tablespaces, files, jobs, resources, and operational changes against English FAQE targets; update English from Korean where needed. |
| `P217` | `Done` | FAQ audit: replication | Sentence-level audit Korean FAQ category 03 replication documents against English FAQE targets; update English from Korean where needed. |
| `P218` | `Done` | FAQ audit: backup SQL and stored procedures | Sentence-level audit Korean FAQ categories 04, 05, and 06 backup/recovery, SQL, and Stored Procedures documents against English FAQE targets; update English from Korean where needed. |
| `P219` | `Done` | FAQ audit: development API | Sentence-level audit Korean FAQ category 07 development/API documents against English FAQE targets; update English from Korean where needed. |
| `P220` | `Done` | FAQ audit: monitoring | Sentence-level audit Korean FAQ category 08 monitoring documents against English FAQE targets; update English from Korean where needed. |
| `P221` | `Done` | FAQ audit: error messages | Sentence-level audit Korean FAQ category 09 error message documents against English FAQE targets; update English from Korean where needed. |
| `P222` | `Done` | FAQ audit: utilities others general | Sentence-level audit Korean FAQ categories 11, 12, and 13 utility, others, and general documents against English FAQE targets; update English from Korean where needed. |
| `P223` | `Done` | Technical attachment source and export revalidation | Revalidate technical-document attachments, external source links, empty Markdown links, legacy # attachment labels, Error rendering macro, Unknown macro, and known export artifacts across audited arch documents; update English references and report risks. |
| `P224` | `Done` | FAQ attachment source English-only and export revalidation | Revalidate FAQ attachments, external source links, empty Markdown links, English-only FAQE classification candidates, legacy # labels, and export artifacts across audited FAQE documents; update English references and report risks. |
| `P225` | `Done` | LLM readiness and multilingual terminology review | Review J013 handoff structure, LLM package readiness, duplicate-handling rules, and multilingual terminology preservation rules without creating final consolidated LLM documents. |
| `P226` | `Done` | Final pass2 validation and report | Run final JSON, diff, document count, mapping, attachment/link, stale-pattern, and workflow checks; update the pass2 review report with changes, evidence, remaining risks, and readiness for LLM consolidation. |

## Resume Rules

- `Fail`: stop before starting later jobs.
- Dirty project files: stop before starting or advancing to another job.
- `Progress`: preserve interruption evidence, set the job back to `ToDo`, then rerun only when project files are clean.
- `Done`: skip.
- Nonzero `codex exec` exits leave the job as `Progress` by default; the next manual run stops if project files are dirty, or resets runtime state and retries when clean.

## Acceptance Checklist

- Each job has a matching prompt in `prompts/`.
- Each job has concrete acceptance criteria.
- Each prompt reads `workflow-requirements.md` before editing.
- Each job records checked documents, findings, changes or no-change evidence, verification, and remaining risk.
- Each successful job leaves project files clean and advances HEAD with a commit.
- `bash -n run-all.sh` and `bash -n run_all.sh` pass.
