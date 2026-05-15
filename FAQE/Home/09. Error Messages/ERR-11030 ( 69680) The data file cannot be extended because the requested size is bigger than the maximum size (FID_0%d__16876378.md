---
title: "ERR-11030 (  69680) The data file cannot be extended because the requested size is bigger than the maximum size (FID:<0%d>)."
page_id: "16876378"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876378"
updated_at: "2021-03-29T10:25:49.000+0900"
version: 1
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# ERR-11030 (  69680) The data file cannot be extended because the requested size is bigger than the maximum size (FID:<0%d>).
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876378
Updated: 2021-03-29T10:25:49.000+0900

**- [Overview](#ERR-11030(69680)Thedatafilecannotbeextendedbecausetherequestedsizeisbiggerthanthemaximumsize(FID:<0%d>).-Overview) - [Version](#ERR-11030(69680)Thedatafilecannotbeextendedbecausetherequestedsizeisbiggerthanthemaximumsize(FID:<0%d>).-Version) - [Cause](#ERR-11030(69680)Thedatafilecannotbeextendedbecausetherequestedsizeisbiggerthanthemaximumsize(FID:<0%d>).-Cause) - [Solution](#ERR-11030(69680)Thedatafilecannotbeextendedbecausetherequestedsizeisbiggerthanthemaximumsize(FID:<0%d>).-Solution) - [Reference](#ERR-11030(69680)Thedatafilecannotbeextendedbecausetherequestedsizeisbiggerthanthemaximumsize(FID:<0%d>).-Reference)**

# Overview

---

When changing the size of the disk tablespace data file, you may encounter the following error message.

```
iSQL> alter tablespace DISK_USER_TBS alter datafile '/home/altibase_home/dbs/user.dbf' size 200M;
[ERR-11030 : The data file cannot be extended because the requested size is bigger than the maximum size (FID:0).]
```

# Version

---

ALTIBASE HDB 4

# Cause

---

The above error message occurs when the size of the data file with the AUTOEXTEND OFF attribute is changed larger than maxsize.

The autoextend attribute and configured size of each data file can be checked with the following statement (on if autoextend is 1, off if 0).

```
iSQL> select name, AUTOEXTEND , INITSIZE, MAXSIZE from v$datafiles;
NAME                                     AUTOEXTEND  INITSIZE             MAXSIZE
 ----------------------------------------------------------------------------------------------------
/home/altibase_home/dbs/temp001.dbf      1           12800                262144 /home/altibase_home/dbs/user.dbf
```

Data files with autoextend on automatically increase their size up to maxsize, so there is a difference between the initial setting size (INITSIZE) and the maximum size (MAXSIZE). However, the maximum size (MAXSIZE) of a data file with autoextend off is set equal to the initial setting size (INITSIZE). Because of this, if you try to change the size larger than the maximum size (MAXSIZE), the above error may occur.

# Solution

---

After changing the AUTOEXTEND property of the data file to ON, you must proceed with the data file size change operation. Follow the steps below.

```
1) Change AUTOEXTEND property
iSQL> alter tablespace DISK_USER_TBS alter datafile '/home/altibase_home/dbs/user.dbf' autoextend on; Alter success.
2) Change data file size
iSQL> alter tablespace DISK_USER_TBS alter datafile '/home/altibase_home/dbs/user.dbf' size 100M; Alter success.
```

# Reference

---

In fact, data files with the autoextend off attribute only make sense for the initial set size (initsize). When the autoextend off clause is included in the CREATE TABLESPACE statement or the ALTER TABLESPACE statement, the nextsize and maxsize clauses cannot be used together in addition to the size clause.

When used together, an SQL statement error occurs as shown below.

```
iSQL> create tablespace user_disk_tbs2 datafile 'user2.dbf' size 1M autoextend off next 1M;
[ERR-31001 : SQL syntax error
line 1: parse error create tablespace USER_DISK_TBS2 DATAFILE 'user2.dbf' SIZE 1M autoextend off NEXT 1M
```

ALTIBASE HDB 4.3.9 lacks handling of this. From ALTIBASE HDB version 5, this restriction is reflected, and the maxsize of the data file with the autoextend off attribute is set to the OS file limit value.

With this change, unlike 4.3.9, maxsize is output as 0 when searching v$datafile,

```
iSQL> select name, AUTOEXTEND , INITSIZE, currsize, MAXSIZE from v$datafiles;
NAME                                AUTOEXTEND  INITSIZE             CURRSIZE            MAXSIZE
-------------------------------------------------------------------------------------------------------
/home/altibase_home/dbs/user.dbf    0           128                  128                 0

It is also possible to change the size.
iSQL> alter tablespace USER_DISK_TBS alter datafile '/home/altibase_home/dbs/user.dbf' size 8M; Alter success.
iSQL> select name, AUTOEXTEND , INITSIZE, currsize, MAXSIZE from v$datafiles;
NAME                                AUTOEXTEND  INITSIZE             CURRSIZE             MAXSIZE
 --------------------------------------------------------------------------------------------------------
/home/altibase_home/dbs/user.dbf    0           128                  2048                 0
```

The OS file limit can be checked with ulimit -a.

```
$ ulimit -a
core file size  (blocks, -c) 2097151
data seg size           (kbytes, -d) 2097152
file size               (blocks, -f) unlimited
max memory size         (kbytes, -m) unlimited
open files                      (-n) 5030
pipe size            (512 bytes, -p) 16
stack size              (kbytes, -s) 131072
cpu time               (seconds, -t) unlimited
max user processes              (-u) 3278
virtual memory          (kbytes, -v) unlimited
```
