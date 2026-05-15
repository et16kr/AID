---
title: "ERR-11049 Too many pages were allocated"
page_id: "6979809"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-11049+Too+many+pages+were+allocated"
updated_at: "2014-11-27T17:06:38.000+0900"
version: 11
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-11049 Too many pages were allocated
Source: https://docs.altibase.com/display/FAQE/ERR-11049+Too+many+pages+were+allocated
Updated: 2014-11-27T17:06:38.000+0900

- [Version](#ERR-11049Toomanypageswereallocated-Version)
- [Explanation](#ERR-11049Toomanypageswereallocated-Explanation)
- [Cause](#ERR-11049Toomanypageswereallocated-Cause)
- [Action](#ERR-11049Toomanypageswereallocated-Action)
- [Reference](#ERR-11049Toomanypageswereallocated-Reference)

## Version

All versions

## Explanation

- A server hang occurred when an INSERT, UPDATE or DELETE statement was executed.
- Unable to store data into memory tablespace.

## Cause

- The memory database exceeded the size limit.
- For memory tablespaces in Altibase, the sum of all the memory tablespaces cannot exceed MEM_MAX_DB_SIZE. Thus, this error occurs when all the memory space is used.

## Action

The user must drop the unnecessary table(s) or increase MEM_MAX_DB_SIZE and restart the Altibase server. After that, check why the memory tablespace usage was increased, and whether there was a large number of selected or altered data for each table.

## Reference

N/A
