---
title: "Table/Column Definition"
page_id: "22642961"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=22642961"
updated_at: "2025-10-20T15:43:03.000+0900"
version: 1
ancestors: ["Home", "08. Monitoring"]
labels: []
---

# Table/Column Definition
Source: https://docs.altibase.com/pages/viewpage.action?pageId=22642961
Updated: 2025-10-20T15:43:03.000+0900

- [Overview](#Table/ColumnDefinition-Overview) - [Table definition](#Table/ColumnDefinition-Tabledefinition) - [Column definition](#Table/ColumnDefinition-Columndefinition)

# Overview

---

This is a query required when creating user table and column definitions.

# Table definition

---

The table owner, table name, number of records, table creation date, and last DDL execution date information can be checked.

The number of records can be checked from Altibase 6.3.1, which added the performance view related to statistical information.

There are differences in the query statement for each version, so refer to the statement for each version.

**Altibase version 6.3.1 or later**

```

-- USER_NAME  : Table owner
-- TABLE_NAME : Table name
-- RECORD_CNT : Number of records. Statistical information must be collected from this information in order to see accurate information. '-' means a table that has never collected statistical information.
-- CREATED_DATE : Date of table creation
-- LAST_DDL_DATE : Date of last DDL execution

SELECT U.USER_NAME 'USER_NAME'
     , T.TABLE_NAME 'TABLE_NAME'
     , DECODE(D.NUM_ROW, NULL, '-', D.NUM_ROW) 'RECORD_CNT'              -- Number of records,'-' is a table that has never collected statistical information
     , TO_CHAR(T.CREATED, 'YYYY-MM-DD HH:MI:SS') 'CREATED_DATE'          -- Date of table creation
     , TO_CHAR(T.LAST_DDL_TIME, 'YYYY-MM-DD HH:MI:SS') 'LAST_DDL_DATE'   -- Date of last DDL execution
  FROM SYSTEM_.SYS_USERS_ U
     , SYSTEM_.SYS_TABLES_ T
       LEFT OUTER JOIN V$DBMS_STATS D ON D.TARGET_ID = T.TABLE_OID AND D.TYPE = 'T'
 WHERE U.USER_ID NOT IN (0, 1)  -- System user PUBLIC, except SYSTEM_
   AND T.TABLE_TYPE = 'T'  -- Table only
   AND U.USER_ID = T.USER_ID
;
```

**Altibase version 5.3.3 / 5.5.1 / 6.1.1**

```
-- USER_NAME  : Table owner
-- TABLE_NAME : Table name
-- CREATED_DATE : Date of table creation
-- LAST_DDL_DATE : Date of last DDL execution

SELECT U.USER_NAME 'USER_NAME'
     , T.TABLE_NAME 'TABLE_NAME'
     , TO_CHAR(T.CREATED, 'YYYY-MM-DD HH:MI:SS') 'CREATED_DATE'          -- Date of table creation
     , TO_CHAR(T.LAST_DDL_TIME, 'YYYY-MM-DD HH:MI:SS') 'LAST_DDL_DATE'   -- Date of last DDL execution
  FROM SYSTEM_.SYS_USERS_ U
     , SYSTEM_.SYS_TABLES_ T
 WHERE U.USER_ID NOT IN (0, 1)  -- System user PUBLIC, except SYSTEM_
   AND T.TABLE_TYPE = 'T'  -- Table only
   AND U.USER_ID = T.USER_ID
;
```

**Altibase version 4.3.9**

```
-- USER_NAME  : Table owner
-- TABLE_NAME : Table name

SELECT U.USER_NAME 'USER_NAME'
     , T.TABLE_NAME 'TABLE_NAME'
  FROM SYSTEM_.SYS_USERS_ U
     , SYSTEM_.SYS_TABLES_ T
 WHERE U.USER_ID NOT IN (0, 1)  -- System user PUBLIC, except SYSTEM_
   AND T.TABLE_TYPE = 'T'  -- Table only
   AND U.USER_ID = T.USER_ID
;
```

# Column definition

---

The column name, data type, size, NOT NULL, constraint information, and column order information can be checked.

There are differences in the query statement for each version, so refer to the statement for each version.

**Altibase version 6.3.1 or later**

```
-- USER_NAME : Owner name
-- TABLE_NAME : Table name
-- COLUMN_NAME : Column name
-- DATA_TYPE : Data type
-- COLUMN_SIZE : Column size
-- CONST_TYPE : Constraint type
-- CHECK_CONDITION : Condition of CHECK constraint
-- COLUMN_ORDER : Column order

SELECT U.USER_NAME 'USER_NAME'
     , T.TABLE_NAME 'TABLE_NAME'
     , C.COLUMN_NAME 'COLUMN_NAME'
     , DECODE(C.DATA_TYPE, 1, 'CHAR', 12, 'VARCHAR', -8, 'NCHAR', -9, 'NVARCHAR', 2, 'NUMERIC/DECIMAL', 6, 'FLOAT/NUMBER', 8, 'DOUBLE', 7, 'REAL', -5, 'BIGINT', 4, 'INTEGER', 5, 'SMALLINT', 9, 'DATE', 30, 'BLOB', 40, 'CLOB', 20001, 'BYTE', 20002, 'NIBBLE', -7, 'BIT', -100, 'VARBIT', 10003, 'GEOMETRY') 'DATA_TYPE'
     , DECODE(C.DATA_TYPE, 2, C.PRECISION||'.'||C.SCALE, 6, C.PRECISION||'.'||C.SCALE, C.PRECISION) COLUMN_SIZE
     , DECODE(CONST.CONSTRAINT_TYPE, 0, 'FK', 1, 'NOT NULL', 2, 'UNIQUE', 3, 'PK', 4, 'NULL', 5, 'TIMESTAMP', 6, 'LOCAL UNIQUE', 7, 'CHECK') CONST_TYPE
     , CONST.CHECK_CONDITION
     , C.COLUMN_ORDER 'COLUMN_ORDER'
  FROM SYSTEM_.SYS_USERS_ U
     , SYSTEM_.SYS_TABLES_ T
     , SYSTEM_.SYS_COLUMNS_ C
       LEFT OUTER JOIN system_.SYS_CONSTRAINT_COLUMNS_ CONST_COL ON CONST_COL.COLUMN_ID = C.COLUMN_ID
       LEFT OUTER JOIN SYSTEM_.SYS_CONSTRAINTS_ CONST ON CONST.CONSTRAINT_ID = CONST_COL.CONSTRAINT_ID
 WHERE U.USER_NAME NOT IN ('PUBLIC', 'SYSTEM_')
   AND T.TABLE_TYPE = 'T'
   AND U.USER_ID = T.USER_ID
   AND T.TABLE_ID = C.TABLE_ID
 ORDER BY U.USER_NAME, T.TABLE_NAME, C.COLUMN_ORDER
;
```

**Altibase version 4.3.9 / 5.3.3 / 5.5.1 / 6.1.1**

```
 -- USER_NAME : Name owner
-- TABLE_NAME : Table name
-- COLUMN_NAME : Column name
-- DATA_TYPE : Data type
-- COLUMN_SIZE : Column size
-- CONST_TYPE : Constraint type
-- COLUMN_ORDER : Column order

SELECT U.USER_NAME 'USER_NAME'
     , T.TABLE_NAME 'TABLE_NAME'
     , C.COLUMN_NAME 'COLUMN_NAME'
     , DECODE(C.DATA_TYPE, 1, 'CHAR', 12, 'VARCHAR', -8, 'NCHAR', -9, 'NVARCHAR', 2, 'NUMERIC/DECIMAL', 6, 'FLOAT/NUMBER', 8, 'DOUBLE', 7, 'REAL', -5, 'BIGINT', 4, 'INTEGER', 5, 'SMALLINT', 9, 'DATE', 30, 'BLOB', 40, 'CLOB', 20001, 'BYTE', 20002, 'NIBBLE', -7, 'BIT', -100, 'VARBIT', 10003, 'GEOMETRY') 'DATA_TYPE'
     , DECODE(C.DATA_TYPE, 2, C.PRECISION||'.'||C.SCALE, 6, C.PRECISION||'.'||C.SCALE, C.PRECISION) COLUMN_SIZE
     , DECODE(CONST.CONSTRAINT_TYPE, 0, 'FK', 1, 'NOT NULL', 2, 'UNIQUE', 3, 'PK', 4, 'NULL', 5, 'TIMESTAMP', 6, 'LOCAL UNIQUE', 7, 'CHECK') CONST_TYPE
     , C.COLUMN_ORDER 'COLUMN_ORDER'
  FROM SYSTEM_.SYS_USERS_ U
     , SYSTEM_.SYS_TABLES_ T
     , SYSTEM_.SYS_COLUMNS_ C
       LEFT OUTER JOIN system_.SYS_CONSTRAINT_COLUMNS_ CONST_COL ON CONST_COL.COLUMN_ID = C.COLUMN_ID
       LEFT OUTER JOIN SYSTEM_.SYS_CONSTRAINTS_ CONST ON CONST.CONSTRAINT_ID = CONST_COL.CONSTRAINT_ID
 WHERE U.USER_NAME NOT IN ('PUBLIC', 'SYSTEM_')
   AND T.TABLE_TYPE = 'T'
   AND U.USER_ID = T.USER_ID
   AND T.TABLE_ID = C.TABLE_ID
 ORDER BY U.USER_NAME, T.TABLE_NAME, C.COLUMN_ORDER
;
```
