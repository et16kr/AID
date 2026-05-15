---
title: "ERR-0104E The property XXX is read-only"
page_id: "7340662"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-0104E+The+property+XXX+is+read-only"
updated_at: "2014-11-20T15:16:34.000+0900"
version: 4
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-0104E The property XXX is read-only
Source: https://docs.altibase.com/display/FAQE/ERR-0104E+The+property+XXX+is+read-only
Updated: 2014-11-20T15:16:34.000+0900

- [Version](#ERR-0104EThepropertyXXXisread-only-Version)
- [Explanation](#ERR-0104EThepropertyXXXisread-only-Explanation)
- [Cause](#ERR-0104EThepropertyXXXisread-only-Cause)
- [Action](#ERR-0104EThepropertyXXXisread-only-Action)
- [Reference](#ERR-0104EThepropertyXXXisread-only-Reference)

## Version

All versions

## Explanation

Unable to modify property.

## Cause

This error occurs when a property cannot be modified online.

## Action

Certain properties have the read-only attribute and cannot be modified online.

Instead of using the ALTER statement, modify the property in $ALTIBASE_HOME/conf/altibase.properties, and then restart the server.

## Reference

N/A
