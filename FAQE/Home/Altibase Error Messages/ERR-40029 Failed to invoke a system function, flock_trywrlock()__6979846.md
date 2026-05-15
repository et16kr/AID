---
title: "ERR-40029 Failed to invoke a system function, flock_trywrlock()"
page_id: "6979846"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=6979846"
updated_at: "2014-10-20T09:48:19.000+0900"
version: 6
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-40029 Failed to invoke a system function, flock_trywrlock()
Source: https://docs.altibase.com/pages/viewpage.action?pageId=6979846
Updated: 2014-10-20T09:48:19.000+0900

- [Version](#ERR-40029Failedtoinvokeasystemfunction,flock_trywrlock()-Version)
- [Explanation](#ERR-40029Failedtoinvokeasystemfunction,flock_trywrlock()-Explanation)
- [Cause](#ERR-40029Failedtoinvokeasystemfunction,flock_trywrlock()-Cause)
- [Action](#ERR-40029Failedtoinvokeasystemfunction,flock_trywrlock()-Action)
- [Reference](#ERR-40029Failedtoinvokeasystemfunction,flock_trywrlock()-Reference)

## Version

All versions

## Explanation

The following message is ouput to altibase_boot.log due to startup failure.

ERR-40029(errno=16) Failed to invoke a system function, flock_trywrlock()

## Cause

The Altibase server started while the Altibase process was already up.

## Action

Wait until the Altibase process is terminated and start the server.

## Reference

N/A
