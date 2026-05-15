---
title: "ERR-61113 A replicated table must have a primary key."
page_id: "7340225"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=7340225"
updated_at: "2014-11-20T15:00:59.000+0900"
version: 4
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-61113 A replicated table must have a primary key.
Source: https://docs.altibase.com/pages/viewpage.action?pageId=7340225
Updated: 2014-11-20T15:00:59.000+0900

- [Version](#ERR-61113Areplicatedtablemusthaveaprimarykey.-Version)
- [Explanation](#ERR-61113Areplicatedtablemusthaveaprimarykey.-Explanation)
- [Cause](#ERR-61113Areplicatedtablemusthaveaprimarykey.-Cause)
- [Action](#ERR-61113Areplicatedtablemusthaveaprimarykey.-Action)
- [Reference](#ERR-61113Areplicatedtablemusthaveaprimarykey.-Reference)

## Version

6.3.1

## Explanation

Unable to start replication.

## Cause

This error occurs if there is no primary key in a replication target table.

## Action

Create a primary key on the replication target table.

## Reference

N/A
