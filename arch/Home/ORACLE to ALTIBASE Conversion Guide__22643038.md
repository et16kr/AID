---
title: "ORACLE to ALTIBASE Conversion Guide"
page_id: "22643038"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/ORACLE+to+ALTIBASE+Conversion+Guide"
updated_at: "2025-10-21T09:45:53.000+0900"
version: 1
ancestors: ["Home"]
labels: []
---

# ORACLE to ALTIBASE Conversion Guide
Source: https://docs.altibase.com/display/arch/ORACLE+to+ALTIBASE+Conversion+Guide
Updated: 2025-10-21T09:45:53.000+0900

- [OverviewStored Procedure or Function 변환](#ORACLEtoALTIBASEConversionGuide-OverviewStoredProcedureorFunction변환) - [Migration Process](#ORACLEtoALTIBASEConversionGuide-MigrationProcess) - [System Analysis](#ORACLEtoALTIBASEConversionGuide-SystemAnalysis) - [Supported Version](#ORACLEtoALTIBASEConversionGuide-SupportedVersion) - [Preliminary Checklist](#ORACLEtoALTIBASEConversionGuide-PreliminaryChecklist) - [SQL Conversion Guide](#ORACLEtoALTIBASEConversionGuide-SQLConversionGuide) - [Data type conversion](#ORACLEtoALTIBASEConversionGuide-Datatypeconversion) - [Object Conversion](#ORACLEtoALTIBASEConversionGuide-ObjectConversion) - [SQL Conversion](#ORACLEtoALTIBASEConversionGuide-SQLConversion) - [Stored Procedure or Function Conversion](#ORACLEtoALTIBASEConversionGuide-StoredProcedureorFunctionConversion) - [Database Migration Procedure](#ORACLEtoALTIBASEConversionGuide-DatabaseMigrationProcedure) - [Data Migration and Application Conversion Procedure](#ORACLEtoALTIBASEConversionGuide-DataMigrationandApplicationConversionProcedure) - [Data Integrity Verification](#ORACLEtoALTIBASEConversionGuide-DataIntegrityVerification) - [Contingency Plan for Database Migration Failures](#ORACLEtoALTIBASEConversionGuide-ContingencyPlanforDatabaseMigrationFailures) - [Database Migration Tool](#ORACLEtoALTIBASEConversionGuide-DatabaseMigrationTool)

# OverviewStored Procedure or Function 변환

---

This document is about how to migrate Oracle Database to Altibase v7.1 or higher.

# Migration Process

---

Migration from Oracle to Altibase follows the following procedure.

![intro1.png](https://docs.altibase.com/download/attachments/embedded-page/arch/ORACLE%20to%20ALTIBASE%20Conversion%20Guide/intro1.png?api=v2)

![migration-process.png](https://docs.altibase.com/download/attachments/embedded-page/arch/ORACLE%20to%20ALTIBASE%20Conversion%20Guide/migration-process.png?api=v2)

# System Analysis

---

Describes the preliminary checklist for Oracle versions and environment configurations that can be migrated to Altibase.

## Supported Version

---

Oracle 12c

## Preliminary Checklist

---

To migrate from Oracle to Altibase, basic information about Oracle must be collected.

### Environment Analysis

---

- Oracle version
- OS and hardware specifications (CPU, memory, disk, etc.) of the system where Oracle is installed
- Altibase version
- OS and hardware specifications (CPU, memory, disk, etc.) of the system where Altibase will be installed
- Storage product, specifications (CPU, memory, network), and configuration (RAID1/RAID5, etc.) of the database server
- Network configuration and speed between the database server and storage

### Oracle Analysis

---

- Number and size of tablespaces
- Number and size of tables
- Number and size of objects
- Physical memory / swap size of the Oracle server
- Proportion of functions/procedures among all queries

### Business Analysis

---

- Ratio of online tasks to batch tasks
- Query complexity of batch tasks (Join, Group By, Order By, etc.)
- Number of concurrent batch tasks (queries)

# SQL Conversion Guide

---

Explanation of SQL conversion methods when migrating from Oracle to Altibase.

## Data type conversion

---

Describes considerations when converting Oracle data types to Altibase.

| Category | Oracle | Altibase | Oracle Max Size | Altibase Max Size | Note |
| --- | --- | --- | --- | --- | --- |
| Character Types | CHAR | CHAR | 2000 bytes | 32000 bytes |  |
| VARCHAR2,VARCHAR | VARCHAR2,VARCHAR | 4000 bytes | 32000 bytes | If MAX_STRING_SIZE=EXTENDED in Oracle, 32767 bytes |  |
| NCHAR | NCHAR | 1000(UTF16), 666(UTF8)<br>Max 2000 bytes | 16000(UTF16), 10666(UTF8)<br>Max 32000 bytes |  |  |
| NVARCHAR2 | NVARCHAR | 2000(UTF16), 1333(UTF8)<br>Max 4000 bytes | 16000(UTF16), 10666(UTF8)<br>Max 32000 bytes | If MAX_STRING_SIZE=EXTENDED in Oracle, 16383 (UTF16), 10922 (UTF8) Max 32767 bytes |  |
| Number Types | NUMBER NUMBER(p) NUMERIC(p, s) | NUMBER NUMBER(p) NUMERIC(p, s) |  |  | NUMBER(38) is an integer type; it is recommended to convert it to native types such as SMALLINT, INTEGER, BIGINT, etc., considering the maximum size. Using native types can reduce conversion overhead during data processing and improve storage efficiency. |
| FLOAT FLOAT(p) | FLOAT FLOAT(p) |  |  |  |  |
| BINARY_FLOAT | REAL |  |  | 4-byte floating point type |  |
| BINARY_DOUBLE | DOUBLE |  |  | 8-byte floating point type |  |
| LONG & RAW Types | LONG | CLOB | 2 GB | 4 GB - 1 | Can be replaced with Altibase CLOB |
| LONG RAW | BLOB | 2 GB | 4 GB - 1 | Can be replaced with Altibase BLOB |  |
| RAW (size) | BLOB | 2000 bytes | 4 GB - 1 | If MAX_STRING_SIZE=EXTENDED in Oracle, 32767 bytes<br>Can be replaced with Altibase BLOB |  |
| Date Types | DATE | DATE |  |  | Altibase DATE: 8 bytes. Range: Jan 1, year 1 to Dec 31, 9999. Stores year, month, day, hour, minute, second, and microseconds. Oracle DATE: 7 bytes. Range: Jan 1, 4712 BC to Dec 31, 9999 AD. Stores year, month, day, hour, minute, and second. |
| INTERVAL YEAR TO MONTH | - |  |  | Not supported in Altibase |  |
| INTERVAL DAY TO SECOND | - |  |  | Not supported in Altibase |  |
| TIMESTAMP WITH TIME ZONE | - |  |  | Not supported in Altibase |  |
| TIMESTAMP WITH LOCAL TIME ZONE | - |  |  | Not supported in Altibase |  |
| TIMESTAMP | DATE |  |  | Can be replaced with Altibase DATE Altibase DATE supports second precision up to 6 digits (microseconds) Oracle TIMESTAMP supports second precision up to 9 digits *Note: In Altibase, TIMESTAMP values cannot be user-defined. |  |
| Large Object Types | BLOB | BLOB | (4 GB - 1) * (database block size) | 4 GB - 1 |  |
| CLOB | CLOB | (4 GB - 1) * (database block size) | 4 GB - 1 |  |  |
| NCLOB | CLOB | (4 GB - 1) * (database block size) | 4 GB - 1 | Can be replaced with Altibase CLOB |  |
| BFILE | BLOB | 4 GB | 4 GB - 1 | Can be replaced with Altibase BLOB |  |
| ROWID Types | ROWID | - |  |  | Not supported in Altibase |
| UROWID | - |  |  | Not supported in Altibase |  |
| Any Types | ANYTYPE | - |  |  | Not supported in Altibase |
| ANYDATA | - |  |  | Not supported in Altibase |  |
| ANYDATASET | - |  |  | Not supported in Altibase |  |
| XML Types | XMLType | - |  |  | Not supported in Altibase |
| URI Data Types | - |  |  | Not supported in Altibase |  |
| URIFactory Package | - |  |  | Not supported in Altibase |  |
| Spatial Types | SDO_GEOMETRY | GEOMETRY |  | 16 bytes ~ 100 MB<br>default: 32,000 bytes | Can be replaced with Altibase GEOMETRY |
| SDO_TOPO_GEOMETRY | - |  |  | Not supported in Altibase |  |
| SDO_GEORASTER | - |  |  | Not supported in Altibase |  |
| Media Types | ORDAudio | - |  |  | Not supported in Altibase |
| ORDDicom | - |  |  | Not supported in Altibase |  |
| ORDDoc | - |  |  | Not supported in Altibase |  |
| ORDImage | - |  |  | Not supported in Altibase |  |
| ORDVideo | - |  |  | Not supported in Altibase |  |
| still_image_object_types | - |  |  | Not supported in Altibase |  |

## Object Conversion

---

Describes considerations when converting Oracle objects to Altibase.

### Object Comparison

---

| Category | Oracle | Altibase |
| --- | --- | --- |
| Schema Object | ANALYTIC VIEW | Not supported |
| ATTRIBUTE DIMENSION | Not supported |  |
| CLUSTER | Not supported |  |
| CONSTRAINT | Supported |  |
| DATABASE LINK | Supported |  |
| DATABASE TRIGGER | Supported |  |
| DIMENSION | Not supported |  |
| EXTERNAL PROCEDURE LIBRARY | Supported(C/C++ only) |  |
| HIERARCHY | Not supported |  |
| INDEX-ORGANIZED TABLE | Not supported |  |
| INDEX | Supports B-TREE, R-TREE, and Function-based indexes (BITMAP, CLUSTER, and Global Partitioned INDEX are not supported) |  |
| INDEXTYPE | Not supported |  |
| JAVA-related objects | Not supported |  |
| JOIN GROUP | Not supported |  |
| MATERIALIZED VIEW | Supported |  |
| MATERIALIZED VIEW LOG | Not supported |  |
| MINING MODEL | Not supported |  |
| OBJECT TABLE | Not supported |  |
| OBJECT TYPE | Not supported |  |
| OBJECT VIEW | Not supported |  |
| OPERATOR | Not supported |  |
| PACKAGE | Supported |  |
| SEQUENCE | Supported |  |
| STORED FUNCTION/PROCEDURE | Supported |  |
| SYNONYM | Supported |  |
| TABLE | Supported |  |
| VIEW | Supported |  |
| ZONE MAP | Not supported |  |
| Nonschema Object | CONTEXT | Not supported |
| DIRECTORY | Supported |  |
| EDITION | Not supported |  |
| FLASHBACK ARCHIVEF | Not supported |  |
| LOCKDOWN PROFILE | Not supported |  |
| PROFILE | Not supported |  |
| RESTROE POINT | Not supported |  |
| ROLE | Supported |  |
| ROLLBACK SEGMENT | Not supported |  |
| TABLESPACE | MEMORY, DISK, VOLATILE, TEMPORARY, UNDO Supported |  |
| TABLESPACE SET | Not supported |  |
| UNIFIED AUDIT POLICY | Not supported |  |
| USER | Supported |  |

### CREATE TABLESPACE

---

Oracle’s Data Tablespace is all Disk Tablespace. Altibase supports both Memory Tablespace and Disk Tablespace, allowing configuration according to business characteristics.

#### DATA TABLESPACE

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| BIGFILE\|SMALLFILE | - | Not supported by Altibase, so delete the corresponding option during conversion |
| DATAFILE File Specification | DATAFILE File Specification |  |
| MINIMUM EXTENT | - | Not supported by Altibase, so delete the corresponding option during conversion |
| BLOCKSIZE | - | Not supported by Altibase, so delete the corresponding option during conversion |
| LOGGING\|NOLOGGING | - | Not supported by Altibase, so delete the corresponding option during conversion |
| FORCE LOGGING | - | Not supported by Altibase, so delete the corresponding option during conversion |
| DEFAULT Storage statement | - | Not supported by Altibase, so delete the corresponding option during conversion |
| ONLINE\|OFFLINE | Can be done with the ALTER TABLESPACE statement | For OFFLINE, since it is not supported in the CREATE TABLESPACE statement, delete the option and add the statement: `ALTER TABLESPACE tablespace_name OFFLINE;` |
| EXTENT MANAGEMENT LOCAL AUTOALLOCATE\|UNIFORM SIZE | EXTENTSIZE | Extent management is not supported; only EXTENTSIZE can be set |
| SEGMENT SPACE MANAGEMENT AUTO\|MANUAL | SEGMENT MANAGEMENT AUTO\|MANUAL |  |
| FLASHBACK ON\|OFF | - | Not supported by Altibase, so delete the corresponding option during conversion |

#### Example of CREATE DATA TABLESPACE conversion

---

| Oracle | Altibase |
| --- | --- |
| ```<br>CREATE   TABLESPACE TESTDATA<br>DATAFILE   'testdata01.dbf'<br>SIZE   1024M<br>AUTOEXTEND   ON<br>NEXT   50M<br>MAXSIZE   UNLIMITED<br>LOGGING<br>ONLINE<br>EXTENT MANAGEMENT LOCAL AUTOALLOCATE<br>BLOCKSIZE 8K<br>SEGMENT   SPACE MANAGEMENT MANUAL<br>FLASHBACK ON;<br>``` | ```<br>CREATE   TABLESPACE TESTDATA<br>DATAFILE   'testdata01.dbf'<br>SIZE   1024M<br>AUTOEXTEND ON<br>NEXT   50M<br>MAXSIZE   UNLIMITED<br>SEGMENT MANAGEMENT MANUAL;<br>``` |

- The SEGMENT clause is modified to SEGMENT MANAGEMENT AUTO|MANUAL, and other unsupported clauses are removed.

#### TEMPORARY TABLESPACE

---

#### Example of

| Oracle | Altibase | 비고 |
| --- | --- | --- |
| TABLESPACE GROUP | - | Not supported by Altibase, so delete the corresponding option during conversion |
| EXTENT MANAGEMENT LOCAL AUTOALLOCATE\|UNIFORM SIZE | EXTENTSIZE | Extent management is not supported; only EXTENTSIZE can be configured |

#### Example of CREATE TEMPORARY TABLESPACE

---

| Oracle | Altibase |
| --- | --- |
| ```<br>CREATE TEMPORARY TABLESPACE   tbs_temp_02<br>TEMPFILE 'temp02.dbf' SIZE   5M AUTOEXTEND ON<br>TABLESPACE GROUP   tbs_grp_01;<br>``` | ```<br>CREATE TEMPORARY TABLESPACE   tbs_temp_02<br>TEMPFILE   'temp02.dbf' SIZE 5M AUTOEXTEND ON;<br>``` |

- TABLESPACE GROUP clause is not supported and should be removed.

#### UNDO TABLESPACE

---

Altibase automatically manages Undo Tablespaces by the system. Only adding data files and resizing are allowed for Undo Tablespaces.

#### Example of CREATE UNDO TABLESPACE

---

| Oracle | Altibase |
| --- | --- |
| ```<br>CREATE UNDO TABLESPACE UNDOTBS2<br>DATAFILE ‘undotbs2.dbf'<br>SIZE 500M<br>AUTOEXTEND ON<br>NEXT 5M<br>MAXSIZE UNLIMITED;<br>``` | ```<br>ALTER TABLESPACE SYS_TBS_DISK_UNDO<br>ADD DATAFILE 'undotbs2.dbf'<br>SIZE 500M<br>AUTOEXTEND ON<br>NEXT 5M<br>MAXSIZE UNLIMITED;<br>``` |

### CREATE TABLE

---

Altibase does not support Object Tables or XMLType Tables, but it does support Memory Tables. Therefore, based on business characteristics, tables can be created by separating them into Memory Tables and Disk Tables.

When specifying segment-related details during TABLE creation, the order should be: specify TABLESPACE → specify PCTFREE/PCTUSED → specify INITRANS/MAXTRANS → specify Storage clause → specify Logging clause.

#### COLUMN DEFINITION 절

---

| Oracle | Altibase | 비고 |
| --- | --- | --- |
| SORT | - | Not supported by Altibase, so delete the corresponding option during conversion |
| DEFAULT | DEFAULT |  |
| ENCRYPT | ENCRYPT |  |
| Constraint statement | Constraint statement | Altibase does not support the ENABLE/DISABLE options for constraints or the ON DELETE SET NULL option in the REFERENCES clause (ON DELETE CASCADE is supported), so these should be removed. When specifying PRIMARY KEY or UNIQUE constraints in Altibase, only the Tablespace clause, Parallel clause, Logging clause, and Force clause are allowed in the Using Index clause. In other words, index names and CREATE INDEX clauses are not supported. |
| Ref Constraint syntax | - | Altibase does not support REF columns, so this option should be removed during conversion |
| ORGANIZATION | - | Not supported by Altibase, so delete the corresponding option during conversion |
| CLUSTER | - | Not supported by Altibase, so delete the corresponding option during conversion |
| COMPRESS\|NOCOMPRESS | COMPRESS | Altibase defaults to NOCOMPRESS if not specified, so the NOCOMPRESS option should be removed during conversion |
| Specifying the Byte keyword for column size | The Byte keyword is not supported when specifying column size. | Oracle allows specifying the Byte keyword for column size, but Altibase does not support it. Example: Oracle: `c1 VARCHAR2(10 Byte)` → Altibase: `c1 VARCHAR2(10)` |

- When specifying PRIMARY KEY or UNIQUE constraints using the USING INDEX clause to set index properties, Altibase only allows TABLESPACE, PARALLEL/NOPARALLEL, and LOGGING/NOLOGGING clauses. In other words, storage-related properties cannot be specified.

#### SEGMENT ATTRIBUTES clause

---

| Oracle | Altibase | 비고 |
| --- | --- | --- |
| TABLESPACE | TABLESPACE |  |
| PCTFREE | PCTFREE |  |
| PCTUSED | PCTUSED |  |
| INITRANS | INITRANS |  |
| MAXTRANS | MAXTRANS | Oracle default/maximum value: 255, Altibase default/maximum value: 120<br>When converting to Altibase, omit this parameter or change it to 120. Note that Oracle's MAXTRANS parameter is deprecated. |
| LOGGING\|NOLOGGING | LOGGING\|NOLOGGING |  |

#### STORAGE clause

---

| Oracle | Altibase | 비고 |
| --- | --- | --- |
| INITIAL | INITEXTENTS | Change from bytes to number of extents |
| NEXT | NEXTEXTENTS | Change from bytes to number of extents |
| MINEXTENTS | MINEXTENTS |  |
| MAXEXTENTS | MAXEXTENTS |  |
| PCTINCREASE | - | Not supported by Altibase, so delete the corresponding option during conversion |
| FREELISTS | - | Not supported by Altibase, so delete the corresponding option during conversion |
| FREELIST | - | Not supported by Altibase, so delete the corresponding option during conversion |
| OPTIMAL | - | Not supported by Altibase, so delete the corresponding option during conversion |
| BUFFER POOL | - | Not supported by Altibase, so delete the corresponding option during conversion |

#### LOB STORAGE clause

---

| Oracle | Altibase | 비고 |
| --- | --- | --- |
| TABLESPACE | TABLESPACE | Altibase의 LOB STORAGE절은 TABLESPACE만 지정 가능 |
| STORAGE | - | Not supported by Altibase, so delete the corresponding option during conversion |
| CHUNK | - | Not supported by Altibase, so delete the corresponding option during conversion |
| PCTVERSION | - | Not supported by Altibase, so delete the corresponding option during conversion |
| RETENTION | - | Not supported by Altibase, so delete the corresponding option during conversion |
| FREEPOOLS | - | Not supported by Altibase, so delete the corresponding option during conversion |
| CACHE | - | Not supported by Altibase, so delete the corresponding option during conversion |
| STORAGE IN ROW | - | Not supported by Altibase, so delete the corresponding option during conversion |
| LOGGING\|NOLOGGING | LOGGING\|NOLOGGING |  |

#### TABLE PARTITION clause

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| PARTITION BY RANGE | PARTITION BY RANGE |  |
| PARTITION BY HASH | PARTITION BY HASH |  |
| PARTITION BY LIST | PARTITION BY LIST |  |
| Composite partitioning statement | - | Not supported by Altibase, so delete the corresponding option during conversion |

#### TABLE PROPERTIES clause

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| ENABLE\|DISABLE ROW MOVEMENT | ENABLE\|DISABLE ROW MOVEMENT | Supported only for partitioned TABLEs |
| NOPARALLEL\|PARALLEL | NOPARALLEL\|PARALLEL |  |
| ENABLE\|DISABLE VALIDATE\|NOVALIDATE | - | Not supported by Altibase, so delete the corresponding option during conversion |

#### example of CREATE TABLE

---

| Oracle | Altibase |
| --- | --- |
| ```<br>CREATE TABLE "SCOTT"."EMP"<br>(	"EMPNO" NUMBER(4,0),<br>"ENAME" VARCHAR2(10 Byte),<br>"JOB" VARCHAR2(9 Byte),<br>"MGR" NUMBER(4,0),<br>"HIREDATE" DATE,<br>"SAL" NUMBER(7,2),<br>"COMM" NUMBER(7,2),<br>"DEPTNO" NUMBER(2,0),<br>CONSTRAINT "PK_EMP" PRIMARY KEY ("EMPNO")<br>USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS<br>STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645<br>PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT)<br>TABLESPACE "USERS" ENABLE,<br>CONSTRAINT "FK_DEPTNO" FOREIGN KEY ("DEPTNO")<br>REFERENCES "SCOTT"."DEPT" ("DEPTNO") ENABLE<br>) PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING<br>STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645<br>PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT)<br>TABLESPACE "USERS" ;<br>``` | ```<br>CREATE TABLE "SCOTT"."EMP"<br>(	"EMPNO" NUMBER(4,0),<br>"ENAME" VARCHAR2(10),<br>"JOB" VARCHAR2(9),<br>"MGR" NUMBER(4,0),<br>"HIREDATE" DATE,<br>"SAL" NUMBER(7,2),<br>"COMM" NUMBER(7,2),<br>"DEPTNO" NUMBER(2,0),<br>CONSTRAINT "PK_EMP" PRIMARY KEY ("EMPNO")<br>USING INDEX TABLESPACE "USERS" ,<br>CONSTRAINT "FK_DEPTNO" FOREIGN KEY ("DEPTNO")<br>REFERENCES "SCOTT"."DEPT" ("DEPTNO")<br>)<br>TABLESPACE "USERS"<br>PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 120<br>STORAGE(INITEXTENTS 1 NEXTEXTENTS 1 MINEXTENTS 1 MAXEXTENTS 2147483645)<br>LOGGING ;<br>``` |

- "ENAME" VARCHAR2(10): Remove Byte
- USING INDEX TABLESPACE "USERS": When specifying PK, only TABLESPACE, PARALLEL/NOPARALLEL, and LOGGING/NOLOGGING clauses are allowed in the USING INDEX clause, so remove options other than TABLESPACE
- REFERENCES "SCOTT"."DEPT" ("DEPTNO"): For FK, ENABLE option is not supported, so remove it
- PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 120: Since the maximum value for MAXTRANS is 120, change it to 120
- STORAGE(INITEXTENTS 1 NEXTEXTENTS 1 MINEXTENTS 1 MAXEXTENTS 2147483645): Change INITIAL and NEXT to INITEXTENTS and NEXTEXTENTS respectively, and adjust their values to the number of extents
- TABLESPACE "USERS" PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 120 STORAGE... LOGGING: When specifying segment-related options, follow this order: specify TABLESPACE → specify PCTFREE/PCTUSED → specify INITRANS/MAXTRANS → specify Storage clause → specify Logging clause

### CREATE INDEX

---

The types of indexes supported by Altibase are BTREE, RTREE, and Function-based INDEX. BITMAP, CLUSTER, REVERSE, and Global partitioned INDEX are not supported.

When specifying segment-related details during Altibase INDEX creation, the order should be: specify TABLESPACE → specify PARALLEL/NOPARALLEL → specify LOGGING/NOLOGGING → specify Storage clause.

| Oracle | Altibase | 비고 |
| --- | --- | --- |
| TABLESPACE | TABLESPACE |  |
| LOGGING\|NOLOGGING | LOGGING\|NOLOGGING |  |
| NOPARALLEL\|PARALLEL | NOPARALLEL\|PARALLEL |  |
| COMPUTE STATISTICS | - | Not supported by Altibase, so delete the corresponding option during conversion |
| REVERSE | - | Not supported by Altibase, so delete the corresponding option during conversion |
| SORT\|NOSORT | - | Not supported by Altibase, so delete the corresponding option during conversion |
| ONLINE | - | Not supported by Altibase, so delete the corresponding option during conversion |
| COMPRESS\|NOCOMPRESS | - | Not supported by Altibase, so delete the corresponding option during conversion |
| PCTFREE, PCTUSED, | - | Not supported by Altibase, so delete the corresponding option during conversion |
| INITRANS | INITRANS |  |
| MAXTRANS | MAXTRANS | Oracle default/maximum value: 255, Altibase default/maximum value: 30<br>When converting to Altibase, omit this parameter or change it to 30. Note that Oracle's MAXTRANS parameter is deprecated. |
| Storage statement | Same as the TABLE Storage clause |  |

#### example of CREATE INDEX

---

| Oracle | Altibase |
| --- | --- |
| ```<br>CREATE INDEX "SCOTT"."EMP_IDX1" ON "SCOTT"."EMP" ("DEPTNO", "SAL")<br>PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS<br>STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645<br>PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT)<br>TABLESPACE "USERS" ;<br>``` | ```<br>CREATE INDEX "SCOTT"."EMP_IDX1" ON "SCOTT"."EMP" ("DEPTNO", "SAL")<br>TABLESPACE "USERS"<br>INITRANS 2 MAXTRANS 30<br>STORAGE(INITEXTENTS 1 NEXTEXTENTS 1 MINEXTENTS 1 MAXEXTENTS 2147483645) ;<br>``` |

- INITRANS 2 MAXTRANS 30: Since MAXTRANS supports up to 30, change it to 30
- STORAGE(INITEXTENTS 1 NEXTEXTENTS 1 MINEXTENTS 1 MAXEXTENTS 2147483645): Only INITEXTENTS, NEXTEXTENTS, MINEXTENTS, and MAXEXTENTS can be specified in the STORAGE clause. Change INITIAL and NEXT to INITEXTENTS and NEXTEXTENTS respectively, and adjust their values to the number of extents
- TABLESPACE "USERS" INITRANS 2 MAXTRANS 30 STORAGE ... When specifying segment-related details, follow this order: specify TABLESPACE → specify PARALLEL/NOPARALLEL → specify LOGGING/NOLOGGING → specify Storage clause

### CREATE VIEW

---

Altibase VIEWs are created using the CREATE OR REPLACE VIEW statement, the same syntax as Oracle VIEW creation.

| Oracle | Altibase | 비고 |
| --- | --- | --- |
| WITH READ ONLY | WITH READ ONLY | If this option is not specified, an updatable view is created |
| NO FORCE | NO FORCE |  |
| WITH CHECK OPTION | - | Not supported by Altibase, so delete the corresponding option during conversion |
| XMLType view statement | - | Not supported by Altibase, so delete the corresponding option during conversion |
| Object view statement | - | Not supported by Altibase, so delete the corresponding option during conversion |

### CREATE TRIGGER

---

Altibase triggers are created using the CREATE OR REPLACE TRIGGER statement, the same syntax as Oracle.

When using Altibase replication, data changes reflected by replication do not trigger trigger execution, so this behavior should be considered in the business logic.

| Oracle | Altibase | 비고 |
| --- | --- | --- |
| CREATE OR REPLACE TRIGGER | CREATE OR REPLACE TRIGGER |  |
| BEFORE\|AFTER\|INSTEAD OF | BEFORE\|AFTER\|INSTEAD OF |  |
| DML event statement | DML event statement | DML event statements are the same as in Oracle |
| DDL event statement | - | Altibase does not support DDL triggers |
| WHEN condition | WHEN condition |  |
| FOR EACH ROW | FOR EACH ROW |  |
| REFERENCING | REFERENCING | In Altibase, OLD and NEW are keywords and cannot be used as aliases |
| Trigger body statement | Trigger body statement |  |

### CREATE SEQUENCE

---

Altibase SEQUENCE is created using the CREATE SEQUENCE statement, the same syntax as Oracle SEQUENCE creation.

| Oracle | Altibase | 비고 |
| --- | --- | --- |
| CREATE SEQUENCE | CREATE SEQUENCE |  |
| START WITH | START WITH |  |
| INCREMENT BY | INCREMENT BY |  |
| MAXVALUE\|NOMAXVALUE | MAXVALUE\|NOMAXVALUE | Oracle’s maxvalue can be specified up to a 28-digit integer.<br>Altibase’s maxvalue can be specified within the range of -9,223,372,036,854,775,805 to 9,223,372,036,854,775,806. |
| MINVALUE\|NOMINVALUE | MINVALUE\|NOMINVALUE |  |
| CYCLE\|NOCYCLE | CYCLE\|NOCYCLE |  |
| CACHE\|NOCACHE | CACHE\|NOCACHE |  |
| ORDER\|NOORDER |  | Not supported by Altibase, so delete the corresponding option during conversion |
| KEEP\|NOKEEP |  | Not supported by Altibase, so delete the corresponding option during conversion |
| SESSION\|GLOBAL |  | Not supported by Altibase, so delete the corresponding option during conversion |

### CREATE SYNONYM

---

Altibase's CREATE SYNONYM statement is the same as Oracle's, except that the EDITIONABLE and NONEDITIONABLE options are not supported.

### ALTER TABLE

---

Altibase allows adding only one constraint at a time.

In Oracle, multiple constraints can be added using the statement: ALTER TABLE ADD (CONSTRAINT constraint_name constraint_type, …);

But in Altibase, this must be split into separate statements for each constraint: ALTER TABLE ADD CONSTRAINT constraint_name constraint_type;

In Oracle, PRIMARY KEY and UNIQUE constraints can be specified after pre-creating the index. However, in Altibase, the index is created internally at the time of constraint definition, so only one of PK constraint, UNIQUE constraint, or INDEX creation is allowed on the same column. This means you cannot define a PK constraint on a column that already has an index.

## SQL Conversion

---

### Numeric Functions

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| ABS(n) | ABS(n) | Returns the absolute value of n |
| ACOS(n) | ACOS(n) | Returns the arc cosine of n |
| ASIN(n) | ASIN(n) | Returns the arc sine of n |
| ATAN(n) | ATAN(n) | Returns the arc tangent of n |
| ATAN2(n1, n2) | ATAN2(n1, n2) | Returns the arc tangent of n1/n2 in radians |
| BITAND(expr1, expr2) | BITAND(expr1, expr2) | Performs bitwise AND between expr1 and expr2 and returns an integer |
| CEIL(n) | CEIL(n) | Returns the smallest integer greater than or equal to n |
| COS(n) | COS(n) | Returns the cosine of n |
| COSH(n) | COSH(n) | Returns the hyperbolic cosine of n |
| EXP(n) | EXP(n) | Returns e raised to the power of n |
| FLOOR(n) | FLOOR(n) | Returns the largest integer less than or equal to n |
| LN(n) | LN(n) | Returns the natural logarithm of n |
| LOG(n2, n1) | LOG(n2, n1) | Returns the logarithm of n1 with base n2 |
| MOD(n2, n1) | MOD(n2, n1) | Returns the remainder of n2 divided by n1 |
| NANVL(n2, n1) | Not Supported | Returns n1 if n2 is NaN, otherwise returns n2 |
| POWER(n2, n1) | POWER(n2, n1) | Returns n2 raised to the power of n1 |
| REMAINDER(n2, n1) | MOD(n2, n1) | Returns the remainder of n2 divided by n1 |
| ROUND(number) | ROUND(number) | Rounds number to the nearest integer |
| SIGN(n) | SIGN(n) | Returns the sign of n |
| SIN(n) | SIN(n) | Returns the sine of n |
| SINH(n) | SINH(n) | Returns the hyperbolic sine of n |
| SQRT(n) | SQRT(n) | Returns the square root of n |
| TAN(n) | TAN(n) | Returns the tangent of n |
| TANH(n) | TANH(n) | Returns the hyperbolic tangent of n |
| TRUNC(number) | TRUNC(number) | Truncates number to the specified decimal places |
| WIDTH_BUCKET | Not Supported | Creates histograms with equal width |

### Character Functions Returning Character Values

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| CHR | CHR | Returns the character corresponding to the input ASCII code value |
| CONCAT | CONCAT | Concatenates char1 and char2 and returns the result |
| INITCAP | INITCAP | Converts the first letter of each word in the input string to uppercase and returns it |
| LOWER | LOWER | Converts the input string to lowercase and returns it |
| LPAD | LPAD | Inserts expr2 repeatedly on the left side of expr1 until the total length is n and returns it |
| LTRIM | LTRIM | Removes characters matching expr2 from the left side of expr1 and returns it |
| NCHR | NCHR | Returns the character corresponding to the value n in the national character set |
| NLS_INITCAP | Not Supported | Converts the first letter of each word in the input string to uppercase and returns it |
| NLS_LOWER | Not Supported | Converts all characters to lowercase and returns it |
| NLS_UPPER | Not Supported | Converts the input string to uppercase and returns it |
| NLSSORT | Not Supported | Sorts the input string and returns it |
| REGEXP_REPLACE | REGEXP_REPLACE | Replaces parts matching the specified regular expression with another string and returns it |
| REGEXP_SUBSTR | REGEXP_SUBSTR | Returns the substring matching the specified regular expression |
| REPLACE | REPLACE2 | Replaces all occurrences of the second string with the third string in the first string and returns the result |
| RPAD | RPAD | Inserts expr2 repeatedly on the right side of expr1 until the total length is n and returns it |
| RTRIM | RTRIM | Removes characters matching expr2 from the right side of expr1 and returns it |
| SOUNDEX | Not Supported | Returns a string representing the phonetic expression of the character |
| SUBSTR | SUBSTR | Returns the substring from expr starting at position start for length characters |
| TRANSLATE | TRANSLATE | Replaces each character in from_string with the corresponding character in to_string and returns it |
| TRANSLATE ... USING | Not Supported | Converts characters between database character set and national character set and returns it |
| TRIM | TRIM | Removes all characters found in expr2 from the beginning and end of expr1 and returns it |
| UPPER | UPPER | Converts all characters to uppercase and returns it |

### Character Functions Returning Number Values

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| ASCII | ASCII | Returns the decimal value corresponding to the ASCII code of the first character in the given char |
| INSTR | INSTR | Returns the position (number) where the specified character first appears in the string |
| LENGTH | CHAR_LENGTH<br>CHARACTER_LENGTH<br>LENGTH | Returns the length of the argument char |
| REGEXP_COUNT | REGEXP_COUNT | Returns the number of occurrences of pattern_expr in the string |
| REGEXP_INSTR | REGEXP_INSTR | Returns the position of the first occurrence that matches the specified pattern (regular expression) |

### Character Set Functions

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| NLS_CHARSET_DECL_LEN<br>NLS_CHARSET_ID<br>NLS_CHARSET_NAME | Not supported | Returns the database character set ID and name |

### Collation Functions

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| COLLATION<br>NLS_COLLATION_ID<br>NLS_COLLATION_NAME | Not supported | Returns information about data collation settings |

### Datetime Functions

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| +, - operations | +, -, DATEADD | Returns the result of increasing or decreasing the specified `date_field_name` part of a date by a given number |
| ADD_MONTHS | ADD_MONTHS | Returns the result of adding a specific number of months (integer) to a date |
| CURRENT_DATE | CURRENT_DATE | Returns the current session's date as a `DATE` type |
| CURRENT_TIMESTAMP | CURRENT_TIMESTAMP | Returns the current session’s date and time (alias of `CURRENT_DATE`) |
| DBTIMEZONE | DB_TIMEZONE | Returns the database time zone value |
| EXTRACT(datetime) | EXTRACT(datetime)<br>DATEPART | Extracts and returns the value of the specified date/time field from a datetime or interval expression |
| FROM_TZ | Not Supported | Converts a timestamp and time zone to a `TIMESTAMP WITH TIME ZONE` value |
| LAST_DAY | LAST_DAY | Returns the last day of the month in which the given date falls |
| LOCALTIMESTAMP | Not Supported | Returns the current date and time in the session time zone as a `TIMESTAMP` value |
| MONTHS_BETWEEN | MONTHS_BETWEEN | Returns the number of months between `date1` and `date2` |
| NEW_TIME | Not Supported | Converts a date and time from `timezone1` to `timezone2` and returns the result |
| NEXT_DAY | NEXT_DAY | Returns the date of the next occurrence of a specified weekday after the given date |
| NUMTODSINTERVAL | NUMTODSINTERVAL<br>TO_INTERVAL | Converts `n` to an `INTERVAL DAY TO SECOND` value |
| NUMTOYMINTERVAL | TO_INTERVAL | Converts `n` to an `INTERVAL YEAR TO MONTH` value |
| ORA_DST_AFFECTED | Not Supported |  |
| ORA_DST_CONVERT | Not Supported |  |
| ORA_DST_ERROR | Not Supported |  |
| ROUND(date) | ROUND(date) | Returns the date rounded to the specified unit |
| SESSIONTIMEZONE | SESSION_TIMEZONE | Returns the time zone of the current session |
| SYS_EXTRACT_UTC | Not Supported | Returns the UTC (Coordinated Universal Time) |
| SYSDATE | SYSDATE | Returns the current date and time of the operating system hosting the database |
| SYSTIMESTAMP | SYSTIMESTAMP | Returns the system date as a `TIMESTAMP WITH TIME ZONE` value |
| TO_CHAR(datetime) | TO_CHAR(datetime) | Converts to a `VARCHAR` value using the specified format |
| TO_DSINTERVAL | Not Supported | Converts the argument to an `INTERVAL DAY TO SECOND` value |
| TO_TIMESTAMP | TO_DATE | Converts a `char` value to a `TIMESTAMP` value |
| TO_TIMESTAMP_TZ | Not Supported | Converts a `char` value to a `TIMESTAMP WITH TIME ZONE` value |
| TO_YMINTERVAL | Not Supported | Converts a string to an `INTERVAL YEAR TO MONTH` value |
| TRUNC(date) | TRUNC(date) | Truncates the date to the specified unit |
| TZ_OFFSET | Not Supported | Returns the time zone offset corresponding to the input based on the date the statement is executed |

### General Comparison Functions

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| GREATEST | GREATEST | Returns the greatest value among one or more arguments |
| LEAST | LEAST | Returns the least value among one or more arguments |

### Conversion Functions

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| ASCIISTR | ASCIISTR | Returns the ASCII string representation of the input string |
| BIN_TO_NUM | BIN_TO_NUM | Converts a bit (binary) vector to its equivalent numeric (decimal) value |
| CAST | CAST | Converts one data type to another |
| CHARTOROWID | Not Supported | Converts a character value to a ROWID |
| COMPOSE | Not Supported | Returns a normalized Unicode string |
| CONVERT | CONVERT | Converts a string to the specified character set |
| DECOMPOSE | Not Supported | Returns a decomposed Unicode string using the same character set as input |
| HEXTORAW | Not Supported | Converts a hexadecimal string to a RAW data type |
| NUMTODSINTERVAL | NUMTODSINTERVAL<br>TO_INTERVAL | Converts `n` to an `INTERVAL DAY TO SECOND` data type |
| NUMTOYMINTERVAL | TO_INTERVAL | Converts `n` to an `INTERVAL YEAR TO MONTH` data type |
| RAWTOHEX | Not Supported | Converts RAW to a hexadecimal string |
| RAWTONHEX | Not Supported | Converts RAW to a hexadecimal string in NVARCHAR2 format |
| RAWIDTOCHAR | Not Supported | Converts a RAWID to VARCHAR2 |
| ROWIDTONCHAR | Not Supported | Converts a RAWID to NVARCHAR2 |
| SCN_TO_TIMESTAMP | Not Supported | Converts a system change number (SCN) to a TIMESTAMP |
| TIMESTAMP_TO_SCN | Not Supported | Returns the approximate SCN associated with the input TIMESTAMP |
| TO_BINARY_DOUBLE | Not Supported | Converts input to a double-precision floating-point number |
| TO_BINARY_FLOAT | Not Supported | Converts input to a single-precision floating-point number |
| TO_BLOB(bfile) | Not Supported | Converts a BFILE to a BLOB |
| TO_BLOB(raw) | Not Supported | Converts a RAW value to a BLOB |
| TO_CHAR(bfile\|blob) | Not Supported | Converts BFILE or BLOB to the database character set |
| TO_CHAR(character) | Not Supported | Converts NCHAR, NVARCHAR2, CLOB, or NCLOB to the database character set |
| TO_CHAR(datetime) | TO_CHAR(datetime) | Converts datetime or interval to a VARCHAR in the specified format |
| TO_CHAR(number) | TO_CHAR(number) | Converts a number to a VARCHAR |
| TO_CLOB(bfile\|blob) | Not Supported | Converts BFILE or BLOB to a CLOB using the database character set |
| TO_CLOB(character) | Not Supported | Converts NCLOB or other strings to a CLOB |
| TO_DATE | TO_DATE | Converts a character string to a DATE data type |
| TO_DSINTERVAL | Not Supported | Converts input to `INTERVAL DAY TO SECOND` |
| TO_LOB | Not Supported | Converts LONG or LONG RAW to LOB |
| TO_MULTI_BYTE | Not Supported | Converts all single-byte characters in the input to multibyte form |
| TO_NCHAR(character) | TO_NCHAR(character) | Converts string, CLOB, or NCLOB to the national character set |
| TO_NCHAR(datetime) | TO_NCHAR(datetime) | Converts datetime or interval to national character set |
| TO_NCHAR(number) | TO_NCHAR(number) | Converts number to national character set |
| TO_NCLOB | Not Supported | Converts a CLOB to an NCLOB |
| TO_NUMBER | TO_NUMBER | Converts an expression to a NUMBER |
| TO_SINGLE_BYTE | Not Supported | Converts all multibyte characters in the input to single-byte form |
| TO_TIMESTAMP | TO_DATE | Converts a character string to TIMESTAMP |
| TO_TIMESTAMP_TZ | Not Supported | Converts a character string to TIMESTAMP WITH TIME ZONE |
| TO_YMINTERVAL | Not Supported | Converts a string to an `INTERVAL YEAR TO MONTH` |
| TREAT | Not Supported | Used for object-oriented type conversion from a supertype to a subtype |
| UNISTR | UNISTR | Represents or converts a Unicode string |
| VALIDATE_CONVERSION | Not Supported | Checks whether an expression can be converted to a specified data type |

### Large Object Functions

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| BFILENAME | Not Supported | Returns a BFILE locator associated with a physical LOB binary file in the server file system |
| EMPTY_BLOB / EMPTY_CLOB | EMPTY_BLOB / EMPTY_CLOB | Function to initialize LOB variables |

### Collection Functions

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| CARDINALITY COLLECT POWERMULTISET POWERMULTISET_BY_CARDINALITY SET | Not Supported | Function performed on nested tables and varrays |

### Hierarchical Functions

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| SYS_CONNECT_BY_PATH | SYS_CONNECT_BY_PATH | Function that returns the path of column values from the root node to the current node |

### Data Mining Functions

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| CLUSTER_DETAILS CLUSTER_DISTANCE CLUSTER_ID CLUSTER_PROBABILITY CLUSTER_SET FEATURE_COMPARE FEATURE_DETAILS FEATURE_ID FEATURE_SET FEATURE_VALUE ORA_DM_PARTITION_NAME PREDICTION PREDICTION_BOUNDS PREDICTION_COST PREDICTION_DETAILS PREDICTION_PROBABILITY PREDICTION_SET | Not Supported | Functions related to data mining |

### XML Functions

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| DEPTH EXISTSNODE EXTRACT (XML) EXTRACTVALUE PATH SYS_DBURIGEN SYS_XMLAGG SYS_XMLGEN XMLAGG XMLCAST XMLCDATA XMLCOLATTVAL XMLCOMMENT XMLCONCAT XMLDIFF XMLELEMENT XMLEXISTS XMLFOREST XMLISVALID XMLPARSE XMLPATCH XMLPI XMLQUERY XMLROOT XMLSEQUENCE XMLSERIALIZE XMLTABLE XMLTRANSFORM | Not Supported | Functions related to XML |

### JSON Functions

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| JSON_QUERY JSON_TABLE JSON_VALUE JSON_ARRAY JSON_ARRAYAGG JSON_OBJECT JSON_OBJECTAGG JSON_DATAGUIDE | Not Supported | Functions related to JSON |

### Encoding and Decoding Functions

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| DECODE | DECODE | Function used to implement IF logic within SQL or PL/SQL |
| DUMP | DUMP | Returns information such as position and length of the specified data in a given format |
| ORA_HASH | Not Supported | Function that calculates a hash value for the given expression |
| STANDARD_HASH | Not Supported | Calculates a standard hash value |
| VSIZE | OCTET_LENGTH | Returns the length of the input string in bytes |

### NULL-Related Functions

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| COALESCE | COALESCE | Returns the first non-NULL expression from the list of arguments, checked in order |
| LNNVL | LNNVL | Returns TRUE if the condition is FALSE or NULL; returns FALSE if the condition is TRUE |
| NANVL | Not Supported | Detects only NaN (Not a Number) floating-point values and replaces them with another value |
| NULLIF | NULLIF | Returns NULL if `expr1` equals `expr2`; otherwise returns `expr1` |
| NVL | NVL | Replaces NULL values in query results |
| NVL2 | NVL2 | Returns `expr2` if `expr1` is not NULL; otherwise returns `expr3` |

### Environment and Identifier Functions

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| CON_DBID_TO_ID CON_GUID_TO_ID CON_NAME_TO_ID CON_UID_TO_ID ORA_INVOKING_USER ORA_INVOKING_USERID | Not Supported |  |
| SYS_CONTEXT | SYS_CONTEXT | Returns the value of a parameter related to the current session's environment using a namespace |
| SYS_GUID | SYS_GUID_STR | Generates and returns a globally unique 16-byte identifier (RAW value) |
| SYS_TYPEID | Not Supported | Returns the type ID of the identifier |
| UID | USER_ID | Returns a unique integer that identifies the session user |
| USER | USER_NAME | Returns the name of the session user |
| USERENV | SESSION_ID | `USERENV` returns information about the session; `SESSION_ID` returns the user's session ID |

### Aggregate/Analytic Functions

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| AVG | AVG | Returns the average of non-NULL values in the specified column that meet the condition |
| CORR | CORR | Returns the correlation coefficient for pairs of numeric values |
| COUNT | COUNT | Returns the number of rows returned by the query |
| COVAR_POP | COVAR_POP | Returns the population covariance of a set of number pairs |
| COVAR_SAMP | COVAR_SAMP | Returns the sample covariance of a set of number pairs |
| CUME_DIST | CUME_DIST | Calculates the cumulative distribution of a value within a group |
| DENSE_RANK | DENSE_RANK | Assigns ranks to rows in order by specified columns or expressions; unlike RANK, the next rank increases by 1 regardless of ties |
| FIRST | FIRST | Used with aggregate functions (MIN, MAX, etc.) to get the first row’s value based on ordering |
| LAST | LAST | Used with aggregate functions (MIN, MAX, etc.) to get the last row’s value based on ordering |
| LISTAGG | LISTAGG | Aggregate function that concatenates string values from multiple rows into a single string |
| MAX | MAX | Returns the maximum value among the arguments |
| MIN | MIN | Returns the minimum value among the arguments |
| PERCENT_RANK | PERCENT_RANK | Returns the relative rank percentage of a value within a group |
| PERCENTILE_CONT | PERCENTILE_CONT | Inverse distribution function assuming a continuous distribution model |
| PERCENTILE_DISC | PERCENTILE_DISC | Inverse distribution function assuming a discrete distribution model |
| RANK | RANK | Calculates the rank of a value within a group |
| REGR_ (Linear Regression) Functions | Not Supported | Aggregate functions for linear regression |
| STDDEV | STDDEV | Returns the sample standard deviation of a numeric expression |
| STDDEV_POP | STDDEV_POP | Calculates the population standard deviation, the square root of population variance |
| STDDEV_SAMP | STDDEV_SAMP | Calculates the cumulative sample standard deviation, the square root of sample variance |
| SUM | SUM | Returns the sum of values in an expression |
| VAR_POP | VAR_POP | Returns the population variance of a set of numbers after excluding NULL values |
| VAR_SAMP | VAR_SAMP | Returns the sample variance of a set of numbers after excluding NULL values |
| VARIANCE | VARIANCE | Returns the variance of an expression |

### Aggregate Functions

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| APPROX_COUNT_DISTINCT APPROX_COUNT_DISTINCT_AGG APPROX_COUNT_DISTINCT_DETAIL APPROX_MEDIAN APPROX_PERCENTILE APPROX_PERCENTILE_AGG APPROX_PERCENTILE_DETAIL | Not Supported |  |
| CORR_* (CORR_S, CORR_K) | Not Supported | Calculates Pearson’s correlation coefficient |
| GROUP_ID | Not Supported | Distinguishes duplicate groups from specified GROUP BY results |
| GROUPING | GROUPING | Function to distinguish aggregation levels when using ROLLUP, CUBE, GROUPING SETS |
| GROUPING_ID | GROUPING_ID | Returns a number corresponding to the GROUPING bit vector related to the row |
| MEDIAN | MEDIAN | Aggregate/analytic function to find the median value |
| STATS_BINOMIAL_TEST | Not Supported | Exact probability test used for binary variables with only two valid exclusive values |
| STATS_CROSSTAB | Not Supported | Method for analyzing two nominal variables |
| STATS_F_TEST | Not Supported | Tests whether two variances have a significant difference |
| STATS_KS_TEST | Not Supported | Kolmogorov-Smirnov function to test whether two samples come from the same population or distribution |
| STATS_MODE | Not Supported | Returns the value with the highest frequency |
| STATS_MW_TEST | Not Supported | Mann-Whitney test comparing two independent samples |
| STATS_ONE_WAY_ANOVA | STATS_ONE_WAY_ANOVA | Tests for statistically significant differences among means (groups or variables) by comparing two variance estimates |
| STATS_T_TEST_* | Not Supported | t-Test to measure the significance of difference between means |
| STATS_WSR_TEST | Not Supported | Performs Wilcoxon Signed-Rank test for paired samples, testing if differences are significantly different from zero |
| SYS_OP_ZONE_ID | Not Supported | Takes rowid as an argument and returns the zone ID |
| TO_APPROX_COUNT_DISTINCT | Not Supported |  |
| TO_APPROX_PERCENTILE | Not Supported |  |

### Analytic Functions

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| CLUSTER_DETAILS CLUSTER_DISTANCE CLUSTER_ID CLUSTER_PROBABILITY CLUSTER_SET | Not Supported |  |
| FEATURE_DETAILS FEATURE_ID FEATURE_SET FEATURE_VALUE | Not Supported |  |
| FIRST_VALUE * | FIRST_VALUE | Returns the first value in an ordered set |
| LAG | LAG | Refers to the previous value relative to the current row |
| LAST_VALUE * | LAST_VALUE | Returns the last value in an ordered window |
| LEAD | LEAD | Refers to the subsequent value relative to the current row |
| NTH_VALUE * |  | Returns the value at the specified offset row |
| NTILE | NTILE | Divides the output into the user-specified number of groups |
| PREDICTION PREDICTION_COST PREDICTION_DETAILS PREDICTION_PROBABILITY PREDICTION_SET | Not Supported |  |
| RATIO_TO_REPORT | RATIO_TO_REPORT | Calculates the ratio of a value to the sum of the set of values |
| ROW_NUMBER | ROW_NUMBER | Assigns a rank to ordered results within each partition |

### Object Reference Functions

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| DEREF MAKE_REF REF REFTOHEX VALUE | Not Supported | Object Reference Functions |

### Model Functions

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| CV ITERATION_NUMBER PRESENTNNV PRESENTV PREVIOUS | Not Supported | Only usable in the Model_clause of a Select statement |

### OLAP Functions

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| CUBE_TABLE | Not Supported | Convert 3D data into 2D data |

### Data Cartridge Functions

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| DATAOBJ_TO_MAT_PARTITION DATAOBJ_TO_PARTITION | Not Supported | Useful for data cartridge development |

### Pseudocolumns

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| ROWID | Not Supported |  |
| ROWNUM | ROWNUM | Order value of selected ROW, not supported in DML |

### Expressions

---

| Oracle | Altibase | Note |
| --- | --- | --- |
| CASE | CASE, CASE2 | If expr1 is true, returns ret_expr1 |

## Stored Procedure or Function Conversion

---

### In Altibase AUTOCOMMIT mode

---

Procedures are processed as a single transaction. Therefore, COMMIT/ROLLBACK statements inside the procedure are ignored, and an automatic COMMIT occurs after the procedure execution.

In contrast, Oracle executes COMMIT/ROLLBACK inside procedures/functions even in AUTOCOMMIT mode, which may lead to different results from Altibase.

In NON-AUTOCOMMIT mode, procedure execution results are the same between Altibase and Oracle.

| Oracle | Altibase |
| --- | --- |
| ```<br>CREATE OR REPLACE PROCEDURE t1_test( in_t IN INTEGER, in_v IN VARCHAR)<br>IS<br>BEGIN<br>INSERT INTO t1 VALUES(in_t, in_v);<br>ROLLBACK;<br>END;<br>/<br>EXEC t1_test(4, '000004');<br>SQL> SELECT COUNT(*) FROM t1;<br>COUNT(*)<br>-----------------<br>0<br>``` | ```<br>CREATE OR REPLACE PROCEDURE t1_test( in_t IN INTEGER, in_v IN VARCHAR(20))<br>IS<br>BEGIN<br>INSERT INTO t1 VALUES(in_t, in_v);<br>ROLLBACK;<br>END;<br>/<br>EXEC t1_test(4,   '000004');<br>iSQL> SELECT COUNT\(*) FROM t1;<br>COUNT<br>-----------<br>1<br>``` |

### PARAMETER TYPES and RETURN TYPES of PROCEDURE/FUNCTION

---

Oracle’s PARAMETER TYPE and RETURN TYPE do not allow size specification and automatically permit the maximum size.

However, even for the same type, the maximum size in SQL and PL/SQL can differ, as detailed in the table below.

In contrast, Altibase’s PARAMETER TYPE and RETURN TYPE allow size specification.

If size is not specified, the maximum size of PARAMETER TYPE and RETURN TYPE is determined according to the following property settings:

- PSM_PARAM_AND_RETURN_WITHOUT_PRECISION_ENABLE = 0 The size of CHAR, NCHAR, NVARCHAR, VARCHAR is 1.
- PSM_PARAM_AND_RETURN_WITHOUT_PRECISION_ENABLE = 1 (default) The size of CHAR, NCHAR, NVARCHAR, VARCHAR is determined by the property settings in the table below.

#### Maximum size of data types in PROCEDURE/FUNCTION

---

| Data Type | Maximum Size in Oracle SQL | Maximum Size in Oralce PL/SQL | Maximum Size in Altibase SQL | Maximum Size in Altibase PL/SQL | Maximum Size in Altibase PL/SQL When Size Not Specified |
| --- | --- | --- | --- | --- | --- |
| Maximum Size in Oracle SQL | 2000 bytes | 32767 bytes | 32000 bytes | 65534 bytes | PSM_CHAR_DEFAULT_PRECISION (default: 32767) |
| Maximum Size in Oracle PL/SQL | 1000(UTF16), 666(UTF8)<br>최대 2000 bytes | 16383(UTF16), 10922(UTF8)<br>Max 32767 bytes | 16000(UTF16), 10666(UTF8)<br>Max 32000 bytes | 32766(UTF16), 21843(UTF8)<br>Max 65534 bytes | PSM_NCHAR_UTF16_DEFAULT_PRECISION (default: 16383)<br>PSM_NCHAR_UTF8_DEFAULT_PRECISION (default: 10921) |
| Maximum Size in Altibase SQL | 2000 bytes | 32767 bytes |  |  |  |
| Maximum Size in Altibase PL/SQL | 4000 bytes | 32767 bytes | 32000 bytes | 65534 bytes | PSM_VARCHAR_DEFAULT_PRECISION (default: 32767) |
| Maximum Size in Altibase PL/SQL When Size Not Specified | 2000(UTF16), 1333(UTF8)<br>최대 4000 bytes | 16383(UTF16), 10922(UTF8)<br>Max 32767 bytes | 16000(UTF16), 10666(UTF8)<br>Max 32000 bytes | 32766(UTF16), 21843(UTF8)<br>Max 65534 bytes | PSM_NVARCHAR_UTF16_DEFAULT_PRECISION (default: 16383)<br>PSM_NVARCHAR_UTF8_DEFAULT_PRECISION (default: 10921) |
| LONG | 2 GB - 1 | 32760 bytes |  |  |  |
| LONG RAW | 2 GB | 32760 bytes |  |  |  |
| BLOB | (4 GB - 1) * (database block size) | 128 TB | 4 GB - 1 | 100 MB | LOB_OBJECT_BUFFER_SIZE (default: 32000) |
| CLOB | (4 GB - 1) * (database block size) | 128 TB | 4 GB - 1 | 100 MB | LOB_OBJECT_BUFFER_SIZE (default: 32000) |
| NCLOB | (4 GB - 1) * (database block size) | 128 TB |  |  |  |

The maximum size of Oracle's Extended Data Types (MAX_STRING_SIZE = EXTENDED) can be found in this document under 'SQL Conversion Guide -> Data Type Conversion.

### Stored procedures and functions provided for input/output and file control

---

Procedures and functions related to input/output and file control are automatically created under the SYSTEM_ user and defined as public synonyms, so users can call them using only the procedure/function names.

| Category | Oracle | Altibase | Note |
| --- | --- | --- | --- |
| Standard Output | DBMS_OUTPUT.DISABLE | Not Supported |  |
| DBMS_OUTPUT.ENABLE | Not Supported |  |  |
| DBMS_OUTPUT.GET_LINE | Not Supported |  |  |
| DBMS_OUTPUT.GET_LINES | Not Supported |  |  |
| DBMS_OUTPUT.NEW_LINE | DBMS_OUTPUT.NEW_LINE | The DBMS_OUTPUT package in Altibase can be created and used by running the scripts located in $ALTIBASE_HOME/packages |  |
| DBMS_OUTPUT.PUT | DBMS_OUTPUT.PUT | Can be replaced with PRINT in Altibase |  |
| DBMS_OUTPUT.PUT_LINE | DBMS_OUTPUT.PUT_LINE | Can be replaced with PRINTLN in Altibase |  |
| File handling | UTL_FILE.FCLOSE | FCLOSE |  |
| UTL_FILE.FCLOSE_ALL | FCLOSE_ALL |  |  |
| UTL_FILE.FCOPY | FCOPY |  |  |
| UTL_FILE.FFLUSH | FFLUSH |  |  |
| UTL_FILE.FGETATTR | Not Supported |  |  |
| UTL_FILE.FGETPOS | Not Supported |  |  |
| UTL_FILE.FOPEN | FOPEN |  |  |
| UTL_FILE.FOPEN_NCHAR | Not Supported |  |  |
| UTL_FILE.FREMOVE | FREMOVE |  |  |
| UTL_FILE.FRENAME | FRENAME |  |  |
| UTL_FILE.FSEEK | Not Supported |  |  |
| UTL_FILE.GET_LINE | GET_LINE |  |  |
| UTL_FILE.GET_LINE_NCHAR | Not Supported |  |  |
| UTL_FILE.GET_RAW | Not Supported |  |  |
| UTL_FILE.IS_OPEN | IS_OPEN |  |  |
| UTL_FILE.NEW_LINE | NEW_LINE |  |  |
| UTL_FILE.PUT | PUT |  |  |
| UTL_FILE.PUT_LINE | PUT_LINE |  |  |
| UTL_FILE.PUT_LINE_NCHAR | Not Supported |  |  |
| UTL_FILE.PUT_NCHAR | Not Supported |  |  |
| UTL_FILE.PUTF | Not Supported |  |  |
| UTL_FILE.PUTF_NCHAR | Not Supported |  |  |
| UTL_FILE.PUT_RAW | Not Supported |  |  |

### DBMS_RANDOM conversion

---

Altibase supports the RANDOM function in addition to the DBMS_RANDOM package.

| Oracle | Altibase | Note |
| --- | --- | --- |
| DBMS_RANDOM.NORMAL | Not supported | Returns a random number from a normal distribution |
| DBMS_RANDOM.SEED | DBMS_RANDOM.SEED | Resets the seed; can be replaced with Altibase’s RANDOM(seed) function |
| DBMS_RANDOM.STRING | DBMS_RANDOM.STRING | Returns a random string |
| DBMS_RANDOM.VALUE | DBMS_RANDOM.VALUE | Returns a random number; can be replaced with Altibase’s RANDOM(0) function |
| DBMS_RANDOM.INITIALIZE | DBMS_RANDOM.INITIALIZE | Procedure to initialize the package; deprecated in Oracle |
| DBMS_RANDOM.RANDOM | DBMS_RANDOM.RANDOM | Generates a random number; deprecated in Oracle |
| DBMS_RANDOM.TERMINATE | Not supported | Procedure to terminate the package; deprecated in Oracle |

### WHERE CURRENT OF clause

---

The WHERE CURRENT OF clause using Oracle’s CURSOR needs to be converted as follows in Altibase.

| Oracle | Altibase |
| --- | --- |
| ```<br>CREATE OR REPLACE PROCEDURE proc1<br>IS<br>CURSOR emp_list IS<br>SELECT empno FROM employee<br>WHERE empno = 1 FOR UPDATE;<br>BEGIN FOR emplst IN emp_list LOOP<br>UPDATE employee SET empjob = 'SALESMAN'<br>WHERE CURRENT OF emp_list;<br>END LOOP;<br>END;<br>/<br>``` | ```<br>CREATE OR REPLACE PROCEDURE proc1<br>AS<br>BEGIN<br>DECLARE CURSOR cur1 IS<br>SELECT empno FROM employee<br>WHERE empno = 1;<br>v_empjob VARCHAR(10);<br>v_empno INTEGER;<br>BEGIN<br>OPEN cur1;<br>LOOP FETCH cur1 INTO v_empno;<br>EXIT WHEN cur1%NOTFOUND;<br>UPDATE employee SET empjob = 'SALESMAN' WHERE empno = v_empno; //emp_no가 PK이어야 한다.<br>END LOOP;<br>CLOSE cur1;<br>END;<br>END;<br>/<br>``` |

### EXCEPTION

---

Oracle and Altibase have predefined exceptions in the system for those that occur in stored PROCEDUREs/FUNCTIONs.

| Oracle | Altibase |  |  |  |
| --- | --- | --- | --- | --- |
| **SQLERRM** | **SQLCODE** | **SQLERRM** | **SQLCODE(integer)** | **SQLCODE(hexadecimal)** |
| ACCESS_INTO_NULL | -6530 |  | Not Supported |  |
| CASE_NOT_FOUND | -6592 |  | Not Supported |  |
| COLLECTION_IS_NULL | -6531 |  | Not Supported |  |
| CURSOR_ALREADY_OPEN | -6511 | CURSOR_ALREADY_OPEN | 201062 | 31166 |
| DUP_VAL_ON_INDEX | -1 | DUP_VAL_ON_INDEX | 201063 | 31167 |
| INVALID_CURSOR | -1001 | INVALID_CURSOR | 201064 | 31168 |
| INVALID_NUMBER | -1722 | INVALID_NUMBER | 201065 | 31169 |
| LOGIN_DENIED | -1017 |  | Not Supported |  |
| NO_DATA_FOUND | +100 | NO_DATA_FOUND | 201066 | 3116A |
| NO_DATA_NEEDED | -6548 |  | Not Supported |  |
| NOT_LOGGED_ON | -1012 |  | Not Supported |  |
| PROGRAM_ERROR | -6501 | PROGRAM_ERROR | 201067 | 3116B |
| ROWTYPE_MISMATCH | -6504 |  | Not Supported |  |
| SELF_IS_NULL | -30625 |  | Not Supported |  |
| STROAGE_ERROR | -6500 | STORAGE_ERROR | 201068 | 3116C |
| SUBSCRIPT_BEYOND_COUNT | -6533 |  | Not Supported |  |
| SUBSCRIPT_OUTSIDE_LIMIT | -6532 |  | Not Supported |  |
| SYS_INVALID_ROWID | -1410 |  | Not Supported |  |
| TIMEOUT_ON_RESOURCE | -51 | TIMEOUT_ON_RESOURCE | 201069 | 3116D |
| TOO_MANY_ROWS | -1422 | TOO_MANY_ROWS | 201070 | 3116E |
| VALUE_ERROR | -6502 | VALUE_ERROR | 201071 | 3116F |
| ZERO_DIVIDE | -1476 | ZERO_DIVIDE | 201072 | 31170 |

# Database Migration Procedure

---

To migrate a database from Oracle to Altibase, you can use the MigrationCenter tool, which automatically performs object conversion and data migration. Before starting the migration, users and tablespaces need to be created in the source database environment to support mapping. Features dependent on Oracle, non-standard functions, or those not supported by Altibase must be converted manually.

![image2025-10-1%209:55:39.png](https://docs.altibase.com/download/attachments/embedded-page/arch/ORACLE%20to%20ALTIBASE%20Conversion%20Guide/image2025-10-1%209:55:39.png?api=v2)

## Data Migration and Application Conversion Procedure

---

![image2025-10-1%2011:3:11.png](https://docs.altibase.com/download/attachments/embedded-page/arch/ORACLE%20to%20ALTIBASE%20Conversion%20Guide/image2025-10-1%2011:3:11.png?api=v2)

## Data Integrity Verification

---

| APPLICATION 검증 | Deriving Verification Plan<br>- Derive the verification plan through prior consultation with the client Example: Online screen capture or report comparison, batch report comparison, etc. |
| --- | --- |
| DATA검증 | Migration Center Report<br>- Compare the total number of table records between the source database and Altibase using the migration result report<br>Deriving Verification Plan<br>- Derive the verification plan through prior consultation with the client Examples: Verify total record counts, Compare sum of data in specific columns, Compare results of specific query executions |

## Contingency Plan for Database Migration Failures

---

![image2025-10-1%2011:10:52.png](https://docs.altibase.com/download/attachments/embedded-page/arch/ORACLE%20to%20ALTIBASE%20Conversion%20Guide/image2025-10-1%2011:10:52.png?api=v2)

## Database Migration Tool

---

When migrating from Oracle to Altibase, the automatic migration tool MigrationCenter is used.

1.

### 1) Advantages of MigrationCenter

---

- Easy to use with a GUI-based interface
- Supports CLI mode for easy execution of migration tasks and high performance
- Migrates schema and data together in a single operation
- Performs migration through mapping between different data types
- Supports user-defined data types for flexible data migration
- Provides step-by-step summary reports of migration results

### 2) How to Use

---

#### (1) Add Database Connection

---

Enter the information for the Source/Target Database

- Connection Name: Can be set arbitrarily
- IP: Database Server IP
- Port: Database Server Port
- User: Connection user account
- Password: Connection user password
- SID: Service name
- IP Version: IPv4/IPv6

![image2025-9-26%2014:30:20.png](https://docs.altibase.com/download/attachments/embedded-page/arch/ORACLE%20to%20ALTIBASE%20Conversion%20Guide/image2025-9-26%2014:30:20.png?api=v2)

Since JDBC drivers are used to connect to the databases, it is important to prepare the appropriate JDBC drivers for both the source and target databases.

For user convenience, MigrationCenter provides several JDBC drivers suitable for supported databases.

#### (2) Create Project

---

Create a project for data migration.

- Project Name: Can be set arbitrarily
- Project Path: Automatically generated
- Source Database: Oracle
- Destination Database: Altibase

![image2025-9-26%2014:36:18.png](https://docs.altibase.com/download/attachments/embedded-page/arch/ORACLE%20to%20ALTIBASE%20Conversion%20Guide/image2025-9-26%2014:36:18.png?api=v2)

#### (3) Connect

---

Connect to both the source and target databases.

![image2025-9-26%2014:39:53.png](https://docs.altibase.com/download/attachments/embedded-page/arch/ORACLE%20to%20ALTIBASE%20Conversion%20Guide/image2025-9-26%2014:39:53.png?api=v2)

#### (4) Build Project

---

- Build User: Collects information on all migratable objects owned by the user connected to the source database.
- Build Table: Manually constructs a list of tables to migrate from the tables owned by the user connected to the source database. Collects object information for the selected tables and their dependent constraints and indexes.

Choose the method (Fast/Slow) to retrieve the record count of tables from the source database and proceed.

![image2025-9-26%2014:51:58.png](https://docs.altibase.com/download/attachments/embedded-page/arch/ORACLE%20to%20ALTIBASE%20Conversion%20Guide/image2025-9-26%2014:51:58.png?api=v2)

#### (5) Reconcile Project

---

This is the step where the migration execution method is defined, and it is the most important phase in the migration process.

![image2025-9-26%2014:55:52.png](https://docs.altibase.com/download/attachments/embedded-page/arch/ORACLE%20to%20ALTIBASE%20Conversion%20Guide/image2025-9-26%2014:55:52.png?api=v2)

- Data Type Mapping: Mapping data types between Oracle and Altibase
- PSM Data Type Mapping: Mapping data types between Oracle PL/SQL and Altibase PSM
- Tablespace to Tablespace Mapping: Mapping tablespaces between Oracle and Altibase
- Table to Tablespace Mapping: Specifying the tablespace where Altibase tables will be stored
- Select Editing: Adding or modifying data retrieval conditions for Oracle data
- DDL Editing: Editing the final DDL for Altibase

![image2025-9-26%2014:56:24.png](https://docs.altibase.com/download/attachments/embedded-page/arch/ORACLE%20to%20ALTIBASE%20Conversion%20Guide/image2025-9-26%2014:56:24.png?api=v2)

#### (6) Run Project

---

Perform the data migration.

![image2025-9-26%2014:59:51.png](https://docs.altibase.com/download/attachments/embedded-page/arch/ORACLE%20to%20ALTIBASE%20Conversion%20Guide/image2025-9-26%2014:59:51.png?api=v2)

#### (7) PL/SQL Converter Tool

---

Use MigrationCenter to modify the syntax related to data types in Oracle PL/SQL files saved as files. Since business logic is not automatically converted, developers need to manually convert it.
