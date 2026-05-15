---
title: "Creating ALTIBASE Database"
page_id: "22643020"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/Creating+ALTIBASE+Database"
updated_at: "2025-10-21T09:26:21.000+0900"
version: 1
ancestors: ["Home"]
labels: []
---

# Creating ALTIBASE Database
Source: https://docs.altibase.com/display/arch/Creating+ALTIBASE+Database
Updated: 2025-10-21T09:26:21.000+0900

---

- [Overview](#CreatingALTIBASEDatabase-Overview) - [How to create a database](#CreatingALTIBASEDatabase-Howtocreateadatabase) - [Considerations when creating a database](#CreatingALTIBASEDatabase-Considerationswhencreatingadatabase) - [Archive log mode](#CreatingALTIBASEDatabase-Archivelogmode) - [DB_NAME](#CreatingALTIBASEDatabase-DB_NAME) - [How to drop a database](#CreatingALTIBASEDatabase-Howtodropadatabase) - [Check the files to be dropped](#CreatingALTIBASEDatabase-Checkthefilestobedropped) - [Dropping a database](#CreatingALTIBASEDatabase-Droppingadatabase)

---

# Overview

---

This document provides a guide on how to create an Altibase database.

This document is based on Altibase version 7.1.0 or higher.

For errors and improvements related to this document, please contact the technical support portal or technical support center.

- Technical support portal: [http://support.altibase.com](http://support.altibase.com/)[/en/](http://support.altibase.com/en/)
- Technical support center: 02-2082-1114

This document is provided for informational purposes only and is subject to change without prior notice. It may contain errors, and Altibase makes no express or implied warranties of any kind, including but not limited to warranties of merchantability or fitness for a particular purpose.

The development, release, and timing of any features or functionality described for Altibase products in this document are at the sole discretion of Altibase.

Altibase may hold patents, trademarks, copyrights, or other intellectual property rights related to the contents of this document.

# How to create a database

---

This section describes how to create a database of versions supported according to Altibase's End of Service (EOS) policy. As for this document, the latest Altibase version is 'Altibase ver. 7' and 'Altibase ver 6 or below' are for EOS. Altibase cannot be operated until the database is created, so the database must be created as follows before starting the Altibase.

- Check DB_NAME in altibase.properties

```
$ cat $ALTIBASE_HOME/conf/altibase.properties | grep DB_NAME
DB_NAME       =  mydb
```

- If DB_NAME is not mydb (default), the server file must be changed.
  (Change mydb in create database mydb command to DB_NAME)

```
$ vi $ALTIBASE_HOME/bin/server
...
startup process;
create database mydb INITSIZE=10M noarchivelog character set $2 national character set $3;
quit
EOF
...
```

- Create a database.
  (server create 'database charset' 'national charset')

```
$ server create UTF8 UTF16
-----------------------------------------------------------------
     Altibase Client Query utility.
     Release Version 7.1.0.0.0
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
ISQL_CONNECTION = UNIX, SERVER = localhost, PORT_NO = 20300
[ERR-910FB : Connected to idle instance]
Connecting to the DB server.... Connected.

TRANSITION TO PHASE : PROCESS
Command executed successfully.
DB Info (Page Size     = 32768)
        (Page Count    = 257)
        (Total DB Size = 8421376)
        (DB File Size  = 1073741824)
...
```

- Or, the user can create a database as follows.

```
$ isql -u sys -p manager -sysdba
...
iSQL(sysdba)> startup process
...
iSQL(sysdba)> create database mydb INITSIZE=10M noarchivelog character set UTF8 national character set UTF16;
...
iSQL(sysdba)> exit
```

The meaning of each character set is as follows.

| Item | Description |
| --- | --- |
| Database character set | This means a character set stored in the database.<br>(US7ASCII, KO16KSC5601, MS949, BIG5, GB231280, UTF8, SHIFTJIS, EUCJP) |
| National character set | This means a Unicode-based character set stored in NVARCHAR and NVARCHAR2.<br>(UTF8, UTF16) |

# Considerations when creating a database

---

Things to be considered when creating a database are as follows.

## Archive log mode

---

- The archive log mode can be set at the control stage.
- Therefore, in order to change from No Archive log mode to Archive log mode, the user must shut down Altibase and enter the control stage during the startup process.
- In the archive log mode, the archive log file requires user management because Altibase only replicates the log file to the designated archive log file directory and does not delete it arbitrarily.
- It is necessary to secure the archive log file directory space in consideration of the backup cycle and the number of log files created within that cycle.

```
$ server stop
$ isql -u sys -p manager -sysdba
...
iSQL(sysdba)> startup control;
...
iSQL(sysdba)> alter database archivelog;
Alter success.
iSQL(sysdba)> startup service;
...
Command executed successfully.
iSQL(sysdba)> exit
```

## DB_NAME

---

- In the case of DB_NAME, it is determined when the database is created.
- In order to change, the database must be recreated, so migration must be performed.
- Therefore, be cautious when creating a database for the first time.

# How to drop a database

---

The user can drop the database by deleting all Altibase configuration files.

## Check the files to be dropped

---

- To check whether the database is dropped normally, check before dropping the data files and log files to be deleted.

```
iSQL> select name, checkpoint_path from v$tablespaces a, v$mem_tablespace_checkpoint_paths b where a.id = b.space_id;
iSQL> select a.name, b.name from v$tablespaces a, v$datafiles b where a.id = b.spaceid;

$ cat $ALTIBASE_HOME/conf/altibase.properties | grep ^LOG | grep DIR
```

## Dropping a database

---

- After Altibase is shut down, the database is dropped in the process stage.

```
$ isql -u sys -p manager -sysdba
...
iSQL(sysdba)> startup process;
Connecting to the DB server.... Connected.

TRANSITION TO PHASE : PROCESS
Command executed successfully.

iSQL(sysdba)> drop database mydb;
Checking Log Anchor files
[Ok] /home/altibase/altibase_home/logs/loganchor0 Exist.
[Ok] /home/altibase/altibase_home/logs/loganchor1 Exist.
[Ok] /home/altibase/altibase_home/logs/loganchor2 Exist.
Removing DB files
Removing Log files
Removing Log Anchor files
Drop success.

iSQL(sysdba)> exit
```

# Korean Source Attachments

The Korean source page also references these downloadable source attachments. They are preserved here so the English document set does not lose those references.

- The Korean source adds a version-specific database creation guide for Altibase 3, 4, and 5.
- [Korean source attachment 1 (PDF)](https://docs.altibase.com/download/attachments/13436812/ALTIBASE_%EB%B2%84%EC%A0%84%EB%B3%84_DB_%EC%83%9D%EC%84%B1_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=2&modificationDate=1758150003000&api=v2)
