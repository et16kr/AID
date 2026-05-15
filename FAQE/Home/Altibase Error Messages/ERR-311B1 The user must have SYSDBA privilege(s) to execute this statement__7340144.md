---
title: "ERR-311B1 The user must have SYSDBA privilege(s) to execute this statement"
page_id: "7340144"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-311B1+The+user+must+have+SYSDBA+privilege%28s%29+to+execute+this+statement"
updated_at: "2014-10-24T11:36:51.000+0900"
version: 3
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-311B1 The user must have SYSDBA privilege(s) to execute this statement
Source: https://docs.altibase.com/display/FAQE/ERR-311B1+The+user+must+have+SYSDBA+privilege%28s%29+to+execute+this+statement
Updated: 2014-10-24T11:36:51.000+0900

- [Version](#ERR-311B1TheusermusthaveSYSDBAprivilege(s)toexecutethisstatement-Version)
- [Explanation](#ERR-311B1TheusermusthaveSYSDBAprivilege(s)toexecutethisstatement-Explanation)
- [Cause](#ERR-311B1TheusermusthaveSYSDBAprivilege(s)toexecutethisstatement-Cause)
- [Action](#ERR-311B1TheusermusthaveSYSDBAprivilege(s)toexecutethisstatement-Action)
- [Reference](#ERR-311B1TheusermusthaveSYSDBAprivilege(s)toexecutethisstatement-Reference)

## Version

All versions

## Explanation

Unable to execute query.

## Cause

This error occurs when a user without SYSDBA privileges performs an operation that requires the SYSDBA privilege.

## Action

Connect as SYSDBA or receive privileges from SYSDBA, and then perform the operation.

## Reference

N/A
