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

# Version

---

All the versions of Altibase

# The biggest difference between In-Memory-based DBMS and Disk-based DBMS

---

As an Altibase Hybrid DBMS, it supports both In-Memory DB and Disk-based DB.

- Differences from Altibase HDB's In-Memory DB
    1. When operating DBMS, the location where the database resides is different.

          1. In a disk-based DBMS, the entire database resides on the disk and the necessary data is cached and managed in the memory buffer, whereas the in-memory DBMS is managed by residing the entire backup database on the disk in the main memory.

      ![HDB_architecture.jpeg](https://docs.altibase.com/download/attachments/embedded-page/FAQE/What%20is%20the%20biggest%20difference%20between%20Altibase%20and%20disk-based%20DBMS%3F/HDB_architecture.jpeg?api=v2)
    2. There is a significant difference in performance.
          1. Although almost the same in terms of functionality, in-memory DBMSs are about 4 to 10 times faster than disk-based DBMSs, depending on the operating environment.
          2. Altibase HDB is divided into three methods: Memory Only, Hybrid, and Disk Only, and five virtual simultaneous transactions that meet TPC-C standards. As a result of measuring online transaction processing performance by combining (order transaction, payment transaction, shipping transaction, order status transaction, stock level transaction), it showed higher performance than Disk DBMS. ![%E1%84%89%E1%85%A5%E1%86%BC%E1%84%82%E1%85%B3%E1%86%BC%E1%84%87%E1%85%B5%E1%84%80%E1%85%AD%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%84%91%E1%85%B3.jpeg](https://docs.altibase.com/download/attachments/embedded-page/FAQE/What%20is%20the%20biggest%20difference%20between%20Altibase%20and%20disk-based%20DBMS%3F/%E1%84%89%E1%85%A5%E1%86%BC%E1%84%82%E1%85%B3%E1%86%BC%E1%84%87%E1%85%B5%E1%84%80%E1%85%AD%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%84%91%E1%85%B3.jpeg?api=v2)

C model of the benchmark standard that measures the processing performance of an online transaction processing (OLTP) system
