---
title: "ERR-0001c Unable to shutdown the communication channel"
page_id: "7340235"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-0001c+Unable+to+shutdown+the+communication+channel"
updated_at: "2014-11-20T15:04:00.000+0900"
version: 4
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-0001c Unable to shutdown the communication channel
Source: https://docs.altibase.com/display/FAQE/ERR-0001c+Unable+to+shutdown+the+communication+channel
Updated: 2014-11-20T15:04:00.000+0900

- [Version](#ERR-0001cUnabletoshutdownthecommunicationchannel-Version)
- [Explanation](#ERR-0001cUnabletoshutdownthecommunicationchannel-Explanation)
- [Cause](#ERR-0001cUnabletoshutdownthecommunicationchannel-Cause)
- [Action](#ERR-0001cUnabletoshutdownthecommunicationchannel-Action)
- [Reference](#ERR-0001cUnabletoshutdownthecommunicationchannel-Reference)

## Version

All versions

## Explanation

Unable to connect to session.

## Cause

The network is disconnected or the client has a problem.

## Action

This error message is just a notification saying that the database server detected and tried to disconnect an abnormal connection. The client did not exist, so the session was closed.

The internal thread (CM detector) which checks abnormal connections is closing the connection. Thus, no action is required.

## Reference

N/A
