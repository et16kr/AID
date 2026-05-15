---
title: "Replication give-up"
page_id: "22642945"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Replication+give-up"
updated_at: "2025-10-20T15:24:44.000+0900"
version: 1
ancestors: ["Home", "03. Replication"]
labels: []
---

# Replication give-up
Source: https://docs.altibase.com/display/FAQE/Replication+give-up
Updated: 2025-10-20T15:24:44.000+0900

**- [Overview](#Replicationgive-up-Overview) - [Version](#Replicationgive-up-Version) - [Replication and log files](#Replicationgive-up-Replicationandlogfiles) - [Replication give-up](#Replicationgive-up-Replicationgive-up) - [Effect of give-up occurrence](#Replicationgive-up-Effectofgive-upoccurrence) - [How to prevent give-up](#Replicationgive-up-Howtopreventgive-up) - [Set whether to proceed with replication when give-up occurs (automatic)](#Replicationgive-up-Setwhethertoproceedwithreplicationwhengive-upoccurs(automatic)) - [Cycle](#Replicationgive-up-Cycle) - [Check whether give-up has occurred](#Replicationgive-up-Checkwhethergive-uphasoccurred)**

# Overview

---

This section explains the potential GIVE-UP phenomenon that may occur during replication and the impact of replication GIVE-UP.

# Version

---

- This content applies to ALTIBASE HDB version 6.1.1 and above.
- For more detailed information or updates, please leave a request at [http://support.altibase.com/en/](http://support.altibase.com/en/) or in the comment section on this page.

# Replication and log files

---

Altibase replication is a data synchronization feature based on Redo logs. In other words, it ensures data consistency between the Active Server and the Standby Server by transferring Redo logs generated on the Active Server to the Standby Server.

In Altibase, Redo log files are not managed using a fixed number of circularly reused files. Instead, logs are generated without a limit as transactions are processed, and once the logs are applied, the corresponding log files are deleted as part of a cleanup process.

This cleanup occurs when a checkpoint is performed. However, Redo log files that meet any of the following conditions cannot be deleted:

(1) Log files currently being referenced by ongoing transactions (2) Log files that are no longer used by active transactions but are still required for replication because the transfer to the Standby Server has not been completed (i.e., log files remaining due to a replication gap) (3) Log files referenced by CLR (Compensation Log Record), which is a type of log created during transaction rollback

If Redo log files matching the above conditions are not cleaned up and continue to accumulate, this may eventually lead to a disk full error on the Active Server.

# Replication give-up

---

In cases where Redo log files are not cleaned up due to replication issues, you can configure the maximum number of Redo log files that replication can retain to prevent a disk full error.

If the number of uncleaned Redo log files exceeds the configured threshold, the system will delete the Redo logs even if data synchronization with the Standby Server has not been completed, in order to prevent a disk full error on the Active Server. This means the replication gap will be abandoned.

This behavior, where Redo log files required for replication are deleted to avoid a disk full issue on the Active Server despite incomplete synchronization, is called **replication GIVE-UP**.

# Effect of give-up occurrence

---

When replication give-up occurs, data inconsistency between both active and standby servers may occur, resulting in serious problems.

# How to prevent give-up

---

- To prevent **replication GIVE-UP**, network performance, which directly affects replication performance, must be maintained in a stable and reliable manner.

- Additionally, in abnormal situations such as power outages or network disconnections, related property values should be appropriately configured to account for worst-case scenarios.

```
REPLICATION_MAX_LOGFILE = 400
```

- The unit of this property is the **number of Redo log files**. For example, if it is set to 400 and more than 400 Redo log files are generated without being cleaned up, the replication GIVE-UP mechanism will be triggered.
- This property can be configured in `$ALTIBASE_HOME/conf/altibase.properties`. For details, refer to the [`REPLICATION_MAX_LOGFILE`](https://github.com/ALTIBASE/Documents/blob/master/Manuals/Altibase_7.1/kor/General%20Reference-1.Data%20Types%20%26%20Altibase%20Properties.md#replication_max_logfile) section in the *General Reference Manual*.

# Set whether to proceed with replication when give-up occurs (automatic)

---

After the **replication GIVE-UP** is triggered due to exceeding the value set by the `REPLICATION_MAX_LOGFILE` property, you can configure how the replication should **restart** afterward.

```
REPLICATION_SENDER_START_AFTER_GIVING_UP = 1  (default)
```

**When set to `0`**

- The `IS_STARTED` column in the `SYS_REPLICATIONS_` metadata table is changed to `0`.
- The replication "Restart SN" (i.e., the `XSN` column in the `SYS_REPLICATIONS_` table) is initialized to `-1`, and replication is stopped.
- In this state, even though replication remains stopped, there will be **no further increase in Redo log files** due to replication.

**When set to `1`**

- The replication "Restart SN" is updated to the **last (largest) SN of the current log file**,
- and replication resumes synchronization **from that point forward** (i.e., synchronization proceeds from the current point in time).

# Cycle

---

Whether or not the **replication GIVE-UP** mechanism is triggered is determined **during the execution of a checkpoint**, which is when Redo log file cleanup occurs.

# Check whether give-up has occurred

---

When a **replication GIVE-UP** occurs, the **give-up time** is recorded in the replication metadata table.

Specifically, Altibase logs GIVE-UP-related information in the `SYSTEM_.SYS_REPLICATIONS_` table when a replication GIVE-UP is triggered.

```
iSQL> set vertical on;
iSQL> select replication_name, is_started, give_up_time from SYSTEM_.SYS_REPLICATIONS_;
REPLICATION_NAME         : REP1
IS_STARTED               : 1
GIVE_UP_TIME             :
1 row selected.
```

| Column name | Description |
| --- | --- |
| REPLICATION_NAME | Replication name |
| IS_STARTED | Whether replication has started (`start`: 1, `stop`: 0) |
| GIVE_UP_TIME | The most recent date and time that replication give-up occurred |
