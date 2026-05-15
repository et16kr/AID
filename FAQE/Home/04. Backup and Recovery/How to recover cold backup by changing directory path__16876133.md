---
title: "How to recover cold backup by changing directory path"
page_id: "16876133"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/How+to+recover+cold+backup+by+changing+directory+path"
updated_at: "2021-04-05T09:42:18.000+0900"
version: 2
ancestors: ["Home", "04. Backup and Recovery"]
labels: []
---

# How to recover cold backup by changing directory path
Source: https://docs.altibase.com/display/FAQE/How+to+recover+cold+backup+by+changing+directory+path
Updated: 2021-04-05T09:42:18.000+0900

**- [Overview](#Howtorecovercoldbackupbychangingdirectorypath-Overview) - [Version](#Howtorecovercoldbackupbychangingdirectorypath-Version) - [How to change directory path](#Howtorecovercoldbackupbychangingdirectorypath-Howtochangedirectorypath) - [Directory path change procedure](#Howtorecovercoldbackupbychangingdirectorypath-Directorypathchangeprocedure) - [Reference](#Howtorecovercoldbackupbychangingdirectorypath-Reference)**

# Overview

---

This document describes how to recover by changing the directory path of major database files such as each data file inevitably after Cold Backup.

# Version

---

ALTIBASE HDB version 4 or later

# How to change directory path

---

When restoring using Cold Backup database files, if there is no change in the directory path, copy (cp) mydb* (memory db), *.dbf (disk db), logs, and loganchor to the corresponding directory, and then when starting B, DB can be restored to the point of backup.

However, if the directory must be renamed inevitably, it is resolved by changing the directory path of each database file (memoryDB, logs, loganchor) and copying the file to the changed directory, but the disk DB must perform the renaming of the data file at the control stage.

# Directory path change procedure

---

1. Create the desired directory and copy the Cold Backup files.

Copy Cold Backup (mydb*, *.dbf, logs, loganchor) to the desired directory using the OS copy command.

2. Modify $ALTIBASE_HOME/conf/altibase.properties.

```
..Omitted
MEM_DB_DIR          = /home/cheol2/altibase_home/dbs # Memory DB Directory

DEFAULT_DISK_DB_DIR =/home/cheol2/altibase_home/dbs # Disk   DB Directory

LOGANCHOR_DIR       =/home/cheol2/altibase_home/logs # LOGANCHOR_DIR1  // 로그앵커
LOGANCHOR_DIR       = /home/cheol2/altibase_home/logs # LOGANCHOR_DIR2
LOGANCHOR_DIR       = /home/cheol2/altibase_home/logs # LOGANCHOR_DIR3

LOG_DIR = /home/cheol2/altibase_home/logs # Redo log file directory
ARCHIVE_DIR   =  /home/cheol2/altibase_home/logs # Archive directory
..Omitted
```

3. Startup at the Control stage.

```
[cheol2@as48-x64 ~/altibase_home/conf]$ is -sysdba
-----------------------------------------------------------------
     Altibase Client Query utility.
     Release Version 6.5.1.0.6
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
ISQL_CONNECTION = UNIX, SERVER = localhost, PORT_NO = 33889
iSQL(sysdba)>startup control;
TRANSITION TO PHASE : PROCESS
TRANSITION TO PHASE : CONTROL
Command execute success.
```

4. Rename datafile in ISQL. (Change directory path)

```
iSQL(sysdba)>alter database rename datafile '/home/cheol2/altibase_home/dbs2/system001.dbf'  to '/home/cheol2/altibase_home/dbs/system001.dbf';
iSQL(sysdba)>alter database rename datafile '/home/cheol2/altibase_home/dbs2/system002.dbf'  to '/home/cheol2/altibase_home/dbs/system002.dbf';
iSQL(sysdba)>alter database rename datafile '/home/cheol2/altibase_home/dbs2/temp001.dbf'  to '/home/cheol2/altibase_home/dbs/temp001.dbf';
iSQL(sysdba)>alter database rename datafile '/home/cheol2/altibase_home/dbs2/undo001.dbf'  to '/home/cheol2/altibase_home/dbs/undo001.dbf';
iSQL(sysdba)>alter database rename datafile '/home/cheol2/altibase_home/dbs2/system001.dbf'  to '/home/cheol2/altibase_home/dbs/system001.dbf';
iSQL(sysdba)>alter database rename  datafile '/home/cheol2/altibase_home/dbs2/system002.dbf'  to '/home/cheol2/altibase_home/dbs/system002.dbf';
iSQL(sysdba)>alter database rename datafile '/home/cheol2/altibase_home/dbs2/temp001.dbf'  to '/home/cheol2/altibase_home/dbs/temp001.dbf';
iSQL(sysdba)>alter database rename datafile '/home/cheol2/altibase_home/dbs2/undo001.dbf'  to '/home/cheol2/altibase_home/dbs/undo001.dbf';
```

5. Startup in ISQL.

```
iSQL(sysdba)> startup service;ISQL_CONNECTION = UNIX, SERVER = localhost, PORT_NO = 33889
[ERR-910FB : Connected to idle instance]
Connecting to the DB server... Connected.

TRANSITION TO PHASE : PROCESS

TRANSITION TO PHASE : CONTROL

TRANSITION TO PHASE : META
  [SM] Recovery Phase - 1 : Preparing Database
                          : Dynamic Memory Version => Parallel Loading
  [SM] Recovery Phase - 2 : Loading Database
  [SM] Recovery Phase - 3 : Skipping Recovery & Starting Threads...
                            Refining Disk Table
  [SM] Refine Memory Table : ............................................................................................................ [SUCCESS]
  [SM] Rebuilding Indices [Total Count:117] ........................................................................................................... [SUCCESS]

TRANSITION TO PHASE : SERVICE
  [CM] Listener started : TCP on port 33889 [IPV4]
  [CM] Listener started : UNIX
  [CM] Listener started : IPC
  [RP] Initialization : [PASS]

--- STARTUP Process SUCCESS ---
Command executed successfully.
```

# Reference

---

More detailed information can be found in the Table of Contents of the **General Reference Manual**.

---
