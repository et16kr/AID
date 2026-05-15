---
title: "ERR-11036 The data file is in use."
page_id: "16876380"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876380"
updated_at: "2021-04-05T11:18:39.000+0900"
version: 3
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# ERR-11036 The data file is in use.
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876380
Updated: 2021-04-05T11:18:39.000+0900

- [Version](#ERR-11036Thedatafileisinuse.-Version) - [Symptom](#ERR-11036Thedatafileisinuse.-Symptom) - [Cause](#ERR-11036Thedatafileisinuse.-Cause) - [Solution](#ERR-11036Thedatafileisinuse.-Solution)

# Version

---

All the versions of Altibase

# Symptom

---

The following error occurs when executing alter tablespace ~ drop datafile.

```
iSQL> alter tablespace SYS_TBS_DISK_DATA drop datafile '/altibase/dbs/DISK_DATA2.dbf';
[ERR-11036 : The data file is in use.|ERR-11036 : The data file is in use.]
```

# Cause

---

The description of the error can be checked using the altierr utility as follows.

$ altierr 0x0109D 0x11036 ( 69686) smERR_ABORT_CannotRemoveDataFileNode The data file is in use. # *Cause: The data file is in use. # *Action: Please remove an unnecessary data file.

Data files that have been used at least once cannot be deleted.

Even if all the data files have only free space by inserting and then deleting them, data files that have been used once cannot be deleted.

The above error occurs when you try to drop a data file that has been used at least once.

For reference, data files that have never been used can be dropped.

# Solution

---

There is no way to drop data files that have been used at least once.

To drop the data file, the tablespace must be recreated.

The following steps are required to recreate the tablespace.

1) Export object creation script and data created in the tablespace

2) Drop & create tablespace

3) Create object and import data
