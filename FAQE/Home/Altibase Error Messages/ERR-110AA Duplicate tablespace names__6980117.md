---
title: "ERR-110AA Duplicate tablespace names"
page_id: "6980117"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-110AA+Duplicate+tablespace+names"
updated_at: "2014-10-27T13:36:41.000+0900"
version: 4
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-110AA Duplicate tablespace names
Source: https://docs.altibase.com/display/FAQE/ERR-110AA+Duplicate+tablespace+names
Updated: 2014-10-27T13:36:41.000+0900

- [Version](#ERR-110AADuplicatetablespacenames-Version)
- [Explanation](#ERR-110AADuplicatetablespacenames-Explanation)
- [Cause](#ERR-110AADuplicatetablespacenames-Cause)
- [Action](#ERR-110AADuplicatetablespacenames-Action)
- [Reference](#ERR-110AADuplicatetablespacenames-Reference)

## Version

All versions

## Explanation

Unable to create tablespace.

## Cause

This error occurs when a tablespace with an existing name is created.

## Action

1. Check the name of the tablespace that is currently being used.

```
iSQL> SELECT name FROM v$tablespaces;
NAME
--------------------------------------------
SYS_TBS_MEM_DIC
SYS_TBS_MEM_DATA
SYS_TBS_DISK_DATA
SYS_TBS_DISK_UNDO
SYS_TBS_DISK_TEMP
VOL_TBS1
VOL_TBS2
MEM_TBS1
DISK_TBS1
```

2. Re-create the tablespace with a distinct name.

## Reference

N/A
