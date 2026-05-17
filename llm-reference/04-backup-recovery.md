# Backup, Recovery, and Failure Response

## Source paths

R009 source paths covered in this revision:

- `arch/Home/Considerations for Altibase Backup Policy__14647709.md`
- `arch/Home/Considerations for Altibase Backup Policy/1. Backup Types__14647714.md`
- `arch/Home/Considerations for Altibase Backup Policy/2. Considerations for Determining Backup Policy__14647722.md`
- `arch/Home/Considerations for Altibase Backup Policy/3. Summary (Considerations for Altibase Backup Policy)__14647728.md`
- `arch/Home/Responding to Failures Guide for Altibase__15138818.md`
- `arch/Home/Responding to Failures Guide for Altibase/1. Classification by type of failure__15138822.md`
- `arch/Home/Responding to Failures Guide for Altibase/2. Procedure by type of failure__15138835.md`
- `arch/Home/Responding to Failures Guide for Altibase/3. References__15138869.md`
- `FAQE/Home/04. Backup and Recovery/Using aexport and iloader__16876103.md`
- `FAQE/Home/04. Backup and Recovery/Using aexport and iloader/What is aexport, iloader__16876105.md`
- `FAQE/Home/04. Backup and Recovery/Using aexport and iloader/Database object backup using aexport__22642949.md`
- `FAQE/Home/04. Backup and Recovery/Using aexport and iloader/Data download using iloader__16876147.md`
- `FAQE/Home/04. Backup and Recovery/Using aexport and iloader/Create database object and upload data__16876145.md`
- `FAQE/Home/04. Backup and Recovery/How to recover cold backup by changing directory path__16876133.md`
- `FAQE/Home/04. Backup and Recovery/Online Backup and Time Based Recovery__16876135.md`

## Source coverage notes

This document covers the R009 topic: backup policy, logical backup with `aexport` and `iloader`, physical cold/offline backup, online backup, incremental backup concepts, archive-mode recovery, time-based incomplete recovery, cold-backup recovery with directory changes, and first-response failure handling.

The backup-policy architecture sources are classified as `Link-validated Korean-source-verified` in `llm-reference/coverage/source-inventory.tsv` because Phase 2 validated the Korean-source PDF attachment. The failure-response architecture sources and all `FAQE/Home/04. Backup and Recovery/**` sources are classified as `Korean-source-verified`.

No English-only auxiliary source is used in this R009 revision.

The backup policy source preserves one URL-backed PDF attachment. The failure-response source preserves two embedded PNG images: `replication.png` and `Reference.png`. These images are registered as `not_document_format`; this topic covers the surrounding procedural meaning without reconstructing image pixels. R009 has no legacy no-downloadable-URL attachment label.

Detailed replication setup, replication conflicts, and replication constraints are expanded by R010. This document includes only the failure-response checks from the R009 failure-response source: Sender/Receiver existence, `REP_GAP`, retained online log risk, trace log evidence, and conflict-log triage.

## Scope and audience

Use this document to answer operational questions from DBAs, support engineers, SREs, platform engineers, and LLM systems about selecting an Altibase backup method, executing backup and restore flows, validating export/import results, and responding to urgent service-impacting failures.

When answering in another language, keep product names, commands, SQL, system views, property names, paths, error codes, environment variables, script names, file names, and source URLs exactly as written.

## Key facts

Altibase backup methods fall into three source-defined groups:

| Backup group | Methods | Server status during backup | Server status during recovery | Database mode | Recovery point |
| --- | --- | --- | --- | --- | --- |
| Logical backup | `aexport`, `iloader` | Running | Running | Irrelevant | Backup point only |
| Physical backup | Online backup | Running | Started to `CONTROL` stage | Archive mode | Backup point, complete recovery, incomplete recovery |
| Physical backup | Offline backup or cold backup | Stopped | Backup files are started directly | Irrelevant | Backup point |
| Incremental backup | Level 0, level 1 differential, level 1 cumulative | Running | Started to `CONTROL` stage | Archive mode | Backup point, complete recovery, incomplete recovery |

Logical backup creates user-readable text files. `aexport` generates database object creation scripts and automation scripts. `iloader` downloads or uploads table data as text files.

`aexport` can extract these object categories: database user, user privilege, tablespace, table, table constraint, index, view, materialized view from `ALTIBASE HDB 6.3.1`, stored procedure, and replication object. Run `aexport` whenever database object definitions change.

`iloader` works by table. It can be used for migration or table-by-table backup. To use `iloader` for table data backup, use a form file and appropriate options. When `aexport` is run, it creates `iloader` command scripts.

Physical backup copies the files that compose the Altibase server, including data files and log anchor files, to a different physical location.

Online backup copies physical files while Altibase is running. It can target the entire database or a tablespace. It backs up one stable memory checkpoint image file. Disk temporary tablespace data files are not backed up.

Offline backup, also called cold backup in the FAQ, copies all database files while Altibase is stopped. Only whole-database backup is possible. Recovery time is usually the shortest because Altibase starts from the copied backup files, but startup still loads memory table data and rebuilds memory indexes.

Incremental backup is supported starting from Altibase `6.3.1`. It backs up only data pages changed since the previous incremental backup and requires the `Page Change Tracking` feature. Level 0 is the baseline, level 1 differential backs up pages changed since the latest level 0 or level 1 backup, and level 1 cumulative backs up pages changed since the latest level 0 backup.

Online backup and incremental backup require archive log mode and archive log file management. Complete recovery and incomplete recovery are possible only when the required online log files and archive log files are available.

Incomplete recovery has two source-defined forms:

| Form | Meaning |
| --- | --- |
| `UNTIL CANCEL` | Recover by specifying a log file. |
| `UNTIL TIME` | Recover by specifying a date and time. |

Online backup and incremental backup can prepare for physical file loss, including data files and log anchor files. Offline backup minimizes recovery time but cannot recover beyond the backup point.

Backup policy should be selected after choosing the backup target, then evaluating data importance, acceptable recovery point, backup size, recovery policy, backup cycle, backup time, backup-file retention period, and operating environment. This is not a DBA-only decision; the business owner or data owner must help define acceptable data loss and downtime.

Keep at least two backup copies. This mitigates bad backups, disk faults, and user faults affecting backup copies.

If backups are stored on disk, the backup destination should be physically separated from database data-file and log-file paths. During operation, disk I/O occurs for transaction log files, memory checkpoint image files, and disk-table data files. Backup I/O should not contend with those paths.

Backup execution takes longer as database size grows and can affect transactions. Schedule backups during the lowest-activity period.

Transaction impact differs by method:

| Backup method | Transaction impact |
| --- | --- |
| `aexport` | DDL cannot be performed temporarily. |
| `iloader` | Memory GC increases during backup. |
| Online backup | Online log files increase because checkpoints cannot run during backup. |
| Offline backup | Service downtime is required. |
| Incremental backup | Routine DB performance degradation can occur from `Page Change Tracking`; online log files increase because checkpoints cannot run during backup. |

Recovery time factors differ by method:

| Backup method | Factors affecting recovery time |
| --- | --- |
| `aexport` | Number of database objects if object creation is required. |
| `iloader` | Number of tables, table data volume, and number of indexes. |
| Online backup | Memory table usage, memory indexes, and number of log files to apply after backup. |
| Offline backup | Memory table usage and memory index rebuild. |
| Incremental backup | Memory table usage, memory indexes, and number of log files to apply after backup. |

Do not arbitrarily delete online log files. If online log files are deleted, the database can become unrecoverable.

## Procedures

### Prepare logical backup with aexport and iloader

Before using `aexport`, configure distinctive separators in `$ALTIBASE_HOME/conf/aexport.properties`. If the file does not exist, copy `aexport.properties.sample`.

```bash
cd $ALTIBASE_HOME/conf
ls -l aexport.properties*
cp -p aexport.properties.sample aexport.properties
```

The source defaults are simple and can collide with character data:

```text
#ILOADER_FIELD_TERM = ^
#ILOADER_ROW_TERM = %n
```

The FAQ recommends distinctive values unlikely to appear in data:

```text
ILOADER_FIELD_TERM = ^Cc__Cc^
ILOADER_ROW_TERM = ^Rr__Rr^%n
```

Run `aexport` after changing the properties. Enter `sys` as `UserID` to back up all objects, or enter a specific user to back up that user's objects. If `sys` is entered, `aexport` asks for passwords for all users created in the database. The password entered there is used in generated `CREATE USER ... IDENTIFIED BY ...` syntax; if it does not match during later `iloader` backup, `iloader` fails.

`aexport` creates `.sql` object scripts and `.sh` scripts on Unix/Linux, or `.bat` scripts on Windows. Depending on version and supported objects, the generated script count can vary. The source lists these scripts:

| Script | Purpose |
| --- | --- |
| `run_il_out.sh` | `iloader formout` and data-out script. |
| `run_is.sh` | `isql` table-schema script. |
| `run_il_in.sh` | `iloader` data-in script. |
| `run_is_refresh_mview.sh` | `isql` materialized view refresh script. |
| `run_is_index.sh` | `isql` table-index script. |
| `run_is_fk.sh` | `isql` table-foreign-key script. |
| `run_is_repl.sh` | `isql` replication script. |
| `run_is_job.sh` | `isql` job script. |

### Download table data with iloader

Before executing `iloader`, set and verify these environment variables in the same shell session or persist them in `.bash_profile` or `.profile`:

```bash
export ALTIBASE_NLS_USE=database_server_character_set
export ILO_DATEFORM='YYYY/MM/DD HH:MI:SS.SSSSSS'
echo $ALTIBASE_NLS_USE
echo $ILO_DATEFORM
```

`ALTIBASE_NLS_USE` prevents Korean character data corruption. `ILO_DATEFORM` prevents duplicate values when a `DATE` column has unique values.

For `ALTIBASE HDB` version 5 or later, check server and client character set values with:

```sql
set linesize 1024;
set colsize 20;
select NLS_USE, NLS_CHARACTERSET from v$nls_parameters;
```

`NLS_CHARACTERSET` is the Altibase server character set. `NLS_USE` is the client character set. Character data is preserved only when these values are identical.

Run all-table data download with the `run_il_out.sh` generated by `aexport` as `sys`:

```bash
sh run_il_out.sh | tee download.out
nohup sh run_il_out.sh &
mv nohup.out download.out
```

Use foreground execution only when terminal closure is not a risk. Use `nohup` for long downloads so the operation continues after disconnect.

To download tables for a single user from a `sys`-generated script, extract only that user's `iloader` commands:

```bash
grep "\-f ALTITEST_" run_il_out.sh > altitest_il_out.sh
sh altitest_il_out.sh | tee download.out
nohup sh altitest_il_out.sh &
mv nohup.out download.out
```

To download one table, extract its `formout` and `out` commands and execute them in order:

```bash
grep 'SYS_ORDERS.fmt' run_il_out.sh
iloader -s localhost -u SYS -p MANAGER formout -f SYS_ORDERS.fmt -T ORDERS
iloader -s localhost -u SYS -p MANAGER out -f SYS_ORDERS.fmt -d SYS_ORDERS.dat -log SYS_ORDERS.log
```

For large backups, monitor the run log:

```bash
tail -f download.out
```

### Validate iloader download results

Check the `run_il_out.sh` execution log:

```bash
grep -i err- download.out
```

If output begins with `ERR-`, such as `ERR-311F4 : Invalid column name`, treat it as a failed table or command and resolve the cause before trusting the backup.

Check table-level logs. `run_il_out.sh` creates `DBUSER_TABLENAME.log`, such as `ALTITEST_ORDERS.log`.

```bash
cat run_il_out.sh | grep fmt | wc -l
ls -l *.fmt | wc -l
cat *.log | grep 'Error Row Count' | awk -F: '{print $2}' | wc -l
cat *.log | grep 'Error Row Count' | awk -F: '{print $2}' | sort -u
```

The count of `Error Row Count` rows should match the table/form-file count. If the sorted unique result is only `0`, no table download failure is recorded in the per-table logs. If a non-zero value appears, inspect the corresponding `.log` and `.bad` files.

Data files are created as `USERNAME_TABLENAME.dat`. A table normally has `.dat`, `.fmt`, and `.log` files:

```bash
ls -l *.dat
ls -l *.dat | wc -l
ls -l ALTITEST_ORDERS*
```

### Restore logical backup objects and data

To restore all database objects and data from `aexport` and `iloader` output, execute scripts 2 through 8 in the source order. `run_il_out.sh` is a backup script and is excluded from restore execution.

```text
1. run_il_out.sh            : iloader formout, data-out script
2. run_is.sh                : isql table-schema script
3. run_il_in.sh             : iloader data-in script
4. run_is_refresh_mview.sh  : isql materialized view refresh script
5. run_is_index.sh          : isql table-index script
6. run_is_fk.sh             : isql table-foreign-key script
7. run_is_repl.sh           : isql replication script
8. run_is_job.sh            : isql job script
```

`run_is.sh` contains `isql` commands that execute `.sql` object-creation files. Source examples include:

```bash
isql -s localhost -u SYS -p MANAGER -f ALL_CRT_TBS.sql
isql -s localhost -u SYS -p MANAGER -f ALL_CRT_USER.sql
isql -s localhost -u SYS -p MANAGER -f ALL_CRT_SYN.sql
isql -s localhost -u SYS -p MANAGER -f ALL_CRT_DIR.sql
isql -s localhost -u SYS -p MANAGER -f ALL_CRT_TBL.sql
isql -s localhost -u SYS -p MANAGER -f ALL_CRT_SEQ.sql
isql -s localhost -u SYS -p MANAGER -f ALL_CRT_LIB.sql
isql -s localhost -u SYS -p MANAGER -f ALL_CRT_VIEW_PROC.sql
isql -s localhost -u SYS -p MANAGER -f ALL_CRT_LINK.sql
```

Leave a log every time a `.sh` file is executed:

```bash
sh run_is.sh | tee run_is.log
nohup sh run_is.sh &
mv nohup.out run_is.log
```

Data upload uses `run_il_in.sh`. To upload only a specific user's tables:

```bash
grep "\-f ALTITEST_" run_il_in.sh > altitest_il_in.sh
sh altitest_il_in.sh | tee upload.out
nohup sh altitest_il_in.sh &
mv nohup.out upload.out
```

To upload only the `SYS.ORDERS` table:

```bash
grep 'SYS_ORDERS.fmt' run_il_in.sh
iloader -s localhost -u SYS -p MANAGER in -f SYS_ORDERS.fmt -d SYS_ORDERS.dat -log SYS_ORDERS.log -bad SYS_ORDERS.bad
```

Monitor upload progress:

```bash
tail -f upload.out
```

Validate object and data restore logs:

```bash
grep -i err- run_is.log
grep -i err- upload.out
ls -l *.fmt | wc -l
ls -l *.log | wc -l
cat *.log | grep 'Error Row Count' | awk -F: '{print $2}' | wc -l
cat *.log | grep 'Error Row Count' | awk -F: '{print $2}' | sort -u
```

The final sorted unique `Error Row Count` result should be `0`.

### Perform online backup

Online backup is possible only when the database is in archive log mode. Check archive mode:

```sql
select ARCHIVE_MODE from v$archive;
```

`ARCHIVE_MODE` value `0` means archive mode is not used. Value `1` means archive mode is used.

Archive mode cannot be changed while the database is online. Stop the DB, connect in `sysdba` mode, start to `CONTROL`, and change archive mode:

```sql
startup control;
alter database archivelog;
```

Back up the entire database while running in archive mode:

```sql
alter database backup database to '/backup';
```

The source lists copied files such as:

```text
SYS_TBS_MEM_DIC-0-0
SYS_TBS_MEM_DATA-0-0
system001.dbf
system002.dbf
undo001.dbf
loganchor0
loganchor1
loganchor2
```

Back up a specific tablespace:

```sql
alter database backup tablespace SYS_TBS_MEM_DIC to '/backup_dir';
```

Back up all log anchor files:

```sql
alter database backup loganchor to '/backup_dir';
```

DBA-managed online backup by tablespace uses `begin backup`, a physical copy, and `end backup`. For memory tablespaces, verify the stable data file first:

```sql
alter tablespace USER_MEMORY_TBS begin backup;
select * from v$stable_mem_datafiles;
```

Copy the stable memory data file:

```bash
cp $ALTIBASE_HOME/dbs/USER_MEMORY_TBS-0-0 /backup_dir/
```

End memory backup, then back up a disk tablespace:

```sql
alter tablespace USER_MEMORY_TBS end backup;
alter tablespace USER_DISK_TBS begin backup;
```

Copy the disk data file and end backup:

```bash
cp $ALTIBASE_HOME/dbs/USER_DISK_TBS.dbf /backup_dir/
```

```sql
alter tablespace USER_DISK_TBS end backup;
```

After DBA-managed online backup, force archive processing for the current log file. This closes the current log file even if it is not full and continues logging to the next file:

```sql
ALTER SYSTEM SWITCH LOGFILE;
```

### Recover cold backup after changing directory paths

This FAQ applies to `ALTIBASE HDB` version 4 or later.

If no directory path changes are needed, copy cold-backup files to the matching directories and start the DB. The source file groups are `mydb*` for memory DB files, `*.dbf` for disk DB files, `logs`, and `loganchor`.

If directory names must change, change paths for memory DB files, logs, and log anchor files in `$ALTIBASE_HOME/conf/altibase.properties`; copy files into the changed directories; then rename disk DB data files in `CONTROL`.

Create the target directories and copy cold-backup files with OS copy commands. Edit properties such as:

```text
MEM_DB_DIR          = /home/cheol2/altibase_home/dbs
DEFAULT_DISK_DB_DIR = /home/cheol2/altibase_home/dbs
LOGANCHOR_DIR       = /home/cheol2/altibase_home/logs
LOGANCHOR_DIR       = /home/cheol2/altibase_home/logs
LOGANCHOR_DIR       = /home/cheol2/altibase_home/logs
LOG_DIR             = /home/cheol2/altibase_home/logs
ARCHIVE_DIR         = /home/cheol2/altibase_home/logs
```

Start to `CONTROL`:

```sql
startup control;
```

Rename each disk data file from the old path to the new path:

```sql
alter database rename datafile '/home/cheol2/altibase_home/dbs2/system001.dbf' to '/home/cheol2/altibase_home/dbs/system001.dbf';
alter database rename datafile '/home/cheol2/altibase_home/dbs2/system002.dbf' to '/home/cheol2/altibase_home/dbs/system002.dbf';
alter database rename datafile '/home/cheol2/altibase_home/dbs2/temp001.dbf' to '/home/cheol2/altibase_home/dbs/temp001.dbf';
alter database rename datafile '/home/cheol2/altibase_home/dbs2/undo001.dbf' to '/home/cheol2/altibase_home/dbs/undo001.dbf';
```

Move to service:

```sql
startup service;
```

Successful startup output transitions through `PROCESS`, `CONTROL`, `META`, and `SERVICE`, initializes listeners, shows `[RP] Initialization : [PASS]`, and ends with `STARTUP Process SUCCESS`.

### Perform time-based incomplete recovery

Time-based recovery applies when the DB operates in archive log mode and at least one full online backup or cold backup exists before the desired recovery time.

In the source scenario, `USER_DISK_TBS` was dropped accidentally at `2015-07-23 14:11`, and the target recovery time is `2015-07-23 14:01:00`.

First, the source assumes a full DB backup exists:

```sql
ALTER DATABASE BACKUP DATABASE TO '/backup_dir';
```

Copy backed-up disk tablespace data files and memory checkpoint files to the original data-file locations:

```bash
cp /backup_dir/*.dbf $ALTIBASE_HOME/dbs
cp /backup_dir/SYS_TBS_* $ALTIBASE_HOME/dbs
```

Check the archive log files required for recovery:

```sql
select last_deleted_logfile from v$lfg;
```

Check `$ALTIBASE_HOME/trc/altibase_sm.log` for the log file forcibly archived when backup completed. In the source example, the message `Waiting logfile15341 to archive` means the recovery requires `logfile15021` through `logfile15341`.

Copy backed-up log anchor files:

```bash
cp /backup_dir/loganchor* /ALTIBASE_HOME/logs
```

Because `SYS_TBS_DISK_TEMP` is not backed up, recreate its data file:

```sql
ALTER DATABASE CREATE DATAFILE 'temp001.dbf';
```

Run incomplete media recovery until the target time:

```sql
ALTER DATABASE RECOVER DATABASE UNTIL TIME '2015-07-23:14:01:00';
```

Because incomplete recovery was performed, use `RESETLOGS` while moving to `META`:

```sql
ALTER DATABASE mydb META RESETLOGS;
```

Start service and immediately take a new full backup because the server has started and logs have been reset:

```sql
ALTER DATABASE mydb SERVICE;
ALTER DATABASE BACKUP DATABASE TO '/backup_dir';
```

### Respond to urgent service-impacting failures

The failure-response source classifies failures as urgent or non-urgent. Urgent failure means a system or Altibase product problem prevents service from continuing. Non-urgent failure means service is running but may cause problems; users perform first response using guides and request technical support as needed.

For urgent failures, gather and provide:

| Evidence | Acquisition |
| --- | --- |
| System log | Use the failure-response section for system problems and OS-specific logs. |
| Altibase trace log | All files under `$ALTIBASE_HOME/trc`. |
| Failure-time specification | Abnormal signs and DB operation history at the failure time. |

Check `$ALTIBASE_HOME`:

```bash
echo $ALTIBASE_HOME
```

Check whether the Altibase process exists:

```bash
ps -ef | grep "altibase -p boot from" | grep -v grep
```

If the process exists, test a local connection:

```bash
isql -u sys -p manager -s 127.0.0.1 -port 20300
```

If the process is absent or connection is unavailable, collect logs and request support through `http://support.altibase.com/en/`, then contact Altibase Technical Support at `02-2082-1114`.

If Altibase must be restarted, use the OS account that installed Altibase:

```bash
server kill
server start
```

If the earlier check already confirms that Altibase has shut down, `server kill` is unnecessary. `server kill` forcibly shuts down Altibase; recovery runs at next startup if needed.

## SQL, commands, and configuration

### Backup and recovery SQL

```sql
select ARCHIVE_MODE from v$archive;
startup control;
alter database archivelog;
alter database backup database to '/backup';
alter database backup tablespace SYS_TBS_MEM_DIC to '/backup_dir';
alter database backup loganchor to '/backup_dir';
alter tablespace USER_MEMORY_TBS begin backup;
select * from v$stable_mem_datafiles;
alter tablespace USER_MEMORY_TBS end backup;
alter tablespace USER_DISK_TBS begin backup;
alter tablespace USER_DISK_TBS end backup;
ALTER SYSTEM SWITCH LOGFILE;
```

### Cold-backup path-change SQL

```sql
startup control;
alter database rename datafile '/old/path/system001.dbf' to '/new/path/system001.dbf';
alter database rename datafile '/old/path/system002.dbf' to '/new/path/system002.dbf';
alter database rename datafile '/old/path/temp001.dbf' to '/new/path/temp001.dbf';
alter database rename datafile '/old/path/undo001.dbf' to '/new/path/undo001.dbf';
startup service;
```

### Time-based recovery SQL

```sql
ALTER DATABASE BACKUP DATABASE TO '/backup_dir';
select last_deleted_logfile from v$lfg;
ALTER DATABASE CREATE DATAFILE 'temp001.dbf';
ALTER DATABASE RECOVER DATABASE UNTIL TIME '2015-07-23:14:01:00';
ALTER DATABASE mydb META RESETLOGS;
ALTER DATABASE mydb SERVICE;
ALTER DATABASE BACKUP DATABASE TO '/backup_dir';
```

### Logical backup commands

```bash
cd $ALTIBASE_HOME/conf
cp -p aexport.properties.sample aexport.properties
aexport
sh run_il_out.sh | tee download.out
nohup sh run_il_out.sh &
mv nohup.out download.out
grep "\-f ALTITEST_" run_il_out.sh > altitest_il_out.sh
grep 'SYS_ORDERS.fmt' run_il_out.sh
iloader -s localhost -u SYS -p MANAGER formout -f SYS_ORDERS.fmt -T ORDERS
iloader -s localhost -u SYS -p MANAGER out -f SYS_ORDERS.fmt -d SYS_ORDERS.dat -log SYS_ORDERS.log
```

### Logical restore commands

```bash
sh run_is.sh | tee run_is.log
nohup sh run_is.sh &
mv nohup.out run_is.log
grep "\-f ALTITEST_" run_il_in.sh > altitest_il_in.sh
sh altitest_il_in.sh | tee upload.out
nohup sh altitest_il_in.sh &
mv nohup.out upload.out
grep 'SYS_ORDERS.fmt' run_il_in.sh
iloader -s localhost -u SYS -p MANAGER in -f SYS_ORDERS.fmt -d SYS_ORDERS.dat -log SYS_ORDERS.log -bad SYS_ORDERS.bad
tail -f upload.out
```

### Failure response and monitoring commands

```bash
echo $ALTIBASE_HOME
ps -ef | grep "altibase -p boot from" | grep -v grep
isql -u sys -p manager -s 127.0.0.1 -port 20300
server kill
server start
ulimit -n
df -k
bdf
tail -f altibase_boot.log | grep "ERR-"
```

### Failure response SQL

```sql
ALTER TABLESPACE [tablespace name] ALTER AUTOEXTEND OFF;
ALTER TABLESPACE [tablespace name] ALTER AUTOEXTEND ON MAXSIZE 1G;
DELETE FROM [table name];
TRUNCATE TABLE [table name];
ALTER TABLE [table name] COMPACT;
ALTER TABLESPACE [tablespace name] ADD DATAFILE 'abcd.dbf' SIZE 1G AUTOEXTEND OFF;
SET LINESIZE 1000;
SELECT *
FROM   V$MEMSTAT
ORDER  BY MAX_TOTAL_SIZE DESC;
SELECT *
FROM   V$STATEMENT
WHERE  TOTAL_TIME > 100000000
AND    EXECUTE_FLAG = 1;
SELECT SESSION_ID,
       ID,
       RPAD(QUERY, 150)
FROM   V$STATEMENT
WHERE  TX_ID = (SELECT ID
                FROM   V$TRANSACTION
                WHERE  MEMORY_VIEW_SCN IN (SELECT MINMEMSCNINTXS
                                            FROM   V$MEMGC
                                            LIMIT  1));
SELECT COUNT(*)
FROM   V$REPSENDER;
SELECT COUNT(*)
FROM   V$REPRECEIVER;
SELECT REP_NAME,
       REP_GAP
FROM   V$REPGAP;
```

### Failure evidence by OS

Collect three stack snapshots at 30-second intervals when Altibase appears hung and connection attempts receive no response.

| OS | Commands |
| --- | --- |
| SUN | `/usr/sbin/pstack -F process_id > 1.txt`, then `2.txt`, then `3.txt` |
| HP IA | `/usr/ccs/bin/pstack process_id > 1.txt`, then `2.txt`, then `3.txt` |
| AIX | `/usr/bin/procstack -F process_id > 1.txt`, then `2.txt`, then `3.txt` |
| Linux | `/usr/bin/pstack process_id > 1.txt`, then `2.txt`, then `3.txt`; older kernels may not have the command |

System logs to check:

| OS | System log |
| --- | --- |
| SUN | `/var/adm/message` |
| HP | `/var/adm/syslog/syslog.log` |
| AIX | `errpt -a` |
| Linux | `/var/log/message` |

## Validation and troubleshooting

### Choose the backup type by recovery requirement

Use `aexport` when object-level backup/recovery is needed and object changes are the main concern. It lets Altibase keep running during recovery, but it only recovers to the backup point.

Use `iloader` when table-level or record-level backup/recovery is needed, point-in-time recovery is unnecessary, and recovery should run while Altibase remains online. It only recovers to the backup point.

Use online backup when data loss must be minimized, point-in-time recovery is required, archive log mode is acceptable, and the backup must prepare for physical loss of data files or log anchor files.

Use offline/cold backup when backup downtime is available and minimizing recovery time is the priority.

Use incremental backup when data loss must be minimized, point-in-time recovery is required, archive log mode is acceptable, `Page Change Tracking` overhead is acceptable, and backup time or backup space must be reduced compared with full online backup.

### Validate startup after recovery

After cold-backup recovery or time-based recovery, validate startup by checking for `PROCESS`, `CONTROL`, `META`, and `SERVICE` transitions, listener startup, `[RP] Initialization : [PASS]`, and `STARTUP Process SUCCESS`.

After incomplete recovery and `RESETLOGS`, immediately take a new full database backup.

### Handle connection failures

Connection failure while the server process exists can come from:

| Cause | Evidence and response |
| --- | --- |
| User account file-descriptor limits | `ERR-01052(errno=24)` on `open()` or `ERR-71016(errno=24)` on `accept()` in `$ALTIBASE_HOME/altibase_boot.log`; check `ulimit -n`, increase it, and restart Altibase. Recommended value is `unlimited`, at least `4096`. |
| Wrong connection information | Check user account, password, target IP, and whether the attempted port differs from `PORT_NO` in `$ALTIBASE_HOME/conf/altibase.properties`. |
| Password or access policy | Source errors include `ERR-50032`, `ERR-31010`, `ERR-4102E`, `ERR-31370`, and `ERR-410E3`. |
| Network failure | Use `netstat`; test `ftp` or `telnet` from other hosts; check whether packet transmission and reception performance degraded. |
| Insufficient disk space | Check `df` or `bdf`; add disk space. Do not delete Altibase online log files. |
| Hang-like system or Altibase state | Collect three OS stack snapshots at 30-second intervals plus system logs and all `$ALTIBASE_HOME/trc` files, then request support. |

### Handle insufficient tablespace

Memory tablespace shortage can raise:

```text
ERR-110F1 : Unable to extend the tablespace(XXXXX) because the current size of tablespace(4194304K) becomes larger than MAXSIZE(4194304K) of the tablespace.
```

For user memory tablespaces, increase `MAXSIZE` above the current value:

```sql
ALTER TABLESPACE [tablespace name] ALTER AUTOEXTEND OFF;
ALTER TABLESPACE [tablespace name] ALTER AUTOEXTEND ON MAXSIZE 1G;
```

If the error occurs in `SYS_TBS_MEM_DATA` or `SYS_TBS_MEM_DIC`, or if total memory tablespace usage already exceeds `MEM_MAX_DB_SIZE`, the `ALTER TABLESPACE` action cannot resolve it. Remove unnecessary data, compact the table, or increase `MEM_MAX_DB_SIZE` in `$ALTIBASE_HOME/conf/altibase.properties` and restart Altibase.

```sql
DELETE FROM [table name];
TRUNCATE TABLE [table name];
ALTER TABLE [table name] COMPACT;
```

Disk tablespace shortage can raise:

```text
ERR-11123 : The tablespace does not have enough free space ( TBS Name :XXXXX ).
```

Add a data file:

```sql
ALTER TABLESPACE [tablespace name] ADD DATAFILE 'abcd.dbf' SIZE 1G AUTOEXTEND OFF;
```

These are urgent measures. Afterward, investigate why tablespace usage suddenly increased, check DBMS object usage per tablespace, review what changed, and remove the cause.

### Handle physical disk and memory pressure

If physical disk space is exhausted, the DB can appear hung because online log files required for transactions cannot be written. Trace logs may also be absent because Altibase cannot write logs. Free or add disk space; there is no substitute response.

For physical memory pressure, periodically collect:

```sql
SET LINESIZE 1000;
SELECT *
FROM   V$MEMSTAT
ORDER  BY MAX_TOTAL_SIZE DESC;
```

Compare module memory usage with previous results to identify abnormal increases.

### Handle bulk changes and long-running queries

Altibase uses MVCC. Deleted data can remain as Garbage Data until related transactions finish. Bulk changes or long-running queries can increase online log files and physical memory usage.

Find currently executing queries over 100 seconds:

```sql
SELECT *
FROM   V$STATEMENT
WHERE  TOTAL_TIME > 100000000
AND    EXECUTE_FLAG = 1;
```

Find a statement whose transaction prevents deleted data cleanup:

```sql
SELECT SESSION_ID,
       ID,
       RPAD(QUERY, 150)
FROM   V$STATEMENT
WHERE  TX_ID = (SELECT ID
                FROM   V$TRANSACTION
                WHERE  MEMORY_VIEW_SCN IN (SELECT MINMEMSCNINTXS
                                            FROM   V$MEMGC
                                            LIMIT  1));
```

### Handle replication-related failure symptoms

R009 includes replication failure response because replication problems can cause data divergence and sender-side online log accumulation.

Check Sender and Receiver existence:

```sql
SELECT COUNT(*)
FROM   V$REPSENDER;

SELECT COUNT(*)
FROM   V$REPRECEIVER;
```

The count should be `1` or higher and must match the number of replication objects that should be running.

Check replication gap:

```sql
SELECT REP_NAME,
       REP_GAP
FROM   V$REPGAP;
```

`REP_NAME` is the replication object name. `REP_GAP` is the size from the log record currently being sent to the last log record not yet sent. The default unit is MB. It should stay close to zero; continuous increase indicates Sender/Receiver or network problems.

In Altibase `6.5.1` or earlier, the source defines `REP_GAP` as the difference between the latest local server `SN` and latest local server `XSN`:

```text
REP_GAP = Latest SN of local SERVER - Latest XSN of local SERVER
```

Check `altibase_rp.log` for normal and abnormal replication messages. Examples include:

```text
[Recovery Sender] Replication REP1 Start...
[Receiver] Replication REP1 Started ...
ERR-61012(errno=111) [Sender] Failed to connect to the peer server
ERR-6104b(errno=0) [Receiver] REP1 receiver is ended (by thr_exit)
RECEIVER:REPLICATION STOP MSG arrived!
```

If repeated replication restart commands do not change status, request support.

Data conflict logs are in `altibase_rp.log` or `altibase_rp_conflict.log`, depending on configuration. Representative source errors are:

| Conflict case | Errors |
| --- | --- |
| INSERT DML duplicate PK | `ERR-11058(errno=0) The row already exists in a unique index.` |
| DELETE DML row missing on peer | `ERR-61036(errno=0) [Receiver] err_not found in deleteXlog()` and `ERR-61000(errno=0) The received record is not found in the database.` |
| UPDATE DML row missing on peer | `ERR-6103a(errno=0) [Receiver] err_not_found in updateXlog()` and `ERR-61000(errno=0) The received record is not found in the database.` |
| UPDATE DML original data differs | `ERR-61035(errno=0) [Receiver] An update conflict encountered.` and `ERR-61001(errno=0) A conflict has been occurred while executing the received statement.` |

Except for INSERT conflicts, the source records two errors for one conflict. SQL that caused the conflict is also logged; review application execution flow based on that SQL.

### Basic monitoring for failure prevention

The failure-response reference lists these baseline monitoring items:

| Item | Method | What to watch |
| --- | --- | --- |
| Altibase process | `ps -ef | grep "altibase -p boot from" | grep -v grep` | At least one process. |
| System free memory | `vmstat` or OS memory command | Maintain about 20% margin. |
| Altibase memory usage | `SELECT SUM(MAX_TOTAL_SIZE) FROM V$MEMSTAT;` | Sudden increase versus normal usage. |
| Memory DB allocation | `SELECT TRUNC((MEM_ALLOC_PAGE_COUNT*32*1024)/MEM_MAX_DB_SIZE*100.0, 2) FROM V$DATABASE;` | Occupancy should not exceed 90%. |
| System disk usage | `df -k` | Directories used by Altibase and sharp increases. |
| Disk DB allocation | `V$TABLESPACES` joined to `V$DATAFILES` | Allocated disk DB space versus total availability. |
| Trace errors | `tail -f altibase_boot.log | grep "ERR-"` | Take action by severity. |
| Log deletion | `altibase_sm.log` message `Remove Online Log File at LFG [0]: File[11252 ~ 11253]` | If file number range repeatedly shows `None`, investigate. |
| Replication gap | `SELECT REP_NAME, REP_GAP FROM V$REPGAP;` | Continuous increase. |

## Version-specific notes

| Source unit | Version or mode condition |
| --- | --- |
| Incremental backup | Supported starting from Altibase `6.3.1`. |
| Materialized view extraction by `aexport` | Provided starting from `ALTIBASE HDB 6.3.1`. |
| Cold-backup recovery FAQ | Applies to `ALTIBASE HDB` version 4 or later. |
| Online backup and time-based recovery FAQ | Applies to `ALTIBASE HDB` version 4 or later. |
| `v$nls_parameters` character-set check | Available starting from `ALTIBASE HDB` version 5. |
| Online backup | Requires archive log mode. |
| Online backup and incremental recovery | Recovery is performed from the `CONTROL` stage. |
| Time-based incomplete recovery | Requires archive log mode and at least one full online backup or cold backup before the target point. |
| Altibase `6.5.1` or earlier `REP_GAP` | Calculate with online log serial numbers `SN` and `XSN`. |

## Related errors

| Error or message | Context | Response basis |
| --- | --- | --- |
| `ERR-01052(errno=24) Unable to invoke open() function on [~~~]` | Connection failure due to file descriptor limit or insufficient disk. | Check `ulimit -n`, disk space, and restart after OS setting changes. |
| `ERR-71016(errno=24) Failed to invoke a system function, accept() Dispatcher failed callback` | File descriptor limit during connection accept. | Increase file descriptor limit, recommended `unlimited` and at least `4096`, then restart Altibase. |
| `ERR-50032 : Client unable to establish a connection.` | Connection attempt failure. | Check IP, port, network, and connection configuration. |
| `ERR-31010 : User not found` | Connection attempt failure. | Check DB user. |
| `ERR-4102E : Invalid password` | Connection attempt failure. | Check password and password policy. |
| `ERR-31370 : The account is locked.` | Password management policy locked the account. | Unlock or resolve according to account policy. |
| `ERR-410E3 : The user cannot connect using TCP.` | TCP connection restriction. | Review access configuration and user policy. |
| `ERR-110F1` | Memory tablespace cannot extend past `MAXSIZE`. | Increase memory tablespace `MAXSIZE`, compact or remove data, or increase `MEM_MAX_DB_SIZE` and restart when required. |
| `ERR-11123` | Disk tablespace lacks free space. | Add a data file to the tablespace. |
| `ERR-311F4 : Invalid column name` | Example `iloader` or script error during download/upload validation. | Inspect run log, table log, `.bad` files, and fix the command or schema mismatch. |
| `ERR-61012(errno=111)` | Replication Sender cannot connect to peer server. | Check peer Receiver, network, and replication status. |
| `ERR-6104b(errno=0)` | Receiver ended. | Determine whether stop was intentional or failure-related. |
| `ERR-11058` | Replication INSERT duplicate conflict. | Inspect conflict SQL and application flow. |
| `ERR-61036`, `ERR-61000` | Replication DELETE conflict where row is missing on peer. | Inspect conflict SQL and data divergence. |
| `ERR-6103a`, `ERR-61000` | Replication UPDATE not-found conflict. | Inspect conflict SQL and data divergence. |
| `ERR-61035`, `ERR-61001` | Replication UPDATE conflict where original data differs. | Inspect conflict SQL and data divergence. |

## Attachments and external references

| Source path | Reference | Status |
| --- | --- | --- |
| `arch/Home/Considerations for Altibase Backup Policy__14647709.md` | `https://docs.altibase.com/download/attachments/14057586/ALTIBASE_%EB%B0%B1%EC%97%85%EC%A0%95%EC%B1%85_%EA%B2%B0%EC%A0%95%EC%9D%84_%EC%9C%84%ED%95%9C_%EA%B3%A0%EB%A0%A4%EC%82%AC%ED%95%AD.pdf?version=1&modificationDate=1698113791000&api=v2` | URL-backed PDF preserved. |
| `arch/Home/Responding to Failures Guide for Altibase/2. Procedure by type of failure__15138835.md` | `https://docs.altibase.com/download/attachments/embedded-page/arch/2.%20Procedure%20by%20type%20of%20failure/replication.png?api=v2` | Embedded image retained in source and registered as `not_document_format`; `REP_GAP` meaning is covered in text. |
| `arch/Home/Responding to Failures Guide for Altibase/3. References__15138869.md` | `https://docs.altibase.com/download/attachments/embedded-page/arch/3.%20References/Reference.png?api=v2` | Embedded image retained in source and registered as `not_document_format`; support-system meaning is covered in text. |
| `arch/Home/Considerations for Altibase Backup Policy__14647709.md` | `http://support.altibase.com` | Technical support portal reference preserved. |
| `arch/Home/Responding to Failures Guide for Altibase__15138818.md` | `http://support.altibase.com/en/` and `02-2082-1114` | Technical support request and phone contact preserved. |
| `FAQE/Home/04. Backup and Recovery/Using aexport and iloader__16876103.md` | `http://support.altibase.com/en/manual` and `https://github.com/ALTIBASE/Documents/tree/master/Manuals/` | Manual download references preserved. |
| `arch/Home/Considerations for Altibase Backup Policy/3. Summary (Considerations for Altibase Backup Policy)__14647728.md` | Administrator Manual chapters `10. Backup and Recovery`, `11. Incremental backup and Recovery`, Utilities Manual `1. aexport`, `iLoader User's Manual`, `https://github.com/ALTIBASE/Documents/tree/master/Manuals`, and `http://support.altibase.com/kr/manual` | Related manual references preserved. |

## Terminology

| Term | Preserve exactly | Meaning |
| --- | --- | --- |
| `aexport` | Yes | Altibase utility that creates object scripts and `iloader` scripts for migration or backup. |
| `iloader` / `iLoader` | Yes | Altibase data load/download utility for table-level text data. Preserve the capitalization used by a source when quoting it. |
| `run_il_out.sh` | Yes | Generated data download script. |
| `run_il_in.sh` | Yes | Generated data upload script. |
| `run_is.sh` | Yes | Generated schema creation script using `isql`. |
| `ALTIBASE_NLS_USE` | Yes | Client character set environment variable for `iloader`. |
| `ILO_DATEFORM` | Yes | Date format environment variable for `iloader`. |
| `ILOADER_FIELD_TERM` | Yes | Field separator property in `aexport.properties`. |
| `ILOADER_ROW_TERM` | Yes | Row separator property in `aexport.properties`. |
| `ARCHIVE_MODE` | Yes | `v$archive` column that indicates archive mode. |
| `LOGANCHOR_DIR` | Yes | Property for log anchor file directories. |
| `LOG_DIR` | Yes | Property for online redo log file directory. |
| `ARCHIVE_DIR` | Yes | Property for archive log directory. |
| `RESETLOGS` | Yes | Required after incomplete recovery before moving through `META`. |
| `Page Change Tracking` | Yes | Feature required for incremental backup. |
| `CONTROL`, `META`, `SERVICE` | Yes | Startup stages used by backup/recovery procedures. |
| `REP_GAP`, `SN`, `XSN` | Yes | Replication gap identifiers used in failure response. |
| `$ALTIBASE_HOME/trc` | Yes | Trace log directory. |
