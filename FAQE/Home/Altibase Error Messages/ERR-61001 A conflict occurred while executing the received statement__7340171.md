---
title: "ERR-61001 A conflict occurred while executing the received statement"
page_id: "7340171"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-61001+A+conflict+occurred+while+executing+the+received+statement"
updated_at: "2014-11-20T13:52:01.000+0900"
version: 6
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-61001 A conflict occurred while executing the received statement
Source: https://docs.altibase.com/display/FAQE/ERR-61001+A+conflict+occurred+while+executing+the+received+statement
Updated: 2014-11-20T13:52:01.000+0900

- [Version](#ERR-61001Aconflictoccurredwhileexecutingthereceivedstatement-Version)
- [Explanation](#ERR-61001Aconflictoccurredwhileexecutingthereceivedstatement-Explanation)
- [Cause](#ERR-61001Aconflictoccurredwhileexecutingthereceivedstatement-Cause)
- [Action](#ERR-61001Aconflictoccurredwhileexecutingthereceivedstatement-Action)
- [Reference](#ERR-61001Aconflictoccurredwhileexecutingthereceivedstatement-Reference)

## Version

All versions

## Explanation

Unable to update a replication table.

## Cause

This error occurs when an UPDATE statement is executed on replication table data of a different value.

This error message is output with ERR-61035.

## Action

Check whether the data exists and then execute the statement.

## Reference

N/A
