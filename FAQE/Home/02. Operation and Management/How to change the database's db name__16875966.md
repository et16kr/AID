---
title: "How to change the database's db name"
page_id: "16875966"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/How+to+change+the+database%27s+db+name"
updated_at: "2021-03-03T17:24:54.000+0900"
version: 1
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# How to change the database's db name
Source: https://docs.altibase.com/display/FAQE/How+to+change+the+database%27s+db+name
Updated: 2021-03-03T17:24:54.000+0900

- [How to change the database's db name](#Howtochangethedatabase'sdbname-Howtochangethedatabase'sdbname) - [Version](#Howtochangethedatabase'sdbname-Version) - [Notes/Considerations](#Howtochangethedatabase'sdbname-Notes/Considerations) - [Change procedure](#Howtochangethedatabase'sdbname-Changeprocedure) - [(1) DB stop](#Howtochangethedatabase'sdbname-(1)DBstop) - [(2) Change the DB name of altibase.properties](#Howtochangethedatabase'sdbname-(2)ChangetheDBnameofaltibase.properties) - [(3) Modify server script](#Howtochangethedatabase'sdbname-(3)Modifyserverscript) - [(4) Delete existing database](#Howtochangethedatabase'sdbname-(4)Deleteexistingdatabase) - [(5) Create a new DB with a new DB name](#Howtochangethedatabase'sdbname-(5)CreateanewDBwithanewDBname) - [(6) Start the DB](#Howtochangethedatabase'sdbname-(6)StarttheDB) - [(7) Check the changed database name](#Howtochangethedatabase'sdbname-(7)Checkthechangeddatabasename)

# How to change the database's db name

---

This section describes how to change the db name of the Altibase database.

# Version

---

This method is applied to ALTIBASE HDB version 5.3.3 or later.

# Notes/Considerations

---

To change the DB NAME, the DB must be recreated. When the DB is recreated, the existing data disappears, so when the existing data is restored, the DB data must be exported and backed up.

# Change procedure

---

## (1) DB stop

Stop DB with DB stop command.

[omegaman@rhel7-x64 ~]$ **server stop** ----------------------------------------------------------------- Altibase Client Query utility. Release Version 6.5.1.1.1 Copyright 2000, ALTIBASE Corporation or its subsidiaries. All Rights Reserved. ----------------------------------------------------------------- ISQL_CONNECTION = UNIX, SERVER = localhost Ok..Shutdown Proceeding....

## (2) Change the DB name of altibase.properties

Change the DB_NAME in the $ALTIBASE_HOME/conf/altibase.properties file to the DB name you want to change.

/* altibase.properties */ #================================================================= # Fixed Properties # must not be modified after the DB is created #================================================================= DB_NAME = **sdb** <--- Replace with the name of the DB you want to change (default: mydb)

## (3) Modify server script

Change the default DB name of the db create-part in $ALTIBASE_HOME/bin/server script to the DB name you want to change.

/* $ALTIBASE_HOME/bin/server script */

......................

'create') if [ $# = 3 ]; then rm -f live-altibase.txt; ${ISQL} << EOF > /dev/null spool live-altibase.txt; EOF if [ -f live-altibase.txt ]; then echo " server is running !!!! \n " echo " you must shutdown first before server create " rm -f live-altibase.txt; else ${ADMIN} << EOF startup process; create database **sdb** INITSIZE=10M noarchivelog character set $2 national character set $3; <---- Change the default DB name mydb to the DB name you want to change. quit EOF

## (4) Delete existing database

To create a new database, the existing DB must be deleted. To delete the existing DB, delete the $ALTIBASE_HOME/dbs/* and $ALTIBASE_HOME/logs/* files.

shell> cd $ALTIBASE_HOME

shell> rm dbs/*

shell> rm logs/*

## (5) Create a new DB with a new DB name

Create a new DB with the server create command.

[omegaman@rhel7-x64](mailto:omegaman@rhel7-x64) altibase_home]$**server create MS949 UTF8** ----------------------------------------------------------------- Altibase Client Query utility. Release Version 6.5.1.1.1 Copyright 2000, ALTIBASE Corporation or its subsidiaries. All Rights Reserved. ----------------------------------------------------------------- ISQL_CONNECTION = UNIX, SERVER = localhost [ERR-910FB : Connected to idle instance] Connecting to the DB server.... Connected.

TRANSITION TO PHASE : PROCESS Command executed successfully.

DB Info (Page Size = 32768) (Page Count = 257) (Total DB Size = 8421376) (DB File Size = 1073741824)

Creating MMDB FILES [SUCCESS]

Creating Catalog Tables [SUCCESS]

Creating DRDB FILES [SUCCESS]

[SM] Rebuilding Indices [Total Count:0] [SUCCESS]

DB Writing Completed. All Done.

Create success.

## (6) Start the DB

---

Start the DB with the server start command.

[omegaman@rhel7-x64](mailto:omegaman@rhel7-x64) altibase_home]$ server start ----------------------------------------------------------------- Altibase Client Query utility. Release Version 6.5.1.1.1 Copyright 2000, ALTIBASE Corporation or its subsidiaries. All Rights Reserved. ----------------------------------------------------------------- ISQL_CONNECTION = UNIX, SERVER = localhost [ERR-910FB : Connected to idle instance] Connecting to the DB server.... Connected.

TRANSITION TO PHASE : PROCESS

TRANSITION TO PHASE : CONTROL .....................................

[CM] Listener started : IPC [RP] Initialization : [PASS]

--- STARTUP Process SUCCESS ---

## (7) Check the changed database name

After starting the DB, the changed DB name can be checked with the following query.

[omegaman@rhel7-x64 altibase_home]$ **is** ----------------------------------------------------------------- Altibase Client Query utility. Release Version 6.5.1.1.1 Copyright 2000, ALTIBASE Corporation or its subsidiaries. All Rights Reserved. ----------------------------------------------------------------- ISQL_CONNECTION = TCP, SERVER = localhost, PORT_NO = 20416

iSQL> **select db_name from v$database;** DB_NAME ------------------------------------------------------------------------------------------------------------------------------------ **sdb** 1 row selected. iSQL>
