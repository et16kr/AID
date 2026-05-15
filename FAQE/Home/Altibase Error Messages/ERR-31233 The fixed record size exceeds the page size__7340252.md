---
title: "ERR-31233 The fixed record size exceeds the page size"
page_id: "7340252"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-31233+The+fixed+record+size+exceeds+the+page+size"
updated_at: "2016-11-22T14:39:49.000+0900"
version: 12
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-31233 The fixed record size exceeds the page size
Source: https://docs.altibase.com/display/FAQE/ERR-31233+The+fixed+record+size+exceeds+the+page+size
Updated: 2016-11-22T14:39:49.000+0900

- [Version](#ERR-31233Thefixedrecordsizeexceedsthepagesize-Version) - [Explanation](#ERR-31233Thefixedrecordsizeexceedsthepagesize-Explanation) - [Cause](#ERR-31233Thefixedrecordsizeexceedsthepagesize-Cause) - [Action](#ERR-31233Thefixedrecordsizeexceedsthepagesize-Action) - [Reference](#ERR-31233Thefixedrecordsizeexceedsthepagesize-Reference)

## Version

All versions

## Explanation

Unable to create view.

```
iSQL> create table t1(c1 char(5000));
Create success.
iSQL> create table t2(c1 char(5000)) tablespace sys_tbs_disk_data;
Create success.
```

ERR-31233 : Fixed record size exceeds a page size.

## Cause

This error occurs if a fixed column that exceeds 32K for memory tables or 8K for disk tables is used. Disk tables use disk temporary tables for sorting/grouping operations. This error can occur if the length of a temporary record exceeds 8K.

## Action

1. Set the table column to VARIABLE, not FIXED when creating for the first time.

2. If the error occurs when executing the SELECT statement using disk temporary tables, the memory temporary table should be used with the hint /*+ temp_tbs_memory */.

## Reference

N/A
