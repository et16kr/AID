---
title: "2-3 Stored Procedure / Function Conversion"
page_id: "14647326"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=14647326"
updated_at: "2021-02-18T17:49:56.000+0900"
version: 6
ancestors: ["Home", "Altibase Oracle Conversion Guide", "2. Environment Setting"]
labels: []
---

# 2-3 Stored Procedure / Function Conversion
Source: https://docs.altibase.com/pages/viewpage.action?pageId=14647326
Updated: 2021-02-18T17:49:56.000+0900

---

## **Procedure processing in ALTIBASE AUTOCOMMIT mode**

COMMIT automatically after executing PROCEDURE/FUNCTION. Therefore, after executing DML statements in PROCEDURE/FUNCTION, the result may be different between ALTIBASE and Oracle.

If ALTIBASE is applied in the NON-AUTOCOMMIT mode, the same results as Oracle's NON-AUTOCOMMIT mode are displayed.

**Oracle**

```
CREATE OR REPLACE PROCEDURE t1_test( in_t IN INTEGER, in_v IN VARCHAR)
IS
BEGIN
    INSERT INTO t1 VALUES(in_t, in_v);
    ROLLBACK;
END;
/
EXEC t1_test(4, '000004');
SQL> SELECT COUNT(*) FROM t1;
COUNT(*)
-----------------
0
```

**Altibase**

```
CREATE OR REPLACE PROCEDURE t1_test( in_t IN INTEGER, in_v IN VARCHAR(20))
IS
BEGIN
    INSERT INTO t1 VALUES(in_t, in_v);
    ROLLBACK;
END;
/
EXEC t1_test(4,   '000004');
iSQL> SELECT COUNT\(*) FROM t1;
COUNT
-----------
1
```

## **TYPE and RETURN TYPE of PARAMETER**

TYPE of PARAMETER and CHAR, VARCHAR of RETURN TYPE must be sized.

In ALTIBASE, if PARAMETER or RETURN TYPE of PROCEDURE or FUNCTION is declared as CHAR or VARCHAR like Oracle, it has the same meaning as CHAR(1) and VARCHAR(1). Therefore, if the user wants to use a string rather than a single character, the user must specify its size. If not specified and the string is more than 2 characters, the following error occurs.

```
ERR-2100D : Invalid length of the data type
```

## **File and Output processing**

ALTIBASE files and outputs related PROCEDUREs are automatically created in the SYSTEM_ user and defined as PUBLIC SYNONYM, so users can call and use only the PROCEDURE name.

| Classification | **Oracle** | **ALTIBASE** |
| --- | --- | --- |
| Standard output | DBMS_OUTPUT.PUT | PRINT |
| Standard output | DBMS_OUTPUT.PUT_LINE | PRINTLN |
| File processing | UTL_FILE.FOPEN | FOPEN |
| File processing | UTL_FILE.FCLOSE | FCLOSE |
| File processing | UTL_FILE.FCLOSE_ALL | FCLOSE_ALL |
| File processing | UTL_FILE.FCOPY | FCOPY |
| File processing | UTL_FILE.FFLUSH | FFLUSH |
| File processing | UTL_FILE.FREMOVE | FREMOVE |
| File processing | UTL_FILE.FRENAME | FRENAME |
| File processing | UTL_FILE.GET_LINE | GET_LINE |
| File processing | UTL_FILE.IS_OPEN | IS_OPEN |
| File processing | UTL_FILE.NEW_LINE | NEW_LINE |

## **REF CURSOR**

The REF CURSOR of ORACLE is usually declared in PACKAGE, and it is declared as OUT PARAMETER of PROCEDURE and used. However, ALTIBASE does not provide PACKAGE, so it must be created and used as TYPESET.

**Oracle**

```
CREATE OR REPLACE PACKAGE ref_cursor_pkg
AS
TYPE ref_type IS REF CURSOR;
PROCEDURE ref_cursor_pro(v_result OUT ref_type, v_sql IN VARCHAR2);
END;
/
CREATE OR REPLACE PACKAGE BODY ref_cursor_pkg
AS
PROCEDURE ref_cursor_pro(v_result OUT ref_type, v_sql IN VARCHAR2)
AS
BEGIN OPEN v_result FOR v_sql [USING] [Bind Var];
END;
/
```

**ALTIBASE**

```
CREATE OR REPLACE TYPESET my_type
AS
TYPE my_cur IS REF CURSOR;
END;
/
CREATE OR REPLACE PROCEDURE opencursor( v_result OUT my_type.my_cur, v_sql IN VARCHAR(200) )
AS
BEGIN
    OPEN y_result FOR v_sql \[USING\] \[Bind Var\];
END;
/
```

## **WHERE CURRENT OF Statement**

ALTIBASE does not support the WHERE CURRENT OF statement using CURSOR. However, if there is a PRIMARY KEY in the table, it can be changed as follows.

**Oracle**

```
CREATE OR REPLACE PROCEDURE proc1
IS

CURSOR emp_list IS
       SELECT empno FROM employee
       WHERE empno = 1 FOR UPDATE;

BEGIN FOR emplst IN emp_list LOOP
    UPDATE employee SET empjob = 'SALESMAN'
     WHERE CURRENT OF emp_list;
END LOOP;
END;
/
```

**ALTIBASE**

```
CREATE OR REPLACE PROCEDURE proc1
AS
BEGIN
DECLARE CURSOR cur1 IS
SELECT empno FROM employee
WHERE empno = 1;

v_empjob VARCHAR(10);
v_empno INTEGER;

BEGIN
    OPEN cur1;
    LOOP FETCH cur1 INTO v_empno, v_empjob;
    EXIT WHEN cur1%NOTFOUND;
    UPDATE employee SET empjob = 'SALESMAN’ WHERE emp_no = v_empno; //emp_no가 PK이어야 한다.
END LOOP;
CLOSE cur1;
END;
END;
/
```

## **EXCEPTION**

Oracle and ALTIBASE have previously defined EXCEPTIONs that occur in Stored PROCEDURE/FUNCTION in the system.

| **Oracle** |  | **ALTIBASE** |  |
| --- | --- | --- | --- |
| **SQLERRM** | **SQLCODE** | **SQLERRM** | **SQLCODE** |
| CURSOR_ALREADY_OPEN | -6530 | CURSOR_ALREADY_OPEN | 201062 |
| DUP_VAL_ON_INDEX | -1 | DUP_VAL_ON_INDEX | 201063 |
| INVALID_CURSOR | -1001 | INVALID_CURSOR | 201064 |
| INVALID_NUMBER | -1722 | INVALID_NUMBER | 201065 |
| NO_DATA_FOUND | +100 | NO_DATA_FOUND | 100 |
| PROGRAM_ERROR | -6501 | PROGRAM_ERROR | 201067 |
| STROAGE_ERROR | -6500 | STROAGE_ERROR | 201068 |
| TIMEOUT_ON_RESOURCE | -51 | TIMEOUT_ON_RESOURCE | 201069 |
| TOO_MANY_ROWS | -1422 | TOO_MANY_ROWS | 201070 |
| VALUE_ERROR | -6502 | VALUE_ERROR | 201071 |
| ZERO_DIVIDE | -1476 | ZERO_DIVIDE | 201072 |
| ACCESS_INTO_NULL | -6530 |  | Not supported |
| CASE_NOT_FOUND | -6592 |  | Not supported |
| COLLECTION_IS_NULL | -6531 |  | Not supported |
| LOGIN_DENIED | -1017 |  | Not supported |
| NOT_LOGGED_ON | -1012 |  | Not supported |
| ROWTYPE_MISMATCH | -6504 |  | Not supported |
| SELF_IS_NULL | -30625 |  | Not supported |
| SUBSCRIPT_BEYOND_COUNT | -6533 |  | Not supported |
| SUBSCRIPT_OUTSIDE_LIMIT | -6532 |  | Not supported |
| SYS_INVALID_ROWID | -1410 |  | Not supported |
