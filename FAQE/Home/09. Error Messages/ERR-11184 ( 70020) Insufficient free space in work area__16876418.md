---
title: "ERR-11184 (  70020) Insufficient free space in work area"
page_id: "16876418"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-11184+%28++70020%29+Insufficient+free+space+in+work+area"
updated_at: "2021-04-05T13:17:25.000+0900"
version: 3
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# ERR-11184 (  70020) Insufficient free space in work area
Source: https://docs.altibase.com/display/FAQE/ERR-11184+%28++70020%29+Insufficient+free+space+in+work+area
Updated: 2021-04-05T13:17:25.000+0900

- [Overview](#ERR-11184(70020)Insufficientfreespaceinworkarea-Overview) - [Version](#ERR-11184(70020)Insufficientfreespaceinworkarea-Version) - [Symptom](#ERR-11184(70020)Insufficientfreespaceinworkarea-Symptom) - [Cause](#ERR-11184(70020)Insufficientfreespaceinworkarea-Cause) - [Solution](#ERR-11184(70020)Insufficientfreespaceinworkarea-Solution) - [How to check the work area setting value](#ERR-11184(70020)Insufficientfreespaceinworkarea-Howtochecktheworkareasettingvalue) - [How to change the work area setting value](#ERR-11184(70020)Insufficientfreespaceinworkarea-Howtochangetheworkareasettingvalue) - [Precautions when changing the work area setting value](#ERR-11184(70020)Insufficientfreespaceinworkarea-Precautionswhenchangingtheworkareasettingvalue)

# Overview

---

This document describes the cause of the ERR-11184 (70020) Insufficient free space in work area error that occurs when executing a query and how to fix it.

# Version

---

Altibase server 6.3.1 or later

# Symptom

---

This can occur when a disk table is used in a query statement and a query statement that requires SORT or HASH operation processing is executed.

# Cause

---

This error occurs due to insufficient memory space called Work Area.

Work Area refers to a memory space of a certain size reserved by the OS when the Altibase server is running for better performance when performing SORT/HASH operations on disk table data.

When SORT or HASH operation is required when executing a query, it is allocated and used in the work area as much as a predetermined size. If SORT operation is required, it is allocated as much as SORT_AREA_SIZE in the work area and used. If the HASH operation is required, it is allocated as much as HASH_AREA_SIZE in the work area and used.

Multiple transactions requiring SORT/HASH operations can be executed at the same time. At this time, if trying to get SORT_AREA_SIZE or HASH_AREA_SIZE from the work area, but there is no free memory to allocate in the work area, this error occurs.

# Solution

---

It is caused by insufficient work area, so the size of the work area must be increased larger than the current value.

The size of the work area can be set with the Altibase server property TOTAL_WA_SIZE.

### How to check the work area setting value

- Check the current setting value with the sentence below.

  ```
  SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME = 'TOTAL_WA_SIZE';
  ```

### How to change the work area setting value

- Change with ALTER SYSTEM statement.

  ```
  ALTER SYSTEM SET TOTAL_WA_SIZE = value ; -- value is in bytes.
  ```
- The Altibase server configuration file is also changed so that the value changed to ALTER SYSTEM is reflected even after restarting the Altibase server.

  ```
  shell> cd $ALTIBASE_HOME/conf
  shell> vi altibase.properties        # Find and change the TOTAL_WA_SIZE property in the altibase.properties file.
  TOTAL_WA_SIZE                        = 134217728 # default = 134217728
  ```

### Precautions when changing the work area setting value

- If TOTAL_WA_SIZE is changed larger than the current setting value, the size of V$MEMSTAT increases, and Altibase server process memory usage and VSZ also increase.
- For Altibase 7 or higher, the Temp_Memory area of V$MEMSTAT increases and
- In the case of Altibase 6.3.1 and 6.5.1, the Storage_Disk_Buffer area of V$MEMSTAT increases.
- If the ALTER SYSTEM SET TOTAL_WA_SIZE statement is executed while a query statement that requires a disk SORT/HASH operation is executed (transaction using a work area), this statement waits until the previously executed transaction is terminated.
- ALTER SYSTEM SET TOTAL_WA_SIZE = ... If a query statement that requires a disk SORT/HASH operation is executed while the statement is being executed, the transaction waits until the ALTER SYSTEM statement is finished.

---
