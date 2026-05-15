---
title: "ERR-91013 The query was too long the maximum length is 65536"
page_id: "7340229"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-91013+The+query+was+too+long+the+maximum+length+is+65536"
updated_at: "2014-11-20T15:02:40.000+0900"
version: 4
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-91013 The query was too long the maximum length is 65536
Source: https://docs.altibase.com/display/FAQE/ERR-91013+The+query+was+too+long+the+maximum+length+is+65536
Updated: 2014-11-20T15:02:40.000+0900

- [Version](#ERR-91013Thequerywastoolongthemaximumlengthis65536-Version)
- [Explanation](#ERR-91013Thequerywastoolongthemaximumlengthis65536-Explanation)
- [Cause](#ERR-91013Thequerywastoolongthemaximumlengthis65536-Cause)
- [Action](#ERR-91013Thequerywastoolongthemaximumlengthis65536-Action)
- [Reference](#ERR-91013Thequerywastoolongthemaximumlengthis65536-Reference)

## Version

All versions

## Explanation

Unable to create procedure or execute query.

## Cause

This error occurs if either a long procedure or query that exceeds the maximum text buffer size of iSQL is created or executed.

## Action

The maximum length that can be handled in iSQL is 655536, by default. This can be changed from an environmental variable called ISQL_BUFFER_SIZE.

Increase ISQL_BUFFER_SIZE to create a long procedure.

```
$ export ISQL_BUFFER_SIZE=256000
```

## Reference

N/A
