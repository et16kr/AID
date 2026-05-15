---
title: "ODBC function, SQLFreeStmt"
page_id: "16876183"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ODBC+function%2C+SQLFreeStmt"
updated_at: "2021-03-23T09:00:00.000+0900"
version: 2
ancestors: ["Home", "07. Development and API", "ODBC"]
labels: []
---

# ODBC function, SQLFreeStmt
Source: https://docs.altibase.com/display/FAQE/ODBC+function%2C+SQLFreeStmt
Updated: 2021-03-23T09:00:00.000+0900

**- [Overview](#ODBCfunction,SQLFreeStmt-Overview) - [Version](#ODBCfunction,SQLFreeStmt-Version) - [SQLFreeStmt options](#ODBCfunction,SQLFreeStmt-SQLFreeStmtoptions)**

# Overview

---

This document describes how to use the ODBC function and SQLFreeStmt.

# Version

---

- This document is written based on ALTIBASE HDB version 6.3.1
- For additional information or updates, please leave a request at [http://support.altibase.com/en/](http://support.altibase.com/en/) or in a comment section on this page.

# SQLFreeStmt options

---

The following four options are described.

|  |  |
| --- | --- |
| SQL_CLOSE | Close the cursor associated with stmt and discard all pending results. The application can reopen this cursor later by executing the SELECT statement again using the same or different variables. If no cursor is open, this option has no effect on the application. |
| SQL_DROP | The resources associated with the input statement handle are released and the handle is invalidated. If there is an open cursor, it is closed and all pending results are discarded. |
| SQL_UNBIND | All columns bound by previous `SQLBindCol()` calls on this statement handle are released. |
| SQL_RESET_PARAMS | All parameters set by previous `SQLBindParameter()` calls on this statement handle are released. The association between the application variable or file reference and the SQL statement parameter marker in the statement handle is broken. |

Among these, SQL_CLOSE and SQL_DROP are mainly used.

1. SQLFreeStmt(stmt, SQL_DROP):
  This means that the resources for the prepared `stmt` (statement handle) are completely freed.
  Call this only when that `stmt` will not be reused.
2. SQLFreeStmt(stmt, SQL_CLOSE):
  If all the retrieved data have not been fetched, an error will occur if you execute SQLExecute again without SQLFreeStmt(SQL_CLOSE).
  If `SQLFreeStmt(stmt, SQL_CLOSE)` is used, the existing `stmt` can be reused without calling `SQLAllocStmt()`.
