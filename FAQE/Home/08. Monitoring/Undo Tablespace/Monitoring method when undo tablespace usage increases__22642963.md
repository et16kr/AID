---
title: "Monitoring method when undo tablespace usage increases"
page_id: "22642963"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Monitoring+method+when+undo+tablespace+usage+increases"
updated_at: "2026-04-13T14:03:34.000+0900"
version: 2
ancestors: ["Home", "08. Monitoring", "Undo Tablespace"]
labels: []
---

# Monitoring method when undo tablespace usage increases
Source: https://docs.altibase.com/display/FAQE/Monitoring+method+when+undo+tablespace+usage+increases
Updated: 2026-04-13T14:03:34.000+0900

- [1. Overview](#Monitoringmethodwhenundotablespaceusageincreases-1.Overview) - [2. Monitoring Query](#Monitoringmethodwhenundotablespaceusageincreases-2.MonitoringQuery) - [3. Key Items to Check During Monitoring](#Monitoringmethodwhenundotablespaceusageincreases-3.KeyItemstoCheckDuringMonitoring) - [4. Diagnostic Criteria by Scenario](#Monitoringmethodwhenundotablespaceusageincreases-4.DiagnosticCriteriabyScenario) - [4.1 Long-Running Update Transactions](#Monitoringmethodwhenundotablespaceusageincreases-4.1Long-RunningUpdateTransactions) - [4.2 Long-Running Open Update Transactions](#Monitoringmethodwhenundotablespaceusageincreases-4.2Long-RunningOpenUpdateTransactions) - [4.3 Statements Accessing Pre-Change Data for an Extended Period](#Monitoringmethodwhenundotablespaceusageincreases-4.3StatementsAccessingPre-ChangeDataforanExtendedPeriod) - [4.4 Open LOB Access in Non-Autocommit Mode](#Monitoringmethodwhenundotablespaceusageincreases-4.4OpenLOBAccessinNon-AutocommitMode) - [4.5 Transactions Undergoing Rollback](#Monitoringmethodwhenundotablespaceusageincreases-4.5TransactionsUndergoingRollback) - [4.6 Replication Transactions](#Monitoringmethodwhenundotablespaceusageincreases-4.6ReplicationTransactions) - [5. Corrective Actions](#Monitoringmethodwhenundotablespaceusageincreases-5.CorrectiveActions) - [5.1 Expanding the Undo Tablespace](#Monitoringmethodwhenundotablespaceusageincreases-5.1ExpandingtheUndoTablespace) - [5.2 Terminating Sessions](#Monitoringmethodwhenundotablespaceusageincreases-5.2TerminatingSessions) - [6. Preventing Undo Tablespace Growth](#Monitoringmethodwhenundotablespaceusageincreases-6.PreventingUndoTablespaceGrowth) - [6.1 Splitting Large Transactions](#Monitoringmethodwhenundotablespaceusageincreases-6.1SplittingLargeTransactions) - [6.2 Configuring UTRANS_TIMEOUT](#Monitoringmethodwhenundotablespaceusageincreases-6.2ConfiguringUTRANS_TIMEOUT) - [6.3 Checking for Uncommitted Transactions](#Monitoringmethodwhenundotablespaceusageincreases-6.3CheckingforUncommittedTransactions) - [6.4 Releasing LOB Resources](#Monitoringmethodwhenundotablespaceusageincreases-6.4ReleasingLOBResources)

# **1. Overview**

---

When undo tablespace usage continues to increase or does not decrease, it is necessary to accurately identify the root cause and take appropriate actions accordingly.

In general, undo usage increases or is not released in the following situations:

- **Long-running update transactions**: When DML transactions on disk tables do not terminate and continue for a long time
- **Uncommitted transactions**: When SQL execution is completed but the transaction remains open because a COMMIT or ROLLBACK has not been performed
- **Undo image reference**: When a query session references pre-change data, preventing the undo area from being reused and causing it to be retained for a long time
- **LOB resources not released**: When LOB data is queried in non-autocommit mode and the LOB cursor or transaction is not properly closed in a timely manner
- **Ongoing rollback**: When a large transaction is canceled and the recovery process takes a long time

This document describes key monitoring items to diagnose the causes of increasing undo usage and provides guidance on corrective and preventive actions for each scenario.

# **2. Monitoring Query**

---

If the undo tablespace usage does not decrease or continues to increase, it is necessary to identify the transactions that are using undo or accessing undo images, along with their status.

The following query can be used to identify such transactions.

### **Altibase 5.3.3 or later**

```
SELECT DECODE(TX.LOG_TYPE, 1, REP.REP_NAME, TX.SESSION_ID) AS SESSION_ID                                    -- Session ID that performed the transaction. Or the replication object name
     , TX.ID AS TX_ID                                                                                       -- Transaction ID
     , ST.ID AS STATEMENT_ID                                                                                -- STATEMENT ID
     , DECODE(TX.TSS_RID,  0, 'SELECT', 'UPDATE') AS TX_TYPE                                                -- Transaction type
     , DECODE(TX.STATUS,   0, 'BEGIN',  1, 'PRECOMMIT', 2, 'COMMIT_IN_MEMORY',
                           3, 'COMMIT', 4, 'ABORT',     5, 'BLOCKED', 6, 'END') AS TX_STATUS                -- Transaction status
     , DECODE(ST.EXECUTE_FLAG, 1, 'SQL ING', 0, 'SQL END')                      AS SQL_STATUS               -- SQL status
     , DECODE(TX.LOG_TYPE,     1, 'REP '||REP.PEER_IP||':'||REP.PEER_PORT, S.COMM_NAME) AS CLIENT_IP        -- Client IP
     , S.CLIENT_PID AS CLIENT_PID                                                                           -- Client process ID
     , DECODE(S.AUTOCOMMIT_FLAG, 1, 'ON', 0, 'OFF') AS AUTOCOMMIT                                           -- AUTOCOMMIT MODE
     , S.UTRANS_TIME_LIMIT AS UTRANS_TIMEOUT                                                                -- UTRANS_TIMEOUT setting value of the session
     , DECODE(ST.LAST_QUERY_START_TIME, NULL, '', ST.LAST_QUERY_START_TIME) AS LAST_QUERY_START_TIME        -- SQL statement start time
     , CASE
           WHEN TX.DISK_VIEW_SCN LIKE 'INFINITE%' THEN ''
           ELSE LTRIM(TX.DISK_VIEW_SCN)
       END AS DISK_VIEW_SCN                                                                                 -- Minimum SCN visible to the query transaction
     , CASE
           WHEN TX.MIN_DISK_LOB_VIEW_SCN LIKE 'INFINITE%' THEN ''
           ELSE LTRIM(TX.MIN_DISK_LOB_VIEW_SCN)
       END AS MIN_DISK_LOB_VIEW_SCN                                                                         -- Minimum SCN visible to the transaction querying LOB data
     , ROUND(((UD_S.TOTAL_EXTENT_COUNT * UD_S.PAGE_COUNT_IN_EXTENT * 8192) / 1024), 2) AS 'UNDO_USED_KB'    -- Undo usage of the update transaction
     , ST.UNDO_READ_PAGE + ST.UNDO_GET_PAGE AS UNDO_PAGE_COUNT_COUNT                                              -- Undo pages
     , DECODE(TX.LOG_TYPE, 1, 'REMOTE_TX_ID : '||REP_TX.REMOTE_TID, LTRIM(ST.QUERY)) AS QUERY               -- Last query executed by the transaction
  FROM V$TRANSACTION TX
  LEFT JOIN (SELECT SESSION_ID
                  , TX_ID
                  , ID
                  , TO_CHAR(TO_DATE('1970010109','YYYYMMDDHH') + (LAST_QUERY_START_TIME) / (60*60*24), 'YYYY-MM-DD HH:MI:SS') LAST_QUERY_START_TIME
                  , EXECUTE_FLAG
                  , UNDO_READ_PAGE
                  , UNDO_GET_PAGE
                  , QUERY
               FROM V$STATEMENT
              WHERE (SESSION_ID, TX_ID, LAST_QUERY_START_TIME)
                 IN (SELECT SESSION_ID, TX_ID, MAX(LAST_QUERY_START_TIME) LAST_QUERY_START_TIME
                      FROM V$STATEMENT
                     GROUP BY SESSION_ID, TX_ID)) ST ON TX.ID = ST.TX_ID
  LEFT JOIN V$SESSION S         ON TX.SESSION_ID = S.ID
  LEFT JOIN V$REPRECEIVER_TRANSTBL REP_TX ON TX.ID = REP_TX.LOCAL_TID
  LEFT JOIN V$REPRECEIVER REP   ON REP_TX.REP_NAME = REP.REP_NAME
  LEFT JOIN V$TXSEGS TX_S       ON TX.ID = TX_S.TRANS_ID
  LEFT JOIN V$UDSEGS UD_S       ON TX_S.ID = UD_S.TXSEG_ENTRY_ID
 WHERE TX.TSS_RID <> 0                                      /* modified transaction */
    OR TX.MIN_DISK_LOB_VIEW_SCN NOT LIKE 'INFINITE%'        /* LOB access transaction */
    OR ((ST.UNDO_READ_PAGE <> 0 OR ST.UNDO_GET_PAGE <> 0)   /* transaction accessing undo pages */
         AND TX.DISK_VIEW_SCN NOT LIKE 'INFINITE%')
 ORDER BY SESSION_ID, TX_ID;
```

# **3. Key Items to Check During Monitoring**

---

When interpreting the monitoring results, analyze the following items with a focus to identify the root cause.

#### **Evaluation Criteria**

| Item | Description | Remarks |
| --- | --- | --- |
| SESSION_ID | Identifier of the session executing the transaction. | For replication transactions, the replication object name is displayed. |
| STATEMENT_ID | Identifier of the SQL statement within the transaction. | **NULL** indicates that the statement has been released. |
| TX_TYPE | Transaction type. | **UPDATE**: Transaction that has performed at least one DML operation.<br>**SELECT**: Read-only transaction |
| TX_STATUS | Transaction status. | **BEGIN**: Transaction is active.<br>**ABORT**: Transaction is undergoing rollback. |
| SQL_STATUS | Status of the SQL statement. | **SQL_ING**: Statement is in execution.<br>**SQL_END**: Execution has completed.<br>**NULL** indicates that the statement has been released. |
| CLIENT_IP | Information about client connection type, IP, PORT | For replication, displays the remote server IP and replication port.<br>**NULL** indicates that the session has ended. |
| CLIENT_PID | Client process ID | Client process ID.<br>**NULL** indicates that the session has ended. |
| AUTOCOMMIT | AutoCommit mode of the session. | **NULL** indicates that the session has ended. |
| DISK_VIEW_SCN | SCN of the undo image visible to the transaction. | Indicates that a previous version of the data is being queried. |
| MIN_DISK_LOB_VIEW_SCN | SCN of the undo image used by the LOB cursor. | Indicates that the LOB cursor is open. |
| UNDO_USED_KB | Size of undo currently used by the query | Size of the undo tablespace used by the update transaction. |
| UNDO_PAGE_COUNT | Number of undo pages accessed by the query | Indicates that undo pages are being accessed. |

# **4. Diagnostic Criteria by Scenario**

---

## **4.1 Long-Running Update Transactions**

---

Update transactions generate undo records for pre-change data, resulting in increased undo usage.

#### **Evaluation Criteria**

| Item | Value | Description |
| --- | --- | --- |
| TX_TYPE | UPDATE | Indicates a transaction that performs data modification |
| TX_STATUS | BEGIN | Transaction is active (not yet committed or rolled back) |
| SQL_STATUS | SQL_ING | SQL statement is currently executing |
| UNDO_USED_KB | Increasing | Indicates growth in undo usage |

※ Undo is also generated when inserting data into tables with foreign key constraints or triggers.

#### **Example Output**

The following example shows a SQL statement that modifies data and is currently in progress:

```
SESSION_ID            : 2
TX_ID                 : 8766080
STATEMENT_ID          : 131072
TX_TYPE               : UPDATE                       -- Transaction with data modification
TX_STATUS             : BEGIN
SQL_STATUS            : SQL ING                      -- SQL statement is in progress
CLIENT_IP             : TCP 127.0.0.1:32102
CLIENT_PID            : 123203
AUTOCOMMIT            : OFF
UTRANS_TIMEOUT        : 3600
LAST_QUERY_START_TIME : 2025-12-02 16:30:47
DISK_VIEW_SCN         : 962767
MIN_DISK_LOB_VIEW_SCN : 962767
UNDO_USED_KB          : 41728                 -- Undo usage increases while the update statement is executing
UNDO_PAGE_COUNT       : 1589737
QUERY                 : UPDATE dt SET c10 = SYSDATE
```

## **4.2 Long-Running Open Update Transactions**

---

If a transaction is not terminated after the SQL statement has completed, the undo segments used by the transaction are not released.

#### **Evaluation Criteria**

| Item | Value | Description |
| --- | --- | --- |
| TX_TYPE | UPDATE | Indicates a transaction that performs data modification |
| TX_STATUS | BEGIN | Transaction remains active (not yet committed or rolled back) |
| SQL_STATUS | SQL_END / NULL | SQL_END: Statement execution has completed<br>NULL: Statement has been closed (released) |
| UNDO_USED_KB | Stable | No further increase after the modifying statement has completed |

**Example Output**

**Case 1: Statement completed, transaction still open**

```
SESSION_ID            : 2
TX_ID                 : 8766080
STATEMENT_ID          : 131072
TX_TYPE               : UPDATE                       -- Transaction with data modification
TX_STATUS             : BEGIN                        -- Transaction remains open
SQL_STATUS            : SQL END                      -- Statement execution has completed
CLIENT_IP             : TCP 127.0.0.1:32102
CLIENT_PID            : 123203
AUTOCOMMIT            : OFF
UTRANS_TIMEOUT        : 3600
LAST_QUERY_START_TIME : 2025-12-02 16:30:47
DISK_VIEW_SCN         :                              -- SCN is cleared after statement completion
MIN_DISK_LOB_VIEW_SCN :                              -- SCN is cleared after statement completion
UNDO_USED_KB          : 71168                        -- Undo usage no longer increases after completion
UNDO_PAGE_COUNT       : 2003444
QUERY                 : UPDATE dt SET c10 = SYSDATE
```

**Case 2: Statement released, transaction still open**

```
SESSION_ID            : 3
TX_ID                 : 1862209
STATEMENT_ID          :
TX_TYPE               : UPDATE                       -- Transaction with data modification
TX_STATUS             : BEGIN                        -- Transaction remains open
SQL_STATUS            :                              -- Statement has been released
CLIENT_IP             : TCP 127.0.0.1:11046
CLIENT_PID            : 206764
AUTOCOMMIT            : OFF
UTRANS_TIMEOUT        : 3600
LAST_QUERY_START_TIME : 2026-01-15 10:51:50
DISK_VIEW_SCN         :
MIN_DISK_LOB_VIEW_SCN :
UNDO_USED_KB          : 256
UNDO_PAGE_COUNT       :
QUERY                 :
```

## **4.3 Statements Accessing Pre-Change Data for an Extended Period**

---

Undo segments are not released while a query continues to access undo images generated by update transactions.

#### **Evaluation Criteria**

| Item | Value | Description |
| --- | --- | --- |
| TX_TYPE | UPDATE / SELECT | UPDATE: Transaction that has performed at least one modification in the past<br>SELECT: Read-only transaction |
| SQL_STATUS | SQL_ING | Statement is currently executing |
| DISK_VIEW_SCN | SCN value | Indicates that a pre-update version of the data is being accessed |
| UNDO_USED_KB | NULL or stable | No increase in undo usage for read-only transactions or queries |
| UNDO_PAGE_COUNT | Increasing | Indicates active access to undo data If unchanged or 0, undo is not being accessed |

#### **Example Output**

**Case 1: Read-only transaction in progress**

```
SESSION_ID            : 9
TX_ID                 : 53804352
STATEMENT_ID          : 589824
TX_TYPE               : SELECT                       -- Read-only transaction
TX_STATUS             : BEGIN
SQL_STATUS            : SQL ING                      -- Statement is in execution
CLIENT_IP             : TCP 127.0.0.1:17731
CLIENT_PID            : 190617
AUTOCOMMIT            : ON
UTRANS_TIMEOUT        : 0
LAST_QUERY_START_TIME : 2025-12-05 14:12:24
DISK_VIEW_SCN         : 322663
MIN_DISK_LOB_VIEW_SCN : 322663
UNDO_USED_KB          :                              -- No undo usage for read-only transactions
UNDO_PAGE_COUNT       : 35207                        -- Increasing value indicates active undo access
QUERY                 : SELECT * FROM TEST_DISK_TBL;
```

**Case 2: Query within an update transaction accessing undo**

```
SESSION_ID            : 1
TX_ID                 : 3393
STATEMENT_ID          : 65537
TX_TYPE               : UPDATE                       -- Transaction that has performed modifications
TX_STATUS             : BEGIN
SQL_STATUS            : SQL ING                      -- Statement is in execution
CLIENT_IP             : TCP 127.0.0.1:46339
CLIENT_PID            : 102737
AUTOCOMMIT            : OFF
UTRANS_TIMEOUT        : 3600
LAST_QUERY_START_TIME : 2026-01-15 11:13:24
DISK_VIEW_SCN         : 801111
MIN_DISK_LOB_VIEW_SCN : 801111
UNDO_USED_KB          : 71168                        -- Undo usage remains stable during query execution
UNDO_PAGE_COUNT       : 3024517                      -- Increasing value indicates active undo access
QUERY                 : SELECT * FROM dt
```

## **4.4 Open LOB Access in Non-Autocommit Mode**

---

In non-autocommit mode, if a transaction is not completed after querying LOB data, or if only the statement is released without closing the LOB cursor, the associated undo segments are not released.

This can result in continuously increasing undo usage.

#### **Evaluation Criteria**

| Item | Value | Description |
| --- | --- | --- |
| TX_STATUS | BEGIN | Transaction remains active (not yet committed or rolled back) |
| MIN_DISK_LOB_VIEW_SCN | SCN value | Indicates that a LOB cursor is still open |

#### **Example Output**

**Case 1: Transaction remains open after querying LOB data**

```
SESSION_ID            : 4
TX_ID                 : 900929
STATEMENT_ID          : 589824
TX_TYPE               : SELECT
TX_STATUS             : BEGIN                        -- Transaction remains open
SQL_STATUS            : SQL END                      -- Statement execution has completed
CLIENT_IP             : TCP 127.0.0.1:49199
CLIENT_PID            : 170256
AUTOCOMMIT            : OFF
UTRANS_TIMEOUT        : 0
LAST_QUERY_START_TIME : 2025-12-05 14:12:24
DISK_VIEW_SCN         :
MIN_DISK_LOB_VIEW_SCN : 324055                       -- Presence of SCN indicates LOB data access
UNDO_USED_KB          :
UNDO_PAGE_COUNT       :
QUERY                 : SELECT * FROM demo_clob;
```

**Case 2: Statement released, but transaction and LOB cursor remain open**

```
SESSION_ID            : 4
TX_ID                 : 900929
STATEMENT_ID          :                              -- NULL indicates statement has been released
TX_TYPE               : SELECT
TX_STATUS             : BEGIN                        -- Transaction remains open
SQL_STATUS            :                              -- Statement has been released
CLIENT_IP             : TCP 127.0.0.1:49199
CLIENT_PID            : 170256
AUTOCOMMIT            : OFF
UTRANS_TIMEOUT        : 0
LAST_QUERY_START_TIME :
DISK_VIEW_SCN         :
MIN_DISK_LOB_VIEW_SCN : 324055                       -- Presence of SCN indicates LOB data access
UNDO_USED_KB          :
UNDO_PAGE_COUNT       :
QUERY                 :
```

## **4.5 Transactions Undergoing Rollback**

---

During rollback, undo segments are used to restore data to its previous state. Undo usage may be retained until the rollback operation completes.

#### **Evaluation Criteria**

| Item | Value | Description |
| --- | --- | --- |
| STATEMENT_ID | Numeric / NULL | Numeric: Session is active<br>NULL: Rollback continues after session termination |
| TX_TYPE | UPDATE | Transaction that performs data modifications |
| TX_STATUS | ABORT | Transaction is in rollback |

#### **Example Output**

**Case 1: Explicit rollback execution**

```
SESSION_ID            : 3
TX_ID                 : 155968
STATEMENT_ID          : 196609
TX_TYPE               : UPDATE                 -- Update transaction
TX_STATUS             : ABORT                  -- Rollback in progress
SQL_STATUS            : SQL ING
CLIENT_IP             : TCP 127.0.0.1:56757
CLIENT_PID            : 185015
AUTOCOMMIT            : OFF
UTRANS_TIMEOUT        : 0
LAST_QUERY_START_TIME : 2025-12-05 12:03:18
DISK_VIEW_SCN         :
MIN_DISK_LOB_VIEW_SCN :
UNDO_USED_KB          : 285696
UNDO_PAGE_COUNT       : 4045648
QUERY                 : rollback
```

**Case 2: Session terminated during rollback**

```
SESSION_ID            : 3
TX_ID                 : 155968
STATEMENT_ID          :
TX_TYPE               : UPDATE                 -- Update transaction
TX_STATUS             : ABORT                  -- Rollback in progress
SQL_STATUS            :
CLIENT_IP             :                        -- Session has been terminated
CLIENT_PID            :
AUTOCOMMIT            :
UTRANS_TIMEOUT        :
LAST_QUERY_START_TIME : 2025-12-05 12:03:18
DISK_VIEW_SCN         :
MIN_DISK_LOB_VIEW_SCN :
UNDO_USED_KB          : 285696
UNDO_PAGE_COUNT       : 4045648
QUERY                 :
```

## **4.6 Replication Transactions**

---

Undo may also be consumed by [replication transactions](https://manual.altibase.com/7.3/en/admin/replication/1.-Replication-Overview/#replication-transaction).

#### **Evaluation Criteria**

| Item | Value | Description |
| --- | --- | --- |
| SESSION_ID | Replication object name | Indicates a replication transaction |
| CLIENT_IP | Remote server IP | Displays the IP address and port of the remote server |
| TX_STATUS | BEGIN | Transaction is in progress |
| QUERY | REMOTE_TX_ID | Identifier of the source transaction |

#### **Example Output**

```
SESSION_ID            : REP                      -- Replication object name is displayed
TX_ID                 : 12354
STATEMENT_ID          :
TX_TYPE               : UPDATE
TX_STATUS             : BEGIN
SQL_STATUS            :
CLIENT_IP             : REP 192.168.1.145:53950
CLIENT_PID            :
AUTOCOMMIT            :
UTRANS_TIMEOUT        :
LAST_QUERY_START_TIME : 2025-12-05 17:22:31
DISK_VIEW_SCN         : 161183
MIN_DISK_LOB_VIEW_SCN : 161183
UNDO_USED_KB          : 19456
UNDO_PAGE_COUNT       : 18793
QUERY                 : REMOTE_TX_ID : 53835072
```

# **5. Corrective Actions**

---

When undo tablespace usage reaches a critical level, immediate actions can be categorized into two approaches: **expanding physical storage** and **removing the root cause (session/transaction)**.

## **5.1 Expanding the Undo Tablespace**

---

If insufficient undo space may impact service availability, increase the undo tablespace capacity. Before proceeding, ensure that sufficient free space is available in the underlying file system.

The following methods can be used:

#### **Method A: Add a Data File**

Additional space can be secured by adding a new data file to the existing tablespace. First, check the current data file configuration:

```
-- 1. Check current data file configuration
SELECT RPAD(T.NAME, 20) SPACE_NAME
     , ROUND((D.INITSIZE*T.PAGE_SIZE)/1024/1024) AS 'INITSIZE(MB)'
     , ROUND((D.CURRSIZE*T.PAGE_SIZE)/1024/1024) AS 'CURRSIZE(MB)'
     , DECODE(D.AUTOEXTEND, 0, 'OFF', 1, 'ON') 'AUTOEXTEND'
     , ROUND((D.NEXTSIZE*T.PAGE_SIZE)/1024/1024) AS 'NEXTSIZE(MB)'
     , DECODE(D.MAXSIZE, 0, ROUND((D.CURRSIZE*T.PAGE_SIZE)/1024/1024), ROUND((D.MAXSIZE*T.PAGE_SIZE)/1024/1024)) AS 'MAXSIZE(MB)'
     , D.NAME DATAFILE
  FROM V$TABLESPACES T, V$DATAFILES D
 WHERE T.ID = D.SPACEID AND T.TYPE = 7
 ORDER BY 7;

-- 2. Example: add a data file
ALTER TABLESPACE SYS_TBS_DISK_UNDO ADD DATAFILE 'undo002.dbf' AUTOEXTEND ON NEXT 1M MAXSIZE 2G;
```

#### **Method B: Resize an Existing Data File**

Capacity can also be increased by extending the size or maximum size of an existing data file.

```
-- 1. Example: When AUTOEXTEND is ON
ALTER TABLESPACE SYS_TBS_DISK_UNDO ALTER DATAFILE 'undo001.dbf' AUTOEXTEND ON NEXT 1M MAXSIZE 4G;

-- 2. Example: When AUTOEXTEND is OFF
ALTER TABLESPACE SYS_TBS_DISK_UNDO ALTER DATAFILE 'undo001.dbf' SIZE 4G;
```

## **5.2 Terminating Sessions**

---

If storage expansion is not feasible, or if a specific session is identified as the cause of excessive undo usage, the session can be terminated.

**Warning** Terminating a DML session processing a large volume of data may trigger rollback. In such cases, undo space may not be released immediately and will only be reclaimed after the rollback completes.

**Impact by Transaction Type**

| Transaction Type | Impact on Termination | Resource Release Timing |
| --- | --- | --- |
| SELECT | Can be terminated immediately | Immediately upon session termination |
| DML | Rollback is performed | After rollback completes |

#### **Terminating a Session**

After identifying the database name from `V$DATABASE`, terminate the target session using the `SESSION_ID` obtained from the monitoring query.

```
ALTER DATABASE database_name SESSION CLOSE session_id ;
```

#### **Terminating a Client Process**

If the database session cannot be terminated normally or the connection must be closed at the application level, terminate the client process at the OS level.

```
$ kill -9 <process_id>
```

The *`process_id`*can be obtained from the `CLIENT_IP` field in the monitoring query.

# **6. Preventing Undo Tablespace Growth**

---

Long-running transactions (bulk transactions) are a primary cause of increased undo tablespace usage, as changes remain uncommitted for an extended period.

When large data modifications are processed within a single transaction, the following issues may occur:

- **Rapid growth of undo space**: Undo segments for before images can increase significantly in a short period
- **Delayed space reuse**: Undo cannot be reused until the transaction is completed (COMMIT or ROLLBACK)
- **Increased rollback overhead**: In case of failure or cancellation, a larger volume of undo must be processed, potentially resulting in rollback time exceeding the original execution time

To mitigate these issues, review the following recommendations and optimize transaction handling accordingly.

## **6.1 Splitting Large Transactions**

---

Instead of processing a large volume of data in a single transaction, divide the workload into smaller batches.

This approach improves undo reuse and reduces overall undo pressure.

In addition, it minimizes the scope of recovery required in case of rollback.

#### **Example**

**Method 1: Using Range Conditions (BETWEEN ~ AND)**

Divide the workload into ranges based on a primary key or indexed column, and commit after each batch.

```
-- Delete rows 1–1000 and commit
DELETE FROM emp WHERE eno BETWEEN 1 AND 1000;
COMMIT;

-- Delete rows 1001–2000 and commit
DELETE FROM emp WHERE eno BETWEEN 1001 AND 2000;
COMMIT;

-- Delete rows 2001–3000 and commit
DELETE FROM emp WHERE eno BETWEEN 2001 AND 3000;
COMMIT;
```

**Method 2: Using Row Limiting (LIMIT)**

Repeatedly delete a fixed number of rows that match a condition.

```
-- Delete up to 1,000 rows per execution (repeat as needed)
DELETE FROM emp WHERE status = 'D' LIMIT 1000;
COMMIT;
```

## **6.2 Configuring UTRANS_TIMEOUT**

---

If update transactions remain active for an extended period, undo images are retained longer, which can lead to increased undo usage.

To mitigate this, configure `UTRANS_TIMEOUT` so that transactions exceeding a defined duration are automatically terminated and rolled back.

#### **Session-Level Configuration**

**iSQL example**

```
ALTER SESSION SET UTRANS_TIMEOUT = 3600;   -- Unit: seconds
```

**Connection string examples**

- **Java**

  ```
  sProps.put("utrans_timeout", "300");
  Connection con = DriverManager.getConnection(url, sProps);
  ```

- **APRE**

  ```
  strcpy(conn_opt3, "DSN=localhost;CONNTYPE=1;UTRANS_TIMEOUT=300");
  EXEC SQL CONNECT :usr IDENTIFIED BY :pwd USING :conn_opt3;
  ```

#### **System-Level Configuration**

Executing the following statement applies the setting to all new sessions:

```
ALTER SYSTEM SET UTRANS_TIMEOUT = 3600;   -- unit: seconds
```

For persistent configuration, update the properties file:

```
$ vi $ALTIBASE_HOME/conf/altibase.properties
UTRANS_TIMEOUT = 3600
```

## **6.3 Checking for Uncommitted Transactions**

---

In applications using non-autocommit mode, ensure that transactions are not left open (idle) due to missing exception handling or incomplete logic.

At the end of business logic, a `COMMIT` or `ROLLBACK` must always be explicitly issued.

## **6.4 Releasing LOB Resources**

---

LOB cursors created during LOB operations retain undo data until the transaction is completed or the cursor is closed.

After processing LOB data, ensure that one of the following actions is performed:

- Close the LOB cursor
- Complete the transaction (COMMIT or ROLLBACK)

> **Warning:** The `SQLFreeLob()` function in SQLCLI does not immediately send a request to the server. Instead, it is transmitted together with subsequent requests. As a result, there may be a delay between the client-side call and the actual release of LOB resources on the server.
>
> If immediate resource release is required, completing the transaction is the most reliable approach.
