---
title: "Altibase Server Configuration for IPC Communication"
page_id: "22642933"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Altibase+Server+Configuration+for+IPC+Communication"
updated_at: "2025-10-20T15:16:57.068+0900"
version: 1
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# Altibase Server Configuration for IPC Communication
Source: https://docs.altibase.com/display/FAQE/Altibase+Server+Configuration+for+IPC+Communication
Updated: 2025-10-20T15:16:57.068+0900

- [Overview](#AltibaseServerConfigurationforIPCCommunication-Overview) - [Version](#AltibaseServerConfigurationforIPCCommunication-Version) - [ALTIBASE HDB Server Configurations](#AltibaseServerConfigurationforIPCCommunication-ALTIBASEHDBServerConfigurations) - [OS Configurations](#AltibaseServerConfigurationforIPCCommunication-OSConfigurations) - [How the application communicates](#AltibaseServerConfigurationforIPCCommunication-Howtheapplicationcommunicates)

# Overview

---

ALTIBASE HDB provides the following communication methods between the database server and clients. Among these, this document describes the ALTIBASE HDB and OS configurations required for IPC communication.

- TCP/IP
- IPC using Unix Domain Socket (UDS)
- IPC using shared memory
- IPCDA (supported from ALTIBASE HDB 7.1.0)
- SSL/TLS (supported from ALTIBASE HDB version 6.5.1)

For a description of each communication method, please refer to the "12. Server/Client Communication" section from the Administrator's manual.

Manual Page:

- [https://github.com/ALTIBASE/Documents/tree/master/Manuals](https://github.com/ALTIBASE/Documents/tree/master/Manuals)
- [http://support.altibase.com/en/manual](http://support.altibase.com/en/manual)

# Version

---

All ALTIBASE HDB versions

# ALTIBASE HDB Server Configurations

---

By default, the Altibase server does not allow IPC access. So, in order to connect to the Altibase server with the IPC connection type, the Altibase server properties must be changed.

Related properties cannot be changed while the Altibase server is running. Therefore, the Altibase server needs to be restarted in order to change the property value.

### IPC_PORT_NO

This property is required when running an Altibase server on a Windows system.

Unix and Linux use the 'Unix domain socket' in the form of a file for IPC connection, but Windows does not support this, so a TCP port is required for IPC connection.

In Windows, IPC connections communicate using shared memory, semaphores, and mutexes over TCP connections.

### IPC_CHANNEL_COUNT

This property configures the maximum number of IPC sessions that can be connected to the Altibase server. The default value is 0, and the Altibase server is configured not to allow IPC access.

### IPC_FILEPATH

IPC communicates with the ALTIBASE HDB server with the 'Unix domain socket' in the form of a file.

If the 'Unix domain socket' file does not exist or the path is set incorrectly, the connection will fail.

Starting from ALTIBASE HDB server version 5.5.1.4.2, the user can change this path arbitrarily with the IPC_FILEPATH property, and the setting value can be checked in the performance view.

```
SELECT NAME, MEMORY_VALUE1 FROM X$PROPERTY WHERE NAME = 'IPC_FILEPATH';
```

ALTIBASE HDB server versions prior to 5.5.1.4.2 cannot change the default path and do not provide a separate verification method.

- The default setting of ALTIBASE HDB server version 4.3.9
  The location and name of the Unix domain socket file is $ALTIBASE_HOME/trc/alti-ipc.
- The default setting of ALTIBASE HDB server versions later than 4.3.9 and earlier than 5.5.1.4.2
  The location and name of the Unix domain socket file is $ALTIBASE_HOME/trc/cm-ipc.

### How to change properties

1. Changing altibase.properties file Change the required values among the properties described above in the $ALTIBASE_HOME/conf/altibase.properties file and save the altibase.properties file.

  ```
  $ cd $ALTIBASE_HOME/conf
  $ vi altibase.properties
  ```
2. Restarting ALTIBASE HDB Restart the Altibase server to reflect the changed property values to the Altibase server.

  ```
  $ server restart
  ```
3. Checking properties Check that the values have been properly reflected.

  ```
  $ is
  iSQL> SELECT NAME, MEMORY_VALUE1 FROM X$PROPERTY WHERE NAME IN ('IPC_FILEPATH', 'IPC_CHANNEL_COUNT');
  ```
4. Testing IPC connection Try to test the iSQL connection with the IPC type.

  ```
  $ export ISQL_CONNECTION=IPC                                                # Change the environment variable that sets the iSQL connection type.
  $ is
  -----------------------------------------------------------------
       Altibase Client Query utility.
       Release Version 7.1.0.6.5
       Copyright 2000, ALTIBASE Corporation or its subsidiaries.
       All Rights Reserved.
  -----------------------------------------------------------------
  ISQL_CONNECTION = IPC, SERVER = localhost                                  # IPC connection succeeds when ISQL_CONNECTION = IPC appears and the iSQL prompt is displayed.
  iSQL>
  ```

# OS Configurations

---

Shared memory and semaphore resources are used for IPC communication. Therefore, to use the IPC type, the related kernel parameters must be set.

Please refer to the documents below depending on the OS. There are no recommended configurations for AIX and Windows.

- Linux: [Linux Setup Guide for Altibase](https://docs.altibase.com/display/arch/Linux+Setup+Guide+for+Altibase)
- SunOS: [Solaris Setup Guide for Altibase](https://docs.altibase.com/display/arch/Solaris+Setup+Guide+for+Altibase)
- HP-UX: [HPUX Setup Guide for Altibase](https://docs.altibase.com/display/arch/HPUX+Setup+Guide+for+Altibase)

# How the application communicates

---

Please refer to each manual for how to set the connection properties in the application program.

- CLI/ODBC: Refer to 2. ALTIBASE HDB CLI function -> SQLDriverConnect function description in CLI User's Manual.
- APRE (C/C++ Precompiler): From Precompiler User's Manual 6. Embedded SQL statement -> SQL statement related to connection -> CONNECT
- JDBC: From the JDBC User's Manual 1. Getting Started with JDBC -> Connection Information
