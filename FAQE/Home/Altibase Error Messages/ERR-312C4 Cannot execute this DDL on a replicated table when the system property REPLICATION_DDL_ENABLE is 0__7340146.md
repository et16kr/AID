---
title: "ERR-312C4 Cannot execute this DDL on a replicated table when the system property REPLICATION_DDL_ENABLE is 0"
page_id: "7340146"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-312C4+Cannot+execute+this+DDL+on+a+replicated+table+when+the+system+property+REPLICATION_DDL_ENABLE+is+0"
updated_at: "2014-11-20T11:32:17.000+0900"
version: 4
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-312C4 Cannot execute this DDL on a replicated table when the system property REPLICATION_DDL_ENABLE is 0
Source: https://docs.altibase.com/display/FAQE/ERR-312C4+Cannot+execute+this+DDL+on+a+replicated+table+when+the+system+property+REPLICATION_DDL_ENABLE+is+0
Updated: 2014-11-20T11:32:17.000+0900

- [Version](#ERR-312C4CannotexecutethisDDLonareplicatedtablewhenthesystempropertyREPLICATION_DDL_ENABLEis0-Version)
- [Explanation](#ERR-312C4CannotexecutethisDDLonareplicatedtablewhenthesystempropertyREPLICATION_DDL_ENABLEis0-Explanation)
- [Cause](#ERR-312C4CannotexecutethisDDLonareplicatedtablewhenthesystempropertyREPLICATION_DDL_ENABLEis0-Cause)
- [Action](#ERR-312C4CannotexecutethisDDLonareplicatedtablewhenthesystempropertyREPLICATION_DDL_ENABLEis0-Action)
- [Reference](#ERR-312C4CannotexecutethisDDLonareplicatedtablewhenthesystempropertyREPLICATION_DDL_ENABLEis0-Reference)

## Version

All versions

## Explanation

Unable to execute DDL on replication tables.

## Cause

This error is due to DDL restrictions on replication tables.

## Action

Set REPLICATION_ENABLE to 1.

```
iSQL>ALTER SYSTEM SET REPLICATION _DDL_ENABLE = 1;
```

## Reference

It is not advisable to execute DDLs during replication. If the user wants to apply the REPLICATION_ENABLE property, we recommend that it is done only in the development stage and for the sake of convenience.

<How to execute DDLs in older versions>

The ALTER COLUMN statement is not supported for ALTIBASE HDB 5.3.3 or below and under certain circumstances, it is impossible to execute DDL statements. For example, a DDL statement that includes a table column position change or a DDL statement that is currently unsupported by Altibase cannot be executed as it is. In such cases, the user needs to back up the data of the replication target table before executing the DDL statement and recover the data afterwards.

In general, the user can take the following steps:

1. Stop services.

2. Check that the replication gap between the target nodes is 0.

3. Stop replication between the target nodes.

4. Remove the table from the replication table list.

5. Back up the table data using iLoader.

```
Shell> iloader formout –T table1 –f table1.fmt
Shell> iloader out –f table1.fmt –d table1.dat
```

6. Execute the DDL statement on the table.

7. Recover the table data using iLoader.

```
Shell> iloader in –f table1.fmt –d table1.dat
```

8. Add the table back to the replication table list.

9. Start replication between the target nodes.

Since data backup and recovery consume time, the user is recommended to estimate how long services will be stopped before performing the above operations.

Further information about iLoader options is available in the *iLoader User's Manual*.
