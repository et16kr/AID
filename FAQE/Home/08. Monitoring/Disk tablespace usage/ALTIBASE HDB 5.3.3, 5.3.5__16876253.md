---
title: "ALTIBASE HDB 5.3.3, 5.3.5"
page_id: "16876253"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ALTIBASE+HDB+5.3.3%2C+5.3.5"
updated_at: "2021-03-24T08:49:49.000+0900"
version: 1
ancestors: ["Home", "08. Monitoring", "Disk tablespace usage"]
labels: []
---

# ALTIBASE HDB 5.3.3, 5.3.5
Source: https://docs.altibase.com/display/FAQE/ALTIBASE+HDB+5.3.3%2C+5.3.5
Updated: 2021-03-24T08:49:49.000+0900

- [Overview](#ALTIBASEHDB5.3.3,5.3.5-Overview) - [Disk tablespace usage query](#ALTIBASEHDB5.3.3,5.3.5-Disktablespaceusagequery)

# Overview

---

- Starting from ALTIBASE HDB version 5.3.3, the actual usage of the tablespace can be checked by using the TOTAL_USED_SIZE column information of X$SEGMENT.
- The TOTAL_USED_SIZE column of X$SEGMENT was added in [BUG-31372](https://altra.altibase.com/altimis-2.0/app_bug_new/bug_view.jsp?pk=31372).
- The version reflecting BUG-31372 is as follows.
    - ALTIBASE HDB 5.3.3.33
    - ALTIBASE HDB 5.3.5.15
    - ALTIBASE HDB 5.5.1.0.3
- Therefore, in ALTIBASE HDB 5.3.3, 5.3.5, 5.5.1 versions without BUG-31372 being modified, an error may occur when using the following query.
- The actual usage of undo tablespaces and temporary tablespaces is not available in this version.

# Disk tablespace usage query

---

```
SET LINESIZE 1024;
SET COLSIZE 30;
SELECT NAME TBS_NAME                                                                                                            -- TBS_NAME : Disk tablespace name
     , TO_CHAR(D.MAX * PAGE_SIZE / 1024 /1024, '999,999,999') 'MAX(M)'                                                          -- MAX(M)   : Max size of tablespace
     , TO_CHAR(TOTAL_PAGE_COUNT*PAGE_SIZE/1024/1024, '999,999,999') 'TOTAL(M)'                                                  -- TOTAL(M) : Total page size allocated to date
     , DECODE(TYPE, 7, TO_CHAR((SELECT (SUM(TOTAL_EXTENT_COUNT*PAGE_COUNT_IN_EXTENT)*PAGE_SIZE)/1024/1024
                          FROM V$UDSEGS)+ (SELECT (SUM(TOTAL_EXTENT_COUNT*PAGE_COUNT_IN_EXTENT)*PAGE_SIZE)/1024/1024
                          FROM V$TSSEGS), '999,999,999') , /* UNDO */
                       TO_CHAR((ALLOCATED_PAGE_COUNT*PAGE_SIZE)/1024/1024, '999,999,999')) 'ALLOC(M)'                           -- ALLOC(M) : Total of only 'used pages' excluding 'blank pages' among the allocated pages so far
     , DECODE(TYPE, 3, TO_CHAR(NVL(DS.USED, 0)/1024/1024, '999,999,999'),
                    4, TO_CHAR(NVL(DS.USED, 0)/1024/1024, '999,999,999') /* SYS_TEMP */
                     , LPAD('-', 12)) 'USED(M)'                                                                                 -- USED(M)  : Size of the pages in use at which data is loaded. TEMP and UNDO cannot obtain USED.
     , DECODE(TYPE, 7, TO_CHAR(((SELECT SUM(TOTAL_EXTENT_COUNT*PAGE_COUNT_IN_EXTENT)
                                  FROM V$UDSEGS)+ (SELECT SUM(TOTAL_EXTENT_COUNT*PAGE_COUNT_IN_EXTENT)
                                  FROM V$TSSEGS)) / D.MAX* 100,  '99.99') ,          /* UNDO */
                    3, TO_CHAR(NVL(DS.USED, 0)/(D.MAX*PAGE_SIZE)* 100,  '99.99') ,
                    4, TO_CHAR(NVL(DS.USED, 0)/(D.MAX*PAGE_SIZE)* 100,  '99.99') ,   /* TEMP */
                       TO_CHAR(ALLOCATED_PAGE_COUNT / D.MAX * 100,  '99.99') ) 'USAGE(%)'                                       -- USAGE(%) : USED compared with MAX. For TEMP and UNDO, ALLOC compared with MAX.
     , DECODE(STATE, 1, 'OFFLINE', 2, 'ONLINE', 5, 'OFFLINE BACKUP', 6, 'ONLINE BACKUP', 128, 'DROPPED', 'DISCARDED') STATE     -- STATE    : Tablespace state
     , D.AUTOEXTEND
  FROM V$TABLESPACES T LEFT OUTER JOIN (SELECT SPACE_ID , SUM(TOTAL_USED_SIZE) USED
                                          FROM X$SEGMENT
                                         GROUP BY SPACE_ID ) DS ON DS.SPACE_ID = T.ID
     ,(SELECT SPACEID
             , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
             , DECODE(MAX(AUTOEXTEND), 1, 'ON', 'OFF') 'AUTOEXTEND'
          FROM V$DATAFILES
         GROUP BY SPACEID ) D
 WHERE T.ID = D.SPACEID
;
```

**Example of output**

```
TBS_NAME                        MAX(M)           TOTAL(M)         ALLOC(M)         USED(M)                   USAGE(%)         STATE           AUTOEXTEND
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
SYS_TBS_DISK_DATA                      2,048              217              217              211               10.32           ONLINE          ON
SYS_TBS_DISK_UNDO                      2,048              323              322                -               15.73           ONLINE          ON
SYS_TBS_DISK_TEMP                      2,048              100                0                -                 .01           ONLINE          ON
USER_DATA                              2,048            2,048              310              309               15.07           ONLINE          OFF
USER_IDX                               2,048            2,048               47               46                2.24           ONLINE          OFF
PART_DATA                              1,024            1,024              173              171               16.72           ONLINE          OFF
PART_DATA_DEF                          1,024            1,024               10                9                 .92           ONLINE          OFF
PART_IDX                               3,072            3,072               70               69                2.23           ONLINE          OFF
8 rows selected.
```
