---
title: "How to use Fail-Over in Altibase JDBC"
page_id: "16876173"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/How+to+use+Fail-Over+in+Altibase+JDBC"
updated_at: "2021-03-22T11:22:23.000+0900"
version: 1
ancestors: ["Home", "07. Development and API", "JDBC"]
labels: []
---

# How to use Fail-Over in Altibase JDBC
Source: https://docs.altibase.com/display/FAQE/How+to+use+Fail-Over+in+Altibase+JDBC
Updated: 2021-03-22T11:22:23.000+0900

**- [Overview](#HowtouseFail-OverinAltibaseJDBC-Overview) - [Glossary of terms](#HowtouseFail-OverinAltibaseJDBC-Glossaryofterms) - [Fail-over related connection properties](#HowtouseFail-OverinAltibaseJDBC-Fail-overrelatedconnectionproperties) - [Checking whether Fail-Over succeeded](#HowtouseFail-OverinAltibaseJDBC-CheckingwhetherFail-Oversucceeded) - [Example](#HowtouseFail-OverinAltibaseJDBC-Example) - [Reference](#HowtouseFail-OverinAltibaseJDBC-Reference)**

# Overview

---

Altibase provides Fail-Over functionality so that services can continue when a failure occurs while operating a database system.

This section describes the functions and usage of Altibase JDBC Fail-Over.

# Glossary of terms

---

- CTF (Connection Time Fail-Over): When a failure is detected while connecting to the DBMS, this means retrying the connection to the DBMS of another available node.
    - If the AlternateServer property is set in the Connection String, CTF operates by default.
    - An application usually should try to connect again.
    - In the form of maintaining a connection pool like WAS, it can be performed automatically through the connection validation setting of WAS.
- STF (Service Time Fail-Over): When a failure is detected while the DBMS is processing a client's request, this refers to reconnecting to the DBMS of another available node.
    - Since the success or failure is returned as an error after executing only the connection, user coding to proceed from the preparation of the statement again must be followed.
- Primary Server: This refers to the server information specified at the first in the Connection URL.
- Alternative Server: This refers to the information of servers specified in AlternateServer connection properties.
- Explicit Connection: This refers to when calling the connect method of the Connection object.
- Implicit Connection: This refers to when the connect method fails or STF occurs, and JDBC internally retries the connection to the DBMS of another available node.

# Fail-over related connection properties

---

*** Case insensitive.**

- AlternateServer: It refers to alternate servers and is described in (IP1:Port1, IP2:Port2,...) format.
    - Alternate servers can be the connection target server in the following cases depending on the settings of LoadBalance and SessionFailOver.
          - When calling the connect method
          - When attempting to reconnect due to a failure of the connect method
          - When attempting to reconnect due to STF occurrence
- ConnectionRetryCount: Set the number of retry attempts to connect to the same server.
- ConnectionRetryDelay: Waiting time for connection attempts to the same server. The unit is seconds.
  Note) ConnectionRetryCount and ConnectionRetryDelay properties are applied only for internal connection, and if it fails after executing ConnectionRetryCount * ConnectionRetryDelay, it tries to connect to another available server in the same way.
- LoadBalance: When connecting to DBMS, set the order of connection attempts between the primary server and the alternate server.
    - When set to ON, it tries to connect randomly between the default server and the alternate server.
    - If it is set to OFF, it tries to connect from the primary server, and if it fails, it tries to connect to the alternate server in the order listed.
    - This setting is for both explicit and internal connections.
- SessionFailOver: Whether to perform STF or not.
    - When set to ON, it operates as CTF+STF.
    - When set to OFF, only CTF operates.
- FailOver_Source: When performing a failover, specify the description of the failover source delivered to the server. This information is stored in the FAILOVER_SOURCE column of the V$SESSION performance view.
- HealthCheckDuration: Altibase JDBC maintains a list of available servers for failover. Upon failover, it tries to reconnect to the servers in the available server list. This is to prevent all servers from attempting to connect in an infinite loop in a failure situation.
    - The HealthCheckDuration property specifies the wait time for the server on which the failover occurred to be set back to the list of available servers.
    - When a failover occurs, the server is removed from the list of available servers and added back to the list of available servers after the HealthCheckDuration time elapses. The unit of this property is seconds.

# Checking whether Fail-Over succeeded

---

- CTF: Success can be checked immediately by whether the database connection is established.
- STF: Success can be checked through exception handling. If `SQLException.getSQLState()` returns `08F01` for Altibase 6.3.1 or later, or `ES_08FO01` for Altibase 6.1.1 or earlier, Fail-Over succeeded.

# Example

---

When writing a program, refer to the following example.

```java
import Altibase.jdbc.driver.*;
import Altibase.jdbc.driver.ex.*;
import java.util.Properties;
import java.sql.*;
import java.io.*;

class FailOverSampleSTF {
    public static void main(String args[]) throws Exception {
        //---------------------------------------------------
        // Initialization
        //---------------------------------------------------
        String sURL = "jdbc:Altibase://127.0.0.1:" + args[0]
                    + "/mydb?AlternateServers=(128.1.3.52:20300,128.1.3.53:20300)"
                    + "&ConnectionRetryCount=3&ConnectionRetryDelay=10"
                    + "&SessionFailOver=on&LoadBalance=off";

        try {
            Class.forName("Altibase.jdbc.driver.AltibaseDriver");
        } catch (Exception e) {
            System.err.println("Can't register Altibase Driver\n");
            return;
        }

        //---------------------------------------------------
        // Test Body
        //---------------------------------------------------
        Properties sProp = new Properties();
        Connection sCon;
        PreparedStatement sStmt = null;
        ResultSet sRes = null;

        sProp.put("user", "SYS");
        sProp.put("password", "MANAGER");

        sCon = DriverManager.getConnection(sURL, sProp);
        sStmt = sCon.prepareStatement("SELECT C1 FROM T2 ORDER BY C1");

        while (true) {
            try {
                sRes = sStmt.executeQuery();
                while (sRes.next()) {
                    System.out.println("VALUE : " + sRes.getString(1));
                }
            } catch (SQLException e) {
                // Check Fail-Over.
                // if (e.getSQLState().equals("ES_08FO01")) // 6.1.1 or earlier
                if (e.getSQLState().equals("08F01")) {      // 6.3.1 or later
                    // Prepare again after Fail-Over occurs.
                    sStmt = sCon.prepareStatement("SELECT * FROM tb_test1");
                    continue;
                }
                System.out.println("EXCEPTION : " + e.getMessage());
                break;
            }
            break;
        }

        sRes.close();

        //---------------------------------------------------
        // Finalize
        //---------------------------------------------------
        sStmt.close();
        sCon.close();
    }
}
```

# Reference

---

- Replication Manual -> Chapter 4 FailOver
- JDBC User's Manual

    - Chapter 1 Getting Started with JDBC -> Connection Information
    - Chapter 3 Advanced Features -> JDBC and FailOver
- [JBOSS Integration Guide for Altibase](https://aid.altibase.com/display/arch/JBOSS+Integration+Guide+for+Altibase)
