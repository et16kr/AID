---
title: "[Notify : Fetch Timeout] Session Closed by Server."
page_id: "16876301"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876301"
updated_at: "2021-04-05T10:47:07.000+0900"
version: 4
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# [Notify : Fetch Timeout] Session Closed by Server.
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876301
Updated: 2021-04-05T10:47:07.000+0900

- [Overview](#id-[Notify:FetchTimeout]SessionClosedbyServer.-Overview) - [Version](#id-[Notify:FetchTimeout]SessionClosedbyServer.-Version) - [Symptom](#id-[Notify:FetchTimeout]SessionClosedbyServer.-Symptom) - [Altibase Server](#id-[Notify:FetchTimeout]SessionClosedbyServer.-AltibaseServer) - [Altibase Client](#id-[Notify:FetchTimeout]SessionClosedbyServer.-AltibaseClient) - [Orange for ALTIBASE](#id-[Notify:FetchTimeout]SessionClosedbyServer.-OrangeforALTIBASE) - [iSQL](#id-[Notify:FetchTimeout]SessionClosedbyServer.-iSQL) - [APRE(SESC), SQLCLI, ODBC, CAPI](#id-[Notify:FetchTimeout]SessionClosedbyServer.-APRE(SESC),SQLCLI,ODBC,CAPI) - [JDBC](#id-[Notify:FetchTimeout]SessionClosedbyServer.-JDBC) - [Cause](#id-[Notify:FetchTimeout]SessionClosedbyServer.-Cause) - [Solution](#id-[Notify:FetchTimeout]SessionClosedbyServer.-Solution) - [Checking the application logic](#id-[Notify:FetchTimeout]SessionClosedbyServer.-Checkingtheapplicationlogic) - [Changing FETCH_TIMEOUT setting value](#id-[Notify:FetchTimeout]SessionClosedbyServer.-ChangingFETCH_TIMEOUTsettingvalue) - [Changing session property](#id-[Notify:FetchTimeout]SessionClosedbyServer.-Changingsessionproperty) - [Changing system property](#id-[Notify:FetchTimeout]SessionClosedbyServer.-Changingsystemproperty) - [How to check the FETCH_TIMEOUT property value](#id-[Notify:FetchTimeout]SessionClosedbyServer.-HowtochecktheFETCH_TIMEOUTpropertyvalue)

# Overview

---

This document describes the Fetch Timeout message.

# Version

---

All the versions of ALTIBASE HDB

# Symptom

---

## Altibase Server

---

In the Altibase server log, the following logs can be checked.

- Check the Altibase server log ($ALTIBASE_HOME/trc/altibase_boot.log).
- The output format is different for each version, so refer to the results below.
- Comprehensively check the log output time, CLIENT_INFO, and Caused by Query to see if it is related to the client-side phenomenon.
- **Altibase HDB 5 or later**

  **Altibase HDB version 5 or later**

  ```
  [2015/04/10 15:48:28] [Thread-1] [Level-1]
  [Notify : Fetch Timeout] Session Closed by Server : Session ID = 32
      CLIENT_INFO           => TCP 127.0.0.1:50696(PID : 18647665)
      Time Limit            => 1
      Running Time          => 2
      Caused by Query       => SELECT * FROM EMP
      Transaction ID        => 544259
  ```
- **ALTIBASE HDB 4.3.9**

  Client IP information cannot be checked in the ALTIBASE HDB 4.3.9 server log. It should be judged with log output time and Caused by Query.

  **Altibase HDB 4.3.9**

  ```
  [2015/04/10 15:44:56] [Thread-139708873230080] [Level-1]
  [Notify : Fetch Timeout] Session Closed by Server : Session ID = 45
  [2015/04/10 15:44:56] [Thread-139708873230080] [Level-1]
           Time   Limit => 2
           Running Time => 2
  [2015/04/10 15:44:56] [Thread-139708873230080] [Level-1]
           Caused by Query => SELECT * FROM EMP
  [2015/04/10 15:44:56] [Thread-139708873230080] [Level-1]
           Transaction ID => 26435
  ```

## Altibase Client

---

The following situations occur on the Altibase client side.

- The error message can be checked when the client sends a request to the Altibase server. Therefore, it may occur after the time left on the Altibase server-side (altibase_boot.log).
- The connection to the Altibase server is disconnected during SELECT (when Fetch is requested).
- When an application processes a fetch result and requests a FETCH back to the database, a disconnected error occurs.
- The session has been closed by the server in the client log. (For ALTIBASE HDB 5.5.1 or later versions)
- The Server closed the connection in the client log. (For ALTIBASE HDB 5.5.1 or later versions.)

Refer to the following for the types of error messages for each client.

### Orange for ALTIBASE

- The following error message occurs when scrolling down the result window below after executing SELECT.

  **Orange for ALTIBASE**

  ```
  Error : # 331843, Communication link failure. Server closed the connection.
  ```

### iSQL

- The following error message occurs while executing SELECT in iSQL.

  **iSQL**

  ```
  iSQL> select * from emp;
  ...중략...
  11          1003        2750000
  12          4002        1890000
  [ERR-91015 : Communication failure.]
  ```

### APRE(SESC), SQLCLI, ODBC, CAPI

- "Communication link failure during fetch in APRE, SQL CLI, ODBC, and CAPI. Server closed the connection." occurs.
- This applies to ALTIBASE HDB version 5 or later

  **APRE**

  ```
  FETCH ERROR         : [-331843] Communication link failure. Server closed the connection.
  ```

  **SQLCLI, ODBC**

  ```
  Error : SELECT * FROM EMP
  Diagnostic Record 1
       SQLSTATE     : 08S01
       Message text : Communication link failure. Server closed the connection.
       Message len  : 57
       Native error : 0x51043
  ```
- SESC (ALTIBASE HDB 4 ~ 5.1.5)

  **SESC**

  ```
  $ ./cursor2
  ...Omitted...
  16      1001     2300000.00
  17      2001     1400000.00
  FETCH ERROR              : [-331843] Communication link failure (0
  CURSOR CLOSE ERROR Error : [-594098] Connection does not exist
  DISCONN ERROR            : [0]
  ```

### JDBC

- In **ALTIBASE HDB 4.3.9,** the following error occurs during FETCH execution and the application may be stopped.

  $ java SimpleSQL ...Omitted... ENO, DNO, SALARY : 20 40020 FETCH ERROR CODE : 0 FETCH ERROR MESSAGE : Altibase JDBC $Revision: 24725 $ ERROR:read time out java.sql.SQLException: Altibase JDBC $Revision: 24725 $ ERROR:read time out at Altibase.jdbc.driver.cmProtocol.fireIOError(cmProtocol.java:87) at Altibase.jdbc.driver.cmProtocolTCP.execFetch(cmProtocolTCP.java:817) at Altibase.jdbc.driver.AltibaseConnection.execFetch(AltibaseConnection.java:298) at Altibase.jdbc.driver.AltibaseResultSet.next(AltibaseResultSet.java:1126) at SimpleSQL.main(SimpleSQL.java:105)
- From **ALTIBASE HDB 5 to 6.1.1**, an error occurs during FETCH, and a disconnection error occurs whenever an application sends a request to the Altibase server afterward.

  **JDBC-ALTIBASE HDB 5, 6.1.1 Occurrence type 1**

  $ java SimpleSQL ...Omitted... ENO, DNO, SALARY : 19 40021800000 ENO, DNO, SALARY : 20 40020 FETCH ERROR CODE : 0 FETCH ERROR MESSAGE : The connection is reset by the peer. (errno:232) java.sql.SQLException: The connection is reset by the peer. (errno:232) at Altibase.jdbc.driver.ex.exception(ex.java:52) at Altibase.jdbc.driver.ex.exception(ex.java:37) at Altibase.jdbc.driver.cmnTCP.recv(cmnTCP.java:130) at Altibase.jdbc.driver.cmp.flush(cmp.java:247) at Altibase.jdbc.driver.cmp.writeFetchRequest(cmp.java:1066) at Altibase.jdbc.driver.ABConnection.writeFetchRequest(ABConnection.java:335) at Altibase.jdbc.driver.ABResultSet.fetchPosition(ABResultSet.java:1184) at Altibase.jdbc.driver.ABResultSet.next(ABResultSet.java:719) at SimpleSQL.main(SimpleSQL.java:105) sPreStmt.close ERROR CODE : 0 sPreStmt.close ERROR MESSAGE : Broken pipe. (errno:32) java.sql.SQLException: The pipe is damaged. (errno:32) at Altibase.jdbc.driver.ex.exception(ex.java:52) at Altibase.jdbc.driver.ex.exception(ex.java:37) at Altibase.jdbc.driver.cmnTCP.send(cmnTCP.java:153) at Altibase.jdbc.driver.cmp.flush(cmp.java:246) at Altibase.jdbc.driver.cmp.free(cmp.java:1085) at Altibase.jdbc.driver.ABConnection.free(ABConnection.java:346) at Altibase.jdbc.driver.ABStatement.close(ABStatement.java:174) at SimpleSQL.main(SimpleSQL.java:133) sCon.close ERROR CODE : 0 sCon.close ERROR MESSAGE : Broken pipe. (errno:32) java.sql.SQLException: The pipe is damaged. (errno:32) at Altibase.jdbc.driver.ex.exception(ex.java:52) at Altibase.jdbc.driver.ex.exception(ex.java:37) at Altibase.jdbc.driver.cmnTCP.send(cmnTCP.java:153) at Altibase.jdbc.driver.cmp.flush(cmp.java:246) at Altibase.jdbc.driver.cmp.disconnect(cmp.java:775) at Altibase.jdbc.driver.ABConnection.close(ABConnection.java:226) at SimpleSQL.main(SimpleSQL.java:142)

  **JDBC-ALTIBASE HDB 5, 6.1.1 Occurrence type 2**

  $ java SimpleSQL ...Omitted... ENO, DNO, SALARY : 19 40021800000 ENO, DNO, SALARY : 20 40020 FETCH ERROR CODE : 331817 FETCH ERROR MESSAGE : Communication link failure java.sql.SQLException: Communication link failure at Altibase.jdbc.driver.ex.exception(ex.java:57) at Altibase.jdbc.driver.ex.exception(ex.java:32) at Altibase.jdbc.driver.ex.test(ex.java:83) at Altibase.jdbc.driver.cmnTCP.recv(cmnTCP.java:110) at Altibase.jdbc.driver.cmp.flush(cmp.java:253) at Altibase.jdbc.driver.cmp.writeFetchRequest(cmp.java:1167) at Altibase.jdbc.driver.ABConnection.writeFetchRequest(ABConnection.java:628) at Altibase.jdbc.driver.ABResultSet.fetchPosition(ABResultSet.java:1184) at Altibase.jdbc.driver.ABResultSet.next(ABResultSet.java:719) at SimpleSQL.main(SimpleSQL.java:105) sPreStmt.close ERROR CODE : 331817 sPreStmt.close ERROR MESSAGE : Broken pipe java.sql.SQLException: Broken pipe at Altibase.jdbc.driver.ex.exception(ex.java:76) at Altibase.jdbc.driver.cmnTCP.send(cmnTCP.java:156) at Altibase.jdbc.driver.cmp.flush(cmp.java:252) at Altibase.jdbc.driver.cmp.free(cmp.java:1186) at Altibase.jdbc.driver.ABConnection.free(ABConnection.java:655) at Altibase.jdbc.driver.ABStatement.close(ABStatement.java:179) at SimpleSQL.main(SimpleSQL.java:134) Caused by: [java.io](http://java.io/).IOException: Broken pipe at [sun.nio.ch](http://sun.nio.ch/).FileDispatcher.write0(Native Method) at [sun.nio.ch](http://sun.nio.ch/).SocketDispatcher.write(SocketDispatcher.java:29) at [sun.nio.ch](http://sun.nio.ch/).IOUtil.writeFromNativeBuffer(IOUtil.java:69) at [sun.nio.ch](http://sun.nio.ch/).IOUtil.write(IOUtil.java:26) at [sun.nio.ch](http://sun.nio.ch/).SocketChannelImpl.write(SocketChannelImpl.java:336) at Altibase.jdbc.driver.cmnTCP.send(cmnTCP.java:147) ... 5 more sCon.close ERROR CODE : 331817 sCon.close ERROR MESSAGE : Broken pipe java.sql.SQLException: Broken pipe at Altibase.jdbc.driver.ex.exception(ex.java:76) at Altibase.jdbc.driver.cmnTCP.send(cmnTCP.java:156) at Altibase.jdbc.driver.cmp.flush(cmp.java:252) at Altibase.jdbc.driver.cmp.disconnect(cmp.java:877) at Altibase.jdbc.driver.ABConnection.close(ABConnection.java:366) at SimpleSQL.main(SimpleSQL.java:143) Caused by: [java.io](http://java.io/).IOException: Broken pipe at [sun.nio.ch](http://sun.nio.ch/).FileDispatcher.write0(Native Method) at [sun.nio.ch](http://sun.nio.ch/).SocketDispatcher.write(SocketDispatcher.java:29) at [sun.nio.ch](http://sun.nio.ch/).IOUtil.writeFromNativeBuffer(IOUtil.java:69) at [sun.nio.ch](http://sun.nio.ch/).IOUtil.write(IOUtil.java:26) at [sun.nio.ch](http://sun.nio.ch/).SocketChannelImpl.write(SocketChannelImpl.java:336) at Altibase.jdbc.driver.cmnTCP.send(cmnTCP.java:147) ... 4 more
- From **ALTIBASE HDB 6.3.1**, the session has been closed by the server error message that occurs during FETCH execution, and a connection disconnection error occurs whenever a request is sent to the Altibase server.

  **JDBC - ALTIBASE HDB 6.3.1**

  FETCH ERROR CODE : 4163 FETCH ERROR MESSAGE : The session has been closed by the server java.sql.SQLException: The session has been closed by the server at Altibase.jdbc.driver.ex.Error.processServerError(Error.java:320) at Altibase.jdbc.driver.AltibaseForwardOnlyResultSet.next(AltibaseForwardOnlyResultSet.java:151) at SimpleSQL.main(SimpleSQL.java:105) sPreStmt.close ERROR CODE : 334337 sPreStmt.close ERROR MESSAGE : Communication link failure: There was no response from the server, and the channel has reached end-of-stream. java.sql.SQLException: Communication link failure: There was no response from the server, and the channel has reached end-of-stream. at Altibase.jdbc.driver.ex.Error.throwSQLExceptionInternal(Error.java:162) at Altibase.jdbc.driver.ex.Error.throwSQLException(Error.java:102) at [Altibase.jdbc.driver.cm](http://altibase.jdbc.driver.cm/).CmChannel.readFromSocket(CmChannel.java:1042) at [Altibase.jdbc.driver.cm](http://altibase.jdbc.driver.cm/).CmChannel.receivePacket(CmChannel.java:1001) at [Altibase.jdbc.driver.cm](http://altibase.jdbc.driver.cm/).CmChannel.sendAndReceive(CmChannel.java:821) at [Altibase.jdbc.driver.cm](http://altibase.jdbc.driver.cm/).CmProtocol.freeStatement(CmProtocol.java:424) at Altibase.jdbc.driver.AltibaseStatement.close(AltibaseStatement.java:436) at SimpleSQL.main(SimpleSQL.java:133) sCon.close ERROR CODE : 334337 sCon.close ERROR MESSAGE : Communication link failure: Broken pipe java.sql.SQLException: Communication link failure: Broken pipe at Altibase.jdbc.driver.ex.Error.throwCommunicationErrorException(Error.java:237) at [Altibase.jdbc.driver.cm](http://altibase.jdbc.driver.cm/).CmChannel.sendPacket(CmChannel.java:921) at [Altibase.jdbc.driver.cm](http://altibase.jdbc.driver.cm/).CmChannel.sendAndReceive(CmChannel.java:819) at [Altibase.jdbc.driver.cm](http://altibase.jdbc.driver.cm/).CmProtocol.disconnect(CmProtocol.java:95) at Altibase.jdbc.driver.AltibaseConnection.disconnect(AltibaseConnection.java:616) at Altibase.jdbc.driver.AltibaseConnection.close(AltibaseConnection.java:601) at SimpleSQL.main(SimpleSQL.java:142) Caused by: [java.net](http://java.net/).SocketException: Broken pipe at [java.net](http://java.net/).SocketOutputStream.socketWrite0(Native Method) at [java.net](http://java.net/).SocketOutputStream.socketWrite(SocketOutputStream.java:109) at [java.net](http://java.net/).SocketOutputStream.write(SocketOutputStream.java:153) at java.nio.channels.Channels$WritableByteChannelImpl.write(Channels.java:292) at [Altibase.jdbc.driver.cm](http://altibase.jdbc.driver.cm/).CmChannel.sendPacket(CmChannel.java:916) ... 5 more

# Cause

---

This is a notification message left by the SessionManager as it cleans up the sessions stuck on FETCH_TMEOUT.

FETCH_TMEOUT is an Altibase server property. this is a property provided to prevent an abnormal increase of DBMS resources as the time to execute the SELECT statement increases.

When the client requests fetch, the DBMS divides the fetch result by a certain amount (in the communication buffer) and sends it to the client. When the client reads all the result sets in the communication buffer, it requests the next result set to the DB server.

If the time interval for requesting the next result set exceeds the value set for FETCH_TIMEOUT, the session is cleaned up and the transaction in progress is rolled back.

If the old image created by the change transaction is viewed by the inquiry transaction, the old image is not cleaned up even when the change transaction ends.

For this reason, if the SELECT statement is executed for a long time, the following symptoms may occur.

- For memory tables, memory usage increases
- For disk tables, undo tablespace usage increases

# Solution

---

### Checking the application logic

- FETCH_TIMEOUT can be a problem if the application mainly processes the fetch result to perform other tasks, and this processing takes longer.
- So, take a look at how the application handles fetch results, determine if there is room for improvement, and then take action. (Take measures after checking if there are any of the following parts)

  **JDBC example**

  ```
  sRS = sStmt.executeQuery( "SELECT EMP_FIRST, EMP_LAST," +
                            " EMP_NO FROM TEST_EMP_TBL " );
  /* Fetch all data */
  while( sRS.next() )
  {
      /* Fetch results are processed for a long time in the application*/
  }
  ```

  **APRE example**

  ```
  /* declare cursor */
  EXEC SQL DECLARE DEPT_CUR CURSOR FOR
           SELECT *
           FROM DEPARTMENTS;

  /* open cursor */
  EXEC SQL OPEN DEPT_CUR;

  /* fetch cursor in loop */
  while(1)
  {
      EXEC SQL FETCH DEPT_CUR INTO :s_department :s_dept_ind;
       /* Fetch results are processed for a long time in the application */
  }
  ```

### Changing FETCH_TIMEOUT setting value

- The default value for the FETCH_TIMEOUT property is 60 seconds. If it is determined that this value is small in the operating environment, it can be changed and used.
- This property can be changed with a system property or a session property.

#### Changing session property

- Session property is applied to the session that executed ALTER SESSIOn on a per session basis and applied to queries executed after ALTER SESSION was executed.

  **iSQL-How to change session properties**

  ```
  iSQL> ALTER SESSION SET FETCH_TIMEOUT = 600;   -- Value is in seconds
  ```
- It can also be changed in the application.

  **JDBC example**

  ```
  sStmt.execute( "ALTER SESSION SET FETCH_TIMEOUT = 600" );
  ```

  **APRE/SESC example**

  ```
   EXEC SQL ALTER SESSION SET ALTER SESSION SET FETCH_TIMEOUT = 600 ;
  ```

#### Changing system property

- System property affects a connected session after executing ALTER SYSTEM.

  **iSQL-How to change system properties**

  ```
  iSQL> ALTER SYSTEM SET FETCH_TIMEOUT = 600;   -- Value is in seconds.
  ```
- To keep the changed system property values even after restarting the Altibase server process, you need to modify the altibase.properties file.

  **iSQL-How to change system properties**

  ```
  $ vi $ALTIBASE_HOME/conf/altibase.properties
  FETCH_TIMEOUT  = 60
  ```

### How to check the FETCH_TIMEOUT property value

- **How to check the property value applied to the session**

  Since FETCH_TIMEOUT can be changed on a per-session basis, the value set for each session may be different. The property value set in the session can be checked in V$SESSION.

  ```
  -- ALTIBASE HDB 5 or later
  iSQL> SELECT ID SESSION_ID, FETCH_TIME_LIMIT FROM V$SESSION WHERE ID = SESSION_ID();

  -- ALTIBASE HDB 4.3.9 (My session ID is unknown, so infer it with client IP, PID, etc.
  iSQL> SELECT ID SESSION_ID, DB_USERNAME, CLIENT_CONSTR, COMM_NAME, CLIENT_PID, FETCH_TIME_LIMIT FROM V$SESSION;
  ```
- **Check system property value** It can be changed with ALTER SYSTEM or check the value set in altibase.properties in V$PROPERTY.

  **How to check the property value applied to the session**

  ```
  iSQL> SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME = 'FETCH_TIMEOUT';
  ```
