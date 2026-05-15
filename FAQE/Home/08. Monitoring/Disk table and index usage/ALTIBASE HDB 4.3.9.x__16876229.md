---
title: "ALTIBASE HDB 4.3.9.x"
page_id: "16876229"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ALTIBASE+HDB+4.3.9.x"
updated_at: "2021-03-23T16:05:48.000+0900"
version: 3
ancestors: ["Home", "08. Monitoring", "Disk table and index usage"]
labels: []
---

# ALTIBASE HDB 4.3.9.x
Source: https://docs.altibase.com/display/FAQE/ALTIBASE+HDB+4.3.9.x
Updated: 2021-03-23T16:05:48.000+0900

- [Overview](#ALTIBASEHDB4.3.9.x-Overview) - [Disk table usage query](#ALTIBASEHDB4.3.9.x-Disktableusagequery) - [Disk index usage query](#ALTIBASEHDB4.3.9.x-Diskindexusagequery) - [Reference - How to check the number of disk tables and indexes](#ALTIBASEHDB4.3.9.x-Reference-Howtocheckthenumberofdisktablesandindexes)

# Overview

---

This is an ALTIBASE HDB version 4.3.9 of the disk table and index usage query.

This query can also be used in ALTIBASE HDB version 5.1.1.

# Disk table usage query

---

**ALTIBASE HDB 4.3.9 Disk Table Usage Query**

```
set linesize 1024;
set colsize 20;
SELECT U.USER_NAME 'USER_NAME'                                                                                      -- Database user
     , TBL.TABLE_NAME 'TABLE_NAME'                                                                                  -- Table name
     , TBS.NAME 'TBS_NAME'                                                                                          -- Name of the tablespace to which the table belongs
     , TO_CHAR((TBS.TOTAL_PAGE_COUNT * TBS.PAGE_SIZE)/1024 , '999,999,999') 'TBS_MAX(KB)'                           -- Maximum size of tablespace
     , TO_CHAR((TBS.A_EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_TOTAL_COUNT)/1024, '999,999,999') 'ALLOC(KB)'  -- The total size allocated from the table
     , TO_CHAR((TBS.A_EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_FULL_COUNT)/1024, '999,999,999') 'USED(KB)'    -- Actual usage of the table (data usage)
     , TO_CHAR((((TBS.A_EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_TOTAL_COUNT)/(TBS.TOTAL_PAGE_COUNT * TBS.PAGE_SIZE))*100), '99.9') 'USAGE(%)' -- Utilization based on the maximum size of the tablespace
  FROM X$SEGMENT SEG
     , SYSTEM_.SYS_TABLES_ TBL
     , V$TABLESPACES TBS
     , SYSTEM_.SYS_USERS_ U
 WHERE SEG.TABLE_OID = TBL.TABLE_OID
   AND SEG.SPACE_ID = TBL.TBS_ID
   AND SEG.SPACE_ID = TBS.ID
   AND TBL.USER_ID = U.USER_ID
   AND TBL.TABLE_TYPE = 'T'
   AND SEG.SEGMENT_TYPE = 6
 ORDER BY USER_NAME, TABLE_NAME
 ;
```

**Example of output**

```
USER_NAME             TABLE_NAME            TBS_NAME              TBS_MAX(KB)      ALLOC(KB)        USED(KB)         USAGE(%)
----------------------------------------------------------------------------------------------------------------------------------------------
SYS                   CUSTOMER              USER_DATA                2,097,152              256                0       0.0
SYS                   DEPARTMENT            SYS_TBS_DATA               254,976              256                0        .1
SYS                   DISK_T                USER_DATA                2,097,152          851,200          850,944      40.6
SYS                   EMPLOYEE              SYS_TBS_DATA               254,976              256                0        .1
SYS                   ORDERS                USER_DATA                2,097,152              256                0       0.0
5 rows selected.
```

# Disk index usage query

---

**ALTIBASE HDB 4.3.9 Disk Index Usage Query**

```
set linesize 1024
set colsize 20
SELECT U.USER_NAME AS 'USER_NAME'           -- Database user
     , TBL.TABLE_NAME AS 'TABLE_NAME'       -- Table name
     , IDX.INDEX_NAME AS 'INDEX_NAME'       -- Index name
     , TBS.NAME AS 'TBS_NAME'               -- Tablespace name to which the index belongs
     , TO_CHAR((TBS.TOTAL_PAGE_COUNT * TBS.PAGE_SIZE)/1024 , '999,999,999') AS 'TBS_MAX(KB)'                            -- Maximum size of table space
     , TO_CHAR((TBS.A_EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_TOTAL_COUNT)/1024, '999,999,999') AS 'ALLOC(KB)'   -- Total size allocated from the index
     , TO_CHAR((TBS.A_EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_FULL_COUNT )/1024, '999,999,999') AS 'USED(KB)'    -- Actual usage of the index (data usage)
    , TO_CHAR((((TBS.A_EXTENT_PAGE_COUNT * SEG.EXTENT_TOTAL_COUNT)/TBS.TOTAL_PAGE_COUNT)*100), '99.9') AS 'USAGE(%)'    -- Utilization based on the maximum size of the tablespace
 FROM  X$SEGMENT SEG
     , V$INDEX I
     , SYSTEM_.SYS_INDICES_ IDX
     , SYSTEM_.SYS_TABLES_ TBL
     , V$TABLESPACES TBS
     , SYSTEM_.SYS_USERS_ U
 WHERE SEG.TABLE_OID = I.TABLE_OID
   AND SEG.SEGMENT_DESC = I.INDEX_SEG_DESC
   AND I.INDEX_ID = IDX.INDEX_ID
   AND IDX.TABLE_ID = TBL.TABLE_ID
   AND SEG.SPACE_ID = IDX.TBS_ID
   AND SEG.SPACE_ID = TBS.ID
   AND IDX.USER_ID = U.USER_ID
   AND TBL.TABLE_TYPE = 'T'
   AND SEG.SEGMENT_TYPE = 5
 ORDER BY U.USER_NAME, TBL.TABLE_NAME, IDX.INDEX_NAME
   ;
```

**Example of output**

```
USER_NAME             TABLE_NAME            INDEX_NAME            TBS_NAME              TBS_MAX(KB)      ALLOC(KB)        USED(KB)         USAGE(%)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
SYS                   CUSTOMER              __SYS_IDX_ID_136      USER_DATA                2,097,152              256                0       0.0
SYS                   DEPARTMENT            DEP_IDX1              USER_IDX                 2,097,152              256                0       0.0
SYS                   DEPARTMENT            __SYS_IDX_ID_134      SYS_TBS_DATA               254,976              256                0        .1
SYS                   DISK_T                DISK_T_IDX_01         USER_IDX                 2,097,152          159,744          159,488       7.6
SYS                   EMPLOYEE              EMP_IDX1              USER_IDX                 2,097,152              256                0       0.0
SYS                   EMPLOYEE              __SYS_IDX_ID_135      SYS_TBS_DATA               254,976              256                0        .1
SYS                   ORDERS                ODR_IDX1              USER_IDX                 2,097,152              256                0       0.0
SYS                   ORDERS                __SYS_IDX_ID_137      USER_DATA                2,097,152              256                0       0.0
8 rows selected.
```

# Reference - How to check the number of disk tables and indexes

---

**Disk Table count query**

```
set linesize 1024
set colsize 30
SELECT 'TABLE CNT : '||COUNT(*) TABLE_COUNT
  FROM V$DISKTBL_INFO D
     , SYSTEM_.SYS_TABLES_ T
 WHERE D.TABLE_OID = T.TABLE_OID ;
```

**Disk Index count query**

```
set linesize 1024;
set colsize 30;
SELECT 'INDEX CNT : '||COUNT(*) INDEX_COUNT
  FROM SYSTEM_.SYS_INDICES_
 WHERE TABLE_ID IN (SELECT TABLE_ID
                      FROM SYSTEM_.SYS_TABLES_ T
                         , V$DISKTBL_INFO D
                     WHERE T.TABLE_OID = D.TABLE_OID);
```
