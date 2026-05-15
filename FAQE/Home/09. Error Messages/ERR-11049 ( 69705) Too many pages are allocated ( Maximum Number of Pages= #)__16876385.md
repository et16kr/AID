---
title: "ERR-11049 (  69705) Too many pages are allocated ( Maximum Number of Pages= #)."
page_id: "16876385"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876385"
updated_at: "2021-04-05T11:19:45.000+0900"
version: 2
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# ERR-11049 (  69705) Too many pages are allocated ( Maximum Number of Pages= #).
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876385
Updated: 2021-04-05T11:19:45.000+0900

- [Version](#ERR-11049(69705)Toomanypagesareallocated(MaximumNumberofPages=#).-Version) - [Cause](#ERR-11049(69705)Toomanypagesareallocated(MaximumNumberofPages=#).-Cause) - [What is MEM_MAX_DB_SIZE?](#ERR-11049(69705)Toomanypagesareallocated(MaximumNumberofPages=#).-WhatisMEM_MAX_DB_SIZE?) - [How to query memory usage](#ERR-11049(69705)Toomanypagesareallocated(MaximumNumberofPages=#).-Howtoquerymemoryusage) - [Solution](#ERR-11049(69705)Toomanypagesareallocated(MaximumNumberofPages=#).-Solution) - [How to change](#ERR-11049(69705)Toomanypagesareallocated(MaximumNumberofPages=#).-Howtochange) - [Note/Consideration](#ERR-11049(69705)Toomanypagesareallocated(MaximumNumberofPages=#).-Note/Consideration) - [Disk space](#ERR-11049(69705)Toomanypagesareallocated(MaximumNumberofPages=#).-Diskspace) - [User environment setting (Linux/Unix)](#ERR-11049(69705)Toomanypagesareallocated(MaximumNumberofPages=#).-Userenvironmentsetting(Linux/Unix)) - [Reference](#ERR-11049(69705)Toomanypagesareallocated(MaximumNumberofPages=#).-Reference)

# Version

---

All the versions of Altibase

# Cause

---

For ALTIBASE memory tablespaces, the sum of all memory tablespaces cannot exceed MEM_MAX_DB_SIZE in $ALTIBASE_HOME/conf/altibase.properties. This error message occurs because all space is exhausted.

# What is MEM_MAX_DB_SIZE?

---

- This refers to the maximum amount of memory that can be used as a memory tablespace (memory table or memory data) stored in physical memory.
- Constraints on the total usage of all memory tablespaces combined.
- This is not the maximum size that each of the memory tablespaces can use.
- The size of the index created on the memory table is not included.
- It also includes historical data that occurs when performing change transactions.
- When a change transaction is performed, past data is retained until the transaction is terminated (MVCC technique). In the case of a memory table, a replica of the record is created in the memory table.
- If the maximum value is not specified when creating a memory tablespace, it is automatically expanded by the value set for MEM_MAX_DB_SIZE.

# How to query memory usage

---

```
set linesize 1024
set colsize 20
SELECT TO_CHAR(MEM_MAX_DB_SIZE/1024/1024, '999,999,999') '       MAX(M)',                                       -- MAX(M)   : MEM_MAX_DB_SIZE setting value
       TO_CHAR(MEM_ALLOC_PAGE_COUNT*32/1024, '999,999,999') '     TOTAL(M)',                                    -- TOTAL(M) : Total page size allocated to the memory tablespace. Also refers to the size of the checkpoint image file.
       TO_CHAR((MEM_ALLOC_PAGE_COUNT-MEM_FREE_PAGE_COUNT)*32/1024, '999,999,999') '     ALLOC(M)',              -- ALLOC(M) : Amount of memory used by the memory tablespace
       (SELECT TO_CHAR(SUM((FIXED_USED_MEM + VAR_USED_MEM))/1024/1024, '999,999,999')
          FROM V$MEMTBL_INFO) '      USED(M)',                                                                  -- USED(M)  : Memory size in which data is stored among ALLOCs
       TO_CHAR((((MEM_ALLOC_PAGE_COUNT-MEM_FREE_PAGE_COUNT)*32*1024)/MEM_MAX_DB_SIZE)*100, '99.99') 'USAGE(%)'  -- USAGE(%) : ALLOC utilization rate compared to MAX
  FROM V$DATABASE ;
       MAX(M)         TOTAL(M)         ALLOC(M)         USED(M)     USAGE(%)
-------------------------------------------------------------------------------------------
       5,120              920              621              142      12.13
1 row selected.

```

When ALLOC_SIZE reaches MEM_MAX_DB_SIZE as a result of the above query, the `Too many pages are allocated` error occurs.

# Solution

---

To prevent the following error from occurring, the MEM_MAX_DB_SIZE property value must be increased in $ALTIBASE_HOME/conf/altibase.properties.

If this value is increased, Altibase DB Size can be increased up to this size. After modifying the properties, you must restart Altibase to apply it.

After increasing the value, check why memory tablespace usage increased by querying usage for each table and checking whether bulk changes occurred.

# How to change

1. **Stop the Altibase server**

  |  |
  | --- |
  | `$ server stop` |
2. **Change the altibase.properties file**

  Save after changing MEM_MAX_DB_SIZE in the Altibase server properties file ($ALTIBASE_HOME/conf/altibase.properties).

  ```
  $ vi $ALTIBASE_HOME/conf/altibase.properties
  MEM_MAX_DB_SIZE        = 2G # MEM_MAX_DB_SIZE
  ```
3. **Start the Altibase server**

  |  |
  | --- |
  | `$ server start` |

# Note/Consideration

---

### **Disk space**

Memory tablespaces store two sets of 'memory checkpoint image files' on disk for backup purposes. So, **it requires twice as much disk space as the memory data usage.**

If MEM_MAX_DB_SIZE large is set, disk usage will also increase, so make sure to free up disk space before changing MEM_MAX_DB_SIZE.

Ex) If MEM_MAX_DB_SIZE is 60G, 120G of disk space is required.

### User environment setting (Linux/Unix)

ulimit -a must be executed to make sure that the settings below are **set to the maximum values allowed by the OS.**

max memory size virtual memory

**Kernel parameter (AIX, HP-UX)**

For AIX, check if data, rss, fsize, etc. are set to -1 in the /etc/security/limits file. For HP, check that the maxdsiz_64bit value is set large enough via kctune. Even if the maxdsiz_64bit value is less than the MEM_MAX_DB_SIZE value of the ALTIBASE property, a 'Too many pages are allocated' error may occur. Therefore, the root account must be set higher than MEM_MAX_DB_SIZE of the ALTIBASE property. Linux and SunOS are not applicable.

# Reference

---

[What is MEM_MAX_DB_SIZE?](https://docs.altibase.com/pages/viewpage.action?pageId=16875991)
