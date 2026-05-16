---
title: "How to determine which queries are being rolled back"
page_id: "16876296"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/How+to+determine+which+queries+are+being+rolled+back"
updated_at: "2021-04-05T10:45:10.000+0900"
version: 2
ancestors: ["Home", "08. Monitoring"]
labels: []
---

# How to determine which queries are being rolled back
Source: https://docs.altibase.com/display/FAQE/How+to+determine+which+queries+are+being+rolled+back
Updated: 2021-04-05T10:45:10.000+0900

# - [Overview](#Howtodeterminewhichqueriesarebeingrolledback-Overview) - [Version](#Howtodeterminewhichqueriesarebeingrolledback-Version) - [How to check](#Howtodeterminewhichqueriesarebeingrolledback-Howtocheck) - [Method that can be used in ALTIBASE HDB 5.1.5 or higher](#Howtodeterminewhichqueriesarebeingrolledback-MethodthatcanbeusedinALTIBASEHDB5.1.5orhigher) - [Method changed starting from ALTIBASE HDB version 6.1.1.2.0](#Howtodeterminewhichqueriesarebeingrolledback-MethodchangedstartingfromALTIBASEHDBversion6.1.1.2.0)

# Overview

---

When a change transaction is in progress, if the session is forcibly disconnected or the transaction is aborted by a session timeout setting, the transaction is rolled back.

Here's how to check which queries are being rolled back.

# Version

---

Altibase version 5.1.5 or later

# How to check

---

## Method that can be used in ALTIBASE HDB 5.1.5 or higher

If the values of the CURRENT_UNDO_NEXT_LSN_FILENO column and CURRENT_UNDO_NEXT_LSN_OFFSET column are gradually decreasing in the query execution result below, it appears that the transaction is being rolled back.

The rollback operation performs an undo operation that cancels the operation performed by the change transaction.

The column starting with CURRENT_UNDO_NEXT_LSN means the value indicating the next log (logfile) to undo while this undo operation is in progress.

If the change transaction performed before the rollback was recorded from logfile 1 to logilfe 10, the value of the column starting with CURRENT_UNDO_NEXT_LSN decreases because undo proceeds from logfile 10 when rolling back.

```
SELECT tx.ID TX_ID,
       tx.SESSION_ID,
       tx.STATUS,
       DECODE(tx.FIRST_UPDATE_TIME, 0, '0', TO_CHAR(TO_DATE('1970010109', 'YYYYMMDDHH') + tx.FIRST_UPDATE_TIME / (60*60*24), 'MM/DD HH:MI:SS')) FIRST_UPDATE_TIME,
       st.TOTAL_TIME/1000000 TOTAL,
       tx.CURRENT_UNDO_NEXT_LSN_FILENO,
       tx.CURRENT_UNDO_NEXT_LSN_OFFSET,
       SUBSTR(QUERY, 1, 100) QUERY
  FROM V$TRANSACTION tx,
       V$STATEMENT st
 WHERE tx.ID = st.TX_ID
   AND tx.SESSION_ID <> SESSION_ID();
```

- The time the query was executed is FIRST_UPDATE_TIME
- Rollback start time is FIRST_UPDATE_TIME + TOTAL

## Method changed starting from ALTIBASE HDB version 6.1.1.2.0

From ALTIBASE HDB version 6.1.1.2.0, it is now possible to easily check the statement being rolled back with the status column of v$transaction.

select query from v$statement where session_id in (select session_id from v$transaction where status=4);

The status column of v$transaction is a value that indicates the transaction status and can have a value of 0 to 6, and the meaning of the value is as follows.

- 0: BEGIN: transaction started
- 1: PRECOMMIT: do not use
- 2: COMMIT_IN_MEMORY: do not use
- 3: COMMIT: Transaction is committed
- 4: ABORT: Rolled back and aborted
- 5: BLOCKED: Wait for lock or other transaction
- 6: END: Free status after using all transactions
