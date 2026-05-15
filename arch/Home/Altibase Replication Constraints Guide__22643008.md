---
title: "Altibase Replication Constraints Guide"
page_id: "22643008"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/Altibase+Replication+Constraints+Guide"
updated_at: "2025-10-21T09:09:28.000+0900"
version: 1
ancestors: ["Home"]
labels: []
---

# Altibase Replication Constraints Guide
Source: https://docs.altibase.com/display/arch/Altibase+Replication+Constraints+Guide
Updated: 2025-10-21T09:09:28.000+0900

- [Overview](#AltibaseReplicationConstraintsGuide-Overview) - [Replication](#AltibaseReplicationConstraintsGuide-Replication) - [Concept of Replication](#AltibaseReplicationConstraintsGuide-ConceptofReplication) - [Data Synchronization Methods](#AltibaseReplicationConstraintsGuide-DataSynchronizationMethods) - [Replication Constraints in Altibase](#AltibaseReplicationConstraintsGuide-ReplicationConstraintsinAltibase) - [Constraints in Replication Configuration](#AltibaseReplicationConstraintsGuide-ConstraintsinReplicationConfiguration) - [Cross Active-Active Configuration](#AltibaseReplicationConstraintsGuide-CrossActive-ActiveConfiguration) - [Primary Key Column Cannot Be Updated](#AltibaseReplicationConstraintsGuide-PrimaryKeyColumnCannotBeUpdated) - [Sequence Replication Notes](#AltibaseReplicationConstraintsGuide-SequenceReplicationNotes) - [Other Considerations](#AltibaseReplicationConstraintsGuide-OtherConsiderations) - [Replication Conflict](#AltibaseReplicationConstraintsGuide-ReplicationConflict) - [Types of Replication Conflicts](#AltibaseReplicationConstraintsGuide-TypesofReplicationConflicts) - [Valid Insert Conflict](#AltibaseReplicationConstraintsGuide-ValidInsertConflict) - [Replication Update Conflict](#AltibaseReplicationConstraintsGuide-ReplicationUpdateConflict) - [Replication Conflict Mitigation](#AltibaseReplicationConstraintsGuide-ReplicationConflictMitigation) - [RP_MSGLOG_FLAG Setting](#AltibaseReplicationConstraintsGuide-RP_MSGLOG_FLAGSetting)

# Overview

---

Currently, the widely known methods for building high availability (HA) systems include disk sharing and network-based data synchronization.

Altibase adopts only the network-based data synchronization method, referred to as Replication.

While network-based synchronization generally offers better performance compared to disk sharing, it comes with certain limitations due to network latency, transmission delays, and potential disconnections.

Altibase's replication feature also has unavoidable constraints caused by the nature of network communication.

This document is intended to guide users in designing an efficient replication configuration from the planning stage by providing an understanding of these constraints.

Recommended Reference Users are advised to also refer to the following document:

1. Altibase Replication Configuration Guide

# Replication

---

This section provides a brief explanation of Altibase replication.

## Concept of Replication

---

Each system in an Altibase high availability (HA) configuration must operate with its own independent database storage.

This is because Altibase’s replication method prioritizes maintaining high availability while minimizing performance degradation. Instead of using disk sharing—which can introduce significant performance overhead—Altibase adopts a network-based data synchronization approach.

Altibase replication works as follows: When a transaction is committed, the redo logs generated are transformed into xlogs (replication logs) by the Sender thread on the local server. These xlogs are transmitted over the network to the counterpart server, where the Receiver thread applies them to the remote database.

One key consideration for users is that, due to the nature of networks, this architecture is inherently susceptible to transmission delays and conflicts. Therefore, a thorough understanding of the replication constraints described in the following sections is essential to minimize potential issues from development through to production.

## Data Synchronization Methods

---

Altibase replication supports two synchronization modes: Asynchronous (Lazy) and Synchronous (Eager).

- Asynchronous replication prioritizes performance, allowing transactions to complete without waiting for the remote server to apply the changes.
- Synchronous replication prioritizes data consistency, ensuring changes are applied to both servers before the transaction is considered complete.

While synchronous mode offers higher data consistency than asynchronous mode, neither approach can fully guarantee perfect consistency between multiple storage systems due to inherent architectural limitations..

| Mode | Description |
| --- | --- |
| Synchronous | The local server waits until the transaction is successfully applied on the remote server. |
| Asynchronous | The local server does not wait for the transaction to be sent or applied to the remote server. |

As shown above, synchronous replication offers stronger data consistency, but at the cost of significantly reduced performance, as it requires acknowledgment from the remote server before completing a transaction.

Therefore, users must choose between synchronous and asynchronous modes based on the business-critical need for data consistency.

Altibase also supports session-level configuration of synchronous/asynchronous replication, allowing users to choose the appropriate mode per workload.

# Replication Constraints in Altibase

---

This section outlines the limitations when using Altibase replication and provides guidance on how to avoid data conflicts and ensure efficient operation of the replication system.

## Constraints in Replication Configuration

---

Altibase replication operates by creating replication objects that group one or more tables together. When setting up replication, the following constraints must be observed:

1. Data Constraints

    - Primary keys are mandatory for all replicated tables.
    - Primary key values must not be updated in replicated tables.
    - LOB columns cannot be used as primary keys or unique keys.
    - The column definitions, primary keys, and NOT NULL constraints must match on both sides.

          - If column counts or definitions differ, replication setup will succeed, but actual data synchronization will only occur for the matching columns.
    - For Memory Tables, there is no size limit on the generated xLogs.
    - For Disk Tables, the size of a single xLog generated from a row must be less than 128KB.
2. Connection Constraints

    - A maximum of 32 replication connections can be established per database.
    - Replication target databases must have the same character set and national character set to establish a connection (applicable from Altibase v5.3.3).
3. Constraints for Non-Replicated Columns

  When table columns do not match across replication nodes, the unmatched ones are treated as non-replicated columns and have the following limitations:

    - During INSERT operations in replicated transactions, non-replicated columns will receive NULL values.
    - If a unique index is created using both replicated and non-replicated columns, replication setup may succeed, but runtime replication will fail.
4. Partitioned Table Constraints
  DDL Constraints on Replicated Tables
    - The partitioning method must be the same on both local and remote servers.
    - For range or list partitions, the partitioning criteria must be identical.
    - For hash partitions, the number of partitions must be the same.
5. By default, DDL operations are not allowed during replication runtime.
   However, the following DDLs can be executed during replication if the `Replication_ddl_enable` property is set to 1.
  - ADD/DROP Column
  - ALTER Column
  - TRUNCATE Table/Partition
  - CREATE/DROP Index
  - CREATE/DROP Trigger

## Cross Active-Active Configuration

---

To implement an Active-Active setup using Altibase replication, it must be configured as a Cross Active-Active model.

Altibase does not support full Active-Active replication, where the same data (i.e., the same tables or rows) is actively written to on both nodes simultaneously. This limitation is due to the risk of data conflicts, which cannot be resolved automatically in such setups.

For more information on why full Active-Active is not supported, please refer to the Replication Conflict Handling section.

![01_replication.png](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20Replication%20Constraints%20Guide/01_replication.png?api=v2)

## Primary Key Column Cannot Be Updated

---

Altibase replication relies on the primary key to synchronize data, so updates to primary key columns are not allowed.

If an update to a primary key column is necessary in a replication environment, the process must be implemented by deleting the existing record and inserting a new one.

## Sequence Replication Notes

---

Altibase supports replication of sequences, but the following considerations must be taken into account:

- Not supported in Active-Active environments
- Larger sequence cache sizes improve generation speed
- During failover, a gap in the sequence values may occur on the remote server, equivalent to the cache size
- When recreating replication or modifying sequences, all servers must apply the changes consistently

It is recommended that sequences be configured to increment by 2, with each server using odd or even values.

For example, Server A can use a sequence that generates odd numbers, and Server B can use one that generates even numbers.

In a 4-way replication setup, it may be necessary to design the sequence together with a server-specific unique ID.

## Other Considerations

---

- Gigabit network interface cards are recommended to ensure replication performance.
   If memory and disk tables are included in the same replication object, slower performance from disk table transactions may delay overall replication processing.
   Therefore, if the application flow does not require strict ordering between memory and disk table replication, it is better to separate them into different replication objects.

# Replication Conflict

---

Altibase replication primarily uses an asynchronous method, which means that conflicts that cannot be logically avoided may occur. Since the DBMS cannot automatically resolve these conflicts, it is important to design and develop the system to prevent conflicts from happening during the development phase.

## Types of Replication Conflicts

---

Replication conflicts are classified as follows:

| Type | Condition | Error Message |
| --- | --- | --- |
| INSERT Conflict | When the record with the corresponding primary key already exists on the receiving side | ERR-11058(errno=0) The row already exists in a unique index. |
| DELETE Conflict | When the record with the corresponding primary key does not exist on the receiving side | ERR-61000(errno=0) The received record is not found in the database. |
| UPDATE Conflict | When the record with the corresponding primary key does not exist on the receiving side | ERR-61000(errno=0) The received record is not found in the database. |
|  | When the data before the update on the receiving side does not match the received "before update" data |  |

- Detailed explanations on UPDATE conflicts are provided later in the document.

## Valid Insert Conflict

---

There are some exceptional cases where an INSERT conflict is considered valid, such as when the code is written as follows.

```
INSERT INTO TABLE
If (SQLCODE == SQL_DUP_ERROR)
{
UPDATE TABLE ~
}
```

The flow of code as described above is commonly used in business applications, but in an Altibase replication environment, it will generate INSERT Conflict errors in the file located at `$ALTIBASE_HOME/trc/altibase_rp_conflict.log`.

The reason why a failed INSERT transaction on the local server is sent to the remote server is that rollback information, generated during the transaction failure due to primary key duplication, is recorded in the redo log. This redo log is then fully transmitted to the remote server.

Since the transaction will also be rolled back on the remote server, it can be safely ignored. However, because there could be other causes for the conflict, it is recommended to review the source code that triggers the SQL statement and, if possible, modify it as follows to prevent such conflicts.

```
UPDATE TABLE
If (SQLCODE == SQL_NO_DATA)
{
INSERT INTO TABLE
}
```

## Replication Update Conflict

---

When an UPDATE transaction occurs in Altibase replication, both the before-image (previous value) and after-image (new value) of the updated columns are sent to the receiving server, where they compare these values with the current data. An UPDATE Conflict occurs when these compared values do not match.

By default, Altibase does not apply the update on the receiving side when an UPDATE Conflict occurs, and it only records a trace log of the conflict error.

However, if the user’s business logic allows forced updates despite conflicts, Altibase provides an operational option by setting the configuration parameter REPLICATION_UPDATE_REPLACE to "1". With this setting enabled, the receiving server applies the update even if the before-image values differ, and no error log is recorded in the trace log.

Example of a conflict scenario:

| State | A Server | B Server |
| --- | --- | --- |
| Current | C2=10 | C2=10 |
| Simultaneous UPDATE on the same PK | C2=30 (10 -> 30 update) | C2=40 (10 -> 40 update) |
| After transaction | Sender: xLog (10 -> 30) | Sender: xLog (10 -> 40) |

In this example, both servers start with the same value (C2=10) but simultaneously issue updates with different values. As a result, Server A updates to 30 and Server B updates to 40.

When Server A sends the log (xLog) of its update to Server B, and vice versa, both servers find that the before-image in the xLog ("10") does not match their current values (already updated to 30 or 40).

Therefore, neither server applies the received update, resulting in inconsistent values between the two servers.

## Replication Conflict Mitigation

---

A key design principle to avoid conflicts is to prevent concurrent access or modification of records with the same primary key across different servers.

1. One way to achieve this is through workload separation
  Server 1 handles all updates (writes) Server 2 is used only for read operations
  ![02_replication.png](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20Replication%20Constraints%20Guide/02_replication.png?api=v2)
2. Primary Key Separation Design
  As shown in the diagram below, conflicts can be avoided by designing the system so that INSERT, UPDATE, and DELETE operations are separated between the two servers based on the primary key. This means each server handles a distinct range or set of primary keys, preventing overlapping data modifications and thus avoiding conflicts.![03_replication.png](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20Replication%20Constraints%20Guide/03_replication.png?api=v2)

## RP_MSGLOG_FLAG Setting

---

When data conflicts occur during replication, setting the MSGLOG_FLAG will output information about the conflicting table and SQL statement to the file $ALTIBASE_HOME/trc/altibase_rp_conflict.log. This provides necessary information for tracking and troubleshooting issues.

The RP_MSGLOG_FLAG can be set in iSQL as follows:

```
iSQL> alter system set RP_MSGLOG_FLAG = 6 ;
```

# Korean Source Attachments

The Korean source page also references these downloadable source attachments. They are preserved here so the English document set does not lose those references.

- [Korean source attachment 1 (PDF)](https://docs.altibase.com/download/attachments/19333729/ALTIBASE_%EC%9D%B4%EC%A4%91%ED%99%94_%EC%A0%9C%EC%95%BD%EC%82%AC%ED%95%AD_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1698111415000&api=v2)
