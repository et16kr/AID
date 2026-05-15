---
title: "Altibase Oracle Conversion Guide"
page_id: "14647316"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/Altibase+Oracle+Conversion+Guide"
updated_at: "2021-02-18T17:36:43.000+0900"
version: 2
ancestors: ["Home"]
labels: []
---

# Altibase Oracle Conversion Guide
Source: https://docs.altibase.com/display/arch/Altibase+Oracle+Conversion+Guide
Updated: 2021-02-18T17:36:43.000+0900

# Overview

This document describes the procedure for converting Oracle DBMS to ALTIBASE HDB version 6.3.

For errors and improvements related to this document, please contact the technical support portal or technical support center

- Technical support portal: [http://support.altibase.com](http://support.altibase.com/)[/en/](http://support.altibase.com/en/)
- Technical support center: 02-2082-1114

## Migration Process

![intro1.png](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20Oracle%20Conversion%20Guide/intro1.png?api=v2)

| Phase | Contents | Output | Management |  |
| --- | --- | --- | --- | --- |
| 1st Phase | System analysis | Requirement analysis | System analysis report | - DBA<br>- APP Developer |
| Environment analysis<br>- OS, HW, SW, etc. | - DBA<br>- APP Developer |  |  |  |
| DBMS analysis<br>- Data size (case, byte)<br>- Number of objects (Table, Index, etc.)<br>- Tablespace Size<br>- Function, Procedure | - DBA<br>- APP Developer |  |  |  |
| Business analysis<br>- The ratio of online/located businesses<br>- Query complexity of batch business |  | - DBA<br>- APP Developer |  |  |
| 2nd Phase | Impact analysis | Risk impact analysis | Impact report | - DBA<br>- APP Developer |
| Analysis of the relationship between the application and the database for table usage, and related matrices | - DBA<br>- APP Developer |  |  |  |
| 3rd Phase | Planning | Schedule planning establishment | Schedule | - PM |
| Support staffs plan establishment |  |  |  |  |
| 4th Phase | Data Migration | Conversion using Migration Center<br>-Schema and data included |  | - DBA |
| Manual conversion for non-standard schema and SP | - Developer |  |  |  |
| Data verification | - DBA<br>- APP Developer |  |  |  |
| 5th Phase | Optimization | Configuration optimization with parameter tuning | Optimization result report | - DBA |
| Performance optimization with SQL and procedure tuning | - DBA<br>- APP Developer |  |  |  |
