---
title: "ERR-21013 Calculation stack overflow"
page_id: "6979710"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-21013+Calculation+stack+overflow"
updated_at: "2014-11-19T16:38:32.000+0900"
version: 13
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-21013 Calculation stack overflow
Source: https://docs.altibase.com/display/FAQE/ERR-21013+Calculation+stack+overflow
Updated: 2014-11-19T16:38:32.000+0900

- [Version](#ERR-21013Calculationstackoverflow-Version)
- [Explanation](#ERR-21013Calculationstackoverflow-Explanation)
- [Cause](#ERR-21013Calculationstackoverflow-Cause)
- [Action](#ERR-21013Calculationstackoverflow-Action)
- [Reference](#ERR-21013Calculationstackoverflow-Reference)

## Version

6.3.1

## Explanation

Unable to execute query.

## Cause

The query requires a stack size that exceeds the size of the stack used by Altibase to run queries (This is to prevent the waste of memory resources of the Altibase server due to maintaining a large stack.).

## Action

Check whether query tuning has been performed; otherwise choose one of the two following methods.

**1. Change the maximum stack size for a specific session only.**

Change the maximum time of query execution. (MAX: 65536)

```
ALTER SESSION SET STACK SIZE = 2048;
```

**2. Change the maximum stack size of all the sessions.**

1) Run the statement in iSQL to change server settings.

```
iSQL> ALTER SYSTEM SET QUERY_STACK_SIZE = 2048;
```

2) Change QUERY_STACK_SIZE from $ALTIBASE_HOME/conf/altibase.properties.

**3. Re-connect all the clients.**

## Reference

If the stack size is set to a value greater than needed, it may become a waste of unnecessary memory space.
