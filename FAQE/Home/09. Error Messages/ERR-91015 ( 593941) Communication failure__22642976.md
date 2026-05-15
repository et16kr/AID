---
title: "ERR-91015 ( 593941) Communication failure"
page_id: "22642976"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-91015+%28+593941%29+Communication+failure"
updated_at: "2025-10-20T15:52:21.000+0900"
version: 1
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# ERR-91015 ( 593941) Communication failure
Source: https://docs.altibase.com/display/FAQE/ERR-91015+%28+593941%29+Communication+failure
Updated: 2025-10-20T15:52:21.000+0900

## - [Overview](#ERR-91015(593941)Communicationfailure-Overview) - [Version](#ERR-91015(593941)Communicationfailure-Version) - [Symptom](#ERR-91015(593941)Communicationfailure-Symptom) - [Cause and Solution](#ERR-91015(593941)Communicationfailure-CauseandSolution) - [When trying to connect to the Altibase server](#ERR-91015(593941)Communicationfailure-WhentryingtoconnecttotheAltibaseserver) - [When occurs while connected to the Altibase server](#ERR-91015(593941)Communicationfailure-WhenoccurswhileconnectedtotheAltibaseserver) - [When the session is terminated by an Altibase server property](#ERR-91015(593941)Communicationfailure-WhenthesessionisterminatedbyanAltibaseserverproperty) - [When the session is terminated by the sysdba user](#ERR-91015(593941)Communicationfailure-Whenthesessionisterminatedbythesysdbauser) - [When running the database server](#ERR-91015(593941)Communicationfailure-Whenrunningthedatabaseserver)

# Overview

---

This document describes ERR-91015 (593941) Communication failure.

# Version

---

All the versions of Altibase HDB

# Symptom

---

ERR-91015 (593941) Communication failure errors can occur in various environments as follows.

- **When trying to connect to the Altibase server** When connecting to an Altibase server, this error occurs mainly when using iSQL.

  **Example of occurrence when connecting to the Altibase server from iSQL**

  ```
  $ is
  -----------------------------------------------------------------
       Altibase Client Query utility.
       Release Version 6.3.1.4.4
       Copyright 2000, ALTIBASE Corporation or its subsidiaries.
       All Rights Reserved.
  -----------------------------------------------------------------
  ISQL_CONNECTION = TCP, SERVER = localhost, PORT_NO = 20300
  [ERR-91015 : Communication failure.]
  ```
- **When occurs while connected to the Altibase server**

  ```
  iSQL> SELECT * FROM CUSTOMERS;
  [ERR-91015 : Communication failure.]
  ```
- **When running the Altibase server**

  **Example of occurrence when running the Altibase server**

  ```
  [eheejung@63138 /data/eheejung/work/sh]$server start
  -----------------------------------------------------------------
       Altibase Client Query utility.
       Release Version 6.3.1.4.4
       Copyright 2000, ALTIBASE Corporation or its subsidiaries.
       All Rights Reserved.
  -----------------------------------------------------------------
  ISQL_CONNECTION = UNIX, SERVER = localhost
  [ERR-910FB : Connected to idle instance]
  Set autocommit off success.
  Connecting to the DB server... Connected.

  TRANSITION TO PHASE : PROCESS

  TRANSITION TO PHASE : CONTROL

  TRANSITION TO PHASE : META
    [SM] Recovery Phase - 1 : Preparing Database
                            : Dynamic Memory Version => Parallel Loading
    [SM] Recovery Phase - 2 : Loading Database
    [SM] Recovery Phase - 3 : Starting Recovery
                              Initializing Active Transaction List
                              Redo
                              Refine Disk Table..
                              Undo
    [SM] Refine Memory Table : ................................................................................................................................ [SUCCESS]
  [ERR-91015 : Communication failure.]
  ```

# Cause and Solution

---

## When trying to connect to the Altibase server

---

**According to the ALTIBASE HDB compatibility policy, this error may occur when attempting to connect from a higher version of the Altibase client to a lower version of the Altibase server than the client.**

In case of this reason, various types of messages are displayed in the altibase_boot.log on the Altibase server, depending on the version of the Altibase server. (However, certain versions may not leave a message at all.)

Therefore, if this error occurs when connecting to the Altibase server, first check the version of the Altibase server and client. **If the client version is later than the server version, you must match the client version to the server version or install and use an earlier version than the server version.**

- How to check ALTIBASE HDB server version

  $ altibase -v version 6.1.1.4.9 X86_64_LINUX_redhat_Enterprise_ES4-64bit-6.3.1.4.4-release-GCC3.4.6 (x86_64-unknown-linux-gnu) Apr 14 2015 11:31:37, binary db version 6.2.1, meta version 6.3.1, cm protocol version 7.1.1, replication protocol version 7.4.1
- How to check ALTIBASE HDB client version

  $ apre -v Altibase Precompiler2(APRE) Ver.1 6.1.1.4.9 XEON_LINUX_redhat_Enterprise_ES4-64bit-6.1.1.4.9-release-GCC3.4.6 (xeon-redhat-linux-gnu) Dec 9 2014 16:06:42

  Or, the version can be checked on the banner when connecting to iSQL.

  $ is

  -----------------------------------------------------------------
   Altibase Client Query utility.
   Release Version 6.1.1.4.9
   Copyright 2000, ALTIBASE Corporation or its subsidiaries.
   All Rights Reserved.
  -----------------------------------------------------------------

## When occurs while connected to the Altibase server

---

### When the session is terminated by an Altibase server property

- If the session is terminated by the Altibase server properties FETCH_TIMEOUT, UTRANS_TIMEOUT, IDLE_TIMEOUT, a communication failure message may occur in the client.
- For this reason, if the session is terminated, an error message stating that the session was terminated due to the timeout setting remains in the altibase_boot.log on the Altibase server side as shown below. (altibase_boot.log is located under the $ALTIBASE_HOME/trc directory. $ALTIBASE_HOME is the installation location of the Altibase server.)

  **Ex) ALTIBASE HDB 6.3.1 - altibase_boot.log**

  ```
  [2016/02/02 10:08:56] [Thread-140294005577504] [Level-1]
  [Notify : Idle Timeout] Session Closed by Server : Session ID = 1
      CLIENT_INFO           => TCP 127.0.0.1:29881(PID : 6881)
      Time Limit            => 3
      Running Time          => 6
  ```

  **Ex) ALTIBASE HDB 4.3.9 - altibase_boot.log**

  ```
  [2016/02/02 09:30:50] [Thread-139691805542144] [Level-1]
  [Notify : Idle Timeout] Session Closed by Server : Session ID = 14

  [2016/02/02 09:30:50] [Thread-139691805542144] [Level-1]
           Time   Limit => 3
           Running Time => 3
  ```
- Please refer to the page below for details on session properties and how to take action.
    - FETCH_TIMEOUT : [\[Notify : Fetch Timeout\] Session Closed by Server.](https://docs.altibase.com/pages/viewpage.action?pageId=16876301)
    - UTRANS_TIMEOUT : [Monitoring method when undo tablespace usage increases](https://aid.altibase.com/display/FAQE/Monitoring+method+when+undo+tablespace+usage+increases)
    - IDLE_TIMEOUT : [Database Security Checklist](https://aid.altibase.com/display/FAQE/Database+Security+Checklist)

### When the session is terminated by the sysdba user

- sysdba ALTER DATABASE *database_name* SESSION CLOSE *session_id*; Communication failure error may occur even if the session is forcibly terminated with a sentence.
- In this case, no additional error information is left on the Altibase server or client-side.

## When running the database server

---

If the Altibase server properties are not set correctly, a communication failure error may occur when the Altibase server is started up. In some cases, it may be difficult to find the cause with the log displayed on the terminal, so find out which property is caused by the following information.

- Log output on terminal
- altibase_boot.log file (located in $ALTIBASE_HOME/trc, $ALTIBASE_HOME is the installation location of the Altibase server.)
- altibase.properties file (located in $ALTIBASE_HOME/conf)
