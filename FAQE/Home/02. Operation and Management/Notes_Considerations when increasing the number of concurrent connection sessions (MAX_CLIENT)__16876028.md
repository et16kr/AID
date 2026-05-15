---
title: "Notes/Considerations when increasing the number of concurrent connection sessions (MAX_CLIENT)"
page_id: "16876028"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876028"
updated_at: "2021-04-02T17:18:06.000+0900"
version: 4
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# Notes/Considerations when increasing the number of concurrent connection sessions (MAX_CLIENT)
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876028
Updated: 2021-04-02T17:18:06.000+0900

- [Overview](#Notes/Considerationswhenincreasingthenumberofconcurrentconnectionsessions(MAX_CLIENT)-Overview) - [Version](#Notes/Considerationswhenincreasingthenumberofconcurrentconnectionsessions(MAX_CLIENT)-Version) - [Changing Procedure](#Notes/Considerationswhenincreasingthenumberofconcurrentconnectionsessions(MAX_CLIENT)-ChangingProcedure) - [Considerations](#Notes/Considerationswhenincreasingthenumberofconcurrentconnectionsessions(MAX_CLIENT)-Considerations) - [MAX_CLIENT property](#Notes/Considerationswhenincreasingthenumberofconcurrentconnectionsessions(MAX_CLIENT)-MAX_CLIENTproperty) - [How to check the current settings](#Notes/Considerationswhenincreasingthenumberofconcurrentconnectionsessions(MAX_CLIENT)-Howtocheckthecurrentsettings) - [How to change the settings](#Notes/Considerationswhenincreasingthenumberofconcurrentconnectionsessions(MAX_CLIENT)-Howtochangethesettings) - [TRANSACTION_TABLE_SIZE](#Notes/Considerationswhenincreasingthenumberofconcurrentconnectionsessions(MAX_CLIENT)-TRANSACTION_TABLE_SIZE) - [How to check the current settings](#Notes/Considerationswhenincreasingthenumberofconcurrentconnectionsessions(MAX_CLIENT)-Howtocheckthecurrentsettings.1) - [How to change the settings](#Notes/Considerationswhenincreasingthenumberofconcurrentconnectionsessions(MAX_CLIENT)-Howtochangethesettings.1) - [Changing OS user resource open files](#Notes/Considerationswhenincreasingthenumberofconcurrentconnectionsessions(MAX_CLIENT)-ChangingOSuserresourceopenfiles) - [Check the setting value](#Notes/Considerationswhenincreasingthenumberofconcurrentconnectionsessions(MAX_CLIENT)-Checkthesettingvalue) - [Reference](#Notes/Considerationswhenincreasingthenumberofconcurrentconnectionsessions(MAX_CLIENT)-Reference)

# Overview

---

This document explains how to change the maximum number of sessions that can be connected to the ALTIBASE HDB server at the same time.

The number of concurrent sessions can be limited by the Altibase server property MAX_CLIENT, and there are some things to consider when changing this property.

# Version

---

All the ALTIBASE HDB versions

# Changing Procedure

---

1. Secure service downtime
2. Shutdown ALTIBASE HDB server
3. Change ALTIBASE server properties (refer to 'Considerations' below)
4. Check OS user resources and change them if necessary (refer to' Considerations' below)
5. Startup ALTIBASE HDB server

# Considerations

---

## MAX_CLIENT property

---

Set the maximum number of sessions that can be connected to the ALTIBASE HDB server at the same time.

The default value is 1000, which can be changed more if necessary. Since this property cannot be changed during operation, the ALTIBASE HDB server must be restarted if changes are required.

#### How to check the current settings

```
SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME = 'MAX_CLIENT';
```

#### How to change the settings

```
Change the MAX_CLIENT value in the $ALTIBASE_HOME/conf/altibase.properties file
```

## TRANSACTION_TABLE_SIZE

---

This property sets the maximum number of transactions that can be performed concurrently on the ALTIBASE HDB server. As the number of concurrently connected sessions increases, the number of concurrent transactions may increase. Therefore, it is recommended to change them together.

Since this property cannot be changed during operation, the ALTIBASE HDB server must be restarted if it needs to be changed.

Transactions should be set to be larger than MAX_CLIENT because not only transactions performed by users, but also system transactions and replication transactions.

#### How to check the current settings

```
SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME = 'TRANSACTION_TABLE_SIZE';
```

#### How to change the settings

```
Change the TRANSACTION_TABLE_SIZE value in the $ALTIBASE_HOME/conf/altibase.properties file
```

The TRANSACTION_TABLE_SIZE property setting value can be set to 2^n, which is larger than the current value, and cannot be changed from a large value to a small value.

Since the change method differs depending on the ALTIBASE HDB server version, be sure to refer to [Notes/Considerations when changing TRANSACTION_TABLE_SIZE](https://docs.altibase.com/pages/viewpage.action?pageId=16876013) before proceeding.

## Changing OS user resource open files

---

open files are the number of files that can be opened by a process, including not only files accessed by the process, but also communication sockets.

For example, if the ALTIBASE HDB server is operated in a user environment where this value is limited to 10, 10 sessions can be connected at the same time. (In fact, considering the files used by the ALTIBASE HDB server, there may not be an accessible session.)

It is recommended to set it to the maximum value allowed by the operating system (if possible, unlimited).

#### Check the setting value

```
$ ulimit -Sn      # soft limit
2000

$ ulimit -Hn      # hard limit
unlimited
```

The soft limit is the value set by the OS user, and the hard limit is the value set by the root user. The soft limit cannot be greater than the hard limit.

If the user needs to set it to a value greater than the hard limit, the user also needs to change the setting of the root user.

##### How to change

###### How to change user preferences

Add the following command to the environment configuration file (.bash_profile or .profile).

```
$ id                                                          # Log in as the OS user running the ALTIBASE HDB server
uid=509(altibase) gid=512(altibase) groups=512(altibase)

$ vi \~/.bash_profile                                         # Add configuration command to environment configuration file (Environment configuration file may be different depending on the shell.)

ulimit \-n unlimited

$ . ~/.bash_profile                                           # Apply user preferences (after logout)

$ ulimit -Sn                                                  # Check the applied value
unlimited
```

###### How the root user changes

```
Change the user's nofiles value in /etc/security/limits.conf file

Setting example) When changing the number of open files of altibase user to 65535
altibase soft nofile 65535
altibase hard nofile 65535
```

**HP-UX**

```
kctune maxfiles=unlimited
```

**AIX**

```
Change nofiles in /etc/security/limits
```

**SunOS**

```
set rlim_fd_max=unlimited
```

# Reference

---

- For information on ALTIBASE HDB server properties, refer to the General Reference manual at [https://github.com/ALTIBASE/Documents/tree/master/Manuals/](https://github.com/ALTIBASE/Documents/tree/master/Manuals/Altibase_7.1/eng).
- MAX_CLIENT and related settings are maximum values, so increasing them does not by itself affect DB performance or system resources.
- System resources may increase if the number of concurrent connection sessions and concurrent transactions increases due to configuration changes. However, it is difficult to answer how much impact it will have as it depends on the operating environment.
