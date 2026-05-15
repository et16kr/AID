---
title: "How to resolve when LOCK TIMEOUT occurs"
page_id: "16875984"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/How+to+resolve+when+LOCK+TIMEOUT+occurs"
updated_at: "2021-03-11T14:19:27.000+0900"
version: 1
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# How to resolve when LOCK TIMEOUT occurs
Source: https://docs.altibase.com/display/FAQE/How+to+resolve+when+LOCK+TIMEOUT+occurs
Updated: 2021-03-11T14:19:27.000+0900

- [Overview](#HowtoresolvewhenLOCKTIMEOUToccurs-Overview) - [Version](#HowtoresolvewhenLOCKTIMEOUToccurs-Version) - [Causes](#HowtoresolvewhenLOCKTIMEOUToccurs-Causes) - [Solution](#HowtoresolvewhenLOCKTIMEOUToccurs-Solution) - [Reference](#HowtoresolvewhenLOCKTIMEOUToccurs-Reference)

# Overview

---

During SQL execution, the following error can prevent the desired operation:

```
The transaction exceeds lock timeout specified by user

$ altierr -w "lock timeout" 0x11075 ( 69749) smERR_ABORT_smcExceedLockTimeWait The transaction exceeds lock timeout specified by user. # *Cause: The transaction failed to lock the object. # *Action: Please abort the transaction.
```

# Version

---

ALTIBASE HDB version 4 or later

# Causes

---

During SQL execution, there are times when the following error occurs and the desired operation cannot be performed.

As shown in the error code above, Altibase cannot lock the target object, such as a table, view, or stored procedure.

All sessions accessing a table acquire a lock on that table. For example, if another session is executing DML such as SELECT/INSERT/UPDATE or DDL such as ALTER TABLE on the table, a DROP TABLE waits until the previous operation commits or rolls back.

In this case, make sure there are no users and wait for the previous operation to commit, or the session can be forced to be disconnected. The session can be forcibly terminated by using the alter database statement as shown in the example below.

# Solution

---

**Check lock information**

```
select T.table_name, X.lock_desc  from system_.sys_tables_ T, v$lock X  where T.table_oid = X.table_oid  and T.table_name = 'T1'; //Check the T1 table LOCK information
```

**Forcefully close the session**

1. Find the SESSION ID

```
select 'alter database mydb session close '||ses_id||'; '
  from (select T.table_name,
               SES.id ses_id,
               X.lock_desc,
               X.lock_cnt,
               x.TRANS_ID,
               SES.client_pid pid,
               SES.COMM_NAME,
               STM.query qry
          from v$session SES,
               v$statement STM,
               v$lock X,
               system_.sys_tables_ T
         where SES.id = STM.session_id
           and STM.tx_id = X.trans_id
           and X.table_oid= T.table_oid
-- and T.table_name like 'TEST1%' -- Please specify the table.
               )
 group by ses_id ;

'alter database mydb session close '||SES_
----------------------------------------------
alter database mydb session close 159;
alter database mydb session close 160;
alter database mydb session close 161;
alter database mydb session close 162;
4 rows selected.
```

2. Close the session

```
 $ isql -sysdba -u sys -p manager
 iSQL(sysdba)>
 alter database mydb session close 159;
 alter database mydb session close 160;
 alter database mydb session close 161;
 alter database mydb session close 162; -- Copy/paste the above SQL result and execute it.
```

# Reference

---

Terminating a session with the `ALTER DATABASE` command does not affect sessions other than the target session.

However, terminating the wrong session ID on a production system can cause problems.

As an operational note, even if the connected session is disconnected on a production system, another application may connect and access the table, creating another lock. Consider this before closing sessions.

If possible, it is advisable to disable the application while operating.
