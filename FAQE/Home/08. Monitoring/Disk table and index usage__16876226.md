---
title: "Disk table and index usage"
page_id: "16876226"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Disk+table+and+index+usage"
updated_at: "2021-03-23T13:58:29.000+0900"
version: 1
ancestors: ["Home", "08. Monitoring"]
labels: []
---

# Disk table and index usage
Source: https://docs.altibase.com/display/FAQE/Disk+table+and+index+usage
Updated: 2021-03-23T13:58:29.000+0900

- [Overview](#Disktableandindexusage-Overview) - [Reference](#Disktableandindexusage-Reference)

# Overview

---

This document summarizes disk table and index usage retrieve queries by version.

The user can use the following two methods for disk table usage. This page provides queries using v$segment(x$segment).

- v$segment: A method of calculating physical pages while full-scanning a table
- v$usage: A sampling method using statistical information

# Reference
