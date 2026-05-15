---
title: "Database Security Checklist"
page_id: "22642935"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Database+Security+Checklist"
updated_at: "2025-10-20T15:18:17.000+0900"
version: 1
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# Database Security Checklist
Source: https://docs.altibase.com/display/FAQE/Database+Security+Checklist
Updated: 2025-10-20T15:18:17.000+0900

- [Overview](#DatabaseSecurityChecklist-Overview) - [Account Manager](#DatabaseSecurityChecklist-AccountManager) - [List of accounts (User account management to block unauthorized access)](#DatabaseSecurityChecklist-Listofaccounts(Useraccountmanagementtoblockunauthorizedaccess)) - [Using weak password (change default account and password)](#DatabaseSecurityChecklist-Usingweakpassword(changedefaultaccountandpassword)) - [Privileges Management](#DatabaseSecurityChecklist-PrivilegesManagement) - [DBA Privilege Management (System Privilege Restriction)](#DatabaseSecurityChecklist-DBAPrivilegeManagement(SystemPrivilegeRestriction)) - [Using WITH GRANT OPTION](#DatabaseSecurityChecklist-UsingWITHGRANTOPTION) - [Checking Environment Files](#DatabaseSecurityChecklist-CheckingEnvironmentFiles) - [il, is, server file permission setting](#DatabaseSecurityChecklist-il,is,serverfilepermissionsetting) - [Altibase.properties file permission setting](#DatabaseSecurityChecklist-Altibase.propertiesfilepermissionsetting) - [Log Anchor, Logfile, Datafile access privilege setting](#DatabaseSecurityChecklist-LogAnchor,Logfile,Datafileaccessprivilegesetting) - [Setting TRC file permissions](#DatabaseSecurityChecklist-SettingTRCfilepermissions) - [Checking iSQL command shell history](#DatabaseSecurityChecklist-CheckingiSQLcommandshellhistory) - [DBMS Security Settings](#DatabaseSecurityChecklist-DBMSSecuritySettings) - [Using Public Synonym](#DatabaseSecurityChecklist-UsingPublicSynonym) - [Account lockout policy settings such as lockout time according to the number of login failure](#DatabaseSecurityChecklist-Accountlockoutpolicysettingssuchaslockouttimeaccordingtothenumberofloginfailure) - [Password complexity setting](#DatabaseSecurityChecklist-Passwordcomplexitysetting) - [Periodic change of password](#DatabaseSecurityChecklist-Periodicchangeofpassword) - [Changing the ALTIBASE HDB default service port](#DatabaseSecurityChecklist-ChangingtheALTIBASEHDBdefaultserviceport) - [Session IDLE_TIMEOUT settings](#DatabaseSecurityChecklist-SessionIDLE_TIMEOUTsettings) - [Basic auditing (user sentences, privileges, objects, etc.)](#DatabaseSecurityChecklist-Basicauditing(usersentences,privileges,objects,etc.)) - [Restriction of remote access to DB server](#DatabaseSecurityChecklist-RestrictionofremoteaccesstoDBserver) - [Setting SYSDBA login restrictions](#DatabaseSecurityChecklist-SettingSYSDBAloginrestrictions) - [Security Patch](#DatabaseSecurityChecklist-SecurityPatch) - [Applying security patch](#DatabaseSecurityChecklist-Applyingsecuritypatch)

# Overview

---

This is a guide on database security inspection and remediation methods.

# Account Manager

---

## List of accounts (User account management to block unauthorized access)

---

#### How to check

**How to check database users**

```
SELECT USER_NAME FROM SYSTEM_.SYS_USERS_;
```

#### How to manage

If any unnecessary accounts are found in the database user output, remove them after confirmation with the DBA or the application owner.

```
-- Delete user
DROP USER user_name ;

-- Delete the user and all objects created by the user
DROP USER user_name CASCADE;
```

Exception Handling:

The SYS, SYSTEM_, and PUBLIC accounts are default accounts created during the Altibase database installation and cannot be deleted.

## Using weak password (change default account and password)

---

#### How to check

The default password for the user is created when ALTIBASE HDB is installed is as follows.

| USER | PASSWORD |
| --- | --- |
| SYS | MANAGER |

Connect to the database and check whether to use the default password.

```
iSQL> CONNECT SYS/MANAGER;
Connect success.
```

#### How to manage

If access is possible with the default password, change the password of the user after checking the association with the application.

**Example of changing password**

```
iSQL> ALTER USER user1 IDENTIFIED BY password1234$;
Alter success.

Run altipasswd under the $ALTIBASE_HOME/conf directory to change the password.
```

To know how to change the SYS user password, refer to the "[How to change the sys user password](https://aid.altibase.com/display/FAQE/How+to+change+sys+user+password)' page.

# Privileges Management

---

## DBA Privilege Management (System Privilege Restriction)

---

Check the privileges of the database user and delete any unnecessary system privileges.

ROLE is supported from ALTIBASE HDB 6.5.1.

#### How to check

**Checking the system privileges the user has**

```
SELECT A.USER_NAME GRANTEE,
       C.USER_NAME GRANTOR,
       REPLACE(D.PRIV_NAME, '_', ' ') PRIV_NAME
  FROM SYSTEM_.SYS_USERS_ A,
       SYSTEM_.SYS_GRANT_SYSTEM_ B,
       SYSTEM_.SYS_USERS_ C,
       SYSTEM_.SYS_PRIVILEGES_ D
 WHERE C.USER_NAME <> 'SYSTEM_'
   AND B.GRANTEE_ID = A.USER_ID
   AND B.GRANTOR_ID = C.USER_ID
   AND B.PRIV_ID = D.PRIV_ID ;

-- ROLE
SELECT A.USER_NAME GRANTEE
     , C.USER_NAME GRANTOR
     , D.USER_NAME ROLE_NAME
  FROM SYSTEM_.SYS_USERS_ A,
       SYSTEM_.SYS_USER_ROLES_ B,
       SYSTEM_.SYS_USERS_ C,
       SYSTEM_.SYS_USERS_ D
 WHERE B.GRANTEE_ID = A.USER_ID
   AND B.GRANTOR_ID = C.USER_ID
   AND B.ROLE_ID = D.USER_ID
 ORDER BY GRANTEE, GRANTOR ;
```

**SYSTEM privilege of ALTIBASE HDB**

```
SELECT DECODE(PRIV_TYPE, 1, 'OBJECT', 'SYSTEM') PRIV_TYPE, PRIV_NAME       -- If PRIV_TYPE is SYSTEM, it means SYSTEM authority.
  FROM SYSTEM_.SYS_PRIVILEGES_
 ORDER BY 1;
```

#### How to manage

**Remove SYSTEM privilege**

```
REVODE 'System privilege' FROM user_name(or role_name);

-- Example of execution
REVOKE CREATE TABLE FROM USER1;
REVOKE CREATE TABLE FROM ROLE1;
```

## Using WITH GRANT OPTION

---

With WITH GRANT OPTION, the user who has been granted object access privileges can grant the appropriate privileges to other users, so object access privileges can be abused without DBA management.

```
SELECT DISTINCT(A.USER_NAME) GRANTEE,      -- Users with WITH GRANT OPTION
       C.USER_NAME GRANTOR,                -- User granted WITH GRANT OPTION
       B.OBJ_TYPE,                         -- 객Object type (T: table, S: sequence, P: stored procedure or stored function, V: view)
       B.OBJ_ID,                           -- Object ID (for tables, views, and sequences, maps to the TABLE_ID of SYS_TABLES_; for stored procedures and stored functions, maps to the PROC_OID of SYS_PROCEDURES_)
       D.PRIV_NAME,                        -- Previlege name
       B.WITH_GRANT_OPTION                 -- If the value is 1, it means that WITH GRANT OPTION has been granted.
  FROM SYSTEM_.SYS_USERS_ A,
       SYSTEM_.SYS_GRANT_OBJECT_ B,
       SYSTEM_.SYS_USERS_ C,
       SYSTEM_.SYS_PRIVILEGES_ D
 WHERE A.USER_NAME <> 'SYSTEM_'
   AND B.GRANTEE_ID = A.USER_ID
   AND B.GRANTOR_ID = C.USER_ID
   AND B.PRIV_ID = D.PRIV_ID
   AND B.WITH_GRANT_OPTION = 1;
```

#### How to manage

**Granting permission without WITH GRANT OPTION after removing WITH GRANT OPTION**

```
-- When the user6 user has the privilege to grant SELECT and DELETE privileges on the employees table to other users.
REVOKE SELECT, DELETE ON employees FROM user6;
GRANT SELECT, DELETE ON employees TO user6;
```

# Checking Environment Files

---

## il, is, server file permission setting

---

Altibase provides the `is`, `il`, and `server` scripts for database operation and access convenience. The permissions of these files can be modified to comply with security audit standards.

#### How to check

**To check file permissions**

```
$ ls -l $ALTIBASE_HOME/bin/il
$ ls -l $ALTIBASE_HOME/bin/is
$ ls -l $ALTIBASE_HOME/bin/server
```

#### How to manage

Set file permission to 700.

**Example of file permission setting**

```
$ chmod 700 $ALTIBASE_HOME/bin/il
$ chmod 700 $ALTIBASE_HOME/bin/is
$ chmod 700 $ALTIBASE_HOME/bin/server
```

## Altibase.properties file permission setting

---

The `altibase.properties` file is a core configuration file of Altibase. Its access permissions can be adjusted according to security audit standards.

#### How to check

**To check altibase.properties file permissions**

```
$ ls -l $ALTIBASE_HOME/conf/altibase.properties
```

#### How to manage

Set the altibase.properties file permission to 600 or 640.

**Example of file permission setting**

```
$ chmod 600 $ALTIBASE_HOME/conf/altibase.properties
```

## Log Anchor, Logfile, Datafile access privilege setting

Database failure may occur if the log anchor, logfile and datafile files, which are important files for ALTIBASE HDB database operation, are modified with malicious intent.

#### How to check

**Check the permissions of Log Anchor, Logfile and Datafile files**

```
$ ls -l $ALTIBASE_HOME/logs
$ ls -l $ALTIBASE_HOME/dbs
```

#### How to manage

logs and dbs directory permissions are set to 700 or 750.

Log Anchor, Logfile and Datafile file permissions are set to 600 or 640.

**Example of privilege setting**

```
$ chmod 700 $ALTIBASE_HOME/logs
$ chmod 700 $ALTIBASE_HOME/dbs
$ chmod 600 $ALTIBASE_HOME/logs/loganchor*
$ chmod 600 $ALTIBASE_HOME/logs/logfile*
$ chmod 600 $ALTIBASE_HOME/dbs/*
```

## Setting TRC file permissions

---

Altibase allows modification of database trace log file permissions to comply with security audit standards.

#### Applicable Versions

- ALTIBASE HDB 6.3.1 and below

#### Action Method

In versions 6.3.1 and below, files are created with default permissions of 666 (rw-rw-rw-).

File permissions can be set using the `chmod` command.

**Example of File Permission Settings**

```
예시)
$ chmod 640 altibase_boot.log
$ chmod 640 altibase_sm.log
```

#### Applicable Versions

- ALTIBASE HDB 6.5.1 and above

#### Action Method

In versions 6.5.1 and above, files are created with default permissions of 644 (rw-r--r--).

Starting from version 6.5.1, trace log file permissions can be configured using the `TRC_ACCESS_PERMISSION` property. A database restart is required after setting this property.

**Example of File Permission Settings**

```
$> vi $ALTIBASE_HOME/conf/altibase.properties
         TRC_ACCESS_PERMISSION = 640    # Additional Properties
$> server restart
```

**Precautions**

```
If any of the users connecting to the database belong to a different group and plan to connect using the IPC method,
caution is required when changing the permission settings of the altibase_ipc.log file.

Incorrect permission settings may prevent those users from connecting to the database via IPC.
```

## Checking iSQL command shell history

---

When connecting to a database using iSQL, if an account and password are entered together, the password may be leaked because the record is recorded in the shell history file.

**How to check**

**To check isql execution history in shell history file**

```
$ grep isql ~/.*history
$ ls -al ~/.*history
```

#### How to manage

When connecting to iSQL, do not enter the user and password at the shell prompt.

**To check isql execution history in shell history file**

```
$ isql -u sys -p manager -s 127.0.0.1 -port 31109          # If the user connects in this way, the user's username and password may be exposed.

# Enter the account and password individually after executing only the iSQL command as shown below.

$ isql
…
Write Server Name (default:127.0.0.1) :
Write UserID : sys
Write Password :
ISQL_CONNECTION = TCP, SERVER = 127.0.0.1, PORT_NO = 20300
iSQL>
```

Set access privilege to 600 to protect the shell history (.history or .sh_history) file.

```
$ chmod 600 ~/.*history
```

# DBMS Security Settings

---

## Using Public Synonym

---

#### How to check

**To check public Synonym**

```
SELECT OBJECT_OWNER_NAME, SYNONYM_NAME FROM SYSTEM_.SYS_SYNONYMS_ WHERE OBJECT_OWNER_NAME = 'SYSTEM_';
```

#### How to Manage

PUBLIC SYNONYMs are objects automatically created to facilitate database usage. They are widely used in procedures such as querying the DUAL table or using PRINT and PRINTLN, so deletion is not recommended. However, if deletion is unavoidable, please consult thoroughly with administrators and developers before executing the DROP command below.

**To drop PUBLIC SYNONYM**

```
DROP PUBLIC SYNONYM synonym_name;
```

#### Workaround

Even if PUBLIC SYNONYMs have been dropped, administrators and developers might still need synonyms. In this case, create PRIVATE SYNONYMs instead of PUBLIC SYNONYMs. Log in with the target account and create the synonym.

**Create PRIVATE SYNONYM**

```
connect user_id/user_passwd;
CREATE SYNONYM PRINT FOR synonym_name;

-- The following three SYNONYMs can be executed only by the sys account.
CREATE SYNONYM SET_SYSTEM_STATS FOR SYSTEM_.SET_SYSTEM_STATS;
CREATE SYNONYM GATHER_SYSTEM_STATS FOR SYSTEM_.GATHER_SYSTEM_STATS;
CREATE SYNONYM GATHER_DATABASE_STATS FOR SYSTEM_.GATHER_DATABASE_STATS;
```

## Account lockout policy settings such as lockout time according to the number of login failure

---

#### Applicable version

- From ALTIBASE HDB 4.3.9.211
- From ALTIBASE HDB 5.3.3.89
- From ALTIBASE HDB 5.5.1.5.1
- From ALTIBASE HDB 6.1.1.2.1
- From ALTIBASE HDB 6.3.1

#### How to check

**Check if the database user has the appropriate settings**

```
-- In FAILED_LOGIN_ATTEMPTS, if the number of connection failures exceeds the set value, the password of the user is locked.
-- PASSWORD_LOCK_TIME means password lockout period (days).
-- If it is 0, it means not set.
SELECT USER_NAME, FAILED_LOGIN_ATTEMPTS, PASSWORD_LOCK_TIME FROM SYSTEM_.SYS_USERS_;
```

#### How to manage

```
-- After adding FAILED_LOGIN_ATTEMPTS and PASSWORD_LOCK_TIME properties in $ALTIBASE_HOME/conf/altibase.properties, restart ALTIBASE HDB server.
-- When a database user is created after setting this property, the password locking is set based on this value.
-- The following is how to check the property settings.

SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME IN ('FAILED_LOGIN_ATTEMPTS', 'PASSWORD_LOCK_TIME');
```

**When creating a database user**

```
CREATE USER user1 IDENTIFIED BY user1 LIMIT (FAILED_LOGIN_ATTEMPTS 10, PASSWORD_LOCK_TIME 1);
```

**When performing ALTER USER**

```
ALTER USER USER1 LIMIT (FAILED_LOGIN_ATTEMPTS 10, PASSWORD_LOCK_TIME 1);

-- For unlocking of locked general account
ALTER USER USER1 ACCOUNT UNLOCK;
-- For unlocking of locked SYS account
$isql -sysdba
iSQL(sysdba)> ALTER USER SYS ACCOUNT UNLOCK;
```

## Password complexity setting

---

#### Applicable version

- From ALTIBASE HDB 4.3.9.211
- From ALTIBASE HDB 5.3.3.89
- From ALTIBASE HDB 5.5.1.5.1
- From ALTIBASE HDB 6.1.1.2.1
- ALTIBASE HDB 6.3.1

#### How to check

```
SELECT USER_NAME, PASSWORD_VERIFY_FUNCTION FROM SYSTEM_.SYS_USERS_;         -- The PASSWORD_VERIFY_FUNCTION column means password complexity setting,
                                                                            -- If it is NULL, it means it is not set.
```

#### How to manage

To set the database user password complexity, create a callback function and use the PASSWORD_VERIFY_FUNCTION option in the LIMIT clause when executing CREATE USER or ALTER USER.

```
CREATE USER username IDENTIFIED BY password LIMIT (PASSWORD_VERIFY_FUNCTION user callback function); -- PASSWORD_VERIFY_FUNCTION option password complexity setting in LIMIT clause

-- Example
CREATE USER user1 IDENTIFIED BY "user1" LIMIT (PASSWORD_VERIFY_FUNCTION pwd_verify_function);
```

```
ALTER USER username LIMIT (PASSWORD_VERIFY_FUNCTION user callback function);

-- Example
ALTER USER user1 LIMIT (PASSWORD_VERIFY_FUNCTION pwd_verify_function);
```

**To create callback function**

```
CREATE OR REPLACE FUNCTION pwd_verify_function
( username varchar(20),
  password varchar(20))
RETURN varchar(100)
AS
result        varchar(100);
pwdLength     integer;
isDigit       boolean;
isChar        boolean;
isPunctuation    boolean;
digitArray    varchar(20);
punctuationArray varchar(25);
charArray     varchar(52);

BEGIN
    digitArray    := '0123456789';
    charArray     := 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    punctuationArray :='!"#$%&()``*+,-/:;<=>?_';

    -- Check if the password is same as the username
    IF LOWER(password) = LOWER(username) THEN
        result := 'Password same as or similar to user';
        RETURN result;
    END IF;

    -- Check for the minimum length of the password
    IF LENGTH(password) < 4 THEN
        result := 'Password length less than 4';
        RETURN result;
    END IF;

    -- Check if the password is too simple.
    IF LOWER(password) IN ('welcome', 'database', 'account', 'user', 'password', 'altibase', 'computer', 'abcd') THEN
        result := 'Password too simple';
        RETURN result;
    END IF;

    -- Check if the password contains at least one letter, one digit and one
    -- punctuation mark.
    -- 1. Check for the digit
    isDigit := FALSE;
    pwdLength := length(password);
    FOR i IN 1...10 LOOP
    FOR j IN 1...pwdLength LOOP
    IF substr(password,j,1) = substr(digitArray,i,1) THEN
        isDigit := TRUE;
        GOTO findchar;
    END IF;
    END LOOP;
    END LOOP;
    IF isDigit = FALSE THEN
        result := 'Password should contain at least one digit, one character and one punctuation';
        RETURN result;
    END IF;

    -- 2. Check for the character
    <<findchar>>
    isChar := FALSE;
    FOR i IN 1...length(charArray) LOOP
    FOR j IN 1...pwdLength LOOP
    IF substr(password,j,1) = substr(charArray,i,1) THEN
        isChar := TRUE;
        --GOTO findpunct;
    END IF;
    END LOOP;
    END LOOP;
    IF isChar = FALSE THEN
        result := 'Password should contain at least one digit, one character and one punctuation';
        RETURN result;
    END IF;

    -- 3. Check for the punctuation
    <<findpunct>>
    isPunctuation := FALSE;
    FOR i IN 1...length(punctuationArray) LOOP
    FOR j IN 1...pwdLength LOOP
    IF substr(password,j,1) = substr(punctuationArray,i,1) THEN
        isPunctuation := TRUE;
        GOTO endsearch;
    END IF;
    END LOOP;
    END LOOP;
    IF isPunctuation = FALSE THEN
        result := 'Password should contain at least one digit, one character and one punctuation';
        RETURN result;
    END IF;

    <<endsearch>>

    result := 'TRUE';
    RETURN result;
END;
/
```

## Periodic change of password

---

#### Applicable version

- ALTIBASE HDB 4.3.9.211
- ALTIBASE HDB 5.3.3.89
- ALTIBASE HDB 5.5.1.5.1
- ALTIBASE HDB 6.1.1.2.1
- ALTIBASE HDB 6.3.1

#### How to check

**Check if PASSWORD_LIFE_TIME for each user is set**

```
-- The value of PASSWORD_LIFE_TIME and PASSWORD_GRACE_TIME is in days, and if it is 0, it means that it is not set.
select user_name, PASSWORD_LIFE_TIME, PASSWORD_GRACE_TIME from system_.sys_users_;
```

#### Check the PASSWORD_LIFE_TIME property with the command below. If the value is 0, it means that the password expiration date is not set.

After adding the PASSWORD_LIFE_TIME and PASSWORD_GRACE_TIME property in $ALTIBASE_HOME/conf/altibase.properties, restart the ALTIBASE HDB server.

When a database user is created after setting this property, the password expiration date and grace period is set based on this value.

**Setting the PASSWORD_LIFE_TIME property**

```
select name, value1 from v$property where name in ('PASSWORD_LIFE_TIME', 'PASSWORD_GRACE_TIME');
```

```
CREATE USER user1 IDENTIFIED BY user1 LIMIT (PASSWORD_LIFE_TIME 5, PASSWORD_GRACE_TIME 3);     -- Setting the password expiration date and grace period using the LIMIT clause
```

**When performing ALTER USER**

```
ALTER USER USER1 LIMIT (PASSWORD_LIFE_TIME 5, PASSWORD_GRACE_TIME 3);
```

## Changing the ALTIBASE HDB default service port

---

The default service port of the ALTIBASE HDB server is 20300.

#### How to check

**To check Service Port**

```
select name, value1 from v$property where name = 'PORT_NO';
```

#### How to manage

After changing the value of PORT_NO in $ALTIBASE_HOME/conf/altibase.properties, restart the Altibase server process.

## Session IDLE_TIMEOUT settings

---

IDLE_TIMEOUT can be changed for each session, so it can be changed in session even if it is affected by ALTIBASE HDB server properties when connected.

#### How to check

**Check ALTIBASE HDB server settings**

```
select name, value1 from v$property where name = 'IDLE_TIMEOUT';
```

**Settings applied per session**

```
select DB_USERNAME, IDLE_TIME_LIMIT, COMM_NAME, CLIENT_APP_INFO, CLIENT_PID from v$session;
```

#### How to manage

**To change properties**

```
ALTER SESSION SET IDLE_TIMEOUT = 60;   -- When changing session units. The unit is seconds.
ALTER SYSTEM SET IDLE_TIMEOUT = 60;    -- When applied to all sessions. Applied from the newly connected session.
```

- To reflect the changed value even when the Altibase server process is restarted, the value of the IDLE_TIMEOUT property must be changed in $ALTIBASE_HOME/conf/altibase.properties.

## Basic auditing (user sentences, privileges, objects, etc.)

---

Auditing function is provided starting from ALTIBASE HDB version 6.3.1.

#### How to check

**How to check-How to check whether auditing is set**

```
SELECT * FROM SYSTEM_.SYS_AUDIT_OPTS_;

--Example
iSQL> SELECT * FROM SYSTEM_.SYS_AUDIT_OPTS_;
USER_NAME             OBJECT_NAME           OBJECT_TYPE           SELECT_OP  INSERT_OP  UPDATE_OP  DELETE_OP  MOVE_OP  MERGE_OP  ENQUEUE_OP  DEQUEUE_OP  LOCK_TABLE_OP  EXECUTE_OP  COMMIT_OP  ROLLBACK_OP  SAVEPOINT_OP  CONNECT_OP  DISCONNECT_OP  ALTER_SESSION_OP  ALTER_SYSTEM_OP  DDL_OP
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
ALTITEST              AUD1                  TABLE                 -/-  A/A  -/-  -/-  -/-  -/-  -/-  -/-  -/-  -/-  -/-  -/-  -/-  -/-  -/-  -/-  -/-  -/-
1 row selected.
```

**How to check-whether to enable auditing**

```
SELECT * FROM SYSTEM_.SYS_AUDIT_

--Example
iSQL> select * from system_.sys_audit_;                      -- If the value of IS_STARTED is 1, it means that the auditing function is activated.
IS_STARTED  START_TIME  STOP_TIME    RELOAD_TIME
--------------------------------------------------------
1           23-JUN-2014               23-JUN-2014
1 row selected.
```

- For a description of each field, please refer to Data Dictionary section of the [General Reference](https://github.com/ALTIBASE/Documents/tree/master/Manuals/Altibase_7.1/eng) manual.

#### How to manage

Refer to Administrator's Manual and SQL Reference AUDIT section.

Manual download page: [http://support.altibase.com/en/manual](http://support.altibase.com/en/manual)

## Restriction of remote access to DB server

---

This feature is available starting from ALTIBASE HDB 5.

#### How to check and manage

Check the ACCESS_LIST property in $ALTIBASE_HOME/conf/altibase.properties.

If it is not set, you need to restart after changing the setting in altibase.properties file.

Refer to ACCESS_LIST property in General Reference Manual.

## Setting SYSDBA login restrictions

ALTIBASE HDB has no login restrictions for SYSDBA and can only control remote access. This feature is available starting from ALTIBASE HDB version 5.

#### How to check

```
SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME ='REMOTE_SYSDBA_ENABLE'; --value1 = 1: remote access of sysdba is possible, value1 = 0: remote access of sysdba is not possible
```

#### How to manage

**How to manage**

```
ALTER SYSTEM SET REMOTE_SYSDBA_ENABLE = 0;
```

- To reflect the changed value even when the Altibase server process is restarted, the value of the REMOTE_SYSDBA_ENABLE property must be changed in $ALTIBASE_HOME/conf/altibase.properties.

# Security Patch

---

## Applying security patch

---

Security patch of Altibase can be found on the [Customer Support Service Portal](http://support.altibase.com/en/product).

- When major bugs including security bugs are fixed, new patch is uploaded on the Customer Support Service Portal.
