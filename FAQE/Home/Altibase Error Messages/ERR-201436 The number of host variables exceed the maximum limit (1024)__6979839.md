---
title: "ERR-201436 The number of host variables exceed the maximum limit (1024)"
page_id: "6979839"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=6979839"
updated_at: "2014-11-20T10:36:04.000+0900"
version: 10
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-201436 The number of host variables exceed the maximum limit (1024)
Source: https://docs.altibase.com/pages/viewpage.action?pageId=6979839
Updated: 2014-11-20T10:36:04.000+0900

- [Version](#ERR-201436Thenumberofhostvariablesexceedthemaximumlimit(1024)-Version)
- [Explanation](#ERR-201436Thenumberofhostvariablesexceedthemaximumlimit(1024)-Explanation)
- [Cause](#ERR-201436Thenumberofhostvariablesexceedthemaximumlimit(1024)-Cause)
- [Action](#ERR-201436Thenumberofhostvariablesexceedthemaximumlimit(1024)-Action)
- [Reference](#ERR-201436Thenumberofhostvariablesexceedthemaximumlimit(1024)-Reference)

## Version

4.3.9 or above

## Explanation

Unable to create the procedure.

## Cause

1024 is the maximum number of host variables that can be used. This error occurs if the number of host variables in the procedure exceeded this number.

## Action

The WITH clause **(for ALTIBASE HDB 6.3.1 or above)** can be used to reduce the number of host variables. It can use more than 1024 by using variable substitution as shown below.

```
WITH dataset1 AS (SELECT V_YYYYMM AS V_EXEC_YYYYMM FROM dual )
```

**For versions below 6.3.1,** either separate the processing modules for each task or change the logic to handle it in a different way, apart from a host variable as the WITH clause is not supported.

## Reference

N/A
