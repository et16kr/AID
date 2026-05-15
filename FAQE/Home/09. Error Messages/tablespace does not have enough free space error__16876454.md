---
title: "tablespace does not have enough free space error"
page_id: "16876454"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/tablespace+does+not+have+enough+free+space+error"
updated_at: "2021-03-30T17:11:44.000+0900"
version: 2
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# tablespace does not have enough free space error
Source: https://docs.altibase.com/display/FAQE/tablespace+does+not+have+enough+free+space+error
Updated: 2021-03-30T17:11:44.000+0900

- [Overview](#tablespacedoesnothaveenoughfreespaceerror-Overview) - [Version](#tablespacedoesnothaveenoughfreespaceerror-Version) - [Cause](#tablespacedoesnothaveenoughfreespaceerror-Cause) - [Solution](#tablespacedoesnothaveenoughfreespaceerror-Solution) - [Reference](#tablespacedoesnothaveenoughfreespaceerror-Reference)

# Overview

---

Insufficient tablespace

# Version

---

ALTIBASE HDB version 4 or later

# Cause

---

This error is caused by the insufficient size of a specific tablespace.

# Solution

---

1. Check the tablespace space usage.

Use the appropriate query statement for the version of Altibase you are using to check the usage.

```
https://docs.altibase.com/display/FAQE/08.+Monitoring
```

2. After querying the tablespace usage, add space to the tablespace with USAGE(%) close to 100% in the query result.

```
ALTER TABLESPACE tablespace_name add datafile '/path/filename' size 2G autoextend off;
```

# Reference

---

When adding a data file, the tablespace is locked, so it is recommended to block the service while performing the work.

For HDB 5.3.3 and earlier, SELECT and DML queries wait for the tablespace add operation to complete.

From HDB 5.5.1 or later through the latest V6, DML waits until the tablespace add operation is completed, but SELECT statements execute normally.
