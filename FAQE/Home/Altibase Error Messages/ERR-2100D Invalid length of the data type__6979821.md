---
title: "ERR-2100D Invalid length of the data type"
page_id: "6979821"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-2100D+Invalid+length+of+the+data+type"
updated_at: "2014-11-27T17:10:08.000+0900"
version: 6
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-2100D Invalid length of the data type
Source: https://docs.altibase.com/display/FAQE/ERR-2100D+Invalid+length+of+the+data+type
Updated: 2014-11-27T17:10:08.000+0900

- [Version](#ERR-2100DInvalidlengthofthedatatype-Version)
- [Explanation](#ERR-2100DInvalidlengthofthedatatype-Explanation)
- [Cause](#ERR-2100DInvalidlengthofthedatatype-Cause)
- [Action](#ERR-2100DInvalidlengthofthedatatype-Action)
- [Reference](#ERR-2100DInvalidlengthofthedatatype-Reference)

## Version

All versions

## Explanation

Unable to execute query.

## Cause

This error occurs when an operation that is not permitted for the data type is performed.

1. If the user tries to create a column which exceeds the maximum size of the data type.

2. If the user tries to insert or update data which exceeds the column size.

## Action

Check the maximum sizes supported for data types in the Altibase version being used and try again.

## Reference

For further information about the maximum sizes supported for data types in Altibase, refer to the *SQL Reference Manual*.
