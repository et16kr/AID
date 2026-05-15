---
title: "ERR-311E0 The estimated size of the index key exceeds the maximum limit"
page_id: "6979717"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-311E0+The+estimated+size+of+the+index+key+exceeds+the+maximum+limit"
updated_at: "2014-11-19T16:48:10.000+0900"
version: 17
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-311E0 The estimated size of the index key exceeds the maximum limit
Source: https://docs.altibase.com/display/FAQE/ERR-311E0+The+estimated+size+of+the+index+key+exceeds+the+maximum+limit
Updated: 2014-11-19T16:48:10.000+0900

- [Version](#ERR-311E0Theestimatedsizeoftheindexkeyexceedsthemaximumlimit-Version)
- [Explanation](#ERR-311E0Theestimatedsizeoftheindexkeyexceedsthemaximumlimit-Explanation)
- [Cause](#ERR-311E0Theestimatedsizeoftheindexkeyexceedsthemaximumlimit-Cause)
- [Action](#ERR-311E0Theestimatedsizeoftheindexkeyexceedsthemaximumlimit-Action)
- [Reference](#ERR-311E0Theestimatedsizeoftheindexkeyexceedsthemaximumlimit-Reference)

## Version

6.1.1 or below

This error message is not output for 6.3.1 or above.

## Explanation

This error occurs when an ORDER BY, GROUP BY or JOIN is used for disk tables.

## Cause

The following error description can be viewed with the AltiErr utility:

$ altierr 0x311E0 0x311E0 ( 201184) qpERR_ABORT_QDX_MAXIMUM_KEY_SIZE_EXCEED The estimated size of the index key exceeds the maximum limit.

# *Cause:

#- The estimated size of the index key exceeds the maximum limit.

# *Action:

# - Please reduce the number of key columns.

The temporary tablespace is used when an ORDER BY, GROUP BY or JOIN is executed on a disk table.

The temporary tablespace is a disk tablespace and has the fixed page size of 8K.

However, this error occurs when a record that is bigger than 8K was created while using the temporary tablespace.

Note: If the size of a single page (8K) of the disk tablespace is exceeded, the data length is approximately greater than or equal to 3000 bytes.

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
```

[ERR-311E0 : The estimated size of the index key exceeds the maximum limit.](#)

# Example(6.3.1)

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

## Action

1. You can use the hint ‘TEMP_TBS_MEMORY’ to avoid the size limit (8K) of disk temporary tablespaces.

When this hint is used, the temporary area is used in memory instead of disk. Thus, query performance is also improved.

```
iSQL> SELECT  /*+ TEMP_TBS_MEMORY */ * FROM T1 ORDER BY I1;
I1
--------------
1
2
3
3 rows selected.
```

2. Upgrade to 6.3.1 or above. This error does not occur in 6.3.1 or above.

## Reference

<How to use a hint>

```
iSQL>SELECT * FROM t1 ORDER BY c2;
iSQL>SELECT /*+ TEMP_TBS_MEMORY */ * FROM t1 ORDER BY c2;
```
