---
title: "ALTIBASE HDB  5.5.1,  6.1.1, 6.3.1"
page_id: "16876263"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ALTIBASE+HDB++5.5.1%2C++6.1.1%2C+6.3.1"
updated_at: "2021-03-24T09:48:18.000+0900"
version: 1
ancestors: ["Home", "08. Monitoring", "Memory tablespace usage"]
labels: []
---

# ALTIBASE HDB  5.5.1,  6.1.1, 6.3.1
Source: https://docs.altibase.com/display/FAQE/ALTIBASE+HDB++5.5.1%2C++6.1.1%2C+6.3.1
Updated: 2021-03-24T09:48:18.000+0900

- [Overview](#ALTIBASEHDB5.5.1,6.1.1,6.3.1-Overview) - [Reference - About Memory Tablespace Attributes](#ALTIBASEHDB5.5.1,6.1.1,6.3.1-Reference-AboutMemoryTablespaceAttributes)

# Overview

---

- Starting from ALTIBASE HDB version 5.5.1, V$VOL_TABLESPACES, which stores information on volatile memory tablespaces, has been added.
- Using this Performance View, all memory tablespace usage including volatile memory tablespace usage can be inquired with the following query.

**ALTIBASE HDB 5.5.1, 6.1.1, 6.3.1 memory tablespace usage query**

```
--
--TBS_ID   : Tablespace ID
--TBS_TYPE : Memory tablespace type
--           0 - System memory tablespace. A tablespace for storing metadata necessary for the operation of the database system
--           1 - System memory tablespace. A tablespace that can store data created by default when creating a database
--           2 - User memory tablespace. User-created memory tablespace
--           8 - Volatile tablespaces created by users
--TBS_NAME : Memory tablespace name
--MAX(M)   : Max amount of memory that can be used by memory tablespace
--           If MAXSIZE is not specified when creating a tablespace, MEM_MAX_DB_SIZE is displayed.
--           If the tablespace attribute is AUTOEXTEND OFF, TOTAL is output.
--TOTAL(M) : Total number of pages allocated from the memory tablespace. It is the same as the size of the checkpoint image file creation.
--           It also includes a free page. Free pages are not loaded into memory when the Altibase server is started. So, it is difficult to use and judge physical memory as much as this value.
--           This value is decreased only by executing DROP TABLESPACE.
--ALLOC(M) : Amount of memory being used by the memory tablespace
--USED(M)  : The size of the memory storing data among ALLOCs
--USAGE(%) : ALLOC utilization rate compared to MAX
--STATE    : State of the tablespace
--           1 - Offline, 2 - Online, 3 - Offline tablespace being backed up, 4 - Online tablespace being backed up,
--           128 - Dropped tablespace, 1024-discarded tablespace, 1028-discarded tablespace being backed up
set linesize 1024
set colsize 20
SELECT ID TBS_ID
     , DECODE(TYPE, 0, 'MEMORY_DICTIONARY', 1, 'MEMORY_SYS_DATA', 2, 'MEMORY_USER_DATA', 8, 'VOLATILE_USER_DATA') TBS_TYPE
     , NAME TBS_NAME
     , ROUND( DECODE(M.MAXSIZE, 140737488322560, D.MEM_MAX_DB_SIZE , 0 , T.TOTAL_PAGE_COUNT * T.PAGE_SIZE, M.MAXSIZE) /1024/1024, 2 ) 'MAX(M)'
     , ROUND( M.ALLOC_PAGE_COUNT * T.PAGE_SIZE / 1024 / 1024, 2) 'TOTAL(M)'
     , ROUND(NVL(M.ALLOC_PAGE_COUNT-M.FREE_PAGE_COUNT,T.TOTAL_PAGE_COUNT)*PAGE_SIZE/1024/1024, 2) 'ALLOC(M)'
     , NVL(MT.USED, 0) 'USED(M)'
     , ROUND(DECODE(MAXSIZE, 140737488322560, (M.ALLOC_PAGE_COUNT-M.FREE_PAGE_COUNT)*T.PAGE_SIZE/ D.MEM_MAX_DB_SIZE ,0, (M.ALLOC_PAGE_COUNT-M.FREE_PAGE_COUNT) / T.TOTAL_PAGE_COUNT , (M.ALLOC_PAGE_COUNT-M.FREE_PAGE_COUNT) * T.PAGE_SIZE/ M.MAXSIZE) * 100 , 2) 'USAGE(%)'
     , DECODE(T.STATE,1,'OFFLINE',2,'ONLINE',5,'OFFLINE BACKUP',6,'ONLINE BACKUP',128,'DROPPED', 'DISCARDED') STATE
     , DECODE(M.AUTOEXTEND_MODE,1,'ON','OFF') 'AUTOEXTEND'
  FROM V$DATABASE D
     , V$TABLESPACES T
     , (SELECT SPACE_ID
             , SPACE_NAME
             , ALLOC_PAGE_COUNT
             , FREE_PAGE_COUNT
             , DECODE(MAX_SIZE, 0, (SELECT VALUE1 FROM V$PROPERTY WHERE NAME = 'VOLATILE_MAX_DB_SIZE'), MAX_SIZE) AS MAXSIZE
             , AUTOEXTEND_MODE
          FROM V$VOL_TABLESPACES
         UNION ALL
        SELECT SPACE_ID
             , SPACE_NAME
             , ALLOC_PAGE_COUNT
             , FREE_PAGE_COUNT
             , MAXSIZE
             , AUTOEXTEND_MODE
          FROM V$MEM_TABLESPACES ) M LEFT OUTER JOIN(SELECT TABLESPACE_ID, ROUND(SUM((FIXED_USED_MEM + VAR_USED_MEM))/(1024*1024),3) USED
          FROM V$MEMTBL_INFO
         GROUP BY TABLESPACE_ID ) MT ON M.SPACE_ID = MT.TABLESPACE_ID
 WHERE T.ID = M.SPACE_ID;
```

**Example of output**

```
TBS_ID      TBS_TYPE            TBS_NAME              MAX(M)      TOTAL(M)    ALLOC(M)    USED(M)     USAGE(%)    STATE           AUTOEXTEND
---------------------------------------------------------------------------------------------------------------------------------------------------------
0           MEMORY_DICTIONARY   SYS_TBS_MEM_DIC       10240       4.03        4           1.007       0.04        ONLINE          ON
1           MEMORY_SYS_DATA     SYS_TBS_MEM_DATA      10240       8.03        0.09        0           0           ONLINE          ON
5           MEMORY_USER_DATA    USER_MEM_TBS          3072.03     3072.03     712.38      686.646     23.19       ONLINE          OFF
6           MEMORY_USER_DATA    USER_MEM_TBS_2        10240       768.03      694.38      686.646     6.78        ONLINE          ON
8           MEMORY_USER_DATA    USER_MEM_TBS_3        1024        512.03      4.03        0           0.39        ONLINE          ON
```

# Reference - About Memory Tablespace Attributes

```
SELECT SPACE_NAME
     , TO_CHAR(CURRENT_SIZE/1024/1024, '999,999,999') 'CURR_SIZE(MB)'
     , TO_CHAR(AUTOEXTEND_NEXTSIZE/1024/1024, '999,999,999') 'NEXT_SIZE(MB)'
     , TO_CHAR(DECODE(MAXSIZE, 0, CURRENT_SIZE, 140737488322560, D.MEM_MAX_DB_SIZE, MAXSIZE)/1024/1024, '999,999,999') ' MAXSIZE(MB)'
     , DECODE(AUTOEXTEND_MODE, 1, 'ON', 0, 'OFF') 'AUTOEXTEND'
  FROM V$MEM_TABLESPACES, V$DATABASE D
UNION ALL
SELECT SPACE_NAME
     , TO_CHAR(CURRENT_SIZE/1024/1024, '999,999,999') 'CURR_SIZE(MB)'
     , TO_CHAR(NEXT_SIZE/1024/1024, '999,999,999') 'NEXT_SIZE(MB)'
     , TO_CHAR(DECODE(MAX_SIZE, 0, CURRENT_SIZE, 140737488322560, D.MEM_MAX_DB_SIZE, MAX_SIZE)/1024/1024, '999,999,999') ' MAXSIZE(MB)'
     , DECODE(AUTOEXTEND_MODE, 1, 'ON', 0, 'OFF') 'AUTOEXTEND'
  FROM V$VOL_TABLESPACES, V$DATABASE D ;
```
