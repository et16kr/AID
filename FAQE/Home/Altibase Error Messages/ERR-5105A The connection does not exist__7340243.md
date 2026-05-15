---
title: "ERR-5105A The connection does not exist."
page_id: "7340243"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=7340243"
updated_at: "2014-10-28T10:36:51.000+0900"
version: 3
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-5105A The connection does not exist.
Source: https://docs.altibase.com/pages/viewpage.action?pageId=7340243
Updated: 2014-10-28T10:36:51.000+0900

- [Version](#ERR-5105ATheconnectiondoesnotexist.-Version)
- [Explanation](#ERR-5105ATheconnectiondoesnotexist.-Explanation)
- [Cause](#ERR-5105ATheconnectiondoesnotexist.-Cause)
- [Action](#ERR-5105ATheconnectiondoesnotexist.-Action)
- [Reference](#ERR-5105ATheconnectiondoesnotexist.-Reference)

## Version

All versions

## Explanation

Unable to execute query.

## Cause

This error occurs when the database is not connected or it is trying to handle a query while it is disconnected.

1. When executing a query while connection is lost due to a timeout policy.

2. A unique connection name is used which does not exist for the thread program.

## Action

1. Shorten the processing time by increasing the session timeout or tune the query.

2. Check whether a unique connection exists when using a thread program.

## Reference

N/A
