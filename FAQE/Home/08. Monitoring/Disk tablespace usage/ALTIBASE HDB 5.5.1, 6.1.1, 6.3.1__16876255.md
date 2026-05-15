---
title: "ALTIBASE HDB 5.5.1, 6.1.1, 6.3.1"
page_id: "16876255"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ALTIBASE+HDB+5.5.1%2C+6.1.1%2C+6.3.1"
updated_at: "2021-04-05T10:28:32.000+0900"
version: 3
ancestors: ["Home", "08. Monitoring", "Disk tablespace usage"]
labels: []
---

# ALTIBASE HDB 5.5.1, 6.1.1, 6.3.1
Source: https://docs.altibase.com/display/FAQE/ALTIBASE+HDB+5.5.1%2C+6.1.1%2C+6.3.1
Updated: 2021-04-05T10:28:32.000+0900

- [Overview](#ALTIBASEHDB5.5.1,6.1.1,6.3.1-Overview) - [Disk tablespace usage query](#ALTIBASEHDB5.5.1,6.1.1,6.3.1-Disktablespaceusagequery) - [Related bug](#ALTIBASEHDB5.5.1,6.1.1,6.3.1-Relatedbug) - [BUG-39985 V$DISK_UNDO_USAGE calculation error correction](#ALTIBASEHDB5.5.1,6.1.1,6.3.1-BUG-39985V$DISK_UNDO_USAGEcalculationerrorcorrection)

# Overview

---

- V$DISK_UNDO_USAGE was added in ALTIBASE HDB 5.5.1.
- This performance view allows users to check the usage of the undo tablespace.

# Disk tablespace usage query

---

**Disk tablespace usage query**

```
SET LINESIZE 1024;
SET COLSIZE 30;
SELECT DECODE(TYPE, 3, 'SYSTEM TABLESPACE', 4, 'USER DATA TABLESPACE', 5, 'SYSTEM TABLESPACE', 6, 'USER TEMP TABLESPACE', 7, 'SYSTEM TABLESPACE') TBS_TYPE
     , NAME TBS_NAME                                                                                                                                    -- TBS_NAME : Tablespace name
     , TO_CHAR((D.MAX * PAGE_SIZE / 1024 /1024), '999,999,999') 'MAX(M)'                                                                                -- MAX(M)   : Maximum size of tablespace
     , TO_CHAR((TOTAL_PAGE_COUNT * PAGE_SIZE)/1024/1024, '999,999,999') 'TOTAL(M)'                                                                      -- TOTAL(M) : Total number of pages allocated so far
     , DECODE(TYPE, 7, TO_CHAR((U.TOTAL_EXT_CNT*PROP.EXTENT_SIZE)/1024/1024, '999,999,999')
                     , TO_CHAR((ALLOCATED_PAGE_COUNT * PAGE_SIZE)/1024/1024, '999,999,999')) 'ALLOC(M)'                                                 -- ALLOC(M) : Total of only 'used pages' excluding 'blank pages' among the allocated pages so far.
     , DECODE(TYPE, 3, TO_CHAR(NVL(DS.USED, 0)/1024/1024, '999,999,999'),
                    4, TO_CHAR(NVL(DS.USED, 0)/1024/1024, '999,999,999'),
                    7, TO_CHAR(((U.TX_EXT_CNT+U.USED_EXT_CNT+U.UNSTEALABLE_EXT_CNT) * PROP.EXTENT_SIZE)/1024/1024, '999,999,999')
                     , LPAD('-', 12))'USED(M)'                                                                                                          -- USED(M)  : Size of the pages in which the data is loaded
     , DECODE(TYPE, 7, TO_CHAR((((U.TX_EXT_CNT+U.USED_EXT_CNT+U.UNSTEALABLE_EXT_CNT) * PROP.EXTENT_SIZE)/(D.MAX*PAGE_SIZE))*100, '99.99'),
                    3, TO_CHAR(NVL(DS.USED, 0)/(D.MAX*PAGE_SIZE)* 100, '99.99'),
                    4, TO_CHAR(NVL(DS.USED, 0)/(D.MAX*PAGE_SIZE)* 100, '99.99')
                     , TO_CHAR((ALLOCATED_PAGE_COUNT/D.MAX) * 100, '99.99')) 'USAGE(%)'                                                                 -- USAGE(%) : Usage (USED versus MAX)
     , DECODE(STATE, 1, 'OFFLINE', 2, 'ONLINE', 5, 'OFFLINE BACKUP', 6, 'ONLINE BACKUP', 128, 'DROPPED', 'DISCARDED') STATE                             -- STATE    : Tablespace state
     , D.AUTOEXTEND
  FROM V$TABLESPACES T LEFT OUTER JOIN(SELECT SPACE_ID , SUM(TOTAL_USED_SIZE) USED
                                         FROM X$SEGMENT
                                        GROUP BY SPACE_ID) DS ON DS.SPACE_ID = T.ID
     , (SELECT SPACEID
             , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
             , DECODE(MAX(AUTOEXTEND), 1, 'ON', 'OFF') 'AUTOEXTEND'
          FROM V$DATAFILES
         GROUP BY SPACEID ) D
     , V$DISK_UNDO_USAGE U
     , (SELECT VALUE1 EXTENT_SIZE
          FROM V$PROPERTY
         WHERE NAME = 'SYS_UNDO_TBS_EXTENT_SIZE') PROP
 WHERE T.ID = D.SPACEID ;
```

**Example of output**

```
TBS_TYPE              TBS_NAME                        MAX(M)           TOTAL(M)         ALLOC(M)         USED(M)                   USAGE(%)         STATE           AUTOEXTEND
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
SYSTEM TABLESPACE     SYS_TBS_DISK_DATA                      2,048              952              952              952               46.46           ONLINE          ON
SYSTEM TABLESPACE     SYS_TBS_DISK_UNDO                      2,048              704                8                8                 .39           ONLINE          ON
SYSTEM TABLESPACE     SYS_TBS_DISK_TEMP                      2,048              100                1                -                 .02           ONLINE          ON
USER DATA TABLESPACE  PART_DATA                              1,024            1,024              177              176               17.19           ONLINE          OFF
USER DATA TABLESPACE  PART_DATA_DEF                          1,024            1,024               12               11                1.07           ONLINE          OFF
USER DATA TABLESPACE  PART_IDX                               3,072            3,072              416              415               13.49           ONLINE          OFF
6 rows selected.
```

# Related bug

---

### BUG-39985 V$DISK_UNDO_USAGE calculation error correction

The REUSABLE_EXT_CNT column of V$DISK_UNDO_USAGE defines the reusable size within the undo tablespace.

An undo tablespace pool phenomenon occurred, but the REUSABLE_EXT_CNT column has an error indicating that there is reusable space, so it has been improved.

This bug is reflected in the version below.

- ALTIBASE HDB version 6.1.1.4.9
- ALTIBASE HDB version 6.3.1

```
SET LINESIZE 1024;
SET COLSIZE 30;
SELECT DECODE(TYPE, 3, 'SYSTEM TABLESPACE', 4, 'USER DATA TABLESPACE', 5, 'SYSTEM TABLESPACE', 6, 'USER TEMP TABLESPACE', 7, 'SYSTEM TABLESPACE') TBS_TYPE
     , NAME TBS_NAME                                                                                                                                    -- TBS_NAME : Tablespace name
     , TO_CHAR((D.MAX * PAGE_SIZE / 1024 /1024), '999,999,999') 'MAX(M)'                                                                                -- MAX(M)   : Max size of tablespace
     , TO_CHAR((TOTAL_PAGE_COUNT * PAGE_SIZE)/1024/1024, '999,999,999') 'TOTAL(M)'                                                                      -- TOTAL(M) : Total number of pages allocated so far.
     , DECODE(TYPE, 7, TO_CHAR((U.TOTAL_EXT_CNT*PROP.EXTENT_SIZE)/1024/1024, '999,999,999')
                     , TO_CHAR((ALLOCATED_PAGE_COUNT * PAGE_SIZE)/1024/1024, '999,999,999')) 'ALLOC(M)'                                                 -- ALLOC(M) : Total of only 'used pages' excluding 'blank pages' among the allocated pages so far.
     , DECODE(TYPE, 3, TO_CHAR(NVL(DS.USED, 0)/1024/1024, '999,999,999'),
                    4, TO_CHAR(NVL(DS.USED, 0)/1024/1024, '999,999,999'),
                    7, TO_CHAR(((U.TX_EXT_CNT+U.USED_EXT_CNT+U.UNSTEALABLE_EXT_CNT) * PROP.EXTENT_SIZE)/1024/1024, '999,999,999')
                     , LPAD('-', 12))'USED(M)'                                                                                                          -- USED(M)  : Size of the pages in which the data is loaded
     , DECODE(TYPE, 7, TO_CHAR((((U.TX_EXT_CNT+U.USED_EXT_CNT+U.UNSTEALABLE_EXT_CNT) * PROP.EXTENT_SIZE)/(D.MAX*PAGE_SIZE))*100, '99.99'),
                    3, TO_CHAR(NVL(DS.USED, 0)/(D.MAX*PAGE_SIZE)* 100, '99.99'),
                    4, TO_CHAR(NVL(DS.USED, 0)/(D.MAX*PAGE_SIZE)* 100, '99.99')
                     , TO_CHAR((ALLOCATED_PAGE_COUNT/D.MAX) * 100, '99.99')) 'USAGE(%)'                                                                 -- USAGE(%) : USED compared with MAX
     , DECODE(STATE, 1, 'OFFLINE', 2, 'ONLINE', 5, 'OFFLINE BACKUP', 6, 'ONLINE BACKUP', 128, 'DROPPED', 'DISCARDED') STATE                             -- STATE    : Tablespace state
     , D.AUTOEXTEND
  FROM V$TABLESPACES T LEFT OUTER JOIN(SELECT SPACE_ID , SUM(TOTAL_USED_SIZE) USED
                                         FROM X$SEGMENT
                                        GROUP BY SPACE_ID) DS ON DS.SPACE_ID = T.ID
     , (SELECT SPACEID
             , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
             , DECODE(MAX(AUTOEXTEND), 1, 'ON', 'OFF') 'AUTOEXTEND'
          FROM V$DATAFILES
         GROUP BY SPACEID ) D
     , V$DISK_UNDO_USAGE U
     , (SELECT VALUE1 EXTENT_SIZE
          FROM V$PROPERTY
         WHERE NAME = 'SYS_UNDO_TBS_EXTENT_SIZE') PROP
 WHERE T.ID = D.SPACEID ;
```

```
SET LINESIZE 1024;
SET COLSIZE 30;
SELECT DECODE(TYPE, 3, 'SYSTEM TABLESPACE', 4, 'USER DATA TABLESPACE', 5, 'SYSTEM TABLESPACE', 6, 'USER TEMP TABLESPACE', 7, 'SYSTEM TABLESPACE') TBS_TYPE
     , NAME TBS_NAME                                                                                                                                    -- TBS_NAME : Tablespace name
     , TO_CHAR((D.MAX * PAGE_SIZE / 1024 /1024), '999,999,999') 'MAX(M)'                                                                                -- MAX(M)   : Max size of tablespace
     , TO_CHAR((TOTAL_PAGE_COUNT * PAGE_SIZE)/1024/1024, '999,999,999') 'TOTAL(M)'                                                                      -- TOTAL(M) : Total number of pages allocated so far.
     , DECODE(TYPE, 7, TO_CHAR((U.TOTAL_EXT_CNT*PROP.EXTENT_SIZE)/1024/1024, '999,999,999')
                     , TO_CHAR((ALLOCATED_PAGE_COUNT * PAGE_SIZE)/1024/1024, '999,999,999')) 'ALLOC(M)'                                                 -- ALLOC(M) : Total of only 'used pages' excluding 'blank pages' among the allocated pages so far.
     , DECODE(TYPE, 3, TO_CHAR(NVL(DS.USED, 0)/1024/1024, '999,999,999'),
                    4, TO_CHAR(NVL(DS.USED, 0)/1024/1024, '999,999,999'),
                    7, TO_CHAR(((U.TX_EXT_CNT+U.USED_EXT_CNT+U.UNSTEALABLE_EXT_CNT) * PROP.EXTENT_SIZE)/1024/1024, '999,999,999')
                     , LPAD('-', 12))'USED(M)'                                                                                                          -- USED(M)  : Size of the pages in which the data is loaded
     , DECODE(TYPE, 7, TO_CHAR((((U.TX_EXT_CNT+U.USED_EXT_CNT+U.UNSTEALABLE_EXT_CNT) * PROP.EXTENT_SIZE)/(D.MAX*PAGE_SIZE))*100, '99.99'),
                    3, TO_CHAR(NVL(DS.USED, 0)/(D.MAX*PAGE_SIZE)* 100, '99.99'),
                    4, TO_CHAR(NVL(DS.USED, 0)/(D.MAX*PAGE_SIZE)* 100, '99.99')
                     , TO_CHAR((ALLOCATED_PAGE_COUNT/D.MAX) * 100, '99.99')) 'USAGE(%)'                                                                 -- USAGE(%) : USED compared with MAX
     , DECODE(STATE, 1, 'OFFLINE', 2, 'ONLINE', 5, 'OFFLINE BACKUP', 6, 'ONLINE BACKUP', 128, 'DROPPED', 'DISCARDED') STATE                             -- STATE    : Tablespace state
     , D.AUTOEXTEND
  FROM V$TABLESPACES T LEFT OUTER JOIN(SELECT SPACE_ID , SUM(TOTAL_USED_SIZE) USED
                                         FROM X$SEGMENT
                                        GROUP BY SPACE_ID) DS ON DS.SPACE_ID = T.ID
     , (SELECT SPACEID
             , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
             , DECODE(MAX(AUTOEXTEND), 1, 'ON', 'OFF') 'AUTOEXTEND'
          FROM V$DATAFILES
         GROUP BY SPACEID ) D
     , V$DISK_UNDO_USAGE U
     , (SELECT VALUE1 EXTENT_SIZE
          FROM V$PROPERTY
         WHERE NAME = 'SYS_UNDO_TBS_EXTENT_SIZE') PROP
 WHERE T.ID = D.SPACEID ;
```
