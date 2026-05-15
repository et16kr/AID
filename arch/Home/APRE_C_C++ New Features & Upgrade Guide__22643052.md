---
title: "APRE*C/C++ New Features & Upgrade Guide"
page_id: "22643052"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=22643052"
updated_at: "2025-10-21T09:58:41.000+0900"
version: 1
ancestors: ["Home"]
labels: []
---

# APRE*C/C++ New Features & Upgrade Guide
Source: https://docs.altibase.com/pages/viewpage.action?pageId=22643052
Updated: 2025-10-21T09:58:41.000+0900

- [Overview](#APRE*C/C++NewFeatures&UpgradeGuide-Overview) - [APRE*C/C++](#APRE*C/C++NewFeatures&UpgradeGuide-APRE*C/C++) - [Terms](#APRE*C/C++NewFeatures&UpgradeGuide-Terms) - [Overview of New Features](#APRE*C/C++NewFeatures&UpgradeGuide-OverviewofNewFeatures) - [Details of New Features](#APRE*C/C++NewFeatures&UpgradeGuide-DetailsofNewFeatures) - [Precautions](#APRE*C/C++NewFeatures&UpgradeGuide-Precautions) - [Notes](#APRE*C/C++NewFeatures&UpgradeGuide-Notes) - [Changes](#APRE*C/C++NewFeatures&UpgradeGuide-Changes) - [Upgrade procedures](#APRE*C/C++NewFeatures&UpgradeGuide-Upgradeprocedures) - [Considerations](#APRE*C/C++NewFeatures&UpgradeGuide-Considerations)

# Overview

---

This document explains the new features and changes of APRE*C/C++, as well as the procedure for upgrading from SESC to APRE.

The document is based on APRE*C/C++ for Altibase 7.3.

It is recommended to refer to the following technical documents to understand the contents of this document.

- [Altibase APRE(SES) *C/C++ Makefile](https://aid.altibase.com/pages/viewpage.action?pageId=15630378)
- [Altibase Precompiler Guide](https://aid.altibase.com/display/arch/Altibase+Precompiler+Guide)

For errors and improvements related to this document, please contact the technical support portal or technical support center

- Technical support portal: [http://support.altibase.com](http://support.altibase.com/)[/en/](http://support.altibase.com/en/)
- Technical support center: 02-2082-1114

# APRE*C/C++

---

This section describes Altibase's new Precompiler of Embedded SQL. Please refer to [Altibase Precompiler Guide](https://aid.altibase.com/display/arch/Altibase+Precompiler+Guide) for specific details such as usage of the function as a summary form.

## Terms

---

****Precompiler of Embedded SQL****

The program that receives source code including embedded SQL and converts the embedded SQL into execution-time library function calls.

**SES*C/C++**

It is an abbreviation of the Precompiler of Embedded SQL for versions lower than Altibase 5.1.5, and supports C and C++ as source code.

**APRE*C/C++**

It is an abbreviation of the Precompiler of Embedded SQL for versions lower than Altibase 5.3.3, and supports C and C++ as source code. Compared to SES*C/C++, the upgrade level function is improved.

## Overview of New Features

---

Many restrictions that existed in SES*C/C++ have been greatly improved.

The name was also changed to APRE*C/C++ (Altibase C/C++ Precompiler of Embedded SQL) while applying the upgrade.

The functions newly added to APRE*C/C++ are as follows:

- Partial C Preprocessor for macro processing
- C Parser for host variable declaration
- Function to rewrite the library to alleviate host variable declaration method and usage restrictions
- DECLARE STATEMENT statement support

In addition, the following improvements were made:

- Function callable when using WHENEVER statement
- APRE*C/C++ executable file (apre) command option has changed and added
- the error message output type has changed
- Supports the RETURNING INTO clause
- The FREE statement is no longer supported; use the DISCONNECT statement instead

## Details of New Features

---

**Equipped with Partial C Preprocessor**

Most of the macros below can be processed without any restrictions on the declaration area.

![(tick)](https://docs.altibase.com/s/en_GB/5637/e1ef10868e8fe2f234a1a0b171b01cde1d9717c4.69/_/images/icons/emoticons/check.png) #include, #define #if, #ifdef, #ifndef, #endif, #else, #elif

![1.Partial%20C%20Preprocessor%20%E1%84%90%E1%85%A1%E1%86%B8%E1%84%8C%E1%85%A2.png](https://docs.altibase.com/download/attachments/embedded-page/arch/APRE*C/C++%20New%20Features%20&%20Upgrade%20Guide/1.Partial%20C%20Preprocessor%20%E1%84%90%E1%85%A1%E1%86%B8%E1%84%8C%E1%85%A2.png?api=v2)

**Equipped with C Parser**

Only when the source code is written in C, the host variable declaration is possible outside the host variable declaration section (DECLARE SECTION).

![C%20parse%20%E1%84%90%E1%85%A1%E1%86%B8%E1%84%8C%E1%85%A2.png](https://docs.altibase.com/download/attachments/embedded-page/arch/APRE*C/C++%20New%20Features%20&%20Upgrade%20Guide/C%20parse%20%E1%84%90%E1%85%A1%E1%86%B8%E1%84%8C%E1%85%A2.png?api=v2)

**Host variable declaration method and ease of using restrictions**

Many restrictions related to the user of host variables have been removed. Details are as follows.

1. The initial value can be assigned at the same time as the host variable declaration

![%E1%84%92%E1%85%A9%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%E1%84%87%E1%85%A7%E1%86%AB%E1%84%89%E1%85%AE_%E1%84%89%E1%85%A5%E1%86%AB%E1%84%8B%E1%85%A5%E1%86%AB%E1%84%80%E1%85%AA_%E1%84%83%E1%85%A9%E1%86%BC%E1%84%89%E1%85%B5%E1%84%8B%E1%85%A6_%E1%84%8E%E1%85%A9%E1%84%80%E1%85%B5%E1%84%80%E1%85%A1%E1%86%B9%E1%84%8B%E1%85%B3%E1%86%AF_%E1%84%92%E1%85%A1%E1%86%AF%E1%84%83%E1%85%A1%E1%86%BC_%E1%84%80%E1%85%A1%E1%84%82%E1%85%B3%E1%86%BC.png](https://docs.altibase.com/download/attachments/embedded-page/arch/APRE*C/C++%20New%20Features%20&%20Upgrade%20Guide/%E1%84%92%E1%85%A9%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%E1%84%87%E1%85%A7%E1%86%AB%E1%84%89%E1%85%AE_%E1%84%89%E1%85%A5%E1%86%AB%E1%84%8B%E1%85%A5%E1%86%AB%E1%84%80%E1%85%AA_%E1%84%83%E1%85%A9%E1%86%BC%E1%84%89%E1%85%B5%E1%84%8B%E1%85%A6_%E1%84%8E%E1%85%A9%E1%84%80%E1%85%B5%E1%84%80%E1%85%A1%E1%86%B9%E1%84%8B%E1%85%B3%E1%86%AF_%E1%84%92%E1%85%A1%E1%86%AF%E1%84%83%E1%85%A1%E1%86%BC_%E1%84%80%E1%85%A1%E1%84%82%E1%85%B3%E1%86%BC.png?api=v2)

2. Structure definition available after typedef (reverse also available)

![typedef_%E1%84%92%E1%85%AE_%E1%84%80%E1%85%AE%E1%84%8C%E1%85%A9%E1%84%8E%E1%85%A6_%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%8B%E1%85%B4_%E1%84%80%E1%85%A1%E1%84%82%E1%85%B3%E1%86%BC.png](https://docs.altibase.com/download/attachments/embedded-page/arch/APRE*C/C++%20New%20Features%20&%20Upgrade%20Guide/typedef_%E1%84%92%E1%85%AE_%E1%84%80%E1%85%AE%E1%84%8C%E1%85%A9%E1%84%8E%E1%85%A6_%E1%84%8C%E1%85%A5%E1%86%BC%E1%84%8B%E1%85%B4_%E1%84%80%E1%85%A1%E1%84%82%E1%85%B3%E1%86%BC.png?api=v2)

3. Array elements can be specified when using array-type host variables in embedded SQL statements.

![%E1%84%82%E1%85%A2%E1%84%8C%E1%85%A1%E1%86%BC_SQL%E1%84%86%E1%85%AE%E1%86%AB%E1%84%8B%E1%85%A6%E1%84%89%E1%85%A5_%E1%84%87%E1%85%A2%E1%84%8B%E1%85%A7%E1%86%AF%E1%84%92%E1%85%A7%E1%86%BC%E1%84%8B%E1%85%B4_%E1%84%92%E1%85%A9%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%E1%84%87%E1%85%A7%E1%86%AB%E1%84%89%E1%85%AE_%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC.png](https://docs.altibase.com/download/attachments/embedded-page/arch/APRE*C/C++%20New%20Features%20&%20Upgrade%20Guide/%E1%84%82%E1%85%A2%E1%84%8C%E1%85%A1%E1%86%BC_SQL%E1%84%86%E1%85%AE%E1%86%AB%E1%84%8B%E1%85%A6%E1%84%89%E1%85%A5_%E1%84%87%E1%85%A2%E1%84%8B%E1%85%A7%E1%86%AF%E1%84%92%E1%85%A7%E1%86%BC%E1%84%8B%E1%85%B4_%E1%84%92%E1%85%A9%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%E1%84%87%E1%85%A7%E1%86%AB%E1%84%89%E1%85%AE_%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC.png?api=v2)

4. Data types other than char * and struct * can be used as pointer type host variables.

![point_%E1%84%8B%E1%85%AC%E1%84%8B%E1%85%B4_%E1%84%83%E1%85%A1%E1%84%85%E1%85%B3%E1%86%AB_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%E1%84%92%E1%85%A7%E1%86%BC%E1%84%83%E1%85%A9_%E1%84%91%E1%85%A9%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%90%E1%85%A5%E1%84%92%E1%85%A7%E1%86%BC_%E1%84%92%E1%85%A9%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%E1%84%87%E1%85%A7%E1%86%AB%E1%84%89%E1%85%AE%E1%84%85%E1%85%A9_%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%80%E1%85%A1%E1%84%82%E1%85%B3%E1%86%BC.png](https://docs.altibase.com/download/attachments/embedded-page/arch/APRE*C/C++%20New%20Features%20&%20Upgrade%20Guide/point_%E1%84%8B%E1%85%AC%E1%84%8B%E1%85%B4_%E1%84%83%E1%85%A1%E1%84%85%E1%85%B3%E1%86%AB_%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5%E1%84%92%E1%85%A7%E1%86%BC%E1%84%83%E1%85%A9_%E1%84%91%E1%85%A9%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%90%E1%85%A5%E1%84%92%E1%85%A7%E1%86%BC_%E1%84%92%E1%85%A9%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%E1%84%87%E1%85%A7%E1%86%AB%E1%84%89%E1%85%AE%E1%84%85%E1%85%A9_%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%80%E1%85%A1%E1%84%82%E1%85%B3%E1%86%BC.png?api=v2)

5. The host variable for output can be used without ":" in INTO clause of the SELECT statement

![select_%E1%84%80%E1%85%AE%E1%84%86%E1%85%AE%E1%86%AB%E1%84%8B%E1%85%B4into%E1%84%8C%E1%85%A5%E1%86%AF%E1%84%8B%E1%85%A6_%E1%84%91%E1%85%AD%E1%84%89%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%8B%E1%85%B5_%E1%84%92%E1%85%A9%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%E1%84%87%E1%85%A7%E1%86%AB%E1%84%89%E1%85%AE_%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%80%E1%85%A1%E1%84%82%E1%85%B3%E1%86%BC.png](https://docs.altibase.com/download/attachments/embedded-page/arch/APRE*C/C++%20New%20Features%20&%20Upgrade%20Guide/select_%E1%84%80%E1%85%AE%E1%84%86%E1%85%AE%E1%86%AB%E1%84%8B%E1%85%B4into%E1%84%8C%E1%85%A5%E1%86%AF%E1%84%8B%E1%85%A6_%E1%84%91%E1%85%AD%E1%84%89%E1%85%B5%E1%84%8B%E1%85%A5%E1%86%B9%E1%84%8B%E1%85%B5_%E1%84%92%E1%85%A9%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%E1%84%87%E1%85%A7%E1%86%AB%E1%84%89%E1%85%AE_%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%80%E1%85%A1%E1%84%82%E1%85%B3%E1%86%BC.png?api=v2)

6. Can be used even if the input host variable of the embedded SQL including the FOR clause is not an array type

![for_%E1%84%8C%E1%85%A5%E1%86%AF%E1%84%8B%E1%85%B4_%E1%84%8B%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A7%E1%86%A8_%E1%84%92%E1%85%A9%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%E1%84%87%E1%85%A7%E1%86%AB%E1%84%89%E1%85%AE%E1%84%80%E1%85%A1_%E1%84%87%E1%85%A2%E1%84%8B%E1%85%A7%E1%86%AF_%E1%84%90%E1%85%A1%E1%84%8B%E1%85%B5%E1%86%B8%E1%84%8B%E1%85%B5_%E1%84%8B%E1%85%A1%E1%84%82%E1%85%B5%E1%84%83%E1%85%A5%E1%84%85%E1%85%A1%E1%84%83%E1%85%A9_%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%80%E1%85%A1%E1%84%82%E1%85%B3%E1%86%BC.png](https://docs.altibase.com/download/attachments/embedded-page/arch/APRE*C/C++%20New%20Features%20&%20Upgrade%20Guide/for_%E1%84%8C%E1%85%A5%E1%86%AF%E1%84%8B%E1%85%B4_%E1%84%8B%E1%85%B5%E1%86%B8%E1%84%85%E1%85%A7%E1%86%A8_%E1%84%92%E1%85%A9%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%E1%84%87%E1%85%A7%E1%86%AB%E1%84%89%E1%85%AE%E1%84%80%E1%85%A1_%E1%84%87%E1%85%A2%E1%84%8B%E1%85%A7%E1%86%AF_%E1%84%90%E1%85%A1%E1%84%8B%E1%85%B5%E1%86%B8%E1%84%8B%E1%85%B5_%E1%84%8B%E1%85%A1%E1%84%82%E1%85%B5%E1%84%83%E1%85%A5%E1%84%85%E1%85%A1%E1%84%83%E1%85%A9_%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%80%E1%85%A1%E1%84%82%E1%85%B3%E1%86%BC.png?api=v2)

7. The union type host variable can be used

![%E1%84%8B%E1%85%B2%E1%84%82%E1%85%B5%E1%84%8B%E1%85%A9%E1%86%AB%E1%84%92%E1%85%A7%E1%86%BC%E1%84%8B%E1%85%B4_%E1%84%92%E1%85%A9%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%E1%84%87%E1%85%A7%E1%86%AB%E1%84%89%E1%85%AE_%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%80%E1%85%A1%E1%84%82%E1%85%B3%E1%86%BC.png](https://docs.altibase.com/download/attachments/embedded-page/arch/APRE*C/C++%20New%20Features%20&%20Upgrade%20Guide/%E1%84%8B%E1%85%B2%E1%84%82%E1%85%B5%E1%84%8B%E1%85%A9%E1%86%AB%E1%84%92%E1%85%A7%E1%86%BC%E1%84%8B%E1%85%B4_%E1%84%92%E1%85%A9%E1%84%89%E1%85%B3%E1%84%90%E1%85%B3%E1%84%87%E1%85%A7%E1%86%AB%E1%84%89%E1%85%AE_%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%80%E1%85%A1%E1%84%82%E1%85%B3%E1%86%BC.png?api=v2)

**Additional support for DECLARE STATEMENT**

The DECLARE STATEMENT is supported as a standard embedded SQL statement.

Identifiers for SQL statements or PL/SQL blocks can be declared so that they can be used in other embedded SQL statements.

![declare_statement_%E1%84%80%E1%85%AE%E1%84%86%E1%85%AE%E1%86%AB_%E1%84%8E%E1%85%AE%E1%84%80%E1%85%A1%E1%84%8C%E1%85%B5%E1%84%8B%E1%85%AF%E1%86%AB.png](https://docs.altibase.com/download/attachments/embedded-page/arch/APRE*C/C++%20New%20Features%20&%20Upgrade%20Guide/declare_statement_%E1%84%80%E1%85%AE%E1%84%86%E1%85%AE%E1%86%AB_%E1%84%8E%E1%85%AE%E1%84%80%E1%85%A1%E1%84%8C%E1%85%B5%E1%84%8B%E1%85%AF%E1%86%AB.png?api=v2)

**Function callable when using WHENEVER statement**

This has been improved so that a specific function can be called when using the WHENEVER statement in the form of WHENEVER <condition> DO <function>.

![whenever%E1%84%80%E1%85%AE%E1%84%86%E1%85%AE%E1%86%AB_%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%89%E1%85%B5_%E1%84%92%E1%85%A1%E1%86%B7%E1%84%89%E1%85%AE_%E1%84%92%E1%85%A9%E1%84%8E%E1%85%AE%E1%86%AF%E1%84%80%E1%85%A1%E1%84%82%E1%85%B3%E1%86%BC.png](https://docs.altibase.com/download/attachments/embedded-page/arch/APRE*C/C++%20New%20Features%20&%20Upgrade%20Guide/whenever%E1%84%80%E1%85%AE%E1%84%86%E1%85%AE%E1%86%AB_%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%89%E1%85%B5_%E1%84%92%E1%85%A1%E1%86%B7%E1%84%89%E1%85%AE_%E1%84%92%E1%85%A9%E1%84%8E%E1%85%AE%E1%86%AF%E1%84%80%E1%85%A1%E1%84%82%E1%85%B3%E1%86%BC.png?api=v2)

**APRE*C/C++ executable file (apre) command option has been changed**

1. -I
  The name has been changed to -I as an option provided as -include option in the existing SES*C/C++.
  This specifies the path of the source doe file included during precompiling.
  This option operations like EXEC SQL OPTION (INCLUDE=library_path) in code
  ![%E1%84%8C%E1%85%A5%E1%86%AB%E1%84%8E%E1%85%A5%E1%84%85%E1%85%B5_%E1%84%89%E1%85%B5_%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%83%E1%85%AC%E1%86%AF_%E1%84%86%E1%85%A2%E1%84%8F%E1%85%B3%E1%84%85%E1%85%A9%E1%84%89%E1%85%A5%E1%86%AB%E1%84%8B%E1%85%A5%E1%86%AB.png](https://docs.altibase.com/download/attachments/embedded-page/arch/APRE*C/C++%20New%20Features%20&%20Upgrade%20Guide/%E1%84%8C%E1%85%A5%E1%86%AB%E1%84%8E%E1%85%A5%E1%84%85%E1%85%B5_%E1%84%89%E1%85%B5_%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%83%E1%85%AC%E1%86%AF_%E1%84%86%E1%85%A2%E1%84%8F%E1%85%B3%E1%84%85%E1%85%A9%E1%84%89%E1%85%A5%E1%86%AB%E1%84%8B%E1%85%A5%E1%86%AB.png?api=v2)

**Command options added to the APRE*C/C++ executable (apre)**

1. -D 전처리(Preprocess)시 사용될 매크로를 선언한다. 이 옵션은 코드 내의 #define 과 같은 기능을 한다.

  |  |
  | --- |
  | `$ apre –DALTIBASE –DOTHER_DBMS -t cpp tmp.sc` |
2. -keyword
  This shows reserved keywords.
  ![%E1%84%8B%E1%85%A8%E1%84%8B%E1%85%A3%E1%86%A8%E1%84%83%E1%85%AC%E1%86%AB_%E1%84%8F%E1%85%B5%E1%84%8B%E1%85%AF%E1%84%83%E1%85%B3%E1%84%83%E1%85%B3%E1%86%AF%E1%84%8B%E1%85%B3%E1%86%AF_%E1%84%87%E1%85%A9%E1%84%8B%E1%85%A7%E1%84%8C%E1%85%AE%E1%86%B7.png](https://docs.altibase.com/download/attachments/embedded-page/arch/APRE*C/C++%20New%20Features%20&%20Upgrade%20Guide/%E1%84%8B%E1%85%A8%E1%84%8B%E1%85%A3%E1%86%A8%E1%84%83%E1%85%AC%E1%86%AB_%E1%84%8F%E1%85%B5%E1%84%8B%E1%85%AF%E1%84%83%E1%85%B3%E1%84%83%E1%85%B3%E1%86%AF%E1%84%8B%E1%85%B3%E1%86%AF_%E1%84%87%E1%85%A9%E1%84%8B%E1%85%A7%E1%84%8C%E1%85%AE%E1%86%B7.png?api=v2)

**-parse *parsing_mode***

a. By specifying the parsing mode, the precompile range for the source file is determined.

b. The parsing mode and processing range of the -parse option are as follows.

c. If the -parse option itself is omitted, the parsing mode is operated as partial.

| Parsing mode | Internal SQL A | Macro B | External declaration part/<br>host variable<br>C | Remarks |
| --- | --- | --- | --- | --- |
| none | O | X | X | Operates the same as SEC*C/C++ #include format header file is not processed |
| partial | O | O | X | Additional operation of Partial C Processor Process even header files in #include format APRE*C/C++ default parsing mode |
| full | O | O | O | Additional operation of C Parser Process even header files in #include format However, source code written in C++ style cannot recognize host variables outside the declaration section |

In the case of [Processing up to #include type header file], even another header file declared as #include type in the corresponding header file is processed. ![main.sc_header.h.png](https://docs.altibase.com/download/attachments/embedded-page/arch/APRE*C/C++%20New%20Features%20&%20Upgrade%20Guide/main.sc_header.h.png?api=v2)

For example, after changing the query in the example above to an optional query using macros as shown below. ![%E1%84%86%E1%85%A2%E1%84%8F%E1%85%B3%E1%84%85%E1%85%A9%E1%84%85%E1%85%B3%E1%86%AF_%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB_%E1%84%89%E1%85%A5%E1%86%AB%E1%84%90%E1%85%A2%E1%86%A8%E1%84%8C%E1%85%A5%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB_%E1%84%8F%E1%85%AF%E1%84%85%E1%85%B5%E1%84%85%E1%85%A9_%E1%84%87%E1%85%A7%E1%86%AB%E1%84%80%E1%85%A7%E1%86%BC%E1%84%92%E1%85%AE.png](https://docs.altibase.com/download/attachments/embedded-page/arch/APRE*C/C++%20New%20Features%20&%20Upgrade%20Guide/%E1%84%86%E1%85%A2%E1%84%8F%E1%85%B3%E1%84%85%E1%85%A9%E1%84%85%E1%85%B3%E1%86%AF_%E1%84%89%E1%85%A1%E1%84%8B%E1%85%AD%E1%86%BC%E1%84%92%E1%85%A1%E1%86%AB_%E1%84%89%E1%85%A5%E1%86%AB%E1%84%90%E1%85%A2%E1%86%A8%E1%84%8C%E1%85%A5%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB_%E1%84%8F%E1%85%AF%E1%84%85%E1%85%B5%E1%84%85%E1%85%A9_%E1%84%87%E1%85%A7%E1%86%AB%E1%84%80%E1%85%A7%E1%86%BC%E1%84%92%E1%85%AE.png?api=v2)

When the parsing option is omitted and precompile with partial(the default parsing mode)

![partial%E1%84%85%E1%85%A9%20preccompile_%E1%84%92%E1%85%A1%E1%86%AF_%E1%84%80%E1%85%A7%E1%86%BC%E1%84%8B%E1%85%AE.png](https://docs.altibase.com/download/attachments/embedded-page/arch/APRE*C/C++%20New%20Features%20&%20Upgrade%20Guide/partial%E1%84%85%E1%85%A9%20preccompile_%E1%84%92%E1%85%A1%E1%86%AF_%E1%84%80%E1%85%A7%E1%86%BC%E1%84%8B%E1%85%AE.png?api=v2) The actual created codes remain only in the stage that the macro processing is completed as follows. (After the macro processing, the removed part is replaced with a blank space). ![%E1%84%87%E1%85%AE%E1%86%AF%E1%84%91%E1%85%B5%E1%86%AF%E1%84%8B%E1%85%AD%E1%84%92%E1%85%A1%E1%86%AB%E1%84%87%E1%85%AE%E1%84%87%E1%85%AE%E1%86%AB_%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%A2%E1%86%A8.png](https://docs.altibase.com/download/attachments/embedded-page/arch/APRE*C/C++%20New%20Features%20&%20Upgrade%20Guide/%E1%84%87%E1%85%AE%E1%86%AF%E1%84%91%E1%85%B5%E1%86%AF%E1%84%8B%E1%85%AD%E1%84%92%E1%85%A1%E1%86%AB%E1%84%87%E1%85%AE%E1%84%87%E1%85%AE%E1%86%AB_%E1%84%80%E1%85%A9%E1%86%BC%E1%84%87%E1%85%A2%E1%86%A8.png?api=v2)

If -parse none is specified to precompile in the same way as the existing SEC*C/C++, a variable duplicate declaration error occurs because the macro processing function does not operate. ![%E1%84%87%E1%85%A7%E1%86%AB%E1%84%89%E1%85%AE_%E1%84%8C%E1%85%AE%E1%86%BC%E1%84%87%E1%85%A9%E1%86%A8%E1%84%89%E1%85%A5%E1%86%AB%E1%84%8B%E1%85%A5%E1%86%AB_%E1%84%8B%E1%85%A6%E1%84%85%E1%85%A5.png](https://docs.altibase.com/download/attachments/embedded-page/arch/APRE*C/C++%20New%20Features%20&%20Upgrade%20Guide/%E1%84%87%E1%85%A7%E1%86%AB%E1%84%89%E1%85%AE_%E1%84%8C%E1%85%AE%E1%86%BC%E1%84%87%E1%85%A9%E1%86%A8%E1%84%89%E1%85%A5%E1%86%AB%E1%84%8B%E1%85%A5%E1%86%AB_%E1%84%8B%E1%85%A6%E1%84%85%E1%85%A5.png?api=v2)

## **Precautions**

---

**Syntax improvement**

In order for existing SES*C/C++ to describe EXEC SQL BEGIN/END DECLARE/ARGUMENT SECTION in the code, it is irrelevant even if the terminator ";" is omitted, but APRE*C/C++ must have ";".

This precaution applies the same as other DBMS precompilers.

The following is an error when the terminator is not specified in the END DECLARE SECTION.

![%E1%84%8C%E1%85%A9%E1%86%BC%E1%84%80%E1%85%A7%E1%86%AF%E1%84%8C%E1%85%A1_%E1%84%82%E1%85%AE%E1%84%85%E1%85%A1%E1%86%A8_%E1%84%8B%E1%85%A6%E1%84%85%E1%85%A5.png](https://docs.altibase.com/download/attachments/embedded-page/arch/APRE*C/C++%20New%20Features%20&%20Upgrade%20Guide/%E1%84%8C%E1%85%A9%E1%86%BC%E1%84%80%E1%85%A7%E1%86%AF%E1%84%8C%E1%85%A1_%E1%84%82%E1%85%AE%E1%84%85%E1%85%A1%E1%86%A8_%E1%84%8B%E1%85%A6%E1%84%85%E1%85%A5.png?api=v2)

**Source code precompile of C++ style**

To use a host variable outside the host variable declaration section, the mode of the parse option must be set to full.

However, if the parsing mode is set to full, the C parser operates, so the source code of C++ style may cause various parsing errors during preprocessing.

In other words, source code written in C++ style should declare host variables only in the host variable declaration section such as SES*C/C++, and if the -parse option is used, the parsing mode should be partial or none.

**-D, -I Options**

If the -D and -I options are used in the C/C++ compilation stage, in most cases, correct precompile is possible only when the same option is given in the precompile stage with APRE*C/C++.

## **Notes**

---

**-I Option**

It is fine to use -include, but it is recommended to change to a new option in consideration of future maintenance.

**Binary data type change**

The name of the previously used SES_CLOB, SES_BLOB, SES_BINARY, SES_BYTES, and SES_NIBBLE types have changed to APRE_CLOB, APRE_BLOB, APRE_BINARY, APRE_BYTES, and APRE_NIBBLE.

Since backward compatibility is considered, it is okay to use an existing name.

# Changes

---

This section describes considerations and procedures when upgrading from SES*C/C++ environment to the ARPE*C/C++ environment.

As the name was changed from SES*C/C++ to APRE*C/C++, the name of execution file, header file, library file, link option, and execution file command options were partially changed as follows.

| **Classification** | **SES*C/C++** | **APRE*C/C++** | **Related file path** | **Remarks** |
| --- | --- | --- | --- | --- |
| Execution file | sesc | apre | $ALTIBASE_HOME/bin | Changed |
| Header file | ses.h | ulpLibInterface.h | $ALTIBASE_HOME/include | Changed |
| Library files | libsesc.a | libapre.a | $ALTIBASE_HOME/lib | Changed |
| libsesc_sl.so | libapre_sl.so | #ALTIBASE_HOME/lib | Changed |  |
| Link option | -lsesc | -lapre | - | Changed |
| Execution file command option | -include | -include or -I | - | Added |

There are no other measures to be taken since the above changes are backward compatible, but it is recommended to change the execution file name and link option to APRE*C/C++ style for future maintenance.

In addition, although it is not essential, it is recommended to change the -include option to -I.

## Upgrade procedures

---

The procedure for upgrading from SES*C/C++ to APRE*C/C++ development environment is as follows:

Refer to the table in the Changes section, execute the relevant statements, and modify options in compilation files such as link options and the makefile.

1. 1. Change the execution file name
      ![%E1%84%89%E1%85%B5%E1%86%AF%E1%84%92%E1%85%A2%E1%86%BC%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%86%AF%E1%84%86%E1%85%A7%E1%86%BC_%E1%84%87%E1%85%A7%E1%86%AB%E1%84%80%E1%85%A7%E1%86%BC.png](https://docs.altibase.com/download/attachments/embedded-page/arch/APRE*C/C++%20New%20Features%20&%20Upgrade%20Guide/%E1%84%89%E1%85%B5%E1%86%AF%E1%84%92%E1%85%A2%E1%86%BC%E1%84%91%E1%85%A1%E1%84%8B%E1%85%B5%E1%86%AF%E1%84%86%E1%85%A7%E1%86%BC_%E1%84%87%E1%85%A7%E1%86%AB%E1%84%80%E1%85%A7%E1%86%BC.png?api=v2)
    2. Change the link option
      ![%E1%84%85%E1%85%B5%E1%86%BC%E1%84%8F%E1%85%B3%E1%84%8B%E1%85%A9%E1%86%B8%E1%84%89%E1%85%A7%E1%86%AB_%E1%84%87%E1%85%A7%E1%86%AB%E1%84%80%E1%85%A7%E1%86%BC.png](https://docs.altibase.com/download/attachments/embedded-page/arch/APRE*C/C++%20New%20Features%20&%20Upgrade%20Guide/%E1%84%85%E1%85%B5%E1%86%BC%E1%84%8F%E1%85%B3%E1%84%8B%E1%85%A9%E1%86%B8%E1%84%89%E1%85%A7%E1%86%AB_%E1%84%87%E1%85%A7%E1%86%AB%E1%84%80%E1%85%A7%E1%86%BC.png?api=v2)
    3. makefile
      ![makefile.png](https://docs.altibase.com/download/attachments/embedded-page/arch/APRE*C/C++%20New%20Features%20&%20Upgrade%20Guide/makefile.png?api=v2)

If the file related to a change is not easily identified or cannot be changed due to the large amount, the procedure in the example above can be omitted, but it is recommended to do a normal upgrade by changing the related name as much as possible.

## Considerations

**-Adding parse none option**

**APRE*C/C++ -> [Notes] ->** Although the syntax is not mentioned in the section, the source that was precompiled without any problems in SES*C/C++ may cause an error in APRE*C/C++. In this case, since the parsing mode of APRE*C/C++ is partial, it is likely an error that occurs while macro processing up to the header file included in the #include method.

Therefore, if the cause of the error is not easily specified, it is necessary to check by adding the -parse none option to precompile the same as SES*C/C++.

**-Error due to use of the precompiler library**

If the existing source code is written to use the SES*C/C++ library directly, compilation may not be possible due to the change of the precompiler library interface. In this case, all related codes must be removed from the existing source code.

The library interface of the precompiler is an internal element that is frequently changed, and used directly by the user is prohibited.

Therefore, Altibase is not responsible for any errors that occur in the future while analyzing the precompiled source code and using the related macros, structures, and functions in the source code arbitrarily.
