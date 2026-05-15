---
title: "ERR-11025 The data file already exists"
page_id: "6980129"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-11025+The+data+file+already+exists"
updated_at: "2014-11-20T15:38:28.000+0900"
version: 7
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-11025 The data file already exists
Source: https://docs.altibase.com/display/FAQE/ERR-11025+The+data+file+already+exists
Updated: 2014-11-20T15:38:28.000+0900

- [Version](#ERR-11025Thedatafilealreadyexists-Version)
- [Explanation](#ERR-11025Thedatafilealreadyexists-Explanation)
- [Cause](#ERR-11025Thedatafilealreadyexists-Cause)
- [Action](#ERR-11025Thedatafilealreadyexists-Action)
- [Reference](#ERR-11025Thedatafilealreadyexists-Reference)

## Version

All versions

## Explanation

Unable to create tablespace.

## Cause

This error occurs if the datafile already exists when creating a database or adding a datafile.

## Action

1. Check whether a duplicate datafile name exists in the directory.

2. Change the datafile name to a distinct one and then add the datafile or recreate the tablespace/database.

## Reference

N/A
