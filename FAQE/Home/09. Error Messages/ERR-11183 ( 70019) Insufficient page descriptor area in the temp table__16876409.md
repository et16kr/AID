---
title: "ERR-11183 (  70019) Insufficient page descriptor area in the temp table."
page_id: "16876409"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876409"
updated_at: "2021-04-05T11:23:57.000+0900"
version: 5
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# ERR-11183 (  70019) Insufficient page descriptor area in the temp table.
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876409
Updated: 2021-04-05T11:23:57.000+0900

- [Overview](#ERR-11183(70019)Insufficientpagedescriptorareainthetemptable.-Overview) - [Version](#ERR-11183(70019)Insufficientpagedescriptorareainthetemptable.-Version) - [Symptom](#ERR-11183(70019)Insufficientpagedescriptorareainthetemptable.-Symptom) - [Cause](#ERR-11183(70019)Insufficientpagedescriptorareainthetemptable.-Cause) - [Solution](#ERR-11183(70019)Insufficientpagedescriptorareainthetemptable.-Solution)

# Overview

---

This document describes the cause and solution of the occurrence of 'ERR-11183 (70019) Insufficient page descriptor area in the temp table' that occurs when executing a query.

# Version

---

- Altibase Server 6.3.1 or later
- Altibase server up to 7.1.0.5.0
    - Altibase 7.1.0.5.1 or later reflects BUG-48369, so this error does not occur.

# Symptom

---

This can occur when a disk table is used in a query statement and a query statement that requires SORT or HASH operation processing is executed.

# Cause

---

This error occurs when the following conditions are satisfied.

- The maximum size of the disk temporary tablespace is set larger than TEMP_MAX_PAGE_COUNT, and
- When a query statement that requires a disk temporary tablespace with a size exceeding TEMP_MAX_PAGE_COUNT is executed.

Altibase server allocates and uses a certain size in memory for fast operation when SORT/HASH operation is required in the process of query processing for disk tables. If all the memory of the specified size is used and additional space for SORT/HASH operations is needed, use a disk temporary tablespace. At this time, the total number of pages that can be used as a disk temporary tablespace is determined by the TEMP_MAX_PAGE_COUNT property.

#### Example of error occurrence: Insufficient page descriptor area in the temp table

The maximum size of the disk temporary tablespace is set to 2G, and the value of the TEMP_MAX_PAGE_COUNT property is set to 32767 (256MB),

```
iSQL> set vertical off;
iSQL> set linesize 1024
iSQL> set colsize 25

-- The disk temporary tablespace is set to use up to 2G.
iSQL> SELECT 'DISK_TEMP_TBS_MAX_SUM'
     , SUM(DECODE(F.MAXSIZE, 0, F.CURRSIZE, F.MAXSIZE)*TBS.PAGE_SIZE) AS 'MAX_SIZE(BYTE)'
  FROM V$DATAFILES F,
       V$TABLESPACES TBS
 WHERE F.SPACEID = TBS.ID
   AND TBS.TYPE IN (5, 6);
'DISK_TEMP_TBS_MAX_SUM'  MAX_SIZE(BYTE)
---------------------------------------------------
DISK_TEMP_TBS_MAX_SUM  2147475456
1 row selected.

-- The unit of the TEMP_MAX_PAGE_COUNT property value is the number of pages, and in terms of size, it is 256MB.
- The result below means that the number of pages that can be used as a disk temporary tablespace is 256MB.
iSQL> SELECT NAME, VALUE1, VALUE1*8192 FROM V$PROPERTY WHERE NAME = 'TEMP_MAX_PAGE_COUNT';
NAME                       VALUE1                     VALUE1*8192
---------------------------------------------------------------------------------
TEMP_MAX_PAGE_COUNT        32767                      268427264
1 row selected.
```

When a query statement whose size for SORT operation exceeds the TEMP_MAX_PAGE_COUNT property value of 32767 (256MB) is executed.

```
iSQL> select count(*) from (select count(*) from t, t2, t3 group by t.c2, t2.c2, t3.c2);
[ERR-11183 : Insufficient page descriptor area in the temp table.]
```

If the disk temporary tablespace usage is queried while executing the query, it can be seen that the disk temporary tablespace usage is close to the TEMP_MAX_PAGE_COUNT property value.

```
-- Query disk temporary tablespace usage when executing a query
iSQL> set vertical on;
iSQL> set colsize 100
iSQL> SELECT TO_CHAR(SYSDATE, 'HH:MI:SS') TIME,
       'TEMP_T_STATS',
       CREATE_TIME, DROP_TIME,
       SS.ID SESSION_ID,
       TRANSACTION_ID TX_ID,
       SS.AUTOCOMMIT_FLAG ,
       STMT.EXECUTE_FLAG ,
       SQL_TEXT,
       STATE,
       ESTIMATED_OPTIMAL_SORT_SIZE,
       ESTIMATED_OPTIMAL_HASH_SIZE,
       ALLOC_WAIT_COUNT,
       WORK_AREA_SIZE,
       NORMAL_AREA_SIZE
  FROM X$TEMPTABLE_STATS TEMP,
       V$STATEMENT STMT,
       V$SESSION SS
 WHERE TRANSACTION_ID = STMT.TX_ID
   AND SS.ID <> SESSION_ID()
   AND STMT.SESSION_ID = SS.ID
 ORDER BY SESSION_ID;
TIME                        : 15:39:03
'TEMP_T_STATS'              : TEMP_T_STATS
CREATE_TIME                 : 20161129_153221
DROP_TIME                   : 20161129_153311
SESSION_ID                  : 1
TX_ID                       : 51842
AUTOCOMMIT_FLAG             : 1
EXECUTE_FLAG                : 0
SQL_TEXT                    : select count(*) from (select count(*) from t, t2, t3 group by t.c2, t2.c2, t3.c2)
STATE                       : SORT_INSERTNSORT
ESTIMATED_OPTIMAL_SORT_SIZE : 562205696
ESTIMATED_OPTIMAL_HASH_SIZE : 0
ALLOC_WAIT_COUNT            : 0
WORK_AREA_SIZE              : 1048576
NORMAL_AREA_SIZE            : 267911168              -- Disk temporary tablespace usage. Similar to the size of TEMP_MAX_PAGE_COUNT converted to bytes.
```

# Solution

---

Change the value of the TEMP_MAX_PAGE_COUNT property according to the maximum value of the disk temporary tablespace.

**1. Check the maximum value of disk temp tablespace** TEMP_MAX_PAGE_COUNT should be set on the assumption that all disk temporary tablespaces will be used to the maximum. Therefore, check the sum of the maximum values of all disk temporary tablespaces created in the Altibase server with the following query.

**Sum of maximum disk temporary tablespaces**

```
SELECT 'DISK_TEMP_TBS_MAX_SUM'
     , SUM(DECODE(F.MAXSIZE, 0, F.CURRSIZE, F.MAXSIZE)*TBS.PAGE_SIZE) AS 'MAX_SIZE(BYTE)'
  FROM V$DATAFILES F,
       V$TABLESPACES TBS
 WHERE F.SPACEID = TBS.ID
   AND TBS.TYPE IN (5, 6);
```

**2. Calculate TEMP_MAX_PAGE property appropriate value** The unit of the TEMP_MAX_PAGE_COUNT property is the number of pages, and the value is calculated using the formula below.

TEMP_MAX_PAGE_COUNT = *Sum of maximum disk temporary tablespaces* / 8192

**Example of TEMP_MAX_PAGE_COUNT calculation**

If the total sum of the maximum disk temporary tablespaces is 17179869184 bytes (16GB), 17179869184/8192 = 2097152, and the value of the TEMP_MAX_PAGE_COUNT property is 2097152.

**TEMP_MAX_PAGE_COUNT setting value for each total maximum of disk temporary tablespaces**

TEMP_MAX_PAGE_COUNT = 1048576 for 8G

TEMP_MAX_PAGE_COUNT = 2096128 for 16G

TEMP_MAX_PAGE_COUNT = 4192256 for 32G

TEMP_MAX_PAGE_COUNT = 8388608 for 64G

#### **3. Change TEMP_MAX_PAGE_COUNT property**

TEMP_MAX_PAGE_COUNT can be changed at the system level during Altibase operation.

```
ALTER SYSTEM SET TEMP_MAX_PAGE_COUNT = value;
```

Check V$PROPERTY to check the changed value.

```
SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME = 'TEMP_MAX_PAGE_COUNT';
```

Altibase server configuration file is also changed so that the value changed to ALTER SYSTEM is reflected even after restarting the Altibase server.

```
shell> cd $ALTIBASE_HOME/conf
shell> vi altibase.properties        # If TEMP_MAX_PAGE_COUNT does not exist in the altibase.properties file, if it is added, the existing value is changed.
TEMP_MAX_PAGE_COUNT = value;
```

**4. Considerations when changing the TEMP_MAX_PAGE_COUNT property** The following three properties are affected by TEMP_MAX_PAGE_COUNT. TOTAL_WA_SIZE SORT_AREA_SIZE HASH_AREA_SIZE  So, if TEMP_MAX_PAGE_COUNT is changed, these properties must be changed as well.  The recommended values for each property are as follows. The recommended value is calculated according to the default ratio, and the appropriate value of the property may be changed during operation.

TOTAL_WA_SIZE: 256 times TEMP_MAX_PAGE_COUNT SORT_AREA_SIZE: 2 times TEMP_MAX_PAGE_COUNT HASH_AREA_SIZE: 8 times TEMP_MAX_PAGE_COUNT

For example, when changing to TEMP_MAX_PAGE_COUNT = 1048576, the recommended value of each property is as follows.

TOTAL_WA_SIZE = 1048576*256 = 268435456 (Unit is bytes) SORT_AREA_SIZE = 1048576*2 = 2097152 (unit is byte) HASH_AREA_SIZE = 1048576*8 = 8388608 (Unit is byte)

Like TEMP_MAX_PAGE_COUNT, the following three properties can be changed at the system level during Altibase operation.

```
ALTER SYSTEM SET TOTAL_WA_SIZE = value;
ALTER SYSTEM SET SORT_AREA_SIZE = value;
ALTER SYSTEM SET HASH_AREA_SIZE = value;
```

Check V$PROPERTY to check the changed value.

```
SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME IN ('TOTAL_WA_SIZE', 'SORT_AREA_SIZE', 'HASH_AREA_SIZE');
```

The altibase server configuration file is also changed so that the value changed to ALTER SYSTEM is reflected even after restarting the Altibase server.

```
shell> cd $ALTIBASE_HOME/conf
shell> vi altibase.properties        # Find and change each property in the altibase.properties file.
TOTAL_WA_SIZE                        = 134217728 # default = 134217728
SORT_AREA_SIZE                       = 1048576   # default = 1048576
HASH_AREA_SIZE                       = 4194304   # default = 4194304
```

**5. Effect of property change**

In the case of the TOTAL_WA_SIZE property, the ALLOC_SIZE and MAX_TOTAL_SIZE of V$MEMSTAT increase immediately after setting, and the memory of the Altibase server process also increases.

The area where the memory increases depend on the Altibase version. In the case of Altibase 7, the Temp_Memory area increases, and in the case of Altibase 6.3.1 and 6.5.1, the Storage_Disk_Buffer area increases.

How to check V$MEMSTAT is as follows.

**Altibase 7 or later**

```
SELECT NAME, ALLOC_SIZE, MAX_TOTAL_SIZE FROM V$MEMSTAT WHERE NAME = 'Temp_Memory';
```

**Altibase 6.3.1, 6.5.1**

```
SELECT NAME, ALLOC_SIZE, MAX_TOTAL_SIZE FROM V$MEMSTAT WHERE NAME = 'Storage_Disk_Buffer';
```

In the case of Unix/Linux, check whether the memory of the Altibase server process is increased with the ps command.

When checking immediately after TOTAL_WA_SIZE is changed, vsz increases, and when sort/hash operation occurs, rss increases.

**Linux, SunOS**

```
shell> ps -o vsz,rss -p process_id
```

**HP-UX**

```
shell> export UNIX95=1
shell> ps -o vsz,rss -p process_id
```

**AIX**

```
shell> ps -o vsz,rssize -p process_id
```
