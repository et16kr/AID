---
title: "ERR-11118 (  69912) The update log size '?????' is bigger than TRX_UPDATE_MAX_LOGSIZE '?????'"
page_id: "16876399"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876399"
updated_at: "2021-04-05T11:22:17.000+0900"
version: 5
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# ERR-11118 (  69912) The update log size '?????' is bigger than TRX_UPDATE_MAX_LOGSIZE '?????'
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876399
Updated: 2021-04-05T11:22:17.000+0900

- [Overview](#ERR-11118(69912)Theupdatelogsize'?????'isbiggerthanTRX_UPDATE_MAX_LOGSIZE'?????'-Overview) - [Version](#ERR-11118(69912)Theupdatelogsize'?????'isbiggerthanTRX_UPDATE_MAX_LOGSIZE'?????'-Version) - [Symptom](#ERR-11118(69912)Theupdatelogsize'?????'isbiggerthanTRX_UPDATE_MAX_LOGSIZE'?????'-Symptom) - [Cause](#ERR-11118(69912)Theupdatelogsize'?????'isbiggerthanTRX_UPDATE_MAX_LOGSIZE'?????'-Cause) - [Solution](#ERR-11118(69912)Theupdatelogsize'?????'isbiggerthanTRX_UPDATE_MAX_LOGSIZE'?????'-Solution) - [Reduce the number of records for UPDATE](#ERR-11118(69912)Theupdatelogsize'?????'isbiggerthanTRX_UPDATE_MAX_LOGSIZE'?????'-ReducethenumberofrecordsforUPDATE) - [Change TRX_UPDATE_MAX_LOGSIZE property setting value](#ERR-11118(69912)Theupdatelogsize'?????'isbiggerthanTRX_UPDATE_MAX_LOGSIZE'?????'-ChangeTRX_UPDATE_MAX_LOGSIZEpropertysettingvalue) - [Reference](#ERR-11118(69912)Theupdatelogsize'?????'isbiggerthanTRX_UPDATE_MAX_LOGSIZE'?????'-Reference) - [Related bug](#ERR-11118(69912)Theupdatelogsize'?????'isbiggerthanTRX_UPDATE_MAX_LOGSIZE'?????'-Relatedbug)

# Overview

---

This document describes an error that occurs while performing a change transaction in the memory table.

# Version

---

Altibase version 4.3.9 or later

# Symptom

---

This error may occur while performing a change transaction on the memory table.

**Example of error occurrence) Table T5 is a memory table**

`iSQL>``update` `t5``set` `c1=``'xxxxxxxxx'` `;`

`[ERR-11118 : The``update` `log``size` `'10486749'` `is` `bigger than TRX_UPDATE_MAX_LOGSIZE``'10485760'``]`

`iSQL>`

The error code differs depending on the Altibase version.

**Altibase 5 or later**

ERR-11118 ( 69912) The update log size '?????' is bigger than TRX_UPDATE_MAX_LOGSIZE '?????'

**Altibase 4.3.9**

ERR-110C3 ( 69827) The update log size '?????' is bigger than TRX_UPDATE_MAX_LOGSIZE '?????'

# Cause

---

This error occurs because the size of the online transaction log created by one change transaction exceeds the TRX_UPDATE_MAX_LOGSIZE setting value.

TRX_UPDATE_MAX_LOGSIZE is an Altibase server property and serves to prevent excessive use of memory due to versioning of the memory table created by a large number of change transactions.

#### Versioning of the memory table?

Altibase uses the Multi-Version Concurrency Control (MVCC) technique for concurrency control. MVCC refers to creating a new version of the record by executing the DML statement on a copy of the record, leaving the record as it was when a DML statement occurs for a record. With this technique, lookup transactions for one record are not affected by change transactions.

Due to the characteristics of each disk and memory, the disk table is in-place and the memory table is out-place and different MVCC techniques are used.

Out-place MVCC of the memory table keeps multiple versions by adding new versions to the new space, leaving the existing records intact when an update occurs on one record. TRX_UPDATE_MAX_LOGSIZE and LOCK_ESCALATION_MEMORY_SIZE properties are provided to prevent this from incurring load on the system, such as increased memory.

Since there is no previous version of INSERT, versioning does not occur, and since there is no new version of DELETE, only the delete flag is set, so multiple versions of versioning do not occur.

# Solution

---

If this error occurs, correct it in one of the ways below.

## Reduce the number of records for UPDATE

---

By reducing the number of records that are changed at one time by an UPDATE statement, the amount of transaction logs created by one transaction is reduced.

#### When there are many records that need to be changed in one table

**For Autocommit mode**

```
iSQL> AUTOCOMMIT ON;
iSQL> UPDATE T1 SET C1=100 LIMIT 1000;        -- Reduce the UPDATE target range with the limit statement and repeat the UPDATE statement.
```

**For Non Autocommit mode**

```
iSQL> AUTOCOMMIT OFF;
iSQL> UPDATE T1 SET C1=100 LIMIT 1000;        -- Reduce the UPDATE target range with the limit statement and repeat the UPDATE statement.
iSQL> COMMIT;                                 -- The commit cycle is also short.
```

#### When performing UPDATE on multiple tables in one transaction

Since the TRX_UPDATE_MAX_LOGSIZE property is applied on a per-transaction basis, if multiple statements are used in one transaction as shown below, TRX_UPDATE_MAX_LOGSIZE may increase until COMMIT or ROLLBACK is performed.

```
iSQL> AUTOCOMMIT OFF;
iSQL> UPDATE T1 SET C1 = 100;
iSQL> COMMIT;                                 -- Shorten the commit cycle.
iSQL> UPDATE T2 SET C1 = 200;
iSQL> COMMIT;
```

## Change TRX_UPDATE_MAX_LOGSIZE property setting value

---

The default value for the TRX_UPDATE_MAX_LOGSIZE property is 10M. If this value is too small, this can be changed at the session or system level.

First, this section will describe how to calculate the size of the transaction log that will be created in a specific transaction and the precautions for changing TRX_UPDATE_MAX_LOGSIZE, and then how to change it.

### Calculation of the TRX_UPDATE_MAX_LOGSIZE value of the transaction

This is how to estimate the amount of transaction log to be used by a particular transaction to change TRX_UPDATE_MAX_LOGSIZE.

| Session 1-UPDATE statement execution | Session 2-Query Performance View |
| --- | --- |
| ```<br>iSQL> AUTOCOMMIT OFF;<br>iSQL> UPDATE ORDER_LINE SET OL_DELIVERY_D = SYSDATE LIMIT 1;    -- Give and execute limit 1<br>``` |  |
|  | Among the results of executing the query below, UPDATE_SIZE * 'Number of records to be updated' is the size of the transaction log that will be created in the transaction.<br>```<br>iSQL> SELECT ST.SESSION_ID SESSION_ID, TX.ID TX_ID<br>, TX.UPDATE_SIZE<br>, SUBSTR(ST.QUERY, 1, 100) QUERY<br>FROM V$TRANSACTION TX, V$STATEMENT ST<br>WHERE TX.ID = ST.TX_ID AND TX.UPDATE_SIZE <> 0 ;<br>``` |
| ```<br>iSQL> ROLLBACK;<br>``` |  |

### Note/Consideration on changing TRX_UPDATE_MAX_LOGSIZE

- It is recommended to set TRX_UPDATE_MAX_LOGSIZE less than LOCK_ESCALATION_MEMORY_SIZE. To prevent memory increase due to memory table MVCC, TRX_UPDATE_MAX_LOGSIZE and LOCK_ESCALATION_MEMORY_SIZE properties are provided.
- If the size of the transaction log created by one transaction exceeds TRX_UPDATE_MAX_LOGSIZE, the transaction is error-processed and rolled back. If LOCK_ESCALATION_MEMORY_SIZE is exceeded, the transaction's LOCK mode is switched from record level IX_LOCK to table level X LOCK.
- In the case of X LOCK, it may cause a problem in the service because the query transaction for the target table is also queued.
- To prevent this problem, set TRX_UPDATE_MAX_LOGSIZE to be smaller than LOCK_ESCALATION_MEMORY_SIZE so that X LOCK does not occur.

### How to change

- **How to check property setting values** TRX_UPDATE_MAX_LOGSIZE should be set smaller than LOCK_ESCALATION_MEMORY_SIZE, so check both properties together.

  **How to check the TRX_UPDATE_MAX_LOGSIZE and LOCK_ESCALATION_MEMORY_SIZE settings**

  ```
  -- This is a method to check the value of a property set in the database.

  iSQL> SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME IN ('TRX_UPDATE_MAX_LOGSIZE', 'LOCK_ESCALATION_MEMORY_SIZE');
  ```

  **How to check the TRX_UPDATE_MAX_LOGSIZE setting value for each session**

  ```
  -- The TRX_UPDATE_MAX_LOGSIZE property can also be set on a per-session basis.
  -- To check the settings for each session
  iSQL> SELECT ID SESSION_ID, COMM_NAME, TRX_UPDATE_MAX_LOGSIZE FROM V$SESSION;

  -- To check the settings of my session. Only available for Altibase 5.3.3 or later
  iSQL> SELECT ID SESSION_ID, COMM_NAME, TRX_UPDATE_MAX_LOGSIZE FROM V$SESSION WHERE ID = SESSION_ID();
  ```
- **How to change session unit** This is applied to transactions performed after ALTER SESSION is executed.

  ```
  iSQL> ALTER SESSION SET TRX_UPDATE_MAX_LOGSIZE = 52428800;        -- Value is in bytes
  ```
- **How to change at the system level**

  After ALTER SYSTEM is executed, it affects transactions performed in new sessions. The value changed by ALTER SYSTEM is applied only while the Altibase server is running, and it returns to the default value when the Altibase server is restarted.

  ```
  iSQL> ALTER SYSTEM SET TRX_UPDATE_MAX_LOGSIZE = 52428800;
  ```

  In order to permanently reflect the changes to the Altibase server, change the altibase.properties file as well.

  ```
  iSQL> ALTER SYSTEM SET TRX_UPDATE_MAX_LOGSIZE = 52428800;

  shell> vi $ALTIBASE_HOME/conf/altibase.properties                  -- Open the altibase.properties file,  find TRX_UPDATE_MAX_LOGSIZE, change the value, and save.
  TRX_UPDATE_MAX_LOGSIZE = 52428800
  ```

  After this is done, the changed value can be kept even if the Altibase server is restarted.

# Reference

---

## Related bug

---

In some versions, due to a bug related to TRX_UPDATE_MAX_LOGSIZE, it may not work properly even if the setting value of TRX_UPDATE_MAX_LOGSIZE is changed.

| Altibase server version | Symptom | Bug |
| --- | --- | --- |
| 4.3.9.103 ~ 4.3.9.133 | The default value of TRX_UPDATE_MAX_LOGSIZE is 10M, but the value of the TRX_UPDATE_MAX_LOGSIZE column of V$SESSION is set to 0 (unlimited). | BUG-20511 |
| 4.3.9.163 ~ 4.3.9.165 | This is a bug that reads TRX_UPDATE_MAX_LOGSIZE incorrectly, and the error does not occur when an error should occur due to TRX_UPDATE_MAX_LOGSIZE. | BUG-26311 |
