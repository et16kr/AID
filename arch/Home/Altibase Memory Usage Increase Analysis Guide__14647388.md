---
title: "Altibase Memory Usage Increase Analysis Guide"
page_id: "14647388"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/Altibase+Memory+Usage+Increase+Analysis+Guide"
updated_at: "2020-08-18T16:12:03.000+0900"
version: 2
ancestors: ["Home"]
labels: []
---

# Altibase Memory Usage Increase Analysis Guide
Source: https://docs.altibase.com/display/arch/Altibase+Memory+Usage+Increase+Analysis+Guide
Updated: 2020-08-18T16:12:03.000+0900

# Overview

---

Problems caused by increased system memory usage are usually caused by application programs (users) or by data growth in memory tablespaces.

Queries used by applications can load database memory and lead to insufficient available memory. When data is managed in memory tablespaces for high-performance Altibase processing, accumulated data can also increase storage space usage and lead to insufficient available memory.

This document examines the memory areas occupied by Altibase and describes how to respond when Altibase uses memory abnormally.

It is recommended to refer to the following documents in advance.

1. [Altibase Developer Guide](http://aid.altibase.com/x/2gRw)
2. [Altibase SQL Tuning Guide](http://aid.altibase.com/x/owGr)
3. [Altibase Monitoring Query Guide](http://aid.altibase.com/x/j4KZ)
4. Altibase Memory Tablespace Management
5. Altibase MVCC & GC

The test environment of this document is as follows.

- Altibase: Altibase version 7 or later
- OS: Linux (2.6.32-504.el6.x86_64)

For errors and improvements related to this document, contact the technical support portal or technical support center.

- Technical support portal: [http://support.altibase.com](http://support.altibase.com/) > Technical Knowledge > Q&A
- Technical support center: 02-2082-1114

# Korean Source Attachments

The Korean source page also references these downloadable source attachments. They are preserved here so the English document set does not lose those references.

- [Korean source attachment 1 (PDF)](https://docs.altibase.com/download/attachments/11698518/ALTIBASE_MEM_PBT%EC%A0%88%EC%B0%A8.pdf?version=1&modificationDate=1698815576000&api=v2)
