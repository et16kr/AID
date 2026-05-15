---
title: "Miscellaneous queries"
page_id: "1802687"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Miscellaneous+queries"
updated_at: "2011-07-22T12:54:04.000+0900"
version: 4
ancestors: ["Home", "ALTIBASE HDB Administration", "Useful SQL"]
labels: []
---

# Miscellaneous queries
Source: https://docs.altibase.com/display/FAQE/Miscellaneous+queries
Updated: 2011-07-22T12:54:04.000+0900

- [State of a service thread](#Miscellaneousqueries-Stateofaservicethread)
    - [ALTIBASE HDB V4](#Miscellaneousqueries-ALTIBASEHDBV4)
    - [ALTIBASE HDB V5](#Miscellaneousqueries-ALTIBASEHDBV5)
- [Lock & Transaction Information](#Miscellaneousqueries-Lock&TransactionInformation)
    - [ALTIBASE HDB V4](#Miscellaneousqueries-ALTIBASEHDBV4.1)
    - [ALTIBASE HDB V5](#Miscellaneousqueries-ALTIBASEHDBV5.1)
- [Redo log files](#Miscellaneousqueries-Redologfiles)
- [Cumulative count of total transaction waits due to logging](#Miscellaneousqueries-Cumulativecountoftotaltransactionwaitsduetologging)
- [Memory Ager GAP](#Miscellaneousqueries-MemoryAgerGAP)
- [Finding a query which blocks ager from aging.](#Miscellaneousqueries-Findingaquerywhichblocksagerfromaging.)
- [Memory status](#Miscellaneousqueries-Memorystatus)
- [Total memory usage of ALTIBASE](#Miscellaneousqueries-TotalmemoryusageofALTIBASE)

# State of a service thread

This query shows the state of a service thread.

| Column Name | Description |
| --- | --- |
| RUN_MODE | the type of service thread. (dedicated or shared) |
| STATE | currenly working state (executing / pool) |
| CNT | the number of threads in the run_mode and state |

## ALTIBASE HDB V4

```
SELECT 	TYPE RUN_MODE,
        STATE,
        COUNT(*) CNT
FROM    V$SERVICE_THREAD
GROUP BY RUN_MODE, STATE
```

## ALTIBASE HDB V5

```
SELECT 	RUN_MODE,
        STATE,
        COUNT(*) CNT
FROM    V$SERVICE_THREAD
GROUP BY RUN_MODE, STATE
```

# Lock & Transaction Information

This query shows the lock & transaction information including replication transactions.

| Column Name | Description |
| --- | --- |
| TX_ID | current transaction id |
| BLOCKED_TX_ID | the transaction id which current transaction is waiting for |
| STATUS | current transaction's status |
| USER_NAME | the user name who has issued the current transaction |
| SESSION_ID | the session id which has issued the current transaction |
| CLIENT_IP | client IP address |
| AUTOCOMMIT | autocommit |
| LOCK_DESC | Lock description |
| FIRST_UPDATE_TIME | the first update time of current transaction |
| TABLE_NAME | table_name |
| CURRENT_QUERY | current query in the current transaction |
| DDL | DDL or not |
| LOGFILE# | logfile number |

## ALTIBASE HDB V4

ALTIBASE HDB V4 does not support this features.

## ALTIBASE HDB V5

```
SELECT 	TX.ID TX_ID,
        WAIT_FOR_TRANS_ID BLOCKED_TX_ID,
        DECODE(TX.STATUS, 0, 'BEGIN', 1, 'PRECOMMIT', 2, 'COMMIT_IN_MEMORY', 3, 'COMMIT', 4, 'ABORT', 5, 'BLOCKED', 6, 'END') STATUS,
        DECODE(TX.LOG_TYPE, 0, U1.USER_NAME, 'REPLICATION') USER_NAME,
        DECODE(TX.LOG_TYPE, 0, TX.SESSION_ID, RT.REP_NAME) SESSION_ID,
        DECODE(TX.LOG_TYPE, 0, ST.COMM_NAME, RR.PEER_IP) CLIENT_IP,
        DECODE(ST.AUTOCOMMIT_FLAG, 1, 'ON', 'OFF') AUTOCOMMIT,
        L.LOCK_DESC,
        DECODE(TX.FIRST_UPDATE_TIME, 0, '0', TO_CHAR(TO_DATE('1970010109','YYYYMMDDHH') + TX.FIRST_UPDATE_TIME / (60*60*24), 'MM/DD HH:MI:SS')) FIRST_UPDATE_TIME,
        U2.USER_NAME||'.'||T.TABLE_NAME TABLE_NAME,
        DECODE(TX.LOG_TYPE, 0, SUBSTR(ST.QUERY, 1, 10), 'REMOTE TX_ID '||REMOTE_TID) CURRENT_QUERY,
        DECODE(TX.DDL_FLAG,0, 'NON-DDL', 'DDL') DDL,
        DECODE(TX.FIRST_UNDO_NEXT_LSN_FILENO, -1, '-', TX.FIRST_UNDO_NEXT_LSN_FILENO) 'LOGFILE#'
FROM 	  V$TRANSACTION TX,
        V$LOCK L LEFT OUTER JOIN
        (
          SELECT ST.*,
                 SS.AUTOCOMMIT_FLAG,
                 SS.DB_USERID,
                 SS.COMM_NAME
          FROM 	 V$STATEMENT ST,
                 V$SESSION SS
          WHERE  SS.ID = ST.SESSION_ID
                 AND SS.CURRENT_STMT_ID = ST.ID
         ) ST ON L.TRANS_ID = ST.TX_ID LEFT OUTER JOIN
         V$REPRECEIVER_TRANSTBL RT ON L.TRANS_ID = RT.LOCAL_TID LEFT OUTER JOIN
         V$REPRECEIVER RR ON RT.REP_NAME = RR.REP_NAME LEFT OUTER JOIN
         V$LOCK_WAIT LW ON L.TRANS_ID = LW.TRANS_ID LEFT OUTER JOIN
         SYSTEM_.SYS_USERS_ U1 ON ST.DB_USERID = U1.USER_ID,
         SYSTEM_.SYS_TABLES_ T LEFT OUTER JOIN
         SYSTEM_.SYS_USERS_ U2 ON T.USER_ID = U2.USER_ID
WHERE 	 TX.ID = L.TRANS_ID AND T.TABLE_OID = L.TABLE_OID AND TX.STATUS != 6 -- 6:END
ORDER BY TX.ID, ST.ID, TX.FIRST_UPDATE_TIME DESC ;
```

# Redo log files

This query shows the information of transaction log files

| Column Name | Description |
| --- | --- |
| OLDEST_LOG_FILE | the oldest log file in LOG_DIR |
| CURRENT_LOG_FILE | the current log file number which service thread is writing to. |
| LOG_FILE_GAP | the interval between CURRENT_LOG_FILE and OLDEST_LOG_FILE |

```
SELECT 	OLDEST_ACTIVE_LOGFILE OLDEST_LOGFILE,
        CURRENT_LOGFILE CURRENT_LOGFILE,
        CURRENT_LOGFILE-OLDEST_ACTIVE_LOGFILE LOGFILE_GAP
FROM V$ARCHIVE ;
```

# Cumulative count of total transaction waits due to logging

This query shows the number of total waits due to lack of the log space exhaustion for logging. If the value returns non-zero value, you'd better increase PREPARE_LOG_FILE_COUNT in altibase.properties.

```
SELECT 	LF_PREPARE_WAIT_COUNT
FROM V$LFG;
```

# Memory Ager GAP

This query shows the memory ager thread's information.

| Column Name | Description |
| --- | --- |
| GC_NAME | the Ager name. (LOGICAL_AGER for index aging , DELTHRD for data aging) |
| SCNOFTAIL | The commit SCN of the tail in garbage collection OID list |
| MINMEMSCNINTXS | The lowest of the view SCNs for memory-related transactions |
| GC_GAP | the OID count which ager has to proceed |

```
SELECT 	GC_NAME,
        SCNOFTAIL,
        MINMEMSCNINTXS,
        ADD_OID_CNT-GC_OID_CNT GC_GAP
FROM V$MEMGC ;
```

# Finding a query which blocks ager from aging.

Aging process will be blocked if there's a transaction which refers the aging target. This query shows the query which blocks from aging.

| Column Name | Description |
| --- | --- |
| SESSION_ID | the session identifier |
| TOTAL_TIME | total elapsed time |
| EXECUTE_TIME | the elapsed time for query execution |
| TX_ID | transaction identifier |
| QUERY | query string |

```
SELECT 	SESSION_ID,
        TOTAL_TIME,
        EXECUTE_TIME,
        TX_ID,
        QUERY
FROM 		V$STATEMENT
WHERE TX_ID IN  (
									SELECT ID
									FROM V$TRANSACTION
									WHERE MEMORY_VIEW_SCN = (
									       SELECT MINMEMSCNINTXS
									       FROM V$MEMGC
									       LIMIT 1
									        )
								) AND EXECUTE_FLAG = 1
ORDER BY 2 DESC ;
```

# Memory status

This query shows the memory state arranged by ALTIBASE module.

| Column Name | Description |
| --- | --- |
| NAME | the name of ALTIBASE module |
| ALLOC_MAX(M) | max alloc size of memory |
| ALLOC(M) | current size of memory |

```
SELECT 	NAME,
	      ROUND(MAX_TOTAL_SIZE/1024/1024) 'ALLOC_MAX(M)',
	      ROUND(ALLOC_SIZE/1024/1024) 'ALLOC(M)'
FROM 	  V$MEMSTAT
ORDER BY 3 DESC ;
```

# Total memory usage of ALTIBASE

This query shows the total memory state.

| Column Name | Description |
| --- | --- |
| ALLOC_MAX(M) | max alloc size of memory |
| ALLOC(M) | current size of memory |

```
SELECT 	ROUND(SUM(MAX_TOTAL_SIZE)/1024/1024) 'ALLOC_MAX(M)',
        ROUND(SUM(ALLOC_SIZE)/1024/1024) 'ALLOC(M)'
FROM V$MEMSTAT ;
```
