---
title: "ERR-61100 rpERR_ABORT_RPC_DUPLICATE_REPLICATION Duplicate replication names. The replication name already exists in the database."
page_id: "6979851"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=6979851"
updated_at: "2014-10-20T09:46:10.000+0900"
version: 6
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-61100 rpERR_ABORT_RPC_DUPLICATE_REPLICATION Duplicate replication names. The replication name already exists in the database.
Source: https://docs.altibase.com/pages/viewpage.action?pageId=6979851
Updated: 2014-10-20T09:46:10.000+0900

- [Version](#ERR-61100rpERR_ABORT_RPC_DUPLICATE_REPLICATIONDuplicatereplicationnames.Thereplicationnamealreadyexistsinthedatabase.-Version)
- [Explanation](#ERR-61100rpERR_ABORT_RPC_DUPLICATE_REPLICATIONDuplicatereplicationnames.Thereplicationnamealreadyexistsinthedatabase.-Explanation)
- [Cause](#ERR-61100rpERR_ABORT_RPC_DUPLICATE_REPLICATIONDuplicatereplicationnames.Thereplicationnamealreadyexistsinthedatabase.-Cause)
- [Action](#ERR-61100rpERR_ABORT_RPC_DUPLICATE_REPLICATIONDuplicatereplicationnames.Thereplicationnamealreadyexistsinthedatabase.-Action)
- [Reference](#ERR-61100rpERR_ABORT_RPC_DUPLICATE_REPLICATIONDuplicatereplicationnames.Thereplicationnamealreadyexistsinthedatabase.-Reference)

## Version

All versions

## Explanation

Unable to create a replication object.

## Cause

A replication object using the same object name, IP or PORT number exists.

## Action

Neither change the object name nor permit the duplicate IP or PORT number.

Increase the number of network cards as needed.

## Reference

N/A
