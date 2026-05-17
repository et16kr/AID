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

R008 will later add the FAQ operation, administration, security, session, charset, and JOB material to this same topic document. This R007 revision does not claim to cover R008 FAQ sources.

## Source coverage notes

This document covers the R007 portion of `llm-reference/03-operation-administration-security.md`: Altibase configuration properties, startup and shutdown stages, system memory and disk capacity sizing, OS-level problem-analysis utilities, and UNIX memory-management behavior.

All R007 source files are classified as `Link-validated Korean-source-verified` in `llm-reference/coverage/source-inventory.tsv`. The R007 source set uses only Korean-source-verified architecture pages. No English-only auxiliary source is used in this revision.

Six unique URL-backed PDF attachments from Korean source pages are preserved in the English source set and registered in `llm-reference/coverage/attachment-diagram-register.tsv`: two configuration-guide PDFs, one startup/shutdown PDF, one capacity-estimation PDF, one OS utility PDF, and one UNIX memory-management PDF. The startup/shutdown parent and split starting page both preserve the same startup/shutdown PDF because the source export repeats it.

The startup and shutdown split pages contain embedded PNG diagrams and command screenshots. These are registered as `not_document_format` source artifacts. This topic covers the surrounding procedural meaning and exact identifiers without reconstructing image pixels.

The capacity-sizing source contains one source-level inconsistency in the disk DB index sizing text: it lists `Index Header Length` as `10 BYTES` in one table and later states that the header size for indexes is `16 bytes`. This document preserves both values and records the issue as an accepted source limitation for exact index-header sizing.

## Scope and audience

Use this document to answer questions about Altibase server configuration, startup stages, shutdown modes, operational capacity planning, OS diagnostic command collection, and UNIX memory behavior. It is written for DBAs, platform engineers, support engineers, and LLM answer generation systems that need exact property names, commands, SQL, paths, view names, version conditions, and support-evidence boundaries.

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
| `$ALTIBASE_HOME/trc/altibase_boot.log` | Startup and shutdown details; timeout and session-related errors. |
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

## Attachments and external references

Downloadable PDF attachments preserved from the R007 source set:

- `202312_Altibase_설정_파일_가이드.pdf`: https://docs.altibase.com/download/attachments/13437165/202312_Altibase_%EC%84%A4%EC%A0%95_%ED%8C%8C%EC%9D%BC_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=4&modificationDate=1702279114000&api=v2
- `201003_ALTIBASE_설정_파일_가이드.pdf`: https://docs.altibase.com/download/attachments/13437165/201003_ALTIBASE_%EC%84%A4%EC%A0%95_%ED%8C%8C%EC%9D%BC_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1701842255000&api=v2
- `ALTIBASE_STARTUP_STOP_과정의이해.pdf`: https://docs.altibase.com/download/attachments/13434993/ALTIBASE_STARTUP_STOP_%EA%B3%BC%EC%A0%95%EC%9D%98%EC%9D%B4%ED%95%B4.pdf?version=1&modificationDate=1697766276000&api=v2
- `ALTIBASE_운영을_위한_시스템_리소스_용량산정_가이드.pdf`: https://docs.altibase.com/download/attachments/14057887/ALTIBASE_%EC%9A%B4%EC%98%81%EC%9D%84_%EC%9C%84%ED%95%9C_%EC%8B%9C%EC%8A%A4%ED%85%9C_%EB%A6%AC%EC%86%8C%EC%8A%A4_%EC%9A%A9%EB%9F%89%EC%82%B0%EC%A0%95_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1698048077000&api=v2
- `ALTIBASE_문제분석을_위한_OS별_유틸리티_사용_가이드.pdf`: https://docs.altibase.com/download/attachments/13436866/ALTIBASE_%EB%AC%B8%EC%A0%9C%EB%B6%84%EC%84%9D%EC%9D%84_%EC%9C%84%ED%95%9C_OS%EB%B3%84_%EC%9C%A0%ED%8B%B8%EB%A6%AC%ED%8B%B0_%EC%82%AC%EC%9A%A9_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1698050117000&api=v2
- `UNIX_Memory_Management.pdf`: https://docs.altibase.com/download/attachments/13436842/UNIX_Memory_Management.pdf?version=1&modificationDate=1698104488000&api=v2

Embedded startup and shutdown images are registered in `llm-reference/coverage/attachment-diagram-register.tsv` as `not_document_format`. They include startup stage diagrams, startup command screenshots, `altibase_boot.log` screenshots, recovery/reset/archive-log-mode screenshots, shutdown mode screenshots, and shutdown log screenshots. Their surrounding procedural meaning is consolidated here.

External references preserved from the R007 source set:

- Altibase technical support portal: http://support.altibase.com/
- Altibase technical support portal for English pages: http://support.altibase.com/en/
- Altibase technical support center: `02-2082-1114`
- System Resource Capacity Planning Guide for Altibase: https://docs.altibase.com/x/n4HW
- Altibase Replication Configuration Guide: https://docs.altibase.com/x/AgDT
- General Reference manuals for Altibase 7.1 English: https://github.com/ALTIBASE/Documents/tree/master/Manuals/Altibase_7.1/eng
- Configuration Guide For Minimizing Disk I/O Contention: https://docs.altibase.com/x/6ICy
- Considerations when increasing concurrent sessions (`MAX_CLIENT`): https://docs.altibase.com/x/FARw

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
