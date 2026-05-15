---
title: "Disk Configuration Guide for Altibase"
page_id: "14647508"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/Disk+Configuration+Guide+for+Altibase"
updated_at: "2021-02-19T15:01:31.000+0900"
version: 3
ancestors: ["Home"]
labels: []
---

# Disk Configuration Guide for Altibase
Source: https://docs.altibase.com/display/arch/Disk+Configuration+Guide+for+Altibase
Updated: 2021-02-19T15:01:31.000+0900

# **Overview**

---

For a recovery technique based on WAL (Write-Ahead Logging) protocol, DBMS records redo log and then changes/saves/deletes data is a general transaction process. Both redo logs and data require persistent physical storage space. Each storage space can be organized on the same disk or on a separate physical disk. When configuring the redo log and data storage space on the same disk, it must take as consideration because I/O contention for disk access may occur in the process of processing numerous transactions at the same time. This document describes how ALTIBASE handles the redo log recording storage and data recording state, and recommends disk configuration methods to minimize the disk bottlenecks.

The test environment of this document is as follows.

- ALTIBASE: Altibase version 6 or later

For errors and improvements related to this document, please contact the technical support portal or technical support center

- Technical support portal: [http://support.altibase.com/en/](http://support.altibase.com/en/)
- Technical support center: 02-2082-1114
