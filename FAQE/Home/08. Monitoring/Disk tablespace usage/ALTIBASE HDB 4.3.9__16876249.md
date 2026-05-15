---
title: "ALTIBASE HDB 4.3.9"
page_id: "16876249"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ALTIBASE+HDB+4.3.9"
updated_at: "2021-03-24T08:35:24.000+0900"
version: 1
ancestors: ["Home", "08. Monitoring", "Disk tablespace usage"]
labels: []
---

# ALTIBASE HDB 4.3.9
Source: https://docs.altibase.com/display/FAQE/ALTIBASE+HDB+4.3.9
Updated: 2021-03-24T08:35:24.000+0900

**Disk tablespace usage query**

```
set linesize 1024;
set colsize 30;
SELECT TBS.NAME TBS_NAME                                                                                                    -- Disk tablespace name
     , TO_CHAR(ROUND(DAT.MAX * TBS.PAGE_SIZE / 1024 /1024, 2)) 'MAX(M)'                                                     -- Maximum size that can be allocated
     , ROUND(TBS.TOTAL_PAGE_COUNT * TBS.PAGE_SIZE / 1024 / 1024, 2) 'TOTAL(M)'                                              -- Total number of pages allocated so far
     , DECODE(TBS.TYPE, 5, ROUND( UNDO.ALLOC * TBS.PAGE_SIZE/1024/1024, 2) /* UNDO TABLESPACE*/
                         , ROUND( TBS.ALLOCATED_PAGE_COUNT * TBS.PAGE_SIZE / 1024 / 1024, 2) ) 'ALLOC(M)'                   -- Total of only 'used pages' excluding 'blank pages' among the allocated pages so far
     , DECODE(TBS.TYPE, 3, '-' /* TEMP TABLESPACE */
                      , 5, ROUND( UNDO.USED * TBS.PAGE_SIZE /1024/1024, 2) /* UNDO TABLESPACE*/                             -- Size of the pages in use at which data is loaded. TEMP TABLESPACE cannot be obtained.
                         , DECODE(SEG.USED, '', 0, ROUND((SEG.USED * TBS.PAGE_SIZE * TBS.A_EXTENT_PAGE_COUNT)/1024/1024, 2)) /* USER TABLESPACE & SYS_TBS_DATA */) 'USED(M)'
     , DECODE(TBS.TYPE, 5, ROUND( UNDO.ALLOC / DAT.MAX * 100, 2) --UNDO
                         , ROUND( TBS.ALLOCATED_PAGE_COUNT / DAT.MAX * 100, 2) ) 'USAGE(%)'
     , DECODE(TBS.STATE, 1, 'ONLINE', 2, 'BEGIN BACKUP', 3, 'END BACKUP', 'NOT DEFINED') STATE
     , DAT.AUTOEXTEND
  FROM V$TABLESPACES TBS LEFT OUTER JOIN (SELECT SPACE_ID , SUM(EXTENT_TOTAL_COUNT) ALLOC , SUM(EXTENT_FULL_COUNT ) USED
                                            FROM X$SEGMENT
                                            GROUP BY SPACE_ID
                                         ) SEG ON TBS.ID = SEG.SPACE_ID
     ,(SELECT SPACEID
             , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
             , DECODE(MAX(AUTOEXTEND), 1, 'ON', 'OFF') 'AUTOEXTEND'
          FROM V$DATAFILES
         GROUP BY SPACEID ) DAT
     , (SELECT SUM(ALLOCATED_PAGE_COUNT) ALLOC
             , SUM(USED_PAGE_COUNT) USED
          FROM V$UNDO_TBS ) UNDO
 WHERE TBS.ID = DAT.SPACEID;
```

**Example of output**

```
TBS_NAME                        MAX(M)                          TOTAL(M)    ALLOC(M)    USED(M)                         USAGE(%)    STATE         AUTOEXTEND
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
SYS_TBS_DATA                    2049                            249         249         0                               12.15       ONLINE        ON
SYS_TBS_UNDO                    2048                            246         245.72      0.02                            12          ONLINE        ON
SYS_TBS_TEMP                    2048                            100         1           -                               0.05        ONLINE        ON
USER_DATA                       2048                            2048        832         831                             40.63       ONLINE        OFF
USER_IDX                        2048                            2048        157         155.75                          7.67        ONLINE        OFF
USER_IDX_TBS                    512                             512         1           0                               0.2         ONLINE        OFF
6 rows selected.
```
