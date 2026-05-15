---
title: "How a query is executed in ALTIBASE HDB"
page_id: "1802795"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/How+a+query+is+executed+in+ALTIBASE+HDB"
updated_at: "2011-08-06T11:41:29.000+0900"
version: 14
ancestors: ["Home", "ALTIBASE HDB Architecture"]
labels: []
---

# How a query is executed in ALTIBASE HDB
Source: https://docs.altibase.com/display/FAQE/How+a+query+is+executed+in+ALTIBASE+HDB
Updated: 2011-08-06T11:41:29.000+0900

![unknown-macro](https://docs.altibase.com/plugins/servlet/confluence/placeholder/unknown-macro?name=gliffy&locale=en_GB&version=2)

There are four steps when ALTIBASE HDB executes a query. These steps are as follows:

# Parsing

Parser checks the syntax of SQL text. If no errors are detected in the SQL, Parser generates "Parse Tree" which is used in Validator. Parser does not look up any information in the system tables, and does not access the database.

# Validating

Validator accesses various system tables in the database to verify that all database objects referenced by the SQL exist, such as tables, columns, views, types, PSMs, etc. If there are no errors, Validator generates "Checked Parse Tree".

# Optimizing

After checking validity of the SQL, Optimizer tries to find out the best way to execute the given "Checked Parse Tree", and then it generates "Plan Tree". There are many sophisticated algorithms and strategies in the ALTIBASE HDB optimization process. If you'd like to know more about the optimization in ALTIBASE HDB, you can refer to the "SQL Tuning" section in [Administrator's Manual](http://atc.altibase.com/sub09/551b/html/Admin/ch10.html).

# Executing

The last phase executes the query. Executor executes the SQL using the given Plan Tree.
