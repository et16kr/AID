---
title: "ERR-11036 The data file is in use"
page_id: "6979796"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-11036+The+data+file+is+in+use"
updated_at: "2014-11-20T14:00:35.000+0900"
version: 11
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-11036 The data file is in use
Source: https://docs.altibase.com/display/FAQE/ERR-11036+The+data+file+is+in+use
Updated: 2014-11-20T14:00:35.000+0900

- [Version](#ERR-11036Thedatafileisinuse-Version)
- [Explanation](#ERR-11036Thedatafileisinuse-Explanation)
- [Cause](#ERR-11036Thedatafileisinuse-Cause)
- [Action](#ERR-11036Thedatafileisinuse-Action)
- [Reference](#ERR-11036Thedatafileisinuse-Reference)

## Version

All versions

## Explanation

The following error message is output when ALTER TABLESPACE ... DROP DATAFILE is executed:

```
iSQL> ALTER TABLESPACE SYS_TBS_DISK_DATA
    2 DROP DATAFILE '/altibase/dbs/DISK_DATA2.dbf';
```

[ERR-11036: The data file is in use.](#)

## Cause

The following error description can be viewed with the AltiErr utility:

$ altierr 0x0109D 0x11036 ( 69686) smERR_ABORT_CannotRemoveDataFileNode The data file is in use.

# *Cause: The data file is in use.

# *Action: Please remove an unnecessary data file.

Even if the user executed an INSERT statement and followed it with a DELETE statement so that all the datafiles can only have free pages, a previously used datafile cannot be dropped.

This error occurs when an attempt is made to drop a datafile that has previously been used.

Only datafiles that have never been used can be dropped.

## Action

It is impossible to drop a datafile that was used even once.

To drop a datafile, the tablespace must be recreated as below:

1. Export the data and object scripts that are created in the tablespace.

2. Drop and create the tablespace.

3. Import the data and create the object.

## Reference

N/A
