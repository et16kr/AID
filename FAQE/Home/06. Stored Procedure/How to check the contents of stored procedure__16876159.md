---
title: "How to check the contents of stored procedure"
page_id: "16876159"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/How+to+check+the+contents+of+stored+procedure"
updated_at: "2021-04-05T09:48:26.000+0900"
version: 4
ancestors: ["Home", "06. Stored Procedure"]
labels: []
---

# How to check the contents of stored procedure
Source: https://docs.altibase.com/display/FAQE/How+to+check+the+contents+of+stored+procedure
Updated: 2021-04-05T09:48:26.000+0900

- [Overview](#Howtocheckthecontentsofstoredprocedure-Overview) - [Version](#Howtocheckthecontentsofstoredprocedure-Version) - [How to check](#Howtocheckthecontentsofstoredprocedure-Howtocheck) - [Using meta table](#Howtocheckthecontentsofstoredprocedure-Usingmetatable) - [Using the aexport utility](#Howtocheckthecontentsofstoredprocedure-Usingtheaexportutility)

# Overview

---

This document describes how to check the contents of stored procedures.

# Version

---

All versions of ALTIBASE HDB

# How to check

---

There are two ways to check stored procedure contents.

- Use meta tables
- Use the `aexport` utility

## Using meta table

---

After creating user-defined helper procedures that use the `SYSTEM_.SYS_PROCEDURES_` and `SYSTEM_.SYS_PROC_PARSE_` meta tables, use them to check stored procedure contents.

### How to create a custom procedure

- **Stored procedure for listing stored procedures and user-defined functions**

  **Query stored procedure and user-defined function names**

  ```
  -- Output stored procedure and user-defined function names to the screen.
  -- EXEC showProcedures;
  CREATE OR REPLACE PROCEDURE showProcedures
  AS
   CURSOR C1 IS
      SELECT U.USER_NAME, PROC.PROC_NAME,
             DECODE(PROC.OBJECT_TYPE, 0, 'PROCEDURE', 1, 'FUNCTION')
        FROM SYSTEM_.SYS_PROCEDURES_ PROC, SYSTEM_.SYS_USERS_ U
       WHERE PROC.USER_ID = U.USER_ID;
      V1 CHAR(40);
      V2 CHAR(40);
      V3 CHAR(20);
  BEGIN
      SYSTEM_.PRINTLN('----------------------------------------------------------------------------------------------------');
      SYSTEM_.PRINT(' USER_NAME                               PROC_NAME');
      SYSTEM_.PRINTLN('                               PROCEDURE/FUNCTION');
      SYSTEM_.PRINTLN('----------------------------------------------------------------------------------------------------');
      OPEN C1;
      LOOP
          FETCH C1 INTO V1, V2, V3;
          EXIT WHEN C1%NOTFOUND;
          SYSTEM_.PRINT(' ');
          SYSTEM_.PRINT(V1);
          SYSTEM_.PRINT(V2);
          SYSTEM_.PRINTLN(V3);
      END LOOP;
      SYSTEM_.PRINTLN('----------------------------------------------------------------------------------------------------');
      CLOSE C1;
  END;
  /
  ```
- **Stored procedure to check the contents of the stored procedure**

  **User-defined procedure to check stored procedure contents**

  ```
  -- Output the contents of the specified stored procedure on the screen.
  -- EXEC showProcBody('USER_NAME', 'PROCEDURE_NAME');
  CREATE OR REPLACE PROCEDURE showProcBody(p1 IN VARCHAR(40), p2 IN VARCHAR(40))
  AS
  CURSOR C1 IS
      SELECT SYSTEM_.SYS_PROC_PARSE_.PARSE
        FROM SYSTEM_.SYS_PROC_PARSE_
       WHERE SYSTEM_.SYS_PROC_PARSE_.PROC_OID = (SELECT P.PROC_OID
                FROM SYSTEM_.SYS_PROCEDURES_ P,
                     SYSTEM_.SYS_USERS_ U
               WHERE U.USER_ID = P.USER_ID
                 AND P.PROC_NAME = p2
                 AND U.USER_NAME = p1)
       ORDER BY SYSTEM_.SYS_PROC_PARSE_.SEQ_NO;
  V1 VARCHAR(4000);
  BEGIN
      OPEN C1;
      SYSTEM_.PRINTLN('---------------------------------');
      SYSTEM_.PRINT(P1);
      SYSTEM_.PRINTLN(' PROCEDURE');
      SYSTEM_.PRINTLN('---------------------------------');
      SYSTEM_.PRINTLN('');
      LOOP
        FETCH C1 INTO V1;
        EXIT WHEN C1%NOTFOUND;
        SYSTEM_.PRINTLN(V1);
      END LOOP;
      CLOSE C1;
  SYSTEM_.PRINTLN('');
  SYSTEM_.PRINTLN('---------------------------------');
  END;
  /
  ```

### How to execute user-defined stored procedures

- **Check the list of stored procedures and user-defined functions**

  ```
  iSQL> exec showProcedures;
  ```
- **Check the contents of the stored procedure**

  ```
  iSQL> exec showProcBody('*USER_NAME*', '*PROC_NAME*');
  ```

## Using the aexport utility

---

`aexport` is a utility that saves database object creation statements to a file. After executing `aexport`, stored procedure contents can be checked in the generated file.

### Execute aexport - all objects

- The creation statements of all stored procedures can be checked in `ALL_CRT_PROC.sql` among the files generated after executing `aexport`.

  ```
  $ aexport
  ```

  **Example**

  ```
  $ aexport
  -----------------------------------------------------------------
       Altibase Export Script Utility.
       Release Version 4.3.9.223
       Copyright 2000, ALTIBASE Corporation or its subsidiaries.
       All Rights Reserved.
  -----------------------------------------------------------------
  Write Server Name (default:127.0.0.1) :                    # Enter the Altibase server IP
  Write UserID : sys                                                         # Enter sys
  Write Password :                                                          # Enter the sys user's password
  ##### TBS #####
  ##### User #####
  ** input user USER1's password (default - same with USER_NAME):     # Enter the user password.
  ** input user EHEE's password (default - same with USER_NAME):
  ** input user ALTITEST's password (default - same with USER_NAME):
  ##### Synonym #####
  ##### Table #####
  ** ALTITEST.ORDERS
  ** SYS.DEMO_EX2
  ** SYS.DEPARTMENT
  ** SYS.EMPLOYEE
  ** SYS.T1
  ** USER1.T1

  ##### QUEUE #####
  ##### Sequence #####
  ##### Procedure & Function #####
  ##### View #####
  ##### Replication #####
  ##### TRIGGER #####
  -------------------------------------------------------
    ##### Follow script files are Generated. #####
    1. run_il_out.sh   : [ iloader formout, data-out script ]
    2. run_is.sh       : [ isql table-schema script ]
    3. run_il_in.sh    : [ iloader data-in script ]
    4. run_is_index.sh : [ isql table-index script ]
    5. run_is_fk.sh    : [ isql table-foreign key script ]
    6. run_is_repl.sh    : [ isql replication script ]
  -------------------------------------------------------
  ```

### Execute aexport for each user

- When you execute `aexport` with the database user name in the `-u` option and that user's password in the `-p` option, only object schemas owned by that user are extracted.
- For stored procedure contents, refer to the `ALL_CRT_PROC.sql` file.
- How to execute

  ```
  $ aexport -u user_name -p user_password -s Altibase_Server_IP

  Or

  $ aexport
  Write Server Name (default:127.0.0.1) :     # Enter the Altibase server IP
  Write UserID :            # Enter the object owner or sys user. Whatever is typed, the result is the same.
  Write Password :       # Password of the user entered above
  ```

### Execute aexport for each object

- The `object` option allows extracting only specific object schemas. **This option is available starting from ALTIBASE HDB version 5.5.1.**
- For stored procedures, specify the value in the format `-object user_name.procedure_name`.
- As a result, a file with a name in the form `user_name_procedure_name_CRT.sql` is created.
- How to execute

  ```
  $ aexport -s Altibase_Server_IP  -u user_name -p user_password -object user_name.procedure_name

  Or

  $ aexport -object user_name.procedure_name
  Write Server Name (default:127.0.0.1) :       # Enter the Altibase server IP
  Write UserID :            # Enter the object owner or sys user. Whatever is typed, the result is the same.
  Write Password :       # Password of the user entered above
  ```
