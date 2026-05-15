---
title: "How to create multiple replication objects with the same IP"
page_id: "16876063"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/How+to+create+multiple+replication+objects+with+the+same+IP"
updated_at: "2021-04-05T09:30:16.000+0900"
version: 4
ancestors: ["Home", "03. Replication"]
labels: []
---

# How to create multiple replication objects with the same IP
Source: https://docs.altibase.com/display/FAQE/How+to+create+multiple+replication+objects+with+the+same+IP
Updated: 2021-04-05T09:30:16.000+0900

- [Overview](#HowtocreatemultiplereplicationobjectswiththesameIP-Overview) - [Version](#HowtocreatemultiplereplicationobjectswiththesameIP-Version) - [Procedure](#HowtocreatemultiplereplicationobjectswiththesameIP-Procedure) - [Check the related property](#HowtocreatemultiplereplicationobjectswiththesameIP-Checktherelatedproperty) - [Change the related property](#HowtocreatemultiplereplicationobjectswiththesameIP-Changetherelatedproperty) - [Create replication objects](#HowtocreatemultiplereplicationobjectswiththesameIP-Createreplicationobjects) - [Check the host information of the replication object](#HowtocreatemultiplereplicationobjectswiththesameIP-Checkthehostinformationofthereplicationobject) - [Reference](#HowtocreatemultiplereplicationobjectswiththesameIP-Reference)

# Overview

---

Altibase replication had a limitation that the same IP address could not be used when creating multiple redundant objects.

**Example of creating multiple replication objects whose IP and PORT of the remote server are 192.168.1.145, 30300**

```
iSQL> CREATE REPLICATION REP1 WITH '192.168.1.145', 30300 FROM ALTITEST.REP_TEST_T TO ALTITEST.REP_TEST_T;
Create success.

iSQL> CREATE REPLICATION REP2 WITH '192.168.1.145', 30300 FROM ALTITEST.REP_TEST_T2 TO ALTITEST.REP_TEST_T2;
[ERR-6110C : Replication hosts already exist.]
```

As a property added to Altibase version 6.5.1 or later, it is possible to create different redundant objects with the same host information without such restrictions.

# Version

---

Altibase version 6.5.1 or later

# Procedure

---

### Check the related property

---

Check the value of the Altibase server property REPLICATION_ALLOW_DUPLICATE_HOSTS.

The default value of this property is 0, which does not allow different objects to have the same host information.

```
set linesize 1024
set colsize 60
SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME = 'REPLICATION_ALLOW_DUPLICATE_HOSTS';
```

### Change the related property

---

If the value of the REPLICATION_ALLOW_DUPLICATE_HOSTS property is 0, change it to 1.

```
ALTER SYSTEM SET REPLICATION_ALLOW_DUPLICATE_HOSTS = 1;
```

In order to permanently apply the property change value, modify the property value in the altibase.properties file and save it.

```
cd $ALTIBASE_HOME/conf
vi altibase.properties
REPLICATION_ALLOW_DUPLICATE_HOSTS     = 1
```

### Create replication objects

---

Create more than one duplicate object with the same host information.

**Example of creating multiple replication objects whose IP and PORT of the remote server are 192.168.1.145, 30300**

```
iSQL> CREATE REPLICATION REP1 WITH '192.168.1.145', 30300 FROM ALTITEST.REP_TEST_T TO ALTITEST.REP_TEST_T;
Create success.

iSQL> CREATE REPLICATION REP2 WITH '192.168.1.145', 30300 FROM ALTITEST.REP_TEST_T2 TO ALTITEST.REP_TEST_T2;
Create success.
```

### Check the host information of the replication object

---

Host information registered in the replicated object can be checked with the following sentence.

```
SELECT REPLICATION_NAME, HOST_IP, PORT_NO FROM SYSTEM_.SYS_REPL_HOSTS_ ORDER BY HOST_NO;
```

# Reference

---

- Altibase 6.5.1 New Features Guide
- General Reference (Altibase 6.5.1 or later)
- Manual Download: [http://support.altibase.com/en/manual](http://support.altibase.com/en/manual) or [https://github.com/ALTIBASE/Documents/tree/master/Manuals/](https://github.com/ALTIBASE/Documents/tree/master/Manuals/Altibase_7.1/eng)
