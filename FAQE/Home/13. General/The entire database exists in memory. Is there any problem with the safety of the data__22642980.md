---
title: "The entire database exists in memory. Is there any problem with the safety of the data?"
page_id: "22642980"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=22642980"
updated_at: "2025-10-20T15:55:10.650+0900"
version: 1
ancestors: ["Home", "13. General"]
labels: []
---

# The entire database exists in memory. Is there any problem with the safety of the data?
Source: https://docs.altibase.com/pages/viewpage.action?pageId=22642980
Updated: 2025-10-20T15:55:10.650+0900

**- [Overview](#Theentiredatabaseexistsinmemory.Isthereanyproblemwiththesafetyofthedata?-Overview) - [Version](#Theentiredatabaseexistsinmemory.Isthereanyproblemwiththesafetyofthedata?-Version) - [How to secure](#Theentiredatabaseexistsinmemory.Isthereanyproblemwiththesafetyofthedata?-Howtosecure) - [Disability management operation plan](#Theentiredatabaseexistsinmemory.Isthereanyproblemwiththesafetyofthedata?-Disabilitymanagementoperationplan)**

# Overview

---

This document describes a technique to guarantee the data stability of the volatile main memory.

# Version

---

- The information is applicable to all versions of ALTIBASE HDB.
- For additional information or updates, please leave a request at [http://support.altibase.com/en/](http://support.altibase.com/en/) or in the comment section on this page.

# How to secure

---

1. WAL protocol method
  WAL (Write Ahead Logging) logging method is used when transaction processing is used to provide database persistence and to secure stability for committed transactions. When the number of log files exceeds a certain number or a fixed period, the changed data page in the memory is displayed. The recovery time is minimized through checkpoints that are written to the disk.
  * WAL: The procedure for saving logs to disk first and then saving DB pages. The last transaction information is stored on the disk, so it can be recovered through the transaction log in case of abnormal termination.
2. Backup and recovery support
  Backup creates a logical/physical copy of the database in case of an abnormal situation in the DBMS. Such a copy of the database can be created online during the DB operation, and in a recovery situation, the database can be normalized by performing complete or incomplete recovery by using the backed up database copy.

# Disability management operation plan

---

| Type | Description |  |
| --- | --- | --- |
| Transaction<br>Failure | Cause | • Occur due to interruption of a transaction by internal or external factors |
| Solution | • Maintain database consistency by automatically recovering data with normal transaction rollback. |  |
| System<br>Failure | Cause | • Occur due to faults in the operating system or failures such as power outages |
| Solution | • Automatic recovery to the state until the point of system failure with the backup data file and Active Log when the system is restarted (Restart Recovery) |  |
| Disk<br>Failure | Cause | • Occur due to corruption of the backup data file due to an error in the disk where the backup data file is stored |
| Solution | • If there is a previous data backup file, it can be restored to the latest database with this file.<br>• However, if the log disk is damaged or the archive log is deleted, recovery to the most recent state is impossible. |  |
