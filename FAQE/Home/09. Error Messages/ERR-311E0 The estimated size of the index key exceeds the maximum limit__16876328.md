---
title: "ERR-311E0 The estimated size of the index key exceeds the maximum limit."
page_id: "16876328"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876328"
updated_at: "2021-04-05T10:51:28.000+0900"
version: 2
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# ERR-311E0 The estimated size of the index key exceeds the maximum limit.
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876328
Updated: 2021-04-05T10:51:28.000+0900

- [Version](#ERR-311E0Theestimatedsizeoftheindexkeyexceedsthemaximumlimit.-Version) - [Symptom](#ERR-311E0Theestimatedsizeoftheindexkeyexceedsthemaximumlimit.-Symptom) - [Cause](#ERR-311E0Theestimatedsizeoftheindexkeyexceedsthemaximumlimit.-Cause) - [Solution](#ERR-311E0Theestimatedsizeoftheindexkeyexceedsthemaximumlimit.-Solution)

# Version

---

Version 6.1.1 or earlier.

No error occurs in version 6.3.1 or later.

# Symptom

---

The following error occurs when using join or Order by / Group by on a disk table.

[ERR-311E0: The estimated size of the index key exceeds the maximum limit.]

# Cause

---

The description of the error can be checked using the altierr utility as follows.

$ altierr 0x311E0 0x311E0 ( 201184) qpERR_ABORT_QDX_MAXIMUM_KEY_SIZE_EXCEED The estimated size of the index key exceeds the maximum limit. # *Cause: # - The estimated size of the index key exceeds the maximum limit. # *Action: # - Please reduce the number of key columns.

When performing joins or order by / group by on a **disk table**, Altibase uses Temp Tablespace internally.

Temp Tablespace is a Disk Tablespace and has a fixed page size of 8K. When using Temp Tablespace, the above error may occur if there is a need to create more than 8K records.

For reference, if the size of the disk tablespace exceeds 1Page(8K), the data length is approximately 3000Bytes or more.

# Example

```
iSQL> CREATE TABLE T1( I1 CHAR(6000) ) TABLESPACE SYS_TBS_DISK_DATA;
Create success.
iSQL> insert into t1 values(1);
1 row inserted.
iSQL> insert into t1 values(2);
1 row inserted.
iSQL> insert into t1 values(3);
1 row inserted.
iSQL> SELECT * FROM T1 ORDER BY I1;
[ERR-311E0 : The estimated size of the index key exceeds the maximum limit.]
```

# Example of 6.3.1 version

```
iSQL> CREATE TABLE T1( I1 CHAR(6000) ) TABLESPACE SYS_TBS_DISK_DATA;
Create success.
iSQL> insert into t1 values(1);
1 row inserted.
iSQL> insert into t1 values(2);
1 row inserted.
iSQL> insert into t1 values(3);
1 row inserted.
iSQL> SELECT * FROM T1 ORDER BY I1;
I1
--------------
1
2
3
3 rows selected.
```

# Solution

---

1. The TEMP_TBS_MEMORY hint can be used to avoid the 1 Page (8K) size limitation of the disk temp tablespace.

In addition, this hint is effective in improving query performance because the memory area is used instead the disk as the temp area.

```
iSQL> SELECT  /*+ TEMP_TBS_MEMORY */ * FROM T1 ORDER BY I1;
I1
--------------
1
2
3
3 rows selected.
```

2. Upgrade to version 6.3.1 or higher.

In version 6.3.1 or later, this error does not occur in the same situation.
