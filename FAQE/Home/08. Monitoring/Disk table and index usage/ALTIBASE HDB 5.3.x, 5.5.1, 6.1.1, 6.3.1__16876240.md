---
title: "ALTIBASE HDB 5.3.x, 5.5.1, 6.1.1, 6.3.1"
page_id: "16876240"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ALTIBASE+HDB+5.3.x%2C+5.5.1%2C+6.1.1%2C+6.3.1"
updated_at: "2021-04-05T10:23:20.000+0900"
version: 2
ancestors: ["Home", "08. Monitoring", "Disk table and index usage"]
labels: []
---

# ALTIBASE HDB 5.3.x, 5.5.1, 6.1.1, 6.3.1
Source: https://docs.altibase.com/display/FAQE/ALTIBASE+HDB+5.3.x%2C+5.5.1%2C+6.1.1%2C+6.3.1
Updated: 2021-04-05T10:23:20.000+0900

- [Overview](#ALTIBASEHDB5.3.x,5.5.1,6.1.1,6.3.1-Overview) - [Version](#ALTIBASEHDB5.3.x,5.5.1,6.1.1,6.3.1-Version) - [To check the usage of disk tables and indexes](#ALTIBASEHDB5.3.x,5.5.1,6.1.1,6.3.1-Tochecktheusageofdisktablesandindexes) - [Disk table](#ALTIBASEHDB5.3.x,5.5.1,6.1.1,6.3.1-Disktable) - [Disk Index](#ALTIBASEHDB5.3.x,5.5.1,6.1.1,6.3.1-DiskIndex) - [Reference - How to check the count of disk table and index](#ALTIBASEHDB5.3.x,5.5.1,6.1.1,6.3.1-Reference-Howtocheckthecountofdisktableandindex)

# Overview

---

# Version

---

The monitoring query introduced on this page can be used from the version that reflects BUG-31372.

- Altibase HDB version 5.3.3.33
- Altibase HDB version 5.3.5.15
- Altibase HDB version 5.5.1.0.3
- Altibase HDB version 6.1.1
- Altibase HDB version 6.3.1

In [BUG-31372](https://altra.altibase.com/altimis-2.0/app_bug_new/bug_view.jsp?pk=31372), the TOTAL_USED_SIZE column of X$SEGMENT has been added so that the actual usage of the disk table can be queried.

In ALTIBASE HDB version 5.3.3, 5.3.5, 5.5.1 without BUG-31372 being modified, an error may occur when using the following query.

# To check the usage of disk tables and indexes

---

- ALTER TABLE table_name AGING and ALTER INDEX index_name AGING commands must be executed to get the correct usage.
- Unaging space is calculated as used, so if there are frequent deletes on a table, it may be calculated larger than the actual usage if aging is not performed.
- During the execution of the ALTER TABLE table_name AGING, ALTER INDEX index_name AGING command, the table is full-scanned while holding X LOCK on the table, so other operations on the table and indexes are waiting.
- TOTAL_USED_SIZE of v$segment is volatile temporary data. When the Altibase server is restarted, it is initialized to the total allocation size of the table and index, not the actual usage amount.
- v$segment query itself does not affect the database.

# Disk table

---

- Even if the table data is deleted with DELETE and USED, it does not decrease.
- To check the actual USED excluding FREE PAGE after DELETE and table_name AGING; must be executed.
- While executing ALTER TABLE ~ AGINING;, the table is locked, so other requests for the table are put in waiting for state.

  **ALTIBASE HDB 5.3.x, 5.5.1, 6.1.1, 6.3.1 Disk table usage query**

  ```
  SELECT U.USER_NAME USER_NAME                                                                                            -- Database user
       , TBL.TABLE_NAME TABLE_NAME                                                                                        -- Table name
       , DECODE(TBL.IS_PARTITIONED, 'T', TBL.PARTITION_NAME, 'F', '-') PARTITIONED_TABLE                                  -- Partitioned table name
       , TBS.NAME TABLESPACE_NAME                                                                                         -- Tablespace
       , TO_CHAR((D.MAX * TBS.PAGE_SIZE)/1024, '999,999,999,999') 'MAX(KB)'                                               -- Maximum size of the tablespace to which the table belongs
       , TO_CHAR((TBS.EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.TOTAL_EXTENT_COUNT)/1024, '999,999,999,999') 'ALLOC(KB)'    -- Current allocated size
       , TO_CHAR(SEG.TOTAL_USED_SIZE/1024, '999,999,999,999') 'USED(KB)'                                                  -- Size of the allocated space that contains data
    FROM (SELECT TBL.USER_ID
               , DECODE(TBL.IS_PARTITIONED, 'F', TBL.TABLE_OID, 'T', PT.PARTITION_OID) TABLE_OID
               , TBL.TABLE_NAME
               , PT.PARTITION_NAME
               , DECODE(TBL.IS_PARTITIONED, 'F', TBL.TBS_ID, 'T', PT.TBS_ID) TBS_ID
               , TBL.IS_PARTITIONED
            FROM SYSTEM_.SYS_TABLES_ TBL LEFT OUTER JOIN SYSTEM_.SYS_TABLE_PARTITIONS_ PT ON TBL.TABLE_ID = PT.TABLE_ID
           WHERE TBL.TABLE_TYPE = 'T'
         ) TBL
       , (SELECT S.TABLE_OID, SUM(S.TOTAL_EXTENT_COUNT) TOTAL_EXTENT_COUNT, SUM(S.TOTAL_USED_SIZE) TOTAL_USED_SIZE
            FROM X$SEGMENT S
           WHERE S.SEGMENT_TYPE IN (6, 7) /* 6 : Table, 7 : LOB data(6.1.1 or earlier), 5 : Index */
           GROUP BY S.TABLE_OID) SEG
       , SYSTEM_.SYS_USERS_ U
       , V$TABLESPACES TBS
       , (SELECT SPACEID
               , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
               , DECODE(MAX(AUTOEXTEND),1,'ON','OFF') 'AUTOEXTEND'
            FROM V$DATAFILES
           GROUP BY SPACEID) D
   WHERE 1=1
     AND SEG.TABLE_OID = TBL.TABLE_OID
     AND U.USER_ID = TBL.USER_ID
     AND D.SPACEID = TBL.TBS_ID
     AND TBS.ID = TBL.TBS_ID
   ORDER BY USER_NAME, TABLE_NAME, PARTITIONED_TABLE
  ;
  ```

  **Example of output**

  ```
  USER_NAME             TABLE_NAME            PARTITIONED_TABLE     TABLESPACE_NAME       MAX(KB)          ALLOC(KB)        USED(KB)
  -------------------------------------------------------------------------------------------------------------------------------------------------------
  SYS                   DISK_T                -                     USER_DATA                2,097,152          316,160              316,032
  SYS                   DISK_T2               -                     USER_DATA                2,097,152              256                    8
  SYS                   EMP                   -                     SYS_TBS_DISK_DATA        2,097,152              256                   16
  SYS                   PART_T1               P1                    PART_DATA                1,048,576              768                  520
  SYS                   PART_T1               P2                    PART_DATA                1,048,576              768                  520
  SYS                   PART_T1               P3                    PART_DATA                1,048,576          126,464              126,384
  SYS                   PART_T2               P201406               PART_DATA                1,048,576           11,520               11,280
  SYS                   PART_T2               P201407               PART_DATA                1,048,576           22,784               22,544
  SYS                   PART_T2               P201408               PART_DATA                1,048,576            5,888                5,648
  SYS                   PART_T2               P201512               PART_DATA                1,048,576            8,704                8,464
  SYS                   PART_T2               PMAX                  PART_DATA_DEF            1,048,576            9,728                9,592
  SYS                   RANGE2                DEF                   SYS_TBS_DISK_DATA        2,097,152              256                    8
  SYS                   RANGE2                Q1_2014               SYS_TBS_DISK_DATA        2,097,152          112,896              112,688
  SYS                   RANGE2                Q2_2014               SYS_TBS_DISK_DATA        2,097,152           56,576               56,352
  SYS                   RANGE2                Q3_2014               SYS_TBS_DISK_DATA        2,097,152            1,792                1,704
  SYS                   RANGE2                Q4_2014               SYS_TBS_DISK_DATA        2,097,152              768                  576
  SYS                   RANGE_SALES           DEF                   SYS_TBS_DISK_DATA        2,097,152              256                    8
  SYS                   RANGE_SALES           Q1_2014               SYS_TBS_DISK_DATA        2,097,152            5,888                5,648
  SYS                   RANGE_SALES           Q2_2014               SYS_TBS_DISK_DATA        2,097,152           11,520               11,280
  SYS                   RANGE_SALES           Q3_2014               SYS_TBS_DISK_DATA        2,097,152            8,704                8,464
  SYS                   RANGE_SALES           Q4_2014               SYS_TBS_DISK_DATA        2,097,152            4,096                3,952
  21 rows selected.
  ```

# Disk Index

---

- Even if the table data is deleted with DELETE, the USED of the index does not decrease.
- To check the actual USED except FREE PAGE after DELETE, ALTER INDEX index_name AGING; must be executed.
- When executing ALTER INDEX ~ AGINING, the table is locked. Therefore, other requests for the table are put in a waiting state, so be cautious when executing the ALTER INDEX ~ AGAING.

  **ALTIBASE HDB 5.3.x, 5.5.1, 6.1.1, 6.3.1 Disk index usage query**

  ```
  -- Disk index usage column description
  -- USER_NAME	: Database user
  -- TABLE_NAME	: Table name
  -- PARTITIONED_NAME	: Partitioned table name. If a non-partitioned, NON-PARTITIONED
  -- INDEX_NAME	: Index name
  -- PARTITIONED_INDEX	: Partitioned index name
  -- TBS_NAME	: Tablespace to which the index belongs
  -- MAX(KB)	: Max size of tablespace
  -- ALLOC(KB)	: Total size allocated
  -- USED(KB)	: Size of the allocated space that includes data
  -- USAGE(%)	: Percentage of utilization compared to the maximum size of the tablespace
  set linesize 1024
  set colsize 20
  SELECT U.USER_NAME USER_NAME
       , I_LIST.TABLE_NAME
       , DECODE(I_LIST.PARTITION_NAME, NULL, 'NON-PARTITIONED', I_LIST.PARTITION_NAME) PARTITIONED_NAME
       , I_LIST.INDEX_NAME INDEX_NAME
       , DECODE(I_LIST.INDEX_PARTITION_NAME, NULL, 'NON-PARTITIONED', I_LIST.INDEX_PARTITION_NAME) PARTITIONED_INDEX
       , TBS.NAME TBS_NAME
       , TO_CHAR((D.MAX * TBS.PAGE_SIZE)/1024, '999,999,999') 'MAX(KB)'
       , TO_CHAR((TBS.EXTENT_PAGE_COUNT * TBS.PAGE_SIZE * SEG.TOTAL_EXTENT_COUNT)/1024, '999,999,999') 'ALLOC(KB)'
       , TO_CHAR(SEG.TOTAL_USED_SIZE/1024, '999,999,999,999') 'USED(KB)'
       , TO_CHAR(((SEG.TOTAL_USED_SIZE/(D.MAX*TBS.PAGE_SIZE))*100), '99.99') 'USAGE(%)'
    FROM (SELECT T.TABLE_NAME
               , PT.PARTITION_NAME
               , I.INDEX_NAME
               , PI.INDEX_PARTITION_NAME
               , DECODE(T.IS_PARTITIONED, 'F', I.TABLE_ID, 'T', PT.TABLE_ID) TABLE_ID
               , DECODE(T.IS_PARTITIONED, 'F', T.TABLE_OID, 'T', PT.PARTITION_OID) TABLE_OID
               , DECODE(I.IS_PARTITIONED, 'F', I.TBS_ID, 'T', PI.TBS_ID) TBS_ID
               , I.INDEX_ID
               , T.USER_ID
            FROM SYSTEM_.SYS_INDICES_ I LEFT OUTER JOIN SYSTEM_.SYS_INDEX_PARTITIONS_ PI ON PI.INDEX_ID = I.INDEX_ID
                                        LEFT OUTER JOIN SYSTEM_.SYS_TABLE_PARTITIONS_ PT ON PT.PARTITION_ID = PI.TABLE_PARTITION_ID
                                        LEFT OUTER JOIN SYSTEM_.SYS_TABLES_ T ON T.TABLE_ID = I.TABLE_ID AND T.TABLE_TYPE = 'T') I_LIST
       , X$SEGMENT SEG
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
   USER_NAME             TABLE_NAME            PARTITIONED_NAME      INDEX_NAME            PARTITIONED_INDEX     TBS_NAME              MAX(KB)          ALLOC(KB)        USED(KB)            USAGE(%)
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  SYS                   DISK_T                NON-PARTITIONED       DISK_T_IDX_01         NON-PARTITIONED       USER_IDX                 2,097,152           47,104               46,984      2.24
  SYS                   DISK_T2               NON-PARTITIONED       DISK_T2_IDX_01        NON-PARTITIONED       USER_IDX                 2,097,152              256                   16      0.00
  SYS                   EMP                   NON-PARTITIONED       EMP_IDX_01            NON-PARTITIONED       SYS_TBS_DISK_DATA        2,097,152              256                   32      0.00
  SYS                   PART_T1               P1                    PART_T1_IDX           P_IDX1                PART_IDX                 3,145,728              256                  216       .01
  SYS                   PART_T1               P2                    PART_T1_IDX           P_IDX2                PART_IDX                 3,145,728              256                  216       .01
  SYS                   PART_T1               P3                    PART_T1_IDX           P_IDX3                PART_IDX                 3,145,728           46,848               46,608      1.48
  SYS                   PART_T2               P201406               PART_T2_IDX_01        P201406               PART_IDX                 3,145,728            3,840                3,808       .12
  SYS                   PART_T2               P201407               PART_T2_IDX_01        P201407               PART_IDX                 3,145,728            7,680                7,528       .24
  SYS                   PART_T2               P201408               PART_T2_IDX_01        P201408               PART_IDX                 3,145,728            2,048                1,936       .06
  SYS                   PART_T2               P201512               PART_T2_IDX_01        P201512               PART_IDX                 3,145,728            3,072                2,856       .09
  SYS                   PART_T2               PMAX                  PART_T2_IDX_01        PMAX                  PART_IDX                 3,145,728            3,328                3,232       .10
  SYS                   PART_T2               P201406               PART_T2_IDX_02        P201406               PART_IDX                 3,145,728            3,840                3,808       .12
  SYS                   PART_T2               P201407               PART_T2_IDX_02        P201407               SYS_TBS_DISK_DATA        2,097,152            7,680                7,528       .36
  SYS                   PART_T2               P201408               PART_T2_IDX_02        P201408               SYS_TBS_DISK_DATA        2,097,152            2,304                1,936       .09
  SYS                   PART_T2               P201512               PART_T2_IDX_02        P201512               SYS_TBS_DISK_DATA        2,097,152            3,328                2,856       .14
  SYS                   PART_T2               PMAX                  PART_T2_IDX_02        PMAX                  SYS_TBS_DISK_DATA        2,097,152            3,584                3,232       .15
  16 rows selected.
  ```

# Reference - How to check the count of disk table and index

---

Error rendering macro 'code': Invalid value specified for parameter 'firstline'

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
SELECT DECODE(T.IS_PARTITIONED, 'T', 'PARTITIONED     INDEX CNT : '||PART_T.CNT, 'F', 'NON-PARTITIONED INDEX CNT : '||T.CNT) INDEX_COUNT
  FROM (SELECT IS_PARTITIONED
             , COUNT(*) CNT
          FROM SYSTEM_.SYS_INDICES_
         WHERE TABLE_ID IN (SELECT TABLE_ID
                              FROM SYSTEM_.SYS_TABLES_ T
                                 , V$DISKTBL_INFO D
                             WHERE T.TABLE_OID = D.TABLE_OID)
         GROUP BY IS_PARTITIONED) T
     , (SELECT COUNT(*) CNT FROM SYSTEM_.SYS_INDEX_PARTITIONS_) PART_T ;
```
