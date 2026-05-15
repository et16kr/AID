---
title: "How to create/delete replication objects"
page_id: "16876082"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876082"
updated_at: "2021-04-05T09:35:15.000+0900"
version: 8
ancestors: ["Home", "03. Replication"]
labels: []
---

# How to create/delete replication objects
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876082
Updated: 2021-04-05T09:35:15.000+0900

- [Overview](#Howtocreate/deletereplicationobjects-Overview) - [Version](#Howtocreate/deletereplicationobjects-Version) - [Preparation](#Howtocreate/deletereplicationobjects-Preparation) - [Enabling the replication function](#Howtocreate/deletereplicationobjects-EnablingthereplicationfunctionRepEnable) - [Creating replication object](#Howtocreate/deletereplicationobjects-Creatingreplicationobjectcreate_rep_obj) - [Starting replication](#Howtocreate/deletereplicationobjects-Startingreplicationcreate_rep_obj_start) - [Deleting replication object](#Howtocreate/deletereplicationobjects-Deletingreplicationobject) - [Error messages](#Howtocreate/deletereplicationobjects-Errormessages) - [Reference Documents](#Howtocreate/deletereplicationobjects-ReferenceDocuments)

# Overview

---

For users who are new to replication, this document explains how to create and delete replication objects.

- This document is written assuming that the user has completed the preliminary operation for replication structure or configuration.
- This document is written assuming that the data is consistent between the target servers for replication. Either all data is identical on both servers, or both servers have zero rows.

# Version

---

Altibase version 4.3.9 or later

# Preparation

---

- Dedicated IP for replication
  It is recommended to use a dedicated network separate from the service network for the IP address used for replication.
- Replication service port
  Set the service port number for replication. It can be arbitrarily set by the user, and 30300 is generally used.
- Select the target table for replication
  The table to be replicated must have a primary key.

# Enabling the replication function

---

- Altibase server's replication function is disabled by default,

  ```
  -- The default value of the REPLICATION_PORT_NO property is 0, which means that the replication function is disabled.

  iSQL> SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME = 'REPLICATION_PORT_NO';
  NAME                            VALUE1
  -------------------------------------------------------------------
  REPLICATION_PORT_NO             0
  1 row selected.
  ```
- To use the replication function, the user must enable it by changing the relevant properties.
- Enabling the replication function requires restarting the Altibase server.

#### Changing REPLICATION_PORT_NO property

- Replication is enabled by changing the value of the Altibase server property REPLICATION_PORT_NO.
- The REPLICATION_PORT_NO property also means the port number to be used between replication threads.
- The port number must not already be used by the server. The user can assign it arbitrarily, and `30300` is commonly used.

1. Check if the replication port specified by the user is in use on the replication target server.

  If `LISTEN` is shown, the port is already used by another process and cannot be used as the replication port.

  ```
  # Example of execution when the replication port, REPLICATION_PORT_NO is set to 30300
  $ netstat -an | grep 30300 | grep LISTEN
  ```
2. Open the altibase.properties file, change the REPLICATION_PORT_NO value, and save it. This must be done on each of the replication target servers.

  ```
  # Example of setting REPLICATION_PORT_NO when setting the replication port to 30300

  $ cd $ALTIBASE_HOME/conf
  $ vi altibase.properties
  REPLICATION_PORT_NO = 30300
  ```
3. Restart the Altibase server process.

  ```
  $ server restart
  ```

  ![grey_arrow_down.png](https://docs.altibase.com/images/icons/grey_arrow_down.png)If you need to block application access during replication object creation

  In order to block access to the application during the process of creating a replication object, change the Altibase server service port and restart it.

  ```
  $ export ALTIBASE_PORT_NO=20400
  $ server restart
  ```
4. After starting the Altibase server, check the replication port LISTEN status and property settings.

  ```
  # Example of Replication port when REPLICATION_PORT_NO is set to 30300
  $ netstat -an | grep 30300 | grep LISTEN
  tcp        0      0 0.0.0.0:30300               0.0.0.0:*                   LISTEN
  ```

  ```
  -- # Example of Replication port when REPLICATION_PORT_NO is set to 30300

  iSQL> SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME = 'REPLICATION_PORT_NO';
  NAME                            VALUE1
  -------------------------------------------------------------------
  REPLICATION_PORT_NO             30300
  1 row selected.
  ```

# Creating replication object

---

- Replication objects are created with the CREATE REPLICATION statement and define information related to replication such as replication mode, replication server information, and replication target table.
- Two servers to be replicated are paired.
- Replication objects must each be created with the same object name on the paired replication server.

  **Syntax for creating replication objects**

  ```
  CREATE REPLICATION replication_name                   -- Define the name of the replication object.
  WITH remote_host_ip, remote_replication_port_no       -- In the WITH clause, specify the IP and PORT of the remote server to be paired with.
  FROM user_name.table_name TO user_name.table_name,    -- List the tables to be replicated in the FROM ~ TO clause.
  FROM ...
  ;
  ```
- Refer to Replication Manual -> 3. Using Replication -> Create Replication (CREATE REPLICATION) for additional options of the replication object creation syntax.
- Manual page: [http://support.altibase.com/en/manual](http://support.altibase.com/en/manual)

![grey_arrow_down.png](https://docs.altibase.com/images/icons/grey_arrow_down.png)Procedure for creating replication objects - Example 1 (when there are 2 replication target servers)

This is an example of creating a replication object when the conditions for creating a replication object are as follows.

- The target server for replication is two A and B servers.
- The replication object name is created as REP1.
- The IP address of the target server A is 192.168.1.112 and the port number is 25524.
- The IP address of the target server B is 192.168.1.113 and the port number is 35524.

![%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-03-17%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%2011.26.41.png](https://docs.altibase.com/download/attachments/embedded-page/FAQE/How%20to%20create/delete%20replication%20objects/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-03-17%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%2011.26.41.png?api=v2)

- The target tables for replication are the SYS user's employees table and departments table.

1. **Server A: IP 192.168.1.112, replication port: 25524**

  ```
  CREATE REPLICATION rep1 WITH '192.168.1.113', 35524
  FROM sys.employees TO sys.employees,
  FROM sys.departments TO sys.departments;
  Create success.
  ```
2. **Server B: IP 192.168.1.113, replication port: 35524**

  ```
  CREATE REPLICATION rep1 WITH '192.168.1.112', 25524
  FROM sys.employees TO sys.employees,
  FROM sys.departments TO sys.departments;
  Create success.
  ```
3. **Check whether the replication object was created**

  **Check on replication target server A**

  ```
   iSQL> SELECT REPLICATION_NAME, HOST_IP, PORT_NO FROM SYSTEM_.SYS_REPL_HOSTS_;
  REPLICATION_NAME                HOST_IP                         PORT_NO
  --------------------------------------------------------------------------------
  REP1                            192.168.1.113                   35524
  1 row selected.

  iSQL> SELECT REPLICATION_NAME, LOCAL_USER_NAME, LOCAL_TABLE_NAME FROM SYSTEM_.SYS_REPL_ITEMS_;
  REPLICATION_NAME                LOCAL_USER_NAME                 LOCAL_TABLE_NAME
  ----------------------------------------------------------------------------------------------------
  REP1                            SYS                             EMPLOYEES
  REP1                            SYS                             DEPARTMENTS
  2 rows selected.
  ```

  **Check on replication target server B**

  ```
  iSQL> SELECT REPLICATION_NAME, HOST_IP, PORT_NO FROM SYSTEM_.SYS_REPL_HOSTS_;
  REPLICATION_NAME                HOST_IP                         PORT_NO
  --------------------------------------------------------------------------------
  REP1                            192.168.1.112                   35524
  1 row selected.

  iSQL> SELECT REPLICATION_NAME, LOCAL_USER_NAME, LOCAL_TABLE_NAME FROM SYSTEM_.SYS_REPL_ITEMS_;
  REPLICATION_NAME                LOCAL_USER_NAME                 LOCAL_TABLE_NAME
  ----------------------------------------------------------------------------------------------------
  REP1                            SYS                             EMPLOYEES
  REP1                            SYS                             DEPARTMENTS
  2 rows selected.
  ```

![grey_arrow_down.png](https://docs.altibase.com/images/icons/grey_arrow_down.png)Procedure for creating replication objects-Example 2 (when there are 3 replication target servers)

This is an example of creating replication objects when the replication target servers are as follows.

- The replication target servers are A, B, and C.
  A synchronizes with B and C, B synchronizes with A and C, and C synchronizes with A and B.
- The replication object names are determined as follows: `REP_A_B` for servers A and B, `REP_B_C` for servers B and C, and `REP_C_A` for servers A and C.
- The IP address and replication port number of each server are as follows: server A is `192.168.1.112:30300`, server B is `192.168.1.113:30300`, and server C is `192.168.1.114:30300`.

![%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-03-17%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%2011.26.07.png](https://docs.altibase.com/download/attachments/embedded-page/FAQE/How%20to%20create/delete%20replication%20objects/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-03-17%20%E1%84%8B%E1%85%A9%E1%84%8C%E1%85%A5%E1%86%AB%2011.26.07.png?api=v2)

- The target tables for replication are the SYS user's employees table and departments table.

1. **A Server : IP 192.168.1.112 , Replication port: 30300**

  ```
  CREATE REPLICATION rep_a_b WITH '192.168.1.113', 30300 FROM sys.employees TO sys.employees, FROM sys.departments TO sys.departments;
  CREATE REPLICATION rep_c_a WITH '192.168.1.114', 30300 FROM sys.employees TO sys.employees, FROM sys.departments TO sys.departments;
  ```
2. **B Server : IP 192.168.1.113 , Replication port: 30300**

  ```
  CREATE REPLICATION rep_a_b WITH '192.168.1.112', 30300 FROM sys.employees TO sys.employees, FROM sys.departments TO sys.departments;
  CREATE REPLICATION rep_b_c WITH '192.168.1.114', 30300 FROM sys.employees TO sys.employees, FROM sys.departments TO sys.departments;
  ```
3. **C Server : IP 192.168.1.114, Replication port: 30300**

  ```
  CREATE REPLICATION rep_c_a WITH '192.168.1.112', 30300 FROM sys.employees TO sys.employees, FROM sys.departments TO sys.departments;
  CREATE REPLICATION rep_b_c WITH '192.168.1.113', 30300 FROM sys.employees TO sys.employees, FROM sys.departments TO sys.departments;
  ```
4. **Check whether the replication object was created**

  **Check on replication target server A**

  ```
  iSQL> SELECT REPLICATION_NAME, HOST_IP, PORT_NO FROM SYSTEM_.SYS_REPL_HOSTS_;
  REPLICATION_NAME                HOST_IP                         PORT_NO
  --------------------------------------------------------------------------------
  REP_A_B                         192.168.1.113                   30300
  REP_C_A                         192.168.1.114                   30300
  2 rows selected.

  iSQL> SELECT REPLICATION_NAME, LOCAL_USER_NAME, LOCAL_TABLE_NAME FROM SYSTEM_.SYS_REPL_ITEMS_;
  REPLICATION_NAME                LOCAL_USER_NAME                 LOCAL_TABLE_NAME
  ----------------------------------------------------------------------------------------------------
  REP_A_B                         SYS                             EMPLOYEES
  REP_A_B                         SYS                             DEPARTMENTS
  REP_C_A                         SYS                             EMPLOYEES
  REP_C_A                         SYS                             DEPARTMENTS
  4 rows selected.
  ```

  **Check on replication target server B**

  ```
  iSQL> SELECT REPLICATION_NAME, HOST_IP, PORT_NO FROM SYSTEM_.SYS_REPL_HOSTS_;
  REPLICATION_NAME                HOST_IP                         PORT_NO
  --------------------------------------------------------------------------------
  REP_A_B                         192.168.1.112                   30300
  REP_B_C                         192.168.1.114                   30300
  2 rows selected.

  iSQL> SELECT REPLICATION_NAME, LOCAL_USER_NAME, LOCAL_TABLE_NAME FROM SYSTEM_.SYS_REPL_ITEMS_;
  REPLICATION_NAME                LOCAL_USER_NAME                 LOCAL_TABLE_NAME
  ----------------------------------------------------------------------------------------------------
  REP_A_B                         SYS                             EMPLOYEES
  REP_A_B                         SYS                             DEPARTMENTS
  REP_B_C                         SYS                             EMPLOYEES
  REP_B_C                         SYS                             DEPARTMENTS
  4 rows selected.
  ```

  **Check on replication target server C**

  ```
  iSQL> SELECT REPLICATION_NAME, HOST_IP, PORT_NO FROM SYSTEM_.SYS_REPL_HOSTS_;
  REPLICATION_NAME                HOST_IP                         PORT_NO
  --------------------------------------------------------------------------------
  REP_B_C                         192.168.1.113                   30300
  REP_C_A                         192.168.1.112                   30300
  2 rows selected.

  iSQL> SELECT REPLICATION_NAME, LOCAL_USER_NAME, LOCAL_TABLE_NAME FROM SYSTEM_.SYS_REPL_ITEMS_;
  REPLICATION_NAME                LOCAL_USER_NAME                 LOCAL_TABLE_NAME
  ----------------------------------------------------------------------------------------------------
  REP_B_C                         SYS                             EMPLOYEES
  REP_B_C                         SYS                             DEPARTMENTS
  REP_C_A                         SYS                             EMPLOYEES
  REP_C_A                         SYS                             DEPARTMENTS
  4 rows selected.
  ```

# Starting replication

---

- Starting replication means starting the data synchronization.
- The server that started the replication starts the replication sender thread, and the remote server paired with the server starts the receive thread.

1. **Selecting the replication start server (active server)**
  The server that starts replication and runs the replication sender is the server where change transactions occur, and is also called the active server.
  Among the replication target servers in a pair, the place where data change occurs is the active server, and the other server becomes the standby server.
  If a change transaction occurs on both servers and synchronizes in both directions, both servers become active servers.
2. **Start of replication** The active server starts replication with the ALTER REPLICATION statement. replication_name is the name of the object created in the replication object creation step.

  ```
  -- The replication sender thread runs on the server that executes this command, and the receiver thread runs on the remote server paired with that server.
  iSQL> ALTER REPLICATION replication_name START;
  ```
3. **Check the status of starting/running replication** This is a statement to check whether the replication sending thread (Sender) and receiving thread (Receiver) are running.

  **How to check the starting status of the replication sender thread (Sender) of the replication start server and active server**

  ```
  iSQL> SELECT REPLICATION_NAME, DECODE(IS_STARTED, 0, 'STOPPED', 1, 'STARTED') IS_STARTED FROM SYSTEM_.SYS_REPLICATIONS_;
  REPLICATION_NAME                IS_STARTED
  -------------------------------------------------------------------
  REP                             STARTED
  1 row selected.

  iSQL> SELECT REP_NAME, DECODE(STATUS, 0, 'STOP', 1, 'START', STATUS) STATUS FROM V$REPSENDER;
  REP_NAME                        STATUS
  -------------------------------------------------------------------
  REP                             START
  1 row selected.
  ```

  **How to check the running status of the replication receiving thread (Receiver)**

  ```
  iSQL> select REP_NAME, MY_IP, MY_PORT FROM V$REPRECEIVER;
  REP_NAME              MY_IP                 MY_PORT
  ------------------------------------------------------------
  REP                   192.168.1.113         30300
  1 row selected.
  ```

# Deleting replication object

---

This section describes how to delete replication objects.

```
-- Stop replication first.
iSQL> ALTER REPLICATION replication_name STOP;

- Delete the replication object.
iSQL> DROP REPLICATION replication_name ;
```

# Error messages

---

Here are some of the error messages that may occur during the process of creating replication objects.

### [ERR-61023 : Replication is disabled]

- This is an error message that can be encountered when executing the CREATE REPLICATION statement. It occurs when the replication function is disabled
- Check the value of the REPLICATION_PORT_NO property. Refer to the section on enabling the replication function.

### [ERR-61113 : A replicated table must have a primary key. (*user_name*.*table_name*)]

- This is an error message that may occur when executing the CREATE REPLICATION statement.
- This occurs when there is no primary key in the replication target table specified in the FROM clause.
- Create a primary key on the table shown in parentheses at the end of the error message, and then execute the replication object creation statement again.

### [ERR-6100D : [Sender] Failed to handshake with the peer server (Handshake Process Error)]

- This is an error message that may occur when ALTER REPLICATION replication_name START is executed.
- Check whether the remote server IP and replication port number entered in the `WITH` clause are correct, and whether the corresponding IP and port are reachable.

# Reference Documents

---

- Replication Manual
- SQL Reference
- Download manual page: [http://support.altibase.com/en/manual](http://support.altibase.com/en/manual)
- Github: [https://github.com/ALTIBASE/Documents/tree/master/Manuals/](https://github.com/ALTIBASE/Documents/tree/master/Manuals/Altibase_7.1/eng)
- Korean source attachment: [D24_ALTIBASE Efficient Replication Guide.pdf](https://docs.altibase.com/download/attachments/13008990/D24_ALTIBASE_%ED%9A%A8%EC%9C%A8%EC%A0%81%EC%9D%B8_%EC%9D%B4%EC%A4%91%ED%99%94_%EA%B0%80%EC%9D%B4%EB%93%9C1.pdf?version=1&modificationDate=1544508306000&api=v2)
- Korean source attachment: [D67_ALTIBASE Replication Constraints Guide.pdf](https://docs.altibase.com/download/attachments/13008990/D67_ALTIBASE_%EC%9D%B4%EC%A4%91%ED%99%94_%EC%A0%9C%EC%95%BD%EC%82%AC%ED%95%AD_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1544508306000&api=v2)
