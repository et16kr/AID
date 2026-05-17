# Monitoring and Diagnostics

## Source paths

R011 source paths covered in this revision:

- `arch/Home/Altibase Monitoring Queries Guide__14058229.md`
- `arch/Home/Altibase Monitoring Queries Guide/1. Altibase Server Monitoring Overview__14058232.md`
- `arch/Home/Altibase Monitoring Queries Guide/2. Altibase Meta Table and Performance View Overview/1. Main meta table and performance views related to session, query, transaction, lock, service thread, and memory DB GC__14058240.md`
- `arch/Home/Altibase Monitoring Queries Guide/2. Altibase Meta Table and Performance View Overview/2. Major Meta Tables and Performance Views related to tablespace, table, column, index, and constraint__14058242.md`
- `arch/Home/Altibase Monitoring Queries Guide/2. Altibase Meta Table and Performance View Overview/3. Main Performance View related to Statistical Information__14058244.md`
- `arch/Home/Altibase Monitoring Queries Guide/2. Altibase Meta Table and Performance View Overview/4. Main Metal Tables and Performance Views Related to Replication__14058248.md`
- `arch/Home/Altibase Monitoring Queries Guide/2. Altibase Meta Table and Performance View Overview/5. Whether Users can Access the Tablespace, System_Object Privileges, PSM, View related Meta Tables and Peformance Views__14058250.md`
- `arch/Home/Altibase Monitoring Queries Guide/2. Altibase Meta Table and Performance View Overview__14058238.md`
- `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/1. Session__14058254.md`
- `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/10. Object__14058276.md`
- `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/11. Privileges__14058278.md`
- `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/12. Constraints__14058280.md`
- `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/13. Replication__14058282.md`
- `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/2. Statement__14058256.md`
- `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/3. Service Thread__14058260.md`
- `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/4. Transaction & Lock__14058264.md`
- `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/5. Redo Logfile__14058266.md`
- `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/6. GC (Garbage Collector)__14058268.md`
- `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/7. Memory__14058270.md`
- `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/8. Tablespace (TBS)__14058272.md`
- `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/9. Disk Buffer__14058274.md`
- `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries__14058252.md`
- `FAQE/Home/08. Monitoring/Disk table and index usage/ALTIBASE HDB 4.3.9.x__16876229.md`
- `FAQE/Home/08. Monitoring/Disk table and index usage/ALTIBASE HDB 5.1.5.x__16876234.md`
- `FAQE/Home/08. Monitoring/Disk table and index usage/ALTIBASE HDB 5.3.x, 5.5.1, 6.1.1, 6.3.1__16876240.md`
- `FAQE/Home/08. Monitoring/Disk table and index usage__16876226.md`
- `FAQE/Home/08. Monitoring/Disk tablespace usage/ALTIBASE HDB 4.3.9__16876249.md`
- `FAQE/Home/08. Monitoring/Disk tablespace usage/ALTIBASE HDB 5.1.5__16876251.md`
- `FAQE/Home/08. Monitoring/Disk tablespace usage/ALTIBASE HDB 5.3.3, 5.3.5__16876253.md`
- `FAQE/Home/08. Monitoring/Disk tablespace usage/ALTIBASE HDB 5.5.1, 6.1.1, 6.3.1__16876255.md`
- `FAQE/Home/08. Monitoring/How to determine which queries are being rolled back__16876296.md`
- `FAQE/Home/08. Monitoring/How to log queries performed in Altibase (altiProfile)__22642959.md`
- `FAQE/Home/08. Monitoring/How to set up and execute altimon__16876266.md`
- `FAQE/Home/08. Monitoring/Lock related properties__16876204.md`
- `FAQE/Home/08. Monitoring/Memory table and index usage__16876259.md`
- `FAQE/Home/08. Monitoring/Memory tablespace usage/ALTIBASE HDB 5.5.1, 6.1.1, 6.3.1__16876263.md`
- `FAQE/Home/08. Monitoring/Monitoring Tools for Windows__16876220.md`
- `FAQE/Home/08. Monitoring/System information by OS__16876206.md`
- `FAQE/Home/08. Monitoring/Table_Column Definition__22642961.md`
- `FAQE/Home/08. Monitoring/Undo Tablespace/Monitoring method when undo tablespace usage increases__22642963.md`
- `FAQE/Home/08. Monitoring/Undo Tablespace/Undo tablespace usage__22642965.md`

## Source coverage notes

This document covers R011: monitoring SQL, system and performance views, session and statement checks, lock and transaction checks, redo log checks, GC checks, memory and tablespace checks, object metadata, privileges, constraints, replication monitoring, `altimon`, `altiProfile`, OS-system evidence examples, and every Korean-source-verified monitoring FAQ variant under `FAQE/Home/08. Monitoring/**`.

The architecture monitoring-query guide sources are classified as `Link-validated Korean-source-verified` in `llm-reference/coverage/source-inventory.tsv`. Most monitoring FAQ sources are `Korean-source-verified`; `FAQE/Home/08. Monitoring/Monitoring Tools for Windows__16876220.md` and `FAQE/Home/08. Monitoring/How to set up and execute altimon__16876266.md` are `Link-validated Korean-source-verified` because Phase 2 validated their links and attachments.

No English-only auxiliary material is used in this R011 revision. The source set includes one preserved monitoring-guide PDF, `altimon_for_windows.zip`, `ALTIMON_USER_GUIDE.pdf`, several non-document-format `altimon` support archives/configuration files, Windows `.bat` and `.vbs` helper files, and embedded PNG/JPEG diagrams or screenshots. These are recorded in `llm-reference/coverage/attachment-diagram-register.tsv` without inventing missing URLs. The legacy `ALTIMON USER GUIDE` hash-only label is preserved as a source limitation with `no downloadable URL in source`.

Because the source contains many exact SQL variants, this topic keeps a curated explanation first and then preserves every source code block in the `Exact SQL, Command, and Configuration Catalog` section. Use the catalog when an answer needs an exact statement, command, profile output format, or version-specific query variant.

## Scope and audience

Use this document to answer DBA, SRE, support, and LLM questions about Altibase monitoring and diagnostics: what to monitor, which `SYSTEM_` meta tables and `V$`/`X$` views to query, which source query ID to use, how to trace SQL with `altiProfile`, how to configure and run `altimon`, how to inspect locks, rollback, undo growth, tablespace usage, object metadata, OS evidence, and replication status.

When answering in another language, keep product names, commands, SQL, meta table names, performance view names, properties, file paths, query IDs, version strings, attachment filenames, and source URLs exactly as written.

## Key facts

Altibase monitoring sources classify DBMS monitoring into three categories:

| Category | Meaning |
| --- | --- |
| Internal Monitoring | Query Altibase data dictionary objects from inside the DBMS. The monitoring-query guide focuses on this category. |
| External Monitoring | Use OS commands and utilities outside the DBMS. |
| Trace Log Monitoring | Inspect trace logs recorded by the DBMS. |

Altibase data dictionary objects are split into meta tables and performance views.

| Object type | Source rule |
| --- | --- |
| Meta table | Created automatically at database creation time, owned by the system administrator user `SYSTEM_`, and normally queried with `SELECT`. |
| Performance view | Returns Altibase internal status at `SELECT` time, is read-only, and usually uses the `V$` prefix. Some FAQ queries also use `X$` fixed tables such as `X$SEGMENT` and `X$TEMPTABLE_STATS`. |

ERD diagrams in the source treat performance views like tables for readability. The source warns that columns with the same attribute can have different names in meta tables and performance views, and that columns, meta tables, and performance views can be added, changed, or deleted by Altibase version.

Terms that must stay stable in answers:

| Term | Source meaning |
| --- | --- |
| Session | A user's access unit connected to the Altibase server; one user can have multiple sessions. |
| Statement/query | Each SQL executed in a transaction. The source uses SQL statement, query, and query statement with the same practical meaning and normalizes on query. |
| Memory DB GC / GC / Ager | Thread that deletes pre-change records maintained for MVCC after commit. Since the disk DB MVCC method changed from Altibase 5.3.3, disk DB GC disappeared and memory DB GC remains. |

`TIMED_STATISTICS` is central to query and profile diagnostics. Query execution statistics in `V$STATEMENT` are updated only when `TIMED_STATISTICS` is enabled (`1`); the source states the default is disabled (`0`). `altiProfile` also requires `TIMED_STATISTICS = 1` to display execution time correctly.

Check the property with:

```sql
SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME = 'TIMED_STATISTICS';
```

Enable it for statement diagnostics with:

```sql
ALTER SYSTEM SET TIMED_STATISTICS=1;
```

The primary meta tables and performance views used by the monitoring-query guide are:

| Area | Objects |
| --- | --- |
| Sessions, statements, transactions, locks, service thread, GC | `SYS_USERS_`, `SYS_TABLES_`, `V$SESSION`, `V$STATEMENT`, `V$SQLTEXT`, `V$PLANTEXT`, `V$SERVICE_THREAD`, `V$TRANSACTION`, `V$MEMGC`, `V$LOCK`, `V$LOCK_WAIT`, `V$LOCK_STATEMENT` |
| Tablespaces, tables, columns, indexes, constraints | `SYS_COLUMNS_`, `SYS_CONSTRAINTS_`, `SYS_CONSTRAINT_COLUMNS`, `SYS_INDICES_`, `V$TABLESPACES`, `V$MEM_TABLESPACES`, `V$DATAFILES`, `V$SEGMENT`, `V$MEMTBL_INFO`, `V$DISKTBL_INFO`, `V$INDEX` |
| Statistics and waits | `v$system_wait_class`, `v$system_event`, `v$session_event`, `v$session_wait`, `v$sysstat`, `v$sesstat`, `v$filestat`, `v$memstat`, `v$buffpool_stat`, `v$lfg` |
| Replication | `SYS_REPLICATIONS_`, `SYS_REPL_HOSTS_`, `SYS_REPL_ITEMS_`, `V$REPSENDER`, `V$REPGAP`, `V$REPRECEIVER`, `V$REPSENDER_TRANSTBL`, `V$REPRECEIVER_TRANSTBL` |
| Tablespace access, privileges, PSM, views | `SYS_TBS_USERS_`, `SYS_PRIVILEGES_`, `SYS_GRANT_SYSTEM_`, `SYS_GRANT_OBJECT_`, `SYS_VIEWS_`, `SYS_VIEW_PARSE_`, `SYS_PROCEDURES_`, `SYS_PROC_PARSE_` |

`V$STATEMENT` is session-related and keeps one directly executed query and multiple prepared queries per session; rows disappear when the session ends. The query text in `V$STATEMENT` is limited to 16 KB. Use `V$SQLTEXT` for full query text and `V$PLANTEXT` for execution plans.

`V$TRANSACTION` is the main current-transaction view and is a primary lock-monitoring source. Replication transactions also use `V$TRANSACTION`, `V$LOCK`, and `V$LOCK_WAIT`, but they do not have session numbers or query numbers. Use `V$REPSENDER_TRANSTBL` and `V$REPRECEIVER_TRANSTBL` to map corresponding transactions on replication peer servers.

`V$LFG.LF_PREPARE_WAIT_COUNT` is the cumulative count of service-thread waits caused by the next redo log file not being ready at redo log switch time. If it is large, increase `PREPARE_LOG_FILE_COUNT` and restart Altibase so enough redo log files are prepared in advance.

## Monitoring Query ID Catalog

The source query IDs are preserved as stable lookup labels. Use the exact SQL in the catalog section when composing operational answers.

| ID | Monitoring area | Source heading | Source path |
| --- | --- | --- | --- |
| `SS01` | session | Total Number of Sessions | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/1. Session__14058254.md` |
| `SS02` | session | Session Information | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/1. Session__14058254.md` |
| `SS03` | session | Session Information Connected With SYSDBA Authority | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/1. Session__14058254.md` |
| `OB01` | database objects | Memory Table Usage | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/10. Object__14058276.md` |
| `OB02` | database objects | Queue | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/10. Object__14058276.md` |
| `OB03` | database objects | Memory Table with Low Efficiency | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/10. Object__14058276.md` |
| `OB04` | database objects | Memory Index and Queue Index Usage | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/10. Object__14058276.md` |
| `OB05` | database objects | Disk Table | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/10. Object__14058276.md` |
| `OB06` | database objects | Disk Index Usage | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/10. Object__14058276.md` |
| `OB07` | database objects | Partition Table Information | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/10. Object__14058276.md` |
| `OB08` | database objects | Sequence | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/10. Object__14058276.md` |
| `OB09` | database objects | Synonym | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/10. Object__14058276.md` |
| `OB10` | database objects | PSM | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/10. Object__14058276.md` |
| `OB11` | database objects | PSM Creation Statement | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/10. Object__14058276.md` |
| `OB12` | database objects | View | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/10. Object__14058276.md` |
| `OB13` | database objects | View Creation Statement | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/10. Object__14058276.md` |
| `OB14` | database objects | Package | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/10. Object__14058276.md` |
| `OB15` | database objects | Package Subprogram | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/10. Object__14058276.md` |
| `OB16` | database objects | Package Creation Statement | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/10. Object__14058276.md` |
| `OB17` | database objects | Trigger | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/10. Object__14058276.md` |
| `OB18` | database objects | Job | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/10. Object__14058276.md` |
| `OB19` | database objects | Database User | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/10. Object__14058276.md` |
| `OB20` | database objects | Tablespace List | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/10. Object__14058276.md` |
| `PV01` | privileges and roles | System Privilege | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/11. Privileges__14058278.md` |
| `PV02` | privileges and roles | Object Privilege | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/11. Privileges__14058278.md` |
| `PV03` | privileges and roles | Role Creation Information | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/11. Privileges__14058278.md` |
| `PV04` | privileges and roles | User Information Granted a Role | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/11. Privileges__14058278.md` |
| `PV05` | privileges and roles | System and Object Privilege Types | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/11. Privileges__14058278.md` |
| `CT01` | constraints and indexes | Full List of Constraints | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/12. Constraints__14058280.md` |
| `CT02` | constraints and indexes | List of Constraints, Tables, and Indexes Related to PK, FK, and UNIQUE | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/12. Constraints__14058280.md` |
| `CT03` | constraints and indexes | Composite Index Column Configuration List | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/12. Constraints__14058280.md` |
| `CT04` | constraints and indexes | Index Information Summary | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/12. Constraints__14058280.md` |
| `RP01` | replication monitoring | Replication Sender Information | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/13. Replication__14058282.md` |
| `RP02` | replication monitoring | Replication Receiver Information | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/13. Replication__14058282.md` |
| `RP03` | replication monitoring | Replication Gap | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/13. Replication__14058282.md` |
| `RP04` | replication monitoring | Overall Status of Replication | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/13. Replication__14058282.md` |
| `RP05` | replication monitoring | Measure Accumulated Redo Log Files Due to Replication Delay | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/13. Replication__14058282.md` |
| `RP06` | replication monitoring | List of Tables to be Replicated | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/13. Replication__14058282.md` |
| `ST01` | statement and query execution | Total Number of Queries | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/2. Statement__14058256.md` |
| `ST02` | statement and query execution | Query Information | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/2. Statement__14058256.md` |
| `ST03` | statement and query execution | Number of Queries Currently Being Executed | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/2. Statement__14058256.md` |
| `ST04` | statement and query execution | Query Information Currently Being Executed | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/2. Statement__14058256.md` |
| `ST05` | statement and query execution | Long-running Query Execution Information | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/2. Statement__14058256.md` |
| `ST06` | statement and query execution | Last Query Information of DML Transaction That is Executed for a Long Time | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/2. Statement__14058256.md` |
| `ST07` | statement and query execution | Full Scan Query Information | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/2. Statement__14058256.md` |
| `ST08` | statement and query execution | Full Scan Query Count Statistics | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/2. Statement__14058256.md` |
| `ST09` | statement and query execution | Query List by Session | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/2. Statement__14058256.md` |
| `ST10` | statement and query execution | Number of Statements Generated per Session | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/2. Statement__14058256.md` |
| `SV01` | service thread | Service Thread Status | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/3. Service Thread__14058260.md` |
| `SV02` | service thread | Check Service Thread Contention | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/3. Service Thread__14058260.md` |
| `TL01` | transaction and lock | Transaction and Lock Information | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/4. Transaction & Lock__14058264.md` |
| `LO01` | redo logfile | Redo Log File Information | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/5. Redo Logfile__14058266.md` |
| `LO02` | redo logfile | Cumulative Number of Waits for Redo Log File Prepare | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/5. Redo Logfile__14058266.md` |
| `GC01` | memory DB garbage collection | Memory DB GC Gap | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/6. GC (Garbage Collector)__14058268.md` |
| `GC02` | memory DB garbage collection | Query Being Executed in a Transaction Where the Memory DB GC Is Waiting | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/6. GC (Garbage Collector)__14058268.md` |
| `MS01` | memory usage | Altibase Memory Usage | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/7. Memory__14058270.md` |
| `MS02` | memory usage | Total Memory Usage of Altibase | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/7. Memory__14058270.md` |
| `TS01` | tablespace and datafile | Memory Tablespace Usage | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/8. Tablespace (TBS)__14058272.md` |
| `TS02` | tablespace and datafile | Total Memory Tablespace Usage | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/8. Tablespace (TBS)__14058272.md` |
| `TS03` | tablespace and datafile | Disk Tablespace Usage | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/8. Tablespace (TBS)__14058272.md` |
| `TS04` | tablespace and datafile | Disk Undo Tablespace Usage | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/8. Tablespace (TBS)__14058272.md` |
| `TS05` | tablespace and datafile | Undo Tablespace Usage by Transaction | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/8. Tablespace (TBS)__14058272.md` |
| `TS06` | tablespace and datafile | Total Tablespace Usage | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/8. Tablespace (TBS)__14058272.md` |
| `TS07` | tablespace and datafile | Memory Tablespace Data File Checkpoint Path | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/8. Tablespace (TBS)__14058272.md` |
| `TS08` | tablespace and datafile | Memory Tablespace Data File | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/8. Tablespace (TBS)__14058272.md` |
| `TS09` | tablespace and datafile | Disk Tablespace Data File | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/8. Tablespace (TBS)__14058272.md` |
| `TS10` | tablespace and datafile | I/O Per Disk Tablespace Data File | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/8. Tablespace (TBS)__14058272.md` |
| `TS11` | tablespace and datafile | Single Page Read I/O per Disk Tablespace Data File | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/8. Tablespace (TBS)__14058272.md` |
| `TS12` | tablespace and datafile | Temporary Tablespace Usage | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/8. Tablespace (TBS)__14058272.md` |
| `TS13` | tablespace and datafile | Temporary Tablespace Usage by Transaction | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/8. Tablespace (TBS)__14058272.md` |
| `TS14` | tablespace and datafile | Overall Tablespace Status | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/8. Tablespace (TBS)__14058272.md` |
| `DB01` | disk buffer | Disk Buffer Hit Ratio | `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/9. Disk Buffer__14058274.md` |

## Procedures

### Choose the monitoring path

1. For live DBMS internals, query the data dictionary with the query IDs in this document.
2. For OS evidence, use the OS-specific command examples from `System information by OS`.
3. For executed SQL trace details, enable `TIMED_STATISTICS` and `QUERY_PROF_FLAG`, then convert profile files with `altiProfile`.
4. For periodic monitoring, configure `altimon` or the Windows monitoring batch files, then add custom monitoring queries to the provided SQL scripts.
5. For a lock or undo emergency, identify the responsible session/transaction before closing a session or killing a client process.

### Start and stop SQL profiling with altiProfile

Start profiling in iSQL:

```sql
ALTER SYSTEM SET TIMED_STATISTICS = 1;
ALTER SYSTEM SET QUERY_PROF_FLAG = value;
```

Stop profiling in iSQL:

```sql
ALTER SYSTEM SET QUERY_PROF_FLAG = 0;
ALTER SYSTEM SET TIMED_STATISTICS = 0;
```

Profile files are created by default under `$ALTIBASE_HOME/trc` with a pattern such as `$ALTIBASE_HOME/trc/alti#timestamp-#sequence.prof`. Convert a single file or multiple files with:

```bash
altiProfile alti-#timestamp-#sequence.prof > #sequence.out
altiProfile *.prof > #sequence.out
```

Use `altiProfile -stat query` or `altiProfile -stat session` to produce `.txt` and `.csv` statistics for identifying SQL statements that may need tuning:

```bash
altiProfile -stat query *.prof > #sequence.out
altiProfile -stat session *.prof > #sequence.out
```

`QUERY_PROF_FLAG` values are additive:

| Value | Output label | Meaning |
| ---: | --- | --- |
| `0` | none | Do not record; default. |
| `1` | `[STATEMENT]` | Executed SQL, execution time, execution info, index access, disk access. Requires `TIMED_STATISTICS=1` for execution time. |
| `2` | `[BIND]` | Bind parameter values for prepared SQL, when binding exists. |
| `4` | `[PLAN]` | Execution plan for each executed SQL statement. |
| `8` | `[SESSION STAT]` | Session information every 3 seconds, equivalent to `SELECT * FROM v$sesstat ORDER BY sid, seqnum`. |
| `16` | `[SYSTEM STAT]` | System information every 3 seconds, equivalent to `SELECT * FROM v$sysstat ORDER BY seqnum`. |
| `32` | `[MEMORY STAT]` | Memory information every 3 seconds, equivalent to `SELECT * FROM v$memstat ORDER BY seqnum`. |

Common combined values are `7` for statement, bind, and plan; `15` for statement, bind, plan, and session statistics; `31` for statement, bind, plan, session statistics, and system statistics; and `63` for all available profile outputs.

Do not leave profiling enabled by default on production servers. The source warns that profiling records execution information for all SQL statements and can increase server/system load and disk usage. Use it for short periods during testing, performance analysis, or tuning, and monitor disk usage while it is enabled.

### Configure and run altimon

Use `FAQE/Home/08. Monitoring/How to set up and execute altimon__16876266.md` for the complete package matrix and exact commands. The main procedure is:

1. Download the proper `altimon` package for the Altibase version and OS listed by the source.
2. Extract the archive with `tar xvf altimon.tar` or the source package filename.
3. Copy `altimon` to `$ALTIBASE_HOME/bin/` and `altimon.conf` to `$ALTIBASE_HOME/conf/`.
4. Edit connection information, process-check properties, and monitored Altibase environment values in `altimon.conf`.
5. Set OS-specific environment variables when needed: `UNIX95=1` for HP-UX or `NMON=t` for AIX.
6. Start with `altimon start` and review `$ALTIBASE_HOME/trc/altimon.log` or the configured log path.

For Windows monitoring, use `FAQE/Home/08. Monitoring/Monitoring Tools for Windows__16876220.md`. Configure the `isql.exe` connection command in `altimon.bat`, add SQL to `ALTIMON_SCRIPT/all.sql`, set the interval with `ping -n`, and use `altimon.vbs` when running the batch file in the background.

### Monitor and resolve locks

The monitoring FAQ identifies `v$lock` and `v$lock_statement` as the main lock views. `v$lock` shows which lock type is held on a table; a `SELECT` statement holds `IS_LOCK`, and `INSERT`, `UPDATE`, and `DELETE` hold `IX_LOCK`. Join `v$lock` to `SYSTEM_.SYS_TABLES_` to map the locked table, and join `v$lock.trans_id` to `v$lock_statement.tx_id` to find the query holding the lock.

After identifying the target session, close it as `sysdba` only when the operational impact is understood:

```sql
ALTER DATABASE database_name SESSION CLOSE session_id;
```

### Diagnose undo tablespace growth

Use the detailed undo monitoring query in the catalog to identify transactions that use undo or access undo images. Interpret these fields together: `SESSION_ID`, `TX_ID`, `STATEMENT_ID`, `TX_TYPE`, `TX_STATUS`, `SQL_STATUS`, `CLIENT_IP`, `CLIENT_PID`, `AUTOCOMMIT`, `UTRANS_TIMEOUT`, `DISK_VIEW_SCN`, `MIN_DISK_LOB_VIEW_SCN`, `UNDO_USED_KB`, `UNDO_PAGE_COUNT`, and `QUERY`.

Source diagnostic scenarios are:

| Scenario | Evidence pattern |
| --- | --- |
| Long-running update transaction | `TX_TYPE=UPDATE`, `TX_STATUS=BEGIN`, `SQL_STATUS=SQL_ING`, increasing `UNDO_USED_KB`. |
| Long-running open update transaction | `TX_TYPE=UPDATE`, `TX_STATUS=BEGIN`, `SQL_STATUS=SQL_END` or null, stable `UNDO_USED_KB`. |
| Statement accessing pre-change data | `SQL_STATUS=SQL_ING`, non-empty `DISK_VIEW_SCN`, increasing `UNDO_PAGE_COUNT`, and `UNDO_USED_KB` null or stable. |
| Open LOB access in non-autocommit mode | `TX_STATUS=BEGIN` and non-empty `MIN_DISK_LOB_VIEW_SCN`. |
| Rollback | `TX_TYPE=UPDATE` and `TX_STATUS=ABORT`; `STATEMENT_ID` may be null if rollback continues after session termination. |
| Replication transaction | `SESSION_ID` shows the replication object name, `CLIENT_IP` shows the remote server IP and port, and `QUERY` shows `REMOTE_TX_ID`. |

Immediate actions are either expanding undo tablespace capacity or removing the root cause. The source warns that terminating a DML session may trigger rollback; undo may be released only after rollback completes. For persistent prevention, split large transactions, configure `UTRANS_TIMEOUT`, avoid uncommitted transactions in non-autocommit applications, and close LOB cursors or complete the transaction.

## SQL, Commands, and Configuration

### Storage and version-specific query selection

The monitoring FAQ intentionally preserves different SQL for different Altibase versions. Do not collapse these variants unless the answer explicitly names the version and the canonical duplicate target.

| Topic | Version or condition | Source |
| --- | --- | --- |
| Disk table and index usage | `ALTIBASE HDB 4.3.9.x`; also usable in `5.1.1` | `FAQE/Home/08. Monitoring/Disk table and index usage/ALTIBASE HDB 4.3.9.x__16876229.md` |
| Disk table and index usage | `ALTIBASE HDB 5.1.5.x` | `FAQE/Home/08. Monitoring/Disk table and index usage/ALTIBASE HDB 5.1.5.x__16876234.md` |
| Disk table and index usage | `ALTIBASE HDB 5.3.x`, `5.5.1`, `6.1.1`, `6.3.1`; `BUG-31372` added `TOTAL_USED_SIZE` to `X$SEGMENT` | `FAQE/Home/08. Monitoring/Disk table and index usage/ALTIBASE HDB 5.3.x, 5.5.1, 6.1.1, 6.3.1__16876240.md` |
| Disk tablespace usage | `ALTIBASE HDB 4.3.9`, `5.1.5`, `5.3.3`, `5.3.5`, `5.5.1`, `6.1.1`, `6.3.1` each has its own query variant | `FAQE/Home/08. Monitoring/Disk tablespace usage/**` |
| Memory tablespace usage | `ALTIBASE HDB 5.5.1`, `6.1.1`, `6.3.1`; `V$VOL_TABLESPACES` was added from `5.5.1` | `FAQE/Home/08. Monitoring/Memory tablespace usage/ALTIBASE HDB 5.5.1, 6.1.1, 6.3.1__16876263.md` |
| Memory table and index usage | Data usage query can be used from `HDB 4.3.9.x` through `HDB 6.3.1.x`; memory table index size is `16 bytes * number of records` per index | `FAQE/Home/08. Monitoring/Memory table and index usage__16876259.md` |
| Rollback query identification | `ALTIBASE HDB 5.1.5` or later | `FAQE/Home/08. Monitoring/How to determine which queries are being rolled back__16876296.md` |
| Lock monitoring properties | Based on `ALTIBASE HDB 6.3.1`; usable in `ALTIBASE HDB 5` and `ALTIBASE HDB 6`, though some monitoring items may cause result errors | `FAQE/Home/08. Monitoring/Lock related properties__16876204.md` |

### Exact SQL, Command, and Configuration Catalog

This catalog copies every fenced source code block from the R011 source set. It intentionally includes SQL, shell commands, Windows commands, configuration snippets, output examples, and `altiProfile` output formats because all can affect answerability.

### 1. Session
Source path: `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/1. Session__14058254.md`

#### [SS01] Total Number of Sessions - source block 1

````text
  SELECT COUNT(*) TOTAL_SESSION_CNT FROM V$SESSION ;
````

#### [SS02] Session Information - source block 2

````text
   SELECT A.ID SESSION_ID
       , A.DB_USERNAME USER_NAME
       , REPLACE2(REPLACE2(A.COMM_NAME, 'SOCKET-', NULL), '-SERVER', NULL) CLIENT_IP
       , A.CLIENT_APP_INFO             -- Delete it if using Altibase v4
       , A.CLIENT_PID
       , A.SESSION_STATE
       , DECODE(A.AUTOCOMMIT_FLAG, 1, 'ON', 'OFF') AUTOCOMMIT
       , DECODE(A.LOGIN_TIME, 0, '-', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + A.LOGIN_TIME / (24*60*60), 'YY/MM/DD HH:MI:SS')) LOGIN_TIME
       , DECODE(A.IDLE_START_TIME, 0, '-', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + A.IDLE_START_TIME / (24*60*60), 'YY/MM/DD HH:MI:SS')) IDLE_TIME
       , NVL(LTRIM(B.QUERY), 'NONE') CURRENT_QUERY
    FROM V$SESSION A LEFT OUTER JOIN V$STATEMENT B ON A.CURRENT_STMT_ID = B.ID ;
````

#### [SS03] Session Information Connected With SYSDBA Authority - source block 3

````text
  SELECT A.ID SESSION_ID
       , A.DB_USERNAME USER_NAME
       , REPLACE2(REPLACE2(A.COMM_NAME, 'SOCKET-', NULL), '-SERVER', NULL) CLIENT_IP
       , A.CLIENT_APP_INFO              -- Delete it if using Altibase v4
       , A.CLIENT_PID
       , A.SESSION_STATE
       , DECODE(A.AUTOCOMMIT_FLAG, 1, 'ON', 'OFF') AUTOCOMMIT
       , DECODE(A.LOGIN_TIME, 0, '-', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + A.LOGIN_TIME / (24*60*60), 'MM/DD HH:MI:SS')) LOGIN_TIME
       , DECODE(A.IDLE_START_TIME, 0, '-', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') +A.IDLE_START_TIME / (24*60*60), 'MM/DD HH:MI:SS')) IDLE_TIME
       , NVL(LTRIM(B.QUERY), 'NONE') CURRENT_QUERY
    FROM V$SESSION A LEFT OUTER JOIN V$STATEMENT B ON A.CURRENT_STMT_ID = B.ID
   WHERE A.SYSDBA_FLAG = 1 ;
````

### 3. Main Performance View related to Statistical Information
Source path: `arch/Home/Altibase Monitoring Queries Guide/2. Altibase Meta Table and Performance View Overview/3. Main Performance View related to Statistical Information__14058244.md`

#### 3. Main Performance View related to Statistical Information - source block 1

````text
SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME = 'TIMED_STATISTICS';
````

### 10. Object
Source path: `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/10. Object__14058276.md`

#### [OB01] Memory Table Usage - source block 1

````text
SELECT MT.USER_NAME
     , MT.TABLE_NAME
     , MT.PARTITION_NAME
     , TBS.NAME TBS_NAME
     , TO_CHAR((MU.FIXED_ALLOC_MEM+MU.VAR_ALLOC_MEM)/1024/1024, '999,999,999.9') 'ALLOC(M)'
     , TO_CHAR((MU.FIXED_USED_MEM+MU.VAR_USED_MEM)/1024/1024,   '999,999,999.9') 'USED(M)'
     , TO_CHAR(((MU.FIXED_USED_MEM+MU.VAR_USED_MEM)/(MU.FIXED_ALLOC_MEM+MU.VAR_ALLOC_MEM))*100, '999.9') 'USAGE(%)'
  FROM (SELECT U.USER_NAME
             , T.TABLE_NAME
             , DECODE(T.IS_PARTITIONED, 'F', T.TABLE_OID, 'T', P.PARTITION_OID) TABLE_OID
             , DECODE(T.IS_PARTITIONED, 'F', RPAD('-', 14), 'T', P.PARTITION_NAME) PARTITION_NAME
             , DECODE(T.IS_PARTITIONED, 'F', T.TBS_ID, 'T', P.TBS_ID) TBS_ID
          FROM SYSTEM_.SYS_USERS_ U
             , SYSTEM_.SYS_TABLES_ T LEFT OUTER JOIN SYSTEM_.SYS_TABLE_PARTITIONS_ P ON T.TABLE_ID = P.TABLE_ID
         WHERE 1=1
           AND U.USER_ID <> 1
           AND U.USER_ID = T.USER_ID
           AND T.TBS_ID IN (SELECT ID FROM V$TABLESPACES WHERE TYPE IN (1, 2, 8))
       ) MT
     , V$MEMTBL_INFO MU
     , V$TABLESPACES TBS
 WHERE 1=1
   AND MT.TABLE_OID = MU.TABLE_OID
   AND TBS.ID = MT.TBS_ID
 ORDER BY 1, 2, 3
   ;
````

#### [OB01] Memory Table Usage - source block 2

````text
SELECT A.USER_NAME
     , B.TABLE_NAME
     , D.NAME TBS_NAME
     , TO_CHAR((C.FIXED_ALLOC_MEM+C.VAR_ALLOC_MEM)/1024/1024, '999,999,999.9') 'ALLOC(M)'
     , TO_CHAR((C.FIXED_USED_MEM+C.VAR_USED_MEM)/1024/1024,   '999,999,999.9') 'USED(M)'
     , TO_CHAR(((C.FIXED_USED_MEM+C.VAR_USED_MEM)/(C.FIXED_ALLOC_MEM+C.VAR_ALLOC_MEM))*100, '999.9') 'USAGE(%)'
  FROM SYSTEM_.SYS_USERS_ A
     , SYSTEM_.SYS_TABLES_ B
     , V$MEMTBL_INFO C
     , V$TABLESPACES D
 WHERE 1=1
   AND A.USER_NAME <> 'SYSTEM_'
   AND B.TABLE_TYPE = 'T'
   AND A.USER_ID = B.USER_ID
   AND B.TABLE_OID = C.TABLE_OID
   AND B.TBS_ID = D.ID
 ORDER BY USER_NAME, TBS_NAME, TABLE_NAME
;
````

#### [OB02] Queue - source block 3

````text
SELECT A.USER_NAME
     , B.TABLE_NAME
     , D.NAME TABLESPACE_NAME
     , C.TABLE_OID
     , TO_CHAR((C.FIXED_ALLOC_MEM+C.VAR_ALLOC_MEM)/1024/1024, '999,999,999.9') 'ALLOC(M)'
     , TO_CHAR((C.FIXED_USED_MEM+C.VAR_USED_MEM)/1024/1024,   '999,999,999.9') 'USED(M)'
     , TO_CHAR(((C.FIXED_USED_MEM+C.VAR_USED_MEM)/(C.FIXED_ALLOC_MEM+C.VAR_ALLOC_MEM))*100, '999.9') 'USAGE(%)'
  FROM SYSTEM_.SYS_USERS_ A
     , SYSTEM_.SYS_TABLES_ B
     , V$MEMTBL_INFO C
     , V$TABLESPACES D
 WHERE 1=1
   AND A.USER_NAME <> 'SYSTEM_'
   AND B.TABLE_TYPE = 'Q'
   AND A.USER_ID = B.USER_ID
   AND B.TABLE_OID = C.TABLE_OID
   AND B.TBS_ID = D.ID ;
````

#### [OB03] Memory Table with Low Efficiency - source block 4

````text
SELECT MT.USER_NAME
     , MT.TABLE_NAME
     , MT.PARTITION_NAME
     , TBS.NAME TBS_NAME
     , TO_CHAR((MU.FIXED_ALLOC_MEM+MU.VAR_ALLOC_MEM)/1024/1024, '999,999,999.9') 'ALLOC(M)'
     , TO_CHAR((MU.FIXED_USED_MEM+MU.VAR_USED_MEM)/1024/1024,   '999,999,999.9') 'USED(M)'
     , TO_CHAR(((MU.FIXED_USED_MEM+MU.VAR_USED_MEM)/(MU.FIXED_ALLOC_MEM+MU.VAR_ALLOC_MEM))*100, '999.9') 'USAGE(%)'
  FROM (SELECT U.USER_NAME
             , T.TABLE_NAME
             , DECODE(T.IS_PARTITIONED, 'F', T.TABLE_OID, 'T', P.PARTITION_OID) TABLE_OID
             , DECODE(T.IS_PARTITIONED, 'F', RPAD('-', 14), 'T', P.PARTITION_NAME) PARTITION_NAME
             , DECODE(T.IS_PARTITIONED, 'F', T.TBS_ID, 'T', P.TBS_ID) TBS_ID
          FROM SYSTEM_.SYS_USERS_ U
             , SYSTEM_.SYS_TABLES_ T LEFT OUTER JOIN SYSTEM_.SYS_TABLE_PARTITIONS_ P ON T.TABLE_ID = P.TABLE_ID
         WHERE 1=1
           AND U.USER_ID <> 1
           AND U.USER_ID = T.USER_ID
           AND T.TBS_ID IN (SELECT ID FROM V$TABLESPACES WHERE TYPE IN (1, 2, 8))
       ) MT
     , V$MEMTBL_INFO MU
     , V$TABLESPACES TBS
 WHERE 1=1
   AND MT.TABLE_OID = MU.TABLE_OID
   AND TBS.ID = MT.TBS_ID
   AND ROUND((FIXED_ALLOC_MEM+VAR_ALLOC_MEM)/1024/1024, 2) >= 1024                                -- 1G or more pages allocated to the memory table
   AND ROUND((FIXED_USED_MEM+VAR_USED_MEM)/(FIXED_ALLOC_MEM+VAR_ALLOC_MEM+0.01)*100, 2) <= 50     -- USAGE is 50% or less
 ORDER BY 1, 2, 3
   ;
````

#### [OB03] Memory Table with Low Efficiency - source block 5

````text
SELECT C.USER_NAME
     , B.TABLE_NAME
     , TO_CHAR((C.FIXED_ALLOC_MEM+C.VAR_ALLOC_MEM)/1024/1024, '999,999,999.9') 'ALLOC(M)'
     , TO_CHAR((C.FIXED_USED_MEM+C.VAR_USED_MEM)/1024/1024,   '999,999,999.9') 'USED(M)'
     , TO_CHAR(((C.FIXED_USED_MEM+C.VAR_USED_MEM)/(C.FIXED_ALLOC_MEM+C.VAR_ALLOC_MEM))*100, '999.9') 'USAGE(%)'
  FROM V$MEMTBL_INFO A
     , SYSTEM_.SYS_TABLES_ B
     , SYSTEM_.SYS_USERS_ C
 WHERE A.TABLE_OID = B.TABLE_OID
   AND B.USER_ID = C.USER_ID
   AND ROUND((FIXED_ALLOC_MEM+VAR_ALLOC_MEM)/1024/1024, 2) >= 1024                                -- 1G or more pages allocated to the memory table
   AND ROUND((FIXED_USED_MEM+VAR_USED_MEM)/(FIXED_ALLOC_MEM+VAR_ALLOC_MEM+0.01)*100, 2) <= 50     -- USAGE is 50% or less
   AND B.USER_ID <> 1
 ORDER BY 'FREE(M)' DESC
;
````

#### [OB04] Memory Index and Queue Index Usage - source block 6

````text
SELECT U.USER_NAME, T.TABLE_NAME TABLE_NAME
     , B.INDEX_NAME
     , LPAD(I.IS_PARTITIONED, 14) INDEX_PARTITIONED
     , ROUND(((USED_NODE_COUNT + PREPARE_NODE_COUNT) / 15 * 32768)/1024/1024, 1) AS 'SIZE(MB)'
  FROM V$MEM_BTREE_HEADER B
     , SYSTEM_.SYS_INDICES_ I
     , SYSTEM_.SYS_TABLES_ T
     , SYSTEM_.SYS_USERS_ U
 WHERE 1=1
   AND B.INDEX_ID = I.INDEX_ID
   AND I.TABLE_ID = T.TABLE_ID
   AND B.INDEX_TBS_ID <> 0
   AND U.USER_ID = T.USER_ID
 ORDER BY TABLE_NAME, B.INDEX_ID
;
````

#### [OB05] Disk Table - source block 7

````text
SELECT U.USER_NAME USER_NAME
     , TBL.TABLE_NAME TABLE_NAME
     , DECODE(TBL.IS_PARTITIONED, 'T', TBL.PARTITION_NAME, 'F', '-') PARTITIONED_TABLE
     , TBS.NAME TBS_NAME
     , TO_CHAR((D.MAX * TBS.PAGE_SIZE)/1024, '999,999,999,999') 'MAX(KB)'
     , TO_CHAR((TBS.EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.TOTAL_EXTENT_COUNT)/1024, '999,999,999,999') 'ALLOC(KB)'
     , TO_CHAR(SEG.TOTAL_USED_SIZE/1024, '999,999,999,999') 'USED(KB)'
  FROM (SELECT TBL.USER_ID
             , DECODE(TBL.IS_PARTITIONED, 'F', TBL.TABLE_OID, 'T', PT.PARTITION_OID) TABLE_OID
             , TBL.TABLE_NAME
             , PT.PARTITION_NAME
             , DECODE(TBL.IS_PARTITIONED, 'F', TBL.TBS_ID, 'T', PT.TBS_ID) TBS_ID
             , TBL.IS_PARTITIONED
          FROM SYSTEM_.SYS_TABLES_ TBL LEFT OUTER JOIN SYSTEM_.SYS_TABLE_PARTITIONS_ PT ON TBL.TABLE_ID = PT.TABLE_ID
         WHERE TBL.TABLE_TYPE = 'T'
       ) TBL
     , (SELECT S.TABLE_OID, SUM(S.TOTAL_EXTENT_COUNT) TOTAL_EXTENT_COUNT, SUM(S.TOTAL_USED_SIZE) TOTAL_USED_SIZE
          FROM X$SEGMENT S
         WHERE S.SEGMENT_TYPE IN (6, 7) /* 6 : Table, 7 : LOB Data (6.1.1 or later), 5 : Index */
         GROUP BY S.TABLE_OID) SEG
     , SYSTEM_.SYS_USERS_ U
     , V$TABLESPACES TBS
     , (SELECT SPACEID
             , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
             , DECODE(MAX(AUTOEXTEND),1,'ON','OFF') 'AUTOEXTEND'
          FROM V$DATAFILES
         GROUP BY SPACEID) D
 WHERE 1=1
   AND SEG.TABLE_OID = TBL.TABLE_OID
   AND U.USER_ID = TBL.USER_ID
   AND D.SPACEID = TBL.TBS_ID
   AND TBS.ID = TBL.TBS_ID
 ORDER BY USER_NAME, TABLE_NAME, PARTITIONED_TABLE
;
````

#### [OB05] Disk Table - source block 8

````text
SELECT U.USER_NAME USER_NAME
     , TBL.TABLE_NAME TABLE_NAME
     , DECODE(TBL.IS_PARTITIONED, 'T', TBL.PARTITION_NAME, 'F', '-') PARTITIONED_TABLE
     , TBS.NAME TBS_NAME
     , TO_CHAR((D.MAX * TBS.PAGE_SIZE)/1024/1024, '999,999,999') 'MAX(MB)'
     , TO_CHAR((TBS.EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_TOTAL_COUNT)/1024/1024, '999,999,999') 'ALLOC(MB)'
  FROM (SELECT TBL.USER_ID
             , DECODE(TBL.IS_PARTITIONED, 'F', TBL.TABLE_OID, 'T', PT.PARTITION_OID) TABLE_OID
             , TBL.TABLE_NAME
             , PT.PARTITION_NAME
             , DECODE(TBL.IS_PARTITIONED, 'F', TBL.TBS_ID, 'T', PT.TBS_ID) TBS_ID
             , TBL.IS_PARTITIONED
          FROM SYSTEM_.SYS_TABLES_ TBL LEFT OUTER JOIN SYSTEM_.SYS_TABLE_PARTITIONS_ PT ON TBL.TABLE_ID = PT.TABLE_ID
       ) TBL
     , V$SEGMENT SEG
     , SYSTEM_.SYS_USERS_ U
     , V$TABLESPACES TBS
     , (SELECT SPACEID
             , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
             , DECODE(MAX(AUTOEXTEND),1,'ON','OFF') 'AUTOEXTEND'
          FROM V$DATAFILES
         GROUP BY SPACEID) D
 WHERE 1=1
   AND SEG.SEGMENT_TYPE = 'TABLE'  /* 'TABLE' : Table, 'INDEX' : Index */
   AND SEG.TABLE_OID = TBL.TABLE_OID
   AND U.USER_ID = TBL.USER_ID
   AND D.SPACEID = TBL.TBS_ID
   AND TBS.ID = TBL.TBS_ID
 ORDER BY USER_NAME, PARTITIONED, TABLE_NAME, PARTITIONED_TABLE
;
````

#### [OB05] Disk Table - source block 9

````text
SELECT U.USER_NAME 'USER_NAME'
     , TBL.TABLE_NAME 'TABLE_NAME'
     , TBS.NAME 'TBS_NAME'
     , TO_CHAR((TBS.TOTAL_PAGE_COUNT * TBS.PAGE_SIZE)/1024 , '999,999,999') 'TBS_MAX(KB)'
     , TO_CHAR((TBS.A_EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_TOTAL_COUNT)/1024, '999,999,999') 'ALLOC(KB)'
     , TO_CHAR((TBS.A_EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_FULL_COUNT)/1024, '999,999,999') 'USED(KB)'
  FROM X$SEGMENT SEG
     , SYSTEM_.SYS_TABLES_ TBL
     , V$TABLESPACES TBS
     , SYSTEM_.SYS_USERS_ U
 WHERE 1=1
   AND SEG.TABLE_OID = TBL.TABLE_OID
   AND SEG.SPACE_ID = TBL.TBS_ID
   AND SEG.SPACE_ID = TBS.ID
   AND TBL.USER_ID = U.USER_ID
   AND TBL.TABLE_TYPE = 'T'
   AND SEG.SEGMENT_TYPE = 6
 ORDER BY USER_NAME, TABLE_NAME
;
````

#### [OB06] Disk Index Usage - source block 10

````text
SELECT U.USER_NAME USER_NAME
     , I_LIST.TABLE_NAME
     , DECODE(I_LIST.PARTITION_NAME, NULL, '-', I_LIST.PARTITION_NAME) PARTITIONED_NAME
     , I_LIST.INDEX_NAME INDEX_NAME
     , DECODE(I_LIST.INDEX_PARTITION_NAME, NULL, '-', I_LIST.INDEX_PARTITION_NAME) PARTITIONED_INDEX
     , TBS.NAME TBS_NAME
     , TO_CHAR((D.MAX * TBS.PAGE_SIZE)/1024/1024, '999,999,999') 'MAX(MB)'
     , TO_CHAR((TBS.EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.TOTAL_EXTENT_COUNT)/1024/1024, '999,999,999') 'ALLOC(MB)'
     , TO_CHAR(SEG.TOTAL_USED_SIZE/1024/1024, '999,999,999') 'USED(MB)'
  FROM (SELECT T.TABLE_NAME
             , PT.PARTITION_NAME
             , I.INDEX_NAME
             , PI.INDEX_PARTITION_NAME
             , DECODE(T.IS_PARTITIONED, 'F', I.TABLE_ID, 'T', PT.TABLE_ID) TABLE_ID
             , DECODE(T.IS_PARTITIONED, 'F', T.TABLE_OID, 'T', PT.PARTITION_OID) TABLE_OID
             , DECODE(I.IS_PARTITIONED, 'F', I.TBS_ID, 'T', PI.TBS_ID) TBS_ID
             , I.INDEX_ID
             , T.USER_ID
          FROM SYSTEM_.SYS_INDICES_ I LEFT OUTER JOIN SYSTEM_.SYS_INDEX_PARTITIONS_ PI ON PI.INDEX_ID = I.INDEX_ID
                                      LEFT OUTER JOIN SYSTEM_.SYS_TABLE_PARTITIONS_ PT ON PT.PARTITION_ID = PI.TABLE_PARTITION_ID
                                      LEFT OUTER JOIN SYSTEM_.SYS_TABLES_ T ON T.TABLE_ID = I.TABLE_ID ) I_LIST
     , X$SEGMENT SEG
     , V$INDEX I
     , V$TABLESPACES TBS
     , SYSTEM_.SYS_USERS_ U
     , (SELECT SPACEID
             , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
             , DECODE(MAX(AUTOEXTEND),1,'ON','OFF') 'AUTOEXTEND'
          FROM V$DATAFILES
         GROUP BY SPACEID) D
 WHERE 1=1
   AND SEG.TABLE_OID = I.TABLE_OID
   AND SEG.SEGMENT_PID = I.INDEX_SEG_PID
   AND SEG.SPACE_ID = I_LIST.TBS_ID
   AND I_LIST.INDEX_ID = I.INDEX_ID
   AND I_LIST.TABLE_OID = I.TABLE_OID
   AND I_LIST.TBS_ID = TBS.ID
   AND D.SPACEID = I_LIST.TBS_ID
   AND U.USER_ID = I_LIST.USER_ID
 ORDER BY I_LIST.TABLE_NAME, I_LIST.INDEX_NAME, I_LIST.PARTITION_NAME, I_LIST.INDEX_PARTITION_NAME
;
````

#### [OB06] Disk Index Usage - source block 11

````text
SELECT U.USER_NAME USER_NAME
     , I_LIST.TABLE_NAME
     , DECODE(I_LIST.PARTITION_NAME, NULL, '-', I_LIST.PARTITION_NAME) PARTITIONED_NAME
     , I_LIST.INDEX_NAME INDEX_NAME
     , DECODE(I_LIST.INDEX_PARTITION_NAME, NULL, '-', I_LIST.INDEX_PARTITION_NAME) PARTITIONED_INDEX
     , TBS.NAME TBS_NAME
     , TO_CHAR((D.MAX * TBS.PAGE_SIZE)/1024/1024, '999,999,999') 'MAX(MB)'
     , TO_CHAR((TBS.EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_TOTAL_COUNT)/1024/1024, '999,999,999') 'ALLOC(MB)'
  FROM (SELECT T.TABLE_NAME
             , PT.PARTITION_NAME
             , I.INDEX_NAME
             , PI.INDEX_PARTITION_NAME
             , DECODE(T.IS_PARTITIONED, 'F', I.TABLE_ID, 'T', PT.TABLE_ID) TABLE_ID
             , DECODE(T.IS_PARTITIONED, 'F', T.TABLE_OID, 'T', PT.PARTITION_OID) TABLE_OID
             , DECODE(I.IS_PARTITIONED, 'F', I.TBS_ID, 'T', PI.TBS_ID) TBS_ID
             , I.INDEX_ID
             , T.USER_ID
          FROM SYSTEM_.SYS_INDICES_ I LEFT OUTER JOIN SYSTEM_.SYS_INDEX_PARTITIONS_ PI ON PI.INDEX_ID = I.INDEX_ID
                                      LEFT OUTER JOIN SYSTEM_.SYS_TABLE_PARTITIONS_ PT ON PT.PARTITION_ID = PI.TABLE_PARTITION_ID
                                      LEFT OUTER JOIN SYSTEM_.SYS_TABLES_ T ON T.TABLE_ID = I.TABLE_ID ) I_LIST
     , V$SEGMENT SEG
     , V$INDEX I
     , V$TABLESPACES TBS
     , SYSTEM_.SYS_USERS_ U
     , (SELECT SPACEID
             , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
             , DECODE(MAX(AUTOEXTEND),1,'ON','OFF') 'AUTOEXTEND'
          FROM V$DATAFILES
         GROUP BY SPACEID) D
 WHERE 1=1
   AND SEG.TABLE_OID = I.TABLE_OID
   AND SEG.SEGMENT_PID = I.INDEX_SEG_PID
   AND SEG.SPACE_ID = I_LIST.TBS_ID
   AND I_LIST.INDEX_ID = I.INDEX_ID
   AND I_LIST.TABLE_OID = I.TABLE_OID
   AND I_LIST.TBS_ID = TBS.ID
   AND D.SPACEID = I_LIST.TBS_ID
   AND U.USER_ID = I_LIST.USER_ID
 ORDER BY I_LIST.TABLE_NAME, I_LIST.INDEX_NAME, I_LIST.PARTITION_NAME, I_LIST.INDEX_PARTITION_NAME
;
````

#### [OB06] Disk Index Usage - source block 12

````text
SELECT U.USER_NAME AS 'USER_NAME'
     , TBL.TABLE_NAME AS 'TABLE_NAME'
     , IDX.INDEX_NAME AS 'INDEX_NAME'
     , TBS.NAME AS 'TBS_NAME'
     , TO_CHAR((TBS.TOTAL_PAGE_COUNT * TBS.PAGE_SIZE)/1024/1024 , '999,999,999') AS 'TBS_MAX(KB)'
     , TO_CHAR((TBS.A_EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_TOTAL_COUNT)/1024/1024, '999,999,999') AS 'ALLOC(MB)'
     , TO_CHAR((TBS.A_EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_FULL_COUNT )/1024/1024, '999,999,999') AS 'USED(MB)'
 FROM  X$SEGMENT SEG
     , V$INDEX I
     , SYSTEM_.SYS_INDICES_ IDX
     , SYSTEM_.SYS_TABLES_ TBL
     , V$TABLESPACES TBS
     , SYSTEM_.SYS_USERS_ U
 WHERE SEG.TABLE_OID = I.TABLE_OID
   AND SEG.SEGMENT_DESC = I.INDEX_SEG_DESC
   AND I.INDEX_ID = IDX.INDEX_ID
   AND IDX.TABLE_ID = TBL.TABLE_ID
   AND SEG.SPACE_ID = IDX.TBS_ID
   AND SEG.SPACE_ID = TBS.ID
   AND IDX.USER_ID = U.USER_ID
   AND TBL.TABLE_TYPE = 'T'
   AND SEG.SEGMENT_TYPE = 5
 ORDER BY U.USER_NAME, TBL.TABLE_NAME, IDX.INDEX_NAME
;
````

#### [OB07] Partition Table Information - source block 13

````text
SELECT U.USER_NAME
     , T.TABLE_NAME
     , P.PARTITION_NAME
     , DECODE(PM.PARTITION_METHOD, 0, RPAD('RANGE', 16), 1, RPAD('HASH', 16), 2, RPAD('LIST', 16)) PARTITION_METHOD
     , RPAD(P.PARTITION_ORDER, 15) PARTITION_ORDER
     , RPAD(PM.ROW_MOVEMENT, 12) ROW_MOVEMENT
     , P.PARTITION_MIN_VALUE
     , P.PARTITION_MAX_VALUE
     , RPAD(P.PARTITION_ACCESS, 6) 'ACCESS'                             -- Delete this column before use in versions earlier than Altibase v6.5.1.
     , TO_CHAR(P.CREATED, 'YYYY-MM-DD HH:MI:SS') CREATED                -- Delete this column before use in versions earlier than Altibase v6.5.1.
     , TO_CHAR(P.LAST_DDL_TIME, 'YYYY-MM-DD HH:MI:SS') LAST_DDL_TIME    -- Delete this column before use in versions earlier than Altibase v6.5.1.
  FROM SYSTEM_.SYS_TABLES_ T
     , SYSTEM_.SYS_TABLE_PARTITIONS_ P
     , SYSTEM_.SYS_PART_TABLES_ PM
     , SYSTEM_.SYS_USERS_ U
 WHERE 1=1
   AND U.USER_ID = T.USER_ID
   AND T.TABLE_ID = P.TABLE_ID
   AND PM.TABLE_ID = T.TABLE_ID ;
````

#### [OB08] Sequence - source block 14

````text
SELECT USER_NAME
     , TABLE_NAME SEQ_NAME
     , MIN_SEQ MIN
     , CURRENT_SEQ
     , MAX_SEQ MAX
     , INCREMENT_SEQ INCREMENT
     , IS_CYCLE
     , CACHE_SIZE CACHE
  FROM V$SEQ A
     , SYSTEM_.SYS_USERS_ B
     , SYSTEM_.SYS_TABLES_ C
 WHERE 1=1
   AND A.SEQ_OID = C.TABLE_OID
   AND B.USER_ID = C.USER_ID
   AND B.USER_NAME <> 'SYSTEM_' ;
````

#### [OB09] Synonym - source block 15

````text
SELECT NVL(U.USER_NAME, 'PUBLIC') SYNONYM_OWNER
     , S.SYNONYM_NAME
     , S.OBJECT_OWNER_NAME OBJECT_OWNER
     , S.OBJECT_NAME
     , TO_CHAR(S.LAST_DDL_TIME, 'YYYY-MM-DD HH:MI:SS') LAST_DDL_TIME
  FROM SYSTEM_.SYS_SYNONYMS_ S
       LEFT OUTER JOIN SYSTEM_.SYS_USERS_ U ON S.SYNONYM_OWNER_ID = U.USER_ID
 WHERE 1=1
   --AND U.USER_ID <> 0       -- If the user wants to exclude PUBLIC synonym, remove comments and use them.
 ;
````

#### [OB09] Synonym - source block 16

````text
SELECT NVL(U.USER_NAME, 'PUBLIC') SYNONYM_OWNER
     , S.SYNONYM_NAME
     , S.SCHEMA_NAME OBJECT_OWNER
     , S.OBJECT_NAME
  FROM SYSTEM_.SYS_SYNONYMS_ S LEFT OUTER JOIN SYSTEM_.SYS_USERS_ U ON S.USER_ID = U.USER_ID
;
````

#### [OB10] PSM - source block 17

````text
SELECT A.USER_NAME
     , PROC_NAME PSM_NAME
     , DECODE(OBJECT_TYPE, 0, 'PROCEDURE', 1, 'FUNCTION', 3, 'TYPESET') PSM_TYPE
     , DECODE(STATUS, 0, 'VALID', 'INVALID') STATUS
     , TO_CHAR(B.CREATED, 'YYYY-MM-DD HH:MI:SS') CREATED
     , TO_CHAR(B.LAST_DDL_TIME, 'YYYY-MM-DD HH:MI:SS') LAST_DDL_TIME    -- Delete this column before use in Altibase v4.
  FROM SYSTEM_.SYS_USERS_ A
     , SYSTEM_.SYS_PROCEDURES_ B
 WHERE 1=1
   AND A.USER_ID = B.USER_ID
   AND A.USER_NAME <> 'SYSTEM_'
 ORDER BY 1, 2, 3;
````

#### [OB11] PSM Creation Statement - source block 18

````text
SELECT PARSE
  FROM SYSTEM_.SYS_PROC_PARSE_
 WHERE PROC_OID = (SELECT PROC_OID
          FROM SYSTEM_.SYS_PROCEDURES_
         WHERE PROC_NAME = 'psm_name')   -- Enter the PSM name that want to be searched
 ORDER BY SEQ_NO ;
````

#### [OB12] View - source block 19

````text
SELECT A.USER_NAME
     , B.TABLE_NAME VIEW_NAME
     , DECODE(C.STATUS, 0, 'VALID', 'INVALID') STATUS
     , TO_CHAR(B.CREATED, 'YYYY-MM-DD HH:MI:SS') CREATED                 -- Delete this column before use in Altibase v4.
     , TO_CHAR(B.LAST_DDL_TIME, 'YYYY-MM-DD HH:MI:SS') LAST_DDL_TIME     -- Delete this column before use in Altibase v4.
  FROM SYSTEM_.SYS_USERS_ A
     , SYSTEM_.SYS_TABLES_ B
     , SYSTEM_.SYS_VIEWS_ C
 WHERE 1=1
   AND A.USER_ID = B.USER_ID
   AND B.TABLE_ID = C.VIEW_ID
   AND B.TABLE_TYPE = 'V' ;
````

#### [OB13] View Creation Statement - source block 20

````text
SELECT PARSE
  FROM SYSTEM_.SYS_VIEW_PARSE_
 WHERE VIEW_ID = (SELECT TABLE_ID
          FROM SYSTEM_.SYS_TABLES_
         WHERE TABLE_NAME = 'view_name')    -- Enter the name of the view you want to view.
 ORDER BY SEQ_NO ;
````

#### [OB14] Package - source block 21

````text
SELECT A.USER_NAME
     , PACKAGE_NAME
     , DECODE(PACKAGE_TYPE, 6, 'PACKAGE_SPEC', 7, 'PACKAGE_BODY') PACKAGE_TYPE
     , DECODE(STATUS, 0, 'VALID', 'INVALID') STATUS
     , TO_CHAR(B.CREATED, 'YYYY-MM-DD HH:MI:SS') CREATED
     , TO_CHAR(B.LAST_DDL_TIME, 'YYYY-MM-DD HH:MI:SS') LAST_DDL_TIME
  FROM SYSTEM_.SYS_USERS_ A
     , SYSTEM_.SYS_PACKAGES_ B
 WHERE 1=1
   AND A.USER_ID = B.USER_ID
   AND A.USER_NAME <> 'SYSTEM_' ;
````

#### [OB15] Package Subprogram - source block 22

````text
SELECT USER_NAME
     , OBJECT_NAME
     , PACKAGE_NAME
     , DECODE(SUB_TYPE, 0, 'PROCEDURE', 1, 'FUNCTION') SUB_TYPE
     , PARA_NAME
     , PARA_ORDER
     , DECODE(INOUT_TYPE, 0, 'IN', 1, 'OUT', 2, 'IN OUT') INOUT_TYPE
     , DATA_TYPE
     , SIZE
     , DEFAULT_VAL
  FROM SYSTEM_.SYS_USERS_ A
     , SYSTEM_.SYS_PACKAGE_PARAS_ B
 WHERE 1=1
   AND A.USER_ID = B.USER_ID
   AND A.USER_NAME <> 'SYSTEM_' ;
````

#### [OB16] Package Creation Statement - source block 23

````text
SELECT PARSE
     , DECODE(PACKAGE_TYPE, 6, 'PACKAGE_SPEC', 7, 'PACKAGE_BODY') PACKAGE_TYPE
  FROM SYSTEM_.SYS_PACKAGE_PARSE_
 WHERE PACKAGE_OID IN (SELECT PACKAGE_OID
                         FROM SYSTEM_.SYS_PACKAGES_
                        WHERE PACKAGE_NAME = 'package_name')   -- Enter the name of the package that wanted to be viewed.
 ORDER BY SEQ_NO ;
````

#### [OB17] Trigger - source block 24

````text
SELECT TR.USER_NAME
     , T.TABLE_NAME
     , TR.TRIGGER_NAME
     , RPAD(DECODE(TR.IS_ENABLE, 0, 'NO',
                                 1, 'YES'), 9) IS_ENABLE
     , RPAD(DECODE(TR.EVENT_TIME, 1, 'BEFORE',
                             2, 'AFTER',
                             3, 'INSTEAD OF'), 10) EVENT_TIME
     , RPAD(DECODE(TR.EVENT_TYPE, 1, 'INSERT',
                             2, 'DELETE',
                             4, 'UPDATE'), 10) EVENT_TYPE
     , DECODE(TR.GRANULARITY, 1, 'FOR EACH ROW',
                              2, 'FOR EACH STATEMENT') GRANULARITY
  FROM SYSTEM_.SYS_TABLES_ T
     , SYSTEM_.SYS_TRIGGERS_ TR
 WHERE 1=1
   AND TR.TABLE_ID = T.TABLE_ID;
````

#### [OB18] Job - source block 25

````text
SELECT JOB_NAME
     , EXEC_QUERY PROC_NAME
     , INTERVAL
     , LPAD(DECODE(INTERVAL_TYPE, 'YY', 'YEARLY',
                                  'MM', 'MONTHLY',
                                  'DD', 'DAILY',
                                  'HH', 'HOURLY',
                                  'MI', 'MINUTELY'), 13) INTERVAL_TYPE
     , LPAD(DECODE(STATE, 0, '-', 1, 'ING'), 5) STATE
     , LPAD(EXEC_COUNT, 10) EXEC_COUNT
     , LPAD(ERROR_CODE, 10) ERROR_CODE
     , TO_CHAR(START_TIME, 'YYYY-MM-DD HH:MI:SS') START_TIME
     , TO_CHAR(LAST_EXEC_TIME, 'YYYY-MM-DD HH:MI:SS') LAST_EXEC_TIME
     , TO_CHAR(END_TIME, 'YYYY-MM-DD HH:MI:SS') END_TIME
     , DECODE(IS_ENABLE, 'T', 'YES', 'F', 'NO') IN_ENABLE     -- Delete this column before use in Altibase v6.3.1.
  FROM SYSTEM_.SYS_JOBS_;
````

#### [OB19] Database User - source block 26

````text
SELECT USER_ID,
       USER_NAME,
       TBS.NAME 'DEFAULT_TBS',
       CREATED
  FROM SYSTEM_.SYS_USERS_ U,
       V$TABLESPACES TBS
 WHERE U.DEFAULT_TBS_ID = TBS.ID;
````

#### [OB20] Tablespace List - source block 27

````text
SELECT ID 'TBS_ID'
    ,  NAME 'TBS_NAME'
    ,  DECODE(TYPE, 0, 'SYSTEM_TBS', 1, 'SYSTEM_TBS', 2, 'USER_MEM_TBS', 3, 'SYSTEM_TBS', 4, 'USER_DISK_TBS', 5, 'SYSTEM_TBS', 6, 'USER_DISK_TEMP', 7, 'SYSTEM_UNDO', 8, 'USER_VOL_TBS') 'TBS_TYPE'
 FROM V$TABLESPACES;
````

### 11. Privileges
Source path: `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/11. Privileges__14058278.md`

#### [PV01] System Privilege - source block 1

````text
SELECT A.USER_NAME GRANTEE
     , C.USER_NAME GRANTOR
     , REPLACE(D.PRIV_NAME, '_', ' ') PRIV_NAME
  FROM SYSTEM_.SYS_USERS_ A,
       SYSTEM_.SYS_GRANT_SYSTEM_ B,
       SYSTEM_.SYS_USERS_ C,
       SYSTEM_.SYS_PRIVILEGES_ D
 WHERE C.USER_NAME <> 'SYSTEM_'
   AND A.USER_TYPE <> 'R'                 -- Delete this condition before use in Altibase v6.5.1 or earlier.
   AND B.GRANTEE_ID = A.USER_ID
   AND B.GRANTOR_ID = C.USER_ID
   AND B.PRIV_ID = D.PRIV_ID
   --AND A.USER_NAME = 'user_name'
 ORDER BY GRANTEE, GRANTOR ;
````

#### [PV02] Object Privilege - source block 2

````text
SELECT A.USER_NAME GRANTEE
     , C.USER_NAME GRANTOR
     , F.USER_NAME OBJECT_OWNER
     , OBJ.OBJ_NAME OBJECT_NAME
     , DECODE(OBJ.OBJ_TYPE, 'T', DECODE(OBJ.OBJ_TYPE1, 'T', 'TABLE', 'V', 'VIEW'),
                            'S', 'SEQUENCE',
                            'P', 'PROCEDURE',
                            'Y', 'External library',
                            'D', 'DIRECTORY') OBJECT_TYPE
     , REPLACE(D.PRIV_NAME, '_', ' ') PRIV_NAME
     , DECODE(B.WITH_GRANT_OPTION, 0, 'NO', 'YES') WITH_GRANT_OPTION
  FROM SYSTEM_.SYS_USERS_ A
     , SYSTEM_.SYS_GRANT_OBJECT_ B
     , SYSTEM_.SYS_USERS_ C
     , SYSTEM_.SYS_PRIVILEGES_ D
     , (SELECT TABLE_NAME as OBJ_NAME, TABLE_TYPE as OBJ_TYPE1, 'T' as OBJ_TYPE, TABLE_ID as obj_id, USER_ID
          FROM SYSTEM_.SYS_TABLES_ WHERE TABLE_TYPE IN ('V', 'T')
         UNION
        SELECT TABLE_NAME as OBJ_NAME, '' as OBJ_TYPE1, TABLE_TYPE as OBJ_TYPE, TABLE_ID as obj_id, USER_ID
          FROM SYSTEM_.SYS_TABLES_ WHERE TABLE_TYPE = 'S'
         UNION
        SELECT PROC_NAME as OBJ_NAME, '' as OBJ_TYPE1, 'P' as OBJ_TYPE, PROC_OID as obj_id, user_id
          FROM system_.SYS_PROCEDURES_
         UNION
        SELECT directory_NAME as OBJ_NAME, '' as OBJ_TYPE1, 'D' as OBJ_TYPE, DIRECTORY_ID as obj_id, user_id
          FROM SYSTEM_.SYS_DIRECTORIES_
         UNION                                                                                                 -- Delete before use in Altibase v6.3.1 or earlier.
        SELECT library_name as OBJ_NAME, '' as OBJ_TYPE1, 'Y' as OBJ_TYPE, library_ID as obj_id, user_id       -- Delete before use in Altibase v6.3.1 or earlier.
          FROM SYSTEM_.SYS_LIBRARIES_                                                                          -- Delete before use in Altibase v6.3.1 or earlier.
       ) OBJ
     , SYSTEM_.SYS_USERS_ F
 WHERE 1=1
   AND C.USER_NAME <> 'SYSTEM_'
   AND A.USER_TYPE <> 'R'        -- Delete this condition before use in Altibase v6.5.1 or earlier.
   AND B.GRANTEE_ID = A.USER_ID
   AND B.GRANTOR_ID = C.USER_ID
   AND B.PRIV_ID = D.PRIV_ID
   AND B.OBJ_ID = OBJ.OBJ_ID
   AND OBJ.OBJ_TYPE = B.OBJ_TYPE
   AND OBJ.USER_ID = F.USER_ID
 ORDER BY GRANTEE, GRANTOR, OBJECT_OWNER, OBJECT_NAME, PRIV_NAME ;
````

#### [PV03] Role Creation Information - source block 3

````text
SELECT A.USER_NAME 'ROLE_NAME'
     , RPAD('SYSTEM', 9) PRIV_TYPE
     , '' OBJECT_NAME, '' OBJECT_TYPE
     , REPLACE(D.PRIV_NAME, '_', ' ') PRIV_NAME
     , '' WITH_GRANT_OPTION
  FROM SYSTEM_.SYS_USERS_ A,
       SYSTEM_.SYS_GRANT_SYSTEM_ B,
       SYSTEM_.SYS_PRIVILEGES_ D
 WHERE 1=1
   AND A.USER_ID <> 0
   AND A.USER_TYPE = 'R'
   AND B.GRANTEE_ID = A.USER_ID
   AND B.PRIV_ID = D.PRIV_ID
UNION
SELECT A.USER_NAME 'ROLE_NAME'
     , RPAD('OBJECT', 9) PRIV_TYPE
     , F.USER_NAME||'.'||OBJ.OBJ_NAME OBJECT_NAME
     , DECODE(OBJ.OBJ_TYPE, 'T', DECODE(OBJ.OBJ_TYPE1, 'T', 'TABLE', 'V', 'VIEW'),
                            'S', 'SEQUENCE',
                            'P', 'PROCEDURE',
                            'Y', 'External library',
                            'D', 'DIRECTORY') OBJECT_TYPE
     , REPLACE(D.PRIV_NAME, '_', ' ') PRIV_NAME
     , DECODE(B.WITH_GRANT_OPTION, 0, 'NO', 'YES') WITH_GRANT_OPTION
  FROM SYSTEM_.SYS_USERS_ A
     , SYSTEM_.SYS_GRANT_OBJECT_ B
     , SYSTEM_.SYS_PRIVILEGES_ D
     , (SELECT TABLE_NAME as OBJ_NAME, TABLE_TYPE as OBJ_TYPE1, 'T' as OBJ_TYPE, TABLE_ID as obj_id, USER_ID
          FROM SYSTEM_.SYS_TABLES_ WHERE TABLE_TYPE IN ('V', 'T')
         UNION
        SELECT TABLE_NAME as OBJ_NAME, '' as OBJ_TYPE1, TABLE_TYPE as OBJ_TYPE, TABLE_ID as obj_id, USER_ID
          FROM SYSTEM_.SYS_TABLES_ WHERE TABLE_TYPE = 'S'
         UNION
        SELECT PROC_NAME as OBJ_NAME, '' as OBJ_TYPE1, 'P' as OBJ_TYPE, PROC_OID as obj_id, user_id
          FROM system_.SYS_PROCEDURES_
         UNION
        SELECT directory_NAME as OBJ_NAME, '' as OBJ_TYPE1, 'D' as OBJ_TYPE, DIRECTORY_ID as obj_id, user_id
          FROM SYSTEM_.SYS_DIRECTORIES_
         UNION
        SELECT library_name as OBJ_NAME, '' as OBJ_TYPE1, 'Y' as OBJ_TYPE, library_ID as obj_id, user_id
          FROM SYSTEM_.SYS_LIBRARIES_
       ) OBJ
     , SYSTEM_.SYS_USERS_ F
 WHERE 1=1
   AND A.USER_ID <> 0
   AND A.USER_TYPE = 'R'
   AND B.GRANTEE_ID = A.USER_ID
   AND B.PRIV_ID = D.PRIV_ID
   AND B.OBJ_ID = OBJ.OBJ_ID
   AND OBJ.OBJ_TYPE = B.OBJ_TYPE
   AND OBJ.USER_ID = F.USER_ID
;
````

#### [PV04] User Information Granted a Role - source block 4

````text
SELECT U1.USER_NAME GRANTEE
     , U2.USER_NAME GRANTOR
     , RU.USER_NAME ROLE_NAME
  FROM SYSTEM_.SYS_USER_ROLES_ R
     , SYSTEM_.SYS_USERS_ RU
     , SYSTEM_.SYS_USERS_ U1
     , SYSTEM_.SYS_USERS_ U2
 WHERE 1=1
   AND RU.USER_TYPE = 'R'
   AND R.ROLE_ID <> 0
   AND RU.USER_ID = R.ROLE_ID
   AND R.GRANTEE_ID = U1.USER_ID
   AND R.GRANTOR_ID = U2.USER_ID
;
````

#### [PV05] System and Object Privilege Types - source block 5

````text
SELECT DECODE(PRIV_TYPE, 1, 'OBJECT', 2, 'SYSTEM') PRIV_TYPE
     , PRIV_NAME
  FROM SYSTEM_.SYS_PRIVILEGES_
 ORDER BY PRIV_TYPE, PRIV_NAME;
````

### 12. Constraints
Source path: `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/12. Constraints__14058280.md`

#### [CT01] Full List of Constraints - source block 1

````text
SELECT USER_NAME
     , TABLE_NAME OBJECT_NAME
     , DECODE(B.TABLE_TYPE, 'T', 'TABLE', 'Q', 'QUEUE', 'V', 'VIEW', 'SEQUENCE') OBJECT_TYPE
     , C.CONSTRAINT_NAME CONST_NAME
     , DECODE(C.CONSTRAINT_TYPE, 0, 'FOREIGN KEY',
                                 1, 'NOT NULL',
                                 2, 'UNIQUE',
                                 3, 'PRIMARY KEY',
                                 4, 'NULL',
                                 5, 'TIMESTAMP',
                                 6, 'LOCAL UNIQUE',
                                 7, 'CHECK') CONST_TYPE
     , COLUMN_NAME
     , CHECK_CONDITION          -- Delete before use in versions earlier than Altibase v6.3.1.
  FROM SYSTEM_.SYS_USERS_ A,
       SYSTEM_.SYS_TABLES_ B,
       SYSTEM_.SYS_CONSTRAINTS_ C,
       SYSTEM_.SYS_COLUMNS_ D,
       SYSTEM_.SYS_CONSTRAINT_COLUMNS_ E
 WHERE A.USER_ID=C.USER_ID
   AND B.TABLE_ID = C.TABLE_ID
   AND A.USER_ID = D.USER_ID
   AND A.USER_ID = E.USER_ID
   AND B.TABLE_ID = D.TABLE_ID
   AND B.TABLE_ID = E.TABLE_ID
   AND C.CONSTRAINT_ID = E.CONSTRAINT_ID
   AND D.COLUMN_ID = E.COLUMN_ID
   AND A.USER_NAME <> 'SYSTEM_'
 ORDER BY USER_NAME, OBJECT_NAME, CONST_TYPE;
````

#### [CT02] List of Constraints, Tables, and Indexes Related to PK, FK, and UNIQUE - source block 2

````text
SELECT A.USER_NAME
     , B.TABLE_NAME
     , DECODE(C.CONSTRAINT_TYPE, 0, 'FK', 2, 'UNIQUE', 3, 'PK', 4, 'NULL') CONST_TYPE
     , C.CONSTRAINT_NAME CONST_NAME
     , DECODE(D.INDEX_NAME, C.CONSTRAINT_NAME, NULL, INDEX_NAME) INDEX_NAME
     , (SELECT TABLE_NAME
          FROM SYSTEM_.SYS_TABLES_
         WHERE TABLE_ID = C.REFERENCED_TABLE_ID) R_TABLE
     , (SELECT INDEX_NAME
          FROM SYSTEM_.SYS_INDICES_
         WHERE INDEX_ID = C.REFERENCED_INDEX_ID) R_INDEX
  FROM SYSTEM_.SYS_USERS_ A,
       SYSTEM_.SYS_TABLES_ B,
       SYSTEM_.SYS_CONSTRAINTS_ C LEFT OUTER JOIN SYSTEM_.SYS_INDICES_ D ON C.INDEX_ID = D.INDEX_ID
 WHERE C.TABLE_ID = B.TABLE_ID
   AND A.USER_NAME <> 'SYSTEM_'
   AND C.USER_ID = A.USER_ID
   AND C.CONSTRAINT_TYPE IN (3, 0, 2, 6) --PK, FK, UNIQUE, LOCAL UNIQUE
 ORDER BY TABLE_NAME, CONST_TYPE ;
````

#### [CT03] Composite Index Column Configuration List - source block 3

````text
SELECT D.USER_NAME
     , C.TABLE_NAME
     , B.INDEX_NAME
     , E.COLUMN_NAME
     , A.INDEX_COL_ORDER COL_ORDER
     , DECODE(A.SORT_ORDER, 'A', 'ASC', 'D', 'DESC') SORT
  FROM SYSTEM_.SYS_INDEX_COLUMNS_ A,
       SYSTEM_.SYS_INDICES_ B,
       SYSTEM_.SYS_TABLES_ C,
       SYSTEM_.SYS_USERS_ D,
       SYSTEM_.SYS_COLUMNS_ E
 WHERE D.USER_NAME <> 'SYSTEM_'
   AND C.TABLE_TYPE = 'T'
   AND A.INDEX_ID = B.INDEX_ID
   AND A.TABLE_ID = C.TABLE_ID
   AND A.USER_ID = D.USER_ID
   AND A.COLUMN_ID = E.COLUMN_ID
 ORDER BY USER_NAME, TABLE_NAME, INDEX_NAME, COL_ORDER ;
````

#### [CT04] Index Information Summary - source block 4

````text
SELECT A.USER_NAME
     , C.INDEX_NAME
     , C.INDEX_ID
     , B.TABLE_NAME
     , NVL(D.NAME, 'SYS_TBS_MEMORY') TBS_NAME
     , C.IS_UNIQUE
     , C.COLUMN_CNT
  FROM SYSTEM_.SYS_USERS_ A,
       SYSTEM_.SYS_TABLES_ B,
       SYSTEM_.SYS_INDICES_ C LEFT OUTER JOIN V$TABLESPACES D ON C.TBS_ID = D.ID
 WHERE A.USER_NAME <> 'SYSTEM_'
   AND B.TABLE_TYPE = 'T'
   AND C.TABLE_ID = B.TABLE_ID
   AND C.USER_ID = A.USER_ID
 ORDER BY B.TABLE_NAME, C.INDEX_NAME ;
````

### 13. Replication
Source path: `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/13. Replication__14058282.md`

#### [RP01] Replication Sender Information - source block 1

````text
SELECT REP_NAME
     , PEER_IP REMOTE_IP
     , PEER_PORT REMOTE_REP_PORT
     , DECODE(STATUS, 0, 'STOP', 1, 'RUN', 2, 'RETRY') AS STAUS
     , REPL_MODE                                                    -- Delete this column before use in Altibase v4.
     , DECODE(NET_ERROR_FLAG, 0, 'OK', 'ERROR') AS NETWORK
     , XSN
  FROM V$REPSENDER ;
````

#### [RP02] Replication Receiver Information - source block 2

````text
SELECT REP_NAME
     , PEER_IP REMOTE_IP
     , PEER_PORT REMOTE_REP_PORT
     , APPLY_XSN
  FROM V$REPRECEIVER ;
````

#### [RP03] Replication Gap - source block 3

````text
SELECT REP_NAME
     , REP_SN
     , REP_LAST_SN
     , REP_GAP
     , READ_FILE_NO
     , START_FLAG        -- Delete this column before use in versions earlier than Altibase v5.3.3.
  FROM V$REPGAP ;
````

#### [RP04] Overall Status of Replication - source block 4

````text
SELECT A.REPLICATION_NAME REP_NAME
     , D.HOST_IP REMOTE_IP
     , NVL(TO_CHAR(E.REP_GAP), '-') AS REP_GAP
     , A.XSN RESTART_XSN
     , DECODE(B.PEER_PORT, NULL, 'OFF', 'ON') AS SENDER
     , DECODE(C.PEER_PORT, NULL, 'OFF', 'ON') AS RECEIVER
  FROM SYSTEM_.SYS_REPL_HOSTS_ D ,
       SYSTEM_.SYS_REPLICATIONS_ A
       LEFT OUTER JOIN V$REPSENDER B ON A.REPLICATION_NAME = B.REP_NAME
       LEFT OUTER JOIN V$REPRECEIVER C ON A.REPLICATION_NAME = C.REP_NAME
       LEFT OUTER JOIN (SELECT REP_NAME, MAX(REP_GAP) REP_GAP
                          FROM V$REPGAP
                         GROUP BY REP_NAME) E ON A.REPLICATION_NAME = E.REP_NAME
 WHERE A.REPLICATION_NAME = D.REPLICATION_NAME
 ORDER BY REP_NAME ;
````

#### [RP05] Measure Accumulated Redo Log Files Due to Replication Delay - source block 5

````text
SELECT CASE2((BUFFER_MIN_SN < READ_SN),
                'REP BUFFER '||ROUND((BUFFER_MAX_SN-READ_SN)/(BUFFER_MAX_SN-BUFFER_MIN_SN)*100, 2)||' % LEFT ',
                (SELECT TO_CHAR(CUR_WRITE_LF_NO - READ_FILE_NO) FROM V$LFG, V$REPGAP)
            ) LOGFILE_FOR_REP
  FROM V$REPLOGBUFFER ;
````

#### [RP06] List of Tables to be Replicated - source block 6

````text
SELECT REPLICATION_NAME REP_NAME
     , LOCAL_USER_NAME||'.'||LOCAL_TABLE_NAME LOCAL_TBL
     , REMOTE_USER_NAME||'.'||REMOTE_TABLE_NAME REMOTE_TBL
  FROM SYSTEM_.SYS_REPL_ITEMS_
 ORDER BY 1, 2 ;
````

### 2. Statement
Source path: `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/2. Statement__14058256.md`

#### How to activate TIMED_STATISTICS - source block 1

````text
ALTER SYSTEM SET TIMED_STATISTICS=1;
````

#### [ST01] Total Number of Queries - source block 2

````text
SELECT COUNT(*) AS TOTAL_STMT_CNT FROM V$STATEMENT ;
````

#### [ST02] Query Information - source block 3

````text
SELECT SESSION_ID
     , ID STMT_ID
     , TX_ID
     , ROUND((PARSE_TIME+VALIDATE_TIME+OPTIMIZE_TIME)/1000000, 1) PREPARE_TIME
     , ROUND(FETCH_TIME/1000000, 1) FETCH_TIME
     , ROUND(EXECUTE_TIME/1000000, 1) EXECUTE_TIME
     , ROUND(TOTAL_TIME/1000000, 1) TOTAL_TIME
     , EXECUTE_FLAG
     , DECODE(LAST_QUERY_START_TIME, 0, '-', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + LAST_QUERY_START_TIME / (24*60*60), 'MM/DD HH:MI:SS')) LAST_START_TIME
     , NVL(LTRIM(QUERY), 'NONE') QUERY
  FROM V$STATEMENT
 ORDER BY EXECUTE_TIME DESC ;
````

#### [ST03] Number of Queries Currently Being Executed - source block 4

````text
SELECT COUNT(*) AS ACTIVE_STMT_CNT
  FROM V$STATEMENT
 WHERE EXECUTE_FLAG = 1 ;
````

#### [ST04] Query Information Currently Being Executed - source block 5

````text
SELECT SESSION_ID
     , ID STMT_ID
     , TX_ID
     , ROUND((PARSE_TIME+VALIDATE_TIME+OPTIMIZE_TIME)/1000000, 1) PREPARE_TIME
     , ROUND(FETCH_TIME/1000000, 1) FETCH_TIME
     , ROUND(EXECUTE_TIME/1000000, 1) EXECUTE_TIME
     , ROUND(TOTAL_TIME/1000000, 1) TOTAL_TIME
     , DECODE(LAST_QUERY_START_TIME, 0, '-', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + LAST_QUERY_START_TIME / (24*60*60), 'MM/DD HH:MI:SS')) LAST_START_TIME
     , NVL(LTRIM(QUERY), 'NONE') QUERY
  FROM V$STATEMENT
 WHERE EXECUTE_FLAG = 1
 ORDER BY EXECUTE_TIME DESC ;
````

#### [ST05] Long-running Query Execution Information - source block 6

````text
SELECT SESSION_ID
     , ID STMT_ID
     , TX_ID
     , ROUND((PARSE_TIME+VALIDATE_TIME+OPTIMIZE_TIME)/1000000, 1) PREPARE_TIME
     , ROUND(FETCH_TIME/1000000, 1) FETCH_TIME
     , ROUND(EXECUTE_TIME/1000000, 1) EXECUTE_TIME
     , ROUND(TOTAL_TIME/1000000, 1) TOTAL_TIME
     , DECODE(LAST_QUERY_START_TIME, 0, '-', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + LAST_QUERY_START_TIME / (24*60*60), 'MM/DD HH:MI:SS')) LAST_START_TIME
     , NVL(LTRIM(QUERY), 'NONE') QUERY
  FROM V$STATEMENT
 WHERE EXECUTE_FLAG = 1
   AND EXECUTE_TIME/1000000 > 600   -- If the user changes the query execution time condition, the user can change the value of this condition. The value is in seconds.
 ORDER BY EXECUTE_TIME DESC ;
````

#### [ST06] Last Query Information of DML Transaction That is Executed for a Long Time - source block 7

````text
SELECT ST.SESSION_ID
     , SS.COMM_NAME CLIENT_IP
     , SS.CLIENT_PID
     , SS.CLIENT_APP_INFO
     , (BASE_TIME - TR.FIRST_UPDATE_TIME) AS UTRANS_TIME
     , ROUND(EXECUTE_TIME/1000000, 1) EXECUTE_TIME
     , ROUND(TOTAL_TIME/1000000, 1) TOTAL_TIME
     , DECODE(LAST_QUERY_START_TIME, 0, '-', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + LAST_QUERY_START_TIME / (24*60*60), 'MM/DD HH:MI:SS')) LAST_START_TIME
     , NVL(LTRIM(ST.QUERY), 'NONE') QUERY
  FROM V$TRANSACTION TR,
       V$STATEMENT ST,
       V$SESSIONMGR,
       V$SESSION SS
 WHERE TR.ID = ST.TX_ID
   AND ST.SESSION_ID = SS.ID
   AND TR.FIRST_UPDATE_TIME != 0  -- 0:read only transaction
   AND (BASE_TIME - TR.FIRST_UPDATE_TIME) > 3600    -- If the user wants to change the execution time condition, the user can change the value of this condition. The value is in seconds.
ORDER BY UTRANS_TIME DESC ;
````

#### [ST07] Full Scan Query Information - source block 8

````text
SELECT SESSION_ID
     , S.COMM_NAME CLIENT_IP
     , S.CLIENT_PID
     , S.CLIENT_APP_INFO
     , DECODE(LAST_QUERY_START_TIME, 0, '-', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + LAST_QUERY_START_TIME / (24*60*60), 'MM/DD HH:MI:SS')) LAST_START_TIME
     , ROUND((PARSE_TIME+VALIDATE_TIME+OPTIMIZE_TIME)/1000000, 1) PREPARE_TIME
     , ROUND(FETCH_TIME/1000000, 1) FETCH_TIME
     , ROUND(EXECUTE_TIME/1000000, 1) EXECUTE_TIME
     , ROUND(TOTAL_TIME/1000000, 1) TOTAL_TIME
     , NVL(LTRIM(QUERY), 'NONE') QUERY
  FROM V$STATEMENT T,
       V$SESSION S
 WHERE S.ID = T.SESSION_ID
   AND (MEM_CURSOR_FULL_SCAN > 0 OR DISK_CURSOR_FULL_SCAN > 0)
   AND UPPER(QUERY) NOT LIKE '%INSERT%'
 ORDER BY EXECUTE_TIME DESC ;
````

#### [ST08] Full Scan Query Count Statistics - source block 9

````text
SELECT COUNT(EXECUTE_SUCCESS) EXECUTE_CNT
     , SUBSTR(LTRIM(QUERY), 1, 40) QUERY
  FROM V$STATEMENT
 WHERE (MEM_CURSOR_FULL_SCAN > 0 OR DISK_CURSOR_FULL_SCAN > 0)
   AND UPPER(QUERY) NOT LIKE '%INSERT%'
 GROUP BY QUERY
 ORDER BY EXECUTE_CNT DESC ;
````

#### [ST09] Query List by Session - source block 10

````text
SELECT SESSION_ID
     , ID STMT_ID
     , TX_ID
     , SUBSTR(QUERY, 1, 100) QUERY
  FROM V$STATEMENT
 ORDER BY 1, 2 ;
````

#### [ST10] Number of Statements Generated per Session - source block 11

````text
SELECT SE.ID SESSION_ID
     , COUNT(DISTINCT ST.ID) CURR_STMT_CNT_PER_SESSION
  FROM V$SESSION SE
     , V$STATEMENT ST
 WHERE 1=1
   AND SE.ID=ST.SESSION_ID
 GROUP BY SE.ID
 ORDER BY SE.ID;
````

### 3. Service Thread
Source path: `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/3. Service Thread__14058260.md`

#### [SV01] Service Thread Status - source block 1

````text
SELECT RUN_MODE
     , STATE
     , COUNT(*) CNT
  FROM V$SERVICE_THREAD
 GROUP BY RUN_MODE, STATE ;
````

#### [SV01] Service Thread Status - source block 2

````text
SELECT TYPE
     , STATE
     , COUNT(*) CNT
  FROM V$SERVICE_THREAD
 GROUP BY TYPE, STATE ;
````

#### [SV02] Check Service Thread Contention - source block 3

````text
SELECT NAME,
       MISS_COUNT,
       TRY_COUNT,
       ROUND(MISS_COUNT/TRY_COUNT*100, 2) PER
  FROM V$MUTEX
 WHERE NAME = 'MMT_SERVICE_THREAD_MUTEX'
 ORDER BY 4 DESC ;
````

### 4. Transaction & Lock
Source path: `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/4. Transaction & Lock__14058264.md`

#### [TL01] Transaction and Lock Information - source block 1

````text
SELECT TX.ID TX_ID
     , WAIT_FOR_TRANS_ID BLOCKED_TX_ID
     , DECODE(TX.STATUS,
                 0, 'BEGIN',
                 1, 'PRECOMMIT',
                 2, 'COMMIT_IN_MEMORY',
                 3, 'COMMIT',
                 4, 'ABORT',
                 5, 'BLOCKED',
                 6, 'END') STATUS
     , DECODE(TX.LOG_TYPE, 0, U1.USER_NAME, 'REPLICATION') USER_NAME
     , DECODE(TX.LOG_TYPE, 0, TX.SESSION_ID, RT.REP_NAME) SESSION_ID
     , DECODE(TX.LOG_TYPE, 0, ST.COMM_NAME, RR.PEER_IP) CLIENT_IP
     , DECODE(ST.AUTOCOMMIT_FLAG, 1, 'ON', 'OFF') AUTOCOMMIT
     , L.LOCK_DESC
     , DECODE(TX.FIRST_UPDATE_TIME,
                 0, '0',
                 TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + TX.FIRST_UPDATE_TIME / (60*60*24), 'MM/DD HH:MI:SS')) FIRST_UPDATE_TIME
     , U2.USER_NAME||'.'||T.TABLE_NAME TABLE_NAME
     , DECODE(TX.LOG_TYPE, 0, SUBSTR(ST.QUERY, 1, 10), 'REMOTE TX_ID '||REMOTE_TID) CURRENT_QUERY
     , DECODE(TX.DDL_FLAG, 0, 'NON-DDL', 'DDL') DDL
     , DECODE(TX.FIRST_UNDO_NEXT_LSN_FILENO, -1, '-', TX.FIRST_UNDO_NEXT_LSN_FILENO) 'LOGFILE#'
  FROM V$TRANSACTION TX,
       V$LOCK L
       LEFT OUTER JOIN (SELECT ST.*, SS.AUTOCOMMIT_FLAG, SS.DB_USERID, SS.COMM_NAME
                          FROM V$STATEMENT ST, V$SESSION SS
                         WHERE SS.ID = ST.SESSION_ID
                           AND SS.CURRENT_STMT_ID = ST.ID) ST ON L.TRANS_ID = ST.TX_ID
       LEFT OUTER JOIN V$REPRECEIVER_TRANSTBL RT ON L.TRANS_ID = RT.LOCAL_TID
       LEFT OUTER JOIN V$REPRECEIVER RR ON RT.REP_NAME = RR.REP_NAME
       LEFT OUTER JOIN V$LOCK_WAIT LW ON L.TRANS_ID = LW.TRANS_ID
       LEFT OUTER JOIN SYSTEM_.SYS_USERS_ U1 ON ST.DB_USERID = U1.USER_ID,
       SYSTEM_.SYS_TABLES_ T
       LEFT OUTER JOIN SYSTEM_.SYS_USERS_ U2 ON T.USER_ID = U2.USER_ID
 WHERE TX.ID = L.TRANS_ID
   AND T.TABLE_OID = L.TABLE_OID
   AND TX.STATUS != 6
ORDER BY TX.ID, ST.ID, TX.FIRST_UPDATE_TIME DESC ;
````

### 5. Redo Logfile
Source path: `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/5. Redo Logfile__14058266.md`

#### [LO01] Redo Log File Information - source block 1

````text
SELECT OLDEST_ACTIVE_LOGFILE OLDEST_LOGFILE
     , CURRENT_LOGFILE CURRENT_LOGFILE
     , CURRENT_LOGFILE-OLDEST_ACTIVE_LOGFILE LOGFILE_GAP
  FROM V$ARCHIVE ;
````

#### [LO02] Cumulative Number of Waits for Redo Log File Prepare - source block 2

````text
SELECT LF_PREPARE_WAIT_COUNT FROM V$LFG ;
````

### 6. GC (Garbage Collector)
Source path: `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/6. GC (Garbage Collector)__14058268.md`

#### [GC01] Memory DB GC Gap - source block 1

````text
SELECT GC_NAME
     , SCNOFTAIL
     , MINMEMSCNINTXS
     , ADD_OID_CNT-GC_OID_CNT GC_GAP
  FROM V$MEMGC ;
````

#### [GC02] Query Being Executed in a Transaction Where the Memory DB GC Is Waiting - source block 2

````text
SELECT SESSION_ID
     , TOTAL_TIME
     , EXECUTE_TIME
     , TX_ID
     , QUERY
  FROM V$STATEMENT
 WHERE TX_ID IN (SELECT ID
                   FROM V$TRANSACTION
                  WHERE MEMORY_VIEW_SCN = (SELECT MINMEMSCNINTXS FROM V$MEMGC LIMIT 1))
   AND EXECUTE_FLAG = 1
 ORDER BY 2 DESC ;
````

#### [GC02] Query Being Executed in a Transaction Where the Memory DB GC Is Waiting - source block 3

````text
SELECT ST.SESSION_ID
     , ST.TX_ID
     , TOTAL_TIME/1000000 'TOTAL(SEC)'
     , EXECUTE_TIME/1000000 'EXECUTE(SEC)'
     , FETCH_TIME/1000000 'FETCH(SEC)'
     , ST.QUERY
  FROM V$STATEMENT ST
     , V$TRANSACTION TX
 WHERE ST.TX_ID = TX.ID
   AND TX_ID IN (SELECT ID
                   FROM V$TRANSACTION
                      , (SELECT MINMEMSCNINTXS FROM V$MEMGC LIMIT 1) GC
                  WHERE MEMORY_VIEW_SCN = GC.MINMEMSCNINTXS
                     OR MIN_MEMORY_LOB_VIEW_SCN = GC.MINMEMSCNINTXS)
   AND ST.SESSION_ID != SESSION_ID()
   AND TX.SESSION_ID <> SESSION_ID()
 ORDER BY 3 DESC
;
````

### 7. Memory
Source path: `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/7. Memory__14058270.md`

#### [MS01] Altibase Memory Usage - source block 1

````text
SELECT NAME
     , ROUND(ALLOC_SIZE/1024/1024) 'ALLOC(M)'
     , ROUND(MAX_TOTAL_SIZE/1024/1024) 'MAX_TOTAL(M)'
  FROM V$MEMSTAT
 ORDER BY 3 DESC ;
````

#### [MS02] Total Memory Usage of Altibase - source block 2

````text
 SELECT ROUND(SUM(ALLOC_SIZE)/1024/1024) 'ALLOC(M)'
     , ROUND(SUM(MAX_TOTAL_SIZE)/1024/1024) 'MAX_TOTAL(M)'
  FROM V$MEMSTAT ;
````

### 8. Tablespace (TBS)
Source path: `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/8. Tablespace (TBS)__14058272.md`

#### [TS01] Memory Tablespace Usage - source block 1

````text
SELECT TBS_ID
     , TBS_TYPE
     , TBS_NAME
     , TO_CHAR(MAX/1024/1024, '999,999,999') 'MAX(M)'
     , TO_CHAR(TOTAL/1024/1024, '999,999,999') 'TOTAL(M)'
     , TO_CHAR(ALLOC/1024/1024, '999,999,999') 'ALLOC(M)'
     , TO_CHAR(USED/1024/1024, '999,999,999') 'USED(M)'
     , TO_CHAR((ROUND((USED/1024/1024), 0)/ROUND((TOTAL/1024/1024), 0))*100, '999.99') 'USAGE(%)'
     , STATE
     , AUTOEXTEND
  FROM (SELECT ID TBS_ID
             , DECODE(TYPE, 0, 'MEM_SYS_DIC', 1, 'MEM_SYS_DATA', 2, 'MEM_USER_DATA', 8, 'VOL_USER_DATA') TBS_TYPE
             , NAME TBS_NAME
             , DECODE(M.MAXSIZE, 140737488322560, D.MEM_MAX_DB_SIZE , 0 , T.TOTAL_PAGE_COUNT * T.PAGE_SIZE, M.MAXSIZE) MAX
             , M.ALLOC_PAGE_COUNT * T.PAGE_SIZE TOTAL
             , NVL(M.ALLOC_PAGE_COUNT-M.FREE_PAGE_COUNT, T.TOTAL_PAGE_COUNT)*PAGE_SIZE ALLOC
             , NVL(MT.USED, 0) USED
             , DECODE(T.STATE, 1, 'OFFLINE', 2, 'ONLINE', 5, 'OFFLINE BACKUP', 6, 'ONLINE BACKUP', 128, 'DROPPED', 'DISCARDED') STATE
             , DECODE(M.AUTOEXTEND_MODE, 1, 'ON', 'OFF') 'AUTOEXTEND'
          FROM V$DATABASE D
             , V$TABLESPACES T
             , (SELECT SPACE_ID
                     , SPACE_NAME
                     , ALLOC_PAGE_COUNT
                     , FREE_PAGE_COUNT
                     , DECODE(MAX_SIZE, 0, (SELECT VALUE1
                                              FROM V$PROPERTY
                                             WHERE NAME = 'VOLATILE_MAX_DB_SIZE'), MAX_SIZE) AS MAXSIZE
                     , AUTOEXTEND_MODE
                  FROM V$VOL_TABLESPACES
                UNION ALL
                SELECT SPACE_ID
                     , SPACE_NAME
                     , ALLOC_PAGE_COUNT
                     , FREE_PAGE_COUNT
                     , MAXSIZE
                     , AUTOEXTEND_MODE
                  FROM V$MEM_TABLESPACES ) M LEFT OUTER JOIN (SELECT TABLESPACE_ID, SUM((FIXED_USED_MEM + VAR_USED_MEM)) USED
                                                                FROM V$MEMTBL_INFO
                                                               GROUP BY TABLESPACE_ID ) MT ON M.SPACE_ID = MT.TABLESPACE_ID
         WHERE T.ID = M.SPACE_ID)
;
````

#### [TS01] Memory Tablespace Usage - source block 2

````text
SELECT TBS_ID
     , TBS_TYPE
     , TBS_NAME
     , TO_CHAR(MAX/1024/1024, '999,999,999') 'MAX(M)'
     , TO_CHAR(TOTAL/1024/1024, '999,999,999') 'TOTAL(M)'
     , TO_CHAR(ALLOC/1024/1024, '999,999,999') 'ALLOC(M)'
     , TO_CHAR(USED/1024/1024, '999,999,999') 'USED(M)'
     , TO_CHAR((ROUND((USED/1024/1024), 0)/ROUND((TOTAL/1024/1024), 0))*100, '999.99') 'USAGE(%)'
     , STATE
     , AUTOEXTEND
  FROM (SELECT ID TBS_ID
             , DECODE(TYPE, 0, 'MEM_SYS_DIC', 1, 'MEM_SYS_DATA', 2, 'MEM_USER_DATA', 8, 'VOL_USER_DATA') TBS_TYPE
             , NAME TBS_NAME
             , DECODE(MAXSIZE, 140737488322560, D.MEM_MAX_DB_SIZE, 0, ALLOCATED_PAGE_COUNT*PAGE_SIZE, MAXSIZE) MAX
             , ALLOCATED_PAGE_COUNT * PAGE_SIZE TOTAL
             , NVL(M.ALLOC_PAGE_COUNT-M.FREE_PAGE_COUNT, TOTAL_PAGE_COUNT)*PAGE_SIZE ALLOC
             , MT.USED USED
             , DECODE(STATE, 1, 'OFFLINE', 2, 'ONLINE', 5, 'OFFLINE BACKUP', 6, 'ONLINE BACKUP', 128, 'DROPPED', 'DISCARDED') STATE
             , DECODE(AUTOEXTEND_MODE, 1, 'ON', 'OFF') 'AUTOEXTEND'
          FROM V$DATABASE D
             , V$TABLESPACES T
             , V$MEM_TABLESPACES M
             , (SELECT TABLESPACE_ID
                     , SUM((FIXED_USED_MEM + VAR_USED_MEM)) USED
                  FROM V$MEMTBL_INFO
                 GROUP BY TABLESPACE_ID) MT
         WHERE T.ID = M.SPACE_ID
           AND ID = MT.TABLESPACE_ID )
;
````

#### [TS01] Memory Tablespace Usage - source block 3

````text
SELECT TBS_NAME
     , TO_CHAR(MAX/1024/1024, '999,999,999') 'MAX(M)'
     , TO_CHAR(TOTAL/1024, '999,999,999') 'TOTAL(M)'
     , TO_CHAR(ALLOC/1024, '999,999,999') 'ALLOC(M)'
     , TO_CHAR(USED/1024/1024, '999,999,999') 'USED(M)'
     , TO_CHAR((ROUND((USED/1024/1024), 0)/ROUND((TOTAL/1024), 0))*100, '999.99') 'USAGE(%)'
  FROM (SELECT 'SYS_TBS_MEMORY' TBS_NAME
             , MEM_MAX_DB_SIZE MAX
             , MEM_ALLOC_PAGE_COUNT * 32 TOTAL
             , (MEM_ALLOC_PAGE_COUNT - MEM_FREE_PAGE_COUNT) * 32 ALLOC
             , MTBL.USED USED
          FROM V$DATABASE DB
             , (SELECT SUM(FIXED_USED_MEM+VAR_USED_MEM) AS USED
                  FROM V$MEMTBL_INFO ) MTBL )
;
````

#### [TS02] Total Memory Tablespace Usage - source block 4

````text
SELECT MEM_MAX_DB_SIZE/1024/1024 'MAX(M)'
    , ROUND(MEM_ALLOC_PAGE_COUNT*32/1024, 2) 'TOTAL(M)'
    , TRUNC((MEM_ALLOC_PAGE_COUNT-MEM_FREE_PAGE_COUNT)*32/1024, 2) 'ALLOC(M)'
    , (SELECT ROUND(SUM((FIXED_USED_MEM + VAR_USED_MEM))/(1024*1024), 3)
         FROM V$MEMTBL_INFO) 'USED(M)'
    , TRUNC(((MEM_ALLOC_PAGE_COUNT-MEM_FREE_PAGE_COUNT)*32*1024)/MEM_MAX_DB_SIZE, 4)*100 'USAGE(%)'
 FROM V$DATABASE ;
````

#### [TS03] Disk Tablespace Usage - source block 5

````text
SELECT TBS_ID
     , TBS_TYPE
     , TBS_NAME
     , TO_CHAR(MAX/1024/1024, '999,999,999') 'MAX(M)'
     , TO_CHAR(TOTAL/1024/1024, '999,999,999') 'TOTAL(M)'
     , TO_CHAR(ALLOC/1024/1024, '999,999,999') 'ALLOC(M)'
     , TO_CHAR(USED/1024/1024, '999,999,999') 'USED(M)'
     , TO_CHAR((ROUND((USED/1024/1024), 0)/ROUND((MAX/1024/1024), 0))*100, '999.99') 'USAGE(%)'
     , STATE
     , AUTOEXTEND
  FROM (SELECT T.ID TBS_ID
             , DECODE(TYPE, 3, 'DISK_SYS_DATA', 4, 'DISK_USER_DATA', 5, 'DISK_SYS_TEMP', 6, 'DISK_USER_TEMP', 7, 'DISK_SYS_UNDO') TBS_TYPE
             , NAME TBS_NAME
             , D.MAX * PAGE_SIZE MAX
             , TOTAL_PAGE_COUNT * PAGE_SIZE TOTAL
             , DECODE(TYPE, 7, U.TOTAL_EXT_CNT * PROP.EXTENT_SIZE, ALLOCATED_PAGE_COUNT * PAGE_SIZE) ALLOC
             , DECODE(TYPE, 3, NVL(DS.USED, 0) , 4, NVL(DS.USED, 0) , 7, (U.TX_EXT_CNT+U.USED_EXT_CNT+U.UNSTEALABLE_EXT_CNT) * PROP.EXTENT_SIZE , ALLOCATED_PAGE_COUNT * PAGE_SIZE ) USED
             , DECODE(STATE, 1, 'OFFLINE', 2, 'ONLINE', 5, 'OFFLINE BACKUP', 6, 'ONLINE BACKUP', 128, 'DROPPED', 'DISCARDED') STATE
             , D.AUTOEXTEND
          FROM V$TABLESPACES T LEFT OUTER JOIN(SELECT SPACE_ID , SUM(TOTAL_USED_SIZE) USED
                  FROM X$SEGMENT
                 GROUP BY SPACE_ID) DS ON DS.SPACE_ID = T.ID
             , (SELECT SPACEID
                     , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
                     , DECODE(MAX(AUTOEXTEND), 1, 'ON', 'OFF') 'AUTOEXTEND'
                  FROM V$DATAFILES
                 GROUP BY SPACEID ) D
             , V$DISK_UNDO_USAGE U
             , (SELECT VALUE1 EXTENT_SIZE
                  FROM V$PROPERTY
                 WHERE NAME = 'SYS_UNDO_TBS_EXTENT_SIZE') PROP
         WHERE T.ID = D.SPACEID ) ;
````

#### [TS03] Disk Tablespace Usage - source block 6

````text
SELECT TBS_ID
     , TBS_TYPE
     , TBS_NAME
     , TO_CHAR(MAX/1024/1024, '999,999,999') 'MAX(M)'
     , TO_CHAR(TOTAL/1024/1024, '999,999,999') 'TOTAL(M)'
     , TO_CHAR(ALLOC/1024/1024, '999,999,999') 'ALLOC(M)'
     , TO_CHAR(USED/1024/1024, '999,999,999') 'USED(M)'
     , TO_CHAR((ROUND((USED/1024/1024), 0)/ROUND((MAX/1024/1024), 0))*100, '999.99') 'USAGE(%)'
     , STATE
     , AUTOEXTEND
  FROM (SELECT T.ID TBS_ID
             , DECODE(TYPE, 3, 'DISK_SYS_DATA', 4, 'DISK_USER_DATA', 5, 'DISK_SYS_TEMP', 6, 'DISK_USER_TEMP', 7, 'DISK_SYS_UNDO') TBS_TYPE
             , NAME TBS_NAME
             , D.MAX * PAGE_SIZE MAX
             , TOTAL_PAGE_COUNT*PAGE_SIZE TOTAL
             , DECODE(TYPE, 7, (SELECT (SUM(TOTAL_EXTENT_COUNT*PAGE_COUNT_IN_EXTENT)*PAGE_SIZE) FROM V$UDSEGS)
                             + (SELECT (SUM(TOTAL_EXTENT_COUNT*PAGE_COUNT_IN_EXTENT)*PAGE_SIZE) FROM V$TSSEGS) , /* UNDO */
                               ALLOCATED_PAGE_COUNT*PAGE_SIZE) ALLOC
             , DECODE(TYPE, 3, NVL(DS.USED, 0),
                            4, NVL(DS.USED, 0) /* SYS_TEMP */
                             , ALLOCATED_PAGE_COUNT*PAGE_SIZE) USED
             , DECODE(STATE, 1, 'OFFLINE', 2, 'ONLINE', 5, 'OFFLINE BACKUP', 6, 'ONLINE BACKUP', 128, 'DROPPED', 'DISCARDED') STATE
             , D.AUTOEXTEND
          FROM V$TABLESPACES T LEFT OUTER JOIN (SELECT SPACE_ID , SUM(TOTAL_USED_SIZE) USED FROM X$SEGMENT GROUP BY SPACE_ID ) DS ON DS.SPACE_ID = T.ID
             ,(SELECT SPACEID
                     , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
                     , DECODE(MAX(AUTOEXTEND), 1, 'ON', 'OFF') 'AUTOEXTEND'
                  FROM V$DATAFILES
                 GROUP BY SPACEID ) D
         WHERE T.ID = D.SPACEID)
;
````

#### [TS03] Disk Tablespace Usage - source block 7

````text
SELECT TBS_ID
     , TBS_TYPE
     , TBS_NAME
     , TO_CHAR(MAX/1024/1024, '999,999,999') 'MAX(M)'
     , TO_CHAR(TOTAL/1024/1024, '999,999,999') 'TOTAL(M)'
     , TO_CHAR(ALLOC/1024/1024, '999,999,999') 'ALLOC(M)'
     , TO_CHAR((ROUND((ALLOC/1024/1024), 0)/ROUND((MAX/1024/1024), 0))*100, '999.99') 'USAGE(%)'
     , STATE
     , AUTOEXTEND
  FROM (SELECT T.ID TBS_ID
             , DECODE(TYPE, 3, 'DISK_SYS_DATA', 4, 'DISK_USER_DATA', 5, 'DISK_SYS_TEMP', 6, 'DISK_USER_TEMP', 7, 'DISK_SYS_UNDO') TBS_TYPE
             , NAME TBS_NAME
             , D.MAX * PAGE_SIZE MAX
             , TOTAL_PAGE_COUNT * PAGE_SIZE TOTAL
             , DECODE(TYPE, 7, (SELECT (SUM(total_page_count) * PAGE_SIZE) FROM V$undo_seg) + (SELECT (SUM(ALLOC_PAGE_COUNT) * PAGE_SIZE) FROM v$tss_seg))
             , ALLOCATED_PAGE_COUNT * PAGE_SIZE ALLOC
             , DECODE(STATE, 1, 'OFFLINE', 2, 'ONLINE', 5, 'OFFLINE BACKUP', 6, 'ONLINE BACKUP', 128, 'DROPPED', 'DISCARDED') STATE
             , D.AUTOEXTEND
          FROM V$TABLESPACES T
             , (SELECT SPACEID
                     , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
                     , DECODE(MAX(AUTOEXTEND), 1, 'ON', 'OFF') 'AUTOEXTEND'
                  FROM V$DATAFILES
                 GROUP BY SPACEID) D
         WHERE T.ID = D.SPACEID)
;
````

#### [TS03] Disk Tablespace Usage - source block 8

````text
SELECT TBS_ID
     , TBS_TYPE
     , TBS_NAME
     , TO_CHAR(MAX/1024/1024, '999,999,999') 'MAX(M)'
     , TO_CHAR(TOTAL/1024/1024, '999,999,999') 'TOTAL(M)'
     , TO_CHAR(ALLOC/1024/1024, '999,999,999') 'ALLOC(M)'
     , TO_CHAR(USED/1024/1024, '999,999,999') 'USED(M)'
     , TO_CHAR((ROUND((USED/1024/1024), 0)/ROUND((MAX/1024/1024), 0))*100, '999.99') 'USAGE(%)'
     , STATE
     , AUTOEXTEND
  FROM (SELECT TBS.ID TBS_ID
             , DECODE(TYPE, 1, 'DISK_SYS_DATA', 2, 'DISK_USER_DATA', 3, 'DISK_SYS_TEMP', 4, 'DISK_USER_TEMP', 5, 'DISK_SYS_UNDO') TBS_TYPE
             , TBS.NAME TBS_NAME
             , DAT.MAX * TBS.PAGE_SIZE MAX
             , TBS.TOTAL_PAGE_COUNT * TBS.PAGE_SIZE TOTAL
             , DECODE(TBS.TYPE, 5, UNDO.ALLOC * TBS.PAGE_SIZE /* UNDO TABLESPACE*/
                                 , TBS.ALLOCATED_PAGE_COUNT * TBS.PAGE_SIZE) ALLOC
             , DECODE(TBS.TYPE, 3, TBS.ALLOCATED_PAGE_COUNT * TBS.PAGE_SIZE /* TEMP TABLESPACE */
                              , 5, UNDO.USED * TBS.PAGE_SIZE /* UNDO TABLESPACE*/
                                 , DECODE(SEG.USED, '', 0, (SEG.USED * TBS.PAGE_SIZE * TBS.A_EXTENT_PAGE_COUNT))) /* USER TABLESPACE & SYS_TBS_DATA */USED
             , DECODE(TBS.STATE, 1, 'ONLINE', 2, 'BEGIN BACKUP', 3, 'END BACKUP', 'NOT DEFINED') STATE
             , DAT.AUTOEXTEND
          FROM V$TABLESPACES TBS
          LEFT OUTER JOIN (SELECT SPACE_ID , SUM(EXTENT_TOTAL_COUNT) ALLOC , SUM(EXTENT_FULL_COUNT ) USED FROM X$SEGMENT GROUP BY SPACE_ID ) SEG ON TBS.ID = SEG.SPACE_ID
             , (SELECT SPACEID
                     , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
                     , DECODE(MAX(AUTOEXTEND), 1, 'ON', 'OFF') 'AUTOEXTEND'
                  FROM V$DATAFILES
                 GROUP BY SPACEID ) DAT
             , (SELECT SUM(ALLOCATED_PAGE_COUNT) ALLOC
                     , SUM(USED_PAGE_COUNT) USED
                  FROM V$UNDO_TBS ) UNDO
         WHERE TBS.ID = DAT.SPACEID )
;
````

#### [TS04] Disk Undo Tablespace Usage - source block 9

````text
SELECT T.NAME TBS_NAME
     , ROUND(D.MAX * PAGE_SIZE / 1024 /1024, 2) 'MAX(M)'
     , ROUND((TOTAL_PAGE_COUNT * PAGE_SIZE) / 1024 / 1024, 2) 'TOTAL(M)'
     , ROUND((U.TOTAL_EXT_CNT*PROP.EXTENT_SIZE)/1024/1024, 2) 'ALLOC(M)'
     , ROUND(((U.TX_EXT_CNT+U.USED_EXT_CNT+U.UNSTEALABLE_EXT_CNT) * PROP.EXTENT_SIZE)/1024/1024, 2) 'USED(M)'
     , ROUND((((U.TX_EXT_CNT+U.USED_EXT_CNT+U.UNSTEALABLE_EXT_CNT) * PROP.EXTENT_SIZE)/(D.MAX*PAGE_SIZE))*100, 2) 'USAGE(%)'
     , DECODE(STATE,1,'OFFLINE',2,'ONLINE',5,'OFFLINE BACKUP',6,'ONLINE BACKUP',128,'DROPPED', 'DISCARDED') STATE
     , D.AUTOEXTEND
  FROM V$TABLESPACES T
     , (SELECT SPACEID
             , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
             , DECODE(MAX(AUTOEXTEND),1,'ON','OFF') 'AUTOEXTEND'
          FROM V$DATAFILES
         GROUP BY SPACEID) D
     , V$DISK_UNDO_USAGE U
     , (SELECT VALUE1 EXTENT_SIZE FROM V$PROPERTY WHERE NAME = 'SYS_UNDO_TBS_EXTENT_SIZE') PROP
 WHERE T.ID = D.SPACEID
   AND T.ID = 3 ;
````

#### [TS05] Undo Tablespace Usage by Transaction - source block 10

````text
SELECT  DECODE(TX.SESSION_ID, -1, 'REP('||REP.REP_NAME||')', TX.SESSION_ID) SESSION_ID
      , TX.ID TX_ID
      , DECODE(TX.STATUS, 0, 'BEGIN', 1, 'PRECOMMIT', 2, 'COMMIT_IN_MEMORY', 3, 'COMMIT', 4, 'ABORT', 5, 'BLOCKED', 6, 'END') TX_STATUS
      , RPAD(DECODE(ST.EXECUTE_FLAG, NULL, 'REP('||REP.REP_NAME||')', 1, 'SQL ING', 0, 'SQL END'), 10) SQL_STATUS
      , RPAD(DECODE(TX.LOG_TYPE, 1, 'REP '||REP.PEER_IP||':'||REP.PEER_PORT, S.COMM_NAME||' PID:'||S.CLIENT_PID), 40) CLIENT_IP
      , RPAD(DECODE(TX.LOG_TYPE, 1, 'REP('||REP.REP_NAME||')', S.CLIENT_APP_INFO), 15) CLIENT_APP_INFO
      , RPAD(DECODE(S.AUTOCOMMIT_FLAG, 1, 'ON', 0, 'OFF', NULL, 'REP('||REP.REP_NAME||')'), 10) AUTOCOMMIT
      , RPAD(DECODE(TX.LOG_TYPE, 1, 'REP('||REP.REP_NAME||')', S.UTRANS_TIME_LIMIT), 15) UTRANS_TIMEOUT
      , DECODE(ST.LAST_QUERY_START_TIME, NULL, TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + TX.FIRST_UPDATE_TIME / (60*60*24), 'YYYY-MM-DD HH:MI:SS'), TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + ST.LAST_QUERY_START_TIME / (60*60*24), 'YYYY-MM-DD HH:MI:SS')) LAST_QUERY_START_TIME
      , ((((TSS.TOTAL_EXTENT_COUNT+TSS.TOTAL_EXTDIR_COUNT)*TSS.PAGE_COUNT_IN_EXTENT)+((UDS.TOTAL_EXTENT_COUNT+UDS.TOTAL_EXTDIR_COUNT)*UDS.PAGE_COUNT_IN_EXTENT))*TBS.PAGE_SIZE) /1024/1024 UNDO_USAGE
      , DECODE(TX.LOG_TYPE, 1, 'REMOTE_TX_ID : '||REP_TX.REMOTE_TID, SUBSTR(ST.QUERY, 1, 30)) QUERY
  FROM  V$TXSEGS TXS
      , V$TSSEGS TSS
      , V$UDSEGS UDS
      , V$TRANSACTION TX LEFT OUTER JOIN V$SESSION S ON TX.ID = S.TRANS_ID LEFT OUTER JOIN V$STATEMENT ST ON S.CURRENT_STMT_ID = ST.ID LEFT OUTER JOIN V$REPRECEIVER_TRANSTBL REP_TX ON TX.ID = REP_TX.LOCAL_TID LEFT OUTER JOIN V$REPRECEIVER REP ON REP_TX.REP_NAME = REP.REP_NAME
      , V$TABLESPACES TBS
 WHERE 1=1
   AND UDS.SPACE_ID = 3
   AND TXS.ID = UDS.TXSEG_ENTRY_ID
   AND TXS.ID = TSS.TXSEG_ENTRY_ID
   AND TXS.TRANS_ID = TX.ID
   AND TBS.ID = UDS.SPACE_ID
 ;
````

#### [TS06] Total Tablespace Usage - source block 11

````text
SELECT TBS_ID
     , TBS_TYPE
     , TBS_NAME
     , TO_CHAR(MAX/1024/1024, '999,999,999') 'MAX(M)'
     , TO_CHAR(TOTAL/1024, '999,999,999') 'TOTAL(M)'
     , TO_CHAR(ALLOC/1024, '999,999,999') 'ALLOC(M)'
     , TO_CHAR(USED/1024/1024, '999,999,999') 'USED(M)'
     , TO_CHAR((ROUND((TOTAL/1024), 0)/ROUND((MAX/1024/1024), 0))*100, '999.99') 'USAGE(%)'
      , '' STATE
      , '' 'AUTOEXTEND'
  FROM (SELECT '' TBS_ID
             , 'ALL_MEM_TBS' TBS_TYPE
             , '-' TBS_NAME
             , MEM_MAX_DB_SIZE MAX
             , MEM_ALLOC_PAGE_COUNT*32 TOTAL
             , (MEM_ALLOC_PAGE_COUNT-MEM_FREE_PAGE_COUNT)*32 ALLOC
             , (SELECT SUM(FIXED_USED_MEM + VAR_USED_MEM)
                  FROM V$MEMTBL_INFO) USED
          FROM V$DATABASE )
UNION ALL
SELECT TBS_ID
     , TBS_TYPE
     , TBS_NAME
     , TO_CHAR(MAX/1024/1024, '999,999,999') 'MAX(M)'
     , TO_CHAR(TOTAL/1024/1024, '999,999,999') 'TOTAL(M)'
     , TO_CHAR(ALLOC/1024/1024, '999,999,999') 'ALLOC(M)'
     , TO_CHAR(USED/1024/1024, '999,999,999') 'USED(M)'
     , TO_CHAR((ROUND((USED/1024/1024), 0)/ROUND((TOTAL/1024/1024), 0))*100, '999.99') 'USAGE(%)'
     , STATE
     , AUTOEXTEND
  FROM (SELECT ID TBS_ID
             , DECODE(TYPE, 0, 'MEM_SYS_DIC', 1, 'MEM_SYS_DATA', 2, 'MEM_USER_DATA', 8, 'VOL_USER_DATA') TBS_TYPE
             , NAME TBS_NAME
             , DECODE(M.MAXSIZE, 140737488322560, D.MEM_MAX_DB_SIZE , 0 , T.TOTAL_PAGE_COUNT * T.PAGE_SIZE, M.MAXSIZE) MAX
             , M.ALLOC_PAGE_COUNT * T.PAGE_SIZE TOTAL
             , NVL(M.ALLOC_PAGE_COUNT-M.FREE_PAGE_COUNT, T.TOTAL_PAGE_COUNT)*PAGE_SIZE ALLOC
             , NVL(MT.USED, 0) USED
             , DECODE(T.STATE, 1, 'OFFLINE', 2, 'ONLINE', 5, 'OFFLINE BACKUP', 6, 'ONLINE BACKUP', 128, 'DROPPED', 'DISCARDED') STATE
             , DECODE(M.AUTOEXTEND_MODE, 1, 'ON', 'OFF') 'AUTOEXTEND'
          FROM V$DATABASE D
             , V$TABLESPACES T
             , (SELECT SPACE_ID
                     , SPACE_NAME
                     , ALLOC_PAGE_COUNT
                     , FREE_PAGE_COUNT
                     , DECODE(MAX_SIZE, 0, (SELECT VALUE1
                                              FROM V$PROPERTY
                                              WHERE NAME = 'VOLATILE_MAX_DB_SIZE'), MAX_SIZE) AS MAXSIZE
                     , AUTOEXTEND_MODE
                  FROM V$VOL_TABLESPACES
                 UNION ALL
                SELECT SPACE_ID
                     , SPACE_NAME
                     , ALLOC_PAGE_COUNT
                     , FREE_PAGE_COUNT
                     , MAXSIZE
                     , AUTOEXTEND_MODE
                  FROM V$MEM_TABLESPACES ) M LEFT OUTER JOIN (SELECT TABLESPACE_ID, SUM((FIXED_USED_MEM + VAR_USED_MEM)) USED
                                                                FROM V$MEMTBL_INFO
                                                               GROUP BY TABLESPACE_ID ) MT ON M.SPACE_ID = MT.TABLESPACE_ID
         WHERE T.ID = M.SPACE_ID)
UNION ALL
SELECT TBS_ID
     , TBS_TYPE
     , TBS_NAME
     , TO_CHAR(MAX/1024/1024, '999,999,999') 'MAX(M)'
     , TO_CHAR(TOTAL/1024/1024, '999,999,999') 'TOTAL(M)'
     , TO_CHAR(ALLOC/1024/1024, '999,999,999') 'ALLOC(M)'
     , TO_CHAR(USED/1024/1024, '999,999,999') 'USED(M)'
     , TO_CHAR((ROUND((USED/1024/1024), 0)/ROUND((MAX/1024/1024), 0))*100, '999.99') 'USAGE(%)'
     , STATE
     , AUTOEXTEND
  FROM (SELECT T.ID TBS_ID
             , DECODE(TYPE, 3, 'DISK_SYS_DATA', 4, 'DISK_USER_DATA', 5, 'DISK_SYS_TEMP', 6, 'DISK_USER_TEMP', 7, 'DISK_SYS_UNDO') TBS_TYPE
             , NAME TBS_NAME
             , D.MAX * PAGE_SIZE MAX
             , TOTAL_PAGE_COUNT * PAGE_SIZE TOTAL
             , DECODE(TYPE, 7, U.TOTAL_EXT_CNT * PROP.EXTENT_SIZE, ALLOCATED_PAGE_COUNT * PAGE_SIZE) ALLOC
             , DECODE(TYPE, 3, NVL(DS.USED, 0) , 4, NVL(DS.USED, 0) , 7, (U.TX_EXT_CNT+U.USED_EXT_CNT+U.UNSTEALABLE_EXT_CNT) * PROP.EXTENT_SIZE , ALLOCATED_PAGE_COUNT * PAGE_SIZE ) USED
             , DECODE(STATE, 1, 'OFFLINE', 2, 'ONLINE', 5, 'OFFLINE BACKUP', 6, 'ONLINE BACKUP', 128, 'DROPPED', 'DISCARDED') STATE
             , D.AUTOEXTEND
          FROM V$TABLESPACES T LEFT OUTER JOIN(SELECT SPACE_ID , SUM(TOTAL_USED_SIZE) USED
                  FROM X$SEGMENT
                 GROUP BY SPACE_ID) DS ON DS.SPACE_ID = T.ID
             , (SELECT SPACEID
                     , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
                     , DECODE(MAX(AUTOEXTEND), 1, 'ON', 'OFF') 'AUTOEXTEND'
                  FROM V$DATAFILES
                 GROUP BY SPACEID ) D
             , V$DISK_UNDO_USAGE U
             , (SELECT VALUE1 EXTENT_SIZE
                  FROM V$PROPERTY
                 WHERE NAME = 'SYS_UNDO_TBS_EXTENT_SIZE') PROP
         WHERE T.ID = D.SPACEID ) ;
````

#### [TS07] Memory Tablespace Data File Checkpoint Path - source block 12

````text
SELECT M.SPACE_ID TBS_ID,
      SPACE_NAME TBS_NAME,
      CHECKPOINT_PATH
 FROM V$MEM_TABLESPACES M,
      V$MEM_TABLESPACE_CHECKPOINT_PATHS C
WHERE M.SPACE_ID = C.SPACE_ID ;
````

#### [TS08] Memory Tablespace Data File - source block 13

````text
SELECT MEM_DATA_FILE DATAFILE_NAME
 FROM V$STABLE_MEM_DATAFILES ;
````

#### [TS09] Disk Tablespace Data File - source block 14

````text
 SELECT B.NAME TBS_NAME,
       A.ID 'FILE#',
       A.NAME DATAFILE_NAME,
       CURRSIZE*8/1024 'ALLOC(M)',
       ROUND(CASE2(A.MAXSIZE=0, CURRSIZE, A.MAXSIZE)*8/1024) 'MAX(M)',
       DECODE(AUTOEXTEND, 0, 'OFF', 'ON') 'AUTOEXTEND'
  FROM V$DATAFILES A,
       V$TABLESPACES B
 WHERE B.ID = A.SPACEID
 ORDER BY B.NAME, A.ID
;
````

#### [TS10] I/O Per Disk Tablespace Data File - source block 15

````text
SELECT NAME TBS_NAME,
       A.PHYRDS PHY_READ,
       A.PHYWRTS PHY_WRITE,
       A.PHYRDS+A.PHYWRTS PHY_TOTAL,
       TRUNC(A.PHYRDS/READ_SUM*100,2) 'READ(%)',
       TRUNC(A.PHYWRTS/WRITE_SUM*100,2) 'WRITE(%)',
       TRUNC( (A.PHYRDS+A.PHYWRTS) / (READ_SUM+WRITE_SUM) * 100 , 2) 'TOTAL(%)',
       A.AVGIOTIM AVG_IO_TIME
  FROM V$FILESTAT A,
       V$DATAFILES B,
       (SELECT SUM(PHYRDS) READ_SUM,
               SUM(PHYWRTS) WRITE_SUM
          FROM V$FILESTAT ) C
 WHERE A.SPACEID = B.SPACEID
       AND A.FILEID = B.ID
       AND READ_SUM > 0
       AND WRITE_SUM > 0
 ORDER BY A.PHYRDS+A.PHYWRTS DESC, ROWNUM DESC
;
````

#### [TS11] Single Page Read I/O per Disk Tablespace Data File - source block 16

````text
SELECT B.NAME TBS_NAME,
       A.SINGLEBLKRDS READ_CNT_PER_PAGE,
       A.SINGLEBLKRDTIM READ_TIME_PER_PAGE,
       TRUNC(A.SINGLEBLKRDTIM/A.SINGLEBLKRDS,2) AVERAGE_TIME
  FROM V$FILESTAT A,
       V$DATAFILES B
 WHERE A.SPACEID = B.SPACEID
       AND A.FILEID = B.ID
       AND A.SINGLEBLKRDS > 0
 ORDER BY AVERAGE_TIME DESC
;
````

#### [TS12] Temporary Tablespace Usage - source block 17

````text
SELECT SUM(NORMAL_AREA_SIZE) SUM_NORMAL_AREA_SIZE
 FROM X$TEMPTABLE_STATS
WHERE DROP_TIME = '19700101_090000' ;
````

#### [TS13] Temporary Tablespace Usage by Transaction - source block 18

````text
SELECT NORMAL_AREA_SIZE
 FROM X$TEMPTABLE_STATS T,
      V$STATEMENT STMT
WHERE T.TRANSACTION_ID = STMT.TX_ID ;
````

#### [TS14] Overall Tablespace Status - source block 19

````text
SELECT NAME TBS_NAME,
      DECODE(STATE, 1, 'OFFLINE',
                    2, 'ONLINE',
                    5, 'OFFLINE BACKUP',
                    6, 'ONLINE BACKUP',
                    128, 'DROPPED', 'DISCARD') STATE
 FROM V$TABLESPACES ;
````

### 9. Disk Buffer
Source path: `arch/Home/Altibase Monitoring Queries Guide/3. Monitoring Elements and Corresponding Monitoring Queries/9. Disk Buffer__14058274.md`

#### [DB01] Disk Buffer Hit Ratio - source block 1

````text
SELECT HIT_RATIO 'HIT_RATIO(%)' FROM V$BUFFPOOL_STAT ;
````

### ALTIBASE HDB 4.3.9.x
Source path: `FAQE/Home/08. Monitoring/Disk table and index usage/ALTIBASE HDB 4.3.9.x__16876229.md`

#### Disk table usage query - source block 1

````text
set linesize 1024;
set colsize 20;
SELECT U.USER_NAME 'USER_NAME'                                                                                      -- Database user
     , TBL.TABLE_NAME 'TABLE_NAME'                                                                                  -- Table name
     , TBS.NAME 'TBS_NAME'                                                                                          -- Name of the tablespace to which the table belongs
     , TO_CHAR((TBS.TOTAL_PAGE_COUNT * TBS.PAGE_SIZE)/1024 , '999,999,999') 'TBS_MAX(KB)'                           -- Maximum size of tablespace
     , TO_CHAR((TBS.A_EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_TOTAL_COUNT)/1024, '999,999,999') 'ALLOC(KB)'  -- The total size allocated from the table
     , TO_CHAR((TBS.A_EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_FULL_COUNT)/1024, '999,999,999') 'USED(KB)'    -- Actual usage of the table (data usage)
     , TO_CHAR((((TBS.A_EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_TOTAL_COUNT)/(TBS.TOTAL_PAGE_COUNT * TBS.PAGE_SIZE))*100), '99.9') 'USAGE(%)' -- Utilization based on the maximum size of the tablespace
  FROM X$SEGMENT SEG
     , SYSTEM_.SYS_TABLES_ TBL
     , V$TABLESPACES TBS
     , SYSTEM_.SYS_USERS_ U
 WHERE SEG.TABLE_OID = TBL.TABLE_OID
   AND SEG.SPACE_ID = TBL.TBS_ID
   AND SEG.SPACE_ID = TBS.ID
   AND TBL.USER_ID = U.USER_ID
   AND TBL.TABLE_TYPE = 'T'
   AND SEG.SEGMENT_TYPE = 6
 ORDER BY USER_NAME, TABLE_NAME
 ;
````

#### Disk table usage query - source block 2

````text
USER_NAME             TABLE_NAME            TBS_NAME              TBS_MAX(KB)      ALLOC(KB)        USED(KB)         USAGE(%)
----------------------------------------------------------------------------------------------------------------------------------------------
SYS                   CUSTOMER              USER_DATA                2,097,152              256                0       0.0
SYS                   DEPARTMENT            SYS_TBS_DATA               254,976              256                0        .1
SYS                   DISK_T                USER_DATA                2,097,152          851,200          850,944      40.6
SYS                   EMPLOYEE              SYS_TBS_DATA               254,976              256                0        .1
SYS                   ORDERS                USER_DATA                2,097,152              256                0       0.0
5 rows selected.
````

#### Disk index usage query - source block 3

````text
set linesize 1024
set colsize 20
SELECT U.USER_NAME AS 'USER_NAME'           -- Database user
     , TBL.TABLE_NAME AS 'TABLE_NAME'       -- Table name
     , IDX.INDEX_NAME AS 'INDEX_NAME'       -- Index name
     , TBS.NAME AS 'TBS_NAME'               -- Tablespace name to which the index belongs
     , TO_CHAR((TBS.TOTAL_PAGE_COUNT * TBS.PAGE_SIZE)/1024 , '999,999,999') AS 'TBS_MAX(KB)'                            -- Maximum size of table space
     , TO_CHAR((TBS.A_EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_TOTAL_COUNT)/1024, '999,999,999') AS 'ALLOC(KB)'   -- Total size allocated from the index
     , TO_CHAR((TBS.A_EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_FULL_COUNT )/1024, '999,999,999') AS 'USED(KB)'    -- Actual usage of the index (data usage)
    , TO_CHAR((((TBS.A_EXTENT_PAGE_COUNT * SEG.EXTENT_TOTAL_COUNT)/TBS.TOTAL_PAGE_COUNT)*100), '99.9') AS 'USAGE(%)'    -- Utilization based on the maximum size of the tablespace
 FROM  X$SEGMENT SEG
     , V$INDEX I
     , SYSTEM_.SYS_INDICES_ IDX
     , SYSTEM_.SYS_TABLES_ TBL
     , V$TABLESPACES TBS
     , SYSTEM_.SYS_USERS_ U
 WHERE SEG.TABLE_OID = I.TABLE_OID
   AND SEG.SEGMENT_DESC = I.INDEX_SEG_DESC
   AND I.INDEX_ID = IDX.INDEX_ID
   AND IDX.TABLE_ID = TBL.TABLE_ID
   AND SEG.SPACE_ID = IDX.TBS_ID
   AND SEG.SPACE_ID = TBS.ID
   AND IDX.USER_ID = U.USER_ID
   AND TBL.TABLE_TYPE = 'T'
   AND SEG.SEGMENT_TYPE = 5
 ORDER BY U.USER_NAME, TBL.TABLE_NAME, IDX.INDEX_NAME
   ;
````

#### Disk index usage query - source block 4

````text
USER_NAME             TABLE_NAME            INDEX_NAME            TBS_NAME              TBS_MAX(KB)      ALLOC(KB)        USED(KB)         USAGE(%)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
SYS                   CUSTOMER              __SYS_IDX_ID_136      USER_DATA                2,097,152              256                0       0.0
SYS                   DEPARTMENT            DEP_IDX1              USER_IDX                 2,097,152              256                0       0.0
SYS                   DEPARTMENT            __SYS_IDX_ID_134      SYS_TBS_DATA               254,976              256                0        .1
SYS                   DISK_T                DISK_T_IDX_01         USER_IDX                 2,097,152          159,744          159,488       7.6
SYS                   EMPLOYEE              EMP_IDX1              USER_IDX                 2,097,152              256                0       0.0
SYS                   EMPLOYEE              __SYS_IDX_ID_135      SYS_TBS_DATA               254,976              256                0        .1
SYS                   ORDERS                ODR_IDX1              USER_IDX                 2,097,152              256                0       0.0
SYS                   ORDERS                __SYS_IDX_ID_137      USER_DATA                2,097,152              256                0       0.0
8 rows selected.
````

#### Reference - How to check the number of disk tables and indexes - source block 5

````text
set linesize 1024
set colsize 30
SELECT 'TABLE CNT : '||COUNT(*) TABLE_COUNT
  FROM V$DISKTBL_INFO D
     , SYSTEM_.SYS_TABLES_ T
 WHERE D.TABLE_OID = T.TABLE_OID ;
````

#### Reference - How to check the number of disk tables and indexes - source block 6

````text
set linesize 1024;
set colsize 30;
SELECT 'INDEX CNT : '||COUNT(*) INDEX_COUNT
  FROM SYSTEM_.SYS_INDICES_
 WHERE TABLE_ID IN (SELECT TABLE_ID
                      FROM SYSTEM_.SYS_TABLES_ T
                         , V$DISKTBL_INFO D
                     WHERE T.TABLE_OID = D.TABLE_OID);
````

### ALTIBASE HDB 5.1.5.x
Source path: `FAQE/Home/08. Monitoring/Disk table and index usage/ALTIBASE HDB 5.1.5.x__16876234.md`

#### Disk table - source block 1

````text
set linesize 1024
set colsize 30
SELECT U.USER_NAME USER_NAME                                                                                                    -- Database user
     , DECODE(TBL.IS_PARTITIONED, 'T', 'PARTITIONED', 'F', 'NON-PARTITIONED') PARTITIONED                                       -- PARTITIONED for a partitioned table, NON-PARTITIONED for a non-partitioned table
     , TBL.TABLE_NAME TABLE_NAME                                                                                                -- Table name
     , DECODE(TBL.IS_PARTITIONED, 'T', TBL.PARTITION_NAME, 'F', '-') PARTITIONED_TABLE                                          -- Partitioned table name
     , TBS.NAME TABLESPACE_NAME                                                                                                 -- Tablespace
     , TO_CHAR((D.MAX * TBS.PAGE_SIZE)/1024, '999,999,999') 'MAX(KB)'                                                           -- Maximum size of the tablespace to which the table belongs
     , TO_CHAR((TBS.EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_TOTAL_COUNT)/1024, '999,999,999') 'ALLOC(KB)'                -- Total size allocated to date
     , TO_CHAR((((TBS.EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_TOTAL_COUNT)/(D.MAX*TBS.PAGE_SIZE))*100), '99.99') 'USAGE(%)' -- Percentage of utilization compared to the maximum size of the tablespace
  FROM (SELECT TBL.USER_ID
             , DECODE(TBL.IS_PARTITIONED, 'F', TBL.TABLE_OID, 'T', PT.PARTITION_OID) TABLE_OID
             , TBL.TABLE_NAME
             , PT.PARTITION_NAME
             , DECODE(TBL.IS_PARTITIONED, 'F', TBL.TBS_ID, 'T', PT.TBS_ID) TBS_ID
             , TBL.IS_PARTITIONED
          FROM SYSTEM_.SYS_TABLES_ TBL LEFT OUTER JOIN SYSTEM_.SYS_TABLE_PARTITIONS_ PT ON TBL.TABLE_ID = PT.TABLE_ID
       ) TBL
     , V$SEGMENT SEG
     , SYSTEM_.SYS_USERS_ U
     , V$TABLESPACES TBS
     , (SELECT SPACEID
             , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
             , DECODE(MAX(AUTOEXTEND),1,'ON','OFF') 'AUTOEXTEND'
          FROM V$DATAFILES
         GROUP BY SPACEID) D
 WHERE 1=1
   AND SEG.SEGMENT_TYPE = 'TABLE'  /* 'TABLE' : table, 'INDEX' : index */
   AND SEG.TABLE_OID = TBL.TABLE_OID
   AND U.USER_ID = TBL.USER_ID
   AND D.SPACEID = TBL.TBS_ID
   AND TBS.ID = TBL.TBS_ID
 ORDER BY USER_NAME, PARTITIONED, TABLE_NAME, PARTITIONED_TABLE
;
````

#### Disk table - source block 2

````text
USER_NAME             PARTITIONED      TABLESPACE_NAME       TABLE_NAME            PARTITIONED_TABLE     MAX(KB)          ALLOC(KB)        USAGE(%)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
SYS                   NON-PARTITIONED  SYS_TBS_DISK_DATA     CUSTOMER              -                        2,097,152              256        .01
SYS                   NON-PARTITIONED  SYS_TBS_DISK_DATA     DEPARTMENT            -                        2,097,152              256        .01
SYS                   NON-PARTITIONED  SYS_TBS_DISK_DATA     EMPLOYEE              -                        2,097,152              256        .01
SYS                   NON-PARTITIONED  SYS_TBS_DISK_DATA     GOODS                 -                        2,097,152              256        .01
SYS                   NON-PARTITIONED  USER_DATA             ORDERS                -                        2,097,152              256        .01
SYS                   PARTITIONED      PART_DATA             PART_T1               P1                         262,144              512        .20
SYS                   PARTITIONED      PART_DATA             PART_T1               P2                         262,144              512        .20
SYS                   PARTITIONED      PART_DATA             PART_T1               P3                         262,144           18,176       6.93
SYS                   PARTITIONED      PART_DATA             PART_T2               P201406                    262,144            9,472       3.61
SYS                   PARTITIONED      PART_DATA             PART_T2               P201407                    262,144           18,944       7.23
SYS                   PARTITIONED      PART_DATA             PART_T2               P201408                    262,144            4,864       1.86
SYS                   PARTITIONED      PART_DATA             PART_T2               P201512                    262,144            7,168       2.73
SYS                   PARTITIONED      PART_DATA_DEF         PART_T2               PMAX                       262,144            8,192       3.13
SYS                   PARTITIONED      SYS_TBS_DISK_DATA     RANGE2                DEF                      2,097,152              256        .01
SYS                   PARTITIONED      SYS_TBS_DISK_DATA     RANGE2                Q1_2014                  2,097,152            1,536        .07
SYS                   PARTITIONED      SYS_TBS_DISK_DATA     RANGE2                Q2_2014                  2,097,152              768        .04
SYS                   PARTITIONED      SYS_TBS_DISK_DATA     RANGE2                Q3_2014                  2,097,152            2,304        .11
SYS                   PARTITIONED      SYS_TBS_DISK_DATA     RANGE2                Q4_2014                  2,097,152              256        .01
SYS                   PARTITIONED      SYS_TBS_DISK_DATA     RANGE_SALES           DEF                      2,097,152              256        .01
SYS                   PARTITIONED      SYS_TBS_DISK_DATA     RANGE_SALES           Q1_2014                  2,097,152              768        .04
SYS                   PARTITIONED      SYS_TBS_DISK_DATA     RANGE_SALES           Q2_2014                  2,097,152            1,536        .07
SYS                   PARTITIONED      SYS_TBS_DISK_DATA     RANGE_SALES           Q3_2014                  2,097,152            1,280        .06
SYS                   PARTITIONED      SYS_TBS_DISK_DATA     RANGE_SALES           Q4_2014                  2,097,152              768        .04
23 rows selected.
````

#### Disk Index - source block 3

````text
set linesize 1024
set colsize 20
SELECT U.USER_NAME USER_NAME                                                                                                   -- Database user
     , I_LIST.TABLE_NAME                                                                                                       -- Table name
     , DECODE(I_LIST.PARTITION_NAME, NULL, 'NON-PARTITIONED', I_LIST.PARTITION_NAME) PARTITIONED_NAME                          -- Partitioned table name, or NON-PARTITIONED for a non-partitioned table
     , I_LIST.INDEX_NAME INDEX_NAME                                                                                            -- Index name
     , DECODE(I_LIST.INDEX_PARTITION_NAME, NULL, 'NON-PARTITIONED', I_LIST.INDEX_PARTITION_NAME) PARTITIONED_INDEX             -- Partitioned index name
     , TBS.NAME TBS_NAME                                                                                                       -- Tablespace to which the index belongs
     , TO_CHAR((D.MAX * TBS.PAGE_SIZE)/1024, '999,999,999') 'MAX(KB)'                                                          -- Maximum size of table space
     , TO_CHAR((TBS.EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_TOTAL_COUNT)/1024, '999,999,999') 'ALLOC(KB)'               -- Total size allocated from the index
     , TO_CHAR((((TBS.EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_TOTAL_COUNT)/(D.MAX*TBS.PAGE_SIZE))*100), '99.99') 'USAGE(%)'   -- Percentage of utilization compared to the maximum size of the tablespace
  FROM (SELECT T.TABLE_NAME
             , PT.PARTITION_NAME
             , I.INDEX_NAME
             , PI.INDEX_PARTITION_NAME
             , DECODE(T.IS_PARTITIONED, 'F', I.TABLE_ID, 'T', PT.TABLE_ID) TABLE_ID
             , DECODE(T.IS_PARTITIONED, 'F', T.TABLE_OID, 'T', PT.PARTITION_OID) TABLE_OID
             , DECODE(I.IS_PARTITIONED, 'F', I.TBS_ID, 'T', PI.TBS_ID) TBS_ID
             , I.INDEX_ID
             , T.USER_ID
          FROM SYSTEM_.SYS_INDICES_ I LEFT OUTER JOIN SYSTEM_.SYS_INDEX_PARTITIONS_ PI ON PI.INDEX_ID = I.INDEX_ID LEFT OUTER JOIN SYSTEM_.SYS_TABLE_PARTITIONS_ PT ON PT.PARTITION_ID = PI.TABLE_PARTITION_ID LEFT OUTER JOIN SYSTEM_.SYS_TABLES_ T ON T.TABLE_ID = I.TABLE_ID ) I_LIST
     , V$SEGMENT SEG
     , V$INDEX I
     , V$TABLESPACES TBS
     , SYSTEM_.SYS_USERS_ U
     , (SELECT SPACEID
             , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
             , DECODE(MAX(AUTOEXTEND),1,'ON','OFF') 'AUTOEXTEND'
          FROM V$DATAFILES
         GROUP BY SPACEID) D
 WHERE 1=1
   AND SEG.TABLE_OID = I.TABLE_OID
   AND SEG.SEGMENT_PID = I.INDEX_SEG_PID
   AND SEG.SPACE_ID = I_LIST.TBS_ID
   AND I_LIST.INDEX_ID = I.INDEX_ID
   AND I_LIST.TABLE_OID = I.TABLE_OID
   AND I_LIST.TBS_ID = TBS.ID
   AND D.SPACEID = I_LIST.TBS_ID
   AND U.USER_ID = I_LIST.USER_ID
 ORDER BY I_LIST.TABLE_NAME, I_LIST.INDEX_NAME, I_LIST.PARTITION_NAME, I_LIST.INDEX_PARTITION_NAME
;
````

#### Disk Index - source block 4

````text
 USER_NAME             TABLE_NAME            PARTITIONED_NAME      INDEX_NAME            PARTITIONED_INDEX     TBS_NAME              MAX(KB)          ALLOC(KB)        USAGE(%)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
SYS                   CUSTOMER              NON-PARTITIONED       __SYS_IDX_ID_113      NON-PARTITIONED       SYS_TBS_DISK_DATA        2,097,152              256        .01
SYS                   DEPARTMENT            NON-PARTITIONED       DEP_IDX1              NON-PARTITIONED       SYS_TBS_DISK_DATA        2,097,152              256        .01
SYS                   DEPARTMENT            NON-PARTITIONED       __SYS_IDX_ID_111      NON-PARTITIONED       SYS_TBS_DISK_DATA        2,097,152              256        .01
SYS                   EMPLOYEE              NON-PARTITIONED       EMP_IDX1              NON-PARTITIONED       SYS_TBS_DISK_DATA        2,097,152              256        .01
SYS                   EMPLOYEE              NON-PARTITIONED       __SYS_IDX_ID_112      NON-PARTITIONED       SYS_TBS_DISK_DATA        2,097,152              256        .01
SYS                   GOODS                 NON-PARTITIONED       __SYS_IDX_ID_114      NON-PARTITIONED       SYS_TBS_DISK_DATA        2,097,152              256        .01
SYS                   GOODS                 NON-PARTITIONED       __SYS_IDX_ID_115      NON-PARTITIONED       SYS_TBS_DISK_DATA        2,097,152              256        .01
SYS                   ORDERS                NON-PARTITIONED       ODR_IDX1              NON-PARTITIONED       USER_IDX                 2,097,152              256        .01
SYS                   ORDERS                NON-PARTITIONED       ODR_IDX2              NON-PARTITIONED       USER_IDX                 2,097,152              256        .01
SYS                   ORDERS                NON-PARTITIONED       ODR_IDX3              NON-PARTITIONED       USER_IDX                 2,097,152              256        .01
SYS                   ORDERS                NON-PARTITIONED       __SYS_IDX_ID_116      NON-PARTITIONED       USER_DATA                2,097,152              256        .01
SYS                   PART_T1               P1                    PART_T1_IDX           P_IDX1                PART_IDX                   786,432              256        .03
SYS                   PART_T1               P2                    PART_T1_IDX           P_IDX2                PART_IDX                   786,432              256        .03
SYS                   PART_T1               P3                    PART_T1_IDX           P_IDX3                PART_IDX                   786,432            7,424        .94
14 rows selected.
````

#### Reference - How to check the number of disk tables and indexes - source block 5

````text
set linesize 1024;
set colsize 50;
SELECT DECODE(T.IS_PARTITIONED, 'T', 'PARTITIONED     TABLE CNT : '||PART_T.CNT, 'F', 'NON-PARTITIONED TABLE CNT : '||T.CNT) TABLE_COUNT
  FROM (SELECT IS_PARTITIONED
             , COUNT(*) CNT
          FROM V$DISKTBL_INFO D
             , SYSTEM_.SYS_TABLES_ T
         WHERE D.TABLE_OID = T.TABLE_OID
         GROUP BY IS_PARTITIONED) T
     , (SELECT COUNT(*) CNT FROM SYSTEM_.SYS_TABLE_PARTITIONS_ ) PART_T ;
````

#### Reference - How to check the number of disk tables and indexes - source block 6

````text
set linesize 1024;
set colsize 50;
SELECT DECODE(T.IS_PARTITIONED, 'T', 'PARTITIONED     INDEX CNT : '||PART_T.CNT, 'F', 'NON-PARTITIONED INDEX CNT : '||T.CNT) INDEX_COUNT
  FROM (SELECT IS_PARTITIONED
             , COUNT(*) CNT
          FROM SYSTEM_.SYS_INDICES_
         WHERE TABLE_ID IN (SELECT TABLE_ID
                              FROM SYSTEM_.SYS_TABLES_ T
                                 , V$DISKTBL_INFO D
                             WHERE T.TABLE_OID = D.TABLE_OID)
         GROUP BY IS_PARTITIONED) T
     , (SELECT COUNT(*) CNT FROM SYSTEM_.SYS_INDEX_PARTITIONS_) PART_T ;
````

### ALTIBASE HDB 5.3.x, 5.5.1, 6.1.1, 6.3.1
Source path: `FAQE/Home/08. Monitoring/Disk table and index usage/ALTIBASE HDB 5.3.x, 5.5.1, 6.1.1, 6.3.1__16876240.md`

#### Disk table - source block 1

````text
  set linesize 1024
  set colsize 20
  SELECT U.USER_NAME USER_NAME                                                                                            -- Database user
       , TBL.TABLE_NAME TABLE_NAME                                                                                        -- Table name
       , DECODE(TBL.IS_PARTITIONED, 'T', TBL.PARTITION_NAME, 'F', '-') PARTITIONED_TABLE                                  -- Partitioned table name
       , TBS.NAME TABLESPACE_NAME                                                                                         -- Tablespace
       , TO_CHAR((D.MAX * TBS.PAGE_SIZE)/1024, '999,999,999,999') 'MAX(KB)'                                               -- Maximum size of the tablespace to which the table belongs
       , TO_CHAR((TBS.EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.TOTAL_EXTENT_COUNT)/1024, '999,999,999,999') 'ALLOC(KB)'    -- Current allocated size
       , TO_CHAR(SEG.TOTAL_USED_SIZE/1024, '999,999,999,999') 'USED(KB)'                                                  -- Size of the allocated space that contains data
    FROM (SELECT TBL.USER_ID
               , DECODE(TBL.IS_PARTITIONED, 'F', TBL.TABLE_OID, 'T', PT.PARTITION_OID) TABLE_OID
               , TBL.TABLE_NAME
               , PT.PARTITION_NAME
               , DECODE(TBL.IS_PARTITIONED, 'F', TBL.TBS_ID, 'T', PT.TBS_ID) TBS_ID
               , TBL.IS_PARTITIONED
            FROM SYSTEM_.SYS_TABLES_ TBL LEFT OUTER JOIN SYSTEM_.SYS_TABLE_PARTITIONS_ PT ON TBL.TABLE_ID = PT.TABLE_ID
           WHERE TBL.TABLE_TYPE = 'T'
         ) TBL
       , (SELECT S.TABLE_OID, SUM(S.TOTAL_EXTENT_COUNT) TOTAL_EXTENT_COUNT, SUM(S.TOTAL_USED_SIZE) TOTAL_USED_SIZE
            FROM X$SEGMENT S
         WHERE S.SEGMENT_TYPE IN (6, 7) /* 6 : Table, 7 : LOB data(6.1.1 or later), 5 : Index */
           GROUP BY S.TABLE_OID) SEG
       , SYSTEM_.SYS_USERS_ U
       , V$TABLESPACES TBS
       , (SELECT SPACEID
               , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
               , DECODE(MAX(AUTOEXTEND),1,'ON','OFF') 'AUTOEXTEND'
            FROM V$DATAFILES
           GROUP BY SPACEID) D
   WHERE 1=1
     AND SEG.TABLE_OID = TBL.TABLE_OID
     AND U.USER_ID = TBL.USER_ID
     AND D.SPACEID = TBL.TBS_ID
     AND TBS.ID = TBL.TBS_ID
   ORDER BY USER_NAME, TABLE_NAME, PARTITIONED_TABLE
  ;
````

#### Disk table - source block 2

````text
  USER_NAME             TABLE_NAME            PARTITIONED_TABLE     TABLESPACE_NAME       MAX(KB)          ALLOC(KB)        USED(KB)
  -------------------------------------------------------------------------------------------------------------------------------------------------------
  SYS                   DISK_T                -                     USER_DATA                2,097,152          316,160              316,032
  SYS                   DISK_T2               -                     USER_DATA                2,097,152              256                    8
  SYS                   EMP                   -                     SYS_TBS_DISK_DATA        2,097,152              256                   16
  SYS                   PART_T1               P1                    PART_DATA                1,048,576              768                  520
  SYS                   PART_T1               P2                    PART_DATA                1,048,576              768                  520
  SYS                   PART_T1               P3                    PART_DATA                1,048,576          126,464              126,384
  SYS                   PART_T2               P201406               PART_DATA                1,048,576           11,520               11,280
  SYS                   PART_T2               P201407               PART_DATA                1,048,576           22,784               22,544
  SYS                   PART_T2               P201408               PART_DATA                1,048,576            5,888                5,648
  SYS                   PART_T2               P201512               PART_DATA                1,048,576            8,704                8,464
  SYS                   PART_T2               PMAX                  PART_DATA_DEF            1,048,576            9,728                9,592
  SYS                   RANGE2                DEF                   SYS_TBS_DISK_DATA        2,097,152              256                    8
  SYS                   RANGE2                Q1_2014               SYS_TBS_DISK_DATA        2,097,152          112,896              112,688
  SYS                   RANGE2                Q2_2014               SYS_TBS_DISK_DATA        2,097,152           56,576               56,352
  SYS                   RANGE2                Q3_2014               SYS_TBS_DISK_DATA        2,097,152            1,792                1,704
  SYS                   RANGE2                Q4_2014               SYS_TBS_DISK_DATA        2,097,152              768                  576
  SYS                   RANGE_SALES           DEF                   SYS_TBS_DISK_DATA        2,097,152              256                    8
  SYS                   RANGE_SALES           Q1_2014               SYS_TBS_DISK_DATA        2,097,152            5,888                5,648
  SYS                   RANGE_SALES           Q2_2014               SYS_TBS_DISK_DATA        2,097,152           11,520               11,280
  SYS                   RANGE_SALES           Q3_2014               SYS_TBS_DISK_DATA        2,097,152            8,704                8,464
  SYS                   RANGE_SALES           Q4_2014               SYS_TBS_DISK_DATA        2,097,152            4,096                3,952
  21 rows selected.
````

#### Disk Index - source block 3

````text
  -- Disk index usage column description
  -- USER_NAME	: Database user
  -- TABLE_NAME	: Table name
  -- PARTITIONED_NAME	: Partitioned table name, or NON-PARTITIONED for a non-partitioned table
  -- INDEX_NAME	: Index name
  -- PARTITIONED_INDEX	: Partitioned index name
  -- TBS_NAME	: Tablespace to which the index belongs
  -- MAX(KB)	: Max size of tablespace
  -- ALLOC(KB)	: Total size allocated
  -- USED(KB)	: Size of the allocated space that includes data
  -- USAGE(%)	: Percentage of utilization compared to the maximum size of the tablespace
  set linesize 1024
  set colsize 20
  SELECT U.USER_NAME USER_NAME
       , I_LIST.TABLE_NAME
       , DECODE(I_LIST.PARTITION_NAME, NULL, 'NON-PARTITIONED', I_LIST.PARTITION_NAME) PARTITIONED_NAME
       , I_LIST.INDEX_NAME INDEX_NAME
       , DECODE(I_LIST.INDEX_PARTITION_NAME, NULL, 'NON-PARTITIONED', I_LIST.INDEX_PARTITION_NAME) PARTITIONED_INDEX
       , TBS.NAME TBS_NAME
       , TO_CHAR((D.MAX * TBS.PAGE_SIZE)/1024, '999,999,999') 'MAX(KB)'
       , TO_CHAR((TBS.EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.TOTAL_EXTENT_COUNT)/1024, '999,999,999') 'ALLOC(KB)'
       , TO_CHAR(SEG.TOTAL_USED_SIZE/1024, '999,999,999,999') 'USED(KB)'
       , TO_CHAR(((SEG.TOTAL_USED_SIZE/(D.MAX*TBS.PAGE_SIZE))*100), '99.99') 'USAGE(%)'
    FROM (SELECT T.TABLE_NAME
               , PT.PARTITION_NAME
               , I.INDEX_NAME
               , PI.INDEX_PARTITION_NAME
               , DECODE(T.IS_PARTITIONED, 'F', I.TABLE_ID, 'T', PT.TABLE_ID) TABLE_ID
               , DECODE(T.IS_PARTITIONED, 'F', T.TABLE_OID, 'T', PT.PARTITION_OID) TABLE_OID
               , DECODE(I.IS_PARTITIONED, 'F', I.TBS_ID, 'T', PI.TBS_ID) TBS_ID
               , I.INDEX_ID
               , T.USER_ID
            FROM SYSTEM_.SYS_INDICES_ I LEFT OUTER JOIN SYSTEM_.SYS_INDEX_PARTITIONS_ PI ON PI.INDEX_ID = I.INDEX_ID
                                        LEFT OUTER JOIN SYSTEM_.SYS_TABLE_PARTITIONS_ PT ON PT.PARTITION_ID = PI.TABLE_PARTITION_ID
                                        LEFT OUTER JOIN SYSTEM_.SYS_TABLES_ T ON T.TABLE_ID = I.TABLE_ID AND T.TABLE_TYPE = 'T') I_LIST
       , X$SEGMENT SEG
       , V$INDEX I
       , V$TABLESPACES TBS
       , SYSTEM_.SYS_USERS_ U
       , (SELECT SPACEID
               , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
               , DECODE(MAX(AUTOEXTEND),1,'ON','OFF') 'AUTOEXTEND'
            FROM V$DATAFILES
           GROUP BY SPACEID) D
   WHERE 1=1
     AND SEG.TABLE_OID = I.TABLE_OID
     AND SEG.SEGMENT_PID = I.INDEX_SEG_PID
     AND SEG.SPACE_ID = I_LIST.TBS_ID
     AND I_LIST.INDEX_ID = I.INDEX_ID
     AND I_LIST.TABLE_OID = I.TABLE_OID
     AND I_LIST.TBS_ID = TBS.ID
     AND D.SPACEID = I_LIST.TBS_ID
     AND U.USER_ID = I_LIST.USER_ID
   ORDER BY I_LIST.TABLE_NAME, I_LIST.INDEX_NAME, I_LIST.PARTITION_NAME, I_LIST.INDEX_PARTITION_NAME
  ;
````

#### Disk Index - source block 4

````text
   USER_NAME             TABLE_NAME            PARTITIONED_NAME      INDEX_NAME            PARTITIONED_INDEX     TBS_NAME              MAX(KB)          ALLOC(KB)        USED(KB)            USAGE(%)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  SYS                   DISK_T                NON-PARTITIONED       DISK_T_IDX_01         NON-PARTITIONED       USER_IDX                 2,097,152           47,104               46,984      2.24
  SYS                   DISK_T2               NON-PARTITIONED       DISK_T2_IDX_01        NON-PARTITIONED       USER_IDX                 2,097,152              256                   16      0.00
  SYS                   EMP                   NON-PARTITIONED       EMP_IDX_01            NON-PARTITIONED       SYS_TBS_DISK_DATA        2,097,152              256                   32      0.00
  SYS                   PART_T1               P1                    PART_T1_IDX           P_IDX1                PART_IDX                 3,145,728              256                  216       .01
  SYS                   PART_T1               P2                    PART_T1_IDX           P_IDX2                PART_IDX                 3,145,728              256                  216       .01
  SYS                   PART_T1               P3                    PART_T1_IDX           P_IDX3                PART_IDX                 3,145,728           46,848               46,608      1.48
  SYS                   PART_T2               P201406               PART_T2_IDX_01        P201406               PART_IDX                 3,145,728            3,840                3,808       .12
  SYS                   PART_T2               P201407               PART_T2_IDX_01        P201407               PART_IDX                 3,145,728            7,680                7,528       .24
  SYS                   PART_T2               P201408               PART_T2_IDX_01        P201408               PART_IDX                 3,145,728            2,048                1,936       .06
  SYS                   PART_T2               P201512               PART_T2_IDX_01        P201512               PART_IDX                 3,145,728            3,072                2,856       .09
  SYS                   PART_T2               PMAX                  PART_T2_IDX_01        PMAX                  PART_IDX                 3,145,728            3,328                3,232       .10
  SYS                   PART_T2               P201406               PART_T2_IDX_02        P201406               PART_IDX                 3,145,728            3,840                3,808       .12
  SYS                   PART_T2               P201407               PART_T2_IDX_02        P201407               SYS_TBS_DISK_DATA        2,097,152            7,680                7,528       .36
  SYS                   PART_T2               P201408               PART_T2_IDX_02        P201408               SYS_TBS_DISK_DATA        2,097,152            2,304                1,936       .09
  SYS                   PART_T2               P201512               PART_T2_IDX_02        P201512               SYS_TBS_DISK_DATA        2,097,152            3,328                2,856       .14
  SYS                   PART_T2               PMAX                  PART_T2_IDX_02        PMAX                  SYS_TBS_DISK_DATA        2,097,152            3,584                3,232       .15
  16 rows selected.
````

#### Reference - How to check the count of disk table and index - source block 5

````text
set linesize 1024;
set colsize 50;
SELECT DECODE(T.IS_PARTITIONED, 'T', 'PARTITIONED     TABLE CNT : '||PART_T.CNT, 'F', 'NON-PARTITIONED TABLE CNT : '||T.CNT) TABLE_COUNT
  FROM (SELECT IS_PARTITIONED
             , COUNT(*) CNT
          FROM V$DISKTBL_INFO D
             , SYSTEM_.SYS_TABLES_ T
         WHERE D.TABLE_OID = T.TABLE_OID
         GROUP BY IS_PARTITIONED) T
     , (SELECT COUNT(*) CNT FROM SYSTEM_.SYS_TABLE_PARTITIONS_ ) PART_T ;
````

#### Reference - How to check the count of disk table and index - source block 6

````text
set linesize 1024;
set colsize 50;
SELECT DECODE(T.IS_PARTITIONED, 'T', 'PARTITIONED     INDEX CNT : '||PART_T.CNT, 'F', 'NON-PARTITIONED INDEX CNT : '||T.CNT) INDEX_COUNT
  FROM (SELECT IS_PARTITIONED
             , COUNT(*) CNT
          FROM SYSTEM_.SYS_INDICES_
         WHERE TABLE_ID IN (SELECT TABLE_ID
                              FROM SYSTEM_.SYS_TABLES_ T
                                 , V$DISKTBL_INFO D
                             WHERE T.TABLE_OID = D.TABLE_OID)
         GROUP BY IS_PARTITIONED) T
     , (SELECT COUNT(*) CNT FROM SYSTEM_.SYS_INDEX_PARTITIONS_) PART_T ;
````

### ALTIBASE HDB 4.3.9
Source path: `FAQE/Home/08. Monitoring/Disk tablespace usage/ALTIBASE HDB 4.3.9__16876249.md`

#### ALTIBASE HDB 4.3.9 - source block 1

````text
set linesize 1024;
set colsize 30;
SELECT TBS.NAME TBS_NAME                                                                                                    -- Disk tablespace name
     , TO_CHAR(ROUND(DAT.MAX * TBS.PAGE_SIZE / 1024 /1024, 2)) 'MAX(M)'                                                     -- Maximum size that can be allocated
     , ROUND(TBS.TOTAL_PAGE_COUNT * TBS.PAGE_SIZE / 1024 / 1024, 2) 'TOTAL(M)'                                              -- Total number of pages allocated so far
     , DECODE(TBS.TYPE, 5, ROUND( UNDO.ALLOC * TBS.PAGE_SIZE/1024/1024, 2) /* UNDO TABLESPACE*/
                         , ROUND( TBS.ALLOCATED_PAGE_COUNT * TBS.PAGE_SIZE / 1024 / 1024, 2) ) 'ALLOC(M)'                   -- Total of only 'used pages' excluding 'blank pages' among the allocated pages so far
     , DECODE(TBS.TYPE, 3, '-' /* TEMP TABLESPACE */
                      , 5, ROUND( UNDO.USED * TBS.PAGE_SIZE /1024/1024, 2) /* UNDO TABLESPACE*/                             -- Size of the pages in use at which data is loaded. TEMP TABLESPACE cannot be obtained.
                         , DECODE(SEG.USED, '', 0, ROUND((SEG.USED * TBS.PAGE_SIZE * TBS.A_EXTENT_PAGE_COUNT)/1024/1024, 2)) /* USER TABLESPACE & SYS_TBS_DATA */) 'USED(M)'
     , DECODE(TBS.TYPE, 5, ROUND( UNDO.ALLOC / DAT.MAX * 100, 2) --UNDO
                         , ROUND( TBS.ALLOCATED_PAGE_COUNT / DAT.MAX * 100, 2) ) 'USAGE(%)'
     , DECODE(TBS.STATE, 1, 'ONLINE', 2, 'BEGIN BACKUP', 3, 'END BACKUP', 'NOT DEFINED') STATE
     , DAT.AUTOEXTEND
  FROM V$TABLESPACES TBS LEFT OUTER JOIN (SELECT SPACE_ID , SUM(EXTENT_TOTAL_COUNT) ALLOC , SUM(EXTENT_FULL_COUNT ) USED
                                            FROM X$SEGMENT
                                            GROUP BY SPACE_ID
                                         ) SEG ON TBS.ID = SEG.SPACE_ID
     ,(SELECT SPACEID
             , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
             , DECODE(MAX(AUTOEXTEND), 1, 'ON', 'OFF') 'AUTOEXTEND'
          FROM V$DATAFILES
         GROUP BY SPACEID ) DAT
     , (SELECT SUM(ALLOCATED_PAGE_COUNT) ALLOC
             , SUM(USED_PAGE_COUNT) USED
          FROM V$UNDO_TBS ) UNDO
 WHERE TBS.ID = DAT.SPACEID;
````

#### ALTIBASE HDB 4.3.9 - source block 2

````text
TBS_NAME                        MAX(M)                          TOTAL(M)    ALLOC(M)    USED(M)                         USAGE(%)    STATE         AUTOEXTEND
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
SYS_TBS_DATA                    2049                            249         249         0                               12.15       ONLINE        ON
SYS_TBS_UNDO                    2048                            246         245.72      0.02                            12          ONLINE        ON
SYS_TBS_TEMP                    2048                            100         1           -                               0.05        ONLINE        ON
USER_DATA                       2048                            2048        832         831                             40.63       ONLINE        OFF
USER_IDX                        2048                            2048        157         155.75                          7.67        ONLINE        OFF
USER_IDX_TBS                    512                             512         1           0                               0.2         ONLINE        OFF
6 rows selected.
````

### ALTIBASE HDB 5.1.5
Source path: `FAQE/Home/08. Monitoring/Disk tablespace usage/ALTIBASE HDB 5.1.5__16876251.md`

#### Disk tablespace usage query - source block 1

````text
SET LINESIZE 1024;SET COLSIZE 30;SELECT  NAME TBS_NAME                                         -- Disk tablespace name
      , TO_CHAR(ROUND(D.MAX * PAGE_SIZE / 1024 /1024, 2)) 'MAX(M)'                             -- Max size of tablespace
      , ROUND(TOTAL_PAGE_COUNT * PAGE_SIZE / 1024 / 1024, 2) 'TOTAL(M)'                        -- Total number of pages allocated so far
      , DECODE(TYPE, 7, ROUND((SELECT (SUM(total_page_count) * PAGE_SIZE)/1024/1024
                                 FROM V$undo_seg)+
                              (SELECT (SUM(ALLOC_PAGE_COUNT) * PAGE_SIZE)/1024/1024
                                 FROM v$tss_seg), 2)
                      , ROUND(ALLOCATED_PAGE_COUNT * PAGE_SIZE / 1024 / 1024, 2)) 'ALLOC(M)'   -- Total of only 'used pages' excluding 'blank pages' among the allocated pages so far
      , DECODE(TYPE, 7, ROUND( ( (SELECT SUM(total_page_count) FROM V$undo_seg) +
                                 (SELECT SUM(ALLOC_PAGE_COUNT) FROM v$tss_seg ) ) / D.MAX  * 100, 2)
                      , ROUND(ALLOCATED_PAGE_COUNT / D.MAX * 100, 2))             'USAGE(%)'   -- ALLOC utilization rate compared to MAX
       , DECODE(STATE, 1, 'OFFLINE', 2, 'ONLINE', 5, 'OFFLINE BACKUP', 6, 'ONLINE BACKUP', 128, 'DROPPED', 'DISCARDED') STATE
       , D.AUTOEXTEND
  FROM V$TABLESPACES T
       ,(SELECT  SPACEID
              , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
              , DECODE(MAX(AUTOEXTEND), 1, 'ON', 'OFF') 'AUTOEXTEND'
           FROM V$DATAFILES
           GROUP BY SPACEID) D
 WHERE T.ID = D.SPACEID
;
````

#### Disk tablespace usage query - source block 2

````text
TBS_NAME                        MAX(M)                          TOTAL(M)    ALLOC(M)    USAGE(%)    STATE           AUTOEXTEND
----------------------------------------------------------------------------------------------------------------------------------------
SYS_TBS_DISK_DATA               2048                            100         0.25        0.01        ONLINE          ON
SYS_TBS_DISK_UNDO               2048                            100         2           0.1         ONLINE          ON
SYS_TBS_DISK_TEMP               2048                            100         0.25        0.01        ONLINE          ON
3 rows selected.
````

### ALTIBASE HDB 5.3.3, 5.3.5
Source path: `FAQE/Home/08. Monitoring/Disk tablespace usage/ALTIBASE HDB 5.3.3, 5.3.5__16876253.md`

#### Disk tablespace usage query - source block 1

````text
SET LINESIZE 1024;
SET COLSIZE 30;
SELECT NAME TBS_NAME                                                                                                            -- TBS_NAME : Disk tablespace name
     , TO_CHAR(D.MAX * PAGE_SIZE / 1024 /1024, '999,999,999') 'MAX(M)'                                                          -- MAX(M)   : Max size of tablespace
     , TO_CHAR(TOTAL_PAGE_COUNT*PAGE_SIZE/1024/1024, '999,999,999') 'TOTAL(M)'                                                  -- TOTAL(M) : Total page size allocated to date
     , DECODE(TYPE, 7, TO_CHAR((SELECT (SUM(TOTAL_EXTENT_COUNT*PAGE_COUNT_IN_EXTENT)*PAGE_SIZE)/1024/1024
                          FROM V$UDSEGS)+ (SELECT (SUM(TOTAL_EXTENT_COUNT*PAGE_COUNT_IN_EXTENT)*PAGE_SIZE)/1024/1024
                          FROM V$TSSEGS), '999,999,999') , /* UNDO */
                       TO_CHAR((ALLOCATED_PAGE_COUNT*PAGE_SIZE)/1024/1024, '999,999,999')) 'ALLOC(M)'                           -- ALLOC(M) : Total of only 'used pages' excluding 'blank pages' among the allocated pages so far
     , DECODE(TYPE, 3, TO_CHAR(NVL(DS.USED, 0)/1024/1024, '999,999,999'),
                    4, TO_CHAR(NVL(DS.USED, 0)/1024/1024, '999,999,999') /* SYS_TEMP */
                     , LPAD('-', 12)) 'USED(M)'                                                                                 -- USED(M)  : Size of the pages in use at which data is loaded. TEMP and UNDO cannot obtain USED.
     , DECODE(TYPE, 7, TO_CHAR(((SELECT SUM(TOTAL_EXTENT_COUNT*PAGE_COUNT_IN_EXTENT)
                                  FROM V$UDSEGS)+ (SELECT SUM(TOTAL_EXTENT_COUNT*PAGE_COUNT_IN_EXTENT)
                                  FROM V$TSSEGS)) / D.MAX* 100,  '99.99') ,          /* UNDO */
                    3, TO_CHAR(NVL(DS.USED, 0)/(D.MAX*PAGE_SIZE)* 100,  '99.99') ,
                    4, TO_CHAR(NVL(DS.USED, 0)/(D.MAX*PAGE_SIZE)* 100,  '99.99') ,   /* TEMP */
                       TO_CHAR(ALLOCATED_PAGE_COUNT / D.MAX * 100,  '99.99') ) 'USAGE(%)'                                       -- USAGE(%) : USED compared with MAX. For TEMP and UNDO, ALLOC compared with MAX.
     , DECODE(STATE, 1, 'OFFLINE', 2, 'ONLINE', 5, 'OFFLINE BACKUP', 6, 'ONLINE BACKUP', 128, 'DROPPED', 'DISCARDED') STATE     -- STATE    : Tablespace state
     , D.AUTOEXTEND
  FROM V$TABLESPACES T LEFT OUTER JOIN (SELECT SPACE_ID , SUM(TOTAL_USED_SIZE) USED
                                          FROM X$SEGMENT
                                         GROUP BY SPACE_ID ) DS ON DS.SPACE_ID = T.ID
     ,(SELECT SPACEID
             , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
             , DECODE(MAX(AUTOEXTEND), 1, 'ON', 'OFF') 'AUTOEXTEND'
          FROM V$DATAFILES
         GROUP BY SPACEID ) D
 WHERE T.ID = D.SPACEID
;
````

#### Disk tablespace usage query - source block 2

````text
TBS_NAME                        MAX(M)           TOTAL(M)         ALLOC(M)         USED(M)                   USAGE(%)         STATE           AUTOEXTEND
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
SYS_TBS_DISK_DATA                      2,048              217              217              211               10.32           ONLINE          ON
SYS_TBS_DISK_UNDO                      2,048              323              322                -               15.73           ONLINE          ON
SYS_TBS_DISK_TEMP                      2,048              100                0                -                 .01           ONLINE          ON
USER_DATA                              2,048            2,048              310              309               15.07           ONLINE          OFF
USER_IDX                               2,048            2,048               47               46                2.24           ONLINE          OFF
PART_DATA                              1,024            1,024              173              171               16.72           ONLINE          OFF
PART_DATA_DEF                          1,024            1,024               10                9                 .92           ONLINE          OFF
PART_IDX                               3,072            3,072               70               69                2.23           ONLINE          OFF
8 rows selected.
````

### ALTIBASE HDB 5.5.1, 6.1.1, 6.3.1
Source path: `FAQE/Home/08. Monitoring/Disk tablespace usage/ALTIBASE HDB 5.5.1, 6.1.1, 6.3.1__16876255.md`

#### Disk tablespace usage query - source block 1

````text
SET LINESIZE 1024;
SET COLSIZE 30;
SELECT DECODE(TYPE, 3, 'SYSTEM TABLESPACE', 4, 'USER DATA TABLESPACE', 5, 'SYSTEM TABLESPACE', 6, 'USER TEMP TABLESPACE', 7, 'SYSTEM TABLESPACE') TBS_TYPE
     , NAME TBS_NAME                                                                                                                                    -- TBS_NAME : Tablespace name
     , TO_CHAR((D.MAX * PAGE_SIZE / 1024 /1024), '999,999,999') 'MAX(M)'                                                                                -- MAX(M)   : Maximum size of tablespace
     , TO_CHAR((TOTAL_PAGE_COUNT * PAGE_SIZE)/1024/1024, '999,999,999') 'TOTAL(M)'                                                                      -- TOTAL(M) : Total number of pages allocated so far
     , DECODE(TYPE, 7, TO_CHAR((U.TOTAL_EXT_CNT*PROP.EXTENT_SIZE)/1024/1024, '999,999,999')
                     , TO_CHAR((ALLOCATED_PAGE_COUNT * PAGE_SIZE)/1024/1024, '999,999,999')) 'ALLOC(M)'                                                 -- ALLOC(M) : Total of only 'used pages' excluding 'blank pages' among the allocated pages so far.
     , DECODE(TYPE, 3, TO_CHAR(NVL(DS.USED, 0)/1024/1024, '999,999,999'),
                    4, TO_CHAR(NVL(DS.USED, 0)/1024/1024, '999,999,999'),
                    7, TO_CHAR(((U.TX_EXT_CNT+U.USED_EXT_CNT+U.UNSTEALABLE_EXT_CNT) * PROP.EXTENT_SIZE)/1024/1024, '999,999,999')
                     , LPAD('-', 12))'USED(M)'                                                                                                          -- USED(M)  : Size of the pages in which the data is loaded
     , DECODE(TYPE, 7, TO_CHAR((((U.TX_EXT_CNT+U.USED_EXT_CNT+U.UNSTEALABLE_EXT_CNT) * PROP.EXTENT_SIZE)/(D.MAX*PAGE_SIZE))*100, '99.99'),
                    3, TO_CHAR(NVL(DS.USED, 0)/(D.MAX*PAGE_SIZE)* 100, '99.99'),
                    4, TO_CHAR(NVL(DS.USED, 0)/(D.MAX*PAGE_SIZE)* 100, '99.99')
                     , TO_CHAR((ALLOCATED_PAGE_COUNT/D.MAX) * 100, '99.99')) 'USAGE(%)'                                                                 -- USAGE(%) : Usage (USED versus MAX)
     , DECODE(STATE, 1, 'OFFLINE', 2, 'ONLINE', 5, 'OFFLINE BACKUP', 6, 'ONLINE BACKUP', 128, 'DROPPED', 'DISCARDED') STATE                             -- STATE    : Tablespace state
     , D.AUTOEXTEND
  FROM V$TABLESPACES T LEFT OUTER JOIN(SELECT SPACE_ID , SUM(TOTAL_USED_SIZE) USED
                                         FROM X$SEGMENT
                                        GROUP BY SPACE_ID) DS ON DS.SPACE_ID = T.ID
     , (SELECT SPACEID
             , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
             , DECODE(MAX(AUTOEXTEND), 1, 'ON', 'OFF') 'AUTOEXTEND'
          FROM V$DATAFILES
         GROUP BY SPACEID ) D
     , V$DISK_UNDO_USAGE U
     , (SELECT VALUE1 EXTENT_SIZE
          FROM V$PROPERTY
         WHERE NAME = 'SYS_UNDO_TBS_EXTENT_SIZE') PROP
 WHERE T.ID = D.SPACEID ;
````

#### Disk tablespace usage query - source block 2

````text
TBS_TYPE              TBS_NAME                        MAX(M)           TOTAL(M)         ALLOC(M)         USED(M)                   USAGE(%)         STATE           AUTOEXTEND
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
SYSTEM TABLESPACE     SYS_TBS_DISK_DATA                      2,048              952              952              952               46.46           ONLINE          ON
SYSTEM TABLESPACE     SYS_TBS_DISK_UNDO                      2,048              704                8                8                 .39           ONLINE          ON
SYSTEM TABLESPACE     SYS_TBS_DISK_TEMP                      2,048              100                1                -                 .02           ONLINE          ON
USER DATA TABLESPACE  PART_DATA                              1,024            1,024              177              176               17.19           ONLINE          OFF
USER DATA TABLESPACE  PART_DATA_DEF                          1,024            1,024               12               11                1.07           ONLINE          OFF
USER DATA TABLESPACE  PART_IDX                               3,072            3,072              416              415               13.49           ONLINE          OFF
6 rows selected.
````

### How to determine which queries are being rolled back
Source path: `FAQE/Home/08. Monitoring/How to determine which queries are being rolled back__16876296.md`

#### Method that can be used in ALTIBASE HDB 5.1.5 or higher - source block 1

````text
SELECT tx.ID TX_ID,
       tx.SESSION_ID,
       tx.STATUS,
       DECODE(tx.FIRST_UPDATE_TIME, 0, '0', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + tx.FIRST_UPDATE_TIME / (60*60*24), 'MM/DD HH:MI:SS')) FIRST_UPDATE_TIME,
       st.TOTAL_TIME/1000000 TOTAL,
       tx.CURRENT_UNDO_NEXT_LSN_FILENO,
       tx.CURRENT_UNDO_NEXT_LSN_OFFSET,
       SUBSTR(QUERY, 1, 100) QUERY
  FROM V$TRANSACTION tx,
       V$STATEMENT st
 WHERE tx.ID = st.TX_ID
   AND tx.SESSION_ID <> SESSION_ID();
````

### How to log queries performed in Altibase (altiProfile)?
Source path: `FAQE/Home/08. Monitoring/How to log queries performed in Altibase (altiProfile)__22642959.md`

#### How to analyze the results - source block 1

````text
[STATEMENT] 2025/07/16 09:45:05(2/131076/129940)
  SQL
     => [UPDATE EMPLOYEES SET DNO = ?, EMP_TEL = ? WHERE ENO = ?]

  User Info
     User    ID     = 2
     Client PID     = 30017
     Client Type    = [CLI-64LE]
     Client AppInfo = [isql]

  Elapsed Time
     Total =            0 sec      618 usec
     SoftP =            0 sec       55 usec
     Parse =            0 sec        0 usec
     Valid =            0 sec        0 usec
     Optim =            0 sec        0 usec
     Execu =            0 sec      563 usec
     Fetch =            0 sec        0 usec

  Query Execute Info
     EXECUTE Result =                    4 (0:failure, 1:rebuild, 2:retry, 3:queue empty, 4:success)
     Optimizer Mode =                    0
     Cost      Mode =                    0
     Used Memory    =                    0
     SUCCESS   SUM  =                    1
     FAILURE   SUM  =                    0
     PROCESSED ROW  =                    1

  XA Info
     XA Flag        =                    0 (0:Non-XA, 1:XA)

  Result Set Info
     FETCH Result   =                    2 (0:failure, 1:success, 2:no result set)

  Index Access Info
     Memory Full  Scan Count  =                    0
     Memory Index Scan Count  =                    1
     Disk   Full  Scan Count  =                    0
     Disk   Index Scan Count  =                    0

  Disk Access Info
     READ   DATA PAGE  =                    0
     WRITE  DATA PAGE  =                    0
     GET    DATA PAGE  =                    0
     CREATE DATA PAGE  =                    0
     READ   UNDO PAGE  =                    0
     WRITE  UNDO PAGE  =                    0
     GET    UNDO PAGE  =                    0
     CREATE UNDO PAGE  =                    0
````

#### How to analyze the results - source block 2

````text
[BIND] 2025/07/16 09:45:05 (2/131076/129940/01)
    [(_integer ) 3001]                          ==>  Bind variable value
[BIND] 2025/07/16 09:45:05 (2/131076/129940/02)
    [(_char    ) (11)                           ==>  Bind variable value
    00000000 01011111111]
[BIND] 2025/07/16 09:45:05 (2/131076/129940/03)
    [(_integer ) 1]                             ==>  Bind variable value
````

#### How to analyze the results - source block 3

````text
[PLAN] 2025/07/16 09:45:05(2/131076/129940)
[------------------------------------------------------------
UPDATE ( TABLE: SYS.EMPLOYEES )
 SCAN ( TABLE: SYS.EMPLOYEES, INDEX: SYS.__SYS_IDX_ID_143, RANGE SCAN, ACCESS: 1, COST: 0.01 )
------------------------------------------------------------
]
````

#### How to analyze the results - source block 4

````text
[SESSION STAT] 2025/07/16 10:05:23 (1)
     logon current                             =          1
     logon cumulative                          =          1
     data page read                            =          0
     data page write                           =          0
     data page gets                            =          0
     data page fix                             =          0
     data page create                          =          0
     undo page read                            =          0
     undo page write                           =          0
     undo page gets                            =          0
     undo page fix                             =          0
     undo page create                          =          0
     base time in second                       =          0
     query timeout                             =          0
     ddl timeout                               =          0
     idle timeout                              =          0
     fetch timeout                             =          0
     utrans timeout                            =          0
     session terminated                        =          0
     ddl sync timeout                          =          0
     statement rebuild count                   =          0
     unique violation count                    =          0
     update retry count                        =          0
     delete retry count                        =          0
     lock row retry count                      =          0
     session commit                            =          0
     session rollback                          =          0
     fetch success count                       =          0
     fetch failure count                       =          0
     execute success count                     =          5
     execute success count : insert            =          0
     execute success count : update            =          0
     execute success count : delete            =          0
     execute success count : select            =          0
     rep_execute success count : insert        =          0
     rep_execute success count : update        =          1
     rep_execute success count : delete        =          0
     execute failure count                     =          0
     prepare success count                     =          4
     prepare failure count                     =          0
     rebuild count                             =          0
     write redo log count                      =          1
     write redo log bytes                      =        272
     read socket count                         =          6
     write socket count                        =          7
     byte received via inet                    =        677
     byte sent via inet                        =        620
     byte received via unix domain             =          0
     byte sent via unix domain                 =          0
     semop count for receiving via ipc         =          0
     semop count for sending via ipc           =          0
     memory table cursor full scan count       =          0
     memory table cursor index scan count      =          1
     memory table cursor GRID scan count       =          0
     disk table cursor full scan count         =          0
     disk table cursor index scan count        =          0
     disk table cursor GRID scan count         =          0
     lock acquired count                       =          3
     lock released count                       =          0
     service thread created count              =          0
     memory table access count                 =          1
     missing ppco x-trylatch count             =          0
     read IB count                             =          0
     write IB count                            =          0
     byte received via IB                      =          0
     byte sent via IB                          =          0
     elapsed time: query parse                 =        407
     elapsed time: query validate              =          0
     elapsed time: query optimize              =          0
     elapsed time: query execute               =   66497143
     elapsed time: query fetch                 =          0
     elapsed time: soft prepare                =        155
     elapsed time: analyze values in DML(disk)  =          0
     elapsed time: record lock validation in DML(disk)  =          0
     elapsed time: allocate data slot in DML(disk)  =          0
     elapsed time: write undo record in DML(disk)  =          0
     elapsed time: allocate tss in dml(disk)   =          0
     elapsed time: allocate undopage in dml(disk)  =          0
     elapsed time: index operation in dml(disk)  =          0
     elapsed time: create page(disk)           =          0
     elapsed time: get page(disk)              =          0
     elapsed time: fix page(disk)              =          0
     elapsed time: logical aging by tx in dml(disk)  =          0
     elapsed time: phyical aging by tx in dml(disk)  =          0
     elapsed time: replace(plan cache)         =          0
     elapsed time: victim free in replace(plan cache)  =          0
     elapsed time: hard rebuild                =          0
     elapsed time: soft rebuild                =          0
     elapsed time: add hard-prepared plan to plan cache  =          0
     elapsed time: add hard-rebuild plan to plan cache  =          0
     elapsed time: search time for parent PCO  =         42
     elapsed time: creation time for parent PCO  =          0
     elapsed time: search time for child PCO   =          0
     elapsed time: creation time for child PCO  =          0
     elapsed time: validation time for child PCO  =         23
     elapsed time: creation time for new child PCO by rebuild at execution   =          0
     elapsed time: creation time for new child PCO by rebuild at soft prepare  =          0
     elapsed time: hard prepare time           =        510
     elapsed time: matching time for child PCO  =         33
     elapsed time: waiting time for hard prepare  =          0
     elapsed time: moving time from cold region to hot region.  =          0
     elapsed time: waiting time for parent PCO  when choosing plan cache replacement victim.  =          0
     elapsed time: privilege checking time during soft prepare.  =          9
     elapsed time: copying logs to replication log buffer (sender side)  =          0
     elapsed time: sender(s) waiting for new logs  =          0
     elapsed time: sender(s) reading logs from replication log buffer  =          0
     elapsed time: sender(s) reading logs from log file(s)  =          0
     elapsed time: sender(s) checking whether logs are useful  =          0
     elapsed time: sender(s) analyzing logs    =          0
     elapsed time: sender(s) sending xlogs to receiver(s)  =          0
     elapsed time: sender(s) receiving ACK from receiver(s)  =          0
     elapsed time: sender(s) setting ACKed value  =          0
     elapsed time: receiver(s) receiving xlogs from sender(s)  =          0
     elapsed time: receiver(s) performing endian conversion  =          0
     elapsed time: receiver(s) beginning transaction(s)  =          0
     elapsed time: receiver(s) committing transaction(s)  =          0
     elapsed time: receiver(s) aborting transaction(s)  =          0
     elapsed time: receiver(s) opening table cursor(s)  =          0
     elapsed time: receiver(s) closing table cursor(s)  =          0
     elapsed time: receiver(s) inserting rows  =          0
     elapsed time: receiver(s) updating rows   =          0
     elapsed time: receiver(s) deleting rows   =          0
     elapsed time: receiver(s) opening lob cursor(s)  =          0
     elapsed time: receiver(s) preparing to write LOB(s)  =          0
     elapsed time: receiver(s) writing LOB piece(s)  =          0
     elapsed time: receiver(s) finish writing LOBs  =          0
     elapsed time: receiver(s) closing LOB cursor(s)  =          0
     elapsed time: receiver(s) comparing images to check for conflicts  =          0
     elapsed time: receiver(s) sending ACK     =          0
     elapsed time: receiver(s) trim LOB(s)     =          0
     elapsed time: task schedule               =          0
     max     time: task schedule               =          0
````

#### How to analyze the results - source block 5

````text
[SYSTEM STAT] 2025/07/16 10:15:26 (0)
     logon current                             =          1
     logon cumulative                          =         12
     data page read                            =          4
     data page write                           =          0
     data page gets                            =      13390
     data page fix                             =        735
     data page create                          =      27754
     undo page read                            =          0
     undo page write                           =          0
     undo page gets                            =          0
     undo page fix                             =          0
     undo page create                          =          0
     base time in second                       = 1752628526
     query timeout                             =          0
     ddl timeout                               =          0
     idle timeout                              =          0
     fetch timeout                             =          0
     utrans timeout                            =          2
     session terminated                        =          0
     ddl sync timeout                          =          0
     statement rebuild count                   =          0
     unique violation count                    =          0
     update retry count                        =          0
     delete retry count                        =          0
     lock row retry count                      =          0
     session commit                            =         85
     session rollback                          =         11
     fetch success count                       =         57
     fetch failure count                       =          0
     execute success count                     =        158
     execute success count : insert            =          0
     execute success count : update            =          0
     execute success count : delete            =          0
     execute success count : select            =         57
     rep_execute success count : insert        =          0
     rep_execute success count : update        =         20
     rep_execute success count : delete        =          0
     execute failure count                     =         12
     prepare success count                     =        135
     prepare failure count                     =         23
     rebuild count                             =          0
     write redo log count                      =      31862
     write redo log bytes                      =    4552687
     read socket count                         =        230
     write socket count                        =        596
     byte received via inet                    =      95951
     byte sent via inet                        =     173741
     byte received via unix domain             =        140
     byte sent via unix domain                 =       9237
     semop count for receiving via ipc         =          0
     semop count for sending via ipc           =          0
     memory table cursor full scan count       =        439
     memory table cursor index scan count      =       8337
     memory table cursor GRID scan count       =          0
     disk table cursor full scan count         =         18
     disk table cursor index scan count        =          0
     disk table cursor GRID scan count         =          0
     lock acquired count                       =       8436
     lock released count                       =       2489
     service thread created count              =         25
     memory table access count                 =      13918
     missing ppco x-trylatch count             =          0
     read IB count                             =          0
     write IB count                            =          0
     byte received via IB                      =          0
     byte sent via IB                          =          0
     elapsed time: query parse                 =      19280
     elapsed time: query validate              =      11934
     elapsed time: query optimize              =       5714
     elapsed time: query execute               = 3199359716
     elapsed time: query fetch                 =       4968
     elapsed time: soft prepare                =       4675
     elapsed time: analyze values in DML(disk)  =          0
     elapsed time: record lock validation in DML(disk)  =          0
     elapsed time: allocate data slot in DML(disk)  =          0
     elapsed time: write undo record in DML(disk)  =          0
     elapsed time: allocate tss in dml(disk)   =          0
     elapsed time: allocate undopage in dml(disk)  =          0
     elapsed time: index operation in dml(disk)  =          0
     elapsed time: create page(disk)           =          0
     elapsed time: get page(disk)              =          0
     elapsed time: fix page(disk)              =          0
     elapsed time: logical aging by tx in dml(disk)  =          0
     elapsed time: phyical aging by tx in dml(disk)  =          0
     elapsed time: replace(plan cache)         =          0
     elapsed time: victim free in replace(plan cache)  =          0
     elapsed time: hard rebuild                =          0
     elapsed time: soft rebuild                =          0
     elapsed time: add hard-prepared plan to plan cache  =         71
     elapsed time: add hard-rebuild plan to plan cache  =          0
     elapsed time: search time for parent PCO  =        451
     elapsed time: creation time for parent PCO  =        279
     elapsed time: search time for child PCO   =          0
     elapsed time: creation time for child PCO  =         34
     elapsed time: validation time for child PCO  =       2247
     elapsed time: creation time for new child PCO by rebuild at execution   =          0
     elapsed time: creation time for new child PCO by rebuild at soft prepare  =          0
     elapsed time: hard prepare time           =      39568
     elapsed time: matching time for child PCO  =        400
     elapsed time: waiting time for hard prepare  =          0
     elapsed time: moving time from cold region to hot region.  =          0
     elapsed time: waiting time for parent PCO  when choosing plan cache replacement victim.  =          0
     elapsed time: privilege checking time during soft prepare.  =        219
     elapsed time: copying logs to replication log buffer (sender side)  =          0
     elapsed time: sender(s) waiting for new logs  =          0
     elapsed time: sender(s) reading logs from replication log buffer  =          0
     elapsed time: sender(s) reading logs from log file(s)  =          0
     elapsed time: sender(s) checking whether logs are useful  =          0
     elapsed time: sender(s) analyzing logs    =          0
     elapsed time: sender(s) sending xlogs to receiver(s)  =          0
     elapsed time: sender(s) receiving ACK from receiver(s)  =          0
     elapsed time: sender(s) setting ACKed value  =          0
     elapsed time: receiver(s) receiving xlogs from sender(s)  =          0
     elapsed time: receiver(s) performing endian conversion  =          0
     elapsed time: receiver(s) beginning transaction(s)  =          0
     elapsed time: receiver(s) committing transaction(s)  =          0
     elapsed time: receiver(s) aborting transaction(s)  =          0
     elapsed time: receiver(s) opening table cursor(s)  =          0
     elapsed time: receiver(s) closing table cursor(s)  =          0
     elapsed time: receiver(s) inserting rows  =          0
     elapsed time: receiver(s) updating rows   =          0
     elapsed time: receiver(s) deleting rows   =          0
     elapsed time: receiver(s) opening lob cursor(s)  =          0
     elapsed time: receiver(s) preparing to write LOB(s)  =          0
     elapsed time: receiver(s) writing LOB piece(s)  =          0
     elapsed time: receiver(s) finish writing LOBs  =          0
     elapsed time: receiver(s) closing LOB cursor(s)  =          0
     elapsed time: receiver(s) comparing images to check for conflicts  =          0
     elapsed time: receiver(s) sending ACK     =          0
     elapsed time: receiver(s) trim LOB(s)     =          0
     elapsed time: task schedule               =          0
     max     time: task schedule               =          0
````

#### How to analyze the results - source block 6

````text
[MEMORY STAT] 2025/07/16 10:25:59
   Main_Module_DirectAttach : (0/ 0/ 0)
   Main_Module_Channel : (0/ 0/ 0)
   Main_Module_CDBC_MAIN : (0/ 0/ 0)
   Main_Module_CDBC_QP : (0/ 0/ 0)
   Main_Module_CDBC_STATE_MEMPOOL : (0/ 0/ 0)
   Main_Module_CDBC_CURSORDATA_MEMPOOL : (0/ 0/ 0)
   Main_Module_CDBC_CONDITIONBUF_MEMPOOL : (0/ 0/ 0)
   Main_Module_Distributed : (0/ 0/ 0)
   Main_Module_Thread : (0/ 0/ 0)
   Main_Module_Queue : (0/ 0/ 0)
   Main_Module_Utility : (0/ 0/ 0)
   SQL_Plan_Cache_Control : (0/ 0/ 0)
   GIS_DataType : (0/ 0/ 0)
   GIS_Disk_Index : (0/ 0/ 0)
   GIS_Function : (0/ 0/ 0)
   GIS_TEMP_MEMORY : (0/ 0/ 0)
   Query_Common : (0/ 0/ 0)
   Query_Meta : (0/ 0/ 0)
   Query_DML : (0/ 0/ 0)
   Query_Sequence : (0/ 0/ 0)
   Query_PSM_Concurrent_Execute : (0/ 0/ 0)
   Replication_Common : (0/ 0/ 0)
   Replication_Control : (0/ 0/ 0)
   Replication_Data : (0/ 0/ 0)
   Replication_Met : (0/ 0/ 0)
   Replication_Network : (0/ 0/ 0)
   Replication_Recovery : (0/ 0/ 0)
   Replication_Storage : (0/ 0/ 0)
   Replication_Executor : (0/ 0/ 0)
   Replication_Sender : (0/ 0/ 0)
   Replication_Receiver : (0/ 0/ 0)
   Replication_Sync : (0/ 0/ 0)
   Replication_Module_Property : (0/ 0/ 0)
   Query_PSM_Node : (0/ 0/ 0)
   Query_PSM_Execute : (0/ 0/ 0)
   Query_Prepare : (0/ 0/ 0)
   Query_PSM_Varray : (0/ 0/ 0)
   Query_Execute : (0/ 0/ 0)
   Query_Binding : (0/ 0/ 0)
   Query_Transaction : (0/ 0/ 0)
   Query_Conversion : (0/ 0/ 0)
   Query_Execute_Cache : (0/ 0/ 0)
   Query_Result_Cache : (0/ 0/ 0)
   Query_PSM_Internal_Execute : (0/ 0/ 0)
   Mathematics : (0/ 0/ 0)
   Storage_Disk_Buffer : (0/ 0/ 0)
   Storage_Disk_Collection : (0/ 0/ 0)
   Storage_Disk_Datafile : (0/ 0/ 0)
   Storage_Disk_SecondaryBuffer : (0/ 0/ 0)
   Storage_Tablespace : (0/ 0/ 0)
   Storage_DataPort : (0/ 0/ 0)
   Storage_Disk_Index : (0/ 0/ 0)
   Storage_Disk_Page : (0/ 0/ 0)
   Storage_Disk_Recovery : (0/ 0/ 0)
   Storage_Global_Memory_Manager : (0/ 0/ 0)
   Storage_Memory_Ager : (0/ 0/ 0)
   Storage_Memory_Logical_Ager : (0/ 0/ 0)
   Storage_Memory_Collection : (0/ 0/ 0)
   Storage_Memory_Interface : (0/ 0/ 0)
   Storage_Memory_Locking : (0/ 0/ 0)
   Storage_Memory_Manager : (0/ 0/ 0)
   Storage_Memory_Index : (0/ 0/ 0)
   Fixed_Table : (0/ 0/ 0)
   Storage_Memory_Page : (0/ 0/ 0)
   Storage_Memory_Recovery : (0/ 0/ 0)
   Storage_Memory_Recovery_Chkpt_Thread : (0/ 0/ 0)
   Storage_Memory_Recovery_LFG_Thread : (0/ 0/ 0)
   Storage_Memory_Recovery_Archive_Thread : (0/ 0/ 0)
   Storage_Memory_Utility : (0/ 0/ 0)
   Storage_Memory_Transaction : (0/ 0/ 0)
   Volatile_Log_Buffer : (0/ 0/ 0)
   Volatile_Memory_Manager : (0/ 0/ 0)
   Volatile_Memory_Page : (0/ 0/ 0)
   Temp_Memory : (0/ 0/ 0)
   Transaction_Table : (0/ 0/ 0)
   Legacy_Transaction_Manager : (0/ 0/ 0)
   Transaction_OID_List : (0/ 0/ 0)
   Transaction_Private_Buffer : (0/ 0/ 0)
   Transaction_Segment_Table : (0/ 0/ 0)
   Transaction_DiskPage_Touched_List : (0/ 0/ 0)
   Transaction_Table_Info : (0/ 0/ 0)
   Index_Memory : (0/ 0/ 0)
   LOG_Memory : (0/ 0/ 0)
   InMemoryRecovery_Memory : (0/ 0/ 0)
   CatalogCache_Memory : (0/ 0/ 0)
   OS_Independent : (0/ 0/ 0)
   Utility_Module : (0/ 0/ 0)
   Async_IO_Manager : (0/ 0/ 0)
   Mutex : (0/ 0/ 0)
   Clock_Manager : (0/ 0/ 0)
   Timer_Manager : (0/ 0/ 0)
   Profile_Manager : (0/ 0/ 0)
   Socket_Manager : (0/ 0/ 0)
   External_Procedure : (0/ 0/ 0)
   External_Procedure_Agent : (0/ 0/ 0)
   Audit_Manager : (0/ 0/ 0)
   Altiwrap : (0/ 0/ 0)
   Process_ThreadInfo : (0/ 0/ 0)
   CM_Buffer : (0/ 0/ 0)
   CM_NetworkInterface : (0/ 0/ 0)
   CM_Multiplexing : (0/ 0/ 0)
   CM_DataType : (0/ 0/ 0)
   CM_Interface : (0/ 0/ 0)
   Database_Link : (0/ 0/ 0)
   Dynamic Module Loader : (0/ 0/ 0)
   Tablespace_Free_Extent_Pool : (0/ 0/ 0)
   Condition_Variable : (0/ 0/ 0)
   WATCHDOG : (0/ 0/ 0)
   Latch : (0/ 0/ 0)
   Thread_Stack : (0/ 0/ 0)
   Remote_Call_Server : (0/ 0/ 0)
   Remote_Call_Client : (0/ 0/ 0)
   Query_Common_Remote_Call : (0/ 0/ 0)
   IDU_MEM_OTHER : (0/ 0/ 0)
   MMAP : (0/ 0/ 0)
   SYSTEM : (0/ 0/ 0)
   Shared Meta : (0/ 0/ 0)
   RESERVED : (0/ 0/ 0)
````

#### How to analyze the results - source block 7

````text
$ altiProfile -stat query alti-1752630730-0.prof
### Processing [alti-1752630730-0.prof]...
100% [====================]
### Writing CSV File [alti-prof-stat-1752631027.csv]...
### Writing TEXT File [alti-prof-stat-1752631027.txt]...
### Successfully done.
$ ls -la  ==> Statistical Information Output Files
-rw-rw-rw- 1 alti0 alti0     747 Jul 16 10:57 alti-prof-stat-1752631027.csv
-rw-rw-rw- 1 alti0 alti0    1241 Jul 16 10:57 alti-prof-stat-1752631027.txt
$ cat alti-prof-stat-1752631027.txt
  COUNT      AVG          TOTAL         MIN         MAX    SUCCESS  FAIL   QUERY
===========================================================================================================
     4     3.959910    15.839640     0.002116     7.665345     4     0    EXEC PROC1(3001, '01046585724', 1)
     7     2.262010    15.834073     0.000159     7.663861     7     0    UPDATE EMPLOYEES SET DNO = ?, EMP_TEL = ? WHERE ENO = ?
     9     0.620658     5.585918     0.000081     5.584472     9     0    UPDATE EMPLOYEES SET DNO = :v1, EMP_TEL = :v2 WHERE ENO = :v3
    10     0.000352     0.003520     0.000088     0.002201    10     0    select * from SYS.CUSTOMERS
     8     0.000364     0.002911     0.000149     0.001264     8     0    commit
     1     0.002279     0.002279     0.002279     0.002279     1     0    ALTER SYSTEM SET QUERY_PROF_FLAG = 7
    12     0.000153     0.001840     0.000072     0.000454    12     0    select * from SYS.DEPARTMENTS
     6     0.000249     0.001492     0.000059     0.000880     6     0    select * from ALTITEST.ORDERS
===========================================================================================================
[TOTAL] Count(Query): 57  Avg(Time): 0.653889  Sum(Time): 37.2717

$ altiProfile -stat session alti-1752630730-0.prof
### Processing [alti-1752630730-0.prof]...
100% [====================]
### Writing CSV File [alti-prof-stat-1752631158.csv]...
### Writing TEXT File [alti-prof-stat-1752631158.txt]...
### Successfully done.
$ ls -la
-rw-rw-rw- 1 alti0 alti0    2319 Jul 16 10:59 alti-prof-stat-1752631158.txt
-rw-rw-rw- 1 alti0 alti0    1393 Jul 16 10:59 alti-prof-stat-1752631158.csv
$ cat alti-prof-stat-1752631158.txt
SESSION    COUNT      AVG          TOTAL         MIN         MAX    SUCCESS  FAIL   QUERY
===========================================================================================================
     1       5     1.117055     5.585273     0.000166     5.584472     5     0    UPDATE EMPLOYEES SET DNO = :v1, EMP_TEL = :v2 WHERE ENO = :v3
     1       2     2.114851     4.229702     0.002116     4.227586     2     0    EXEC PROC1(3001, '01046585724', 1)
     1       3     1.408920     4.226760     0.000335     4.225859     3     0    UPDATE EMPLOYEES SET DNO = ?, EMP_TEL = ? WHERE ENO = ?
     1       5     0.000562     0.002812     0.000112     0.002201     5     0    select * from SYS.CUSTOMERS
     1       1     0.002279     0.002279     0.002279     0.002279     1     0    ALTER SYSTEM SET QUERY_PROF_FLAG = 7
     1       6     0.000367     0.002201     0.000149     0.001264     6     0    commit
     1       4     0.000332     0.001328     0.000115     0.000880     4     0    select * from ALTITEST.ORDERS
     1       6     0.000175     0.001049     0.000082     0.000454     6     0    select * from SYS.DEPARTMENTS
===========================================================================================================
[SUB-TOTAL] Count(Query): 32  Avg(Time): 0.439106  Sum(Time): 14.0514
     2       2     5.804969    11.609938     3.944593     7.665345     2     0    EXEC PROC1(3001, '01046585724', 1)
     2       4     2.901828    11.607313     0.000159     7.663861     4     0    UPDATE EMPLOYEES SET DNO = ?, EMP_TEL = ? WHERE ENO = ?
     2       6     0.000132     0.000791     0.000072     0.000229     6     0    select * from SYS.DEPARTMENTS
     2       2     0.000355     0.000710     0.000261     0.000449     2     0    commit
     2       5     0.000142     0.000708     0.000088     0.000186     5     0    select * from SYS.CUSTOMERS
     2       4     0.000161     0.000645     0.000081     0.000305     4     0    UPDATE EMPLOYEES SET DNO = :v1, EMP_TEL = :v2 WHERE ENO = :v3
     2       2     0.000082     0.000164     0.000059     0.000105     2     0    select * from ALTITEST.ORDERS
===========================================================================================================
[SUB-TOTAL] Count(Query): 25  Avg(Time): 0.928811  Sum(Time): 23.2203
````

### How to set up and execute altimon
Source path: `FAQE/Home/08. Monitoring/How to set up and execute altimon__16876266.md`

#### Uploading ALTIMON file - source block 1

````text
$ tar xvf altimon.tar
````

#### Uploading ALTIMON file - source block 2

````text
$ ls -l altimon
total 8336
drwxr-xr-x    2 eheejung staff           256 Dec 30 15:26 ACTION_LOG
drwxr-xr-x    2 eheejung staff           256 Dec 30 15:26 ACTION_SCRIPT
-rw-r--r--    1 eheejung staff           318 Dec 30 11:23 Makefile
-rwxr-xr-x    1 eheejung staff       3991619 Dec 30 15:10 altimon            // execution file
-rw-r--r--    1 eheejung staff         18120 Dec 30 11:23 altimon.conf       // configuration file
-rw-r--r--    1 eheejung staff         78141 Dec 30 11:23 altimon.cpp
-rw-r--r--    1 eheejung staff        166311 Dec 30 15:10 altimon.o
drwxr-xr-x    2 eheejung staff           256 Dec 30 15:26 log
````

#### Copying ALTIMON execution file - source block 3

````text
 $ cp -p altimon $ALTIBASE_HOME/bin/
````

#### Copying ALTIMON configuration file - source block 4

````text
$ cp -p altimon.conf $ALTIBASE_HOME/conf/
````

#### Things to be changed in the ALTIMON configuration file - source block 5

````text
#########################################
## Connection Group
#########################################
<CONNECTION_INFO>
    <DB_IP>        127.0.0.1 </DB_IP>
    <SYS_PASSWD>   manager     </SYS_PASSWD>               # Enter sys account password
    <PORT_NO>      20300       </PORT_NO>                  # Enter the Altibase server service port
    <NLS_USE>      US7ASCII    </NLS_USE>                  # Enter database server character set iSQL> select NLS_CHARACTERSET from v$nls_parameters; Can be checked.
</CONNECTION_INFO>

#########################################
## ALTIMON PROPERTY
#########################################
<ALTIMON_PROPERTY>
    <DATE_FORMAT>   1    </DATE_FORMAT>
    <SLEEP_TIME>    300  </SLEEP_TIME>                                       # If a problem occurs, change it to suit your environment so that the situation at that time can be logged. The unit is seconds.
    <LOG_FILE>      /home/altibase/altimon/log/altimon.log </LOG_FILE>       # Change the log file path to suit the environment. Enter it as an absolute path, leave the file name as it is, and change only the path.
    <LOG_DIR>       /home/altibase/altimon/log </LOG_DIR>                    # Enter the log file path again as an absolute path to suit the environment.
    <LIFE_CYCLE>    3    </LIFE_CYCLE>                                       # Log file retention period, in daily units. Change it to suit the environment.
    <LOGGING_LV>    2    </LOGGING_LV>
    <ALARM_FILE>    /home/altibase/altimon/log/alarm.log   </ALARM_FILE>     # Change the alarm log file path to suit your environment. Enter it as an absolute path, leave the filename as it is, and change only the path.
    <DB_SAVE>       OFF   </DB_SAVE>
    <LISTEN_PORT>   22300 </LISTEN_PORT>
</ALTIMON_PROPERTY>
````

#### Things to be changed in the ALTIMON configuration file - source block 6

````text
#########################################
## PROCESS CHECK PROPERTY
#########################################
<OS_QUERY_GROUP_SET>
    <CPU_USAGE> 80 </CPU_USAGE>
    <CPU_ACT>                                        # From this setting, the path $HOME/altimon/ACTION_SCRIPT/ will continue to be used. If the altimon directory is located differently from the one below, it will be changed.
       is -silent -f $HOME/altimon/ACTION_SCRIPT/cpu_act.sql -o $HOME/altimon/ACTION_LOG/cpu_act.log.`date +%Y%m%d_%H%M%S`
    </CPU_ACT>
    <MEM_USAGE> 100000000 </MEM_USAGE>
    <MEM_ACT>
       is -silent -f $HOME/altimon/ACTION_SCRIPT/mem_act.sql -o $HOME/altimon/ACTION_LOG/mem_act.log.`date +%Y%m%d_%H%M%S`
    </MEM_ACT>
    <DISK_CHK_ENABLE> ON </DISK_CHK_ENABLE>
    <DISK1>  /home       </DISK1>                    # Please modify the file system to be monitored.
    <DISK1_USAGE> 90     </DISK1_USAGE>              # Enter the file system usage threshold. The unit is %.
    <DISK2>  /home1   </DISK2>
    <DISK2_USAGE> 90     </DISK2_USAGE>
    <DISK_ACT>
    </DISK_ACT>
</OS_QUERY_GROUP_SET>
````

#### Executing ALTIMON - source block 7

````text
$ export UNIX95=1             (For Bourne Shell, Korn Shell, Bash Shell)
Or
$ setenv UNIX95 1             ( For C Shell)
````

#### Executing ALTIMON - source block 8

````text
$ export NMON=t              (For Bourne Shell, Korn Shell, Bash Shell)
Or
$ setenv NMON t              ( For C Shell)
````

#### Executing ALTIMON - source block 9

````text
$ altimon start
````

#### Check Altibase Log - source block 10

````text
<LOG_FILE>      /home/eheejung/altimon/log/altimon.log </LOG_FILE>
````

### Lock related properties
Source path: `FAQE/Home/08. Monitoring/Lock related properties__16876204.md`

#### How to monitor - source block 1

````text
select table_name , lock_desc
from system_.sys_tables_ a, v$lock b
where a.table_oid = b.table_oid;
````

#### How to monitor - source block 2

````text
select query
from v$lock a, v$lock_statement b
where a.trans_id = b.tx_id;
````

#### How to monitor - source block 3

````text
ALTER DATABASE database_name SESSION CLOSE session_id;
````

#### How to monitor - source block 4

````text
connect sys/manager as sysdba;
````

#### How to monitor - source block 5

````text
select query, tx_id
from v$statement
where tx_id in ( select trans_id from v$lock_wait);
````

#### How to monitor - source block 6

````text
select
id tx_id,
lw.wait_for_trans_id wait_tx_id,
decode (status,0,'BEGIN',
1,'PRECOMMIT',
2,'COMMIT_IN_MEMORY',
3,'COMMIT',
4,'ABORT',
5,'BLOCKED',
6,'END', 'UNKNOWN') status,
decode(update_status,0,'READ',1,'UPDATING','UNKNOWN') TTYPE,
decode(first_undo_next_lsn_fileno,-1,'READ_TRN',first_undo_next_lsn_fileno) firstlog,
base_time - decode(first_update_time, 0, base_time, first_update_time) time
from
v$transaction tx
left outer join v$lock_wait lw
on tx.id = lw.trans_id,
(select base_time from v$sessionmgr) base
where status != 6
order by time desc;
````

#### How to monitor - source block 7

````text
select a.table_oid, a.lock_desc, c.client_pid , b.session_id
from v$lock a, v$statement b, v$session c
where a.trans_id = b.tx_id
and b.session_id = c.id;
````

### Memory table and index usage
Source path: `FAQE/Home/08. Monitoring/Memory table and index usage__16876259.md`

#### Memory table data usage query - source block 1

````text
set linesize 2048;
set colsize 30;
SELECT   a.user_name
        ,NVL(d.name,'SYS_TBS_MEMORY')  AS 'TABLESPACE_NAME'
        , b.table_name
        , round((c.fixed_alloc_mem + c.var_alloc_mem)/(1024*1024),2) 'ALLOC(M)'
        , round((c.fixed_used_mem + c.var_used_mem)/(1024*1024),2) 'USED(M)'
        , round((c.fixed_used_mem + c.var_used_mem)/(c.fixed_alloc_mem + c.var_alloc_mem)*100,2) 'EFFICIENCY(%)'
FROM   system_.sys_users_ a
     , system_.sys_tables_ b
     , v$memtbl_info c left outer join v$tablespaces d  on c.tablespace_id = d.id
WHERE  b.table_type = 'T'
  and a.user_id = b.user_id
  and b.table_oid = c.table_oid
order by 1,2,3, 4 desc ;
````

#### Memory table data usage query - source block 2

````text
USER_NAME                       TABLESPACE_NAME                 TABLE_NAME                      TABLE_OID            ALLOC(M)    USED(M)     EFFICIENCY(%)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
SYS                             SYS_TBS_MEM_DATA                TEST_T2                         3323512              0.41        0.38        93.9
SYS                             USER_MEM_TBS                    MEM_T1                          3321192              0.03        0           0
SYSTEM_                         SYS_TBS_MEM_DIC                 STO_COLUMNS_                    1453416              0.03        0           0
SYSTEM_                         SYS_TBS_MEM_DIC                 STO_DATUMS_                     1469656              0.03        0           0
SYSTEM_                         SYS_TBS_MEM_DIC                 STO_ELLIPSOIDS_                 1471976              0.03        0           0
````

#### Query to check memory table index information (all available from HDB 4 to HDB 6) - source block 3

````text
set linesize 2048;
set colsize 30;

 SELECT
        c.user_name
        , decode(f.table_type, 'Q', 'QUEUE', 'T', 'TABLE') object_type
        , table_name object_name
        , e.index_name
        , rpad(case2(e.index_type=1, 'b-tree', 'r-tree'),10,' ') index_type
        , '16 bytes * rowcount' 'ALLOC'
 FROM      v$memtbl_info a
        ,  v$index b
        , system_.sys_users_ c
        , system_.sys_indices_ e
        , system_.sys_tables_ f
 WHERE
       a.table_oid = f.table_oid
   and b.index_id = e.index_id
   and e.user_id = c.user_id
   and f.user_id = e.user_id
   and f.tbs_id = a.tablespace_id
   and f.table_oid = b.table_oid
   and c.user_name <> 'SYSTEM_' ;
````

#### Query to check memory table index information (all available from HDB 4 to HDB 6) - source block 4

````text
USER_NAME                       OBJECT_TYPE  OBJECT_NAME                     INDEX_NAME                      INDEX_TYPE  ALLOC
-----------------------------------------------------------------------------------------------------------------------------------------------------
SYS                             TABLE  T1                              IDX1_T2                         b-tree      16 bytes * rowcount
SYS                             TABLE  T1                              IDX1_T1                         b-tree      16 bytes * rowcount
2 rows selected.
````

#### Query to check usage per memory table index (available from HDB 5.x or later) - source block 5

````text
1. Create a function that can count the number of records in the table.
CREATE FUNCTION GETCOUNT(u_name varchar(40), t_name varchar(40))
 RETURN INTEGER
 AS
    RECORDCOUNT integer;
BEGIN
       EXECUTE IMMEDIATE 'SELECT count(*)  FROM ' || u_name||'.'||t_name INTO RECORDCOUNT ;
RETURN RECORDCOUNT;

END;

/

2. Use function to query the usage per index.
set linesize 2048;
set colsize 30;
SELECT
        c.user_name
        , decode(f.table_type, 'Q', 'QUEUE', 'T', 'TABLE') object_type
        , table_name object_name
        , e.index_name
        , rpad(case2(e.index_type=1, 'b-tree', 'r-tree'),10,' ') index_type
        , ROUND( 16 * GETCOUNT(c.user_name, f.table_name) / 1024/1024, 2)  'ALLOC(M)'
 FROM      v$memtbl_info a
        ,  v$index b
        , system_.sys_users_ c
        , system_.sys_indices_ e
        , system_.sys_tables_ f
 WHERE
       a.table_oid = f.table_oid
   and b.index_id = e.index_id
   and e.user_id = c.user_id
   and f.user_id = e.user_id
   and f.tbs_id = a.tablespace_id
   and f.table_oid = b.table_oid
   and c.user_name <> 'SYSTEM_' ;
````

#### Query to check usage per memory table index (available from HDB 5.x or later) - source block 6

````text
USER_NAME                       OBJECT_TYPE  OBJECT_NAME                     INDEX_NAME                      INDEX_TYPE     ALLOC(M)
-----------------------------------------------------------------------------------------------------------------------------------------------
SYS                             TABLE  T1                              IDX1_T2                         b-tree         0.76
SYS                             TABLE  T1                              IDX1_T1                         b-tree         0.76
SYS                             TABLE  T2                              IDX2                            b-tree         0.31
3 rows selected.
````

#### Query to check total index usage per memory table (available from HDB 5.x or later) - source block 7

````text
1. Create a function that can count the number of records in the table.
CREATE FUNCTION GETCOUNT(u_name varchar(40), t_name varchar(40))
 RETURN INTEGER
 AS
    RECORDCOUNT integer;
BEGIN
       EXECUTE IMMEDIATE 'SELECT count(*)  FROM ' || u_name||'.'||t_name INTO RECORDCOUNT ;
RETURN RECORDCOUNT;

END;

/

2. Use function to look up the total index usage size per table.
select
          user_name
        , table_name
        , count(index_name) AS 'INDEX_COUNT'
        , round( SUM(alloc) /1024/1024, 2 ) as 'Alloc(M)'
from (
         SELECT
                  c.user_name
                , f.table_name
                , e.index_name
                , 16 * GETCOUNT(c.user_name, f.table_name) AS alloc
         FROM      v$memtbl_info a
                ,  v$index b
                , system_.sys_users_ c
                , system_.sys_indices_ e
                , system_.sys_tables_ f
         WHERE
               a.table_oid = f.table_oid
           and b.index_id = e.index_id
           and e.user_id = c.user_id
           and f.user_id = e.user_id
           and f.tbs_id = a.tablespace_id
           and f.table_oid = b.table_oid
           and c.user_name <> 'SYSTEM_'
     )
 group by user_name, table_name;
````

#### Query to check total index usage per memory table (available from HDB 5.x or later) - source block 8

````text
 USER_NAME                       TABLE_NAME                      INDEX_COUNT          Alloc(M)
------------------------------------------------------------------------------------------------------
SYS                             T1                              2                    1.53
SYS                             T2                              1                    0.31
2 rows selected.
iSQL>
````

#### Query size per index of memory table (for 6.x) - source block 9

````text
SELECT U.USER_NAME, T.TABLE_NAME TABLE_NAME
     , B.INDEX_NAME
     , LPAD(I.IS_PARTITIONED, 14) INDEX_PARTITIONED
     , ROUND(((USED_NODE_COUNT+ PREPARE_NODE_COUNT) / 15 * 32768)/1024/1024, 1) AS 'SIZE(MB)'
  FROM V$MEM_BTREE_HEADER B
     , SYSTEM_.SYS_INDICES_ I
     , SYSTEM_.SYS_TABLES_ T
     , SYSTEM_.SYS_USERS_ U
 WHERE 1=1
   AND B.INDEX_ID = I.INDEX_ID
   AND I.TABLE_ID = T.TABLE_ID
   AND B.INDEX_TBS_ID <> 0
   AND U.USER_ID = T.USER_ID
 ORDER BY TABLE_NAME, B.INDEX_ID
;
````

#### Query size per index of memory table (for 6.x) - source block 10

````text
USER_NAME             TABLE_NAME            INDEX_NAME            INDEX_PARTITIONED     SIZE(MB)
----------------------------------------------------------------------------------------------------------
SYS                   EMPLOYEES             __SYS_IDX_ID_143                   F        0
SYS                   EMPLOYEES             EMP_IDX1                           F        0
SYS                   FOO                   __SYS_IDX_ID_171                   F        0
SYS                   GOODS                 __SYS_IDX_ID_145                   F        0
SYS                   GOODS                 __SYS_IDX_ID_146                   F        0
SYS                   MEM_T                 M_IDX01                            F        36.5
SYS                   M_PART_SALES          M_IDX_PREFIX                       T        0
SYS                   M_PART_SALES          IDX_PART_1                         T        8.7
SYS                   M_PART_SALES          IDX_PART_2                         T        0.7
SYS                   M_PART_SALES          IDX_PART_3                         T        0.7
````

### ALTIBASE HDB  5.5.1,  6.1.1, 6.3.1
Source path: `FAQE/Home/08. Monitoring/Memory tablespace usage/ALTIBASE HDB 5.5.1, 6.1.1, 6.3.1__16876263.md`

#### Overview - source block 1

````text
--
--TBS_ID   : Tablespace ID
--TBS_TYPE : Memory tablespace type
--           0 - System memory tablespace. A tablespace for storing metadata necessary for the operation of the database system
--           1 - System memory tablespace. A tablespace that can store data created by default when creating a database
--           2 - User memory tablespace. User-created memory tablespace
--           8 - Volatile tablespaces created by users
--TBS_NAME : Memory tablespace name
--MAX(M)   : Max amount of memory that can be used by memory tablespace
--           If MAXSIZE is not specified when creating a tablespace, MEM_MAX_DB_SIZE is displayed.
--           If the tablespace attribute is AUTOEXTEND OFF, TOTAL is output.
--TOTAL(M) : Total number of pages allocated from the memory tablespace. It is the same as the size of the checkpoint image file creation.
--           It also includes a free page. Free pages are not loaded into memory when the Altibase server is started. So, it is difficult to use and judge physical memory as much as this value.
--           This value is decreased only by executing DROP TABLESPACE.
--ALLOC(M) : Amount of memory being used by the memory tablespace
--USED(M)  : The size of the memory storing data among ALLOCs
--USAGE(%) : ALLOC utilization rate compared to MAX
--STATE    : State of the tablespace
--           1 - Offline, 2 - Online, 3 - Offline tablespace being backed up, 4 - Online tablespace being backed up,
--           128 - Dropped tablespace, 1024-discarded tablespace, 1028-discarded tablespace being backed up
set linesize 1024
set colsize 20
SELECT ID TBS_ID
     , DECODE(TYPE, 0, 'MEMORY_DICTIONARY', 1, 'MEMORY_SYS_DATA', 2, 'MEMORY_USER_DATA', 8, 'VOLATILE_USER_DATA') TBS_TYPE
     , NAME TBS_NAME
     , ROUND( DECODE(M.MAXSIZE, 140737488322560, D.MEM_MAX_DB_SIZE , 0 , T.TOTAL_PAGE_COUNT * T.PAGE_SIZE, M.MAXSIZE) /1024/1024, 2 ) 'MAX(M)'
     , ROUND( M.ALLOC_PAGE_COUNT * T.PAGE_SIZE / 1024 / 1024, 2) 'TOTAL(M)'
     , ROUND(NVL(M.ALLOC_PAGE_COUNT-M.FREE_PAGE_COUNT,T.TOTAL_PAGE_COUNT)*PAGE_SIZE/1024/1024, 2) 'ALLOC(M)'
     , NVL(MT.USED, 0) 'USED(M)'
     , ROUND(DECODE(MAXSIZE, 140737488322560, (M.ALLOC_PAGE_COUNT-M.FREE_PAGE_COUNT)*T.PAGE_SIZE/ D.MEM_MAX_DB_SIZE ,0, (M.ALLOC_PAGE_COUNT-M.FREE_PAGE_COUNT) / T.TOTAL_PAGE_COUNT , (M.ALLOC_PAGE_COUNT-M.FREE_PAGE_COUNT) * T.PAGE_SIZE/ M.MAXSIZE) * 100 , 2) 'USAGE(%)'
     , DECODE(T.STATE,1,'OFFLINE',2,'ONLINE',5,'OFFLINE BACKUP',6,'ONLINE BACKUP',128,'DROPPED', 'DISCARDED') STATE
     , DECODE(M.AUTOEXTEND_MODE,1,'ON','OFF') 'AUTOEXTEND'
  FROM V$DATABASE D
     , V$TABLESPACES T
     , (SELECT SPACE_ID
             , SPACE_NAME
             , ALLOC_PAGE_COUNT
             , FREE_PAGE_COUNT
             , DECODE(MAX_SIZE, 0, (SELECT VALUE1 FROM V$PROPERTY WHERE NAME = 'VOLATILE_MAX_DB_SIZE'), MAX_SIZE) AS MAXSIZE
             , AUTOEXTEND_MODE
          FROM V$VOL_TABLESPACES
         UNION ALL
        SELECT SPACE_ID
             , SPACE_NAME
             , ALLOC_PAGE_COUNT
             , FREE_PAGE_COUNT
             , MAXSIZE
             , AUTOEXTEND_MODE
          FROM V$MEM_TABLESPACES ) M LEFT OUTER JOIN(SELECT TABLESPACE_ID, ROUND(SUM((FIXED_USED_MEM + VAR_USED_MEM))/(1024*1024),3) USED
          FROM V$MEMTBL_INFO
         GROUP BY TABLESPACE_ID ) MT ON M.SPACE_ID = MT.TABLESPACE_ID
 WHERE T.ID = M.SPACE_ID;
````

#### Overview - source block 2

````text
TBS_ID      TBS_TYPE            TBS_NAME              MAX(M)      TOTAL(M)    ALLOC(M)    USED(M)     USAGE(%)    STATE           AUTOEXTEND
---------------------------------------------------------------------------------------------------------------------------------------------------------
0           MEMORY_DICTIONARY   SYS_TBS_MEM_DIC       10240       4.03        4           1.007       0.04        ONLINE          ON
1           MEMORY_SYS_DATA     SYS_TBS_MEM_DATA      10240       8.03        0.09        0           0           ONLINE          ON
5           MEMORY_USER_DATA    USER_MEM_TBS          3072.03     3072.03     712.38      686.646     23.19       ONLINE          OFF
6           MEMORY_USER_DATA    USER_MEM_TBS_2        10240       768.03      694.38      686.646     6.78        ONLINE          ON
8           MEMORY_USER_DATA    USER_MEM_TBS_3        1024        512.03      4.03        0           0.39        ONLINE          ON
````

#### Reference - About Memory Tablespace Attributes - source block 3

````text
SELECT SPACE_NAME
     , TO_CHAR(CURRENT_SIZE/1024/1024, '999,999,999') 'CURR_SIZE(MB)'
     , TO_CHAR(AUTOEXTEND_NEXTSIZE/1024/1024, '999,999,999') 'NEXT_SIZE(MB)'
     , TO_CHAR(DECODE(MAXSIZE, 0, CURRENT_SIZE, 140737488322560, D.MEM_MAX_DB_SIZE, MAXSIZE)/1024/1024, '999,999,999') ' MAXSIZE(MB)'
     , DECODE(AUTOEXTEND_MODE, 1, 'ON', 0, 'OFF') 'AUTOEXTEND'
  FROM V$MEM_TABLESPACES, V$DATABASE D
UNION ALL
SELECT SPACE_NAME
     , TO_CHAR(CURRENT_SIZE/1024/1024, '999,999,999') 'CURR_SIZE(MB)'
     , TO_CHAR(NEXT_SIZE/1024/1024, '999,999,999') 'NEXT_SIZE(MB)'
     , TO_CHAR(DECODE(MAX_SIZE, 0, CURRENT_SIZE, 140737488322560, D.MEM_MAX_DB_SIZE, MAX_SIZE)/1024/1024, '999,999,999') ' MAXSIZE(MB)'
     , DECODE(AUTOEXTEND_MODE, 1, 'ON', 0, 'OFF') 'AUTOEXTEND'
  FROM V$VOL_TABLESPACES, V$DATABASE D ;
````

### Monitoring Tools for Windows
Source path: `FAQE/Home/08. Monitoring/Monitoring Tools for Windows__16876220.md`

#### Checking connection information - source block 1

````text
set ISQL="%ALTIBASE_HOME%\bin\isql.exe" -s localhost -u sys -p manager -silent
````

#### Adding monitoring items - source block 2

````text
SELECT TO_CHAR(SYSDATE, 'HH:MI:SS') TIME, '_MON_REP_GAP'
     , REP_NAME
     , REP_SN
     , REP_GAP
  FROM V$REPGAP
 ORDER BY REP_NAME, REP_GAP;
````

#### Monitoring cycle - source block 3

````text
ping -n 60 127.0.0.1 > nul
````

#### Deleting old log function - source block 4

````text
forfiles /P . /M mon.log* /D -30 /C "cmd /c del @file"
````

#### Modifying altimon.vbs file - source block 5

````text
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "C:\Users\Altibase\Desktop\altimon.bat" & Chr(34), 0
Set WshShell = Nothing
````

#### How to run in the foreground - source block 6

````text
C:\Users\Altibase>start altimon.bat
or
C:\Users\Altibase>start altimon
````

#### How to run in the foreground - source block 7

````text
C:\Users\Altibase>altimon.bat
or
C:\Users\Altibase>altimon
````

#### How to execute in background - source block 8

````text
C> alti_mon.vbs
````

#### How to execute in background - source block 9

````text
C:\Users\Altibase\Desktop>alti_mon.vbs
Microsoft (R) Windows Script Host version 5.8
Copyright (C) Microsoft Corporation 1996-2001. All rights reserved.
````

#### When executing in the background - source block 10

````text
C> taskkill /fi "windowtitle eq ALTIMON FOR WINDOWS"
````

#### When executing in the background - source block 11

````text
C:\Users\Altibase\Desktop>taskkill /fi "windowtitle eq ALTIMON FOR WINDOWS"
Success: A shutdown signal was sent to the process (PID 8216).
````

### System information by OS
Source path: `FAQE/Home/08. Monitoring/System information by OS__16876206.md`

#### LINUX - source block 1

````text
$$> ps -elf
F S UID        PID  PPID  C PRI  NI ADDR SZ WCHAN  STIME TTY          TIME CMD
4 S root         1     0  0  76   0 -  1193 109952 Dec17 ?        00:00:01 init [5]
1 S root         2     1  0 -40   - -     0 migrat Dec17 ?        00:00:00 [migration/0]
1 S root         3     1  0  94  19 -     0 ksofti Dec17 ?        00:00:00 [ksoftirqd/0]
1 S root         4     1  0 -40   - -     0 migrat Dec17 ?        00:00:00 [migration/1]
1 S root         5     1  0  94  19 -     0 ksofti Dec17 ?        00:00:00 [ksoftirqd/1]
1 S root         6     1  0 -40   - -     0 migrat Dec17 ?        00:00:01 [migration/2]
1 S root         7     1  0  94  19 -     0 ksofti Dec17 ?        00:00:00 [ksoftirqd/2]

SZ : approximate amount of swap space that would be required if the process were to dirty all
                           writable pages and then be swapped out. This number is very rough!
````

#### LINUX - source block 2

````text
$> ps aux
USER       PID %CPU %MEM   VSZ  RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0  4772  564 ?        S    Dec17   0:01 init [5]
root         2  0.0  0.0     0    0 ?        S    Dec17   0:00 [migration/0]
root         3  0.0  0.0     0    0 ?        SN   Dec17   0:00 [ksoftirqd/0]
root         4  0.0  0.0     0    0 ?        S    Dec17   0:00 [migration/1]
root         5  0.0  0.0     0    0 ?        SN   Dec17   0:00 [ksoftirqd/1]
root         6  0.0  0.0     0    0 ?        S    Dec17   0:01 [migration/2]

RSS : resident set size, the non-swapped physical memory that a task has used (in kiloBytes).
VSZ : virtual memory usage of entire process.
````

#### LINUX - source block 3

````text
$> free
             total       used       free     shared    buffers     cached
Mem:      16423300   15075408    1347892          0     227604    8810452
-/+ buffers/cache:    6037352   10385948
Swap:     32764556     928104   31836452
````

#### LINUX - source block 4

````text
$> vmstat 1 5
procs -----------memory---------- ---swap-- -----io---- --system-- ----cpu----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in    cs us sy id wa
 0  0 928104 1348148 227612 8810444    0    0     3    26    1     5  1  0 99  0
 0  0 928104 1348148 227612 8810444    0    0     0   156 1047 34212  0  0 100  0
 0  0 928104 1348148 227612 8810444    0    0     0    60 1012 34163  2  0 98  0
 0  0 928104 1348148 227612 8810444    0    0     0     0 1024 34142  0  0 100  0
 0  0 928104 1348148 227612 8810444    0    0     0    20 1014 34142  0  0 100  0

 swpd: the amount of virtual memory used.
 free: the amount of idle memory.
 buff: the amount of memory used as buffers.
 cache: the amount of memory used as cache.
````

#### LINUX - source block 5

````text
$> iostat 3 1
avg-cpu:  %user   %nice    %sys %iowait   %idle
           0.70    0.00    0.09    0.03   99.18
Device:            tps   Blk_read/s   Blk_wrtn/s   Blk_read   Blk_wrtn
sda               1.08         4.70        19.46    4417994   18312224
sda1              0.56         0.43        10.33     403074    9717672
sda2              0.01         0.13         2.05     120828    1930960
sda3              0.24         2.02         2.75    1905302    2586944
sda4              0.00         0.00         0.00          2          0
sda5              0.00         0.00         0.00       3646         16
sda6              0.27         2.11         4.33    1984142    4076632
sdb               4.36        43.73       401.08   41142700  377382768
sdb1              2.27        29.27       297.20   27540998  279645952
sdb2              2.09        14.45       103.87   13600254   97736816

tps
       Indicate  the  number  of transfers per second that were issued to the device. A transfer is an  I/O  request  to
       the  device.  Multiple  logical requests can be combined into a single I/O request to the device. A  transfer  is
       of indeterminate size.
Blk_read/s
       Indicate   the  amount  of  data  read  from  the  drive expressed in a number of blocks per second.  Blocks  are
       equivalent  to  sectors  with  2.4 kernels and newer and therefore have a size of 512 bytes. With older  kernels,
       a block is of indeterminate size.
Blk_wrtn/s
       Indicate  the  amount  of  data  written  to  the  drive expressed in a number of blocks per second.
Blk_read
       The total number of blocks read.
Blk_wrtn
       The total number of blocks written.
````

#### LINUX - source block 6

````text
$> netstat
Active Internet connections (w/o servers)
Proto Recv-Q Send-Q Local Address               Foreign Address             State
tcp        0      0 localhost:50273             localhost:20416             ESTABLISHED
tcp        0      0 localhost:20416             localhost:50273             ESTABLISHED
tcp        0      0 localhost:ftp-data          192.168.6.18:62643          TIME_WAIT
tcp        0      0 localhost:ftp-data          192.168.6.18:62640          TIME_WAIT

Proto
    The protocol (tcp, udp, raw) used by the socket.
Recv-Q
    The count of bytes not copied by the user program connected to this socket.
Send-Q
    The count of bytes not acknowledged by the remote host.
Local Address
    Address and port number of the local end of the socket.  Unless the --numeric (-n) option is specified, the  socket
    address  is  resolved  to  its canonical host name (FQDN), and the port number is translated into the corresponding
    service name.
Foreign Address
    Address and port number of the remote end of the socket.  Analogous to "Local Address."
State
    The state of the socket. Since there are no states in raw mode and usually no states used in UDP, this  column  may
    be left blank.
````

#### SUN System - source block 7

````text
$> ps -elf
 F S      UID   PID  PPID   C PRI NI     ADDR     SZ    WCHAN    STIME TTY         TIME CMD
 1 T     root     0     0   0   0 SY        ?      0            Sep 28 ?           1:48 sched
 0 S     root     1     0   0  40 20        ?    501        ?   Sep 28 ?           0:53 /sbin/init
 1 S     root     2     0   0   0 SY        ?      0        ?   Sep 28 ?           0:01 pageout
 1 S     root     3     0   0   0 SY        ?      0        ?   Sep 28 ?        2647:44 fsflush
 0 S     root   116     1   0  40 20        ?    634        ?   Sep 28 ?           0:00 /usr/lib/picl/picld

SZ : The total size of  the  process  in  virtual memory,   including  all  mapped  files  and
     devices, in pages.
````

#### SUN System - source block 8

````text
$> iostat 3 5
   tty        sd0           sd1           nfs1           cpu
 tin tout kps tps serv  kps tps serv  kps tps serv   us sy wt id
   0    1   0   0    0    2   0   15    0   0    0    0  0  0 99
   0   65   0   0    0    0   0    0    0   0    0    0  0  0 99
   0   22   0   0    0    0   0    0    0   0    0    0  0  0 99
   0   22   0   0    0    0   0    0    0   0    0    1  0  0 99
   0   22   0   0    0    1   0    0    0   0    0    0  1  0 98
````

#### SUN System - source block 9

````text
$> ifconfig -a
lo0: flags=2001000849<UP,LOOPBACK,RUNNING,MULTICAST,IPv4,VIRTUAL> mtu 8232 index 1
        inet xxx.xxx.xxx.xxx netmask ff000000
bge0: flags=1000843<UP,BROADCAST,RUNNING,MULTICAST,IPv4> mtu 1500 index 2
        inet xxx.xxx.xxx.xxx netmask ffffff00 broadcast 192.168.1.255
````

#### AIX - source block 10

````text
Topas Monitor for host:    aix53-t9             EVENTS/QUEUES    FILE/TTY
Tue Dec 22 13:54:01 2015   Interval:  2         Cswitch   40310  Readch    31765
                                                Syscall   32027  Writech  712.6K
CPU  User%  Kern%  Wait%  Idle%                 Reads        20  Rawin         0
ALL   20.6   16.3    1.4   61.7                 Writes        7  Ttyout      825
                                                Forks         0  Igets         0
Network  KBPS   I-Pack  O-Pack   KB-In  KB-Out  Execs         0  Namei       204
en0       1.0      3.5     1.5     0.2     0.9  Runqueue    0.0  Dirblk        0
lo0       0.0      0.0     0.0     0.0     0.0  Waitqueue   0.0
Disk    Busy%     KBPS     TPS KB-Read KB-Writ  PAGING           MEMORY
hdisk1    5.0      2.8K   10.1     0.0     2.8K Faults       89  Real,MB    7936
hdisk0    0.0      0.0     0.0     0.0     0.0  Steals        0  % Comp     90.0
                                                PgspIn        0  % Noncomp   9.9
Name            PID  CPU%  PgSp Owner           PgspOut       0  % Client    9.9
altibase     700654   6.1 663.3 hanulcat        PageIn        0
altibase     737490   5.8 377.4 durusari        PageOut     177  PAGING SPACE
java         786586   5.1  57.7 wsalti3         Sios        177  Size,MB   16896
altibase     508126   4.1 780.6 jeehb                            % Used     61.1
altibase     549024   3.1 396.0 dongjun         NFS (calls/sec)  % Free     39.9
altibase     794804   3.1 1808.6 wsalti3        ServerV2       0
altibase     577762   2.3 448.4 high7777        ClientV2       0   Press:
altibase     696356   1.4 1486.1 hyun1          ServerV3       0   "h" for help
altibase     282794   1.0 411.8 newhyuki        ClientV3       0   "q" to quit
altibase     532612   1.0 276.5 cheol
altibase     467112   0.9 411.2 gom
altibase     553176   0.8 258.0 taeseong
altibase     417846   0.8 1022.7 durusari
altibase     372888   0.7 309.9 hyundong
altibase     438348   0.6 284.7 eheejung
topas        389362   0.3   1.4 wsalti3
java         159854   0.1  20.3 root    i
getty        319520   0.0   0.5 root
ksh          802892   0.0   0.5 wsalti3
telnetd      675996   0.0   0.6 root
````

#### AIX - source block 11

````text
$> ps aux
USER        PID %CPU %MEM   SZ  RSS    TTY STAT    STIME  TIME COMMAND
root       8196 19.5  0.0  384  384      - A      Apr 14 141722:02 wait
root      53274 18.6  0.0  384  384      - A      Apr 14 134782:46 wait
hanulcat 700654  3.5  1.0 686892 42184      - A      Oct 23 6062:39 /home/ts2_team/h
durusari 737490  2.8  5.0 394120 389104      - A      Dec 16 500:43 /home/ts2_team/d
wsalti3  786586  1.9  0.0 59168 16052      - A      Sep 17 5331:05 /usr/java5/bin/j

SZ:  The virtual size of the data section of the process (in 1KB units).
RSS : The real-memory (resident set) size of the process (in 1KB units)
````

#### AIX - source block 12

````text
$>vmstat 1
System configuration: lcpu=2 mem=7936MB
kthr    memory              page              faults        cpu
----- ----------- ------------------------ ------------ -----------
 r  b   avm   fre  re  pi  po  fr   sr  cy  in   sy  cs us sy id wa
15  0 4186138  3380   0   0   0   0    0   0  13 31222 40260 21 16 63  0
 3  0 4186139  3379   0   0   0   0    0   0   7 30787 39611 21 16 63  0
 1  0 4186140  3378   0   0   0   0    0   0   9 30636 39011 22 16 62  0
13  0 4186136  3382   0   0   0   0    0   0  17 31331 40298 21 16 62  0
16  0 4186136  3382   0   0   0   0    0   0   7 31859 40632 22 16 62  0

Memory: information about the usage of virtual and real memory. Virtual pages are considered active if they have been accessed.
        A page is 4096 bytes.
avm : Active virtual pages.
fre : Size of the free list.
````

#### AIX - source block 13

````text
$>iostat 3 1
System configuration: lcpu=2 drives=2 paths=2 vdisks=0
tty:      tin         tout    avg-cpu: % user % sys % idle % iowait
          0.0         19.3               20.4  16.3   60.5      2.8
Disks:        % tm_act     Kbps      tps    Kb_read   Kb_wrtn
hdisk1           6.0     1893.3      13.3          0      5680
hdisk0           5.3      24.0       6.0          0        72

% tm_act : Indicates the percentage of time the physical disk/tape was active
          (bandwidth utilization for the drive).
Kbps : Indicates the amount of data transferred (read or written) to the drive in KB per second.
tps : Indicates the number of transfers per second that were issued to the physical disk/tape. A transfer is an I/O request to the
     physical disk/tape. Multiple logical requests can be combined into a single I/O request to the disk.
     A transfer is of indeterminate size.
Kb_read : The total number of KB read.
Kb_wrtn : The total number of KB written.
````

#### AIX - source block 14

````text
$> netstat
Active Internet connections
Proto Recv-Q Send-Q  Local Address          Foreign Address        (state)
tcp4       0      2  81.altibase.loca.telne 192.168.6.26.pscupd    ESTABLISHED
tcp4       0      0  localhost.29945        localhost.38131        ESTABLISHED
tcp4       0      0  localhost.38131        localhost.29945        ESTABLISHED
tcp4       0      0  81.altibase.loca.42129 as48-x64.altibas.39945 TIME_WAIT
tcp4       0      0  81.altibase.loca.42130 as48-x64.altibas.39945 TIME_WAIT
````

#### HP-UX - source block 15

````text
$> glance (a key after performing glance)

 GlancePlus C.04.55.00          15:57:51   rx6600     ia64    Current  Avg  High
--------------------------------------------------------------------------------
CPU  Util   SUU                                                |  6%    6%    6%
Disk Util   F          FV V                                    | 29%   29%   29%
Mem  Util   S     SU                 U                         | 57%   57%   57%
Swap Util   UUR      R                                         | 20%   20%   20%
--------------------------------------------------------------------------------
                                CPU BY PROCESSOR                    Users=    6
CPU  State     Util   LoadAvg(1/5/15 min)   CSwitch   Last Pid
--------------------------------------------------------------------------------
  3 Enable     12.1     0.1/  0.0/  0.0       175       25741
  4 Enable      0.0     0.1/  0.1/  0.1       167       18641
  6 Enable      0.0     0.1/  0.1/  0.1       158        1769
  7 Enable      5.2     0.0/  0.0/  0.0       263        1979
  8 Enable     53.4     0.1/  0.1/  0.1       155        1979
 10 Enable      0.9     0.1/  0.1/  0.1       163        1979
 13 Enable      0.9     0.0/  0.0/  0.0       244       18641
  5 Enable      0.0     0.0/  0.0/  0.0       219        1979
  2 Enable      1.7     0.1/  0.1/  0.1       204        1979
  9 Enable     13.8     0.0/  0.0/  0.0       261       25223
  0 Enable      0.0     0.1/  0.1/  0.1       160       18641
````

#### HP-UX - source block 16

````text
$> top
System: rx6600                                        Tue Dec 22 16:00:58 2015
Load averages: 0.08, 0.07, 0.07
430 processes: 362 sleeping, 68 running
Cpu states:
CPU   LOAD   USER   NICE    SYS   IDLE  BLOCK  SWAIT   INTR   SSYS
 0    0.15   3.8%   0.0%   1.4%  94.9%   0.0%   0.0%   0.0%   0.0%
 1    0.03   1.8%   0.0%   1.6%  96.6%   0.0%   0.0%   0.0%   0.0%
 2    0.08   8.9%   0.0%   2.0%  89.1%   0.0%   0.0%   0.0%   0.0%
 3    0.04   9.5%   0.0%   1.2%  89.3%   0.0%   0.0%   0.0%   0.0%
 4    0.06   7.9%   0.0%   0.4%  91.7%   0.0%   0.0%   0.0%   0.0%
 5    0.04   4.5%   0.0%   1.0%  94.5%   0.0%   0.0%   0.0%   0.0%
 6    0.13  14.8%   0.0%   0.0%  85.2%   0.0%   0.0%   0.0%   0.0%
 7    0.04   3.8%   0.0%   1.4%  94.9%   0.0%   0.0%   0.0%   0.0%
 8    0.09  14.8%   0.0%   2.0%  83.2%   0.0%   0.0%   0.0%   0.0%
 9    0.06   8.3%   0.0%   1.0%  90.7%   0.0%   0.0%   0.0%   0.0%
10    0.14  11.9%   0.0%   1.4%  86.8%   0.0%   0.0%   0.0%   0.0%
11    0.06   5.1%   0.0%   0.8%  94.1%   0.0%   0.0%   0.0%   0.0%
12    0.09  17.2%   0.0%   2.2%  80.6%   0.0%   0.0%   0.0%   0.0%
13    0.04   7.7%   0.0%   0.4%  91.9%   0.0%   0.0%   0.0%   0.0%
14    0.14  11.7%   0.0%   2.6%  85.8%   0.0%   0.0%   0.0%   0.0%
15    0.06   3.2%   0.0%   1.0%  95.9%   0.0%   0.0%   0.0%   0.0%
---   ----  -----  -----  -----  -----  -----  -----  -----  -----
avg   0.08   8.3%   0.0%   1.4%  90.3%   0.0%   0.0%   0.0%   0.0%
````

#### HP-UX - source block 17

````text
$> ps -elf
  F S      UID   PID  PPID  C PRI NI             ADDR   SZ            WCHAN    STIME TTY       TIME COMD
1003 S     root     0     0  0 127 20 e000000100769810    0 e000000100000004 12▒▒ 21  ?         0:25 swapper
541 R     root     1     0  0 152 20 e00000010415e380  481                - 12▒▒ 21  ?         0:04 init
1003 S     root    13     0  0 152 20 e0000001301a4080    0 e0000001301a30a0 12▒▒ 21  ?         0:00 net_str_cached
1003 S     root    12     0  0 152 20 e000000131004d00    0 e0000001301a3080 12▒▒ 21  ?         0:00 net_str_cached
1003 R     root    11     0  0 152 20 e000000131004a00    0                - 12▒▒ 21  ?         0:03 escsid

sz : The size in physical pages of the core image of the process, including text, data, and stack space.
     Physical page size is defined by _SC_PAGE_SIZE in the header file <unistd.h>
````

#### HP-UX - source block 18

````text
$> vmstat 1 5
         procs           memory                   page                              faults       cpu
    r     b     w      avm    free   re   at    pi   po    fr   de    sr     in     sy    cs  us sy id
    1     0     0  5614057  2977741    0    0     0    0     0    0     2   4639  11383  3479   0  0 100
    1     0     0  5614057  2977750    0    0     1    0     0    0     0   4648  10931  3786   0  0 100
    1     0     0  5614057  2977633    0    0     0    0     0    0     0   4645  10537  3788   0  0 100
    1     0     0  5614057  2977633    0    0     0    0     0    0     0   4642  10072  3783   0  0 100
    1     0     0  5614057  2977633    0    0     0    0     0    0     0   4638   9594  3776   0  0 100

memory : Information about the usage of virtual and real memory.
         Virtual pages are considered active if they belong to processes
         that are running or have run in the last 20 seconds.
avm : Active virtual pages
free : Size of the free list
````

#### HP-UX - source block 19

````text
$> netstat -nr
IPv4 Routing tables:
Destination           Gateway            Flags   Refs Interface  Pmtu
127.0.0.1             127.0.0.1          UH    0    lo0       32808
192.168.1.28          192.168.1.28       UH    0    lan0      32808
192.168.1.0           192.168.1.28       U     2    lan0       1500
127.0.0.0             127.0.0.1          U     0    lo0       32808
default               192.168.1.1        UG    0    lan0       1500
IPv6 Routing tables:
Destination/Prefix          Gateway                  Flags Refs Interface Pmtu
::1/128                     ::1                      UH    0    lo0      32808
fe80::217:a4ff:fe51:7308/128
                            fe80::217:a4ff:fe51:7308 UH    0    lan0     32808
fe80::/10                   fe80::217:a4ff:fe51:7308 U     2    lan0      1500
default                     fe80::221:d8ff:feb6:123f UG    0    lan0         0
````

### Table/Column Definition
Source path: `FAQE/Home/08. Monitoring/Table_Column Definition__22642961.md`

#### Table definition - source block 1

````text

-- USER_NAME  : Table owner
-- TABLE_NAME : Table name
-- RECORD_CNT : Number of records. Statistical information must be collected from this information in order to see accurate information. '-' means a table that has never collected statistical information.
-- CREATED_DATE : Date of table creation
-- LAST_DDL_DATE : Date of last DDL execution

SELECT U.USER_NAME 'USER_NAME'
     , T.TABLE_NAME 'TABLE_NAME'
     , DECODE(D.NUM_ROW, NULL, '-', D.NUM_ROW) 'RECORD_CNT'              -- Number of records,'-' is a table that has never collected statistical information
     , TO_CHAR(T.CREATED, 'YYYY-MM-DD HH:MI:SS') 'CREATED_DATE'          -- Date of table creation
     , TO_CHAR(T.LAST_DDL_TIME, 'YYYY-MM-DD HH:MI:SS') 'LAST_DDL_DATE'   -- Date of last DDL execution
  FROM SYSTEM_.SYS_USERS_ U
     , SYSTEM_.SYS_TABLES_ T
       LEFT OUTER JOIN V$DBMS_STATS D ON D.TARGET_ID = T.TABLE_OID AND D.TYPE = 'T'
 WHERE U.USER_ID NOT IN (0, 1)  -- System user PUBLIC, except SYSTEM_
   AND T.TABLE_TYPE = 'T'  -- Table only
   AND U.USER_ID = T.USER_ID
;
````

#### Table definition - source block 2

````text
-- USER_NAME  : Table owner
-- TABLE_NAME : Table name
-- CREATED_DATE : Date of table creation
-- LAST_DDL_DATE : Date of last DDL execution

SELECT U.USER_NAME 'USER_NAME'
     , T.TABLE_NAME 'TABLE_NAME'
     , TO_CHAR(T.CREATED, 'YYYY-MM-DD HH:MI:SS') 'CREATED_DATE'          -- Date of table creation
     , TO_CHAR(T.LAST_DDL_TIME, 'YYYY-MM-DD HH:MI:SS') 'LAST_DDL_DATE'   -- Date of last DDL execution
  FROM SYSTEM_.SYS_USERS_ U
     , SYSTEM_.SYS_TABLES_ T
 WHERE U.USER_ID NOT IN (0, 1)  -- System user PUBLIC, except SYSTEM_
   AND T.TABLE_TYPE = 'T'  -- Table only
   AND U.USER_ID = T.USER_ID
;
````

#### Table definition - source block 3

````text
-- USER_NAME  : Table owner
-- TABLE_NAME : Table name

SELECT U.USER_NAME 'USER_NAME'
     , T.TABLE_NAME 'TABLE_NAME'
  FROM SYSTEM_.SYS_USERS_ U
     , SYSTEM_.SYS_TABLES_ T
 WHERE U.USER_ID NOT IN (0, 1)  -- System user PUBLIC, except SYSTEM_
   AND T.TABLE_TYPE = 'T'  -- Table only
   AND U.USER_ID = T.USER_ID
;
````

#### Column definition - source block 4

````text
-- USER_NAME : Owner name
-- TABLE_NAME : Table name
-- COLUMN_NAME : Column name
-- DATA_TYPE : Data type
-- COLUMN_SIZE : Column size
-- CONST_TYPE : Constraint type
-- CHECK_CONDITION : Condition of CHECK constraint
-- COLUMN_ORDER : Column order

SELECT U.USER_NAME 'USER_NAME'
     , T.TABLE_NAME 'TABLE_NAME'
     , C.COLUMN_NAME 'COLUMN_NAME'
     , DECODE(C.DATA_TYPE, 1, 'CHAR', 12, 'VARCHAR', -8, 'NCHAR', -9, 'NVARCHAR', 2, 'NUMERIC/DECIMAL', 6, 'FLOAT/NUMBER', 8, 'DOUBLE', 7, 'REAL', -5, 'BIGINT', 4, 'INTEGER', 5, 'SMALLINT', 9, 'DATE', 30, 'BLOB', 40, 'CLOB', 20001, 'BYTE', 20002, 'NIBBLE', -7, 'BIT', -100, 'VARBIT', 10003, 'GEOMETRY') 'DATA_TYPE'
     , DECODE(C.DATA_TYPE, 2, C.PRECISION||'.'||C.SCALE, 6, C.PRECISION||'.'||C.SCALE, C.PRECISION) COLUMN_SIZE
     , DECODE(CONST.CONSTRAINT_TYPE, 0, 'FK', 1, 'NOT NULL', 2, 'UNIQUE', 3, 'PK', 4, 'NULL', 5, 'TIMESTAMP', 6, 'LOCAL UNIQUE', 7, 'CHECK') CONST_TYPE
     , CONST.CHECK_CONDITION
     , C.COLUMN_ORDER 'COLUMN_ORDER'
  FROM SYSTEM_.SYS_USERS_ U
     , SYSTEM_.SYS_TABLES_ T
     , SYSTEM_.SYS_COLUMNS_ C
       LEFT OUTER JOIN system_.SYS_CONSTRAINT_COLUMNS_ CONST_COL ON CONST_COL.COLUMN_ID = C.COLUMN_ID
       LEFT OUTER JOIN SYSTEM_.SYS_CONSTRAINTS_ CONST ON CONST.CONSTRAINT_ID = CONST_COL.CONSTRAINT_ID
 WHERE U.USER_NAME NOT IN ('PUBLIC', 'SYSTEM_')
   AND T.TABLE_TYPE = 'T'
   AND U.USER_ID = T.USER_ID
   AND T.TABLE_ID = C.TABLE_ID
 ORDER BY U.USER_NAME, T.TABLE_NAME, C.COLUMN_ORDER
;
````

#### Column definition - source block 5

````text
 -- USER_NAME : Name owner
-- TABLE_NAME : Table name
-- COLUMN_NAME : Column name
-- DATA_TYPE : Data type
-- COLUMN_SIZE : Column size
-- CONST_TYPE : Constraint type
-- COLUMN_ORDER : Column order

SELECT U.USER_NAME 'USER_NAME'
     , T.TABLE_NAME 'TABLE_NAME'
     , C.COLUMN_NAME 'COLUMN_NAME'
     , DECODE(C.DATA_TYPE, 1, 'CHAR', 12, 'VARCHAR', -8, 'NCHAR', -9, 'NVARCHAR', 2, 'NUMERIC/DECIMAL', 6, 'FLOAT/NUMBER', 8, 'DOUBLE', 7, 'REAL', -5, 'BIGINT', 4, 'INTEGER', 5, 'SMALLINT', 9, 'DATE', 30, 'BLOB', 40, 'CLOB', 20001, 'BYTE', 20002, 'NIBBLE', -7, 'BIT', -100, 'VARBIT', 10003, 'GEOMETRY') 'DATA_TYPE'
     , DECODE(C.DATA_TYPE, 2, C.PRECISION||'.'||C.SCALE, 6, C.PRECISION||'.'||C.SCALE, C.PRECISION) COLUMN_SIZE
     , DECODE(CONST.CONSTRAINT_TYPE, 0, 'FK', 1, 'NOT NULL', 2, 'UNIQUE', 3, 'PK', 4, 'NULL', 5, 'TIMESTAMP', 6, 'LOCAL UNIQUE', 7, 'CHECK') CONST_TYPE
     , C.COLUMN_ORDER 'COLUMN_ORDER'
  FROM SYSTEM_.SYS_USERS_ U
     , SYSTEM_.SYS_TABLES_ T
     , SYSTEM_.SYS_COLUMNS_ C
       LEFT OUTER JOIN system_.SYS_CONSTRAINT_COLUMNS_ CONST_COL ON CONST_COL.COLUMN_ID = C.COLUMN_ID
       LEFT OUTER JOIN SYSTEM_.SYS_CONSTRAINTS_ CONST ON CONST.CONSTRAINT_ID = CONST_COL.CONSTRAINT_ID
 WHERE U.USER_NAME NOT IN ('PUBLIC', 'SYSTEM_')
   AND T.TABLE_TYPE = 'T'
   AND U.USER_ID = T.USER_ID
   AND T.TABLE_ID = C.TABLE_ID
 ORDER BY U.USER_NAME, T.TABLE_NAME, C.COLUMN_ORDER
;
````

### Monitoring method when undo tablespace usage increases
Source path: `FAQE/Home/08. Monitoring/Undo Tablespace/Monitoring method when undo tablespace usage increases__22642963.md`

#### **Altibase 5.3.3 or later** - source block 1

````text
SELECT DECODE(TX.LOG_TYPE, 1, REP.REP_NAME, TX.SESSION_ID) AS SESSION_ID                                    -- Session ID that performed the transaction. Or the replication object name
     , TX.ID AS TX_ID                                                                                       -- Transaction ID
     , ST.ID AS STATEMENT_ID                                                                                -- STATEMENT ID
     , DECODE(TX.TSS_RID,  0, 'SELECT', 'UPDATE') AS TX_TYPE                                                -- Transaction type
     , DECODE(TX.STATUS,   0, 'BEGIN',  1, 'PRECOMMIT', 2, 'COMMIT_IN_MEMORY',
                           3, 'COMMIT', 4, 'ABORT',     5, 'BLOCKED', 6, 'END') AS TX_STATUS                -- Transaction status
     , DECODE(ST.EXECUTE_FLAG, 1, 'SQL ING', 0, 'SQL END')                      AS SQL_STATUS               -- SQL status
     , DECODE(TX.LOG_TYPE,     1, 'REP '||REP.PEER_IP||':'||REP.PEER_PORT, S.COMM_NAME) AS CLIENT_IP        -- Client IP
     , S.CLIENT_PID AS CLIENT_PID                                                                           -- Client process ID
     , DECODE(S.AUTOCOMMIT_FLAG, 1, 'ON', 0, 'OFF') AS AUTOCOMMIT                                           -- AUTOCOMMIT MODE
     , S.UTRANS_TIME_LIMIT AS UTRANS_TIMEOUT                                                                -- UTRANS_TIMEOUT setting value of the session
     , DECODE(ST.LAST_QUERY_START_TIME, NULL, '', ST.LAST_QUERY_START_TIME) AS LAST_QUERY_START_TIME        -- SQL statement start time
     , CASE
           WHEN TX.DISK_VIEW_SCN LIKE 'INFINITE%' THEN ''
           ELSE LTRIM(TX.DISK_VIEW_SCN)
       END AS DISK_VIEW_SCN                                                                                 -- Minimum SCN visible to the query transaction
     , CASE
           WHEN TX.MIN_DISK_LOB_VIEW_SCN LIKE 'INFINITE%' THEN ''
           ELSE LTRIM(TX.MIN_DISK_LOB_VIEW_SCN)
       END AS MIN_DISK_LOB_VIEW_SCN                                                                         -- Minimum SCN visible to the transaction querying LOB data
     , ROUND(((UD_S.TOTAL_EXTENT_COUNT * UD_S.PAGE_COUNT_IN_EXTENT * 8192) / 1024), 2) AS 'UNDO_USED_KB'    -- Undo usage of the update transaction
     , ST.UNDO_READ_PAGE + ST.UNDO_GET_PAGE AS UNDO_PAGE_COUNT                                              -- Undo pages
     , DECODE(TX.LOG_TYPE, 1, 'REMOTE_TX_ID : '||REP_TX.REMOTE_TID, LTRIM(ST.QUERY)) AS QUERY               -- Last query executed by the transaction
  FROM V$TRANSACTION TX
  LEFT JOIN (SELECT SESSION_ID
                  , TX_ID
                  , ID
                  , TO_CHAR(TO_DATE('1970010109','YYYYMMDDHH') + (LAST_QUERY_START_TIME) / (60*60*24), 'YYYY-MM-DD HH:MI:SS') LAST_QUERY_START_TIME
                  , EXECUTE_FLAG
                  , UNDO_READ_PAGE
                  , UNDO_GET_PAGE
                  , QUERY
               FROM V$STATEMENT
              WHERE (SESSION_ID, TX_ID, LAST_QUERY_START_TIME)
                 IN (SELECT SESSION_ID, TX_ID, MAX(LAST_QUERY_START_TIME) LAST_QUERY_START_TIME
                      FROM V$STATEMENT
                     GROUP BY SESSION_ID, TX_ID)) ST ON TX.ID = ST.TX_ID
  LEFT JOIN V$SESSION S         ON TX.SESSION_ID = S.ID
  LEFT JOIN V$REPRECEIVER_TRANSTBL REP_TX ON TX.ID = REP_TX.LOCAL_TID
  LEFT JOIN V$REPRECEIVER REP   ON REP_TX.REP_NAME = REP.REP_NAME
  LEFT JOIN V$TXSEGS TX_S       ON TX.ID = TX_S.TRANS_ID
  LEFT JOIN V$UDSEGS UD_S       ON TX_S.ID = UD_S.TXSEG_ENTRY_ID
 WHERE TX.TSS_RID <> 0                                      /* modified transaction */
    OR TX.MIN_DISK_LOB_VIEW_SCN NOT LIKE 'INFINITE%'        /* LOB access transaction */
    OR ((ST.UNDO_READ_PAGE <> 0 OR ST.UNDO_GET_PAGE <> 0)   /* transaction accessing undo pages */
         AND TX.DISK_VIEW_SCN NOT LIKE 'INFINITE%')
 ORDER BY SESSION_ID, TX_ID;
````

#### **Example Output** - source block 2

````text
SESSION_ID            : 2
TX_ID                 : 8766080
STATEMENT_ID          : 131072
TX_TYPE               : UPDATE                       -- Transaction with data modification
TX_STATUS             : BEGIN
SQL_STATUS            : SQL ING                      -- SQL statement is in progress
CLIENT_IP             : TCP 127.0.0.1:32102
CLIENT_PID            : 123203
AUTOCOMMIT            : OFF
UTRANS_TIMEOUT        : 3600
LAST_QUERY_START_TIME : 2025-12-02 16:30:47
DISK_VIEW_SCN         : 962767
MIN_DISK_LOB_VIEW_SCN : 962767
UNDO_USED_KB          : 41728                 -- Undo usage increases while the update statement is executing
UNDO_PAGE_COUNT       : 1589737
QUERY                 : UPDATE dt SET c10 = SYSDATE
````

#### **Evaluation Criteria** - source block 3

````text
SESSION_ID            : 2
TX_ID                 : 8766080
STATEMENT_ID          : 131072
TX_TYPE               : UPDATE                       -- Transaction with data modification
TX_STATUS             : BEGIN                        -- Transaction remains open
SQL_STATUS            : SQL END                      -- Statement execution has completed
CLIENT_IP             : TCP 127.0.0.1:32102
CLIENT_PID            : 123203
AUTOCOMMIT            : OFF
UTRANS_TIMEOUT        : 3600
LAST_QUERY_START_TIME : 2025-12-02 16:30:47
DISK_VIEW_SCN         :                              -- SCN is cleared after statement completion
MIN_DISK_LOB_VIEW_SCN :                              -- SCN is cleared after statement completion
UNDO_USED_KB          : 71168                        -- Undo usage no longer increases after completion
UNDO_PAGE_COUNT       : 2003444
QUERY                 : UPDATE dt SET c10 = SYSDATE
````

#### **Evaluation Criteria** - source block 4

````text
SESSION_ID            : 3
TX_ID                 : 1862209
STATEMENT_ID          :
TX_TYPE               : UPDATE                       -- Transaction with data modification
TX_STATUS             : BEGIN                        -- Transaction remains open
SQL_STATUS            :                              -- Statement has been released
CLIENT_IP             : TCP 127.0.0.1:11046
CLIENT_PID            : 206764
AUTOCOMMIT            : OFF
UTRANS_TIMEOUT        : 3600
LAST_QUERY_START_TIME : 2026-01-15 10:51:50
DISK_VIEW_SCN         :
MIN_DISK_LOB_VIEW_SCN :
UNDO_USED_KB          : 256
UNDO_PAGE_COUNT       :
QUERY                 :
````

#### **Example Output** - source block 5

````text
SESSION_ID            : 9
TX_ID                 : 53804352
STATEMENT_ID          : 589824
TX_TYPE               : SELECT                       -- Read-only transaction
TX_STATUS             : BEGIN
SQL_STATUS            : SQL ING                      -- Statement is in execution
CLIENT_IP             : TCP 127.0.0.1:17731
CLIENT_PID            : 190617
AUTOCOMMIT            : ON
UTRANS_TIMEOUT        : 0
LAST_QUERY_START_TIME : 2025-12-05 14:12:24
DISK_VIEW_SCN         : 322663
MIN_DISK_LOB_VIEW_SCN : 322663
UNDO_USED_KB          :                              -- No undo usage for read-only transactions
UNDO_PAGE_COUNT       : 35207                        -- Increasing value indicates active undo access
QUERY                 : SELECT * FROM TEST_DISK_TBL;
````

#### **Example Output** - source block 6

````text
SESSION_ID            : 1
TX_ID                 : 3393
STATEMENT_ID          : 65537
TX_TYPE               : UPDATE                       -- Transaction that has performed modifications
TX_STATUS             : BEGIN
SQL_STATUS            : SQL ING                      -- Statement is in execution
CLIENT_IP             : TCP 127.0.0.1:46339
CLIENT_PID            : 102737
AUTOCOMMIT            : OFF
UTRANS_TIMEOUT        : 3600
LAST_QUERY_START_TIME : 2026-01-15 11:13:24
DISK_VIEW_SCN         : 801111
MIN_DISK_LOB_VIEW_SCN : 801111
UNDO_USED_KB          : 71168                        -- Undo usage remains stable during query execution
UNDO_PAGE_COUNT       : 3024517                      -- Increasing value indicates active undo access
QUERY                 : SELECT * FROM dt
````

#### **Example Output** - source block 7

````text
SESSION_ID            : 4
TX_ID                 : 900929
STATEMENT_ID          : 589824
TX_TYPE               : SELECT
TX_STATUS             : BEGIN                        -- Transaction remains open
SQL_STATUS            : SQL END                      -- Statement execution has completed
CLIENT_IP             : TCP 127.0.0.1:49199
CLIENT_PID            : 170256
AUTOCOMMIT            : OFF
UTRANS_TIMEOUT        : 0
LAST_QUERY_START_TIME : 2025-12-05 14:12:24
DISK_VIEW_SCN         :
MIN_DISK_LOB_VIEW_SCN : 324055                       -- Presence of SCN indicates LOB data access
UNDO_USED_KB          :
UNDO_PAGE_COUNT       :
QUERY                 : SELECT * FROM demo_clob;
````

#### **Example Output** - source block 8

````text
SESSION_ID            : 4
TX_ID                 : 900929
STATEMENT_ID          :                              -- NULL indicates statement has been released
TX_TYPE               : SELECT
TX_STATUS             : BEGIN                        -- Transaction remains open
SQL_STATUS            :                              -- Statement has been released
CLIENT_IP             : TCP 127.0.0.1:49199
CLIENT_PID            : 170256
AUTOCOMMIT            : OFF
UTRANS_TIMEOUT        : 0
LAST_QUERY_START_TIME :
DISK_VIEW_SCN         :
MIN_DISK_LOB_VIEW_SCN : 324055                       -- Presence of SCN indicates LOB data access
UNDO_USED_KB          :
UNDO_PAGE_COUNT       :
QUERY                 :
````

#### **Example Output** - source block 9

````text
SESSION_ID            : 3
TX_ID                 : 155968
STATEMENT_ID          : 196609
TX_TYPE               : UPDATE                 -- Update transaction
TX_STATUS             : ABORT                  -- Rollback in progress
SQL_STATUS            : SQL ING
CLIENT_IP             : TCP 127.0.0.1:56757
CLIENT_PID            : 185015
AUTOCOMMIT            : OFF
UTRANS_TIMEOUT        : 0
LAST_QUERY_START_TIME : 2025-12-05 12:03:18
DISK_VIEW_SCN         :
MIN_DISK_LOB_VIEW_SCN :
UNDO_USED_KB          : 285696
UNDO_PAGE_COUNT       : 4045648
QUERY                 : rollback
````

#### **Example Output** - source block 10

````text
SESSION_ID            : 3
TX_ID                 : 155968
STATEMENT_ID          :
TX_TYPE               : UPDATE                 -- Update transaction
TX_STATUS             : ABORT                  -- Rollback in progress
SQL_STATUS            :
CLIENT_IP             :                        -- Session has been terminated
CLIENT_PID            :
AUTOCOMMIT            :
UTRANS_TIMEOUT        :
LAST_QUERY_START_TIME : 2025-12-05 12:03:18
DISK_VIEW_SCN         :
MIN_DISK_LOB_VIEW_SCN :
UNDO_USED_KB          : 285696
UNDO_PAGE_COUNT       : 4045648
QUERY                 :
````

#### **Example Output** - source block 11

````text
SESSION_ID            : REP                      -- Replication object name is displayed
TX_ID                 : 12354
STATEMENT_ID          :
TX_TYPE               : UPDATE
TX_STATUS             : BEGIN
SQL_STATUS            :
CLIENT_IP             : REP 192.168.1.145:53950
CLIENT_PID            :
AUTOCOMMIT            :
UTRANS_TIMEOUT        :
LAST_QUERY_START_TIME : 2025-12-05 17:22:31
DISK_VIEW_SCN         : 161183
MIN_DISK_LOB_VIEW_SCN : 161183
UNDO_USED_KB          : 19456
UNDO_PAGE_COUNT       : 18793
QUERY                 : REMOTE_TX_ID : 53835072
````

#### **Method A: Add a Data File** - source block 12

````text
-- 1. Check current data file configuration
SELECT RPAD(T.NAME, 20) SPACE_NAME
     , ROUND((D.INITSIZE*T.PAGE_SIZE)/1024/1024) AS 'INITSIZE(MB)'
     , ROUND((D.CURRSIZE*T.PAGE_SIZE)/1024/1024) AS 'CURRSIZE(MB)'
     , DECODE(D.AUTOEXTEND, 0, 'OFF', 1, 'ON') 'AUTOEXTEND'
     , ROUND((D.NEXTSIZE*T.PAGE_SIZE)/1024/1024) AS 'NEXTSIZE(MB)'
     , DECODE(D.MAXSIZE, 0, ROUND((D.CURRSIZE*T.PAGE_SIZE)/1024/1024), ROUND((D.MAXSIZE*T.PAGE_SIZE)/1024/1024)) AS 'MAXSIZE(MB)'
     , D.NAME DATAFILE
  FROM V$TABLESPACES T, V$DATAFILES D
 WHERE T.ID = D.SPACEID AND T.TYPE = 7
 ORDER BY 7;

-- 2. Example: add a data file
ALTER TABLESPACE SYS_TBS_DISK_UNDO ADD DATAFILE 'undo002.dbf' AUTOEXTEND ON NEXT 1M MAXSIZE 2G;
````

#### **Method B: Resize an Existing Data File** - source block 13

````text
-- 1. Example: When AUTOEXTEND is ON
ALTER TABLESPACE SYS_TBS_DISK_UNDO ALTER DATAFILE 'undo001.dbf' AUTOEXTEND ON NEXT 1M MAXSIZE 4G;

-- 2. Example: When AUTOEXTEND is OFF
ALTER TABLESPACE SYS_TBS_DISK_UNDO ALTER DATAFILE 'undo001.dbf' SIZE 4G;
````

#### **Terminating a Session** - source block 14

````text
ALTER DATABASE database_name SESSION CLOSE session_id ;
````

#### **Terminating a Client Process** - source block 15

````text
$ kill -9 <process_id>
````

#### **Example** - source block 16

````text
-- Delete rows 1–1000 and commit
DELETE FROM emp WHERE eno BETWEEN 1 AND 1000;
COMMIT;

-- Delete rows 1001–2000 and commit
DELETE FROM emp WHERE eno BETWEEN 1001 AND 2000;
COMMIT;

-- Delete rows 2001–3000 and commit
DELETE FROM emp WHERE eno BETWEEN 2001 AND 3000;
COMMIT;
````

#### **Example** - source block 17

````text
-- Delete up to 1,000 rows per execution (repeat as needed)
DELETE FROM emp WHERE status = 'D' LIMIT 1000;
COMMIT;
````

#### **Session-Level Configuration** - source block 18

````text
ALTER SESSION SET UTRANS_TIMEOUT = 3600;   -- Unit: seconds
````

#### **Session-Level Configuration** - source block 19

````text
  sProps.put("utrans_timeout", "300");
  Connection con = DriverManager.getConnection(url, sProps);
````

#### **Session-Level Configuration** - source block 20

````text
  strcpy(conn_opt3, "DSN=localhost;CONNTYPE=1;UTRANS_TIMEOUT=300");
  EXEC SQL CONNECT :usr IDENTIFIED BY :pwd USING :conn_opt3;
````

#### **System-Level Configuration** - source block 21

````text
ALTER SYSTEM SET UTRANS_TIMEOUT = 3600;   -- unit: seconds
````

#### **System-Level Configuration** - source block 22

````text
$ vi $ALTIBASE_HOME/conf/altibase.properties
UTRANS_TIMEOUT = 3600
````

### Undo tablespace usage
Source path: `FAQE/Home/08. Monitoring/Undo Tablespace/Undo tablespace usage__22642965.md`

#### Undo tablespace usage - source block 1

````text
SELECT T.NAME TBS_NAME
     , ROUND(D.MAX * PAGE_SIZE / 1024 /1024, 2) 'MAX(M)'                                                                        -- Max size of undo tablespace
     , ROUND((TOTAL_PAGE_COUNT * PAGE_SIZE) / 1024 / 1024, 2) 'TOTAL(M)'                                                        -- Total size allocated for undo tablespace
     , ROUND((U.TOTAL_EXT_CNT*PROP.EXTENT_SIZE)/1024/1024, 2) 'ALLOC(M)'                                                        -- Total of only 'used pages' excluding 'blank pages' among the allocated pages so far
     , ROUND(((U.TX_EXT_CNT+U.USED_EXT_CNT+U.UNSTEALABLE_EXT_CNT) * PROP.EXTENT_SIZE)/1024/1024, 2) 'USED(M)'                   -- Size of the EXTENT that cannot be reused or in use by the change transaction
     , ROUND((((U.TX_EXT_CNT+U.USED_EXT_CNT+U.UNSTEALABLE_EXT_CNT) * PROP.EXTENT_SIZE)/(D.MAX*PAGE_SIZE))*100, 2) 'USAGE(%)'    -- USED compared with MAX
     , DECODE(STATE,1,'OFFLINE',2,'ONLINE',5,'OFFLINE BACKUP',6,'ONLINE BACKUP',128,'DROPPED', 'DISCARDED') STATE               -- Tablespace state
     , D.AUTOEXTEND
  FROM V$TABLESPACES T
     , (SELECT SPACEID
             , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
             , DECODE(MAX(AUTOEXTEND),1,'ON','OFF') 'AUTOEXTEND'
          FROM V$DATAFILES
         GROUP BY SPACEID) D
     , V$DISK_UNDO_USAGE U
     , (SELECT VALUE1 EXTENT_SIZE FROM V$PROPERTY WHERE NAME = 'SYS_UNDO_TBS_EXTENT_SIZE') PROP
 WHERE T.ID = D.SPACEID
   AND T.ID = 3 ;
````

#### Undo tablespace usage - source block 2

````text
TBS_NAME                        MAX(M)      TOTAL(M)    ALLOC(M)    USED(M)     USAGE(%)    STATE           AUTOEXTEND
---------------------------------------------------------------------------------------------------------------------------------
SYS_TBS_DISK_UNDO               2047.99     302         122.25      84.25       4.11        ONLINE          ON
1 row selected.
````


## Validation and troubleshooting

Use query IDs by symptom:

| Symptom or question | Primary query IDs or source rows |
| --- | --- |
| How many statements exist or execute now? | `ST01`, `ST03`, `ST10` |
| Which query is active, long-running, full scanning, or tied to a session? | `ST02`, `ST04`, `ST05`, `ST07`, `ST08`, `ST09` |
| Which last DML statement belongs to a long transaction? | `ST06` |
| Which service thread is active or contended? | `SV01`, `SV02` |
| Which transaction is blocking or holding a lock? | `TL01`, lock FAQ queries using `v$lock`, `v$lock_wait`, `v$lock_statement`, `v$statement`, `v$session` |
| Are redo log files accumulating or log-file preparation waits growing? | `LO01`, `LO02`, `V$LFG.LF_PREPARE_WAIT_COUNT` |
| Is memory DB GC waiting behind an old transaction or statement? | `GC01`, `GC02` |
| How much memory does Altibase allocate? | `MS01`, `MS02`, `V$MEMSTAT` |
| Which tablespace, datafile, undo, temporary tablespace, or I/O path is growing? | `TS01` through `TS14`, disk tablespace FAQ variants, undo FAQ variants |
| Is disk buffer hit ratio low? | `DB01` |
| Which memory/disk objects, partitions, sequences, synonyms, PSMs, views, packages, triggers, jobs, users, or tablespaces exist? | `OB01` through `OB20` |
| Which privileges, roles, constraints, or indexes exist? | `PV01` through `PV05`, `CT01` through `CT04` |
| What is replication sender, receiver, gap, retained redo log, or target-table status? | `RP01` through `RP06` |
| Which SQLs are executed by the server and what were the bind values/plans/statistics? | `altiProfile` procedure and `QUERY_PROF_FLAG` outputs |
| What OS evidence should be collected? | `System information by OS` command catalog for Linux, Sun, AIX, and HP-UX |

For disk, memory, and tablespace usage, use the source variant that matches the Altibase version. Several FAQ pages preserve older SQL because view columns changed across versions. If an answer must cover multiple versions, present the version-specific choices rather than giving only the newest query.

For lock response, identify the lock holder before closing a session. Closing a session can interrupt application work and may trigger rollback for DML transactions. For undo growth, terminating a DML session can increase rollback work before the space is reclaimed.

For `altiProfile`, always stop profiling after the observation window. Leaving `QUERY_PROF_FLAG` enabled can produce heavy profile logs under `$ALTIBASE_HOME/trc` or `QUERY_PROF_LOG_DIR` and can affect performance.

## Version-specific notes

- The monitoring-query guide warns that meta tables and performance views can be added, deleted, or have column-name changes depending on Altibase server version.
- `V$STATEMENT` query execution statistics require `TIMED_STATISTICS=1`; default is `0`.
- Disk DB GC disappeared after the disk DB MVCC method changed from Altibase `5.3.3`; only memory DB GC remains in the terminology used by the guide.
- `V$VOL_TABLESPACES` was added from `ALTIBASE HDB 5.5.1`, so memory tablespace usage including volatile memory tablespaces uses the `5.5.1`, `6.1.1`, `6.3.1` FAQ query.
- `BUG-31372` added the `TOTAL_USED_SIZE` column of `X$SEGMENT`, which affects disk table and index usage queries for `5.3.x`, `5.5.1`, `6.1.1`, and `6.3.1`.
- The rollback-query FAQ applies to `ALTIBASE HDB 5.1.5` or later.
- The lock-property FAQ is based on `ALTIBASE HDB 6.3.1` and states that both `ALTIBASE HDB 5` and `ALTIBASE HDB 6` can use it, but some monitoring items may cause result errors.
- The undo monitoring FAQ query is for `Altibase 5.3.3 or later`.

## Related errors

R011 is primarily monitoring and diagnostics, not an error-message catalog. Error answers should normally link to R013/R014 once those jobs are complete. Within this R011 scope, preserve these operational failure conditions:

| Condition | Monitoring evidence or action |
| --- | --- |
| Lock waits and lock timeout symptoms | Inspect `v$lock`, `v$lock_wait`, `v$lock_statement`, `v$statement`, and `v$session`; close the target session only after confirming impact. |
| Undo tablespace exhaustion risk | Identify long update, open transaction, undo-image reader, LOB resource, rollback, or replication transaction; expand undo datafiles or remove the root cause. |
| Redo log preparation waits | Inspect `V$LFG.LF_PREPARE_WAIT_COUNT`; if large, increase `PREPARE_LOG_FILE_COUNT` and restart Altibase. |
| Profile log disk pressure | Stop `QUERY_PROF_FLAG` and monitor disk usage when `altiProfile` tracing is enabled. |
| Replication delay retaining redo logs | Use `RP03`, `RP05`, and related replication monitoring to measure gap and retained log risk. |

## Attachments and external references

Preserved document-format attachments and source references:

- `ALTIBASE_모니터링_쿼리_가이드.pdf`: `https://docs.altibase.com/download/attachments/10060431/ALTIBASE_%EB%AA%A8%EB%8B%88%ED%84%B0%EB%A7%81_%EC%BF%BC%EB%A6%AC_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1698627365000&api=v2`
- `altimon_for_windows.zip`: `https://docs.altibase.com/download/attachments/7340488/altimon_for_windows.zip?version=1&modificationDate=1415946725000&api=v2`
- `ALTIMON_USER_GUIDE.pdf`: `https://docs.altibase.com/download/attachments/6979592/ALTIMON_USER_GUIDE.pdf?version=2&modificationDate=1422495172000&api=v2`

Non-document-format but source-preserved monitoring artifacts include `altimon.bat`, `altimon.vbs`, `altimon_linux_631.tar`, `altimon_linux_611.tar`, `altimon_sunos_x86_439.tar`, `altimon_linux.tar`, `altimon_hpux_ia64.tar`, `altimon_sunos_sparc.tar`, `altimon.conf.631`, `altimon.conf.5.1.5`, and embedded PNG/JPEG diagrams or screenshots. These are registered as `not_document_format` in the attachment register.

The legacy `ALTIMON USER GUIDE` label from the Korean source is a hash-only label with no downloadable source URL. It is preserved as `legacy_no_downloadable_url`; do not invent a URL from the label.

External references preserved from R011 sources include:

- Altibase manuals: `https://github.com/ALTIBASE/Documents/tree/master/Manuals`
- Altibase support portal references: `http://altibase.com/support-center/en/`, `http://support.altibase.com/en/`
- Replication transaction manual link used by the undo FAQ: `https://manual.altibase.com/7.3/en/admin/replication/1.-Replication-Overview/#replication-transaction`
- `BUG-31372`: `https://altra.altibase.com/altimis-2.0/app_bug_new/bug_view.jsp?pk=31372`

## Terminology

Keep these exact identifiers untranslated in multilingual answers:

`TIMED_STATISTICS`, `QUERY_PROF_FLAG`, `QUERY_PROF_LOG_DIR`, `UTRANS_TIMEOUT`, `PREPARE_LOG_FILE_COUNT`, `VOLATILE_MAX_DB_SIZE`, `V$PROPERTY`, `V$SESSION`, `V$STATEMENT`, `V$SQLTEXT`, `V$PLANTEXT`, `V$SERVICE_THREAD`, `V$TRANSACTION`, `V$MEMGC`, `V$LOCK`, `V$LOCK_WAIT`, `V$LOCK_STATEMENT`, `V$TABLESPACES`, `V$MEM_TABLESPACES`, `V$VOL_TABLESPACES`, `V$DATAFILES`, `V$SEGMENT`, `V$MEMTBL_INFO`, `V$DISKTBL_INFO`, `V$INDEX`, `V$LFG`, `V$ARCHIVE`, `V$DATABASE`, `V$BUFFPOOL_STAT`, `V$REPSENDER`, `V$REPGAP`, `V$REPRECEIVER`, `V$REPSENDER_TRANSTBL`, `V$REPRECEIVER_TRANSTBL`, `X$SEGMENT`, `X$TEMPTABLE_STATS`, `SYSTEM_.SYS_USERS_`, `SYSTEM_.SYS_TABLES_`, `SYSTEM_.SYS_COLUMNS_`, `SYSTEM_.SYS_CONSTRAINTS_`, `SYSTEM_.SYS_CONSTRAINT_COLUMNS`, `SYSTEM_.SYS_INDICES_`, `SYSTEM_.SYS_REPLICATIONS_`, `SYSTEM_.SYS_REPL_HOSTS_`, `SYSTEM_.SYS_REPL_ITEMS_`, `SYSTEM_.SYS_TBS_USERS_`, `SYSTEM_.SYS_PRIVILEGES_`, `SYSTEM_.SYS_GRANT_SYSTEM_`, `SYSTEM_.SYS_GRANT_OBJECT_`, `SYSTEM_.SYS_VIEWS_`, `SYSTEM_.SYS_VIEW_PARSE_`, `SYSTEM_.SYS_PROCEDURES_`, `SYSTEM_.SYS_PROC_PARSE_`, `altiProfile`, `altimon`, `altimon.conf`, `altimon.bat`, `altimon.vbs`, `$ALTIBASE_HOME`, `$ALTIBASE_HOME/trc`, `$ALTIBASE_HOME/conf/altibase.properties`, `ST01` through `ST10`, `SV01`, `SV02`, `TL01`, `LO01`, `LO02`, `GC01`, `GC02`, `MS01`, `MS02`, `TS01` through `TS14`, `DB01`, `OB01` through `OB20`, `PV01` through `PV05`, `CT01` through `CT04`, and `RP01` through `RP06`.
