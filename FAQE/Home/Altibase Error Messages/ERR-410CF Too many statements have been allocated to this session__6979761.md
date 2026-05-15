---
title: "ERR-410CF Too many statements have been allocated to this session"
page_id: "6979761"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-410CF+Too+many+statements+have+been+allocated+to+this+session"
updated_at: "2014-10-20T09:47:28.000+0900"
version: 5
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-410CF Too many statements have been allocated to this session
Source: https://docs.altibase.com/display/FAQE/ERR-410CF+Too+many+statements+have+been+allocated+to+this+session
Updated: 2014-10-20T09:47:28.000+0900

- [Version](#ERR-410CFToomanystatementshavebeenallocatedtothissession-Version)
- [Explanation](#ERR-410CFToomanystatementshavebeenallocatedtothissession-Explanation)
- [Cause](#ERR-410CFToomanystatementshavebeenallocatedtothissession-Cause)
- [Action](#ERR-410CFToomanystatementshavebeenallocatedtothissession-Action)
- [Reference](#ERR-410CFToomanystatementshavebeenallocatedtothissession-Reference)

## Version

5.3.3 or above

## Explanation

Unable to execute the query.

## Cause

This error message is output when the number of queries allocated to a single session for preparation exceeded the limit.

## Action

1. Check the prepared queries of the session to determine whether the session is running normally and increase MAX_STATEMENTS_PER_SESSION.

2. Check whether the application is closing statements.

## Reference

N/A
