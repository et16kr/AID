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

Problems caused by an increase in the memory usage of the system are usually caused by an increase in data in the application program (user) and in the memory tablespace.

Database memory can increase due to queries used in the application program, which can lead to insufficient memory.

This document examines the parts of memory spaces occupied by Altibase and describes how to resolve it when memory is used abnormally.

This document was written based on Altibase version 7.1 or later.

# Korean Source Attachments

The Korean source page also references these downloadable source attachments. They are preserved here so the English document set does not lose those references.

- [Korean source attachment 1 (PDF)](https://docs.altibase.com/download/attachments/11698518/ALTIBASE_MEM_PBT%EC%A0%88%EC%B0%A8.pdf?version=1&modificationDate=1698815576000&api=v2)
