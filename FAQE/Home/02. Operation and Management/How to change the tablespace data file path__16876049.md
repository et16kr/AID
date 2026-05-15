---
title: "How to change the tablespace data file path"
page_id: "16876049"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/How+to+change+the+tablespace+data+file+path"
updated_at: "2021-04-02T17:29:32.000+0900"
version: 3
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# How to change the tablespace data file path
Source: https://docs.altibase.com/display/FAQE/How+to+change+the+tablespace+data+file+path
Updated: 2021-04-02T17:29:32.000+0900

- [Overview](#Howtochangethetablespacedatafilepath-Overview) - [Summary of change procedure](#Howtochangethetablespacedatafilepath-Summaryofchangeprocedure) - [Detailed procedure](#Howtochangethetablespacedatafilepath-Detailedprocedure) - [1. Check the current path of the data file](#Howtochangethetablespacedatafilepath-1.Checkthecurrentpathofthedatafile1.PathCheck) - [2. Stop the Altibase server](#Howtochangethetablespacedatafilepath-2.StoptheAltibaseserver) - [3. Change the data file default path](#Howtochangethetablespacedatafilepath-3.Changethedatafiledefaultpath) - [4. Copy the physical data file path](#Howtochangethetablespacedatafilepath-4.Copythephysicaldatafilepath) - [5. Start the Altibase server as a control stage](#Howtochangethetablespacedatafilepath-5.StarttheAltibaseserverasacontrolstage) - [6. Execute the data file path change DDL](#Howtochangethetablespacedatafilepath-6.ExecutethedatafilepathchangeDDL) - [7. Start the Altibase server as a service stage](#Howtochangethetablespacedatafilepath-7.StarttheAltibaseserverasaservicestage) - [Error messages that may occur during the operation](#Howtochangethetablespacedatafilepath-Errormessagesthatmayoccurduringtheoperation) - [The data file does not exist](#Howtochangethetablespacedatafilepath-Thedatafiledoesnotexist) - [The data file 'XXXXXX' has an invalid header](#Howtochangethetablespacedatafilepath-Thedatafile'XXXXXX'hasaninvalidheader) - [Unable to invoke the create() function on \[XXXXXX/dwfile0.dwf\]](#Howtochangethetablespacedatafilepath-Unabletoinvokethecreate()functionon[XXXXXX/dwfile0.dwf]) - [CANNOT IDENTIFY DATAFILE](#Howtochangethetablespacedatafilepath-CANNOTIDENTIFYDATAFILE) - [Reference](#Howtochangethetablespacedatafilepath-Reference)

# Overview

---

This document describes the procedure for changing the path of data files in disk tablespaces and memory checkpoint image files in memory tablespaces.

Change the data file path after securing service downtime.

# Summary of change procedure

---

1. Check the current path of the data file
2. Stop the Altibase server.
3. Change the data file default path.
4. Copy the data file to the new path.
5. Start Altibase server as a control stage.
6. Execute the data file path change DDL.
7. Start the Altibase server as a service stage.

# Detailed procedure

---

## 1. Check the current path of the data file

---

The verification method differs depending on the disk tablespace and the memory tablespace, so they need to be checked separately. Use the query below to check and write down the output result.

- **Data file path of disk tablespace**

  **All the Altibase server versions**

  ```
  -- Output the disk tablespace name and data file path and name.
  set linesize 1024
  set colsize 100
  SELECT T.NAME TBS_NAME, D.NAME DATAFILE
    FROM V$DATAFILES D, V$TABLESPACES T
   WHERE D.SPACEID = T.ID
   ORDER BY D.SPACEID, D.ID ;
  ```
- **Path to checkpoint image file in memory tablespace**

  **How to check in Altibase version 5 or later**

  ```
  -- For memory tablespaces, only the tablespace name and path can be checked.
  set linesize 1024
  set colsize 100
  SELECT TBS.NAME TBS_NAME,
         MEM_PATH.CHECKPOINT_PATH DATAFILE
    FROM V$TABLESPACES TBS,
         V$MEM_TABLESPACE_CHECKPOINT_PATHS MEM_PATH
   WHERE MEM_PATH.SPACE_ID = TBS.ID
   ORDER BY TBS_NAME, DATAFILE;
  ```

  **How to check in Altibase version 4**

  ```
  $ grep MEM_DB_DIR $ALTIBASE_HOME/conf/altibase.properties | sort -u
  ```

## 2. Stop the Altibase server

---

- The Altibase server must be stopped as the user needs to physically move the data files.

  ```
    # Altibase server stop command
  $ server stop

    # How to check the Altibase server process
  $ ps -ef | grep 'altibase -p' | grep -v grep
  ```

## 3. Change the data file default path

---

- The data file default path refers to the path where the data file will be located if the user specifies only the data file name without specifying a path when creating a tablespace or adding a data file.
- Do this if the user also needs to change the default path when working with data file path change.
- Set in the altibase.properties file, find the MEM_DB_DIR, DEFAULT_DISK_DB_DIR properties, and change the default path.

  ```
    # Property names differ depending on the disk and memory tablespaces.
    # Find the properties MEM_DB_DIR, DEFAULT_DISK_DB_DIR in the altibase.properties file and change the default path.
  $ egrep 'MEM_DB_DIR|DEFAULT_DISK_DB_DIR' $ALTIBASE_HOME/conf/altibase.properties
  MEM_DB_DIR          = ?/dbs # Memory DB Directory
  DEFAULT_DISK_DB_DIR = ?/dbs # Disk   DB Directory
  ```

## 4. Copy the physical data file path

---

- Copy all data files and memory checkpoint image files located in the path identified in "1. Check the current path of the data file" to the path the user wants to change.

  **cp example**

  ```
     # System disk tablespace data files are created in *.dbf format.
     # User disk tablespace data files are created with the name specified by the user when the tablespace is created.
  $ cp -p /home/altibase_home/dbs_old_path/*.dbf /home/altibase_home/dbs_new_path/*.dbf

     # Memory checkpoint image file names use the format memory_tablespace_name_#_#.
  $ cp -p /home/altibase_home/dbs_old_path/SYS_MEM* /home/altibase_home/dbs_new_path/SYS_MEM*
  ```
- Compare the number and size of files to verify that they were copied correctly.

  ```
     # Compare the number of files
  $ ls -l /old_path/* | wc -l
  $ ls -l /new_path/* | wc -l

     # Compare the size of files
  $ du -sk /old_path/*
  $ du -sk /new_path/*
  ```
- Change the original path to another name.

  When starting the Altibase server, avoid the possibility of reading the original file and change the original path to a different name for the backup of the original file.

  ```
  $ mv /old_path /old_path_backup
  ```

## 5. Start the Altibase server as a control stage

---

- After connecting to the iSQL with sysdba privileges

  ```
  $is -silent -sysdba
  [ERR-910FB : Connected to idle instance]
  iSQL(sysdba)> STARTUP CONTROL
  ```
- Start as a control stage

  ```
  iSQL(sysdba)> STARTUP CONTROL
  Connecting to the DB server.... Connected.
  TRANSITION TO PHASE : PROCESS
  TRANSITION TO PHASE : CONTROL
  Command executed successfully.
  iSQL(sysdba)>
  ```

## 6. Execute the data file path change DDL

---

The disk data file and memory checkpoint image file path information are stored in the log anchor file. Execute the DDL statement to change the information known to the log anchor.

- **How to change the disk data file path**

  The ALTER DATABASE statement is repeated as many times as the number of all data files checked in "1. Check the current path of data files". The user must enter the same file name by changing only the path.

  ```
  iSQL(sysdba)> ALTER DATABASE RENAME DATAFILE
  '/old_path/system001.dbf'  TO '/new_path/system001.dbf';
  Alter success.
  ```
- **Check the disk data file change path**

  Make sure the path has been changed correctly.

  ```
  # Output the disk tablespace name and data file path and name.
  set linesize 1024
  set colsize 100
  SELECT T.NAME TBS_NAME, D.NAME DATAFILE
    FROM V$DATAFILES D, V$TABLESPACES T
   WHERE D.SPACEID = T.ID
   ORDER BY D.SPACEID, D.ID ;
  ```
- **Change the memory checkpoint image file path**

  Repeat the ALTER TABLESPACE statement for the number of memory tablespaces checked in "1. Check the current path of the data file". In this case, specify only the old and new paths without specifying a file name.

  **Altibase version 5 or later**

  ```
  iSQL(sysdba)> ALTER TABLESPACE memory_tablespace_name RENAME CHECKPOINT PATH
  '/old_path' TO '/new_path';

  Example)
  iSQL(sysdba)> ALTER TABLESPACE SYS_TBS_MEM_DIC RENAME CHECKPOINT PATH
  '/home/altibase_home/dbs_old_path' TO '/home1/altibase_home/dbs_new_path';
  Alter success.
  iSQL(sysdba)> ALTER TABLESPACE USER_MEM_TBS RENAME CHECKPOINT PATH
  '/home/altibase_home/dbs_old_path' TO '/home1/altibase_home/dbs_new_path';
  Alter success.
  ```

  **Altibase version 4**

  ```
  # In Altibase version 4, no DDL operation is required.
  # Change the MEM_DB_DIR property value in the altibase.properties file, then save the file.

  $ cd $ALTIBASE_HOME/conf/
  $ vi altibase.properties
  ```
- **How to check the memory checkpoint image file change path**

  **How to check in Altibase 5 or later version**

  ```
  -- For in-memory tablespaces, the tablespace name and path can be checked.
  set linesize 1024
  set colsize 100
  SELECT TBS.NAME TBS_NAME,
         MEM_PATH.CHECKPOINT_PATH DATAFILE
    FROM V$TABLESPACES TBS,
         V$MEM_TABLESPACE_CHECKPOINT_PATHS MEM_PATH
   WHERE MEM_PATH.SPACE_ID = TBS.ID
   ORDER BY TBS_NAME, DATAFILE;
  ```

## 7. Start the Altibase server as a service stage

---

Execute while connected to the iSQL with sysdba privilege.

```
iSQL(sysdba)> startup
The database server is already up and running.
TRANSITION TO PHASE : META
...Omitted...
--- STARTUP Process SUCCESS ---
Command executed successfully.
iSQL(sysdba)>
```

# Error messages that may occur during the operation

---

These are error messages that may occur while changing the data file path, and this section describes how to handle them.

## The data file does not exist

---

- **Cause**
  This can happen if the change statement was performed without physically moving the data file.

- **Solution**
  After moving the data file to the location where you want to change the data file, execute the rename statement that changes the location of the data file in the DB.

## The data file 'XXXXXX' has an invalid header

---

- **Cause**
  This can happen if the data file copy phase is not physically performed normally. When starting the database in the service stage, the startup fails.
- **Solution**
  Redo the operation of the physical data file

## Unable to invoke the create() function on [XXXXXX/dwfile0.dwf]

---

- **Cause**

  This can happen if the double write file does not exist. The double write file is required for restart recovery when the database is abnormally terminated. The default path is `$ALTIBASE_HOME/dbs`. If all files in the `$ALTIBASE_HOME/dbs` path are moved, an error may occur. The error message may differ depending on the Altibase server version.

- **Solution** `dwfile0.dwf` and `dwfile1.dwf` files can be manually created with the touch command.

  Or change $ALTIBASE_HOME/conf/altibase.properties to USE_DW_BUFFER = 0 (add it if it doesn't exist) and start the Altibase server. When the Altibase server is started, change it to USE_DW_BUFFER = 1 or delete the USE_DW_BUFFER setting from altibase.properties. After changing the default path of the double write file, the Altibase server can be started.

  ```
     # Change the value of the DOUBLE_WRITE_DIRECTORY property.
  $ vi $ALTIBASE_HOME/conf/altibase.properties
  DOUBLE_WRITE_DIRECTORY       = ?/dbs
  DOUBLE_WRITE_DIRECTORY       = ?/dbs
  ```

## CANNOT IDENTIFY DATAFILE

---

- **Cause**

  When starting the Altibase server in the service stage, this can happen if the physical data file cannot be found at the data file path stored in the meta table. This can happen if an incorrect data file path was entered in the control stage.

  ```
  iSQL(sysdba)> startup
  The database server is already up and running.
  TRANSITION TO PHASE : META
    [SM-WARNING] CANNOT IDENTIFY DATAFILE
                                  [TBS:USER_DATA, PPID-0-FID-0] Datafile Not Found
    [SM-WARNING] CANNOT IDENTIFY DATAFILE
                                  [TBS:USER_DATA, PPID-1-FID-0] Datafile Not Found
  [FAILURE] The data file does not exist.
  Startup Failed....
  [ERR-91015 : Communication failure.]
  $
  ```
- **Solution**

  In the control stage, execute the DDL statement with the correct path.

# Reference

---

- [How to change the path of log anchor, online log file, archive log file, and double write file](https://aid.altibase.com/display/FAQE/How+to+change+the+path+of+log+anchor%2C+online+log+file%2C+archive+log+file%2C+and+double+write+file)
