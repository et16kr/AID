# Architecture, Storage, and Disk Concepts

## Source paths

R006 source paths covered in this revision:

- `arch/Home/Home/ALTIBASE HDB White papers__4030581.md`
- `arch/Home/Home/Storage Guide__9110563.md`
- `arch/Home/Disk Configuration Guide for Altibase__14647508.md`
- `arch/Home/Disk Configuration Guide for Altibase/1. Disk I_O Occurrence Type__14647512.md`
- `arch/Home/Disk Configuration Guide for Altibase/2. Data File Configuration Plan__14647521.md`
- `arch/Home/Disk Configuration Guide for Altibase/3. File System__14647523.md`
- `arch/Home/Disk Configuration Guide for Altibase/4. Disk Configuraiton__14647527.md`
- `arch/Home/Disk Configuration Guide for Altibase/5. Disk I_O Optimization__14647545.md`
- `arch/Home/Configuration Guide For Minimizing Disk I_O Contention__22643018.md`
- `FAQE/Home/13. General/The entire database exists in memory. Is there any problem with the safety of the data__22642980.md`
- `FAQE/Home/13. General/What interface does Altibase provide__22642982.md`
- `FAQE/Home/13. General/What is the biggest difference between Altibase and disk-based DBMS__16876485.md`

## Source coverage notes

This document covers the R006 portion of `llm-reference/02-architecture-storage-concepts.md`: Altibase architecture concepts, memory and disk DBMS behavior, WAL, checkpoints, storage files, disk I/O contention, Direct I/O, file-system support, RAID/storage guidance, and the general FAQ concepts assigned to this job.

All R006 source files are classified as `Korean-source-verified` or `Link-validated Korean-source-verified` in `llm-reference/coverage/source-inventory.tsv`. No English-only auxiliary source is used in this R006 consolidation.

The split `arch/Home/Disk Configuration Guide for Altibase/**` pages and `arch/Home/Configuration Guide For Minimizing Disk I_O Contention__22643018.md` intentionally overlap. The consolidated `Configuration Guide For Minimizing Disk I/O Contention` page is the canonical source for the normalized English wording, while the split pages provide duplicate coverage evidence for redo log, checkpoint, disk DB, undo tablespace, disk layout, file-system, RAID, Direct I/O, and page-size units.

The source set contains downloadable PDF attachments and embedded diagrams/images. Downloadable document-format URLs are preserved exactly in the attachment register and in this document. Embedded diagrams are not document-format attachments; their URLs are preserved in the attachment register, and this document covers the surrounding textual meaning without reconstructing visual content. No R006 source contains a missing Gliffy/export diagram placeholder, so no `diagram_unavailable` row is needed for this job.

The white-paper source page lists PDF attachments only. R006 preserves the labels and URLs from that Markdown page; it does not claim to extract the PDF bodies.

## Scope and audience

Use this document to answer architecture, storage, WAL, checkpoint, durability, disk layout, Direct I/O, file-system, and general interface questions about Altibase. It is written for DBAs, platform engineers, support engineers, and LLM answer generation systems that must preserve exact paths, property names, technology names, version conditions, and attachment URLs.

When answering in another language, keep product names, commands, SQL/API names, configuration properties, paths, file names, version strings, and attachment URLs exactly as written.

## Key facts

Altibase is a hybrid DBMS. It supports both in-memory database operation and disk-based database operation in the same product. In a disk-based DBMS, the entire database resides on disk and data needed for processing is cached in memory buffers. In an in-memory DBMS, the backup database stored on disk is loaded into main memory and managed there.

Altibase memory-table data is managed in fixed 32KB pages. Each memory page is divided into slots according to the record size of the table that owns the page. Altibase disk-table buffer pages are fixed at 8KB. These page sizes cannot be changed, and Altibase does not recommend changing the OS block size to match them; the source states that no performance degradation case has been reported from mismatch between Altibase page size and OS block size.

Altibase uses WAL (Write Ahead Logging) for transaction durability. Redo logs are written before database pages are saved so that committed transaction information exists on disk and can be used for recovery after abnormal termination. Redo logs record changes to data and changes to resources required for transaction processing.

Redo logs are first recorded in an `mmap` memory-mapped area and are periodically saved to redo log files by `LogSyncThread`. This default behavior minimizes frequent disk I/O for performance. The source says log loss does not occur unless there is a power failure or an OS hang, and that the redo log writing method can be changed by properties when high transaction performance is not required.

For memory tables, modified pages are registered in an internal dirty-page list. A checkpoint saves those dirty pages to physical storage. Checkpoints are necessary because memory is volatile. The general FAQ also states that checkpoints occur when the number of log files exceeds a configured threshold or when a fixed interval is reached, and that checkpoints minimize recovery time.

For disk tables, all data is stored in disk files. Altibase reduces disk access cost by using a user-sized buffer area made of 8KB pages. When a disk-table query runs, Altibase first checks whether the required data is already in the buffer. If not, it reads the data from the physical datafile. Modified pages are registered in the Flush List and are written to disk when flushing occurs. If the buffer lacks free space, the LRU algorithm stores rarely accessed pages to disk and reuses the space; this is called `BufferReplace`.

Memory tables use an MVCC-style out-place update method: an undo image is managed in memory, original data is copied to a separate area, and the change is applied to the copy. Disk tables use an in-place update method: original data is copied to the undo tablespace and the original location is changed. During recovery, original data from the undo tablespace is copied back to its original location.

Disk I/O contention occurs when redo log writes, memory-table checkpoints, disk-table buffer flushes, disk-table `BufferReplace`, disk index activity, and disk undo writes compete on the same physical disk. The R006 sources repeatedly recommend separating redo logs, memory table datafiles, disk table datafiles, disk indexes, disk undo tablespace files, and `$ALTIBASE_HOME` onto physically separate disks when the environment allows it.

Memory indexes do not require a separate disk for index I/O. They are rebuilt in memory after the memory DB is loaded during Altibase startup, and memory index changes are not logged separately.

Altibase supports major file systems except file systems that do not support `mmap` or Direct I/O. Raw storage devices are not supported because Altibase cannot access files configured on raw devices. Some NFS/NAS file systems that do not support `mmap` can cause errors during database creation when Altibase creates data files or log files.

Direct I/O bypasses the OS file buffer cache. It can reduce CPU and memory overhead from double copying when a DBMS already performs application-level caching. Buffered I/O can be faster for local disks because OS buffered I/O can read multiple blocks and prefetch required disk pages.

RAID 10 is the database RAID configuration emphasized by the disk configuration source because it is known for strong IOPS. RAID 10 combines RAID 1 mirroring and RAID 0 striping. RAID 1 stores identical copies on multiple disks to reduce data-loss risk; RAID 0 divides data into blocks and distributes them across multiple disks to improve read/write speed. The source recommends choosing a RAID level with a storage expert based on database size and available disks.

For disk-based databases with frequent random I/O, SSDs with high random I/O performance are recommended. Disk performance depends on system traffic and should be evaluated with a maximum traffic test.

The general FAQ states that in-memory DBMS performance is about 4 to 10 times faster than disk-based DBMS performance depending on the operating environment. It also records that Altibase HDB was measured in `Memory Only`, `Hybrid`, and `Disk Only` modes with five TPC-C OLTP transaction types: order, payment, delivery, order status, and stock level.

Altibase complies with ANSI SQL-1999 and provides standard interfaces including `ODBC`, `ADO.NET`, `JDBC`, and Embedded SQL. The R006 interface FAQ is based on Altibase HDB 6.1.1 or later.

## Procedures

### Plan disk layout to avoid contention

1. Place database storage on dedicated storage that is physically separated from OS and application disks. The disk configuration source states that OS or application disk I/O should be eliminated as a direct influence on database performance.
2. Separate redo logs from other database files whenever possible. Even the minimum model requires redo logs on a separate physical disk.
3. For stronger separation, place these categories on separate physical disks:

| Classification | Example disk path |
| --- | --- |
| `$ALTIBASE_HOME` | `/ALTIBASE` |
| Redo logs | `/ALTIBASE_REDO_LOG` |
| Memory table datafiles | `/ALTIBASE_MEMORY_DATA` |
| Disk table datafiles | `/ALTIBASE_DISK_DATA` |
| Disk indexes | `/ALTIBASE_DISK_INDEX` |
| Disk undo tablespace datafiles | `/ALTIBASE_DISK_UNDO` |

4. Keep `$ALTIBASE_HOME` separate when possible because it stores binaries, headers, libraries, operation files, and important trace logs generated during operation.
5. Separate disk DB datafiles and disk indexes to reduce contention caused by datafile expansion or DB schema changes.
6. Treat disk backup planning as a separate backup/recovery topic. The disk configuration source explicitly does not describe disk considerations for backup.

### Use the minimum separation model

Use the minimum separation model only when the system mainly uses memory DB, the disk DB workload has few changes, or the system has only the minimum number of disks.

| Classification | Example disk path |
| --- | --- |
| Redo logs | `/ALTIBASE_REDO_LOG` |
| `$ALTIBASE_HOME` and all datafiles | `/ALTIBASE` |

This model can reduce disk I/O contention only for memory-DB-heavy environments or disk DB services with few update operations.

### Use separated disk DB paths for mixed workloads

When diverse workloads and large amounts of data are configured as disk DB, separate tablespaces for complex queries from tablespaces used mainly for simple processing, and place their physical datafiles on separate disks.

| Classification | Example disk path |
| --- | --- |
| Redo logs | `/ALTIBASE_REDO_LOG` |
| `$ALTIBASE_HOME` and memory table datafiles | `/ALTIBASE` |
| Disk table datafiles 1, complex tasks | `/ALTIBASE_DISK_COMPLEX` |
| Disk table datafiles 2, simple tasks | `/ALTIBASE_DISK_SIMPLE` |

This can distribute disk I/O, but the source warns that it may be less effective when disk `BufferReplace` occurs frequently.

### Choose and configure Direct I/O or Buffered I/O

Use Direct I/O when the database is larger than system memory and the storage device has a large disk buffer, such as some SAN devices. Direct I/O is also a solution when large databases receive frequent bulk updates and checkpoint activity causes CPU and memory overhead from double copying between OS file cache and DB buffer cache.

Use Buffered I/O when local disk behavior benefits from OS-level multi-block reads and prefetching. The source says Buffered I/O is generally better for local disks.

To enable Direct I/O for Altibase data and log file I/O, configure these Altibase properties:

```properties
DIRECT_IO_ENABLED = 1 # 0: Buffered I/O, 1:Direct I/O
DATABASE_IO_TYPE = 1 # 0: Buffered I/O, 1:Direct I/O
LOG_IO_TYPE = 1 # 0: Buffered I/O, 1:Direct I/O
```

Some operating systems or file systems require mount options before Direct I/O can be used. If the file system does not support Direct I/O, modify Altibase properties accordingly and refer to the manual or `altibase.properties`.

### Plan data durability and failure response

Use WAL and checkpoints as the normal durability mechanism for memory data. Use backup and recovery for abnormal DBMS situations and for restoring a logical or physical database copy. Online backup can create a database copy while the database is operating, and recovery can be complete or incomplete depending on the available backup and logs.

For failure handling:

| Failure type | Cause | Resolution basis |
| --- | --- | --- |
| Transaction failure | A transaction is interrupted by internal or external factors. | Altibase maintains consistency through normal transaction rollback. |
| System failure | Operating system defect or failure such as power outage. | On restart, Altibase performs restart recovery using backup data files and active logs to recover to the system-failure point. |
| Disk failure | A backup data file is corrupted because of an error on the disk where the backup data file is stored. | Restore from a previous data backup file if one exists. If the log disk is damaged or archive logs are deleted, recovery to the most recent state is impossible. |

## SQL, commands, and configuration

No R006 source defines SQL statements that must be executed for architecture or storage setup. The answer-affecting configuration items are storage paths, file-system mount options, Direct I/O properties, supported interfaces, and version-specific API support.

### Direct I/O mount actions

| OS | File system | Required action |
| --- | --- | --- |
| Solaris | `UFS` | None |
| Solaris | `VxFS` | Mount with `convosync=direct` |
| Solaris | `ZFS` | Direct I/O is not supported |
| HP | `HFS` | None |
| HP | `JFS` | None |
| HP | `VxFS` | Mount with `convosync=direct` |
| AIX | `JFS` | Mount with `-o dio` |
| AIX | `VxFS` | Mount with `convosync=direct` |
| Windows | `NTFS` | None |
| Windows | `FAT32` | None |
| Linux `(2.4 > K )` | `Ext2/Ext3/Ext4` | None |

### Supported file-system matrix

| OS | File system | Source note |
| --- | --- | --- |
| Solaris | `UFS` | Mount option changes are required when using Direct I/O. |
| Solaris | `VxFS` | Supported by source table. |
| Solaris | `ZFS` | Database property changes are required because Direct I/O is not supported. |
| HP | `HFS` | Supported by source table. |
| HP | `JFS` | Mount option changes are required when using Direct I/O. |
| HP | `VxFS` | Mount option changes are required when using Direct I/O. |
| AIX | `JFS` | Supported by source table. |
| AIX | `VxFS` | Supported by source table. |
| Windows | `NTFS` | Supported by source table. |
| Windows | `FAT32` | Supported by source table. |
| Linux | `Ext2/Ext3/Ext4` | Supported by source table. |

### Client interface support

| Interface type | Supported functions and version notes |
| --- | --- |
| `ODBC` | Used to access Altibase from most development environments, including RAD tools such as Visual Basic and PowerBuilder; standard support is reinforced through reimplementation. |
| `JDBC` | Used for Java application programs and WAS connection pools; supports `JDBC 2.0 API` up to Altibase 6.1.1 with partial `JDBC 3.0 API`; supports `JDBC 3.0 API` from Altibase 6.3.1; supports `JDBC 3.0 API` and partial `JDBC 4.2 API` from Altibase 7.1.0; supports `JDBC 4.2 API` from Altibase 7.3.0. |
| `SQLCLI` | Altibase low-level C API; provides `LOB API`, `ALA (ALTIBASE Log Analyzer) API`, and `ACS (ALTIBASE Call-Level for Spatial) API`. |
| Embedded SQL (Pre-Compiler) | Interface used from C or C++ host languages; improves productivity by allowing SQL statements to be used directly in the host language. |
| `ADO.NET` | Up to Altibase 6.5.1, provides a .NET Data Provider based on the .NET Framework. From Altibase 7.1.0.8.3 / 7.3.0.0.5 and later, provides Altibase ADO.NET based on .NET Core 3.1. |
| Unix ODBC | Standard DB connection API compatible with Windows ODBC source on Unix; provides compatibility with ETL tools such as DataStage and Informatica and OLAP tools such as MSTR and Sagent. |
| `PDO` | Provided based on PHP 5.3.3, PHP 7.1.20, and PHP 8.1.8. |
| Hibernate Support | Hibernate 6.4 is supported starting from Altibase 7.1.0.9.2 and Altibase 7.3.0.0.2. |

### Server development capabilities

| Function | Characteristics |
| --- | --- |
| SQL | Supports full-featured SQL92, internationally standardized complex queries such as Sub Query and INLINE View, and tuning with hints and SQL execution plans. |
| Built-in Function | Provides more than 100 built-in functions. |
| Stored Procedure & Function | Supports Stored Procedure and Stored Function based on ANSI SQL, sending a Result Set to the client from a procedure, Structured Type and Array Type in procedures, and Dynamic SQL/DDL in procedures. |
| View | Supports efficient queries by unioning multiple tables or creating a view from specific SQL. |
| Trigger | Supports standard Trigger functionality for business logic based on data events and supports Update Trigger for a specific column. |

## Validation and troubleshooting

When diagnosing disk I/O contention, check whether redo log writing, checkpoint flushing, disk-table buffer flushing, disk-table `BufferReplace`, disk index activity, or disk undo tablespace writes are concentrated on the same physical disk. If they are, move the highest-contention areas to physically separate disks, starting with redo logs.

If checkpoints become heavy, verify whether in-memory transaction volume is creating many dirty pages and whether memory table datafiles share a disk with redo logs or disk DB files.

If disk DB performance degrades, verify buffer hit behavior, flush activity, and `BufferReplace` frequency. The split-source example that separates complex-query tablespaces from simple-processing tablespaces is less effective when disk `BufferReplace` is frequent.

If database creation fails on NFS/NAS storage, verify whether the file system supports `mmap`. The R006 source warns that some NFS/NAS file systems that do not support `mmap` can cause errors while creating data or log files.

If Direct I/O is configured but not working, verify both Altibase properties and OS/file-system mount requirements. Some file systems do not support Direct I/O or require mount options such as `convosync=direct` or `-o dio`. `ZFS` is explicitly listed as not supporting Direct I/O in the source tables.

If OS swapping causes irregular response time or hang-like behavior, review OS file cache and swap kernel settings from the platform setup documents referenced by the source: HPUX Setup Guide for Altibase, AIX Setup Guide for Altibase, Solaris Setup Guide for Altibase, and Linux Setup Guide for Altibase.

If a disk failure affects backup data files, recovery depends on the previous data backup and available logs. If the log disk is damaged or archive logs have been deleted, recovery to the most recent state is impossible.

## Version-specific notes

| Source area | Version condition |
| --- | --- |
| `arch/Home/Home/Storage Guide__9110563.md` | Up to date as of ALTIBASE HDB version 6.5. |
| `arch/Home/Disk Configuration Guide for Altibase__14647508.md` | Test environment is Altibase version 6 or later. |
| `arch/Home/Configuration Guide For Minimizing Disk I_O Contention__22643018.md` | Based on Altibase 6.5 or later. |
| `FAQE/Home/13. General/The entire database exists in memory...` | Applicable to all versions of ALTIBASE HDB. |
| `FAQE/Home/13. General/What interface does Altibase provide__22642982.md` | Based on Altibase HDB 6.1.1 or later, with later API-specific version conditions preserved in the interface table. |
| `FAQE/Home/13. General/What is the biggest difference...` | Applicable to all versions of ALTIBASE HDB. |

## Related errors

The R006 source set does not list exact Altibase error codes. It does describe failure and error conditions that affect answerability:

- Some NFS/NAS file systems that do not support `mmap` can cause errors during database creation when data files or log files are created.
- Disk failure can make latest-state recovery impossible if the log disk is damaged or archive logs are deleted.
- Power failure or OS hang are the source-listed cases where redo log loss can occur despite the default `mmap` and `LogSyncThread` behavior.

## Attachments and external references

Downloadable PDF attachments preserved from the R006 source set:

- `Altibase White Paper 110630.pdf`: https://docs.altibase.com/download/attachments/4030581/Altibase%20White%20Paper%20110630.pdf?version=1&modificationDate=1338527626000&api=v2
- `User Memory Tablespaces Overview.pdf`: https://docs.altibase.com/download/attachments/4030581/User%20Memory%20Tablespaces%20Overview.pdf?version=1&modificationDate=1338527626000&api=v2
- `ALTIBASE HDB Replication Services Whitepaper.pdf`: https://docs.altibase.com/download/attachments/4030581/ALTIBASE%20HDB%20Replication%20Services%20Whitepaper.pdf?version=1&modificationDate=1338527626000&api=v2
- `ORACLE_to_ALTIBASE_migration_white_paper.pdf`: https://docs.altibase.com/download/attachments/4030581/ORACLE_to_ALTIBASE_migration_white_paper.pdf?version=1&modificationDate=1338527626000&api=v2
- `202312_Altibase_디스크IO_병목을_고려한_볼륨구성_가이드.pdf`: https://docs.altibase.com/download/attachments/11698408/202312_Altibase_%EB%94%94%EC%8A%A4%ED%81%ACIO_%EB%B3%91%EB%AA%A9%EC%9D%84_%EA%B3%A0%EB%A0%A4%ED%95%9C_%EB%B3%BC%EB%A5%A8%EA%B5%AC%EC%84%B1_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=2&modificationDate=1702282370000&api=v2
- `201511_ALTIBASE_디스크IO_병목을_고려한_볼륨구성_가이드.pdf`: https://docs.altibase.com/download/attachments/11698408/201511_ALTIBASE_%EB%94%94%EC%8A%A4%ED%81%ACIO_%EB%B3%91%EB%AA%A9%EC%9D%84_%EA%B3%A0%EB%A0%A4%ED%95%9C_%EB%B3%BC%EB%A5%A8%EA%B5%AC%EC%84%B1_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1701925177000&api=v2
- `200912_ALTIBASE_디스크IO_병목을_고려한_볼륨구성_가이드.pdf`: https://docs.altibase.com/download/attachments/11698408/200912_ALTIBASE_%EB%94%94%EC%8A%A4%ED%81%ACIO_%EB%B3%91%EB%AA%A9%EC%9D%84_%EA%B3%A0%EB%A0%A4%ED%95%9C_%EB%B3%BC%EB%A5%A8%EA%B5%AC%EC%84%B1_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1701925145000&api=v2

Embedded source images and diagrams are preserved by URL in `llm-reference/coverage/attachment-diagram-register.tsv`. They include the Storage Guide Direct I/O image, the Data File Configuration Plan redo/disk I/O image, the Disk I/O Optimization Direct I/O image, the configuration guide disk I/O images, and the general FAQ architecture/performance images. Their surrounding textual meaning is consolidated here; their pixels are not reconstructed.

External references preserved from the source set:

- Altibase technical support portal: http://support.altibase.com/en/
- Altibase technical support center: `02-2082-1114`
- Related source document: `Configuration Guide For Minimizing Disk I/O Contention`, https://docs.altibase.com/pages/viewpage.action?pageId=22643018

## Terminology

- `Altibase`, `ALTIBASE HDB`: Product names; keep exact capitalization from the cited source when quoting or referencing a title.
- `WAL`, `Write Ahead Logging`: Transaction durability mechanism that writes logs before database pages.
- `redo log`: Recovery log that records transaction changes and related resource changes.
- `mmap`: Memory-mapped area used before redo logs are periodically saved to redo log files.
- `LogSyncThread`: Thread that periodically saves redo logs to redo log files.
- `checkpoint`: Process that writes dirty memory-table pages to physical storage.
- `dirty page`: Modified page registered internally for checkpoint flushing.
- `memory table`, `disk table`: Altibase storage modes with fixed page sizes of 32KB and 8KB respectively.
- `Flush List`: Internal list of modified disk-buffer pages that must be written to disk.
- `LRU`, `BufferReplace`: Buffer replacement behavior used when disk-table buffer space is insufficient.
- `MVCC`: Method used by memory tables with out-place updates and in-memory undo images.
- `undo tablespace`: Disk-table recovery area that stores original data before in-place updates.
- `Direct I/O`, `Buffered I/O`: File I/O modes; Direct I/O bypasses OS file cache, while Buffered I/O uses OS cache and prefetch behavior.
- `DIRECT_IO_ENABLED`, `DATABASE_IO_TYPE`, `LOG_IO_TYPE`: Altibase properties that control Direct I/O use for datafiles and log files.
- `RAID 10`, `RAID 1`, `RAID 0`: Storage configuration terms; do not translate the identifiers.
- `$ALTIBASE_HOME`, `/ALTIBASE_REDO_LOG`, `/ALTIBASE_MEMORY_DATA`, `/ALTIBASE_DISK_DATA`, `/ALTIBASE_DISK_INDEX`, `/ALTIBASE_DISK_UNDO`: Source path examples that must remain exact.
- `ODBC`, `JDBC`, `SQLCLI`, Embedded SQL, `ADO.NET`, Unix ODBC, `PDO`, Hibernate Support: Interface names preserved from the FAQ source.
- `ALA`, `ACS`, `LOB API`: `SQLCLI`-related API names.
- `SQL92`, `ANSI SQL-1999`, Sub Query, INLINE View, Stored Procedure, Stored Function, Dynamic SQL/DDL, View, Trigger: Server-side SQL capability terms from the source.
