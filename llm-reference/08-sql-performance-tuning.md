# SQL, Stored Procedures, and Query Behavior

## Source paths

R015 Korean-source-verified source paths covered in this revision:

- `arch/Home/Altibase Development Guide__14058519.md`
- `arch/Home/Altibase Development Guide/2. Considerations when Developing__14058531.md`
- `FAQE/Home/05. SQL/Comparison between VARCHAR and CHAR types__16876151.md`
- `FAQE/Home/05. SQL/How to check the privileges granted to an object__16876153.md`
- `FAQE/Home/06. Stored Procedure/How to check the contents of stored procedure__16876159.md`
- `FAQE/Home/06. Stored Procedure/How to check the number of records affected by DML within the stored procedure__16876157.md`

Additional source paths read for the wider workflow boundary, but not re-owned by R015:

- `arch/Home/Altibase Development Guide/1. Considerations when Designing__22642998.md` - R016 owns the performance, design, partitioning, HPT, and index semantics.
- `arch/Home/Altibase Development Guide/3. Altibase Trace Logs__22643000.md` - R012 owns trace-log diagnostics and R013 uses error-message cross-labels.
- `arch/Home/Altibase Development Guide/4. CLIENT APPLICATION Error Messages__14058547.md` - R013 owns client application error-message coverage.
- `FAQE/Home/12. Others/Building a Large-Scale DRDB Index__22642978.md` - R016 owns DRDB index build tuning coverage.
- `FAQE/Home/12. Others/Thread process debugging method__16876474.md` - R012 owns thread debugging diagnostics.

## Source coverage notes

This document covers R015: SQL behavior, stored procedure inspection, stored procedure row-count examples, connection/session query behavior, cursor behavior, LOB query restrictions, prepared statement usage, timeout behavior, exact SQL examples, object privilege queries, and development cautions that affect SQL answerability.

The R015 source set is Korean-source-verified. `FAQE/Home/06. Stored Procedure/How to check the number of records affected by DML within the stored procedure__16876157.md` is link-validated Korean-source-verified because Phase 2 verified the preserved support artifact URL for `SP_DML_RECORD_COUNT.txt`.

`SP_DML_RECORD_COUNT.txt` is a downloadable `.txt` support artifact, not a document-format attachment under the `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.zip` preservation gate. The exact source URL is preserved in this topic and in `llm-reference/coverage/attachment-diagram-register.tsv`.

The wider Altibase Development Guide source also contains two Korean legacy PDF labels, `ALTIBASE_개발가이드.pdf` and `ALTIBASE_개발가이드_5.3.pdf`, with no downloadable source URL. R013 already registers those labels for the client application error chapter; R015 does not invent URLs for them.

R016 will add optimizer, index, partitioning, HPT, SQL tuning guide, large DRDB index, and performance-specific coverage to this same topic file. Until R016 is complete, use only the R015 sections below for SQL and stored procedure answer generation.

## Scope and audience

Use this document to answer developer, DBA, support, and LLM questions about Altibase SQL behavior that affects applications: connection type selection, auto-commit, session timeout settings, cursor lifecycle, commit and rollback during fetch, error checking around `PREPARE` and `DECLARE CURSOR`, LOB query requirements, prepared statements, execution-plan checks, `CHAR` and `VARCHAR` comparison behavior, object privilege lookup SQL, stored procedure body extraction, and `SQL%ROWCOUNT`.

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

For SQL performance validation, the Development Guide's R015 source only covers basic execution-plan checking with `ALTER SESSION SET EXPLAIN PLAN = ON`; deeper optimizer, index, partitioning, and SQL Tuning Guide content belongs to R016.

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
| R015 execution plan check | Development Guide source shows `ALTER SESSION SET EXPLAIN PLAN = ON`; deeper tuning version boundaries are R016-owned. |

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

## Attachments and external references

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
