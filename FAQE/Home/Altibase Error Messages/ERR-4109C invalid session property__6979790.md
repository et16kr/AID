---
title: "ERR-4109C invalid session property"
page_id: "6979790"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-4109C+invalid+session+property"
updated_at: "2014-10-20T09:50:53.000+0900"
version: 5
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-4109C invalid session property
Source: https://docs.altibase.com/display/FAQE/ERR-4109C+invalid+session+property
Updated: 2014-10-20T09:50:53.000+0900

- [Version](#ERR-4109Cinvalidsessionproperty-Version)
- [Explanation](#ERR-4109Cinvalidsessionproperty-Explanation)
- [Cause](#ERR-4109Cinvalidsessionproperty-Cause)
- [Action](#ERR-4109Cinvalidsessionproperty-Action)
- [Reference](#ERR-4109Cinvalidsessionproperty-Reference)

## Version

4.3.9 or above

## Explanation

Unable to connect to the database.

## Cause

This error occurs when the Altibase client and server are of the same major version but the client has a higher patch version than the server.

## Action

Upgrade the Altibase server version or downgrade the client version.

This error message is generally output due to a major version discrepancy.

Yet, this error can also occur due to a cm protocol version discrepancy, despite the server and client having the same major version.

## Reference

N/A
