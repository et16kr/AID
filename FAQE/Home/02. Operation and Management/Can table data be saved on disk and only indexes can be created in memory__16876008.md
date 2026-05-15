---
title: "Can table data be saved on disk and only indexes can be created in memory?"
page_id: "16876008"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876008"
updated_at: "2021-03-11T17:54:29.000+0900"
version: 2
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# Can table data be saved on disk and only indexes can be created in memory?
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876008
Updated: 2021-03-11T17:54:29.000+0900

# Phenomenon

---

Since indexes are basically created in the same type as the table, indexes of disk tables cannot be created in the memory tablespace, and an ERR-311EC error is displayed.

- **Create test table T1 in disk tablespace**

|  |
| --- |
| iSQL> create table t1 (c1 char(10), c2 char(5)) tablespace **SYS_TBS_DISK_DATA**; Create success. |

- **Create an index for the test table in the memory tablespace**

If the user tries to create a disk table index in the memory tablespace (SYS_TBS_MEM_DATA) as shown below, an ERR-311EC error occurs.

|  |
| --- |
| iSQL> create index idx_t1 on t1(c1 desc) tablespace **SYS_TBS_MEM_DATA**; [ERR-311EC : The type (memory/disk/volatile) of the tablespace in which to create the index is not the same as the type of the table.] |

# Solution

---

If the index of the disk table is created in the disk tablespace, it is created normally without causing an error.

- **Create disk table index in disk tablespace**

  |  |
  | --- |
  | iSQL> create index idx_t1 on t1(c1 desc) tablespace **SYS_TBS_DISK_DATA**; Create success. |
