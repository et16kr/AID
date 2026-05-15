---
title: "ERR-31020 You cannot execute DDL on a replicated table"
page_id: "7340135"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-31020+You+cannot+execute+DDL+on+a+replicated+table"
updated_at: "2014-10-23T14:56:42.000+0900"
version: 3
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-31020 You cannot execute DDL on a replicated table
Source: https://docs.altibase.com/display/FAQE/ERR-31020+You+cannot+execute+DDL+on+a+replicated+table
Updated: 2014-10-23T14:56:42.000+0900

- [Version](#ERR-31020YoucannotexecuteDDLonareplicatedtable-Version)
- [Explanation](#ERR-31020YoucannotexecuteDDLonareplicatedtable-Explanation)
- [Cause](#ERR-31020YoucannotexecuteDDLonareplicatedtable-Cause)
- [Action](#ERR-31020YoucannotexecuteDDLonareplicatedtable-Action)
- [Reference](#ERR-31020YoucannotexecuteDDLonareplicatedtable-Reference)

## Version

All versions

## Explanation

Unable to execute DDL on table.

## Cause

This error occurs when a DDL statement is executed on a replication target table.

## Action

DDL statements cannot be directly executed on replication target tables.

Instead, the user should :

1. Stop replication on both servers.

2. Remove the table from the replication table list.

3. Execute the DDL statement on the table.

4. Once execution is complete, add the table back to the replication table list.

## Reference

N/A
