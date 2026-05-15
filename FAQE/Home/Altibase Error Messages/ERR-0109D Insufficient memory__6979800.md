---
title: "ERR-0109D Insufficient memory"
page_id: "6979800"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-0109D+Insufficient+memory"
updated_at: "2014-11-27T17:06:02.000+0900"
version: 18
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-0109D Insufficient memory
Source: https://docs.altibase.com/display/FAQE/ERR-0109D+Insufficient+memory
Updated: 2014-11-27T17:06:02.000+0900

- [Version](#ERR-0109DInsufficientmemory-Version)
- [Explanation](#ERR-0109DInsufficientmemory-Explanation)
- [Cause](#ERR-0109DInsufficientmemory-Cause)
- [Action](#ERR-0109DInsufficientmemory-Action)
- [Reference](#ERR-0109DInsufficientmemory-Reference)

## Version

All versions

## Explanation

Unable to execute query.

This error occurs when the execution of a certain query fails due to insufficient temporary memory.

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

# 5.5.1 or above

```
iSQL> select count(*) from (select count(*) from t, t2, t3 group by t.c2, t2.c2, t3.c2);
```

ERR-0109D : Insufficient memory

# 5.3.3

```
iSQL> select count(*) from (select count(*) from t, t2, t3 group by t.c2, t2.c2, t3.c2);
```

[ERR-01067 : The allocated memory size of statement exceeds the maximum limit ( Name : Query_Execute, Wanted Memory Size : 1114112, Max size : 1048576 ).|"linktype="raw" wikidestination="" originalalias="ERR-01067 : The allocated memory size of statement exceeds the maximum limit ( Name : Query_Execute, Wanted Memory Size : 1114112, Max size : 1048576 ).|" class="linkerror" >ERR-01067 : The allocated memory size of statement exceeds the maximum limit ( Name : Query_Execute, Wanted Memory Size : 1114112, Max size : 1048576 ).|||||||||\\](https://docs.altibase.com/display/FAQE/ERR-0109D+Insufficient+memory)

## Cause

The following error description can be viewed with the AltiErr utility:

$ altierr 0x0109D 0x0109D ( 4253) idERR_ABORT_InsufficientMemory Insufficient memory

# *Cause: Insufficient memory

# *Action: Please make sure that the system has enough available memory.

The temporary area is used when executing a query including a GROUP BY or ORDER BY clause for memory. However, this temporary area also uses memory.

This error occurs due to EXECUTE_STMT_MEMORY_MAXIMUM while allocating memory to execute a query.

## Action

Altibase uses memory space for temporary memory tables, instead of disk space.

Consequently, the necessary memory space must be secured at query execution with the following property:

```
EXECUTE_STMT_MEMORY_MAXIMUM (default value: 1G)
```

The unit is bytes and an error occurs if more memory than the value specified for this property is used during the execution stage of query execution.

This property is set as the maximum value to prevent unnecessary memory increase.

**<How to Fix the Error>**

1. Check the increase in Query_Execute.

```
iSQL> SELECT * FROM v$memstat WHERE name = 'Query_Execute';
NAME          ALLOC_SIZE   ALLOC_COUNT   MAX_TOTAL_SIZE
----------------------------------------------------------------------------------------------------
Query_Execute  5091105640          75431       5091105640
```

2. Check the current value of EXECUTE_STMT_MEMORY_MAXIMUM

```
iSQL> set vertical on;
iSQL> select name, value1 from v$property where name='EXECUTE_STMT_MEMORY_MAXIMUM';
NAME   : EXECUTE_STMT_MEMORY_MAXIMUM
VALUE1 : 1073741824
```

3. Using the ALTER statement, set a value (in bytes) larger than ALLOC_SIZE for EXECUTE_STMT_MEMORY_MAXIMUM.

Set an appropriate value by estimating how much the execution space will extend for the query.

```
iSQL> ALTER SYSTEM SET EXECUTE_STMT_MEMORY_MAXIMUM=5368709120; (5G)
Alter success.
```

4. To apply the change permanently, the value has to be changed in the altibase.properties file as well($ALTIBASE_HOME/conf/altibase.properties).

## Reference

The EXECUTE_STMT_MEMORY_MAXIMUM property specifies the maximum memory that a single statement can use for execution, not the pre-allocation memory that a single statement can use.

Memory usage can increase as much as specified by the property. Therefore, the user is recommended to set an appropriate value.
