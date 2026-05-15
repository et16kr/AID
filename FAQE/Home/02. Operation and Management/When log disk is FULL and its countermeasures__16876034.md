---
title: "When log disk is FULL and its countermeasures"
page_id: "16876034"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/When+log+disk+is+FULL+and+its+countermeasures"
updated_at: "2025-09-29T15:02:21.000+0900"
version: 3
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# When log disk is FULL and its countermeasures
Source: https://docs.altibase.com/display/FAQE/When+log+disk+is+FULL+and+its+countermeasures
Updated: 2025-09-29T15:02:21.000+0900

**- [Overview](#WhenlogdiskisFULLanditscountermeasures-Overview) - [Applicable versions](#WhenlogdiskisFULLanditscountermeasures-Applicableversions) - [Altibase operation status when the disk is full](#WhenlogdiskisFULLanditscountermeasures-Altibaseoperationstatuswhenthediskisfull) - [When the directory containing log files is full](#WhenlogdiskisFULLanditscountermeasures-Whenthedirectorycontaininglogfilesisfull) - [Countermeasures when the log disk is full](#WhenlogdiskisFULLanditscountermeasures-Countermeasureswhenthelogdiskisfull)**

# Overview

---

This document describes the situation and countermeasures that can occur only when a full disk occurs in the directory where the log file exists during the operation.

# Applicable versions

---

- This document is written based on ALTIBASE HDB 6.3.1.
- If you need additional inquiries or updates, please leave a request post at [http://support.altibase.com/en/](http://support.altibase.com/en/) or make a comment on this page.

# Altibase operation status when the disk is full

---

The filesystem full phenomenon during the Altibase operation may be a full file system with a DB file or a full file system with a log file.

If the file system with the DB file is full, it does not affect general transactions.

However, the checkpoint operation cannot be performed because there is not enough free disk space when performing checkpoint.

Therefore, all changes made to the DB are reflected only in the DB in memory.

When the file system with the LOG file is full, transactions that make changes to the DB are no longer executed and the Altibase process enters a waiting state. In other words, services except for 'select' are stopped.

In general, disk full occurs because the file system size is small, and it is recommended to operate Altibase after securing sufficient disk space.

# When the directory containing log files is full

---

The following are cases in which there are abnormally many log files because the log files are not deleted even though the disk space is secured and operated.

1. When using replication, replication data may not be reflected on the other server because of network instability or another reason. To confirm this, check the replication gap.

  ```
  SELECT * FROM V$REPGAP;
  ```
2. When the value of the ARCHIVE_FULL_ACTION property is set to 1 => This property controls the operation of the archive thread that performs archive log backup when there is not enough disk space in the file system to which the directory set in ARCHIVE_DIR belongs. If the value is 0, the archive thread outputs an error message and then stops backing up the archive log file. Even after sufficient disk space is secured thereafter, archive log backup is not resumed unless the user explicitly enters a command to enable archive log backup. In this case, when a checkpoint occurs, unnecessary log files are deleted even if the archive log files are not backed up, so be cautious during the operation. If the value is 1, the archive thread waits until enough disk space is available to back up the archive log file. During this period, even if a checkpoint occurs, log files are not deleted because archive log files cannot be backed up. The user can refer to the $ALTIBASE_HOME/conf/altibase.properties file or check the value of this property in isql.

  ```
  select name, value1 from v$property where name like '%ARCHIVE_FULL_ACTION%';
  ```
3. If the checkpoint has not been performed => Since log file deletion occurs only at the checkpoint, check whether or not the checkpoint has been successfully executed. Checkpoint execution can be checked by referring to the $ALTIBASE_HOME/trc/altibase_sm.log file. Logs are recorded when the checkpoint is normally executed as shown below.

  ```
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-9]
  [CHECKPOINT BY USER]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-9]
  [CHECKPOINT-BEGIN]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-9]
  [CHECKPOINT-step2] Write BeginChkpt Log [0,0,6232554]
  Active Tx Recovery LSN [0,0,6232554]
  Disk Buffer Oldest LSN [0,0,6232554]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-9]
  [CHECKPOINT-step3] Flush Dirty Page(s)
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-9]
  [PRE-DirtyPageCount=0]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-9]
  [NEW-DirtyPageCount=8]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-9]
  [DUP-DirtyPageCount=0]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-9]
      + Begin Sync For All-LFG - Request LSN [0,0,6232995]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-9]
      + End Sync For All-LFG
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-9]
  [FLU-DirtyPageCount=8]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-9]
  [REM-DirtyPageCount=0]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-9]
  [CHECKPOINT-step4] sync Database File
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-0]
  ==========================================================
  SM IO STAT  - Checkpoint
  DB SIZE      :       262144 Byte ( 8 Page)
  LOG SIZE     :          441 Byte
  TOTAL TIME   :      0 s 2416 us
  LOG SYNC TIME:      0 s 665 us
  DB FLUSH TIME:      0 s 1751us
        SYNC TIME :      0 s 860 us
        WAIT TIME :      0 s 0 us
        WRITE TIME:      0 s 891 us
  LOG IO PERF  : 136.16138155429 MB/sec
  DB IO PERF   : 142.775556824672 MB/sec
  =========================================================
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-9]
  [CHECKPOINT-step5] Write End_Chkpt Log [0,0,6233141]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-9]
  [CHECKPOINT-step6] Sync Log File
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-9]
      + Begin Sync For All-LFG - Request LSN [0,0,6233182]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-9]
      + End Sync For All-LFG
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-9]
  [CHECKPOINT-step7] Check LogFiles That Is Not Needed
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-9]
  Replication MinSN48192
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-9]
  [CHECKPOINT-step8] Update and Flush Log Anchor
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-9]
  [CHECKPOINT-step9] Remove Online Log File[None]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-6]
  [CHECK DATABASE SID=0, PPID=0, FID=0]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-6]
  LogAnchor SpaceID=0, SmVersion=100794369, LFGCount=1
  DBFileHdr SpaceID=0, SmVersion=100794369, LFGCount=1
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-6]
  RedoLSN=control[0,0,6232554], [0,0,6232554]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-6]
  CreateLSN=control[0,0,504], [0,0,504]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-6]
  [CHECK DATABASE SID=0, PPID=1, FID=0]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-6]
  LogAnchor SpaceID=0, SmVersion=100794369, LFGCount=1
  DBFileHdr SpaceID=0, SmVersion=100794369, LFGCount=1
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-6]
  RedoLSN=control[0,0,6232554], [0,0,6232554]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-6]
  CreateLSN=control[0,0,504], [0,0,504]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-6]
  [CHECK DATABASE SID=1, PPID=0, FID=0]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-6]
  LogAnchor SpaceID=1, SmVersion=100794369, LFGCount=1
  DBFileHdr SpaceID=1, SmVersion=100794369, LFGCount=1
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-6]
  RedoLSN=control[0,0,6232554], [0,0,6232554]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-6]
  CreateLSN=control[0,0,1426], [0,0,1426]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-6]
  [CHECK DATABASE SID=1, PPID=1, FID=0]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-6]
  LogAnchor SpaceID=1, SmVersion=100794369, LFGCount=1
  DBFileHdr SpaceID=1, SmVersion=100794369, LFGCount=1
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-6]
  RedoLSN=control[0,0,6232554], [0,0,6232554]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-6]
  CreateLSN=control[0,0,1426], [0,0,1426]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-9]
  [CHECKPOINT-summary] BeginChkptLSN=[0,0,6232554], EndChkptLSN=[0,0,6233141], DiskRecLSN=[0,0,6232554]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-9]
  Minimum LSN = [0,0,6232554]
  [2015/12/14 10:42:50] [Thread-140330825209600] [Level-9]
  [CHECKPOINT-END]
  [2015/12/14 10:42:50] [Thread-140326782105344] [Level-9]
  Sleep checkpoint thread ( next time : 2015-12-14 12:22:50 )
  ```
4. When the checkpoint is executed normally
  (1) Among the message contents displayed when executing checkpoint
  [CHECKPOINT-step9] Check the Remove Online Log File part.
  If `[None]` or `skip` appears at the end of each checkpoint execution, the checkpoint executed normally, but log files may not be deleted because a long transaction exists or replication data has not been sent.
  (2) If the log partition is full even though the log file is deleted every time a checkpoint occurs, check whether the transaction is very busy and the size of the file system.
  =>Since transactions are very busy while the checkpoint is being executed, new log files may be created as many as the number of log files deleted. Consider this and set the size of the file system to be large enough.

# Countermeasures when the log disk is full

---

Move the log files in `$ALTIBASE_HOME/logs` to a directory with enough free space, create symbolic links, and free the logs space so that the DBMS has space to perform I/O on log files.

*Script to move log files and make symbolic links

```
echo "Move Logfile Number"
read i
echo "Move Logfile Count"
read j
echo "ALTIBASE LOG DIR"
ALTI_DIR=/sas_home/hychoi/altibase_home_631/logs
echo $ALTI_DIR
echo "MOVE LOG DIR"
MOVE_DIR=/sas_home/hychoi/altibase_home_631/backuplog
echo $MOVE_DIR
MAX=`expr $i + $j`
cd
while true
  do
  log='logfile'$i
mv $ALTI_DIR/$log $MOVE_DIR
ln -s $MOVE_DIR/$log $ALTI_DIR/$log
i=`expr $i + 1`
if [ $i -eq $MAX ]
  then
    exit;
  fi;
done
```

For reference, if the current DB is running, the user must move and link the log files except for the log files in use.

* How to check the log files in use

```
lsof -p PID(ALTIBASE DB) | grep logfile
```
