---
title: "ERR-61036 Receiver err_not found in deleteXlog()"
page_id: "7340210"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=7340210"
updated_at: "2014-11-27T17:20:28.000+0900"
version: 5
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-61036 Receiver err_not found in deleteXlog()
Source: https://docs.altibase.com/pages/viewpage.action?pageId=7340210
Updated: 2014-11-27T17:20:28.000+0900

- [Version](#ERR-61036Receivererr_notfoundindeleteXlog()-Version)
- [Explanation](#ERR-61036Receivererr_notfoundindeleteXlog()-Explanation)
- [Cause](#ERR-61036Receivererr_notfoundindeleteXlog()-Cause)
- [Action](#ERR-61036Receivererr_notfoundindeleteXlog()-Action)
- [Reference](#ERR-61036Receivererr_notfoundindeleteXlog()-Reference)

## Version

All versions

## Explanation

Unable to execute the DELETE statement.

## Cause

This error occurs when there is no data for the DELETE statement in a replication environment. -Not Found (with ERR-61000)

## Action

Verify that the data exists and execute the DELETE statement.

## Reference

N/A
