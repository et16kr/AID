---
title: "ERR-11118 The update log size '…' is bigger than TRX_UPDATE_MAX_LOGSIZE '…'"
page_id: "7340281"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=7340281"
updated_at: "2014-11-19T10:19:00.000+0900"
version: 6
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-11118 The update log size '…' is bigger than TRX_UPDATE_MAX_LOGSIZE '…'
Source: https://docs.altibase.com/pages/viewpage.action?pageId=7340281
Updated: 2014-11-19T10:19:00.000+0900

- [Version](#ERR-11118Theupdatelogsize'…'isbiggerthanTRX_UPDATE_MAX_LOGSIZE'…'-Version)
- [Explanation](#ERR-11118Theupdatelogsize'…'isbiggerthanTRX_UPDATE_MAX_LOGSIZE'…'-Explanation)
- [Cause](#ERR-11118Theupdatelogsize'…'isbiggerthanTRX_UPDATE_MAX_LOGSIZE'…'-Cause)
- [Action](#ERR-11118Theupdatelogsize'…'isbiggerthanTRX_UPDATE_MAX_LOGSIZE'…'-Action)
- [Reference](#ERR-11118Theupdatelogsize'…'isbiggerthanTRX_UPDATE_MAX_LOGSIZE'…'-Reference)

## Version

All versions

## Explanation

This error occurs when there is a bulk modifying operation.

This error message applies only to memory tables.

## Cause

In Altibase, this error occurs and the ROLLBACK is executed for the corresponding transaction when the number of redo log files due to bulk transactions exceeds TRX_UPDATE_MAX_LOGSIZE (The TRX_UPDATE_MAX_LOGSIZE property restricts the number of log files created by a DML statement.).

## Action

If the transaction has to be executed with a single query only, the user is advised to change the property in a session level as follows.

```
ALTER SESSION SET TRX_UPDATE_MAX_LOGSIZE = 0; (Disabling property)
```

However, the user should remember that the number of redo logfiles will increase and this might cause a disk full error. Also, when executing bulk operations, an X lock is acquired in a table to prevent resource increase due to MVCC. Thus, caution is advised that any SELECT or DML statements might have to wait for an X lock to be released.

## Reference

N/A
