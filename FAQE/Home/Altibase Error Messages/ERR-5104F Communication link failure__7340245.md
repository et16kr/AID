---
title: "ERR-5104F Communication link failure."
page_id: "7340245"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=7340245"
updated_at: "2014-10-28T10:38:15.000+0900"
version: 3
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-5104F Communication link failure.
Source: https://docs.altibase.com/pages/viewpage.action?pageId=7340245
Updated: 2014-10-28T10:38:15.000+0900

- [Version](#ERR-5104FCommunicationlinkfailure.-Version)
- [Explanation](#ERR-5104FCommunicationlinkfailure.-Explanation)
- [Cause](#ERR-5104FCommunicationlinkfailure.-Cause)
- [Action](#ERR-5104FCommunicationlinkfailure.-Action)
- [Reference](#ERR-5104FCommunicationlinkfailure.-Reference)

## Version

All versions

## Explanation

Unable to connect to database.

## Cause

This error means the session is disconnected from the query execution process. This is generally because the connection is lost due to a timeout policy. It can sometimes occur due to network problems.

## Action

1. Check whether the log contains information about any disconnected sessions from altibase_boot.log.

2. Check whether the cautions for thread programs were followed accordingly.

3. Check whether there was a problem in the network.

## Reference

N/A
