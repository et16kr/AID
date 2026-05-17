# Troubleshooting and Error Messages

## Source paths

R013 primary Korean-source-verified source paths covered in this revision:

- `FAQE/Home/09. Error Messages/Closed Socket by client is Detected__16876319.md`
- `FAQE/Home/09. Error Messages/ERR-0109D Insufficient memory__16876324.md`
- `FAQE/Home/09. Error Messages/ERR-11030 ( 69680) The data file cannot be extended because the requested size is bigger than the maximum size (FID_0%d__16876378.md`
- `FAQE/Home/09. Error Messages/ERR-11036 The data file is in use__16876380.md`
- `FAQE/Home/09. Error Messages/ERR-11049 ( 69705) Too many pages are allocated ( Maximum Number of Pages= #)__16876385.md`
- `FAQE/Home/09. Error Messages/ERR-1105D Unable to begin a new update statement__22642969.md`
- `FAQE/Home/09. Error Messages/ERR-11075 The transaction has exceeded the lock timeout specified by the user__16876388.md`
- `FAQE/Home/09. Error Messages/ERR-11118 ( 69912) The update log size '_' is bigger than TRX_UPDATE_MAX_LOGSIZE '_'__16876399.md`
- `FAQE/Home/09. Error Messages/ERR-11183 ( 70019) Insufficient page descriptor area in the temp table__16876409.md`
- `FAQE/Home/09. Error Messages/ERR-11184 ( 70020) Insufficient free space in work area__16876418.md`
- `FAQE/Home/09. Error Messages/ERR-21010 Value overflow__16876422.md`
- `FAQE/Home/09. Error Messages/ERR-21011 _ Invalid literal__16876425.md`
- `FAQE/Home/09. Error Messages/ERR-311E0 The estimated size of the index key exceeds the maximum limit__16876328.md`
- `FAQE/Home/09. Error Messages/ERR-31283 Unable to create a primary key or a unique key constraint in the local non-prefixed index__16876430.md`
- `FAQE/Home/09. Error Messages/ERR-4103C (266300) Request of fetching data to an unprepared SQL statement__16876347.md`
- `FAQE/Home/09. Error Messages/ERR-41059 ( 266329) Task pool overflow. Check properties__16876433.md`
- `FAQE/Home/09. Error Messages/ERR-4109C Invalid session property__22642975.md`
- `FAQE/Home/09. Error Messages/ERR-410D2 (266450) Fetch out of sequence__16876332.md`
- `FAQE/Home/09. Error Messages/ERR-5102E ( 331822) Invalid cursor state__16876356.md`
- `FAQE/Home/09. Error Messages/ERR-71018 ( 462872) Failed to invoke a system function, read() or Failed to invoke the read() system function__16876441.md`
- `FAQE/Home/09. Error Messages/ERR-71019(errno=104) Failed to invoke a system function, write()__16876443.md`
- `FAQE/Home/09. Error Messages/ERR-7101D ( 462877) Protocol header error__16876373.md`
- `FAQE/Home/09. Error Messages/ERR-91015 ( 593941) Communication failure__22642976.md`
- `FAQE/Home/09. Error Messages/How to check the 8-digit errorcode of altibase_qp.log__16876313.md`
- `FAQE/Home/09. Error Messages/Not found data__16876451.md`
- `FAQE/Home/09. Error Messages/[Notify _ Fetch Timeout] Session Closed by Server__16876301.md`
- `FAQE/Home/09. Error Messages/[Warning] Memory allocation failed__16876308.md`
- `FAQE/Home/09. Error Messages/altibase_boot.log - TRY_COUNT, LOCK_COUNT, MISS_COUNT__22642967.md`
- `FAQE/Home/09. Error Messages/tablespace does not have enough free space error__16876454.md`
- `arch/Home/Altibase Development Guide/4. CLIENT APPLICATION Error Messages__14058547.md`
- `arch/Home/Altibase Precompiler Guide/4. Frequently Occurring Error Messages__22643006.md`

Cross-topic Korean-source-verified troubleshooting paths used as source labels and context:

- `arch/Home/Altibase Development Guide/3. Altibase Trace Logs__22643000.md`
- `arch/Home/Responding to Failures Guide for Altibase__15138818.md`
- `arch/Home/Responding to Failures Guide for Altibase/1. Classification by type of failure__15138822.md`
- `arch/Home/Responding to Failures Guide for Altibase/2. Procedure by type of failure__15138835.md`
- `arch/Home/Responding to Failures Guide for Altibase/3. References__15138869.md`
- `arch/Home/Troubleshooting Altibase Installation Problems__15138879.md`

## Source coverage notes

This document covers R013: Korean-source-verified troubleshooting and error-message answerability from `FAQE/Home/09. Error Messages/**`, the Korean-source-verified client application error chapter in the Altibase Development Guide, and the Korean-source-verified frequent precompiler error chapter.

The cross-topic paths above are already owned by R004, R009, or R012 for primary coverage. R013 uses only their troubleshooting labels and error signatures so answers about error messages can route users to the right operational topic without re-owning full installation, failure-response, trace-log, or diagnostic procedures.

`FAQE/Home/09. Error Messages/[Warning] Memory allocation failed__16876308.md` is `Link-validated Korean-source-verified` and contains the preserved document-format PDF attachment `ALTIBASE_운영을_위한_HPUX_설정_가이드.pdf`. `FAQE/Home/09. Error Messages/ERR-4109C Invalid session property__22642975.md` and `FAQE/Home/09. Error Messages/ERR-7101D ( 462877) Protocol header error__16876373.md` contain embedded screenshot/image URLs; these are registered as `not_document_format` and should not be treated as document-format attachments.

No R014 English-only error catalog sources are integrated here. `FAQE/Home/Altibase Error Messages__6979655.md`, `FAQE/Home/Altibase Error Messages/**`, and `FAQE/Home/ALTIBASE HDB Troubleshooting/**` remain for R014 and must be labeled `English-only source` when used.

The Development Guide source includes two Korean legacy PDF labels, `ALTIBASE_개발가이드.pdf` and `ALTIBASE_개발가이드_5.3.pdf`, without downloadable source URLs. They are preserved as legacy labels only; no URL is invented.

## Scope and audience

Use this document to answer DBA, developer, support, and LLM questions about Altibase error messages, client-side failures, cursor and precompiler failures, communication failures, memory or tablespace exhaustion, lock/time-out conditions, and SQL/data conversion errors.

When answering in another language, keep product names, commands, SQL, properties, paths, trace-log filenames, error codes, SQLCODE values, errno values, class names, attachment filenames, and URLs exactly as written.

## Key facts

Most R013 FAQ pages follow the same troubleshooting structure: version, symptom, cause, solution, and sometimes reference/version differences. Preserve the source-specific version boundary because the same behavior can produce different codes by Altibase version.

Important trace and utility names:

| Identifier | Meaning in this source set |
| --- | --- |
| `$ALTIBASE_HOME/trc/altibase_boot.log` | Primary server log for timeout, session, communication, startup, mutex, and task-pool evidence. |
| `$ALTIBASE_HOME/trc/altibase_qp.log` | Query processor log; Altibase 6.1.1 or earlier can record an 8-digit decimal error code here. |
| `$ALTIBASE_HOME/trc/altibase_rp.log` | Replication log; can record `ERR-11075`, Sender/Receiver disconnection, and replication conflict evidence. |
| `$ALTIBASE_HOME/conf/altibase.properties` | Persistent property file for settings such as `FETCH_TIMEOUT`, `MEM_MAX_DB_SIZE`, `TRX_UPDATE_MAX_LOGSIZE`, `TOTAL_WA_SIZE`, and `TEMP_MAX_PAGE_COUNT`. |
| `altierr` | Utility used to translate error codes into symbolic names, cause, and action text. |
| `SQLCODE` and `sqlca.sqlerrm.sqlerrmc` | Precompiler/APRE fields used by the frequent precompiler error chapter. |

Version-dependent code differences that must not be normalized:

| Condition | Source rule |
| --- | --- |
| Cursor fetch after COMMIT/ROLLBACK with an open cursor | Altibase 4.3.9 reports `ERR-4103C`; Altibase 5.3.3 through 6.1.1 reports SQLCODE `100` / `Not found data`; Altibase 6.3.1 or later reports `ERR-410D2`. |
| Function called from `SELECT` performs DML, `COMMIT`, or `ROLLBACK` | Altibase 6.1.1 or earlier reports `ERR-1105D`; 6.3.1, 6.5.1, and 7.1.0 or later report `ERR-31386`. |
| `TRX_UPDATE_MAX_LOGSIZE` exceeded | Altibase 5 or later reports `ERR-11118`; Altibase 4.3.9 reports `ERR-110C3`. |
| Disk temporary tablespace descriptor shortage | `ERR-11183` can occur from Altibase 6.3.1 through 7.1.0.5.0; BUG-48369 is reflected from Altibase 7.1.0.5.1, so the source says this error does not occur there. |
| `ERR-311E0` estimated index key exceeds limit | The source applies to Altibase 6.1.1 or earlier; the same case does not fail in 6.3.1 or later. |
| Client/server compatibility | Before 5.3.3, server and client must have the same `cm protocol version`; from 5.3.3, backward compatibility allows same-or-newer server with same-or-older client, but a client newer than the server can fail. |

## Procedures

### Triage an Altibase error message

1. Preserve the exact message, including `ERR-` code, SQLCODE, errno, trace-log filename, source line, and any `Session ID`, `Transaction ID`, `CLIENT_INFO`, query text, or file path.
2. Check the source context: connection/startup, query execution, cursor fetch, memory/tablespace, lock/replication, client compatibility, or precompiler host-variable handling.
3. Check the appropriate log:
   - `$ALTIBASE_HOME/trc/altibase_boot.log` for session cleanup, timeout, startup, communication, mutex, memory allocation, task pool, and property/startup evidence.
   - `$ALTIBASE_HOME/trc/altibase_qp.log` for query processor DDL/query errors.
   - `$ALTIBASE_HOME/trc/altibase_rp.log` for replication Sender/Receiver errors, `ERR-11075`, and conflict evidence.
4. Use `altierr` when the source gives a hex code or when an older log uses an 8-digit decimal code.
5. Apply the source-specific version boundary before giving a fix.
6. Prefer root-cause fixes over only increasing timeout or memory properties. Several sources warn that large timeout, memory, or log settings can keep resources occupied or create disk-full risk.

### Convert an 8-digit `altibase_qp.log` error code

Altibase 6.1.1 or earlier can write only an unknown decimal error code in `$ALTIBASE_HOME/trc/altibase_qp.log`; Altibase 6.3.1 or later writes a 5-digit error code and message directly.

Procedure for 6.1.1 or earlier:

1. Convert the 8-digit decimal error code to hexadecimal, for example decimal `822329545` becomes `3103C0C9`.
2. Take the first five hex digits as the actual error code, for example `3103C`.
3. Run `altierr` with the hex code:

```sh
altierr 0x3103C
```

The source example resolves `0x3103C` to `qpERR_ABORT_QDR_NOT_EXISTS_USER Undefined user name`.

### Investigate fetch timeout and server-closed sessions

Use this procedure for `[Notify : Fetch Timeout] Session Closed by Server`, client `ERR-91015` during fetch, APRE/ODBC `Communication link failure`, or JDBC messages such as `The session has been closed by the server`.

1. Check `$ALTIBASE_HOME/trc/altibase_boot.log`.
2. For Altibase HDB 5 or later, correlate `Session ID`, `CLIENT_INFO`, `Time Limit`, `Running Time`, `Caused by Query`, and `Transaction ID`.
3. For Altibase HDB 4.3.9, client IP is not in the server log; correlate by log time and `Caused by Query`.
4. Review application fetch logic. `FETCH_TIMEOUT` can be exceeded when the application processes fetched rows for longer than the timeout before requesting the next result set.
5. If the operational timeout is genuinely too small, change `FETCH_TIMEOUT` for the session or system and persist it in `altibase.properties` when required.

```sql
ALTER SESSION SET FETCH_TIMEOUT = 600;
ALTER SYSTEM SET FETCH_TIMEOUT = 600;
SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME = 'FETCH_TIMEOUT';
SELECT ID SESSION_ID, FETCH_TIME_LIMIT FROM V$SESSION WHERE ID = SESSION_ID();
```

`FETCH_TIMEOUT` default is 60 seconds. The source warns that long-running SELECT statements can retain old versions: memory table memory usage can increase and disk table undo tablespace usage can increase.

### Fix fetch-across-commit cursor failures

Use this procedure for `ERR-4103C`, `Not found data`, or `ERR-410D2` when rows remain but fetch fails after `COMMIT` or `ROLLBACK`.

1. Confirm that the application opens a cursor and then executes `COMMIT` or `ROLLBACK` before all rows are fetched.
2. Remember the version mapping: 4.3.9 = `ERR-4103C`; 5.3.3 through 6.1.1 = `Not found data`; 6.3.1 or later = `ERR-410D2`.
3. Change application structure. The R013 sources offer these options:
   - Use separate connections, for example `conn1` for fetch and `conn2` for DML/commit/rollback.
   - Repeatedly open the cursor with a `LIMIT :s_start, n` range sized to fit the communication buffer.
   - For Altibase 6.3.1 or later APRE, use `CURSOR WITH HOLD` for fetch across commit when that behavior is required.
4. For Altibase 4.3.9, the source states the communication buffer is 64 KB. For Altibase 5 or later, the `Not found data` source states 64 KB, while the `ERR-410D2` source states 32 KB; keep the source-specific value when citing the page.

### Check client/server version compatibility

Use this procedure for `ERR-4109C Invalid session property`, `ERR-7101D Protocol header error`, or `ERR-91015` at connection time when a later client connects to an earlier server.

```sh
altibase -v
apre -v
java -jar Altibase.jar
```

Use the same or earlier client version than the server. If a later client must be used, patch or upgrade the Altibase server to the same version. For ODBC on Windows, check `altiodbc.dll` file properties in Windows Explorer.

### Diagnose memory, work-area, and tablespace exhaustion

Use the exact source condition before changing properties:

- `ERR-0109D` during query execution can be governed by `EXECUTE_STMT_MEMORY_MAXIMUM`; check and increase the property if appropriate.
- `[Warning] Memory allocation failed` is OS-level memory allocation failure, especially HP-UX `maxdsiz` / `maxdsiz_64bit`, 32-bit process limits, or physical memory shortage.
- `ERR-11049` means total memory tablespace allocation is constrained by `MEM_MAX_DB_SIZE`; increasing it requires an Altibase restart and twice the memory-data amount as checkpoint-image disk space.
- `ERR-11183` requires aligning `TEMP_MAX_PAGE_COUNT` with the total maximum disk temporary tablespace size.
- `ERR-11184` requires increasing `TOTAL_WA_SIZE`, with memory growth visible in `V$MEMSTAT` and process `vsz` / `rss`.
- `tablespace does not have enough free space` and development/precompiler tablespace errors require adding a datafile for disk tablespaces or freeing/compacting memory tablespace data.

## SQL, commands, and configuration

### Core diagnostic and version commands

```sh
altibase -v
apre -v
java -jar Altibase.jar
altierr 0x3103C
grep MAX_CLIENT $ALTIBASE_HOME/conf/altibase.properties
ulimit -a
/usr/sbin/kctune | grep maxdsiz
```

### Timeout and session cleanup

```sql
ALTER SESSION SET FETCH_TIMEOUT = 600;
ALTER SYSTEM SET FETCH_TIMEOUT = 600;
SELECT ID SESSION_ID, FETCH_TIME_LIMIT FROM V$SESSION WHERE ID = SESSION_ID();
SELECT ID SESSION_ID, DB_USERNAME, CLIENT_CONSTR, COMM_NAME, CLIENT_PID, FETCH_TIME_LIMIT FROM V$SESSION;
SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME = 'FETCH_TIMEOUT';
ALTER DATABASE database_name SESSION CLOSE session_id;
```

### Query execution memory

```sql
SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME = 'EXECUTE_STMT_MEMORY_MAXIMUM';
ALTER SYSTEM SET EXECUTE_STMT_MEMORY_MAXIMUM = 2147483648;
```

### Memory tablespace and `MEM_MAX_DB_SIZE`

```sql
SELECT TO_CHAR(MEM_MAX_DB_SIZE/1024/1024, '999,999,999') '       MAX(M)',
       TO_CHAR(MEM_ALLOC_PAGE_COUNT*32/1024, '999,999,999') '     TOTAL(M)',
       TO_CHAR((MEM_ALLOC_PAGE_COUNT-MEM_FREE_PAGE_COUNT)*32/1024, '999,999,999') '     ALLOC(M)',
       (SELECT TO_CHAR(SUM((FIXED_USED_MEM + VAR_USED_MEM))/1024/1024, '999,999,999')
          FROM V$MEMTBL_INFO) '      USED(M)',
       TO_CHAR((((MEM_ALLOC_PAGE_COUNT-MEM_FREE_PAGE_COUNT)*32*1024)/MEM_MAX_DB_SIZE)*100, '99.99') 'USAGE(%)'
  FROM V$DATABASE;
```

```sh
server stop
vi $ALTIBASE_HOME/conf/altibase.properties
server start
```

### Transaction update log limits

```sql
SELECT ST.SESSION_ID SESSION_ID, TX.ID TX_ID,
       TX.UPDATE_SIZE,
       SUBSTR(ST.QUERY, 1, 100) QUERY
  FROM V$TRANSACTION TX, V$STATEMENT ST
 WHERE TX.ID = ST.TX_ID
   AND TX.UPDATE_SIZE <> 0;

SELECT NAME, VALUE1
  FROM V$PROPERTY
 WHERE NAME IN ('TRX_UPDATE_MAX_LOGSIZE', 'LOCK_ESCALATION_MEMORY_SIZE');

SELECT ID SESSION_ID, COMM_NAME, TRX_UPDATE_MAX_LOGSIZE FROM V$SESSION;
SELECT ID SESSION_ID, COMM_NAME, TRX_UPDATE_MAX_LOGSIZE FROM V$SESSION WHERE ID = SESSION_ID();
ALTER SESSION SET TRX_UPDATE_MAX_LOGSIZE = 52428800;
ALTER SYSTEM SET TRX_UPDATE_MAX_LOGSIZE = 52428800;
```

### Disk temporary tablespace and work area

```sql
SELECT 'DISK_TEMP_TBS_MAX_SUM',
       SUM(DECODE(F.MAXSIZE, 0, F.CURRSIZE, F.MAXSIZE)*TBS.PAGE_SIZE) AS 'MAX_SIZE(BYTE)'
  FROM V$DATAFILES F,
       V$TABLESPACES TBS
 WHERE F.SPACEID = TBS.ID
   AND TBS.TYPE IN (5, 6);

SELECT NAME, VALUE1, VALUE1*8192 FROM V$PROPERTY WHERE NAME = 'TEMP_MAX_PAGE_COUNT';
ALTER SYSTEM SET TEMP_MAX_PAGE_COUNT = value;
SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME = 'TEMP_MAX_PAGE_COUNT';
ALTER SYSTEM SET TOTAL_WA_SIZE = value;
ALTER SYSTEM SET SORT_AREA_SIZE = value;
ALTER SYSTEM SET HASH_AREA_SIZE = value;
SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME IN ('TOTAL_WA_SIZE', 'SORT_AREA_SIZE', 'HASH_AREA_SIZE');
SELECT NAME, ALLOC_SIZE, MAX_TOTAL_SIZE FROM V$MEMSTAT WHERE NAME = 'Temp_Memory';
SELECT NAME, ALLOC_SIZE, MAX_TOTAL_SIZE FROM V$MEMSTAT WHERE NAME = 'Storage_Disk_Buffer';
```

For process memory checks after work-area changes:

```sh
ps -o vsz,rss -p process_id
export UNIX95=1
ps -o vsz,rss -p process_id
ps -o vsz,rssize -p process_id
```

### Tablespace and datafile changes

```sql
SELECT NAME, AUTOEXTEND, INITSIZE, MAXSIZE FROM V$DATAFILES;
ALTER TABLESPACE DISK_USER_TBS ALTER DATAFILE '/home/altibase_home/dbs/user.dbf' AUTOEXTEND ON;
ALTER TABLESPACE DISK_USER_TBS ALTER DATAFILE '/home/altibase_home/dbs/user.dbf' SIZE 100M;
ALTER TABLESPACE tablespace_name ADD DATAFILE '/path/filename' SIZE 2G AUTOEXTEND OFF;
ALTER TABLESPACE [tablespace name] ALTER AUTOEXTEND OFF;
ALTER TABLESPACE [tablespace name] ALTER AUTOEXTEND ON MAXSIZE 1G;
ALTER TABLE [table name] COMPACT;
```

### Task pool overflow checks

```sql
SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME = 'MAX_CLIENT';
SELECT COUNT(*) FROM V$SESSION;
SELECT NAME, VALUE FROM V$SYSSTAT WHERE NAME = 'logon current';
```

```sh
export ISQL_CONNECTION=IPC
is -silent -sysdba
netstat -an | grep 20300 | grep ESTA | wc -l
lsof -p PID | grep -e IPv4 -e sock | grep -v LISTEN
pfiles PID | grep sock
ipcs -m | grep -i -e nattch -e altibase
ipcs -ma | grep -e NATTCH -e altibase
```

## Validation and troubleshooting

### Korean-source-verified error catalog

| Error or message | Version/source condition | Symptom and cause | Resolution |
| --- | --- | --- | --- |
| `[Notify : Fetch Timeout] Session Closed by Server` | All Altibase HDB versions; server log format differs for HDB 5+ and HDB 4.3.9. | `FETCH_TIMEOUT` exceeded between fetch requests; server closes the session and rolls back the transaction. Client can see `ERR-91015`, APRE/ODBC communication link failure, or JDBC closed-session/broken-pipe variants. | Review application fetch processing; tune query if needed; change `FETCH_TIMEOUT` by `ALTER SESSION`, `ALTER SYSTEM`, and `altibase.properties` only when operationally justified. |
| `[Warning] Memory allocation failed` / `ERR-01051` | All Altibase HDB versions; mainly HP-UX. | OS memory allocation fails during transaction execution, startup, shutdown, or new connection. Causes include HP-UX `maxdsiz` / `maxdsiz_64bit`, 32-bit process limits, or insufficient physical memory. | Check HP-UX kernel parameters, physical memory with `top` or `glance`, and unexpected use of default memory tablespace `SYS_TBS_MEM_DATA`; use the preserved HP-UX setup PDF as reference. |
| `altibase_boot.log` `TRY_COUNT`, `LOCK_COUNT`, `MISS_COUNT` reset | 6.3.1 or earlier uses `INTEGER` for `V$MUTEX` counters; 6.5.1 and 7.1.0+ use `BIGINT`; 7.1.0+ adds `THREAD_ID`. | Mutex statistics exceed their maximum value and are logged before reset to zero. | No action is required; this is a counter reset message. |
| 8-digit `altibase_qp.log` error code | Altibase 6.1.1 or earlier; 6.3.1+ prints five-digit error and message. | Query processor log shows a decimal code such as `822329545` without message. | Convert decimal to hex, take the first five hex digits, then run `altierr`, for example `822329545` -> `3103C0C9` -> `0x3103C`. |
| `[Notify : Detect] Closed Socket by client is Detected` | All versions. | Client disconnects normally, client process terminates, or network disconnect is detected; server logs and cleans the session. | No server action if service impact is absent. Check application restart or network if unexpected. |
| `ERR-0109D Insufficient memory` | All versions; same cause can show `ERR-01067` in 5.3.3. | Query execution using memory temp area exceeds `EXECUTE_STMT_MEMORY_MAXIMUM`, often with `ORDER BY` / `GROUP BY` on memory tables. | Check `EXECUTE_STMT_MEMORY_MAXIMUM`; increase appropriately in bytes; preserve in property file if needed; contact Altibase support if this does not resolve another memory-allocation cause. |
| `ERR-311E0 The estimated size of the index key exceeds the maximum limit` | Altibase 6.1.1 or earlier; same source case succeeds in 6.3.1+. | Join, `ORDER BY`, or `GROUP BY` on disk table uses disk temp tablespace with fixed 8 KB page; record larger than one page can fail. | Use `/*+ TEMP_TBS_MEMORY */` to use memory temp area or upgrade to 6.3.1 or later. |
| `ERR-4103C Request of fetching data to an unprepared SQL statement` | Altibase 4.3.9. | COMMIT/ROLLBACK is executed after cursor open; fetch proceeds until the communication buffer is exhausted, then fails. | Change application: separate fetch and DML sessions or repeatedly open cursor with `LIMIT`; see fetch-across-commit procedure. |
| `Not found data` while cursor fetch remains | Altibase 5.3.3, 5.5.1, 6.1.1. | Same open-cursor COMMIT/ROLLBACK pattern as `ERR-4103C`, but reported as SQLCODE `100` / `02000`. | Same application fixes as `ERR-4103C`; preserve the version-specific code in answers. |
| `ERR-410D2 Fetch out of sequence` | Altibase 6.3.1 or later. | Same open-cursor COMMIT/ROLLBACK pattern; source also documents `CURSOR WITH HOLD` for APRE. | Separate fetch and DML sessions; use repeated `LIMIT`; or use APRE `CURSOR WITH HOLD` when fetch across commit is required. |
| `ERR-5102E Invalid cursor state` | Altibase HDB 4 or later; HDB 4.3.9 may produce it even though the HDB 4.3.9 error manual/altierr lacks the explanation. | Cursor is reused while open, close failure is ignored, result data remains, or SQLCLI/ODBC executes/prepare/direct-exec while fetch is active. | Explicitly close cursors, add exception handling for cursor close, and reuse only after remaining data is fetched or cursor is closed. |
| `ERR-7101D Protocol header error` | All Altibase versions. | Incompatible client connects; client version newer than server or pre-5.3.3 protocol mismatch. Message is logged in `altibase_boot.log` and does not affect server operation. | Find the client and install a compatible same-or-earlier client; check versions with `altibase -v`, `sesc -v` / `apre -v`, `java -jar $ALTIBASE_HOME/lib/Altibase.jar`, or ODBC DLL properties. |
| `ERR-11030 The data file cannot be extended because the requested size is bigger than the maximum size` | Altibase HDB 4. | Datafile with `AUTOEXTEND OFF` is resized larger than `MAXSIZE`. In HDB 4.3.9, `autoextend off next` / `maxsize` handling is limited; HDB 5 sets maxsize to OS file limit (`0` in `V$DATAFILES`). | Turn `AUTOEXTEND ON`, resize the datafile, and check OS file limit with `ulimit -a`. |
| `ERR-11036 The data file is in use` | All versions. | `ALTER TABLESPACE ... DROP DATAFILE` targets a datafile that has been used at least once, even if now free. | Used datafiles cannot be dropped. Export objects/data, drop and recreate the tablespace, then recreate/import. |
| `ERR-11049 Too many pages are allocated` | All versions. | Total memory tablespace allocation reaches `MEM_MAX_DB_SIZE`; memory table indexes are excluded, but MVCC historical data and all memory tablespaces are included. | Increase `MEM_MAX_DB_SIZE` in `altibase.properties` and restart; check per-table usage and bulk changes; ensure checkpoint-image disk capacity is about twice memory data usage; review OS limits. |
| `ERR-1105D` / `ERR-31386` DML, commit, or rollback inside query | `ERR-1105D` in 6.1.1 or earlier; `ERR-31386` in 6.3.1, 6.5.1, and 7.1.0+. | Function used in a `SELECT` contains `INSERT`, `UPDATE`, `COMMIT`, or `ROLLBACK`. | Functions called from `SELECT` must contain only `SELECT`; execute the function outside `SELECT` if DML is required. |
| `ERR-11075 The transaction has exceeded the lock timeout specified by the user` | All versions; wording differs for 4.3.9 through 5.3.3 versus 5.5.1+. | Lock cannot be acquired for DDL, memory-table lock escalation, `SELECT FOR UPDATE WAIT N/NOWAIT`, or replication apply waiting for local transaction. | Run DDL in idle time; inspect long-running/uncommitted transactions; reduce bulk memory changes; retry or increase `WAIT`; in replication, avoid simultaneous updates to the same record and verify data integrity. |
| `ERR-11118` / `ERR-110C3` update log larger than `TRX_UPDATE_MAX_LOGSIZE` | HDB 5+ = `ERR-11118`; HDB 4.3.9 = `ERR-110C3`. | One memory-table change transaction produces online transaction log larger than `TRX_UPDATE_MAX_LOGSIZE`; memory table out-place MVCC can create multiple versions. | Reduce rows per update, shorten commit cycle, estimate `UPDATE_SIZE`, and change `TRX_UPDATE_MAX_LOGSIZE` at session/system/property level. Keep it below `LOCK_ESCALATION_MEMORY_SIZE` to avoid X lock. |
| `ERR-11183 Insufficient page descriptor area in the temp table` | Altibase 6.3.1 through 7.1.0.5.0; not expected after BUG-48369 in 7.1.0.5.1+. | Disk temporary tablespace maximum exceeds `TEMP_MAX_PAGE_COUNT`, and a disk SORT/HASH operation requires more pages than `TEMP_MAX_PAGE_COUNT`. | Set `TEMP_MAX_PAGE_COUNT` to total max disk temp tablespace bytes / 8192; also review `TOTAL_WA_SIZE`, `SORT_AREA_SIZE`, and `HASH_AREA_SIZE`. |
| `ERR-11184 Insufficient free space in work area` | Altibase server 6.3.1 or later. | Concurrent disk SORT/HASH operations cannot allocate `SORT_AREA_SIZE` or `HASH_AREA_SIZE` from Work Area. | Increase `TOTAL_WA_SIZE`; update `altibase.properties`; monitor `V$MEMSTAT` and process memory; remember `ALTER SYSTEM SET TOTAL_WA_SIZE` can wait behind active SORT/HASH transactions. |
| `ERR-21010 Value overflow` | All versions. | Input value exceeds the range of the target data type, for example `2147483648` into `INTEGER`. | Change input value or data type; consult General Reference data-type ranges. |
| `ERR-21011 Invalid literal` | All versions. | Conversion/comparison data types do not match: incompatible `UNION`, invalid `TO_NUMBER`, automatic cast of nonnumeric CHAR, blank converted without `TRIM`. | Align data types, quote character comparisons, clean nonnumeric values, or use `TRIM` before numeric conversion where source data contains spaces. |
| `ERR-31283 Unable to create a primary key or a unique key constraint in the local non-prefixed index` | Altibase 6.1.1 or earlier. | Global index is unsupported; local non-prefixed index cannot guarantee table-wide uniqueness across partitions. | Make PK/UNIQUE a local prefixed index with partition key and index key aligned, use non-unique index, or upgrade to 6.3.1+ for global index support. |
| `ERR-41059 Task pool overflow. Check properties` | Altibase HDB 5 or later. | Task count reaches `MAX_CLIENT`; possible causes are increased connections, all service threads in `EXECUTE`, or `TRANSACTION_TABLE_SIZE` full while new connections create tasks. | Check `MAX_CLIENT`, session count, `logon current`, OS sockets/files, and `altibase_boot.log`; increase `MAX_CLIENT` only with `TRANSACTION_TABLE_SIZE` and open-file limits reviewed; fix application connection lifecycle. |
| `ERR-71018` / `ERR-71019` read/write system function failure | HDB 4 through 5.3.3 wording differs from 5.5.1+. | Session manager detects lost TCP connection. `ERR-71018` is read-side loss while waiting for client request; `ERR-71019` is write-side loss while sending response. Causes include client RST (`ECONNRESET`), timeout (`ETIMEDOUT`), L4/firewall idle cleanup, network device failure, or client abnormal restart. | No server action if it only records cleanup. Investigate network/client when frequent or service-impacting. For replication, similar messages can appear in `altibase_rp.log` when Sender detects Receiver stop. |
| `ERR-91015 Communication failure` | All Altibase HDB versions. | Can occur when connecting, while connected, or during startup. Causes include later client connecting to older server, session termination by `FETCH_TIMEOUT` / `UTRANS_TIMEOUT` / `IDLE_TIMEOUT`, forced session close by SYSDBA, or invalid startup properties. | Check server/client versions first for connection failures. If connected session fails, inspect `altibase_boot.log` for timeout notifications. During startup, compare terminal output, `altibase_boot.log`, and `altibase.properties`. |
| `tablespace does not have enough free space` | Altibase HDB 4 or later. | Specific tablespace is insufficient. | Check tablespace usage using version-appropriate monitoring queries, then add datafile to the near-100% tablespace. Adding datafile locks the tablespace; block service if needed. HDB 5.3.3 and earlier make SELECT and DML wait; HDB 5.5.1 through latest V6 lets SELECT run but DML waits. |

### Client application error catalog

The Development Guide chapter is a developer-facing index of frequent application errors:

| Error label | Developer action |
| --- | --- |
| `Connection does not exist` | Check DBMS connection state, TIMEOUT disconnection, and threaded-program connection names. |
| `Communication link failure` | Check `altibase_boot.log` for timeout/session disconnect, threaded-program precautions, and temporary network problems. |
| `Calculate stack overflow` | Run `ALTER SESSION SET STACK SIZE = 8192;`; prefer session-level change because memory usage increases. |
| `Conversion not applicable` | Check unsupported type conversion, for example CLOB into BYTE; consult Altibase SQL Reference conversion functions. |
| `Invalid cursor state` | Close cursors explicitly; control threaded connection-object concurrency. |
| `Not defined cursor` | Check errors at `DECLARE` / `PREPARE` before `EXECUTE` or `OPEN CURSOR`. |
| `Invalid request to process the SQL statement` | In threaded programs, enforce connection concurrency and order such as `PREPARE -> BINDING -> EXECUTE`. |
| `Invalid literal` | Do not insert character data into numeric types; match values to column/host-variable types. |
| `Invalid length of data type` | Input cannot exceed column length, for example 4 bytes into `CHAR(2)`. |
| `Indicator variable required but not supplied` | Use an indicator variable for nullable SELECT columns or APRE `-unsafe_null`. |
| `Invalid size of data to bind to host variable` | Check host variable length, initialization/garbage values, and threaded binding mix-ups. |
| `Invalid character in use` | For Korean text, avoid mixed data outside `KO16KSC5601`; source recommends `MS949` / `UTF8` and matching client/server character sets. |
| `Too many pages are allocated` | Delete unnecessary memory data or increase `MEM_MAX_DB_SIZE` and restart; then investigate per-table usage or bulk changes. |
| `The Tablespace does not have enough free space` | Add a datafile for disk tablespaces. |
| `The transaction exceeds lock timeout specified by user` | Check table locks before DDL; DDL can fail immediately when DML already holds a lock. |
| `The update log size ... is bigger than TRX_UPDATE_MAX_LOGSIZE ...` | Change `TRX_UPDATE_MAX_LOGSIZE` at session level only when needed; beware redo log growth, disk full, and X-Lock waits. |
| `String data right truncated` | Declare host variable as column size plus 1 byte. |
| `Value overflow` | Ensure numeric input fits the column range. |
| `Several statement still opened` | Finish cursor fetch or close open cursors before running DDL in the same session, or run DDL in another session. |

### Precompiler SQLCODE catalog

The precompiler guide groups frequent APRE/SESC errors by `SQLCODE` and `sqlca.sqlerrm.sqlerrmc`. Two SQLCODE values can map to the same message because different internal modules can raise the same content; the corrective action is the same.

| Precompiler error | SQLCODE values | Resolution basis |
| --- | --- | --- |
| `Connection does not exist.` | `-2` | Check connection handling and `EXEC SQL AT`; if server disconnected the connection, inspect timeout-related messages. |
| `String data right truncated.` | `1` | Increase variable length to data length plus 1 byte. |
| `Invalid size of data to bind to a host variable` | `-201144`, `-266423` | Host variable is shorter than actual column data; check variable length, memory damage, and threaded connection concurrency. |
| `Calculation stack overflow` | `-135187`, `-659475` | Execute `EXEC SQL ALTER SESSION SET STACK SIZE = 4096;`; default is 1024. |
| `Value overflow` / `Numeric value out of range` | `-135184`, `-659472`, `-331890` | Correct the value or column type. |
| `Conversion not applicable` | `-135180`, `-659468` | Use convertible column/host-variable types; source notes unsupported CLOB/BLOB host-variable conversion. |
| `Invalid length of the data type` | `-135181`, `-659469` | Input must fit DB column length. |
| `Invalid literal` | `-135185`, `-659473` | Numeric host variables and numeric functions must receive numeric strings. |
| `Invalid character value for cast specification` | `-331893` | Declare host variable suitable for the column type. |
| `Invalid cursor state` / `Function sequence error` | `-331822`, `-331796` | Follow cursor order and avoid fetching a closed or fully consumed cursor. |
| `The cursor must be opened for fetch` / `The cursor does not exist` | `-1`, `-589857` | Use `PREPARE -> DECLARE -> OPEN -> FETCH -> CLOSE`. |
| `Not enough insert values` | `-200787` | Match INSERT column count to host variable count. |
| `The tablespace does not have enough free space` | `-69685`, `-69923` | Add disk datafile or free/compact memory tablespace data. |
| `Input literal is not long enough for date format` | `-135218` | Check date input length, for example `TO_DATE('10123', 'yyyymmdd')`. |
| `Literals in the input do not match format string` | `-135224` | Match date string and format, for example avoid `TO_DATE('2010123', ' yyyy-mmdd')`. |
| `The transaction is already active` | `-266311`, `-266312` | Commit or rollback before changing Auto-Commit; review connection-pool/thread use. |
| `The row already exists in a unique index` | `-69720` | Check whether PK/UNIQUE value already exists. |
| `Unable to insert (or update) NULL into NOT NULL column` | `-200790` | Trace input values or change `NOT NULL` constraints appropriately. |
| `Indicator variable required but not supplied` | `-331841`, `-594101`, `594103` | Use `NVL`, indicator variable, or APRE `-unsafe_null`; this can be returned as `SQL_SUCCESS_WITH_INFO`. |
| `Client's query exceeded in the execution time limitation` | `-4164` | Tune execution plan or set `QUERY_TIMEOUT = 0` only after resource impact review. |
| `Communication link failure` | `-331843`, `-331855` | Check timeout messages in `altibase_boot.log`; adjust `FETCH_TIMEOUT` or `UTRANS_TIMEOUT` only when the root cause is understood; investigate network/L4/firewall with PBT if no log remains. |

## Version-specific notes

- `FETCH_TIMEOUT` default is 60 seconds in the FAQ source.
- `UTRANS_TIMEOUT` is described by the precompiler source as a 3600-second limit for an uncommitted change transaction.
- `TRX_UPDATE_MAX_LOGSIZE` default is 10 MB (`10485760` bytes).
- `TEMP_MAX_PAGE_COUNT` is a page count; convert to bytes by multiplying by 8192.
- Recommended work-area ratios when changing `TEMP_MAX_PAGE_COUNT`: `TOTAL_WA_SIZE = TEMP_MAX_PAGE_COUNT * 256`, `SORT_AREA_SIZE = TEMP_MAX_PAGE_COUNT * 2`, and `HASH_AREA_SIZE = TEMP_MAX_PAGE_COUNT * 8`.
- For `ERR-11183`, example values are `TEMP_MAX_PAGE_COUNT = 1048576` for 8 GB, `2097152` for 16 GB, `4192256` for 32 GB, and `8388608` for 64 GB.
- The `ERR-11118` source records BUG-20511 for versions 4.3.9.103 through 4.3.9.133 and BUG-26311 for versions 4.3.9.163 through 4.3.9.165.
- For `ERR-71018` / `ERR-71019`, source system error codes are: `ECONNRESET` Linux 104, AIX 73, HP-UX 232, SUN 131, Windows 10054; `ETIMEDOUT` Linux 110, AIX 78, HP-UX 238, SUN 145, Windows 10060.
- For tablespace add operations, HDB 5.3.3 and earlier make SELECT and DML wait. From HDB 5.5.1 through latest V6 in the source, DML waits but SELECT executes normally.

## Related errors

| Relationship | Error/messages |
| --- | --- |
| Fetch timeout can surface as client communication errors | `[Notify : Fetch Timeout]`, `ERR-91015`, APRE `-331843`, SQLCLI/ODBC `SQLSTATE 08S01`, JDBC closed-session/broken-pipe messages. |
| Open cursor plus COMMIT/ROLLBACK | `ERR-4103C`, `Not found data`, `ERR-410D2`. |
| Client/server compatibility | `ERR-4109C`, `ERR-7101D`, sometimes `ERR-91015` at connection. |
| Memory and work-area resource limits | `[Warning] Memory allocation failed`, `ERR-0109D`, `ERR-11049`, `ERR-11183`, `ERR-11184`. |
| Tablespace space/datafile handling | `ERR-11030`, `ERR-11036`, `ERR-11123`, `tablespace does not have enough free space`. |
| Lock and bulk update | `ERR-11075`, `ERR-11118`, `ERR-110C3`, `LOCK_ESCALATION_MEMORY_SIZE`, `TRX_UPDATE_MAX_LOGSIZE`. |
| SQL/data typing | `ERR-21010`, `ERR-21011`, `Invalid literal`, `Value overflow`, `Invalid length of data type`, `String data right truncated`. |
| Replication conflict/failure labels from cross-topic troubleshooting | `ERR-61012`, `ERR-61022`, `ERR-61035`, `ERR-61036`, `ERR-6103a`, `ERR-61047`, `ERR-61048`, `ERR-6104b`, `ERR-61000`, `ERR-61001`, `ERR-11058`. |

## Attachments and external references

Preserved R013 attachment and image evidence:

| Source path | Label or URL | Status |
| --- | --- | --- |
| `FAQE/Home/09. Error Messages/[Warning] Memory allocation failed__16876308.md` | `ALTIBASE_운영을_위한_HPUX_설정_가이드.pdf` at `https://docs.altibase.com/download/attachments/9109748/ALTIBASE_%EC%9A%B4%EC%98%81%EC%9D%84_%EC%9C%84%ED%95%9C_HPUX_%EC%84%A4%EC%A0%95_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1449022354000&api=v2` | `preserved_url` |
| `FAQE/Home/09. Error Messages/ERR-4109C Invalid session property__22642975.md` | Three embedded PNG screenshot URLs showing client/server property exchange and ODBC DLL properties | `not_document_format` |
| `FAQE/Home/09. Error Messages/ERR-7101D ( 462877) Protocol header error__16876373.md` | Embedded `odbcdll.png` screenshot URL | `not_document_format` |
| `arch/Home/Altibase Development Guide/4. CLIENT APPLICATION Error Messages__14058547.md` | `ALTIBASE_개발가이드.pdf`; `ALTIBASE_개발가이드_5.3.pdf` | `legacy_no_downloadable_url` |

External reference labels and URLs preserved in the source set:

| Source context | Label | URL |
| --- | --- | --- |
| `ERR-21010 Value overflow` | Altibase manuals | `http://support.altibase.com/en/manual` |
| `ERR-21010 Value overflow` | ALTIBASE Documents on GitHub | `https://github.com/ALTIBASE/Documents` |
| `ERR-410D2 Fetch out of sequence` | Altibase manuals | `http://support.altibase.com/en/manual/` |
| `ERR-410D2 Fetch out of sequence` | ALTIBASE Documents manuals | `https://github.com/ALTIBASE/Documents/tree/master/Manuals` |
| Development Guide conversion errors | Altibase SQL Reference conversion functions | `https://github.com/ALTIBASE/Documents/blob/master/Manuals/Altibase_7.3/kor/SQL%20Reference.md#%EB%B3%80%ED%99%98-%ED%95%A8%EC%88%98` |
| Development Guide `TRX_UPDATE_MAX_LOGSIZE` warning and `ERR-11075` reference | `ERR-11118` FAQ | `https://docs.altibase.com/pages/viewpage.action?pageId=16876399` |
| `ERR-91015 Communication failure` | `FETCH_TIMEOUT` FAQ | `https://docs.altibase.com/pages/viewpage.action?pageId=16876301` |
| `ERR-91015 Communication failure` | `UTRANS_TIMEOUT` undo monitoring FAQ | `https://docs.altibase.com/display/FAQE/Monitoring+method+when+undo+tablespace+usage+increases` |
| `ERR-91015 Communication failure` | `IDLE_TIMEOUT` database security checklist | `https://docs.altibase.com/display/FAQE/Database+Security+Checklist` |
| Cursor version-reference tables | `ERR-4103C` FAQ | `https://docs.altibase.com/pages/viewpage.action?pageId=16876347` |
| Cursor version-reference tables | `Not found data` FAQ | `https://docs.altibase.com/pages/viewpage.action?pageId=16876451` |
| Cursor version-reference tables | `ERR-410D2` FAQ | `https://docs.altibase.com/pages/viewpage.action?pageId=16876332` |
| `ERR-41059 Task pool overflow` | `MAX_CLIENT` considerations FAQ | `https://docs.altibase.com/pages/viewpage.action?pageId=16876028` |
| `ERR-11049 Too many pages are allocated` | `MEM_MAX_DB_SIZE` FAQ | `https://docs.altibase.com/pages/viewpage.action?pageId=16875991` |
| `tablespace does not have enough free space` | Monitoring FAQ category | `https://docs.altibase.com/display/FAQE/08.+Monitoring` |

## Terminology

| Term | Preservation rule |
| --- | --- |
| `FETCH_TIMEOUT`, `UTRANS_TIMEOUT`, `IDLE_TIMEOUT`, `QUERY_TIMEOUT` | Keep property names untranslated and uppercase. |
| `TRX_UPDATE_MAX_LOGSIZE`, `LOCK_ESCALATION_MEMORY_SIZE`, `TEMP_MAX_PAGE_COUNT`, `TOTAL_WA_SIZE`, `SORT_AREA_SIZE`, `HASH_AREA_SIZE`, `MEM_MAX_DB_SIZE`, `EXECUTE_STMT_MEMORY_MAXIMUM`, `MAX_CLIENT`, `TRANSACTION_TABLE_SIZE` | Keep exact property names and do not translate. |
| `altibase_boot.log`, `altibase_qp.log`, `altibase_rp.log`, `altibase_error.log`, `altibase_dump.log`, `$ALTIBASE_HOME/conf/altibase.properties` | Keep exact filenames and paths. |
| `altierr`, `isql`, `apre`, `sesc`, `iloader`, `server start`, `server stop` | Keep utility names and commands unchanged. |
| `ERR-0109D`, `ERR-11030`, `ERR-11036`, `ERR-11049`, `ERR-1105D`, `ERR-11075`, `ERR-11118`, `ERR-11183`, `ERR-11184`, `ERR-21010`, `ERR-21011`, `ERR-311E0`, `ERR-31283`, `ERR-4103C`, `ERR-41059`, `ERR-4109C`, `ERR-410D2`, `ERR-5102E`, `ERR-71018`, `ERR-71019`, `ERR-7101D`, `ERR-91015`, `ERR-31386` | Keep exact error codes and message text where cited. |
| `SQLCODE`, `sqlca.sqlerrm.sqlerrmc`, `SQL_SUCCESS`, `SQL_NO_DATA`, `SQL_SUCCESS_WITH_INFO` | Keep exact precompiler/SQL status identifiers. |
| `ECONNRESET`, `ETIMEDOUT`, `errno`, `RST packet`, `L4 switch`, `firewall` | Keep network/system terminology stable. |
| `Sender`, `Receiver`, `REP_GAP`, `XSN`, `SN`, `Replication Gap` | Keep replication terms as source identifiers. |
