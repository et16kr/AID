---
title: "ERR-11118 The update log size '10485760' is bigger than TRX_UPDATE_MAX_LOGSIZE"
page_id: "6979741"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-11118+The+update+log+size+%2710485760%27+is+bigger+than+TRX_UPDATE_MAX_LOGSIZE"
updated_at: "2014-11-20T15:13:53.000+0900"
version: 11
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-11118 The update log size '10485760' is bigger than TRX_UPDATE_MAX_LOGSIZE
Source: https://docs.altibase.com/display/FAQE/ERR-11118+The+update+log+size+%2710485760%27+is+bigger+than+TRX_UPDATE_MAX_LOGSIZE
Updated: 2014-11-20T15:13:53.000+0900

- [Version](#ERR-11118Theupdatelogsize'10485760'isbiggerthanTRX_UPDATE_MAX_LOGSIZE-Version)
- [Explanation](#ERR-11118Theupdatelogsize'10485760'isbiggerthanTRX_UPDATE_MAX_LOGSIZE-Explanation)
- [Cause](#ERR-11118Theupdatelogsize'10485760'isbiggerthanTRX_UPDATE_MAX_LOGSIZE-Cause)
- [Action](#ERR-11118Theupdatelogsize'10485760'isbiggerthanTRX_UPDATE_MAX_LOGSIZE-Action)
- [Reference](#ERR-11118Theupdatelogsize'10485760'isbiggerthanTRX_UPDATE_MAX_LOGSIZE-Reference)

## Version

4.3.9 or above

## Explanation

Unable to execute an UPDATE statement.

## Cause

This error occurs when the size of the redo log which is generated when executing an UPDATE statement exceeds TRX_UPDATE_MAX_LOGSIZE.

The size of the redo log generated when executing an UPDATE statement can be much bigger than the record.

## Action

1. To fix this error, modify TRX_UPDATE_MAX_LOGSIZE with the following command:

```
ALTER SESSION SET TRX_UPDATE_MAX_LOGSIZE = 20480000;
```

2. Reduce the number of updates by using the LIMIT clause in the UPDATE statement and repeatedly execute smaller update operations.

For example, if there are 100,000 records to be updated, the LIMIT10000 clause repeatedly performs 10 update operations.

## Reference

1. If TRX_UPDATE_MAX_LOGSIZE is set to a high value, memory usage can increase to store images of previous versions of data using MVCC.

2. mem_gc can be delayed until the update is complete.

3. If TRX_UPDATE_MAX_LOGSIZE is set to a higher value than LOCK_ESCALATION_MEMORY_SIZE, a lock escalation can occur during an UPDATE operation.

In a lock escalation scenario, a SELECT operation fails if an IX lock converts to an X lock and as a consequence, all services may have to wait.

Therefore, the user is recommended to reduce the number of update operations, rather than increase TRX_UPDATE_MAX_LOGSIZE.
