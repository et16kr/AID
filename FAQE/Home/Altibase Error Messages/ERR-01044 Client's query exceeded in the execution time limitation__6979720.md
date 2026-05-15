---
title: "ERR-01044 Client's query exceeded in the execution time limitation"
page_id: "6979720"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-01044+Client%27s+query+exceeded+in+the+execution+time+limitation"
updated_at: "2014-11-19T15:19:37.000+0900"
version: 12
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-01044 Client's query exceeded in the execution time limitation
Source: https://docs.altibase.com/display/FAQE/ERR-01044+Client%27s+query+exceeded+in+the+execution+time+limitation
Updated: 2014-11-19T15:19:37.000+0900

- [Version](#ERR-01044Client'squeryexceededintheexecutiontimelimitation-Version)
- [Explanation](#ERR-01044Client'squeryexceededintheexecutiontimelimitation-Explanation)
- [Cause](#ERR-01044Client'squeryexceededintheexecutiontimelimitation-Cause)
- [Action](#ERR-01044Client'squeryexceededintheexecutiontimelimitation-Action)
- [Reference](#ERR-01044Client'squeryexceededintheexecutiontimelimitation-Reference)

## Version

All versions

## Explanation

The query abnormally terminates.

## Cause

QUERY_TIMEOUT specifies the maximum amount of time allowed for a query to complete its execution.

This property prevents long-running queries from causing server load.

This error message is output when a query was executed for a longer time than the value specified for QUERY_TIMEOUT.

Information of the query is output to Altibase_boot.log.

## Action

This error occurs when the query execution time exceeded QUERY_TIMEOUT.

QUERY_TIMEOUT is the maximum amount of time allowed for a query to complete its execution.

The best way to fix this error is to reduce the overall execution time by tuning the query (e.g., adding an index).

A quick workaround would be to increase QUERY_TIMEOUT to avoid the error.

- Check the QUERY_TIMEOUT property value (default : 3600 seconds).

  ```
  SELECT name, value1 FROM v$property WHERE name LIKE '%TIMEOUT%';
  ```
- Modify the value.

  ```
  ALTER SYSTEM SET query_ timeout= desired value;
  ```

## Reference

This error message can be attributed to various causes: high service traffic load or suddenly changed query plans can incur prolonged query execution time.

This error should be fixed by tuning queries.
