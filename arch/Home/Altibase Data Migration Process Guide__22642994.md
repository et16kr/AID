---
title: "Altibase Data Migration Process Guide"
page_id: "22642994"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/Altibase+Data+Migration+Process+Guide"
updated_at: "2025-10-21T08:57:43.000+0900"
version: 1
ancestors: ["Home"]
labels: []
---

# Altibase Data Migration Process Guide
Source: https://docs.altibase.com/display/arch/Altibase+Data+Migration+Process+Guide
Updated: 2025-10-21T08:57:43.000+0900

- [Overview](#AltibaseDataMigrationProcessGuide-Overview) - [Key Concepts](#AltibaseDataMigrationProcessGuide-KeyConcepts) - [Full Migration Process](#AltibaseDataMigrationProcessGuide-FullMigrationProcess) - [Detailed Step-by-Step Process](#AltibaseDataMigrationProcessGuide-DetailedStep-by-StepProcess) - [1. Preliminary Check](#AltibaseDataMigrationProcessGuide-1.PreliminaryCheck) - [2. Run aexport](#AltibaseDataMigrationProcessGuide-2.Runaexport) - [3. Data extraction](#AltibaseDataMigrationProcessGuide-3.Dataextraction) - [4. Target Altibase Configuration](#AltibaseDataMigrationProcessGuide-4.TargetAltibaseConfiguration) - [5. Data Loading](#AltibaseDataMigrationProcessGuide-5.DataLoading) - [6. Verification and Follow-up Actions](#AltibaseDataMigrationProcessGuide-6.VerificationandFollow-upActions) - [Reference Documents](#AltibaseDataMigrationProcessGuide-ReferenceDocuments)

# **Overview**

---

This document describes the standard procedure for safely migrating database objects and data in an Altibase environment.

It covers procedures commonly required in practice, such as version upgrades, server migration, and logical backup and recovery, focusing on the use of the Altibase tools aexport and iloader.

For errors and improvements related to this document, contact the technical support portal or technical support center.

- Technical support portal: [http://support.altibase.com](http://support.altibase.com/) > Technical Knowledge > Q&A
- Technical support center: 02-2082-1114

This document is provided for informational purposes and may change without prior notice. This document may contain errors, and Altibase assumes no express or implied responsibility for merchantability or fitness for a particular purpose.

The schedule for developing or releasing features and functions of Altibase products described in this document is at Altibase's discretion.

Altibase may hold patent rights, trademark rights, copyrights, or other intellectual property rights related to this document.

# **Key Concepts**

---

Data migration refers to the overall process of safely transferring database objects and data to a different environment.

### Use Cases

- Altibase server version upgrade
- Reconfiguration of the operating environment or migration of server/platform
- Logical backup and recovery
- Partitioning or relocation of large tables

### Main Tools

- **aexport:** Extracts database object creation DDL and generates data extraction/loading scripts
- **iloader:** Performs data extraction and loading

# **Full Migration Process**

---

Altibase data migration involves extracting object definitions and data from the source Altibase and applying them to the target Altibase. The general procedure is as follows.

| Order | Step | Description |
| --- | --- | --- |
| 1 | Preliminary Check | Stop service, check disk space, create working directory, verify source data count |
| 2 | Run aexport | Generate object definitions (DDL) and data extraction/loading scripts |
| 3 | Data Extraction | Create text files (.fmt, .dat) using `run_il_out.sh` |
| 4 | Configure Target Altibase | Install target Altibase and create objects using `run_is.sh` |
| 5 | Data Loading | Run `run_il_in.sh` (apply performance options if necessary) |
| 6 | Verification and Follow-up | Create subsequent objects such as indexes, foreign keys, triggers, and replication; check data count, object status, and service |

# **Detailed Step-by-Step Process**

---

## **1. Preliminary Check**

---

### 1.1 Stop Service

Migration is performed with the service completely stopped. No DML or DDL is allowed during the process.

### 1.2 Prepare Working Directory and Disk Space

Since text data can be larger than the internal storage size, ensure at least twice the data size in free space.

If backing up the source Altibase, prepare additional space accordingly.

```
$ mkdir mig_test
```

### 1.3 Record Source Data Counts

Record the data counts for each table in advance for verification after migration.

```
$ vi tbl_cnt.sql
SELECT COUNT(*) FROM table_name1;
SELECT COUNT(*) FROM table_name2;
SELECT COUNT(*) FROM table_name3;
...

$ is -f tbl_cnt.sql -o tbl_cnt.out
```

If you run the following SQL, you can automatically generate SQL to query the count for each user table.

```
SELECT 'SELECT COUNT(*) FROM '|| USER_NAME||'.'||TABLE_NAME||';'
  FROM SYSTEM_.SYS_USERS_ U, SYSTEM_.SYS_TABLES_ T
 WHERE U.USER_ID NOT IN (0, 1)
   AND U.USER_ID = T.USER_ID
   AND TABLE_TYPE = 'T'
 ORDER BY USER_NAME, TABLE_NAME;
```

### 1.4 Install the DBMS_METADATA package

This operation is performed only on Altibase 7.3 or higher.

The DBMS_METADATA package extracts object creation DDL statements and GRANT statements from the database dictionary and is supported starting from Altibase 7.3.

```
$ cd $ALTIBASE_HOME/packages
$ is -f dbms_metadata.sql
$ is -f dbms_metadata.plb
```

## **2. Run aexport**

---

### 2.1 Set the ALTIBASE_NLS_USE environment variable.

Match the Altibase client character set (environment variable ALTIBASE_NLS_USE) to the Altibase server character set.

**Check the Altibase server character set**

```
SELECT NLS_CHARACTERSET FROM V$NLS_PARAMETERS;
```

When the server character set is UTF8:

**Set the Altibase client character set**

```
$ export ALTIBASE_NLS_USE=UTF8
```

### 2.2 Modify aexport.properties.

To prevent errors caused by delimiter conflicts, remove the comments from `ILOADER_FIELD_TERM` and `ILOADER_ROW_TERM` to change their default values.

```
$ vi $ALTIBASE_HOME/conf/aexport.properties
... omitted ...
#######################
# iloader option
#######################
ILOADER_FIELD_TERM = ^C_c^
ILOADER_ROW_TERM = ^R_r^%n
... omitted ...
```

### 2.3 Run aexport

Execute aexport in the working directory. During the process, enter the server IP, user account, and password to scan objects and generate related scripts.

```
$ cd mig_test
$ aexport
```

**Example of execution:**

```
$ aexport
-----------------------------------------------------------------
     Altibase Export Script Utility.
     Release Version 7.3.0.0.6
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
Write Server Name (default:localhost) :                                          # Enter the IP of the source Altibase.
Write UserID : sys                                                               # Enter sys
Write Password :                                                                 # Enter sys password
##### TBS #####
##### USER  #####
** input user ALTITEST's password(default - same with USER_NAME):                # Enter database user password
##### SYNONYM #####
##### DIRECTORY #####
##### TABLE #####
** "ALTITEST"."ORDERS"
** "SYS"."CUSTOMERS"
... omitted ...
##### JOB #####
-------------------------------------------------------
  ##### The following script files were generated. #####
  1. run_il_out.sh            : [ iloader formout, data-out script ]
  2. run_is.sh                : [ isql table-schema script ]
  3. run_il_in.sh             : [ iloader data-in script ]
  4. run_is_refresh_mview.sh  : [ isql materialized view refresh script ]
  5. run_is_index.sh          : [ isql table-index script ]
  6. run_is_fk.sh             : [ isql table-foreign key script ]
  7. run_is_repl.sh           : [ isql replication script ]
  8. run_is_job.sh            : [ isql job script ]
  9. run_is_alt_tbl.sh        : [ isql table-alter script ]
-------------------------------------------------------
$
```

### 2.4 Check the results

When aexport execution is complete, an SQL file for creating database objects, a script to execute the SQL, and scripts for data extraction and loading are generated.

```
$ ls -l
total 60
-rw-rw-rw- 1 eheejung eheejung  222 2025-08-26 18:45 ALL_ALT_TBL.sql
-rw-rw-rw- 1 eheejung eheejung    0 2025-08-26 18:45 ALL_CRT_DIR.sql
-rw-rw-rw- 1 eheejung eheejung    0 2025-08-26 18:45 ALL_CRT_FK.sql
-rw-rw-rw- 1 eheejung eheejung 1646 2025-08-26 18:45 ALL_CRT_INDEX.sql
-rw-rw-rw- 1 eheejung eheejung    0 2025-08-26 18:45 ALL_CRT_JOB.sql
-rw-rw-rw- 1 eheejung eheejung    0 2025-08-26 18:45 ALL_CRT_LIB.sql
-rw-rw-rw- 1 eheejung eheejung    0 2025-08-26 18:45 ALL_CRT_LINK.sql
-rw-rw-rw- 1 eheejung eheejung    0 2025-08-26 18:45 ALL_CRT_REP.sql
-rw-rw-rw- 1 eheejung eheejung    0 2025-08-26 18:45 ALL_CRT_SEQ.sql
-rw-rw-rw- 1 eheejung eheejung    0 2025-08-26 18:45 ALL_CRT_SYN.sql
-rw-rw-rw- 1 eheejung eheejung 3239 2025-08-26 18:45 ALL_CRT_TBL.sql
-rw-rw-rw- 1 eheejung eheejung  754 2025-08-26 18:45 ALL_CRT_TBS.sql
-rw-rw-rw- 1 eheejung eheejung    0 2025-08-26 18:45 ALL_CRT_TRIG.sql
-rw-rw-rw- 1 eheejung eheejung  211 2025-08-26 18:45 ALL_CRT_USER.sql
-rw-rw-rw- 1 eheejung eheejung 1670 2025-08-26 18:45 ALL_CRT_VIEW_PROC.sql
-rw-rw-rw- 1 eheejung eheejung    0 2025-08-26 18:45 ALL_EXE_STATS.sql
-rw-rw-rw- 1 eheejung eheejung    0 2025-08-26 18:45 ALL_REFRESH_MVIEW.sql
-rw-rw-rw- 1 eheejung eheejung 1050 2025-08-26 18:45 run_il_in.sh
-rw-rw-rw- 1 eheejung eheejung 1748 2025-08-26 18:45 run_il_out.sh
-rw-rw-rw- 1 eheejung eheejung  503 2025-08-26 18:45 run_is.sh
-rw-rw-rw- 1 eheejung eheejung   55 2025-08-26 18:45 run_is_alt_tbl.sh
-rw-rw-rw- 1 eheejung eheejung  110 2025-08-26 18:45 run_is_fk.sh
-rw-rw-rw- 1 eheejung eheejung   57 2025-08-26 18:45 run_is_index.sh
-rw-rw-rw- 1 eheejung eheejung   55 2025-08-26 18:45 run_is_job.sh
-rw-rw-rw- 1 eheejung eheejung   61 2025-08-26 18:45 run_is_refresh_mview.sh
-rw-rw-rw- 1 eheejung eheejung   55 2025-08-26 18:45 run_is_repl.sh
```

## **3. Data extraction**

---

### 3.1 Run run_il_out.sh

Execute the `run_il_out.sh` script to extract data.

```
$ time sh run_il_out.sh | tee download.out
```

If the processing time is long, run it in the background to maintain the session. Rename and manage the `nohup.out` file.

```
$ time nohup sh run_il_out.sh > download.out 2>&1 &
```

### 3.2 Verification

**Check for errors**

Search for error messages in the execution log.

```
$ grep -i err- download.out
```

Check the number of tables

Verify that the number of `.fmt` files and `.dat` files matches the actual number of tables.

```
$ ls -l *.fmt | wc -l               # Check the number of .fmt files.
$ ls -l *.dat | wc -l               # Check the number of .dat files.
```

Check for record extraction errors

Verify that the `Error Row Count` value in each log file is 0. If any value is not zero, review the error details and re-extract the data.

```
$ grep -i 'error row count' *.log
```

## **4. Target Altibase Configuration**

---

Install the target Altibase and run the object definition scripts extracted by aexport to set up the database.

### 4.1 Check Source Altibase Information

To make the target environment the same as the source, query the following items.

```
-- Database name
SELECT DB_NAME FROM V$DATABASE;

-- Database server character set and national character set
SELECT NLS_CHARACTERSET, NLS_NCHAR_CHARACTERSET FROM V$NLS_PARAMETERS;

-- Archive log mode
SELECT ARCHIVELOG_MODE FROM V$LOG;

-- Paths for memory checkpoint image, disk data, transaction logs, log anchors, and archive log files
SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME IN ('MEM_DB_DIR', 'DEFAULT_DISK_DB_DIR', 'LOG_DIR', 'LOGANCHOR_DIR', 'ARCHIVE_DIR');
```

### 4.2 Stop and Backup Source Altibase

This procedure is performed when the source and target Altibase are located on the same server.

When migrating on the same server, first stop the source Altibase, then back up the Altibase home directory, disk data files, memory checkpoint image files, log anchor files, and transaction log files. The example below assumes that all files exist in the Altibase home directory.

```
$ server stop
$ mv $ALTIBASE_HOME $ALTIBASE_HOME.bak
```

### 4.3 Install Target Altibase

Install the target Altibase. For the required input information during installation, refer to the previously gathered '4.1 Check Source Altibase Information.'

### 4.4 Verify Data File Paths

If the data path of the target Altibase differs from the source, modify the paths of the disk data files and memory checkpoint image files in `ALL_CRT_TBS.sql`.

```
$ cat ALL_CRT_TBS.sql
connect "SYS" / "manager"
ALTER TABLESPACE "SYS_TBS_DISK_DATA"
ALTER DATAFILE '/data/altibase_home/dbs/system001.dbf'                    # Modify the data file paths as needed.
SIZE 102400K;
ALTER TABLESPACE "SYS_TBS_DISK_DATA"
ALTER DATAFILE '/data/altibase_home/dbs/system001.dbf'                    # Modify the data file paths as needed.
AUTOEXTEND ON NEXT 1024K MAXSIZE 2097144K;
... omitted ...
```

### 4.5 Change Altibase connection address in scripts

In the scripts generated by aexport, change the Altibase connection address to the target Altibase's IP.

**Example of change:** when the target Altibase's IP is 192.168.1.145

```
$ sed -i 's/-s localhost/-s 192.168.1.145/g' *.sh
```

### 4.6 Create database objects

Run the `run_is.sh` file to create tablespaces, database users, synonyms, directories, sequences, tables, libraries, views, stored procedures, and database links.

```
$ sh run_is.sh | tee run_is.out
```

Check for any errors that occurred during the database object creation process.

```
$ grep -i err- run_is.out
```

## **5. Data Loading**

---

### 5.1 Data Loading

Run the `run_il_in.sh` file to load the data.

```
$ time sh run_il_in.sh | tee upload.out
```

If there is a large amount of data or the process takes a long time, run it in the background to prevent the session from disconnecting.

```
$ time nohup sh run_il_in.sh > upload.out 2>&1 &
```

![(info)](https://docs.altibase.com/s/en_GB/5637/e1ef10868e8fe2f234a1a0b171b01cde1d9717c4.69/_/images/icons/emoticons/information.png) To improve data loading speed, add the [performance options](https://manual.altibase.com/7.3/tools/iloader/2.-Using-iLoader/#%EC%84%B1%EB%8A%A5-%EC%98%B5%EC%85%98) `-array` and `-commit` to the iloader command inside `run_il_in.sh` when executing.

```
$ vi run_il_in.sh
iloader -s localhost -u ALTITEST -p ALTITEST in -f ALTITEST_ORDERS.fmt -d ALTITEST_ORDERS.dat -log ALTITEST_ORDERS.log -bad ALTITEST_ORDERS.bad -array 1000 -commit 100                # Add the performance options array and commit.
iloader -s localhost -u SYS -p manager in -f SYS_CUSTOMERS.fmt -d SYS_CUSTOMERS.dat -log SYS_CUSTOMERS.log -bad SYS_CUSTOMERS.bad -array 1000 -commit 100
iloader -s localhost -u SYS -p manager in -f SYS_DEPARTMENTS.fmt -d SYS_DEPARTMENTS.dat -log SYS_DEPARTMENTS.log -bad SYS_DEPARTMENTS.bad -array 1000 -commit 100
iloader -s localhost -u SYS -p manager in -f SYS_D_DEPARTMENTS.fmt -d SYS_D_DEPARTMENTS.dat -log SYS_D_DEPARTMENTS.log -bad SYS_D_DEPARTMENTS.bad -array 1000 -commit 100
iloader -s localhost -u SYS -p manager in -f SYS_EMPLOYEES.fmt -d SYS_EMPLOYEES.dat -log SYS_EMPLOYEES.log -bad SYS_EMPLOYEES.bad -array 1000 -commit 100
iloader -s localhost -u SYS -p manager in -f SYS_GOODS.fmt -d SYS_GOODS.dat -log SYS_GOODS.log -bad SYS_GOODS.bad -array 1000 -commit 100
iloader -s localhost -u SYS -p manager in -f SYS_ORDERS.fmt -d SYS_ORDERS.dat -log SYS_ORDERS.log -bad SYS_ORDERS.bad -array 1000 -commit 100
iloader -s localhost -u SYS -p manager in -f SYS_PSM_TABLE.fmt -d SYS_PSM_TABLE.dat -log SYS_PSM_TABLE.log -bad SYS_PSM_TABLE.bad -array 1000 -commit 100
```

### 5.2 Verification

**Check for errors**

Search for error messages in the execution log.

```
$ grep -i err- upload.out
```

**Check the number of tables**

The number of `.log` and `.bad` files should match the number of tables.

```
$ ls -l *.log | wc -l
$ ls -l *.bad | wc -l
```

**Record error verification**

Check the log files for any failed records during loading. The `Error Row Count` should be 0 in all logs.

```
$ grep -i 'error row count' *.log
```

**Verify .bad files**

Verify that all `.bad` files have size 0:

```
$ ls -l *.bad | awk '{print $5}' | sort -u
```

Find `.bad` files with size greater than 0:

```
$ find ./ -type f -name "*.bad" ! -size 0
```

If there are tables with an Error Row Count or .bad file size greater than 0, check the records and error messages in the `username_tablename.log` file, address the issues, and then re-extract the data.

**Example of execution**: Since an error was found in the sample output, review the corresponding log file (`SYS_ORDERS.log` in this example).

```
$ grep -i 'error row count' *.log
ALTITEST_ORDERS.log:Error Row Count : 0
SYS_CUSTOMERS.log:Error Row Count : 0
SYS_DEPARTMENTS.log:Error Row Count : 0
SYS_D_DEPARTMENTS.log:Error Row Count : 0
SYS_EMPLOYEES.log:Error Row Count : 0
SYS_GOODS.log:Error Row Count : 0
SYS_ORDERS.log:Error Row Count : 1             # An error occurred in `SYS_ORDERS.log`
SYS_PSM_TABLE.log:Error Row Count : 0

$ cat SYS_ORDERS.log
<DataLoad>
TableName : ORDERS
Start Time : Wed Sep 10 13:26:57 2025
Record 7 : 12300004,2011/12/30 00:00:00:000000,20,15,"D1111000020",1000,2012/01/02 00:00:00:000000,"P"
[ERR-9102B : Token value length overflow. Maximum token length=10. Column =GNO, Value=D1111000020]
End Time : Wed Sep 10 13:26:57 2025
Total Row Count : 30
Load Row Count  : 29
Error Row Count : 1
```

The `.bad` files contain the records that failed to load.

```
$ cat SYS_ORDERS.bad
12300004,2011/12/30 00:00:00:000000,20,15,"D1111000020",1000,2012/01/02 00:00:00:000000,"P"
```

## **6. Verification and Follow-up Actions**

---

After data loading and object creation are complete, the database administrator and business personnel compare the data between the source Altibase and the target Altibase, and verify that key objects are functioning correctly. They also run applications and batch jobs to ensure that services operate normally.

# **Reference Documents**

---

For detailed features and advanced usage of aexport and iloader, refer to the following manuals.

- [Utilities Manual](https://manual.altibase.com/7.3/en/tools/util/copyright/)
- [iLoader User's Manual](https://manual.altibase.com/7.3/en/tools/iloader/copyright/)
