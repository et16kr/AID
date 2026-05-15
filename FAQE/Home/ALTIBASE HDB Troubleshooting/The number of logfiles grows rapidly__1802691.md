---
title: "The number of logfiles grows rapidly"
page_id: "1802691"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/The+number+of+logfiles+grows+rapidly"
updated_at: "2012-05-11T09:23:59.000+0900"
version: 21
ancestors: ["Home", "ALTIBASE HDB Troubleshooting"]
labels: ["long_running_transaction", "replication", "checkpoint", "logfile", "pbt", "disk_full"]
---

# The number of logfiles grows rapidly
Source: https://docs.altibase.com/display/FAQE/The+number+of+logfiles+grows+rapidly
Updated: 2012-05-11T09:23:59.000+0900

- [About the contents](#Thenumberoflogfilesgrowsrapidly-Aboutthecontents)
- [Symptoms](#Thenumberoflogfilesgrowsrapidly-Symptoms)
- [Caused by](#Thenumberoflogfilesgrowsrapidly-Causedby)
    - [Long running transactions exist (Transactions that are not committed or rolled back)](#Thenumberoflogfilesgrowsrapidly-Longrunningtransactionsexist(Transactionsthatarenotcommittedorrolledback))
          - [Description](#Thenumberoflogfilesgrowsrapidly-Description)
          - [How to find uncommitted transactions?](#Thenumberoflogfilesgrowsrapidly-Howtofinduncommittedtransactions?)
          - [Available Actions](#Thenumberoflogfilesgrowsrapidly-AvailableActions)
    - [Replication sender does not work properly](#Thenumberoflogfilesgrowsrapidly-Replicationsenderdoesnotworkproperly)
          - [Description](#Thenumberoflogfilesgrowsrapidly-Description.1)
          - [How to find out that there are Replication problems?](#Thenumberoflogfilesgrowsrapidly-HowtofindoutthatthereareReplicationproblems?)
          - [Available Actions](#Thenumberoflogfilesgrowsrapidly-AvailableActions.1)
    - [Checkpoint thread does not work properly](#Thenumberoflogfilesgrowsrapidly-Checkpointthreaddoesnotworkproperly)
          - [Description](#Thenumberoflogfilesgrowsrapidly-Description.2)
          - [How to figure out that Checkpoint thread does not work properly?](#Thenumberoflogfilesgrowsrapidly-HowtofigureoutthatCheckpointthreaddoesnotworkproperly?)
    - [Archiving thread does not work properly](#Thenumberoflogfilesgrowsrapidly-Archivingthreaddoesnotworkproperly)
          - [Description](#Thenumberoflogfilesgrowsrapidly-Description.3)
          - [How to find out that Archiving thread does not work properly?](#Thenumberoflogfilesgrowsrapidly-HowtofindoutthatArchivingthreaddoesnotworkproperly?)
- [Conclusion](#Thenumberoflogfilesgrowsrapidly-Conclusion)
- [Reference](#Thenumberoflogfilesgrowsrapidly-Reference)

# About the contents

|  |  |
| --- | --- |
| Purpose | The contents here explains why in some cases, ALTIBASE HDB does not remove the transaction log files. |
| Applies to | HDB versions 4.3.9 or later |
| Prerequisite | Administrator's Manual |

# Symptoms

- The number of log files in LOG_DIR grows rapidly. (The log file location is specified in altibase.properties)

# Caused by

In ALTIBASE HDB, Checkpoint thread removes the unnecessary transaction log files(logfiles). However, Checkpoint thread does not remove the transaction log files under the following conditions.

1. Long-run transaction exists.(Transaction is not committed or rolled backed.)
2. Replication sender does not work properly.
3. Checkpoint thread does not work properly.
4. Archiving thread does not work properly.

## Long running transactions exist (Transactions that are not committed or rolled back)

### Description

When a transaction is rolled back, ALTIBASE HDB has to read information from transaction log files in order to undo the transaction. Therefore, if there is such an unfinished transaction, ALTIBASE HDB has to keep the log files associated with that transaction.

 ![unknown-macro](https://docs.altibase.com/plugins/servlet/confluence/placeholder/unknown-macro?name=gliffy&locale=en_GB&version=2)

For example in the above diagram, Transaction D is not finished, and it may roll back. Therefore, ALTIBASE HDB has to keep the log files after log#6 until transaction D is finished (commit or rollback). Although transactions E and F are started and ended after log#6, ALTIBASE HDB has to save log files for transaction D. In other words, even though the transaction does not finish for a long time and many update transactions are executed during that period. In this case Checkpoint thread does not remove the log files after log#6, therefore, the disk space will be exhausted.

You can prevent this problem by editing the timeout properties of ALTIBASE HDB. ALTIBASE HDB automatically rollbacks the transaction if it exceeds the time specified in timeout properties. Please, refer to IDLE_TIMEOUT / QUERY_TIMEOUT / FETCH_TIMEOUT / UTRANS_TIMEOUT in the Starting User's Manual.

### How to find uncommitted transactions?

1. You can find the long running uncommitted transactions in ALTIBASE HDB using by [this query.](http://aid.altibase.com/display/arch/SQL+about+Statements#SQLaboutStatements-Longrunningquery%28over10seconds%29)
2. Check the UTRANS_TIME from the result of the query.

### Available Actions

1. Terminate the session that has the long running transaction. (See also, [How to terminate a session](https://docs.altibase.com/display/FAQE/How+to+terminate+a+session) )
2. You may consider setting the value of UTRANS_TIMEOUT to the smaller value.

## Replication sender does not work properly

### Description

If you are using the ALTIBASE HDB's Replication functionality, malfunctioning of Replication sender thread may prevent Checkpoint thread to remove the log files.

Replication sender thread uses the log files to synchronize data between replicated servers. Therefore, Checkpoint thread cannot remove the log files unless Replication sender finishes its work on them.

 ![unknown-macro](https://docs.altibase.com/plugins/servlet/confluence/placeholder/unknown-macro?name=gliffy&locale=en_GB&version=2)

In the above diagram, let's assume that Replication sender is reading logfile#3, and service threads are writing on logfile#6. In this case, the Replication sender needs not only logfile#3 but also logfile#4, logfile#5 and logfile#6 to synchronize with the receiving server. Thus, Checkpoint thread cannot remove logfile#3 and newer, but only logfile#1 and logfile#2. Checkpoint thread will remove the log files after logfile#3 once Replication sender thread applies the log files to the receiving server. (For further information of how Replication works, please refer to [this page](https://docs.altibase.com/display/FAQE/ALTIBASE+HDB+Replication).)

Furthermore, Checkpoint thread cannot remove the log files if Replication sender does not work due to network failures or DBA human errors - such as shutdown of Replication by mistake.

### How to find out that there are Replication problems?

1. You have to check whether Replication sender is running or not by using [this query](http://aid.altibase.com/display/arch/SQL+about+Replications#SQLaboutReplications-ReplicationSender).
2. Check the Replication gap in Replication object by using [this query.](http://aid.altibase.com/display/arch/SQL+about+Replications#SQLaboutReplications-Replicationgap)

### Available Actions

1. Start the Replication sender if it is stopped.
2. Fix the Replication problem.

## Checkpoint thread does not work properly

### Description

As we mentioned earlier, Checkpoint thread removes the log files, thus if Checkpoint thread does not work properly, the log files can not be removed.

- Check whether CHECK_POINT_ENABLE is set to 0
   Setting the value of CHECK_POINT_ENABLE to 0 means that ALTIBASE HDB does not perform Checkpoint automatically. In this case, you have to perform the Checkpoint manually. Sometimes disabling Checkpoint is helpful. For example, if there are I/O issues on the system, disabling Checkpoint reduces I/O activity. However, you have to monitor the disk space of LOG_DIR since Checkpoint thread does not empty the space automatically.

  You have to consider all the details before setting the value of CHECK_POINT_ENABLE to 0.

- The duration of Checkpoint operation
   Checkpoint thread figures out which log files are removable at first, and removes those files at the end of every Checkpoint operation. Thus, if the Checkpoint operation takes too much time, the log files created after the Checkpoint procedure started can not be removed before the checkpoint operation finishes. You can refer to altibase_sm.log file (location of the file is specified in altibase.properties) to analyze what slows down the procedure.

### How to figure out that Checkpoint thread does not work properly?

1. Make sure that CHECK_POINT_ENABLE property in altibase.properties is set to 1.
2. Check altibase_sm.log to analyze the status of Checkpoint thread.

## Archiving thread does not work properly

### Description

If Archiving thread does not work properly, archiving of the log files process will fail. (i.e. archive log partition is full). In this case, Checkpoint thread does not remove unarchived log files. Archiving thread must copy them to ARCH_DIR (the file location is specified in altibase.properties) before Checkpoint thread removes them.

### How to find out that Archiving thread does not work properly?

1. Check altibase_sm.log. Archiving thread related error message are added in the log when Archiving thread has a problem.

# Conclusion

In order to operate ALTIBASE HDB properly, it is very important to monitor the folders containing the log files (LOG_DIR ) . Once LOG_DIR is full, all transactions are suspended and you may have to shutdown ALTIBASE HDB to fix the problem. Furthermore, it may cause the service to go offline.

# Reference

- ALTIBASE Administrator's Manual
