---
title: "ERR-21010 Value overflow"
page_id: "6979763"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-21010+Value+overflow"
updated_at: "2014-11-27T17:10:27.000+0900"
version: 12
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-21010 Value overflow
Source: https://docs.altibase.com/display/FAQE/ERR-21010+Value+overflow
Updated: 2014-11-27T17:10:27.000+0900

- [Version](#ERR-21010Valueoverflow-Version)
- [Explanation](#ERR-21010Valueoverflow-Explanation)
- [Cause](#ERR-21010Valueoverflow-Cause)
- [Action](#ERR-21010Valueoverflow-Action)
- [Reference](#ERR-21010Valueoverflow-Reference)

## Version

All versions

## Explanation

Unable to execute an INSERT or UPDATE statement.

This error message is output when an INSERT or UPDATE statement is executed:

## Cause

The following error description can be viewed with the AltiErr utility:

$ altierr 0x21010

0x21010 ( 135184) mtERR_ABORT_VALUE_OVERFLOW Value overflow

# *Cause: Value overflow

# *Action: Please change the value or data type.

This error occurs when the input value is not within the supported data type range.

# Example

```
iSQL> create table test(i1 integer);
Create success.
iSQL> insert into test values(2147483648);
[ERR-21010 : Value overflow
0001 : insert into TEST values(2147483648)
                              ^         ^
]
iSQL> insert into test values(2147483647);
1 row inserted.
```

The INTEGER data type stores integers in the range of -2,147,483,647~ 2,147,483,647.

This error occurred because the value to be stored in the column is outside this range.

## Action

Check whether the value to be stored in the column exceeds the maximum allowed for the column's data type.

If so, change the input value or convert the column's data type.

## Reference

For further information about the range of values for the data types supported by Altibase, refer to the *General Reference Manual*.
