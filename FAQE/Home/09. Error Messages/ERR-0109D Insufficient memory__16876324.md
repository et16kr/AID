---
title: "ERR-0109D Insufficient memory."
page_id: "16876324"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876324"
updated_at: "2021-03-25T11:13:44.000+0900"
version: 2
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# ERR-0109D Insufficient memory.
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876324
Updated: 2021-03-25T11:13:44.000+0900

- [Version](#ERR-0109DInsufficientmemory.-Version) - [Symptom](#ERR-0109DInsufficientmemory.-Symptom) - [Cause](#ERR-0109DInsufficientmemory.-Cause) - [Solution](#ERR-0109DInsufficientmemory.-Solution) - [Reference](#ERR-0109DInsufficientmemory.-Reference)

# Version

---

All versions

In the case of this error message, this error may occur for the same error cause or another error may occur depending on the Altibase version.

In addition, the cause of the error may be different depending on the version of Altibase for this error message.

# Symptom

---

# Example

```
create table t (c1 integer, c2 integer);
create table t2 (c1 integer, c2 integer);
create table t3 (c1 integer, c2 integer);
create index t_idx_01 on t(c1, c2);
create index t2_idx_01 on t2(c1, c2);
create index t3_idx_01 on t3(c1, c2);
insert into t select level, level from dual connect by level < 301;
insert into t2 select level, level from dual connect by level < 301;
insert into t3 select level, level from dual connect by level < 301;
alter system set EXECUTE_STMT_MEMORY_MAXIMUM = 1048576;
```

# Results from version 5.5.1 or later

```
iSQL> select count(*) from (select count(*) from t, t2, t3 group by t.c2, t2.c2, t3.c2);
[ERR-0109D : Insufficient memory]
```

# Result of execution in version 5.3.3

```
iSQL> select count(*) from (select count(*) from t, t2, t3 group by t.c2, t2.c2, t3.c2);
[ERR-01067 : The allocated memory size of statement exceeds the maximum limit ( Name : Query_Execute, Wanted Memory Size : 1114112, Max size : 1048576 ).]
```

# Cause

---

The description of the error can be checked using the altierr utility as follows.

$ altierr 0x0109D 0x0109D ( 4253) idERR_ABORT_InsufficientMemory Insufficient memory # *Cause: Insufficient memory # *Action: Please make sure that the system has enough available memory.

When performing queries such as order by and group by on a memory table, the temporary area is used. The temporary area also uses memory space.

This error occurs when the ALTIBASE HDB server makes a memory allocation request to execute a query and an error is returned by the EXECUTE_STMT_MEMORY_MAXIMUM attribute value.

# Solution

---

The value of the following property must be increased.

EXECUTE_STMT_MEMORY_MAXIMUM

Default value: 1G The unit is Gigabyte, and if the memory is used more than this attribute value in the execution step during query processing, an error is handled. This attribute value is set to a maximum value to prevent unnecessary memory growth.

1. If the error occurs during query execution, check the "EXECUTE_STMT_MEMORY_MAXIMUM" property value with the following SQL statement.

```
iSQL> set vertical on;
iSQL> select name, value1 from v$property where name='EXECUTE_STMT_MEMORY_MAXIMUM';
NAME   : EXECUTE_STMT_MEMORY_MAXIMUM
VALUE1 : 1073741824
```

2. Increase the property value appropriately with the ALTER statement. (The unit is byte.)

The following is an example of setting to 2G.

```
iSQL> alter system set EXECUTE_STMT_MEMORY_MAXIMUM = 2147483648;
Alter success.
```

3. The above command is applied to the entire server after execution, but it is applied as the setting value of the property file when Altibase is restarted.

Therefore, to apply it permanently, the property value must be changed in the property file as well.

Change the property value in the $ALTIBASE_HOME/conf/altibase.properties file as above.

# Reference

---

1. The EXECUTE_STMT_MEMORY_MAXIMUM property specifies the maximum value, and memory is not allocated as much as the preset value.

  However, the memory usage may increase as much as the set value, so be careful when setting it.

  Therefore, it is recommended to increase it appropriately empirically rather than setting it large in advance.
2. The "Insufficient memory" error can be a number of memory allocation failure errors in addition to the cases described here.

  Therefore, if the above solutions do not solve the problem, please contact Altibase Technical Support.
