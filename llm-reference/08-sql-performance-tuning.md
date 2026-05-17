# SQL, Stored Procedures, Query Behavior, and Performance Tuning

## Source paths

Korean-source-verified and link-validated source paths covered by R015 and R016:

- `arch/Home/Altibase Development Guide__14058519.md`
- `arch/Home/Altibase Development Guide/1. Considerations when Designing__22642998.md`
- `arch/Home/Altibase Development Guide/2. Considerations when Developing__14058531.md`
- `arch/Home/Altibase SQL Tuning Guide__22643010.md`
- `FAQE/Home/05. SQL/Comparison between VARCHAR and CHAR types__16876151.md`
- `FAQE/Home/05. SQL/How to check the privileges granted to an object__16876153.md`
- `FAQE/Home/06. Stored Procedure/How to check the contents of stored procedure__16876159.md`
- `FAQE/Home/06. Stored Procedure/How to check the number of records affected by DML within the stored procedure__16876157.md`
- `FAQE/Home/12. Others/Building a Large-Scale DRDB Index__22642978.md`

English-only auxiliary source paths used by R016. These are useful performance diagnostics but are not Korean-source-verified:

- `FAQE/Home/ALTIBASE HDB Performance Tuning/Performance diagnostics for ALTIBASE HDB__1802804.md`
- `FAQE/Home/ALTIBASE HDB Performance Tuning/Performance diagnostics for ALTIBASE HDB/1. Application side diagnostics__1802808.md`
- `FAQE/Home/ALTIBASE HDB Performance Tuning/Performance diagnostics for ALTIBASE HDB/2. Database side diagnostics__1802812.md`
- `FAQE/Home/ALTIBASE HDB Performance Tuning/Performance diagnostics for ALTIBASE HDB/3. System side diagnostics__1802815.md`

Additional Development Guide chapters read for the wildcard boundary, but canonically owned elsewhere:

- `arch/Home/Altibase Development Guide/3. Altibase Trace Logs__22643000.md` - R012 owns trace-log diagnostics; R016 only cross-references DDL/index-build log evidence where relevant.
- `arch/Home/Altibase Development Guide/4. CLIENT APPLICATION Error Messages__14058547.md` - R013 owns client application error-message coverage; R016 only cross-references performance-related errors where relevant.

## Source coverage notes

This document covers R015 and R016. R015 covers SQL behavior, stored procedure inspection, stored procedure row-count examples, connection/session query behavior, cursor behavior, LOB query restrictions, prepared statement usage, timeout behavior, exact SQL examples, object privilege queries, and development cautions that affect SQL answerability.

The R015 source set is Korean-source-verified. `FAQE/Home/06. Stored Procedure/How to check the number of records affected by DML within the stored procedure__16876157.md` is link-validated Korean-source-verified because Phase 2 verified the preserved support artifact URL for `SP_DML_RECORD_COUNT.txt`.

`SP_DML_RECORD_COUNT.txt` is a downloadable `.txt` support artifact, not a document-format attachment under the `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.zip` preservation gate. The exact source URL is preserved in this topic and in `llm-reference/coverage/attachment-diagram-register.tsv`.

R016 covers performance design, storage placement, HPT, partition-table caveats, native data type selection, join/index design, execution-plan reading, index scan failure patterns, join/LIMIT/subquery/DML tuning guidance, runtime diagnostic SQL, plan cache, log/checkpoint/GC tuning, system-side evidence capture, and large DRDB index build settings. The `arch/Home/Altibase SQL Tuning Guide__22643010.md` page is a link-validated Markdown wrapper for two preserved PDF URLs. The linked `D68_Altibase_SQL_Tuning_Guide.pdf` was read during R016 and its Korean slide content is represented below in English while exact SQL, properties, hints, object names, and paths are preserved.

The `FAQE/Home/ALTIBASE HDB Performance Tuning` tree is `English-only source` material. It is integrated as auxiliary diagnostic guidance and must not be described as Korean-source-verified. Its semantic-unit rows use `english_only_auxiliary` status and retain the source-label risk.

The wider Altibase Development Guide source also contains two Korean legacy PDF labels, `ALTIBASE_개발가이드.pdf` and `ALTIBASE_개발가이드_5.3.pdf`, with no downloadable source URL. R013 already registers those labels for the client application error chapter; this document does not invent URLs for them.

## Scope and audience

Use this document to answer developer, DBA, support, and LLM questions about Altibase SQL behavior and performance: connection type selection, auto-commit, session timeout settings, cursor lifecycle, commit and rollback during fetch, error checking around `PREPARE` and `DECLARE CURSOR`, LOB query requirements, prepared statements, execution-plan checks, index and optimizer behavior, HPT and partition-table caveats, DRDB index build properties, diagnostic SQL, performance-view interpretation, `CHAR` and `VARCHAR` comparison behavior, object privilege lookup SQL, stored procedure body extraction, and `SQL%ROWCOUNT`.

When answering in another language, keep SQL keywords, object names, meta table names, view names, properties, connection-string options, error messages, filenames, and URLs exactly as written.

## Key facts

### Development session and query behavior

Altibase connection type is selected with `CONNTYPE=n`.

| Connection type | Meaning | Source guidance |
| --- | --- | --- |
| `CONNTYPE=1` | TCP/IP | Use for normal connections and for applications on a different server from the DBMS. |
| `CONNTYPE=2` | UNIX Domain Socket | Available only on the local server; recommended for local applications to reduce network communication cost. |
| `CONNTYPE=3` | IPC | Available only on the local server; recommended for local applications to reduce network communication cost. |

JDBC connections use auto-commit mode by the standard specification. Other applications use the `AUTO_COMMIT` property in `$ALTIBASE_HOME/conf/altibase.properties` unless the application or session changes it. If `AUTO_COMMIT = 1`, commit is performed automatically after a change transaction completes normally.

To switch a session to non-auto-commit mode:

```sql
ALTER SESSION SET AUTOCOMMIT = FALSE;
```

In Java, use `setAutoCommit`. `ALTER SYSTEM` can change the setting at runtime for the whole system, but the value is restored after restart, so persistent system-wide changes require editing `$ALTIBASE_HOME/conf/altibase.properties` and restarting Altibase.

Threaded programs and connection pools must not let multiple threads use one connection without concurrency control. Altibase communication follows protocol order such as `PREPARE -> BIND -> EXECUTE -> FETCH`. If another SQL interrupts the required order on the same connection, session processing can fail with messages such as:

```text
Communication link failure (EXEC->INVL)
Communication link failure (PREP->EXEC)
Invalid request to process the SQL statement
```

Applications should release SQL resources explicitly. Java code should close `ResultSet`, `Statement`, and `Connection` in `finally`. In CLI/ODBC, release a statement allocated with `SQLAllocStmt` by calling `SQLFreeStmt`; use `SQL_CLOSE` when reusing a statement and `SQL_DROP` to release it completely.

### Timeout properties and session state

Altibase manages connected sessions with timeout policies. The Development Guide states that the Korean-source-highlighted options `CONNECTION_TIMEOUT` and `TIMEOUT` can be controlled only in the connection string.

| Timeout option | Session state after error | Meaning |
| --- | --- | --- |
| `CONNECTION_TIMEOUT` | Disconnected | Timeout while blocked between network send and receive after connecting to the DB. |
| `TIMEOUT` | Disconnected | Timeout while trying to connect to the DB. |
| `QUERY_TIMEOUT` | Connected | Total query execution time exceeded while connected to the DB. |
| `FETCH_TIMEOUT` | Disconnected | Time between `FETCH` protocol operations exceeded after a `SELECT`. |
| `IDLE_TIMEOUT` | Disconnected | Idle time with no query exceeded while connected to the DB. |
| `UTRANS_TIMEOUT` | Disconnected | Time before `COMMIT` or `ROLLBACK` after query execution exceeded; the execution query is rolled back. |

Connection-string example:

```text
DSN=127.0.0.1;CONNTYPE=2;TIMEOUT=5;CONNECTION_TIMEOUT=30
```

Per-session timeout examples:

```sql
ALTER SESSION SET QUERY_TIMEOUT = 30;
ALTER SESSION SET FETCH_TIMEOUT = 30;
```

A timeout value of `0` means unlimited. Other timeout settings use the units configured in `$ALTIBASE_HOME/conf/altibase.properties`.

The application-visible timeout messages are:

| Timeout option | Error message |
| --- | --- |
| `CONNECTION_TIMEOUT` | `Connection time out` |
| `FETCH_TIMEOUT` | `The session has been closed by the server` |
| `IDLE_TIMEOUT` | `The session has been closed by the server` |
| `QUERY_TIMEOUT` | `Client's query exceeded in the execution time limitation` |
| `TIMEOUT` | `Client unable to establish connection` |
| `UTRANS_TIMEOUT` | `The session has been closed by the server` |

Timeout-related errors are also recorded in `$ALTIBASE_HOME/trc/altibase_boot.log`. If the timeout is caused by a query-processing bottleneck, tune the query. If `UTRANS_TIMEOUT` occurs, correct transaction-control logic so `COMMIT` or `ROLLBACK` is performed. If business processing must be forced, prefer changing the timeout for the program's DB session instead of changing the whole DB property.

### Cursor, SQL error, and LOB behavior

When using a `SELECT` cursor, check errors on `FETCH` and close the cursor after an error or after all data is read. Fetching a cursor that has already been read or operating on a cursor that has not been closed can cause unintended errors.

In Altibase, if `COMMIT` or `ROLLBACK` occurs during `FETCH`, the open cursor is automatically closed. If another transaction must be processed while fetching, use a separate DB session or complete all fetch operations before `COMMIT` or `ROLLBACK`. For large changes, prefer a structure that processes data through separate sessions or separable conditions rather than one bulk change transaction.

Check SQL errors at every SQL processing step. If an error at `PREPARE` or `DECLARE CURSOR` is not checked, a later `EXECUTE` or `OPEN` can report an error such as `Not defined (XX)` and obscure the real cause.

LOB columns require non-auto-commit mode when queried. If a LOB type is included in the `SELECT` target list while the connection is in auto-commit mode, the source records:

```text
[ERR-91101 : Connection is in autocommit mode. One can not operate on LOB data with autocommit mode on.]
```

Queries that exclude LOB columns are not affected. With the ALTIBASE HDB 6.3.1 or later JDBC driver, LOB data can be queried in auto-commit mode by enabling client-side transaction commit control, for example `ClientSide_Auto_Commit = On` in `altibase_cli.ini`.

### Prepared statements and execution plans

Altibase stores execution plans for internally executed queries. If an application repeatedly performs `PREPARE` and `EXECUTE` for the same query, the prepared execution plan can be reused internally, but the network cost of `PREPARE` is still incurred every time. Prepare once and execute repeatedly where possible.

Preferred pattern:

```text
Prepare statement
while (1)
{
    Execute statement
}
```

Avoid this pattern when the same statement can be reused:

```text
while (1)
{
    Prepare statement
    Execute statement
}
```

For dynamic SQL constructed each time:

```c
sprintf (sql, "INSERT INTO t1 VALUES (%d, %d)", szNum1, szNum2);
EXEC SQL Prepare S for :sql;
EXECUTE S;
```

Prefer host variables where possible:

```sql
EXEC SQL INSERT INTO t1 VALUES (:szNum1, :szNum2);
```

Use the execution plan before development or before release to verify whether each query uses the intended access path:

```sql
ALTER SESSION SET EXPLAIN PLAN = ON;
```

### Bulk change cautions

Bulk changes can affect memory, redo logs, locks, and replication.

| Caution | Source guidance |
| --- | --- |
| Memory increase in memory tables | Altibase MVCC duplicates records into empty table space when changes occur. Ten million changes can create ten million copied versions. The increased area can be reused as data or replication area, but it is not released in real time. |
| Redo log growth | A large transaction writes redo for each changed row. Altibase deletes transaction log files at checkpoint, but a log file cannot be deleted while information for an ongoing transaction remains in it. This can cause disk shortage. |
| Replication deadlock or delay | In replication, all changed records in one transaction are sent to the peer. The peer Receiver holds locks on those records; if the peer changes the same range, a deadlock can occur between replicated changes and peer-local transactions. |

### Performance design, HPT, and partitioning

Choose the table storage location according to workload:

| Storage choice | Use when | Performance caveat |
| --- | --- | --- |
| Memory tablespace | Very high processing performance is needed, transactions are frequent, and data validity is short, such as session information or same-day transaction data. | Memory capacity and MVCC garbage behavior still need operational monitoring. |
| Disk tablespace | Long-term retention or large-volume historical querying is needed. | Queries that access large disk ranges remain subject to disk I/O performance. |
| `Hybrid Partitioned Table (HPT)` | One logical table should combine memory partitions for recent data and disk partitions for older data. | Applications can query one table without separating tables, but queries that include disk partitions are still affected by disk I/O performance. |

For ALTIBASE partition tables as of version `7.3.0`, partitioned local indexes and non-partitioned global indexes are supported, while partitioned global indexes are not supported. Partition tables are recommended for separating historical data by month or business purpose. A significant performance decrease can occur when a query scans the entire partition table without including the partition key in the condition clause.

Column type selection can affect performance:

- Prefer native numeric types when they can represent the value: `SMALLINT`, `INTEGER`, `BIGINT`, or `DOUBLE`.
- Use `NUMERIC(p, s)` only when exact precision is required. It supports up to 38 digits, but storage and comparison require internal conversion.
- For simple integer data, choose the smallest appropriate type among `SMALLINT`, `INTEGER`, and `BIGINT`.
- Use `DOUBLE` for floating-point data when fixed precision is not mandatory.
- For columns frequently used in `SUM` or `AVG`, prefer `DOUBLE` or `BIGINT` when the business semantics allow it.
- Use `DATE` when date operations are important. Use `CHAR` or `VARCHAR` only when the value is limited to search or comparison operations.
- Define join columns with the same data type. Comparisons between different data types trigger internal conversion and can prevent efficient index use.

Avoid indiscriminate foreign-key use where transaction performance is critical. For replication target tables, maintain a primary key.

### Index and optimizer fundamentals from the SQL Tuning Guide

SQL tuning means changing or revising SQL so the required result is produced with minimum cost such as I/O, CPU usage, and elapsed time. The SQL Tuning Guide also treats index composition and placement as part of SQL tuning. It warns that tuning has limits if performance was not considered during modeling, when a very large result set is returned, or when the business process must handle a very large volume as a whole.

Altibase indexes use a sorted B-tree structure and separate storage space. Memory-table indexes consist of sorted pointers to existing data and are about `16 bytes` per row. Disk-table indexes contain data values and the address of the row location.

| Index type | Tuning meaning |
| --- | --- |
| Single-column index | Sorts by one column. Consider only ordering such as `ASC` or `DESC`. |
| Composite index | Uses multiple columns. Column order and ordering per column are critical; create it after checking the conditions commonly used by the workload. |
| Unique index | A primary key creates a unique index that disallows `NULL`; the optimizer can navigate from the root node to a table pointer and then read the row. |
| Non-unique index | Multiple rows can match one key; the index still provides row pointers for matching table rows. |

The source cautions:

- For memory tables, index access is generally advantageous over full scan.
- For disk tables, an index is not always faster than a full scan; selectivity matters.
- Index benefit grows as the target range becomes smaller.
- Not every SQL shape can use an index. SQL may need to be rewritten so the index is usable.
- As the number of indexes increases, `INSERT`, `UPDATE`, and `DELETE` execution time increases. Create only necessary indexes.
- When one table is accessed, Altibase uses only one index for that table access; the optimizer chooses which one.

Index scan can fail or be rejected in these cases:

| Pattern | Example or condition | Tuning action |
| --- | --- | --- |
| Function or operator applied to an indexed column | `SELECT * FROM T1 WHERE C1 + 1 > 0`; `SELECT * FROM T1 WHERE TO_CHAR(SOME_DATE) = '2007-01-01'`; `SELECT * FROM EMPLOYEE WHERE UPPER(DNO) = '1'` | Rewrite so the indexed column can be used directly. The source notes that Altibase does not currently support `FBI (Function Based Index)`. |
| Data type mismatch | `SELECT * FROM T1 WHERE CHAR_COLUMN = 1` | Compare with the same data type. For `CHAR` or `VARCHAR` columns, numeric comparison can cause column conversion. |
| Optimizer cost decision | Optimizer judges index scan cost as higher than the alternative. | Check plan, access count, and selectivity. |
| Composite index order mismatch | Composite index is declared on `C1 + C2`, but the query uses only `C2 = :value`. | Include the leading column condition, for example `C1 = :value1 and C2 = :value2`, when semantically valid. |
| `NOT IN` subquery | `SELECT * FROM EMPLOYEE WHERE DNO NOT IN (SELECT DNO FROM DEPARTMENT WHERE DNO > 4)` | Consider rewriting as an anti-join pattern when equivalent. |

If an index scan occurs but `ACCESS` count is high, check index cardinality and which index is used. For an `A+B+C` composite index, a condition on `A` and `C` can still have high access count because only the leading `A` condition can be used efficiently. Use predicate output in the plan during analysis:

```sql
ALTER SYSTEM SET TRCLOG_PREDICATE=1;
```

The SQL Tuning Guide also describes `TRCLOG_DETAIL_PREDICATE=1` for more detailed execution-plan predicate information. Use these predicate settings only when diagnostic detail is required and follow operational logging policy.

### Execution plans and optimizer validation

Altibase processes SQL through parse/validation, optimize, and execute phases. SQL query tuning focuses on the optimize phase, where the plan is generated. A plan shows how Altibase will execute a query. The SQL Tuning Guide states that plans are generated for `SELECT`, `UPDATE`, and `DELETE` statements with `WHERE` clauses; `INSERT` has no execution plan in this sense.

Use `ALTER SESSION` to control plan output:

| Command | Meaning |
| --- | --- |
| `ALTER SESSION SET EXPLAIN PLAN = ON;` | Show the actual execution plan and query result. Access-count information is accurate because the query is executed. |
| `ALTER SESSION SET EXPLAIN PLAN = ONLY;` | Show only the plan without executing the query. Use this for very large result sets or long-running queries. |
| `ALTER SESSION SET EXPLAIN PLAN = OFF;` | Stop plan output and return only query results. |

Read Altibase plans from the innermost node outward, top to bottom. Check `ACCESS` count carefully, identify whether the access path is `FULL SCAN` or `INDEX SCAN`, and try to drive `FULL SCAN` cases toward index access where the result semantics and selectivity justify it.

Predicate classes in plan output:

| Predicate class | Meaning | Tuning objective |
| --- | --- | --- |
| `KEY` condition | Uses indexing to find target data. | Use `KEY` predicates to filter as much data as possible. |
| `FILTER` condition | Searches/filter rows after broader access. | Leave as little data as possible to `FILTER` predicates. |

Store plan and execution-time setup SQL in `$ALTIBASE_HOME/conf/glogin.sql` when useful. `isql` executes `glogin.sql` before accepting user input, so developers can validate plans early and reduce later tuning burden.

### Join, LIMIT, subquery, and DML tuning

Join tuning is needed when:

- A join condition causes full scan or high index access count.
- An index is used inefficiently or cannot be used.
- The optimizer chooses the wrong join method.
- Too many joined tables make plan generation and validation expensive.
- The query performs join before grouping even though grouping before join is semantically possible and cheaper.

Keep join-condition data types the same. If internal conversion occurs, an index may not be usable. If a mismatch is unavoidable, check the plan before release and confirm whether the condition uses the intended index.

Avoid reading the same table repeatedly when one access can produce the required data. Inline views and subqueries can make SQL easy to write, but repeated access to the same table can degrade performance. When possible, rewrite repeated scalar subqueries as joins.

When joining a memory table and a disk table, disk temporary tablespace can be used, especially for `GROUP BY` or other sort work. The source recommends the hint below to place temporary work in memory when this is appropriate:

```sql
/*+ TEMP_TBS_MEMORY */
```

Use the hint carefully. If a very large result set is sorted in memory, the Altibase `VSZ` can grow.

For outer joins, the base table condition becomes the key access path. If a condition exists only on the outer table side, an index on that outer-side table may not help because the outer-join semantics prevent accessing that table first. If the outer join is unnecessary and an inner join is semantically equivalent, rewriting it as an inner join can avoid full scan and improve performance.

For `ORDER BY ... LIMIT n`, create an index that matches the ordering when the query is frequent and needs only the top rows. The source example uses `ORDER BY SALARY DESC LIMIT 2`; an index on salary descending lets Altibase read only two index entries and table rows, giving near-constant execution cost even as table size grows. Limit stop-key optimization is restricted when `GROUP BY` is used, when `ORDER BY` uses columns that cannot use an index, and when the table output must stream without intermediate changes. The source states that `LIMIT` is most favorable when the `WHERE` clause can be minimized.

For `NOT IN`, an index cannot be used in the source's guidance. When equivalent, rewrite to a left outer join with `IS NULL`, for example:

```sql
SELECT X.*
  FROM EMPLOYEE X LEFT OUTER JOIN DEPARTMENT_DELETED Y
    ON X.DNO = Y.DNO
 WHERE Y.DNO IS NULL
 LIMIT 10;
```

DML tuning checks:

| DML symptom | Check |
| --- | --- |
| `INSERT` is slow | Too many indexes, too-small `BUFFER_POOL_SIZE` for disk tables, table lock in `V$LOCK`, or I/O contention. |
| `UPDATE` or `DELETE` is slow | Apply `SELECT` query tuning checks, `INSERT` slowdown checks, and check whether key columns are being updated unnecessarily. |

### Performance diagnostics from English-only source

The `ALTIBASE HDB Performance Tuning` FAQ tree applies to ALTIBASE HDB `4.3.9 or later`, assumes Altibase administrator privileges, and is English-only auxiliary material.

Before running its diagnostic queries, enable `TIMED_STATISTICS`:

```sql
ALTER SYSTEM SET TIMED_STATISTICS = 1;
```

Application-side diagnostics focus on four frequent causes:

| Cause | Evidence | Interpretation |
| --- | --- | --- |
| Preparing a statement for every execution or using dynamic SQL | `V$SYSSTAT` `SEQNUM IN (27, 29)` for prepare and execute counts. | Normally, execute success count should be much larger than prepare success count. If not, check whether the application prepares repeatedly. |
| Bad SQL consuming many resources | Top running SQL from `V$STATEMENT`; full-scan plan nodes from `V$PLANTEXT`. | Find long-running queries and queries whose plan contains `FULL`. |
| Connecting and disconnecting for every request | `V$SYSSTAT` `SEQNUM = 1` cumulative connection count sampled several times over short intervals. | A rapidly growing connection count can indicate per-request connection creation. |
| Not using local IPC when possible | `V$SESSION.COMM_NAME` grouped by connection type. | Use `CONNTYPE=3`/IPC only when client and database are on the same machine and `IPC_CHANNEL_COUNT` is greater than `0`. Default `IPC_CHANNEL_COUNT` is `0`, so IPC is disabled unless configured. |

Database-side diagnostics:

| Area | Diagnostic or property | Action and caveat |
| --- | --- | --- |
| Log file I/O contention | `select LF_OPEN_COUNT, LF_PREPARE_COUNT, LF_PREPARE_WAIT_COUNT from v$lfg;` and `PREPARE_LOG_FILE_COUNT` default `5`. | If `LF_PREPARE_WAIT_COUNT > 1`, double `PREPARE_LOG_FILE_COUNT`, retest, and repeat up to `100`. If it remains over `1`, disk performance is slow and disk replacement or storage change should be considered. Larger values allocate more log-file memory. |
| Checkpoint I/O | Log files and data files on the same file system, or OS buffered I/O flush behavior. | Separate physical log and data locations. Consider Direct I/O if buffered I/O causes fluctuation. Tuning writes can lengthen checkpoint duration and require more log disk. |
| `MULTIPLEXING_THREAD_COUNT` | Compare `V$SERVICE_THREAD`, IPC sessions, and `V$PROPERTY` `MULTIPLEXING%_THREAD_COUNT`. | Start by testing values 2x to 4x CPU cores. `DEDICATED` greater than IPC count or `SOCKET` greater than `MULTIPLEXING_THREAD_COUNT` can indicate long-running queries. |
| Memory Ager / GC | `V$MEMGC` `ADD_OID_CNT - GC_OID_CNT` and long-query query using `V$TRANSACTION`, `V$STATEMENT`, and `V$SESSION`. | Increasing `GCGAP` can mean long-running queries prevent GC. Lower `AGER_WAIT_MINIMUM` and `AGER_WAIT_MAXIMUM` only after checking symptoms; faster wake-up consumes more CPU and can slow transaction response. |
| Buffer cache | `BUFFER_AREA_SIZE`, hot/cold LRU, `HOT_LIST_PCT` default `50`. | Analyze access pattern before changing `HOT_LIST_PCT`; example tuning uses `alter system set HOT_LIST_PCT = 60;`. |
| SQL plan cache | `V$SQL_PLAN_CACHE`, `V$SQL_PLAN_CACHE_PCO`, `V$SQL_PLAN_CACHE_SQLTEXT`; properties `SQL_PLAN_CACHE_SIZE`, `SQL_PLAN_CACHE_BUCKET_CNT`, `SQL_PLAN_CACHE_HOT_REGION_LRU_RATIO`, `SQL_PLAN_CACHE_PREPARED_EXECUTION_CONTEXT_CNT`. | The source recommends `CACHE_MISS_COUNT / CACHE_HIT_COUNT` normally below `1/10000`, `SQL_PLAN_CACHE_BUCKET_CNT` about total statements divided by `4`, and `SQL_PLAN_CACHE_PREPARED_EXECUTION_CONTEXT_CNT` similar to CPU count to avoid contention. |

When all earlier checks are applied and performance issues remain, collect:

```sh
pstack $ALTIBASE_PID
```

Gather `pstack` three consecutive times with a sleep interval such as `10` seconds. Also inspect mutex and wait views:

```sql
select * from v$mutex order by miss_count desc limit 10;
select event, wait_time from v$statement where wait_time > 1;
select event, TOTAL_WAITS, time_waited from v$system_event order by 2,3;
```

System-side diagnostics:

- Confirm OS kernel and environment variables match the Installation manual and `pre_install.sh` guidance before deeper analysis.
- Measure disk write performance with `time dd if=/dev/zero of=MyTestFile bs=1M count=1024`; this creates a 1 GB zero-filled file and displays copy time.
- Check Direct I/O feasibility using `LOG_IO_TYPE`, `DATABASE_IO_TYPE`, and `DIRECT_IO_ENABLED`. If Direct I/O cannot be used on a system, Altibase uses Buffered I/O regardless of property settings.
- Collect OS evidence with `vmstat` and `iostat`; the source examples are AIX shell loops and group disks into MEMORY, DISK, and LOGS storage devices.

Direct I/O mount options from the source:

| OS | File system | Mount option |
| --- | --- | --- |
| Solaris | UFS | none |
| HP-UX | Veritas VxFS | `convosync=direct` |
| Solaris | Veritas VxFS | `convosync=direct` |
| AIX | Veritas VxFS | `convosync=direct` |
| AIX | JFS | use `-o dio` |
| Windows NT/2000 | All | none |
| Tru64 Unix | AdvFS | none |
| Linux 2.4 or later | All | none |

### Large-scale DRDB index builds

Index building reads, sorts, and stores data. Running index builds in parallel can degrade performance because of excessive disk I/O and buffer misses. Tune the properties below to reduce I/O and buffer misses, optimize sorting, and shorten build time for large disk-based indexes.

For versions `6.5.1~7.1.0`:

| Property | Unit | Recommended source value |
| --- | --- | --- |
| `BUFFER_AREA_SIZE` | bytes | Larger values are generally better. |
| `SORT_AREA_SIZE` | bytes | Number of physical cores in the system multiplied by `20 MB`. |
| `DISK_INDEX_BUILD_MERGE_PAGE_COUNT` | pages | `1%` of `BUFFER_AREA_SIZE`, but review the merge-page considerations. |
| `INDEX_BUILD_THREAD_COUNT` | cores | Number of physical cores in the hardware. |

For version `7.3.0 or later`:

| Property | Unit | Recommended source value |
| --- | --- | --- |
| `BUFFER_AREA_SIZE` | bytes | Larger values are generally better. |
| `DISK_INDEX_BUILD_SORT_AREA_SIZE` | bytes | Number of physical cores in the system multiplied by `20 MB`. |
| `DISK_INDEX_BUILD_MERGE_PAGE_COUNT` | pages | `1%` of `BUFFER_AREA_SIZE`. |
| `INDEX_BUILD_THREAD_COUNT` | cores | Number of physical cores in the hardware. |

Considerations:

- Larger `BUFFER_AREA_SIZE` increases startup time.
- In `6.5.1~7.1.0`, one index build uses at least `SORT_AREA_SIZE` memory. Two parallel index builds use `SORT_AREA_SIZE * 2`. `SORT_AREA_SIZE` is also shared with disk temp tables, so changing it affects disk temp table operations.
- In `7.3.0 or later`, one index build uses at least `DISK_INDEX_BUILD_SORT_AREA_SIZE`; two parallel index builds use `DISK_INDEX_BUILD_SORT_AREA_SIZE * 2`. `SORT_AREA_SIZE` is not used for this purpose.
- `DISK_INDEX_BUILD_MERGE_PAGE_COUNT` is in pages, while `BUFFER_AREA_SIZE` is in bytes.
- In `6.5.1~7.1.0`, if the merge page count is large but the index is small, performance can degrade.
- In `6.5.1~7.1.0`, performance can degrade when `DISK_INDEX_BUILD_MERGE_PAGE_COUNT > (index key length * number of records) / SORT_AREA_SIZE`.
- The source states that those merge-page degradation issues do not occur in version `7.3.0 or later`.

### `CHAR` and `VARCHAR` comparison behavior

The SQL FAQ applies to all Altibase versions. When comparing `CHAR` values, `0x20` is added to the shorter value and comparison uses the longer length. When comparing `CHAR` and `VARCHAR`, comparison uses the valid data in the `VARCHAR` value up to the `0x00` position.

In SESC code, variables are sometimes initialized to `0x00` for `VARCHAR` and `0x20` for `CHAR`. Because of the source comparison rules, it is better to initialize them to `0x00`.

### Stored procedure inspection

There are two source-supported ways to check stored procedure contents:

- Use `SYSTEM_.SYS_PROCEDURES_` and `SYSTEM_.SYS_PROC_PARSE_` meta tables through helper stored procedures.
- Use the `aexport` utility and inspect generated SQL files.

`aexport` writes all stored procedure creation statements to `ALL_CRT_PROC.sql`. Starting from ALTIBASE HDB 5.5.1, the `-object user_name.procedure_name` option can extract a specific object and creates a file named in the form `user_name_procedure_name_CRT.sql`.

Use `SQL%ROWCOUNT` in a stored procedure to read how many rows were affected by DML.

## Procedures

### Tune SQL and index access paths

1. Enable execution-plan output with `ALTER SESSION SET EXPLAIN PLAN = ON` for actual execution or `ONLY` when the query is too expensive to run.
2. Read the plan from the innermost node outward, top to bottom.
3. Check whether each important table access is `FULL SCAN` or `INDEX SCAN`, and check `ACCESS` count.
4. If a full scan is unexpected, verify that the predicate can use an index: no function/operator wraps the indexed column, data types match, leading columns of composite indexes are present, and the SQL does not use an index-hostile pattern such as `NOT IN`.
5. For high `ACCESS` count despite index use, check cardinality and whether a composite index is only using its leading column.
6. Use predicate trace output such as `TRCLOG_PREDICATE=1` only when deeper plan predicate detail is needed.
7. For frequent top-N queries, align the index order with `ORDER BY ... LIMIT n` so Altibase can stop after the required index entries.
8. For repeated scalar subqueries or repeated access to the same table, rewrite to a join when the result is equivalent.
9. For unnecessary outer joins, rewrite to an inner join only when it is semantically equivalent and enables the intended key access path.

### Diagnose application-side performance

1. Enable `TIMED_STATISTICS`.
2. Compare prepare and execute counts from `V$SYSSTAT` `SEQNUM IN (27, 29)`. If prepares are too close to executes, inspect application code for repeated prepare or dynamic SQL.
3. Query `V$STATEMENT` for the longest currently running statements.
4. Join `V$STATEMENT` to `V$PLANTEXT` to identify statements whose plan text contains `FULL`.
5. Sample cumulative connection count from `V$SYSSTAT` `SEQNUM = 1` several times in a short period. Rapid growth can indicate connect/disconnect per request.
6. Group `V$SESSION.COMM_NAME` by connection type. If client and DB are on the same machine, consider IPC only after setting `IPC_CHANNEL_COUNT > 0`.

### Diagnose and tune database-side performance

1. Check log file I/O contention with `v$lfg`. If `LF_PREPARE_WAIT_COUNT > 1`, increase `PREPARE_LOG_FILE_COUNT` by doubling and retesting, up to `100`; if waits remain, treat storage performance as the bottleneck.
2. Check whether log files and data files share the same physical file system. Separate them when checkpoint or log I/O contention is suspected.
3. If OS buffered I/O causes performance fluctuation, consider Direct I/O settings and OS mount support.
4. Check service-thread counts against IPC sessions and `MULTIPLEXING_THREAD_COUNT`. `DEDICATED` count greater than IPC sessions or `SOCKET` count greater than `MULTIPLEXING_THREAD_COUNT` can indicate long-running queries.
5. Monitor `V$MEMGC`. If `GCGAP` increases, use the provided `V$TRANSACTION`, `V$STATEMENT`, and `V$SESSION` query to identify the long-running transaction or query.
6. Tune `AGER_WAIT_MINIMUM` and `AGER_WAIT_MAXIMUM` only after symptom checks; lowering them can consume more CPU.
7. Check plan-cache hit/miss counts, statement count, and plan-cache properties before changing `SQL_PLAN_CACHE_SIZE`, `SQL_PLAN_CACHE_BUCKET_CNT`, `SQL_PLAN_CACHE_HOT_REGION_LRU_RATIO`, or `SQL_PLAN_CACHE_PREPARED_EXECUTION_CONTEXT_CNT`.

### Build a large DRDB index

1. Avoid building many large disk indexes in parallel unless the storage and memory budget can absorb the I/O and sort load.
2. For `6.5.1~7.1.0`, set `SORT_AREA_SIZE` to physical cores multiplied by `20 MB`, use `INDEX_BUILD_THREAD_COUNT` equal to physical cores, and review `DISK_INDEX_BUILD_MERGE_PAGE_COUNT` against index size.
3. For `7.3.0 or later`, use `DISK_INDEX_BUILD_SORT_AREA_SIZE` instead of `SORT_AREA_SIZE`, set it to physical cores multiplied by `20 MB`, and use `INDEX_BUILD_THREAD_COUNT` equal to physical cores.
4. Treat `BUFFER_AREA_SIZE` increases as a startup-time tradeoff.
5. Remember that memory use doubles when two index builds run in parallel because each build needs its own sort area.

### Capture system-side performance evidence

1. Confirm OS kernel and environment variables match the Altibase installation guidance and `pre_install.sh`.
2. Measure disk write speed with `time dd if=/dev/zero of=MyTestFile bs=1M count=1024` and remove the test file afterward according to local operational policy.
3. Verify Direct I/O property settings and filesystem mount support.
4. Collect `vmstat` and `iostat` evidence during the symptom window. Use the source AIX examples as patterns for repeated sampling and grouping memory, disk, and log devices.
5. If database-side checks do not isolate the problem, collect `pstack $ALTIBASE_PID` three times with a sleep interval such as `10` seconds and correlate it with `V$MUTEX`, `V$STATEMENT`, and `V$SYSTEM_EVENT`.

### Configure session behavior for application SQL

1. Choose the correct connection type. Use `CONNTYPE=1` when the application is remote, and consider `CONNTYPE=2` or `CONNTYPE=3` only when DBMS and application are on the same server.
2. Decide whether transaction control must be auto-commit or manual. For session-level manual commit, run `ALTER SESSION SET AUTOCOMMIT = FALSE`.
3. Set timeout behavior at the right scope. Put `CONNECTION_TIMEOUT` and `TIMEOUT` in the connection string when needed; use `ALTER SESSION SET QUERY_TIMEOUT = n` or `ALTER SESSION SET FETCH_TIMEOUT = n` for session-level query and fetch behavior.
4. If LOB columns are queried, use non-auto-commit mode unless using the ALTIBASE HDB 6.3.1 or later JDBC driver with `ClientSide_Auto_Commit = On`.
5. In threaded code and connection pools, do not share one connection concurrently without serialization around the SQL protocol sequence.

### Use cursors safely

1. Check errors on `PREPARE` and `DECLARE CURSOR`.
2. Check errors on `OPEN` and every `FETCH`.
3. Close each cursor after all data is read or after an error.
4. Do not issue `COMMIT` or `ROLLBACK` on the same session during fetch unless closing the cursor is intended.
5. If another transaction must occur during fetch, use a separate DB session.
6. Run DDL only after cursor fetch is complete and the open cursor is closed, or run DDL in a separate session.

### Check object privileges granted between DB users

Run the object privilege query from the SQL FAQ. It applies to ALTIBASE HDB 4.3.9 or later and lists grantee, grantor, object owner, object name, object type, privilege, and grant option.

```sql
SELECT a.user_name grantee,
       c.user_name grantor,
       f.user_name object_owner,
       e.table_name object_name,
       e.table_type object_type,
       replace(d.priv_name, '_', ' ') priv_name,
       decode(b.with_grant_option, 0, 'NO', 'YES') grantable
  FROM system_.sys_users_ a,
       system_.sys_grant_object_ b,
       system_.sys_users_ c,
       system_.sys_privileges_ d,
       system_.sys_tables_ e,
       system_.sys_users_ f
 WHERE c.user_name <> 'SYSTEM_'
   and b.grantee_id = a.user_id
   and b.grantor_id = c.user_id
   and b.priv_id = d.priv_id
   and b.obj_id = e.table_id
   and e.user_id = f.user_id
 ORDER BY grantee,
       grantor,
       object_owner,
       object_type,
       object_name,
       priv_name;
```

Example setup:

```sql
create user user1 identified by user1;
create user user2 identified by user2;
connect user1/user1;
create table user1_t1 ( c1 integer );
grant select on user1_t1 to user2;
grant insert on user1_t1 to user2;
```

Expected result shape:

```text
GRANTEE GRANTOR OBJECT_OWNER OBJECT_NAME OBJECT_TYPE PRIV_NAME GRANTABLE
USER2   USER1   USER1        USER1_T1    T           INSERT    NO
USER2   USER1   USER1        USER1_T1    T           SELECT    NO
```

### Inspect stored procedure contents with meta tables

Create the helper procedure that lists stored procedures and user-defined functions:

```sql
CREATE OR REPLACE PROCEDURE showProcedures
AS
 CURSOR C1 IS
    SELECT U.USER_NAME, PROC.PROC_NAME,
           DECODE(PROC.OBJECT_TYPE, 0, 'PROCEDURE', 1, 'FUNCTION')
      FROM SYSTEM_.SYS_PROCEDURES_ PROC, SYSTEM_.SYS_USERS_ U
     WHERE PROC.USER_ID = U.USER_ID;
    V1 CHAR(40);
    V2 CHAR(40);
    V3 CHAR(20);
BEGIN
    SYSTEM_.PRINTLN('----------------------------------------------------------------------------------------------------');
    SYSTEM_.PRINT(' USER_NAME                               PROC_NAME');
    SYSTEM_.PRINTLN('                               PROCEDURE/FUNCTION');
    SYSTEM_.PRINTLN('----------------------------------------------------------------------------------------------------');
    OPEN C1;
    LOOP
        FETCH C1 INTO V1, V2, V3;
        EXIT WHEN C1%NOTFOUND;
        SYSTEM_.PRINT(' ');
        SYSTEM_.PRINT(V1);
        SYSTEM_.PRINT(V2);
        SYSTEM_.PRINTLN(V3);
    END LOOP;
    SYSTEM_.PRINTLN('----------------------------------------------------------------------------------------------------');
    CLOSE C1;
END;
/
```

Run it with:

```sql
exec showProcedures;
```

Create the helper procedure that prints the stored procedure body:

```sql
CREATE OR REPLACE PROCEDURE showProcBody(p1 IN VARCHAR(40), p2 IN VARCHAR(40))
AS
CURSOR C1 IS
    SELECT SYSTEM_.SYS_PROC_PARSE_.PARSE
      FROM SYSTEM_.SYS_PROC_PARSE_
     WHERE SYSTEM_.SYS_PROC_PARSE_.PROC_OID = (SELECT P.PROC_OID
              FROM SYSTEM_.SYS_PROCEDURES_ P,
                   SYSTEM_.SYS_USERS_ U
             WHERE U.USER_ID = P.USER_ID
               AND P.PROC_NAME = p2
               AND U.USER_NAME = p1)
     ORDER BY SYSTEM_.SYS_PROC_PARSE_.SEQ_NO;
V1 VARCHAR(4000);
BEGIN
    OPEN C1;
    SYSTEM_.PRINTLN('---------------------------------');
    SYSTEM_.PRINT(P1);
    SYSTEM_.PRINTLN(' PROCEDURE');
    SYSTEM_.PRINTLN('---------------------------------');
    SYSTEM_.PRINTLN('');
    LOOP
      FETCH C1 INTO V1;
      EXIT WHEN C1%NOTFOUND;
      SYSTEM_.PRINTLN(V1);
    END LOOP;
    CLOSE C1;
SYSTEM_.PRINTLN('');
SYSTEM_.PRINTLN('---------------------------------');
END;
/
```

Run it with:

```sql
exec showProcBody('USER_NAME', 'PROC_NAME');
```

### Inspect stored procedure contents with `aexport`

To export all objects and inspect stored procedures, run:

```sh
aexport
```

Then inspect `ALL_CRT_PROC.sql` among the generated files.

To export object schemas for one user:

```sh
aexport -u user_name -p user_password -s Altibase_Server_IP
```

Interactive alternative:

```text
$ aexport
Write Server Name (default:127.0.0.1) :     # Enter the Altibase server IP
Write UserID :                              # Enter the object owner or sys user.
Write Password :                            # Password of the user entered above
```

To export one stored procedure object on ALTIBASE HDB 5.5.1 or later:

```sh
aexport -s Altibase_Server_IP -u user_name -p user_password -object user_name.procedure_name
```

Interactive alternative:

```text
$ aexport -object user_name.procedure_name
Write Server Name (default:127.0.0.1) :       # Enter the Altibase server IP
Write UserID :                                # Enter the object owner or sys user.
Write Password :                              # Password of the user entered above
```

### Count affected DML rows inside a stored procedure

Use `SQL%ROWCOUNT` after the DML statement:

```sql
CREATE OR REPLACE PROCEDURE proc1
AS
  v1 INTEGER;
BEGIN
  DELETE FROM MEM_T LIMIT 10 ;
  v1 := SQL%ROWCOUNT;
  PRINTLN(v1);
END;
/
```

Example execution:

```text
iSQL> exec proc1;
10
Execute success.
```

### Compare `CHAR` and `VARCHAR` values with trailing spaces

The SQL FAQ example preserves these comparison outcomes:

```sql
create table dual (X char(1));
insert into dual values ('x');
select 1 from dual where char'a ' = char'a ';
select 1 from dual where varchar'a ' = varchar'a ';
select 1 from dual where varchar'a' = char'a ';
select 1 from dual where varchar'a' = char'a';
select 1 from dual where varchar'a ' = char'a ';
```

The source outcomes are:

| Predicate | Result |
| --- | --- |
| `char'a ' = char'a '` | `1 row selected` |
| `varchar'a ' = varchar'a '` | `No rows selected` |
| `varchar'a' = char'a '` | `No rows selected` |
| `varchar'a' = char'a'` | `1 row selected` |
| `varchar'a ' = char'a '` | `1 row selected` |

## SQL, commands, and configuration

### Performance plan, predicate, and diagnostic controls

```sql
ALTER SESSION SET EXPLAIN PLAN = ON;
ALTER SESSION SET EXPLAIN PLAN = ONLY;
ALTER SESSION SET EXPLAIN PLAN = OFF;
ALTER SYSTEM SET TRCLOG_PREDICATE = 1;
ALTER SYSTEM SET TRCLOG_DETAIL_PREDICATE = 1;
ALTER SYSTEM SET TIMED_STATISTICS = 1;
```

### Application-side performance diagnostic SQL

Prepare and execute counts:

```sql
SELECT   TO_CHAR(SYSDATE, 'YYYYMMDD HH:MI:SS') CUR_TIME,
         RPAD(NAME, 50) NAME,
         VALUE
  FROM   V$SYSSTAT
 WHERE   SEQNUM IN (27, 29);
```

Top currently running statements:

```sql
SELECT EXECUTE_TIME / 1000000 EXEC_SECOND,
       RPAD(QUERY, 500) QUERY
  FROM V$STATEMENT
 WHERE EXECUTE_FLAG = 1
 ORDER BY 1 DESC
 LIMIT 5;
```

Queries with a `FULL` plan node:

```sql
SELECT RPAD(QUERY, 200),
       COUNT(*) CNT
  FROM V$STATEMENT
 WHERE (SESSION_ID, ID) IN
       (SELECT SID,
               STMT_ID
          FROM V$PLANTEXT
         WHERE TEXT LIKE '%FULL%')
 GROUP BY QUERY;
```

Cumulative connection count:

```sql
SELECT TO_CHAR(SYSDATE, 'YYYYMMDD HH:MI:SS') CUR_TIME,
       RPAD(NAME, 50) NAME,
       VALUE
  FROM V$SYSSTAT
 WHERE SEQNUM = 1;
```

Connection type distribution:

```sql
SELECT SUBSTR(COMM_NAME, 1, 4) CON_TYPE,
       COUNT(*) CNT
  FROM V$SESSION
 GROUP BY SUBSTR(COMM_NAME, 1, 4);
```

### Database-side performance diagnostic SQL

Log file I/O contention:

```sql
select LF_OPEN_COUNT, LF_PREPARE_COUNT, LF_PREPARE_WAIT_COUNT from v$lfg;
```

Service thread and IPC session check:

```sql
select rpad(type, 30), count(*) from v$service_thread group by type
union all
select '# of IPC ', count(*) from v$session where comm_name like '%IPC%';
```

Multiplexing property check:

```sql
select rpad(type, 30), count(*) from v$service_thread group by type
union all
select rpad(name, 30), value1 from v$property where name like 'MULTIPLEXING%_THREAD_COUNT';
```

Memory GC gap:

```sql
select add_oid_cnt, gc_oid_cnt, add_oid_cnt - gc_oid_cnt GCGAP from v$memgc;
```

Long-running transaction or query blocking memory GC:

```sql
select c.session_id, comm_name, client_pid, execute_flag, total_time, execute_time, fetch_time, rpad(query, 500)
  from (select * from v$memgc limit 1) a, v$transaction b, v$statement c, v$session d
 where (a.MINMEMSCNINTXS = b.MEMORY_VIEW_SCN or a.MINMEMSCNINTXS = b.MIN_MEMORY_LOB_VIEW_SCN)
   and b.id = c.tx_id
   and c.session_id = d.id;
```

Memory GC holder query from the SQL Tuning Guide:

```sql
SELECT ID, SESSION_ID, QUERY
  FROM V$STATEMENT
 WHERE TX_ID = (SELECT ID
                  FROM v$TRANSACTION
                 WHERE MEMORY_VIEW_SCN = (SELECT MINMEMSCNINTX
                                             FROM V$MEMGC
                                            LIMIT 1));
```

Disk GC gap:

```sql
SELECT ADD_TSS_CNT - GC_TSS_CNT FROM v$DISKGC;
```

Lock holder query:

```sql
SELECT ID STMT_ID, SESSION_ID, QUERY
  FROM V$STATEMENT
 WHERE TX_ID = #Trans ID#;
```

SQL plan cache hit and miss counts:

```sql
select CACHE_HIT_COUNT, CACHE_MISS_COUNT from v$sql_plan_cache;
```

Total statement count for `SQL_PLAN_CACHE_BUCKET_CNT` sizing:

```sql
select count(*) as total_number_of_statement from v$statement;
```

Mutex and wait evidence:

```sql
select * from v$mutex order by miss_count desc limit 10;
select event, wait_time from v$statement where wait_time > 1;
select event, TOTAL_WAITS, time_waited from v$system_event order by 2,3;
```

### Performance properties and sizing formulas

```text
IPC_CHANNEL_COUNT > 0
PREPARE_LOG_FILE_COUNT default 5, double and retest up to 100 when LF_PREPARE_WAIT_COUNT > 1
CHECKPOINT_BULK_WRITE_PAGE_COUNT 0 => 100
CHECKPOINT_BULK_WRITE_SLEEP_SEC 0 => 0
CHECKPOINT_BULK_WRITE_SLEEP_USEC 0 => 5000
CHECKPOINT_BULK_SYNC_PAGE_COUNT 3200 => 100
MULTIPLEXING_THREAD_COUNT test at 2x to 4x CPU cores
AGER_WAIT_MINIMUM = 200000 microseconds
AGER_WAIT_MAXIMUM = 1000000 microseconds
HOT_LIST_PCT default 50
SQL_PLAN_CACHE_SIZE default example 67108864
SQL_PLAN_CACHE_BUCKET_CNT default example 127; source sizing rule: total_number_of_statement / 4
SQL_PLAN_CACHE_HOT_REGION_LRU_RATIO default example 50
SQL_PLAN_CACHE_PREPARED_EXECUTION_CONTEXT_CNT default example 1; source recommendation: similar to CPU count
```

```sql
alter system set HOT_LIST_PCT = 60;
```

DRDB index build properties:

```text
6.5.1~7.1.0:
BUFFER_AREA_SIZE = larger values are generally better
SORT_AREA_SIZE = physical core count * 20 MB
DISK_INDEX_BUILD_MERGE_PAGE_COUNT = 1% of BUFFER_AREA_SIZE, subject to merge-page caveat
INDEX_BUILD_THREAD_COUNT = physical core count

7.3.0 or later:
BUFFER_AREA_SIZE = larger values are generally better
DISK_INDEX_BUILD_SORT_AREA_SIZE = physical core count * 20 MB
DISK_INDEX_BUILD_MERGE_PAGE_COUNT = 1% of BUFFER_AREA_SIZE
INDEX_BUILD_THREAD_COUNT = physical core count
```

### System-side commands

```sh
time dd if=/dev/zero of=MyTestFile bs=1M count=1024
pstack $ALTIBASE_PID
```

Collect `pstack` three times with a sleep interval such as `10` seconds when deeper evidence is needed.

### Session and timeout SQL

```sql
ALTER SESSION SET AUTOCOMMIT = FALSE;
ALTER SESSION SET QUERY_TIMEOUT = 30;
ALTER SESSION SET FETCH_TIMEOUT = 30;
ALTER SESSION SET EXPLAIN PLAN = ON;
```

### LOB client-side commit control example

```ini
[ DataSource ]
Server=192.168.1.1
Port=20300
User=SYS
Password=MANAGER
AlternateServers=(192.168.1.2:20300,192.168.1.3:20300)
ConnectionRetryCount=3
ConnectionRetryDelay=5
LoadBalance = On
SessionFailOver = Off
ClientSide_Auto_Commit = On
```

### SQL error checking pattern

```text
EXEC SQL PREPARE ....
EXEC SQL EXECUTE ....
If (SQLCODE != SQL_SUCCESS)
   Error_log ();

Or,
EXEC SQL DECLARE CURSOR...
EXEC SQL OPEN ....
If (SQLCODE != SQL_SUCCESS)
   Error_log ();
```

The source warns that this example omits error checking after `PREPARE` or `DECLARE CURSOR`; production code must check those steps too.

### Execution plan example

After enabling `EXPLAIN PLAN`, a full table scan can appear as:

```text
PROJECT ( COLUMN_COUNT: 2, TUPLE_SIZE: 16 )
 GROUP-AGGREGATION ( ITEM_SIZE: 32, GROUP_COUNT: 1, BUCKET_COUNT: 1024, ACCESS: 1, SELF_ID: 3, REF_ID: 2 )
  SCAN ( TABLE: T1, FULL SCAN, ACCESS: 262145, SELF_ID: 2 )
```

If an index is used, output can appear as:

```text
PROJECT ( COLUMN_COUNT: 1, TUPLE_SIZE: 4 )
 SCAN ( TABLE: T1, INDEX: IDX_T1, ACCESS: 2, SELF_ID: 2 )
```

## Validation and troubleshooting

Check `$ALTIBASE_HOME/trc/altibase_boot.log` when timeout-related errors occur. The source example for `UTRANS_TIMEOUT` includes `Session ID`, `CLIENT_INFO`, `Time Limit`, `Running Time`, `Last Query`, and `Caused by Transaction`. Those fields should be preserved in troubleshooting answers because they identify the affected client and the transaction-control issue.

For threaded programs or connection pools, messages such as `Communication link failure (EXEC->INVL)`, `Communication link failure (PREP->EXEC)`, and `Invalid request to process the SQL statement` require checking whether one connection is being used concurrently without correct protocol sequencing.

For cursor problems, the main corrective actions are to check errors at `PREPARE` or `DECLARE CURSOR`, fetch until completion or error, close the cursor, and avoid `COMMIT` or `ROLLBACK` on the same session while fetching unless cursor closure is intended.

For LOB query errors, switch to non-auto-commit mode before selecting LOB columns unless the environment is ALTIBASE HDB 6.3.1 or later JDBC with client-side commit control configured.

For SQL performance validation, start with plan evidence and access counts. Use `EXPLAIN PLAN = ON` when actual access counts are needed and `EXPLAIN PLAN = ONLY` when executing the statement would be too expensive. If a plan shows unexpected `FULL SCAN`, verify predicate form, data type matching, composite-index leading columns, unsupported function-based-index expectations, and `NOT IN` subquery patterns.

If `INDEX SCAN` appears but the query remains slow, inspect cardinality and `ACCESS` count. For composite indexes, verify that the predicate can use the leading column sequence. Enable predicate trace detail only for diagnostic sessions where the additional log volume is acceptable.

For application-side symptoms, compare prepare and execute counts, long-running statements, full-scan plans, connection counts, and connection types before changing database properties. The English-only diagnostic source explicitly treats application logic as the most common cause of performance problems.

For database-side symptoms, do not tune properties blindly. Each property has a source caveat: `PREPARE_LOG_FILE_COUNT` consumes memory, checkpoint write tuning can lengthen checkpoint duration and require more log disk, faster Ager wake-up consumes CPU, `HOT_LIST_PCT` depends on access patterns, and plan-cache execution contexts can enlarge plan memory without improving performance.

For system-side symptoms, collect OS evidence during the same time window as DB evidence. Correlate `dd`, `vmstat`, `iostat`, `pstack`, `V$MUTEX`, `V$STATEMENT`, and `V$SYSTEM_EVENT` rather than interpreting one sample in isolation.

For large DRDB index builds, check the Altibase version before choosing sort-area properties. `SORT_AREA_SIZE` applies to version `6.5.1~7.1.0`, while `DISK_INDEX_BUILD_SORT_AREA_SIZE` applies to version `7.3.0 or later`.

For stored procedure body inspection, use the helper procedures when SQL access to meta tables is enough. Use `aexport` when file-based object DDL extraction is needed. For a single object, use the `-object` option only on ALTIBASE HDB 5.5.1 or later.

For the `SQL%ROWCOUNT` procedure example, the source notes that copying a procedure creation statement in Internet Explorer may insert blank spaces. Use the preserved `SP_DML_RECORD_COUNT.txt` support artifact if necessary.

## Version-specific notes

| Source item | Version condition |
| --- | --- |
| `CHAR` and `VARCHAR` comparison FAQ | Applicable to all versions of Altibase. |
| Object privilege query FAQ | Available in ALTIBASE HDB 4.3.9 or later. |
| Stored procedure content inspection FAQ | Applies to all versions of ALTIBASE HDB. |
| `aexport -object user_name.procedure_name` | Available starting from ALTIBASE HDB 5.5.1. |
| LOB query in auto-commit mode using JDBC client-side commit control | Available with ALTIBASE HDB 6.3.1 or later JDBC driver. |
| Altibase SQL Tuning Guide PDF | Markdown page says the guide was written based on Altibase v5; the PDF content is preserved as source guidance with that legacy context. |
| Partition table limitation in Development Guide | As of version `7.3.0`, partitioned local indexes and non-partitioned global indexes are supported; partitioned global indexes are not supported. |
| English-only performance diagnostics FAQ | Applies to ALTIBASE HDB `4.3.9 or later`; classify as English-only auxiliary. |
| DRDB index build settings | Use `SORT_AREA_SIZE` for `6.5.1~7.1.0`; use `DISK_INDEX_BUILD_SORT_AREA_SIZE` for `7.3.0 or later`. |

## Related errors

| Error or message | R015 source meaning |
| --- | --- |
| `Communication link failure (EXEC->INVL)` | SQL protocol order can be broken by concurrent use of one connection or by an interrupt during a required protocol sequence. |
| `Communication link failure (PREP->EXEC)` | Same threaded or connection-pool sequencing risk as above. |
| `Invalid request to process the SQL statement` | Often indicates incorrect connection-object concurrency control in threaded programs. |
| `Connection time out` | Application message for `CONNECTION_TIMEOUT`. |
| `Client unable to establish connection` | Application message for `TIMEOUT`. |
| `Client's query exceeded in the execution time limitation` | Application message for `QUERY_TIMEOUT`. |
| `The session has been closed by the server` | Application message for `FETCH_TIMEOUT`, `IDLE_TIMEOUT`, or `UTRANS_TIMEOUT`. |
| `ERR-91101` | LOB data cannot be operated on while the connection is in auto-commit mode. |
| `Not defined (XX)` | Can be a misleading later error when `PREPARE` or `DECLARE CURSOR` errors were not checked. |
| `TRX_UPDATE_MAX_LOGSIZE` error text | Bulk changes can exceed the configured redo-log limit; R013 keeps the exact error entry, while R016 covers the performance cause and large-change caveat. |
| `Too many pages are allocated` | Memory tablespace exhaustion can follow growth or mass changes; check memory tablespace usage and `MEM_MAX_DB_SIZE` in the operations topic before increasing capacity. |
| `The Tablespace does not have enough free space` | Disk tablespace free-space shortage can appear as a performance or DML failure symptom; add data files according to operations guidance. |
| `ERR-311E0` | Disk-table sort/group index-key size issue is covered in the troubleshooting topic; R016 cross-references it when memory temporary tablespace or disk temp behavior affects performance. |
| `ERR-31283` | Partitioned-table local non-prefixed primary/unique index restriction is covered in the troubleshooting topic; R016 preserves the partition/index design caveat. |

## Attachments and external references

Preserved R016 SQL Tuning Guide document attachments:

- English source attachment: `D68_Altibase_SQL_Tuning_Guide.pdf` - `https://docs.altibase.com/download/attachments/22643010/D68_Altibase_SQL_Tuning_Guide.pdf?version=1&modificationDate=1761005430000&api=v2`
- Korean source attachment preserved in English target: `D68_Altibase_SQL_Tuning_Guide.pdf` - `https://docs.altibase.com/download/attachments/19333563/D68_Altibase_SQL_Tuning_Guide.pdf?version=1&modificationDate=1697696104000&api=v2`

English-only performance diagnostic source links:

- `https://docs.altibase.com/display/FAQE/Performance+diagnostics+for+ALTIBASE+HDB`
- `https://docs.altibase.com/display/FAQE/1.+Application+side+diagnostics`
- `https://docs.altibase.com/display/FAQE/2.+Database+side+diagnostics`
- `https://docs.altibase.com/display/FAQE/3.+System+side+diagnostics`
- `http://atc.altibase.com/sub09/551b/html/Admin/ch03s128.html` - `V$STATNAME` explanation linked by the English-only application diagnostics source.

Preserved R015 support artifact:

- `SP_DML_RECORD_COUNT.txt`: `https://docs.altibase.com/download/attachments/8454526/SP_DML_RECORD_COUNT.txt?version=1&modificationDate=1421821636000&api=v2`

The artifact is `.txt`, so it is registered as `not_document_format` rather than `preserved_url` under the document-format attachment gate. The URL itself is still preserved exactly for users who need the procedure source text.

Development Guide references from the R015 parent source:

- Altibase Disk I/O Bottleneck Volume Configuration Guide: `https://docs.altibase.com/pages/viewpage.action?pageId=11698408`
- Considerations for Altibase Backup Policy: `https://docs.altibase.com/pages/viewpage.action?pageId=14057586`
- Altibase Replication Configuration Guide: `https://docs.altibase.com/pages/viewpage.action?pageId=13828098`
- Altibase Replication Constraints Guide: `https://docs.altibase.com/pages/viewpage.action?pageId=19333729`
- System Data Capacity Estimation Guide for Altibase Operations: `https://docs.altibase.com/pages/viewpage.action?pageId=14057887`
- Altibase Precompiler Guide: `https://docs.altibase.com/pages/viewpage.action?pageId=11698385`
- Altibase SQL Tuning Guide: `https://docs.altibase.com/pages/viewpage.action?pageId=19333563`
- JAVA Developer's Guide: `https://docs.altibase.com/pages/viewpage.action?pageId=14057500`
- Altibase VC 2010 Development Guide: `https://docs.altibase.com/pages/viewpage.action?pageId=19334121`
- ORACLE to ALTIBASE Conversion Guide: `https://docs.altibase.com/pages/viewpage.action?pageId=7341605`

Development Guide legacy document labels from the wider guide source are source limitations only:

- `ALTIBASE_개발가이드.pdf` - no downloadable URL in source.
- `ALTIBASE_개발가이드_5.3.pdf` - no downloadable URL in source.

## Terminology

| Term | Preserve as | Meaning |
| --- | --- | --- |
| `CONNTYPE=1`, `CONNTYPE=2`, `CONNTYPE=3` | Do not translate | Altibase connection type selector for TCP/IP, UNIX Domain Socket, and IPC. |
| `AUTO_COMMIT` | Do not translate | Property controlling default auto-commit behavior for non-JDBC applications unless overridden. |
| `AUTOCOMMIT` | Do not translate | Session property in `ALTER SESSION SET AUTOCOMMIT = FALSE`. |
| `CONNECTION_TIMEOUT`, `TIMEOUT`, `QUERY_TIMEOUT`, `FETCH_TIMEOUT`, `IDLE_TIMEOUT`, `UTRANS_TIMEOUT` | Do not translate | Altibase timeout options with distinct session-state effects. |
| `$ALTIBASE_HOME/conf/altibase.properties` | Do not translate | Persistent configuration file path. |
| `$ALTIBASE_HOME/trc/altibase_boot.log` | Do not translate | Timeout and session-close evidence log. |
| `PREPARE`, `BIND`, `EXECUTE`, `FETCH` | Do not translate | Required SQL protocol sequence. |
| `SQLAllocStmt`, `SQLFreeStmt`, `SQL_CLOSE`, `SQL_DROP` | Do not translate | CLI/ODBC statement allocation and release identifiers. |
| `SYSTEM_.SYS_PROCEDURES_`, `SYSTEM_.SYS_PROC_PARSE_`, `SYSTEM_.SYS_GRANT_OBJECT_`, `SYSTEM_.SYS_PRIVILEGES_`, `SYSTEM_.SYS_TABLES_`, `SYSTEM_.SYS_USERS_` | Do not translate | Meta tables used by R015 SQL and stored procedure queries. |
| `showProcedures`, `showProcBody`, `SQL%ROWCOUNT` | Do not translate | Stored procedure helper names and row-count attribute. |
| `aexport`, `ALL_CRT_PROC.sql`, `user_name_procedure_name_CRT.sql` | Do not translate | Utility and generated files for procedure DDL extraction. |
| `SP_DML_RECORD_COUNT.txt` | Do not translate | Preserved support artifact filename for the `SQL%ROWCOUNT` example. |
| `Hybrid Partitioned Table (HPT)` | Preserve full term and abbreviation | One logical table with memory and disk partitions. |
| `EXPLAIN PLAN`, `FULL SCAN`, `INDEX SCAN`, `ACCESS`, `KEY`, `FILTER` | Do not translate | Execution-plan controls and plan evidence terms. |
| `TRCLOG_PREDICATE`, `TRCLOG_DETAIL_PREDICATE`, `TIMED_STATISTICS` | Do not translate | Diagnostic properties used for performance evidence. |
| `V$STATEMENT`, `V$PLANTEXT`, `V$SQLTEXT`, `V$SYSSTAT`, `V$SESSTAT`, `V$SESSION`, `V$SERVICE_THREAD`, `V$PROPERTY`, `V$LFG`, `V$MEMGC`, `V$DISKGC`, `V$TRANSACTION`, `V$MUTEX`, `V$SYSTEM_EVENT` | Do not translate | Performance views used by R016 diagnostics. |
| `TEMP_TBS_MEMORY` | Do not translate | Hint used to place temporary work in memory for memory/disk table join cases. |
| `IPC_CHANNEL_COUNT`, `PREPARE_LOG_FILE_COUNT`, `MULTIPLEXING_THREAD_COUNT`, `MULTIPLEXING_MAX_THREAD_COUNT` | Do not translate | Connection and service-thread performance properties. |
| `CHECKPOINT_BULK_WRITE_PAGE_COUNT`, `CHECKPOINT_BULK_WRITE_SLEEP_SEC`, `CHECKPOINT_BULK_WRITE_SLEEP_USEC`, `CHECKPOINT_BULK_SYNC_PAGE_COUNT` | Do not translate | Checkpoint I/O tuning properties. |
| `AGER_WAIT_MINIMUM`, `AGER_WAIT_MAXIMUM`, `BUFFER_AREA_SIZE`, `HOT_LIST_PCT`, `BUFFER_POOL_SIZE` | Do not translate | GC, buffer cache, and disk-table performance properties. |
| `SQL_PLAN_CACHE_SIZE`, `SQL_PLAN_CACHE_BUCKET_CNT`, `SQL_PLAN_CACHE_HOT_REGION_LRU_RATIO`, `SQL_PLAN_CACHE_PREPARED_EXECUTION_CONTEXT_CNT` | Do not translate | SQL plan-cache tuning properties. |
| `SORT_AREA_SIZE`, `DISK_INDEX_BUILD_SORT_AREA_SIZE`, `DISK_INDEX_BUILD_MERGE_PAGE_COUNT`, `INDEX_BUILD_THREAD_COUNT` | Do not translate | Large DRDB index build tuning properties. |
| `LOG_IO_TYPE`, `DATABASE_IO_TYPE`, `DIRECT_IO_ENABLED` | Do not translate | Direct I/O related properties. |
| `pstack`, `vmstat`, `iostat`, `dd`, `$ALTIBASE_PID`, `$ALTIBASE_HOME/conf/glogin.sql` | Do not translate | OS commands, environment variable, and startup SQL path used in diagnostics. |
