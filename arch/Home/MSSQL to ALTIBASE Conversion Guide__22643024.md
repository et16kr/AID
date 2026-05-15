---
title: "MSSQL to ALTIBASE Conversion Guide"
page_id: "22643024"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/MSSQL+to+ALTIBASE+Conversion+Guide"
updated_at: "2025-10-21T09:28:09.000+0900"
version: 1
ancestors: ["Home"]
labels: []
---

# MSSQL to ALTIBASE Conversion Guide
Source: https://docs.altibase.com/display/arch/MSSQL+to+ALTIBASE+Conversion+Guide
Updated: 2025-10-21T09:28:09.000+0900

- [Overview](#MSSQLtoALTIBASEConversionGuide-Overview) - [Considerations When Converting SQL Server Schema](#MSSQLtoALTIBASEConversionGuide-ConsiderationsWhenConvertingSQLServerSchema) - [Object Conversion](#MSSQLtoALTIBASEConversionGuide-ObjectConversion) - [DATATYPE](#MSSQLtoALTIBASEConversionGuide-DATATYPE) - [FUNCTION & EXPRESSION](#MSSQLtoALTIBASEConversionGuide-FUNCTION&EXPRESSION) - [OBJECT](#MSSQLtoALTIBASEConversionGuide-OBJECT) - [CREATE TABLESPACE](#MSSQLtoALTIBASEConversionGuide-CREATETABLESPACE) - [CREATE TABLE](#MSSQLtoALTIBASEConversionGuide-CREATETABLE) - [CREATE USER](#MSSQLtoALTIBASEConversionGuide-CREATEUSER) - [CREATE INDEX](#MSSQLtoALTIBASEConversionGuide-CREATEINDEX) - [SQL Conversion](#MSSQLtoALTIBASEConversionGuide-SQLConversion) - [JOIN](#MSSQLtoALTIBASEConversionGuide-JOIN) - [Execution Query](#MSSQLtoALTIBASEConversionGuide-ExecutionQuery) - [Temporary Table](#MSSQLtoALTIBASEConversionGuide-TemporaryTable) - [Control Statement](#MSSQLtoALTIBASEConversionGuide-ControlStatement) - [Identity Attribute](#MSSQLtoALTIBASEConversionGuide-IdentityAttribute) - [Procedure Conversion](#MSSQLtoALTIBASEConversionGuide-ProcedureConversion) - [Using Cursor](#MSSQLtoALTIBASEConversionGuide-UsingCursor) - [Exception Code](#MSSQLtoALTIBASEConversionGuide-ExceptionCode)

# Overview

---

This document explains the considerations and methods for migrating from Microsoft SQL Server to ALTIBASE.

It targets SQL Server 2016 and Altibase version 7.1 or later.

For errors and improvements related to this document, contact the technical support portal or technical support center.

- Technical support portal: [http://support.altibase.com](http://support.altibase.com/) > Technical Knowledge > Q&A
- Technical support center: 02-2082-1114

This document is provided for informational purposes only and may be changed without prior notice. It may contain errors, and there is no explicit or implicit liability for commercial use or suitability for specific purposes.

The timing of development or release of the features and functions of Altibase products included in this document is at Altibase’s discretion.

Altibase may hold patents, trademarks, copyrights, or other intellectual property rights related to this document.

# Considerations When Converting SQL Server Schema

---

The schema in SQL Server is a container for objects (a logical namespace).

In Altibase, schemas and users are not separated, so conversion must be done by mapping to a specific user unit.

| Item | **SQL Server** | **Altibase** |
| --- | --- | --- |
| Feature | Schemas and users are separated (since SQL Server 2005) One user can access multiple schemas Permissions can be granted at the schema level | Schema = User Schemas cannot be created separately; objects must be created per USER |
| Example | CREATE SCHEMA Sales AUTHORIZATION John; CREATE TABLE Sales.Customers (...); | CREATE USER Sales IDENTIFIED BY salespwd; CREATE TABLE Sales.Customers (...); |

When migrating SQL Server schemas to Altibase, replace schemas with "Schema = User" as shown in the table below, and common schemas like dbo should be replaced by creating separate users.

| Item | SQL Server | Altibase | Remarks |
| --- | --- | --- | --- |
| Schema Structure | Independent from user | user = Schema | When converting, SQL Server schemas must be mapped to Altibase users |
| Default Schema | dbo | Not supported | Altibase does not have dbo schema, so it should be replaced by creating a specific user |
| Common Object Management | Uses dbo | Create separate user and grant permissions | dbo.TableName format needs to be mapped to a specific user schema and granted permissions |
| Permission Grant Unit | Can be at schema level | Only at object level | Schema-level permissions must be broken down into object-level permissions |
| Naming Conflict Handling | Resolved by schema separation | Resolved by user name | Be careful that SQL Server schema names do not conflict with Altibase user names during conversion |

# Object Conversion

---

This section describes the considerations when converting SQL Server objects to ALTIBASE.

## DATATYPE

---

This section explains how each DATATYPE in SQL Server tables is converted when migrating to Altibase.

| Category | **SQL Server** | **Altibase** | SQL Server Maximum | **ALTIBASE Maximum** | Remark |
| --- | --- | --- | --- | --- | --- |
| Character Types | CHAR | CHAR | 8000 byte CHAR(MAX) : 2GB | 32000 byte | CHAR(MAX) is converted to CLOB in ALTIBASE. |
| VARCHAR | VARCHAR | 8000 byte VARCHAR(MAX) : Max 2GB | 32000 byte | VARCHAR(MAX) is converted to CLOB in ALTIBASE. |  |
| NCHAR | NCHAR | 8000 byte<br>NCHAR(MAX) : 2GB | Max length: 16000(UTF16), Max length: 10666(UTF8) | NCHAR(MAX) is converted to CLOB in ALTIBASE. |  |
| NVARCHAR | NVARCHAR | 8000 byte<br>NVARCHAR(MAX) : 2GB | Max length: 16000(UTF16), Max length: 10666(UTF8) | NVARCHAR(MAX) is converted to CLOB in ALTIBASE. |  |
| BINARY | BYTE | 8000 byte | 32000 byte |  |  |
| VARBINARY | BLOB | 8000 byte | 2GB | VARBINARY(MAX) is converted to BLOB in ALTIBASE. |  |
| IMAGE -> VARBINARY(MAX) | BLOB | 2GB | 2GB | Since SQL Server 2005,<br>it is recommended to use VARBINARY(MAX) as a replacement. |  |
| TEXT, NTEXT<br>-> VARCHAR(MAX)<br>NVARCHAR(MAX) | CLOB | TEXT : 65536 byte NTEXT : 2GB | 2GB | Since SQL Server 2005,<br>it is recommended to use VARCHAR(MAX) or NVARCHAR(MAX) as replacements. |  |
| Numeric Types | BIGINT | BIGINT |  |  |  |
| NUMERIC | NUMERIC |  |  |  |  |
| BIT | BIT |  |  |  |  |
| SMALLINT | SMALLINT |  |  |  |  |
| TINYINT | SMALLINT | TINEYINT : 1 byte | SMALLINT : 2 byte |  |  |
| REAL | REAL |  |  |  |  |
| INT | INTEGER |  |  |  |  |
| MONEY | decimal(p, s) |  |  |  |  |
| SMALLMONEY | decimal(p, s) |  |  |  |  |
| Date Types | DATE | DATE |  |  | Stores only the date. Format: YYYY-MM-DD |
| DATETIMEOFFSET | Not Supported |  |  | Store the date, time, and time zone. Format: YYYY-MM-DD hh:mm:ss [+\|-]hh:mm In Altibase, this can be replaced with DATE if the time zone is excluded. |  |
| DATETIME2 | DATE |  |  | Store the date and time. Format: YYYY-MM-DD hh:mm:ss Altibase stores up to microseconds (6 decimal places). |  |
| SAMMLLDATETIME | DATE |  |  | Store the date and time. Format: YYYY-MM-DD hh:mm:ss |  |
| DATETIME | DATE |  |  | Store the date and time (for backward compatibility). Format: YYYY-MM-DD hh:mm:ss |  |
| TIME | DATE |  |  | Store time only. Format: hh:mm:ss SQL Server stores up to 100 nanoseconds (7 decimal places). Altibase stores up to microseconds (6 decimal places). |  |

## FUNCTION & EXPRESSION

---

|  |  |  |  |
| --- | --- | --- | --- |
| **Category** | **SQL Server** | **Altibase** | **Remarks** |
| Aggregate | AVG | AVG |  |
| CHECKSUM_AGG | Not Supported |  |  |
| COUNT | COUNT |  |  |
| COUNT_BIG | Replace with COUNT |  |  |
| GROUPING | GROUPING | A function that distinguishes aggregation levels when using ROLLUP, CUBE, or GROUPING SETS. |  |
| GROUPING_ID | GROUPING_ID | Returns a numeric value corresponding to the GROUPING bit vector associated with the row. |  |
| MAX | MAX |  |  |
| MIN | MIN |  |  |
| STDEV | STDDEV |  |  |
| STDEVP | Not Supported |  |  |
| SUM | SUM |  |  |
| VAR | VARIANCE |  |  |
| Ranking | DENSE_RANK | DENSE_RANK |  |
| NTILE | NTILE |  |  |
| RANK | RANK |  |  |
| ROW_NUMBER | ROW_NUMBER |  |  |
| Conversion | CAST, CONVERT | CAST | The CONVERT function in Altibase provides different functionality |
| PARSE | CAST | The CONVERT function can be used to change the character set |  |
| TRY_CAST | CAST | Returns an error if casting fails |  |
| TRY_CONVERT | Not Supported |  |  |
| TRY_PARSE | Not Supported |  |  |
| Date | CURRENT_TIMESTAMP | CURRENT_TIMESTAMP |  |
| DATENAME | DATENAME |  |  |
| DATEPART | DATEPART |  |  |
| DAY | DATEPART |  |  |
| DATEADD | DATEADD | In Altibase, date strings must be formatted using the TO_DATE() function |  |
| DATEDIFF | DATEDIFF |  |  |
| DATEFROMPARTS | TO_DATE |  |  |
| DATETIME2FROMPARTS | TO_DATE |  |  |
| DATETIMEFROMPARTS | TO_DATE |  |  |
| DATETIMEOFFSETFROMPARTS | TO_DATE |  |  |
| EOMONTH | LAST_DAY |  |  |
| GETDATE | SYSDATE | Conversion Type: datetime |  |
| GETUTCDATE | Replace with unix_date |  |  |
| ISDATE | Not Supported |  |  |
| SMALLDATETIMEFROMPARTS | TO_DATE |  |  |
| SWITCHOFFSET | Replace with CONV_TIMEZONE |  |  |
| SYSDATETIME | SYSDATE | Conversion Type: datetime2SWITCHOFFSET |  |
| SYSDATETIMEOFFSET | Not Supported |  |  |
| SYSUTCDATETIME | Replace with unix_date |  |  |
| TIMEFROMPARTS | TO_DATE |  |  |
| TODATETIMEOFFSET | Not Supported |  |  |
| YEAR | Replace with DATEPART or EXTRACT |  |  |
| Logical | CHOOSE | Not Supported |  |
| IIF | Replace with case2 |  |  |
| Mathematical | ABS | ABS |  |
| ACOS | ACOS |  |  |
| ASIN | ASIN |  |  |
| ATAN | ATAN |  |  |
| ATN2 | ATN2 |  |  |
| CEIL(n) | CEIL(n) |  |  |
| COS | COS |  |  |
| COT | Not Supported |  |  |
| DEGREES | Not Supported |  |  |
| EXP | EXP |  |  |
| FLOOR | FLOOR |  |  |
| LOG | LOG | LOG (m, n) |  |
| LOG10 | LOG(10,m) |  |  |
| PI | Not Supported |  |  |
| POWER | POWER |  |  |
| RADIANS | Not Supported |  |  |
| RAND | RAND | SQL Server: Returns a pseudo-random float value between 0 and 1. Altibase: Returns a pseudo-random integer value between 0 and 2,147,483,647. |  |
| ROUND | ROUND |  |  |
| SIGN | SIGN |  |  |
| SIN | SIN |  |  |
| SQRT | SQRT |  |  |
| SQUARE | Not Supported |  |  |
| TAN | TAN |  |  |
| String | ASCII | ASCII |  |
| CHAR | CHAR |  |  |
| CHARINDEX | INSTR, POSITION |  |  |
| CONCAT | CONCAT |  |  |
| DIFFERENCE | Not Supported |  |  |
| LEFT | SUBSTR, SUBSTRING | SUBSTR (expr, start [, length]) Specify a positive value for Start |  |
| LEN | LENGTH |  |  |
| LOWER | LOWER |  |  |
| LTRIM | LTRIM | In Altibase, LTRIM(expr1 [, expr2]) is used. |  |
| RTRIM | RTRIM | In Altibase, RTRIM(expr1 [, expr2]) is used. |  |
| PATINDEX | INSTR, POSITION |  |  |
| QUOTENAME | Not Supported |  |  |
| REPLACE | REPLACE |  |  |
| REPLICATE | REPLICATE |  |  |
| REVERSE | REVERSE_STR |  |  |
| RIGHT | SUBSTR, SUBSTRING | SUBSTR (expr, start [, length]) Specify a negative value for Start |  |
| PATINDEX | INSTR, POSITION |  |  |
| SOUNDEX | Not Supported |  |  |
| SPACE | LPAD, RPAD |  |  |
| STR | TO_CHAR |  |  |
| STUFF | STUFF |  |  |
| SUBSTRING | SUBSTRING |  |  |
| UNICODE | Not Supported |  |  |
| UPPER | UPPER |  |  |

## OBJECT

---

| **Category** | **SQL Server** | **Altibase** | **Remark** |
| --- | --- | --- | --- |
| CONSTRAINT | Supported | Supported |  |
| TRIGGER | Supported | Supported |  |
| Multi Key-Index | Supported | Supported |  |
| VIEW | Supported | Supported |  |
| UPDATABLE VIEW | Supported | Supported | In Altibase, if the WITH READ ONLY option is not specified when creating a VIEW, an updatable view is created. |
| SEQUENCE | Supported | Supported |  |
| STORED FUNCTION/PROCEDURE | Supported | Supported |  |
| SYNONYM | Supported | Supported |  |
| Temporary Table | Supported | Supported | In Altibase, temporary tables are created and used within a Volatile TableSpace. |
| USER | Supported | Supported |  |
| REPLICATION | Supported | Supported |  |

## CREATE TABLESPACE

---

In SQL Server, databases are managed as data storage units, whereas in Altibase, tablespaces are managed. In Altibase, tablespaces are classified based on storage type into memory tablespaces and disk tablespaces, by creator into system tablespaces and user-defined tablespaces, and by stored content into dictionary tablespaces, undo tablespaces, temporary tablespaces, and data tablespaces.

Therefore, when converting to Altibase, use `CREATE MEMORY DATA TABLESPACE` or `CREATE DISK DATA TABLESPACE` depending on the type of data storage.

The following explains guidelines for mapping various options in the `CREATE TABLESPACE` statement when converting a SQL Server DATABASE to an Altibase tablespace.

```
CREATE TABLESPACE user_data DATAFILE '/tmp/tbs.user' SIZE 10M AUTOEXTEND ON NEXT 128M;
```

| **SQL Server** | **Altibase** | **Remark** |
| --- | --- | --- |
| FILENAME | FILENAME |  |
| SIZE | SIZE | default 100MB |
| MAXSIZE | MAXSIZE |  |
| FILEGROWTH | AUTOEXTEND ON NEXT |  |
| FILESTREAM | Not Supported | Delete when generating the statement in Altibase |
| DEFAULT_FULLTEXT_LANGUAGE | Not Supported | Delete when generating the statement in Altibase |
| DEFAULT_LANGUAGE | Not Supported | Delete when generating the statement in Altibase |
| NESTED_TRIGGERS | Not Supported | Delete when generating the statement in Altibase |
| TRANSFORM_NOISE_WORDS | Not Supported | Delete when generating the statement in Altibase |
| TWO_DIGIT_YEAR_CUTOFF | Not Supported | Delete when generating the statement in Altibase |
| DB_CHAINING | Not Supported | Delete when generating the statement in Altibase |
| TRUSTWORTHY | Not Supported | Delete when generating the statement in Altibase |

## CREATE TABLE

---

When converting a SQL Server TABLE to Altibase, various options used in the CREATE TABLE statement must be appropriately modified. Altibase does not provide OBJECT TABLE or XMLType TABLE. Altibase provides memory TABLE, so if the characteristics of the table to be converted fit a memory TABLE, it should be created specifying a memory TABLESPACE.

If a memory TABLE is created, the options used in the SQL Server CREATE TABLE statement cannot be used. Refer to Altibase SQL manuals for the syntax to create memory TABLEs.

If converting a SQL Server TABLE to a DISK TABLE, the various options set in CREATE TABLE should be converted to Altibase-compatible options as follows.

1. **Column definition**

| **SQL Server** | **Altibase** | **Remark** |
| --- | --- | --- |
| FILESTREAM | Not Supported |  |
| COLLATE | Not Supported |  |
| CONSTRAINT | CONSTRAINT | In Altibase, you cannot specify an index name when defining a PRIMARY KEY or UNIQUE constraint |
| IDENTITY | Not Supported |  |
| ROWGUIDCOL | Not Supported |  |

2. **data type**

| **SQL Server** | **Altibase** | **Remark** |
| --- | --- | --- |
| Precision, scale | Precision, scale |  |
| max | Not Supported |  |
| CONTENT | Not Supported |  |
| DOCUMENT | Not Supported |  |
| xml_schema_collection | Not Supported |  |

3. **column constraint**

| **SQL Server** | **Altibase** | **Remark** |
| --- | --- | --- |
| PRIMARY KEY | PRIMARY KEY |  |
| NULL, NOT NULL | NULL, NOT NULL |  |
| UNIQUE | UNIQUE |  |
| CLUSTERED, NONCLUSTERED | Not Supported |  |
| FOREIGN KEY REFERENCES | FOREIGN KEY REFERENCES |  |
| partition_scheme_name | PARTITION BY RANGE \| HASH \| LIST | Specify the type of partitioned table when creating a table |

4. **computed column definition**

Not Supported

5. **table constraint**

| **SQL Server** | **Altibase** | **Remark** |
| --- | --- | --- |
| PRIMARY KEY | PRIMARY KEY |  |
| CLUSTERED, NONCLUSTERED | Not Supported |  |
| FOREIGN KEY REFERENCES | FOREIGN KEY REFERENCES |  |
| partition_scheme_name | PARTITION BY RANGE \| HASH \| LIST | Specify the type of partitioned table when creating a table |

6. **table_option**

| **SQL Server** | Altibase | **Remark** |
| --- | --- | --- |
| DATA_COMPRESSION | Replace with COMPRESS(column_name) | Altibase provides column-level compression |

7. **index_option**

| **SQL Server** | **Altibase** | **Remark** |
| --- | --- | --- |
| PAD_INDEX | Not Supported |  |
| FILLFACTOR | Not Supported |  |
| IGNORE_DUP_KEY | Not Supported | Altibase is in the OFF state |
| STATISTICS_NORECOMPUTE | Not Supported | Altibase is in the OFF state |
| ALLOW_ROW_LOCKS | Not Supported | Defined according to the Durability Level setting |
| ALLOW_PAGE_LOCKS | Not Supported | Defined according to the Durability Level setting |
| DATA_COMPRESSION | Not Supported | Index compression is not supported |

## CREATE USER

---

In Altibase, database login and user are not created separately; a single user is created and managed.

| SQL Server | Altibase | **Remark** |
| --- | --- | --- |
| ```<br>CREATE LOGIN <login_name> WITH PASSWORD = '<password>';<br>Users based on logins in master<br>CREATE USER user_name<br>[<br>{ FOR \| FROM } LOGIN login_name<br>]<br>[ WITH DEFAULT_SCHEMA = schema_name ]<br>[ ; ]<br>``` | ```<br>CREATE USER <user_name> IDENTIFIED BY ‘<password>’<br>DEFAULT TABLESPACE = tablespace_name<br>``` |  |

## CREATE INDEX

---

Altibase provides only BTREE and RTREE indexes and does not support BITMAP, CLUSTER, REVERSE, or Global partitioned indexes.

The following explains how to convert the options used in the CREATE INDEX statement when migrating to Altibase.

| **SQL Server** | **Altibase** | **Remark** |
| --- | --- | --- |
| UNIQUE | UNIQUE |  |
| CLUSTERED \| NONCLUSTERED | Not Supported |  |
| ASC \| DESC | ASC \| DESC |  |
| INCLUDE | Not Supported |  |
| filter_predicate | Not Supported |  |
| partition_scheme_name | PARTITION ON | Only local indexes are supported |
| ON filegroup_name | Not Supported |  |
| table_or_view_name | Table_name | Views are not supported |
| PAD_INDEX | Not Supported |  |
| FILLFACTOR | Not Supported |  |
| SORT_IN_TEMPDB | Not Supported |  |
| IGNORE_DUP_KEY | Not Supported | Altibase is in the ON state |
| STATISTICS_NORECOMPUTE | Not Supported | Altibase is in the OFF state |
| DROP_EXISTING | Not Supported |  |
| ONLINE | Not Supported | Altibase is in the OFF state |
| ALLOW_ROW_LOCKS | Not Supported | Defined according to the Durability Level setting |
| ALLOW_PAGE_LOCKS | Not Supported | Defined according to the Durability Level setting |
| MAXDOP | Not Supported | Applied only at creation |
| DATA_COMPRESSION | Replace with COMPRESS(column_name) |  |

# SQL Conversion

---

This explains how to convert SQL statements from SQL Server to Altibase.

## JOIN

---

In addition to the joins below, Altibase also provides Semi Join and Anti Join.

| **SQL Server** | **Altibase** | **Remark** |
| --- | --- | --- |
| INNER JOIN | INNER JOIN |  |
| LEFT OUTER JOIN | LEFT OUTER JOIN |  |
| RIGHT OUTER JOIN | RIGHT OUTER JOIN |  |
| FULL OUTER JOIN | FULL OUTER JOIN |  |
| CROSS JOIN | CROSS JOIN |  |

## Execution Query

---

The query terminator in Altibase is “;”. Therefore, if you want to execute multiple queries at once, each query must be separated by the terminator “;”.

| **SQL Server** | **Altibase** | **Remark** |
| --- | --- | --- |
| GO | ; Commit; | default Autocommit |

## Temporary Table

---

| SQL Server | Altibase | **Remark** |
| --- | --- | --- |
| CREATE TABLE #TempProcess | CREATE TABLE TEMPORARY *table_name* (…) on commit (...) rows TABLESPACE *volatile_tablespace_name* |  |

## Control Statement

---

|  | **SQL Server** | **Altibase** |
| --- | --- | --- |
| IF | If (condition) Else if (condition) Else End | If condition then Elseif condition then Else End |
| While | While (condition) BEING END BREAK => Exit the while loop | While condition loop End loop Exit when condition => Exit the loop when the condition is met |

## Identity Attribute

---

Altibase does not have an Identity property. Therefore, if needed, create a SEQUENCE and apply it as the DEFAULT value for the column.

For example:

| SQL Server | Altibase |
| --- | --- |
| ```<br>-- Apply auto-increment by 1 to the c1 column.<br>```<br>```<br>create table seq_test<br>(c1 int identity(1,1) not null<br>```<br>```<br>...<br>);<br>``` | ```<br>-- create a sequence<br>create sequence seq1 start with 1 increment by 1 nocache;<br>-- Apply the sequence as the default value.<br>```<br>```<br>create table seq_test<br>(c1 integer default seq1.nextval not null,<br>...<br>);<br>``` |

## Procedure Conversion

---

The syntax for creating and executing a PROCEDURE in Altibase differs from that of SQL Server. This example demonstrates how to modify a PROCEDURE.

### Parameter Declaration

---

When converting the parameter declaration section from SQL Server to Altibase: Remove the '@' symbol used in SQL Server parameter declarations. Specify `in`, `out`, or `in out` depending on the nature of each parameter. For functions, since they return a single value upon execution, the data type must be specified after `RETURN`.

| SQL Server | Altibase |
| --- | --- |
| ```<br>CREATE Procedure dbo.sp1<br>@nTop INT -- ignored<br>, @nGroupCode INT = -2<br>, @nObjectCode INT = -2<br>, @nRCLS INT=1 – 1:Set , 0:Unset<br>, @nLCRS INT=1 – 1:Set , 0:Unset<br>, @nLCLS INT=1 – 1:Set , 0:Unset<br>, @sStartDate VARCHAR(19) = '' –- ignored<br>, @sEndDate VARCHAR(19) = '' –- ignored<br>, @nSort INT = 0 – 0:Number of detections, 1:Number of attempts, 2:DataSize<br>, @sSignatureName VARCHAR(100) = ''<br>As<br>…<br>``` | ```<br>create or replace procedure sp1<br>(<br>i_nTop IN INT -- ignored<br>, i_nGroupCode IN INT := -2<br>, i_nObjectCode IN INT := -2<br>, i_nRCLS IN INT:=1 – 1:Set , 0:Unset<br>, i_nLCRS IN INT:=1 – 1:Set , 0:Unset<br>, i_nLCLS IN INT:=1 – 1:Set , 0:Unset<br>, i_sStartDate IN VARCHAR(19) := '' –- ignored<br>, i_sEndDate IN VARCHAR(19) := '' –- ignored<br>, i_nSort IN INT := 0 – 0:Number of detections, 1:Number of attempts, 2:DataSize<br>, i_sSignatureName IN VARCHAR(100) := ''<br>)<br>as …<br>``` |

### Variable Declaration

---

In Altibase, variables are declared between `AS` and `BEGIN`. Remove the `@` symbol from variable declarations used in SQL Server. Replace the delimiter `,` with `;` when declaring variables. Always end the last variable declaration with a `;` to indicate the end.

| SQL Server | Altibase |
| --- | --- |
| ```<br>create or replace procedure sp1<br>(<br>……<br>)<br>as<br>DECLARE @sTotalQry VARCHAR(3000)<br>, @sQry VARCHAR(3000)<br>, @sFilterQry VARCHAR(1000)<br>, @dStartDate DATETIME<br>, @dEndDate DATETIME<br>, @sSort VARCHAR(20)<br>, @sSortSub VARCHAR(90)<br>, @sTop VARCHAR(10)<br>, @sTable VARCHAR(50)<br>, @nSec INT<br>, @sBaseDate VARCHAR(23)<br>``` | ```<br>create or replace procedure sp1<br>(<br>……<br>)<br>as<br>i_sTotalQry VARCHAR(3000);<br>i_sQry VARCHAR(3000);<br>i_sFilterQry VARCHAR(1000);<br>i_dStartDate DATE;<br>i_dEndDate DATE;<br>i_sSort VARCHAR(20);<br>i_sSortSub VARCHAR(90);<br>i_sTop VARCHAR(10);<br>i_sTable VARCHAR(50);<br>i_nSec INT;<br>i_sBaseDate VARCHAR(23);<br>``` |

### Assignment

---

In SQL Server, variables are assigned values using `SET` and the `@` symbol. Altibase supports two methods to modify this:

1. Remove `SET` and the `@` symbol, replace `=` with `:=`, replace the delimiter `,` with `;`, and always end with a `;` to indicate the end.
2. Remove the `@` symbol, replace the delimiter `,` with `;`, and always end with a `;` to indicate the end.

| SQL Server | Altibase |
| --- | --- |
| ```<br>SET @sTop = '1000'<br>SET @sBaseDate = CONVERT(VARCHAR, DATEADD(dd, -1, GETDATE()), 121)<br>``` | ```<br>i_sTop := '1000' ;<br>i_sBaseDate := to_char(DATEADD (SYSDATE, -1, 'DAY'), 'YYYY-MM-DD HH:MI:SS') ;<br>OR<br>Set i_sTop = '1000' ;<br>Set i_sBaseDate = to_char(DATEADD (SYSDATE, -1, 'DAY'), 'YYYY-MM-DD HH:MI:SS') ;<br>``` |

### Flow Control (Control_flow_statement) - IF statement

---

In Altibase, every statement must end with a `;` to indicate the end. An `IF` statement begins with `IF (condition) THEN`. It ends with `END IF` to indicate the end of the `IF` block.

| SQL Server | Altibase |
| --- | --- |
| ```<br>IF (@nRCLS = 1) AND (@nLCRS = 1) AND (@nLCLS = 1) SET @sFilterQry = ''<br>ELSE IF (@nRCLS = 0) AND (@nLCRS = 0) AND (@nLCLS = 0) SET @sFilterQry = ''<br>``` | ```<br>IF (i_nRCLS = 1) AND (i_nLCRS = 1) AND (i_nLCLS = 1) THEN<br>i_sFilterQry := '' ;<br>ELSIF (i_nRCLS = 0) AND (i_nLCRS = 0) AND (i_nLCLS = 0) THEN<br>i_sFilterQry := '' ;<br>END IF;<br>``` |

### SELECT clause

---

In Altibase, every statement must end with a `;` to indicate the end. To send a SELECT result set to the client in Altibase, a REF CURSOR must first be defined as a database object. The REF CURSOR should then be included as a parameter in the stored procedure. When executing the corresponding query, use the `OPEN` command. Remove the `@` symbol used in SQL Server.

| SQL Server | Altibase |
| --- | --- |
| ```<br>……<br>SET @sQry = 'select * from test_tbl'<br>EXEC(@sQry)<br>……<br>``` | ```<br>CREATE TYPESET MY_TYPE<br>AS<br>TYPE MY_CUR IS REF CURSOR;<br>END;<br>/<br>create or replace procedure spTMSGetEventSignatureRankVariation<br>(<br>……<br>, P1 OUT MY_TYPE.MY_CUR<br>)<br>As<br>i_sQry := 'select * from test_tbl' ;<br>OPEN P1 FOR i_sQry;<br>END;<br>``` |

### Exception Handler

---

In Altibase, every statement must end with a `;` to indicate the end. The Exception Handler in Altibase is used to handle specific exceptions when they occur. Exception handling must always be written within a `BEGIN ... END;` block. Specify either a system-defined or user-defined exception name; when that exception occurs, the corresponding statement will be executed. If the specific exception is not handled, it will be caught by the `OTHERS` routine as a fallback. To check if the number of affected records is zero, use the `SQL%ROWCOUNT` constant. System-defined exceptions are included at the end of the file.

| SQL Server | Altibase |
| --- | --- |
| ```<br>IF @@ERROR <> 0 BEGIN<br>IF @@ROWCOUNT = 0 BEGIN<br>ROLLBACK<br>END<br>END<br>``` | ```<br>BEGIN<br>……<br>EXCEPTION WHEN NO_DATA_FOUND THEN<br>rollback;<br>END;<br>OR<br>IF SQL%ROWCOUNT = 0 then<br>ROLLBACK<br>END if;<br>``` |

### SP Call

---

In Altibase, every statement must end with a `;` to indicate the end. In SQL Server, a stored procedure is called using `exec sp_name` without parentheses around the parameters. In Altibase, the stored procedure is executed by specifying the procedure name followed by its parameters in parentheses. Remove the `@` symbol used in SQL Server.

| SQL Server | Altibase |
| --- | --- |
| ```<br>IF @ID IS NOT NULL BEGIN<br>EXEC AddCustomer 'David', 'Seoul';<br>or<br>EXEC AddCustomer @Name = 'David', @City = 'Seoul';<br>``` | ```<br>IF ID IS NOT NULL THEN<br>EXEC AddCustomer('David', 'Seoul');<br>``` |

### Functions

---

In Altibase, every statement must end with a `;` to indicate the end. Usage may vary by function, and function names may differ. Remove the `@` symbol used in SQL Server functions.

| SQL Server | Altibase |
| --- | --- |
| ```<br>1. LEFT, RIGHT function<br>LEFT(@ID_NUMBER,6)<br>RIGHT(@ID_NUMBER,7)<br>2. ISNULL(V1, 0)<br>3. CASE sample WHEN '0' THEN B.sample1+B.package ELSE ISNULL(D.sample2,0) END<br>4. Convert<br>CONVERT(VARCHAR(10),,120) <= B.dStartDate TO_CHAR(CASE2(i_dStartDate1=NULL,SYSDATE),'YYYY-MM-DD');<br>5. LEN<br>6. RTRIM(LTRIM())<br>7. DATEADD(mi, -20, GETDATE())<br>8. CEILING<br>9. Remainder operator % (a % b )<br>10. charIndex(‘aaa’, ‘aaabbbcccddd’)<br>11. String concatenation + : (‘alti’ + ‘base’)<br>``` | ```<br>1. Replace with SubStr<br>SUBSTR(ID_NUMBER,1,6)<br>SUBSTR(ID_NUMBER,8,7)<br>2. NVL(V1, 0)<br>3. CASE2(sample = '0', B.sample1 \|\| B.package,D.sample2=NULL,0,)<br>4. Convert<br>CONVERT(VARCHAR(23), dStartDate, 121) => TO_CHAR(dStartDate, 'YYYY-MM-DD HH:MI:SS.FF3');<br>CONVERT(DATETIME, sEndDate) => TO_DATE(sEndDate, 'YYYY-MM-DD HH:MI:SS');<br>5. LENGTH<br>6. TRIM()<br>7. DATEADD(sysdate, -20, 'MINITUE');<br>8. CEIL<br>9. MOD(a, b)<br>10. INSTR(‘aaabbbcccddd’, ‘aaa’)<br>11. \|\| (‘alti’ \|\| ’base’)<br>``` |

### ETC

---

In Altibase, every statement must end with a `;` to indicate the end. Remove the `@` symbol used in SQL Server.

| SQL Server | Altibase |
| --- | --- |
| `UPDATE STATISTICS index_name` | Not required |
| `with (nolock)` | Not required (remove) |
| Use of keywords like `order`, `level` | Do not use keywords like `order`, `level` (reserved in Altibase) |

### DB Link

---

When using a DB Link in Altibase, use `REMOTE_TABLE(dblink_name, query)` for SELECT statements, and `REMOTE_EXECUTE_IMMEDIATE(dblink_name, query)` for DML statements. For more details about ALTIBASE DB LINK, refer to the ALTIBASE 7.3 Online Manual ([Database Link User’s Manual](https://manual.altibase.com/7.3/en/admin/dblink/copyright/)).

### JOIN Update

---

In Altibase, there are two methods to perform a join update:

1. Use JOIN UPDATE

- Each table must have a Primary Key or a Unique Key.

2. Use an update with MERGE JOIN

- Merge into A using ( SELECT … )
  WHEN matched then
  Update …

## Using Cursor

---

Let's look at how to convert a SQL Server cursor to Altibase using an example.

| SQL Server | Altibase |
| --- | --- |
| ```<br>declare security_cursor cursor for<br>select fldID from tblDept where fldParentID=@fldID<br>open security_cursor<br>fetch next from security_cursor into @fldID<br>while @@fetch_status = 0<br>begin<br>exec sr_GetSubDeptID_Str @fldID, @DeptID OUTPUT<br>declare @sql as varchar(8000)<br>begin<br>exec(@sql)<br>end<br>fetch next from security_cursor into @fldID<br>end<br>close security_cursor<br>deallocate security_cursor<br>``` | ```<br>Here is an example of an Altibase stored procedure that calculates the number of employees and the total salary by department.<br>CREATE OR REPLACE PROCEDURE ForCursor_Test<br>AS<br>BEGIN<br>DECLARE CURSOR dept_sum IS<br>SELECT b.dname, COUNT(a.empno) cnt, SUM(a.sal) salary<br>FROM emp a, dept b<br>WHERE a.deptno = b.deptno<br>GROUP BY b.dname;<br>–- Execute the cursor using a FOR loop.<br>BEGIN<br>FOR emp_list IN dept_sum LOOP<br>println('dept name : ' \|\| emp_list.dname);<br>println ('employee count : ' \|\| emp_list.cnt);<br>println('total salary : ' \|\| emp_list.salary);<br>END LOOP;<br>END;<br>END;<br>/<br>``` |

# Exception Code

---

Refer to the [Error Message Reference](https://manual.altibase.com/7.3/en/ref/error/copyright/) manual.

| **Exception Name** | **Error Code** **(integer)** | **Error Code** **(hexadecimal)** | **Error Section** |
| --- | --- | --- | --- |
| "CURSOR_ALREADY_OPEN" | 201062 | 31166 | qpERR_ABORT_QSX_CURSOR_ALREADY_OPEN |
| "DUP_VAL_ON_INDEX" | 201063 | 31167 | qpERR_ABORT_QSX_DUP_VAL_ON_INDEX |
| "INVALID_CURSOR" | 201064 | 31168 | qpERR_ABORT_QSX_INVALID_CURSOR |
| "INVALID_NUMBER" | 201065 | 31169 | qpERR_ABORT_QSX_INVALID_NUMBER |
| "NO_DATA_FOUND" | 201066 | 3116A | qpERR_ABORT_QSX_NO_DATA_FOUND |
| "PROGRAM_ERROR" | 201067 | 3116B | qpERR_ABORT_QSX_PROGRAM_ERROR |
| "STORAGE_ERROR" | 201068 | 3116C | qpERR_ABORT_QSX_STORAGE_ERROR |
| "TIMEOUT_ON_RESOURCE" | 201069 | 3116D | qpERR_ABORT_QSX_TIMEOUT_ON_RESOURCE |
| "TOO_MANY_ROWS" | 201070 | 3116E | qpERR_ABORT_QSX_TOO_MANY_ROWS |
| "VALUE_ERROR" | 201071 | 3116F | qpERR_ABORT_QSX_VALUE_ERROR |
| "ZERO_DIVIDE" | 201072 | 31170 | qpERR_ABORT_QSX_ZERO_DIVIDE |
| "INVALID_PATH" | 201237 | 31215 | qpERR_ABORT_QSX_FILE_INVALID_PATH |
| "INVALID_MODE" | 201235 | 31213 | qpERR_ABORT_QSX_INVALID_FILEOPEN_MODE |
| "INVALID_FILEHANDLE" | 201238 | 31216 | qpERR_ABORT_QSX_FILE_INVALID_FILEHANDLE |
| "INVALID_OPERATION" | 201239 | 31217 | qpERR_ABORT_QSX_FILE_INVALID_OPERATION |
| "READ_ERROR" | 201242 | 3121A | qpERR_ABORT_QSX_FILE_READ_ERROR |
| "WRITE_ERROR" | 201243 | 3121B | qpERR_ABORT_QSX_FILE_WRITE_ERROR |
| "ACCESS_DENIED" | 201236 | 31214 | qpERR_ABORT_QSX_DIRECTORY_ACCESS_DENIED |
| "DELETE_FAILED" | 201240 | 31218 | qpERR_ABORT_QSX_FILE_DELETE_FAILED |
| "RENAME_FAILED" | 201241 | 31219 | qpERR_ABORT_QSX_FILE_RENAME_FAILED |

The Korean source lists the legacy document placeholder `ALTIBASE_MSSQL_변환가이드.pdf` without a downloadable URL.
