---
title: "How to terminate a session"
page_id: "1802689"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/How+to+terminate+a+session"
updated_at: "2011-07-22T12:46:31.000+0900"
version: 11
ancestors: ["Home", "ALTIBASE HDB Administration"]
labels: []
---

# How to terminate a session
Source: https://docs.altibase.com/display/FAQE/How+to+terminate+a+session
Updated: 2011-07-22T12:46:31.000+0900

# About this document.

|  |  |
| --- | --- |
| Purpose | This document explains how to terminate a session in ALTIBASE HDB. |
| Applied to | 4.3.9 or later |
| Prerequisite | Administrator's Manual |

# Description

You may want to terminate an ALTIBASE HDB session in abnormal behavior. In order to terminate the session, you have to connect to ALTIBASE HDB as SYSDBA.

Only SYSDBA can terminate a session.

1. **Connecting as SYSDBA**

  ```
  -bash-3.00$ isql -SYSDBA
  -----------------------------------------------------------------
       Altibase Client Query utility.
       Release Version 5.5.1.0.4
       Copyright 2000, ALTIBASE Corporation or its subsidiaries.
       All Rights Reserved.
  -----------------------------------------------------------------
  Write UserID : sys
  Write Password :
  ISQL_CONNECTION = UNIX, SERVER = localhost, PORT_NO = 27562
  iSQL(SYSDBA)>
  ```
2. **Finding the session identifier which you want to terminate.**
   Assume that there is a session connected from "192.168.1.84", and you want to terminate that session.

  ```
  iSQL(SYSDBA)> SELECT id, comm_name FROM v$session;
  ID          COMM_NAME
  ---------------------------------------------------------------------------------
  4           UNIX
  5           TCP 192.168.1.84:35679
  2 rows selected.
  ```

   The session identifier which you want to terminate is "5".
3. **Terminating the session.**
   You can use the query below to terminate the session by specifying the session identifier.

  ```
  ALTER DATABASE MYDB SESSION CLOSE [session identifier];
  ```

You can terminate the session #5 and verify that is terminated as shown below:

```
iSQL(SYSDBA)> alter database mydb session close 5;
Alter success.
iSQL(SYSDBA)> SELECT id, comm_name FROM v$session;
ID          COMM_NAME
---------------------------------------------------------------------------------
4           UNIX
1 row selected.
```

If an active transaction is running on the session, ALTIBASE HDB rollbacks the transaction before terminating the session. Therefore, sometimes, terminating a session may not work immediately.
