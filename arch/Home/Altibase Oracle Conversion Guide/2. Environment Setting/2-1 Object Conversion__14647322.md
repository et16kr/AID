---
title: "2-1 Object Conversion"
page_id: "14647322"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/2-1+Object+Conversion"
updated_at: "2021-02-18T17:46:00.000+0900"
version: 7
ancestors: ["Home", "Altibase Oracle Conversion Guide", "2. Environment Setting"]
labels: []
---

# 2-1 Object Conversion
Source: https://docs.altibase.com/display/arch/2-1+Object+Conversion
Updated: 2021-02-18T17:46:00.000+0900

## **- #id-2-1ObjectConversion- - [DATATYPE](#id-2-1ObjectConversion-DATATYPE) - [Object Comparison](#id-2-1ObjectConversion-ObjectComparison) - [CREATE TABLESPACE](#id-2-1ObjectConversion-CREATETABLESPACE) - [DATA TABLESPACE](#id-2-1ObjectConversion-DATATABLESPACE) - [Example of DATA TABLESPACE](#id-2-1ObjectConversion-ExampleofDATATABLESPACE) - [TEMPORARY TABLESPACE](#id-2-1ObjectConversion-TEMPORARYTABLESPACE) - [Example of TEMPORARY TABLESPACE](#id-2-1ObjectConversion-ExampleofTEMPORARYTABLESPACE) - [UNDO TABLESPACE](#id-2-1ObjectConversion-UNDOTABLESPACE) - [CREATE TABLE](#id-2-1ObjectConversion-CREATETABLE) - [COLUMN DEFINITION Clause](#id-2-1ObjectConversion-COLUMNDEFINITIONClause) - [SEGMENT ATTRIBUTES Clause](#id-2-1ObjectConversion-SEGMENTATTRIBUTESClause) - [STORAGE Clause](#id-2-1ObjectConversion-STORAGEClause) - [LOB STORAGE Clause](#id-2-1ObjectConversion-LOBSTORAGEClause) - [TABLE PARTITION Clause](#id-2-1ObjectConversion-TABLEPARTITIONClause) - [TABLE PROPERTIES Clause](#id-2-1ObjectConversion-TABLEPROPERTIESClause) - [Example of TABLE conversion](#id-2-1ObjectConversion-ExampleofTABLEconversion) - [CREATE INDEX](#id-2-1ObjectConversion-CREATEINDEX) - [Example of INDEX conversion](#id-2-1ObjectConversion-ExampleofINDEXconversion) - [CREATE VIEW](#id-2-1ObjectConversion-CREATEVIEW) - [CREATE TRIGGER](#id-2-1ObjectConversion-CREATETRIGGER) - [CREATE SEQUENCE](#id-2-1ObjectConversion-CREATESEQUENCE) - [CREATE SYNONYM](#id-2-1ObjectConversion-CREATESYNONYM) - [ALTER TABLE](#id-2-1ObjectConversion-ALTERTABLE)**

---

## **DATATYPE**

| **Classification** | **Oracle** | **ALTIBASE** | Remark |
| --- | --- | --- | --- |
| Character Type | CHAR | CHAR | Up to 32K |
| VARCHAR2,VARCHAR | VARCHAR2,VARCHAR | Up to 32K. When querying by DESC, query by VARCHAR |  |
| NCHAR | NCHAR | Character length up to 16000B (UTF16), character length up to 10666B (UTF8) |  |
| NVARCHAR2 | NVARCHAR | Character length up to 16000B (UTF16), character length up to 10666B (UTF8) |  |
| LONG | CLOB | Up to 2G |  |
| LOB Type | BLOB | BLOB | Up to 2G |
| CLOB | CLOB | Up to 2G |  |
| NCLOB | CLOB | Up to 2G |  |
| Numeric Type | NUMERIC(p, s) | NUMERIC(p, s) | If data can be specified as a native type such as SMALLINT, INTEGER, BIGINT, REAL, DOUBLE, etc., it is recommended to specify it as a native type. This is because overhead due to conversion cost can be reduced during data processing, and the efficiency of storage space is improved. |
| NUMBER (p, s) | NUMBER(p, s) |  |  |
| DECIMAL(p, s) | DECIMAL(p, s) |  |  |
| FLOAT(p),BINARY_FLOAT | FLOAT(p) |  |  |
| SMALLINT | SMALLINT | 2 Byte integer type |  |
| INT | INTEGER | 4 Byte integer type |  |
| REAL | REAL | 4 Byte integer type |  |
| BINARY_DOUBLE | DOUBLE | 8 Byte integer type |  |
| Date Type | DATE | DATE | ALTIBASE HDB DATE type includes the expression range of ORACLE DATE type |
| INTERVAL YEARTO MONTH | - | Not supported |  |
| INTERVAL DAYTO SECOND | - |  |  |
| TIMESTAMP WITH TIME ZONE | - |  |  |
| TIMESTAMP WITH LOCAL TIME ZONE | - |  |  |
| TIMESTAMP | TIMESATAMP |  |  |
| Binary Type | BFILE | BLOB | Up to 2G |
| RAW (size) | BLOB |  |  |
| LONG RAW | BLOB |  |  |

## **Object Comparison**

|  |  |
| --- | --- |
| **Oracle** | **ALTIBASE** |
| CLUSTER | Not supported |
| CONSTRAINT | Supported |
| DATABASE LINK | Supported |
| DATABASE TRIGGER | Supported |
| DIMENSION | Not supported |
| EXTERNAL PROCEDURE LIBRARY | Supported (Only C/C++) |
| INDEX-ORGANIZED TABLE | Not supported |
| INDEX | B-TREE, R-TREE, Function based supported(BITMAP, CLUSTER, Global Partitioned INDEX are not supported) |
| INDEXTYPE | Not supported |
| JAVA related object | Not supported |
| MATERIALIZED VIEW | Supported |
| MATERIALIZED VIEW LOG | Not supported |
| OBJECT TABLE | Not supported |
| OBJECT TYPE | Not supported |
| OBJECT VIEW | Not supported |
| OPERATOR | Not supported |
| PACKAGE | Supported |
| SEQUENCE | Supported |
| STORED FUNCTION/PROCEDURE | Supported |
| SYNONYM | Supported |
| TABLE | Supported |
| VIEW | Supported |
| CONTEXT | Not supported |
| DIRECTORY | Supported |
| PARAMETER FILE | Not supported as an object. Supported by altibase.properties file |
| PROFILE | Not supported |
| ROLE | Supported |
| TABLESPACE | MEMORY, DISK, VOLATILE, TEMPORARY, UNDO are supported |
| USER | Supported |

## **CREATE TABLESPACE**

Date tablespaces of the Oracle are all disk tablespaces. When converting to ALTIBASE HDB, disk tablespaces must be created using the CREATE DISK TABLESPACE statement.

### DATA TABLESPACE

|  |  |  |
| --- | --- | --- |
| **Oracle** | **ALTIBASE** | **Remark** |
| BIGFILE\|SMALLFILE | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| DATAFILE File Specification | DATAFILE File Specification |  |
| MINIMUM EXTENT | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| BLOCKSIZE | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| LOGGING\|NOLOGGING | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| FORCE LOGGING | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| DEFAULT Storage Statement | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| ONLINE\|OFFLINE | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| EXTENT MANAGEMENT LOCAL\|DICTIONARY | - |  |
| SEGMENT SPACE MANAGEMENT AUTO\|MANUAL | SEGMENT MANAGEMENT AUTO\|MANUAL |  |
| FLASHBACK ON\|OFF | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |

### Example of DATA TABLESPACE

|  |  |
| --- | --- |
| **Oracle** | **ALTIBASE** |
| ```<br>CREATE   TABLESPACE TESTDATA<br>DATAFILE   'testdata01.dbf'<br>SIZE   1024M<br>AUTOEXTEND   ON<br>NEXT   50M<br>MAXSIZE   UNLIMITED<br>LOGGING<br>ONLINE<br>EXTENT MANAGEMENT LOCAL AUTOALLOCATE<br>BLOCKSIZE 8K<br>SEGMENT   SPACE MANAGEMENT MANUAL<br>FLASHBACK ON;<br>``` | ```<br>CREATE   TABLESPACE TESTDATA<br>DATAFILE   'testdata01.dbf'<br>SIZE   1024M<br>AUTOEXTEND ON<br>NEXT   50M<br>MAXSIZE   UNLIMITED<br>SEGMENT MANAGEMENT MANUAL;<br>``` |

 Modify the SEGMENT clause with the SEGMENT MANAGEMENT AUTO|MANUAL clause and delete all other clauses as they are not supported.

### TEMPORARY TABLESPACE

|  |  |  |
| --- | --- | --- |
| **Oracle** | **ALTIBASE** | **Remark** |
| TABLESPACE GROUP | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| EXTENT MANAGEMENT LOCAL\|DICTIONARY | - |  |

### Example of TEMPORARY TABLESPACE

|  |  |
| --- | --- |
| **Oracle** | **ALTIBASE** |
| ```<br>CREATE TEMPORARY TABLESPACE   tbs_temp_02<br>TEMPFILE 'temp02.dbf' SIZE   5M AUTOEXTEND ON<br>TABLESPACE GROUP   tbs_grp_01;<br>``` | ```<br>CREATE TEMPORARY TABLESPACE   tbs_temp_02<br>TEMPFILE   'temp02.dbf' SIZE 5M AUTOEXTEND ON;<br>``` |

 Deleted because the TABLESPACE GROUP clause is not supported.

### UNDO TABLESPACE

ALTIBASE automatically manages Undo Tablespace by the system. The user can only add and resize data files to the Undo Tablespace.

|  |  |
| --- | --- |
| **Oracle** | **ALTIBASE** |
| ```<br>CREATE UNDO TABLESPACE UNDOTBS2<br>DATAFILE ‘undotbs2.dbf'<br>SIZE 500M<br>AUTOEXTEND ON<br>NEXT 5M<br>MAXSIZE UNLIMITED;<br>``` | ```<br>ALTER TABLESPACE SYS_TBS_DISK_UNDO<br>ADD DATAFILE 'undotbs2.dbf'<br>SIZE 500M<br>AUTOEXTEND ON<br>NEXT 5M<br>MAXSIZE UNLIMITED;<br>``` |

## **CREATE TABLE**

ALTIBASE HDB does not provide Temporary Table, Object Table, or XMLType Table. ALTIBASE HDB provides a Memory Table. By grasping the characteristics of an existing table, it can be divided into a memory table or a disk table. However, the options used in the CREATE TABLE statement used in Oracle when creating a memory table cannot be used. In addition, when specifying Segment related contents when creating a table, you must specify the tablespace -> specify PCTFREE/PCTUSED -> specify INITRANS/MAXTRANS -> Storage clause -> Logging clause.

### COLUMN DEFINITION Clause

|  |  |  |
| --- | --- | --- |
| **Oracle** | **ALTIBASE** | **Remark** |
| SORT | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| DEFAULT | DEFAULT |  |
| ENCRYPT | ENCRYPT |  |
| Constraint statement | Constraint statement | Because ALTIBASE HDB does not provide an ON DELETE SET NULL (ON DELETE CASCADE is supported) option in the reference clauses, these are deleted. In ALTIBASE HDB, when the PRIMARY KEY and UNIQUE are specified, only the Tablespace clause, Parallel clause, Logging clause, and Force clause can be specified in the Using Index clause. That is, the index name and CREATE INDEX clause are not provided. |
| Ref Constraint statement | - | Since the REF column is not supported by ALTIBASE HDB, the option is deleted during conversion |
| ORGANIZATION | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| CLUSTER | - |  |
| COMPRESS\|NOCOMPRESS | COMPRESS\|NOCOMPRESS |  |
| Byte keyword can be specified when specifying column size | Byte keyword is not provided when specifying column size | Oracle can specify the byte keyword when specifying the size of the column, but ALTIBASE HDB does not provide byte when specifying the size. ex) ORACLE : c1 VARCHAR2(10 Byte) => ALTIBASE : c1 VARCHAR2(10) |

 When specifying the PRIMARY KEY, UNIQUE Constraint, and specifying the INDEX attribute using the USING INDEX clause, ALTIBASE HDB can only specify the TABLESPACE clause, PARALLEL/NOPARALLEL clause, and LOGGING/NOLOGGING clause. That is, storage-related properties cannot be specified.

### SEGMENT ATTRIBUTES Clause

|  |  |  |
| --- | --- | --- |
| **Oracle** | **ALTIBASE** | **Remark** |
| TABLESPACE | TABLESPACE |  |
| PCTFREE | PCTFREE |  |
| PCTUSED | PCTUSED |  |
| INITRANS | INITRANS |  |
| MAXTRANS | MAXTRANS | Change 255 to 120. Oracle's MAXTRANS is Deprecate, and its value is always 255. On the other hand, the MAXTRANS value of ALTIBASE can be specified up to 120, so change it to 120. |
| LOGGING\|NOLOGGING | LOGGING\|NOLOGGING |  |

### STORAGE Clause

|  |  |  |
| --- | --- | --- |
| **Oracle** | **ALTIBASE** | **Remark** |
| INITIAL | INITEXTENTS | Bytes -> change to the number of extents |
| NEXT | NEXTEXTENTS | Bytes -> change to the number of extents |
| MINEXTENTS | MINEXTENTS |  |
| MAXEXTENTS | MAXEXTENTS |  |
| PCTINCREASE | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| FREELISTS | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| FREELIST | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| OPTIMAL | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| BUFFER POOL | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |

### LOB STORAGE Clause

|  |  |  |
| --- | --- | --- |
| **Oracle** | **ALTIBASE** | **Remark** |
| TABLESPACE | TABLESPACE | Only TABLESPACE can be specified in the LOB STORAGE clause of ALTIBASE. |
| STORAGE | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| CHUNK | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| PCTVERSION | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| RETENTION | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| FREEPOOLS | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| CACHE | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| STORAGE IN ROW | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| LOGGING\|NOLOGGING | LOGGING\|NOLOGGING |  |

### TABLE PARTITION Clause

|  |  |  |
| --- | --- | --- |
| **Oracle** | **ALTIBASE** | **Remark** |
| PARTITION BY RANGE | PARTITION BY RANGE |  |
| PARTITION BY HASH | PARTITION BY HASH |  |
| PARTITION BY LIST | PARTITION BY LIST |  |
| Composite partitioning statement | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |

### TABLE PROPERTIES Clause

|  |  |  |
| --- | --- | --- |
| **Oracle** | **ALTIBASE** | **Remark** |
| ENABLE\|DISABLE ROW MOVEMENT | ENABLE\|DISABLE ROW MOVEMENT | Only Supported for partitioned table |
| NOPARALLEL\|PARALLEL | NOPARALLEL\|PARALLEL |  |
| ENABLE\|DISABLE VALIDATE\|NOVALIDATE | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |

### Example of TABLE conversion

|  |  |
| --- | --- |
| **Oracle** | **ALTIBASE** |
| ```<br>CREATE TABLE "SCOTT"."EMP"<br>(   "EMPNO" NUMBER(4,0),<br>"ENAME" VARCHAR2(10 Byte),<br>"JOB" VARCHAR2(9 Byte),<br>"MGR" NUMBER(4,0),<br>"HIREDATE" DATE,<br>"SAL" NUMBER(7,2),<br>"COMM" NUMBER(7,2),<br>"DEPTNO" NUMBER(2,0),<br>CONSTRAINT "PK_EMP" PRIMARY KEY ("EMPNO")<br>USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS<br>STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645<br>PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT)<br>TABLESPACE "USERS" ENABLE,<br>CONSTRAINT "FK_DEPTNO" FOREIGN KEY ("DEPTNO")<br>REFERENCES "SCOTT"."DEPT" ("DEPTNO") ENABLE<br>) PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING<br>STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645<br>PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT)<br>TABLESPACE "USERS" ;<br>``` | ```<br>CREATE TABLE "SCOTT"."EMP"<br>(   "EMPNO" NUMBER(4,0),<br>"ENAME" VARCHAR2(10),<br>"JOB" VARCHAR2(9),<br>"MGR" NUMBER(4,0),<br>"HIREDATE" DATE,<br>"SAL" NUMBER(7,2),<br>"COMM" NUMBER(7,2),<br>"DEPTNO" NUMBER(2,0),<br>CONSTRAINT "PK_EMP" PRIMARY KEY ("EMPNO")<br>USING INDEX TABLESPACE "USERS" ,<br>CONSTRAINT "FK_DEPTNO" FOREIGN KEY ("DEPTNO")<br>REFERENCES "SCOTT"."DEPT" ("DEPTNO")<br>)<br>TABLESPACE "USERS"<br>PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 120<br>STORAGE(INITEXTENTS 1 NEXTEXTENTS 1 MINEXTENTS 1 MAXEXTENTS 2147483645)<br>LOGGING ;<br> Delete "ENAME" VARCHAR2(10 Byte)Byte<br> When specifying USING INDEX TABLESPACE "USERS" PK, only the TABLESPACE clause, PARALLEL/NOPARALLEL clause, and LOGGING/NOLOGGING clause can be specified in the USING INDEX clause, so other options other than the TABLESPACE clause are deleted.<br> REFERENCES "SCOTT"."DEPT" ("DEPTNO")<br>When FK is specified, delete because ENABLE option is not supported.<br> PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 120<br>The maximum value of MAXTRANS is 120, so modify it to 120<br>STORAGE (INITEXTENTS 1 NEXTEXTENTS 1 MINEXTENTS 1 MAXEXTENTS 2147483645)<br>INITIAL and NEXT must be changed to INITEXTENTS and NEXTEXTENTS, respectively, and the value is also modified to the number of extents.<br>   TABLESPACE "USERS"<br>PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 120<br>STORAGE...<br>LOGGING<br>When specifying segment-related content, specify TABLESPACE -> PCTFREE/PCTUSED -> INITRANS/MAXTRANS -> Storage clause -> logging clause.<br>``` |

## **CREATE INDEX**

ALTIBASE only provides BTREE and RTREE INDEX, but does not provide BITMAP, CLUSTER, Function based, REVERSE, and Global partitioned INDEX. In addition, when creating ALTIBASE INDEX, when specifying segment-related content, specify in the order of TABLESPACE -> PARALLEL/NOPARALLEL -> LOGGING/NOLOGGING -> storage clause.

|  |  |  |
| --- | --- | --- |
| **Oracle** | **ALTIBASE** | **Remark** |
| TABLESPACE | TABLESPACE |  |
| LOGGING\|NOLOGGING | LOGGING\|NOLOGGING |  |
| NOPARALLEL\|PARALLEL | NOPARALLEL\|PARALLEL |  |
| COMPUTE STATISTICS | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| REVERSE | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| SORT\|NOSORT | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| ONLINE | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| COMPRESS\|NOCOMPRESS | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| PCTFREE, PCTUSED, | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| INITRANS | INITRANS | \| |
| MAXTRANS | MAXTRANS | ALTIBASE supports up to 30 |
| Storage statement | Same as the storage statement of TABLE |  |

### Example of INDEX conversion

|  |  |
| --- | --- |
| **Oracle** | **ALTIBASE** |
| ```<br>CREATE INDEX "SCOTT"."EMP_IDX1" ON "SCOTT"."EMP" ("DEPTNO", "SAL")<br>PCTFREE 10 INITRANS 2 MAXTRANS 255 COMPUTE STATISTICS<br>STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645<br>PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT)<br>TABLESPACE "USERS" ;<br>``` | ```<br>CREATE INDEX "SCOTT"."EMP_IDX1" ON "SCOTT"."EMP" ("DEPTNO", "SAL")<br>TABLESPACE "USERS"<br>INITRANS 2 MAXTRANS 30<br>STORAGE(INITEXTENTS 1 NEXTEXTENTS 1 MINEXTENTS 1 MAXEXTENTS 2147483645) ;<br>1. INITRANS 2 MAXTRANS 30<br>MAXTRANS supports up to 30, so change it to 30<br>2. STORAGE(INITEXTENTS 1 NEXTEXTENTS 1 MINEXTENTS 1 MAXEXTENTS 2147483645) ;<br>Only INITEXTENTS, NEXTEXTENTS, MINEXTENTS, and MAXEXTENTS can be specified in the STORAGE clause, and INITIAL and NEXT must be changed to INITEXTENTS and NEXTEXTENTS, respectively, and the value must be modified with the number of extents.<br>3. TABLESPACE "USERS"<br>INITRANS 2 MAXTRANS 30<br>STORAGE ... ;<br>When specifying segment-related content, specify TABLESPACE -> PARALLEL/NOPARALLEL -> LOGGING/NOLOGGING -> storage clause<br>``` |

## **CREATE VIEW**

ALTIBASE VIEW is created with the CREATE or REPLACE view statement, the same as Oracle's View creation statement.

| **Oracle** | **ALTIBASE** | Remark |
| --- | --- | --- |
| WITH READ ONLY | WITH READ ONLY | ALTIBASE provides only VIEW with the WITH READ ONLY OPTION, so the option is default. |
| [DOCKI:NO] FORCE | [DOCKI:NO] FORCE |  |
| WITH CHECK OPTION | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| XMLType view statement | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |
| Object view statement | - | Since it is not supported by ALTIBASE HDB, the option is deleted during conversion. |

## **CREATE TRIGGER**

ALTIBASE TRIGGER is created with the CREATE OR REPLACE TRIGGER syntax in the same way as Oracle's TRIGGER creation syntax. Change of table data reflected due to redundancy does not trigger action. ALTIBASE cannot contain LOB columns in the TRIGGER target table.

|  |  |  |
| --- | --- | --- |
| **Oracle** | **ALTIBASE** | **Remark** |
| CREATE OR REPLACE TRIGGER | CREATE OR REPLACE TRIGGER |  |
| BEFORE\|AFTER\|INSTEAD OF | BEFORE\|AFTER | ALTIBASE does not support INSTEAD OF |
| DML event statement | DML event syntax | DML event syntax is the same as Oracle |
| DDL event statement | - | ALTIBASE does not provide DDL TRIGGER |
| WHEN condition | WHEN condition |  |
| FOR EACH ROW | FOR EACH ROW |  |
| REFERENCING | REFERENCING | In DELETE event, NEW cannot be REFERENCING, and in INSERT event, OLD cannot be REFERENCING. When an alias is given to OLD/NEW, OLD/NEW is a keyword and cannot be used as an alias. |
| Trigger body statement | Trigger body statement | The ALTIBASE Trigger body statement must begin with the AS BEGIN statement. In addition, Oracle's trigger body syntax can begin with a DECLARE clause, but ALTIBASE's trigger body must specify the declaration part in the AS clause, and the DECLARE clause cannot be specified. When using the OLD/NEW row,':' cannot be used. Ex) :old (x) -> old(o) |

## **CREATE SEQUENCE**

The statement of CREATE SEQUENCE in ALTIBASE is the same as in Oracle. However, ORDER and NOORDER options provided by Oracle are not supported. In addition, the maxvalue of ORACLE SEQUENCE can be specified up to 28 digit integers, but the maxvalue of ALTIBASE SEQUENCE can be specified within the range of (-9223372036854775807) to 9223372036854775806.

## **CREATE SYNONYM**

The statement of CREATE SYNONYM in ALTIBASE is the same as in Oracle

## **ALTER TABLE**

In ALTIBASE, only one constraint can be added at a time when Constraint is added.

In Oracle “ALTER TABLE ADD (CONSTRAINT constraint_name constraint_type,…);” Sentences that add multiple constraints with a statement are divided by constraints, and “ALTER TABLE ADD CONSTRAINT constraint_name constraint_type;” It should be executed by separating it by constraint by the statement.

In Oracle, when PRIMARY KEY and UNIQUE are specified, INDEX can be created in advance and then specified, but ALTIBASE internally creates INDEX at the time constraint is specified, so only one of PK Constraint, UNIQUE Constraint, and INDEX can be created for the same column. Do it. In other words, PK Constraint cannot be specified for the column that created INDEX.
