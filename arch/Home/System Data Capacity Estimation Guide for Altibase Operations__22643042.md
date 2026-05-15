---
title: "System Data Capacity Estimation Guide for Altibase Operations"
page_id: "22643042"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/System+Data+Capacity+Estimation+Guide+for+Altibase+Operations"
updated_at: "2025-10-21T09:48:11.000+0900"
version: 1
ancestors: ["Home"]
labels: []
---

# System Data Capacity Estimation Guide for Altibase Operations
Source: https://docs.altibase.com/display/arch/System+Data+Capacity+Estimation+Guide+for+Altibase+Operations
Updated: 2025-10-21T09:48:11.000+0900

- [Overview](#SystemDataCapacityEstimationGuideforAltibaseOperations-Overview) - [Memory Capacity Estimation](#SystemDataCapacityEstimationGuideforAltibaseOperations-MemoryCapacityEstimation) - [Size of the Memory Database](#SystemDataCapacityEstimationGuideforAltibaseOperations-SizeoftheMemoryDatabase) - [Buffer Size of the Disk Database](#SystemDataCapacityEstimationGuideforAltibaseOperations-BufferSizeoftheDiskDatabase) - [Memory for Query Execution](#SystemDataCapacityEstimationGuideforAltibaseOperations-MemoryforQueryExecution) - [Example of Memory Capacity Estimation](#SystemDataCapacityEstimationGuideforAltibaseOperations-ExampleofMemoryCapacityEstimation) - [Disk Capacity Estimation](#SystemDataCapacityEstimationGuideforAltibaseOperations-DiskCapacityEstimation) - [Memory Checkpoint Image Files](#SystemDataCapacityEstimationGuideforAltibaseOperations-MemoryCheckpointImageFiles) - [Transaction Log File Space](#SystemDataCapacityEstimationGuideforAltibaseOperations-TransactionLogFileSpace) - [Estimated Space for Disk DB](#SystemDataCapacityEstimationGuideforAltibaseOperations-EstimatedSpaceforDiskDB) - [Undo Tablespace and Temporary Tablespace of Disk DB](#SystemDataCapacityEstimationGuideforAltibaseOperations-UndoTablespaceandTemporaryTablespaceofDiskDB) - [Backup Space for Disk DB](#SystemDataCapacityEstimationGuideforAltibaseOperations-BackupSpaceforDiskDB) - [Considerations When Using Backup via iloader](#SystemDataCapacityEstimationGuideforAltibaseOperations-ConsiderationsWhenUsingBackupviailoader) - [Disk Capacity Calculation Example](#SystemDataCapacityEstimationGuideforAltibaseOperations-DiskCapacityCalculationExample) - [Summary](#SystemDataCapacityEstimationGuideforAltibaseOperations-Summary)

# Overview

---

Before carrying out a project using Altibase, the storage capacity of the server must be determined. This document explains how to estimate the required memory and disk capacity for server configuration.

This document is based on the following version:

- Altibase 7.1.0 or higher

# Memory Capacity Estimation

---

Memory capacity estimation should take the following three factors into account.

1. Size of the memory database
2. Buffer size for the disk database
3. Memory required for query execution

## Size of the Memory Database

---

Tables created in a memory tablespace are allocated pages in 32 KB units. Each page is further divided into units called "slots," depending on the record length of the corresponding table.

Therefore, a single 32 KB page is divided into multiple slots based on the length of the records in the table.

The exact slot size and number of slots per page can be checked through the Altibase performance view `V$MEMTBL_INFO`.

Altibase’s memory database keeps all data and indexes resident in memory.

Therefore, when estimating the size of the memory database in a production environment, it should be calculated based on the actual memory table schema to be created and the expected number of records.

It can be estimated as follows:

| Record Length | The sum of the lengths of all columns that make up one record |  |
| --- | --- | --- |
| Record Header Length | 32 BYTES |  |
| Expected Number of Records | The expected number of records based on the retention period |  |
| Index Pointer Length | 8 BYTES |  |
| 인덱스 포인터의 길이 | 8 BYTES |  |
| Example |  |  |
| Record Length | 500 BYTES |  |
| Header Length | 32 BYTES |  |
| Expected Number of Records | 10,000,000 records (based on 1 year) |  |
| Estimated Table Size | (500 + 32) * 10,000,000 = 5,073.54 MB (estimated) |  |
| Estimated Index Size | 8 * 10,000,000 = 76.29 MB (estimated) |  |
| Applying a Correction Factor Considering Business Growth | Table | 5073 * 1.1 (Based on 1 Year) = 5580 MB |
| Index | 76 * 1.1 (Based on 1 Year) = 83 MB |  |

- The index of a memory table manages only pointer information that refers to the actual location in memory, so it is calculated as (number of records * 8 bytes).
   Depending on the number of memory indexes, it can be calculated using the formula: 8 bytes * number of records * number of indexes.
- The total sum of each estimated size of the table calculated by the above formula can be considered as the capacity of the memory database. Additionally, when estimating the memory DB capacity, it is recommended to include a margin of 30% to 50% in the calculated capacity.
   (The necessary margin will be further explained in the section "Memory for Query Execution" below.)
- To accurately determine the record length, after creating the table, you can clearly find it by querying the sum of the SIZE of the corresponding table columns in SYSTEM_.SYS_COLUMNS_.
- For volatile tablespaces, since actual data occupies memory when present, they should also be included in capacity estimation based on the same criteria above.
   (Data in tables created in volatile tablespaces is lost when the Altibase server is restarted. The volatile tablespace concept is provided for tables used for fast temporary processing without recording physical transaction logs for transactions on these tables.)

## Buffer Size of the Disk Database

---

There is no fixed formula for estimating the buffer size of the disk database.

However, it is recommended that the buffer size be at least 10% of the disk database size expected to be frequently accessed.

For example, if the frequently accessed data size in the disk database is estimated to be 100 GB, the buffer size should be set to at least 10 GB, which is 10%.

## Memory for Query Execution

---

When estimating memory capacity, in addition to data, the memory size for the following three areas should be considered.

1. Query Information and Query Execution Plan
2. Temporary Memory Space for Operations
3. Separate Memory Margin for MVCC (Multi-Version Concurrency Control) Technique

### **Query Information and Query Execution Plan**

When a query is executed, Altibase internally goes through a process of creating an optimized execution plan to handle the query efficiently. The creation and evaluation of this execution plan play a crucial role in query performance.

However, to reduce the overhead of generating an execution plan for the same query repeatedly, Altibase stores and manages query information and execution plans for queries that have already been executed. This requires session memory space.

Altibase has two main types of session memory areas: the SQL Plan Cache, which is shared by all sessions, and memory areas allocated per session.

Since the size of the SQL Plan Cache does not dynamically increase, if it cannot store all execution plans for queries, the plans are stored in the memory allocated to individual sessions.

Therefore, when estimating memory capacity, the memory space allocated per session must also be considered.

### **Temporary Memory Space**

When queries involving operations such as GROUP BY or aggregation are executed in the memory database, a separate storage area is required to store intermediate result sets in order to process raw data into the query results requested by the user. This separate storage area is referred to as temporary memory space.

(In the case of disk databases, temporary tablespaces on disk are used by default, but for performance improvement, hints can be applied to use memory areas instead.)

As a result, this area cannot be precisely calculated mathematically. The amount of temporary memory space required varies greatly depending on the type of query, the size of the data, and the number of concurrent queries being executed.

However, since this allocated memory is reused continuously after allocation, if estimated appropriately, it does not significantly impact the overall memory estimation.

### **Separate Margin for MVCC Technique**

When a read transaction occurs during a modifying transaction, Altibase uses a concurrency control method called MVCC (Multi-Version Concurrency Control) to minimize contention between the two transactions and maximize performance.

To support this MVCC method, the database temporarily stores previous images of versioned data within the table. (For more detailed information on MVCC, refer to the "MVCC Guide" document.)

Therefore, when estimating memory capacity, a margin to accommodate MVCC should also be taken into consideration.

| Margin Consideration Item | Typical Calculation Formula |
| --- | --- |
| Query Information Memory Area | Number of queries * 1 MB |
| Temporary Memory Area for Operations | Total memory tablespace capacity * 0.1 |
| Margin for MVCC | Total memory tablespace capacity * 0.35 |

## Example of Memory Capacity Estimation

---

Assuming that memory tables increase by 1 million records per year and data is retained for 10 years, the capacity can be estimated as follows.

```
CREATE TABLE memory_size (
    C1 CHAR(20),
    C2 INTEGER,
    C3 CHAR(30),
    C4 VARCHAR(200),
    C5 DATE,
    C6 NUMERIC(20,8),
PRIMARY KEY (C1)
) TABLESPACE SYS_TBS_MEM_DATA;

CREATE UNIQUE INDEX idx_1 ON memory_size (C1,C2);
```

The record length of the above table can be confirmed using the following SQL statement.

```
SELECT CEIL(SUM(B.SIZE)/8)*8
  FROM SYSTEM_.SYS_TABLES_ A,SYSTEM_.SYS_COLUMNS_ B
 WHERE A.TABLE_ID = B.TABLE_ID
   AND A.TABLE_NAME = 'MEMORY_SIZE';

CEIL(SUM(B.SIZE)/8)*8
-------------------------
288
1 row selected.
```

Altibase manages memory resources with 8-byte alignment. In other words, sizes that are not multiples of 8 are managed as the next largest multiple of 8.

Therefore, if the record length is 282 bytes, it should be estimated as 288 bytes per record according to the alignment rule.

Once the record length is determined as above, the calculation can be done using the following table.

| Input Data | 288 (record) + 32 (record header) | 1,000,000 | 10 | 1.1 (considering 1 year) |
| --- | --- | --- | --- | --- |
| Data Capacity | (288 + 32) * 1,000,000 = 305.17 MB |  | (1 year capacity * 10 years) = 3,051.7 MB | 3,051.7 * 1.1 = 3,356.8 MB |
| Index Capacity | 8 * 2 (1 primary key, 1 index) | (8 * 1,000,000 * 2) = 15.25 MB | (1 year capacity * 10 years) = 152.5 MB | 152.5 * 1.1 = 167.7 MB |
| 인덱스 용량 | 8*2 (프라이머리 키 1개, 인덱스 1개) | (8*1000000*2) = 15.25 | (1년 용량 * 10년) = 152.5 | 152.5 * 1.1 = 167.7 MB |
| Total | 3204.2 | 3524.5 MB |  |  |

Once the input data is created for each table as shown above, it becomes possible to estimate the capacity for both data and indexes.

After estimating the capacity for data and indexes, the total required memory capacity can be calculated as follows.

| Memory DB Capacity | 20 GB (Sum of capacities for all memory tables) |  |
| --- | --- | --- |
| Disk Buffer | 5 GB (Estimated considering the size of the disk DB) |  |
| 디스크 버퍼 | 5 GB (디스크 DB의 크기를 고려한 산정) |  |
| Applying Margin | Number of Queries = 1,000 | 1000개 * 1 MB = 1 GB |
|  | 20 GB * 0.1 = 2 GB |  |
|  | 20 GB * 0.3 = 6 GB |  |
| Estimated Memory Capacity | 20 GB + 5 GB + 1 GB + 2 GB + 6 GB = 34 GB |  |

This memory capacity estimation purely covers Altibase’s requirements. If you plan to run user applications on the same server, a separate capacity estimation for those components must also be conducted.

# Disk Capacity Estimation

---

Disk capacity should consider the following four items:

1. Memory checkpoint image files
2. Transaction log file space
3. Estimated space for the disk database
4. Backup space for the disk database

## Memory Checkpoint Image Files

---

Altibase periodically saves the contents of the memory database to physical data files to enable recovery of data changed in memory in case of sudden failure.

This process is called a checkpoint, and the size of the data files created during this process corresponds to the size of the memory database. (For detailed information on checkpoints, refer to the "Altibase Checkpoint Guide" document.)

Since two files are created—one set each—this requires disk capacity equal to twice the size of the memory database.

| Expected Memory DB Size | 20 GB |
| --- | --- |
| Size of Memory Checkpoint Image Files | 20 GB * 2 = 40 GB |

## Transaction Log File Space

---

Altibase performs logging of transactions to support recovery using the WAL (Write-Ahead Logging) protocol.

During the logging process, physical files require storage space, and these files are called online log files.

Online log files are automatically deleted when a checkpoint occurs, but in some cases, they may be retained without deletion. Examples include:

- When the redundancy sender in a dual-redundancy environment cannot send required logs and retains them
- When a transaction remains open for a long time due to a large volume of changes

To prevent disk space shortage issues caused by the continuous retention of online log files, it is recommended to secure stable storage space.

However, it is generally difficult to recommend disk space for online log files through a fixed formula.

Because it varies depending on system size, it is best to estimate based on data such as the amount of log files generated from performance load tests.

If such tests are difficult to perform, at least 50 GB of disk space is recommended.

## Estimated Space for Disk DB

---

Unlike memory DB capacity estimation, it is recommended to estimate disk DB capacity on a per-page basis. This is because the attributes PCTFREE and PCTUSED impose constraints on the usable space within each page.

The page size for the disk DB is 8,192 bytes. For each page, the space available for records is calculated by considering the space reserved according to the PCTFREE setting.

The header lengths for records and indexes are as follows. Unlike memory DB, disk DB capacity estimation must consider the length of columns that make up the index.

| Record Header Length | Length (1 BYTE) + Slot Directory (2 BYTES) + 34 BYTES |
| --- | --- |
| Index Header Length | 10 BYTES |

- Each column has 1 byte for length information. If a column exceeds 250 bytes, it includes a 3-byte header for length information.
- The slot directory area, which stores precise offset information within the page for quick access, is also included in the storage calculation.

Disk DB capacity estimation is performed as follows. (For indexes, the lengths of the columns composing the key must be summed.)

| Page Size | 8192 BYTES |
| --- | --- |
| PCTFREE 10% Applied | 8192 - (8192 * 0.1) = 7373 BYTES |
| Fixed Page Header | Part used for page management = 80 BYTES |
| Fixed Page Footer | Part used for page consistency check = 16 BYTES |
| Available Page Size | 7373 - 96 = 7277 BYTES |
| Selected Record Length | 288 BYTES |
| Records per Page | 7277 / (288 + 34) = 22 |
| Estimated Annual Records | 1,000,000 records |
| Final Capacity Estimate | 1,000,000 (records) / 22 (records per page) * 8192 = 3551 MB |

By calculating the number of records per page, you can determine the number of pages required for the estimated record count.

Since the actual pages are measured in 8,192-byte units, the final capacity estimate multiplies by 8,192 bytes.

For indexes, the same calculation applies. Use the length of the key columns as the record length.

The header size for indexes is 16 bytes.

Once the capacity for all disk tables is calculated, sum them up and apply a margin of 30% to 50% to determine the final capacity.

| Item | Calculated Data (Example) |
| --- | --- |
| Disk DB Capacity | 500 GB (Sum of capacities for disk tables) |
| Margin Applied | 500 GB * 0.3 (margin) = 150 GB |
| Estimated Disk Capacity | 500 GB + 150 GB = 650 GB |

## Undo Tablespace and Temporary Tablespace of Disk DB

---

**Undo Tablespace**

The undo tablespace in the disk DB is used as a temporary storage area for copies of changed images until the transaction completes. Since usage varies depending on the queries executed by users, it is difficult to predict the exact usage. For example, if a transaction updates a 1 TB table all at once, the undo tablespace would require 1 TB. Ignoring such worst-case scenarios, it is generally advisable to estimate the undo tablespace capacity as about 30% of the largest table’s size.

**Temporary Tablespace**

The temporary tablespace usage also varies depending on the type of query, making it difficult to predict usage. Therefore, similar to the undo tablespace, it is recommended to estimate the temporary tablespace capacity as about 30% of the largest table’s size.

Both the undo tablespace and temporary tablespace should be allocated sufficient space to ensure smooth operation without issues.

## Backup Space for Disk DB

---

For detailed information on backup, refer to the "Altibase Backup and Recovery Guide." Here, only the capacity estimation related to backups is explained.

To perform backups in Altibase, the system must operate in archive log mode, which requires two separate disk spaces.

| Archive log file directory | Space where backup files of online log files are stored |
| --- | --- |
| Backup space | Space for data files to be stored through online backups, etc. |

For backup space, it can be estimated by the total predicted capacity of the memory DB and disk DB.

Since there are various backup types such as full DB backup every time, incremental backup, and tablespace-level backup, space should be estimated according to each backup type.

For the archive log file directory, it is acceptable to delete all previous log files that are not referenced after the user has completed the backup.

Therefore, since the volume of log files retained may vary depending on the backup cycle and policy, it can be considered flexible according to the backup policy.

Let's understand this through the following example. In the example below, the backup policy is assumed to be on a daily basis.

| Item | Memory DB | Disk DB | Daily Online Log File Size |
| --- | --- | --- | --- |
| Capacity Prediction | 20 GB | 500 GB | 200 GB |
| Required Backup Space | 20 GB | 500 GB | 200 GB (archive) |
| Space Considering Previous Backup | 20 * 2 = 40 GB | 500 * 2 = 1 TB | 200 GB * 2 = 400 GB |

- The memory DB is stored as one set (two files) at the checkpoint, but during the backup phase, only one stable file is backed up, so the backup space should be considered equal to the memory DB capacity.
- For the disk DB, assuming a full backup policy, backup space equal to the predicted disk DB capacity is required.
- Archive log files must be retained until the next backup occurs because recovery to the current point in time is possible using the previously backed-up backup. Therefore, all archive log files generated during the backup cycle must be stored.
- From the perspective of the backup cycle, the previous backup can only be deleted after the current backup is successful, so if the previous backup is kept on disk, twice the backup space is required.

## Considerations When Using Backup via iloader

---

In addition to online backup methods, if it is necessary to back up tables individually, a utility called iloader can be used to back up tables as text files.

In such cases, when calculating disk capacity, the size of the data files backed up through iloader must be taken into account.

Generally, about 5 bytes of data delimiters are required per column, so additional space calculated by the following arithmetic is needed on top of the expected disk DB capacity.

|  |
| --- |
| - Delimiter size = 5 BYTES * number of records * number of columns Example> For a table with 10 columns and 1 million records, an additional 5 * 10 * 1,000,000 = 50 MB is required. |

In other words, additional delimiter capacity is required on top of the initially estimated disk DB size.

Also, when storing the backup compressed on disk, the size of the storage space must be calculated by considering the compression ratio relative to the capacity estimated above.

This aspect is not included in the disk capacity calculation example below, so users choosing this backup method must take it into account.

## Disk Capacity Calculation Example

---

| Item | Size |  |
| --- | --- | --- |
| Memory DB data file | Space required equal to 2 times the Memory DB size |  |
| Disk DB data file | Space required equal to the Disk DB size |  |
| Online log file | 20GB (varies depending on system scale) |  |
| Archive log file | Amount of online log files stored during the backup cycle |  |
| Backup file | Memory DB size + Disk DB size |  |
| Calculation Example | Size | Required Disk Space |
| Memory DB data file | 20 GB | 20 * 2 = 40 GB |
| Disk DB data file | 500 GB | 500 GB |
| Online log file | 20 GB | 20 GB |
| Archive log file | 40 GB | 40 GB |
| Backup file | Memory DB + Disk DB + Archive log file | 560 GB |
| **Total required space** | 40 + 500 + 20 + 40 + (560 * 2) | 1720 GB |

# Summary

---

We have covered how to estimate the memory and disk capacity required to operate Altibase.

However, since there are many factors to consider for each item when estimating database system capacity, it is recommended to thoroughly review the data beforehand to determine the most suitable configuration when building an actual system.
