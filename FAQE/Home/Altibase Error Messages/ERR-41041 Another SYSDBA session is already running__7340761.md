---
title: "ERR-41041 Another SYSDBA session is already running"
page_id: "7340761"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-41041+Another+SYSDBA+session+is+already+running"
updated_at: "2014-11-27T17:51:47.000+0900"
version: 5
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-41041 Another SYSDBA session is already running
Source: https://docs.altibase.com/display/FAQE/ERR-41041+Another+SYSDBA+session+is+already+running
Updated: 2014-11-27T17:51:47.000+0900

- [Version](#ERR-41041AnotherSYSDBAsessionisalreadyrunning-Version)
- [Explanation](#ERR-41041AnotherSYSDBAsessionisalreadyrunning-Explanation)
- [Cause](#ERR-41041AnotherSYSDBAsessionisalreadyrunning-Cause)
- [Action](#ERR-41041AnotherSYSDBAsessionisalreadyrunning-Action)
- [Reference](#ERR-41041AnotherSYSDBAsessionisalreadyrunning-Reference)

## Version

All versions

## Explanation

Unable to connect as SYSDBA.

## Cause

This error occurs if a client tries to connect to the database as SYSDBA when there already is another client connected as SYSDBA.

## Action

Only one client can be connected as SYSDBA per session.

1. Check whether a previously connected session exists.

2. If necessary, clean up the session.

3. Reconnect.

## Reference

N/A
