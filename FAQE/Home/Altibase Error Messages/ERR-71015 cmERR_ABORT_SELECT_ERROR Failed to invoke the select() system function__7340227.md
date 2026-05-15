---
title: "ERR-71015 cmERR_ABORT_SELECT_ERROR Failed to invoke the select() system function"
page_id: "7340227"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-71015+cmERR_ABORT_SELECT_ERROR+Failed+to+invoke+the+select%28%29+system+function"
updated_at: "2014-11-27T17:21:40.000+0900"
version: 5
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-71015 cmERR_ABORT_SELECT_ERROR Failed to invoke the select() system function
Source: https://docs.altibase.com/display/FAQE/ERR-71015+cmERR_ABORT_SELECT_ERROR+Failed+to+invoke+the+select%28%29+system+function
Updated: 2014-11-27T17:21:40.000+0900

- [Version](#ERR-71015cmERR_ABORT_SELECT_ERRORFailedtoinvoketheselect()systemfunction-Version)
- [Explanation](#ERR-71015cmERR_ABORT_SELECT_ERRORFailedtoinvoketheselect()systemfunction-Explanation)
- [Cause](#ERR-71015cmERR_ABORT_SELECT_ERRORFailedtoinvoketheselect()systemfunction-Cause)
- [Action](#ERR-71015cmERR_ABORT_SELECT_ERRORFailedtoinvoketheselect()systemfunction-Action)
- [Reference](#ERR-71015cmERR_ABORT_SELECT_ERRORFailedtoinvoketheselect()systemfunction-Reference)

## Version

All versions

## Explanation

Unable to connect to database.

## Cause

Failed to call the SELECT function that detects the socket during network communication.

## Action

This error can occur because of a network issue, server shutdown, session disconnection due to timeout and a sudden increase of connection requests. Check the OS network status or distribute connection overloads.

## Reference

N/A
