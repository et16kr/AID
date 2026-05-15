---
title: "ERR-410D5 Client unable to establish connection."
page_id: "6979736"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=6979736"
updated_at: "2014-11-19T10:52:42.000+0900"
version: 7
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-410D5 Client unable to establish connection.
Source: https://docs.altibase.com/pages/viewpage.action?pageId=6979736
Updated: 2014-11-19T10:52:42.000+0900

- [Version](#ERR-410D5Clientunabletoestablishconnection.-Version)
- [Explanation](#ERR-410D5Clientunabletoestablishconnection.-Explanation)
- [Cause](#ERR-410D5Clientunabletoestablishconnection.-Cause)
- [Action](#ERR-410D5Clientunabletoestablishconnection.-Action)
- [Reference](#ERR-410D5Clientunabletoestablishconnection.-Reference)

## Version

5.5.1 or above

## Explanation

Unable to connect to database.

## Cause

1. A general user cannot connect with IPC as there is an IPC channel for sysdba only.

2. Altibase port or connection method (TCP/UNIX/IPC) is incorrect or is blocked by a firewall.

## Action

Clean up unnecessary IPC sessions:

Check the IPC session information from V$SESSION and clean up if there are unnecessary sessions connected, then get another IPC channel and re-connect.

## Reference

<How to change the IPC_CHANNEL_COUNT>

Search the IPC_CHANNEL_COUNT from $ALTIBASE_HOME/conf/altibase.properties, then change it and restart the database.
