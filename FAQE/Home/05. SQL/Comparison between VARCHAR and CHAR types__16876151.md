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

In the case of char type, 0x20 is added and compared based on the larger length when comparing, and when comparing char and varchar, the comparison is performed based on the valid data of varchar (position of 0x00).

Sometimes, when SESC coding, variables are initialized to 0x00 for varchar and 0x20 for char. There are rules above, so it is better to initialize them to 0x00.
