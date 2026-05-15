---
title: "ERR-31283 Unable to create a primary key or a unique key constraint in the local non-prefixed index"
page_id: "6979844"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-31283+Unable+to+create+a+primary+key+or+a+unique+key+constraint+in+the+local+non-prefixed+index"
updated_at: "2014-11-20T10:40:32.000+0900"
version: 14
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-31283 Unable to create a primary key or a unique key constraint in the local non-prefixed index
Source: https://docs.altibase.com/display/FAQE/ERR-31283+Unable+to+create+a+primary+key+or+a+unique+key+constraint+in+the+local+non-prefixed+index
Updated: 2014-11-20T10:40:32.000+0900

- [Version](#ERR-31283Unabletocreateaprimarykeyorauniquekeyconstraintinthelocalnon-prefixedindex-Version)
- [Explanation](#ERR-31283Unabletocreateaprimarykeyorauniquekeyconstraintinthelocalnon-prefixedindex-Explanation)
- [Cause](#ERR-31283Unabletocreateaprimarykeyorauniquekeyconstraintinthelocalnon-prefixedindex-Cause)
- [Action](#ERR-31283Unabletocreateaprimarykeyorauniquekeyconstraintinthelocalnon-prefixedindex-Action)
- [Reference](#ERR-31283Unabletocreateaprimarykeyorauniquekeyconstraintinthelocalnon-prefixedindex-Reference)

## Version

6.1.1 or below

## Explanation

Unable to create a non-prefixed index on a partitioned table using the primary key or unique key.

This error message is output when a user tries to create a primary key or a unique key constraint in the local non-prefixed index.

## Cause

The following error description can be viewed with the AltiErr utility:

$ altierr 0x31283

0x31283 ( 201347) qpERR_ABORT_QDX_NOT_ALLOWED_PRIMARY_AND_UNIQUE_KEY_OF_NONE_PREFIXED_INDEX Unable to create a primary key or a unique key constraint in the local non-prefixed index.

# - The user tried to create a primary key or a unique key constraint in the local prefixed index.

# *Action:

# - Please do not create a primary key or a unique key constraint in the local non-prefixed index.

The global index is not supported for ALTIBASE HDB 6.1.1 or below.

Therefore, all partitioned indexes are local indexes and local non-prefixed indexes cannot be created for the primary key or unique index.

This is because even if a column value ​​within a particular partition is unique, its uniqueness within a table cannot be guaranteed.

(The entire partition must be scanned to check the unique property of a table but a local index only needs to check the unique property within a certain partition.)

## Action

1. The prefixed index needs to be created with a primary key or unique index. In other words, the partition key column and the index column should be the same for a primary key or unique index.

2. You can create a non-unique index if you want to create an index with a column that is not the same as the partition key column.

3. It is possible to create a primary key or unique index with a global index if you upgrade to ALTIBASE HDB 6.3.1 or above.

# Examples

```
iSQL> CREATE TABLE REALSET_CONTENTS
2 (
3 CT_ID VARCHAR (32) NOT NULL,
4 CT_TYPE VARCHAR (2) NOT NULL,
5 CT_PATH VARCHAR (256) NOT NULL,
6 CT_URL VARCHAR (256) NOT NULL,
7 REG_DATE DATE NOT NULL,
8 FILE_NAME VARCHAR (256) NOT NULL,
9 STATUS VARCHAR (4) NOT NULL
10 )
11 PARTITION BY RANGE (REG_DATE)
12 (
13 PARTITION P_1 VALUES LESS THAN (to_date('2013-05-01', 'YYYY-MM-DD')),
14 PARTITION P_2 VALUES LESS THAN (to_date('2013-09-01', 'YYYY-MM-DD')),
15 PARTITION P_DEF VALUES DEFAULT
16 )
17 TABLESPACE SYS_TBS_DISK_DATA;
Create success.
iSQL> alter table REALSET_CONTENTS add primary key(CT_ID,REG_DATE);
```

ERR-31283 : Unable to create a primary key or a unique key constraint in the local non-prefixed index.

1. The following example changes the primary key column order and creates a local prefixed index for the primary key.

```
iSQL> alter table REALSET_CONTENTS add primary key(REG_DATE,CT_ID);
Alter success.
iSQL> desc REALSET_CONTENTS
[ TABLESPACE : SYS_TBS_DISK_DATA ]
[ ATTRIBUTE ]
------------------------------------------------------------------------------
NAME                                     TYPE                        IS NULL
------------------------------------------------------------------------------
CT_ID                                    VARCHAR(32)                 NOT NULL
CT_TYPE                                  VARCHAR(2)                  NOT NULL
CT_PATH                                  VARCHAR(256)                NOT NULL
CT_URL                                   VARCHAR(256)                NOT NULL
REG_DATE                                 DATE                        NOT NULL
FILE_NAME                                VARCHAR(256)                NOT NULL
STATUS                                   VARCHAR(4)                  NOT NULL
[ INDEX ]
------------------------------------------------------------------------------
NAME                                     TYPE     IS UNIQUE     COLUMN
------------------------------------------------------------------------------
__SYS_IDX_ID_142                         BTREE    UNIQUE        REG_DATE ASC,
                                                                CT_ID ASC
[ PRIMARY KEY ]
------------------------------------------------------------------------------
REG_DATE, CT_ID
```

2. The following example creates a non-unique index (instead of a local non-prefixed index) for the primary key.

```
iSQL> create index REALSET_CONTENTS_IDX1 on REALSET_CONTENTS(CT_ID,REG_DATE) local;
Create success.
iSQL> desc REALSET_CONTENTS
[ TABLESPACE : SYS_TBS_DISK_DATA ]
[ ATTRIBUTE ]
------------------------------------------------------------------------------
NAME                                     TYPE                        IS NULL
------------------------------------------------------------------------------
CT_ID                                    VARCHAR(32)                 NOT NULL
CT_TYPE                                  VARCHAR(2)                  NOT NULL
CT_PATH                                  VARCHAR(256)                NOT NULL
CT_URL                                   VARCHAR(256)                NOT NULL
REG_DATE                                 DATE                        NOT NULL
FILE_NAME                                VARCHAR(256)                NOT NULL
STATUS                                   VARCHAR(4)                  NOT NULL
[ INDEX ]
------------------------------------------------------------------------------
NAME                                     TYPE     IS UNIQUE     COLUMN
------------------------------------------------------------------------------
REALSET_CONTENTS_IDX1                    BTREE                  CT_ID ASC,
                                                                REG_DATE ASC
REALSET_CONTENTS has no primary key
```

3. The following example upgrades to version 6.3.1 and then creates a global index for the primary key.

```
iSQL>  alter table REALSET_CONTENTS add primary key(CT_ID,REG_DATE);
Alter success.
iSQL> desc REALSET_CONTENTS
[ TABLESPACE : SYS_TBS_DISK_DATA ]
[ ATTRIBUTE ]
------------------------------------------------------------------------------
NAME                                     TYPE                        IS NULL
------------------------------------------------------------------------------
CT_ID                                    VARCHAR(32)                 NOT NULL
CT_TYPE                                  VARCHAR(2)                  NOT NULL
CT_PATH                                  VARCHAR(256)                NOT NULL
CT_URL                                   VARCHAR(256)                NOT NULL
REG_DATE                                 DATE                        NOT NULL
FILE_NAME                                VARCHAR(256)                NOT NULL
STATUS                                   VARCHAR(4)                  NOT NULL
[ INDEX ]
------------------------------------------------------------------------------
NAME                                     TYPE     IS UNIQUE     COLUMN
------------------------------------------------------------------------------
__SYS_IDX_ID_922                         BTREE    UNIQUE        CT_ID ASC,
                                                                REG_DATE ASC
[ PRIMARY KEY ]
------------------------------------------------------------------------------
CT_ID, REG_DATE
```

## Reference

# Index types for partitioned tables

| Classification 1 | Classification 2 | Classification 3 | Index Type | Supported by Altibase |
| --- | --- | --- | --- | --- |
| Partitioned Index | index part key = table part key | index part key = index key | (Partitioned) Local prefixed Index | Yes |
|  |  | index part key != index key | (Partitioned) Local nonprefixed Index | Yes |
|  | index part key != table part key | index part key = index key | (Partitioned) Global prefixed Index | No |
|  |  | index part key != index key | (Partitioned) Global nonprefixed Index | No |
| Non-partitioned Index |  |  | Non-partitioned global index | Supported for 6.3.1 and above |

The difference between a prefixed index and a non-prefixed index is uniqueness.

A non-prefixed index cannot be created for the primary key or unique index because even if it is unique within the partition, it cannot be guaranteed to be unique within the entire table.
