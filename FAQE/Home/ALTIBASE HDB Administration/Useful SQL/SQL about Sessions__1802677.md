---
title: "SQL about Sessions"
page_id: "1802677"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/SQL+about+Sessions"
updated_at: "2011-07-22T16:25:11.000+0900"
version: 4
ancestors: ["Home", "ALTIBASE HDB Administration", "Useful SQL"]
labels: []
---

# SQL about Sessions
Source: https://docs.altibase.com/display/FAQE/SQL+about+Sessions
Updated: 2011-07-22T16:25:11.000+0900

- [Total number of sessions](#SQLaboutSessions-Totalnumberofsessions)
- [Session Information](#SQLaboutSessions-SessionInformation)
    - [ALTIBASE HDB 4](#SQLaboutSessions-ALTIBASEHDB4)
    - [ALTIBASE HDB 5](#SQLaboutSessions-ALTIBASEHDB5)
- [Session information connected as SYSDBA](#SQLaboutSessions-SessioninformationconnectedasSYSDBA)
    - [ALTIBASE HDB 4](#SQLaboutSessions-ALTIBASEHDB4.1)
    - [ALTIBASE HDB 5](#SQLaboutSessions-ALTIBASEHDB5.1)

# Total number of sessions

This query returns the number of sessions which are currently established.

```
SELECT  COUNT(*) TOTAL_SESSION_CNT
FROM    V$SESSION ;
```

# Session Information

This query returns the information about a session.

| Column Name | Description |  |
| --- | --- | --- |
| SESSSION_ID | the unique identifier of the session |  |
| USER_NAME | the database user name |  |
| CLIENT_IP | the client IP address |  |
| CLIENT_APP_INFO | the type of client application | not supported in ALTIBASE HDB 4 |
| CLIENT_PID | the client process idenfier |  |
| SESSION_STATE | the status of the session |  |
| AUTOCOMMIT | the autocommit mode |  |
| LOGIN_TIME | the time when the session is established |  |
| IDLE_TIME | the time when the session has been idle |  |
| CURRENT_QUERY | the query that the session has last executed | not supported in ALTIBASE HDB 4 |

## ALTIBASE HDB 4

```
SELECT  A.ID SESSION_ID,
        A.DB_USERNAME USER_NAME,
        REPLACE2(REPLACE2(A.COMM_NAME, 'SOCKET-', NULL), '-SERVER', NULL) CLIENT_IP,
        A.CLIENT_PID,
        A.SESSION_STATE,
        DECODE(A.AUTOCOMMIT_FLAG, 1, 'ON', 'OFF') AUTOCOMMIT,
        DECODE(A.LOGIN_TIME, 0, '-', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + A.LOGIN_TIME / (24*60*60), 'MM/DD HH:MI:SS')) LOGIN_TIME,
        DECODE(A.IDLE_START_TIME, 0, '-', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + A.IDLE_START_TIME / (24*60*60), 'MM/DD HH:MI:SS')) IDLE_TIME
FROM    V$SESSION A ;
```

## ALTIBASE HDB 5

```
SELECT  A.ID SESSION_ID,
        A.DB_USERNAME USER_NAME,
        REPLACE2(REPLACE2(A.COMM_NAME, 'SOCKET-', NULL), '-SERVER', NULL) CLIENT_IP,
        A.CLIENT_APP_INFO,
        A.CLIENT_PID,
        A.SESSION_STATE,
        DECODE(A.AUTOCOMMIT_FLAG, 1, 'ON', 'OFF') AUTOCOMMIT,
        DECODE(A.LOGIN_TIME, 0, '-', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + A.LOGIN_TIME / (24*60*60), 'MM/DD HH:MI:SS')) LOGIN_TIME,
        DECODE(A.IDLE_START_TIME, 0, '-', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + A.IDLE_START_TIME / (24*60*60), 'MM/DD HH:MI:SS')) IDLE_TIME,
        NVL(LTRIM(B.QUERY), 'NONE') CURRENT_QUERY
FROM    V$SESSION A LEFT OUTER JOIN
        V$STATEMENT B ON A.CURRENT_STMT_ID = B.ID ;
```

# Session information connected as SYSDBA

This query returns the information about a session which connects as SYSDBA .

| Column Name | Description |  |
| --- | --- | --- |
| SESSSION_ID | the unique identifier of the session |  |
| USER_NAME | the database user name |  |
| CLIENT_IP | the client IP address |  |
| CLIENT_APP_INFO | the type of client application | not supported in ALTIBASE HDB 4 |
| CLIENT_PID | the client process idenfier |  |
| SESSION_STATE | the status of sthe ession |  |
| AUTOCOMMIT | the autocommit mode |  |
| LOGIN_TIME | the time when the session is established |  |
| IDLE_TIME | the time when the session has been idle |  |
| CURRENT_QUERY | the query that the session last executed | not supported in ALTIBASE HDB 4 |

## ALTIBASE HDB 4

```
SELECT  A.ID SESSION_ID,
        A.DB_USERNAME USER_NAME,
        REPLACE2(REPLACE2(A.COMM_NAME, 'SOCKET-', NULL), '-SERVER', NULL) CLIENT_IP,
        A.CLIENT_PID,
        A.SESSION_STATE,
        DECODE(A.AUTOCOMMIT_FLAG, 1, 'ON', 'OFF') AUTOCOMMIT,
        DECODE(A.LOGIN_TIME, 0, '-', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + A.LOGIN_TIME / (24*60*60), 'MM/DD HH:MI:SS')) LOGIN_TIME,
        DECODE(A.IDLE_START_TIME, 0, '-', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + A.IDLE_START_TIME / (24*60*60), 'MM/DD HH:MI:SS')) IDLE_TIME
FROM    V$SESSION A
WHERE   A.SYSDBA_FLAG = 1;
```

## ALTIBASE HDB 5

```
SELECT  A.ID SESSION_ID,
        A.DB_USERNAME USER_NAME,
        REPLACE2(REPLACE2(A.COMM_NAME, 'SOCKET-', NULL), '-SERVER', NULL) CLIENT_IP,
        A.CLIENT_APP_INFO,
        A.CLIENT_PID,
        A.SESSION_STATE,
        DECODE(A.AUTOCOMMIT_FLAG, 1, 'ON', 'OFF') AUTOCOMMIT,
        DECODE(A.LOGIN_TIME, 0, '-', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + A.LOGIN_TIME / (24*60*60), 'MM/DD HH:MI:SS')) LOGIN_TIME,
        DECODE(A.IDLE_START_TIME, 0, '-', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + A.IDLE_START_TIME / (24*60*60), 'MM/DD HH:MI:SS')) IDLE_TIME,
        NVL(LTRIM(B.QUERY), 'NONE') CURRENT_QUERY
FROM    V$SESSION A LEFT OUTER JOIN
        V$STATEMENT B ON A.CURRENT_STMT_ID = B.ID
WHERE   A.SYSDBA_FLAG = 1;
```
