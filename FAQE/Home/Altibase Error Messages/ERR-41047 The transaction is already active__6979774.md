---
title: "ERR-41047 The transaction is already active"
page_id: "6979774"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-41047+The+transaction+is+already+active"
updated_at: "2014-11-19T15:56:53.000+0900"
version: 5
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-41047 The transaction is already active
Source: https://docs.altibase.com/display/FAQE/ERR-41047+The+transaction+is+already+active
Updated: 2014-11-19T15:56:53.000+0900

- [Version](#ERR-41047Thetransactionisalreadyactive-Version)
- [Explanation](#ERR-41047Thetransactionisalreadyactive-Explanation)
- [Cause](#ERR-41047Thetransactionisalreadyactive-Cause)
- [Action](#ERR-41047Thetransactionisalreadyactive-Action)
- [Reference](#ERR-41047Thetransactionisalreadyactive-Reference)

## Version

All versions

## Explanation

Unable to transition to AUTOCOMMIT mode.

Unable to execute certain queries and SELECT statements on metadata.

## Cause

This error message is output if the user attempts to change to AUTOCOMMIT mode when a transaction that is not committed or rolled back exists

## Action

Change the commit mode after checking whether a previously processed transaction exists in the session and execute the COMMIT or ROLLBACK statement.

## Reference

N/A
