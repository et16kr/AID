---
title: "ERR-51192 The call to getaddrinfo() failed. The host name or service may be unknown"
page_id: "7340769"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-51192+The+call+to+getaddrinfo%28%29+failed.+The+host+name+or+service+may+be+unknown"
updated_at: "2014-11-27T17:51:15.000+0900"
version: 6
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-51192 The call to getaddrinfo() failed. The host name or service may be unknown
Source: https://docs.altibase.com/display/FAQE/ERR-51192+The+call+to+getaddrinfo%28%29+failed.+The+host+name+or+service+may+be+unknown
Updated: 2014-11-27T17:51:15.000+0900

- [Version](#ERR-51192Thecalltogetaddrinfo()failed.Thehostnameorservicemaybeunknown-Version)
- [Explanation](#ERR-51192Thecalltogetaddrinfo()failed.Thehostnameorservicemaybeunknown-Explanation)
- [Cause](#ERR-51192Thecalltogetaddrinfo()failed.Thehostnameorservicemaybeunknown-Cause)
- [Action](#ERR-51192Thecalltogetaddrinfo()failed.Thehostnameorservicemaybeunknown-Action)
- [Reference](#ERR-51192Thecalltogetaddrinfo()failed.Thehostnameorservicemaybeunknown-Reference)

## Version

All versions

## Explanation

Unable to connect to database using iSQL.

## Cause

This error occurs due to invalid server information when using the 'is' script to connect to the database.

## Action

1. Check whether the server information of the 'is' script is correct.

```
(SERVER = localhost)
```

2. If the error persists although the server information is correct, change localhost information to 127.0.0.1 and reconnect.

## Reference

N/A
