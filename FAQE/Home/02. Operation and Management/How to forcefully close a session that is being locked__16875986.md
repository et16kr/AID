---
title: "How to forcefully close a session that holds a lock"
page_id: "16875986"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/How+to+forcefully+close+a+session+that+is+being+locked"
updated_at: "2021-03-11T14:31:33.000+0900"
version: 1
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# How to forcefully close a session that holds a lock
Source: https://docs.altibase.com/display/FAQE/How+to+forcefully+close+a+session+that+is+being+locked
Updated: 2021-03-11T14:31:33.000+0900

- [Overview](#Howtoforcefullycloseasessionthatisbeinglocked-Overview) - [Version](#Howtoforcefullycloseasessionthatisbeinglocked-Version) - [Solution](#Howtoforcefullycloseasessionthatisbeinglocked-Solution) - [Reference](#Howtoforcefullycloseasessionthatisbeinglocked-Reference)

# Overview

---

This is a method for forcibly closing a session that holds a lock.

# Version

---

ALTIBASE HDB version 4 or later

# Solution

---

It must be performed by accessing the sys account.

1. Check the table name, transaction ID, and lock type in v$lock.

```
 Select a.table_name, b.trans_id, b.lock_desc From system_.sys_tables_ a, v$lock b
 Where a.table_oid = b.table_oid;
```

2. Use the trans_id obtained above to find the session.

```
Select session_id, execute_flag, total_time, execute_time, rpad(query,400)  From v$statement
Where tx_id = trans_id obtained from above;
```

3. Use the session_id to check the session information.

```
Select comm_name, client_app_info From v$session
Where id = session_id obtained from above;
```

4. Disconnect the session.

```
iSQL> Alter database mydb session close session_id;
For `mydb`, use the database name from the `DB_NAME` setting in `$ALTIBASE_HOME/conf/altibase.properties`.
For `session_id`, enter the session ID obtained above.
```

# Reference

---

- A session with rollback in progress is not disconnected even if `session close` is executed, so wait until rollback finishes.

- For information about the above `V$` views or `SYSTEM_META_TABLE` columns, refer to the Admin manual.
