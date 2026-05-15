---
title: "SQL about Statements"
page_id: "1802679"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/SQL+about+Statements"
updated_at: "2011-07-22T16:49:35.000+0900"
version: 5
ancestors: ["Home", "ALTIBASE HDB Administration", "Useful SQL"]
labels: []
---

# SQL about Statements
Source: https://docs.altibase.com/display/FAQE/SQL+about+Statements
Updated: 2011-07-22T16:49:35.000+0900

- [Total number of statements](#SQLaboutStatements-Totalnumberofstatements)
- [Statement information](#SQLaboutStatements-Statementinformation)
- [The number of currently running statements](#SQLaboutStatements-Thenumberofcurrentlyrunningstatements)
- [Information about currently running statements](#SQLaboutStatements-Informationaboutcurrentlyrunningstatements)
- [Long running query ( over 10 seconds)](#SQLaboutStatements-Longrunningquery(over10seconds))
- [Long running transaction's last statement information (over 1 minute)](#SQLaboutStatements-Longrunningtransaction'slaststatementinformation(over1minute))
- [Information about a query running a FULL SCAN](#SQLaboutStatements-InformationaboutaqueryrunningaFULLSCAN)

# Total number of statements

This query returns the number of statements that currently are established.

```
SELECT  COUNT(*) STATEMENT_CNT
FROM    V$STATEMENT;
```

# Statement information

This query returns the information about statements, sorted in descending order by the execution time .

| Column Name | Description |
| --- | --- |
| SESSSION_ID | the unique identifier of the session |
| STMT_ID | the unique identifier of the statement in the session |
| TX_ID | the transaction identifier if the statement participates in a transaction |
| PREPARE_TIME | the time taken to perform preparing the statement. (microsecond) |
| FETCH_TIME | the time taken to perform a fetch operation (microsecond) |
| EXECUTE_TIME | the time taken to execute the statement (microsecond) |
| TOTAL_TIME | the total elapsed time |
| EXECUTE_FLAG | set 1 if the statement is currently executed |
| LAST_START_TIME | the time when the statement last started |
| QUERY | the query string |

```
SELECT  SESSION_ID,
        ID STMT_ID,
        TX_ID,
        (PARSE_TIME+VALIDATE_TIME+OPTIMIZE_TIME) PREPARE_TIME,
        FETCH_TIME,
        EXECUTE_TIME,
        TOTAL_TIME,
        EXECUTE_FLAG,
        DECODE(LAST_QUERY_START_TIME, 0, '-', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + LAST_QUERY_START_TIME / (24*60*60), 'MM/DD HH:MI:SS')) LAST_START_TIME,
        NVL(LTRIM(QUERY), 'NONE') QUERY
FROM    V$STATEMENT
ORDER BY EXECUTE_TIME DESC ;
```

# The number of currently running statements

This query returns the number of statements that are currently executing.

```
SELECT  COUNT(*) AS ACTIVE_STATEMENT_CNT
FROM    V$STATEMENT
WHERE   EXECUTE_FLAG = 1 ;
```

# Information about currently running statements

This query returns the statement information about those that are currently executing.

| Column Name | Description |
| --- | --- |
| SESSSION_ID | the unique identifier of the session |
| STMT_ID | the unique identifier of statement in the session |
| TX_ID | the transaction identifier if the statement participate in a transaction |
| PREPARE_TIME | the time taken to perform preparing the statement. (microsecond) |
| FETCH_TIME | the time taken to perform a fetch operation (microsecond) |
| EXECUTE_TIME | the time taken to execute the statement (microsecond) |
| TOTAL_TIME | the total elapsed time |
| EXECUTE_FLAG | set 1 if the statement is currently executed |
| LAST_START_TIME | the time when the statement last started |
| QUERY | the query string |

```
SELECT  SESSION_ID,
        ID STMT_ID,
        TX_ID,
        (PARSE_TIME+VALIDATE_TIME+OPTIMIZE_TIME) PREPARE_TIME,
        FETCH_TIME,
        EXECUTE_TIME,
        TOTAL_TIME,
        DECODE(LAST_QUERY_START_TIME, 0, '-', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + LAST_QUERY_START_TIME / (24*60*60), 'MM/DD HH:MI:SS')) LAST_START_TIME,
        NVL(LTRIM(QUERY), 'NONE') QUERY
FROM    V$STATEMENT
WHERE   EXECUTE_FLAG = 1
ORDER BY EXECUTE_TIME DESC ;
```

# Long running query ( over 10 seconds)

This query returns the statement information about queries that are considered long running. (the queries with elapsed time over 10 seconds)

| Column Name | Description |
| --- | --- |
| SESSSION_ID | the unique identifier of the session |
| STMT_ID | the unique identifier of statement in the session |
| TX_ID | the transaction identifier if the statement participate in a transaction |
| PREPARE_TIME | the time taken to perform preparing statement. (microsecond) |
| FETCH_TIME | the time taken to perform a fetch operation (microsecond) |
| EXECUTE_TIME | the time taken to execute statement (microsecond) |
| TOTAL_TIME | the total elapsed time |
| EXECUTE_FLAG | set 1 if the statement is currently executed |
| LAST_START_TIME | the time when the statement last started |
| QUERY | the query string |

```
SELECT  SESSION_ID,
        ID STMT_ID,
        TX_ID,
        (PARSE_TIME+VALIDATE_TIME+OPTIMIZE_TIME) PREPARE_TIME,
        FETCH_TIME,
        EXECUTE_TIME,
        TOTAL_TIME,
        DECODE(LAST_QUERY_START_TIME, 0, '-', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + LAST_QUERY_START_TIME / (24*60*60), 'MM/DD HH:MI:SS')) LAST_START_TIME,
        NVL(LTRIM(QUERY), 'NONE') QUERY
FROM    V$STATEMENT
WHERE   EXECUTE_FLAG = 1 AND EXECUTE_TIME/1000000 > 10
ORDER BY EXECUTE_TIME DESC ;
```

# Long running transaction's last statement information (over 1 minute)

In the case of long running transactions in ALTIBASE HDB, this query shows the information for the last query of a transaction with an elapsed time over 1 minute.

| Column Name | Description |
| --- | --- |
| SESSSION_ID | the unique identifier of the session |
| CLIENT_IP | the client IP address |
| CLIENT_PID | the client process identifier |
| UTRANS_TIME | the time taken during the transaction. (microsecond) |
| EXECUTE_TIME | the time taken to execute statement (microsecond) |
| TOTAL_TIME | the total elapsed time |
| LAST_START_TIME | the time when the statement last started |
| QUERY | the query string |

```
SELECT 	ST.SESSION_ID,
        SS.COMM_NAME CLIENT_IP,
        SS.CLIENT_PID,
        (BASE_TIME - TR.FIRST_UPDATE_TIME) AS UTRANS_TIME,
        EXECUTE_TIME,
        TOTAL_TIME,
        DECODE(LAST_QUERY_START_TIME, 0, '-', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + LAST_QUERY_START_TIME / (24*60*60), 'MM/DD HH:MI:SS')) LAST_START_TIME,
        NVL(LTRIM(ST.QUERY), 'NONE') QUERY
FROM 	V$TRANSACTION TR,
        V$STATEMENT ST,
        V$SESSIONMGR,
        V$SESSION SS
WHERE   TR.ID = ST.TX_ID
        AND ST.SESSION_ID = SS.ID
        AND TR.FIRST_UPDATE_TIME != 0 -- 0:READ ONLY TRANSACTION
        AND (BASE_TIME - TR.FIRST_UPDATE_TIME) > 60
ORDER BY UTRANS_TIME DESC ;
```

# Information about a query running a FULL SCAN

This query shows the information about a query that is running a FULL SCAN. You need to be careful and check the SQL if there is a FULL SCAN plan node in the statement.

| Column Name | Description |
| --- | --- |
| SESSSION_ID | the unique identifier of the session |
| CLIENT_IP | the client IP address |
| CLIENT_PID | the client process identifier |
| LAST_START_TIME | the time when the statement last started |
| PREPARE_TIME | the time taken to perform preparing statement. (microsecond) |
| FETCH_TIME | the time taken to perform a fetch operation (microsecond) |
| EXECUTE_TIME | the time taken to execute statement (microsecond) |
| TOTAL_TIME | the total elapsed time |
| QUERY | the query string |

```
SELECT 	SESSION_ID,
        S.COMM_NAME CLIENT_IP,
        S.CLIENT_PID,
        DECODE(LAST_QUERY_START_TIME, 0, '-', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + LAST_QUERY_START_TIME / (24*60*60), 'MM/DD HH:MI:SS')) LAST_START_TIME,
        (PARSE_TIME+VALIDATE_TIME+OPTIMIZE_TIME) PREPARE_TIME,
        FETCH_TIME,
        EXECUTE_TIME,
        TOTAL_TIME,
        NVL(LTRIM(QUERY), 'NONE') QUERY
FROM    V$STATEMENT T,
        V$SESSION S
WHERE   S.ID = T.SESSION_ID
        AND (MEM_CURSOR_FULL_SCAN > 0 OR DISK_CURSOR_FULL_SCAN > 0)
        AND UPPER(QUERY) NOT LIKE '%INSERT%'
ORDER BY EXECUTE_TIME DESC ;
```
