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

**- [Overview](#Theentiredatabaseexistsinmemory.Isthereanyproblemwiththesafetyofthedata?-Overview) - [Version](#Theentiredatabaseexistsinmemory.Isthereanyproblemwiththesafetyofthedata?-Version) - [How to secure data durability](#Theentiredatabaseexistsinmemory.Isthereanyproblemwiththesafetyofthedata?-Howtosecuredatadurability) - [Failure management operation plan](#Theentiredatabaseexistsinmemory.Isthereanyproblemwiththesafetyofthedata?-Failuremanagementoperationplan)**

# Overview

---

This document describes techniques that secure data durability for volatile main memory.

# Version

---

- The information is applicable to all versions of ALTIBASE HDB.
- For additional information or updates, please leave a request at [http://support.altibase.com/en/](http://support.altibase.com/en/) or in the comment section on this page.

# How to secure data durability

---

1. WAL protocol method
  Altibase uses WAL (Write Ahead Logging) during transaction processing to provide database durability and protect committed transactions. When the number of log files exceeds a configured threshold or a fixed interval is reached, checkpoints write changed memory data pages to disk, minimizing recovery time.
  * WAL: The procedure for saving logs to disk before saving DB pages. Because the latest transaction information is stored on disk, the database can be recovered through transaction logs after abnormal termination.
2. Backup and recovery support
  Backup creates a logical or physical copy of the database in case an abnormal DBMS situation occurs. This database copy can be created online during database operation. During recovery, the database can be brought back to a normal state by performing complete or incomplete recovery with the backed-up database copy.

# Failure management operation plan

---

| Type | Classification | Description |
| --- | --- | --- |
| Transaction Failure | Cause | Occurs when a transaction is interrupted by internal or external factors. |
| Transaction Failure | Resolution | Maintain database consistency by automatically recovering data through normal transaction rollback. |
| System Failure | Cause | Occurs due to operating system defects or failures such as power outages. |
| System Failure | Resolution | When the system restarts, Altibase automatically recovers to the state at the point of system failure by using backup data files and active logs. This is restart recovery. |
| Disk Failure | Cause | Occurs when a backup data file is corrupted because of an error on the disk where the backup data file is stored. |
| Disk Failure | Resolution | If a previous data backup file exists, the database can be restored with that file. However, if the log disk is damaged or archive logs are deleted, recovery to the most recent state is impossible. |
