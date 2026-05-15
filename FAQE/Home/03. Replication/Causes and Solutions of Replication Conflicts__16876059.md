---
title: "Causes and Solutions of Replication Conflicts"
page_id: "16876059"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Causes+and+Solutions+of+Replication+Conflicts"
updated_at: "2021-04-05T09:24:46.000+0900"
version: 4
ancestors: ["Home", "03. Replication"]
labels: []
---

# Causes and Solutions of Replication Conflicts
Source: https://docs.altibase.com/display/FAQE/Causes+and+Solutions+of+Replication+Conflicts
Updated: 2021-04-05T09:24:46.000+0900

- [Overview](#CausesandSolutionsofReplicationConflicts-Overview) - [When data conflicts occur in a replication environment](#CausesandSolutionsofReplicationConflicts-Whendataconflictsoccurinareplicationenvironment) - [Measures to prevent conflict as much as possible](#CausesandSolutionsofReplicationConflicts-Measurestopreventconflictasmuchaspossible) - [Conflict type](#CausesandSolutionsofReplicationConflicts-Conflicttype)

# Overview

---

This document describes the causes and solutions of replication conflicts.

# When data conflicts occur in a replication environment

---

A replication conflict occurs when insert/update/delete is executed on the same key value at the same time.

● insert conflict: When an INSERT conflict occurs, the INSERT fails and a conflict error message is written to `altibase_rp.log`. Use the `REPLICATION_INSERT_REPLACE` property to set the policy for resolving conflicts that occur when inserting data with the same key as an existing record. `REPLICATION_INSERT_REPLACE=1`: delete and then insert. `REPLICATION_INSERT_REPLACE=0`: do not delete or insert, and output an error message.

● update conflict: When an UPDATE conflict occurs, the UPDATE fails and a conflict error message is written to `altibase_rp.log`. The `REPLICATION_UPDATE_REPLACE` property can be used for conflict resolution. This occurs when the before image changes other data or attempts to change to a primary key that does not exist. For example, if the current data is 10 and a replication transaction tries to update the value from 20 to 30, the following policy can be used depending on the situation: `REPLICATION_UPDATE_REPLACE=1`: update. `REPLICATION_UPDATE_REPLACE=0`: do not update, and output a conflict error message.

● delete conflict: When a DELETE conflict occurs, the DELETE fails and a conflict error message is written to `altibase_rp.log`.

For example in the case of insert:

1) After data with key=1 is inserted in server A, before transmitting the replication data to server B

2) When the same key=1 data is inserted in server B, the replication data received later in server B already has data with the same key=1 in server B, so a conflict occurs.

# Measures to prevent conflict as much as possible

---

The best way is to avoid insert/update/delete with the same Key value on both servers.

For example, if the sequence is the primary key for a specific table, if the user inserts/updates/deletes data only with odd numbers on one side and even numbers on the other server, there will be no replication conflict.

In addition, do not do bulk insert/update/delete.

There are three solutions for replication conflict provided by Altibase.

1) User-Oriented Scheme

(1) Insert conflict: If you try to insert data with the same key, it is not reflected. (Output Conflict Error Message to altibase_rp.log)

(2) delete conflict: If you want to delete data with the same key, it is not reflected. (Output Conflict Error Message to altibase_rp.log)

(3) Update conflict: In the case of updating data with the same key, it is specified whether or not it is reflected according to the following attribute values.

- `REPLICATION_UPDATE_REPLACE=1`: Apply the update.

- `REPLICATION_UPDATE_REPLACE=0`: Do not update, and output a conflict error message.

2) Master-slave Scheme

When declaring a replication object, if as a master or as a slave is specified in the syntax, the replication conflict is handled as follows.

(1) Master's processing method: All Insert/Update/Delete conflicts are not reflected.

(2) Slave processing method

- Insert conflict: Delete an existing record and add a new record.

- Update conflict: The conflict is ignored and unconditionally reflected.

- Insert conflict: Not reflected.

3) Timestamp-based Scheme

After setting the REPLICATION_TIMESTAMP_RESOLUTION property value to 1, a timestamp column is used in the replication table to reflect the latest value. In this method, there is a limitation that the timestamp column must be added to all of the replication target tables, and the time between both servers being replicated must be set equally.

# Conflict type

---

When a conflict occurs, a log is recorded in `$ALTIBASE_HOME/trc/altibase_rp.log`.

● Insert conflict: Occurs when the same PK (Primary Key) already exists.

```
[2015/04/28 10:11:33] [Thread-489] [Level-2]
ERR-11058(errno=0) The row already exists in a unique index.

[2015/04/28 10:11:33] [Thread-489] [Level-3]
INSERT INTO TEST VALUES ( 14, 0, 0,  , 0, 0, 0, 0 );
```

● update conflict: Occurs when the PK (Primary Key) is the same, but the pre-change value from the remote server is different from the current value.

```
[2015/04/27 18:49:32] [Thread-489] [Level-2]
ERR-610f7(errno=16) [Receiver] Unable to find record in executeUpdate() function

[2015/04/27 18:49:32] [Thread-489] [Level-2]
ERR-61000(errno=16) The received record is not found in the database.

[2015/04/27 18:49:32] [Thread-489] [Level-3]
UPDATE TEST SET C2 = 20150428 WHERE C1 =1231232 ;
```

● delete conflict: Occurs when the PK (Primary Key) is the same, but the pre-change value from the remote server is different from the current value.

```
[2015/10/28 17:03:08] [Thread-140059163547392] [Level-2]
ERR-610f7(errno=16) [Receiver] Unable to find record in executeDelete() function

[2015/10/28 17:03:08] [Thread-140059163547392] [Level-3]
DELETE FROM TEST WHERE C1 = 21987744;
```
