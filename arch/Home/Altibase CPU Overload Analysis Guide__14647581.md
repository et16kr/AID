---
title: "Altibase CPU Overload Analysis Guide"
page_id: "14647581"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/Altibase+CPU+Overload+Analysis+Guide"
updated_at: "2021-02-22T13:18:22.000+0900"
version: 5
ancestors: ["Home"]
labels: []
---

# Altibase CPU Overload Analysis Guide
Source: https://docs.altibase.com/display/arch/Altibase+CPU+Overload+Analysis+Guide
Updated: 2021-02-22T13:18:22.000+0900

# **Overview**

---

The CPU load of the system is basically caused by the application program (User) and the kernel (Sys/Kernel). Cases created by the kernel are generally when events about system resource usage occur, and other cases are mostly used by application programs. In the case of Altibase, various algorithms are applied to process queries (transactions) created by users, and use of various system resources such as communication and replication with clients connected to DB, and disk I/O by processing data files occurs. CPU usage of both the User area and the Sys/Kernel area occurs.

This document describes what parts to examine when the CPU utilization rate occupied by Altibase increases, whether it is normal/abnormal, and how to solve it in abnormal cases.

It is recommended to refer to the following documents in advance.

- Altibase Development Guide
- Altibase SQL Tuning Guide
- Altibase Monitoring Query Guide

The test environment of this document is as follows.

- Altibase: Altibase version 6 or later
- OS: Linux (2.6.32-504.el6.x86_64)

For errors and improvements related to this document, please contact the technical support portal or technical support center

- Technical support portal: [http://support.altibase.com](http://support.altibase.com/)[/en/](http://support.altibase.com/en/)
- Technical support center: 02-2082-1114

# Korean Source Attachments

The Korean source page also references these downloadable source attachments. They are preserved here so the English document set does not lose those references.

- [Korean source attachment 1 (PDF)](https://docs.altibase.com/download/attachments/11698396/ALTIBASE_CPU_PBT%EC%A0%88%EC%B0%A8.pdf?version=1&modificationDate=1698801484000&api=v2)
