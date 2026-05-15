---
title: "ERR-31088 A replicated table must have a primary key"
page_id: "6979805"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-31088+A+replicated+table+must+have+a+primary+key"
updated_at: "2014-10-20T09:48:56.000+0900"
version: 5
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-31088 A replicated table must have a primary key
Source: https://docs.altibase.com/display/FAQE/ERR-31088+A+replicated+table+must+have+a+primary+key
Updated: 2014-10-20T09:48:56.000+0900

- [Version](#ERR-31088Areplicatedtablemusthaveaprimarykey-Version)
- [Explanation](#ERR-31088Areplicatedtablemusthaveaprimarykey-Explanation)
- [Cause](#ERR-31088Areplicatedtablemusthaveaprimarykey-Cause)
- [Action](#ERR-31088Areplicatedtablemusthaveaprimarykey-Action)
- [Reference](#ERR-31088Areplicatedtablemusthaveaprimarykey-Reference)

## Version

All versions

## Explanation

Unable to perform replication.

## Cause

This error message is output if the replicated table does not have a primary key.

## Action

One of the replication restrictions is that a replicated table must have a primary key column.

This is because primary key columns are used to check data consistency.

To fix this error, use the ALTER TABLE statement to create a primary key column and try again.

## Reference

N/A
