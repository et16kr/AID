---
title: "ERR-61000 The received record was not found in the database"
page_id: "7340772"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-61000+The+received+record+was+not+found+in+the+database"
updated_at: "2014-11-27T17:51:07.000+0900"
version: 4
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-61000 The received record was not found in the database
Source: https://docs.altibase.com/display/FAQE/ERR-61000+The+received+record+was+not+found+in+the+database
Updated: 2014-11-27T17:51:07.000+0900

- [Version](#ERR-61000Thereceivedrecordwasnotfoundinthedatabase-Version)
- [Explanation](#ERR-61000Thereceivedrecordwasnotfoundinthedatabase-Explanation)
- [Cause](#ERR-61000Thereceivedrecordwasnotfoundinthedatabase-Cause)
- [Action](#ERR-61000Thereceivedrecordwasnotfoundinthedatabase-Action)
- [Reference](#ERR-61000Thereceivedrecordwasnotfoundinthedatabase-Reference)

## Version

All versions

## Explanation

Unable to execute DML statements on replication tables.

## Cause

This error occurs when an UPDATE statement is executed on replication table data of a different value or the primary key does not exist.

## Action

Check whether the data exists and then execute the statement.

## Reference

N/A
