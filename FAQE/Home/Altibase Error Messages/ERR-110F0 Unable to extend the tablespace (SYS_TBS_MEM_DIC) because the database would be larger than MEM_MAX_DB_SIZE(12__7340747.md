---
title: "ERR-110F0 Unable to extend the tablespace (SYS_TBS_MEM_DIC) because the database would be larger than MEM_MAX_DB_SIZE(12582912K)"
page_id: "7340747"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=7340747"
updated_at: "2014-11-27T17:51:57.000+0900"
version: 11
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-110F0 Unable to extend the tablespace (SYS_TBS_MEM_DIC) because the database would be larger than MEM_MAX_DB_SIZE(12582912K)
Source: https://docs.altibase.com/pages/viewpage.action?pageId=7340747
Updated: 2014-11-27T17:51:57.000+0900

- [Version](#ERR-110F0Unabletoextendthetablespace(SYS_TBS_MEM_DIC)becausethedatabasewouldbelargerthanMEM_MAX_DB_SIZE(12582912K)-Version)
- [Explanation](#ERR-110F0Unabletoextendthetablespace(SYS_TBS_MEM_DIC)becausethedatabasewouldbelargerthanMEM_MAX_DB_SIZE(12582912K)-Explanation)
- [Cause](#ERR-110F0Unabletoextendthetablespace(SYS_TBS_MEM_DIC)becausethedatabasewouldbelargerthanMEM_MAX_DB_SIZE(12582912K)-Cause)
- [Action](#ERR-110F0Unabletoextendthetablespace(SYS_TBS_MEM_DIC)becausethedatabasewouldbelargerthanMEM_MAX_DB_SIZE(12582912K)-Action)
- [Reference](#ERR-110F0Unabletoextendthetablespace(SYS_TBS_MEM_DIC)becausethedatabasewouldbelargerthanMEM_MAX_DB_SIZE(12582912K)-Reference)

## Version

All versions

## Explanation

INSERT/UPDATE/DELETE statements cannot be executed on memory tablespaces. Only the SELECT statement is executable.

## Cause

This error occurs when the total sum of memory tablespaces (SYS_TBS_MEM_DIC+SYS_TBS_MEM_DATA+USER_MEMORY_TABLESPACE) exceeds MEM_MAX_DB_SIZE.

## Action

MEM_MAX_DB_SIZE is the maximum amount of memory that can be used by memory tablespaces. For further information, refer to the *[Technical Article] ALTIBASE Monitoring Query Guide, [TS01] Memory Table Space Usage (page 29)*.

The tablespace area cannot be returned unless a tablespace is dropped. (The COMPACT command can return the blank page, but the effect is negligible. Thus, it is not recommended.)

Therefore, if MEM_MAX_DB_SIZE is set lower than the actual amount, change the value of MEM_MAX_DB_SIZE from $ALTIBASE_HOME/conf/altibase.proeperties and restart the Altibase server process.

It is recommended to set the maximum value of MEM_MAX_DB_SIZE as the sum of VOLATILE_MAX_DB_SIZE and MEM_MAX_DB_SIZE within 60 to 70 percent of the physical memory.

- Checking MEM_MAX_DB_SIZE

  ```
  iSQL> SELECT value1/32/1024 FROM v$property WHERE name = 'MEM_MAX_DB_SIZE';
  VALUE1/32/1024 : 32768

  1 row selected.
  ```

   The above example shows the maximum number of pages that can be used (It is divided by 32 as the size of one page is 32K).
- Checking Usage

  ```
  iSQL> SELECT space_name, maxsize/32/1024, alloc_page_count FROM v$mem_tablespaces;
  SPACE_NAME       : SYS_TBS_MEM_DIC
  MAXSIZE/32/1024  : 4294967295
  ALLOC_PAGE_COUNT : 129

  SPACE_NAME       : SYS_TBS_MEM_DATA
  MAXSIZE/32/1024  : 4294967295
  ALLOC_PAGE_COUNT : 29313

  SPACE_NAME       : MEM_TBS
  MAXSIZE/32/1024  : 3200
  ALLOC_PAGE_COUNT : 3201

  3 rows selected.
  ```

   1. The above example shows the current usage of the memory tablespace. There are 32,643 pages allocated in total.

2. For SYS_TBS_MEM_DIC and SYS_TBS_MEM_DATA, they have not reached MAXSIZE but the error has occurred because the sum of all the memory tablespaces has almost reached MEM_MAX_DB_SIZE.

The current sum shows the value of 32,643 and the actual MEM_MAX_DB_SIZE is 32,768. Thus, there are still 125 pages that can be allocated. However, as the default value of EXPAND_CHUNK_PAGE_COUNT (the number of pages by which to increase the size of the memory tablespace) is 128, it means that all the pages are currently being used.

(The error occurs when MEM_MAX_DB_SIZE is exceeded because the transaction tried to expand.)

Each memory tablespace has its own MAXSIZE. This error not only occurs when it has reached its MAXSIZE but also when the sum of all the memory tablespaces exceeds MEM_MAX_DB_SIZE.

- Restarting Altibase server after increasing MEM_MAX_DB_SIZE

  ```
  Shell> vi $ALTIBASE_HOME/conf/altibase.properties
  ....
  ....
  UNIXDOMAIN_FILEPATH    =?/trc/cm-unix
  MEM_MAX_DB_SIZE        =  1G             <===== Change this value to the appropriate size (Using GB/MB unit)
  LOG_FILE_SIZE          =  10M
  ....
  ....
  :wq!

  Shell> server restart
  ```

   It needs to restart the server after modification.

- Checkpoint Image File Size

For in-memory databases of ALITBASE HDB, any modified data from in-memory databases is saved on disk when checkpointing is executed. The disk file where memory data is saved is called the Checkpoint Image file. This file cannot be resized, which means that once it is expanded, it cannot be reduced.

In order to reduce the Checkpoint Image file size, REORG has to be executed. This has to be done with the migration of all data, including the disk database.

## Reference

N/A
