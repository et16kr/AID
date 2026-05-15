---
title: "ERR-91044 Error occurred during data file IO."
page_id: "7340233"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=7340233"
updated_at: "2014-10-28T10:20:27.000+0900"
version: 3
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-91044 Error occurred during data file IO.
Source: https://docs.altibase.com/pages/viewpage.action?pageId=7340233
Updated: 2014-10-28T10:20:27.000+0900

- [Version](#ERR-91044ErroroccurredduringdatafileIO.-Version)
- [Explanation](#ERR-91044ErroroccurredduringdatafileIO.-Explanation)
- [Cause](#ERR-91044ErroroccurredduringdatafileIO.-Cause)
- [Action](#ERR-91044ErroroccurredduringdatafileIO.-Action)
- [Reference](#ERR-91044ErroroccurredduringdatafileIO.-Reference)

## Version

6.3.1

## Explanation

Unable to input/output file data while using iLoader.

## Cause

1. There is no more space in the file system.

2. The file does not exist.

3. The file size is too big

## Action

1. Check the available space in the file system.

2. Check whether the file name for uploading exists.

3. Check the file size.

## Reference

N/A
