---
title: "ERR-21011 : Invalid literal"
page_id: "16876425"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-21011+%3A+Invalid+literal"
updated_at: "2021-03-30T14:07:42.000+0900"
version: 2
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# ERR-21011 : Invalid literal
Source: https://docs.altibase.com/display/FAQE/ERR-21011+%3A+Invalid+literal
Updated: 2021-03-30T14:07:42.000+0900

- [Overview](#ERR-21011:Invalidliteral-Overview) - [Version](#ERR-21011:Invalidliteral-Version) - [Cause](#ERR-21011:Invalidliteral-Cause)

# Overview

---

This document describes the causes and examples of invalid literal error.

# Version

---

All the versions of Altibase

# Cause

---

It occurs when the data types between comparison targets do not match when using conversion functions such as TO_NUMBER and CAST or comparison operators.

It can also occur when you have a value that cannot be converted to the data type you want to convert during automatic casting.

#### Case 1. When using UNION and UNION ALL, the data type of the column to be mapped is different.

```
 iSQL> SELECT 0 from DUAL
    2 UNION
    3 SELECT 'A' from DUAL;
0
--------------
0
[ERR-21011 : Invalid literal]
1 row selected.
```

#### Case 2. When the value given to the TO_NUMBER function is a character type that cannot be converted to a numeric type.

```
iSQL> SELECT TO_NUMBER('1-1') from DUAL;
[ERR-21011 : Invalid literal
0001 : SELECT TO_NUMBER('1-1') from DUAL
                       ^    ^
]
iSQL>
```

#### Case 3. When there is a data value that cannot be converted automatically in a column used in a comparison operation.

```
iSQL> CREATE TABLE T (NO CHAR(1));
Create success.
iSQL> INSERT INTO T VALUES('1');
1 row inserted.
iSQL> INSERT INTO T VALUES('2');
1 row inserted.
iSQL> SELECT * FROM T WHERE NO = 1;         -- Compare the value of the CHAR type column with the numeric data. NO column value is automatically converted to numeric type.
NO                                          -- Since only values that can be converted to numeric type exist in the NO column, it is executed without error.
------
1
1 row selected.

iSQL> INSERT INTO T VALUES('A');            -- A value that cannot be converted to a numeric type is entered in the NO column.
1 row inserted.
iSQL> SELECT * FROM T WHERE NO = 1;         -- As the value of the NO column is automatically converted into a numeric type, an invalid literal error occurs due to the value of'A'.
[ERR-21011 : Invalid literal]

iSQL> SELECT * FROM T WHERE NO = '1';       -- For character columns, single quotation marks (') must be used for comparison values.
NO
------
1
1 row selected.

iSQL> INSERT INTO T VALUES(' ');            -- An Invalid literal error occurs even if the NO column contains blank characters.
1 row inserted.
iSQL> SELECT TO_NUMBER(NO) FROM T;
[ERR-21011 : Invalid literal]

iSQL> SELECT TO_NUMBER(TRIM(NO)) FROM T;    -- In the case of space characters, the error can be eliminated by using the TRIM function.
TO_NUMBER(TRIM(CODE))
------------------------
1
2

3 rows selected.
iSQL>
```
