---
title: "What is the biggest difference between Altibase and disk-based DBMS?"
page_id: "16876485"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876485"
updated_at: "2021-04-01T13:21:53.000+0900"
version: 1
ancestors: ["Home", "13. General"]
labels: []
---

# What is the biggest difference between Altibase and disk-based DBMS?
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876485
Updated: 2021-04-01T13:21:53.000+0900

# Overview

---

This document explains the biggest differences between an in-memory DBMS and a disk-based DBMS.

# Version

---

All versions of ALTIBASE HDB

# The biggest difference between In-Memory-based DBMS and Disk-based DBMS

---

As a hybrid DBMS, Altibase supports both in-memory databases and disk-based databases.

- Differences from Altibase HDB's in-memory database:
    1. The location where the database resides is different.

          1. In a disk-based DBMS, the entire database resides on disk and required data is cached in memory buffers. In an in-memory DBMS, the entire backup database that exists on disk is loaded into main memory and managed there.

      ![HDB_architecture.jpeg](https://docs.altibase.com/download/attachments/embedded-page/FAQE/What%20is%20the%20biggest%20difference%20between%20Altibase%20and%20disk-based%20DBMS%3F/HDB_architecture.jpeg?api=v2)
    2. There is a significant difference in performance.
          1. Although almost the same in terms of functionality, in-memory DBMSs are about 4 to 10 times faster than disk-based DBMSs, depending on the operating environment.
          2. Altibase HDB was configured in three modes, Memory Only, Hybrid, and Disk Only, and online transaction processing performance was measured by combining five concurrent transaction types that comply with TPC-C: order, payment, delivery, order status, and stock level transactions. The result showed higher performance than a disk-based DBMS. ![%E1%84%89%E1%85%A5%E1%86%BC%E1%84%82%E1%85%B3%E1%86%BC%E1%84%87%E1%85%B5%E1%84%80%E1%85%AD%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%84%91%E1%85%B3.jpeg](https://docs.altibase.com/download/attachments/embedded-page/FAQE/What%20is%20the%20biggest%20difference%20between%20Altibase%20and%20disk-based%20DBMS%3F/%E1%84%89%E1%85%A5%E1%86%BC%E1%84%82%E1%85%B3%E1%86%BC%E1%84%87%E1%85%B5%E1%84%80%E1%85%AD%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%84%91%E1%85%B3.jpeg?api=v2)

TPC-C is the C model of the benchmark standard used to measure online transaction processing (OLTP) performance.
