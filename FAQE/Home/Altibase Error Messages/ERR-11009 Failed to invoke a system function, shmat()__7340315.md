---
title: "ERR-11009 Failed to invoke a system function, shmat()"
page_id: "7340315"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=7340315"
updated_at: "2014-10-28T17:55:21.000+0900"
version: 3
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-11009 Failed to invoke a system function, shmat()
Source: https://docs.altibase.com/pages/viewpage.action?pageId=7340315
Updated: 2014-10-28T17:55:21.000+0900

- [Version](#ERR-11009Failedtoinvokeasystemfunction,shmat()-Version)
- [Explanation](#ERR-11009Failedtoinvokeasystemfunction,shmat()-Explanation)
- [Cause](#ERR-11009Failedtoinvokeasystemfunction,shmat()-Cause)
- [Action](#ERR-11009Failedtoinvokeasystemfunction,shmat()-Action)
- [Reference](#ERR-11009Failedtoinvokeasystemfunction,shmat()-Reference)

## Version

All versions

## Explanation

Unable to create database.

## Cause

This error can occur under the following circumstances:

- ALTIBASE HDB is being used in shared memory mode.
- a lack of shared memory due to too small shared memory kernel parameter value.
- the shared memory key value(SHM_DB_KEY) is already in use.

## Action

1. Check the shared memory kernel parameter value. If it is too small, change it to an appropriate value.
2. If SHM_DB_KEY is an arbitrary value used by the system, change the key value.

## Reference

N/A
