---
title: "ERR-410B7 Invalid size of data to bind to a host variable Data Size"
page_id: "7340272"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-410B7+Invalid+size+of+data+to+bind+to+a+host+variable+Data+Size"
updated_at: "2014-11-27T17:17:41.000+0900"
version: 6
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-410B7 Invalid size of data to bind to a host variable Data Size
Source: https://docs.altibase.com/display/FAQE/ERR-410B7+Invalid+size+of+data+to+bind+to+a+host+variable+Data+Size
Updated: 2014-11-27T17:17:41.000+0900

- [Version](#ERR-410B7InvalidsizeofdatatobindtoahostvariableDataSize-Version)
- [Explanation](#ERR-410B7InvalidsizeofdatatobindtoahostvariableDataSize-Explanation)
- [Cause](#ERR-410B7InvalidsizeofdatatobindtoahostvariableDataSize-Cause)
- [Action](#ERR-410B7InvalidsizeofdatatobindtoahostvariableDataSize-Action)
- [Reference](#ERR-410B7InvalidsizeofdatatobindtoahostvariableDataSize-Reference)

## Version

All versions

## Explanation

Unable to execute query.

## Cause

Generally, this error occurs when a developer fails to initialize the variable or when there are incorrect values. It can also occur when binding sentence B rather than binding sentence A (after executing PREPARE) due to concurrency control failure in a thread environment. (Sentence A needs to be bound with 20 bytes but instead, sentence B is bound with 100 bytes, thus it is incorrectly handled.).

## Action

The user is advised to check whether the length exceeds the host variables output and verify that there are no problems with concurrency as part of the thread handling.

## Reference

N/A
