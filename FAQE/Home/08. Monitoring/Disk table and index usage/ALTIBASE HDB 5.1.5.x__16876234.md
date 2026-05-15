---
title: "ALTIBASE HDB 5.1.5.x"
page_id: "16876234"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ALTIBASE+HDB+5.1.5.x"
updated_at: "2021-04-05T10:21:25.000+0900"
version: 3
ancestors: ["Home", "08. Monitoring", "Disk table and index usage"]
labels: []
---

# ALTIBASE HDB 5.1.5.x
Source: https://docs.altibase.com/display/FAQE/ALTIBASE+HDB+5.1.5.x
Updated: 2021-04-05T10:21:25.000+0900

- [Overview](#ALTIBASEHDB5.1.5.x-Overview) - [Disk table](#ALTIBASEHDB5.1.5.x-Disktable) - [Disk Index](#ALTIBASEHDB5.1.5.x-DiskIndex) - [Reference - How to check the number of disk tables and indexes](#ALTIBASEHDB5.1.5.x-Reference-Howtocheckthenumberofdisktablesandindexes)

# Overview

---

- This is a disk table and index usage query for ALTIBASE HDB version 5.1.5.
- In ALTIBASE HDB 5, due to a change in the structure of the disk table, only the size allocated to the table can be known and the actual usage cannot be checked.
- This means that data cannot be calculated except for the free space that occurred after DELETE.
- From ALTIBASE HDB 5.3.3.33, 5.3.5.15, 5.5.1.0.3, it has been improved so that the usage can be checked.

# Disk table

---

**ALTIBASE HDB 5.1.5 Disk Table Usage Query**

```
set linesize 1024
set colsize 30
SELECT U.USER_NAME USER_NAME                                                                                                    -- Database user
     , DECODE(TBL.IS_PARTITIONED, 'T', 'PARTITIONED', 'F', 'NON-PARTITIONED') PARTITIONED                                       -- If a partitioned table, PARTITIONED a non-partitioned, then NON-PARTITIONED
     , TBL.TABLE_NAME TABLE_NAME                                                                                                -- Table name
     , DECODE(TBL.IS_PARTITIONED, 'T', TBL.PARTITION_NAME, 'F', '-') PARTITIONED_TABLE                                          -- Partitioned table name
     , TBS.NAME TABLESPACE_NAME                                                                                                 -- Tablesapce
     , TO_CHAR((D.MAX * TBS.PAGE_SIZE)/1024, '999,999,999') 'MAX(KB)'                                                           -- Maximum size of the tablespace to which the table belongs
     , TO_CHAR((TBS.EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_TOTAL_COUNT)/1024, '999,999,999') 'ALLOC(KB)'                -- Total size allocated to date
     , TO_CHAR((((TBS.EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_TOTAL_COUNT)/(D.MAX*TBS.PAGE_SIZE))*100), '99.99') 'USAGE(%)' -- Percentage of utilization compared to the maximum size of the tablespace
  FROM (SELECT TBL.USER_ID
             , DECODE(TBL.IS_PARTITIONED, 'F', TBL.TABLE_OID, 'T', PT.PARTITION_OID) TABLE_OID
             , TBL.TABLE_NAME
             , PT.PARTITION_NAME
             , DECODE(TBL.IS_PARTITIONED, 'F', TBL.TBS_ID, 'T', PT.TBS_ID) TBS_ID
             , TBL.IS_PARTITIONED
          FROM SYSTEM_.SYS_TABLES_ TBL LEFT OUTER JOIN SYSTEM_.SYS_TABLE_PARTITIONS_ PT ON TBL.TABLE_ID = PT.TABLE_ID
       ) TBL
     , V$SEGMENT SEG
     , SYSTEM_.SYS_USERS_ U
     , V$TABLESPACES TBS
     , (SELECT SPACEID
             , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
             , DECODE(MAX(AUTOEXTEND),1,'ON','OFF') 'AUTOEXTEND'
          FROM V$DATAFILES
         GROUP BY SPACEID) D
 WHERE 1=1
   AND SEG.SEGMENT_TYPE = 'TABLE'  /* 'TABLE' :, 'INDEX' : */
   AND SEG.TABLE_OID = TBL.TABLE_OID
   AND U.USER_ID = TBL.USER_ID
   AND D.SPACEID = TBL.TBS_ID
   AND TBS.ID = TBL.TBS_ID
 ORDER BY USER_NAME, PARTITIONED, TABLE_NAME, PARTITIONED_TABLE
;
```

**Example of output**

```
USER_NAME             PARTITIONED      TABLESPACE_NAME       TABLE_NAME            PARTITIONED_TABLE     MAX(KB)          ALLOC(KB)        USAGE(%)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
SYS                   NON-PARTITIONED  SYS_TBS_DISK_DATA     CUSTOMER              -                        2,097,152              256        .01
SYS                   NON-PARTITIONED  SYS_TBS_DISK_DATA     DEPARTMENT            -                        2,097,152              256        .01
SYS                   NON-PARTITIONED  SYS_TBS_DISK_DATA     EMPLOYEE              -                        2,097,152              256        .01
SYS                   NON-PARTITIONED  SYS_TBS_DISK_DATA     GOODS                 -                        2,097,152              256        .01
SYS                   NON-PARTITIONED  USER_DATA             ORDERS                -                        2,097,152              256        .01
SYS                   PARTITIONED      PART_DATA             PART_T1               P1                         262,144              512        .20
SYS                   PARTITIONED      PART_DATA             PART_T1               P2                         262,144              512        .20
SYS                   PARTITIONED      PART_DATA             PART_T1               P3                         262,144           18,176       6.93
SYS                   PARTITIONED      PART_DATA             PART_T2               P201406                    262,144            9,472       3.61
SYS                   PARTITIONED      PART_DATA             PART_T2               P201407                    262,144           18,944       7.23
SYS                   PARTITIONED      PART_DATA             PART_T2               P201408                    262,144            4,864       1.86
SYS                   PARTITIONED      PART_DATA             PART_T2               P201512                    262,144            7,168       2.73
SYS                   PARTITIONED      PART_DATA_DEF         PART_T2               PMAX                       262,144            8,192       3.13
SYS                   PARTITIONED      SYS_TBS_DISK_DATA     RANGE2                DEF                      2,097,152              256        .01
SYS                   PARTITIONED      SYS_TBS_DISK_DATA     RANGE2                Q1_2014                  2,097,152            1,536        .07
SYS                   PARTITIONED      SYS_TBS_DISK_DATA     RANGE2                Q2_2014                  2,097,152              768        .04
SYS                   PARTITIONED      SYS_TBS_DISK_DATA     RANGE2                Q3_2014                  2,097,152            2,304        .11
SYS                   PARTITIONED      SYS_TBS_DISK_DATA     RANGE2                Q4_2014                  2,097,152              256        .01
SYS                   PARTITIONED      SYS_TBS_DISK_DATA     RANGE_SALES           DEF                      2,097,152              256        .01
SYS                   PARTITIONED      SYS_TBS_DISK_DATA     RANGE_SALES           Q1_2014                  2,097,152              768        .04
SYS                   PARTITIONED      SYS_TBS_DISK_DATA     RANGE_SALES           Q2_2014                  2,097,152            1,536        .07
SYS                   PARTITIONED      SYS_TBS_DISK_DATA     RANGE_SALES           Q3_2014                  2,097,152            1,280        .06
SYS                   PARTITIONED      SYS_TBS_DISK_DATA     RANGE_SALES           Q4_2014                  2,097,152              768        .04
23 rows selected.
```

# Disk Index

---

```
set linesize 1024
set colsize 20
SELECT U.USER_NAME USER_NAME                                                                                                   -- Database user
     , I_LIST.TABLE_NAME                                                                                                       -- Table name
     , DECODE(I_LIST.PARTITION_NAME, NULL, 'NON-PARTITIONED', I_LIST.PARTITION_NAME) PARTITIONED_NAME                          -- Partitioned table name. If a non-partitioned, then NON-PARTITIONED
     , I_LIST.INDEX_NAME INDEX_NAME                                                                                            -- Index name
     , DECODE(I_LIST.INDEX_PARTITION_NAME, NULL, 'NON-PARTITIONED', I_LIST.INDEX_PARTITION_NAME) PARTITIONED_INDEX             -- Partitioned index name
     , TBS.NAME TBS_NAME                                                                                                       -- Tablespace to which the index belongs
     , TO_CHAR((D.MAX * TBS.PAGE_SIZE)/1024, '999,999,999') 'MAX(KB)'                                                          -- Maximum size of table space
     , TO_CHAR((TBS.EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_TOTAL_COUNT)/1024, '999,999,999') 'ALLOC(KB)'               -- Total size allocated from the index
     , TO_CHAR((((TBS.EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.EXTENT_TOTAL_COUNT)/(D.MAX*TBS.PAGE_SIZE))*100), '99.99') 'USAGE(%)'   -- Percentage of utilization compared to the maximum size of the tablespace
  FROM (SELECT T.TABLE_NAME
             , PT.PARTITION_NAME
             , I.INDEX_NAME
             , PI.INDEX_PARTITION_NAME
             , DECODE(T.IS_PARTITIONED, 'F', I.TABLE_ID, 'T', PT.TABLE_ID) TABLE_ID
             , DECODE(T.IS_PARTITIONED, 'F', T.TABLE_OID, 'T', PT.PARTITION_OID) TABLE_OID
             , DECODE(I.IS_PARTITIONED, 'F', I.TBS_ID, 'T', PI.TBS_ID) TBS_ID
             , I.INDEX_ID
             , T.USER_ID
          FROM SYSTEM_.SYS_INDICES_ I LEFT OUTER JOIN SYSTEM_.SYS_INDEX_PARTITIONS_ PI ON PI.INDEX_ID = I.INDEX_ID LEFT OUTER JOIN SYSTEM_.SYS_TABLE_PARTITIONS_ PT ON PT.PARTITION_ID = PI.TABLE_PARTITION_ID LEFT OUTER JOIN SYSTEM_.SYS_TABLES_ T ON T.TABLE_ID = I.TABLE_ID ) I_LIST
     , V$SEGMENT SEG
     , V$INDEX I
     , V$TABLESPACES TBS
     , SYSTEM_.SYS_USERS_ U
     , (SELECT SPACEID
             , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
             , DECODE(MAX(AUTOEXTEND),1,'ON','OFF') 'AUTOEXTEND'
          FROM V$DATAFILES
         GROUP BY SPACEID) D
 WHERE 1=1
   AND SEG.TABLE_OID = I.TABLE_OID
   AND SEG.SEGMENT_PID = I.INDEX_SEG_PID
   AND SEG.SPACE_ID = I_LIST.TBS_ID
   AND I_LIST.INDEX_ID = I.INDEX_ID
   AND I_LIST.TABLE_OID = I.TABLE_OID
   AND I_LIST.TBS_ID = TBS.ID
   AND D.SPACEID = I_LIST.TBS_ID
   AND U.USER_ID = I_LIST.USER_ID
 ORDER BY I_LIST.TABLE_NAME, I_LIST.INDEX_NAME, I_LIST.PARTITION_NAME, I_LIST.INDEX_PARTITION_NAME
;
```

**Example of output**

```
 USER_NAME             TABLE_NAME            PARTITIONED_NAME      INDEX_NAME            PARTITIONED_INDEX     TBS_NAME              MAX(KB)          ALLOC(KB)        USAGE(%)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
SYS                   CUSTOMER              NON-PARTITIONED       __SYS_IDX_ID_113      NON-PARTITIONED       SYS_TBS_DISK_DATA        2,097,152              256        .01
SYS                   DEPARTMENT            NON-PARTITIONED       DEP_IDX1              NON-PARTITIONED       SYS_TBS_DISK_DATA        2,097,152              256        .01
SYS                   DEPARTMENT            NON-PARTITIONED       __SYS_IDX_ID_111      NON-PARTITIONED       SYS_TBS_DISK_DATA        2,097,152              256        .01
SYS                   EMPLOYEE              NON-PARTITIONED       EMP_IDX1              NON-PARTITIONED       SYS_TBS_DISK_DATA        2,097,152              256        .01
SYS                   EMPLOYEE              NON-PARTITIONED       __SYS_IDX_ID_112      NON-PARTITIONED       SYS_TBS_DISK_DATA        2,097,152              256        .01
SYS                   GOODS                 NON-PARTITIONED       __SYS_IDX_ID_114      NON-PARTITIONED       SYS_TBS_DISK_DATA        2,097,152              256        .01
SYS                   GOODS                 NON-PARTITIONED       __SYS_IDX_ID_115      NON-PARTITIONED       SYS_TBS_DISK_DATA        2,097,152              256        .01
SYS                   ORDERS                NON-PARTITIONED       ODR_IDX1              NON-PARTITIONED       USER_IDX                 2,097,152              256        .01
SYS                   ORDERS                NON-PARTITIONED       ODR_IDX2              NON-PARTITIONED       USER_IDX                 2,097,152              256        .01
SYS                   ORDERS                NON-PARTITIONED       ODR_IDX3              NON-PARTITIONED       USER_IDX                 2,097,152              256        .01
SYS                   ORDERS                NON-PARTITIONED       __SYS_IDX_ID_116      NON-PARTITIONED       USER_DATA                2,097,152              256        .01
SYS                   PART_T1               P1                    PART_T1_IDX           P_IDX1                PART_IDX                   786,432              256        .03
SYS                   PART_T1               P2                    PART_T1_IDX           P_IDX2                PART_IDX                   786,432              256        .03
SYS                   PART_T1               P3                    PART_T1_IDX           P_IDX3                PART_IDX                   786,432            7,424        .94
14 rows selected.
```

# Reference - How to check the number of disk tables and indexes

---

**Disk table count query**

```
set linesize 1024;
set colsize 50;
SELECT DECODE(T.IS_PARTITIONED, 'T', 'PARTITIONED     TABLE CNT : '||PART_T.CNT, 'F', 'NON-PARTITIONED TABLE CNT : '||T.CNT) TABLE_COUNT
  FROM (SELECT IS_PARTITIONED
             , COUNT(*) CNT
          FROM V$DISKTBL_INFO D
             , SYSTEM_.SYS_TABLES_ T
         WHERE D.TABLE_OID = T.TABLE_OID
         GROUP BY IS_PARTITIONED) T
     , (SELECT COUNT(*) CNT FROM SYSTEM_.SYS_TABLE_PARTITIONS_ ) PART_T ;
```

**Disk index count query**

```
set linesize 1024;
set colsize 50;
SELECT DECODE(T.IS_PARTITIONED, 'T', 'PARTITIONED     TABLE CNT : '||PART_T.CNT, 'F', 'NON-PARTITIONED TABLE CNT : '||T.CNT) TABLE_COUNT
  FROM (SELECT IS_PARTITIONED
             , COUNT(*) CNT
          FROM V$DISKTBL_INFO D
             , SYSTEM_.SYS_TABLES_ T
         WHERE D.TABLE_OID = T.TABLE_OID
         GROUP BY IS_PARTITIONED) T
     , (SELECT COUNT(*) CNT FROM SYSTEM_.SYS_TABLE_PARTITIONS_ ) PART_T ;
```
