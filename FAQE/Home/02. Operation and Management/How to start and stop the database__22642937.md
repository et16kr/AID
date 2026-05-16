---
title: "How to start and stop the database"
page_id: "22642937"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/How+to+start+and+stop+the+database"
updated_at: "2025-10-20T15:20:19.206+0900"
version: 1
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# How to start and stop the database
Source: https://docs.altibase.com/display/FAQE/How+to+start+and+stop+the+database
Updated: 2025-10-20T15:20:19.206+0900

- [How to stop Altibase](#Howtostartandstopthedatabase-HowtostopAltibase) - [(1) Using the server stop script](#Howtostartandstopthedatabase-(1)Usingtheserverstopscript) - [(2) Using the shutdown command after connecting to isql](#Howtostartandstopthedatabase-(2)Usingtheshutdowncommandafterconnectingtoisql) - [How to start Altibase](#Howtostartandstopthedatabase-HowtostartAltibase) - [(1) Using the server start script](#Howtostartandstopthedatabase-(1)Usingtheserverstartscript) - [(2) Using the startup command after connecting to isql](#Howtostartandstopthedatabase-(2)Usingthestartupcommandafterconnectingtoisql) - [How to check whether the database is started normally after starting the database](#Howtostartandstopthedatabase-Howtocheckwhetherthedatabaseisstartednormallyafterstartingthedatabase) - [(1) Displayed message after server start](#Howtostartandstopthedatabase-(1)Displayedmessageafterserverstart) - [(2) Connection test with isql](#Howtostartandstopthedatabase-(2)Connectiontestwithisql) - [(3) Simply checking query](#Howtostartandstopthedatabase-(3)Simplycheckingquery) - [How to forcibly shutdown Altibase](#Howtostartandstopthedatabase-HowtoforciblyshutdownAltibase) - [Error message at ALTIBASE server start/stop](#Howtostartandstopthedatabase-ErrormessageatALTIBASEserverstart/stop) - [(1) The database server is already up and running.](#Howtostartandstopthedatabase-(1)Thedatabaseserverisalreadyupandrunning.) - [(2) Another SYSDBA session is already running](#Howtostartandstopthedatabase-(2)AnotherSYSDBAsessionisalreadyrunning)

# How to stop Altibase

---

There are two methods to stop the Altibase database as follows.

## (1) Using the server stop script

The DB server can be stopped with a simple command, and this is the most commonly used method. Run `server stop` from the Unix user account where Altibase is installed.

Command: shell> server stop

**How to stop db with the server stop command**

**$ server stop** ----------------------------------------------------------------- Altibase Client Query utility. Release Version 7.1.0.9.9 Copyright 2000, ALTIBASE Corporation or its subsidiaries. All Rights Reserved. ----------------------------------------------------------------- ISQL_CONNECTION = UNIX, SERVER = localhost Ok..Shutdown Proceeding....

TRANSITION TO PHASE : Shutdown Altibase [RP] Finalization : PASS **shutdown immediate success. (If the shutdown is successful, the message shown on the left is displayed.)**

## (2) Using the shutdown command after connecting to isql

After connecting to isql, the DB can be stopped by selectively using the shutdown method with the shutdown command.

**db stop using shutdown command after connecting isql**

$ **isql -sysdba <- - - Must connect in sysdba mode.** ----------------------------------------------------------------- Altibase Client Query utility. Release Version 7.1.0.9.9 Copyright 2000, ALTIBASE Corporation or its subsidiaries. All Rights Reserved. ----------------------------------------------------------------- Write UserID : sys Write Password : ISQL_CONNECTION = UNIX, SERVER = localhost

iSQL(sysdba)> select db_name from v$database; DB_NAME ------------------------------------------------------------------------------------------------------------------------------------ **mydb** 1 row selected. iSQL(sysdba)> **alter database***mydb* **shutdown immediate; <- - mydb, the dbname, is optional during installation and may vary from DB to DB.** Ok..Shutdown Proceeding....

TRANSITION TO PHASE : Shutdown Altibase [RP] Finalization : PASS **Alter success.** iSQL(sysdba)> exit

# How to start Altibase

---

There are two methods to start the Altibase database.

## (1) Using the server start script

---

The DB server can be started with a simple command and this is the most used method. The DB server can be started with the command "server start" as follows from the unix user account where Altibase is installed.

Command: shell> server start

**db start method with the server start command**

**$ server start** ----------------------------------------------------------------- Altibase Client Query utility. Release Version 7.1.0.9.9 Copyright 2000, ALTIBASE Corporation or its subsidiaries. All Rights Reserved. ----------------------------------------------------------------- ISQL_CONNECTION = UNIX, SERVER = localhost Connected to idle instance. Connecting to the DB server.... Connected.

TRANSITION TO PHASE : PROCESS

TRANSITION TO PHASE : CONTROL

TRANSITION TO PHASE : META [SM] Recovery Phase - 1 : Preparing Database : Dynamic Memory Version => Parallel Loading [SM] Recovery Phase - 2 : Loading Database [SM] Recovery Phase - 3 : Skipping Recovery & Starting Threads... Refining Disk Table [SM] Refine Memory Table : ........................................................................................................................................................................... [SUCCESS] [SM] Rebuilding Indices [Total Count:133] ..................................................................................................................................... [SUCCESS]

TRANSITION TO PHASE : SERVICE [CM] Listener started : TCP on port 20370 [IPV4] [CM] Listener started : UNIX [CM] Listener started : IPC [RP] Initialization : [PASS]

**--- STARTUP Process SUCCESS ---** **Command executed successfully.** $

## (2) Using the startup command after connecting to isql

---

The DB can be started step by step after connecting to the DB in sysdba mode with isql from the unix user account where Altibase is installed.

**How to start db after connecting to isql**

**$ isql -sysdba** ----------------------------------------------------------------- Altibase Client Query utility. Release Version 7.1.0.9.9 Copyright 2000, ALTIBASE Corporation or its subsidiaries. All Rights Reserved. ----------------------------------------------------------------- Write UserID : sys Write Password : ISQL_CONNECTION = UNIX, SERVER = localhost Connected to idle instance. iSQL(sysdba)> **startup** Connecting to the DB server.... Connected.

TRANSITION TO PHASE : PROCESS

TRANSITION TO PHASE : CONTROL

TRANSITION TO PHASE : META [SM] Recovery Phase - 1 : Preparing Database : Dynamic Memory Version => Parallel Loading [SM] Recovery Phase - 2 : Loading Database [SM] Recovery Phase - 3 : Skipping Recovery & Starting Threads... Refining Disk Table [SM] Refine Memory Table : ........................................................................................................................................................................... [SUCCESS] [SM] Rebuilding Indices [Total Count:133] ..................................................................................................................................... [SUCCESS]

TRANSITION TO PHASE : SERVICE [CM] Listener started : TCP on port 20370 [IPV4] [CM] Listener started : UNIX [CM] Listener started : IPC [RP] Initialization : [PASS]

**--- STARTUP Process SUCCESS ---** **Command executed successfully.** iSQL(sysdba)> exit

# How to check whether the database is started normally after starting the database

---

After starting Altibase, it can be checked whether the ALTIBASE DB server has been successfully started using the following method.

## (1) Displayed message after server start

When starting the DB with the server start command or isql, it checks whether "— STARTUP Process Success —" is output as follows.

**Message after server start**

**$ server start** ----------------------------------------------------------------- Altibase Client Query utility. Release Version 7.1.0.9.9 Copyright 2000, ALTIBASE Corporation or its subsidiaries. All Rights Reserved. ----------------------------------------------------------------- ISQL_CONNECTION = UNIX, SERVER = localhost Connected to idle instance. Connecting to the DB server.... Connected.

..............................omitted...............................

..................................................................... [CM] Listener started : TCP on port 20370 [IPV4]

[CM] Listener started : UNIX [CM] Listener started : IPC [RP] Initialization : [PASS]

**--- STARTUP Process SUCCESS ---** **Command executed successfully.**

## (2) Connection test with isql

---

The DB status can be checked by executing a simple SQL statement on is or isql, an interactive query execution tool, and checking whether the query is operating normally.

**DB status check with isql connection**

$ is ----------------------------------------------------------------- Altibase Client Query utility. Release Version 7.1.0.9.9 Copyright 2000, ALTIBASE Corporation or its subsidiaries. All Rights Reserved. ----------------------------------------------------------------- ISQL_CONNECTION = TCP, SERVER = localhost, PORT_NO = 20370 iSQL> select sysdate from dual; SYSDATE --------------- 14-JUL-2025 1 row selected. iSQL>

## (3) Simply checking query

---

The DB status can be checked by executing the query below.

- Check the number of sessions: Check the number of sessions currently connected to the DB.

  ```
  iSQL> select count(*) from v$session;
  COUNT
  -----------------------
  1
  1 row selected.

  ```
- Check the replication gap: If the user is using the replication, the replication gap can be checked. If the replication gap value increases or decreases repeatedly, it is normal.

  ```
  iSQL> select rep_name, rep_gap from v$repgap;
  REP_NAME                                  REP_GAP
  ------------------------------------------------------------------
  REP1                                      567
  1 rows selected.
  iSQL>

  ```
- Transaction processing status Inquire about the accumulated transaction throughput currently being processed by DML or DB. If it continues to increase, it is normal.

  ```
  iSQL> select * from v$sysstat where name like '%execute%count%';
  SEQNUM      NAME                                                VALUE
  -----------------------------------------------------------------------------------------
  28          execute success count                               3186
  29          execute success count : insert                      3119
  30          execute success count : update                      0
  31          execute success count : delete                      0
  32          execute success count : select                      66
  33          rep_execute success count : insert                  0
  34          rep_execute success count : update                  0
  35          rep_execute success count : delete                  0
  36          execute failure count                               0
  9 rows selected.
  iSQL>

  ```

# How to forcibly shutdown Altibase

---

If the Altibase database server is in a hang state due to system malfunction or lack of system resources, and the DB cannot be stopped using a normal method such as server stop, the following command can be used.

**How to forcibly shutdown Altibase**

$ server kill ----------------------------------------------------------------- Altibase Client Query utility. Release Version 7.1.0.9.9 Copyright 2000, ALTIBASE Corporation or its subsidiaries. All Rights Reserved. ----------------------------------------------------------------- ISQL_CONNECTION = UNIX, SERVER = localhost

$

server kill kills the DB process in the same way as killing ALTIBASE with kill -9. It is not recommended under normal circumstances.

If ALTIBASE is forcibly shutdown with the server kill, the recovery process will be performed at the next start. If there is a large amount of undo and redo transactions during the recovery process, it may take a long time to start the server.

Therefore, it is recommended to stop the database with the normal `server stop` command whenever possible.

# Error message at ALTIBASE server start/stop

---

## (1) The database server is already up and running.

If the user tries to start an additional server while the Altibase server is already started, the following message is displayed. The server cannot be started because the database has already been started.

$ server start ----------------------------------------------------------------- Altibase Client Query utility. Release Version 7.1.0.9.9 Copyright 2000, ALTIBASE Corporation or its subsidiaries. All Rights Reserved. ----------------------------------------------------------------- ISQL_CONNECTION = UNIX, SERVER = localhost **The database server is already up and running.** [ERR-4107A : Unable to start up in the specified phase in the current state.] $

## (2) Another SYSDBA session is already running

---

Sessions with sysdba privileges only allow one connection to the DB. This is an error message that appears when an additional sysdba connection for server start or server stop fails when there is a session already connected to sysdba.

Try to reconnect after ending a connected sysdba session.

$ server start ----------------------------------------------------------------- Altibase Client Query utility. Release Version 7.1.0.9.9 Copyright 2000, ALTIBASE Corporation or its subsidiaries. All Rights Reserved. ----------------------------------------------------------------- ISQL_CONNECTION = UNIX, SERVER = localhost **[ERR-41041 : Another SYSDBA session is already running.]** $
