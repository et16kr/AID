---
title: "ERR-51043 Communication link failure"
page_id: "6979768"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-51043+Communication+link+failure"
updated_at: "2014-10-20T09:45:46.000+0900"
version: 6
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-51043 Communication link failure
Source: https://docs.altibase.com/display/FAQE/ERR-51043+Communication+link+failure
Updated: 2014-10-20T09:45:46.000+0900

- [Version](#ERR-51043Communicationlinkfailure-Version)
- [Explanation](#ERR-51043Communicationlinkfailure-Explanation)
- [Cause](#ERR-51043Communicationlinkfailure-Cause)
- [Action](#ERR-51043Communicationlinkfailure-Action)
- [Reference](#ERR-51043Communicationlinkfailure-Reference)

## Version

6.3.1

## Explanation

Connection is disconnected.

## Cause

This error has various causes. The following are the main causes:

1. The server forcefully closed the client connection due to timeout.

2. The user forcefully closed the connection.

3. The database was shut down.

## Action

1. Tune a long-running query and increase the session’s timeout value

2. Check whether the database service runs normally.

## Reference

N/A
