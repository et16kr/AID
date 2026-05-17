# Application and Framework Integration

## Source paths

R019 source paths covered:

- `arch/Home/TOMCAT Integration Guide for Altibase__14058489.md`
- `arch/Home/TOMCAT Integration Guide for Altibase/1. TOMCAT Installation__14058491.md`
- `arch/Home/TOMCAT Integration Guide for Altibase/2. JDBC Driver Configuration__14058500.md`
- `arch/Home/TOMCAT Integration Guide for Altibase/3. Integrating ALTIBASE and TOMCAT__14058506.md`
- `arch/Home/TOMCAT Integration Guide for Altibase/4. Fail-Over Configuration__14058508.md`
- `arch/Home/TOMCAT Integration Guide for Altibase/5. Considerations when integrating TOMCAT__22643044.md`
- `arch/Home/TOMCAT Integration Guide for Altibase/6. Errors when integrating TOMCAT__14058515.md`
- `arch/Home/JEUS Integration Guide for Altibase__14058459.md`
- `arch/Home/JEUS Integration Guide for Altibase/1. JEUS Installation__14058463.md`
- `arch/Home/JEUS Integration Guide for Altibase/2. Integrating ALTIBASE and JEUS__14058474.md`
- `arch/Home/JEUS Integration Guide for Altibase/3. Sample Examples__14058486.md`
- `arch/Home/JBOSS Integration Guide for Altibase__14647358.md`
- `arch/Home/JBOSS Integration Guide for Altibase/1. JBoss Installation__14647370.md`
- `arch/Home/JBOSS Integration Guide for Altibase/2. Integrating Altibase and JBOSS__14647372.md`
- `arch/Home/JBOSS Integration Guide for Altibase/3. Examples__14647382.md`
- `arch/Home/WEBLOGIC Integration Guide for Altibase__14058319.md`
- `arch/Home/WEBLOGIC Integration Guide for Altibase/WebLogic Glossary__14058321.md`
- `arch/Home/WEBLOGIC Integration Guide for Altibase/0. Prerequisites__14058324.md`
- `arch/Home/WEBLOGIC Integration Guide for Altibase/1. WebLogic Setup__14058327.md`
- `arch/Home/WEBLOGIC Integration Guide for Altibase/2. Starting and Shutdown the WebLogic Server Instance__14058329.md`
- `arch/Home/WEBLOGIC Integration Guide for Altibase/3. ALTIBASE and WebLogic Integration__14058331.md`
- `arch/Home/WEBLOGIC Integration Guide for Altibase/4. Fail-Over & Load-Balancing Settings__14058337.md`
- `arch/Home/WEBLOGIC Integration Guide for Altibase/Integration Error__14058339.md`
- `arch/Home/WebSphere Integration Guide for Altibase__14058343.md`
- `arch/Home/Spring Integration Guide for Altibase__14058410.md`
- `arch/Home/Spring Integration Guide for Altibase/1. What is Spring__14058412.md`
- `arch/Home/Spring Integration Guide for Altibase/2. Setting before Developing Spring__14058420.md`
- `arch/Home/Spring Integration Guide for Altibase/3. Setting up JDBC Driver__14058424.md`
- `arch/Home/Spring Integration Guide for Altibase/4. Configuring DataSource__14058429.md`
- `arch/Home/Spring Integration Guide for Altibase/5. Additional Connection__14058433.md`
- `arch/Home/Spring Integration Guide for Altibase/6. Transaction Manager__14058437.md`
- `arch/Home/Spring Integration Guide for Altibase/7. Considerations_Notes for Spring Integration__14058445.md`
- `arch/Home/Spring Integration Guide for Altibase/8. Appendix - HelloSpring__14058449.md`
- `arch/Home/iBatis Integration Guide for Altibase__14058303.md`
- `arch/Home/iBatis Integration Guide for Altibase/1. iBatis Overview__14058305.md`
- `arch/Home/iBatis Integration Guide for Altibase/2. Sample Preparation using iBATIS__14058307.md`
- `arch/Home/iBatis Integration Guide for Altibase/3. Altibase Integration__14058309.md`
- `arch/Home/iBatis Integration Guide for Altibase/4. iBATIS, Spring, Altibase Integration__14058311.md`
- `arch/Home/iBatis Integration Guide for Altibase/5. Spring Integration Guide for Altibase__14058315.md`
- `arch/Home/iBatis Integration Guide for Altibase/Appendix__14058317.md`
- `arch/Home/MyBatis Integration Guide for Altibase__14058349.md`
- `arch/Home/MyBatis Integration Guide for Altibase/1. MyBatis Overview__14058351.md`
- `arch/Home/MyBatis Integration Guide for Altibase/2. Differences Between MyBatis, and iBatis__14058354.md`
- `arch/Home/MyBatis Integration Guide for Altibase/3. Sample Preparation using MyBatis__14058356.md`
- `arch/Home/MyBatis Integration Guide for Altibase/4. Altibase Integration__22643026.md`
- `arch/Home/MyBatis Integration Guide for Altibase/5. MyBatis, Spring, Altibase Integration__22643028.md`
- `arch/Home/MyBatis Integration Guide for Altibase/6. Transaction Management__22643030.md`
- `arch/Home/MyBatis Integration Guide for Altibase/7. Considerations for MyBatis Integration__22643032.md`
- `arch/Home/MyBatis Integration Guide for Altibase/8. Appendix 1 (MyBatis-Altibase Integration)__22643034.md`
- `arch/Home/MyBatis Integration Guide for Altibase/9. Appendix 2(Spring-MyBatis-Altibase Integration)__22643036.md`
- `arch/Home/Hibernate Integration Guide for Altibase__14058388.md`

## Source coverage notes

This document consolidates the R019 WAS and framework integration set: Tomcat, JEUS, JBoss, WebLogic, WebSphere, Spring, iBATIS, MyBatis, and Hibernate. It keeps the framework-specific setup procedures separate because driver placement, datasource fields, transaction behavior, and failover support differ by framework.

R018 owns the FAQ source `FAQE/Home/07. Development and API/How to manage Spring+iBatis transaction__16876194.md` in `llm-reference/09-development-client-api.md`. This R019 document still covers the Spring, iBATIS, and MyBatis framework guides, including overlapping LOB and transaction rules from the technical guides.

Embedded screenshots in the source are evidence for UI procedures. They are not reconstructed here. URL-backed document attachments, external references, and legacy no-downloadable-URL labels are recorded in `llm-reference/coverage/attachment-diagram-register.tsv`.

## Scope and audience

Use this document to answer how to integrate Altibase with Java application servers, Spring-based applications, SQL mapping frameworks, and Hibernate. The expected readers are application developers, middleware engineers, DBAs, support engineers, and LLMs that need exact setup parameters, commands, paths, JDBC URL forms, datasource class names, failover properties, transaction requirements, and source-specific cautions.

When answering in another language, keep product names, class names, jar names, command names, XML element names, property names, SQL, paths, error text, and JDBC URL properties exactly as written.

## Key facts

### Common JDBC integration facts

Altibase provides the JDBC driver as `Altibase.jar` under `$ALTIBASE_HOME/lib`. Starting from Altibase version 5, the source guides also describe major-version jar names such as `Altibase5.jar`, and in WebLogic/MyBatis multi-version examples also use names such as `Altibase6.jar` or `Altibase7.jar`.

Use the general JDBC driver class for the current Altibase driver:

```text
Altibase.jdbc.driver.AltibaseDriver
```

Use major-version-prefixed driver classes when loading multiple Altibase versions in one application:

```text
Altibase5.jdbc.driver.AltibaseDriver
Altibase6.jdbc.driver.AltibaseDriver
Altibase7.jdbc.driver.AltibaseDriver
```

The normal JDBC URL form is:

```text
jdbc:Altibase://IP:port_no/db_name
```

Check JDBC driver compatibility by comparing the JDBC driver's `CMP` value with the server `cm protocol version`.

```bash
java -jar Altibase.jar
altibase -v
```

In framework datasource examples, the standard test query is one of these:

```sql
select 1 from dual
SELECT 1 FROM DUAL
select * from dual
select to_char(sysdate,'yyyy/mm/dd hh24:mi:ss') from dual
```

### Driver placement by framework

| Framework | Driver placement or classpath rule |
| --- | --- |
| Tomcat | Put `Altibase.jar` in `CLASSPATH` through `$CATALINA_HOME/bin/catalina.sh`, or place it where the web application or Tomcat can load it. |
| JEUS | Put `Altibase.jar` in `$JEUS_HOME/lib/datasource`. |
| JBoss | Put `Altibase.jar` in `JBOSS_HOME/common/lib`; restart JBoss because the directory is not reflected dynamically. |
| WebLogic | Put JDBC jars in `$DOMAIN_HOME/lib` or add them to `CLASSPATH` in `startWebLogic.cmd`; restart the Administration Server. |
| WebSphere | Put `Altibase.jar` in `${WAS_INSTALL_ROOT}\universalDriver\lib` and configure a JDBC provider. |
| Spring | Add `Altibase.jar` to the Eclipse project, JRE library, or web application `WEB-INF/lib`. |
| iBATIS | Add `Altibase.jar` and `ibatis-2.3.4.x.jar` to the Java project. |
| MyBatis | Add `Altibase.jar` and `mybatis-3.2.8.jar`; add `mybatis-spring-1.x.x.jar` for Spring integration. |
| Hibernate | Add `Altibase.jar`, Hibernate jars, and the Altibase dialect classes packaged into the Hibernate core jar. |

### Source version baselines

| Source area | Version baseline from source |
| --- | --- |
| Tomcat | Altibase v6.3 or later and Tomcat v7.0; Tomcat install example uses `apache-tomcat-7.0.56.tar.gz`. |
| JEUS | ALTIBASE 6.3.1 with JEUS6.0; JEUS6.0 requires JDK 5.0 Update 4 (`1.5.0_04`) or later and at least 300 MB free disk space. |
| JBoss | Altibase 6.5.1 and JBoss 6.1.0.Final; JBoss requires JDK 1.6 or later and the test used JDK 1.7. |
| WebLogic | WebLogic 12.1.3.0 on Windows; WebLogic 8.1.6.0 or later is recommended. |
| WebSphere | Altibase v7.1.0 and WebSphere v9.0; IBM Installation Manager 1.8.5 is the source baseline. |
| Spring | Spring Framework 3.2.x, ALTIBASE 6.3.1, Eclipse; old Spring 2.5 document is preserved as an attachment. |
| iBATIS | iBATIS 2.3.4, Spring Framework 2.5.6, Altibase 5.3.3, Eclipse. |
| MyBatis | MyBatis 3.2.8, ALTIBASE 6.3.1, Eclipse and Maven. |
| Hibernate | Hibernate 5.4.8 in the updated source, with Altibase dialect classes added manually. |

## Procedures

### Tomcat integration

Install Tomcat after JDK or JRE is available. The source example downloads `apache-tomcat-7.0.56.tar.gz`, extracts it, moves the directory to `/app/was/tomcat7`, and sets:

```bash
export CATALINA_HOME=/app/was/tomcat7
export JAVA_HOME=/app/java/jdk1.6
export PATH=$CATALINA_HOME/bin:$JAVA_HOME/bin:$PATH
catalina.sh start
catalina.sh stop
```

To expose the Altibase driver globally, add `$ALTIBASE_HOME/lib/Altibase.jar` to `CLASSPATH` in `$CATALINA_HOME/bin/catalina.sh`, then stop and start Tomcat.

For Tomcat JNDI, define a datasource in `$CATALINA_HOME/conf/context.xml`:

```xml
<context>
  <Resource name="jdbc/Altibase" auth="Container"
    type="javax.sql.DataSource"
    driverClassName="Altibase.jdbc.driver.AltibaseDriver"
    url="jdbc:Altibase://127.0.0.1:20300/mydb"
    username="sys" password="manager"
    maxActive="3" maxIdle="2" initialSize="1"
    defaultAutoCommit="false"
    removeAbandoned="true" logAbandoned="true"
    removeAbandonedTimeout="60"
    validationQuery="select 1 from dual"/>
</context>
```

Register the resource reference in `WEB-INF/web.xml` with `res-ref-name` `jdbc/Altibase`, `res-type` `javax.sql.DataSource`, and `res-auth` `Container`. Application code looks up either `java:/comp/env` plus `jdbc/Altibase`, or directly `java:comp/env/jdbc/Altibase`, then calls `DataSource.getConnection()`.

The general JDBC method loads `Altibase.jdbc.driver.AltibaseDriver`, uses `DriverManager.getConnection(url, prop)`, executes a SQL statement, and closes `ResultSet`, `Statement`, and `Connection`.

Tomcat itself does not provide failover. Use Altibase JDBC failover parameters in the datasource URL. Altibase failover is available starting from Altibase v5.3.3:

```text
jdbc:Altibase://192.168.6.224:21129/mydb?AlternateServers=(192.168.1.35:21129)&ConnectionRetryCount=3&ConnectionRetryDelay=3&SessionFailOver=off&LoadBalance=off
```

Tomcat DBCP cautions:

- When changing `testOnBorrow` or `poolPrepareStatements` for performance, JDK/JRE 1.6 or later is recommended.
- With JDK 1.5 and Tomcat 6 DBCP 1.3, `testOnBorrow=False` and `poolPrepareStatements=true` are not recommended.
- Explicitly close `ResultSet`, `Statement`, and `Connection`; unclosed connections are not returned to the pool and unclosed statements increase DB server `Query_Prepare` memory.
- Use `removeAbandoned="true"` to recover abandoned DBCP connections.

### JEUS integration

The JEUS source installs JEUS6.0 in console mode with `jeus60_unix_generic_ko.bin`, accepts the license, selects the OS platform, chooses the install path such as `/app/was/jeus6`, selects the install set, enters the JDK location, and sets the administrator password.

JEUS environment variables include:

| Variable | Meaning or value |
| --- | --- |
| `PATH` | Should include `$JEUS_HOME/bin`, `$JEUS_HOME/webserver/bin`, and `$JEUS_HOME/lib/system`. |
| `JEUS_LIBPATH` | `$JEUS_HOME/lib/system` |
| `JEUS_HOME` | JEUS installation directory, for example `$HOME/jeus6/` |
| `JEUS_BASSPORT` | Basic JEUS port, default `9763` |
| `JAVA_HOME` | JAVA2 installation directory |

Start JEUS with `jeus`; the expected standby message is `JEUS Manager is READY`. Shut it down with `jeusadmin`, connect to the node, run `down`, confirm with `y`, and look for `all containers successfully shutdowned`. Verify the process with:

```bash
ps -ef | grep jeus
```

Installation cautions:

- Selecting the wrong OS architecture can cause `java.lang.UnsatisfiedLinkError` for `$HOME/jeus6/lib/system/libRunner.so`.
- On Linux, GLIBC lower than 2.4 can cause `version 'GLIBC_2.4' not found`; check with `rpm -qa |grep glibc`.

Put `Altibase.jar` under `$JEUS_HOME/lib/datasource`. Configure datasources in `JEUSMain.xml` or WebAdmin. The source describes four datasource types: `DataSource`, `ConnectionPoolDataSource`, `XADataSource`, and `LocalXADataSource`.

For `BlackboxConnectionPoolDataSource`, JEUS manages the pool. In `JEUSMain.xml`, use `vendor` `others`, `data-source-class-name` `jeus.jdbc.driver.blackbox.BlackboxConnectionPoolDataSource`, `data-source-type` `ConnectionPoolDataSource`, and properties:

```text
DriverClassName=Altibase.jdbc.driver.AltibaseDriver
URL=jdbc:Altibase://server_ip:server_port/dbname
USER=sys
PASSWORD=manager
```

Do not also set `Database Name`, `Port Name`, and `Server Name` when using the Blackbox property form; the source says an error occurs if those fields are set while the required `Property` values are absent or conflicting.

For `AltibaseConnectionPoolDataSource`, use:

```xml
<data-source-class-name>Altibase.jdbc.driver.AltibaseConnectionPoolDataSource</data-source-class-name>
<data-source-type>ConnectionPoolDataSource</data-source-type>
<database-name>mydb</database-name>
<port-number>20300</port-number>
<server-name>127.0.0.1</server-name>
<user>sys</user>
<password>manager</password>
<auto-commit>true</auto-commit>
<property>
  <name>Encoding</name>
  <type>java.lang.String</type>
  <value>KSC5601</value>
</property>
<property>
  <name>maxPoolSize</name>
  <type>java.lang.Integer</type>
  <value>30</value>
</property>
```

Version caution: in Altibase 6.3.1 or later, use uppercase `URL`; in some earlier versions, use lowercase `Url`. If the property name does not match the driver method, JEUS can raise `java.lang.NoSuchMethodException: Altibase.jdbc.driver.ABConnectionPoolDataSource.setURL(java.lang.String)`.

Deadlock caution: when using `AltibaseConnectionPoolDataSource`, lock can occur with `initialPoolSize`. The source says to use `maxPoolSize` instead of `initialPoolSize`.

JEUS connection validation uses `check-query`, `check-query-timeout`, `non-validation-interval`, and `destroy-policy-on-check-query`. Use a SELECT-only check query such as `select 1 from dual`; do not use update statements. `check-query-timeout` is in milliseconds and values less than `1000` are treated as `0`. `destroy-policy-on-check-query` can be `FailedConnectionOnly` or `AllConnections`.

Monitor JEUS pools with:

```text
Jeusadmin> dsinfo -con Container name Data source name
Jeusadmin> dsconinfo -con Container name Data source name
Jeusadmin> testdsconfig data source name
```

JEUS sample JSPs either look up a datasource such as `DataSource1` or connect through `DriverManager` with `jdbc:Altibase://127.0.0.1:20300/mydb`, `user=sys`, `password=manager`, and `encoding=KO16KSC5601`. The deployment sample creates a Dynamic Web Project in Eclipse, places the JSP and `Altibase.jar`, exports a WAR, uploads and deploys the WAR through WebAdmin, and tests a URL such as `http://192.168.1.76:8088/AltiTest/test.jsp`.

### JBoss integration

The JBoss guide installs JBoss by downloading and unzipping `jboss-6.1.0.GA.zip`. The created `jboss-6.1.0.Final` directory is treated as `JBOSS_HOME`. Configure JDK by setting `JAVA_HOME` in the system environment or by editing `JBOSS_HOME/bin/run.bat` on Windows or `JBOSS_HOME/bin/run.sh` on Unix.

Run JBoss with:

```bash
sh run.sh
```

It is running normally when the final log says `JBossAS [6.1.0.Final "Neo"] Started`. Shut down with:

```bash
sh shutdown.sh -S
```

JBoss default port is `8080`. If another process uses it, startup can fail with `java.net.BindException: Address already in use /127.0.0.1:8080`. Change the connector port in `JBOSS_HOME/server/default/deploy/jbossweb.sar/server.xml`, for example:

```xml
<Connector protocol="HTTP/1.1" port="8088" address="${jboss.bind.address}" redirectPort="${jboss.web.https.port}" />
```

For JNDI datasource use, place `Altibase.jar` in `JBOSS_HOME/common/lib` and restart JBoss. Datasource XML files are placed in `JBOSS_HOME/server/default/deploy` with names such as `altibase-ds.xml` or `altibase-xa-ds.xml`.

A local transaction datasource uses:

```xml
<datasources>
  <local-tx-datasource>
    <jndi-name>AltiTest</jndi-name>
    <connection-url>jdbc:Altibase://127.0.0.1:20300/mydb</connection-url>
    <driver-class>Altibase.jdbc.driver.AltibaseDriver</driver-class>
    <user-name>sys</user-name>
    <password>manager</password>
    <min-pool-size>10</min-pool-size>
    <max-pool-size>100</max-pool-size>
    <blocking-timeout-millis>5000</blocking-timeout-millis>
    <idle-timeout-minutes>15</idle-timeout-minutes>
    <metadata>
      <type-mapping>Altibase</type-mapping>
    </metadata>
  </local-tx-datasource>
</datasources>
```

Distributed transactions use `xa-datasource`, `Altibase.jdbc.driver.ABXADataSource`, `ServerName`, `PortNumber`, `User`, `Password`, and a validation query such as `select * from system_.sys_database_`.

For Altibase library failover, use an Altibase JDBC failover URL. This supports CTF and STF starting from Altibase 5.3.3:

```xml
<connection-url>jdbc:Altibase://127.0.0.1:20911/mydb?AlternateServers=(192.168.1.76:20911)&ConnectionRetryCount=3&ConnectionRetryDelay=3&LoadBalance=off&SessionFailOver=off</connection-url>
```

JBoss also supports a datasource URL delimiter form:

```xml
<connection-url>jdbc:Altibase://127.0.0.1:20911/mydb,jdbc:Altibase://192.168.1.76:20911/mydb</connection-url>
<url-delimiter>,</url-delimiter>
```

The JBoss syntax provides only CTF.

JBoss JSP examples look up `java:/AltiTest`, run `select * from dual`, close resources, and can be tested by adding a JSP to `ROOT.war` or by creating and deploying a WAR through the JBoss web console. Example URLs include `http://localhost/test.jsp` and `http://localhost:8080/AltiTest/test.jsp`.

### WebLogic integration

The WebLogic source is based on WebLogic 12.1.3.0 on Windows. It recommends WebLogic 8.1.6.0 or later. Lower versions can fail or hang when using incompatible Altibase JDBC drivers.

Altibase 5 JDBC was built with JDK 1.4 based on JDBC 3.0. Applications written against JDBC 4.0 on JRE 1.6 or later can hit unsupported JDBC APIs, so the source says to comply with JDBC 3.0 when necessary and review unsupported specifications in the API Manual.

Create a WebLogic domain with the Configuration Wizard. Important paths:

- `WL_HOME`: WebLogic installation path.
- `DOMAIN_HOME`: domain path.
- `$DOMAIN_HOME/autodeploy`: auto-deploy location in development mode.

Use scripts under `$DOMAIN_HOME/bin`:

```text
startWebLogic.cmd
stopWebLogic.cmd
startManagedWebLogic.cmd
stopManagedWebLogic.cmd
```

Startup is normal when the server enters `RUNNING` and `Server state changed to RUNNING`. The shutdown script result alone does not guarantee normal shutdown; if the process remains, check the WebLogic Server instance log.

To configure the Altibase JDBC driver, either put jars in `$DOMAIN_HOME/lib` or edit `startWebLogic.cmd`:

```text
set CLASSPATH=%SAVE_CLASSPATH%;C:\WebLogic_lib\Altibase5.jar;C:\WebLogic_lib\Altibase.jar
```

Restart the Administration Server after changing driver placement or classpath.

Create a JDBC datasource in the Administration Console at `http://127.0.0.1:7001/console`. Use database type `Other`. For the connection pool, use:

```text
Driver class name: Altibase.jdbc.driver.AltibaseDriver
URL: jdbc:Altibase://127.0.0.1:20300/mydb
Property: user = sys for ALTIBASE 4; can be omitted for ALTIBASE 5 and ALTIBASE 6
Test Table: dual
```

Deploy the datasource to the target server and use the same datasource name and JNDI name when possible. The source example creates datasource `altibase`, changes `Initial Capacity` in the connection pool settings, then checks:

- WebLogic: Monitoring tab, Testing tab for the datasource.
- Altibase: query `v$session` to confirm the expected number of `JDBC` sessions.

```sql
select comm_name, client_type, db_username, id session_id from v$session;
```

The web application sample creates `WEB-INF/web.xml`, deploys under `$DOMAIN_HOME/autodeploy`, then uses JSP code to look up JNDI name `altibase` and query `v$database` for `db_name`, `product_signature`, and `sysdate`.

For simultaneous Altibase versions, create a datasource per version:

- `altibase` using `Altibase.jdbc.driver.AltibaseDriver`
- `altibase5` using `Altibase5.jdbc.driver.AltibaseDriver`

The WebLogic source says the package's current `Altibase.jar` and renamed compatibility jar for a major version are the same driver under different names, used to allow multiple driver classes in one process. It lists compatibility names by major version: `Altibase5.jar`, `Altibase6.jar`, and `Altibase7.jar`.

WebLogic multiple datasource failover sends the request to the first datasource and then to the next until one succeeds. Multiple datasource load balancing distributes connection requests across the datasource list and also provides failover behavior. Altibase library-layer failover and load balancing are available from Altibase v5.3.3 and are configured in the JDBC URL.

### WebSphere integration

The WebSphere guide is based on WebSphere v9.0 and Altibase v7.1.0. It installs IBM Installation Manager first, then WebSphere Application Server through IBM repository URLs such as:

```text
http://www.ibm.com/software/repositorymanager/V9WASBase
http://www.ibm.com/software/repositorymanager/V9WASND
```

The Korean-source note preserved in English says IBM Installation Manager download is available only through Internet Explorer.

The source uses WebSphere profiles. Product binary files are shared, and profile-specific environment and configuration live under `Profiles`. In the profile structure, important directories include `bin`, `config`, `configuration`, `etc`, `installableApps`, `logs`, `properties`, and `tranlog`. Resource changes made through the web console are written to `Resource.xml` under the relevant `cell`, `node`, or `server` config directory.

Start WebSphere from the current profile `bin` directory:

```text
startServer server1
```

The default server name is `server1`. Normal startup shows the server opened for e-business and prints a process ID. The management console URL is:

```text
http://SERVER_IP:9060/ibm/console
```

Stop with:

```text
stopServer server1
```

Management console port `9060` and application service port `9080` are source defaults.

Put `Altibase.jar` in:

```text
${WAS_INSTALL_ROOT}\universalDriver\lib
```

Create a JDBC Provider with:

| Field | Value |
| --- | --- |
| Database Type | `User-Defined` |
| Implementation Class Name | `Altibase.jdbc.driver.AltibaseConnectionPoolDataSource` |
| Name | `Altibase JDBC Provider` |
| Classpath | `${WAS_INSTALL_ROOT}\universalDriver\lib` path containing `Altibase.jar` |

For Altibase 6.1.1 and earlier, use `Altibase.jdbc.driver.ABConnectionPoolDataSource`.

Create a Data Source at cell scope. The source example uses data source name `altitest` and JNDI name `jdbc/altitest`. In `User Defined Properties`, set:

| Property | Example |
| --- | --- |
| `databaseName` | `mydb` |
| `serverName` | `192.168.1.35` |
| `user` | `sys` |
| `password` | `manager` |
| `portNumber` | `20911` |

Test Connection from the console. For application deployment, register a WAR through `Application -> New Application -> New Enterprise Application`, use Fast path for the test, map modules and virtual host `default_host`, specify a context root, save to master, and manually start the installed application.

The integration JSP sample looks up `jdbc/altitest`, obtains a connection, executes `select * from dual`, closes resources, and is run at:

```text
http://serverIP:applicationserviceport/contextrootname/JSPfilename
http://127.0.0.1:9080/altiweb/test.jsp
```

WebSphere does not provide Altibase-specific failover. Use Altibase JDBC failover from Altibase 5.3.3 or later:

```text
jdbc:Altibase://ServerIP:DBportnumber/DBname?AlternateServers=(ServerIP:DBportnumber)&ConnectionRetryCount=3&ConnectionRetryDelay=3&SessionFailOver=off
```

The WebSphere failover test repeatedly queries `select to_char(sysdate,'yyyy/mm/dd hh24:mi:ss') from dual`; after the local DB is terminated, the source expects failover to the `AlternateServer`.

### Spring integration

The Spring guide describes Spring Framework 3.2.x with ALTIBASE 6.3.1 and Eclipse. Use STS and Maven to build the Spring environment. The source's Maven dependency example uses `spring-context` with `3.2.xx.RELEASE`; the exact patch version must be chosen by the user.

The Altibase JDBC driver can be added to an Eclipse project through Installed JREs or placed in a web application under:

```text
Web_application\WEB-INF\lib
project\WebContent\WEB-INF\lib
```

Spring datasource options in `applicationContext.xml`:

1. `org.springframework.jdbc.datasource.DriverManagerDataSource`
2. `org.apache.commons.dbcp.BasicDataSource`
3. `Altibase.jdbc.driver.AltibaseConnectionPoolDataSource`

For `DriverManagerDataSource`, use:

```xml
<bean id="dataSource" class="org.springframework.jdbc.datasource.DriverManagerDataSource">
  <property name="driverClassName" value="Altibase.jdbc.driver.AltibaseDriver" />
  <property name="url" value="jdbc:Altibase://192.168.1.35:21129/mydb" />
  <property name="username" value="sys" />
  <property name="password" value="manager" />
</bean>
```

For DBCP, use `org.apache.commons.dbcp.BasicDataSource`; properties include `driverClassName`, `url`, `username`, `password`, `maxActive`, `initialSize`, `maxIdle`, `maxWait`, `validationQuery`, `defaultAutoCommit`, and `defaultTransactionIsolation`. Altibase's default isolation level is `READ COMMITTED`.

For Altibase's connection pool, use `Altibase.jdbc.driver.AltibaseConnectionPoolDataSource`. The driver class is automatically loaded, so `driverClassName` is not required. Use `user`, not `username`; and the source warns that the connection URL property is uppercase `URL` in the example:

```xml
<bean id="dataSource" class="Altibase.jdbc.driver.AltibaseConnectionPoolDataSource">
  <property name="URL" value="jdbc:Altibase://192.168.1.35:21129/mydb"/>
  <property name="user" value="sys"/>
  <property name="password" value="manager" />
</bean>
```

Altibase pool properties include `URL`, `user`, `password`, `maxPoolSize`, `minPoolSize`, `initialPoolSize`, `maxIdleTime`, and `propertyCycle`.

Spring failover is configured by putting Altibase failover properties in the datasource URL. The example uses DBCP:

```text
jdbc:Altibase://192.168.1.62:21020/mydb?AlternateServers=(192.168.1.146:21020)&ConnectionRetryCount=1&ConnectionRetryDelay=1&SessionFailOver=off&LoadBalance=off
```

For simultaneous Altibase versions, define separate datasource beans, one with `Altibase5.jdbc.driver.AltibaseDriver` and one with `Altibase.jdbc.driver.AltibaseDriver`, then define separate DAO beans. The example reads `accountDao1` and `accountDao2` from `applicationContext.xml`. The source says `Altibase.jar` and `Altibase5.jar` are required.

For local transactions, configure `org.springframework.jdbc.datasource.DataSourceTransactionManager` and use `org.springframework.transaction.interceptor.TransactionProxyFactoryBean`. Transaction attribute values have this source-defined form:

```text
PROPAGATION, ISOLATION_NAME, readOnly, timeout, +Exception, -Exception
```

Altibase supports `READ_COMMITTED`, `SERIALIZABLE`, and `REPETABLE_READ` as listed in the source. Preserve the source spelling `REPETABLE_READ` when quoting the source table.

For distributed transactions, the source uses `org.springframework.transaction.jta.JtaTransactionManager`, `org.springframework.transaction.jta.JotmFactoryBean`, and `Altibase.jdbc.driver.AltibaseXADataSource`. JOTM jars listed in the source include `carol-2.0.5.jar`, `connector-1_5.jar`, `howl-0.1.11.jar`, `jotm.jar`, `jta-spec1_0_1.jar`, `xapool-1.5.0.jar`, and separately `cglib-nodep-2.1.3.jar`; names may differ by downloaded JOTM version.

Spring LOB rule: Altibase LOB processing requires autocommit `false` and transaction management. Define a `TransactionManager` bean, and with declarative transaction processing use one of `PROPAGATION_REQUIRED`, `PROPAGATION_REQUIRES_NEW`, or `PROPAGATION_NESTED`. If not, LOB queries can return `null` or fail with:

```text
java.sql.SQLException: [0]:LobLocator can not span the transaction 101858625.
```

### iBATIS integration

iBATIS 2.3.4 separates SQL into XML SqlMap files and maps JavaBeans to DB tables. Older iBATIS versions required `ibatis-comm.jar` and `ibatis-sqlmap.jar`; iBATIS 2.3.4 consolidates them into `ibatis-2.3.4.x.jar`.

Create SqlMap XML files for statements and result mapping. The source examples use `Person.xml` with `resultMap`, `select`, `insert`, `update`, `delete`, and `getAllPersons`. Create `SqlMapConfigExample.xml` with `properties`, `settings`, `transactionManager type="JDBC"`, `dataSource type="SIMPLE"`, pool properties, and `sqlMap resource="Person.xml"`.

iBATIS .NET integration through ODBC uses:

```xml
<database>
  <provider name="Odbc2.0"/>
  <dataSource name="Altibase" connectionString="DSN=Altibase5;USER ID=sys;PASSWORD=manager"/>
</database>
```

For Altibase integration, define `db.properties`:

```text
driver=Altibase.jdbc.driver.AltibaseDriver
url=jdbc:Altibase://192.168.1.35:21129/mydb
username=sys
password=manager
```

Then map the values in `SqlMapConfigExample.xml`:

```xml
<property name="JDBC.Driver" value="${driver}"/>
<property name="JDBC.ConnectionURL" value="${url}"/>
<property name="JDBC.Username" value="${username}"/>
<property name="JDBC.Password" value="${password}"/>
```

iBATIS failover is configured by putting Altibase failover properties in the `url` property:

```text
url=jdbc:Altibase://192.168.6.224:21129/mydb?AlternateServers=(192.168.1.35:21129)&ConnectionRetryCount=1&ConnectionRetryDelay=1&SessionFailOver=off&LoadBalance=off
```

For simultaneous versions, use separate `SqlMapConfig` files. For Altibase 5, set:

```text
driver=Altibase5.jdbc.driver.AltibaseDriver
url=jdbc:Altibase://192.168.6.224:21129/mydb
```

For versions earlier than Altibase 5 in the source example, set:

```text
driver=Altibase.jdbc.driver.AltibaseDriver
url=jdbc:Altibase://192.168.1.35:21129/mydb
```

Load `Altibase5.jdbc.driver.AltibaseDriver` first by reading its `SqlMapConfig` first.

iBATIS procedure/function calls use `<procedure>` and parameter maps:

```xml
<procedure id="sumProc" parameterMap="ProcedureParam">
  {call sum_proc(?,?,?)}
</procedure>

<procedure id="sumFunc" parameterMap="FunctionParam">
  {call ? := sum_func(?,?)}
</procedure>
```

For iBATIS + Spring, either define the datasource in Spring and set `SqlMapClientFactoryBean` to reference it, or define the datasource in iBATIS `SqlMapConfig` and let Spring create only `SqlMapClientFactoryBean`. Required jars include `Altibase.jar`, `ibatis-2.3.4.x.jar`, `spring-jdbc.jar`, `spring-orm.jar`, `spring.jar`, and `commons-logging.jar`.

iBATIS transaction handling:

- When datasource is specified in `<transactionManager>` of `SqlMapConfig`, iBATIS calls `setAutoCommit(false)` internally during CRUD methods, commits after method termination, and returns to default autocommit.
- Direct application transaction management uses `SqlMapClient.startTransaction()`, `commitTransaction()`, and `endTransaction()`.

iBATIS LOB rule: in SqlMap parameter and result mappings, specify `jdbcType="CLOB"` or `jdbcType="BLOB"`. If not, data can be incorrectly inserted or queried due to length limits, or invalid-length errors can occur. In iBATIS alone, the datasource transaction manager disables autocommit internally; in iBATIS + Spring, define Spring transaction management for LOB.

### MyBatis integration

MyBatis supports developer-specified SQL, stored procedures, XML and annotation mapping, primitive types, `Map` interfaces, and Java POJOs. The guide uses MyBatis 3.2.8.

Differences from iBATIS:

- iBATIS can use JDK 1.4 or later; MyBatis requires JDK 1.5 or later, and MyBatis 3.2 or later requires JDK 1.6 or later.
- Package prefix changed from `com.ibatis.*` to `org.apache.ibatis.*`.
- `parameterMap` is deprecated; use `parameterType` and inline parameter options.
- Terms changed from `SqlMapConfig` to `Configuration`, and from `sqlMap` to `mapper`.
- Namespace is required in MyBatis and must use the full path, for example `com.altibase.sample.mapper.LobMapper`.

MyBatis mapper files define CRUD with `<select>`, `<insert>`, `<update>`, and `<delete>`. Configuration files define `properties`, `typeAliases`, `environments`, `transactionManager`, `dataSource`, and `mappers`.

The Altibase datasource properties in `db.properties` use:

```text
jdbc.driver=Altibase.jdbc.driver.AltibaseDriver
jdbc.url=jdbc:Altibase://192.168.1.35:36492/mydb
jdbc.username=sys
jdbc.password=manager
```

In `mybatis-config.xml`, set:

```xml
<transactionManager type="JDBC" />
<dataSource type="POOLED">
  <property name="driver" value="${jdbc.driver}" />
  <property name="url" value="${jdbc.url}" />
  <property name="username" value="${jdbc.username}" />
  <property name="password" value="${jdbc.password}" />
  <property name="poolPingQuery" value="select 1 from dual"/>
  <property name="poolMaximumActiveConnections" value="100"/>
  <property name="poolMaximumIdleConnections" value="50"/>
  <property name="poolMaximumCheckoutTime" value="20000"/>
</dataSource>
```

MyBatis uses `SqlSessionFactoryBuilder`, `SqlSessionFactory`, and `SqlSession`. The source example opens the session with:

```java
sqlSession = sqlSessionFactory.openSession(false);
```

The Boolean argument controls autocommit; `false` sets autocommit false.

MyBatis failover extends the Altibase JDBC URL with:

```text
AlternateServers=(192.168.1.35:21129)
ConnectionRetryCount=1
ConnectionRetryDelay=1
SessionFailOver=off
LoadBalance=off
Healthcheckduration=10
Failover_source=MESSAGE
```

`Healthcheckduration` controls when a failed server is re-added to the `AlternativeServer` list after failover. `Failover_source` sends a description stored in `V$SESSION.FAILOVER_SOURCE`.

For simultaneous versions, MyBatis can define multiple `<environment>` entries in one configuration and select one by environment id when building `SqlSessionFactory`. The source still requires `Altibase5.jdbc.driver.AltibaseDriver` to load before `Altibase.jdbc.driver.AltibaseDriver`. The example uses environment ids `release` and `development`.

Procedure/function calls require `statementType="CALLABLE"` because the old iBATIS `<procedure>` tag and `<parameterMap>` are not used. Procedure call form:

```xml
<select id="testSelectProc" statementType="CALLABLE" parameterType="INTEGER" resultType="User">
  { call PROC_SEL_TEST(
    #{userNo,mode=IN,jdbcType=INTEGER,javaType=INTEGER}
  ) }
</select>
```

Function call form:

```xml
<select id="testSelectFunc" statementType="CALLABLE" parameterType="map" resultType="INTEGER">
  { call #{resNum,mode=OUT,jdbcType=INTEGER,javaType=INTEGER} := SUM_FUNC(
    #{Num1,mode=IN,jdbcType=INTEGER,javaType=INTEGER},
    #{Num2,mode=IN,jdbcType=INTEGER,javaType=INTEGER}
  ) }
</select>
```

For MyBatis + Spring, define:

- `SqlSessionFactoryBean`
- `DataSourceTransactionManager`
- datasource bean
- mapper interface/mapper XML, usually with `MapperScannerConfigurer`

`mybatis-spring-1.x.x.jar` requires Java 1.5 or higher. Source compatibility table:

| MyBatis-Spring module | MyBatis | Spring |
| --- | --- | --- |
| `1.0.0` and `1.0.1` | `3.0.1` to `3.0.5` | `3.0.0` or higher |
| `1.0.2` | `3.0.6` | `3.0.0` or higher |
| `1.1.0` or higher | `3.1.0` or higher | `3.0.0` or higher |

Spring-MyBatis can use either `Altibase.jdbc.driver.AltibaseConnectionPoolDataSource` with `URL`, `user`, and `password`, or Apache DBCP `org.apache.commons.dbcp.BasicDataSource` with `driverClassName`, `url`, `username`, `password`, `initialSize`, `minIdle`, `maxIdle`, `maxActive`, and `validationQuery`.

MyBatis LOB rule: specify `jdbcType=BLOB` and `jdbcType=CLOB` inline in mapped columns. MyBatis defaults autocommit to true, so set autocommit false when obtaining the session. Without autocommit false, Altibase can raise:

```text
java.sql.SQLException: [0]:LobLocator can not span the transaction 101858625.
```

MyBatis duplicate insert caution: if `useGeneratedKeys` is set to `true` in the MyBatis configuration XML, duplicate insert-query behavior can occur in Altibase. The source says to set it to `false`. The default value is `false`.

### Hibernate integration

Hibernate uses `hibernate-configuration` XML for connection/dialect settings and `hibernate-mapping` XML for Java object to table mapping. The source sample maps `examples.domain.Person` to `person`, uses sequence `PERSON_SEQ`, and uses `SessionFactory`, `Session`, `Transaction`, and `Criteria`.

Hibernate does not provide an Altibase dialect by default. Add Altibase dialect classes to the Hibernate jar:

```bash
mv hibernate-core-x.x.x.Final.jar to-the-java-file-directory
cd to-the-java-file-directory
jar xvf hibernate-core-x.x.x.Final.jar
mv Altibase*.java to-the-java-file-directory
javac -d . -cp . AltibaseLimitHandler.java
javac -d . -cp . AltibaseDialect.java
javac -d . -cp . SequenceInformationExtractorAltibaseDatabaseImpl.java
jar -cvfm hibernate-core-x.x.x.Final.jar META-INF/MANIFEST.MF .
```

Altibase dialect source reference:

```text
https://github.com/ALTIBASE/hibernate-orm/blob/master/ALTIBASE_DIALECT_PORTING.md
```

The Hibernate Altibase configuration properties are:

```xml
<property name="connection.driver_class">Altibase.jdbc.driver.AltibaseDriver</property>
<property name="connection.url">jdbc:Altibase://192.168.1.35:20300/mydb</property>
<property name="connection.username">sys</property>
<property name="connection.password">manager</property>
<property name="connection.pool_size">1</property>
<property name="dialect">org.hibernate.dialect.AltibaseDialect</property>
<property name="current_session_context_class">thread</property>
<property name="show_sql">true</property>
<mapping resource="Person.hbm.xml"/>
```

Hibernate failover is configured in `connection.url`:

```text
jdbc:Altibase://192.168.1.35:20300/mydb?AlternateServers=(127.0.0.1:20300)&ConnectionRetryCount=1&ConnectionRetryDelay=1&SessionFailOver=off&LoadBalance=off
```

For simultaneous Altibase versions, create separate Hibernate configuration files, for example `Hibernate.Altibase5.cfg.xml` using `Altibase5.jdbc.driver.AltibaseDriver` and `Hibernate.Altibase7.cfg.xml` using `Altibase.jdbc.driver.AltibaseDriver`. The application must build the `SessionFactory` for `Hibernate.Altibase5.cfg.xml` first so the Altibase 5 driver class is loaded first.

Hibernate + Spring supports two integration styles:

1. Define a Spring `dataSource`, set `LocalSessionFactoryBean`, `mappingResources`, `hibernateProperties`, and DAO beans with `sessionFactory`.
2. Put connection properties directly in `hibernateProperties` on `LocalSessionFactoryBean`.

Altibase's connection pool can be used with Hibernate only when integrating with Spring. The source example uses `Altibase.jdbc.driver.ABConnectionPoolDataSource` with `url`, `user`, and `password`.

Hibernate transaction rule: call `Session.beginTransaction()`, then call `Transaction.commit()` or `rollback()`. `beginTransaction()` calls `setAutoCommit(false)` and holds the transaction.

Hibernate LOB rule:

- For CLOB, map with `type="org.hibernate.type.StringClobType"` and `sql-type="clob"`.
- For BLOB, map with `type="org.hibernate.type.PrimitiveByteArrayBlobType"` and `sql-type="blob"`.
- Call `beginTransaction()` before LOB work. In Hibernate + Spring, the source recommends calling `beginTransaction()` in the Java application because autocommit false may not apply even when Spring manages the transaction.

If `beginTransaction()` is not called, LOB select can return `null` or raise `LobLocator can not span the transaction 101858625`; LOB insert can raise:

```text
java.sql.SQLException: [0]: Connection is in autocommit mode. One can not operate on LOB datas with autocommit mode on.
```

Hibernate stored procedure/function calls are not supported directly in the source. Obtain a JDBC `Connection` from `Session` and use `CallableStatement`:

```java
String sql1 = "{call sum_proc(?,?,?)}";
CallableStatement altibaseStatement1 = con.prepareCall(sql1);
altibaseStatement1.setInt(1,10);
altibaseStatement1.setInt(2,20);
altibaseStatement1.registerOutParameter(3,java.sql.Types.NUMERIC);
altibaseStatement1.execute();

String sql2 = "{call ? := sum_func(?,?)}";
CallableStatement altibaseStatement2 = con.prepareCall(sql2);
altibaseStatement2.registerOutParameter(1,java.sql.Types.NUMERIC);
altibaseStatement2.setInt(2,10);
altibaseStatement2.setInt(3,20);
altibaseStatement2.execute();
```

For Altibase-specific SQL such as `MOVE`, define a named native SQL query in the mapping file and execute it through `session.getNamedQuery()`:

```xml
<sql-query name="nativeSQLMove">
  <![CDATA[
    MOVE INTO t2 (c1,c2,c3)
    FROM t1(c1,c2,c3)
  ]]>
</sql-query>
```

## SQL, commands, and configuration

### Common failover properties

| Property | Meaning |
| --- | --- |
| `AlternateServer` or `AlternateServers` | Alternate servers to connect to when failure occurs. Source examples use both names; preserve the form shown by the source or driver manual being followed. |
| `ConnectionRetryCount` | Number of retry attempts when an alternate server connection fails. |
| `ConnectionRetryDelay` | Seconds to wait before retrying an alternate server connection. |
| `LoadBalance` | `on` randomly selects from primary and alternate servers on first connection; `off` uses the default server first, then `AlternateServer`. |
| `SessionFailOver` | `on` enables STF; `off` uses CTF. STF reconnects and restores session properties, but failed transactions must be reprocessed by the application. |
| `Healthcheckduration` | MyBatis source property controlling when a failed server is re-added to the alternate list after failover. |
| `Failover_source` | MyBatis source property recorded in `V$SESSION.FAILOVER_SOURCE`. |

### Common validation commands

```bash
java -jar Altibase.jar
altibase -v
isql -s 127.0.0.1 -u sys -p manager -port 20300
```

```sql
select comm_name, client_type, db_username, id session_id from v$session;
select db_name, product_signature from v$database;
select to_char(sysdate,'yyyy/mm/dd hh24:mi:ss') from dual;
select 1 from dual;
```

### Common datasource classes

```text
Altibase.jdbc.driver.AltibaseDriver
Altibase.jdbc.driver.AltibaseConnectionPoolDataSource
Altibase.jdbc.driver.ABConnectionPoolDataSource
Altibase.jdbc.driver.AltibaseXADataSource
Altibase.jdbc.driver.ABXADataSource
jeus.jdbc.driver.blackbox.BlackboxConnectionPoolDataSource
org.springframework.jdbc.datasource.DriverManagerDataSource
org.apache.commons.dbcp.BasicDataSource
org.springframework.jdbc.datasource.DataSourceTransactionManager
org.springframework.transaction.jta.JtaTransactionManager
org.mybatis.spring.SqlSessionFactoryBean
org.mybatis.spring.mapper.MapperScannerConfigurer
org.springframework.orm.hibernate3.LocalSessionFactoryBean
org.hibernate.dialect.AltibaseDialect
```

## Validation and troubleshooting

| Symptom or message | Likely cause and action |
| --- | --- |
| Tomcat `No suitable driver` | URL starts with the wrong protocol such as `jdbc:mysql://...`; use `jdbc:Altibase://...` and ensure `Altibase.jar` is visible. |
| Tomcat `Communication link failure` | Altibase server is down, JDBC driver/server versions are incompatible, or IP/`PORT_NO` in the URL is wrong. |
| Tomcat `client unable to establish a connection` or driver class null after context changes | Delete the web application `name.xml` file under `$CATALINA_HOME/conf/catalina` so the changed `context.xml` is reloaded. |
| Tomcat `Failure to find statement` with DBCP prepared statements | Review JDK/JRE version, `testOnBorrow`, and `poolPrepareStatements`; JDK/JRE 1.6 or later is recommended when changing these settings. |
| JEUS `ClassNotFoundException` for Altibase datasource class | Check whether the class name matches the Altibase version: `ABConnectionPoolDataSource` for ALTIBASE 6.1.1 or lower and `AltibaseConnectionPoolDataSource` for ALTIBASE 6.3.1 or later. |
| JEUS `NoSuchMethodException ... setURL` | Use the correct `URL` or `Url` property spelling for the driver version. |
| JEUS lock with `initialPoolSize` | Avoid `initialPoolSize` with `AltibaseConnectionPoolDataSource`; use `maxPoolSize`. |
| JBoss `Address already in use /127.0.0.1:8080` | Change the HTTP connector port in `JBOSS_HOME/server/default/deploy/jbossweb.sar/server.xml`. |
| WebLogic `Cannot load driver` | Configure `Altibase.jar` in `$DOMAIN_HOME/lib` or `CLASSPATH` and restart. |
| WebLogic `Invalid Altibase URL` or `No suitable driver` | Check URL format and ensure the JDBC item is `Altibase`. |
| WebLogic `Could not create pool connection` | Check connection pool fields; for ALTIBASE 4, source says enter user as `user=sys` in Property. |
| WebLogic hang | Can occur when JDBC driver `CMP` and server `cm protocol version` differ; restart WebLogic instances and align driver/server compatibility. |
| Spring, iBATIS, MyBatis, Hibernate LOB errors | Set autocommit false and manage transactions; for mapping frameworks also declare `CLOB`/`BLOB` mapping where required. |
| MyBatis duplicate insert query with `useGeneratedKeys=true` | Set `useGeneratedKeys` to `false`; default is `false`. |

## Version-specific notes

- Altibase failover is available starting from Altibase 5.3.3 in the Tomcat, JBoss, WebSphere, Spring, iBATIS, MyBatis, and Hibernate source examples.
- JEUS uses `ABConnectionPoolDataSource` for ALTIBASE 6.1.1 or earlier and `AltibaseConnectionPoolDataSource` for ALTIBASE 6.3.1 or later.
- WebSphere uses `AltibaseConnectionPoolDataSource`, but for Altibase 6.1.1 and earlier it requires `ABConnectionPoolDataSource`.
- MyBatis 3.2 or later requires JDK 1.6 or later; older iBATIS supports JDK 1.4 or later.
- WebLogic JDBC 3.0 cautions matter for Altibase 5 drivers built on JDK 1.4.
- For multi-version JDBC loading in iBATIS, MyBatis, Hibernate, and WebLogic, load or configure the major-version-specific driver first when the source requires it, especially `Altibase5.jdbc.driver.AltibaseDriver`.

## Related errors

Exact error and warning strings preserved in this R019 source set include:

```text
java.sql.SQLException: No suitable driver
java.sql.SQLException: Communication link failure
Failure to find statement
java.lang.UnsatisfiedLinkError: ... libRunner.so ...
version `GLIBC_2.4' not found
java.lang.ClassNotFoundException: Altibase.jdbc.driver.ABConnectionPoolDataSource
java.lang.ClassNotFoundException: Altibase.jdbc.driverAltibaseConnectionPoolDataSource
java.lang.NoSuchMethodException: Altibase.jdbc.driver.ABConnectionPoolDataSource.setURL(java.lang.String)
java.net.BindException: Address already in use /127.0.0.1:8080
java.sql.SQLException: [0]:LobLocator can not span the transaction 101858625.
java.sql.SQLException: [0]: Connection is in autocommit mode. One can not operate on LOB datas with autocommit mode on.
```

## Attachments and external references

Document-format attachments preserved from Korean source evidence:

- Tomcat guide PDF: `https://docs.altibase.com/download/attachments/7341030/ALTIBASE_TOMCAT%EC%97%B0%EB%8F%99_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1417566911000&api=v2`
- Tomcat 5.5 guide PDF: `https://docs.altibase.com/download/attachments/7341030/ALTIBASE_TOMCAT_%EC%97%B0%EB%8F%99_%EA%B0%80%EC%9D%B4%EB%93%9C_5.5.pdf?version=1&modificationDate=1417599249000&api=v2`
- JEUS guide PDF: `https://docs.altibase.com/download/attachments/7341028/ALTIBASE_JEUS_%EC%97%B0%EB%8F%99_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1417566887000&api=v2`
- JEUS 6.0 guide PDF: `https://docs.altibase.com/download/attachments/7341028/ALTIBASE_JEUS_%EC%97%B0%EB%8F%99_%EA%B0%80%EC%9D%B4%EB%93%9C_6.0.pdf?version=1&modificationDate=1417651669000&api=v2`
- WebLogic 12c guide PDF: `https://docs.altibase.com/download/attachments/7340101/ALTIBASE_WebLogic_%EC%97%B0%EB%8F%99_%EA%B0%80%EC%9D%B4%EB%93%9C_12c.pdf?version=1&modificationDate=1417567027000&api=v2`
- WebLogic 10.3 guide PDF: `https://docs.altibase.com/download/attachments/7340101/ALTIBASE_WebLogic_%EC%97%B0%EB%8F%99_%EA%B0%80%EC%9D%B4%EB%93%9C_10.3.pdf?version=1&modificationDate=1417591117000&api=v2`
- WebSphere guide PDF: `https://docs.altibase.com/download/attachments/13435602/ALTIBASE_Websphere_%EC%97%B0%EB%8F%99%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1698197781000&api=v2`
- Spring guide PDF: `https://docs.altibase.com/download/attachments/7340945/ALTIBASE_Spring_%EC%97%B0%EB%8F%99%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1417566993000&api=v2`
- Spring 2.5 guide PDF: `https://docs.altibase.com/download/attachments/7340945/ALTIBASE_Spring_%EC%97%B0%EB%8F%99%EA%B0%80%EC%9D%B4%EB%93%9C_2.5.pdf?version=1&modificationDate=1417598735000&api=v2`
- iBATIS guide PDF: `https://docs.altibase.com/download/attachments/7340053/ALTIBASE_iBATIS_%EC%97%B0%EB%8F%99%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1417566939000&api=v2`
- MyBatis guide PDF: `https://docs.altibase.com/download/attachments/7340818/ALTIBASE_MyBatis_%EC%97%B0%EB%8F%99%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1417566977000&api=v2`
- Hibernate guide PDF: `https://docs.altibase.com/download/attachments/14057878/ALTIBASE_Hibernate_%EC%97%B0%EB%8F%99%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1698369532000&api=v2`

Legacy no-downloadable-URL source limitations:

- JEUS Korean source legacy UI hash labels: `연결풀`, `고급 선택사항`, `File`, `New`, `Project`, `Web`, `Export`.
- Hibernate Korean source legacy reference label: `JAVA 개발 가이드`.
- MyBatis Korean source legacy hash labels `0` in LobLocator SQLException examples.

External references preserved by the source set include:

- `http://support.altibase.com`
- `http://tomcat.apache.org/download-70.cgi`
- `http://tomcat.apache.org/tomcat-5.5-doc/config/valve.html`
- `http://www.jboss.org/jbossas/downloads`
- `http://docs.oracle.com/middleware/1213/wls/index.html`
- `http://www.oracle.com/technetwork/middleware/downloads/index.html`
- `http://www.ibm.com/software/repositorymanager/V9WASBase`
- `http://www.ibm.com/software/repositorymanager/V9WASND`
- `http://ibatis.apache.org`
- `http://ibatis.apache.org/java.cgi`
- `http://blog.mybatis.org/`
- `http://mybatis.github.io/mybatis-3/`
- `http://mybatis.github.io/mybatis-3/ko/`
- `http://repo1.maven.org/maven2/org/mybatis/mybatis/3.2.8/`
- `http://hibernate.org/orm/releases/5.4`
- `https://github.com/ALTIBASE/hibernate-orm/blob/master/ALTIBASE_DIALECT_PORTING.md`
- `http://forge.ow2.org/projects/jotm/`
- `http://maven.apache.org/download.html`

## Terminology

| Term | Preserve as | Meaning in this document |
| --- | --- | --- |
| Connection Time Fail-Over | `CTF` | Failure recognized at connection time; the client connects to another available node. |
| Service Time Fail-Over | `STF` | Failure occurs after connection; the client reconnects and restores session properties, but failed transactions must be retried by the application. |
| JNDI | `JNDI` | Java lookup mechanism used by Tomcat, JEUS, JBoss, WebLogic, WebSphere, and sample JSPs. |
| DBCP | `DBCP` | Apache/Jakarta database connection pool used in Tomcat and Spring examples. |
| XA | `XA`, `XADataSource` | Distributed/global transaction datasource. |
| Local XA | `LocalXADataSource` | JEUS local transaction emulation for XA participation, with recovery limitations. |
| SqlMap | `SqlMap` | iBATIS SQL mapping XML. |
| Mapper | `Mapper` | MyBatis SQL mapping XML or mapper interface. |
| SessionFactory | `SessionFactory` | Hibernate object used to open sessions. |
| AltibaseDialect | `org.hibernate.dialect.AltibaseDialect` | Hibernate dialect class required for Altibase-specific SQL. |
| LobLocator | `LobLocator` | Altibase LOB locator; must not span transaction boundaries without proper transaction handling. |
