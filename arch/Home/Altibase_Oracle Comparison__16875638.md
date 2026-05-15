---
title: "Altibase/Oracle Comparison"
page_id: "16875638"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16875638"
updated_at: "2021-02-22T16:31:49.000+0900"
version: 12
ancestors: ["Home"]
labels: []
---

# Altibase/Oracle Comparison
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16875638
Updated: 2021-02-22T16:31:49.000+0900

- [Overview](#Altibase/OracleComparison-Overview) - [Model Comparison](#Altibase/OracleComparison-ModelComparison) - [Architecture](#Altibase/OracleComparison-Architecture) - [Logical Structure](#Altibase/OracleComparison-LogicalStructure) - [Physical Structure](#Altibase/OracleComparison-PhysicalStructure) - [Considerations/Notes](#Altibase/OracleComparison-Considerations/Notes) - [Feature Comparison](#Altibase/OracleComparison-FeatureComparison) - [Supported function](#Altibase/OracleComparison-Supportedfunction) - [Supported tool](#Altibase/OracleComparison-Supportedtool) - [Partition Table](#Altibase/OracleComparison-PartitionTable) - [Partition table feature details](#Altibase/OracleComparison-Partitiontablefeaturedetails) - [Backup & Recovery](#Altibase/OracleComparison-Backup&Recovery) - [Development Support Comparison](#Altibase/OracleComparison-DevelopmentSupportComparison) - [SQL Support](#Altibase/OracleComparison-SQLSupport) - [Data Type Comparison](#Altibase/OracleComparison-DataTypeComparison) - [API Comparison](#Altibase/OracleComparison-APIComparison) - [Built-In Function](#Altibase/OracleComparison-Built-InFunction)

# Overview

---

This document compares the features of Altibase version 7.1 or later with Oracle 12c.

For errors and improvements related to this document, please contact the technical support portal or technical support center.

- Technical support portal: [http://support.altibase.com](http://support.altibase.com/)[/en/](http://support.altibase.com/en/)
- Technical support center: 02-2082-1114

# Model Comparison

---

Let's compare the overall model of Altibase and Oracle.

## Architecture

---

| Feature | Oracle | Altibase | Remark |
| --- | --- | --- | --- |
| Database Structure | Multi-process structure | Multi-thread structure |  |
| Model | Relational database structure | Relational database structure |  |
| Architecture | Client-server architecture | Client-server architecture |  |
| Replication | Real Application Cluster (RAC) | Data Replication | Altibase replication replicates only table data |
| Individual instance | Internal thread |  |  |
| Shared storage | Separate storage |  |  |
| Shared schema | Separate schema |  |  |
| Shared data | Data replication |  |  |
| 64bit mode support | Supported | Supported |  |
| Locking mode | Row-Level Locking | Row-Level Locking | MVCC supported |
| Database recovery | Use Checkpoint & Logfile | Use Checkpoint & Logfile |  |
| DeadLock Detection | (Auto Deadlock Detect & Recovery) | (Auto Deadlock Detect & Recovery) |  |

## Logical Structure

---

| Feature | Oracle | Altibase | Remark |  |
| --- | --- | --- | --- | --- |
| Management Structure | Database(DB) | Database(DB) | Altibase is a single database |  |
| Tablespace | Tablespace |  |  |  |
| Segment | Segment |  |  |  |
| Extent | Extent |  |  |  |
| Block | Page |  |  |  |
| Row | Record |  |  |  |
| System Tablespace | Data Dictionary | SYSTEM, SYSAUX | SYS_TBS_MEM_DIC |  |
| Undo | UNDOTBS | SYS_TBS_DISK_UNDO |  |  |
| Memory Data | - | SYS_TBS_MEM_DATA |  |  |
| Temp | TEMP | SYS_TBS_DISK_TEMP |  |  |
| Disk Data | SYSTEM | SYS_TBS_DISK_DATA |  |  |
| User Tablespace | Undo | Specified by user | Global Undo Tablespace |  |
| Memory Data | Specified by user | Specified by user | This is possible in Oracle by setting the memory option |  |
| Temp | Specified by user | Specified by user |  |  |
| Disk Data | Specified by user | Specified by user |  |  |
| Volatile Data | Not available | Specified by user |  |  |

## Physical Structure

---

| Feature | Oracle | Altibase | Remark |
| --- | --- | --- | --- |
| Data File | Data File | Data File |  |
| Data Information File | Control File | Log Anchor File |  |
| Online Log File | Online Log File (Recycle) | Online Log File (Serial) |  |
| Archive Log File | %t_%s_%r.arc | logfile0 ~ | It is a replicate of the online log file, with the same name and different storage locations. |

## Considerations/Notes

---

| Feature | Oracle | Altibase | Remark |
| --- | --- | --- | --- |
| Length of object name | 128 Byte | 40 Byte |  |
| Number of tablespaces | 65,533 | 65,533 | Maximum number per database |
| Number of database files | Operating system dependent; usually 1,022 | 1024 | Maximum per tablespace |
| 65,533 | 67,108,864 | Maximum per database |  |
| Number of users | 2,147,483,638 | 2,147,483,638 | Maximum per database |
| Number of tables | Unlimited | 2,097,151 | Maximum per database |
| Number of indexes | Unlimited | 64 | Maximum per table |
| Number of Columns | 1,000 | 1024 | Per table |
| 32 | 32 | Per index |  |
| Trigger Cascade Limit | Operating system-dependent, typically 32 | Unlimited | Maximum value |
| Number of rows | Unlimited | Unlimited |  |
| Number of partitions | Unlimited | System-wide<br>2,097,151 | Not divided into table units |
| Number of constraints | Unlimited | System-wide<br>2,097,151 | Not divided into in column units |

# Feature Comparison

---

Let's compare the common features between Altibase and Oracle.

## Supported function

---

| Feature | Oracle | Altibase | Remark |
| --- | --- | --- | --- |
| Table | Supported | Supported |  |
| Multi Key-Index | Supported | Supported |  |
| Stored Procedure | Supported | Supported |  |
| Stored Function | Supported | Supported |  |
| Package | Supported | Supported |  |
| Trigger | Supported | Supported |  |
| View | Supported | Supported | Including Materialized View |
| Sequence | Supported | Supported |  |
| Queue | Supported (Advanced Queue) | Supported |  |
| Monitoring View | Supported | Supported |  |
| Authority Management | Supported | Supported |  |
| Role | Supported | Supported |  |
| Snapshot | Supported | Not supported |  |
| DB Link | Supported | Supported | Supported by standard JDBC |
| Synonym | Supported | Supported |  |
| Table partitioning | Supported | Supported | Global Non Partitioned Index Supported |
| User Defined Type | Supported | Partially Supported | Only supported in Procedure |
| Cluster Object | Supported | Not supported |  |
| On-Line Backup | Supported | Supported |  |
| XML | Supported | Not supported |  |
| Auto Expansion of DB space | Supported | Supported |  |

## Supported tool

---

| Feature | Oracle | Altibase | Remark |
| --- | --- | --- | --- |
| GUI Admin Tool | OEM and various 3rd party products | Squirrel SQL, Orange available |  |
| Interactive SQL Processor | SQL*Plus | iSQL |  |
| Data Loader | SQL*Loader | iLoader |  |
| DMBS Admin TOOL | SQL*Plus | iSQL |  |
| Data Transfer | exp/imp | iLoader/aexport | Download / Upload as text type data |
| Connection Dispatcher | Listener | Embedded in DBMS |  |
| DB Create | DBCA | iSQL |  |
| DB Destroyer | Not available | iSQL |  |
| C Precompiler | Pro*C/C++ | APRE*C/C++ |  |
| Recovery Manager | RMAN | iSQL, aexport, iLoader | Connection with storage company tools (API provided) |
| DBMS |  | checkServer |  |

## Partition Table

---

| Classification | Feature | Oracle | Altibase | Remark |
| --- | --- | --- | --- | --- |
| Type (Method | RANGE partition | Supported | Supported |  |
| LIST partition | Supported | Supported |  |  |
| HASH partition | Supported | Supported |  |  |
| COMPOSITE partition | Supported | Not supported |  |  |
| Management command | ALTER tablespace | - | Supported | Refer to details of the partition table function |
| ADD partition | Supported | Partially supported |  |  |
| COALESCE partition | Supported | Partially supported |  |  |
| DROP partition | Supported | Supported |  |  |
| SPLIT partition | Supported | Supported |  |  |
| MERGE partition | Supported | Supported |  |  |
| TRUNCATE partition | Supported | Supported |  |  |
| RENAME partition | Supported | Supported |  |  |
| EXCHANGE partition | Supported | Not supported |  |  |
| MODIFY partition | Supported | Not supported |  |  |
| MOVE partition | Supported | Not supported |  |  |
| Index | Global Index | Supported | Partially supported | Global Non Partitioned index supported |
|  | Local Index | Supported | Supported |  |

## Partition table feature details

---

Operations based on Altibase partition type (method)

| Operation | Range | List | Hash |
| --- | --- | --- | --- |
| Alter tablespace | ALTER TABEL PARTITION | ALTER TABLE PARTITION | ALTER TABLE PARTITION |
| ADD | N/A | N/A | ADD PARTITION |
| COALESCE | N/A | N/A | COALESCE PARTITION |
| DROP | DROP PARTITION | DROP PARTITION | N/A |
| MERGE | MERGE PARTITIONS | MERGE PARTITIONS | N/A |
| RENAME | RENAME PARTITION | RENAME PARTITION | RENAME PARTITION |
| SPLIT | SPLIT PARTITIOn | SPLIT PARTITION | N/A |
| TRUNCATE | TRUNCATE PARTITION | TRUNCATE PARTITION | TRUNCATE PARTITION |

Operations based on Oracle partition type (method)

| Operation | Range | List | Hash | Composite |  |
| --- | --- | --- | --- | --- | --- |
| Range-Hash | Range-List |  |  |  |  |
| ADD | ADD PARTITION | ADD PARTITION | ADD PARTITION | ADD PARTITION,<br>MODIFY PARTITION ... ADD SUBPARTITION | ADD PARTITION,<br>MODIFY PARTITION<br>SUBPARTITION |
| COALESCE | N/A | N/A | COALESCE PARTITION | MODIFY PARTITION ... COALESCE SUBPARTITION | N/A |
| DROP | DROP PARTITION | DROP PARTITION | N/A | DROP PARTITION | DROP [SUB]PARTITION |
| MERGE | MERGE PARTITIONS | MERGE PARTITIONS | N/A | MERGE PARTITIONS | MERGE [SUB]PARTITION |
| RENAME | RENAME PARTITION | RENAME PARTITION | RENAME PARTITION | RENAME [SUB]PARTITION | RENAME [SUB]PARTITION |
| SPLIT | SPLIT PARTITION | SPLIT PARTITION | N/A | SPLIT PARTITION | SPLIT [SUB]PARTITION |
| TRUNCATE | TRUNCATE PARTITION | TRUNCATE PARTITION | TRUNCATE PARTITION | TRUNCATE [SUB]PARTITION | TRUNCATE [SUB] PARTITION |
| EXCHANGE | EXCHANGE PARTITION | EXCHANGE PARTITION | EXCHANGE PARTITION | EXCHANGE [SUB] PARTITION | EXCHANGE [SUB] PARTITION |
| MOVE | MOVE PARTITION | MOVE PARTITION | MOVE PARTITION | MOVE SUBPARTITION | MOVE SUBPARTITION |

## Backup & Recovery

---

| Feature | Oracle | Altibase | Remark |
| --- | --- | --- | --- |
| Online Backup (Hot) | Supported | Supported |  |
| Offline Backup (Cold) | Supported | Supported |  |
| Table-by-table Backup | Supported | Supported |  |
| Incomplete Backup | Supported | Supported |  |
| Complete Backup | Supported | Supported |  |
| Specific Tablespace Recovery | Supported | Supported |  |
| Incremental Backup | Supported | Supported |  |
| Text Data Backup & Recovery | Supported | Partially supported | Object and Data Text available with aexport |

# Development Support Comparison

---

This section describes a comparison of features that can be referred to when developing by converting Oracle to Altibase.

## SQL Support

---

| Feature | Oracle | Altibase | Remark |
| --- | --- | --- | --- |
| SQL | Standard SQL, Transform SQL<br>(Support ANSI-SQL92, ANSI-SQL1999) | Standard SQL<br>(Support ANSI-SQL92) | Object-oriented features of ANSI-SQL1999 are not supported |
| Sub-query(In-Line View) | Supported | Supported |  |
| Sub-query(Scalar) | Supported | Supported |  |
| Sub-query(=,IN,EXISTS) | Supported | Supported |  |
| Equi Join | Supported | Supported |  |
| Inner Join | Supported | Supported |  |
| Outer Join | Supported | Supported | Oracle (+) is also supported |
| Self Join | Supported | Supported |  |
| Hierarchical query<br>CONNECT BY ~ WITH | Supported | Supported | CONNECT_BY_ISYCYCLE is not supported |
| Array Processing | Supported | Supported |  |
| Move statement | Not supported | Supported |  |
| Queue | Advanced Queue | Enqueue/Dequeue | Differences in statement/method used |
| SELECT ~ FOR UPDATE | Supported | Supported | Join is not supported |
| SELECT DISTINCT ~ | Supported | Supported |  |
| UNION | Supported | Supported |  |
| UNION ALL | Supported | Supported |  |
| INTERSECT | Supported | Supported |  |
| MINUS | Supported | Supported |  |
| CERATE TABLE AS SELECT ~ | Supported | Supported |  |
| Literal/Bind SQL | Supported | Supported |  |
| DML with VIEW | Supported | Supported |  |
| WHERE REGEXP_LIKE Condition | Supported | Supported |  |
| Hint function | Supported | Supported |  |
| Cost Optimizer | Supported | Supported |  |
| Parallel Select | Supported | Supported |  |
| Parallel Insert | Supported | Supported |  |
| Parallel Index Build | Supported | Supported |  |

## Data Type Comparison

---

| Classification | Oracle | Altibase |  |  |
| --- | --- | --- | --- | --- |
| Data type | Description | Data Type | Description |  |
| Character Type | CHAR | Fixed-length character type. Up to 2000 bytes | CHAR | Fixed-length character type. Up to 32K |
| VARCHAR2 | Variable-length character type. Up to 4000 bytes | VARCHAR | Variable-length character type. Up to 32K |  |
| NCHAR | Unicode fixed-length character type. Up to 2000 bytes | NCHAR | Character length up to 16000 (UTF16),<br>Character length up to 10666 (UTF8) |  |
| NVARCHAR2 | Unicode variable-length character type.<br>Up to 4000 bytes | NVARCHAR | Character length up to 16000 (UTF16),<br>Character length up to 10666 (UTF8) |  |
| LONG | Character type, Up to 2G |  | Can be replaced with CLOB |  |
| LOB Type | BLOB | Single binary type.<br>Max: (4G-1) * (database block size) | BLOB | Up to 2G |
| CLOB | Single byte character type.<br>Max: (4G-1) * (database block size) | CLOB | Up to 2G |  |
| NCLOB | Unicode character type.<br>Max: (4G-1) * (database block size) |  | Can be replaced with CLOB |  |
| Numeric Type | NUMERIC(p, s) | Numeric type. Accuracy p 1 to 38, scale s -87 to 127 | NUMERIC(p, s) | Fixed point.<br>Accuracy p 1 to 38, scale s -84 to 128 |
| NUMBER (*p, s*) |  | NUMBER(p, s) | Same as FLOAT if p and s are not specified. Given p or p, s is the same as NUMERIC |  |
| DECIMAL(p, s) |  | DECIMAL(p, s) | Same as NUMERIC (p, s) |  |
| FLOAT(p),<br>BINARY_FLOAT |  | FLOAT(p) | Floating point. Only precision (p) can be specified |  |
| SMALLINT |  | SMALLINT | 2 byte integer type |  |
| INT |  | INTEGER | 4 byte integer type |  |
|  |  | BIGINT | 8 byte integer type |  |
| REAL |  | REAL | 4 byte real type |  |
| DOUBLE, BINARY_DOUBLE |  | DOUBLE | 8 byte real type |  |
| Date Type | DATE | Date type. January 1, 4712 BC-December 31, 9999 AD | DATE | Date Type 8byte |
| INTERVAL YEAR TO MONTH |  |  | Not supported |  |
| INTERVAL DAY TO SECOND |  |  | Not supported |  |
| TIMESTAMP WITH TIME ZONE |  |  | Not supported |  |
| TIMESTAMP WITH LOCAL TIME ZONE |  |  | Not supported |  |
| TIMESTAMP | The precision of the second information can be expressed up to 9 digits. | DATE | Express up to micro sec (6 digits) |  |
|  |  | TIMESTAMP | Option Type used in case of REPLICATION conflict |  |
| Binary Type | BFILE | Large binary file type. Up to 4G |  | Can be replaced with BLOB |
|  | RAW (*size*) | Primitive binary type. Up to 2000 bytes |  | Can be replaced with BLOB |
|  | LONG RAW | Variable-length Winshi binary type. Up to 2G |  | Use BLOB |
|  |  |  | BYTE | 1 to 32000, fixed length binary data type |
|  |  |  | NIBBLE | 1-254, variable length binary data type |
|  |  |  | BIT | 1~60576, consisting only of 0 and 1<br>Fixed-length binary data type |
|  |  |  | VARBIT | 1 to 131068, variable length binary data type consisting only of 0s and 1s |
| Spatial Data Type |  |  | GEOMETRY | Spatial data type up to 100M |

## API Comparison

---

| Feature | Oracle | Altibase | Remark |
| --- | --- | --- | --- |
| SQL | Standard SQL, transformed SQL | Standard SQL, transformed SQL |  |
| JDBC Driver | Provided | Provided |  |
| ODBC Driver | Provided | Provided |  |
| PHP Driver | Provided | Use ODBC |  |
| PDO Driver | Provided | Provided |  |
| Embedded SQL | Provided (Pro*C/C++) | Provided (APRE*C/C++) |  |
| CLI Interface | Provided (OCI) | Provided (CLi) |  |
| XA API | Provided | Provided |  |
| Threaded Application | Supported | Supported |  |

## Built-In Function

---

| Classification | Oracle | Altibase | Description |
| --- | --- | --- | --- |
| Numeric Function | ABS | ABS | Return absolute value |
| ACOS | ACOS | Return the arc cosine of n |  |
| ASIN | ASIN | Return the arc sine of n |  |
| ATAN | ATAN | Return the arctangent of n |  |
| ATAN2 | ATAN2 | Return the arc tangent of n/m |  |
| BITAND | BITAND | Return an integer by performing AND operation on the bits of argument 1 and 2 |  |
| BITNOT | BITNOT | Return the result fo NOT operation for the bits of bit_a |  |
| BITOR | BITOR | Return the result of OR operation for the bits of bit_a and bit_b |  |
| BITXOR | BITXOR | Return the XOR (exclusive OR) operation result for the bits of bit_a and bit_b |  |
| CEIL | CEIL | Round up the number specified in the argument and return an integer |  |
| COS | COS | Return the cosine value |  |
| COSH | COSH | Return the hyperbolic cosine |  |
| EXP | EXP | Return e to the power of n |  |
| FLOOR | FLOOR | Return the maximum value among integers less than or equal to a specified number |  |
| Not supported | ISNUMERIC | Determine whether the entered formula is valid as a numeric data type |  |
| LN | LN | Return the natural logarithm of the input |  |
| LOG | LOG | Return the logarithm of n with the base m in LOG(m,n) |  |
| MOD | MOD | Return the remainder of dividing n2 by n1 |  |
| NANVL | Not supported | If the input value n2 is Nan (non-numeric), the replacement value n1 is returned. If n2 is not NaN, return n2 |  |
| Not supported | NUMAND | Return the result of bitwise AND operation of BIGINT type bigint_a and bigint_a as BIGINT type result value |  |
| Not supported | NUMOR | Return the result of bitwise OR operation of BIGINT type bigint_a and bigint_a as BIGINT type result value |  |
| Not supported | NUMSHIFT | Return the result of shifting as many as n bits to bigint, which is a BIGINT type, as a result value of BIGINT type |  |
| Not supported | NUMXOR | Return the result of bitwise XOR operation of BIGINT type bigint_a and bigint_a as BIGINT type result value |  |
| POWER | POWER | Return the value of n2 to the power of n1 |  |
| Not supported | RAND | Generate a random number between 0 and less than 1 and return it as a double type value |  |
| dbms.random() | RANDOM | Return a pseudo-random integer value |  |
| REMAINDER | MOD | Return the remainder of n2 divided by n1 |  |
| ROUND (number) | ROUND (number) | Return n value after the decimal point is rounded to integer |  |
| SIGN | SIGN | Return the sign of n |  |
| SIN | SIN | Return the sine of n |  |
| SINH | SINH | Return the hyperbolic sine of n |  |
| SQRT | SQRT | Return the square root of n |  |
| TAN | TAN | Return the tangent of n |  |
| TANH | TANH | Returns the hyperbolic tangent of n |  |
| TRUNC (number) | TRUNC (number) | Truncate factor n1 to decimal place parameter n2 or less |  |
| WIDTH_BUCKET | Not supported | Create a histogram with the same area |  |
| Character functions that returns character values | Not supported | CHOSUNG | Extract and return only the first letter of each letter from the entered Hangul string |
| CHR | CHR | Return the ASCII code corresponding to the decimal number n |  |
| CONCAT | CONCAT | Concatenate char1 and char2 and return |  |
| Not supported | DIGEST | Return the hash digest of expr as a VARCHAR type using a quasi-encrypted hash algorithm. |  |
| Not supported | DIGITS | Return input integer as a string |  |
| INITCAP | INITCAP | Convert the first letter of each word from the input string to uppercase and the rest to lowercase and return |  |
| LOWER | LOWER | Convert input string to lower case |  |
| LPAD | LPAD | Fill expr1 from the specified digit n, and fill expr1 in the remaining space on the left |  |
| LTRIM | LTRIM | Remove all characters specified by set from the left side of the character string char |  |
| NCHR | NCHR | Return Unicode character |  |
| NLS_INITCAP | Not supported | Return char by converting the first letter of each word to uppercase and the remaining letters to lowercase |  |
| NLS_LOWER | Not supported | Convert all characters to lowercase and return |  |
| NLS_UPPER | Not supported | Return the input string converted to all uppercase letters |  |
| NLSSORT | Not supported | Sort input string and return string |  |
| Not supported | RANDOM_STRING | Create an arbitrary string as long as the length in the format specified in the option |  |
| REGEXP_REPLACE | REGEXP_REPLACE | Replace the part that satisfies the specified regular expression with another specified string |  |
| REGEXP_SUBSTR | REGEXP_SUBSTR | Return a substring that satisfies the specified regular expression |  |
| REPLACE | REPLACE | In the first string given as a parameter, all the second strings are replaced with the third-string and the result is returned |  |
| Not supported | REPLICATE | Return a string repeated expr n times |  |
| Not supported | REVERSE_STR | Return the result of inverting the character order of expr |  |
| RPAD | RPAD | To the right of the argument expr1, the character specified by the argument expr2 is repeated as long as n is necessary |  |
| RTRIM | RTRIM | Remove all characters specified by set from the right end of the argument char |  |
| Not supported | SIZEOF | Return the size of a string or the size allocated to it |  |
| SOUNDEX | Not supported | Return a string with the phonetic representation of char |  |
| Not supported | STUFF | Remove length from the position specified by start and return a string with expr2 inserted in that position |  |
| SUBSTR | SUBSTR<br>SUBSTRING | Return a string of length from the start character in expr |  |
| SUBSTRB | SUBSTRB | Determine position and length in bytes, not characters |  |
| TRANSLATE | TRANSLATE | Each character in from_string is replaced with the corresponding character in to_string and expr is returned |  |
| TREAT | Not supported | Change the declaration type of the argument |  |
| TRIP | TRIMp | Remove leading or trailing (both sides) characters from the string |  |
| UPPER | UPPER | Conver all letters to uppercase |  |
| Character functions that return numeric values | ASCII | ASCII | Return the decimal value corresponding to the ASCII value of the first character of a given char |
|  | Not supported | DATE_TO_UNIX | Convert expr of DATE type to a value in seconds based on 1970-01-01 00:00:00 (UTC +00:00 time zone) and return Returns the decimal value corresponding to the ASCII value of the first character of |
|  | INSTR | INSTR | Return the position of the first occurrence of the specified character in a string as a number |
|  | Not supported | INSTRB | Return the position of the specified string in bytes rather than characters |
|  | LENGTH | CHAR_LENGTH<br>CHARACTER_LENGTH<br>LENGTH | Return the length of the argument char |
|  | Not supported | LENGTHB | Return the length of the input string in bytes |
|  | Not supported | OCT_TO_NUM | Convert expr to octal |
|  | Not supported | PKCS7PAD16 | Fit the total byte length of expr to a multiple of 16 |
|  | Not supported | PKCS7UNPAD16 | Restore a multiple of 16 byte string created using the KCS7PAD16() function to the data before padding |
|  | Not supported | POSITION | Find substring in input expr string and return the position of the first character of the substring |
|  | REGEXP_COUNT | REGENX_COUNT | Return the number of times the pattern is bright in a string |
|  | REGEXP_INSTR | REGEXP_INSTR | Return the first position (what character) of the part that satisfies the specified condition (regular expression) |
| NLS character function | NLS_CHARSET_DECL_LEN<br>NLS_CHARSET_ID<br>NLS_CHARSET_NAME | Not supported | Return DB charset ID and name |
| Collation function | COLLATION<br>NLS_COLLATION_ID<br>NLS_COLLATION_NAME | Not supported | Return information about collation settings |
| Datetime function | ADD_MONTHS | ADD_MONTHS | Return the value of the date plus a specific number of months integer |
| Not supported | CONV_TIMEZONE | Convert expr based on src_tz time zone to dest_tz time zone |  |
| CURRENT_DATE | CURRENT_DATE | Return the date information of the current session as Date data type |  |
| CURRENT_TIMESTAMP | CURRENT_TIMESTAMP | Return the date and time information of the current session |  |
| +, - operation | +, -, DATEADD | Return the result by increasing the date_field_name part of date by the number |  |
| Not supported | DATEDIFF | Return the value of enddate minus startdate (i.e. enddate-startdate) in the unit specified in date_field_name |  |
| Not supported | DATENAME | Return the name of the month or weekday of the specified date according to the input date_field_name |  |
| DBTIMEZONE | DB_TIMEZONE | Return the value of the database time zone |  |
| EXTRACT (datetime) | DATEPART<br>EXTRACT (datetime) | Return only the value corresponding to date_field_name in the input date |  |
| FROM_TZ | Not supported | Convert timestamp data type and time zone data type to TIMESTAMP WITH TIME ZONE data type |  |
| LAST_DAY | LAST_DAY | Return the last day of the month in which the date belongs |  |
| LOCALTIMESTAMP | Not supported | Output the current date and time of timestamp |  |
| MONTHS_BETWEEN | MONTHS_BETWEEN | Calculate the month between date date1 and date2 |  |
| NEW_TIME | Not supported | Output the Zone1 time in zone2 time |  |
| NEXT_DAY | NEXT_DAY | Convert the next date of the specified weekday based on that day |  |
| NUMTODSINTERVAL | Not supported | Change n to INTERVAL DAY TO SECOND character |  |
| NUMTOYMINTERVAL | Not supported | Change n to INTERVAL YEAR TO MONTH character |  |
| ORA_DST_AFFECTED | Not supported |  |  |
| ORA_DST_CONVERT | Not supported |  |  |
| ORA_DST_ERROR | Not supported |  |  |
| ROUND (date) | ROUND (date) | Return the date rounded to the unit specified by the format model fmt |  |
| SESSIONTIMEZONE | SESSION_TIMEZONE | Reflect the time zone of the current session |  |
| SYS_EXTRACT_UTC | Not supported | Return Coordinated Universal Time—formerly Greenwich Mean Time (UTC) |  |
| SYSDATE | SYSDATE | Return the date and time of the OS where the database is located |  |
| SYSTIMESTAMP | SYSTIMESTAMP | Return the system date |  |
| TRUNC (date) | TRUNC (date) | Round or cut dates based on year, month, and day |  |
| TZ_OFFSET | Not supported | Return the time zone offset corresponding to the argument based on the date the statement was executed |  |
| Not supported | UNIX_DATE | Output the current date and time of the operating system based on the UTC +00:00 time zone |  |
| Not supported | UNIX_TIMESTAMP | Output the current date and time of the operating system based on the UTC +00:00 time zone |  |
| Not supported | UNIX_TO_DATE | Convert expr to DATE type and return |  |
| Comparison function | CASE | CASE, CASE2 | Convert expr to DATE type and return |
| GREATEST | GREATEST | Return the largest value among one or more arguments |  |
| LEAST | LEAST | Return the smallest value among the list of arguments EXPR |  |
| Conversion function | ACSIISTR | ASCIISTR | Return the ASCII string of a string |
|  | Not supported | BASE64_DECODE | Decode the input string of VARBYTE type encoded in base64 format and return the original data of VARBYTE type |
|  | Not supported | BASE64_DECODE_64 | VARBYTE type value is encoded in base64 format and VARBYTE type string is returned |
|  | Not supported | BASE64_ENCODE_STR | Return the result of base64-encoded hexadecimal input string as a VARCHAR type string. |
|  | Not supported | BINARY_LENGTH | Return the data length of binary data types such as BLOB, BYTE, and NIBBLE |
|  | BIN_TO_NUM | BIN_TO_NUM | Convert bit (binary) vector to equivalent number (decimal) |
|  | CAST | CAST | Convert data type or collection type to another data type or collection type |
|  | CHARTOROWID | Not supported | Convert character type value to ROWID type |
|  | COMPOSE | Not supported | Return Unicode in normalized form |
|  | CONVERT | CONVERT | Convert character set to another character set |
|  | DECOMPOSE | Not supported | Return the UNICODE string after decomposition into the same character set as the input |
|  | Not supported | HEX_DECODE | Convert hexadecimal string to ASCII string and return |
|  | Not supported | HEX_ENCODE | Convert ASCII string to hexadecimal string corresponding to each character and return |
|  | Not supported | HEX_TO_NUM | convert expr to decimal |
|  | HEXTORAW | Not supported | Convert hexadecimal to raw value |
|  | RAWTOHEX | Not supported | Convert RAW to hexadecimal characters |
|  | RAWTONHEX | Not supported | Convert RAW TO NVARCHAR2 hexadecimal number |
|  | Not supported | RAW_CONCAT | Concatenate and return values of multiple input VARBYTE data types that are not NULL |
|  | Not supported | RAW_SIZEOF | Return the actual size of the data space allocated to the input expr |
|  | Not supported | RAW_TO_FLOAT | Convert the value converted to VARBYTE data type to NUMERIC or FLOAT data type using TO_RAW function and return |
|  | Not supported | RAW_TO_INTEGER | Return the value converted to VARBYTE as INTEGER data type by using TO_RAW function |
|  | Not supported | RAW_TO_NUMERIC | Convert the value converted to VARBYTE data type to NUMERIC or FLOAT data type using TO_RAW function and return |
|  | Not supported | RAW_TO_VARCHAR | Convert VARCHAR type data to VARCHAR type data converted VARBYTE type value using the TO_RAW function |
|  | ROWIDTOCHAR | Not supported | Convert rowid value to VARCHAR2 format |
|  | ROWIDTOONCHAR | Not supported | Convert rowid value to NVARCHAR2 format |
|  | ROWNUM | ROWNUM | Order the value of a selected row, not supported in DML |
|  | SCN_TO_TIMESTAMP | Not supported | Take a number evaluated as a system change number (SCN) as an argument and return the nearest timestamp related to the SCN |
|  | TIMESTAMP_TO_SCN | Not supported | Return system change number (SCN) related to timestamp |
|  | Not supported | TO_BIN | Convert n to binary |
|  | TO_BiNARY_DOUBLE | Not supported | Return double-precision floating point |
|  | TO_BINARY_FLOAT | Not supported | Return a single-precision floating-point number |
|  | TO_BLOB (bfile) | Not supported | Convert BFILE to BLOB |
|  | TO_BLOB (raw) | Not supported | Convert RAW to BLOB |
|  | TO_CHAR (bfile\|blob) | Not supported | Convert BFILE and BLOB to database charset |
|  | TO_CHAR (character) | Not supported | Convert to database character set |
|  | TO_CHAR (datetime) | TO_CHAR (datetime) | Convert to VARCHAR data type value of specified format |
|  | TO_CHAR (number) | TO_CHAR (number) | Convert to VARCHAR data type value |
|  | TO_CLOB (bfile\|blob) | Not supported | Convert NCLOB value to CLOB value |
|  | TO_CLOB (character) | Not supported | Convert character value to CLOB |
|  | TO_DATE | TO_DATE | Convert char to date data type value |
|  | TO_DSINTERVAL | Not supported | Convert INTERVAR DAY TO SECOND value |
|  | Not supported | TO_HEX | Convert n to hexadecimal |
|  | Not supported | TO_INTERVAL<br>(NUMTODSINTERVAL) | Convert n to interval_unit unit and return |
|  | TO_LOB | Not supported | Convert LONG or LONG ROW value to LOB value |
|  | TO_MULTI_BYTE | Not supported | Return the character converted from a multibyte character to the corresponding single-byte character |
|  | TO_NCHAR (character) | TO_NCHAR (character) | Convert to national character set |
|  | TO_NCHAR (number) | TO_NCHAR (number) | Covert n to national character set |
|  | TO_NCHAR (datetime) | TO_NCHAR (datetime) | Convert to national character set |
|  | TO_NCLOB | Not supported | Convert CLOB value to NCLOB value |
|  | TO_NUMBER | TO_NUMBER | Convert expr to a value of data type NUMBER |
|  | Not supported | TO_OCT | Convert n to octal |
|  | Not supported | TO_RAW | Convert all data type values entered in n into VARBYTE type and return |
|  | TO_SINGLE_BYTE | Not supported | Convert multibyte characters into corresponding single-byte characters and return char |
|  | TO_TIMESTAMP | TO_DATE | Convert char to value of TIMESTAMP data type |
|  | TO_TIMESTAMP_TZ | Not supported | Convert char to TIMESTAMP WITH TIME ZONE data type |
|  | TO_YMINTERVAL | Not supported | Change string to INTERVAL YEAR TO MONTH format |
|  | TRANSLATE ... USING | Not supported | Convert char to the specified character set for conversion between the database character set and national character cents |
|  | UNISTR | UNISTR | Take a text string as an argument and return it as a national language character set |
|  | VALIDATE_CONVERSION | Not supported | Determine whether expr can be converted to the specified data type |
| Large Object (LOB) function | BFILENAME | Not supported | Return the BFILE locator associated with the physical LOB binary file of the server file system |
|  | EMPTY_BLOB | EMPTY_BLOB | Initialize lob variable and return the location of empty lob |
|  | EMPTY_CLOB | EMPTY_CLOB | Initialize lob variable and return the location of empty lob |
| Collection functions related to nested tables | CARDINALITY<br>COLLECT<br>POWERMULTISET<br>POWERMULTISET_BY_CARDINALITY<br>SET | Not supported | Functions related to nested tables |
| Hierarchical function | SYS_CONNECT_BY_PATH | SYS_CONNECT_BY_PATH | Return the column value Path from root to node |
| Data mining functions | CLUSTER_DETAILS<br>CLUSTER_DISTANCE<br>CLUSTER_ID<br>CLUSTER_PROBABILITY<br>CLUSTER_SET<br>FEATURE_COMPARE<br>FEATURE_DETAILS<br>FEATURE_ID<br>FEATURE_SET<br>FEATURE_VALUE<br>ORA_DM_PARTITION_NAME<br>PREDICTION<br>PREDICTION_BOUNDS<br>PREDICTION_COST<br>PREDICTION_DETAILS<br>PREDICTION_PROABILITY<br>PREDICTION_SET | Not supported | Data mining related functions |
| XML functions | APPRENDCHILDXML<br>DELETEXML<br>DEPTH<br>EXISTSNODE<br>EXTRACT (XML)<br>EXTRACTVALUE<br>INSERTCHILDXML<br>INSERTCHILDXMLAFTER<br>INSERTCHILDXMLBEFORE<br>INSERTXMLAFTER<br>INSERTXMLBEFORE<br>PATH<br>SYS_DBURIGEN<br>SYS_XMLAGG<br>SYS_XMLGEN<br>UPDATEXML<br>XMLAGG<br>XMLCAST<br>XMLCDATA<br>XMLCOLATTAVAL<br>XMLCOMMENT<br>XMLCONCAT<br>XMLDIFF<br>XMELEMENT<br>XMLEXISTS<br>XMLFOREST<br>XMLISVALID<br>XMLPARSE<br>XMLPATCH<br>XMLPI<br>XMLQUERY<br>XMLROOT<br>XMLSEQUENCE<br>XMLSERIALIZE<br>XMLTABLE<br>XMLTRANSFORM | Not supported | XML related functions |
| JSON functions | JSON_ARRAY<br>JSON_ARRAYAGG<br>JSON_DATAGUIDE<br>JSON_OBJECT<br>JSON_OBJECTAGG<br>JSON_QUERY<br>JSON_TABLE<br>JSON_VALUE | Not supported | JSON related functions |
| Encoding/Decoding functions | DECODE | DECODE | Same as CASE WHEN where simple_case_expr is used |
| DUMP | DUMP | Return the location and length of specified data in a specified format |  |
| ORA_HASH | Not supported | Calculate a hash value for a given expression |  |
| STANDARD_HASH | Not supported | Calculate standard hash value |  |
| VSIZE | OCTET_LENGTH | Return the length of the input string in bytes |  |
| NULL functions | COALESCE | COALESCE | Returns the first non-NULL argument |
| LNNVL | LNNVL | If the result of the condition is FALSE or NULL, TRUE is returned, and if the condition is TRUE, FALSE is returned |  |
| NULLIF | NULLIF | If expr1 and expr2 is the same, return NULL value |  |
| NVL | NVL | Replace NULL values with blanks in the query result |  |
| NVL2 | NVL2 | If expr1 is not NULL, NVL2 returns expr2. If it is NULL, expr3 is returned. |  |
| Environment and identifier functions | Not supported | HOST_NAME | Return the name of the currently connected host |
| CON_DBID_TO_ID<br>CON_GUID_TO_ID<br>CON_NAME_TO_ID<br>CON_UID_TO_ID<br>ORA_INVOKING_USER<br>ORA_INVOKING_USERID | Not supported |  |  |
| Not supported | SENDMSG | Send message to ip=address, port as Socket datagram |  |
| SYS_CONTEXT | SYS_CONTEXT | Return the result value of related parameters using the environment information (context) connected to the current session as a namespace |  |
| SYS_GUID | SYS_GUID_STR | Create and return a globally unique identifier (RAW value) consisting of 16 bytes.<br>Create a globally unique identifier of 16 bytes and returns it as a 32 hexadecimal string |  |
| SYS_TYPEID | Not supported | Return the typeid of the identifier |  |
| UID | USER_ID | Return an integer that uniquely identifies the session user |  |
| USER | USER_NAME | Return the name of the session user |  |
| USERENV | SESSION_ID | USERENV returns information about the session.<br>SESSION_ID returns the user's SESSION_ID |  |
| Approxiamtion functions | APPROX_COUNT_DISTINCT<br>APPROX_COUNT_DISTINCT_AGG<br>APPROX_COUNT_DISTINCT_DETAIL<br>APPROX_MEDIAN<br>APPROX_PERCENTILE<br>APPROX_PERCENTILE_AGG<br>APPROX_PERCENTILE_DETAIL | Not supported |  |
|  | GROUP_ID | Not supported | Distinguish duplicate groups from the specified GROUP BY result |
|  | GROUPING | GROUPING | When a column described in the GROUPING function is grouped by using it with the ROLLUP or CUBE operator.<br>In other words, a function that shows whether it was used in ROLLUP or CUBE operation. |
|  | GROUPING_ID | GROUPING_ID | Return the number corresponding to the GROUPING bit vector associated with the row |
|  | MEDIAN | Not supported | Returns the median or interpolated value after sorting of values |
|  | STAT_BINOMIAL_TEST | Not supported | An exact probability test used for dichotomous variables where only two valid values exist (variables with two exclusive values) |
|  | STATS_CROSSTAB | Not supported | Analyze two nominal variables |
|  | STATS_F_TEST | Not supported | Test whether there is a significant difference between the two variances |
|  | STATS_KS_TEST | Not supported | The Kolmogorov-Smirnov function that tests whether two samples belong to the same population or that they belong to a population with the same distribution |
|  | STATS_MODE | Not supported | Return the value with the largest frequency |
|  | STATS_MW_TEST | Not supported | A Mann-Whitney test compares two independent samples. |
|  | STATS_ONE_WAY_ANOVA | STATS_ONE_WAY_ANOVA | The one-way analysis of variance function (STATS_ONE_WAY_ANOVA) verifies the significant difference in the mean (for a group or variable) for statistical significance by comparing two other estimates of variance |
|  | STAT_T_TEST_(STATS_T_TEST_ONE, STAT_T_TEST_PAIRED, STATS_T_TEST_INDEP and STATS_T_TEST_INDEPU) | Not supported | In t-test, the significance of the difference between the mean values is measured |
|  | STATS_WSR_TEST | Not supported | Wilcox sign ranking test of paired pairs is performed, and the difference between samples is tested whether there is a significant difference from zero |
|  | SYS_OP_ZONE_ID | Not supported | Take a rowid as an argument and return the area ID |
|  | TO_APPROX_COUNT_DISTINCT | Not supported |  |
|  | TO_APPROX_PERCENTILE | NOt supported |  |
| Analysis functions | FIRST_VALUE | FIRST_VALUE | Return the first value in an ordered set of values |
| Not supported | FIRST_VALUE_IGNORE_NULLS | Get the value of the first row excluding null values |  |
| LAG | LAG | Refer to the previous value relative to the current row |  |
| Not supported | LAG_IGNORE_NULLS | Calculate the value of the first non-NULL row from the offset th after the current row |  |
| NTH_VALUE | NTH_VALUE | Find the value of the offset th row |  |
| Not supported | NTH_VALUE_IGNORE_NULLS | Find the value of the offset th row excluding null values |  |
| NTILE | NTILE | Divide the output result by the number of groups specified by the user and output it |  |
| RATIO_TO_REPORT | RATIO_TO_REPORT | Calculate the ratio of a value to the sum of a set of values |  |
| ROW_NUMBER | ROW_NUMBER | Give a ranking for the results sorted by division |  |
| Aggregation/analysis function | AVG | AVG | Return the average of the rows that satisfy the conditions for the specified column, excluding nulls |
|  | CORR | CORR | Return the correlation coefficient for a pair of numbers |
|  | CORR_ (CORR_S, CORR_K) | Not supported | (See CORR) Calculate Pearson's correlation coefficient |
|  | COUNT | COUNT | Return the number of rows returned by the query |
|  | COVAR_POP | COVAR_POP | Return the population covariance of a set of number combinations |
|  | COVAR_SAMP | COVAR_SAMP | Return the sample covariance of a set of number pairs |
|  | CUME_DIST | CUME_DIST | Compute the cumulative distribution of values in a group of values |
|  | DENSE_RANK | DENSE_RANK | Rank is given to the column or expression used in the ORDER BY clause. Unlike RANK(), the rank after the same rank returns a value that is increased by 1 regardless of the number of the same rank. |
|  | FIRST | FIRST | Operate on a set of values from a set of rows by ranking as FIRST or LAST for a given sort specification |
|  | Not supported | GROUP_CONCAT | Return the string concatenated with non-NULL expr1 in each group |
|  | LAST | LAST | The last row is extracted by sequencing the rows |
|  | LISTAGG | LISTAGG | Return a single string by concatenating a string and a separator for all rows in a group |
|  | MAX | MAX | Return the maximum value among arguments |
|  | MIN | MIN | Return the minimum value among arguments |
|  | PERCENT_RANK | PERCENT_RANK | Return the rank percentage of a value for the number of groups |
|  | PERCENTILE_CONT | PERCENTILE_CONT | Inverse distribution function assuming a continuous distribution model |
|  | PERCENTILE_DISK | PERCENTILE_DISC | Inverse distribution function assuming a discrete distribution model |
|  | RANK | RANK | Calculate the rank of values in a group of values |
|  | REGR_ (Linear Regression) Functions | Not supported | The linear regression function fits a normal least squares regression line to a set of numeric pairs |
|  | STDDEV | STDDEV | Return the sample standard deviation of expr, which is a combination of numbers |
|  | STDDEV_POP | STDDEV_POP | Calculate the population standard deviation and return the square root of the population variance |
|  | STDDEV_SAMP | STDDEV_SAMP | Calculate the cumulative sample standard deviation and returns the square root of the sample variance |
|  | SUM | SUM | Return the sum of the values of expr |
|  | VAR_POP | VAR_POP | Return the population variance of a set of Numbers after removing null values |
|  | VAR_SAMP | VAR_SAMP | Return the sampling variance of a set of numbers after removing nulls. |
|  | VARIANCE | VARIANCE | Return the variance of expr |
| Object reference functions | DEREF<br>MAKE_REF<br>REF<br>REFTOHEX<br>VALUE | Not supported | Object reference functions |
| Model functions | CV<br>ITERATION_NUMBER<br>PRESENTNNV<br>PRESENTV<br>PREVIOUS | Not supported | Available only in Model_clause of Select statement |
| OLAP function | CUBE_TABLE | Not supported | Convert 3D data to 2D data |
| Data cartridge function | DATAOBJ_TO_MAT_PARTITION<br>DATAOBJ_TO_PARTITION | Not supported | Useful for data cartridge development |
| Encryption | DBMS_CRYPTO | AESDECRYPT<br>AESENCRYPT<br>DESDECRYPT<br>DESENCRYPT<br>TDESDECRYPT<br>TRIPLE_DESDECRYPT<br>TDESENCRYPT<br>TRIPLE_DESENCRYPT |  |
