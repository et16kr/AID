---
title: "ERR-11098 smERR_ABORT_BackupLogMode cannot be executed in no archive log mode"
page_id: "6980107"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-11098+smERR_ABORT_BackupLogMode+cannot+be+executed+in+no+archive+log+mode"
updated_at: "2014-11-20T10:52:04.000+0900"
version: 7
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-11098 smERR_ABORT_BackupLogMode cannot be executed in no archive log mode
Source: https://docs.altibase.com/display/FAQE/ERR-11098+smERR_ABORT_BackupLogMode+cannot+be+executed+in+no+archive+log+mode
Updated: 2014-11-20T10:52:04.000+0900

- [Version](#ERR-11098smERR_ABORT_BackupLogModecannotbeexecutedinnoarchivelogmode-Version)
- [Explanation](#ERR-11098smERR_ABORT_BackupLogModecannotbeexecutedinnoarchivelogmode-Explanation)
- [Cause](#ERR-11098smERR_ABORT_BackupLogModecannotbeexecutedinnoarchivelogmode-Cause)
- [Action](#ERR-11098smERR_ABORT_BackupLogModecannotbeexecutedinnoarchivelogmode-Action)
- [Reference](#ERR-11098smERR_ABORT_BackupLogModecannotbeexecutedinnoarchivelogmode-Reference)

## Version

All versions

## Explanation

Unable to perform an online backup.

## Cause

An online backup has been performed in NO ARCHIVING mode.

## Action

An online backup can only be performed in ARCHIVING mode. Otherwise, an error occurs.

Check whether the database is running in ARCHIVING mode with the following command:

```
iSQL>select archivelog_mode from v$log;
ARCHIVELOG_MODE
------------------------
NOARCHIVE
```

**<How to change to ARCHIVING mode from NOARCHIVING mode>**

1. Shut down the database.

2. Re-start the database.

3. Run the database in the CONTROL phase.

```
SHELL>server stop
SHELL>is –silent –sysdba
```

ERR-910FB : Connected to idle instance

```
isql(sysdba)>startup control
```

4. Change to ARCHIVING mode using the ALTER DATABASE ARCHIVELOG statement.

```
isql(sysdba)>alter database archivelog
```

**<Execute an online backup in ARCHIVING MODE>**

1. Run the database in the SERVICE phase.

```
isql(sysdba)>startup service
```

2. Re-start backup.

## Reference

N/A
