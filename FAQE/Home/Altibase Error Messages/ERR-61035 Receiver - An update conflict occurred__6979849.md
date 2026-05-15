---
title: "ERR-61035 Receiver - An update conflict occurred"
page_id: "6979849"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-61035+Receiver+-+An+update+conflict+occurred"
updated_at: "2014-10-20T09:45:58.000+0900"
version: 6
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-61035 Receiver - An update conflict occurred
Source: https://docs.altibase.com/display/FAQE/ERR-61035+Receiver+-+An+update+conflict+occurred
Updated: 2014-10-20T09:45:58.000+0900

- [Version](#ERR-61035Receiver-Anupdateconflictoccurred-Version)
- [Explanation](#ERR-61035Receiver-Anupdateconflictoccurred-Explanation)
- [Cause](#ERR-61035Receiver-Anupdateconflictoccurred-Cause)
- [Action](#ERR-61035Receiver-Anupdateconflictoccurred-Action)
- [Reference](#ERR-61035Receiver-Anupdateconflictoccurred-Reference)

## Version

All versions

## Explanation

A replication update conflict occurred

## Cause

1. The data that needs to be updated does not exist.

2. The target value is different.

## Action

This error occurred when a replication object tried to change data that has already been changed.

This is a common message. If you want to revert to the value of the target server, you must change the property and start the server again.

REPLICATION_UPDATE_REPLACE=1 ($ALTIBASE_HOME/conf/altibase.properties)

## Reference

N/A
