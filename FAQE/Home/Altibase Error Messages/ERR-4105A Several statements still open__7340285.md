---
title: "ERR-4105A Several statements still open"
page_id: "7340285"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-4105A+Several+statements+still+open"
updated_at: "2014-11-20T15:15:15.000+0900"
version: 7
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-4105A Several statements still open
Source: https://docs.altibase.com/display/FAQE/ERR-4105A+Several+statements+still+open
Updated: 2014-11-20T15:15:15.000+0900

- [Version](#ERR-4105ASeveralstatementsstillopen-Version)
- [Explanation](#ERR-4105ASeveralstatementsstillopen-Explanation)
- [Cause](#ERR-4105ASeveralstatementsstillopen-Cause)
- [Action](#ERR-4105ASeveralstatementsstillopen-Action)
- [Reference](#ERR-4105ASeveralstatementsstillopen-Reference)

## Version

All versions

## Explanation

Unable to execute query.

## Cause

This error occurs when a query (e.g., CREATE TABLE) is executed while the Fetch protocol is in progress.

## Action

The DDL statement has to be executed once CURSOR FETCH is complete in all sessions, or after closing all the open cursors, the code needs to be changed to enable DDL statements to be executed in other sessions.

## Reference

N/A
