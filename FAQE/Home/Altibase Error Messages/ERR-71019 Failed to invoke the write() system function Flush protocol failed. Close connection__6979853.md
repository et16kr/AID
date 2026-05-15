---
title: "ERR-71019 Failed to invoke the write() system function Flush protocol failed. Close connection"
page_id: "6979853"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-71019+Failed+to+invoke+the+write%28%29+system+function+Flush+protocol+failed.+Close+connection"
updated_at: "2014-11-27T17:13:21.000+0900"
version: 8
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-71019 Failed to invoke the write() system function Flush protocol failed. Close connection
Source: https://docs.altibase.com/display/FAQE/ERR-71019+Failed+to+invoke+the+write%28%29+system+function+Flush+protocol+failed.+Close+connection
Updated: 2014-11-27T17:13:21.000+0900

- [Version](#ERR-71019Failedtoinvokethewrite()systemfunctionFlushprotocolfailed.Closeconnection-Version)
- [Explanation](#ERR-71019Failedtoinvokethewrite()systemfunctionFlushprotocolfailed.Closeconnection-Explanation)
- [Cause](#ERR-71019Failedtoinvokethewrite()systemfunctionFlushprotocolfailed.Closeconnection-Cause)
- [Action](#ERR-71019Failedtoinvokethewrite()systemfunctionFlushprotocolfailed.Closeconnection-Action)
- [Reference](#ERR-71019Failedtoinvokethewrite()systemfunctionFlushprotocolfailed.Closeconnection-Reference)

## Version

All versions

## Explanation

The connection to the client is terminated or there is no incident.

## Cause

The connection was terminated due to a network problem or the abnormal termination of a client program.

## Action

1. Check whether the network is stable.

2. Check the operation status of the client program.

3. Check the connection close part of the database from the application and verify that it is disconnected.

## Reference

N/A
