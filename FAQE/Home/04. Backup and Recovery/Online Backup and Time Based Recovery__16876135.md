---
title: "Online Backup and Time Based Recovery"
page_id: "16876135"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Online+Backup+and+Time+Based+Recovery"
updated_at: "2021-04-05T09:43:08.000+0900"
version: 5
ancestors: ["Home", "04. Backup and Recovery"]
labels: []
---

# Online Backup and Time Based Recovery
Source: https://docs.altibase.com/display/FAQE/Online+Backup+and+Time+Based+Recovery
Updated: 2021-04-05T09:43:08.000+0900

- [Overview](#OnlineBackupandTimeBasedRecovery-Overview) - [Version](#OnlineBackupandTimeBasedRecovery-Version) - [Online backup procedure](#OnlineBackupandTimeBasedRecovery-Onlinebackupprocedure) - [Time based recovery](#OnlineBackupandTimeBasedRecovery-Timebasedrecovery) - [Reference](#OnlineBackupandTimeBasedRecovery-Reference)

# Overview

---

This section explains how to perform Online Backup and Time Based Recovery, which can be performed when the Altibase server is operated in archive log mode.

Online Backup is not possible except in Archivelog Mode.

# Version

---

ALTIBASE HDB version 4 or later

# Online backup procedure

---

1. Online backup is possible only when the DB is running in the archive mode, and the procedure to check and change the archive mode is as follows.

A. How to check Archivelog mode

```
iSQL> select ARCHIVE_MODE from v$archive;ARCHIVE_MODE
 -----------------------
0                        // 0: Archive_mode not used, 1: Archive mode used
```

B. How to change Archive mode

The Archive mode cannot be changed while online and can be changed at the Control stage after DB shutdown.

After connecting to sysdba mode, start-up in the Control stage and change to Archive mode.

```
[cheol@as48-x64 ~]$ is -sysdba
iSQL(sysdba)> startup control;
Connecting to the DB server...
Connected.TRANSITION TO PHASE : PROCESS
TRANSITION TO PHASE : CONTROL
Command execute success.

2) Change to Archivelog mode
iSQL(sysdba)> alter database archivelog;Alter success.
```

2. Procedure to perform Online Backup when DB is operating in Archivelog Mode

A. Database Online Backup by database system

1) Database unit online backup

```
iSQL> alter database backup database to '/backup';  // The backup directory can be arbitrarily changed.
```

The following files are copied to the /backup directory.

```
SYS_TBS_MEM_DIC-0-0
SYS_TBS_MEM_DATA-0-0
system001.dbf
system002.dbf
undo001.dbf
loganchor0
loganchor2
loganchor1
```

2) In case of online backup for a specific tablespace unit

```
iSQL(sysdba)> alter database backup tablespace SYS_TBS_MEM_DIC to ‘/backup_dir’;  // A stable version of the SYS_TBS_MEM_DIC data files is backed up online to the /backup_dir directory.
$ ls /backup_dirSYS_TBS_MEM_DIC-0-0
```

3) Log anchor online backup

```
iSQL(sysdba)> alter database backup loganchor to ‘/backup_dir’;  // All log anchor files are backed up online to the /backup_dir directory.
$ ls /backup_dir
loganchor0 loganchor1 loganchor2
```

B. Online backup by DBA

1) Online backup by tablespace

Ex) Online backup of data files of USER_MEMORY_TBS and USER_DISK_TBS tablespaces in /backup_dir.

```
Ex) Online backup of data files of USER_MEMORY_TBS and USER_DISK_TBS tablespaces in /backup_dir.
```

The memory tablespace data file is backed up online after confirming that it is a stable version of the data file.

```
iSQL(sysdba)> alter tablespace USER_MEMORY_TBS begin backup;
iSQL(sysdba)> select * from v$stable_mem_datafiles;
MEM_DATA_FILE
--------------------------------------------------
/altibase_home/dbs/USER_MEM_TBS-0-0  // stable version

$ cp $ALTIBASE_HOME/dbs/USER_MEMORY_TBS-0-0  /backup_dir/

iSQL(sysdba)> alter tablespace USER_MEMORY_TBS end backup;
iSQL(sysdba)> alter tablespace USER_DISK_TBS begin backup;

$ cp $ALTIBASE_HOME/dbs/USER_DISK_TBS.dbf /backup_dir/

iSQL(sysdba)> alter tablespace USER_DISK_TBS end backup;

$ ls /backup_dir
USER_MEMORY_TBS-0-0 USER_DISK_TBS.dbf
```

2) Finishing online backup by DBA

Commands to force archive log files related to the backup must be executed so that even if the current log file is not used up, it is instructed to close it and continue logging to the next log file.

```
iSQL(sysdba)> ALTER SYSTEM SWITCH LOGFILE;
```

# Time based recovery

---

It is operating in Archivelog Mode and is a recovery procedure when online backup (or cold backup) for the entire DB is performed more than once before the desired recovery point.

Ex) The tablespace USER_DISK_TBS was deleted by mistake. (July 23, 2015 14:11)

Database recovery procedure to the state of 10 minutes before the tablespace existed

At the last backup, the entire DB was backed up as follows.

```
iSQL(sysdba)> ALTER DATABASE BACKUP DATABASE TO ‘/backup_dir’;
```

A. Copy the data files of all disk tablespaces of the backed up database to the original location of the data files.

```
$ cp /backup_dir/*.dbf $ALTIBASE_HOME/dbs
$ cp /backup_dir/SYS_TBS_* $ALTIBASE_HOME/dbs
```

B. Check the archive log files required for recovery and copy and use the backed up log anchor files.

1) Check the archive log files required for recovery

```
iSQL(sysdba)> select last_deleted_logfile from v$lfg;
LAST_DELETED_LOGFILE
------------------------
15021                // Archive log file number required for recovery
```

In the altibase_sm.log file created in the $ALTIBASE_HOME/trc directory, check the files that were forcibly archived when the backup was completed.

```
[2015/07/23 13:59:59] [Thread-6] [Level-9]Waiting logfile15341 to archive  //Forced archived file number, i.e. logfile15021 ~ logfile15341 files are required for recovery.
```

2) Copy the backed up log anchor file

```
$ cp /backup_dir/loganchor* /ALTIBASE_HOME/logs;
```

3) Because the SYS_TBS_DISK_TEMP tablespace is not backed up, create a new one.

```
iSQL(sysdba)> ALTER DATABASE CREATE DATAFILE ‘temp001.dbf’
```

4) Perform incomplete media recovery.

```
iSQL(sysdba)> ALTER DATABASE RECOVER DATABASE  UNTIL TIME '2015-07-23:14:01:00';
```

Since the incomplete media recovery has performed, the resetlogs option must be used while going to the meta startup stage.

```
iSQL(sysdba)> ALTER DATABASE mydb META RESETLOGS;
```

5) Since the server was started and the log was reset, the entire database was backed up.

```
iSQL(sysdba)> ALTER DATABASE mydb SERVICE;
iSQL(sysdba)> ALTER DATABASE BACKUP DATABASE TO ‘/backup_dir’;
```

# Reference

---

More detailed information can be found in the Table of Contents of the Admin Manual > **Backup and Recovery cases**.
