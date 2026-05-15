---
title: "DDL operation on the table for Altibase replication"
page_id: "22642943"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/DDL+operation+on+the+table+for+Altibase+replication"
updated_at: "2025-10-20T15:23:29.000+0900"
version: 1
ancestors: ["Home", "03. Replication"]
labels: []
---

# DDL operation on the table for Altibase replication
Source: https://docs.altibase.com/display/FAQE/DDL+operation+on+the+table+for+Altibase+replication
Updated: 2025-10-20T15:23:29.000+0900

- [Overview](#DDLoperationonthetableforAltibasereplication-Overview) - [Version](#DDLoperationonthetableforAltibasereplication-Version) - [Procedure](#DDLoperationonthetableforAltibasereplication-Procedure) - [Operation under service outages](#DDLoperationonthetableforAltibasereplication-Operationunderserviceoutages) - [Operation under uninterrupted constraints](#DDLoperationonthetableforAltibasereplication-Operationunderuninterruptedconstraints)

# Overview

---

In general, DDL operations on the DB require an exclusive lock on the table. ALTIBASE HDB uses network-based replication in which data is kept consistent by transmitting transaction logs generated on the local server to the peer server.

DDL-like operations are not sent to the log, so DDL operations are not replicated. Therefore, different from the disk sharing method, a different method of performing DDL operations on each node (Server) is required.

# Version

---

The types of DDL statements supported by ALTIBASE HDB vary depending on the version, and the features of DDL statements related to replication also differ.

For detailed information, please refer to the manual for your specific version at [http://support.altibase.com/kr/manual](http://support.altibase.com/kr/manual).

# Procedure

---

## Operation under service outages

In an environment where all services accessing the database can be stopped for a certain period of time, the operation can be completed with a relatively simple procedure.

| Step | A node | B node |
| --- | --- | --- |
| STEP 1 | - **Stop the service (take action to prevent transactions from occurring)**<br>- To block the service reliably, the DB may be stopped, the service port may be changed, and then the DB may be started again before performing the operation.<br>- Check sessions connected to the database or statements currently being executed.<br>- iSQL> select count(*) from v$session;<br>- iSQL> select count(*) from v$statement where execute_flag =1 ; |  |
| STEP 2 | - **Check that the replication gaps of the target nodes are all "0" (this means the DB where the replication sender is driven)**<br>- Check the replication object to which the target table for DDL execution belongs<br>          - iSQL> select REPLICATION_NAME,LOCAL_USER_NAME, LOCAL_TABLE_NAME from SYSTEM_.SYS_REPL_ITEMS_;<br>- Check the replication gap<br>- iSQL> SELECT rep_name, rep_gap FROM v$repgap; # Check that rep_gap is all 0. |  |
| STEP 3 | - **Stop the replication of target node**<br>    - iSQL> ALTER REPLICATION *rep_name* STOP; # The replication object (REP_NAME) is checked in STEP 2. |  |
| STEP 4 | - **Remove the target table to execute DDL from the replication object**<br>    - iSQL> ALTER REPLICATION *rep_name* DROP TABLE FROM *user_name.table_name* TO *user_name.table_name*; |  |
| STEP 5 | - **Perform DDL operation**<br>- iSQL> ALTER TABLE t1 ADD COLUMN ( c1 INTEGER); |  |
| STEP 6 | - **Add the replication target table removed in STEP 4 back to the replication object list**<br>    - iSQL> ALTER REPLICATION *rep_name* ADD TABLE FROM *user_name.table_name* TO *user_name.table_name*; |  |
| STEP 7 | - **Start the replication at the target node**<br>- iSQL> ALTER REPLICATION *rep_name* START |  |
| STEP 8 | - **Initiate the service**<br>- If the service port number of the DB is changed in STEP 1, restore the service port and restart the database.<br>- After restarting the DB service by running the application, check the DB status. |  |

## Operation under uninterrupted constraints

---

In an environment that requires uninterrupted service, there may be a limitation that one node must alternately work one node at a time while operating the database.

Under these conditions, more steps are required than in an environment where service interruption is allowed, and extra caution may be required.

- For details, refer to the manual for your Altibase version at [http://support.altibase.com/kr/manual](http://support.altibase.com/kr/manual).
- Get technical support from the ALTIBASE Technical Support Division. Service portal: [http://support.altibase.com](http://support.altibase.com), TEL +82-2-2082-1114.
