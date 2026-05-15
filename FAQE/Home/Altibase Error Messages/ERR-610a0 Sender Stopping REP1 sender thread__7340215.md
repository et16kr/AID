---
title: "ERR-610a0 Sender Stopping REP1 sender thread"
page_id: "7340215"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-610a0+Sender+Stopping+REP1+sender+thread"
updated_at: "2014-10-28T09:30:00.000+0900"
version: 3
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-610a0 Sender Stopping REP1 sender thread
Source: https://docs.altibase.com/display/FAQE/ERR-610a0+Sender+Stopping+REP1+sender+thread
Updated: 2014-10-28T09:30:00.000+0900

- [Version](#ERR-610a0SenderStoppingREP1senderthread-Version)
- [Explanation](#ERR-610a0SenderStoppingREP1senderthread-Explanation)
- [Cause](#ERR-610a0SenderStoppingREP1senderthread-Cause)
- [Action](#ERR-610a0SenderStoppingREP1senderthread-Action)
- [Reference](#ERR-610a0SenderStoppingREP1senderthread-Reference)

## Version

All versions

## Explanation

Replication is stopped.

## Cause

If the existing number of logfiles exceeds REPLICATION_MAX_LOGFILE, Altibase stops replication and deletes all the log files preceding the Restart Redo Point. This error occurs when replication starts from a new Restart Redo Point.

## Action

Disable REPLICATION_MAX_LOGFILE or increase it.

## Reference

N/A
