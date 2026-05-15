---
title: "How to change the jdbc.trc file creation location"
page_id: "16876175"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/How+to+change+the+jdbc.trc+file+creation+location"
updated_at: "2021-04-05T09:53:11.000+0900"
version: 3
ancestors: ["Home", "07. Development and API", "JDBC"]
labels: []
---

# How to change the jdbc.trc file creation location
Source: https://docs.altibase.com/display/FAQE/How+to+change+the+jdbc.trc+file+creation+location
Updated: 2021-04-05T09:53:11.000+0900

- [Creation time and usage](#Howtochangethejdbc.trcfilecreationlocation-Creationtimeandusage) - [Version](#Howtochangethejdbc.trcfilecreationlocation-Version) - [Creation location](#Howtochangethejdbc.trcfilecreationlocation-Creationlocation) - [How to change the creation path](#Howtochangethejdbc.trcfilecreationlocation-Howtochangethecreationpath)

# Creation time and usage

---

The jdbc.trc file is a log file created for JDBC-related traces, and is automatically generated when the JDBC driver is initialized.

If fail-over is specified in the connection URL, it is also used for event trace when fail-over occurs.

If fail-over is not specified in the connection url, or fail-over does not occur, it is 0 byte to the default value.

File size varies slightly from platform to platform.

When one Java program is executed at the same time, as many as the number of executions are created,

jdbc.trc jdbc.trc.lck jdbc.trc.1 jdbc.trc.1.lck jdbc.trc.2 jdbc.trc.2.lck

When connecting each connection object separately in a single Java program, the jdbc.trc file is shared and used.

# Version

---

The jdbc.trc file is created for JDBC-related traces from ALTIBASE HDB version 5.5.1 or later.

# Creation location

---

If the ALTIBASE_HOME environment variable is set in the client environment, it is created in **$ALTIBASE_HOME/trc**, If the ALTIBASE_HOME environment variable is not set, it is created in the location **where the Java program is executed.**

Sometimes, if the user does not have write permission in the directory where the jdbc.trc file is created, the following error may occur in the application due to file creation failure.

[java.io](http://java.io).IOException: Couldn't get lock for /opt/altibase-HDB-server-6.1.1/trc/jdbc.trc

If the above error occurs, give permission to the directory or set the ALTIBASE_HOME environment variable to an appropriate location.

# How to change the creation path

---

| ALTIBASE HDB Version | How to change the jdbc.trc log creation location |
| --- | --- |
| version 6.1.1.1.3 or earlier | Not available |
| version 6.1.1.1.4 ~ 6.1.1.1.7 | Can be set as an option when running java<br>java -D**ALTIBASE_JDBC_TRCLOG_DISABLE=true** |
| version 6.1.1.1.8 or later | Set option when running java<br>java -D**ALTIBASE_JDBC_TRCLOG_DISABLE=true**<br>Or<br>Set as an environment variable of the java execution user<br>export **ALTIBASE_JDBC_TRCLOG_DISABLE=true** |
