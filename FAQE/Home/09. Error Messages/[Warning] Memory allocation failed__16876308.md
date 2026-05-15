---
title: "[Warning] Memory allocation failed."
page_id: "16876308"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876308"
updated_at: "2021-04-05T10:47:48.000+0900"
version: 2
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# [Warning] Memory allocation failed.
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876308
Updated: 2021-04-05T10:47:48.000+0900

- [Overview](#id-[Warning]Memoryallocationfailed.-Overview) - [Version](#id-[Warning]Memoryallocationfailed.-Version) - [Situation](#id-[Warning]Memoryallocationfailed.-Situation) - [Cause and solution](#id-[Warning]Memoryallocationfailed.-Causeandsolution) - [When memory usage is limited by kernel parameters](#id-[Warning]Memoryallocationfailed.-Whenmemoryusageislimitedbykernelparameters) - [When running an Altibase server on a 32-bit OS](#id-[Warning]Memoryallocationfailed.-WhenrunninganAltibaseserverona32-bitOS) - [Insufficient physical memory](#id-[Warning]Memoryallocationfailed.-Insufficientphysicalmemory) - [Reference](#id-[Warning]Memoryallocationfailed.-Reference)

# Overview

---

This document explains '[Warning] Memory allocation failed]. This message is created when memory allocation fails due to the OS environment.

# Version

---

All the versions of ALTIBASE HDB

# Situation

---

- In $ALTIBASE_HOME/trc/altibase_boot.log, '[Warning] Memory allocation failed' error occurs.
- There may be an error such as [ERR-01051: Memory allocation failed.].
- This error can also occur during transaction execution or when STARTUP/SHUTDOWN on the Altibase server.
- When this error occurs, new connections may also fail.
- It mainly occurs on HP-UX.

# Cause and solution

---

### When memory usage is limited by kernel parameters

This is the most common cause.

For HP-UX, kernel parameters can limit the amount of memory a process can use. If the memory usage of the Altibase server process exceeds the setting value of this parameter, '[Warning] Memory allocation failed' message occurs.

The kernel parameters are as follows.

- maxdsiz (for 32bit process)
- maxdsiz_64bit (for 64bit processes)

How to check kernel parameters is as follows. The unit is in bytes and should be set large enough in consideration of the physical memory size. If necessary, ask the system engineer to make changes.

$ /usr/sbin/kctune | grep maxdsiz

### When running an Altibase server on a 32-bit OS

In 32-bit OS, the memory size that can be used by one process is limited to 2G, so if the Altibase server is operating without taking this into account, this message may occur.

### Insufficient physical memory

This message also occurs when there is not enough physical memory. Use a system resource monitoring tool such as top and glance to check the physical memory usage.

# Reference

---

- The default tablespace for ALTIBASE HDB server is SYS_TBS_MEM_DATA. So, if you do not specify a tablespace when performing CREATE TABLE, this tablespace is designated by default. This tablespace is a system memory tablespace, and the data in the table uses memory. Therefore, memory usage may increase differently from the user's intention, so make sure to check this as well.
- [HP-UX Setup Guide for ALTIBASE HDB PDF](https://docs.altibase.com/download/attachments/9109748/ALTIBASE_%EC%9A%B4%EC%98%81%EC%9D%84_%EC%9C%84%ED%95%9C_HPUX_%EC%84%A4%EC%A0%95_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1449022354000&api=v2)
