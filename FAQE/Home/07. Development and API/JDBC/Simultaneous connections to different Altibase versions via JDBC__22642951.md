---
title: "Simultaneous connections to different Altibase versions via JDBC"
page_id: "22642951"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Simultaneous+connections+to+different+Altibase+versions+via+JDBC"
updated_at: "2025-10-20T15:29:01.000+0900"
version: 1
ancestors: ["Home", "07. Development and API", "JDBC"]
labels: []
---

# Simultaneous connections to different Altibase versions via JDBC
Source: https://docs.altibase.com/display/FAQE/Simultaneous+connections+to+different+Altibase+versions+via+JDBC
Updated: 2025-10-20T15:29:01.000+0900

- [Overview](#SimultaneousconnectionstodifferentAltibaseversionsviaJDBC-Overview) - [Driver location](#SimultaneousconnectionstodifferentAltibaseversionsviaJDBC-Driverlocation) - [Version check](#SimultaneousconnectionstodifferentAltibaseversionsviaJDBC-Versioncheck) - [Usage example](#SimultaneousconnectionstodifferentAltibaseversionsviaJDBC-Usageexample)

# Overview

---

This document explains how to connect to different versions of Altibase using the Altibase JDBC Driver.

Altibase provides additional JDBC drivers to enable connections to different Altibase versions. This explanation is based on Altibase version 7.3, and the additional driver file provided in version 7.3 is Altibase7_3.jar.

In the application, when loading the driver class using the `Class.forName()` method, you can connect to different Altibase versions by specifying the class names separately as:

- `Altibase.jdbc.driver.AltibaseDriver`
- `Altibase7_3.jdbc.driver.AltibaseDriver`

This allows simultaneous connections to different Altibase versions.

# Driver location

---

The driver is located in `$ALTIBASE_HOME/lib`, and for version 7.3, the file name is `Altibase7_3.jar`.

```
$ ls -al
-rw-rw-rw- 1 altibase altibase  509530 Apr 20 11:10 Altibase7_3.jar
-rw-rw-rw- 1 altibase altibase  506968 Apr 20 11:10 Altibase.jar
```

# Version check

---

Check the driver for connecting to other versions

```
$ java -jar Altibase7_3.jar
Altibase 7.3.0.1.0 with CMP 7.1.8 for JDBC 4.2 compiled with JDK 8
```

# Usage example

---

The example explains simultaneous connections to versions 7.1 and 7.3.

Use the `Altibase.jar` file from version 7.1 located at `$ALTIBASE_HOME/lib/` and the `Altibase7_3.jar` file from version 7.3 located at `$ALTIBASE_HOME/lib/`.

```
// - AltibaseMultiversionConnection.java file
// ALTIBASE 7.3 Driver class - using Altibase7_3.jar file
Class.forName("Altibase7_3.jdbc.driver.AltibaseDriver");
// ALTIBASE 7.1 Driver class - using Altibase.jar file
Class.forName("Altibase.jdbc.driver.AltibaseDriver");
// ALTIBASE 7.3 version URL
String db_url1 = "jdbc:Altibase://192.168.1.111:20300/mydb";
// ALTIBASE 7.1 version URL
String db_url2 = "jdbc:Altibase://192.168.1.222:20300/mydb";
```
