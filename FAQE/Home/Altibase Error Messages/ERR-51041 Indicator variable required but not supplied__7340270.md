---
title: "ERR-51041 Indicator variable required but not supplied"
page_id: "7340270"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-51041+Indicator+variable+required+but+not+supplied"
updated_at: "2014-10-28T11:20:37.000+0900"
version: 3
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-51041 Indicator variable required but not supplied
Source: https://docs.altibase.com/display/FAQE/ERR-51041+Indicator+variable+required+but+not+supplied
Updated: 2014-10-28T11:20:37.000+0900

- [Version](#ERR-51041Indicatorvariablerequiredbutnotsupplied-Version)
- [Explanation](#ERR-51041Indicatorvariablerequiredbutnotsupplied-Explanation)
- [Cause](#ERR-51041Indicatorvariablerequiredbutnotsupplied-Cause)
- [Action](#ERR-51041Indicatorvariablerequiredbutnotsupplied-Action)
- [Reference](#ERR-51041Indicatorvariablerequiredbutnotsupplied-Reference)

## Version

All versions

## Explanation

This error occurs when using a precompiler in the development environment.

## Cause

When the INDICATOR variable is not specified while NULL is returned as the return value of a column in the SELECT statement, this error occurs with SQL_SUCCESS_WITH_INFO.

## Action

```
int IND_C1;

int IND_C2;

EXEC SELECT C1, C2

INTO :H_C1 INDICATOR :IND_C1 , :H_C2 INDICATOR :IND_C2;
```

This error can be avoided by using the option ‘unsafe_null’ in the precompiler option or using the INDICATOR variable as in the above example.

## Reference

N/A
