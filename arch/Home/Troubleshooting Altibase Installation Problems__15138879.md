---
title: "Troubleshooting Altibase Installation Problems"
page_id: "15138879"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/Troubleshooting+Altibase+Installation+Problems"
updated_at: "2021-02-22T14:23:26.000+0900"
version: 14
ancestors: ["Home"]
labels: []
---

# Troubleshooting Altibase Installation Problems
Source: https://docs.altibase.com/display/arch/Troubleshooting+Altibase+Installation+Problems
Updated: 2021-02-22T14:23:26.000+0900

---

- [Overview](#TroubleshootingAltibaseInstallationProblems-Overview) - [Troubleshooting in common environments](#TroubleshootingAltibaseInstallationProblems-Troubleshootingincommonenvironments) - [Unable to interpret Binary](#TroubleshootingAltibaseInstallationProblems-UnabletointerpretBinary) - [Environment variable not registered](#TroubleshootingAltibaseInstallationProblems-Environmentvariablenotregistered) - [Problem with user's file privileges](#TroubleshootingAltibaseInstallationProblems-Problemwithuser'sfileprivileges) - [Absence of altibase.properties file](#TroubleshootingAltibaseInstallationProblems-Absenceofaltibase.propertiesfile) - [Absence of license file](#TroubleshootingAltibaseInstallationProblems-Absenceoflicensefile) - [License error](#TroubleshootingAltibaseInstallationProblems-Licenseerror) - [Expired License error](#TroubleshootingAltibaseInstallationProblems-ExpiredLicenseerror) - [Property value error](#TroubleshootingAltibaseInstallationProblems-Propertyvalueerror) - [Writing file error](#TroubleshootingAltibaseInstallationProblems-Writingfileerror) - [Skipping the database creation procedure](#TroubleshootingAltibaseInstallationProblems-Skippingthedatabasecreationprocedure) - [Listener port bind failure](#TroubleshootingAltibaseInstallationProblems-Listenerportbindfailure) - [Replication port bind failure](#TroubleshootingAltibaseInstallationProblems-Replicationportbindfailure)

# Overview

---

This document describes troubleshooting for each type of problem that may occur when users attempt to install ALTIBASE products.

Problems not listed in the document may occur and the type of occurrence may differ depending on the version of ALTIBASE.

For problems that are no described in this document, please send an email to [support@altibase.com](mailto:support@altibase.com) with a description of the occurrence conditions and the ALTIBASE trace log files ('trc' directory under the ALTIBASE installation path).

- Altibase version 5.5.1 or later

For errors and improvements related to this document, please contact the technical support portal or technical support center.

- Technical support portal: [http://support.altibase.com](http://support.altibase.com/)[/en/](http://support.altibase.com/en/)
- Technical support center: 02-2082-1114

# Troubleshooting in common environments

---

This section describes the list of types of problems that may occur during the installation with corrective solutions.

## Unable to interpret Binary

---

- The ALTIBASE package is compiled and distributed according to the supported CPU classification.
- This can occur if the user tries to download and install the ALTIBASe package that does not match the CPU of the device where the user wants to install ALTIBASE.com
- To check whether the installed executable file is normal, simply use the altibase -v command.
- The error message in the example below is the most common error situation. In addition to this, other error messages such as library compatibility can be returned.

**Example 1: When the CPU of the device and the ALTIBASe package do not match**

```
$ ./altibase-HDB-server-6.5.1.6.8-LINUX-POWERPC-64bit-release.run
-bash: ./altibase-HDB-server-6.5.1.6.8-LINUX-POWERPC-64bit-release.run: cannot execute binary file
```

- **Solution: Reinstall the pack for the CPU of the device.**

## Environment variable not registered

---

- In order to connect ALTIBASE in sysdba mode, the path where ALTIBASe is installed must be registered in a variable named "ALTIBASE_HOME'.
- If this variable is not registered, the following error occurs.

```
$ isql -s 127.0.0.1 -u sys -p manager -port 20300 -sysdbaISQL_CONNECTION = UNIX, SERVER = 127.0.0.1, PORT_NO = 20300
[ERR-91003 : Environment (ALTIBASE_HOME) does not exists.
```

- **Solution: Register the ALTIBASE installation path with the value of the variable named 'ALTIBASE_HOME'.**

## Problem with user's file privileges

---

- When installing and creating a database, it must be connected in the sysdba.
- At this time access to sysdba mode is possible only with the user who installed ALTIBASE.

```
$ isql -s 127.0.0.1 -u sys -p manager -port 26084 -sysdba-----------------------------------------------------------------
     Altibase Client Query utility.
     Release Version 6.5.1.6.8
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
WARNING: A port number is not required when connecting via IPC or UNIX, so the -port option was ignored.
ISQL_CONNECTION = UNIX, SERVER = 127.0.0.1
[ERR-9100B : Privilege error for sysdba user account.]
```

- **Solution: Try again as the user who installed ALTIBASE, or change the owner's privileges of all files under the ALTIABSE installation path to the current user.**

## Absence of altibase.properties file

---

- This problem occurs when there is no altibase.properfies file in the 'conf' directory under the ALTIBASE installation path.

```
iSQL(sysdba)> startup process
idp readConf() Error : Open File [/hdb_home/651/conf/altibase.properties] Error.
```

- **Solution: 'altibase.properties.sample' file for first-time users is provided in the 'conf' directory under the ALTIBASE installation path. Edit this file and the altibase.properties file to suit the environment.**

## Absence of license file

---

- This problem occurs when proceeding without creating a license file in the 'conf' directory under the ALTIBASE installation path.

```
TRANSITION TO PHASE : PROCESSCommencing Server as Community Edition
DISK_MAX_DB_SIZE(Unlimited) exceeded limit 8192M
[FAILURE] License invalid or expired.
Startup Failed....
[ERR-91015 : Communication failure.]
```

- **Solution: Based on the license issued from ALTIBASe, a license file should be created in the corresponding location.**

## License error

---

- MAC ADDRESS may be changed for reasons such as changing the network card of the device. Or, the wrong license may been issued because the license issuance information was incorrectly sent to ALTIBASE.

```
TRANSITION TO PHASE : PROCESSInvalid or expired license in License File(/hdb_home/651/conf/license)
[FAILURE] License invalid or expired.
Startup Failed....
[ERR-91015 : Communication failure.]
```

- **Solution: If the hostid or Mac Address when the license is issued is different from the information of the target device, the license must be reissued.**

## Expired License error

---

This problem occurs when the issued license has expired.

```
TRANSITION TO PHASE : PROCESSInvalid or expired license in License File(/hdb_home/651/conf/license)
[FAILURE] License invalid or expired.
Startup Failed....
[ERR-91015 : Communication failure.]
```

- **Solution: Apply/request for a new license from the Altibase Technical Support Portal ([http://support.altibase.com/en/)](http://support.altibase.com/en/)).**

## Property value error

---

- This problem occurs when the value specified in the altibase.properties file or the value specified with the environment variable in the 'conf' directory under the ALTIBASE installation path is incorrect.

**When the currently set value is out of range**

```
idp checkRange() Error : Property [property_name] [current_value] Overflowed the Value Range.(min_value~max_value)
```

**If the currently set value is impossible to convert the data type**

```
 idp convertFromString() Error : The property [property_name] value [current_value] is not convertable.
```

**When the same property is duplicated**

```
idp insertBySrc() Error : Property [property_name] Can't Store Multiple Values.
```

- **Solution: Check the problem property and correct it to a normal value.**

## Writing file error

---

- Writing file error can be caused by a number of problem factors
- The disk may not have enough free space, or the directory may have omitted privileges.

```
TRANSITION TO PHASE : PROCESSCommand execute success.

DB Info (Page Size     = 32768)
        (Page Count    = 257)
        (Total DB Size = 8421376)
        (DB File Size  = 1073741824)

FAILURE of createdb.

[ERR-0103C : Unable to invoke create() function on [/ALTIBASE/altibase_home/dbs/dwfile0.dwf]]
```

- **Solution: check the free space on the disk and the privileges of the directory.**

## Skipping the database creation procedure

---

- In order to start Altibase in service mode, the database creation procedure must be preceded.
- This problem occurs when the user omits this procedure and starts the server in a shell prompt, starts in iSQL, or starts ALTIBASE as a service in the WINDOWS environment.
- Usually, when ALTIBASE starts up, the loganchor file is retrieved for the first time, so an error message indicating that the file does not exist is returned.

```
TRANSITION TO PHASE : CONTROL[FAILURE] The log anchor file does not exist or it is not valid.

Startup Failed....

[ERR-91015 : Communication failure.]
```

- **Solution: Perform database creation procedure.**

## Listener port bind failure

---

- This problem occurs when the ALTIBASE process fails to bind the TCP port to be used.

```
TRANSITION TO PHASE : SERVICE  [CM] Listener failed  : TCP on port 20300 [IPV4]
[FAILURE] Unable to bind the socket.
Startup Failed....
[ERR-91015 : Communication failure.]
```

- **Solution: Find the case that the port cannot be bound, and then solve it.**
  **If another application is preempted, the application or the port used for ALTIBASE must be changed.**

## Replication port bind failure

---

- This problem occurs when the ALTIBASE replication thread fails in the step of binding the port to be used.

```
TRANSITION TO PHASE : SERVICE  [CM] Listener started : TCP on port 20300 [IPV4]
  [CM] Listener started : UNIX
  [CM] Listener started : IPC
  [RP] Initialization : FAIL
[FAILURE] [Receiver] Failed to listen to a replication socket (Port No:30300)
Startup Failed....
[ERR-91015 : Communication failure.]
```

- **Solution: Find the cause that the port cannot be bound, then solve it.**
  **If another application is preempted, the application or the port used for ALTIBASE must be changed.**

# Korean Source Attachments

The Korean source page also references these downloadable source attachments. They are preserved here so the English document set does not lose those references.

- [Korean source attachment 1 (PDF)](https://docs.altibase.com/download/attachments/13437056/ALTIBASE_%EC%84%A4%EC%B9%98_%EC%8B%9C_%EB%B0%9C%EC%83%9D%ED%95%A0_%EC%88%98_%EC%9E%88%EB%8A%94_%EB%AC%B8%EC%A0%9C%EC%83%81%ED%99%A9%EA%B3%BC_%EC%A1%B0%EC%B9%98.pdf?version=1&modificationDate=1697764061000&api=v2)
