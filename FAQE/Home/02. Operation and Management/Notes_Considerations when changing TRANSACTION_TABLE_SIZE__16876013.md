---
title: "Notes/Considerations when changing TRANSACTION_TABLE_SIZE"
page_id: "16876013"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876013"
updated_at: "2021-04-02T16:08:24.000+0900"
version: 3
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# Notes/Considerations when changing TRANSACTION_TABLE_SIZE
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876013
Updated: 2021-04-02T16:08:24.000+0900

- [Overview](#Notes/ConsiderationswhenchangingTRANSACTION_TABLE_SIZE-Overview) - [Restriction](#Notes/ConsiderationswhenchangingTRANSACTION_TABLE_SIZE-Restriction) - [How to change](#Notes/ConsiderationswhenchangingTRANSACTION_TABLE_SIZE-Howtochange) - [Change (offline)](#Notes/ConsiderationswhenchangingTRANSACTION_TABLE_SIZE-Change(offline)) - [Change (ALTER SYSTEM)](#Notes/ConsiderationswhenchangingTRANSACTION_TABLE_SIZE-Change(ALTERSYSTEM)) - [Change procedures](#Notes/ConsiderationswhenchangingTRANSACTION_TABLE_SIZE-Changeprocedures) - [When data migration is required](#Notes/ConsiderationswhenchangingTRANSACTION_TABLE_SIZE-Whendatamigrationisrequired) - [When it can be changed offline](#Notes/ConsiderationswhenchangingTRANSACTION_TABLE_SIZE-Whenitcanbechangedoffline) - [Maximum value](#Notes/ConsiderationswhenchangingTRANSACTION_TABLE_SIZE-Maximumvalue) - [TRANSACTION_TABLE_SIZE and memory usage](#Notes/ConsiderationswhenchangingTRANSACTION_TABLE_SIZE-TRANSACTION_TABLE_SIZEandmemoryusage) - [When TRANSACTION_TABLE_SIZE is exceeded](#Notes/ConsiderationswhenchangingTRANSACTION_TABLE_SIZE-WhenTRANSACTION_TABLE_SIZEisexceeded) - [Performance View](#Notes/ConsiderationswhenchangingTRANSACTION_TABLE_SIZE-PerformanceView) - [Error Messages](#Notes/ConsiderationswhenchangingTRANSACTION_TABLE_SIZE-ErrorMessages) - [Reference](#Notes/ConsiderationswhenchangingTRANSACTION_TABLE_SIZE-Reference)

# Overview

---

TRANSACTION_TABLE_SIZE is an Altibase server property and means the maximum number of transactions that can be executed simultaneously while operating the database.

There is always one transaction in one session. Therefore, if the number of concurrent connection sessions increases, the number of concurrent transactions may increase. Therefore, when increasing the MAX_CLIENT property value, consider changing the TRANSACTION_TABLE_SIZE.

TRANSACTION_TABLE_SIZE also refers to the unique number (TID) of the transaction. This property requires caution when changing because different transactions can be recognized as one transaction if the TID causes problems due to an incorrect change.

Also, the change method differs depending on the ALTIBASE HDB version, so the related contents are summarized.

# Restriction

---

- Depending on the ALTIBASE HDB version, there are versions that require data migration to change TRANSACTION_TABLE_SIZE. Please refer to the 'How to change' section below.
- It can only be changed to a 2^n value greater than the current value.
- It can be changed in the order of 2^n 16 -> 32 -> 64 -> 128 -> 256 -> 512 -> 1024 -> 2048 -> 4096 -> 8192 -> 16384.
- It cannot be changed from a large value to a small value.
- The number of concurrent transactions must be set higher than MAX_CLIENT because it includes all user transactions, replication transactions, and internal transactions.
- In a replication environment, it may be necessary to set up to twice of MAX_CLIENT in consideration of replication transactions.
- In a replication environment, the TRANSACTION_TABLE_SIZE must all be the same between the replication target servers. If the TRANSACTION_TABLE_SIZE is different, the replication sender thread will not start.

  **Example**

  ```
  iSQL> alter replication REP_MEM start;
  [ERR-6100D : [Sender] Failed to handshake with the peer server (Transaction Table Size mismatch [1024:4096])]
  ```

# How to change

---

### Change (offline)

Starting with the versions listed below, `TRANSACTION_TABLE_SIZE` can be changed offline. (ALTIBASE HDB 4 is excluded.)

| ALTIBASE HDB server version | 4.3.9 | From 5.1.5.93 | From 5.3.3.48 | From 5.3.5.17 | From 5.5.1.1.0 |
| --- | --- | --- | --- | --- | --- |
| Change (offline) | Cannot be changed. Data migration required. | Changeable. Data migration is not required. | Changeable. Data migration is not required. | Changeable. Data migration is not required. | Changeable. Data migration is not required. |

| ALTIBASE HDB server version | 4.3.9 | 5.1.5.0 ~ 5.1.5.92 | 5.3.3.0 ~ 5.3.3.47 | 5.3.5.0 ~ 5.3.5.16 | 5.5.1.0.0 ~ 5.5.1.0.9 |
| --- | --- | --- | --- | --- | --- |
| Change (offline) | Cannot be changed. Data migration required. | Cannot be changed. Data migration required. | Cannot be changed. Data migration required. | Cannot be changed. Data migration required. | Cannot be changed. Data migration required. |

### Change (ALTER SYSTEM)

When changed with `ALTER SYSTEM`, the `Alter success.` message may make the property appear changeable, but `TRANSACTION_TABLE_SIZE` cannot be changed while Altibase is online.

| ALTIBASE HDB server version | 4.3.9 | 5.1.5 | From 5.3.3.64 | From 5.3.5.26 | From 5.5.1.2.13 |
| --- | --- | --- | --- | --- | --- |
| Change (online) (alter system) | It looks like it can be done with an alter system, but it cannot be changed. | It looks like it can be done with an alter system, but it cannot be changed. | Cannot be changed | Cannot be changed | Cannot be changed |

| ALTIBASE HDB server version | 4.3.9 | 5.1.5 | 5.3.3.0 ~ 5.3.3.63 | 5.3.5.0 ~ 5.3.5.25 | 5.5.1.0.0 ~ 5.5.1.2.12 |
| --- | --- | --- | --- | --- | --- |
| Change (online) (alter system) | It looks like it can be done with an alter system, but it cannot be changed. | It looks like it can be done with an alter system, but it cannot be changed. | It looks like it can be done with an alter system, but it cannot be changed. | It looks like it can be done with an alter system, but it cannot be changed. | It looks like it can be done with an alter system, but it cannot be changed. |

In the version where BUG-33467 is reflected, [ERR-0104E: The property [TRANSACTION_TABLE_SIZE] is read-only.] error occurs when changing to ALTER SYSTEM.

##### Related bug

BUG-33467 Change TRANSACTION_TABLE_SIZE property attribute to read-only. Modify so that it cannot be changed with ALTER SYSTEM.

BUG-31862 Improves the ability to change TRANSACTION_TABLE_SIZE without migration. It can only be changed to a value of 2^n greater than the current value.

# Change procedures

---

### When data migration is required

1. Secure service downtime
2. Database backup using aexport, iloader
3. Shutdown Altibase server
4. Change TRANSACTION_TABLE_SIZE in altibase.properties
5. Recreate database
6. Load the data from the backup created in step 2
7. Startup Altibase server

### When it can be changed offline

1. Securing service downtime
2. Altibase server shutdown
3. Change TRANSACTION_TABLE_SIZE in altibase.properties
4. Startup Altibase server

# Maximum value

---

Depending on the ALTIBASE HDB server version, the maximum value for TRANSACTION_TABLE_SIZE is different. In previous versions, some manuals have errors in the description of the maximum value, so please refer to the table below.

| ALTIBASE HDB server version | From 4.3.9.222 | From 5.1.5.112 | From 5.3.3.91 | From 5.3.5.35 | From 5.5.1.5.3 |
| --- | --- | --- | --- | --- | --- |
| Maximum value | 16384 | 16384 | 16384 | 16384 | 16384 |

| ALTIBASE HDB server version | 4.3.9.0 ~ 4.3.9.221 | 5.1.5.0 ~ 5.1.5.111 | 5.3.3.0 ~ 5.3.3.90 | 5.3.5.0 ~ 5.3.5.34 | 5.5.1.0.0 ~ 5.5.1.5.2 |
| --- | --- | --- | --- | --- | --- |
| Maximum value | 8192 | 8192 | 8192 | 8192 | 8192 |

##### Related bug

BUG-37851 The maximum value of the TRANSACTION_TABLE_SIZE value needs to be modified.

# TRANSACTION_TABLE_SIZE and memory usage

---

When running the ALTIBASE HDB server, memory for TRANSACTION_TABLE_SIZE is allocated in advance. So, depending on the TRANSACTION_TABLE_SIZE setting, memory usage may increase slightly.

The following is an example of comparing memory usage according to the TRANSACTION_TABLE_SIZE setting value.

Memory usage may vary depending on the system environment. Please note only the difference according to the TRANSACTION_TABLE_SIZE setting value. The unit is KB.

|  | 1024 | 2048 | 4096 | 8192 | 16384 |
| --- | --- | --- | --- | --- | --- |
| VSZ | 1,484,952 | 1,647,264 | 2,019,544 | 2,911,096 | 5,309,148 |
| RSS | 660,900 | 825,956 | 1,164,640 | 2,093,068 | 4,465,108 |

The test server environment is as follows:

- Linux
- Environment variable MALLOC_ARENA_MAX=4
- ALTIBASE HDB 6.3.1.2.7

The following `V$MEMSTAT` items show the largest difference. The unit is bytes.

| V$MEMSTAT item | 1024 | 16384 | Difference |
| --- | --- | --- | --- |
| Storage_Memory_Locking | 7,276,872 | 1,618,233,672 | 1,610,956,800 |
| Storage_Memory_Utility | 73,101,528 | 1,149,161,688 | 1,076,060,160 |
| Storage_Memory_Transaction | 70,129,144 | 1,093,979,352 | 1,023,850,208 |
| Transaction_Table | 5,852,872 | 89,657,032 | 83,804,160 |
| Mutex_Manager | 71,388,392 | 136,578,888 | 65,190,496 |
| Transaction_Table_Info | 1,662,976 | 26,607,616 | 24,944,640 |

# When TRANSACTION_TABLE_SIZE is exceeded

---

If the number of concurrent transactions exceeds TRANSACTION_TABLE_SIZE, the database may appear to hang due to the following phenomena.

- Unable to connect to a new session
- No response when executing SQL in the connected session

The following message appears in altibase_boot.log.

```
TRANSACTION_TABLE_SIZE is full !!
Current TRANSACTION_TABLE_SIZE is 1024
Please check TRANSACTION_TABLE_SIZE
```

# Performance View

---

The TRANSACTION_TABLE_SIZE setting value and the number of running transactions can be checked in V$TRANSACTION_MGR.

```
-- TOTAL_COUNT refers to the value of TRANSACTION_TABLE_SIZE setting, and ACTIVE_COUNT refers to the number of transactions in progress.

iSQL> SELECT TOTAL_COUNT, ACTIVE_COUNT FROM V$TRANSACTION_MGR;
TOTAL_COUNT ACTIVE_COUNT
----------------------------
8192        4
1 row selected.
```

# Error Messages

---

##### ERR-10166(errno=2) TRANSACTION_TABLE_SIZE ['4094'] is not a power of two.

This is an error message that occurs when the value of the TRANSACTION_TABLE_SIZE property is not 2^n.

2^n values are 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384.

##### ERR-10018(errno=0) The version of data file for backup is not compatible with the version of storage manager. Backup DB => [ Version ID = 4.11.1, Bit = 64, Endian = BIG LogSize = 10485760 Transaction Table Size = 1024 ] Server=>[ Version ID = 4.11.1, Bit = 64, Endian = BIG LogSize = 10485760 Transaction Table Size = 2048 ]

This is an error message that occurs in the version where the TRANSACTION_TABLE_SIZE set when creating the database cannot be changed.

This can happen when changing from a large value to a small value.

# Reference

---

[BUG-31862 TRANSACTION_TABLE_SIZE expansion](http://nok.altibase.com/pages/viewpage.action?pageId=6851652)
