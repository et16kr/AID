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

1. **Stop the replication**

  Execute this on the server where the replication sender thread is running. With the statement below, the local server's replication sender thread and the remote server's receiver thread are stopped.

  ```
  iSQL> ALTER REPLICATION replication_name STOP;

  -- Check the replication running status
  iSQL> SELECT REPLICATION_NAME, DECODE(IS_STARTED, 0, 'STOPPED', 1, 'STARTED') IS_STARTED FROM SYSTEM_.SYS_REPLICATIONS_;
  ```
2. **Add the replication target table**

  This statement adds a replication target table to the replication object. Execute it on each replication target server.

  ```
  iSQL> ALTER REPLICATION replication_name ADD TABLE FROM user_name.table_name TO user_name.table_name;
  ```

  Check whether the table was added to the replication object.

  ```
  iSQL> SELECT REPLICATION_NAME, LOCAL_USER_NAME, LOCAL_TABLE_NAME FROM SYSTEM_.SYS_REPL_ITEMS_;
  ```
3. **SYNC the replication**

  If the data on both servers does not match, truncate the table on one server and then execute the `SYNC` statement on the server that has the data to make the data consistent. If the data already matches on both servers, proceed to step 4 and start replication.

  ```
  iSQL> ALTER REPLICATION replication_name SYNC ONLY TABLE user_name.table_name;
  ```
4. **Start the replication**

  If the data on both servers matches, execute the replication start statement.

  ```
  iSQL> ALTER REPLICATION replication_name START;

  -- Check the replication running status.
  iSQL> SELECT REPLICATION_NAME, DECODE(IS_STARTED, 0, 'STOPPED', 1, 'STARTED') IS_STARTED FROM SYSTEM_.SYS_REPLICATIONS_;
  ```

# Deleting replication target table

---

- This is the procedure for deleting tables to be replicated in the replication object.

1. **Stop the replication**

  Execute this on the server where the replication sender thread is running. With the statement below, the local server's replication sender thread and the remote server's receiver thread are stopped.

  ```
  iSQL> ALTER REPLICATION replication_name STOP;

  -- Check the replication running status.
  iSQL> SELECT REPLICATION_NAME, DECODE(IS_STARTED, 0, 'STOPPED', 1, 'STARTED') IS_STARTED FROM SYSTEM_.SYS_REPLICATIONS_;
  ```
2. **Delete the replication target table**

  This statement deletes the replication target table from the replication object. Execute it on each replication target server.

  ```
  iSQL> ALTER REPLICATION replication_name DROP TABLE FROM user_name.table_name TO user_name.table_name;

  -- Statement for checking the replication target table.
  iSQL> SELECT REPLICATION_NAME, LOCAL_USER_NAME, LOCAL_TABLE_NAME FROM SYSTEM_.SYS_REPL_ITEMS_;
  ```
3. **Start the replication**

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
