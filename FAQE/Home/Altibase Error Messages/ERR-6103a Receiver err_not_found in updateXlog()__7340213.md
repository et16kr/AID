---
title: "ERR-6103a Receiver err_not_found in updateXlog()"
page_id: "7340213"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=7340213"
updated_at: "2014-11-27T17:20:48.000+0900"
version: 4
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-6103a Receiver err_not_found in updateXlog()
Source: https://docs.altibase.com/pages/viewpage.action?pageId=7340213
Updated: 2014-11-27T17:20:48.000+0900

- [Version](#ERR-6103aReceivererr_not_foundinupdateXlog()-Version)
- [Explanation](#ERR-6103aReceivererr_not_foundinupdateXlog()-Explanation)
- [Cause](#ERR-6103aReceivererr_not_foundinupdateXlog()-Cause)
- [Action](#ERR-6103aReceivererr_not_foundinupdateXlog()-Action)
- [Reference](#ERR-6103aReceivererr_not_foundinupdateXlog()-Reference)

## Version

All versions

## Explanation

Unable to execute the UPDATE statement.

## Cause

This error occurs when there is no data found for the UPDATE statement in a replication environment. -Not Found (withERR-61000)

## Action

Verify that the data exists and execute the UPDATE statement.

## Reference

N/A
