---
title: "Connection disconnection, error codes, and error messages in each case (APRE*C/C++, SQLCLI)"
page_id: "16876167"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876167"
updated_at: "2021-04-05T09:49:34.000+0900"
version: 3
ancestors: ["Home", "07. Development and API"]
labels: []
---

# Connection disconnection, error codes, and error messages in each case (APRE*C/C++, SQLCLI)
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876167
Updated: 2021-04-05T09:49:34.000+0900

**- [Overview](#Connectiondisconnection,errorcodes,anderrormessagesineachcase(APRE*C/C++,SQLCLI)-Overview) - [Version](#Connectiondisconnection,errorcodes,anderrormessagesineachcase(APRE*C/C++,SQLCLI)-Version) - [When the connection is disconnected from the application program](#Connectiondisconnection,errorcodes,anderrormessagesineachcase(APRE*C/C++,SQLCLI)-Whentheconnectionisdisconnectedfromtheapplicationprogram) - [How to check error codes and error messages for each application program](#Connectiondisconnection,errorcodes,anderrormessagesineachcase(APRE*C/C++,SQLCLI)-Howtocheckerrorcodesanderrormessagesforeachapplicationprogram) - [Connection error state and error message](#Connectiondisconnection,errorcodes,anderrormessagesineachcase(APRE*C/C++,SQLCLI)-Connectionerrorstateanderrormessage) - [Conclusion](#Connectiondisconnection,errorcodes,anderrormessagesineachcase(APRE*C/C++,SQLCLI)-Conclusion)**

# Overview

---

This document describes the cases where the connection is disconnected in the application program and the error codes and messages in each situation.

# Version

---

- This document is written based on ALTIBASE HDB version 6.3.1.
- For additional information or updates, please leave a request at [http://support.altibase.com/en/](http://support.altibase.com/en/) or leave a comment on this page.

# When the connection is disconnected from the application program

---

In the following situations, the connection is not established.

1. It is not connected
2. Communication socket error or disconnection from the server-side
3. If a previously disconnected connection was not detected (if the connection was previously disconnected)
4. If it is disconnected by timeout
  There are Query Timeout, Fetch Timeout, UTrans Timeout, and Idle Timeout. In the case of Query Timeout, the connection is not disconnected, but in all other cases, the connection is disconnected.
5. When the DB Server is shutdown
6. If the connection is not possible because the DB server is shutdown (Connect failure)

# How to check error codes and error messages for each application program

---

If the application program is written in ALTIBASE Embedded SQL (APRE*C/C++), the values that can be checked are as follows.

1. sqlca.sqlcode (query execution return value - SQL_SUCCESS, SQL_ERROR, etc)
2. sqlca.sqlerrm.sqlerrmc (error message)
3. SQLCODE (error code)
4. SQLSTATE (state code)

If the application is written in SQLCLI, the following values can be checked.

It can be checked by calling SQLError(env,dbc,stmt,state,err,msg,msgMax,msgLength).

1. state (state code)
2. err (error code)
3. msg (error message)

# Connection error state and error message

---

1. In case of not connecter or previously disconnected

  ```
  [APRE*C/C++]
  	====================================================
  	sqlca STRUCTURE
  	.sqlcode [-2] (SQL_ERROR)
  	.sqlerrm.sqlerrmc The connection does not exist. (Name:default connection)
  	SQLCODE [-2]
  	SQLSTATE ["08003"]
  	====================================================

  [SQLCLI/ODBC]
  1. In case of haven't connected
  	====================================================
  	return value [-2]
  	SQLError(env,dbc,stmt,state,err,msg,msgMax,msgLength)
  	error state (state) [""]
  	error number (err) [0] in Hex(0)
  	error message (msg) [ ?]
  	====================================================
  2. In case of disconnected before
  	====================================================
  	return value [-1] (SQL_ERROR)
  	SQLError(env,dbc,stmt,state,err,msg,msgMax,msgLength)
  	error state (state) ["08003"]
  	error number (err) [331830] in Hex(51036)
  	error message (msg) [Connection does not exist (err8)]
  	====================================================
  ```
2. In case of the connection is disconnected (the server disconnection or a network error)

  ```
  [APRE*C/C++]
  ====================================================
  sqlca STRUCTURE
  .sqlcode [-1]
  .sqlerrm.sqlerrmc [Communication link failure('errno')]
  SQLCODE [-331843] in Hex(51043)
  SQLSTATE ["08S01"]
  ====================================================

  [SQLCLI/ODBC]
  ====================================================
  return value [-1]
  SQLError(env,dbc,stmt,state,err,msg,msgMax,msgLength)
  error state (state) ["08S01"]
  error number (err) [331843] in Hex(51043)
  error message (msg) [Communication link failure('errno')]
  ====================================================
  ```
3. In case of the query was executed again without detecting that the connection was previously disconnected.

  ```
  [APRE*C/C++]
  ====================================================
  sqlca STRUCTURE
  .sqlcode [-1]
  .sqlerrm.sqlerrmc [Connection does not exist (err11)]
  SQLCODE [-1]
  SQLSTATE ["08003"]
  ====================================================

  [SQLCLI/ODBC]
  ====================================================
  return value [-1]
  SQLError(env,dbc,stmt,state,err,msg,msgMax,msgLength)
  error state (state) ["08003"]
  error number (err) [331830] in Hex(51036)
  error message (msg) [Connection does not exist (err8)]
  ====================================================
  ```
4. In case of disconnection by Timeout Fetch Timeout, UTrans Timeout, Idle Timeout all return the same error. (Timeout is recorded in altibase_boot.log.)

  ```
  [APRE*C/C++]
  ====================================================
  sqlca STRUCTURE
  .sqlcode [-1]
  .sqlerrm.sqlerrmc [Communication link failure(131)]
  SQLCODE [-331843] in Hex(51043)
  SQLSTATE ["08S01"]
  ====================================================

  [SQLCLI/ODBC]
  ====================================================
  return value [-1]
  SQLError(env,dbc,stmt,state,err,msg,msgMax,msgLength)
  error state (state) ["08S01"]
  error number (err) [331843] in Hex(51043)
  error message (msg) [Communication link failure(131)]
  ====================================================
  ```
5. In case of the DB server is shutdown

  ```
  [APRE*C/C++]
  ====================================================
  sqlca STRUCTURE
  .sqlcode [-1]
  .sqlerrm.sqlerrmc [Communication link failure(131)]
  SQLCODE [-331843] in Hex(51043)
  SQLSTATE ["08S01"]
  ====================================================

  [SQLCLI/ODBC]
  ====================================================
  return value [-1]
  SQLError(env,dbc,stmt,state,err,msg,msgMax,msgLength)
  error state (state) ["08S01"]
  error number (err) [331843] in Hex(51043)
  error message (msg) [Communication link failure(131)]
  ====================================================
  ```
6. Connection failure

  ```
  [APRE*C/C++]
  ====================================================
  sqlca STRUCTURE
  .sqlcode [-1]
  .sqlerrm.sqlerrmc [Client unable to establish connection]
  SQLCODE [-327730] [50032]
  SQLSTATE [08001]
  ====================================================

  [SQLCLI/ODBC]
  ====================================================
  return value [-1]
  SQLError(env,dbc,stmt,state,err,msg,msgMax,msgLength)
  error state (state) [08001]
  error number (err) [327730] in Hex(50032)
  error message (msg) [Client unable to establish connection]
  ====================================================
  ```

# Conclusion

---

As a result of checking the error code for each situation, there are 3 cases as follows.

- - SQLSTATE(state) ["08001"] SQLCODE [1(0x01)] errno [32770(0x050032)]
  Connection failure
- - SQLSTATE(state) ["08003"] SQLCODE(errno) [331830(0x051036)]
  In case of not connected (after disconnection)
  In case the connection is already disconnected
- - SQLSTATE(state) ["08S01"] SQLCODE(errno) [331843(0x051043)]
  Socket disconnection
  In case of interruption due to timeout
  In case of the server being shutdown
