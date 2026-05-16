---
title: "2-2 SQL Conversion"
page_id: "14647324"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/2-2+SQL+Conversion"
updated_at: "2021-02-18T17:47:43.000+0900"
version: 5
ancestors: ["Home", "Altibase Oracle Conversion Guide", "2. Environment Setting"]
labels: []
---

# 2-2 SQL Conversion
Source: https://docs.altibase.com/display/arch/2-2+SQL+Conversion
Updated: 2021-02-18T17:47:43.000+0900

## **- #id-2-2SQLConversion- - [Math Function](#id-2-2SQLConversion-MathFunction) - [String Function](#id-2-2SQLConversion-StringFunction) - [Date Function](#id-2-2SQLConversion-DateFunction) - [Compare Function](#id-2-2SQLConversion-CompareFunction) - [Convert Function](#id-2-2SQLConversion-ConvertFunction) - [Encode/Decode Function](#id-2-2SQLConversion-Encode/DecodeFunction) - [Large Object Function](#id-2-2SQLConversion-LargeObjectFunction) - [Analyze Function](#id-2-2SQLConversion-AnalyzeFunction)**

---

## **Math Function**

| **Oracle** | **ALTIBASE** | Remark |
| --- | --- | --- |
| ABS | ABS | Return absolute value |
| ACOS | ACOS | arc cosine of n |
| ASIN | ASIN | arc sine of n |
| ATAN | ATAN | arc tangent of n |
| ATAN2 | ATAN2 | ATAN2(n,m) returns the arc tangent of n/m |
| AVG | AVG | Calculate the average value of the expr value of a row |
| BITAND | BITAND | Return an integer by performing and operation on the bits of argument 1 and 2 |
| CEIL | CEIL | Return an integer by rounding up the number specified in the argument |
| COS | COS | Return the cosine of n |
| COSH | COSH | Return the hyperbolic cosine of n |
| COUNT | COUNT | Analysis function that counts the number of rows. |
| DENSE_RANK | DENSE_RANK | Like the RANK function, the DENSE_RANK function ranks by a specific member of a result set or partition. However, after a duplicate ranking occurs, the next ranking is placed without skipping. The return value type is BIGINT. |
| EXP | EXP | Return e to the power of n |
| FLOOR | FLOOR | Return the largest integer less than or equal to a specified number |
| LAG | LAG | Calculate the value of the previous offset-throw based on the current row in each sorted partition |
| LN | LN | Calculate the input natural logarithm |
| LOG(N,M) | LOG(N,M) | Return the logarithm of m with the base n |
| MOD | MOD | Return the remainder of dividing n2 by n1 |
| NANVL | N/A | If the input value n2 is not numeric, it returns the replacement value n1 |
| NTH_VALUE | NTH_VALUE | Calculate the value of the offset-th row in the partition or window |
| POWER | POWER | Return n2 to the power of 1n1 |
| ROUND | ROUND | Return n value after the decimal point is rounded to integer |
| ROW_NUMBER | ROW_NUMBER | The ROW_NUMBER function assigns a number of consecutive unique numbers based on a specific member of a result set or partition. Starting from 1, it assigns in the order specified in the ORDER by expression. |
| SIGN | SIGN | Return the sign of n |
| SIN | SIN | Return the sine of n |
| SINH | SINH | Return the hyperbolic sine of n |
| SQRT | SQRT | Return the square root of n |
| STDDEV | STDDEV | Return the standard deviation of the input expression |
| TAN | TAN | Return the tangent of N |
| TANH | TANH | Return the hyperbolic tangent of N |
| VARIANCE | VARIANCE | Return the amount of variation in the input expressions |

## **String Function**

| **Oracle** | **ALTIBASE** | Remark |
| --- | --- | --- |
| CONCAT | CONCAT | concatenate char1 and char2 and return |
| CHR | CHR | Return the character corresponding to the number |
| NCHR | NCHR | Convert Unicode characters |
| LOWER | LOWER | Convert the input string to lowercase |
| UPPER | UPPER | Return input string in upper case |
| LPAD | LPAD | Fills EXPR1 from the specified number of digits N, and fill expr1 in the remaining space on the left |
| LTRIM | LTRIM | Remove all characters specified by the set from the left side of the character string char |
| RTRIM | RTRIM | Remove all characters specified by the set from the right side of the character string char. |
| RPAD | RPAD | To the right of the argument expr1, the character specified by the argument expr2 is repeated as long as n is necessary. |
| RPAD | RPAD | Fill in spaces to the right of the argument expr1 |
| SOUNDEX | N/A | Return a string with the sound representation of char |
| SUBSTR | SUBSTR | Extract and return the string as long as Substring_Length character length from the position character position in the character string Char |
| REPLACE | REPLACE2 | In the first string given as a parameter, all the second strings are replaced with the third-string and the result is returned |
| REGEXP_REPLACE/SUBSTR | N/A | Replace and return the part that satisfies the specified regular expression |
| INITCAP | INITCAP | Convert the first letter of each word in the input string to upper case |
| NLS_INITCAP | N/A | Convert the first letter of each word in the input string to uppercase (multilingual support) |
| NLSSORT | N/A | Sort the input string and return a string |
| TRANSLATE | TRANSLATE | Replace Each character in from_string with the corresponding character in to_sting and return expr |
| TO_CHAR | TO_CHAR | Return as CHAR type |
| TREAT | N/A | Change the declaration type of argument |
| NLS_CHARSET_DECL_LEN | N/A | Return the declared width of the NCHR column |
| NLS_CHARSET_ID | N/A | Return the ID number corresponding to the charset name |
| ASCII | ASCII | Return the decimal value corresponding to the ASCII value of the first character of a given char |
| INSTR | INSTR | Return the first occurrence of a specified character in a string as a number |
| LENGTH | LENGTH | Return the length of the argument char |
| LENGTHB | LENGTHB | Calculate length in bytes instead of char |
| REGEXP_INSTR | REGEXP_INSTR | Return the first position of the part that satisfies the specified condition (regular expression) |

## **Date Function**

| **Oracle** | **ALTIBASE** | Remark |
| --- | --- | --- |
| (use +) | (use +) | Return the date plus integer from the date date |
| (use - ) | (use -) | Return the date minus integer from the date Date |
| ADD_MONTHS | ADD_MONTHS | Return the value of the date plus a specific number of months integer |
| CURRENT_DATE | CURRENT_DATE | Return the date information of the current session in date type |
| CURRENT_TIME | N/A | Output the current time based on the time zone of the current session. |
| CURRENT_TIMESTAMP | CURRENT_TIMESTAMP | Return the date and time information of the current session (* is an alias of CURRENT_DATE) |
| LAST_DAY | LAST_DAY | Return the last date of the month in which the date belongs |
| NEW_TIME | CONV_TIMEZONE | Output date,zone1 time zone in zone2 time zone |
| NEXT_DAY | NEXT_DAY | Return the next day of the specified weekday from that day |
| ROUND | ROUND | Return the date rounded to the specified unit |
| TRUNC | TRUNC | Return date by truncating to the specified unit |
| EXTRACT(datetime) | EXTRACT(datetime) | Extract and return the value of the specified date range from a specific date, time value, or date value expression |
| LOCALTIMESTAMP | DB_TIMEZONE | Output the current date and time of the timestamp |
| SYSTIMESTAMP | SYSTIMESTAMP | Return system date |
| MONTHS_BETWEEN | MONTHS_BETWEEN | Output data in time zone between date1 and date 2 |
| TO_CHAR(datetime) | TO_CHAR(datetime) | Convert to data of varchar2 type with user-specified form |
| TO_NUMBER(TO_CHAR()) | TO_NUMBER(TO_CHAR()) | Convert to the specified number format |
| TO_DATE | TO_DATE | Convert to the specified date format |
| TO_DSINTERVAL | Replaceable with DATEDIFF | Convert to interval year to month format |
| SYSDATE | SYSDATE | Return the date and time of the OS with the database |
| N/A | DATENAME | Return the month or weekday name from the specified date according to `date_field_name` |
| N/A | DATEDIFF | Return enddate minus startdate (ie enddate-startdate) in the unit specified in date_field_name |
| N/A | DATEPART | Return only the value corresponding to date_field_name in the input date |
| N/A | DATEADD | Increment data_filed_name part of date by number and return the result |

## **Compare Function**

| **Oracle** | **ALTIBASE** | Remark |
| --- | --- | --- |
| GREATEST | GREATEST | Return the largest of one or more arguments |
| LEAST | LEAST | Return the smallest value among the list of expr arguments |

## **Convert Function**

| **Oracle** | **ALTIBASE** | Remark |
| --- | --- | --- |
| CAST | CAST | Convert data format |
| CONVERT | CONVERT | Convert specified character set |
| RAWTOHEX | N/A | Convert RAW to hexadecimal characters |
| HEXTORAW | N/A | Convert hexadecimal to the raw value |
| RAWINTOCHAR | N/A | Convert rowid value to VARCHAR2 format |
| SCN TO TIMESTAMP | N/A | Convert to system change number (SCN) |
| TO_BINARY_DOUBLE | N/A | Convert binary double floating-point |
| TO_CLOB | N/A | Convert nclob value to clob value |
| TO_LOB | N/A | Convert long or long raw values to lob values |
| COLEASE | COLEASE | Check the listed values sequentially and return the first non-NULL argument |
| LNNVL | N/A | Method for evaluating conditional statements when one or both operators of the condition are NULL |
| NULLIF | NULLIF | If expr1 and expr2 are the same, return the null value |
| NVL | NVL | Replace NULL (returned as blank) value in the query result |
| NVL2 | NVL2 | If expr1 is not NULL, return expr2. If it is NULL, return expr3. |

## **Encode/Decode Function**

| **Oracle** | **ALTIBASE** | Remark |
| --- | --- | --- |
| DECODE | DECODE | Bring IF statements from programming languages into SQL and PL/SQL |
| DUMP | DUMP | Return the location and length of specified data in a specified format |
| VSIZE | SIZEOF | Return the number of bytes in the internal representation of expr |

## **Large Object Function**

| **Oracle** | **ALTIBASE** | Remark |
| --- | --- | --- |
| EMPTY_BLOB/EMPTY_CLOB | N/A | Initialize LOB variable |
| BFILENAME | N/A | Return the BFILE Locator associated with the physical LOB BinaryFile of the Server File System. |

## **Analyze Function**

| **Oracle** | **ALTIBASE** | Remark |
| --- | --- | --- |
| MAX | MAX | Return the maximum value among arguments |
| MIN | MIN | Return the minimum value among arguments |
| SUM | SUM | Sum of row expr |
| RANK | RANK | Rank of values in groups of values |
| LEAD | LEAD | Reference lead values based on the present type |
| GROUP_ID | N/A | Distinguish duplicate groups from the specified GROUP BY result |
| FIRST_VALUE | FIRST_VALUE | Calculate the value of the first row in a partition or window |
| LAST_VALUE | LAST_VALUE | Calculate the value of the last row in the partition or window |
