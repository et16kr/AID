---
title: "What is Offline Replicator?"
page_id: "1803108"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=1803108"
updated_at: "2011-07-30T17:01:55.000+0900"
version: 22
ancestors: ["Home", "ALTIBASE HDB Replication"]
labels: []
---

# What is Offline Replicator?
Source: https://docs.altibase.com/pages/viewpage.action?pageId=1803108
Updated: 2011-07-30T17:01:55.000+0900

- [Offline Replicator](#WhatisOfflineReplicator?-OfflineReplicator)
    - [Background](#WhatisOfflineReplicator?-Background)
    - [How to use Offline Replicator?](#WhatisOfflineReplicator?-HowtouseOfflineReplicator?)

# Offline Replicator

 ![unknown-macro](https://docs.altibase.com/plugins/servlet/confluence/placeholder/unknown-macro?name=gliffy&locale=en_GB&version=2)

## Background

In the above diagram, some XLogs of SYSTEM A may not be sent to the remote server (SYSTEM B) when the SYSTEM A has a failure. In this case, the system has to fail over to SYSTEM B, but SYSTEM B needs those unsent XLogs to start the service, otherwise, data in between those systems will be inconsistent. This can be achieved if SYSTEM B is able to access the log files of SYSTEM A and apply them locally.

## How to use Offline Replicator?

Follow the steps below if you need to use Offline Replicator feature.

| steps | Description |
| --- | --- |
| 1 | Mount a volume with the access enabled for SYSTEM-B |
| 2 | Create Offline Replicator on SYSTEM-B<br> <br>```<br>iSQL> CREATE REPLICATION rep1 OPTIONS OFFLINE '/data1/logfiles'<br>WITH '192.168.1.13', 30300 FROM SYS.table TO SYS.table;<br>``` |
| 3 | Execute SQL to start offline replication<br> <br>```<br>iSQL> ALTER REPLICATION rep1 START WITH OFFLINE;<br>``` |

Status of Offline Replicator becomes "stop" once it completes its work. You can start the fail over procedure after checking this status.

To learn more, [refer to this manual](http://atc.altibase.com/sub09/551b/html/Replication/ch03s06.html#CJAEFAJC)
