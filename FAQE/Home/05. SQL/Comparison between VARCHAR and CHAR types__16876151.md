---
title: "Comparison between VARCHAR and CHAR types"
page_id: "16876151"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Comparison+between+VARCHAR+and+CHAR+types"
updated_at: "2021-03-18T14:49:05.000+0900"
version: 1
ancestors: ["Home", "05. SQL"]
labels: []
---

# Comparison between VARCHAR and CHAR types
Source: https://docs.altibase.com/display/FAQE/Comparison+between+VARCHAR+and+CHAR+types
Updated: 2021-03-18T14:49:05.000+0900

- [Overview](#ComparisonbetweenVARCHARandCHARtypes-Overview) - [Version](#ComparisonbetweenVARCHARandCHARtypes-Version) - [Comparison between VARCHAR and CHAR types](#ComparisonbetweenVARCHARandCHARtypes-ComparisonbetweenVARCHARandCHARtypes)

# Overview

---

This is a comparison between varchar type and char type.

# Version

---

Applicable to all versions of Altibase.

# Comparison between VARCHAR and CHAR types

---

```
iSQL> create table dual (X char(1));
Create success.
iSQL> insert into dual values ('x');
1 row inserted.
iSQL> select 1 from dual;
1
--------------
1
1 row selected.
iSQL> select 1 from dual where char'a ' = char'a ';
1
--------------
1
1 row selected.
iSQL> select 1 from dual where varchar'a ' = varchar'a ';
1
--------------
No rows selected.
iSQL> select 1 from dual where varchar'a' = char'a ';
1
--------------
No rows selected.
iSQL> select 1 from dual where varchar'a' = char'a';
1
--------------
1
1 row selected.
iSQL> select 1 from dual where varchar'a ' = char'a ';
1
--------------
1
1 row selected.
```

When comparing `CHAR` values, `0x20` is added to the shorter value and the comparison uses the longer length. When comparing `CHAR` and `VARCHAR`, the comparison uses the valid data in the `VARCHAR` value, up to the `0x00` position.

In SESC code, variables are sometimes initialized to `0x00` for `VARCHAR` and to `0x20` for `CHAR`. Because of the comparison rules above, it is better to initialize them to `0x00`.
