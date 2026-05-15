---
title: "ERR-61016 rpERR_ABORT_RP_SENDER_MAKE_XLOG Sender Failed to make an xlog"
page_id: "7340206"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-61016+rpERR_ABORT_RP_SENDER_MAKE_XLOG+Sender+Failed+to+make+an+xlog"
updated_at: "2014-11-20T13:54:19.000+0900"
version: 4
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-61016 rpERR_ABORT_RP_SENDER_MAKE_XLOG Sender Failed to make an xlog
Source: https://docs.altibase.com/display/FAQE/ERR-61016+rpERR_ABORT_RP_SENDER_MAKE_XLOG+Sender+Failed+to+make+an+xlog
Updated: 2014-11-20T13:54:19.000+0900

- [Version](#ERR-61016rpERR_ABORT_RP_SENDER_MAKE_XLOGSenderFailedtomakeanxlog-Version)
- [Explanation](#ERR-61016rpERR_ABORT_RP_SENDER_MAKE_XLOGSenderFailedtomakeanxlog-Explanation)
- [Cause](#ERR-61016rpERR_ABORT_RP_SENDER_MAKE_XLOGSenderFailedtomakeanxlog-Cause)
- [Action](#ERR-61016rpERR_ABORT_RP_SENDER_MAKE_XLOGSenderFailedtomakeanxlog-Action)
- [Reference](#ERR-61016rpERR_ABORT_RP_SENDER_MAKE_XLOGSenderFailedtomakeanxlog-Reference)

## Version

All versions

## Explanation

Replication is stopped.

## Cause

Altibase sends the replication information in the form of Xlogs.

Xlogs are included and managed by the Altibase redo log to guarantee the database transaction order.

This error occurs when there is a lack of disk space in the redo log area.

## Action

Check the directory and the disk space with the following SQL command.

```
iSQL> select value1 from v$property where name = 'LOG_DIR';

VALUE1
----------------------------------------------------------
/home/luj/altibase_home/logs

1 row selected
```

## Reference

A lack of disk space occurs, mainly because checkpointing is not executed for a long time or failed to execute. Thus, it is important to find out the cause of the error.
