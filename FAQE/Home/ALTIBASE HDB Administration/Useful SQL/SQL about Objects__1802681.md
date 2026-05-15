---
title: "SQL about Objects"
page_id: "1802681"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/SQL+about+Objects"
updated_at: "2011-07-22T16:25:44.000+0900"
version: 8
ancestors: ["Home", "ALTIBASE HDB Administration", "Useful SQL"]
labels: []
---

# SQL about Objects
Source: https://docs.altibase.com/display/FAQE/SQL+about+Objects
Updated: 2011-07-22T16:25:44.000+0900

- [Memory Table](#SQLaboutObjects-MemoryTable)
    - [ALTIBASE HDB V4](#SQLaboutObjects-ALTIBASEHDBV4)
    - [ALTIBASE HDB V5](#SQLaboutObjects-ALTIBASEHDBV5)
- [Queue Table](#SQLaboutObjects-QueueTable)
    - [ALTIBASE HDB V4](#SQLaboutObjects-ALTIBASEHDBV4.1)
    - [ALTIBASE HDB V5](#SQLaboutObjects-ALTIBASEHDBV5.1)
- [Memory table / Queue table Index information](#SQLaboutObjects-Memorytable/QueuetableIndexinformation)
    - [ALTIBASE HDB V4](#SQLaboutObjects-ALTIBASEHDBV4.2)
    - [ALTIBASE HDB V5](#SQLaboutObjects-ALTIBASEHDBV5.2)
- [Disk Table](#SQLaboutObjects-DiskTable)
- [Disk Index](#SQLaboutObjects-DiskIndex)
    - [ALTIBASE HDB V4](#SQLaboutObjects-ALTIBASEHDBV4.3)
    - [ALTIBASE HDB V5](#SQLaboutObjects-ALTIBASEHDBV5.3)
- [Sequence](#SQLaboutObjects-Sequence)
- [Synonym](#SQLaboutObjects-Synonym)
    - [ALTIBASE HDB V4](#SQLaboutObjects-ALTIBASEHDBV4.4)
    - [ALTIBASE HDB V5](#SQLaboutObjects-ALTIBASEHDBV5.4)
- [PSM (Stored Procedures / Function / Typeset)](#SQLaboutObjects-PSM(StoredProcedures/Function/Typeset))
    - [ALTIBASE HDB V4](#SQLaboutObjects-ALTIBASEHDBV4.5)
    - [ALTIBASE HDB V5](#SQLaboutObjects-ALTIBASEHDBV5.5)
- [View](#SQLaboutObjects-View)
    - [ALTIBASE HDB V4](#SQLaboutObjects-ALTIBASEHDBV4.6)
    - [ALTIBASE HDB V5](#SQLaboutObjects-ALTIBASEHDBV5.6)
- [System Privileges](#SQLaboutObjects-SystemPrivileges)
- [Object Privileges](#SQLaboutObjects-ObjectPrivileges)
- [Constraint list](#SQLaboutObjects-Constraintlist)
- [Primary Key, Foreign Key, Unique Constraint](#SQLaboutObjects-PrimaryKey,ForeignKey,UniqueConstraint)
- [Index column list](#SQLaboutObjects-Indexcolumnlist)
- [Index information](#SQLaboutObjects-Indexinformation)

# Memory Table

This query returns the object information about a memory table.

| Column Name | Description |
| --- | --- |
| USER_NAME | the object owner |
| TABLE_NAME | the object name |
| TABLESPACE_NAME | the tablespace name which this object belongs to |
| TABLE_OID | the table object identifier |
| ALLOC(M) | allocated size of the memory table (Megabyte) |
| USED(M) | actually used size of the memory table (Megabyte) |
| EFFICIENCY(%) | store efficiency of the object |

## ALTIBASE HDB V4

```
SELECT  A.USER_NAME,
        B.TABLE_NAME,
        'SYS_TBS_MEMORY' TABLESPACE_NAME,
        C.TABLE_OID,
        ROUND((C.FIXED_ALLOC_MEM + C.VAR_ALLOC_MEM)/(1024*1024),2) 'ALLOC(M)',
        ROUND((C.FIXED_USED_MEM + C.VAR_USED_MEM)/(1024*1024),2) 'USED(M)',
        ROUND((C.FIXED_USED_MEM + C.VAR_USED_MEM)/(C.FIXED_ALLOC_MEM + C.VAR_ALLOC_MEM)*100,2) 'EFFICIENCY(%)'
FROM    SYSTEM_.SYS_USERS_ A,
        SYSTEM_.SYS_TABLES_ B,
        V$MEMTBL_INFO C
WHERE   A.USER_NAME <> 'SYSTEM_'
        AND B.TABLE_TYPE = 'T'
        AND A.USER_ID = B.USER_ID
        AND B.TABLE_OID = C.TABLE_OID;
```

## ALTIBASE HDB V5

```
SELECT  A.USER_NAME,
        B.TABLE_NAME,
        D.NAME TABLESPACE_NAME,
        C.TABLE_OID,
        ROUND((C.FIXED_ALLOC_MEM + C.VAR_ALLOC_MEM)/(1024*1024),2) 'ALLOC(M)',
        ROUND((C.FIXED_USED_MEM + C.VAR_USED_MEM)/(1024*1024),2) 'USED(M)',
        ROUND((C.FIXED_USED_MEM + C.VAR_USED_MEM)/(C.FIXED_ALLOC_MEM + C.VAR_ALLOC_MEM)*100,2) 'EFFICIENCY(%)'
FROM    SYSTEM_.SYS_USERS_ A,
        SYSTEM_.SYS_TABLES_ B,
        V$MEMTBL_INFO C,
        V$TABLESPACES D
WHERE   A.USER_NAME <> 'SYSTEM_'
        AND B.TABLE_TYPE = 'T'
        AND A.USER_ID = B.USER_ID
        AND B.TABLE_OID = C.TABLE_OID
        AND B.TBS_ID = D.ID ;
```

# Queue Table

This query returns the object information about a queue table.

| Column Name | Description |
| --- | --- |
| USER_NAME | the object owner |
| TABLE_NAME | the object name |
| TABLESPACE_NAME | the tablespace name which this object belongs to |
| TABLE_OID | the table object identifier |
| ALLOC(M) | allocated size of the memory table (Megabyte) |
| USED(M) | actually used size of the memory table (Megabyte) |
| EFFICIENCY(%) | store efficiency of the object |

Queue table structure is the same as a memory table except its functionality.

## ALTIBASE HDB V4

```
SELECT  A.USER_NAME,
        B.TABLE_NAME,
        'SYS_TBS_MEMORY' TABLESPACE_NAME,
        C.TABLE_OID,
        ROUND((C.FIXED_ALLOC_MEM + C.VAR_ALLOC_MEM)/(1024*1024),2) 'ALLOC(M)',
        ROUND((C.FIXED_USED_MEM + C.VAR_USED_MEM)/(1024*1024),2) 'USED(M)',
        ROUND((C.FIXED_USED_MEM + C.VAR_USED_MEM)/(C.FIXED_ALLOC_MEM + C.VAR_ALLOC_MEM)*100,2) 'EFFICIENCY(%)'
FROM    SYSTEM_.SYS_USERS_ A,
        SYSTEM_.SYS_TABLES_ B,
        V$MEMTBL_INFO C
WHERE   A.USER_NAME <> 'SYSTEM_'
        AND B.TABLE_TYPE = 'Q'
        AND A.USER_ID = B.USER_ID
        AND B.TABLE_OID = C.TABLE_OID;
```

## ALTIBASE HDB V5

```
SELECT  A.USER_NAME,
        B.TABLE_NAME,
        D.NAME TABLESPACE_NAME,
        C.TABLE_OID,
        ROUND((C.FIXED_ALLOC_MEM + C.VAR_ALLOC_MEM)/(1024*1024),2) 'ALLOC(M)',
        ROUND((C.FIXED_USED_MEM + C.VAR_USED_MEM)/(1024*1024),2) 'USED(M)',
        ROUND((C.FIXED_USED_MEM + C.VAR_USED_MEM)/(C.FIXED_ALLOC_MEM + C.VAR_ALLOC_MEM)*100,2) 'EFFICIENCY(%)'
FROM    SYSTEM_.SYS_USERS_ A,
        SYSTEM_.SYS_TABLES_ B,
        V$MEMTBL_INFO C,
        V$TABLESPACES D
WHERE   A.USER_NAME <> 'SYSTEM_'
        AND B.TABLE_TYPE = 'Q'
        AND A.USER_ID = B.USER_ID
        AND B.TABLE_OID = C.TABLE_OID
        AND B.TBS_ID = D.ID ;
```

# Memory table / Queue table Index information

This query returns the index information of a memory table and a queue object.

| Column Name | Description |
| --- | --- |
| USER_NAME | the object owner |
| OBJECT_TYPE | the type of object |
| OBJECT_NAME | the object name |
| TABLESPACE_NAME | the tablespace name which this object belongs to |
| INDEX_NAME | the table object identifier |
| INDEX_TYPE | the table object identifier |

Estimating of memory index is very simple in most cases. ALTIBASE HDB index just consists of pointers, thus you just multiply 16 bytes by the number of table rows to get the size of each index.

## ALTIBASE HDB V4

```
SELECT  C.USER_NAME,
        DECODE(F.TABLE_TYPE, 'Q', 'QUEUE', 'T', 'TABLE') OBJECT_TYPE,
        TABLE_NAME OBJECT_NAME,
        'SYS_TBS_MEMORY' TABLESPACE_NAME,
        E.INDEX_NAME,
        RPAD(CASE2(E.INDEX_TYPE=1, 'B-TREE', 'R-TREE'),10,' ') INDEX_TYPE
FROM    V$INDEX B,
        SYSTEM_.SYS_USERS_ C,
        SYSTEM_.SYS_INDICES_ E,
        SYSTEM_.SYS_TABLES_ F
WHERE   B.INDEX_ID = E.INDEX_ID
        AND E.USER_ID = C.USER_ID
        AND F.USER_ID = E.USER_ID
        AND F.TABLE_OID = B.TABLE_OID
        AND C.USER_NAME <> 'SYSTEM_';
```

## ALTIBASE HDB V5

```
SELECT  C.USER_NAME,
        DECODE(F.TABLE_TYPE, 'Q', 'QUEUE', 'T', 'TABLE') OBJECT_TYPE,
        TABLE_NAME OBJECT_NAME,
        D.SPACE_NAME TABLESPACE_NAME,
        E.INDEX_NAME,
        RPAD(CASE2(E.INDEX_TYPE=1, 'B-TREE', 'R-TREE'),10,' ') INDEX_TYPE
FROM    V$INDEX B,
        SYSTEM_.SYS_USERS_ C,
        V$MEM_TABLESPACES D,
        SYSTEM_.SYS_INDICES_ E,
        SYSTEM_.SYS_TABLES_ F
WHERE   B.INDEX_ID = E.INDEX_ID
        AND E.USER_ID = C.USER_ID
        AND F.USER_ID = E.USER_ID
        AND F.TBS_ID = D.SPACE_ID
        AND F.TABLE_OID = B.TABLE_OID
        AND C.USER_NAME <> 'SYSTEM_';
```

# Disk Table

This query returns the object information about a disk table.

| Column Name | Description |
| --- | --- |
| USER_NAME | the object owner |
| TABLE_NAME | the object name |
| TABLESPACE_NAME | the tablespace name which this object belongs to |
| TABLE_OID | the table object identifier |
| ALLOC(M) | allocated size of the memory table (Megabyte) |

```
SELECT  USER_NAME,
        A.TABLE_NAME,
        D.NAME TBS_NAME,
        A.TABLE_OID,
        ROUND((B.DISK_PAGE_CNT*8)/1024) 'ALLOC(M)'
FROM    SYSTEM_.SYS_TABLES_ A,
        V$DISKTBL_INFO B,
        SYSTEM_.SYS_USERS_ C,
        V$TABLESPACES D
WHERE   A.TABLE_OID = B.TABLE_OID
        AND A.USER_ID = C.USER_ID
        AND A.TBS_ID=D.ID
        AND C.USER_NAME <> 'SYSTEM_';
```

# Disk Index

This query returns the object information about a disk index.

| Column Name | Description |
| --- | --- |
| USER_NAME | the object owner |
| TABLE_NAME | the object name |
| TBS_NAME | the tablespace name which this object belongs to |
| INDEX_NAME | the name of index |
| INDEX_TYPE | the type of index |
| ALLOC(M) | allocated size of the memory table (Megabyte) |

## ALTIBASE HDB V4

```
SELECT  USER_NAME,
        TABLE_NAME,
        D.NAME TBS_NAME,
        E.INDEX_NAME,
        RPAD(CASE2(E.INDEX_TYPE=1,'B-TREE', 'R-TREE'),10,' ') INDEX_TYPE,
        ROUND(D.A_EXTENT_PAGE_COUNT*D.PAGE_SIZE*A.EXTENT_TOTAL_COUNT/1024/1024) 'ALLOC(M)'
FROM    V$SEGMENT A,
        V$INDEX B,
        V$TABLESPACES D,
        SYSTEM_.SYS_USERS_ C,
        SYSTEM_.SYS_INDICES_ E,
        SYSTEM_.SYS_TABLES_ F
WHERE   A.SEGMENT_DESC = B.INDEX_SEG_DESC
        AND B.INDEX_ID = E.INDEX_ID
        AND E.USER_ID = C.USER_ID
        AND A.SPACE_ID = D.ID
        AND F.TBS_ID = D.ID
        AND A.SEGMENT_TYPE='INDEX'
        AND F.USER_ID = E.USER_ID
        AND F.TABLE_OID = B.TABLE_OID ;
```

## ALTIBASE HDB V5

```
SELECT  USER_NAME,
        TABLE_NAME,
        D.NAME TBS_NAME,
        E.INDEX_NAME,
        RPAD(CASE2(E.INDEX_TYPE=1,'B-TREE', 'R-TREE'),10,' ') INDEX_TYPE,
        ROUND(D.EXTENT_PAGE_COUNT*D.PAGE_SIZE*A.EXTENT_TOTAL_COUNT/1024/1024) 'ALLOC(M)'
FROM    V$SEGMENT A,
        V$INDEX B,
        V$TABLESPACES D,
        SYSTEM_.SYS_USERS_ C,
        SYSTEM_.SYS_INDICES_ E,
        SYSTEM_.SYS_TABLES_ F
WHERE   A.SEGMENT_PID = B.INDEX_SEG_PID
        AND B.INDEX_ID = E.INDEX_ID
        AND E.USER_ID = C.USER_ID
        AND A.SPACE_ID = D.ID
        AND F.TBS_ID = D.ID
        AND A.SEGMENT_TYPE='INDEX'
        AND F.USER_ID = E.USER_ID
        AND F.TABLE_OID = B.TABLE_OID ;
```

# Sequence

This query returns the object information about a sequence.

| Column Name | Description |
| --- | --- |
| USER_NAME | the object owner |
| SEQ_NAME | the object name |
| MIN | the minimum value of the sequence |
| CURRENT_SEQ | the current value of the sequence |
| MAX | the maximum value of the sequence |
| INCREMENT | increment property of the sequence |
| IS_CYCLE | can be cycled |
| CACHE | the cache size of the sequence |

```
SELECT  USER_NAME,
        TABLE_NAME SEQ_NAME,
        MIN_SEQ MIN,
        CURRENT_SEQ,
        MAX_SEQ MAX,
        INCREMENT_SEQ INCREMENT,
        IS_CYCLE,
        CACHE_SIZE CACHE
FROM    V$SEQ A,
        SYSTEM_.SYS_USERS_ B,
        SYSTEM_.SYS_TABLES_ C
WHERE   A.SEQ_OID = C.TABLE_OID
        AND B.USER_ID = C.USER_ID
        AND B.USER_NAME <> 'SYSTEM_' ;
```

# Synonym

This query returns the object information about a synonym.

| Column Name | Description |
| --- | --- |
| SYNONYM_OWNER | the object owner |
| SYNONYM_NAME | the object name |
| OBJECT_OWNER | the minimum value of the sequence |
| OBJECT_NAME | the current value of the sequence |
| LAST_DDL_TIME | the last DDL occured time |

## ALTIBASE HDB V4

```
SELECT  NVL(USER_NAME, 'PUBLIC') SYNONYM_OWNER,
        SYNONYM_NAME,
        SCHEMA_NAME OBJECT_OWNER,
        OBJECT_NAME
FROM    SYSTEM_.SYS_SYNONYMS_ A LEFT OUTER JOIN
        SYSTEM_.SYS_USERS_ B ON A.USER_ID = B.USER_ID
WHERE
				A.SCHEMA_NAME != 'SYSTEM_' ;
```

## ALTIBASE HDB V5

```
SELECT  NVL(USER_NAME, 'PUBLIC') SYNONYM_OWNER,
        SYNONYM_NAME,
        OBJECT_OWNER_NAME OBJECT_OWNER,
        OBJECT_NAME,
        TO_CHAR(A.LAST_DDL_TIME, 'YYYY-MM-DD HH:MI:SS') LAST_DDL_TIME
FROM    SYSTEM_.SYS_SYNONYMS_ A LEFT OUTER JOIN
        SYSTEM_.SYS_USERS_ B ON A.SYNONYM_OWNER_ID = B.USER_ID
WHERE   OBJECT_OWNER_NAME <> 'SYSTEM_' ;
```

# PSM (Stored Procedures / Function / Typeset)

This query returns the object information about a PSM.

| Column Name | Description |
| --- | --- |
| USER_NAME | the object owner |
| PSM_TYPE | the type of PSM |
| PSM_NAME | the name of PSM |
| STATUS | the status of PSM |
| LAST_DDL_TIME | the last DDL occured time |

## ALTIBASE HDB V4

```
SELECT  A.USER_NAME,
        DECODE(OBJECT_TYPE, 0, 'PROCEDURE', 1, 'FUNCTION', 3, 'TYPESET') PSM_TYPE,
        PROC_NAME PSM_NAME,
        DECODE(STATUS, 0, 'VALID', 'INVALID') STATUS
FROM    SYSTEM_.SYS_USERS_ A,
        SYSTEM_.SYS_PROCEDURES_ B
WHERE A.USER_ID = B.USER_ID AND A.USER_NAME <> 'SYSTEM_' ;
```

## ALTIBASE HDB V5

```
SELECT  A.USER_NAME,
        DECODE(OBJECT_TYPE, 0, 'PROCEDURE', 1, 'FUNCTION', 3, 'TYPESET') PSM_TYPE,
        PROC_NAME PSM_NAME,
        DECODE(STATUS, 0, 'VALID', 'INVALID') STATUS,
        TO_CHAR(B.LAST_DDL_TIME, 'YYYY-MM-DD HH:MI:SS') LAST_DDL_TIME
FROM    SYSTEM_.SYS_USERS_ A,
        SYSTEM_.SYS_PROCEDURES_ B
WHERE A.USER_ID = B.USER_ID AND A.USER_NAME <> 'SYSTEM_' ;
```

# View

This query returns the object information about a view.

| Column Name | Description |
| --- | --- |
| USER_NAME | the object owner |
| VIEW_NAME | the type of PSM |
| STATUS | the status of PSM |
| LAST_DDL_TIME | the last DDL occured time |

## ALTIBASE HDB V4

```
SELECT  A.USER_NAME,
        B.TABLE_NAME VIEW_NAME,
        DECODE(STATUS, 0, 'VALID', 'INVALID') STATUS
FROM    SYSTEM_.SYS_USERS_ A,
        SYSTEM_.SYS_TABLES_ B,
        SYSTEM_.SYS_VIEWS_ C
WHERE   A.USER_ID = B.USER_ID
        AND B.TABLE_ID = C.VIEW_ID
        AND B.TABLE_TYPE = 'V' ;
```

## ALTIBASE HDB V5

```
SELECT  A.USER_NAME,
        B.TABLE_NAME VIEW_NAME,
        DECODE(STATUS, 0, 'VALID', 'INVALID') STATUS,
        TO_CHAR(B.LAST_DDL_TIME, 'YYYY-MM-DD HH:MI:SS') LAST_DDL_TIME
FROM    SYSTEM_.SYS_USERS_ A,
        SYSTEM_.SYS_TABLES_ B,
        SYSTEM_.SYS_VIEWS_ C
WHERE   A.USER_ID = B.USER_ID
        AND B.TABLE_ID = C.VIEW_ID
        AND B.TABLE_TYPE = 'V' ;
```

# System Privileges

This query returns the object information about system privileges.

| Column Name | Description |
| --- | --- |
| GRANTEE | the grantee |
| GRANTOR | the granter |
| PRIV_NAME | the name of privilege |

```
SELECT  A.USER_NAME GRANTEE,
        C.USER_NAME GRANTOR,
        REPLACE(D.PRIV_NAME, '_', ' ') PRIV_NAME
FROM    SYSTEM_.SYS_USERS_ A,
        SYSTEM_.SYS_GRANT_SYSTEM_ B,
        SYSTEM_.SYS_USERS_ C,
        SYSTEM_.SYS_PRIVILEGES_ D
WHERE   C.USER_NAME <> 'SYSTEM_'
        AND B.GRANTEE_ID = A.USER_ID
        AND B.GRANTOR_ID = C.USER_ID
        AND B.PRIV_ID = D.PRIV_ID ;
```

# Object Privileges

This query returns the information about object privileges.

| Column Name | Description |
| --- | --- |
| GRANTEE | the grantee |
| GRANTOR | the granter |
| OBJECT_OWNER | the object owner |
| OBJECT_NAME | the object name |
| OBJECT_TYPE | the object type |
| PRIV_NAME | the name of privilege |
| GRANTABLE | is grant-able |

```
SELECT  A.USER_NAME GRANTEE,
        C.USER_NAME GRANTOR,
        F.USER_NAME OBJECT_OWNER,
        E.TABLE_NAME OBJECT_NAME,
        E.TABLE_TYPE OBJECT_TYPE,
        REPLACE(D.PRIV_NAME, '_', ' ') PRIV_NAME,
        DECODE(B.WITH_GRANT_OPTION, 0, 'NO', 'YES') GRANTABLE
FROM    SYSTEM_.SYS_USERS_ A,
        SYSTEM_.SYS_GRANT_OBJECT_ B,
        SYSTEM_.SYS_USERS_ C,
        SYSTEM_.SYS_PRIVILEGES_ D,
        SYSTEM_.SYS_TABLES_ E,
        SYSTEM_.SYS_USERS_ F
WHERE   C.USER_NAME <> 'SYSTEM_'
        AND B.GRANTEE_ID = A.USER_ID
        AND B.GRANTOR_ID = C.USER_ID
        AND B.PRIV_ID = D.PRIV_ID
        AND B.OBJ_ID = E.TABLE_ID
        AND E.USER_ID = F.USER_ID
ORDER BY GRANTEE, GRANTOR, OBJECT_OWNER, OBJECT_TYPE, OBJECT_NAME, PRIV_NAME ;
```

# Constraint list

This query returns the information about object constraints.

| Column Name | Description |
| --- | --- |
| USER_NAME | the object owner |
| OBJECT_NAME | the object name |
| OBJECT_TYPE | the object type |
| CONST_NAME | the constraint name |
| CONST_type | the constraint type |
| COLUMN_NAME | the column name |

```
SELECT  USER_NAME,
        TABLE_NAME OBJECT_NAME,
        DECODE(B.TABLE_TYPE, 'T', 'TABLE', 'Q', 'QUEUE', 'V', 'VIEW', 'SEQUENCE') OBJECT_TYPE,
        C.CONSTRAINT_NAME CONST_NAME,
        DECODE(C.CONSTRAINT_TYPE,0, 'FK', 1, 'NOT NULL', 2, 'UNIQUE', 3, 'PK', 4, 'NULL', 5, 'TIMESTAMP', 6, 'LOCAL UNIQUE') CONST_TYPE,
        COLUMN_NAME
FROM    SYSTEM_.SYS_USERS_ A,
        SYSTEM_.SYS_TABLES_ B,
        SYSTEM_.SYS_CONSTRAINTS_ C,
        SYSTEM_.SYS_COLUMNS_ D,
        SYSTEM_.SYS_CONSTRAINT_COLUMNS_ E
WHERE   A.USER_ID=C.USER_ID
        AND B.TABLE_ID = C.TABLE_ID
        AND A.USER_ID = D.USER_ID
        AND A.USER_ID = E.USER_ID
        AND B.TABLE_ID = D.TABLE_ID
        AND B.TABLE_ID = E.TABLE_ID
        AND C.CONSTRAINT_ID = E.CONSTRAINT_ID
        AND D.COLUMN_ID = E.COLUMN_ID
        AND A.USER_NAME <> 'SYSTEM_' ;
```

# Primary Key, Foreign Key, Unique Constraint

This query returns the information about object constraints.

| Column Name | Description |
| --- | --- |
| USER_NAME | the object owner |
| TABLE_NAME | the table name |
| CONST_TYPE | the constraint type |
| CONST_NAME | the constraint name |
| INDEX_NAME | the index name |
| R_TABLE | the referenced table |
| R_INDEX | the referenced index |

```
SELECT  A.USER_NAME,
        B.TABLE_NAME,
        DECODE(C.CONSTRAINT_TYPE,0, 'FK', 2, 'UNIQUE', 3, 'PK', 4, 'NULL') CONST_TYPE,
        C.CONSTRAINT_NAME CONST_NAME,
        DECODE(D.INDEX_NAME,C.CONSTRAINT_NAME,NULL,INDEX_NAME) INDEX_NAME,
        (SELECT TABLE_NAME FROM SYSTEM_.SYS_TABLES_ WHERE TABLE_ID = C.REFERENCED_TABLE_ID) R_TABLE,
        (SELECT INDEX_NAME FROM SYSTEM_.SYS_INDICES_ WHERE INDEX_ID = C.REFERENCED_INDEX_ID) R_INDEX
FROM     SYSTEM_.SYS_USERS_ A,
         SYSTEM_.SYS_TABLES_ B,
         SYSTEM_.SYS_CONSTRAINTS_ C LEFT OUTER JOIN
         SYSTEM_.SYS_INDICES_ D ON C.INDEX_ID = D.INDEX_ID
WHERE    C.TABLE_ID = B.TABLE_ID
         AND A.USER_NAME <> 'SYSTEM_'
         AND C.USER_ID = A.USER_ID
         AND C.CONSTRAINT_TYPE IN (3, 0, 2, 6) --PK, FK, UNIQUE, LOCAL UNIQUE
ORDER BY TABLE_NAME, CONST_TYPE ;
```

# Index column list

This query returns the information about index columns.

| Column Name | Description |
| --- | --- |
| USER_NAME | the object owner |
| TABLE_NAME | the table name |
| INDEX_NAME | the index name |
| COLUMN_NAME | the column name |
| COL_ORDER | column order (when composite index) |

```
SELECT  D.USER_NAME,
        C.TABLE_NAME,
        B.INDEX_NAME,
        E.COLUMN_NAME,
        A.INDEX_COL_ORDER COL_ORDER,
        DECODE(A.SORT_ORDER, 'A', 'ASC', 'D', 'DESC') SORT
FROM    SYSTEM_.SYS_INDEX_COLUMNS_ A,
        SYSTEM_.SYS_INDICES_ B,
        SYSTEM_.SYS_TABLES_ C,
        SYSTEM_.SYS_USERS_ D,
        SYSTEM_.SYS_COLUMNS_ E
WHERE   D.USER_NAME <> 'SYSTEM_'
        AND C.TABLE_TYPE = 'T'
        AND A.INDEX_ID = B.INDEX_ID
        AND A.TABLE_ID = C.TABLE_ID
        AND A.USER_ID = D.USER_ID
        AND A.COLUMN_ID = E.COLUMN_ID
ORDER BY USER_NAME, TABLE_NAME, INDEX_NAME, COL_ORDER ;
```

# Index information

This query returns the information about an index.

| Column Name | Description |
| --- | --- |
| USER_NAME | the object owner |
| INDEX_NAME | the index name |
| INDEX_ID | the index name |
| TABLE_NAME | the table name |
| TBS_NAME | the tablespace which this object belongs to |
| IS_UNIQUE | unique index or not |
| COLUMN_CNT | the number of columns |

```
SELECT  A.USER_NAME,
        C.INDEX_NAME,
        C.INDEX_ID,
        B.TABLE_NAME,
        NVL(D.NAME, 'SYS_TBS_MEMORY') TBS_NAME,
        C.IS_UNIQUE,
        C.COLUMN_CNT
FROM    SYSTEM_.SYS_USERS_ A,
        SYSTEM_.SYS_TABLES_ B,
        SYSTEM_.SYS_INDICES_ C LEFT OUTER JOIN
        V$TABLESPACES D ON C.TBS_ID = D.ID
WHERE   A.USER_NAME <> 'SYSTEM_'
        AND B.TABLE_TYPE = 'T'
        AND C.TABLE_ID = B.TABLE_ID
        AND C.USER_ID = A.USER_ID
ORDER BY B.TABLE_NAME, C.INDEX_NAME ;
```
