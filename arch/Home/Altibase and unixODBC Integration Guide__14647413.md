---
title: "Altibase and unixODBC Integration Guide"
page_id: "14647413"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/Altibase+and+unixODBC+Integration+Guide"
updated_at: "2020-08-19T11:20:32.000+0900"
version: 2
ancestors: ["Home"]
labels: []
---

# Altibase and unixODBC Integration Guide
Source: https://docs.altibase.com/display/arch/Altibase+and+unixODBC+Integration+Guide
Updated: 2020-08-19T11:20:32.000+0900

# **Overview**

---

This document describes how to integrate the ODBC Driver Manager for Unix with the ODBC driver for Unix provided by Altibase. This document is based on the ODBC Driver Manager provided by [http://www.unixodbc.org/](http://www.unixodbc.org/).

This document assumes the native compiler for each platform. For gcc/g++, there are no special cautions other than the compile bit type, so gcc/g++ is not described separately. Installing unixODBC and preparing the installation environment are user responsibilities, so Altibase does not generally provide technical support for that part.

The test environment of this document is as follows:

- Altibase: Altibase 6.3.1
- OS: Linux ( 2.6.32-504.el6.x86_64 )
- unixODBC: unixODBC-2.3.2

For errors and improvements related to this document, contact the technical support portal or technical support center.

- Technical support portal: [http://support.altibase.com](http://support.altibase.com/) -> Technical Knowledge -> Q&A
- Technical support center: 02-2082-1114
