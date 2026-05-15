---
title: "ERR-9103D Data parsing error - LineXXXX"
page_id: "6979857"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-9103D+Data+parsing+error+-+LineXXXX"
updated_at: "2014-10-20T09:52:07.000+0900"
version: 6
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-9103D Data parsing error - LineXXXX
Source: https://docs.altibase.com/display/FAQE/ERR-9103D+Data+parsing+error+-+LineXXXX
Updated: 2014-10-20T09:52:07.000+0900

- [Version](#ERR-9103DDataparsingerror-LineXXXX-Version)
- [Explanation](#ERR-9103DDataparsingerror-LineXXXX-Explanation)
- [Cause](#ERR-9103DDataparsingerror-LineXXXX-Cause)
- [Action](#ERR-9103DDataparsingerror-LineXXXX-Action)
- [Reference](#ERR-9103DDataparsingerror-LineXXXX-Reference)

## Version

All versions

## Explanation

Unable to upload data.

## Cause

1. Data is not recognized due to the column delimiter being included in the data.

2. The column delimiter is the same as the data.

## Action

1. This error usually occurs when a column delimiter is included in the data and this causes the data not to be recognized; an iLoader statement has column and row delimiters.

For example, if a column contains ^C_ and a row contains ^R_, an error occurs because the delimiters are included in the data.

However, if the delimiters are written in a more complex way and the data is downloaded/uploaded again, an error does not occur.

2. This error occurs when the actual data is the same as the delimiter during data uploads.

The data should not overlap with the delimiter when the data is downloaded.

## Reference

N/A
