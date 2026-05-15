---
title: "Altibase Replication Configuration Guide"
page_id: "14647672"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/Altibase+Replication+Configuration+Guide"
updated_at: "2021-02-22T13:32:55.000+0900"
version: 24
ancestors: ["Home"]
labels: []
---

# Altibase Replication Configuration Guide
Source: https://docs.altibase.com/display/arch/Altibase+Replication+Configuration+Guide
Updated: 2021-02-22T13:32:55.000+0900

- [Overview](#AltibaseReplicationConfigurationGuide-Overview) - [High Availability](#AltibaseReplicationConfigurationGuide-HighAvailability) - [Node](#AltibaseReplicationConfigurationGuide-Node) - [Fail-over](#AltibaseReplicationConfigurationGuide-Fail-over) - [Plan for High Availability](#AltibaseReplicationConfigurationGuide-PlanforHighAvailability) - [Concept of Replication](#AltibaseReplicationConfigurationGuide-ConceptofReplication) - [The basic concept of replication](#AltibaseReplicationConfigurationGuide-Thebasicconceptofreplication) - [Sender](#AltibaseReplicationConfigurationGuide-Sender) - [Receiver](#AltibaseReplicationConfigurationGuide-Receiver) - [Problems that can occur in a replication environment](#AltibaseReplicationConfigurationGuide-Problemsthatcanoccurinareplicationenvironment) - [Efficient Replication Configuration](#AltibaseReplicationConfigurationGuide-EfficientReplicationConfiguration) - [Off-Line Replicator](#AltibaseReplicationConfigurationGuide-Off-LineReplicator) - [Service Configuration using the HA Solution](#AltibaseReplicationConfigurationGuide-ServiceConfigurationusingtheHASolution) - [Data Delay Considerations](#AltibaseReplicationConfigurationGuide-DataDelayConsiderations) - [Service configuration to prevent data conflict](#AltibaseReplicationConfigurationGuide-Serviceconfigurationtopreventdataconflict) - [Replication configuration considering data consistency](#AltibaseReplicationConfigurationGuide-Replicationconfigurationconsideringdataconsistency) - [Design of N-Way Replication](#AltibaseReplicationConfigurationGuide-DesignofN-WayReplication) - [Importance of Replication Design](#AltibaseReplicationConfigurationGuide-ImportanceofReplicationDesign) - [Additional Considerations for Replication Configuration](#AltibaseReplicationConfigurationGuide-AdditionalConsiderationsforReplicationConfiguration) - [Considerations for Disk Capacity](#AltibaseReplicationConfigurationGuide-ConsiderationsforDiskCapacity) - [Caution for Bulk Change](#AltibaseReplicationConfigurationGuide-CautionforBulkChange) - [Sender Status Monitoring](#AltibaseReplicationConfigurationGuide-SenderStatusMonitoring) - [Replication Dedicated Line](#AltibaseReplicationConfigurationGuide-ReplicationDedicatedLine) - [Parallel Applier Option](#AltibaseReplicationConfigurationGuide-ParallelApplierOption) - [Sequence Replication](#AltibaseReplicationConfigurationGuide-SequenceReplication) - [Constraints to Consider for Replication Configuration](#AltibaseReplicationConfigurationGuide-ConstraintstoConsiderforReplicationConfiguration) - [Summary](#AltibaseReplicationConfigurationGuide-Summary)

# Overview

---

In a system operating environment that provides non-stop service, the following should be considered.

- Ensure availability in case of failure
- Configuration and extension of the system considering performance

As a method to implement these, a disk sharing method, a replication method using a network, and a switching method using an HA solution are widely used in the field.

The high-availability (HA) architecture of Altibase considers performance and proposes a network-based data replication configuration.

This document describes the replication provided by Altibase and efficient system configuration based on it. Among the high-availability methods listed above, Altibase does not support the disk-sharing method.

This document was prepared based on Altibase version 7.1.0 or later.

For errors and improvements related to this document, please contact the technical support portal or technical support center.

- Technical support portal: [http://support.altibase.com](http://support.altibase.com/) > Technical Knowledge > Q&A
- Technical support center: 02-2082-1114

# High Availability

---

This section describes the goals and purposes of high availability and explains the pros and cons of the current industry-wide approach of high availability.

## Node

---

This refers to each server connected to one or more networks configured to perform the service operated by the user. Each node can serve independently and all nodes can process the same service.

## Fail-over

---

This refers to the process of transferring service to another normal node when a failure occurs between nodes configured for service. Fail-over allows only minimal service downtime.

## Plan for High Availability

---

For high availability, the user must configure a service system by grouping two or more nodes for the same or different services. The system must meet the following goals:

1. Compared to the environment composed of a single node, there should be no significant performance degradation.
2. Only minimal service downtime is allowed in a fail-over situation due to failure.

High availability requires ensuring that the service system operated by the user exhibits the maximum performance, and in any type of failure, it can be seen that it requires a method that allows the service to immediately resume with minimal downtime. (Goals: high performance and continuous service)

| Method | Description |
| --- | --- |
| Disk sharing method | A method of sharing a single DB on a disk accessible to all nodes (sharing DB) |
| Network replication method | All nodes own their respective DBs, and the method of transmitting and reflecting changes through the network (each node owns a separate DB) |

First, let's take a closer look at the disk sharing method.

![disk-share_eng.png](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20Replication%20Configuration%20Guide/disk-share_eng.png?api=v2)

In the disk sharing method, each node has its own buffer cache, and a master node that controls buffer-cache synchronization must exist within the group. When a node needs to read data that is not in its own buffer cache from the shared disk, it requests the read from the master node. If another node in the group already has the data in its buffer cache, the master node copies and sends the data from that node; otherwise, it allows the requesting node to read the data from disk. For changes, access is also possible only when the master node allows the change.

This form may be the best method for data integrity, but has the following problems.

1. All nodes cause significant performance degradation due to contention caused by communication with the master node and waiting for access to the buffer.
2. Communication equipment for high-speed replication of buffers is required between all nodes. If there is a failure in such communication equipment and line, it may cause an overall failure.
3. Even when a failure occurs in the shared disk device, the entire system cannot be serviced.

On the other hand, the network replication method is based on the operation mode of a single system and the transmission of additional transaction logs. Therefore in terms of performance, it is possible to maintain a performance level of 90% or more compared to a single system because it is not necessary except for the cost of log transmission with the network.

In addition, even if a specific node in a group fails, it is possible to maintain continuous service because each has a separate DB.

However, when transaction logs are transmitted over a network, the time at which a transaction occurs on the local system can differ from the time at which it is applied on the peer node. Therefore, this method cannot guarantee 100% data consistency across two or more nodes. This problem is described in detail later.

Both of the above methods have their own pros and cons. Therefore, the user needs to configure the optimal system with an accurate understanding of each method.

Altibase is a performance-oriented product that focuses on high availability while providing maximum performance in service operation. The next section describes the concept of replication and how network replication can be used for high availability despite data consistency concerns.

# Concept of Replication

---

This section describes the concept and operation structure of replication.

## The basic concept of replication

---

The structure of Altibase replication is as follows.

![rep_confi_eng.png](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20Replication%20Configuration%20Guide/rep_confi_eng.png?api=v2)

Several threads required for transaction processing in Altibase use the storage-manager module. The log thread that uses the SM module records the transaction log required for recovery during transaction processing.

The basic flow is that when a transaction log is recorded locally by the SM, the Sender reads the recorded transaction log and sends it to the designated node or nodes. The Receiver on each receiving node analyzes the received log and applies it to its own node.

- Asynchronous replication using a transaction log-based network.
- A replication configuration can include n tables, and every table included in the replication configuration must have a PK.
- Multiple networks can be configured for replication stability.

Let's take a look at the operation of the Sender and Receiver.

## Sender

---

When a change transaction such as Insert/Update/Delete other than the select statement occurs, information necessary for processing and restoring is recorded. Based on this transaction log, the sender finds out what type of transaction occurred and the value before and after the data change.

The sender creates a transmission data called xLog based on the read log. It can be seen as a structure containing the following information.

| Item | Description |
| --- | --- |
| Table | The target table must be found in the receiving node. |
| PK | The target data must be found in the receiving node. |
| Column | The target column must be found in the receiving node. |
| Before Value | To compare whether data is the same between the receiving node and the transmitting node. |
| After Value | This value is used when the data value can be changed in the receiving node. |

The sender collects only necessary data for each transaction, creates xLog, and sends it to the Receiver of the other node.

| Transaction | Sender log |
| --- | --- |
| INSERT | Table, Column Value |
| UPDATE | Table, PK, Before Value, After Value |
| DELETE | Table, PK |

Since the transaction that occurs locally is processed regardless of whether it is transmitted in replication (only the sender is checked), there is no interference due to replication, ensuring the processing performance. (This is called lazy mode replication.)

This raises the question of whether the peer node can miss data. The Receiver behavior below explains how Altibase handles that case.

The Sender uses Lazy mode by default. It can also be configured to wait until the transaction is applied on the peer node; this is called Eager mode.

## Receiver

---

The Receiver sends the received xLog to Receiver-Applier (hereinafter referred to as Applier). Because the received xLog was generated from a transaction log that had already passed through QueryProcessor on the peer node, the Applier requests processing from SM without a separate validation process. (QueryProcessor refers to an internal module that performs validation and optimization for queries executed in Altibase.)

When the receiving node applies the data, it must first check that the received Before Value matches the value currently stored in its own node.

After applying the data, the Receiver sends an acknowledgment to the peer Sender. The Sender then updates the position from which it must retransmit logs. Because the replication communication buffer can contain multiple transaction xLogs, the Sender always records both the position of the log it is sending and the transaction-log position to retransmit from in case transmission fails or the peer node fails. This information is updated when the Receiver acknowledges which portion has been applied.

Therefore, even if the Sender does not immediately confirm every apply operation on the receiving node, it eventually confirms progress through acknowledgments, so the logs that the Sender must send are not lost. The same behavior applies when a network failure occurs.

In other words, when the Sender detects a network failure, it checks the network at a fixed interval. When normal communication is restored, it connects to the Receiver on the peer node and resumes sending from the retransmission position it has recorded.

## Problems that can occur in a replication environment

---

Since replication uses a network, the following problems can occur:

1. Data conflict
2. Data transmission gap

In the case of a transaction in which two nodes change data with the same PK to different values, the disk sharing method has no choice but to proceed with the change transaction one by one by the node requesting each processing. Therefore, if such transactions are frequent, the performance is bound to be slow.

On the other hand, unlike the disk sharing method, replication does not consider changes to data on other nodes when a local transaction occurs. Because the nodes do not interfere with each other, data conflicts can occur.

| Order of occurrence | Node A | Node B |
| --- | --- | --- |
| Before occurrence | Pk=1, c1=10 | Pk=1, c1=10 |
| Update at the same time | Update t1 set c1 = 15 where pk = 1 | Update t1 set c1 = 20 where pk = 1 |
| After occurrence | Pk=1, c1=15 | Pk=1, c1=20 |
| Sender | Send (t1, pk=1, c1=10 --> 15) | Send (t1, pk=1, c1=10 --> 20) |

As in the example above, the data is identical before the update, but each node updates the row with the same PK to a different value and proceeds without considering the transaction on the other node. When the already-changed data is then transmitted between nodes, each node compares the previous value in the received xLog with its current value. On node A, the current value is 15 but the before value in the received xLog is 10, so the transaction for the received xLog fails. This is called Update Conflict.

The types of Conflict are as follows.

| Type | Description |
| --- | --- |
| Dup Conflict | When data having the same PK already exists in the receiving node while performing Insert, etc. |
| Update Conflict | When the current value of the target column is not the same as the received before value while performing Update |
| Not Found Conflict | When data does not exist while performing Update or Delete on PK in the receiving node |

That is, when two or more nodes change data differently for the same PK, there may be cases in which data exists in an incorrect state at the same time.

To avoid this problem, trigger transactions against separate PK ranges for each node. In other words, configure Active/Active by considering PK ranges instead of using the Full Active method.

Altibase provides the `REPLICATION_UPDATE_REPLACE` property so that the receiving node can apply the received value even when the previous value differs for an UPDATE transaction. However, this is not a complete solution to Update Conflict. If all service nodes continuously update data with the same PK to different values, the nodes will eventually diverge again. This property is only based on the assumption that the data will eventually converge.

Another replication problem occurs when the sending node accumulates change transaction logs faster than it can transmit xLogs to the peer node. At a specific point in time, query results on the sending node and receiving node can differ. In other words, transaction logs that could not be transmitted to the peer node through the network are accumulated on the sending node; this is called a replication gap.

These problems can make users hesitate to choose replication in terms of data consistency, even if high-performance data processing is possible. In the next section, we will take a look into how to properly avoid such data conflicts and delays to enable service with efficient replication configuration.

# Efficient Replication Configuration

---

This section will describe the configuration method using the Off-line Replicator function and HA solution, which are complementary functions of replication provided by Altibase.

## Off-Line Replicator

---

The major issue with replication transmission delay is how to guarantee consistency for data that could not be sent when the sending node failed. If the system separates PK ranges and can control the delay, the delayed data will still be applied after some time. However, a failure that occurs while data is delayed can be critical for the business.

Altibase provides a function called Off-Line Replicator starting from Altibase v5.3 to solve this problem. When the server that was actively providing service fails, the operator creates an Off-Line Replicator on the healthy server. The Off-Line Replicator reads the failed node's transaction log files directly and applies data that was not transmitted, resolving the data consistency issue. The operator can create it easily with an SQL statement.

To use the Off-Line Replicator, either configure shared disk equipment so that every node can write its own transaction logs to the disk shared with the failed server, or connect to the failed server by FTP and bring the transaction logs over for apply.

With this method, the consistency due to the non-transmission of data is eliminated and the service can be started in the normal node.

![offline_eng.png](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20Replication%20Configuration%20Guide/offline_eng.png?api=v2)

The exact configuration can differ by system environment. The basic approach is that, when a failure occurs, the healthy node directly reads the transaction logs that the failed node could not transmit and applies them locally to prepare for service switchover.

## Service Configuration using the HA Solution

---

Configuration using an HA solution means that one node performs the service while another node remains in standby. The HA solution periodically checks the node that is providing service. If it determines that a problem has occurred, it switches the shared disk so that the standby node can access it and take over the service.

When applied to Altibase, there are the following limitations, but it has the advantage of avoiding the data inconsistency problem.

1. Altibase on the standby node cannot be running. It must be shut down. The Altibase engines on both nodes cannot run at the same time.
2. After switchover, Altibase must go through the startup phase. If memory DB usage is large, startup time increases in proportion to the data size. If a large workload was running at the time of failure, the startup phase also requires recovery time for that workload. Consider this when service downtime is critical.

![disk_share2.png](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20Replication%20Configuration%20Guide/disk_share2.png?api=v2)

Active/Standby is classified from the service perspective, and Altibase on the standby node is in the shutdown state.

Generally, it is composed as follows.

| Category | Configuration items |
| --- | --- |
| Shared disk | Transaction log file and data file |
| Each node | Altibase engine, trace log file, license, property file |

If configured as above, when a situation in which the HA solution is switched over occurs, the standby node that can access the shared disk runs by using the transaction log and data file located on the shared disk, and the service can become available.

Since this HA solution configuration does not use network-based replication, data conflict and replication gap issues do not need to be considered during switchover.

## Data Delay Considerations

---

If a service that uses Altibase replication continuously processes changes, data delay cannot be avoided in a network-based replication configuration. However, the configuration can still be usable if the volume of changed data in each transaction is within the level that replication can handle and the service can tolerate temporary data delay.

Even when data was not sent at the time of failure, the service can be configured to avoid service-level impact by recovering with the Off-Line Replicator before switching service.

Such a configuration is based on prediction, and it is a case of considering transmission delay to some extent. If a service cannot consider transmission delay, a method of configuring the replication mode to Eager mode can be used.

| Replication operation method | Description |
| --- | --- |
| Lazy | The sending node does not wait for the progress of the local transaction and the transmission of xLog. |
| Eager | The sending node first applies the local transaction, sends the xLog to the receiving node, and waits for the apply result from the receiving node. |

The data transmission delay problem of replication described so far can occur in the lazy mode, and in order to avoid this problem, the Eager mode is provided. Since the Eager mode checks the reflection of the other node, there is no data delay. However, since it has to wait for the transaction of the other node to be reflected, the Eager mode causes a significant performance degradation compared to the Lazy mode. However, even in this part, the degree of performance degradation may not be significant depending on the proportion of the change operation among the entire transaction.

Therefore, users can choose Lazy or Eager mode according to the workload. If the workload does not need to account for data delay, use Lazy mode for better performance. If the workload must account for data delay, use Eager mode. Because Lazy/Eager mode can be specified per session, it can be applied separately by session.

| Operation | Replication operation method |
| --- | --- |
| Account balance, deposit | The session to perform this task is in Eager mode |
| Login time information | The session to perform this task is in Lazy mode |

Unlike the Lazy mode, the local transaction also fails when conflict occurs in the Eager mode. Therefore, it should be well planned so that the data does not change due to transactions in the Lazy mode.

## Service configuration to prevent data conflict

---

Data conflict occurs when trying to access data with the same PK at the same time in a replication environment. Therefore, it is recommended to configure the service so that the service program of the user does not access the same PK.

| Configuration | Service configuration example 1 | Service configuration example 2 |
| --- | --- | --- |
| Node A | Change transaction + retrieval transaction | Transactions of Seoul and Gyeonggi areas |
| Node B | Retrieval transaction | Transaction of Chungcheong, Jeolla, and Gyeongsang areas |

In the same configuration as for example 2 of the service configuration, there are many things to consider at the stage of user development, such as the distribution of transactions. This requires more consideration of how to classify the range and how to implement it.

Altibase provides the following functions for data conflict. It is important to choose the function that fits each service configuration.

| Method | Description |
| --- | --- |
| `REPLICATION_UPDATE_REPLACE=1` | Performs the UPDATE even when the Before Value in the received xLog does not match the target data value on the receiving node. |
| Master / Slave method | Designates each node as Master or Slave and handles conflicts according to the transaction rules below. |
| TimeStamp method | When a conflict occurs in a table configured for replication, compares each timestamp and aligns the data to the later value. |

The Master / Slave method behaves as follows when conflict occurs.

| Transaction | Master | Slave |
| --- | --- | --- |
| Insert | Ignored | Reflect after deleting existing data |
| Update | Ignored | Reflect as it is |
| Delete | Ignored | Ignored |

More detailed explanations can be found in the manual.

## Replication configuration considering data consistency

---

As discussed above, replication requires the configuration of a service system in consideration of the problem of data delay and conflict. If the following configuration is made using the function provided by Altibase, the data inconsistency and delay can be completely solved.

1. Configure Active/Standby type
2. Failure recovery with the Off-Line Replicator

All services are handled on one side. When a failure occurs, the Off-Line Replicator applies data that has not yet been reflected, then service is switched and started on the other node.

| Situation | Node A | Node B |
| --- | --- | --- |
| Normal Service | Process all services | Receive only replication logs, standby status |
| Failure occurs | Perform failure recovery | After reflecting all transaction logs of Node A that Node B has not received with the Off-Line Replicator, service is performed at Node B |
| Node A recovery | Match data by receiving all replication logs from Node B after failure | Automatically detect recovery of Node A and transmit all transaction logs after failure through replication |

When using an HA solution in the above configuration, it is possible to automate all service switchover processes without user intervention when a failure occurs. Because the Off-Line Replicator operates as an SQL statement as described above, it can be registered as a script in the HA solution and included in the switchover procedure for straightforward automation.

## Design of N-Way Replication

---

Altibase replication supports N-way replication, and one node can connect to up to 32 peer nodes. When three or more nodes are configured for replication, replication objects must be created as shown below, and network-card expansion should be considered in advance.

![nway_eng.png](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20Replication%20Configuration%20Guide/nway_eng.png?api=v2)

A Sender and Receiver for each target connection must exist on every node. For this, each node must have a replication object for every target node to which it sends data. In the figure above, node A must have replication objects for A-B and A-C. Node B can synchronize data normally among A-B-C only when replication objects for B-A and B-C are also created.

## Importance of Replication Design

---

The important thing can be said to be the design part of whether to use each function in a good combination suitable for the operation purpose. At the design stage, the following two options should be fully considered.

1. Which method to choose between a lazy and eager mode for the replication? Or, if both are used together, what kind of operation will be serviced in different ways?
2. What is the right solution for data conflict and delay?

# Additional Considerations for Replication Configuration

---

This section describes considerations for replication configuration.

## Considerations for Disk Capacity

---

If a problem occurs in the replication connection in any form, the Sender cannot send transaction logs occurring locally to the other node. In this case, even if a checkpoint occurs, the transaction log files cannot be deleted to maintain the log files to be replicated.

Therefore, a primary transmission-delay failure can cause a secondary failure from insufficient disk space as transaction log files accumulate. To avoid this problem, the `REPLICATION_MAX_LOGFILE` property can be used so that, when transaction log files are generated beyond the specified value, all replication transmission history is abandoned and the corresponding transaction log files can be deleted at checkpoint.

However, this is not recommended except in special situations because the user must perform additional work after failure recovery to make the databases consistent between nodes. Instead, estimate disk capacity in advance based on the daily transaction-log volume so that accumulation for the expected failure-recovery window does not become a problem.

## Caution for Bulk Change

---

What is sent in replication is based on the transaction log, not based on SQL. Therefore, when the bulk change is performed, the transaction log must be transmitted to the other node as much as the number of changed data. For this reason, in the case of a busy system that handles very frequent services, the reflection is delayed. Therefore, the following two methods are recommended to perform the bulk change.

1. Divide the work into small batches by using a `LIMIT` clause.
2. Run the same change on all nodes after using the `ALTER SESSION SET REPLICATION = FALSE;` option. This option means that the transaction logs from that session are not sent through replication.

## Sender Status Monitoring

---

If a Sender remains stopped after it has been started at least once, Altibase continues to retain the logs that the Sender must send. If this is not monitored separately, transaction logs can continue to increase and cause a disk-full failure.

## Replication Dedicated Line

---

It is recommended to use a dedicated line separately from the service network for replication. In particular, it is recommended to use a network with a bandwidth of 1G or higher. In addition, it is also recommended to secure stability by having two or more dedicated LAN cards for replication in case of network failure.

## Parallel Applier Option

---

Parallel Applier is an option that improves replication performance by creating multiple appliers that are reflected in the storage manager.

Replication performance is improved by distributing the xLog received from the Sender to appliers by transaction unit and executing DML in parallel. Therefore, this option is suitable for replication workloads that contain long transactions. If there are many replicated transactions composed of short transactions, performance can decrease because commit synchronization occurs frequently. If there are many replicated transactions composed of long transactions, performance can improve because commit synchronization is less frequent.

## Sequence Replication

---

Sequence replication is a function that allows a remote server and local server to use the same sequence even when Fail-over occurs. Thus, the same sequence and the same program source can be used in the application.

Sequence replication requires replicating the cache start value so that sequence values do not overlap between two servers. A cache-size range of sequence values is stored in memory and used; when all stored values are consumed, another cache-size range is stored in memory.

Altibase replication supports only tables, so Altibase internally creates a table for sequence replication.

## Constraints to Consider for Replication Configuration

---

- Tables configured for replication must have a PK.
- Tables configured for replication cannot update the PK. (From the DBMS perspective, implementing a workload that updates the PK is itself an incorrect approach.)
- Tables in a node configured for replication must have the same column information, PK, and NOT NULL information.
- Since data inconsistency may occur due to replication delay, it is recommended to avoid using triggers and foreign keys in principle. However, they can be allowed depending on the configuration environment or business purpose.
- When executing a DDL operation on a table configured for replication, the table must be temporarily removed from the replication target list before execution. (Some DDLs, such as add column, can be executed without removing the table from the replication list during operation. Refer to the manual for details.)
- Since memory DB and disk DB apply speeds differ, it is recommended to separate replication objects for memory and disk when the apply order between memory and disk is not important for the workload.
- Fail-over refers to transferring service to another healthy node when a failure occurs between nodes configured for service. Fail-over allows only minimal service downtime.

# Summary

---

We have described the overview, problems, and solutions of Altibase replication.

Replication using a network clearly has a data consistency problem due to transmission delay in case of data conflict or failure. However, it is possible to avoid the problem of data conflict by classifying the range of the change transaction by node properly with operation analysis as in real cases. The problem of data consistency occurring when a failure occurs can be solved with the Off-Line Replicator.

Therefore, the following three processes should be sufficiently considered:

1. It is necessary to first identify the operation requirements to prevent data conflict.

| Requirement | When configuring Active/Active | When configuring Active/Standby |
| --- | --- | --- |
| Task implementation requirements | Separate configuration for each task<br>Separate configuration of the change scope | Only one node performs change transactions<br>Retrieval transactions are executed on one or all nodes |
| Purpose | Configure replication so that data conflicts do not occur in the first place by preventing access to the same PK. |  |

Active/Standby classification is based on service. This means that all Altibase engines are running.

2. Consider data that could not be transmitted at the time of failure. As described above, resolve this by using the Off-Line Replicator provided in Altibase version 5.3 or later, or design another business-appropriate method into the system configuration.
3. As described in "Constraints to Consider for Replication Configuration", there are precautions and constraints that must be considered for replication configuration. If they are not fully understood during design, the replication configuration itself may not be possible.
