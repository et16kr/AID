---
title: "ALTIBASE HDB 5.1.5"
page_id: "16876251"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ALTIBASE+HDB+5.1.5"
updated_at: "2021-03-24T08:42:58.000+0900"
version: 1
ancestors: ["Home", "08. Monitoring", "Disk tablespace usage"]
labels: []
---

# ALTIBASE HDB 5.1.5
Source: https://docs.altibase.com/display/FAQE/ALTIBASE+HDB+5.1.5
Updated: 2021-03-24T08:42:58.000+0900

# - [Overview](#ALTIBASEHDB5.1.5-Overview) - [Disk tablespace usage query](#ALTIBASEHDB5.1.5-Disktablespaceusagequery)

# Overview

---

- In ALTIBASE HDB version 5, the disk tablespace usage cannot be queried due to the change in the disk table structure, and only the allocated size is known.
- Starting from ALTIBASE HDB version 5.3.3, it has been improved so that the usage can be queried. (Excluding undo tablespaces and temporary tablespaces)

# Disk tablespace usage query

---

**Disk tablespace usage query**

```
SET LINESIZE 1024;SET COLSIZE 30;SELECT  NAME TBS_NAME                                         -- Disk tablespace name
      , TO_CHAR(ROUND(D.MAX * PAGE_SIZE / 1024 /1024, 2)) 'MAX(M)'                             -- Max size of tablespace
      , ROUND(TOTAL_PAGE_COUNT * PAGE_SIZE / 1024 / 1024, 2) 'TOTAL(M)'                        -- Total number of pages allocated so far
      , DECODE(TYPE, 7, ROUND((SELECT (SUM(total_page_count) * PAGE_SIZE)/1024/1024
                                 FROM V$undo_seg)+
                              (SELECT (SUM(ALLOC_PAGE_COUNT) * PAGE_SIZE)/1024/1024
                                 FROM v$tss_seg), 2)
                      , ROUND(ALLOCATED_PAGE_COUNT * PAGE_SIZE / 1024 / 1024, 2)) 'ALLOC(M)'   -- Total of only 'used pages' excluding 'blank pages' among the allocated pages so far
      , DECODE(TYPE, 7, ROUND( ( (SELECT SUM(total_page_count) FROM V$undo_seg) +
                                 (SELECT SUM(ALLOC_PAGE_COUNT) FROM v$tss_seg ) ) / D.MAX  * 100, 2)
                      , ROUND(ALLOCATED_PAGE_COUNT / D.MAX * 100, 2))             'USAGE(%)'   -- ALLOC utilization rate compared to MAX
       , DECODE(STATE, 1, 'OFFLINE', 2, 'ONLINE', 5, 'OFFLINE BACKUP', 6, 'ONLINE BACKUP', 128, 'DROPPED', 'DISCARDED') STATE
       , D.AUTOEXTEND
  FROM V$TABLESPACES T
       ,(SELECT  SPACEID
              , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
              , DECODE(MAX(AUTOEXTEND), 1, 'ON', 'OFF') 'AUTOEXTEND'
           FROM V$DATAFILES
           GROUP BY SPACEID) D
 WHERE T.ID = D.SPACEID
;
```

**Example of output**

```
TBS_NAME                        MAX(M)                          TOTAL(M)    ALLOC(M)    USAGE(%)    STATE           AUTOEXTEND
----------------------------------------------------------------------------------------------------------------------------------------
SYS_TBS_DISK_DATA               2048                            100         0.25        0.01        ONLINE          ON
SYS_TBS_DISK_UNDO               2048                            100         2           0.1         ONLINE          ON
SYS_TBS_DISK_TEMP               2048                            100         0.25        0.01        ONLINE          ON
3 rows selected.
```
