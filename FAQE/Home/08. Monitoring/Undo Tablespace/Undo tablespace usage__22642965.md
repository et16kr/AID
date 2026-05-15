---
title: "Undo tablespace usage"
page_id: "22642965"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Undo+tablespace+usage"
updated_at: "2025-10-20T15:45:22.000+0900"
version: 1
ancestors: ["Home", "08. Monitoring", "Undo Tablespace"]
labels: []
---

# Undo tablespace usage
Source: https://docs.altibase.com/display/FAQE/Undo+tablespace+usage
Updated: 2025-10-20T15:45:22.000+0900

- [Overview](#Undotablespaceusage-Overview) - [Version](#Undotablespaceusage-Version) - [Undo tablespace usage](#Undotablespaceusage-Undotablespaceusage) - [V$DISK_UNDO_USAGE performance view](#Undotablespaceusage-V$DISK_UNDO_USAGEperformanceview) - [Related bug](#Undotablespaceusage-Relatedbug)

# Overview

---

- Prior to ALTIBASE HDB 5.5.1, only ALLOC of undo tablespace could be checked, but USED could not be checked.
- This chapter describes how to check the actual usage tablespaces using V$DISK_UNDO_USAGE added from ALTIBASE HDB version 5.5.1.

#### ALLOC and USED of undo tablespace

---

- The undo tablespace is made up of segments, and segments are made up of smaller units called extents.
- When a change transaction occurs in a disk table, it is allocated in units of extents. Whenever an extent is newly allocated, the size of the undo tablespace ALLOC increases.
- When the transaction ends, the extent becomes reusable.
- However, if any of the extents within a segment are in use, even if there are reusable extents, all of the extents within that segment become unusable. (UNSTEALABLE EXTENT)
- Either the extent is used because a change transaction is executing, or the UNSTEALABLE extent is counted as USED for the undo tablespace.

# Version

---

This monitoring query is available in the version below.

- Altibase 5.5.1
- Altibase 6.1.1
- Altibase 6.3.1
- Altibase 6.5.1
- Altibase 7.1.1
- Altibase 7.3.1

# Undo tablespace usage

---

- ALLOC and USED may increase while a change transaction is being performed on the disk table.
- If the transaction is committed, the USED that is increased during the execution of the transaction is reduced.
- If the transaction is rolled back, the ALLOC and USED that have increased during the execution of the transaction will be reduced.

**Undo tablespace usage query**

```
SELECT T.NAME TBS_NAME
     , ROUND(D.MAX * PAGE_SIZE / 1024 /1024, 2) 'MAX(M)'                                                                        -- Max size of undo tablespace
     , ROUND((TOTAL_PAGE_COUNT * PAGE_SIZE) / 1024 / 1024, 2) 'TOTAL(M)'                                                        -- Total size allocated for undo tablespace
     , ROUND((U.TOTAL_EXT_CNT*PROP.EXTENT_SIZE)/1024/1024, 2) 'ALLOC(M)'                                                        -- Total of only 'used pages' excluding 'blank pages' among the allocated pages so far
     , ROUND(((U.TX_EXT_CNT+U.USED_EXT_CNT+U.UNSTEALABLE_EXT_CNT) * PROP.EXTENT_SIZE)/1024/1024, 2) 'USED(M)'                   -- Size of the EXTENT that cannot be reused or in use by the change transaction
     , ROUND((((U.TX_EXT_CNT+U.USED_EXT_CNT+U.UNSTEALABLE_EXT_CNT) * PROP.EXTENT_SIZE)/(D.MAX*PAGE_SIZE))*100, 2) 'USAGE(%)'    -- USED compared with MAX
     , DECODE(STATE,1,'OFFLINE',2,'ONLINE',5,'OFFLINE BACKUP',6,'ONLINE BACKUP',128,'DROPPED', 'DISCARDED') STATE               -- Tablespace state
     , D.AUTOEXTEND
  FROM V$TABLESPACES T
     , (SELECT SPACEID
             , SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX
             , DECODE(MAX(AUTOEXTEND),1,'ON','OFF') 'AUTOEXTEND'
          FROM V$DATAFILES
         GROUP BY SPACEID) D
     , V$DISK_UNDO_USAGE U
     , (SELECT VALUE1 EXTENT_SIZE FROM V$PROPERTY WHERE NAME = 'SYS_UNDO_TBS_EXTENT_SIZE') PROP
 WHERE T.ID = D.SPACEID
   AND T.ID = 3 ;
```

**Example of output**

```
TBS_NAME                        MAX(M)      TOTAL(M)    ALLOC(M)    USED(M)     USAGE(%)    STATE           AUTOEXTEND
---------------------------------------------------------------------------------------------------------------------------------
SYS_TBS_DISK_UNDO               2047.99     302         122.25      84.25       4.11        ONLINE          ON
1 row selected.
```

| Column Name | Description |
| --- | --- |
| TBS_NAME | Tablespace Name |
| MAX(M) | Maximum Size of Undo Tablespace |
| TOTAL(M) | Total Allocated Size for Undo Tablespace |
| ALLOC(M) | Total Used Pages (excluding free pages) among Allocated Pages |
| USED(M) | Size of Extents Used or Unusable Due to Active Transactions |
| USAGE(%) | Usage (USED vs. MAX) |
| STATE | Tablespace Status |
| AUTOEXTEND | Auto Extend Enabled up to Maximum Size |

# V$DISK_UNDO_USAGE performance view

---

| Column name | Data type | Description |
| --- | --- | --- |
| TX_EXT_CNT | BIGINT | Number of extents for a segment (Transaction Status Segment, TSS) that stores transaction status information. It is allocated when an update transaction occurs in the disk table. |
| USED_EXT_CNT | BIGINT | Number of extents in the undo segment being used in the transaction. When an update transaction occurs in the disk table, it is allocated as needed. |
| UNSTEALABLE_EXT_CNT | BIGINT | Number of extents that cannot be taken from other undo segments. The extent that belongs to the online undo segment and the extent that has header information. Contains the extent the transaction is accessing. Even if the undo segment has reusable extents, it cannot be taken from other undo segments. |
| REUSABLE_EXT_CNT | BIGINT | Number of reusable extents USED_EXT_CNT used during transaction progress increases as USED_EXT_CNT decreases when the transaction is committed. |
| TOTAL_EXT_CNT | BIGINT | The total number of extents allocated from the undo tablespace. When a transaction is rolled back, the extents used in the transaction are returned to the undo tablespace. When a transaction is committed, the extents used in the transaction are held in the corresponding undo segment. |

# Related bug

---

**Bug Description**

- Improved an issue where undo areas that cannot be reused were incorrectly counted as available space. (Extents corresponding to the UNSTEALABLE_EXT_CNT column were mistakenly calculated as usable extents.) (BUG-39985)

**Applied Versions**

- Altibase 6.1.1.4.9 or later

- Altibase 6.3.1.3.3 or later

- Altibase 6.5.1 or later
