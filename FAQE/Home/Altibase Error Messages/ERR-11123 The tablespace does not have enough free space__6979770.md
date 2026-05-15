---
title: "ERR-11123 The tablespace does not have enough free space"
page_id: "6979770"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-11123+The+tablespace+does+not+have+enough+free+space"
updated_at: "2014-11-27T17:09:24.000+0900"
version: 8
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-11123 The tablespace does not have enough free space
Source: https://docs.altibase.com/display/FAQE/ERR-11123+The+tablespace+does+not+have+enough+free+space
Updated: 2014-11-27T17:09:24.000+0900

- [Version](#ERR-11123Thetablespacedoesnothaveenoughfreespace-Version)
- [Explanation](#ERR-11123Thetablespacedoesnothaveenoughfreespace-Explanation)
- [Cause](#ERR-11123Thetablespacedoesnothaveenoughfreespace-Cause)
- [Action](#ERR-11123Thetablespacedoesnothaveenoughfreespace-Action)
- [Reference](#ERR-11123Thetablespacedoesnothaveenoughfreespace-Reference)

## Version

All versions

## Explanation

Unable to additionally input or modify data using the INSERT or UPDATE statement.

## Cause

This error occurs when data input fails due to insufficient space in the tablespace.

## Action

1. Increase the tablespace size by adding a datafile to the tablespace on which the error has occurred.

2. If the undo tablespace caused the error, COMMIT/ROLLBACK operations are unsuccessfully carried out for a long time.

Check whether a transaction using undo tablespace exists.

Since DML operations fail due to insufficient space in the tablespace, try again after increasing the tablespace size.

## Reference

N/A
