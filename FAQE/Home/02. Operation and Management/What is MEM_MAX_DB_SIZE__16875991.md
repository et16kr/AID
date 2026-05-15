---
title: "What is MEM_MAX_DB_SIZE?"
page_id: "16875991"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16875991"
updated_at: "2021-04-02T11:29:11.000+0900"
version: 2
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# What is MEM_MAX_DB_SIZE?
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16875991
Updated: 2021-04-02T11:29:11.000+0900

- [Overview](#WhatisMEM_MAX_DB_SIZE?-Overview) - [Target versions](#WhatisMEM_MAX_DB_SIZE?-Targetversions) - [Description](#WhatisMEM_MAX_DB_SIZE?-Description) - [Maximum Value](#WhatisMEM_MAX_DB_SIZE?-MaximumValue) - [How to Change](#WhatisMEM_MAX_DB_SIZE?-HowtoChange) - [When to set it larger than the current value](#WhatisMEM_MAX_DB_SIZE?-Whentosetitlargerthanthecurrentvalue) - [When to set it less than the current value](#WhatisMEM_MAX_DB_SIZE?-Whentosetitlessthanthecurrentvalue) - [DB restart](#WhatisMEM_MAX_DB_SIZE?-DBrestart) - [How to change](#WhatisMEM_MAX_DB_SIZE?-Howtochange) - [Possible error messages](#WhatisMEM_MAX_DB_SIZE?-Possibleerrormessages) - [Check the setting value](#WhatisMEM_MAX_DB_SIZE?-Checkthesettingvalue) - [Reference](#WhatisMEM_MAX_DB_SIZE?-Reference)

# Overview

---

This page explains what `MEM_MAX_DB_SIZE` means and how to change it.

# Target versions

---

- All Altibase versions

# Description

---

- This refers to the **maximum amount of memory that can be used as a memory tablespace (memory table or memory data)** stored in physical memory.
- Constraints on the total usage of all memory tablespaces combined.
- This is not the maximum size that each of the memory tablespaces can use.
- The size of the index created on the memory table **is not included.**
- **It also includes historical data that occurs when performing change transactions.**
  When a change transaction is performed, the past data is retained until the transaction is terminated (MVCC technique). In the case of a memory table, a replica of the record is created in the memory table.
- If the maximum value is not specified when creating a memory tablespace, it is automatically expanded by the value set for MEM_MAX_DB_SIZE.

# Maximum Value

---

- **It is recommended to set it to about 60~70% of the physical memory.**
- **In addition to the memory data, must consider the size of the record replicas**that will be created by the MVCC technique when performing a change transaction.
  For example, if a change transaction occurs in a 1G memory table, the size of the table may be 2G when the transaction is completed.
- Since memory is a shared resource that should be used by the OS and other processes as well as the Altibase server process, it should be set lesser than the physical memory.
- Although it is possible to set MEM_MAX_DB_SIZE larger than the physical memory, if the memory is used beyond the physical memory, swap in/out may occur, resulting in performance degradation and various problems in the system.

# How to Change

---

## When to set it larger than the current value

---

This section describes the parts to be considered when setting MEM_MAX_DB_SIZE larger than the current value.

### Disk space

Memory tablespaces store two sets of 'memory checkpoint image files on disk for backup purposes. So it requires **twice as much disk space as the memory data usage.**

If MEM_MAX_DB_SIZE is set large, disk usage will also increase, so make sure to free up disk space before changing MEM_MAX_DB_SIZE.

Ex) If MEM_MAX_DB_SIZE is 60G, 120G of disk space is required.

### User environment setting (Linux/Unix)

The user should run ulimit -a to make sure that the settings below are **set to the maximum values allowed by the OS.**

max memory size virtual memory

### Kernel parameters (AIX, HP-UX)

For AIX, check if data, rss, fsize, etc. are set to -1 in the /etc/security/limits file.

For HP, check that the maxdsiz_64bit value is set large enough via kctune.

Linux and SunOS are not applicable.

## When to set it less than the current value

---

This section describes the parts to be considered when setting MEM_MAX_DB_SIZE less than the current value.

- MEM_MAX_DB_SIZE cannot be set less unconditionally.
- Check the increased 'Checkpoint Image File' size and set it larger than that.
  Its size can be checked with the statement below.

If TOTAL is less than MAX, set MEM_MAX_DB_SIZE to be larger than TOTAL and smaller than the existing value.

If the user copies the SQL statement in IE, a blank line may appear, so please use the attached file if necessary. total_memory_tablespaces_usage.txt

```
set linesize 1024
set colsize 20
SELECT TO_CHAR(MEM_MAX_DB_SIZE/1024/1024, '999,999,999') '       MAX(M)',                                       -- MAX(M)   : MEM_MAX_DB_SIZE setting value
       TO_CHAR(MEM_ALLOC_PAGE_COUNT*32/1024, '999,999,999') '     TOTAL(M)',                                    -- TOTAL(M) : The total page size allocated to the memory tablespace. Also refers to the size of the checkpoint image file.
       TO_CHAR((MEM_ALLOC_PAGE_COUNT-MEM_FREE_PAGE_COUNT)*32/1024, '999,999,999') '     ALLOC(M)',              -- ALLOC(M) : Amount of memory used by the tablespace
       (SELECT TO_CHAR(SUM((FIXED_USED_MEM + VAR_USED_MEM))/1024/1024, '999,999,999')
          FROM V$MEMTBL_INFO) '      USED(M)',                                                                  -- USED(M)  : Memory size in which data is stored among ALLOCs
       TO_CHAR((((MEM_ALLOC_PAGE_COUNT-MEM_FREE_PAGE_COUNT)*32*1024)/MEM_MAX_DB_SIZE)*100, '99.99') 'USAGE(%)'  -- USAGE(%) : ALLOC utilization rate compared to MAX
  FROM V$DATABASE ;
       MAX(M)         TOTAL(M)         ALLOC(M)         USED(M)     USAGE(%)
-------------------------------------------------------------------------------------------
       5,120            2,920              621              142      12.13
1 row selected.
```

![grey_arrow_down.png](https://docs.altibase.com/images/icons/grey_arrow_down.png)TOTAL is...

TOTAL(M) means the total page size allocated to the memory tablespace.

This value also includes free pages in the memory tablespace. Free pages may not be loaded into physical memory. So this value cannot be viewed as the physical memory usage of the memory tablespace.

```
This value also refers to the size of the checkpoint image file.
```

```
TOTAL does not decrease except in the case of DROP TABESPACE. Restarting the Altibase server does not decrease the value.
```

**Comparing to checkpoint image file**

```
iSQL> /
      MAX(M)         TOTAL(M)         ALLOC(M)          USED(M)    USAGE(%)
-------------------------------------------------------------------------------------------
       5,120            4,108              158              123       3.10
1 row selected.

iSQL> ! ls -l $ALTIBASE_HOME/dbs/*MEM* | sort -n | awk '{sum += $5} END{print (sum/1024/1024)/2" MB"}'        -- It may look different depending on when the checkpoint is performed.
4108.17 MB                                                                                                    -- When a checkpoint is performed, it becomes equal to TOTAL.
```

## DB restart

---

- The Altibase server must be restarted to change the `MEM_MAX_DB_SIZE` value.
- This property cannot be changed dynamically while the server is running, so service downtime is required.

## How to change

1. **Stop the Altibase Server**

```
$ server stop
```

2. **Change the altibase.properties file**

Save after changing MEM_MAX_DB_SIZE in the Altibase server properties file ($ALTIBASE_HOME/conf/altibase.properties).

```
$ vi $ALTIBASE_HOME/conf/altibase.properties
MEM_MAX_DB_SIZE        = 2G # MEM_MAX_DB_SIZE
```

3. **Start the Altibase Server**

```
$ server start
```

## Possible error messages

---

#### [FAILURE] The size of the DB file(SYS_TBS_MEM_DATA-number-number) exceeds the size specified in the MEM_MAX_DB_SIZE property.

- Cause

  This startup error can occur if `MEM_MAX_DB_SIZE` is set smaller than the increased checkpoint image file size.

- Resolution

  Set `MEM_MAX_DB_SIZE` larger than the increased checkpoint image file size.

  Full error example:

  ```
  $ server start
  -----------------------------------------------------------------
       Altibase Client Query utility.
       Release Version 7.1.0.5.9
       Copyright 2000, ALTIBASE Corporation or its subsidiaries.
       All Rights Reserved.
  -----------------------------------------------------------------
  ISQL_CONNECTION = UNIX, SERVER = localhost
  [ERR-910FB : Connected to idle instance]
  Connecting to the DB server.... Connected.

  TRANSITION TO PHASE : PROCESS

  TRANSITION TO PHASE : CONTROL
  [FAILURE] The size of the DB file(SYS_TBS_MEM_DATA-0-2) exceeds the size specified in the MEM_MAX_DB_SIZE property.
  Startup Failed....
  [ERR-91015 : Communication failure.]
  ```

## Check the setting value

---

The setting value can be checked in two methods as below.

```
iSQL> set linesize 1024
iSQL> set colsize 20
iSQL> SELECT NAME, TO_CHAR(VALUE1/1024/1024, '999,999') AS 'VALUE(MB)' FROM V$PROPERTY WHERE NAME = 'MEM_MAX_DB_SIZE';
```

Or,

```
SELECT TO_CHAR(MEM_MAX_DB_SIZE/1024/1024, '999,999') AS 'MEM_MAX_DB_SIZE(MB)' FROM V$DATABASE;
```

# Reference

---

- Related error: [ERR-11049 ( 69705) Too many pages are allocated ( Maximum Number of Pages= number).](https://aid.altibase.com/pages/viewpage.action?pageId=9110685)
- Video: [http://youtube.com/watch?v=tWAC4ghMO3c](https://youtu.be/tWAC4ghMO3c)
