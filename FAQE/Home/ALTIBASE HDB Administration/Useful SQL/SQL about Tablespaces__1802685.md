---
title: "SQL about Tablespaces"
page_id: "1802685"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/SQL+about+Tablespaces"
updated_at: "2011-07-22T17:00:00.000+0900"
version: 4
ancestors: ["Home", "ALTIBASE HDB Administration", "Useful SQL"]
labels: []
---

# SQL about Tablespaces
Source: https://docs.altibase.com/display/FAQE/SQL+about+Tablespaces
Updated: 2011-07-22T17:00:00.000+0900

- [The usage of a Memory tablespace](#SQLaboutTablespaces-TheusageofaMemorytablespace)
    - [ALTIBASE HDB V4](#SQLaboutTablespaces-ALTIBASEHDBV4)
    - [ALTIBASE HDB V5](#SQLaboutTablespaces-ALTIBASEHDBV5)
- [Total memory tablespace usage](#SQLaboutTablespaces-Totalmemorytablespaceusage)
- [Disk Tablespace Usage](#SQLaboutTablespaces-DiskTablespaceUsage)
    - [ALTIBASE HDB V4](#SQLaboutTablespaces-ALTIBASEHDBV4.1)
    - [ALTIBASE HDB V5](#SQLaboutTablespaces-ALTIBASEHDBV5.1)
- [The datafile information](#SQLaboutTablespaces-Thedatafileinformation)
- [I/O statistics of datafiles](#SQLaboutTablespaces-I/Ostatisticsofdatafiles)
    - [ALTIBASE HDB V4](#SQLaboutTablespaces-ALTIBASEHDBV4.2)
    - [ALTIBASE HDB V5](#SQLaboutTablespaces-ALTIBASEHDBV5.2)

# The usage of a Memory tablespace

This query returns the information about a memory tablespace.

| Columns | Description |
| --- | --- |
| TBS_ID | the unique identifier of the tablespace |
| TBS_TYPE | the type of the tablespace |
| TBS_NAME | the name of the tablespace |
| MAX(M) | the max size of the tablespace (Megabyte) |
| TOTAL(M) | the total size of the tablespace (Megabyte) |
| ALLOC(M) | the allocated size of the tablespace (Megabyte) |
| USED(M) | actually used size of the tablespace (Megabyte) |
| USAGE(%) | the tablespace usages. (USED(M) / MAX(M)) * 100. if MAX(M) is unlimited, it assumes that MAX(M) is MEM_MAX_DB_SIZE in altibase.properties. |
| STATE | the state of the tablespace |
| AUTOEXTEND | whether the tablespace can be extended automatically |

## ALTIBASE HDB V4

ALTIBASE HDB V4 does not support User Memory Tablespaces. There's only one memory tablespace including system dictionary tablespace.

## ALTIBASE HDB V5

```
SELECT 	ID TBS_ID,
        DECODE(TYPE, 0, 'MEMORY_DICTIONARY', 1, 'MEMORY_SYS_DATA', 2, 'MEMORY_USER_DATA', 8, 'VOLATILE_USER_DATA') TBS_TYPE,
        NAME TBS_NAME,
        DECODE(MAXSIZE, 140737488322560, 'UNDEFINED', MAXSIZE) 'MAX(M)',
        ROUND(ALLOCATED_PAGE_COUNT * PAGE_SIZE / 1024 / 1024, 2) 'TOTAL(M)',
        ROUND(NVL(M.ALLOC_PAGE_COUNT-M.FREE_PAGE_COUNT,TOTAL_PAGE_COUNT)*PAGE_SIZE/1024/1024,2) 'ALLOC(M)',
        MT.USED 'USED(M)',
        DECODE(MAXSIZE, 140737488322560, ROUND((M.ALLOC_PAGE_COUNT-M.FREE_PAGE_COUNT)*PAGE_SIZE/ MEM_MAX_DB_SIZE*100,2),
        ROUND((M.ALLOC_PAGE_COUNT-M.FREE_PAGE_COUNT)*PAGE_SIZE/MAXSIZE*100,2)) 'USAGE(%)',
        DECODE(STATE,1,'OFFLINE',2,'ONLINE',5,'OFFLINE BACKUP',6,'ONLINE BACKUP',128,'DROPPED', 'DISCARDED') STATE,
        DECODE(AUTOEXTEND_MODE,1,'ON','OFF') 'AUTOEXTEND'
FROM    V$DATABASE D,
        V$TABLESPACES T,
        V$MEM_TABLESPACES M,
        (
          SELECT TABLESPACE_ID,
                 ROUND(SUM((FIXED_USED_MEM + VAR_USED_MEM))/(1024*1024),3) USED
          FROM   V$MEMTBL_INFO
          GROUP BY TABLESPACE_ID
        ) MT
WHERE T.ID = M.SPACE_ID AND ID = MT.TABLESPACE_ID ;
```

# Total memory tablespace usage

This query returns the total memory tablespace usage.

| Columns | Description |
| --- | --- |
| MAX(M) | the max size of the tablespace (Megabyte) |
| TOTAL(M) | the total size of the tablespace (Megabyte) |
| ALLOC(M) | allocated size of the tablespace (Megabyte) |
| USED(M) | actually used size of the tablespace (Megabyte) |
| USAGE(%) | the tablespace usages. (USED(M) / MAX(M)) * 100. if MAX(M) is unlimited, it assumes that MAX(M) is MEM_MAX_DB_SIZE in altibase.properties. |

```
SELECT 	MEM_MAX_DB_SIZE/1024/1024 'MAX(M)',
        ROUND(MEM_ALLOC_PAGE_COUNT*32/1024, 2) 'TOTAL(M)',
        TRUNC((MEM_ALLOC_PAGE_COUNT-MEM_FREE_PAGE_COUNT)*32/1024, 2) 'ALLOC(M)',
        (SELECT ROUND(SUM((FIXED_USED_MEM + VAR_USED_MEM))/(1024*1024),3) FROM V$MEMTBL_INFO) 'USED(M)',
        TRUNC(((MEM_ALLOC_PAGE_COUNT-MEM_FREE_PAGE_COUNT)*32*1024)/MEM_MAX_DB_SIZE, 4)*100 'USAGE(%)'
FROM V$DATABASE ;
```

# Disk Tablespace Usage

This query returns the disk tablespace usage information.

| Columns | Description |
| --- | --- |
| TBS_ID | the unique identifier of the tablespace |
| TBS_TYPE | the type of the tablespace |
| TBS_NAME | the name of the tablespace |
| MAX(M) | the max size of the tablespace (Megabyte) |
| TOTAL(M) | the total size of the tablespace (Megabyte) |
| ALLOC(M) | allocated size of the tablespace (Megabyte) |
| AUTOEXTEND | whether the tablespace can be extended automatically |

## ALTIBASE HDB V4

```
SELECT 	ID TBS_ID,
        DECODE(TYPE, 1, 'DISK_SYS_DATA', 2, 'DISK_USER_DATA', 3, 'DISK_SYS_TEMP', 4, 'DISK_USER_TEMP', 5, 'DISK_UNDO') TBS_TYPE,
        NAME TBS_NAME,
        ROUND(D.MAX * PAGE_SIZE / 1024 /1024, 2) 'MAX(M)',
        ROUND(TOTAL_PAGE_COUNT * PAGE_SIZE / 1024 / 1024, 2) 'TOTAL(M)',
        ROUND(ALLOCATED_PAGE_COUNT * PAGE_SIZE / 1024 / 1024,2) 'ALLOC(M)',
        ROUND(ALLOCATED_PAGE_COUNT / D.MAX * 100, 2) 'USAGE(%)',
        D.AUTOEXTEND
FROM    V$TABLESPACES T,
        (
         SELECT 	SPACEID,
                  SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX,
                  DECODE(MAX(AUTOEXTEND),1,'ON','OFF') 'AUTOEXTEND'
         FROM V$DATAFILES
         GROUP BY SPACEID
         ) D
WHERE T.ID = D.SPACEID ;
```

## ALTIBASE HDB V5

```
SELECT 	ID TBS_ID,
        DECODE(TYPE, 3, 'DISK_SYS_DATA', 4, 'DISK_USER_DATA', 5, 'DISK_SYS_TEMP', 6, 'DISK_USER_TEMP', 7, 'DISK_UNDO') TBS_TYPE,
        NAME TBS_NAME,
        ROUND(D.MAX * PAGE_SIZE / 1024 /1024, 2) 'MAX(M)',
        ROUND(TOTAL_PAGE_COUNT * PAGE_SIZE / 1024 / 1024, 2) 'TOTAL(M)',
        DECODE(TYPE, 7, ROUND((SELECT (SUM(TOTAL_EXTENT_COUNT*PAGE_COUNT_IN_EXTENT) * PAGE_SIZE)/1024/1024 FROM V$UDSEGS)+(SELECT (SUM(TOTAL_EXTENT_COUNT*PAGE_COUNT_IN_EXTENT) * PAGE_SIZE)/1024/1024 FROM V$TSSEGS),2), ROUND(ALLOCATED_PAGE_COUNT * PAGE_SIZE / 1024 / 1024,2)) 'ALLOC(M)',
        DECODE(TYPE, 7, ROUND(((SELECT SUM(TOTAL_EXTENT_COUNT*PAGE_COUNT_IN_EXTENT) FROM V$UDSEGS)+(SELECT SUM(TOTAL_EXTENT_COUNT*PAGE_COUNT_IN_EXTENT) FROM V$TSSEGS)) / D.MAX* 100, 2), ROUND(ALLOCATED_PAGE_COUNT / D.MAX * 100, 2)) 'USAGE(%)', DECODE(STATE,1,'OFFLINE',2,'ONLINE',5,'OFFLINE BACKUP',6,'ONLINE BACKUP',128,'DROPPED', 'DISCARDED') STATE,
        D.AUTOEXTEND
FROM    V$TABLESPACES T,
        (
         SELECT 	SPACEID,
                  SUM(DECODE(MAXSIZE, 0, CURRSIZE, MAXSIZE)) AS MAX,
                  DECODE(MAX(AUTOEXTEND),1,'ON','OFF') 'AUTOEXTEND'
         FROM V$DATAFILES
         GROUP BY SPACEID
         ) D
WHERE T.ID = D.SPACEID ;
```

# The datafile information

This query returns the information about data files containing tablespaces.

| Columns | Description |
| --- | --- |
| TBS_NAME | the name of the tablespace |
| FILE# | the file number of datafiles containing the tablespace. It starts with 0. |
| DATAFILE_NAME | the name of the datafile |
| ALLOC(M) | allocated size of the datafile (Megabyte) |
| MAX(M) | the max size of the datafile (Megabyte) |
| AUTOEXTEND | can be extended automatically |

```
SELECT 	B.NAME TBS_NAME,
        A.ID 'FILE#',
        A.NAME DATAFILE_NAME,
        CURRSIZE*8/1024 'ALLOC(M)',
        ROUND(CASE2(A.MAXSIZE=0, CURRSIZE, A.MAXSIZE)*8/1024) 'MAX(M)',
        DECODE(AUTOEXTEND, 0, 'OFF', 'ON') 'AUTOEXTEND'
FROM    V$DATAFILES A,
        V$TABLESPACES B
WHERE   B.ID = A.SPACEID
ORDER BY B.NAME, A.ID ;
```

# I/O statistics of datafiles

This query returns I/O statistics for datafiles.

## ALTIBASE HDB V4

ALTIBASE HDB V4 does not support V$FILESTAT performance view to retrieve the I/O statistics of datafiles.

## ALTIBASE HDB V5

```
SELECT 	NAME TBS_NAME,
        A.PHYRDS PHY_READ,
        A.PHYWRTS PHY_WRITE,
        A.PHYRDS+A.PHYWRTS PHY_TOTAL,
        TRUNC(A.PHYRDS/READ_SUM*100,2) 'READ(%)',
        TRUNC(A.PHYWRTS/WRITE_SUM*100,2) 'WRITE(%)',
        TRUNC( (A.PHYRDS+A.PHYWRTS) / (READ_SUM+WRITE_SUM) * 100 , 2) 'TOTAL(%)',
        A.AVGIOTIM AVG_IO_TIME
FROM 	  V$FILESTAT A,
	      V$DATAFILES B,
	      (
	         	SELECT 	SUM(PHYRDS) READ_SUM,
	         					SUM(PHYWRTS) WRITE_SUM
	         	FROM V$FILESTAT
	      ) C
WHERE 	A.SPACEID = B.SPACEID
	   	  AND A.FILEID = B.ID
	   	  AND READ_SUM > 0
	   	  AND WRITE_SUM > 0
ORDER BY A.PHYRDS+A.PHYWRTS DESC, ROWNUM DESC ;
```
