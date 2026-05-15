---
title: "What interface does Altibase provide?"
page_id: "22642982"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=22642982"
updated_at: "2025-10-20T15:55:59.000+0900"
version: 1
ancestors: ["Home", "13. General"]
labels: []
---

# What interface does Altibase provide?
Source: https://docs.altibase.com/pages/viewpage.action?pageId=22642982
Updated: 2025-10-20T15:55:59.000+0900

# - [Overview](#WhatinterfacedoesAltibaseprovide?-Overview) - [Version](#WhatinterfacedoesAltibaseprovide?-Version) - [Interface provided by Altibase](#WhatinterfacedoesAltibaseprovide?-InterfaceprovidedbyAltibase) - [Client development environment](#WhatinterfacedoesAltibaseprovide?-Clientdevelopmentenvironment) - [Server development environment](#WhatinterfacedoesAltibaseprovide?-Serverdevelopmentenvironment)

# Overview

---

This document explains the interfaces provided by Altibase.

# Version

---

All the versions of Altibase HDB

# Interface provided by Altibase

---

- Altibase complies with the international standard ANSI SQL-1999 and provides various standard interfaces such as ODBC, ADO. Net, JDBC, and Embedded SQL.

### Client development environment

| **Interface type** | Support function |
| --- | --- |
| ODBC | - RAD (Rapid Application Development) tools such as Visual Basic and PowerBuilder, as well as used when accessing ALTIBASE in most development environments<br>- Reinforced standard support with re-implementation |
| JDBC | - Used when developing ALTIBASE application programs in JAVA environment<br>- Also used when configuring a connection pool in WAS<br>- Improved performance with re-implementation<br>- JDBC 2.0 API support up to Altibase 6.1.1, JDBC 3.0 API support partially.<br>- JDBC 3.0 API support from Altibase 6.3.1.<br>- Altibase 7.1.0 and later: Supports JDBC 3.0 API and partial support for JDBC 4.2 API.<br>- Altibase 7.3.0 and later: Provides full support for JDBC 4.2 API. |
| SQLCLI | - ALTIBASE's low-level API based on C language<br>- Provide LOB API, ALA (ALTIBASE Log Analyzer) API, ACS (ALTIBASE Call-Level for Spatial) API |
| Embedded<br>SQL (Pre-Compiler) | - Interface used by the host language of C or C++<br>- Improved development productivity by using SQL statements as they are in the host language |
| ADO.NET | - Up to Altibase 6.5.1: Provided .NET Data Provider based on the .NET Framework.<br>- From Altibase 7.1.0.8.3 / 7.3.0.0.5 and later: Provides Altibase ADO.NET based on .NET Core 3.1. |
| Unix ODBC | - Standard DB connection API compatible with Windows ODBC source on Unix<br>- Provide compatibility with ETL tools such as DataStage and Informatica and OLAP tools such as MSTR and Sagent |
| PDO | - PDO interface is provided based on PHP 5.3.3, PHP 7.1.20, and PHP 8.1.8. |
| Hibernate Support | - Support for Hibernate 6.4 is available starting from Altibase 7.1.0.9.2 and Altibase 7.3.0.0.2. |

### Server development environment

| Function | Characterstic |
| --- | --- |
| SQL | - Support Full Featured SQL92<br>- Support international standard complex query such as Sub Query INLINE view |
| Built-in Function | - Provides more than 100 built-in functions<br>- Users can perform various operations in SQL statements by using Built-in Function |
| Stored Procedure & Function | - Support Stored Procedure and Stored Function based on ANSI SQL standard<br>- Result Set can be sent to the client in the procedure<br>- Support structured type and array type within procedure<br>- Support Dynamic SQL/DDL within the procedure |
| View | - Efficiently query by unioning multiple tables or creating a specific SQL as a view |
| Trigger | - Support Trigger by standard for business function in the form of data events<br>- Support Update Trigger for a specific column |
