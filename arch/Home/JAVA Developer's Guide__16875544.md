---
title: "JAVA Developer's Guide"
page_id: "16875544"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/JAVA+Developer%27s+Guide"
updated_at: "2021-02-22T16:17:30.000+0900"
version: 15
ancestors: ["Home"]
labels: []
---

# JAVA Developer's Guide
Source: https://docs.altibase.com/display/arch/JAVA+Developer%27s+Guide
Updated: 2021-02-22T16:17:30.000+0900

- [Overview](#JAVADeveloper'sGuide-Overview) - [Settings before the development](#JAVADeveloper'sGuide-Settingsbeforethedevelopment) - [Types of Altibase JDBC Drivers](#JAVADeveloper'sGuide-TypesofAltibaseJDBCDrivers) - [How to check Altibase JDBC Driver version](#JAVADeveloper'sGuide-HowtocheckAltibaseJDBCDriverversion) - [Setting up JDBC Driver](#JAVADeveloper'sGuide-SettingupJDBCDriver) - [How to set it up in JRE](#JAVADeveloper'sGuide-HowtosetitupinJRE) - [Method 1. CLASSPATH environment variable](#JAVADeveloper'sGuide-Method1.CLASSPATHenvironmentvariable) - [Method 2. JRE(Java Runtime Environment) directory](#JAVADeveloper'sGuide-Method2.JRE(JavaRuntimeEnvironment)directory) - [Method 3. –classpath option at run time](#JAVADeveloper'sGuide-Method3.–classpathoptionatruntime) - [How to set it up in Eclipse](#JAVADeveloper'sGuide-HowtosetitupinEclipse) - [How to use Driver loading & Connection URL](#JAVADeveloper'sGuide-HowtouseDriverloading&ConnectionURL) - [Driver loading](#JAVADeveloper'sGuide-Driverloading) - [General Connection](#JAVADeveloper'sGuide-GeneralConnection) - [Property to be set during the Connection](#JAVADeveloper'sGuide-PropertytobesetduringtheConnection) - [Connection using the Altibase ConnectionPool](#JAVADeveloper'sGuide-ConnectionusingtheAltibaseConnectionPool) - [Connection using the XA](#JAVADeveloper'sGuide-ConnectionusingtheXA) - [Connection using the Failover](#JAVADeveloper'sGuide-ConnectionusingtheFailover) - [Simultaneous connections to different Altibase versions](#JAVADeveloper'sGuide-SimultaneousconnectionstodifferentAltibaseversions) - [Calling Procedure/Function](#JAVADeveloper'sGuide-CallingProcedure/Function) - [Considerations for Development](#JAVADeveloper'sGuide-ConsiderationsforDevelopment) - [Use of PreparedStatement](#JAVADeveloper'sGuide-UseofPreparedStatement) - [Use of executeBatch()](#JAVADeveloper'sGuide-UseofexecuteBatch()) - [Use of setFetchSize()](#JAVADeveloper'sGuide-UseofsetFetchSize()) - [Return of resources](#JAVADeveloper'sGuide-Returnofresources) - [Handling NULL values](#JAVADeveloper'sGuide-HandlingNULLvalues) - [LOB Data Processing](#JAVADeveloper'sGuide-LOBDataProcessing) - [How to use REF CURSOR](#JAVADeveloper'sGuide-HowtouseREFCURSOR) - [Errors](#JAVADeveloper'sGuide-Errors) - [Communication link failure](#JAVADeveloper'sGuide-Communicationlinkfailure) - [No suitable driver](#JAVADeveloper'sGuide-Nosuitabledriver) - [Client unable to establish connection](#JAVADeveloper'sGuide-Clientunabletoestablishconnection) - [Timeout related errors](#JAVADeveloper'sGuide-Timeoutrelatederrors) - [Invalid descriptor index](#JAVADeveloper'sGuide-Invaliddescriptorindex) - [Optional feature not implemented](#JAVADeveloper'sGuide-Optionalfeaturenotimplemented)

# Overview

---

This Developer's guide describes how to develop in integration with Altibase in the JAVA environment and matters to consider during the development. Altibase version 6.5.1, JRE or JDK is version 1.5, and development IDE is based on Eclipse.

In addition to this document, please refer to the following documents during the development.

1. Altibase Development Guide
2. Altibase SQL Tuning Guide

For errors and improvements related to this document, please contact the technical support portal or technical support center.

- Technical support portal: [http://support.altibase.com](http://support.altibase.com/) -> Technical Knowledge -> Q&A
- Technical support center: 02-2082-1114

# Settings before the development

---

Altibase JDBC Driver is required to integrate with Altibase in the JAVA environment. This section describes the Altibase JDBC driver.

## Types of Altibase JDBC Drivers

---

Altibase provides two types of JDBC drivers, and the location of the file is $ALTIBASE_HOME/lib directory.

- Altibase.jar : A general JDBC Driver file used when integrating Altibase DB or multiple Altibase servers of the same version
- Altibase6_5.jar : JDBC Driver file used when integrating Altibase version 5 or earlier version

How to integrate with Altibase with different versions using Altibase.jar and Altibase6_5.jar is described below.

## How to check Altibase JDBC Driver version

To verify the compatibility of the Altibase Server and Altibase JDBC Driver, the user must check the Altibase JDBC Driver version.

It is compatible if the cm protocol versions of Altibase DB Server and CMP of Altibase JDBC Driver are the same.

The command to check the Altibase JDBC Driver version is as follows.

```
$ java –jar Altibase.jar
JDBC Driver Info : Altibase Ver = 6.5.1.5.10 for JavaVM v1.4, CMP:7.1.3, Sep  6 2018 09:17:52
```

The command to check the Altibase DB Server version is as follows.

```
$ altibase -v
version 6.5.1.5.10 X86_64_LINUX_redhat_Enterprise_release6.0-64bit-6.5.1.5.10-release-GCC4.6.3 (x86_64-unknown-linux-gnu) Sep  6 2018 09:26:56, binary db version 6.3.1, meta version 8.1.1, cm protocol version 7.1.3, replication protocol version 7.4.2
```

Generally, it is recommended to use the latest Altibase JDBC Driver file of the same or later version than the Altibase DB Server version.

# Setting up JDBC Driver

---

This section describes how to set the Altibase JDBC Driver.

## How to set it up in JRE

---

To use the Altibase JDBC Driver in the Java Application, the Altibase JDBC Driver must be recognized in JRE.

Use one of the three methods presented below.

#### Method 1. CLASSPATH environment variable

Add the Altibase JDBC Driver (Altibase.jar) file location to the CLASSPATH environment variable.

1) Windows

- Create a new CLASSPATH: Register the CLASSPATH variable by clicking the [New] button in My Computer -> Properties -> Advanced -> Environment Variables.
- Use existing CLASSPATH: Add Altibase JDBC Driver location to the end of the specified variable

![image2019-5-8%2013_40_42.png](https://docs.altibase.com/download/attachments/embedded-page/arch/JAVA%20Developer's%20Guide/image2019-5-8%2013_40_42.png?api=v2)

2) Unix

- Add CLASSPATH to the environment configuration file (for example, `.profile`).

```
export ALTIBASE_HOME=$HOME/altibase_home
export CLASSPATH=.:$ALTIBASE_HOME/lib/Altibase.jar
```

3) Linux

- Add CLASSPATH to the environment configuration file (for example, `.bash_profile`).

```
export ALTIBASE_HOME=$HOME/altibase_home
export CLASSPATH=.:$ALTIBASE_HOME/lib/Altibase.jar
```

#### Method 2. JRE(Java Runtime Environment) directory

- Place the Altibase.jar file in the following directory so that the Altibase JDBC Driver (Altibase.jar) can be automatically referenced in the JRE environment.

```
$JAVA_HOME/jre/lib/ext directory
or
$JRE_HOME/lib/ext directory
```

$JAVA_HOME is the JDK installation directory and $JRE_HOME is the JRE installation directory.

#### Method 3. –classpath option at run time

- When running the Java application with the java command, specify the Altibase JDBC Driver with the -cp or -classpath option

```
$ java –classpath [directory path]/Altibase.jar ClassFileName
Example)
$ java –classpath $ALTIBASE_HOME/lib/Altibase.jar HelloApp
```

## How to set it up in Eclipse

---

This section describes how to add Altibase JDBC Driver in Eclipse.

1. Click JRE System Library [J2SE-1.5] in the Project
2. Click JRE System Library [J2SE-1.5] in the Properties
3. Click the Installed JREs button
4. Select jre among Installed JREs and click Edit button
5. Click the Add External JARs button
6. Select Altibase.jar in the $ALTIBASE_HOME/lib directory

![image2019-10-29%2013_51_58.png](https://docs.altibase.com/download/attachments/embedded-page/arch/JAVA%20Developer's%20Guide/image2019-10-29%2013_51_58.png?api=v2)

# How to use Driver loading & Connection URL

---

This section describes how to load the Altibase JDBC Driver and connect to Altibase.

## Driver loading

---

The class name of Altibase JDBC Driver is Altibase.jdbc.driver.AltibaseDriver.

The following is an example of the code that loads the Driver by calling the Class.forName method.

```
Class.forName("Altibase.jdbc.driver.AltibaseDriver");
```

## General Connection

---

When receiving a connection object from JDBC, the DriverManager.getConnection method is called.

At this time, the String type url should be entered as an argument. An example of writing the Altibase connection url is as follows.

```
jdbc:Altibase://ip_address:port_no/db_name
  * ip_address : ip of Altibase DB server
  * port_no : port_no of Altibase(Defined as PORT_NO property in $ALTIBASE_HOME/conf/altibase.properties)
  * db_name : Altibase DB name (the `DB_NAME` property in `$ALTIBASE_HOME/conf/altibase.properties`)
```

The following is an example of receiving a connection object according to the above format.

**AltibaseConnection.java**

```
String db_url1 = "jdbc:Altibase://192.168.1.111:20300/mydb";
Properties props1 = new Properties();
props1.put("user", "sys");
props1.put("password", "manager");
Connection altibaseConnection1 = DriverManager.getConnection(db_url1, props1);
* Server ip is 192.168.1.111, port_no is 20300, db_name is mydb
```

The following is how to lookup the DB_Name.

```
iSQL> SELECT DB_NAME FROM V$DATABASE;
DB_NAME
------------------------------------------------------------------------------------------------------------------------------------
mydb
1 row selected.
```

## Property to be set during the Connection

---

When connecting, the user can specify various properties including the user name and password of the db. Properties can be specified by using the java.util.Properties class, or by connecting to the String url part in the form of &property_name=value.

The properties that can be specified are as follows.

| Property name | Description | Default value |
| --- | --- | --- |
| portNumber | PORT_NO of DB | 20300 |
| databaseName | NAME of DB | JDBC |
| user | User name of DB | SYS |
| password | password of DB | MANAGER |
| serverName | IP of DB server | localhost |
| connType | Connection type<br>1: TCP/IP<br>3: IPC | 1 |

The following are examples of specifying properties.

1. Using the Property class

  ```
  Properties props1 = new Properties();
  props1.put("user", "sys");
  props1.put("password", "manager");
  Connection altibaseConnection1 = DriverManager.getConnection(db_url1, props1);
  ```
2. Connecting to URL and specifying

  ```
  String db_url1 = "jdbc:Altibase://192.168.1.111:20300/mydb?user=sys&password=manager";
  Connection altibaseConnection1 = DriverManager.getConnection(db_url1);
  ```

## Connection using the Altibase ConnectionPool

1. Version 6.3.1 or later

If you use the `AltibaseConnectionPoolDataSource` class provided by Altibase, you can manage connections by using ConnectionPool. After creating an `AltibaseConnectionPoolDataSource` object, set the connection URL information by using the `setUrl()` method, or call the `setXXX()` method that sets each property. The `AltibaseConnectionPoolDataSource` class is defined in the `Altibase.jdbc.driver` package.

  **AltibaseConnectionPool.java**

  ```
  import Altibase.jdbc.driver.*;
  …
  String db_url1 = "jdbc:Altibase://192.168.1.111:20300/mydb";
  AltibaseConnectionPoolDataSource pool = new AltibaseConnectionPoolDataSource();
                          pool.setUrl(db_url1);
                          pool.setUser("sys");
                          pool.setPassword("manager");
                          pool.setInitialPoolSize(10);
                          pool.setMinPoolSize(5);
                          pool.setMaxPoolSize(15);
  pool.setMaxIdleTime(10);
  ..
  Connection altibaseConnection1 = pool.getConnection();
  ...
  ```
2. Version 6.1.1

If you use the `ABPoolingDataSource` class provided by Altibase, you can manage connections by using ConnectionPool. After creating an `ABPoolingDataSource` object, set the connection URL information by using the `setUrl()` method, or call the `setXXX()` method that sets each property. The `ABPoolingDataSource` class is defined in the `Altibase.jdbc.driver` package.

  **AltibaseConnectionPool.java**

  ```
  import Altibase.jdbc.driver.*;
  …
  String db_url1 = "jdbc:Altibase://192.168.1.111:20300/mydb";

  ABPoolingDataSource pool = new ABPoolingDataSource();
                          pool.setUrl(db_url1);
                          pool.setUser("sys");
                          pool.setPassword("manager");
                          pool.setInitialPoolSize(10);
                          pool.setMinPoolSize(5);
                          pool.setMaxPoolSize(15);
  pool.setMaxIdleTime(10);
  ..
  Connection altibaseConnection1 = pool.getConnection();
  ...
  ```

If necessary, the following properties can be applied to the ConnectionPool.

| Property | Description |
| --- | --- |
| url | Connection string information for connecting with Altibase<br>jdbc:Altibase://IP:port_no/db_name |
| user | Database account |
| password | Database password |
| maxPoolSize | Maximum number of Connections. Default value: 10. |
| minPoolSize | Minimum number of Connections. Default value: 0. |
| initialPoolSize | Initial number of Connections. Default value: 1. |
| maxIdleTime | Idle wait time |
| propertyCycle | Waiting time when the ConnectionPool is full (millisec) |

## Connection using the XA

---

1. Version 6.3.1 or later

To manage distributed transactions, use the `AltibaseXADataSource` class to get a connection. This class is defined in the `Altibase.jdbc.driver` package. The following example implements XA by getting an `XAConnection` object through an `AltibaseXAResource` object, and then getting a `Connection` object through the `XAConnection` object.

  **AltibaseXAConnection.java**

  ```
  import Altibase.jdbc.driver.*;
  …
  AltibaseXADataSource axds1 = new AltibaseXADataSource();
  axds1.setUrl("jdbc:Altibase://192.168.1.111:20300/mydb");
  axds1.setUser("SYS");
  axds1.setPassword("MANAGER");
  AltibaseXADataSource axds2 = new AltibaseXADataSource();
  axds2.setUrl("jdbc:Altibase://192.168.1.222:20300/mydb");
  axds2.setUser("SYS");
  axds2.setPassword("MANAGER");
  // Get XA connections to the underlying data sources
  XAConnection pc1  = axds1.getXAConnection();
  XAConnection pc2  = axds2.getXAConnection();
  // Get the physical connections
  Connection conn1 = pc1.getConnection();
  Connection conn2 = pc2.getConnection();
  // Get the XA resources
  XAResource axar1 = pc1.getXAResource();
  XAResource axar2 = pc2.getXAResource();
  ```
2. Version 6.1.1

To manage distributed transactions, use the `ABXADataSource` class provided by Altibase to get a connection. This class is defined in the `Altibase.jdbc.driver` package. As in the following example, XA can be implemented by getting an `XAConnection` object through an `ABXAResource` object, and then getting a `Connection` object through the `XAConnection` object.

  **AltibaseXAConnection.java**

  ```
  import Altibase.jdbc.driver.*;
  …
  ABXADataSource axds1 = new ABXADataSource();
  axds1.setUrl("jdbc:Altibase://192.168.1.111:20300/mydb");
  axds1.setUser("SYS");
  axds1.setPassword("MANAGER");
  ABXADataSource axds2 = new ABXADataSource();
  axds2.setUrl("jdbc:Altibase://192.168.1.222:20300/mydb");
  axds2.setUser("SYS");
  axds2.setPassword("MANAGER");
  // Get XA connections to the underlying data sources
  XAConnection pc1 = axds1.getXAConnection();
  XAConnection pc2 = axds2.getXAConnection();
  // Get the physical connections
  Connection conn1 = pc1.getConnection();
  Connection conn2 = pc2.getConnection();
  // Get the XA resources
  XAResource axar1 = pc1.getXAResource();
  XAResource axar2 =
  pc2.getXAResource();
  ```

## Connection using the Failover

---

Starting from Altibase version 5.3.3, the user can define Failover-related properties in the connection url part.

This is an example of connecting to Altibase by using Failover.

**AltibaseFailOverConnection.java**

```
String db_url1 = "jdbc:Altibase://192.168.1.1111:20300/mydb?alternateservers=(192.168.1.1111:20300,192.168.1.222:20300)
 &connectionretrycount=3&connectionretrydelay=3&sessionfailover=off
 &loadbalance=off";
Properties props1 = new Properties();
props1.put("user", "sys");
props1.put("password", "manager");
Connection altibaseConnection1 = DriverManager.getConnection(db_url1,props1);
```

Failover-related properties are as follows.

| Property | Description |
| --- | --- |
| alternateservers | This indicates an available server to be connected in case of a failure (IP Address1:Port1, IP Address2:Port2,...) |
| connectionretrycount | The number of retries of connection attempts when the connection to an available server fails |
| connectionretrydelay | The time to wait before retrying to connect when the connection to an available server fails (in seconds) |
| loadbalance | on setting: Randomly selects the default server and available server when attempting to connect for the first time<br>off setting: Connects to the default server when attempting to connect for the first time, and connects to the server described as AlternateServer if the connection fails. |
| sessionfailover | Indicates whether to perform Service Time Fail-Over (STF). Altibase recommends CTF.<br>on: STF, off: CTF<br>- CTF (Connection Time Fail-Over): Recognizes a failure when connecting to the DBMS, connects to another available DBMS node instead of the failed DBMS, and proceeds with service.<br>- STF (Service Time Fail-Over): Handles a failure that occurs during service after a successful DBMS connection. It reconnects to another available DBMS node, restores session properties, and then executes the user application's business logic again. Configure STF when the operation performed on the failed DBMS must be performed again. |

## Simultaneous connections to different Altibase versions

Starting from Altibase version 5 or later, an additional Altibase Driver (`Altibase5.jar`) is provided so that one application can connect to later and earlier Altibase versions at the same time. The driver class name is defined as `Altibase5.jdbc.driver.AltibaseDriver`.

When loading the driver class by using the `Class.forName()` method in the application, specify the class names as `Altibase.jdbc.driver.AltibaseDriver` and `Altibase5.jdbc.driver.AltibaseDriver` to connect to and use different Altibase versions.

**To connect to different Altibase versions simultaneously, load `Altibase5.jdbc.driver.AltibaseDriver` first.**

The following is an example of simultaneous connections to different Altibase versions.

```
 - AltibaseMultiversionConnection.java file
// ALTIBASE 6.5 Driver class
Class.forName("Altibase5.jdbc.driver.AltibaseDriver");
// ALTIBASE 6.3 Driver class
Class.forName("Altibase.jdbc.driver.AltibaseDriver");
//ALTIBASE version 6.5 URL
String db_url1 = "jdbc:Altibase://192.168.1.111:20300/mydb";
//ALTIBASE version 6.3 URL
String db_url2 = "jdbc:Altibase://192.168.1.222:20300/mydb";
```

### Considerations for IBM Java 1.6 environment

Because the `DriverManager` of IBM Java 1.6 handles exceptions immediately without retrying, the URL including the cm protocol version must be specified in the connection string.

The following is an example of configuration considering the characteristics of DriverManager of IBM Java 1.6.

**AltibaseMultiversionConnection.java**

```
// Example of URL with cm version added
String db_url1 = "jdbc:Altibase_5.6.2://192.168.1.111:20300/mydb";
String db_url2 = "jdbc:Altibase_4.5.1://192.168.1.222:20300/mydb";
```

## Calling Procedure/Function

---

When calling the stored procedure created in the DB, write the call SQL statement as follows.

1. **Stored Procedure**

  ```
  { call procedure_name(?,?,....) }
  * `?` is a parameter corresponding to the parameter of the procedure.
  ```
2. **Stored Function**

  ```
  { call ? := function_name(?,?,....) }
  * The `?` before `:=` is a parameter indicating the result value after calling the function.
   The `?` in `()` is a parameter corresponding to the parameter of a function.
  ```

The following is an example of calling stored procedures and functions.

**AltibasePSMCall.java**

```
// Calling Stored Procedure
String sql1 = "{call sum_proc(?,?,?)}";
CallableStatement altibaseStatement1 = altibaseConnection1.prepareCall(sql1);
altibaseStatement1.setInt(1,10);
altibaseStatement1.setInt(2,20);
altibaseStatement1.registerOutParameter(3,java.sql.Types.NUMERIC);
altibaseStatement1.execute();
System.out.println(altibaseStatement1.getDouble(3));
System.out.println();
// Calling Stored Function
String sql2 = "{call ? := sum_func(?,?)}";
CallableStatement altibaseStatement2 = altibaseConnection1.prepareCall(sql2);
altibaseStatement2.registerOutParameter(1,java.sql.Types.NUMERIC);
altibaseStatement2.setInt(2,10);
altibaseStatement2.setInt(3,20);
altibaseStatement2.execute();
System.out.println(altibaseStatement2.getDouble(1));
```

# Considerations for Development

---

This section describes the considerations to be referred when developing JAVA.

## Use of PreparedStatement

---

PreparedStatement is an object that creates SQL statements in advance and binds and processes values with parameters as needed.

For SQL statements that can be processed with binding-execute using parameters, using `PreparedStatement` objects provides better performance than using `Statement` objects that process SQL statements with prepare-execute each time. For example, use a `PreparedStatement` object for statements that insert n rows or repeatedly select with a specific value as a condition.

## Use of executeBatch()

---

When bulk DML statement processing is required, use `executeBatch()` so multiple data rows can be stored in an array and sent to the server at once through array processing.

When using the `executeUpdate()` method to process bulk DML statements, communication costs with the DB server are incurred for each method call. Using `executeBatch()` can reduce the number of communications with the DB server and improve performance.

To use it, first call `addBatch()` repeatedly to store n rows of data in the array, and then execute `executeBatch()`.

## Use of setFetchSize()

---

If the user uses the setFetchSize() method, the user can specify the number of records to be fetched from the DB server at one time when searching.

However, because client memory usage increases in proportion to the number of records specified by `setFetchSize`, it is not recommended to set an unnecessarily large value.

For example, in a program that fetches 5000-byte records, setting `setFetchSize(1000)` instead of `setFetchSize(10)` increases memory usage by about `5000 * (1000 - 10) = 4950K bytes`.

## Return of resources

---

When finishing using the Connection, Statement, or ResultSet object, the close() method must be explicitly called to return the resource.

If `close()` is not called, unused `Connection`, `Statement`, and `ResultSet` objects may remain in heap memory. In particular, if a `Statement` object remains in heap memory, the DB server must continue storing the prepared SQL contents, which increases unnecessary DB server memory usage. The same applies to `PreparedStatement`.

## Handling NULL values

---

When using a `PreparedStatement` object, the `setObject()` and `setNull()` methods can be used to set a NULL value.

- Use setObject(parameterIndex, null, SQLType.NULL) method
- Use setNull(parameterIndex, null) method

Altibase does not support the setObject(parameterIndex, null) method.

## LOB Data Processing

---

In order to process LOB data, **autocommit** must be set to **off**.

If LOB data is processed while autocommit is on, the "Connection is in autocommit mode. One can not operate on LOB datas with autocommit mode on" error or a null value may be returned, resulting in unwanted behavior.

Since autocommit is on by default in JDBC, process LOB data after calling `setAutoCommit(false)` on the `Connection`.

For LOB data integration examples, refer to the Java source files under `$ALTIBASE_HOME/sample/JDBC/CLOB` and `$ALTIBASE_HOME/sample/JDBC/BLOB`.

## How to use REF CURSOR

---

How to use REF CURSOR in Java Program is as follows.

```
-- Define TYPE
CREATE OR REPLACE TYPESET my_type
AS
TYPE my_cur IS REF CURSOR;
END;
/

-- Define REF CURSOR
CREATE OR REPLACE PROCEDURE my_ref_cursor
( v_result OUT my_type.my_cur, v_sql IN VARCHAR(1000) )
AS
BEGIN
OPEN v_result FOR v_sql;
END;
/
-- AltibaseRefCursor.java file
…
String sql = "SELECT to_char(sysdate,'YYYY-MM-DD') FROM dual";
altibaseStatement3= altibaseConnection1.prepareCall(" { call my_ref_cursor(?)}");
altibaseStatement3.setString(1,sql);
altibaseStatement3.execute();
rs = altibaseStatement3.getResultSet();
while(rs.next()){
System.out.println(rs.getString(1));
}
```

# Errors

---

This section describes errors frequently encountered during the development.

## Communication link failure

---

**Causes**

- When the DB is not running
- When connection-related properties are incorrect when connecting
- When the version of Altibase.jar is wrong (eg: If Altibase.jar is used from Altibase version 5.1.5 to access Altibase version 5.3.3)
- In case of disconnection due to TIMEOUT during service

**Solutions**

- **Error occurred when connecting:** Check connection-related properties such as DB server IP, `port_no`, user, and password.
- **Error occurred during service:** Check whether the session was terminated because TIMEOUT occurred.

## No suitable driver

---

**Causes**

- When the Altibase JDBC Driver is incorrect (for example, using the `Altibase.jar` file for Altibase version 4 when connecting to Altibase version 5)

**Solutions**

- Reset Altibase JDBC Driver

## Client unable to establish connection

---

**Causes**

- When the Altibase server is not running

**Solutions**

- Check whether the Altibase server is running

## Timeout related errors

---

**Causes**

- When the defined Timeout value is exceeded

**Solutions**

- Adjust the Timeout value
- Refer to the troubleshooting guide document.

When a client program requests a task to the DB server, a client error message is returned, and an error log is recorded in the server.

| Category | Client error message | Server error message (altibase_boot.log) | Result |
| --- | --- | --- | --- |
| QUERY_TIMEOUT | Client's query exceeded in the execution time limitation | [Notify : Query Timeout] Query Canceled by Server | ROLLBACK the statement and return an error |
| FETCH_TIMEOUT | Communication link failure. | [Notify : Fetch Timeout] Session Closed by Server | ROLLBACK the statement and close the session |
| IDLE_TIMEOUT | Communication link failure. | [Notify : Idle Timeout] Session Closed by Server | ROLLBACK the statement and close the session |
| UTRANS_TIMEOUT | The session has been closed by server. | [Notify : UTrans Timeout] Session Closed by Server | ROLLBACK the statement and close the session |

- Server error message location: `$ALTIBASE_HOME/trc/altibase_boot.log`

## Invalid descriptor index

---

**Causes**

- When calling setXXX() with more values than the bind variable specified in PreparedStatement

**Solutions**

- Adjust the bind variable

## Optional feature not implemented

---

**Causes**

- When calling a method not provided by Altibase

**Solutions**

- Refer to the JDBC manual for JDBC API support.

# Korean Source Attachments

The Korean source page also references these downloadable source attachments. They are preserved here so the English document set does not lose those references.

- [Korean source attachment 1 (PDF)](https://docs.altibase.com/download/attachments/14057500/JAVA_%EA%B0%9C%EB%B0%9C%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1698304337000&api=v2)
