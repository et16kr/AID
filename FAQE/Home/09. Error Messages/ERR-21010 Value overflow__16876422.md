---
title: "ERR-21010 Value overflow."
page_id: "16876422"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876422"
updated_at: "2021-04-05T13:18:15.000+0900"
version: 2
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# ERR-21010 Value overflow.
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876422
Updated: 2021-04-05T13:18:15.000+0900

- [Version](#ERR-21010Valueoverflow.-Version) - [Symptom](#ERR-21010Valueoverflow.-Symptom) - [Cause](#ERR-21010Valueoverflow.-Cause) - [Solution](#ERR-21010Valueoverflow.-Solution) - [Notes/Considerations](#ERR-21010Valueoverflow.-Notes/Considerations)

# Version

---

All the versions of Altibase

# Symptom

---

The following error occurs when executing INSERT/UPDATE, etc.

[ERR-21010: Value overflow]

# Cause

---

The description of the error can be checked using the altierr utility as follows.

$ altierr 0x21010

0x21010 ( 135184) mtERR_ABORT_VALUE_OVERFLOW Value overflow

# *Cause: Value overflow

# *Action: Please change the value or data type.

In other words, it is an error that occurs when the input value exceeds the range supported by the data type.

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

The range of integer type values is **-2,147,483,647 ~ 2,147,483,647** integer values.

Therefore, the error occurred because the value to be stored in the column is out of the range of the integer value.

# Solution

---

Check if the input value to be saved in a specific column exceeds the maximum size of the column data type.

If it exceeds the maximum size, it is necessary to modify the input value or change the data type of the column.

# Notes/Considerations

---

The range of values for each data type supported by Altibase can be found in the General Reference manual at [http://support.altibase.com/en/manual](http://support.altibase.com/kr/manual)[/](http://support.altibase.com/en/manual.) or GitHub: [https://github.com/ALTIBASE/Documents](https://github.com/ALTIBASE/Documents)[.](http://support.altibase.com/kr/manual)
