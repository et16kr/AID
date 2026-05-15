---
title: "What is aexport, iloader?"
page_id: "16876105"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876105"
updated_at: "2021-03-18T11:12:15.000+0900"
version: 2
ancestors: ["Home", "04. Backup and Recovery", "Using aexport and iloader"]
labels: []
---

# What is aexport, iloader?
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876105
Updated: 2021-03-18T11:12:15.000+0900

# aexport

---

aexport is a utility that creates scripts that can download object creation scripts and data from the database as text files.

The database objects that aexport can extract are as follows:

- Database user
- User privilege
- Tablespace
- Table
- Table constraint
- Index
- View
- Materialized view (Provided starting from ALTIBASE HDB 6.3.1)
- Stored procedure
- Replication object

It is recommended that aexport be performed whenever there is a database object change.

# iloader

---

iloader is a utility that allows you to download or upload database data in table units. The data is saved in a text file that can be viewed by the user.

This can be used for database migration or table-by-table backup purposes.

To back up table data using iloader, a form file and various options are required. If aexport is executed, the iloader execution command is created as a script.
