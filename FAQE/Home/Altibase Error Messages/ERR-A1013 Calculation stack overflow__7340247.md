---
title: "ERR-A1013 Calculation stack overflow"
page_id: "7340247"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-A1013+Calculation+stack+overflow"
updated_at: "2014-10-28T10:50:22.000+0900"
version: 4
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-A1013 Calculation stack overflow
Source: https://docs.altibase.com/display/FAQE/ERR-A1013+Calculation+stack+overflow
Updated: 2014-10-28T10:50:22.000+0900

- [Version](#ERR-A1013Calculationstackoverflow-Version)
- [Explanation](#ERR-A1013Calculationstackoverflow-Explanation)
- [Cause](#ERR-A1013Calculationstackoverflow-Cause)
- [Action](#ERR-A1013Calculationstackoverflow-Action)
- [Reference](#ERR-A1013Calculationstackoverflow-Reference)

## Version

All versions

## Explanation

Unable to execute query.

## Cause

If there are not enough stacks necessary for the query being executed by an object from the internal query handling procedure, this error occurs.

## Action

The user is advised to execute the following SQL command then re-execute the query that caused this error.

```
iSQL>ALTER SESSION SET STACK SIZE = 8192;
```

The user is advised to change it from the session only rather than from the entire system because it causes a memory increase.

## Reference

N/A
