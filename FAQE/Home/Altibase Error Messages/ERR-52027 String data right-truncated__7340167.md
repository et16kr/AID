---
title: "ERR-52027 String data right-truncated"
page_id: "7340167"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-52027+String+data+right-truncated"
updated_at: "2014-11-20T15:18:46.000+0900"
version: 8
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-52027 String data right-truncated
Source: https://docs.altibase.com/display/FAQE/ERR-52027+String+data+right-truncated
Updated: 2014-11-20T15:18:46.000+0900

- [Version](#ERR-52027Stringdataright-truncated-Version)
- [Explanation](#ERR-52027Stringdataright-truncated-Explanation)
- [Cause](#ERR-52027Stringdataright-truncated-Cause)
- [Action](#ERR-52027Stringdataright-truncated-Action)
- [Reference](#ERR-52027Stringdataright-truncated-Reference)

## Version

All versions

## Explanation

Unable to select data.

## Cause

This error message is output when:

1. the CHAR data type value returned from the SELECT statement is larger than the declared host variable.

2. a parsing error occurs in the executed query due to NULL values or special characters.

## Action

1. Connect to the database

2. Check the table column size.

3. Declare the host variable used in the statement with the length (column size + 1 byte).

4. Check whether rpad was used in the statement where the error occurred.

5. If so, rewrite the query.

## Reference

N/A
