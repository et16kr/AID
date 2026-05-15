---
title: "ERR-61023 rpERR_ABORT_RP_REPLICATION_DISABLED Replication is disabled"
page_id: "7340208"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-61023+rpERR_ABORT_RP_REPLICATION_DISABLED+Replication+is+disabled"
updated_at: "2014-11-20T15:17:59.000+0900"
version: 5
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-61023 rpERR_ABORT_RP_REPLICATION_DISABLED Replication is disabled
Source: https://docs.altibase.com/display/FAQE/ERR-61023+rpERR_ABORT_RP_REPLICATION_DISABLED+Replication+is+disabled
Updated: 2014-11-20T15:17:59.000+0900

- [Version](#ERR-61023rpERR_ABORT_RP_REPLICATION_DISABLEDReplicationisdisabled-Version)
- [Explanation](#ERR-61023rpERR_ABORT_RP_REPLICATION_DISABLEDReplicationisdisabled-Explanation)
- [Cause](#ERR-61023rpERR_ABORT_RP_REPLICATION_DISABLEDReplicationisdisabled-Cause)
- [Action](#ERR-61023rpERR_ABORT_RP_REPLICATION_DISABLEDReplicationisdisabled-Action)
- [Reference](#ERR-61023rpERR_ABORT_RP_REPLICATION_DISABLEDReplicationisdisabled-Reference)

## Version

All versions

## Explanation

Unable to create a replication object.

## Cause

The replication port needs to be changed.

## Action

The replication port is set to 0 by default. This needs to be changed to a value other than ‘20300’ (the database default port). Once it is changed, the database has to be restarted and replication can be used again.

## Reference

N/A
