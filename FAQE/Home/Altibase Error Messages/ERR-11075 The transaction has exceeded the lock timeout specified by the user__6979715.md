---
title: "ERR-11075 The transaction has exceeded the lock timeout specified by the user"
page_id: "6979715"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-11075+The+transaction+has+exceeded+the+lock+timeout+specified+by+the+user"
updated_at: "2014-11-27T17:08:12.000+0900"
version: 24
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-11075 The transaction has exceeded the lock timeout specified by the user
Source: https://docs.altibase.com/display/FAQE/ERR-11075+The+transaction+has+exceeded+the+lock+timeout+specified+by+the+user
Updated: 2014-11-27T17:08:12.000+0900

- [Version](#ERR-11075Thetransactionhasexceededthelocktimeoutspecifiedbytheuser-Version)
- [Explanation](#ERR-11075Thetransactionhasexceededthelocktimeoutspecifiedbytheuser-Explanation)
- [Cause](#ERR-11075Thetransactionhasexceededthelocktimeoutspecifiedbytheuser-Cause)
- [Action](#ERR-11075Thetransactionhasexceededthelocktimeoutspecifiedbytheuser-Action)
- [Reference](#ERR-11075Thetransactionhasexceededthelocktimeoutspecifiedbytheuser-Reference)

## Version

All versions

## Explanation

This error message is output or written to altibase_rp.log when a DDL/UPDATE/SELECT FOR UPDATE statement is executed.

## Cause

The following error description can be viewed with the AltiErr utility:

$ altierr 0x11075 0x11075 ( 69749) smERR_ABORT_smcExceedLockTimeWait The transaction has exceeded the lock timeout specified by the user.

# *Cause: The transaction failed to lock the object.

# *Action: Please abort the transaction.

This error can occur under the following circumstances:

**1. If an UPDATE statement has been executed:**

If the transaction is to be converted to a table lock due to LOCK_ESCALATION_MEMORY_SIZE but fails to acquire an X lock because the table is already locked (e.g., IX lock).

| **Session 1** | **Session 2** |
| --- | --- |
| ```<br>iSQL> autocommit off;<br>Set autocommit off success.<br>iSQL> update tb_test1 set c10=sysdate where c1=1;<br>1 row updated.<br>``` |  |
|  | ```<br>iSQL> select count(*) from tb_test1;<br>COUNT<br>-----------------------<br>1000000<br>1 row selected.<br>iSQL> alter session set TRX_UPDATE_MAX_LOGSIZE=100000000;<br>Alter success.<br>iSQL> alter system set LOCK_ESCALATION_MEMORY_SIZE=100000000;<br>Alter success.<br>iSQL> update tb_test1 set c10=sysdate;<br>```<br> <br>[ERR-11075 : The transaction has exceeded the lock timeout specified by the user.](#) |

The last UPDATE statement in Session 2 performs the update operation using row-level locking, and then tries to acquire an X lock when the update log size exceeds LOCK_ESCALATION_MEMORY_SIZE.

However, Session 2's UPDATE statement returns the above error because Session 1's UPDATE statement is not committed and holds an IX lock.

Remember that this error did not occur immediately after an UPDATE statement was executed, but after the UPDATE statement was executed and while trying to acquire an X LOCK.

**2. If a DDL statement has been executed:**

If a table lock (X lock) must be acquired for the execution of a DDL statement but the lock cannot be acquired because the table is already locked (e.g., IX lock).

| Session 1 | **Session 2** |
| --- | --- |
| ```<br>iSQL> autocommit off;<br>Set autocommit off success.<br>iSQL> update tb_test1 set c10=sysdate where c1=1;<br>1 row updated.<br>``` |  |
|  | ```<br>iSQL> truncate table tb_test1;<br>```<br> <br>[ERR-11075 : The transaction has exceeded the lock timeout specified by the user.](#) |

This error is related to the DDL_LOCK_TIMEOUT property.

The default value for DDL_LOCK_TIMEOUT is 0 and this means that the DDL statement will not wait to acquire an X lock.

In other words, an error is returned if the statement fails to acquire an X lock.

If a value larger than 0 is set for this property, the DDL statement waits for as many seconds as specified (by the value) to acquire a lock and returns an error, when unsuccessful.

**3. If a SELECT FOR UPDATE statement has been executed:**

If a NOWAIT or WAIT N option is used but a lock is not acquired immediately or within a certain period of time.

| **Session 1** | **Session 2** |
| --- | --- |
| ```<br>iSQL> autocommit off;<br>Set autocommit off success.<br>iSQL> update tb_test1 set c10=sysdate where c1=1;<br>1 row updated.<br>``` |  |
|  | ```<br>iSQL> select * from tb_test1 where c1<10 for update nowait;<br>```<br> <br>[ERR-11075 : The transaction has exceeded the lock timeout specified by the user.](#) |

**4.****If the error message has been output to altibase_rp.log:**

If a replication transaction is waiting for a transaction on the local server to terminate.

| Active Server | Standby Server |
| --- | --- |
| ```<br>alter replication rep1 start;<br>``` | Does not start replication. |
|  | ```<br>iSQL>  autocommit off;<br>Set autocommit off success.<br>iSQL> insert into tb_test1(c1,c10) values(1000001, sysdate);<br>1 row inserted.<br>``` |
| ```<br>iSQL> autocommit off;<br>Set autocommit off success.<br>iSQL> insert into tb_test1(c1,c10) values(1000001, sysdate);<br>1 row inserted.<br>``` |  |

After an INSERT statement has been executed on the Active server, the following message is output to altibase_rp.log on the Standby server.

[] [FAQINTERNAL:Thread-1398925664](#) [FAQINTERNAL:Level-2](#) ERR-11075(errno=0) The transaction has exceeded the lock timeout specified by the user. [] [FAQINTERNAL:Thread-1398925664](#) [FAQINTERNAL:Level-3](#) INSERT INTO SYS.TB_TEST1 VALUES ( 1000001, , , , , , , , , 2014-08-28 13:00:09.960371 ); (TID : 35456)

This error is affected by REPLICATION_LOCK_TIMEOUT.

If the replication transaction (or Standby server) fails to acquire a lock within the time specified by REPLICATION_LOCK_TIMEOUT, an error occurs and the replication transaction fails.

# The above scenarios are only one kind of example for each error cause. Various cases can be attributed to the same cause.

## Action

**1. If an UPDATE statement has been executed:**

A bulk update operation is generally discouraged in DBMSs.

If this error has been caused by LOCK_ESCALATION_MEMORY_SIZE, it is highly likely that a bulk update operation was involved.

The user is advised to reduce the number of records to be updated and perform multiple update operations by dividing the bulk update into smaller updates using the condition clause or LIMIT clause.

If the operation must be performed in a single UPDATE statement, the following options are available (but not advised):

1) Increase LOCK_ESCALATION_MEMORY_SIZE.

The memory tablespace and Altibase process memory usage can increase since undo images for all the records to be updated must be saved.

2) Attempt a bulk update when the system usage is low.

In this case, it is easy to acquire an X lock on the table. However, if the X lock incurs a lock escalation, the table needs to wait for a SELECT and this can be mistaken as service failure.

**2. If a DDL statement has been executed:**

It is generally advisable to execute a DDL statement when the system usage is low.

If a DDL statement is executed while multiple transactions are being processed, the session can fail to acquire an X lock to lock the table, and repeatedly attempt to acquire the lock until the DDL statement is successfully executed.

Thus, the user should check whether the service is busy or a long-running query (a slow running or uncommitted query) exists, take the appropriate steps and then re-execute the DDL statement.

**3. If a SELECT FOR UPDATE statement has been executed:**

1) Repeatedly execute the SELECT FOR UPDATE statement until it succeeds.

2) Find the uncommitted transaction and either execute the COMMIT or ROLLBACK statement

3) Increase the time for the WAIT option.

**4. If the error message has been output to altibase_rp.log:**

When designing the system, caution should be taken so that data is not simultaneously changed on the Master/Slave servers.

The user should check the data as this error can disrupt the data consistency of the Master/Slave servers.

# Since ALTIBASE HDB can temporarily fail to acquire a lock (e.g., #1 and 3 above) while it is running in the SERVICE phase, repeat the operation multiple times.

## Reference

The LOCK_ESCALATION_MEMORY_SIZE property is related only to memory tables.

Therefore, the user should remember that what follows pertains only to memory tables.

The purpose of LOCK_ESCALATION_MEMORY_SIZE is to prevent the memory usage for storing undo images from drastically increasing when performing bulk update operations using record-level locking.

If the update log size exceeds LOCK_ESCALATION_MEMORY_SIZE during a bulk update, an attempt is made to escalate locks by acquiring an X lock.

The above error occurs if the session fails to acquire the X lock.

When successful, the session holds the X lock and continues to update. Memory usage does not increase because in-place updates are performed from this point onward (For further information about in-place updates, refer to the *Administrator's Manual*.).

Since the session holds the X lock on the table, it cannot be accessed by other sessions and all DML statements and the SELECT statement enter a state of waiting. The user could interpret this as a service error.

Thus, the user is advised to reduce the number of update target records and increase the number of updates.

For example, an update of 100,000 records should be divided into 10 updates of 10,000 records using the condition clause or LIMIT clause.

The user should also refer to the following error as well:

[ERR-11118 : The update log size '10485800' is bigger than TRX_UPDATE_MAX_LOGSIZE '10485760'](#)

This warning error is output before the session is converted to an X lock due to LOCK_ESCALATION_MEMORY_SIZE.

The default values for LOCK_ESCALATION_MEMORY_SIZE is 100M and TRX_UPDATE_MAX_LOGSIZE is 10M.

If the update log size exceeds TRX_UPDATE_MAX_LOGSIZE, an error is returned to prevent the session from converting to an X lock.

When the TRX_UPDATE_MAX_LOGSIZE error occurs, adequately increase TRX_UPDATE_MAX_LOGSIZE (the value must not exceed LOCK_ESCALATION_MEMORY_SIZE) and execute the UPDATE statement with every increase.

When changing these property values, LOCK_ESCALATION_MEMORY_SIZE must be larger than TRX_UPDATE_MAX_LOGSIZE.
