---
title: "ERR-266447 mmERR_ABORT_TOO_MANY_STATEMENTS_IN_THE_SESSION"
page_id: "7340133"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-266447+mmERR_ABORT_TOO_MANY_STATEMENTS_IN_THE_SESSION"
updated_at: "2014-11-20T11:19:20.000+0900"
version: 5
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-266447 mmERR_ABORT_TOO_MANY_STATEMENTS_IN_THE_SESSION
Source: https://docs.altibase.com/display/FAQE/ERR-266447+mmERR_ABORT_TOO_MANY_STATEMENTS_IN_THE_SESSION
Updated: 2014-11-20T11:19:20.000+0900

- [Version](#ERR-266447mmERR_ABORT_TOO_MANY_STATEMENTS_IN_THE_SESSION-Version)
- [Explanation](#ERR-266447mmERR_ABORT_TOO_MANY_STATEMENTS_IN_THE_SESSION-Explanation)
- [Cause](#ERR-266447mmERR_ABORT_TOO_MANY_STATEMENTS_IN_THE_SESSION-Cause)
- [Action](#ERR-266447mmERR_ABORT_TOO_MANY_STATEMENTS_IN_THE_SESSION-Action)
- [Reference](#ERR-266447mmERR_ABORT_TOO_MANY_STATEMENTS_IN_THE_SESSION-Reference)

## Version

All versions

## Explanation

Unable to execute query.

## Cause

This error occurs if QUERY_STACK_SIZE is insufficient when a statement has not been properly closed.

## Action

Check whether the statement is closed properly after query execution or increase QUERY_STACK_SIZE.

## Reference

N/A
