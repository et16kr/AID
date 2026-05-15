---
title: "Altibase APRE(SES) *C/C++ Makefile"
page_id: "15630378"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=15630378"
updated_at: "2021-01-19T10:40:48.000+0900"
version: 3
ancestors: ["Home"]
labels: []
---

# Altibase APRE(SES) *C/C++ Makefile
Source: https://docs.altibase.com/pages/viewpage.action?pageId=15630378
Updated: 2021-01-19T10:40:48.000+0900

# Overview

---

This document describes how to compile using the APRE (formerly SESC)*C/C++ precompiler provided by Altibase on the Unix system and how to solve problems that may occur at each stage of compilation.

Examples and descriptions used in this document were written in the Linux and GCC compilation environment, and additional information has been described so that other compiler users of other UNIX environments (HP, SUN, AIX) can refer to them.

It is recommended to refer to the following documents in advance.

1. Altibase Precompiler Guide
2. Altibase APRE New Features Upgrade Guide

The test environment of this document is as follows:

- ALTIBASE : Altibase version 6 and later
- OS : Linux ( 2.6.32-504.el6.x86_64 )
- Compiler version : gcc version 4.4.7 20120313 (Red Hat 4.4.7-11) (GCC)

For errors and improvements related to this document, please contact the technical support portal or technical support center.

- Technical support portal: [http://support.altibase.com](http://support.altibase.com/) > Technical Knowledge > Q&A
- Technical support center: 02-2082-1114
