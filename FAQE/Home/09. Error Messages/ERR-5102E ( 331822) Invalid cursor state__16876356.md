---
title: "ERR-5102E ( 331822) Invalid cursor state."
page_id: "16876356"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876356"
updated_at: "2021-03-25T17:13:48.000+0900"
version: 3
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# ERR-5102E ( 331822) Invalid cursor state.
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876356
Updated: 2021-03-25T17:13:48.000+0900

- [Overview](#ERR-5102E(331822)Invalidcursorstate.-Overview) - [Version](#ERR-5102E(331822)Invalidcursorstate.-Version) - [Symptom](#ERR-5102E(331822)Invalidcursorstate.-Symptom) - [Cause and Solution](#ERR-5102E(331822)Invalidcursorstate.-CauseandSolution) - [1. When the cursor with the same name is reused without closing the cursor after completing the FETCH](#ERR-5102E(331822)Invalidcursorstate.-1.WhenthecursorwiththesamenameisreusedwithoutclosingthecursoraftercompletingtheFETCH) - [2. When Exception handling is omitted when cursor CLOSE fails after FETCH is completed](#ERR-5102E(331822)Invalidcursorstate.-2.WhenExceptionhandlingisomittedwhencursorCLOSEfailsafterFETCHiscompleted) - [3. When the cursor is reused while the result of the data to be fetched remains](#ERR-5102E(331822)Invalidcursorstate.-3.Whenthecursorisreusedwhiletheresultofthedatatobefetchedremains)

# Overview

---

This error occurs when reusing an opened cursor when handling a statement in an application.

# Version

---

ALTIBASE HDB version 4 or later

"HDB 4.3.9 Error Message" manual or altierr utility "Invalid cursor state." cannot confirm the explanation, but HDB 4.3.9 can also cause this error.

# Symptom

---

- Invalid cursor state occurs when executing CURSOR DECLARE or CURSOR OPEN during CURSOR FETCH in APRE (or SESC).
- Invalid cursor state occurs when executing CURSOR DECLARE or CURSOR OPEN after CURSOR FETCH in APRE (or SESC).
- Invalid cursor state occurs when executing one of SQLExecute(), SQLPrepare(), and SQLExecDirect() while executing SQLFetch() in SQLCLI or ODBC.
- Invalid cursor state occurs when executing one of SQLExecute(), SQLPrepare(), and SQLExecDirect() after executing SQLFetch() in SQLCLI or ODBC.

# Cause and Solution

---

#### 1. When the cursor with the same name is reused without closing the cursor after completing the FETCH

- This is for HDB 5 or later version. In HDB 4 version, there is no error in this case.
- In some cases, an error may occur because the cursor with the same name is reused without executing cursor CLOSE.
- Example code.

  ```
  declare cursor A;
  open cursor A;
  fetch cursor A;       // fetch completed!
  // close cursor A;    // Do not process cursor close!
  declare cursor A;     // Reuse the cursor of the same name!
  ```
- **If this is the case, add a CLOSE statement to the cursor.**

#### 2. When Exception handling is omitted when cursor CLOSE fails after FETCH is completed

- Cursor CLOSE fails, but the exception is not handled, and the cursor is reused with the same name without knowing that the cursor CLOSE failed.
- This is for HDB 5 or later version. In HDB 4 version, there is no error in this case.
- Example code

  ```
  declare cursor A;
  if (  sqlca.sqlcode != SQL_SUCCESS ) {
     exception handling;
  }
  open cursor A;
  if (  sqlca.sqlcode != SQL_SUCCESS ) {
     exception handling;
  }
  fetch cursor A;                                          // fetch completed!
  if (  sqlca.sqlcode != SQL_SUCCESS ) {
     exception handling;
  }

  close cursor A;                                          //  No exception handling.
  /* close cursor A failed!! */

  declare cursor A;
  if (  sqlca.sqlcode != SQL_SUCCESS ) {
     exception handling;
  }
  ```
- **If this is the case, add exception handling to the cursor CLOSE statement and figure out what caused the cursor CLOSE to fail.**

#### **3. When the cursor is reused while the result of the data to be fetched remains**

- If there is data to be fetched in the DB server, the result is deleted when the cursor is closed.
- In other words, the cursor with the same name cannot be reused until the data to be fetched is deleted. In order to reuse, the cursor must be FETCHed after OPENed.

  **Example 1**

  ```
  while(1)
  {
     fetch cursor A             // Data to be fetched remains
     open cursor A             // An error occurs when the cursor with the same name is reused while the data to be fetched remains!
  }
  ```

  ```
  while(1)
  {
     SQLFetch(stmt)          // Data to be fetched remains
     SQLExecute(stmt)      // An error occurs when the cursor with the same name is reused while the data to be fetched remains!
  }
  ```
- **If this is the case, try to reuse the cursor after adding the cursor CLOSE statement.**
