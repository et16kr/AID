---
title: "ERR-610D2 The primary key column count of the replicated table does not match"
page_id: "7340220"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-610D2+The+primary+key+column+count+of+the+replicated+table+does+not+match"
updated_at: "2014-11-20T15:00:30.000+0900"
version: 4
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-610D2 The primary key column count of the replicated table does not match
Source: https://docs.altibase.com/display/FAQE/ERR-610D2+The+primary+key+column+count+of+the+replicated+table+does+not+match
Updated: 2014-11-20T15:00:30.000+0900

- [Version](#ERR-610D2Theprimarykeycolumncountofthereplicatedtabledoesnotmatch-Version)
- [Explanation](#ERR-610D2Theprimarykeycolumncountofthereplicatedtabledoesnotmatch-Explanation)
- [Cause](#ERR-610D2Theprimarykeycolumncountofthereplicatedtabledoesnotmatch-Cause)
- [Action](#ERR-610D2Theprimarykeycolumncountofthereplicatedtabledoesnotmatch-Action)
- [Reference](#ERR-610D2Theprimarykeycolumncountofthereplicatedtabledoesnotmatch-Reference)

## Version

4.3.9 or above

## Explanation

Unable to start replication.

## Cause

This error occurs if the primary key is different from the replication target table.

## Action

Set an identical value for the primary key on both servers.

## Reference

N/A
