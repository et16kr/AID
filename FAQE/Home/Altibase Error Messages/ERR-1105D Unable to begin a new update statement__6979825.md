---
title: "ERR-1105D Unable to begin a new update statement"
page_id: "6979825"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-1105D+Unable+to+begin+a+new+update+statement"
updated_at: "2014-10-21T16:46:52.000+0900"
version: 16
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-1105D Unable to begin a new update statement
Source: https://docs.altibase.com/display/FAQE/ERR-1105D+Unable+to+begin+a+new+update+statement
Updated: 2014-10-21T16:46:52.000+0900

- [Version](#ERR-1105DUnabletobeginanewupdatestatement-Version)
- [Explanation](#ERR-1105DUnabletobeginanewupdatestatement-Explanation)
- [Cause](#ERR-1105DUnabletobeginanewupdatestatement-Cause)
- [Action](#ERR-1105DUnabletobeginanewupdatestatement-Action)
- [Reference](#ERR-1105DUnabletobeginanewupdatestatement-Reference)

## Version

6.1.1 or below.

The error code and message have been changed for 6.3.1

## Explanation

The following error occurs when a user function is used inside the SELECT statement:

```
iSQL> select func1() from dual;
```

[ERR-1105D : Unable to begin a new update statement. 0004 : insert into T1 values(C1);]

The error code and message have been changed for 6.3.1 as follows:

```
iSQL> select func1() from dual;
```

[ERR-31386 : Cannot perform a DML, commit, or rollback inside a query.

In FUNC1 0004 : insert into T1 values(C1); ^ ^ ]

## Cause

The following error descriptions can be viewed with the AltiErr utility:

# 6.1.1 or below

$ altierr 0x1105D 0x1105D ( 69725) smERR_ABORT_smiCantBeginUpdateStatement Unable to begin a new update statement.

# *Cause: Either the statement is read-only, or more than one update child statement has been requested.

# *Action: Please make sure that the request to begin a new update statement is valid.

# 6.3.1

$ altierr 0x31386 0x31386 ( 201606) qpERR_ABORT_QSX_PSM_INSIDE_QUERY Cannot perform a DML, commit, or rollback inside a query.

# *Cause :

# - The program attempted to perform a DML, commit, or rollback inside a query.

# *Action :

# - Do not use a DML, commit, or rollback statement inside a query.

When a user function is used inside the SELECT statement, the function must only include the SELECT statement.

However, this error occurs when DMLs are included in a user function.

## Action

Remove the DML statement from a user function inside the SELECT statement.

# In the following example, the error occurs when a function including the INSERT statement is used within the SELECT statement.

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
```

[ERR-1105D : Unable to begin a new update statement. 0004 : insert into T1 values(C1); ^ ^ ]

# In the following example, the above function is successfully executed using the EXECUTE statement

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

# In the following example, the function is successfully executed when the INSERT statement is removed from the SELECT statement.

```
iSQL> create or replace function func1() return varchar(10) as c1 varchar(10);
    2 begin
    3 select c1 into c1 from t1;
    4 return c1;
    5 end;
    6 /
Create success.
```

```
iSQL> select func1() from dual;
FUNC1
--------------
abc
1 row selected.
```

## Reference

N/A
