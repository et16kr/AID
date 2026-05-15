---
title: "ERR-31240 Invalid request to process SQL statement"
page_id: "7340268"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-31240+Invalid+request+to+process+SQL+statement"
updated_at: "2014-11-20T15:09:12.000+0900"
version: 4
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-31240 Invalid request to process SQL statement
Source: https://docs.altibase.com/display/FAQE/ERR-31240+Invalid+request+to+process+SQL+statement
Updated: 2014-11-20T15:09:12.000+0900

- [Version](#ERR-31240InvalidrequesttoprocessSQLstatement-Version)
- [Explanation](#ERR-31240InvalidrequesttoprocessSQLstatement-Explanation)
- [Cause](#ERR-31240InvalidrequesttoprocessSQLstatement-Cause)
- [Action](#ERR-31240InvalidrequesttoprocessSQLstatement-Action)
- [Reference](#ERR-31240InvalidrequesttoprocessSQLstatement-Reference)

## Version

All versions

## Explanation

Unable to create a program that has thread architecture.

## Cause

This usually happens in the thread architecture program and sometimes concurrency control for the thread connection object is not performed properly. When this happens, the protocols to be exchanged between the Altibase server and client can be in the wrong order.

## Action

First, if the structure of the program is a thread, you must check whether concurrency control was performed properly or the query is executed in the following order: PREPARE > BINDING > EXECUTE.

## Reference

N/A
