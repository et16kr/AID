---
title: "ERR-1105D Unable to begin a new update statement."
page_id: "22642969"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=22642969"
updated_at: "2025-10-20T15:47:14.000+0900"
version: 1
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# ERR-1105D Unable to begin a new update statement.
Source: https://docs.altibase.com/pages/viewpage.action?pageId=22642969
Updated: 2025-10-20T15:47:14.000+0900

- [Overview](#ERR-1105DUnabletobeginanewupdatestatement.-Overview) - [Version](#ERR-1105DUnabletobeginanewupdatestatement.-Version) - [Symptom](#ERR-1105DUnabletobeginanewupdatestatement.-Symptom) - [Cause](#ERR-1105DUnabletobeginanewupdatestatement.-Cause) - [Solution](#ERR-1105DUnabletobeginanewupdatestatement.-Solution)

# **Overview**

---

This document describes the causes and recommended actions for handling ERR-1105D and ERR-31386 errors that may occur during query execution.

```
ERR-1105D : Unable to begin a new update statement.
```

```
ERR-31386 : Cannot perform a DML, commit, or rollback inside a query.
```

# Version

---

In Altibase version 6.1.1 and earlier, only the ERR-1105D error code and message are generated. Starting from versions 6.3.1, 6.5.1, and 7.1.0 or later, the error code was updated to ERR-31386, and the message format was modified accordingly.

# Symptom

---

The following error occurs when a function is used inside a SELECT statement.

6.1.1 or earlier

```
iSQL> select func1() from dual;
[ERR-1105D : Unable to begin a new update statement.
0004 :       insert into T1 values(C1);
            ^                         ^
]
```

6.3.1, 6.5.1

```
iSQL> select func1() from dual;
[ERR-31386 : Cannot perform a DML, commit, or rollback inside a query.

In FUNC1
0004 :  insert into T1 values(C1);
       ^                         ^
]
```

7.1.0 or later

```
iSQL> select func1() from dual;
[ERR-31386 : Cannot perform a DML, commit, or rollback inside a query.
at "SYS.FUNC1", line 4]
```

# Cause

---

The description of the error can be checked using the altierr utility as follows.

6.1.1 or earlier

$ altierr 0x1105D 0x1105D ( 69725) smERR_ABORT_smiCantBeginUpdateStatement Unable to begin a new update statement. # *Cause: Either the statement is read-only, or more than one update child statement has been requested. # *Action: Please make sure that the request to begin a new update statement is valid.

6.3.1 or later

$ altierr 0x31386 0x31386 ( 201606) qpERR_ABORT_QSX_PSM_INSIDE_QUERY Cannot perform a DML, commit, or rollback inside a query. # *Cause : # - The program attempted to perform a DML, commit, or rollback inside a query. # *Action : # - Do not use a DML, commit, or rollback statement inside a query.

When using a function within a SELECT statement, the function must contain only the SELECT statement.

If the function includes INSERT/UPDATE, the above error occurs.

# Solution

---

Functions used within the SELECT statement must contain only the select statement.

# Example of where an error occurs when a function including an insert statement is used in a SELECT statement

```
iSQL> create or replace function func1() return varchar(10) as c1 varchar(10);
2 begin
3 select c1 into c1 from t1;
4 insert into t1 values(c1);
5 return c1;
6 end;
7 /
Create success.
iSQL> select func1() from dual;
[ERR-1105D : Unable to begin a new update statement.
0004 :       insert into T1 values(C1);
            ^                         ^
]
```

# Example of executing the above function using execute statement

Executed successfully in the execute statement.

```
iSQL> select * from t1;
C1
--------------
abc
1 row selected.
iSQL> var c1 varchar(10);
iSQL> exec :c1 := func1();
Execute success.
iSQL> print var;
[ HOST VARIABLE ]
-------------------------------------------------------
NAME                 TYPE                 VALUE
-------------------------------------------------------
C1                   VARCHAR(10)          abc
iSQL> select * from t1;
C1
--------------
abc
abc
2 rows selected.
```

# Example that is successfully executed when the above function is used in the SELECT statement after removing the insert statement to use it in the SELECT statement.

```
iSQL> create or replace function func1() return varchar(10) as c1 varchar(10);
2 begin
3 select c1 into c1 from t1;
4 return c1;
5 end;
6 /
Create success.
iSQL> select func1() from dual;
FUNC1
--------------
abc
1 row selected.
```
