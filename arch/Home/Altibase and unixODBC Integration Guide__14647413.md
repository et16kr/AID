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

This document describes how to integrate with the ODBC driver Manager for Unix by using the odbc driver for UNIX provided by ALTIBASE. This document described based on the ODBC Driver Manager provided from [http://www.unixodbc.org/.](http://www.unixodbc.org/.)

This document is based on the native compiler for each device, and in the case of gcc/g++ since there are no special precautions except for the compilation byte, it is not described separately. In addition, since the installation of unixODBC and the establishment of all environments for installation is a matter for the user, ALTIBASE does not provide technical support services for this part.

The test environment of this document is as follows:

- ALTIBASE: Altibase 6.3.1
- OS: Linux ( 2.6.32-504.el6.x86_64 )
- unixODBC: unixODBC-2.3.2

For errors and improvements related to this document, please contact the technical support portal or technical support center

- Technical support portal: [http://support.altibase.com](http://support.altibase.com/)[/en/](http://support.altibase.com/en/)
- Technical support center: 02-2082-1114
