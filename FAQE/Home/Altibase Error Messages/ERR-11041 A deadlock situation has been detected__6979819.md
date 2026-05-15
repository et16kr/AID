---
title: "ERR-11041 A deadlock situation has been detected"
page_id: "6979819"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-11041+A+deadlock+situation+has+been+detected"
updated_at: "2014-11-19T16:32:12.000+0900"
version: 6
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-11041 A deadlock situation has been detected
Source: https://docs.altibase.com/display/FAQE/ERR-11041+A+deadlock+situation+has+been+detected
Updated: 2014-11-19T16:32:12.000+0900

- [Version](#ERR-11041Adeadlocksituationhasbeendetected-Version)
- [Explanation](#ERR-11041Adeadlocksituationhasbeendetected-Explanation)
- [Cause](#ERR-11041Adeadlocksituationhasbeendetected-Cause)
- [Action](#ERR-11041Adeadlocksituationhasbeendetected-Action)
- [Reference](#ERR-11041Adeadlocksituationhasbeendetected-Reference)

## Version

All versions

## Explanation

Unable to execute query.

## Cause

This error occurs when a deadlock has occurred and the query that caused the deadlock is not executed for concurrency control.

## Action

1. Find the queries that cause locks and check which of their logic is causing a deadlock.

Modify the queries so that the problematic logic is not executed.

2. As deadlocks can occur in replication, check the locks that are acquired during replication.

## Reference

N/A
