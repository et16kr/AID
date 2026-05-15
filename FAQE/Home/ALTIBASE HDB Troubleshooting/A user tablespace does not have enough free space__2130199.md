---
title: "A user tablespace does not have enough free space"
page_id: "2130199"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/A+user+tablespace+does+not+have+enough+free+space"
updated_at: "2011-08-03T17:41:24.000+0900"
version: 10
ancestors: ["Home", "ALTIBASE HDB Troubleshooting"]
labels: []
---

# A user tablespace does not have enough free space
Source: https://docs.altibase.com/display/FAQE/A+user+tablespace+does+not+have+enough+free+space
Updated: 2011-08-03T17:41:24.000+0900

- [What is this error?](#Ausertablespacedoesnothaveenoughfreespace-Whatisthiserror?)
- [How to resolve this error?](#Ausertablespacedoesnothaveenoughfreespace-Howtoresolvethiserror?)

# What is this error?

```
iSQL> CREATE TABLESPACE disk_tbs datafile 'dbf1.dbf' SIZE 10M AUTOEXTEND OFF;
iSQL> CREATE TABLE t2 (c1 CHAR(100)) TABLESPACE disk_tbs;
iSQL> INSERT INTO T2 VALUES ('1');
iSQL> INSERT INTO T2 SELECT * FROM T2;
.....
(repeat above SQL)
.....
iSQL> INSERT INTO T2 SELECT * FROM T2;
[ERR-11035 : The tablespace does not have enough free space ( TBS ID : 4, TBS Name :DISK_TBS, Type : 2, Used Page Limit : 128 ).]
```

As it is illustrated in the above example, an error message is displayed when a user tablespace's usage grows up to the limit specified at the initial creation of that tablespace.In this example it is 10Mbytes. Please also note that this message is different for the versions of ALTIBASE HDB earlier than version 5. How to check usage of a tablespaces? [refer to this page.](http://aid.altibase.com/display/arch/SQL+about+Tablespaces#SQLaboutTablespaces-DiskTablespaceUsage)

# How to resolve this error?

First, please check to make sure that in fact the user tablespace does not have enough resource (disk space in our example). Second, execute the following DDL statements to expand the user tablespace.

```
iSQL>ALTER TABLESPACE disk_tbs ADD DATAFILE 'dbf2.dbf' SIZE 10M AUTOEXTEND ON;

(if TBS name equals to "SYS_TBS_UNDO", execute below DDL)
iSQL> ALTER TABLESPACE sys_tbs_undo ADD DATAFILE 'undo002.dbf' size 1G autoextent on;
```
