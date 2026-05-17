# Operation, Administration, and Security

## Source paths

R007 source paths covered in this revision:

- `arch/Home/Altibase Configuration File Guide__22642991.md`
- `arch/Home/Understanding the Altibase Start_Shut down Process__14909450.md`
- `arch/Home/Understanding the Altibase Start_Shut down Process/1. Starting Altibase__14909452.md`
- `arch/Home/Understanding the Altibase Start_Shut down Process/2. Shutting Altibase Down__14909483.md`
- `arch/Home/System Data Capacity Estimation Guide for Altibase Operations__22643042.md`
- `arch/Home/Utility Guide for each OS for Problem Analysis__16875587.md`
- `arch/Home/UNIX Memory Management__16875572.md`

R008 source paths covered in this revision:

- `FAQE/Home/02. Operation and Management/Altibase Server Configuration for IPC Communication__22642933.md`
- `FAQE/Home/02. Operation and Management/Automatic altibase startup during OS booting in Solaris__16875996.md`
- `FAQE/Home/02. Operation and Management/Can PUBLIC SYNONYM be dropped__16875993.md`
- `FAQE/Home/02. Operation and Management/Can table data be saved on disk and only indexes can be created in memory__16876008.md`
- `FAQE/Home/02. Operation and Management/Database Security Checklist__22642935.md`
- `FAQE/Home/02. Operation and Management/Detailed procedure for changing character set__16876045.md`
- `FAQE/Home/02. Operation and Management/How to change sys user password__16876004.md`
- `FAQE/Home/02. Operation and Management/How to change the database's db name__16875966.md`
- `FAQE/Home/02. Operation and Management/How to change the path of log anchor, online log file, archive log file, and double write file__16876052.md`
- `FAQE/Home/02. Operation and Management/How to change the tablespace data file path__16876049.md`
- `FAQE/Home/02. Operation and Management/How to check the history of adding datafiles__16875969.md`
- `FAQE/Home/02. Operation and Management/How to create a user (CREATE USER) and change a password (ALTER USER)__16876036.md`
- `FAQE/Home/02. Operation and Management/How to create and execute Job objects__16876042.md`
- `FAQE/Home/02. Operation and Management/How to forcefully close a session that is being locked__16875986.md`
- `FAQE/Home/02. Operation and Management/How to modify column__16875952.md`
- `FAQE/Home/02. Operation and Management/How to resolve when LOCK TIMEOUT occurs__16875984.md`
- `FAQE/Home/02. Operation and Management/How to start and stop the database__22642937.md`
- `FAQE/Home/02. Operation and Management/How to startup Altibase automatically when booting from HP-UX__16875976.md`
- `FAQE/Home/02. Operation and Management/Maximum Capacity Specifications for Altibase__16875989.md`
- `FAQE/Home/02. Operation and Management/Notes on using floating point data type (double, float)__16875974.md`
- `FAQE/Home/02. Operation and Management/Notes_Considerations when changing TRANSACTION_TABLE_SIZE__16876013.md`
- `FAQE/Home/02. Operation and Management/Notes_Considerations when increasing the number of concurrent connection sessions (MAX_CLIENT)__16876028.md`
- `FAQE/Home/02. Operation and Management/The OS time and the DB time do not match__22642939.md`
- `FAQE/Home/02. Operation and Management/User password length limitation - Differences by version__22642941.md`
- `FAQE/Home/02. Operation and Management/What is MEM_MAX_DB_SIZE__16875991.md`
- `FAQE/Home/02. Operation and Management/When log disk is FULL and its countermeasures__16876034.md`
- `FAQE/Home/02. Operation and Management/When server create errors occur after DB name change__16875972.md`
- `FAQE/Home/02. Operation and Management/[Linux] How to register Altibase server process auto start script__16875947.md`

R021 English-only auxiliary source paths indexed in this revision:

- `FAQE/Home/ALTIBASE HDB Administration/How to terminate a session__1802689.md`
- `FAQE/Home/ALTIBASE HDB Administration/Useful SQL/Miscellaneous queries__1802687.md`
- `FAQE/Home/ALTIBASE HDB Administration/Useful SQL/SQL about Objects__1802681.md`
- `FAQE/Home/ALTIBASE HDB Administration/Useful SQL/SQL about Replication__1802683.md`
- `FAQE/Home/ALTIBASE HDB Administration/Useful SQL/SQL about Sessions__1802677.md`
- `FAQE/Home/ALTIBASE HDB Administration/Useful SQL/SQL about Statements__1802679.md`
- `FAQE/Home/ALTIBASE HDB Administration/Useful SQL/SQL about Tablespaces__1802685.md`

## Source coverage notes

This document covers the R007 and R008 portions of `llm-reference/03-operation-administration-security.md`: Altibase configuration properties, startup and shutdown stages, system memory and disk capacity sizing, OS-level problem-analysis utilities, UNIX memory-management behavior, and operational FAQ coverage for administration, security, sessions, clients, character sets, JOBs, file movement, and data/log operations.

All R007 source files are classified as `Link-validated Korean-source-verified` in `llm-reference/coverage/source-inventory.tsv`. The R007 source set uses only Korean-source-verified architecture pages. No English-only auxiliary source is used in this revision.

Six unique URL-backed PDF attachments from Korean source pages are preserved in the English source set and registered in `llm-reference/coverage/attachment-diagram-register.tsv`: two configuration-guide PDFs, one startup/shutdown PDF, one capacity-estimation PDF, one OS utility PDF, and one UNIX memory-management PDF. The startup/shutdown parent and split starting page both preserve the same startup/shutdown PDF because the source export repeats it.

The startup and shutdown split pages contain embedded PNG diagrams and command screenshots. These are registered as `not_document_format` source artifacts. This topic covers the surrounding procedural meaning and exact identifiers without reconstructing image pixels.

The capacity-sizing source contains one source-level inconsistency in the disk DB index sizing text: it lists `Index Header Length` as `10 BYTES` in one table and later states that the header size for indexes is `16 bytes`. This document preserves both values and records the issue as an accepted source limitation for exact index-header sizing.

All R008 sources are classified as `Korean-source-verified` in `llm-reference/coverage/source-inventory.tsv`. R008 does not use English-only auxiliary source material.

R021 adds the `FAQE/Home/ALTIBASE HDB Administration/**` tree as `English-only source` auxiliary material. The R021 administration pages are useful SQL and procedure indexes outside Korean-core FAQ semantic verification. Answers that cite them must keep the `English-only source` label and should not describe the SQL catalog as Korean-source-verified. The SQL bodies remain in the source files; this consolidated topic indexes each answerable query family, the exact version split when present, and the key system views or commands required to locate the source query.

The R008 FAQ set has no URL-backed document-format attachments. It contains one downloadable support script, `altibased`, which is registered as `not_document_format`; one embedded `modify_column.png` image, also registered as `not_document_format`; and one legacy FAQ attachment label, `total_memory_tablespaces_usage.txt`, where the Korean source provides no downloadable URL. The legacy label is recorded as an accepted source limitation and no synthetic URL is introduced.

The R021 administration auxiliary pages contain no document-format attachments. Their risk is classification-based: they are English-only source indexes and have no Korean-source semantic audit.

## Scope and audience

Use this document to answer questions about Altibase server configuration, startup stages, shutdown modes, auto-start scripts, user and password management, DB security checks, session and lock handling, IPC client connection setup, character-set or database-name changes, JOB scheduler operation, operational capacity planning, OS diagnostic command collection, and UNIX memory behavior. It is written for DBAs, platform engineers, support engineers, and LLM answer generation systems that need exact property names, commands, SQL, paths, view names, version conditions, and support-evidence boundaries.

When answering in another language, keep product names, commands, SQL, system views, property names, paths, error messages, environment variables, function names, file names, and attachment URLs exactly as written.

## Key facts

Altibase server configuration is stored in `$ALTIBASE_HOME/conf/altibase.properties`. The configuration guide describes visible properties in that file and does not describe hidden properties. To see the currently applied value, query `V$PROPERTY` rather than relying only on the file, because some hidden values are not visible in the file.

The configuration guide is written for Altibase `7.1.0` and `7.3.0`. It points readers to the General Reference manual for detailed property definitions and recommends consulting Altibase engineers before applying general recommendations to a specific system.

In `altibase.properties`, the `?` placeholder means the path defined by `$ALTIBASE_HOME`.

Properties can be changed in the configuration file, with `ALTER SYSTEM`, or with `ALTER SESSION`, depending on the property. Runtime DCL changes are case-insensitive. If Altibase is restarted, DCL changes are reset to the values in `altibase.properties`, so permanent changes must be written to the configuration file. `ALTER SYSTEM` applies to subsequent sessions, not already connected sessions; use `ALTER SESSION` for a currently connected session.

Read-only or non-changeable property attempts can return:

```text
[ERR-0104E: The property [propery_name] is read-only.]
```

Properties that should be set at database creation include:

| Property | Default or source example | Operational meaning |
| --- | --- | --- |
| `DB_NAME` | `mydb` | User-defined database name. |
| `MEM_DB_DIR` | `?/dbs`; example `/home/altidata` | Directory for memory DB data files. |
| `DEFAULT_DISK_DB_DIR` | `?/dbs`; example `/home/altidata` | Directory for disk DB data files. |
| `LOGANCHOR_DIR` | `?/logs`; example `/home/altilog` | Directory for log anchor files. |
| `LOG_DIR` | `?/logs`; example `/home/altilog` | Directory for transaction log files. |
| `ARCHIVE_DIR` | `?/arch_logs`; example `/home/altibackup/arch_log` | Backup directory recommended when archive mode is used. |
| `MEM_MAX_DB_SIZE` | `2G`; source example `8G` | Maximum memory DB size predicted by capacity planning; the source generally recommends about 50% of physical memory. |
| `BUFFER_AREA_SIZE` | `128M` | Disk table buffer size. |
| `PORT_NO` | `20300` | Service port that must not conflict with another process. |
| `AUTO_COMMIT` | `1` | `1` commits after DML execution; `0` lets users control commits. Session setting takes precedence over `altibase.properties`. |
| `SQL_PLAN_CACHE` | `64M` | Maximum SQL plan cache size; useful when many duplicate SQL statements exist. |
| `REPLICATION_PORT_NO` | `0` | Replication port when replication is required. |

Properties that cannot be changed after DB creation must be chosen carefully. Changing them requires data migration and DB recreation.

| Property | Source note |
| --- | --- |
| `DB_NAME` | Specified when creating the database. |
| `LOG_FILE_SIZE` | `v7.1.0: 10M`; `v7.3.0: 100M`; specified when creating the database. |
| `EXPAND_CHUNK_PAGE_COUNT` | Default `128`; specified when creating the database. |
| `TRANSACTION_TABLE_SIZE` | Default `1024`; only upward adjustment is possible. |
| `CHARACTERSET` | Specified when creating the database. |
| `NATIONAL CHARACTERSET` | Specified when creating the database. |

The configuration guide recommends separating `LOG_DIR`, `MEM_DB_DIR`, `DEFAULT_DISK_DB_DIR`, and future user-created data files onto physical disks separated from the transaction log directory. The related disk I/O topic is covered in `llm-reference/02-architecture-storage-concepts.md`.

Session-related operational properties include:

| Property | Default | Operational meaning |
| --- | --- | --- |
| `MAX_CLIENT` | `1000` | Maximum concurrent DB sessions; increase and restart Altibase if more sessions are expected. |
| `MULTIPLEXING_THREAD_COUNT` | Number of logical cores on the host machine | Number of service threads. If omitted, threads are created during startup by CPU core count. The source recommends `(CPU Core Count * 2)` as a default starting point, then tuning by workload. |

Resource-limit properties are intended to limit heavy query work, bulk changes, transaction log growth, statement memory, and idle or stalled sessions. They should normally be changed only for sessions that need them.

| Property | Default | Source behavior |
| --- | --- | --- |
| `LOCK_ESCALATION_MEMORY_SIZE` | `100M` | For memory DB bulk changes, if changed-record size exceeds this value, a table lock is acquired. Can only be changed at system level. |
| `TRX_UPDATE_MAX_LOGSIZE` | `10M` | Returns an update-log-size error when transaction log generated by query processing exceeds the property. |
| `PREPARE_STMT_MEMORY_MAXIMUM` | `200M` | Returns a prepare-stage statement memory exceeded error. |
| `EXECUTE_STMT_MEMORY_MAXIMUM` | `v7.1.0: 1024M`; `v7.3.0: 2048M` | Returns an execute-stage statement memory exceeded error. |
| `QUERY_TIMEOUT` | `600 sec` | Returns `Client's query exceeded the execution time limit.` after the query execution time exceeds the value. |
| `FETCH_TIMEOUT` | `60 sec` | Terminates a session if result-set communication is absent for longer than the value; source message: `The session has been closed by the server`. |
| `UTRANS_TIMEOUT` | `3600 sec` | Terminates a session when a change query is not followed by commit or rollback within the value; source message: `The transaction has exceeded the lock timeout specified by the user.` |
| `IDLE_TIMEOUT` | `0` | Forcibly terminates an idle session after the configured interval; source message: `The session has been closed by the server.` |

Timeout and session-related errors are recorded in `altibase_boot.log`; find the relevant session there when investigating.

Disk I/O and disk-work-area properties include `BUFFER_AREA_SIZE`, `BUFFER_FLUSHER_CNT`, `PREPARE_LOG_FILE_COUNT`, `CHECKPOINT_BULK_WRITE_PAGE_COUNT`, `CHECKPOINT_BULK_WRITE_SLEEP_SEC`, `CHECKPOINT_BULK_WRITE_SLEEP_USEC`, `DIRECT_IO_ENABLED`, `DATABASE_IO_TYPE`, `TOTAL_WA_SIZE`, `SORT_AREA_SIZE`, and `HASH_AREA_SIZE`.

Problem Tracking properties include:

| Property | Default | Use |
| --- | --- | --- |
| `QP_MSGLOG_FLAG` | `2` | With value `2`, DDL execution records can be checked for problem analysis. |
| `RP_CONFLICT_MSGLOG_FLAG` | `0` | With value `6`, DML logs generated during replication conflicts are recorded. |
| `TIMED_STATISTICS` | `0` | Can be enabled in real time to record SQL execution time in `v$statement`. |

Altibase startup has four stages: `PROCESS`, `CONTROL`, `META`, and `SERVICE`. Use the `STARTUP` command after connecting to iSQL with `SYSDBA` privileges. Each stage can move forward to the next stage; returning to a previous stage is not supported. The source examples use Altibase `7.1.0`; output can differ by version.

The startup stage meanings are:

| Stage | Command | Main purpose | User operations allowed |
| --- | --- | --- | --- |
| `PROCESS` | `STARTUP PROCESS` | Initialize modules, load properties, validate license, create the process, initialize lock and main modules, and allow iSQL communication. DB space is not accessible. | `CREATE DATABASE`, `DROP DATABASE`, allowed property changes, fixed/performance view access, transition to `CONTROL`. |
| `CONTROL` | `STARTUP CONTROL` | Prepare managers to a level where DB recovery is possible. DDL and DML changes are prohibited. | Recovery statements, online log reset before `META` after incomplete recovery, archive-log-mode changes, extra performance views, transition to `META`. |
| `META` | `STARTUP META` | Check memory and disk tablespace data files and online log files, perform restart recovery when needed, rebuild transaction segment entries, start checkpoint thread, rebuild minimum SCN, run garbage and delete managers, rebuild memory indexes, refine memory tables. DDL and DML changes are prohibited. | All performance views, transition to `SERVICE`. |
| `SERVICE` | `STARTUP SERVICE` or `STARTUP` | Start normal database service, listeners, query/security/database link modules, meta DB checks, replication manager, and replication heartbeat manager. | iSQL connection and normal DB operation. |

Altibase writes startup details to `$ALTIBASE_HOME/trc/altibase_boot.log`.

Shutdown proceeds in reverse stage order, from `SERVICE` through `META`, `CONTROL`, and `PROCESS`, and terminates in one step. Connect to iSQL with `-sysdba` and run `SHUTDOWN`. `NORMAL` and `IMMEDIATE` can be executed only in `SERVICE`; `ABORT` can be executed at any stage. The shutdown command can be executed only by the OS account that installed Altibase.

| Shutdown option | Source behavior |
| --- | --- |
| `NORMAL` | Waits until all clients disconnect, then terminates communication-session detection, service threads, data storage manager, modules, and process. |
| `IMMEDIATE` | Forcibly disconnects sessions, rolls back currently running transactions, shuts down modules and process. `server stop` performs the same operation. During internal shutdown it releases resources, performs table compaction, flushes dirty pages, and checkpoints memory tablespace. Many dirty pages or checkpoint targets increase shutdown wait time. |
| `ABORT` | Sends `kill -9` to the server process and waits for termination. Database consistency cannot be guaranteed, so recovery runs when the server starts again. |

R008 operational FAQ facts:

| Area | Consolidated fact |
| --- | --- |
| Communication methods | Altibase supports `TCP/IP`, IPC using Unix Domain Socket, IPC using shared memory, `IPCDA` from ALTIBASE HDB `7.1.0`, and `SSL/TLS` from ALTIBASE HDB `6.5.1`. |
| IPC access | IPC is disabled by default because `IPC_CHANNEL_COUNT` defaults to `0`; related properties require an Altibase restart. |
| Windows IPC | `IPC_PORT_NO` is required on Windows because Windows does not support Unix Domain Socket files. |
| Unix/Linux IPC path | `IPC_FILEPATH` can be changed from ALTIBASE HDB `5.5.1.4.2`; version `4.3.9` defaults to `$ALTIBASE_HOME/trc/alti-ipc`, and later versions before `5.5.1.4.2` default to `$ALTIBASE_HOME/trc/cm-ipc`. |
| Disk table indexes | Indexes must be created in the same tablespace type as their table. A disk table index cannot be created in memory tablespace; the source error is `ERR-311EC`. |
| Public synonym | Dropping all `PUBLIC SYNONYM` objects does not affect Altibase server operation, but it is not recommended because common DUAL queries and procedures such as `PRINT` and `PRINTLN` can rely on them. |
| Floating point | `DOUBLE` and `FLOAT` use approximate values. iSQL and `iloader` can display or export truncated decimals, while a program using a double host variable can retrieve the normal double value. Use fixed-point `NUMERIC` when decimal precision must be preserved. |
| OS time | Changing OS time alone is reflected in `SYSDATE`; changing time zone or applying DST while Altibase is running can make OS time and `SYSDATE` differ until Altibase is restarted. |

`MEM_MAX_DB_SIZE` is the maximum combined memory-tablespace capacity for memory tables and memory data, not a per-tablespace limit. Memory-table index size is not included, but old record images generated by MVCC update transactions are included. If a memory table using `1G` is changed, the memory tablespace can require about `2G` until the transaction ends.

`MEM_MAX_DB_SIZE` should normally be set to about `60~70%` of physical memory. It can be set larger than physical memory, but then swap in/out can cause performance degradation and system problems. Memory checkpoint image files require twice the memory data usage on disk because two sets are stored for backup.

When reducing `MEM_MAX_DB_SIZE`, compare it with `TOTAL(M)` from `V$DATABASE`, where `TOTAL(M)` means total allocated memory tablespace pages and also the checkpoint image file size. `TOTAL` does not decrease except when `DROP TABLESPACE` is executed, and an Altibase restart does not reduce it.

`MAX_CLIENT` controls the maximum concurrent sessions and defaults to `1000`. It cannot be changed online; edit `$ALTIBASE_HOME/conf/altibase.properties` and restart Altibase. Increasing `MAX_CLIENT` does not by itself increase DB performance or resource usage, but actual increases in concurrent sessions and concurrent transactions can increase system resources.

`TRANSACTION_TABLE_SIZE` is the maximum number of concurrent transactions and also the transaction unique number table (`TID`) capacity. Because one session always has one transaction and because user, replication, and internal transactions are included, set it greater than `MAX_CLIENT`. In replication environments, it may need to be up to twice `MAX_CLIENT`, and it must match between replication peer servers or the Sender will not start.

`TRANSACTION_TABLE_SIZE` restrictions:

| Rule | Detail |
| --- | --- |
| Allowed values | Must be a `2^n` value greater than the current value: `16`, `32`, `64`, `128`, `256`, `512`, `1024`, `2048`, `4096`, `8192`, `16384`. |
| Direction | Cannot be changed from a larger value to a smaller value. |
| Online change | `ALTER SYSTEM` does not actually change it online; versions with `BUG-33467` return `[ERR-0104E: The property [TRANSACTION_TABLE_SIZE] is read-only.]`. |
| Offline change support | Supported without migration from `5.1.5.93`, `5.3.3.48`, `5.3.5.17`, and `5.5.1.1.0`; ALTIBASE HDB `4.3.9` and earlier ranges in the source require data migration. |
| Maximum value | `16384` from `4.3.9.222`, `5.1.5.112`, `5.3.3.91`, `5.3.5.35`, and `5.5.1.5.3`; earlier source ranges list `8192`. |

When `TRANSACTION_TABLE_SIZE` is exceeded, new sessions can fail to connect and connected sessions can stop responding to SQL. The source message in `altibase_boot.log` is `TRANSACTION_TABLE_SIZE is full !!`.

Account and password rules from the R008 FAQ set:

| Item | Rule |
| --- | --- |
| Default account | `sys` is created with password `manager`; if `CONNECT sys/manager` succeeds, change it after checking application dependencies. |
| Undeletable accounts | `SYS`, `SYSTEM_`, and `PUBLIC` are default accounts and cannot be deleted. |
| General user SQL | Use `CREATE USER user_name IDENTIFIED BY password;`, `ALTER USER user_name IDENTIFIED BY change_password;`, `DROP USER user_name;`, or `DROP USER user_name CASCADE;`. |
| SYS password | Change with `ALTER USER sys IDENTIFIED BY "new_password";`, run `altipasswd` online to update `$ALTIBASE_HOME/conf/syspassword`, then update `$ALTIBASE_HOME/bin/server`, `$ALTIBASE_HOME/bin/is`, and `$ALTIBASE_HOME/bin/il` if they embed the old password. |
| Password lockout | Login-failure lockout is available from `4.3.9.211`, `5.3.3.89`, `5.5.1.5.1`, `6.1.1.2.1`, `6.3.1`, and later versions. |
| Password complexity | Use a callback function through `PASSWORD_VERIFY_FUNCTION` in the `LIMIT` clause of `CREATE USER` or `ALTER USER`. |
| Password lifetime | Use `PASSWORD_LIFE_TIME` and `PASSWORD_GRACE_TIME`; values are in days and `0` means unset. |

Password length changed by version:

| Change | Applied versions and platform detail |
| --- | --- |
| No visible limit to 8-byte style limit | `4.3.9.200`, `5.1.5.98`, `5.3.3.62`, `5.3.5.25`, `5.5.1.2.10`, `6.1.1.0.0`; Windows and Solaris have `11byte`, other platforms have `8byte`. |
| 8 characters to 16 characters | `4.3.9.221`, `5.3.3.89`, `5.5.1.5.1`, `6.1.1.1.5`, `6.3.1`; Windows and Solaris have `22byte`, other platforms have `16byte`. |
| 16 characters to 40 characters | `6.5.1`, `7.1`, `7.3`; Windows has `40byte`. ALTIBASE HDB `5.1.5` and `5.3.5` do not reflect the password policy function and remain unchanged after the 8-digit change. |

Security checklist facts:

| Security area | Key source requirements |
| --- | --- |
| System privileges | Check `SYSTEM_.SYS_GRANT_SYSTEM_`, `SYSTEM_.SYS_USER_ROLES_`, and `SYSTEM_.SYS_PRIVILEGES_`; `ROLE` is supported from ALTIBASE HDB `6.5.1`; revoke unnecessary system privileges. |
| `WITH GRANT OPTION` | Object privileges granted with `WITH GRANT OPTION` can be abused outside DBA management; revoke and regrant without the option when necessary. |
| Convenience scripts | Set `$ALTIBASE_HOME/bin/il`, `$ALTIBASE_HOME/bin/is`, and `$ALTIBASE_HOME/bin/server` to permission `700` when required by audit policy. |
| Main property file | Set `$ALTIBASE_HOME/conf/altibase.properties` to `600` or `640`. |
| Log/data files | Set `$ALTIBASE_HOME/logs` and `$ALTIBASE_HOME/dbs` to `700` or `750`; set `loganchor*`, `logfile*`, and data files to `600` or `640`. |
| Trace files | Versions `6.3.1` and below create trace logs with default permission `666`; versions `6.5.1` and above create default `644` and can use `TRC_ACCESS_PERMISSION` with a restart. |
| Shell history | Do not pass iSQL username and password directly on the shell command line; protect `~/.*history` with permission `600`. |
| Service port | Default `PORT_NO` is `20300`; change it in `altibase.properties` and restart. |
| Idle sessions | `IDLE_TIMEOUT` can be changed per session; `ALTER SYSTEM` applies to newly connected sessions, and persistent change requires `altibase.properties`. |
| Auditing | Auditing is available from ALTIBASE HDB `6.3.1`; check `SYSTEM_.SYS_AUDIT_OPTS_` and `SYSTEM_.SYS_AUDIT_`. |
| Remote access | `ACCESS_LIST` is available from ALTIBASE HDB `5`; configure permit and deny rules in `altibase.properties` and restart. |
| SYSDBA remote access | `REMOTE_SYSDBA_ENABLE = 1` allows remote SYSDBA access and `0` blocks it; change with `ALTER SYSTEM` or persist in `altibase.properties`. |

JOB objects are available from Altibase `6.3.1` or later. A JOB runs a stored procedure through the task scheduler, not through a service thread. To run JOBs, set both `JOB_SCHEDULER_ENABLE` and `JOB_THREAD_COUNT` to `1` or higher. `JOB_SCHEDULER_ENABLE` can be changed with `ALTER SYSTEM`; `JOB_THREAD_COUNT` and `JOB_THREAD_QUEUE_SIZE` require an Altibase restart. If two or more JOBs can run simultaneously, set `JOB_THREAD_COUNT` at least to the number of concurrent JOBs to avoid delay.

From Altibase `6.5.1`, a JOB is disabled unless the `ENABLE` option is used in `CREATE JOB` or `ALTER JOB job_name SET ENABLE;` is executed. In Altibase `6.3.1`, a JOB is enabled immediately when created. Set the JOB interval longer than the execution time of the procedure executed by the JOB, or executions can be delayed.

Maximum capacity FAQ values:

| Object | Maximum |
| --- | --- |
| Identifier length | `40 bytes` |
| Tablespaces per database | `64 * 1,024` |
| Datafiles per tablespace | `1,023` |
| Datafile size | `32 gigabytes` on a 64-bit standard |
| Users per database | `2,147,483,638` |
| Tables per database | `2,097,151` |
| Indexes per table | `64` |
| Columns per table | `1,024` |
| Columns per index | `32` |
| Rows per table | Limited by available storage or `maxrows` |
| Partitions per partitioned table or index | `2,147,483,638` |
| Constraints per database | `2,147,483,638` |
| Replications per database | `32` in `6.1.1` or earlier; `REPLICATION_MAX_COUNT` in `6.3.1` or later |
| Tables per replication | `2147483647` |

## Procedures

### Inspect and change configuration properties

Query current applied properties:

```sql
SELECT name, value1 FROM v$property;
```

Inspect the configuration file:

```bash
cat $ALTIBASE_HOME/conf/altibase.properties
```

Use this syntax in `altibase.properties`:

```properties
PORT_NO = 20300
```

Use DCL for runtime changes when supported:

```sql
ALTER SYSTEM SET query_timeout = 30;
ALTER SESSION SET query_timeout = 30;
```

For selected resource-limit changes:

```sql
ALTER SESSION SET TRX_UPDATE_MAX_LOGSIZE = 20000000;
ALTER SYSTEM SET TRX_UPDATE_MAX_LOGSIZE = 10000000;
ALTER SESSION SET QUERY_TIMEOUT = 3600;
ALTER SESSION SET UTRANS_TIMEOUT = 60;
```

To enable SQL elapsed-time recording:

```sql
ALTER SYSTEM SET TIMED_STATISTICS = 1;
```

### Start Altibase by stage

Connect with SYSDBA privileges:

```bash
isql -sysdba
```

Use startup commands according to the required operation:

```sql
STARTUP PROCESS;
STARTUP CONTROL;
STARTUP META;
STARTUP SERVICE;
STARTUP;
```

Use `PROCESS` for database creation or drop operations. Use `CONTROL` for recovery, incomplete recovery follow-up, online log reset, and archive-log-mode changes. Use `META` when recovery and metadata checks are needed before client service. Use `SERVICE` or `STARTUP` to make the database available to normal users.

After incomplete recovery in `CONTROL`, reset online log files before transitioning to `META`; otherwise, online log files that were not reflected in recovery may cause startup problems. The source represents this as an image-based SQL example, so preserve the decision point and consult the source/manual for the exact syntax in a live runbook.

### Shut Altibase down

Connect with SYSDBA privileges from the OS account that installed Altibase:

```bash
isql -sysdba
```

Choose one shutdown mode:

```sql
SHUTDOWN NORMAL;
SHUTDOWN IMMEDIATE;
SHUTDOWN ABORT;
```

Use `NORMAL` when waiting for all sessions to disconnect is acceptable. Use `IMMEDIATE` or `server stop` when sessions must be disconnected and active transactions rolled back. Use `ABORT` only as a forced stop, because it is equivalent to `kill -9` and recovery is required on the next start.

### Estimate memory capacity

Estimate memory capacity from:

1. Memory database size.
2. Disk database buffer size.
3. Memory for query execution.

For memory tables, Altibase allocates 32KB pages, divides each page into slots by record length, and keeps memory-table data and indexes resident in memory. Check exact slot size and slots per page in `V$MEMTBL_INFO`.

Memory table sizing should use actual schema and expected record count:

| Component | Source formula or value |
| --- | --- |
| Record header | `32 BYTES` |
| Data size | `(record length + 32) * expected row count` |
| Memory index pointer | `8 BYTES` |
| Index size | `8 bytes * number of records * number of indexes` |
| Recommended data/index margin | Add `30%` to `50%` to the calculated memory DB capacity. |

To determine aligned record length after table creation, use:

```sql
SELECT CEIL(SUM(B.SIZE)/8)*8
  FROM SYSTEM_.SYS_TABLES_ A,SYSTEM_.SYS_COLUMNS_ B
 WHERE A.TABLE_ID = B.TABLE_ID
   AND A.TABLE_NAME = 'MEMORY_SIZE';
```

Altibase manages memory resources with 8-byte alignment. A 282-byte record should be estimated as 288 bytes.

For volatile tablespaces, include data in capacity estimation using the same criteria when actual data is present. Data in volatile tablespaces is lost when the Altibase server restarts.

For disk DB buffer size, the source does not provide a fixed formula. It recommends a buffer at least `10%` of the disk database size expected to be frequently accessed. Example: if frequently accessed disk DB data is `100 GB`, use at least `10 GB`.

Query execution memory includes:

| Area | Source guidance |
| --- | --- |
| `SQL_CACHE` and per-session plan memory | `SQL_CACHE` is shared and does not dynamically expand. If it cannot store all execution plans, plans are stored in per-session memory. |
| Temporary memory for operations | Needed for `GROUP BY`, aggregation, and intermediate results in memory DB; amount varies by query type, data size, and concurrency. |
| MVCC margin | Previous images of versioned data must be temporarily stored to support MVCC. |

The source gives typical margin formulas:

| Margin item | Formula |
| --- | --- |
| Query information memory area | `number of queries * 1 MB` |
| Temporary memory area for operations | `total memory tablespace capacity * 0.1` |
| Margin for MVCC | `total memory tablespace capacity * 0.35` |

The source example estimates total Altibase-only memory as:

```text
20 GB memory DB + 5 GB disk buffer + 1 GB query margin + 2 GB temporary memory + 6 GB MVCC margin = 34 GB
```

If user applications run on the same server, estimate their capacity separately.

### Estimate disk capacity

Estimate disk capacity from:

1. Memory checkpoint image files.
2. Transaction log file space.
3. Disk database data and index space.
4. Undo and temporary tablespace space.
5. Backup and archive log space.
6. Optional `iloader` text backup space.

Memory checkpoint image files require twice the memory DB size because two sets are created. Example:

```text
20 GB memory DB * 2 = 40 GB checkpoint image files
```

Online log files are physical transaction log files used for WAL recovery. They are automatically deleted when a checkpoint occurs, but may be retained when a replication Sender cannot send required logs or when a long-running large transaction remains open. The source recommends estimating log space from load tests; if testing is difficult, secure at least `50 GB`.

Disk DB capacity should be estimated by page. Disk DB page size is `8192 BYTES`. Source example:

| Item | Value |
| --- | --- |
| Page size | `8192 BYTES` |
| `PCTFREE 10%` applied | `8192 - (8192 * 0.1) = 7373 BYTES` |
| Fixed page header | `80 BYTES` |
| Fixed page footer | `16 BYTES` |
| Available page size | `7373 - 96 = 7277 BYTES` |
| Selected record length | `288 BYTES` |
| Records per page | `7277 / (288 + 34) = 22` |
| Estimated annual records | `1,000,000 records` |
| Final estimate | `1,000,000 / 22 * 8192 = 3551 MB` |

For records, the source lists `Length (1 BYTE) + Slot Directory (2 BYTES) + 34 BYTES`. If a column exceeds 250 bytes, it includes a 3-byte length header. For indexes, sum the key-column lengths as the record length. The source lists `Index Header Length` as `10 BYTES` in one table and later states that the header size for indexes is `16 bytes`; keep this source limitation in mind for exact index sizing.

After calculating all disk tables and indexes, sum them and apply a `30%` to `50%` margin. The source example uses:

```text
500 GB disk DB + 500 GB * 0.3 margin = 650 GB
```

For disk DB undo tablespace, estimate about `30%` of the largest table size if not planning for worst-case transactions. For disk DB temporary tablespace, also estimate about `30%` of the largest table size. A single transaction that updates a `1 TB` table can require `1 TB` of undo.

Backup planning in archive log mode requires a separate archive log file directory and backup space. Backup space should account for memory DB capacity, disk DB capacity, archive log generation during the backup cycle, backup type, and whether previous backups remain on disk until current backup completion.

The daily backup example uses:

| Item | Example |
| --- | --- |
| Memory DB | `20 GB` |
| Disk DB | `500 GB` |
| Daily online log file size | `200 GB` |
| Memory DB backup consideration | `20 GB`; checkpoint stores two files, but backup uses one stable file. |
| Disk DB backup consideration | `500 GB` for full backup policy. |
| Archive logs | Keep all archive logs generated during the backup cycle until the next backup. |
| Previous backup retained | Requires twice the backup space. |

The source disk-capacity calculation example totals:

```text
Memory DB data file: 20 * 2 = 40 GB
Disk DB data file: 500 GB
Online log file: 20 GB
Archive log file: 40 GB
Backup file: Memory DB + Disk DB + Archive log file = 560 GB
Total required space: 40 + 500 + 20 + 40 + (560 * 2) = 1720 GB
```

If using `iloader` to back up individual tables as text files, add delimiter capacity:

```text
delimiter size = 5 BYTES * number of records * number of columns
```

Example: a 10-column table with 1 million records needs `5 * 10 * 1,000,000 = 50 MB` additional delimiter space. If compressed backups are stored on disk, estimate the compressed storage according to the compression ratio.

### Collect OS problem-analysis evidence

Use common commands on all OS families:

```bash
netstat -in
vmstat 1 5
```

For `netstat -in`, increasing `RX-ERR`, `RX-DRP`, `RX-OVR`, `TX-ERR`, `TX-DRP`, or `TX-OVR` indicates packet or network problems that should be checked by the system administrator.

For `vmstat 1 5`, the source means 5 outputs at 1-second intervals. Watch:

| Field | Meaning |
| --- | --- |
| `procs r` | Number of threads waiting for CPU; a large value can indicate CPU bottleneck. |
| `memory free` | Free physical memory. |
| `swap si`, `swap so` | Increase means disk I/O between swap disk and memory. |
| `cpu us sy id wa st` | Observe trend changes. |

Linux CPU/thread evidence:

```bash
top -H
ps -LFm -p <process id>
pstack <process id>
ls -l /proc/<process id>/fd
```

`top -H` requires `procps` version `3.2.7` or later. In `ps -LFm`, `LWP` is the unique thread number and `C` is CPU usage. Interpret `pstack` output by thread and read each stack from bottom to top to understand what the high-CPU thread is doing. Linux file evidence can be gathered from `/proc/<process id>/fd` when `lsof` is not installed. Linux system logs are usually under `/var/log/`, commonly the `messages` file.

The Linux pstack example includes identifiers such as `mmtServiceThread::findReadyTask`, `mmtServiceThread::run`, `qmnSCAN::doItNext`, `qmnJOIN::doIt`, `qci::moveNextRecord`, `mmtServiceThread::executeTask_READY`, `smrLogMgr::writeLog`, `smrLogMgr::updateTransLSNInfo`, `smxTrans::setLstUndoNxtLSN`, and `iduPosixLock`. Preserve these identifiers when reporting stack evidence.

Solaris evidence:

```bash
prstat -L -p <process id> <refresh interval>
pstack -F <process pid> | c++filt
pfiles -F <process id>
vi /var/adm/messages
```

The Solaris source is based on Solaris `5.10`. `prstat -L -p 22951 1` means viewing the process at a 1-second refresh interval. Use `c++filt` when C/C++ function names are not displayed clearly; it is usually under a compiler executable directory such as `/opt/SUNWspro/bin/`. For system logs, check `/var/adm/messages.*`; the extension indicates the week, and current-week logs are in `messages`.

AIX evidence:

```bash
ps -mo THREAD -p <process id>
procstack <process id>
pfiles -n <process id>
errpt -a | more
```

Some commands may not be supported before AIX `5.1`. In `ps -mo THREAD`, the `CP` column shows thread CPU occupancy. Interpret `procstack` by `tid#` and read each stack from bottom to top. Use `pfiles -n` to check file names in use. `errpt -a` can show disk device errors, network device errors, and abnormal process termination.

HP-UX evidence:

```bash
glance
pstack <process id>
pfiles <process id>
vi /var/adm/syslog/syslog.log
```

HP systems are classified as PA-RISC or Itanium, and some commands may not be supported on PA-RISC. In `glance`, press `s` to enter a process ID and `G` to check CPU usage per thread for that process. Interpret `pstack` by `lwpid` and read bottom to top. The HP pstack example shows replication Sender activity through `rpxSender::sleepForNextConnect`, `rpxSender::attemptHandshake`, and `rpxSender::run`.

### Check UNIX memory behavior

Solaris reserves swap before allocating physical memory. When a process requests `10M`, Solaris first reserves `10M` in swap, then allocates physical memory when the process actually accesses the memory. If swap is insufficient, Solaris cannot run the process.

```bash
/usr/sbin/swap -s
pmap -F <process id>
```

Solaris uses free physical memory for file cache while free memory is greater than `lotsfree`, which is `1/64` of total memory. In Solaris `5.7` or earlier, an option had to be set so file cache could be selected first when free memory was needed. From Solaris `5.8` or later, file cache is included in free memory by default, so a separate setting like AIX or HP is not needed. If free memory stays below `lotsfree`, Solaris searches for unused pages; this appears in the `sr` field of `vmstat`. `fr` means freed memory pages, and if changed pages are written to disk, frequent disk I/O can degrade performance.

In Solaris `pmap`, the top entry is process memory, `[ heap ]` contains memory DB and related data, `anon` is the initial-access area for `MMAP_PRIVATE` pages, and entries with `ino` can be treated as redo log buffer areas loaded by `mmap`.

AIX classifies memory as:

| Classification | Meaning |
| --- | --- |
| `Persistent` | JFS file cache. |
| `Client` | CDROM, NFS, and JFS2 file cache. |
| `Computational` | Process stack, heap, and shared memory. |

Use:

```bash
svmon -G
svmon -P <process id>
ps v <process id>
```

`svmon` values are page units; one page is basically 4KB unless otherwise indicated. Watch `pgsp`: if it increases, memory is actually insufficient or computational memory was stolen and swapped, which can degrade Altibase performance. Compare `svmon` and `ps v`; the sum of `svmon` `inuse` should match the `ps` `SIZE`, but if page-out occurred, `ps` can be larger.

AIX file-cache tuning terms:

| Property | Meaning |
| --- | --- |
| `MAXPERM` | Maximum share of physical memory used for file cache, soft limit. |
| `MINPERM` | Minimum share of physical memory used for file cache. |
| `NUMPERM` | Actual file-cache occupation, checked with `vmtune` or `vmo`. |
| `MAXCLIENT` | Maximum share of file cache used by NFS, JFS2, and similar client file systems. |
| `stric_maxperm` | If `1`, maintains `MAXPERM`. |
| `lru_file_repage` | If `0`, steals on memory shortage are forced to occur only in file cache such as JFS2. |

For AIX `5.2ML04` or later, the source recommends setting several properties to reduce jitter caused by file-cache and computational-memory stealing.

HP-UX uses arena-based memory allocation for threaded programs. Example:

```bash
export _M_ARENA_OPT=16:8
```

This allocates memory with 16 arenas. If an arena memory pool becomes insufficient, it expands in units of `8*4096 bytes`. If the expansion unit is too large, memory can increase rapidly, so test extensively before setting this variable. The source default is `8:32`.

Use `glance` and `pmap` for HP memory checks. HP can adjust file cache similarly to AIX; the source generally recommends:

| Kernel property | Recommended source value |
| --- | --- |
| `dbc_min_pct` | `5%` |
| `dbc_max_pct` | `15%` |

Linux tries to use free memory as file cache. Starting with kernel `2.6`, file-cache use can be limited with `swappiness`.

```bash
cat /proc/sys/vm/swappiness
```

Configure with `sysctl`. The source states the default is `60(%)`. When physical memory use goes beyond the value set in `swappiness`, swapping starts because Linux tries to secure file cache below the set value. Although the source does not make a special Altibase recommendation, it records that MySQL and similar systems recommend setting this kernel value to `0`.

Linux arena notes from the source:

| Item | Source condition |
| --- | --- |
| RHEL arena feature | Added in Red Hat Enterprise Linux `6` to improve memory contention between threads in multi-threaded applications. |
| Default arena count | Number of CPU cores * `MALLOC_ARENA_TEST`. |
| `MALLOC_ARENA_TEST` default | `2` for 32-bit, `8` for 64-bit. |
| `MALLOC_ARENA_MAX` | Operates properly in `glibc2.10` or later. |

Linux process memory can be checked with `top` or `pmap`.

Do not assume that `VSZ` immediately decreases after `free()`. The operating system normally returns a process memory area to free memory only when the process ends. Even if a process explicitly calls `free()`, monitoring tools can still show the same `VSZ` because the memory manager keeps fragments in a reusable free-list to avoid high kernel cost.

### Configure IPC communication

Edit `$ALTIBASE_HOME/conf/altibase.properties` and set the required IPC properties. At minimum, set `IPC_CHANNEL_COUNT` to the number of IPC sessions to allow. Set `IPC_PORT_NO` on Windows. Set `IPC_FILEPATH` only on versions that support it.

```bash
cd $ALTIBASE_HOME/conf
vi altibase.properties
server restart
```

Verify the applied IPC properties:

```sql
SELECT NAME, MEMORY_VALUE1
  FROM X$PROPERTY
 WHERE NAME IN ('IPC_FILEPATH', 'IPC_CHANNEL_COUNT');
```

Test an iSQL IPC connection:

```bash
export ISQL_CONNECTION=IPC
is
```

The connection is successful when the prompt appears and the startup banner shows `ISQL_CONNECTION = IPC, SERVER = localhost`.

### Start, stop, validate, and forcibly stop Altibase

Use the simple scripts from the OS account where Altibase is installed:

```bash
server stop
server start
```

Or connect with SYSDBA and use SQL commands:

```bash
isql -sysdba
```

```sql
ALTER DATABASE mydb SHUTDOWN IMMEDIATE;
STARTUP;
```

The database name in `ALTER DATABASE mydb SHUTDOWN IMMEDIATE;` is the value of `DB_NAME` and can differ by installation. After startup, validate with these source checks:

```sql
SELECT COUNT(*) FROM V$SESSION;
SELECT REP_NAME, REP_GAP FROM V$REPGAP;
SELECT * FROM V$SYSSTAT WHERE NAME LIKE '%execute%count%';
SELECT TO_CHAR(SYSDATE, 'YYYY-MM-DD HH:MI:SS.SSSSSS') FROM DUAL;
```

`--- STARTUP Process SUCCESS ---`, TCP/UNIX/IPC listener messages, and `[RP] Initialization : [PASS]` indicate a normal startup in the source examples.

Use `server kill` only when the Altibase server is hung and normal stop methods cannot be used:

```bash
server kill
```

`server kill` is equivalent to `kill -9`. It is not recommended in normal operation because recovery runs at the next startup and can take a long time if undo or redo work is large.

### Register Altibase auto-start on Linux, Solaris, and HP-UX

On Red Hat family v7 or later, create `/usr/lib/systemd/system/altibased.service` with `Type=forking`, `User=altibase`, `Group=altibase`, `LimitNOFILE=1048576`, `LimitNPROC=infinity`, `TimeoutSec=0`, `KillMode=none`, `ExecStart=/etc/rc.d/init.d/altibase start`, and `ExecStop=/etc/rc.d/init.d/altibase stop`. Create `/etc/rc.d/init.d/altibase` to source the Altibase user environment and run `${ALTIBASE_HOME}/bin/server start` or `${ALTIBASE_HOME}/bin/server stop`.

```bash
chmod 755 altibased.service
chmod 755 /etc/rc.d/init.d/altibase
cd /etc/systemd/system/multi-user.target.wants
ln -s /usr/lib/systemd/system/altibased.service altibased.service
systemctl enable altibased.service
systemctl start altibased.service
systemctl stop altibased.service
systemctl status altibased.service
```

If SELinux is enabled, change the current mode to permissive according to OS policy. `setenforce 0` is temporary. For a persistent change, set `SELINUX=permissive` in `/etc/selinux/config` and restart the OS.

On Red Hat family v6 or earlier, create `/etc/init.d/altibased`, set `user=altibase`, log to `/var/log/${user}_altibased.log`, start only when `ps -ef | grep ${user} | grep 'altibase -p' | grep -v grep | wc -l` is not `1`, and stop only when it is `1`. Register with `chkconfig`.

```bash
chmod +x /etc/init.d/altibased
chkconfig --add altibased
ls -l /etc/rc.d/rc*.d/K*alti*
ls -l /etc/rc.d/rc*.d/S*alti*
```

The source links an existing downloadable sample script named `altibased`; it is registered as a support script, not a document-format attachment.

For Solaris, create `/etc/alti-conf.d/alti.conf` with `ALTIBASE_HOME`, `PATH`, `ALTIBASE_OWNER`, and `START_ALTIBASE=1`. Create `/etc/init.d/alti_start` to run `startup` through `${ALTIBASE_HOME}/bin/isql -s 127.0.0.1 -u sys -p manager -sysdba`, create `/etc/init.d/alti_stop` to run `shutdown immediate`, create `/etc/init.d/altibase` to dispatch `start` and `stop`, hard-link it as `/etc/rc3.d/S955altibase`, set permissions, and test as root:

```bash
cd /etc/rc3.d
ln /etc/init.d/altibase S955altibase
chmod 755 S955altibase
cd /etc/init.d
chmod 755 *alti*
/etc/init.d/altibase start
/etc/init.d/altibase stop
```

For HP-UX, create `/etc/rc.config.d/altibase_conf`, `/sbin/init.d/alti_start`, `/sbin/init.d/alti_stop`, and `/sbin/init.d/altibase`. The HP-UX stop script clears checkpoint bulk write sleep/count values with `ALTER SYSTEM SET CHECKPOINT_BULK_WRITE_PAGE_COUNT = 0`, `CHECKPOINT_BULK_WRITE_SLEEP_SEC = 0`, and `CHECKPOINT_BULK_WRITE_SLEEP_USEC = 0`, runs `killCheckServer > ${ALTIBASE_HOME}/trc/killCheckServer.log 2>&1`, then runs `shutdown immediate`. Create links in `/sbin/rc2.d`:

```bash
cd /sbin/rc2.d
ln -s /sbin/init.d/altibase S955altibase
ln -s /sbin/init.d/altibase K955altibase
chmod 755 S955altibase
chmod 755 K955altibase
cd /sbin/init.d
chmod 755 *alti*
/sbin/init.d/altibase
```

### Change DB_NAME or character set

`DB_NAME` and database character set are database-creation-time values. Back up required data before changing either one, because the procedure deletes and recreates the database.

To change `DB_NAME` in versions `5.3.3` or later:

1. Stop Altibase with `server stop`.
2. Change `DB_NAME` in `$ALTIBASE_HOME/conf/altibase.properties`.
3. Change the `create database mydb ...` section in `$ALTIBASE_HOME/bin/server` so it uses the same DB name.
4. Delete the existing database files under `$ALTIBASE_HOME/dbs/*` and `$ALTIBASE_HOME/logs/*`.
5. Recreate the DB, for example `server create MS949 UTF8`.
6. Start with `server start`.
7. Verify with `SELECT DB_NAME FROM V$DATABASE;`.

If `server create` fails with `Invalid Database Name. Check the properties and retry.` and `[ERR-91015 : Communication failure.]` after a DB name change, check whether `$ALTIBASE_HOME/bin/server` still uses `mydb`.

To change the database character set while preserving required data, use the source five-step export/recreate/import flow:

1. Set `ALTIBASE_NLS_USE` to the current DB character set and download the full schema with `aexport`.
2. Set `ALTIBASE_NLS_USE` to the current DB character set, split `run_il_out.sh` into `formout.sh` and `dataout.sh`, run `formout.sh`, verify `DATA_NLS_USE`, run `dataout.sh`, and verify the `.dat` file.
3. Stop Altibase, remove `$ALTIBASE_HOME/dbs/*` and `$ALTIBASE_HOME/logs/*`, set `ALTIBASE_NLS_USE` to the new character set, and run `server create <db_charset> <national_charset>`, such as `server create MS949 UTF16`.
4. Run `run_is.sh` to recreate schema.
5. Change `DATA_NLS_USE` in the `.fmt` file to the new character set, run `run_il_in.sh`, and verify `V$NLS_PARAMETERS` and sample table data.

The charset source intentionally includes Korean sample data. Preserve examples such as `US7ASII_한글테스트합니다`, `"한글 데이터입니다"`, and `C1 : US7ASII_한글테스트합니다 .` exactly when quoting the source.

### Move data, log, archive, log anchor, and double write files

To change disk tablespace data file paths or memory checkpoint image paths, secure service downtime and use this flow:

1. Check disk datafiles:

   ```sql
   SELECT T.NAME TBS_NAME, D.NAME DATAFILE
     FROM V$DATAFILES D, V$TABLESPACES T
    WHERE D.SPACEID = T.ID
    ORDER BY D.SPACEID, D.ID;
   ```

2. Check memory checkpoint paths in Altibase version `5` or later:

   ```sql
   SELECT TBS.NAME TBS_NAME,
          MEM_PATH.CHECKPOINT_PATH DATAFILE
     FROM V$TABLESPACES TBS,
          V$MEM_TABLESPACE_CHECKPOINT_PATHS MEM_PATH
    WHERE MEM_PATH.SPACE_ID = TBS.ID
    ORDER BY TBS_NAME, DATAFILE;
   ```

3. For Altibase version `4`, check memory DB directories with `grep MEM_DB_DIR $ALTIBASE_HOME/conf/altibase.properties | sort -u`.
4. Stop Altibase and verify the process is gone with `ps -ef | grep 'altibase -p' | grep -v grep`.
5. Change `MEM_DB_DIR` and `DEFAULT_DISK_DB_DIR` if the default paths should change.
6. Copy physical files with `cp -p`, compare file count and size with `ls -l | wc -l` and `du -sk`, and rename the original path as backup.
7. Start to `CONTROL` with `STARTUP CONTROL`.
8. For disk datafiles, run `ALTER DATABASE RENAME DATAFILE '/old_path/system001.dbf' TO '/new_path/system001.dbf';` for each file.
9. For memory checkpoint paths in version `5` or later, run `ALTER TABLESPACE memory_tablespace_name RENAME CHECKPOINT PATH '/old_path' TO '/new_path';` for each memory tablespace.
10. In Altibase version `4`, no DDL is required; change `MEM_DB_DIR` in `altibase.properties`.
11. Start to service with `startup`.

To change log anchor, online log, archive log, and double write paths, secure service downtime, check current values from `V$PROPERTY`, stop Altibase, copy files, edit properties, start Altibase, and recheck.

| File type | Property | File name format |
| --- | --- | --- |
| Log anchor | `LOGANCHOR_DIR` | `loganchor0`, `loganchor1`, `loganchor2` |
| Online log file | `LOG_DIR` | `logfile*#*` |
| Archive log file | `ARCHIVE_DIR` | `logfile*#*` |
| Double Write file | `DOUBLE_WRITE_DIRECTORY` | `*.dwf` |

### Respond when log disk is full

If the filesystem that contains DB files is full, general transactions are not affected immediately, but checkpoint cannot be performed and changes remain only in memory. If the filesystem that contains log files is full, transactions that modify the DB no longer execute and Altibase enters a waiting state; services except `SELECT` stop.

When log files are not deleted even though disk space should be sufficient:

1. Check replication gap with `SELECT * FROM V$REPGAP;`.
2. Check `ARCHIVE_FULL_ACTION` in `V$PROPERTY`. If it is `0`, archive backup stops after an error and does not resume automatically; checkpoint can delete unneeded logs even if archive backup has not resumed, so operate carefully. If it is `1`, the archive thread waits for enough archive space and log files are not deleted during that wait.
3. Check checkpoint success in `$ALTIBASE_HOME/trc/altibase_sm.log`.
4. Inspect `[CHECKPOINT-step9] Remove Online Log File`; `[None]` or `skip` can mean checkpoint succeeded but log files remain because of a long transaction or unsent replication data.

As an emergency countermeasure, move log files in `$ALTIBASE_HOME/logs` to a directory with enough space and create symbolic links back to the original log directory. Do not move log files currently in use; check them first:

```bash
lsof -p PID(ALTIBASE DB) | grep logfile
```

### Manage users, SYS password, and security settings

Create, change, or drop users with:

```sql
CREATE USER user_name IDENTIFIED BY password;
ALTER USER user_name IDENTIFIED BY change_password;
DROP USER user_name;
DROP USER user_name CASCADE;
```

To change the `SYS` password:

1. Connect as `SYS` and run `ALTER USER sys IDENTIFIED BY "new_password";`.
2. While Altibase is online, run `altipasswd` and enter the previous and new passwords.
3. Update embedded passwords in `$ALTIBASE_HOME/bin/server`, `$ALTIBASE_HOME/bin/is`, and `$ALTIBASE_HOME/bin/il`.

If startup fails with an invalid password after changing `SYS`, check the `server` script first. If the script is correct, `altipasswd` may not have been run.

For security checks, inventory users with `SELECT USER_NAME FROM SYSTEM_.SYS_USERS_;`, revoke unnecessary system privileges, remove risky `WITH GRANT OPTION` grants, harden file permissions, set password lockout and lifetime policies, configure `ACCESS_LIST`, and disable remote SYSDBA access when required.

### Resolve lock timeout and force-close locked sessions

For lock timeout errors, first inspect lock information:

```sql
SELECT T.TABLE_NAME, X.LOCK_DESC
  FROM SYSTEM_.SYS_TABLES_ T, V$LOCK X
 WHERE T.TABLE_OID = X.TABLE_OID
   AND T.TABLE_NAME = 'T1';
```

To identify and close sessions involved in locks:

```sql
SELECT A.TABLE_NAME, B.TRANS_ID, B.LOCK_DESC
  FROM SYSTEM_.SYS_TABLES_ A, V$LOCK B
 WHERE A.TABLE_OID = B.TABLE_OID;

SELECT SESSION_ID, EXECUTE_FLAG, TOTAL_TIME, EXECUTE_TIME, RPAD(QUERY,400)
  FROM V$STATEMENT
 WHERE TX_ID = trans_id;

SELECT COMM_NAME, CLIENT_APP_INFO
  FROM V$SESSION
 WHERE ID = session_id;

ALTER DATABASE mydb SESSION CLOSE session_id;
```

Use the actual `DB_NAME` from `$ALTIBASE_HOME/conf/altibase.properties` instead of `mydb`. Closing a target session does not affect other sessions, but closing the wrong production session can cause problems. A session currently rolling back is not disconnected by `SESSION CLOSE`; wait for rollback to finish. Applications can reconnect and reacquire locks, so disable the application if possible before operating.

### Create and monitor JOB objects

Enable the task scheduler before using JOB objects:

```bash
server stop
cd $ALTIBASE_HOME/conf
vi altibase.properties
server start
```

Set `JOB_SCHEDULER_ENABLE = 1` and `JOB_THREAD_COUNT = 1` or higher. Then verify:

```sql
SELECT NAME, MEMORY_VALUE1
  FROM X$PROPERTY
 WHERE NAME IN ('JOB_SCHEDULER_ENABLE', 'JOB_THREAD_COUNT');
```

Create and test the stored procedure before registering it in a JOB. Then create the JOB:

```sql
CREATE JOB job1
EXEC proc1
START sysdate
END sysdate + 3
INTERVAL 1 HOUR;
```

For Altibase `6.5.1` or later, enable the JOB:

```sql
ALTER JOB job_name SET ENABLE;
```

Or create it enabled:

```sql
CREATE JOB job1
EXEC proc1
START sysdate
END sysdate + 3
INTERVAL 1 HOUR
ENABLE;
```

Monitor JOB definitions and results in `SYSTEM_.SYS_JOBS_`. Check `JOB_NAME`, `IS_ENABLE`, `EXEC_QUERY`, `INTERVAL`, `INTERVAL_TYPE`, `STATE`, `EXEC_COUNT`, `ERROR_CODE`, `START_TIME`, `END_TIME`, and `LAST_EXEC_TIME`. If a JOB records an error code, use `altierr`, for example `altierr 0x31129`.

### Change columns and preserve numeric precision

From Altibase HDB `5.3.3`, use `ALTER TABLE table_name MODIFY COLUMN (column_name column_type(length))` to change a column type or length. Use `TOLERATE DATA LOSS` only when accepting possible data loss. `DATE` conversion follows `DEFAULT_DATE_FORMATE` as written in the source.

Do not reduce a column below the original size. Follow replication DDL procedures for replicated tables. For large target tables, expect operation delay and increased log-area usage. In version `5.3.3`, changing a memory table creates a restoration copy table in memory, so memory tablespace must have free space. In version `6.1.1`, the copy table is saved in disk tablespace, so required tablespace and disk space are enough. Altibase recommends backing up memory tables with `iloader`, creating a new target table, and importing data.

For precise decimal values, use fixed-point `NUMERIC(precision, scale)` instead of `DOUBLE` or `FLOAT`. The source example shows iSQL and `iloader` truncating display/export of `double'100.00000000000001421085471520200372'`, while `NUMERIC(35, 32)` preserves values when selected with `TO_CHAR`.

### Use R021 English-only administration SQL as an auxiliary catalog

The `ALTIBASE HDB Administration` SQL pages are English-only auxiliary material. Use them as source-indexed operational query families, not as Korean-source-verified FAQ rows.

| Source page | Indexed query families | Key objects and identifiers |
| --- | --- | --- |
| `How to terminate a session` | Connect as SYSDBA, find a target session, close it, and verify removal. Active transactions can delay session termination because Altibase rolls them back before closing. | `isql -SYSDBA`, `V$SESSION`, `ALTER DATABASE MYDB SESSION CLOSE [session identifier]` |
| `SQL about Sessions` | Total session count; session details for `ALTIBASE HDB 4` and `ALTIBASE HDB 5`; SYSDBA-connected session details for `ALTIBASE HDB 4` and `ALTIBASE HDB 5`. | `V$SESSION`, `V$STATEMENT`, `V$TRANSACTION`, `COMM_NAME`, `DB_USERNAME`, `SYSDBA_FLAG`, `AUTOCOMMIT_FLAG` |
| `SQL about Statements` | Total statement count; statement information; active statement count; currently running statements; long-running query over 10 seconds; long-running transaction last statement over 1 minute; queries running a full scan. | `V$STATEMENT`, `V$SESSION`, `V$TRANSACTION`, `V$PLANTEXT`, `EXECUTE_TIME`, `UTRANS_TIME`, `QUERY` |
| `SQL about Tablespaces` | Memory tablespace usage for `ALTIBASE HDB V4` and `ALTIBASE HDB V5`; total memory tablespace usage; disk tablespace usage for V4 and V5; datafile information; datafile I/O statistics for V4 and V5. | `V$TABLESPACES`, `V$MEMTBL_INFO`, `V$MEMSTAT`, `V$DATAFILES`, `X$DATAFILES`, `V$FILESTAT`, `MEM_MAX_DB_SIZE` |
| `SQL about Objects` | Memory table, queue table, memory/queue-table indexes, disk table, disk indexes, sequence, synonym, PSM, view, system privileges, object privileges, constraints, primary/foreign/unique constraints, index columns, and index information. Several queries have `ALTIBASE HDB V4` and `ALTIBASE HDB V5` variants. | `SYSTEM_.SYS_USERS_`, `SYSTEM_.SYS_TABLES_`, `SYSTEM_.SYS_COLUMNS_`, `SYSTEM_.SYS_INDICES_`, `SYSTEM_.SYS_SYNONYMS_`, `SYSTEM_.SYS_PROCEDURES_`, `SYSTEM_.SYS_VIEWS_`, `SYSTEM_.SYS_PRIVILEGES_`, `SYSTEM_.SYS_CONSTRAINTS_` |
| `SQL about Replication` | Sender state, Receiver state, replication gap, replication status, log buffer or file status occupied by unsent XLOG for `ALTIBASE HDB V4` and `ALTIBASE HDB V5`, and replication table list. | `V$REPSENDER`, `V$REPRECEIVER`, `V$REPGAP`, `V$LFG`, `SYSTEM_.SYS_REPLICATIONS_`, `SYSTEM_.SYS_REPL_HOSTS_`, `SYSTEM_.SYS_REPL_ITEMS_`, `XSN`, `APPLY_XSN`, `REP_GAP`, `RESTART_XSN` |
| `Miscellaneous queries` | Service thread state for HDB V4/V5; lock and transaction information for HDB V4/V5; redo log files; cumulative transaction waits caused by logging; Memory Ager gap; query blocking Ager from aging; memory status; total Altibase memory usage. | `V$SERVICE_THREAD`, `V$TRANSACTION`, `V$STATEMENT`, `SYSTEM_.SYS_USERS_`, `SYSTEM_.SYS_TABLES_`, `V$LFG`, `V$MEMGC`, `V$MEMSTAT`, `FIRST_UPDATE_TIME`, `LF_PREPARE_WAIT_COUNT`, `GC_NAME` |

## SQL, commands, and configuration

### Core SQL and DCL

```sql
SELECT name, value1 FROM v$property;
ALTER SYSTEM SET query_timeout = 30;
ALTER SESSION SET query_timeout = 30;
ALTER SESSION SET TRX_UPDATE_MAX_LOGSIZE = 20000000;
ALTER SYSTEM SET TRX_UPDATE_MAX_LOGSIZE = 10000000;
ALTER SESSION SET QUERY_TIMEOUT = 3600;
ALTER SESSION SET UTRANS_TIMEOUT = 60;
ALTER SYSTEM SET TIMED_STATISTICS = 1;
```

### Startup and shutdown commands

```bash
isql -sysdba
server stop
```

```sql
STARTUP PROCESS;
STARTUP CONTROL;
STARTUP META;
STARTUP SERVICE;
STARTUP;
SHUTDOWN NORMAL;
SHUTDOWN IMMEDIATE;
SHUTDOWN ABORT;
```

### Capacity SQL

```sql
SELECT CEIL(SUM(B.SIZE)/8)*8
  FROM SYSTEM_.SYS_TABLES_ A,SYSTEM_.SYS_COLUMNS_ B
 WHERE A.TABLE_ID = B.TABLE_ID
   AND A.TABLE_NAME = 'MEMORY_SIZE';
```

### R008 operational SQL and commands

```sql
SELECT NAME, MEMORY_VALUE1 FROM X$PROPERTY WHERE NAME IN ('IPC_FILEPATH', 'IPC_CHANNEL_COUNT');
SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME IN ('LOGANCHOR_DIR', 'LOG_DIR', 'DOUBLE_WRITE_DIRECTORY', 'ARCHIVE_DIR');
SELECT DB_NAME FROM V$DATABASE;
SELECT COUNT(*) FROM V$SESSION;
SELECT REP_NAME, REP_GAP FROM V$REPGAP;
SELECT * FROM V$SYSSTAT WHERE NAME LIKE '%execute%count%';
SELECT TO_CHAR(SYSDATE, 'YYYY-MM-DD HH:MI:SS.SSSSSS') FROM DUAL;
SELECT * FROM V$REPGAP;
SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME LIKE '%ARCHIVE_FULL_ACTION%';
SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME = 'MAX_CLIENT';
SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME = 'TRANSACTION_TABLE_SIZE';
SELECT TOTAL_COUNT, ACTIVE_COUNT FROM V$TRANSACTION_MGR;
```

```bash
export ISQL_CONNECTION=IPC
server start
server stop
server restart
server kill
server create MS949 UTF8
server create MS949 UTF16
altipasswd
chkconfig --add altibased
systemctl enable altibased.service
systemctl start altibased.service
systemctl stop altibased.service
sestatus
setenforce 0
setenforce 1
lsof -p PID(ALTIBASE DB) | grep logfile
```

### R021 auxiliary administration SQL locator

Use this index when an answer needs an auxiliary SQL query from the English-only Administration corpus. Cite the source path and preserve the `English-only source` label.

| Need | Source heading |
| --- | --- |
| Count or inspect sessions | `SQL about Sessions` -> `Total number of sessions`, `Session Information`, `Session information connected as SYSDBA` |
| Close a session | `How to terminate a session` -> `ALTER DATABASE MYDB SESSION CLOSE [session identifier]` |
| Count or inspect statements | `SQL about Statements` -> `Total number of statements`, `Statement information`, `Information about currently running statements` |
| Find long-running work | `SQL about Statements` -> `Long running query ( over 10 seconds)`, `Long running transaction's last statement information (over 1 minute)` |
| Find full scans | `SQL about Statements` -> `Information about a query running a FULL SCAN` |
| Check memory/disk tablespace usage | `SQL about Tablespaces` -> memory usage, total memory usage, disk usage, datafile information, I/O statistics |
| Inspect object metadata | `SQL about Objects` -> table, queue, index, sequence, synonym, PSM, view, privilege, constraint, and index-column headings |
| Inspect replication runtime state | `SQL about Replication` -> Sender, Receiver, gap, status, unsent XLOG, and table list |
| Inspect service thread, lock, logging, Ager, and memory diagnostics | `Miscellaneous queries` -> service thread state, lock and transaction information, redo log files, logging waits, Memory Ager gap, blocked aging query, memory status |

### User, security, session, and JOB SQL

```sql
SELECT USER_NAME FROM SYSTEM_.SYS_USERS_;
CONNECT sys/manager;
CREATE USER user_name IDENTIFIED BY password;
ALTER USER user_name IDENTIFIED BY change_password;
ALTER USER sys IDENTIFIED BY "new_password";
DROP USER user_name;
DROP USER user_name CASCADE;

SELECT A.USER_NAME GRANTEE,
       C.USER_NAME GRANTOR,
       REPLACE(D.PRIV_NAME, '_', ' ') PRIV_NAME
  FROM SYSTEM_.SYS_USERS_ A,
       SYSTEM_.SYS_GRANT_SYSTEM_ B,
       SYSTEM_.SYS_USERS_ C,
       SYSTEM_.SYS_PRIVILEGES_ D
 WHERE C.USER_NAME <> 'SYSTEM_'
   AND B.GRANTEE_ID = A.USER_ID
   AND B.GRANTOR_ID = C.USER_ID
   AND B.PRIV_ID = D.PRIV_ID;

REVOKE CREATE TABLE FROM USER1;
REVOKE CREATE TABLE FROM ROLE1;

ALTER SESSION SET IDLE_TIMEOUT = 60;
ALTER SYSTEM SET IDLE_TIMEOUT = 60;
ALTER SYSTEM SET REMOTE_SYSDBA_ENABLE = 0;

CREATE JOB job1
EXEC proc1
START sysdate
END sysdate + 3
INTERVAL 1 HOUR;

ALTER JOB job_name SET ENABLE;
```

### File movement SQL

```sql
SELECT T.NAME TBS_NAME, D.NAME DATAFILE
  FROM V$DATAFILES D, V$TABLESPACES T
 WHERE D.SPACEID = T.ID
 ORDER BY D.SPACEID, D.ID;

SELECT TBS.NAME TBS_NAME,
       MEM_PATH.CHECKPOINT_PATH DATAFILE
  FROM V$TABLESPACES TBS,
       V$MEM_TABLESPACE_CHECKPOINT_PATHS MEM_PATH
 WHERE MEM_PATH.SPACE_ID = TBS.ID
 ORDER BY TBS_NAME, DATAFILE;

ALTER DATABASE RENAME DATAFILE
'/old_path/system001.dbf' TO '/new_path/system001.dbf';

ALTER TABLESPACE SYS_TBS_MEM_DIC RENAME CHECKPOINT PATH
'/home/altibase_home/dbs_old_path' TO '/home1/altibase_home/dbs_new_path';
```

### Lock and session SQL

```sql
SELECT T.TABLE_NAME, X.LOCK_DESC
  FROM SYSTEM_.SYS_TABLES_ T, V$LOCK X
 WHERE T.TABLE_OID = X.TABLE_OID
   AND T.TABLE_NAME = 'T1';

SELECT A.TABLE_NAME, B.TRANS_ID, B.LOCK_DESC
  FROM SYSTEM_.SYS_TABLES_ A, V$LOCK B
 WHERE A.TABLE_OID = B.TABLE_OID;

SELECT SESSION_ID, EXECUTE_FLAG, TOTAL_TIME, EXECUTE_TIME, RPAD(QUERY,400)
  FROM V$STATEMENT
 WHERE TX_ID = trans_id;

SELECT COMM_NAME, CLIENT_APP_INFO
  FROM V$SESSION
 WHERE ID = session_id;

ALTER DATABASE mydb SESSION CLOSE session_id;
```

### OS utilities

```bash
netstat -in
vmstat 1 5
top -H
ps -LFm -p <process id>
pstack <process id>
ls -l /proc/<process id>/fd
prstat -L -p <process id> <refresh interval>
pstack -F <process pid> | c++filt
pfiles -F <process id>
ps -mo THREAD -p <process id>
procstack <process id>
pfiles -n <process id>
errpt -a | more
glance
pfiles <process id>
/usr/sbin/swap -s
pmap -F <process id>
svmon -G
svmon -P <process id>
ps v <process id>
cat /proc/sys/vm/swappiness
```

### Important paths and files

| Path or file | Meaning |
| --- | --- |
| `$ALTIBASE_HOME/conf/altibase.properties` | Main configuration file. |
| `$ALTIBASE_HOME/conf/syspassword` | File changed by `altipasswd` for SYS password use during shutdown stage. |
| `$ALTIBASE_HOME/trc/altibase_boot.log` | Startup and shutdown details; timeout and session-related errors. |
| `$ALTIBASE_HOME/trc/altibase_qp.log` | DDL execution trace used to check datafile-add history when `QP_MSGLOG_FLAG = 2`. |
| `$ALTIBASE_HOME/trc/altibase_sm.log` | Storage manager trace used to verify checkpoint execution and log-file deletion behavior. |
| `$ALTIBASE_HOME/trc/killCheckServer.log` | HP-UX auto-stop script output from `killCheckServer`. |
| `$ALTIBASE_HOME/bin/server` | Convenience server script; can embed SYS password and DB creation SQL. |
| `$ALTIBASE_HOME/bin/is` | Convenience iSQL script; can embed SYS password. |
| `$ALTIBASE_HOME/bin/il` | Convenience `iloader` script; can embed SYS password. |
| `$ALTIBASE_HOME/logs` | Default log anchor and online log directory in many source examples. |
| `$ALTIBASE_HOME/dbs` | Default data file, memory checkpoint image, and double write file directory in many source examples. |
| `/usr/lib/systemd/system/altibased.service` | Red Hat family v7 or later systemd service file for Altibase auto-start. |
| `/etc/rc.d/init.d/altibase` | Red Hat family v7 or later service script run by `altibased.service`. |
| `/etc/init.d/altibased` | Red Hat family v6 or earlier `chkconfig` script. |
| `/var/log/${user}_altibased.log` | Red Hat family v6 or earlier auto-start script log. |
| `/etc/alti-conf.d/alti.conf` | Solaris auto-start configuration file. |
| `/etc/init.d/alti_start`, `/etc/init.d/alti_stop`, `/etc/init.d/altibase` | Solaris auto-start and stop scripts. |
| `/etc/rc3.d/S955altibase` | Solaris run-level hard link for Altibase startup. |
| `/etc/rc.config.d/altibase_conf` | HP-UX auto-start configuration file. |
| `/sbin/init.d/alti_start`, `/sbin/init.d/alti_stop`, `/sbin/init.d/altibase` | HP-UX auto-start and stop scripts. |
| `/sbin/rc2.d/S955altibase`, `/sbin/rc2.d/K955altibase` | HP-UX run-level links for startup and shutdown. |
| `/proc/<process id>/fd` | Linux file descriptors and open files for the process. |
| `/var/log/messages` | Common Linux system log location. |
| `/var/adm/messages.*` | Solaris system log files. |
| `/var/adm/messages` | Current Solaris messages file. |
| `/var/adm/syslog/syslog.log` | HP-UX system log file. |
| `/opt/SUNWspro/bin/` | Example compiler executable directory where `c++filt` may be located. |

## Validation and troubleshooting

If a property query from `altibase.properties` does not match the effective runtime value, query `V$PROPERTY`; the configuration file can omit hidden property values.

If a DCL property change appears ineffective, check whether the property supports `ALTER SYSTEM` or `ALTER SESSION`, whether the current session also needs `ALTER SESSION`, and whether a restart reset the property to the file value.

If changing a property returns `[ERR-0104E: The property [propery_name] is read-only.]`, the property is read-only or not changeable in the current mode. For DB-creation-time properties, recreate and migrate the database rather than forcing a runtime change.

If startup fails or behaves unexpectedly, inspect `$ALTIBASE_HOME/trc/altibase_boot.log`. The startup source repeatedly uses this file to verify what internal operation occurred at each stage.

If duplicate Altibase process startup is suspected, check the PROCESS stage note: Altibase initializes a process lock file and acquires a lock through `$ALTIBASE_HOME/conf/altibase.properties` to prevent duplicate startup.

If recovery was performed incompletely in `CONTROL`, reset online log files before moving to `META`; otherwise, online logs not reflected by recovery can cause startup problems.

If `SHUTDOWN NORMAL` appears to hang, verify whether client sessions are still connected. `NORMAL` waits until every client disconnects.

If `SHUTDOWN IMMEDIATE` takes a long time, check whether many dirty pages must be flushed or many checkpoint targets exist. The source says wait time increases in those cases.

If online log files keep accumulating, check replication Sender status and long-running large-change transactions. Retention can occur when the Sender cannot send required logs or when a transaction remains open for a long time.

If `vmstat` shows increasing `si` or `so`, the system is issuing disk I/O between swap disk and memory. For Altibase, this can introduce severe response-time jitter and should trigger OS memory and file-cache review.

If a thread has high CPU, collect per-thread CPU information and stack output on the relevant OS, then match the high-CPU thread ID to the stack paragraph. Read the stack from bottom to top.

If system-level symptoms appear outside Altibase, collect OS logs at the failure time: Linux `/var/log/messages`, Solaris `/var/adm/messages.*`, AIX `errpt -a`, and HP-UX `/var/adm/syslog/syslog.log`.

If process memory appears not to return after `free()`, do not conclude from `VSZ` alone that memory is still logically in use. The UNIX memory source explains that OS memory managers often keep freed process memory in reusable fragments until process termination.

If IPC connection fails, verify that `IPC_CHANNEL_COUNT` is not `0`, that the server was restarted after property changes, and that the Unix Domain Socket file path is valid. On versions before `5.5.1.4.2`, use the documented default path because `IPC_FILEPATH` cannot be changed or checked separately.

If `server create` returns `Invalid Database Name. Check the properties and retry.` after a `DB_NAME` change, update the `create database mydb ...` line in `$ALTIBASE_HOME/bin/server` to match the new `DB_NAME` in `altibase.properties`.

If startup returns `[FAILURE] The size of the DB file(SYS_TBS_MEM_DATA-number-number) exceeds the size specified in the MEM_MAX_DB_SIZE property.`, set `MEM_MAX_DB_SIZE` larger than the checkpoint image file size.

If `TRANSACTION_TABLE_SIZE is full !!` appears in `altibase_boot.log`, increase `TRANSACTION_TABLE_SIZE` to a valid larger `2^n` value and consider whether `MAX_CLIENT`, replication transactions, or internal transactions increased concurrent transaction demand.

If replication Sender fails with `Transaction Table Size mismatch [1024:4096]`, set the same `TRANSACTION_TABLE_SIZE` on both replication target servers.

If lock timeout returns `The transaction exceeds lock timeout specified by user`, identify the lock holder through `V$LOCK`, `V$STATEMENT`, and `V$SESSION`, then close only the intended session with `ALTER DATABASE mydb SESSION CLOSE session_id;`. Closing the wrong session in production can cause application impact.

If the Altibase service is stopped with `server kill`, expect restart recovery at the next startup. Recovery can take a long time when many undo and redo transactions must be processed.

If changing file paths produces `The data file does not exist`, physically copy or move the data file first, then rerun the rename statement. If startup fails with `The data file 'XXXXXX' has an invalid header`, redo the physical file copy. If `CANNOT IDENTIFY DATAFILE` appears, return to `CONTROL` and run the DDL again with the correct path.

If startup fails with `Unable to invoke the create() function on [XXXXXX/dwfile0.dwf]`, recreate `dwfile0.dwf` and `dwfile1.dwf` with `touch`, or temporarily set `USE_DW_BUFFER = 0`, start Altibase, restore `USE_DW_BUFFER = 1` or remove the temporary setting, then start after correcting `DOUBLE_WRITE_DIRECTORY`.

If log files are not removed after checkpoint, check whether `[CHECKPOINT-step9] Remove Online Log File` ends in `[None]` or `skip`. This can indicate a long transaction or replication data that has not been sent.

If OS time and `SYSDATE` differ after a time zone or DST change, restart Altibase. When performing incomplete recovery using `UNTIL TIME` on a server with DST applied, account for the DST time difference.

If a JOB does not execute, verify `JOB_SCHEDULER_ENABLE`, `JOB_THREAD_COUNT`, whether the procedure runs normally outside the scheduler, and whether the JOB is enabled on Altibase `6.5.1` or later. Use `SYSTEM_.SYS_JOBS_` and `altierr` for error code interpretation.

If decimal precision appears truncated in iSQL or `iloader`, do not assume the stored value is necessarily exact or displayable as entered. Use fixed-point `NUMERIC` and `TO_CHAR` when exact decimal representation is required.

When using R021 English-only administration SQL, keep version labels such as `ALTIBASE HDB V4`, `ALTIBASE HDB V5`, and `ALTIBASE HDB 5` from the source heading. Do not normalize V4 and V5 query variants unless a coverage row explicitly points to a canonical duplicate.

## Version-specific notes

| Source area | Version condition |
| --- | --- |
| `arch/Home/Altibase Configuration File Guide__22642991.md` | Written based on Altibase `7.1.0` and `7.3.0`. |
| `LOG_FILE_SIZE` immutable property | `v7.1.0: 10M`; `v7.3.0: 100M`. |
| `EXECUTE_STMT_MEMORY_MAXIMUM` | `v7.1.0: 1024M`; `v7.3.0: 2048M`. |
| `arch/Home/Understanding the Altibase Start_Shut down Process__14909450.md` and split pages | Examples were performed in Altibase `7.1.0`; output can differ by version. |
| `arch/Home/System Data Capacity Estimation Guide for Altibase Operations__22643042.md` | Based on Altibase `7.1.0` or higher. |
| Solaris memory management | Solaris `5.7` or earlier required an option for selecting file cache first; Solaris `5.8` or later includes file cache in free memory by default. |
| OS utility guide Solaris section | Commands are based on Solaris `5.10`. |
| AIX utility guide | Some commands may not be supported before AIX `5.1`. |
| HP-UX utility guide | Command support can differ by PA-RISC and Itanium. |
| Linux memory management | Kernel `2.6` introduces a limit on file-cache usage; Red Hat Enterprise Linux `6` added arena behavior for multi-threaded memory contention; `MALLOC_ARENA_MAX` operates properly in `glibc2.10` or later. |
| IPCDA | Supported from ALTIBASE HDB `7.1.0`. |
| SSL/TLS communication | Supported from ALTIBASE HDB `6.5.1`. |
| `IPC_FILEPATH` | Changeable from ALTIBASE HDB `5.5.1.4.2`; earlier versions use fixed default socket file paths. |
| Linux auto-start FAQ | Splits procedures between Red Hat family v7 or later and v6 or earlier; applies to Altibase v4 or later. |
| Column modify | `ALTER TABLE ... MODIFY COLUMN ...` is supported from Altibase HDB `5.3.3`; memory-table copy behavior differs between `5.3.3` and `6.1.1`. |
| DB name change | FAQ method applies to ALTIBASE HDB `5.3.3` or later; versions `5.3.3` and earlier require manual DB creation. |
| Lock timeout and session close FAQs | Apply to ALTIBASE HDB version `4` or later. |
| `MEM_MAX_DB_SIZE` | Applies to all Altibase versions and requires server restart to change. |
| `TRANSACTION_TABLE_SIZE` offline change | `4.3.9` cannot change it without migration; it is changeable without migration from `5.1.5.93`, `5.3.3.48`, `5.3.5.17`, and `5.5.1.1.0`. |
| `TRANSACTION_TABLE_SIZE` maximum | `16384` from `4.3.9.222`, `5.1.5.112`, `5.3.3.91`, `5.3.5.35`, and `5.5.1.5.3`; earlier source ranges list `8192`. |
| `MAX_CLIENT` FAQ | Applies to all ALTIBASE HDB versions. |
| JOB objects | Supported from Altibase `6.3.1`; explicit enable/disable behavior is added in `6.5.1`. |
| Character set change | Applies to ALTIBASE HDB `5.3.1` or later, which supports multiple languages. |
| Security `ROLE` | Supported from ALTIBASE HDB `6.5.1`. |
| Trace permission property | `TRC_ACCESS_PERMISSION` can be used from ALTIBASE HDB `6.5.1`; versions `6.3.1` and below require OS `chmod` handling. |
| Auditing | Available from ALTIBASE HDB `6.3.1`. |
| `ACCESS_LIST` and `REMOTE_SYSDBA_ENABLE` | Remote access and SYSDBA remote-access controls are available from ALTIBASE HDB version `5`. |
| Password policy functions | Applied from `4.3.9.211`, `5.3.3.89`, `5.5.1.5.1`, `6.1.1.2.1`, `6.3.1`, `6.5.1`, `7.1`, and `7.3`. |
| `FAQE/Home/ALTIBASE HDB Administration/**` | English-only auxiliary FAQE material. Many SQL pages have explicit `ALTIBASE HDB V4` and `ALTIBASE HDB V5` query variants; keep those variants separate. |

## Related errors

The R007 source set includes error and message text rather than a large error-code catalog:

| Message or condition | Meaning and action |
| --- | --- |
| `[ERR-0104E: The property [propery_name] is read-only.]` | The property is read-only or cannot be changed in the attempted way. Use a supported mode or recreate/migrate if it is a DB-creation-time property. |
| `The update log size '10485873' is bigger than TRX_UPDATE_MAX_LOGSIZE '10485760'` | Query processing generated more transaction log than `TRX_UPDATE_MAX_LOGSIZE`. Adjust session/system limit only for sessions that need it. |
| `The memory size allocated for the statement has exceeded the maximum limit ( Name : Query_Prepare, Wanted Memory Size : 1073741832, Max size : 1073741824 )` | Prepare-stage statement memory exceeded `PREPARE_STMT_MEMORY_MAXIMUM`. |
| `The memory size allocated for the statement has exceeded the maximum limit ( Name : Query_Execute, Wanted Memory Size : 1073807360, Max size : 1073741824 )` | Execute-stage statement memory exceeded `EXECUTE_STMT_MEMORY_MAXIMUM`. |
| `Client's query exceeded the execution time limit.` | Query exceeded `QUERY_TIMEOUT`. |
| `The session has been closed by the server` | Source message for `FETCH_TIMEOUT` or `IDLE_TIMEOUT` closure. |
| `The transaction has exceeded the lock timeout specified by the user.` | Source message for `UTRANS_TIMEOUT` behavior. |
| `ERR-311EC : The type (memory/disk/volatile) of the tablespace in which to create the index is not the same as the type of the table.` | A disk-table index was attempted in memory tablespace or another mismatched tablespace type. Create the index in the same tablespace type as the table. |
| `ERR-91015 : Communication failure.` with `Invalid Database Name. Check the properties and retry.` | `server create` used a DB name that did not match the changed `DB_NAME`; update `$ALTIBASE_HOME/bin/server`. |
| `ERR-910FB : Connected to idle instance` | Appears in source startup/create examples before connecting to an idle instance; not by itself the root cause in those examples. |
| `[ERR-4107A : Unable to start up in the specified phase in the current state.]` | Starting an already running database fails; do not start another server for the same instance. |
| `[ERR-41041 : Another SYSDBA session is already running.]` | Only one SYSDBA session is allowed; end the existing SYSDBA session and retry. |
| `The transaction exceeds lock timeout specified by user` and `smERR_ABORT_smcExceedLockTimeWait` | Altibase could not lock the target object. Wait for commit/rollback or close the intended locking session. |
| `[ERR-6100D : [Sender] Failed to handshake with the peer server (Transaction Table Size mismatch [1024:4096])]` | Replication peers have different `TRANSACTION_TABLE_SIZE`; set the same value on both servers. |
| `TRANSACTION_TABLE_SIZE is full !!` | Concurrent transactions exceeded `TRANSACTION_TABLE_SIZE`; increase it to a valid larger `2^n` value after planning downtime or migration as required. |
| `ERR-10166(errno=2) TRANSACTION_TABLE_SIZE ['4094'] is not a power of two.` | `TRANSACTION_TABLE_SIZE` was set to a value that is not `2^n`. |
| `ERR-10018(errno=0) The version of data file for backup is not compatible with the version of storage manager... Transaction Table Size = 1024 ... Transaction Table Size = 2048` | Appears in versions where `TRANSACTION_TABLE_SIZE` cannot be changed after DB creation, or when changing from a large value to a small value. |
| `[FAILURE] The size of the DB file(SYS_TBS_MEM_DATA-0-2) exceeds the size specified in the MEM_MAX_DB_SIZE property.` | `MEM_MAX_DB_SIZE` is smaller than the checkpoint image file size; increase it. |
| `The data file does not exist` | Physical data file was not moved before the rename/path-change operation. |
| `The data file 'XXXXXX' has an invalid header` | Physical data file copy was not performed normally; redo the copy. |
| `Unable to invoke the create() function on [XXXXXX/dwfile0.dwf]` | Double write file is missing; create `dwfile0.dwf` and `dwfile1.dwf` or use the temporary `USE_DW_BUFFER = 0` procedure. |
| `CANNOT IDENTIFY DATAFILE` | The path stored in metadata is wrong or the physical data file is missing; correct the path in `CONTROL` stage. |
| `0x31129 (201001) qpERR_ABORT_QSV_NOT_EXIST_PROC_SQLTEXT Procedure or function not found : <0%s>.` | JOB execution can report this through `ERROR_CODE`; verify that the registered procedure or function exists. |

## Attachments and external references

Downloadable PDF attachments preserved from the R007 source set:

- `202312_Altibase_설정_파일_가이드.pdf`: https://docs.altibase.com/download/attachments/13437165/202312_Altibase_%EC%84%A4%EC%A0%95_%ED%8C%8C%EC%9D%BC_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=4&modificationDate=1702279114000&api=v2
- `201003_ALTIBASE_설정_파일_가이드.pdf`: https://docs.altibase.com/download/attachments/13437165/201003_ALTIBASE_%EC%84%A4%EC%A0%95_%ED%8C%8C%EC%9D%BC_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1701842255000&api=v2
- `ALTIBASE_STARTUP_STOP_과정의이해.pdf`: https://docs.altibase.com/download/attachments/13434993/ALTIBASE_STARTUP_STOP_%EA%B3%BC%EC%A0%95%EC%9D%98%EC%9D%B4%ED%95%B4.pdf?version=1&modificationDate=1697766276000&api=v2
- `ALTIBASE_운영을_위한_시스템_리소스_용량산정_가이드.pdf`: https://docs.altibase.com/download/attachments/14057887/ALTIBASE_%EC%9A%B4%EC%98%81%EC%9D%84_%EC%9C%84%ED%95%9C_%EC%8B%9C%EC%8A%A4%ED%85%9C_%EB%A6%AC%EC%86%8C%EC%8A%A4_%EC%9A%A9%EB%9F%89%EC%82%B0%EC%A0%95_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1698048077000&api=v2
- `ALTIBASE_문제분석을_위한_OS별_유틸리티_사용_가이드.pdf`: https://docs.altibase.com/download/attachments/13436866/ALTIBASE_%EB%AC%B8%EC%A0%9C%EB%B6%84%EC%84%9D%EC%9D%84_%EC%9C%84%ED%95%9C_OS%EB%B3%84_%EC%9C%A0%ED%8B%B8%EB%A6%AC%ED%8B%B0_%EC%82%AC%EC%9A%A9_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1698050117000&api=v2
- `UNIX_Memory_Management.pdf`: https://docs.altibase.com/download/attachments/13436842/UNIX_Memory_Management.pdf?version=1&modificationDate=1698104488000&api=v2

Embedded startup and shutdown images are registered in `llm-reference/coverage/attachment-diagram-register.tsv` as `not_document_format`. They include startup stage diagrams, startup command screenshots, `altibase_boot.log` screenshots, recovery/reset/archive-log-mode screenshots, shutdown mode screenshots, and shutdown log screenshots. Their surrounding procedural meaning is consolidated here.

R008 attachment and source-reference handling:

- `FAQE/Home/02. Operation and Management/[Linux] How to register Altibase server process auto start script__16875947.md` links a downloadable sample script named `altibased`: https://docs.altibase.com/download/attachments/12517478/altibased?version=1&modificationDate=1536132439000&api=v2. This is a support script without a document-format extension, so it is registered as `not_document_format`.
- `FAQE/Home/02. Operation and Management/How to modify column__16875952.md` embeds `modify_column.png`: https://docs.altibase.com/download/attachments/embedded-page/FAQE/How%20to%20modify%20column/modify_column.png?api=v2. The SQL syntax and cautions are covered in text; the embedded PNG is registered as `not_document_format`.
- `FAQE/Home/02. Operation and Management/What is MEM_MAX_DB_SIZE__16875991.md` references `total_memory_tablespaces_usage.txt` as a legacy FAQ attachment label with no downloadable URL in the Korean source. It is recorded as `legacy_no_downloadable_url`; no URL is invented.

External references preserved from the R007 source set:

- Altibase technical support portal: http://support.altibase.com/
- Altibase technical support portal for English pages: http://support.altibase.com/en/
- Altibase technical support center: `02-2082-1114`
- System Resource Capacity Planning Guide for Altibase: https://docs.altibase.com/x/n4HW
- Altibase Replication Configuration Guide: https://docs.altibase.com/x/AgDT
- General Reference manuals for Altibase 7.1 English: https://github.com/ALTIBASE/Documents/tree/master/Manuals/Altibase_7.1/eng
- Configuration Guide For Minimizing Disk I/O Contention: https://docs.altibase.com/x/6ICy
- Considerations when increasing concurrent sessions (`MAX_CLIENT`): https://docs.altibase.com/x/FARw

External references preserved from the R008 source set include:

- Red Hat SELinux states and modes documentation: https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/system_design_guide/changing-selinux-states-and-modes_system-design-guide#changing-selinux-states-and-modes_system-design-guide
- Altibase manuals on GitHub: https://github.com/ALTIBASE/Documents/tree/master/Manuals
- Altibase 7.1 English manuals: https://github.com/ALTIBASE/Documents/tree/master/Manuals/Altibase_7.1/eng
- Altibase English support manual page: http://support.altibase.com/en/manual
- Altibase English support portal: http://support.altibase.com/en/
- Altibase patch notes: http://support.altibase.com/en/patch-note
- `TRANSACTION_TABLE_SIZE` BUG-31862 reference from the source: http://nok.altibase.com/pages/viewpage.action?pageId=6851652
- `MEM_MAX_DB_SIZE` related error reference: https://aid.altibase.com/pages/viewpage.action?pageId=9110685
- `MEM_MAX_DB_SIZE` source video reference: https://youtu.be/tWAC4ghMO3c

R021 administration source URLs:

- `https://docs.altibase.com/display/FAQE/How+to+terminate+a+session`
- `https://docs.altibase.com/display/FAQE/Miscellaneous+queries`
- `https://docs.altibase.com/display/FAQE/SQL+about+Objects`
- `https://docs.altibase.com/display/FAQE/SQL+about+Replication`
- `https://docs.altibase.com/display/FAQE/SQL+about+Sessions`
- `https://docs.altibase.com/display/FAQE/SQL+about+Statements`
- `https://docs.altibase.com/display/FAQE/SQL+about+Tablespaces`

## Terminology

- `Altibase`, `ALTIBASE HDB`: Product names; keep exact capitalization from source titles and examples.
- `$ALTIBASE_HOME`: Environment variable for the Altibase installation home. In `altibase.properties`, `?` means this path.
- `altibase.properties`: Main server configuration file under `$ALTIBASE_HOME/conf/`.
- `V$PROPERTY`, `V$MEMTBL_INFO`, `SYSTEM_.SYS_TABLES_`, `SYSTEM_.SYS_COLUMNS_`, `v$statement`: Preserve exact SQL identifiers.
- `PROCESS`, `CONTROL`, `META`, `SERVICE`: Startup stages. Preserve as uppercase state names.
- `STARTUP PROCESS`, `STARTUP CONTROL`, `STARTUP META`, `STARTUP SERVICE`, `STARTUP`: Startup commands.
- `SHUTDOWN NORMAL`, `SHUTDOWN IMMEDIATE`, `SHUTDOWN ABORT`: Shutdown modes.
- `SYSDBA`, `isql -sysdba`, `server stop`: Preserve exact command and privilege notation.
- `SQL_CACHE`, `MVCC`, `PCTFREE`, `WAL`, `iloader`: Preserve exact technical names.
- `RX-ERR`, `RX-DRP`, `RX-OVR`, `TX-ERR`, `TX-DRP`, `TX-OVR`, `si`, `so`, `sr`, `fr`, `LWP`, `CP`, `tid#`, `lwpid`, `pgsp`, `VSZ`: OS diagnostic fields; do not translate identifiers.
- `MAXPERM`, `MINPERM`, `NUMPERM`, `MAXCLIENT`, `stric_maxperm`, `lru_file_repage`, `swappiness`, `_M_ARENA_OPT`, `MALLOC_ARENA_TEST`, `MALLOC_ARENA_MAX`: OS memory-management parameters and environment variables; preserve exact names.
- `IPC_PORT_NO`, `IPC_CHANNEL_COUNT`, `IPC_FILEPATH`, `IPCDA`, `ISQL_CONNECTION=IPC`: IPC communication identifiers; preserve exact capitalization.
- `MEM_MAX_DB_SIZE`, `MAX_CLIENT`, `TRANSACTION_TABLE_SIZE`, `TOTAL(M)`, `ALLOC(M)`, `USED(M)`, `USAGE(%)`: Capacity/session FAQ terms; do not translate identifiers.
- `SYS`, `SYSTEM_`, `PUBLIC`, `PUBLIC SYNONYM`, `PRIVATE SYNONYM`, `WITH GRANT OPTION`, `ROLE`: Account and privilege terms; keep exact SQL object names.
- `FAILED_LOGIN_ATTEMPTS`, `PASSWORD_LOCK_TIME`, `PASSWORD_VERIFY_FUNCTION`, `PASSWORD_LIFE_TIME`, `PASSWORD_GRACE_TIME`, `REMOTE_SYSDBA_ENABLE`, `ACCESS_LIST`, `TRC_ACCESS_PERMISSION`: Security properties and user policy identifiers.
- `JOB_SCHEDULER_ENABLE`, `JOB_THREAD_COUNT`, `JOB_THREAD_QUEUE_SIZE`, `SYSTEM_.SYS_JOBS_`, `ALTER JOB`, `CREATE JOB`, `DROP JOB`: JOB scheduler identifiers.
- `LOGANCHOR_DIR`, `LOG_DIR`, `ARCHIVE_DIR`, `DOUBLE_WRITE_DIRECTORY`, `USE_DW_BUFFER`, `dwfile0.dwf`, `dwfile1.dwf`: File movement and double write terms.
- `V$LOCK`, `V$STATEMENT`, `V$SESSION`, `SESSION CLOSE`, `LOCK TIMEOUT`: Lock/session troubleshooting identifiers.
- `ALTIBASE_NLS_USE`, `DATA_NLS_USE`, `V$NLS_PARAMETERS`, `NLS_USE`, `NLS_CHARACTERSET`, `NLS_NCHAR_CHARACTERSET`: Character-set migration identifiers.
- `US7ASII_한글테스트합니다`, `"한글 데이터입니다"`: Korean sample data from the charset procedure; preserve exactly when referencing source examples.
- `English-only source`, `english_only_auxiliary`: Coverage labels for R021 administration SQL sources; keep exact and do not translate.
- `ALTER DATABASE MYDB SESSION CLOSE [session identifier]`: Session-close syntax from the English-only administration source.
- `V$SERVICE_THREAD`, `V$LFG`, `V$MEMGC`, `V$FILESTAT`, `X$DATAFILES`, `V$REPSENDER`, `V$REPRECEIVER`, `V$REPGAP`, `SYSTEM_.SYS_REPL_HOSTS_`, `SYSTEM_.SYS_REPL_ITEMS_`: Additional R021 auxiliary SQL identifiers.
- `ALTIBASE HDB V4`, `ALTIBASE HDB V5`: Source version labels in R021 SQL pages; preserve when selecting a query variant.
