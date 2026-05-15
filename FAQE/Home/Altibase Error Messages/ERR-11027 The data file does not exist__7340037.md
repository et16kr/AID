---
title: "ERR-11027 The data file does not exist"
page_id: "7340037"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-11027+The+data+file+does+not+exist"
updated_at: "2014-10-27T14:28:34.000+0900"
version: 6
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-11027 The data file does not exist
Source: https://docs.altibase.com/display/FAQE/ERR-11027+The+data+file+does+not+exist
Updated: 2014-10-27T14:28:34.000+0900

- [Version](#ERR-11027Thedatafiledoesnotexist-Version)
- [Explanation](#ERR-11027Thedatafiledoesnotexist-Explanation)
- [Cause](#ERR-11027Thedatafiledoesnotexist-Cause)
- [Action](#ERR-11027Thedatafiledoesnotexist-Action)
- [Reference](#ERR-11027Thedatafiledoesnotexist-Reference)

## Version

All versions

## Explanation

Unable to start server.

## Cause

This error occurs if data file information stored in meta data cannot be found in the specified path.

## Action

1. Start the server until CONTROL phase and check whether the datafile path matches the meta data.

2. If not, input the correct path.

## Reference

N/A
