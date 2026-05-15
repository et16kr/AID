---
title: "Database object backup using aexport"
page_id: "22642949"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Database+object+backup+using+aexport"
updated_at: "2025-10-20T15:26:59.000+0900"
version: 1
ancestors: ["Home", "04. Backup and Recovery", "Using aexport and iloader"]
labels: []
---

# Database object backup using aexport
Source: https://docs.altibase.com/display/FAQE/Database+object+backup+using+aexport
Updated: 2025-10-20T15:26:59.000+0900

# Preparation before executing aexport

---

Change the values of the following settings in the aexport.properties file.

- ILOADER_FIELD_TERM
- ILOADER_ROW_TERM

ILOADER_FIELD_TERM stands for field separator, and ILOADER_ROW_TERM stands for record separator.

If the aexport.properties file has never been changed, these settings are commented out and the defaults are set as follows.

**Default value of separator**

```
$ grep TERM aexport.properties
#ILOADER_FIELD_TERM = ^
#ILOADER_ROW_TERM = %n
```

If the default values above are used, change them to more distinctive separator values as follows.

**Change separator property setting value**

```
$ grep TERM aexport.properties
ILOADER_FIELD_TERM = ^Cc__Cc^
ILOADER_ROW_TERM = ^Rr__Rr^%n
```

The location of the aexport.properties file is $ALTIBASE_HOME/conf. If this file does not exist, copy and use the aexport.properties.sample file.

```
$ cd $ALTIBASE_HOME/conf
$ ls -l aexport.properties*
-rw-r--r-- 1 user1 user1 1636 Mar  9  2022 aexport.properties.sample

$ cp -p aexport.properties.sample aexport.properties
```

When aexport is executed, the following scripts are created.

- Database object creation script
- Data download/upload script using iloader

The data download/upload script using iloader contains iloader commands. iloader can use several options, and the value used for the option depends on the above setting.

The above setting means field separator and row separator, respectively, and the default values are simply set. If this setting value is included in the character data type column, data may not be uploaded normally when uploading data.

Therefore, it is recommended to use distinctive separator values that are unlikely to appear in character data.

## Executing aexport

Execute aexport after changing aexport.properties.

```
$ aexport
-----------------------------------------------------------------
     Altibase Export Script Utility.
     Release Version 6.3.1.2.7
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
Write Server Name (default:localhost) :          # Press enter when running locally, and enter IP when connecting to a remotely installed Altibase server.
Write UserID :                                   # Enter sys to back up all objects in the database, and enter corresponding USER to back up objects of a specific user.
Write Password :                                 # Enter USER's password

##### TBS #####

##### USER  #####
** input user ALTITEST's password(default - same with USER_NAME):            # If sys is entered for UserID, passwords of all users created in the database must be entered.
** input user USER1's password(default - same with USER_NAME): USER1         # Even if the user enters the password randomly, a backup script is created, but if the password does not match during the actual iloader backup, iloader will fail. Also, be aware that you are creating the create user ~identified by ~ syntax with the password entered here.
** input user USER2's password(default - same with USER_NAME): USER2

##### SYNONYM #####

##### DIRECTORY #####

##### TABLE #####
** "ALTITEST"."ORDERS"

** "SYS"."CUSTOMERS"

** "SYS"."DATE_T"

** "SYS"."DEMO_EX1"

** "SYS"."DEPARTMENTS"

** "SYS"."DISK_T"

** "SYS"."DISK_T2"

** "SYS"."EMPLOYEES"

** "SYS"."GOODS"

** "SYS"."MEM_T"

** "SYS"."ORDERS"

** "SYS"."PLAN_TEST"

** "SYS"."T"

** "SYS"."TEST_EMP_TBL"

** "SYS"."T_BINARY"

** "SYS"."T_BLOB"

** "SYS"."T_BYTES"

** "SYS"."T_CLOB"

** "SYS"."T_NIBBLE"

** "SYS"."VOL_T"

** "USER1"."T"

##### QUEUE #####

##### SEQUENCE #####

##### DATABASE LINK #####

##### VIEW #####

##### MATERIALIZED VIEW #####

##### STORED PROCEDURE #####

##### STORED PACKAGE #####

##### TRIGGER #####

##### LIBRARY #####

##### REPLICATION #####

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
-------------------------------------------------------
```

When aexport is executed, .sh (.bat for Windows system) files and .sql files are created as follows.

The .sql files contain the syntax for creating database objects and are scripts that execute .sh files to .sql files at once.

(**Note:** The number of `.sh` files may vary depending on the supported objects for each Altibase version.)

```
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
-------------------------------------------------------
```
