---
title: "Memory table and index usage"
page_id: "16876259"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Memory+table+and+index+usage"
updated_at: "2021-04-05T10:30:52.000+0900"
version: 2
ancestors: ["Home", "08. Monitoring"]
labels: []
---

# Memory table and index usage
Source: https://docs.altibase.com/display/FAQE/Memory+table+and+index+usage
Updated: 2021-04-05T10:30:52.000+0900

- [Overview](#Memorytableandindexusage-Overview) - [Memory table data usage query](#Memorytableandindexusage-Memorytabledatausagequery) - [Memory table index usage](#Memorytableandindexusage-Memorytableindexusage) - [Query to check memory table index information (all available from HDB 4 to HDB 6)](#Memorytableandindexusage-Querytocheckmemorytableindexinformation(allavailablefromHDB4toHDB6)) - [Query to check usage per memory table index (available from HDB 5.x or later)](#Memorytableandindexusage-Querytocheckusagepermemorytableindex(availablefromHDB5.xorlater)) - [Query to check total index usage per memory table (available from HDB 5.x or later)](#Memorytableandindexusage-Querytochecktotalindexusagepermemorytable(availablefromHDB5.xorlater)) - [Query size per index of memory table (for 6.x)](#Memorytableandindexusage-Querysizeperindexofmemorytable(for6.x))

# Overview

---

This document describes the memory table and index usage query.

# Memory table data usage query

The following query can be used from HDB 4.3.9.x through HDB 6.3.1.x.

```
set linesize 2048;
set colsize 30;
SELECT   a.user_name
        ,NVL(d.name,'SYS_TBS_MEMORY')  AS 'TABLESPACE_NAME'
        , b.table_name
        , round((c.fixed_alloc_mem + c.var_alloc_mem)/(1024*1024),2) 'ALLOC(M)'
        , round((c.fixed_used_mem + c.var_used_mem)/(1024*1024),2) 'USED(M)'
        , round((c.fixed_used_mem + c.var_used_mem)/(c.fixed_alloc_mem + c.var_alloc_mem)*100,2) 'EFFICIENCY(%)'
FROM   system_.sys_users_ a
     , system_.sys_tables_ b
     , v$memtbl_info c left outer join v$tablespaces d  on c.tablespace_id = d.id
WHERE  b.table_type = 'T'
  and a.user_id = b.user_id
  and b.table_oid = c.table_oid
order by 1,2,3, 4 desc ;
```

**Example of output**

```
USER_NAME                       TABLESPACE_NAME                 TABLE_NAME                      TABLE_OID            ALLOC(M)    USED(M)     EFFICIENCY(%)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
SYS                             SYS_TBS_MEM_DATA                TEST_T2                         3323512              0.41        0.38        93.9
SYS                             USER_MEM_TBS                    MEM_T1                          3321192              0.03        0           0
SYSTEM_                         SYS_TBS_MEM_DIC                 STO_COLUMNS_                    1453416              0.03        0           0
SYSTEM_                         SYS_TBS_MEM_DIC                 STO_DATUMS_                     1469656              0.03        0           0
SYSTEM_                         SYS_TBS_MEM_DIC                 STO_ELLIPSOIDS_                 1471976              0.03        0           0

```

# Memory table index usage

---

The index usage of a memory table cannot be checked directly by a query. Altibase memory tables have a size of 16 bytes per index regardless of the number and type of index columns, and the index usage can be calculated as 16 bytes * number of records.

## Query to check memory table index information (all available from HDB 4 to HDB 6)

The index information for each table can be checked with the following query. To check the index size, the user must check the number of records and calculate it separately, or use a query that calculates the size of the index of the memory table containing the function.

```
set linesize 2048;
set colsize 30;

 SELECT
        c.user_name
        , decode(f.table_type, 'Q', 'QUEUE', 'T', 'TABLE') object_type
        , table_name object_name
        , e.index_name
        , rpad(case2(e.index_type=1, 'b-tree', 'r-tree'),10,' ') index_type
        , '16 bytes * rowcount' 'ALLOC'
 FROM      v$memtbl_info a
        ,  v$index b
        , system_.sys_users_ c
        , system_.sys_indices_ e
        , system_.sys_tables_ f
 WHERE
       a.table_oid = f.table_oid
   and b.index_id = e.index_id
   and e.user_id = c.user_id
   and f.user_id = e.user_id
   and f.tbs_id = a.tablespace_id
   and f.table_oid = b.table_oid
   and c.user_name <> 'SYSTEM_' ;
```

**Example of output**

```
USER_NAME                       OBJECT_TYPE  OBJECT_NAME                     INDEX_NAME                      INDEX_TYPE  ALLOC
-----------------------------------------------------------------------------------------------------------------------------------------------------
SYS                             TABLE  T1                              IDX1_T2                         b-tree      16 bytes * rowcount
SYS                             TABLE  T1                              IDX1_T1                         b-tree      16 bytes * rowcount
2 rows selected.
```

## Query to check usage per memory table index (available from HDB 5.x or later)

The user can use the following query to check usage per memory table index. Before using the query, the user must create a DB function that can get the number of records for that table.

```
1. Create a function that can count the number of records in the table.
CREATE FUNCTION GETCOUNT(u_name varchar(40), t_name varchar(40))
 RETURN INTEGER
 AS
    RECORDCOUNT integer;
BEGIN
       EXECUTE IMMEDIATE 'SELECT count(*)  FROM ' || u_name||'.'||t_name INTO RECORDCOUNT ;
RETURN RECORDCOUNT;

END;

/

2. Use function to query the usage per index.
set linesize 2048;
set colsize 30;
SELECT
        c.user_name
        , decode(f.table_type, 'Q', 'QUEUE', 'T', 'TABLE') object_type
        , table_name object_name
        , e.index_name
        , rpad(case2(e.index_type=1, 'b-tree', 'r-tree'),10,' ') index_type
        , ROUND( 16 * GETCOUNT(c.user_name, f.table_name) / 1024/1024, 2)  'ALLOC(M)'
 FROM      v$memtbl_info a
        ,  v$index b
        , system_.sys_users_ c
        , system_.sys_indices_ e
        , system_.sys_tables_ f
 WHERE
       a.table_oid = f.table_oid
   and b.index_id = e.index_id
   and e.user_id = c.user_id
   and f.user_id = e.user_id
   and f.tbs_id = a.tablespace_id
   and f.table_oid = b.table_oid
   and c.user_name <> 'SYSTEM_' ;
```

**Example of output**

```
USER_NAME                       OBJECT_TYPE  OBJECT_NAME                     INDEX_NAME                      INDEX_TYPE     ALLOC(M)
-----------------------------------------------------------------------------------------------------------------------------------------------
SYS                             TABLE  T1                              IDX1_T2                         b-tree         0.76
SYS                             TABLE  T1                              IDX1_T1                         b-tree         0.76
SYS                             TABLE  T2                              IDX2                            b-tree         0.31
3 rows selected.
```

## Query to check total index usage per memory table (available from HDB 5.x or later)

Query the total index usage per table used by the memory table. Before using the query, the user must create a DB function that can get the number of records for that table.

```
1. Create a function that can count the number of records in the table.
CREATE FUNCTION GETCOUNT(u_name varchar(40), t_name varchar(40))
 RETURN INTEGER
 AS
    RECORDCOUNT integer;
BEGIN
       EXECUTE IMMEDIATE 'SELECT count(*)  FROM ' || u_name||'.'||t_name INTO RECORDCOUNT ;
RETURN RECORDCOUNT;

END;

/

2. Use function to look up the total index usage size per table.
select
          user_name
        , table_name
        , count(index_name) AS 'INDEX_COUNT'
        , round( SUM(alloc) /1024/1024, 2 ) as 'Alloc(M)'
from (
         SELECT
                  c.user_name
                , f.table_name
                , e.index_name
                , 16 * GETCOUNT(c.user_name, f.table_name) AS alloc
         FROM      v$memtbl_info a
                ,  v$index b
                , system_.sys_users_ c
                , system_.sys_indices_ e
                , system_.sys_tables_ f
         WHERE
               a.table_oid = f.table_oid
           and b.index_id = e.index_id
           and e.user_id = c.user_id
           and f.user_id = e.user_id
           and f.tbs_id = a.tablespace_id
           and f.table_oid = b.table_oid
           and c.user_name <> 'SYSTEM_'
     )
 group by user_name, table_name;
```

```
 USER_NAME                       TABLE_NAME                      INDEX_COUNT          Alloc(M)
------------------------------------------------------------------------------------------------------
SYS                             T1                              2                    1.53
SYS                             T2                              1                    0.31
2 rows selected.
iSQL>
```

## Query size per index of memory table (for 6.x)

The user can query more accurate memory table usage per index with the following query. Available in version 6.1.1 or later.

```
SELECT U.USER_NAME, T.TABLE_NAME TABLE_NAME
     , B.INDEX_NAME
     , LPAD(I.IS_PARTITIONED, 14) INDEX_PARTITIONED
     , ROUND(((USED_NODE_COUNT+ PREPARE_NODE_COUNT) / 15 * 32768)/1024/1024, 1) AS 'SIZE(MB)'
  FROM V$MEM_BTREE_HEADER B
     , SYSTEM_.SYS_INDICES_ I
     , SYSTEM_.SYS_TABLES_ T
     , SYSTEM_.SYS_USERS_ U
 WHERE 1=1
   AND B.INDEX_ID = I.INDEX_ID
   AND I.TABLE_ID = T.TABLE_ID
   AND B.INDEX_TBS_ID <> 0
   AND U.USER_ID = T.USER_ID
 ORDER BY TABLE_NAME, B.INDEX_ID
;
```

**Example of output**

```
USER_NAME             TABLE_NAME            INDEX_NAME            INDEX_PARTITIONED     SIZE(MB)
----------------------------------------------------------------------------------------------------------
SYS                   EMPLOYEES             __SYS_IDX_ID_143                   F        0
SYS                   EMPLOYEES             EMP_IDX1                           F        0
SYS                   FOO                   __SYS_IDX_ID_171                   F        0
SYS                   GOODS                 __SYS_IDX_ID_145                   F        0
SYS                   GOODS                 __SYS_IDX_ID_146                   F        0
SYS                   MEM_T                 M_IDX01                            F        36.5
SYS                   M_PART_SALES          M_IDX_PREFIX                       T        0
SYS                   M_PART_SALES          IDX_PART_1                         T        8.7
SYS                   M_PART_SALES          IDX_PART_2                         T        0.7
SYS                   M_PART_SALES          IDX_PART_3                         T        0.7
```
