---
title: "What is a Replication Conflict?"
page_id: "1802533"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=1802533"
updated_at: "2011-08-06T10:46:14.000+0900"
version: 50
ancestors: ["Home", "ALTIBASE HDB Replication"]
labels: []
---

# What is a Replication Conflict?
Source: https://docs.altibase.com/pages/viewpage.action?pageId=1802533
Updated: 2011-08-06T10:46:14.000+0900

- [What is a replication conflict?](#WhatisaReplicationConflict?-Whatisareplicationconflict?)
    - [Simple case](#WhatisaReplicationConflict?-Simplecase)
    - [Types of Conflict](#WhatisaReplicationConflict?-TypesofConflict)
- [Summary](#WhatisaReplicationConflict?-Summary)

# What is a replication conflict?

## Simple case

 ![unknown-macro](https://docs.altibase.com/plugins/servlet/confluence/placeholder/unknown-macro?name=gliffy&locale=en_GB&version=2)

In a nutshell, let's assume that the Sender in node B processes transactions faster than the Sender in node A. After steps (#1, #2) are completed as illustrated in the diagram above, the Receiver in node A cannot update the records since the before-value("10") in XLog is different from the current value("20") We call this situation as a Replication Conflict.

## Types of Conflict

| Types | Description |
| --- | --- |
| Insert-conflict | The record in XLog already had been inserted |
| Update-conflict | Before value of the record in XLog is different from the current value of the target column |
| Delete-conflict | Record in XLog already had been deleted |

Conflict error message is written on $ALTIBASE_HOME/trc/altibase_rp.log. for example,

| Types | message |
| --- | --- |
| Insert-conflict | ERR-11058(errno=0) The row already exists in a unique index. |
| Update-conflict | ERR-61001(errno=0) A conflict has been occurred while executing the received statement. |
| Delete-conflict | ERR-61000(errno=0) The received record is not found in the database. |

altibase_rp.log also contains information about the SQL statement which causes the conflict in the remote server.

```
[Thread-280|Thread-280] [Level-2|Level-2]
ERR-61035(errno=0) [Receiver] An update conflict encountered.

[Thread-280|Thread-280] [Level-2|Level-2]
ERR-61001(errno=0) A conflict has been occurred while executing the received statement.

[Thread-280|Thread-280] [Level-3|Level-3]
UPDATE SYS.REP_TEST2 SET C2 = ccc WHERE C1 = 1;
```

# Summary

It is important to analyze and address “replication conflicts” when using asynchronous replication. Asynchronous replication implements “eventual consistency”; an approach that has many benefits, yet requires additional care.

When using asynchronous replication, it is important to design the service to minimize conflicts. The way to avoid conflicts is to ensure that the same records are not updated on different systems concurrently. Designating one server as the “read-only” copy, partitioning the data based on primary key, or other approaches can be used to avoid replication conflicts.

If you want to know more in detail, please [refer to this document](http://aid.altibase.com/x/QoEb)
