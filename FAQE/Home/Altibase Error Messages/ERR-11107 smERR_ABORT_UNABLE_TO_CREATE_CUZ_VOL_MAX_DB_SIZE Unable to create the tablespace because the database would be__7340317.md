---
title: "ERR-11107 smERR_ABORT_UNABLE_TO_CREATE_CUZ_VOL_MAX_DB_SIZE Unable to create the tablespace because the database would be larger than VOLATILE_MAX_DB_SIZE"
page_id: "7340317"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=7340317"
updated_at: "2014-11-20T15:20:40.000+0900"
version: 5
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-11107 smERR_ABORT_UNABLE_TO_CREATE_CUZ_VOL_MAX_DB_SIZE Unable to create the tablespace because the database would be larger than VOLATILE_MAX_DB_SIZE
Source: https://docs.altibase.com/pages/viewpage.action?pageId=7340317
Updated: 2014-11-20T15:20:40.000+0900

- [Version](#ERR-11107smERR_ABORT_UNABLE_TO_CREATE_CUZ_VOL_MAX_DB_SIZEUnabletocreatethetablespacebecausethedatabasewouldbelargerthanVOLATILE_MAX_DB_SIZE-Version)
- [Explanation](#ERR-11107smERR_ABORT_UNABLE_TO_CREATE_CUZ_VOL_MAX_DB_SIZEUnabletocreatethetablespacebecausethedatabasewouldbelargerthanVOLATILE_MAX_DB_SIZE-Explanation)
- [Cause](#ERR-11107smERR_ABORT_UNABLE_TO_CREATE_CUZ_VOL_MAX_DB_SIZEUnabletocreatethetablespacebecausethedatabasewouldbelargerthanVOLATILE_MAX_DB_SIZE-Cause)
- [Action](#ERR-11107smERR_ABORT_UNABLE_TO_CREATE_CUZ_VOL_MAX_DB_SIZEUnabletocreatethetablespacebecausethedatabasewouldbelargerthanVOLATILE_MAX_DB_SIZE-Action)
- [Reference](#ERR-11107smERR_ABORT_UNABLE_TO_CREATE_CUZ_VOL_MAX_DB_SIZEUnabletocreatethetablespacebecausethedatabasewouldbelargerthanVOLATILE_MAX_DB_SIZE-Reference)

## Version

5.1.1. or above

## Explanation

Unable to execute DML statements.

## Cause

This error occurs when creating a volatile tablespace larger than VOLATILE_MAX_DB_SIZE.

## Action

1. Increase VOLATILE_MAX_DB_SIZE (to a value larger than the actual usage) in $ALTIBASE_HOME/conf/altibase.properties.
2. Restart the Altibase server.

The user is recommended to set the maximum value of VOLATILE_MAX_DB_SIZE to the sum of MEM_MAX_DB_SIZE and VOLATILE_MAX_DB_SIZE which accounts for less than 60~70% of physical memory.

## Reference

N/A
