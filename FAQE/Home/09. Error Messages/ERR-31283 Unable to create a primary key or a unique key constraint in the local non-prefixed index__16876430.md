---
title: "ERR-31283 Unable to create a primary key or a unique key constraint in the local non-prefixed index."
page_id: "16876430"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876430"
updated_at: "2021-04-05T13:21:14.000+0900"
version: 2
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# ERR-31283 Unable to create a primary key or a unique key constraint in the local non-prefixed index.
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876430
Updated: 2021-04-05T13:21:14.000+0900

- [Version](#ERR-31283Unabletocreateaprimarykeyorauniquekeyconstraintinthelocalnon-prefixedindex.-Version) - [Symptom](#ERR-31283Unabletocreateaprimarykeyorauniquekeyconstraintinthelocalnon-prefixedindex.-Symptom) - [Cause](#ERR-31283Unabletocreateaprimarykeyorauniquekeyconstraintinthelocalnon-prefixedindex.-Cause) - [Solution](#ERR-31283Unabletocreateaprimarykeyorauniquekeyconstraintinthelocalnon-prefixedindex.-Solution) - [Reference](#ERR-31283Unabletocreateaprimarykeyorauniquekeyconstraintinthelocalnon-prefixedindex.-Reference)

# Version

---

Altibase version 6.1.1 or earlier

# Symptom

---

The following error occurs when creating PK or UNIQUE INDEX in the partition table.

[ERR-31283: Unable to create a primary key or a unique key constraint in the local non-prefixed index.]

# Cause

---

The description of the error can be checked using the altierr utility as follows.

$ altierr 0x31283

0x31283 ( 201347) qpERR_ABORT_QDX_NOT_ALLOWED_PRIMARY_AND_UNIQUE_KEY_OF_NONE_PREFIXED_INDEX Unable to create a primary key or a unique key constraint in the local non-prefixed index. # - The user tried to create a primary key or a unique key constraint in the local prefixed index. # *Action: # - Please do not create a primary key or a unique key constraint in the local non-prefixed index.

The global index is not supported in versions of Altibase 6.1.1 or earlier.

Therefore, all partition indexes are local indexes, and local non-prefixed indexes cannot be created with PK or UNIQUE INDEX.

The reason that local non-prefixed indexes cannot be created with PK or UNIQUE INDEX is that even if the column value is the only value within a specific partition, it cannot be guaranteed to be unique across the table.

(To check the UNIQUE attribute in the entire table, the entire partition must be examined, but the local index checks the UNIQUE attribute only within a specific partition.)

# Solution

---

1. PK or UNIQUE INDEX must be created as a prefixed index. That is, PK or UNIQUE INDEX must have the same partitioning key column and index column.

2. In order to create an index with a column that is not the same as the partitioning key column, it can be created with NON-UNIQUE INDEX.

3. If it is upgraded to Altibase version 6.3.1 or higher, PK or UNIQUE INDEX can be created as a global index.

# Example

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
[ERR-31283 : Unable to create a primary key or a unique key constraint in the local non-prefixed index.]
```

1. An example of creating a local prefixed index as PK by changing the PK column order.

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

2. An example of creating a local non-prefixed index as a non-unique index without creating a PK.

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

3. An example of creating a PK with a global index after upgrading to version 6.3.1.

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

# Reference

---

# Index type for the partitioned table

| Class condition 1 | Class condition 2 | Class condition 3 | Index type | Support/Not Supported |
| --- | --- | --- | --- | --- |
| The index is partitioned. | index part key = table part key | index part key = index key | (Partitioned) Local prefixed Index | Supported |
|  |  | index part key != index key | (Partitioned) Local nonprefixed Index | Supported |
|  | index part key != table part key | index part key = index key | (Partitioned) Global prefixed Index | Not supported |
|  |  | index part key != index key | (Partitioned) Global nonprefixed Index | Not supported |
| The index is not partitioned. |  |  | Nonpartitioned global index | Supported in version 6.3.1 or later |

The distinction between prefixed and nonprefixed indexes is due to the unique property.

In the case of a nonprefixed index, even if it is unique within a partition, it is not guaranteed to be unique across the table.

Therefore, nonprefixed indexes cannot be created with PK or UNIQUE INDEX.
