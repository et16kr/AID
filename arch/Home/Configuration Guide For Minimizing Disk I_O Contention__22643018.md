---
title: "Configuration Guide For Minimizing Disk I/O Contention"
page_id: "22643018"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=22643018"
updated_at: "2025-10-21T09:25:04.000+0900"
version: 1
ancestors: ["Home"]
labels: []
---

# Configuration Guide For Minimizing Disk I/O Contention
Source: https://docs.altibase.com/pages/viewpage.action?pageId=22643018
Updated: 2025-10-21T09:25:04.000+0900

**- [Overview](#ConfigurationGuideForMinimizingDiskI/OContention-Overview) - [What Causes Disk I/O](#ConfigurationGuideForMinimizingDiskI/OContention-WhatCausesDiskI/O) - [Redo Log](#ConfigurationGuideForMinimizingDiskI/OContention-RedoLog) - [Check Point](#ConfigurationGuideForMinimizingDiskI/OContention-CheckPoint) - [On-Disk DB](#ConfigurationGuideForMinimizingDiskI/OContention-On-DiskDB) - [Undo TableSpace](#ConfigurationGuideForMinimizingDiskI/OContention-UndoTableSpace) - [Recommendations for Effective Data File Configuration](#ConfigurationGuideForMinimizingDiskI/OContention-RecommendationsforEffectiveDataFileConfiguration) - [Disk I/O](#ConfigurationGuideForMinimizingDiskI/OContention-DiskI/O) - [Configuration Example](#ConfigurationGuideForMinimizingDiskI/OContention-ConfigurationExample) - [File System](#ConfigurationGuideForMinimizingDiskI/OContention-FileSystem) - [Supported File Systems](#ConfigurationGuideForMinimizingDiskI/OContention-SupportedFileSystems) - [Unsupported File Systems](#ConfigurationGuideForMinimizingDiskI/OContention-UnsupportedFileSystems) - [Disk Configuration](#ConfigurationGuideForMinimizingDiskI/OContention-DiskConfiguration) - [Dedicated Storage for the Database](#ConfigurationGuideForMinimizingDiskI/OContention-DedicatedStoragefortheDatabase) - [RAID](#ConfigurationGuideForMinimizingDiskI/OContention-RAID) - [Disk Performance](#ConfigurationGuideForMinimizingDiskI/OContention-DiskPerformance) - [Disk I/O Optimization](#ConfigurationGuideForMinimizingDiskI/OContention-DiskI/OOptimization) - [OS File Cache Configuration Changes](#ConfigurationGuideForMinimizingDiskI/OContention-OSFileCacheConfigurationChanges) - [Direct I/O](#ConfigurationGuideForMinimizingDiskI/OContention-DirectI/O) - [Page Size](#ConfigurationGuideForMinimizingDiskI/OContention-PageSize)**

# **Overview**

---

When a database handles a transaction, it generally records a redo log using WAL (Write Ahead Logging) for recovery purposes. Changing, saving or deleting data is the general process of handling the transaction after recording the redo log. Both redo logs and data require persistent physical storage space. This physical storage can be allocated either to the same disk or to physically distinct disks.

However, the user should note that significant disk I/O contention may occur if redo logs and data are placed on the same disk while processing numerous transactions.

This guide describes how ALTIBASE HDB writes redo logs and data and how to configure disk volumes to minimize disk I/O contention.

This guide is up to date as of ALTIBASE HDB version 6.5.

# **What Causes Disk I/O**

---

## Redo Log

ALTIBASE HDB’s redo logs record all changes that were made by any transactions. Redo logs are crucial for the purpose of data recovery.

Redo logs contain information about any changes made to data, as well as changes made to any resources required to handle transactions.

ALTIBASE HDB’s redo logs are initially recorded in the memory mapping area by mmap and are then periodically saved into the redo log file by LogSyncThread. The history of changes in the memory mapping area is guaranteed to be saved into a file even if an executed process terminates abnormally.Therefore, the log file cannot be lost except in the case of power failure or an OS hang (*if this issue is encountered, please refer to the ALTIBASE Troubleshooting Guide*).

This method is used by default in order to minimize frequent disk I/O and maximize performance. However, the redo log writing method can be changed if high transaction performance is not required.

## Check Point

As a hybrid database, ALTIBASE HDB provides support for both in-memory tables and disk tables. In this section, activities that incur disk I/O for memory tables will be discussed.

During the startup stage, data contained within memory tables must be loaded from disk. The storage space for in-memory data is managed as pages, and each page has a fixed size of 32K. Each page is divided into *n* slots based on the table record size, and each slot records data.

When data is changed, saved or deleted by a transaction, the page that stored the modified data is registered to the list of dirty pages. This process is managed internally. The process of saving these dirty pages to physical storage on disk is referred to as a checkpoint.

Due to the fact that memory is a volatile storage medium, the checkpoint process is necessary to provide data durability in the case of situations such as power failures.

As the number of transactions being processed by in-memory tables increases, the number of dirty pages that must be flushed to disk by the checkpoint process will increase as well. If redo logs and in-memory table datafiles are located on the same physical disk, this load may cause disk I/O contention. In order to avoid any possible performance degradation, it is highly recommended to store redo logs and datafiles on separate physical disks.

For example:

| **Classification** | **Disk Configuration** |
| --- | --- |
| Redo Logs | /ALTIBASE_REDO_LOG |
| Datafiles | /ALTIBASE_DATA |

## On-Disk DB

In the previous section, we discussed the process of storing redo logs and causes for disk I/O for in-memory tables. This section will describe causes for disk I/O for disk tables, as well as configuration recommendations.

Because disk tables keep all data on a disk file, disk queries must access the physical disk every time a transaction is executed. This is extremely costly from a disk I/O perspective. Therefore, virtually every disk DBMS creates and utilizes a temporary memory storage area commonly referred to as a buffer. By storing frequently used data in the buffer area, disk I/O costs can be reduced significantly.

The size of the memory buffer is determined by the user and has a page size of 8K.

When a query is executed against a disk table, ALTIBASE HDB will initially search the buffer area to determine if it contains the requested data. If the data does not exist in the buffer, ALTIBASE HDB will load the data from the physical datafile. Any modified pages will be registered to the Flush List. When a flush occurs, any of the pages registered to this list will be transferred and stored on disk. If the buffer area lacks sufficient space, the LRU algorithm will identify and transfer rarely accessed pages to disk. This process is also referred to as BufferReplace.

If the datafiles for in-memory tablespaces and disk tablespaces are allocated to the same physical disks, performance may degrade if frequent checkpoints and BufferReplaces cause excessive disk I/O.

Therefore, for maximum performance the user should always allocate memory and disk datafiles to separate physical disks.

For example:

| **Classification** | **Disk configuration** |
| --- | --- |
| Redo Logs | /ALTIBASE_REDO_LOG |
| Memory Table Datafiles | /ALTIBASE_MEMORY_DATA |
| Disk Table Datafiles | /ALTIBASE_DISK_DATA |

## Undo TableSpace

When a transaction modifies data, memory tables manage an undo image in memory for recovery purposes. The original data is copied to a separate area, and an out-place update is made to the replicated data. This method is also known as MVCC.

In contrast, disk tables copy the original data to the undo tablespace. The transaction then modifies the data located in the original location. This method is known as an in-place update.

For recovery, the copy of the original data will be copied back into the undo tablespace. However, it is important to note that the undo tablespace is being constantly updated as disk tables continue to process transactions. Therefore, the user should consider placing disk table datafiles and undo tablespace datafiles on separate physical disks to prevent disk I/O related performance issues.

For example:

| **Classification** | **Disk Configuration** |
| --- | --- |
| Redo Logs | /ALTIBASE_REDO_LOG |
| Memory Table Datafiles | /ALTIBASE_MEMORY_DATA |
| Disk Table Datafiles | /ALTIBASE_DISK_DATA |
| Undo Tablespace Datafiles | /ALTIBASE_DISK_UNDO |

# **Recommendations for Effective Data File Configuration**

---

As described in the previous sections, significant disk I/O contention may occur if the same physical disk is used to write redo logs and store memory table datafiles and disk table datafiles.

This issue becomes most apparent when the system is under significant load. Redo logs, memory table datafiles and disk table datafiles should be placed on separate physical disks to reduce the chance of disk I/O related performance degradation.

## Disk I/O

As depicted visually above, avoiding disk bottlenecks is difficult if redo log writing, checkpointing and buffer management all occur on a single disk.

![diskio_1.png](https://docs.altibase.com/download/attachments/embedded-page/DOCK/21.%20Altibase%20%EB%94%94%EC%8A%A4%ED%81%ACI/O%20%EB%B3%91%EB%AA%A9%EC%9D%84%20%EA%B3%A0%EB%A0%A4%ED%95%9C%20%EB%B3%BC%EB%A5%A8%EA%B5%AC%EC%84%B1%20%EA%B0%80%EC%9D%B4%EB%93%9C/diskio_1.png?api=v2)

## Configuration Example

### **Example 1.**

Adhering to the configuration below is highly recommended. If this configuration is not feasible due to your current system environment, at a bare minimum the redo logs should be segregated onto a separate physical disk.

| **Classification** | **Disk Configuration** |
| --- | --- |
| ALTIBASE HOME | /ALTIBASE |
| Redo Logs | /ALTIBASE_REDO_LOG |
| Memory Table Datafiles | /ALTIBASE_MEMORY_DATA |
| Disk Table Datafiles | /ALTIBASE_DISK_DATA |
| Disk Indexes | /ALTIBASE_DISK_INDEX |
| Undo Tablespace Datafiles | /ALTIBASE_DISK_UNDO |

- ALTIBASE_HOME stores binaries, headers, libraries, and other files for development and operation. Because important trace logs generated during operation are also written under ALTIBASE_HOME, it is recommended to allocate a separate physical disk for it.

- There is no need to allocate a separate physical disk for memory indexes because indexes are rebuilt in memory after the memory DB is loaded during ALTIBASE HDB startup. Changes to memory indexes are not logged separately.

- Separating disk DB datafiles and disk indexes onto separate physical disks is recommended to minimize disk I/O contention caused by datafile expansion or DB schema changes.

- This document does not describe disk considerations related to backup. Refer to the Backup/Recovery guide for backup and recovery considerations.

### **Example 2.**

The following configuration is the minimum separation model. It is recommended when the system is configured mainly with memory DB, when the disk DB workload has few changes, or when the system has only the minimum number of disks.

| **Classification** | **Disk Configuration** |
| --- | --- |
| Redo Logs | /ALTIBASE_REDO_LOG |
| ALTIBASE HOME and All Datafiles | /ALTIBASE |

This configuration can reduce disk I/O contention only for environments mainly using memory DB or disk DB services with few update operations.

### Example 3.

If memory tables are used sparsely and the vast majority of data and processing is performed by disk tables, the following configuration can be considered.

| **Classification** | **Disk Configuration** |
| --- | --- |
| Redo Logs | /ALTIBASE_REDO_LOG |
| ALTIBASE HOME and Memory Table Datafiles | /ALTIBASE |
| Disk Table Datafiles 1 (Complex Tasks) | /ALTIBASE_DISK_COMPLEX |
| Disk Table Datafiles 2 (Simple Tasks) | /ALTIBASE_DISK_SIMPLE |

Placing tablespaces that regularly process complex queries and tablespaces that typically process simple queries on separate physical volumes is an effective method of dispersing disk I/O. However, if the environment frequently executes BufferReplace processes, this configuration may suffer from performance degradation.

# **File System**

---

We will look into the types and characteristics of file systems supported by Altibase, as well as the necessary configurations.

## Supported File Systems

---

Altibase supports all major file systems except for some that do not support mmap or Direct I/O.

When using Direct I/O, it may be necessary to change the mount options of the file system to enable Direct I/O support.

If the file system does not support Direct I/O, the Altibase properties must be modified accordingly.

For detailed configuration, refer to the manual or the altibase.properties file.

| **OS** | **File System** | **Characteristics** |
| --- | --- | --- |
| Solaris | UFS | Mount option changes are required when using Direct I/O. |
| VxFS |  |  |
| ZFS | Database property changes are required when Direct I/O is not supported. |  |
| HP | HFS |  |
| JFS | Mount option changes are necessary when using Direct I/O |  |
| VxFS | Mount option changes are necessary when using Direct I/O. |  |
| AIX | JFS |  |
| VxFS |  |  |
| Windows | NTFS |  |
| FAT32 |  |  |
| Linux | Ext2/Ext3/Ext4 |  |

## Unsupported File Systems

---

Problems may occur when using Altibase on certain file systems that do not support `mmap` or Direct I/O.

### Raw Storage Device

---

Altibase cannot access files configured on raw devices, so they are not supported.

The main reason for using raw devices in a database is to directly control the OS file cache behavior.

To achieve this, Altibase can use a file system that supports Direct I/O instead of raw devices.

### Certain NFS(Network File System), NAS ( Network attached Storage )

---

On some NFS/NAS file systems that do not support `mmap`, errors may occur during the database creation phase when trying to create data or log files.

# Disk Configuration

---

The performance of a database is closely related to the performance of disk I/O. This section explains key considerations for disk configuration that should be reviewed as a basic requirement.

## Dedicated Storage for the Database

---

To prevent any impact on database performance from external factors such as OS or application disk I/O, these influences must be eliminated at the source.

A dedicated storage system, physically separated from the disks used by the OS and other applications, is required exclusively for the database.

## RAID

---

RAID (Redundant Array of Independent Disks) configurations for databases typically use **RAID 10**, which is known to provide the best IOPS (Input/Output Operations Per Second). RAID 10 is a combination of RAID 1 (mirroring) and RAID 0 (striping).

Since the number of disks required varies depending on the RAID level, the appropriate configuration should be selected in consultation with a storage expert, considering the size of the database and the number of available disks.

- mirror (RAID 1)

Stores identical copies of data on multiple disks, providing resilience against data loss.

- striping (RAID 0)

Splits data into blocks and distributes them across multiple disks, significantly improving read/write speed.

## Disk Performance

---

Disk performance depends on system traffic and should be assessed through maximum traffic testing. For disk-based databases where random I/O operations are frequent, SSDs with high random I/O performance are recommended.

# Disk I/O Optimization

---

The performance of a database is closely related to the Disk I/O performance of the storage. This section explains several methods to improve Disk I/O performance in storage.

## OS File Cache Configuration Changes

---

Proper file cache settings are recommended to suppress swap-out events on the memory areas used by Altibase. This helps minimize delays in Disk I/O caused by swapping at the OS layer, which can lead to performance degradation in Altibase.

File cache is a type of system buffer managed by the operating system to resolve bottlenecks caused by the speed difference between main memory and secondary storage. Although each OS manages its file cache according to its own policies, it generally has a direct relationship with swap policies. Swapping allows handling applications or data files larger than the main memory, which is useful, but in systems running long-resident applications like DBMS, swapping can cause irregular DBMS response times or even hangs due to OS-level Disk I/O delays. Therefore, system usage must consider this factor.

To ensure consistent response times in Altibase, it is advisable to configure file cache and swap kernel parameters to minimize swapping.

For guidance on appropriate file cache settings, please refer to the following documents:

- HPUX Setup Guide for Altibase
- AIX Setup Guide for Altibase
- Solaris Setup Guide for Altibase
- Linux Setup Guide for Altibase

## Direct I/O

---

The OS file system uses a structure like Buffered I/O, which includes a File Buffer Cache memory area to cache accessed file blocks, improving access performance to slow disks.

![diskio_2.png](https://docs.altibase.com/download/attachments/embedded-page/DOCK/21.%20Altibase%20%EB%94%94%EC%8A%A4%ED%81%ACI/O%20%EB%B3%91%EB%AA%A9%EC%9D%84%20%EA%B3%A0%EB%A0%A4%ED%95%9C%20%EB%B3%BC%EB%A5%A8%EA%B5%AC%EC%84%B1%20%EA%B0%80%EC%9D%B4%EB%93%9C/diskio_2.png?api=v2)![disIO.PNG](https://docs.altibase.com/download/attachments/11698413/disIO.PNG?version=1&modificationDate=1490754079000&api=v2)

However, when an application like a DBMS performs data caching at the application level, overhead can occur as data moves from the disk to the file buffer cache and then again to the DB’s own buffer cache. This is called "double copying," and it can result in increased CPU and memory usage.

In such cases, using Direct I/O — a file input/output method that bypasses the OS file cache as shown in the diagram on the right — can reduce CPU and memory consumption by the DBMS.

For Altibase to perform data and log file I/O using Direct I/O, the following Altibase properties must be set:

- DIRECT_IO_ENABLED = 1 # 0: Buffered I/O, 1:Direct I/O
- DATABASE_IO_TYPE = 1 # 0: Buffered I/O, 1:Direct I/O
- LOG_IO_TYPE = 1 # 0: Buffered I/O, 1:Direct I/O

Some operating systems or file systems may not support Direct I/O on files or at the application level, and using Direct I/O may require additional configuration steps.

In such cases, the file system must be mounted with specific options as shown in the example below.

| **OS** | **File System** | **Required Action** |
| --- | --- | --- |
| Solaris | UFS | None |
| VxFS | mount with convosync=direct |  |
| ZFS | Does not support Direct I/O. |  |
| HP | HFS | None |
| JFS | None |  |
| VxFS | mount with convosync=direct |  |
| AIX | JFS | mount with use -o dio |
| VxFS | mount with convosync=direct |  |
| Windows | NTFS | None |
| FAT32 | None |  |
| Linux(2.4 > K ) | Ext2/Ext3/Ext4 | None |

### When Using Direct I/O Is Advantageous

---

Direct I/O can be beneficial when the database size is larger than the system memory and the disk buffer size is large. For example, SAN devices often support large buffers internally, making Direct I/O advantageous in such cases.

In databases that are large and undergo frequent bulk updates, a significant amount of disk I/O occurs during checkpoint processes. The overhead of copying data twice—once to the OS file cache and again to the DB buffer cache—can cause a sharp increase in CPU and memory usage.

In these situations, using Direct I/O can be an effective solution.

### When Using Buffered I/O Is Advantageous

---

Generally, when using local disks, Buffered I/O tends to offer better performance compared to Direct I/O.

OS-level Buffered I/O reads data in multiple blocks and prefetches the necessary disk pages, improving I/O speed. As a result, performance often improves when using Buffered I/O.

## Page Size

---

Altibase uses the term “page size” instead of “block size.”

The page size in Altibase is fixed: memory tables use 32KB per page, and disk tables use 8KB per page. These values cannot be changed.

While other DB vendors sometimes adjust the DB page size at creation time to optimize I/O efficiency by considering the OS block size, Altibase’s page size is fixed and cannot be modified.

Additionally, Altibase does not recommend changing the OS block size to match the DB page size.

There have been no reported cases of performance degradation due to mismatches between Altibase’s page size and the OS block size.

# Korean Source Attachments

The Korean source page also references these downloadable source attachments. They are preserved here so the English document set does not lose those references.

- [Korean source attachment 1 (PDF)](https://docs.altibase.com/download/attachments/11698408/202312_Altibase_%EB%94%94%EC%8A%A4%ED%81%ACIO_%EB%B3%91%EB%AA%A9%EC%9D%84_%EA%B3%A0%EB%A0%A4%ED%95%9C_%EB%B3%BC%EB%A5%A8%EA%B5%AC%EC%84%B1_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=2&modificationDate=1702282370000&api=v2)
- [Korean source attachment 2 (PDF)](https://docs.altibase.com/download/attachments/11698408/201511_ALTIBASE_%EB%94%94%EC%8A%A4%ED%81%ACIO_%EB%B3%91%EB%AA%A9%EC%9D%84_%EA%B3%A0%EB%A0%A4%ED%95%9C_%EB%B3%BC%EB%A5%A8%EA%B5%AC%EC%84%B1_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1701925177000&api=v2)
- [Korean source attachment 3 (PDF)](https://docs.altibase.com/download/attachments/11698408/200912_ALTIBASE_%EB%94%94%EC%8A%A4%ED%81%ACIO_%EB%B3%91%EB%AA%A9%EC%9D%84_%EA%B3%A0%EB%A0%A4%ED%95%9C_%EB%B3%BC%EB%A5%A8%EA%B5%AC%EC%84%B1_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1701925145000&api=v2)
