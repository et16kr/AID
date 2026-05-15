---
title: "Lock related properties"
page_id: "16876204"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Lock+related+properties"
updated_at: "2021-04-05T09:58:44.000+0900"
version: 2
ancestors: ["Home", "08. Monitoring"]
labels: []
---

# Lock related properties
Source: https://docs.altibase.com/display/FAQE/Lock+related+properties
Updated: 2021-04-05T09:58:44.000+0900

**- [Overview](#Lockrelatedproperties-Overview) - [Version](#Lockrelatedproperties-Version) - [How to monitor](#Lockrelatedproperties-Howtomonitor)**

- [Overview](#Lockrelatedproperties-Overview) - [Version](#Lockrelatedproperties-Version) - [How to monitor](#Lockrelatedproperties-Howtomonitor)

# Overview

---

The user can monitor performance degradation due to transaction lock.

# Version

---

- This document is written based on Altibase HDB version 6.3.1.
- Both ALTIBASE HDB 5 and ALTIBASE HDB 6 can be used, but some monitoring items may cause a result error.
- For more information and updates, please leave a request at [http://support.altibase.com/en/](http://support.altibase.com/en/) or in the comment section on this page.

# How to monitor

---

First of all, there are two performance views for the lock information of Altibase.

These are v$loc and v$lock_statement.

First, in v$lock, the user can inquire what type of lock is applied to a table. In the case of a select statement, IX_LOCK will be locked in case of changes such as IS_LOCK, insert, update, delete, etc.

By joining this view and the system_.sys_tables_ meta table, the user can check table name and lock information.

```
select table_name , lock_desc
from system_.sys_tables_ a, v$lock b
where a.table_oid = b.table_oid;
```

In addition, the user can also check which queries are holding the lock with v$lock_statement.

The user can check the query holding the lock by joining the trans_id of v$lock and the tx_id of v$lock_statement.

```
select query
from v$lock a, v$lock_statement b
where a.trans_id = b.tx_id;
```

The user can check the session ID of the query currently holding the lock by using multiple joins.

desc v$lock;

With v$lock_statement;, check which columns are existed.

the session can also be killed with the session_id obtained in this wa.

```
ALTER DATABASE database_name SESSION CLOSE session_id;
```

The above command can be executed by entering sysdba.

```
connect sys/manager as sysdba;
```

++ Lock wait query

```
select query, tx_id
from v$statement
where tx_id in ( select trans_id from v$lock_wait);
```

++ Look up based on v$lock_wait view, such as tx_id waiting, lock grant time, related redo logfile location, etc.

```
select
id tx_id,
lw.wait_for_trans_id wait_tx_id,
decode (status,0,'BEGIN',
1,'PRECOMMIT',
2,'COMMIT_IN_MEMORY',
3,'COMMIT',
4,'ABORT',
5,'BLOCKED',
6,'END', 'UNKNOWN') status,
decode(update_status,0,'READ',1,'UPDATING','UNKNOWN') TTYPE,
decode(first_undo_next_lsn_fileno,-1,'READ_TRN',first_undo_next_lsn_fileno) firstlog,
base_time - decode(first_update_time, 0, base_time, first_update_time) time
from
v$transaction tx
left outer join v$lock_wait lw
on tx.id = lw.trans_id,
(select base_time from v$sessionmgr) base
where status != 6
order by time desc;
```

++ Check the client_pid and session_id holding the lock

```
select a.table_oid, a.lock_desc, c.client_pid , b.session_id
from v$lock a, v$statement b, v$session c
where a.trans_id = b.tx_id
and b.session_id = c.id;
```
