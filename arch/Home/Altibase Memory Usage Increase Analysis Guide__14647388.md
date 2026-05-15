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

The database memory is loaded due to queries used int the application program, which can lead to insufficient memory.

This document examines the parts of memory spaces occupied by Altibase and describes how to resolve it when memory is used abnormally.

This document was written based on Altibase version 7.1 or later.
