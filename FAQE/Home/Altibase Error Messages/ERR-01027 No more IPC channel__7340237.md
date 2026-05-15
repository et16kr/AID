---
title: "ERR-01027 No more IPC channel"
page_id: "7340237"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-01027+No+more+IPC+channel"
updated_at: "2014-11-20T15:04:22.000+0900"
version: 4
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-01027 No more IPC channel
Source: https://docs.altibase.com/display/FAQE/ERR-01027+No+more+IPC+channel
Updated: 2014-11-20T15:04:22.000+0900

- [Version](#ERR-01027NomoreIPCchannel-Version)
- [Explanation](#ERR-01027NomoreIPCchannel-Explanation)
- [Cause](#ERR-01027NomoreIPCchannel-Cause)
- [Action](#ERR-01027NomoreIPCchannel-Action)
- [Reference](#ERR-01027NomoreIPCchannel-Reference)

## Version

All versions

## Explanation

Unable to connect to IPC.

## Cause

Unable to establish connection as IPC_CHANNEL_COUNT has exceeded the maximum value.

## Action

Restart the server after increasing IPC_CHANNEL_COUNT.

## Reference

N/A
