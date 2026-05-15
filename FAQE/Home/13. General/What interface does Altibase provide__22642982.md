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

Altibase HDB 6.1.1 or later

# Interface provided by Altibase

---

- Altibase complies with the international standard ANSI SQL-1999 and provides various standard interfaces such as ODBC, ADO.NET, JDBC, and Embedded SQL.

### Client development environment

| **Interface type** | Supported functions |
| --- | --- |
| ODBC | - Used to access ALTIBASE from most development environments, including RAD (Rapid Application Development) tools such as Visual Basic and PowerBuilder<br>- Reinforces standard support through reimplementation |
| JDBC | - Used when developing ALTIBASE application programs in a Java environment<br>- Also used when configuring a connection pool in WAS<br>- Improves performance through reimplementation<br>- Supports JDBC 2.0 API up to Altibase 6.1.1, with partial support for JDBC 3.0 API<br>- Supports JDBC 3.0 API from Altibase 6.3.1<br>- Supports JDBC 3.0 API and partial JDBC 4.2 API from Altibase 7.1.0<br>- Supports JDBC 4.2 API from Altibase 7.3.0 |
| SQLCLI | - Altibase's low-level API based on C language<br>- Provides LOB API, ALA (ALTIBASE Log Analyzer) API, and ACS (ALTIBASE Call-Level for Spatial) API |
| Embedded<br>SQL (Pre-Compiler) | - Interface used from C or C++ host languages<br>- Improves development productivity because SQL statements can be used as-is in the host language |
| ADO.NET | - Up to Altibase 6.5.1: Provided .NET Data Provider based on the .NET Framework.<br>- From Altibase 7.1.0.8.3 / 7.3.0.0.5 and later: Provides Altibase ADO.NET based on .NET Core 3.1. |
| Unix ODBC | - Standard DB connection API compatible with Windows ODBC source on Unix<br>- Provides compatibility with ETL tools such as DataStage and Informatica and OLAP tools such as MSTR and Sagent |
| PDO | - PDO interface is provided based on PHP 5.3.3, PHP 7.1.20, and PHP 8.1.8. |
| Hibernate Support | - Support for Hibernate 6.4 is available starting from Altibase 7.1.0.9.2 and Altibase 7.3.0.0.2. |

### Server development environment

| Function | Characteristic |
| --- | --- |
| SQL | - Supports full-featured SQL92<br>- Supports internationally standardized complex queries such as Sub Query and INLINE View<br>- Supports tuning by using hints and SQL execution plans |
| Built-in Function | - Provides more than 100 built-in functions<br>- Users can perform various operations in SQL statements by using built-in functions |
| Stored Procedure & Function | - Supports Stored Procedure and Stored Function based on the ANSI SQL standard<br>- Result Set can be sent to the client from a procedure<br>- Supports Structured Type and Array Type within procedures<br>- Supports Dynamic SQL/DDL within procedures |
| View | - Efficiently queries by unioning multiple tables or creating a view from specific SQL |
| Trigger | - Supports standard Trigger functionality for business logic based on data events<br>- Supports Update Trigger for a specific column |
