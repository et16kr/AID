---
title: "Transaction Durability in ALTIBASE HDB"
page_id: "2558087"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Transaction+Durability+in+ALTIBASE+HDB"
updated_at: "2011-09-07T10:34:44.000+0900"
version: 27
ancestors: ["Home", "ALTIBASE HDB Architecture"]
labels: []
---

# Transaction Durability in ALTIBASE HDB
Source: https://docs.altibase.com/display/FAQE/Transaction+Durability+in+ALTIBASE+HDB
Updated: 2011-09-07T10:34:44.000+0900

## Transaction

A database transaction is a logical unit of work that comprises one or more SQL statements. A transaction begins with the first execution of an SQL statement by a user, and ends when it is committed or rolled back, either explicitly with a COMMIT or ROLLBACK statement or implicitly when a DDL statement is issued.

## ACID

To maintain database integrity, a properly executed transaction must exhibit the four ACID properties: Atomicity, Consistency, Isolation, and Durability.

• **Atomicity** - Either all of the statements that constitute a transaction are completely executed, or none of them are. That is, the transaction cannot be partially successful.

• **Consistency** - A properly executed transaction does not break the consistency of the database.

• **Isolation** - When multiple transactions are underway at the same time, none of the transactions have access to the results of the other transactions.

• **Durability** - Once a transaction has been committed, the resultant changes are not lost regardless of the circumstances, such as system failure.

ALTIBASE HDB guarantees reliable transactional processing by implementing a database server that satisfies all ACID requirements.

## Durability

Durability means that after a transaction has been committed, the committed transaction must be guaranteed, even if a database failure occurs before the changed data are physically written to a disk.

ALTIBASE HDB provides durability with a combination of checkpointing and transaction logging.

## WAL Protocol

ALTIBASE HDB adheres to WAL (write-ahead logging) protocol. Based on WAL protocol, before overwriting an object with "uncommitted" updates, ALTIBASE HDB writes the log records related to such updates to disk storage for UNDO operations. And similarly, before committing an update to a database object, it writes the log records related to such an update to the log on disk storage for REDO operations.

## Durability & Performance

In ALTIBASE HDB transaction durability has a significant influence on the processing performance. Especially on the memory-based side of the database which can potentially exhibit performance up to 20 times faster than the disk-based side of the database, guaranteeing transaction durability has a much bigger impact on performance. This is due the fact that based on the WAL protocol, in order for a ALTIBASE HDB to provide complete transaction durability, it has to write logs for all database updates to a log file on disk therefore introducing additional disk I/O activity which can degrade the performance.

## Durability Levels Overview

Users need to consider a trade-off between complete transaction durability and transaction processing performance. ALTIBASE HDB provides multiple levels of durability controls, from most relaxed to most strict, to enable users to have a balance between durability and performance. Each of these levels in ALTIBASE HDB guarantees durability to a different extent and realizes different performance characteristics. Relaxed durability yields the best performance; where as strict durability eliminates loss of transactions.

Relaxed durability (Level 2): On system or database crash, recovery point is the last checkpoint.

Enhanced durability (Level 3): On database crash no data loss, recovery point is the last point where OS syncs kernel buffer to disk.

Strict durability (Level 5): No data loss with system or database crash, each transaction committed only when written to disk.

In addition to these durability levels listed above, with ALTIBASE HDB, users have the option to use Volatile tablespaces which omit logging process completely.

## Managing Durability Levels

ALTIBASE HDB provides users with two properties to manage durability level settings. Those properties are: COMMIT_WRITE_WAIT_MODE and LOG_BUFFER_TYPE.

**COMMIT_WRITE_WAIT_MODE** specifies whether a transaction waits until an update log has been written to a log file on disk. This property can be specified for the entire system (ALTER SYSTEM) or for individual sessions (ALTER SESSION).

| Property | Value | Notes |
| --- | --- | --- |
| COMMIT_WRITE_WAIT_MODE | 0 | Asynchronous method, a transaction does wait until an update log has been written to a log file on disk. This is the default setting for ALTIBASE HDB. When using this setting, a service thread writes transaction logs in the log buffer, and returns the result to a user without waiting until the logs files have been written to disk. This setting is suitable for performance-oriented environments since it avoids I/O bottlenecks. With the asynchronous mode, there is still some protection against data loss due to database crashes if LOG_BUFFER_TYPE is set for 1 (see below). |
| COMMIT_WRITE_WAIT_MODE | 1 | Synchronous method, a transaction has to wait until related logs have been written to a log file on disk before returning commit. This mode guarantees transaction durability, and it is suitable for mission critical environments in which transaction durability is more important than performance. |

**LOG_BUFFER_TYPE** specifies the type of log buffer that is used when update logs are written to a log file. This property can't be changed while the system is running.

| Property | Value | Notes |
| --- | --- | --- |
| LOG_BUFFER_TYPE | 0 | OS Kernel log buffer. This is the default setting for ALTIBASE HDB. When using this setting, ALTIBASE HDB uses memory-mapped files for disk I/O related to transaction logs. With memory mapped file IO, the file to be read is mapped to the virtual memory of the underlying OS. This mode provides improved durability in the case that the database crashes but not the OS, since changes to memory-mapped files are maintained in the OS kernel memory. In this mode, log flushing is handled by the operating system leveraging msync() function. |
| LOG_BUFFER_TYPE | 1 | Process memory log buffer. When using this setting, transaction logs are written to a memory-resident log buffer. In this mode, log flushing is handled by the database process using fsync() function. This method is slightly faster than memory-mapped method, but it compromises from durability in the case of a database crash. |

## Relaxed Durability (Level 2)

When using ALTIBASE HDB Relaxed durability setting, on a system or a database crash, recovery point is the last checkpoint. This level is suitable for use in business environments in which database durability is not critical, but fast processing of transactions is required. Businesses that can tolerate a certain level of data loss may want to take advantage of this level for high performance transactions.

| Property | Value |
| --- | --- |
| COMMIT_WRITE_WAIT_MODE | 0 |
| LOG_BUFFER_TYPE | 1 |

## Enhanced Durability (Level 3)

When using ALTIBASE HDB Enhanced durability setting, on database crash there is no data loss, and the recovery point is the last point where OS syncs kernel buffer to disk. In other words, even if the database crashes, durability is still ensured by the OS. This level is suitable for environments characterized by low rates of failures such as OS crashes, hardware faults and power outages. Businesses that can tolerate a certain level of data loss may want to take advantage of this level. This is the default setting for ALTIBASE HDB.

| Property | Value |
| --- | --- |
| COMMIT_WRITE_WAIT_MODE | 0 |
| LOG_BUFFER_TYPE | 0 |

## Strict Durability (Level 5)

When using ALTIBASE HDB Strict durability setting, since each transaction committed only when written to disk, there will be no data loss with either system or database crash, This level is suitable for use in business environments in which data durability is more important than faster performance. Businesses that cannot tolerate any kinds of data loss should use this level.

| Property | Value |
| --- | --- |
| COMMIT_WRITE_WAIT_MODE | 1 |
| LOG_BUFFER_TYPE | 1 |
