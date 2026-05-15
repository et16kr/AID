---
title: "ERR-51014 Function sequence error"
page_id: "7340763"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-51014+Function+sequence+error"
updated_at: "2014-11-27T17:51:39.000+0900"
version: 4
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-51014 Function sequence error
Source: https://docs.altibase.com/display/FAQE/ERR-51014+Function+sequence+error
Updated: 2014-11-27T17:51:39.000+0900

- [Version](#ERR-51014Functionsequenceerror-Version)
- [Explanation](#ERR-51014Functionsequenceerror-Explanation)
- [Cause](#ERR-51014Functionsequenceerror-Cause)
- [Action](#ERR-51014Functionsequenceerror-Action)
- [Reference](#ERR-51014Functionsequenceerror-Reference)

## Version

All versions

## Explanation

This is an application error.

## Cause

The function calling sequence is incorrect.

## Action

This is usually an application issue. Take the following steps:

1. Check whether concurrency is being controlled by the connection handles in the thread program.

2. Use cursors when executing the SELECT statement to check whether execution completes successfully after a timeout occurs, without raising an error.

3. Check whether functions are called in order.

4. Check whether the application has been debugged for memory invasion.

## Reference

N/A
