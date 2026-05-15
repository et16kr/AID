---
title: "Altibase Configuration File Guide"
page_id: "22642991"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/Altibase+Configuration+File+Guide"
updated_at: "2025-10-21T08:50:42.000+0900"
version: 1
ancestors: ["Home"]
labels: []
---

# Altibase Configuration File Guide
Source: https://docs.altibase.com/display/arch/Altibase+Configuration+File+Guide
Updated: 2025-10-21T08:50:42.000+0900

- [Overview](#AltibaseConfigurationFileGuide-Overview) - [Altibase Configuration Items](#AltibaseConfigurationFileGuide-AltibaseConfigurationItems) - [Property Inquiry and Configuration](#AltibaseConfigurationFileGuide-PropertyInquiryandConfiguration) - [Altibase Configuration Guide](#AltibaseConfigurationFileGuide-AltibaseConfigurationGuide) - [Properties that must be changed when creating DB](#AltibaseConfigurationFileGuide-PropertiesthatmustbechangedwhencreatingDB) - [Properties that cannot be changed after creating DB](#AltibaseConfigurationFileGuide-PropertiesthatcannotbechangedaftercreatingDB) - [File path configuration properties](#AltibaseConfigurationFileGuide-Filepathconfigurationproperties) - [Session properties](#AltibaseConfigurationFileGuide-Sessionproperties) - [Resource limit related properties](#AltibaseConfigurationFileGuide-Resourcelimitrelatedproperties) - [Disk I/O Performance-related properties](#AltibaseConfigurationFileGuide-DiskI/OPerformance-relatedproperties) - [PBT(Problem Tracking) related properties](#AltibaseConfigurationFileGuide-PBT(ProblemTracking)relatedproperties)

# Overview

---

This document describes the properties of the altibase.properties file for effective use of Altibase, and how to specify values. This document does not include a description of the hidden property.

This documentation is written based on Altibase versions 7.1.0 and 7.3.0.. It is recommended that users refer to the following documents:

1. System Resource Capacity Planning Guide for Altibase
2. Altibase Replication Configuration Guide

For errors and improvements related to this document, please contact the technical support portal or technical support center.

- Technical support portal: [http://support.altibase.com](http://support.altibase.com/)[/en/](http://support.altibase.com/en/)
- Technical support center: 02-2082-1114

# Altibase Configuration Items

---

For a more detailed description of each property, please refer to the General Reference manual.

Refer to the link below for the manual.

[https://github.com/ALTIBASE/Documents/tree/master/Manuals/Altibase_7.1/eng](https://github.com/ALTIBASE/Documents/tree/master/Manuals/Altibase_7.1/eng)

## Property Inquiry and Configuration

---

Each property can be inquired as follows.

```
iSQL> SELECT name, value1 FROM v$property ;
```

Alternatively, it can also be inquired in the $ALTIBASE_HOME/conf/altibase.properties file. However, when inquiring with a file, some of the hidden property values are not known, and in order to accurately find out the currently applied value, it is recommended to inquire with the above SQL.

The change of each property value can be described in the configuration file or can be changed in real time with the DCL statement (ALTER SYSTEM/ALTER SESSION statement). Some properties are read-only values and some cannot be changed while operating. If a property is changed, the following error occurs.

```
[ERR-0104E: The property [propery_name] is read-only.]
```

When changing the properties in the configuration file, the following format is used.

```
Property name = Property value
Ex) PORT_NO = 20300
```

For example, when changing with a DCL, proceed as follows. (Case-insensitive)

```
iSQL> ALTER SYSTEM SET query_timeout = 30;
iSQL> ALTER SESSION SET query_timeout = 30;
```

In the case of DCL, there are items that can be changed at the session level and the system level. However, in both cases, if Altibase is restarted, it is reset to the value described in the configuration file, so in order to reflect it permanently, the configuration file needs to be changed. (Items that cannot be changed after creating a DB are introduced later in this document.)

# Altibase Configuration Guide

---

Each item described in the $ALTIBASE_HOME/conf/altibase.properties file is summarized by each category and the recommendations are described.

Because the user's system has a wide variety of environments, this recommendation is recommended for general experience. Therefore it is recommended to change and apply the configuration file with prior consultation with Altibase engineers.

## Properties that must be changed when creating DB

---

The items that the user must configure at least when creating the DB are as follows. For the sake of understanding, it is assumed that the disk volume is configured as follows.

| Disk volume | Description |
| --- | --- |
| /home/altibase | Path where Altibase is installed |
| /home/altidata | Directory where data files will be saved |
| /home/altilog | Directory where transaction log files will be saved |

Assuming the above volume configuration, it can be set as follows.

| Configuration Item | Default Value | Description |
| --- | --- | --- |
| DB_NAME | mydb | Configure to any name by the user |
| MEM_DB_DIR | ?/dbs | /home/altidata |
| DEFAULT_DISK_DB_DIR | ?/dbs | /home/altidata |
| LOGANCHOR_DIR | ?/logs | /home/altilog |
| LOG_DIR | ?/logs | /home/altilog |
| ARCHIVE_DIR | ?/arch_logs | It is recommended to specify the backup directory when the archive mode is set. (ex:/home/altibackup/arch_log) |
| MEM_MAX_DB_SIZE | 2G | It is set to the size predicted by calculating the capacity. (ex: 8G) |
| BUFFER_AREA_SIZE | 128M | When using a disk table, the size of the buffer is closely related to performance, so set it large within the range of available physical memory. 1G or more is recommended. |
| PORT_NO | 20300 | Set a port that is not being used by other processes in the system, such as 20300. |
| AUTO_COMMIT | 1 | If it is set to 1, it is automatically reflected in the DB after DML is executed, so if the user wants to control it directly, set it to 0. |
| SQL_PLAN_CACHE | 64M | This is the maximum size of the SQL plan cache. The more replicate SQL is, the more effective the SQL plan cache is to save memory. |
| REPLICATION_PORT_NO | 9 | When replication is required, specify the port. |

## Properties that cannot be changed after creating DB

Once after creating Altibase, there are some properties that Altibase cannot be restarted if it is changed in any form from the initial configuration value. Therefore, it is recommended to configure these properties carefully when initially configuring them.

| Configuration item | Description |
| --- | --- |
| DB_NAME | mydb (Specify when creating) |
| LOG_FILE_SIZE | 10M (Specify when creating) |
| EXPAND_CHUNK_PAGE_COUNT | 128 (Specify when creating) |
| TRANSACTION_TABLE_SIZE | 1024 (Only upward adjustment is possible) |
| CHARACTERSET | Specify when creating DB |

## File path configuration properties

---

This section only deals with files with configuration paths for transaction log files and data files. Generally, if the transaction log file and data file are specified to use the same disk on one disk, performance degradation occurs due to simultaneous disk I/O. Therefore, it is recommended to change each configuration item by referring to the following document.

Reference: Configuration Guide For Minimizing Disk I/O Contention

| Configuration item | Default Value | Description |
| --- | --- | --- |
| LOG_DIR | ?/logs | Directory where transaction log files are created |
| MEM_DB_DIR | ?/logs | Directory where data files of the memory DB are created unless the user does not explicitly specify it. |
| DEFAULT_DISK_DB_DIR | ?/logs | Directory where disk files of the disk DB are created unless the user does not explicitly specify it. |

It is recommended that the above three paths and each data file to be created by the user in the future use a disk that is physically separated from LOG_DIR.

## Session properties

---

The properties related to the session are the following items.

| Configuration item | Default Value | Description |
| --- | --- | --- |
| MAX_CLIENT | 1000 | Because there is a limit of sessions to connect to the DB at the same time, if it is expected that more sessions will be connected than this value, increase this value and restart the Altibase server. |
| MULTIPLEXING_THREAD_COUNT | Number of logical cores on the host machine | This value specifies the number of service threads. If not set, threads as much as the number of cores of the CPU is automatically created in the startup stage. If many sessions are internally connected, it is automatically created when it is determined that more service threads are needed., but the distribution of tasks at the time of creation can cause temporary performance jitter, so it is important to configure to obtain a sufficient number in advance. |

It is recommended for MULTIPLEXING_THREAD_COUNT to be (CPU Core Count * 2) by default, but this value should be set according to the situation.

## Resource limit related properties

---

The resources used by Altibase refer to resources such as physical memory/disk space and logical tablespace. This section describes each property that flexibly limits query execution, such as a large number of changes at the session/system level, which can lead to resource shortages. It is recommended that these properties be operated to change//apply only necessary sessions with configuration change at the session-level rather than changing the default configuration.

| Configuration item | Default Value | Description |
| --- | --- | --- |
| LOCK_ESCALATION_MEMORY_SIZE | 100M | When performing a bulk change operation on a memory DB table, if the size of the changed record exceeds this property value, a table lock is acquired and a query is executed (Can only be changed at the system-level) |
| TRX_UPDATE_MAX_LOGSIZE | 10M | If the amount of transaction log created by query processing is more than this property value, the following error is returned:<br>The update log size '10485873' is bigger than TRX_UPDATE_MAX_LOGSIZE '10485760' |
| PREPARE_STMT_MEMORY_MAXIMUM | 200M | If the amount of memory used in the prepare stage by query processing is more than this property value, the following error is returned:<br>The memory size allocated for the statement has exceeded the maximum limit ( Name : Query_Prepare, Wanted Memory Size : 1073741832, Max size : 1073741824 ) |
| EXECUTE_STMT_MEMORY_MAXIMUM | v7.1.0 : 1024M<br>v7.3.0 : 2048M | If the amount of memory used in the execute stage by query processing is more than this property value, the following error is returned:<br>The memory size allocated for the statement has exceeded the maximum limit ( Name : Query_Execute, Wanted Memory Size : 1073807360, Max size : 1073741824 ) |
| QUERY_TIMEOUT | 600 sec | If the time exceeds this property value after executing the query, the following error is returned:<br>Client's query exceeded the execution time limit. |
| FETCH_TIMEOUT | 60 sec | In the process of exchanging the result set created after the query was normally executed, if communication does not occur even after this property value elapses between the previous communication and the next communication, the session is terminated.<br>The session has been closed by the server |
| UTRANS_TIMEOUT | 3600 sec | After the change query is executed, if the execution of Commit/Rollback does not occur even after as much time as this property value, the session is terminated.<br>The transaction has exceeded the lock timeout specified by the user. |
| IDLE_TIMEOUT | 0 | If the session is maintained as much as this property value without any action, the session is forcibly terminated.<br>The session has been closed by the server. |

An example of how to change is as follows.

```
iSQL> ALTER SESSION SET TRX_UPDATE_MAX_LOGSIZE = 20000000 ;
iSQL> ALTER SYSTEM  SET TRX_UPDATE_MAX_LOGSIZE = 10000000 ;
iSQL> ALTER SESSION SET QUERY_TIMEOUT = 3600 ;
iSQL> ALTER SESSION SET UTRANS_TIMEOUT = 60 ;
```

- Since all the QUERY/IDLE/UTRANS/FETCH Timeout properties and errors related to the session are recorded in altibase.boot.log, find the session and take action when it occurs.
- Notes/Considerations for ALTER SYSTEM and ALTER SESSION: ALTER SYSTEM changes will take effect from the subsequent sessions. Therefore, since the currently connected session is not applied, the desired result can be applied only by performing ALTER SESSION for individual connected sessions.

## Disk I/O Performance-related properties

---

This describes the property items related to Altibase's disk I/O performance.

| Configuration item | Default Value | Description |
| --- | --- | --- |
| BUFFER_AREA_SIZE | 128M | Specify the buffer size of the disk DB. If there is enough memory in the system, it is recommended to set it as large as possible. |
| BUFFER_FLUSHER_CNT | 2 | This is a thread that writes a buffer to the disk to secure dirty pages in the disk DB or free space in the buffer, and adjusts according to the number of CPUs or disk I/O performance of the system. |
| PREPARE_LOG_FILE_COUNT | 5 | A separate thread creates an empty log file to record the transaction log. If this value is too small, performance may be degraded if the transaction progress has to wait for the creation of an empty log file. Therefore, if thhe LF_PREPARE_WAIT_COUNT value of v$lfg appears to be larger, the value must be adjusted accordingly. Even if it is set too large, disk I/O load that actually creates an empty log file will occur, so it is recommended to change it carefully by testing. |
| CHECKPOINT_BULK_WRITE_PAGE_COUNT | 0 | When it is determined that performance is degraded due to the disk I/O that occurs because there are many pages to be written when the memory DB checkpoint is in progress, the amount of disk I/O of the checkpoint can be distributed with this property value. In other words, after writing the page as much as the value specified in CHECKPOINT_BULK_WRITE_PAGE_COUNT, it waits for (CHECKPOINT_BULK_WRITE_SLEEP_SEC + CHECKPOINT_BULK_WRITE_SLEEP_USEC) and then writes again. This property can be effective on equipment with low disk performance. |
| CHECKPOINT_BULK_WRITE_SLEEP_SEC | 0 sec |  |
| CHECKPOINT_BULK_WRITE_SLEEP_USEC | 0 microsec |  |
| DIRECT_IO | 1 | In the process of writing to a data file with the file cache, it may be difficult to predict two disk writes (file cache, disk sync) and when the file cache will be synced to the disk. As a result, there may be an unexpected performance degradation when the operating system empties the file cache. If DIRECT IO is set, it can be completed with one write. However, it is recommended to set this setting only when the disk performance is high enough. |
| DATABASE_IO_TYPE | 0 |  |
| TOTAL_WA_SIZE | 128M | Specify the maximum amount of memory that can be allocated so that disk DB sorting or hashing operations can be performed simultaneously. (TOTAL_WA_SIZE)<br>If SORT_AREA_SIZE and HASH_AREA_SIZE are increased appropriately, the performance of the disk DB can be improved. |
| SORT_AREA_SIZE | 1M |  |
| HASH_AREA_SIZE | 4M |  |

## PBT(Problem Tracking) related properties

---

This section describes properties necessary for tracking when a problem occurs in Altibase.

| Configuration item | Default Value | Description |
| --- | --- | --- |
| QP_MSGLOG_FLAG | 2 | If it is set to 2, all DDL performance records can be checked, so when a problem occurs, which can be helpful for analysis if DDL performance is based. |
| RP_CONFLICT_MSGLOG_FLAG | 0 | If it is set to 6, a log of DML occurs when a replication conflict is recorded. which can be helpful for analysis. |
| TIMED_STATISTICS | 0 | The default value is 0. To know the execution times of each SQL statement related to performance, it can be activated in real time as follows.<br>iSQL> ALTER SYSTEM SET timed_statistics = 1 ;<br>When activated, the execution times of each SQL statement start to be recorded in v$statement. |
