---
title: "How to add/delete replication target table"
page_id: "16876094"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876094"
updated_at: "2021-04-05T09:36:11.000+0900"
version: 3
ancestors: ["Home", "03. Replication"]
labels: []
---

# How to add/delete replication target table
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876094
Updated: 2021-04-05T09:36:11.000+0900

- [Overview](#Howtoadd/deletereplicationtargettable-Overview) - [Version](#Howtoadd/deletereplicationtargettable-Version) - [Adding replication target table](#Howtoadd/deletereplicationtargettable-Addingreplicationtargettable) - [Deleting replication target table](#Howtoadd/deletereplicationtargettable-Deletingreplicationtargettable) - [Reference documents](#Howtoadd/deletereplicationtargettable-Referencedocuments)

# Overview

---

This document describes how to add or delete replication target tables in the replication object.

# Version

---

Altibase version 4.3.9 or later

# Adding replication target table

---

- This is the procedure for adding tables to be replicated in the replication object.

1. **Stop the replication** Execute in the server where the replication sending thread is running. With the statement below, the replication sender of the local server and the receive thread of the remote server are stopped.

  ```
  iSQL> ALTER REPLICATION replication_name STOP;

  -- Check the replication running status
  iSQL> SELECT REPLICATION_NAME, DECODE(IS_STARTED, 0, 'STOPPED', 1, 'STARTED') IS_STARTED FROM SYSTEM_.SYS_REPLICATIONS_;
  ```
2. **Add the replication target table**

  ```
  iSQL> SELECT REPLICATION_NAME, LOCAL_USER_NAME, LOCAL_TABLE_NAME FROM SYSTEM_.SYS_REPL_ITEMS_;
  ```
3. **SYNC the replication** If the data on both servers do not match, TRUNCATE one server table and then perform a SYNC statement on the server where the data exists to match the data. If the data matches on both servers 4, start the replication.

  ```
  iSQL> ALTER REPLICATION replication_name SYNC ONLY TABLE user_name.table_name;
  ```
4. **Start the replication** If the data on both servers match each other, execute the replication start statement.

  ```
  iSQL> ALTER REPLICATION replication_name START;

  -- Chcek the replication running status.
  iSQL> SELECT REPLICATION_NAME, DECODE(IS_STARTED, 0, 'STOPPED', 1, 'STARTED') IS_STARTED FROM SYSTEM_.SYS_REPLICATIONS_;
  ```

# Deleting replication target table

---

- This is the procedure for deleting tables to be replicated in the replication object.

1. **Stop the replication** Execute in the server where the replication sending thread is running. With the statement below, the replication sender of the local server and the receive thread of the remote server are stopped.

  ```
  iSQL> ALTER REPLICATION replication_name STOP;

  -- Chcek the replication running status.
  iSQL> SELECT REPLICATION_NAME, DECODE(IS_STARTED, 0, 'STOPPED', 1, 'STARTED') IS_STARTED FROM SYSTEM_.SYS_REPLICATIONS_;
  ```
2. Delete the replication target table

  This is the statement for deleting the replication target table in the replication object in each of the replication target servers.

  ```
  iSQL> ALTER REPLICATION replication_name DROP TABLE user_name.table_name TO user_name.table_name;

  -- Statement for checking the replication target table.
  iSQL> SELECT REPLICATION_NAME, LOCAL_USER_NAME, LOCAL_TABLE_NAME FROM SYSTEM_.SYS_REPL_ITEMS_;
  ```
3. Start the replication

  ```
  iSQL> ALTER REPLICATION replication_name START;

  -- Check the replication running status
  iSQL> SELECT REPLICATION_NAME, DECODE(IS_STARTED, 0, 'STOPPED', 1, 'STARTED') IS_STARTED FROM SYSTEM_.SYS_REPLICATIONS_;
  ```

# Reference documents

---

- For syntax explanation and additional options of the ALTER REPLICATION statement, refer to SQL Reference Manual -> 3. Data Definition Language -> ALTER REPLICATION.
- Manual download page: [http://support.altibase.com/en/manual](http://support.altibase.com/en/manual)
- Github: [https://github.com/ALTIBASE/Documents/tree/master/Manuals/](https://github.com/ALTIBASE/Documents/tree/master/Manuals/Altibase_7.1/eng)
