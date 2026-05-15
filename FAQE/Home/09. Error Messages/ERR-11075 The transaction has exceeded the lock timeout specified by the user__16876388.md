---
title: "ERR-11075 The transaction has exceeded the lock timeout specified by the user."
page_id: "16876388"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876388"
updated_at: "2021-04-05T11:21:01.000+0900"
version: 8
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# ERR-11075 The transaction has exceeded the lock timeout specified by the user.
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876388
Updated: 2021-04-05T11:21:01.000+0900

- [Overview](#ERR-11075Thetransactionhasexceededthelocktimeoutspecifiedbytheuser.-Overview) - [Version](#ERR-11075Thetransactionhasexceededthelocktimeoutspecifiedbytheuser.-Version) - [Symptom](#ERR-11075Thetransactionhasexceededthelocktimeoutspecifiedbytheuser.-Symptom) - [1. Occur when executing a DDL statement](#ERR-11075Thetransactionhasexceededthelocktimeoutspecifiedbytheuser.-1.OccurwhenexecutingaDDLstatement) - [2. Occurs when a change transaction is performed on the memory table](#ERR-11075Thetransactionhasexceededthelocktimeoutspecifiedbytheuser.-2.Occurswhenachangetransactionisperformedonthememorytable) - [3. Occur when executing a SELECT statement using SELECT FOR UPDATE WAIT N (or NOWAIT)](#ERR-11075Thetransactionhasexceededthelocktimeoutspecifiedbytheuser.-3.OccurwhenexecutingaSELECTstatementusingSELECTFORUPDATEWAITN(orNOWAIT)) - [4. Occur in altibase_rp.log in a replication environment](#ERR-11075Thetransactionhasexceededthelocktimeoutspecifiedbytheuser.-4.Occurinaltibase_rp.loginareplicationenvironment) - [Cause](#ERR-11075Thetransactionhasexceededthelocktimeoutspecifiedbytheuser.-Cause) - [1. Occur when executing a DDL statement](#ERR-11075Thetransactionhasexceededthelocktimeoutspecifiedbytheuser.-1.OccurwhenexecutingaDDLstatement.1) - [2. Occur when a change transaction is performed on the memory table](#ERR-11075Thetransactionhasexceededthelocktimeoutspecifiedbytheuser.-2.Occurwhenachangetransactionisperformedonthememorytable) - [3. Occur when SELECT FOR UPDATE WAIT N (or NOWAIT) is executed](#ERR-11075Thetransactionhasexceededthelocktimeoutspecifiedbytheuser.-3.OccurwhenSELECTFORUPDATEWAITN(orNOWAIT)isexecuted) - [4. Occurs in altibase_rp.log in a replication environment](#ERR-11075Thetransactionhasexceededthelocktimeoutspecifiedbytheuser.-4.Occursinaltibase_rp.loginareplicationenvironment) - [Solution](#ERR-11075Thetransactionhasexceededthelocktimeoutspecifiedbytheuser.-Solution) - [Reference](#ERR-11075Thetransactionhasexceededthelocktimeoutspecifiedbytheuser.-Reference)

# Overview

---

Error messages that may occur when performing change transactions.

# Version

---

This error message can occur in all versions of Altibase, but the error message differs depending on the version of the Altibase server.

- ALTIBASE HDB 4.3.9 ~ 5.3.3
  ERR-11075 ( 69749) The transaction exceeds the lock timeout specified by user.
- ALTIBASE HDB 5.5.1 or later
  ERR-11075 ( 69749) The transaction has exceeded the lock timeout specified by the user.

# Symptom

---

The following are examples of some of the most common symptoms in which this error message occurs.

### 1. Occur when executing a DDL statement

| Session-1 | Session-2<br>Error occurs while executing a DDL statement (`TRUNCATE`) |
| --- | --- |
| autocommit off; |  |
| update test_emp_tbl set emp_no = 10; |  |
| while executing update... | truncate table test_emp_tbl;<br>[ERR-11075 : The transaction has exceeded the lock timeout specified by the user.] |

### 2. Occurs when a change transaction is performed on the memory table

| Session-1 | Session-2 |
| --- | --- |
| iSQL> autocommit off; Set autocommit off success.<br>iSQL> update tb_test1 set c10=sysdate where c1=1; 1 row updated. |  |
|  | iSQL> select count(*) from tb_test1; COUNT ----------------------- 1000000 1 row selected.<br>iSQL> alter session set TRX_UPDATE_MAX_LOGSIZE=100000000; Alter success.<br>iSQL> alter system set LOCK_ESCALATION_MEMORY_SIZE=100000000; Alter success.<br>iSQL> update tb_test1 set c10=sysdate; [ERR-11075 : The transaction has exceeded the lock timeout specified by the user.] |

### 3. Occur when executing a SELECT statement using SELECT FOR UPDATE WAIT N (or NOWAIT)

| Session-1 | Session-2 |
| --- | --- |
| autocommit off;<br>update test_emp_tbl set emp_no = 10; |  |
|  | select * from test_emp_tbl for update wait 1;<br>[ERR-11075 : The transaction has exceeded the lock timeout specified by the user.] |
|  | select * from test_emp_tbl for update nowait;<br>[ERR-11075 : The transaction has exceeded the lock timeout specified by the user.] |

### 4. Occur in altibase_rp.log in a replication environment

In a replication environment, an error may occur in $ALTIBASE_HOME/trc/altibase_rp.log.

```
[2014/08/28 13:00:14] [FAQINTERNAL:Thread-1398925664] [FAQINTERNAL:Level-2]
ERR-11075(errno=0) The transaction has exceeded the lock timeout specified by the user.
[2014/08/28 13:00:14] [FAQINTERNAL:Thread-1398925664] [FAQINTERNAL:Level-3]
INSERT INTO SYS.TB_TEST1 VALUES ( 1000001, , , , , , , , , 2014-08-28 13:00:09.960371 ); (TID : 35456)
```

# Cause

---

This error occurs when trying to acquire a lock on an object, but the object is already locked and the lock cannot be acquired.

```
$ altierr 0x11075
0x11075 (  69749) smERR_ABORT_smcExceedLockTimeWait The transaction has exceeded the lock timeout specified by the user.
# *Cause: The transaction failed to lock the object.
# *Action: Increase the transaction's lock timeout value or check whether the data has a transaction with a long-term lock.
```

### 1. Occur when executing a DDL statement

When executing DDL statements, if the target table is already locked by another transaction, DDL execution may fail because the LOCK for DDL execution cannot be acquired immediately.

This may behave differently depending on the DDL_LOCK_TIMEOUT setting of the Altibase server property.

- DDL_LOCK_TIMEOUT = 0 (default): if the LOCK is not acquired, DDL fails immediately.
- DDL_LOCK_TIMEOUT = -1: if the LOCK cannot be acquired, wait indefinitely.
- DDL_LOCK_TIMEOUT = seconds: if the LOCK is not acquired during DDL execution, wait for the specified time and try again. If the LOCK is still not acquired, DDL fails.

### 2. Occur when a change transaction is performed on the memory table

When the size of the transaction log file exceeds the value of the LOCK_ESCALATION_MEMORY_SIZE property due to a change transaction performed on the memory table, it switches from record level IX_LOCK to table level X_LOCK. At this time, if IX_LOCK is locked on another record of the table in another session, the table level X_LOCK acquisition may fail and an error may occur.

### 3. Occur when SELECT FOR UPDATE WAIT N (or NOWAIT) is executed

A SELECT statement using SELECT FOR UPDATE WAIT N or SELECT FOR UPDATE NOWAIT locks the record and executes it.

However, if a lock is first locked in another session on the same table, an error may occur because the lock cannot be acquired.

### 4. Occurs in altibase_rp.log in a replication environment

When the transaction to be reflected is waiting for the transaction of the local server to be finished.

| Active Server | Standby Server |
| --- | --- |
| alter replication rep1 start; |  |
|  | iSQL> autocommit off; Set autocommit off success. iSQL> insert into tb_test1(c1,c10) values(1000001, sysdate); 1 row inserted. |
| iSQL> autocommit off; Set autocommit off success. iSQL> insert into tb_test1(c1,c10) values(1000001, sysdate); 1 row inserted. |  |

The insert statement of the active server should be reflected in the standby server, but when the replication transaction cannot be reflected due to the local transaction of the standby server, an error message is recorded in altibase_rp.log.

This symptom is affected by the value of the REPLICATION_LOCK_TIMEOUT property.

If the server reflecting the replication log (standby server in the example above) does not acquire LOCK within the REPLICATION_LOCK_TIMEOUT (seconds) time, the above error occurs and the replication transaction attempted to reflect fails.

# Solution

---

- **Occur when executing DDL**
  Generally, it is recommended to perform DDL in idle time. If the service is not stopped, X LOCK acquisition may fail instantaneously. If an error occurs, try performing DDL several times. If the same error still occurs, check whether the target table is busy or there is a long-run query (a query that takes a long time to execute or a query that has not been committed), and execute DDL again after taking action.
- **Occur when performing a change transaction in memory**
  If the above error occurs due to LOCK_ESCALATION_MEMORY_SIZE, there is a high possibility of a large amount of change transactions.
  Make sure not to make a large number of change operations. It is recommended that the number of records to be changed is reduced by using conditional clauses and limit clauses and divided into multiple times to perform change transactions.
- **Occur when executing SELECT FOR UPDATE statement**
  Repeat the SELECT FOR UPDATE statement until it succeeds.
  Find uncommitted transactions and commit or rollback.
  Increase the time of the WAIT option.
- **Occur in a replication environment**
  When designing for replication, consideration should be given to avoiding simultaneous changes on both servers for the same record. When this error occurs, it may cause a problem with the data integrity of both servers, so the data must be checked.

# Reference

---

- Additional explanation regarding `LOCK_ESCALATION_MEMORY_SIZE`: [ERR-11118 (69912) The update log size '_' is bigger than TRX_UPDATE_MAX_LOGSIZE '_'](https://docs.altibase.com/pages/viewpage.action?pageId=16876399)
