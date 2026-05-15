---
title: "ERR-01067 The memory size allocated for the statement has exceeded the maximum limit"
page_id: "6979765"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-01067+The+memory+size+allocated+for+the+statement+has+exceeded+the+maximum+limit"
updated_at: "2014-11-19T17:19:51.000+0900"
version: 10
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-01067 The memory size allocated for the statement has exceeded the maximum limit
Source: https://docs.altibase.com/display/FAQE/ERR-01067+The+memory+size+allocated+for+the+statement+has+exceeded+the+maximum+limit
Updated: 2014-11-19T17:19:51.000+0900

- [Version](#ERR-01067Thememorysizeallocatedforthestatementhasexceededthemaximumlimit-Version)
- [Explanation](#ERR-01067Thememorysizeallocatedforthestatementhasexceededthemaximumlimit-Explanation)
- [Cause](#ERR-01067Thememorysizeallocatedforthestatementhasexceededthemaximumlimit-Cause)
- [Action](#ERR-01067Thememorysizeallocatedforthestatementhasexceededthemaximumlimit-Action)
- [Reference](#ERR-01067Thememorysizeallocatedforthestatementhasexceededthemaximumlimit-Reference)
    - [1. PREPARE_STMT_MEMORY_MAXIMUM:](#ERR-01067Thememorysizeallocatedforthestatementhasexceededthemaximumlimit-1.PREPARE_STMT_MEMORY_MAXIMUM:)
    - [2. EXECUTE_STMT_MEMORY_MAXIMUM:](#ERR-01067Thememorysizeallocatedforthestatementhasexceededthemaximumlimit-2.EXECUTE_STMT_MEMORY_MAXIMUM:)

## Version

5.5.1 or above

# For 5.3.3, the following error message is output:

[ERR-01067 : The allocated memory size of statement exceeds the maximum limit ( Name : Query_Execute, Wanted Memory Size : 1114112, Max size : 1048576 ).]

## Explanation

This error occurs if query execution has stopped due to query preparation failure.

## Cause

The amount of memory used for query preparation exceeded PREPARE_STMT_MEMORY_MAXIMUM.

## Action

1. Tune the query to reduce memory usage. 2. Increase the memory usage for query execution with the ALTER SYSTEM command or altibase.properties file. 1)

```
iSQL> ALTER SYSTEM SET PREPARE_STMT_MEMORY_MAXIMUM = 419430400;
```

2) Change the value of PREPARE_STMT_MEMORY_MAXIMUM from $ALTIBASE_HOME/conf/altibase.properties.

## Reference

##### 1. PREPARE_STMT_MEMORY_MAXIMUM:

Check this property when query preparation has insufficient memory.

##### 2. EXECUTE_STMT_MEMORY_MAXIMUM:

Check this property to modify the size used by group functions.
