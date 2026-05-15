---
title: "ERR-71018 Failed to invoke the read() system function"
page_id: "6979756"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-71018+Failed+to+invoke+the+read%28%29+system+function"
updated_at: "2014-10-20T09:46:21.000+0900"
version: 6
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-71018 Failed to invoke the read() system function
Source: https://docs.altibase.com/display/FAQE/ERR-71018+Failed+to+invoke+the+read%28%29+system+function
Updated: 2014-10-20T09:46:21.000+0900

- [Version](#ERR-71018Failedtoinvoketheread()systemfunction-Version)
- [Explanation](#ERR-71018Failedtoinvoketheread()systemfunction-Explanation)
- [Cause](#ERR-71018Failedtoinvoketheread()systemfunction-Cause)
- [Action](#ERR-71018Failedtoinvoketheread()systemfunction-Action)
- [Reference](#ERR-71018Failedtoinvoketheread()systemfunction-Reference)

## Version

All versions

## Explanation

The client connection abnormally terminates.

## Cause

If the server checks whether a session is running after a client session has already been physically terminated, the server confirms that the session is physically terminated and outputs this error message to clean up the session.

## Action

1. Check whether the network is unstable.

2. Check whether the client program malfunctions.

## Reference

N/A
