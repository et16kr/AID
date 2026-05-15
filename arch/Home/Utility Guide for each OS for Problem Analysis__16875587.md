---
title: "Utility Guide for each OS for Problem Analysis"
page_id: "16875587"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/Utility+Guide+for+each+OS+for+Problem+Analysis"
updated_at: "2021-02-04T13:49:25.000+0900"
version: 6
ancestors: ["Home"]
labels: []
---

# Utility Guide for each OS for Problem Analysis
Source: https://docs.altibase.com/display/arch/Utility+Guide+for+each+OS+for+Problem+Analysis
Updated: 2021-02-04T13:49:25.000+0900

- [Overview](#UtilityGuideforeachOSforProblemAnalysis-Overview) - [Common Command](#UtilityGuideforeachOSforProblemAnalysis-CommonCommand) - [netstat](#UtilityGuideforeachOSforProblemAnalysis-netstat) - [vmstat](#UtilityGuideforeachOSforProblemAnalysis-vmstat) - [Linux](#UtilityGuideforeachOSforProblemAnalysis-Linux) - [CPU usage by thread](#UtilityGuideforeachOSforProblemAnalysis-CPUusagebythread) - [pstack](#UtilityGuideforeachOSforProblemAnalysis-pstack) - [Checking the list of files in use](#UtilityGuideforeachOSforProblemAnalysis-Checkingthelistoffilesinuse) - [System Log](#UtilityGuideforeachOSforProblemAnalysis-SystemLog) - [SUN](#UtilityGuideforeachOSforProblemAnalysis-SUN) - [prstat](#UtilityGuideforeachOSforProblemAnalysis-prstat) - [pstack](#UtilityGuideforeachOSforProblemAnalysis-pstack.1) - [pfiles](#UtilityGuideforeachOSforProblemAnalysis-pfiles) - [System Log](#UtilityGuideforeachOSforProblemAnalysis-SystemLog.1) - [AIX](#UtilityGuideforeachOSforProblemAnalysis-AIX) - [ps](#UtilityGuideforeachOSforProblemAnalysis-ps) - [prostack](#UtilityGuideforeachOSforProblemAnalysis-prostack) - [procfiles](#UtilityGuideforeachOSforProblemAnalysis-procfiles) - [System Log](#UtilityGuideforeachOSforProblemAnalysis-SystemLog.2) - [HP-UX](#UtilityGuideforeachOSforProblemAnalysis-HP-UX) - [CPU usage by thread with glance](#UtilityGuideforeachOSforProblemAnalysis-CPUusagebythreadwithglance) - [pstack](#UtilityGuideforeachOSforProblemAnalysis-pstack.2) - [pfiles](#UtilityGuideforeachOSforProblemAnalysis-pfiles.1) - [System Log](#UtilityGuideforeachOSforProblemAnalysis-SystemLog.3)

# Overview

---

When technical support related to DBMS is provided, there are cases where information for problem-solving is insufficient only with the performance view provided by Altibase.

This document describes several related commands provided by the operating system to obtain necessary information.

For errors and improvements related to this document, please contact the technical support portal or technical support center.

- Technical support portal: [http://support.altibase.com](http://support.altibase.com/)[/en/](http://support.altibase.com/en/)
- Technical support center: 02-2082-1114

# Common Command

---

This section describes commands that do not have special restrictions that can be executed by all operating systems.

## netstat

---

- This command checks whether there is a network configuration or an error packet.

  ```
  Shell> netstat -in
  Kernel Interface table
  Iface      MTU    RX-OK RX-ERR RX-DRP RX-OVR    TX-OK TX-ERR TX-DRP TX-OVR Flg
  enp5s0    1500 11116829      0 126934 0         74209      0      0      0 BMRU
  enp7s0    1500        0      0      0 0             0      0      0      0 BMU
  lo       65536  4709762      0      0 0       4709762      0      0      0 LRU
  ```

  If a problem occurs between sender and receiver on a packet, the value of R(T)X-ERR/R(T)X-DRP/R(T)X-OVR increases. In this case, there may be some problem on the network, so take measures to have the administrator check.

## vmstat

---

- This command checks system memory, disk, swap in/out, and CPU status at intervals set by the user.

  ```
  Shell> vmstat 1 5 (Display 5 times per second)
  procs   -----------memory---------- ---swap--  -----io---- -system-- ------cpu-----
   r  b   swpd   free   buff  cache   si   so      bi    bo   in   cs  us sy id wa st
   1  0      0 14407272 377356 472884    0    0     0     1    1    1  0  0 100  0  0
   1  0      0 14405904 377356 472884    0    0     0     0  150  381  0  0 99  0  0
   1  0      0 14406332 377356 472884    0    0     0     0   56  111  0  0 100  0  0
   0  0      0 14406332 377356 472884    0    0     0     0   36   67  0  0 100  0  0
   0  0      0 14407200 377356 472884    0    0     0    16   45  104  0  0 100  0  0
  ```

  The main indicators to be checked are as follows.

  |  | Description |
  | --- | --- |
  | proc r | The number of threads waiting to occupy the CPU. If the value is large, it can be judged that a CPU bottleneck occurs. |
  | memory free | Free space on physical memory |
  | swap si, so | An increase of si/so means that disk I/Os between the swap disk and memory are issued |
  | CPU us sy id wa st | Change trends for each item should be observed |

# Linux

---

## CPU usage by thread

---

- In Linux, the user can also check the CPU for each thread with the top command. If executed with the top -H option, the search is performed for each thread. However, it is possible only if the installed procps version is 3.2.7 or later. If not, simply check as follows. (Not well supported in lower version)

  ```
  Shell> ps -LFm -p <process id>
  UID          PID  PPID   LWP  C NLWP    SZ   RSS PSR STIME TTY          TIME CMD
  altibase    7153     1     -  8   47 921763 896248 - 16:53 ?        00:10:50 /home/lim272/altibase_home/bin/altibase -p b
  altibase       -     -  7153  0    -     -     -   2 16:53 -        00:00:00 -
  altibase       -     -  7154  0    -     -     -   0 16:53 -        00:00:00 -
  altibase       -     -  7163  0    -     -     -   7 16:53 -        00:00:10 -
  altibase       -     -  7164  0    -     -     -   1 16:53 -        00:00:10 -
  altibase       -     -  7165  2    -     -     -   1 16:53 -        00:03:20 -
  ```

  LWP is a unique number for each thread, and the value displayed in the C item is the CPU usage rate.

  |  | Description |
  | --- | --- |
  | CPU | CPU share that the thread is currently using |
  | LWPID | Unique number of thread |

## pstack

---

- Like pstack, when checking the CPU occupancy of a thread, it is used as a way to check what part the thread is currently executing.

  ```
  Shell> pstack <process id>
  Thread 45 (Thread 0x7f8d27794700 (LWP 7164)):
  #0  0x00007f8d2e8669b3 in epoll_wait () from /lib64/libc.so.6
  #1  0x0000000000f5e761 in cmnDispatcherDetectSOCKEpoll(cmnDispatcher*, iduList*, unsigned int*, PDL_Time_Value*) ()
  #2  0x0000000000f49dcb in cmiSelectDispatcher(cmnDispatcher*, iduList*, unsigned int*, PDL_Time_Value*) ()
  #3  0x000000000042a4fc in mmtServiceThread::findReadyTask(PDL_Time_Value*) ()
  #4  0x000000000042cfb7 in mmtServiceThread::run() ()
  #5  0x0000000000f80da2 in idtContainer::staticRunner(void*) ()
  #6  0x00007f8d2f796df3 in start_thread () from /lib64/libpthread.so.0
  #7  0x00007f8d2e8663dd in clone () from /lib64/libc.so.6
  Thread 44 (Thread 0x7f8d26bf3700 (LWP 7165)):
  #0  0x0000000000e6660e in smnnSeq::fetchNext(smnnIterator*, void const**) ()
  #1  0x0000000000ec70ce in smiTableCursor::readRow(void const**, scGRID*, unsigned int) ()
  #2  0x00000000006b83f2 in qmnSCAN::readRow(qcTemplate*, qmncSCAN*, qmndSCAN*, int*) ()
  #3  0x00000000006b851b in qmnSCAN::doItNext(qcTemplate*, qmnPlan*, int*) ()
  #4  0x00000000006b710b in qmnSCAN::doIt(qcTemplate*, qmnPlan*, int*) ()
  #5  0x0000000000887a1a in qmnJOIN::doItRight(qcTemplate*, qmnPlan*, int*) ()
  #6  0x0000000000887c3f in qmnJOIN::doIt(qcTemplate*, qmnPlan*, int*) ()
  #7  0x0000000000881b14 in qmnHSDS::doItDependent(qcTemplate*, qmnPlan*, int*) ()
  #8  0x0000000000881c4f in qmnHSDS::doIt(qcTemplate*, qmnPlan*, int*) ()
  #9  0x00000000006bb2a4 in qmnPROJ::doIt(qcTemplate*, qmnPlan*, int*) ()
  #10 0x00000000004d27cf in qci::moveNextRecord(qciStatement*, smiStatement*, idBool*) ()
  #11 0x000000000043f682 in mmtServiceThread::fetch(cmiProtocolContext*, mmcSession*, mmcStatement*, unsigned short, unsigned short, unsigned short, unsigned int) ()
  #12 0x00000000004402ad in mmtServiceThread::fetchProtocol(cmiProtocolContext*, cmpProtocol*, void*, void*) ()
  #13 0x0000000000f4b477 in cmiRecv(cmiProtocolContext*, void*, PDL_Time_Value*, void*) ()
  #14 0x000000000042a7ef in mmtServiceThread::executeTask_READY(mmcTask*, mmcTaskState*) ()
  #15 0x000000000042c355 in mmtServiceThread::executeTask() ()
  #16 0x000000000042c922 in mmtServiceThread::multiplexingAsShared() ()
  #17 0x000000000042cfb7 in mmtServiceThread::run() ()
  #18 0x0000000000f80da2 in idtContainer::staticRunner(void*) ()
  #19 0x00007f8d2f796df3 in start_thread () from /lib64/libpthread.so.0
  #20 0x00007f8d2e8663dd in clone () from /lib64/libc.so.6
  ```

  Since all of the above results are output for each thread, classify each thread and check from the bottom to the top within the paragraph. In the example above, Thread 44 (LWP:7165) is in the following order.

  |  | Description |
  | --- | --- |
  | clone start_thread staticRunner run multiplexingAsShared execute_Task execute_Task_READY | creating and starting a thread |
  | cmiRecv | The user's query request has been read in the communication |
  | mmtServiceThread::executeProtocol mmtSerivceThread::execute doExecute | Enter the execution stage |
  | mmcStatement::execute mmcStatement::executeDML qci::execute qmx:executeInsertSelect qmnINST:doItNext qmnINST:insertOneRow smiTableCursor::insertRow smiTableCursor::normalInsertRow smcRecord::insertVersion | Check the execution of Insert statement |
  | smcRecordUpdate::writeInsertLog smxTrans::writeTransLog smrLogMgr::writeLog | Write redo log to execute insert statement |
  | smLogMgr::updateTransLSNInfo smxTrans::setLstUndoNxtLSN | Update transaction lsn for undo |
  | iduPosixLock | Acquire a lock on a thread |

  By looking at the information of ps/pstack as shown above, it is possible to check what specific thread that uses the most CPU is performing. Also among many SQL statements, a more narrow trace can be made with the above pstack results.

## Checking the list of files in use

---

- If a separate utility, such as lsof in Linux, is not installed, do the following.

  ```
  Shell> ls -l /proc/<process id>/fd
  lrwx------ 1 altibase altibase 64 Aug 14 18:56 44 -> socket:[130274146]
  lrwx------ 1 altibase altibase 64 Aug 14 18:56 46 -> /home/altibase/altibase_home/logs/logfile21
  lrwx------ 1 altibase altibase 64 Aug 14 18:56 47 -> /home/altibase/altibase_home/logs/logfile22
  lrwx------ 1 altibase altibase 64 Aug 14 18:56 48 -> /home/altibase/altibase_home/logs/logfile23
  lrwx------ 1 altibase altibase 64 Aug 14 18:56 49 -> /home/altibase/altibase_home/logs/logfile24
  ```

  In Linux, various information can be checked under the /proc/<process id> path, so please refer to the related information.

## System Log

---

- Check the files that exist in /var/log/. Generally, check the messages file.

# SUN

---

- These are commands based on Solaris 5.10.

## prstat

---

- Altibase is developed in the thread structure, and this command is used to check which thread occupies and uses a lot of CPU in some cases.

  ```
  Shell> prstat -L -p <process id> <refresh interval>
  Ex) prstat -L -p 22951 1   (Means to view the process in 1 second)
  PID      USERNAME      SIZE   RSS   STATE  PRI NICE   TIME  CPU   PROCESS/LWPID
  22951    altibase      502M  106M   sleep   59    0   0:22:50   1.7%   altibase/5
  22951    altibase      502M  106M   sleep   59    0   0:23:49   0.3%   altibase/4
  22951    altibase      502M  106M   sleep   59    0   0:00:10   0.1%   altibase/12
  22951    altibase      502M  106M   sleep   59    0   0:00:05   0.1%   altibase/47
  22951    altibase      502M  106M   sleep   59    0   0:25:28   0.0%   altibase/6
  22951    altibase      502M  106M   sleep   59    0   0:22:19   0.0%   altibase/9
  22951    altibase      502M  106M   sleep   59    0   0:23:13   0.0%   altibase/8
  ```

## pstack

---

- Similar to prstat, when checking the CPU occupancy of a thread, it is used as a way to check what part the thread is currently executing.

  ```
  Shell> pstack -F <process pid> | c++filt
  -----------------  lwp# 7 / thread# 7  --------------------
  ffffffff7e1d9ce8 pollsys  (ffffffff7b4ffa50, 0, ffffffff7b4ffb10, 0)
  ffffffff7e173c44 pselect (0, ffffffff7b4ffa50, ffffffff7e344710, ffffffff7e344710, ffffffff7b4ffb10, 0) + 1f0
  ffffffff7e173fe8 select (0, 106eea070, 0, 0, ffffffff7b4ffbd8, fffc00) + a0
  00000001006f6df4 IDE_RC cmnDispatcherSelectSOCK(cmnDispatcher*,iduList*,unsigned*,PDL_Time_Value*) (106eea040, ffffffff7b4ffd88, 0, 106cc5818, ffffffff, 106eea070) + 50
  00000001006f089c IDE_RC cmiSelectDispatcher(cmnDispatcher*,iduList*,unsigned*,PDL_Time_Value*) (106eea040, ffffffff7b4ffd88, 0, 106cc5818, ffffffffffffffff, 1006f6da4) + 1c
  0000000100140790 void mmtServiceThread::findReadyTask() (106cc56d8, 105966f18, 101000, 0, 2710, 0) + 14
  000000010013f878 void mmtServiceThread::run() (106cc56d8, 1, ffffffffffffffff, 2ec6bb9, 101329000, 10132b000) + 560
  0000000100717034 void*idtBaseThread::staticRunner(void*) (106cc56d8, 100000, 0, 0, 100a120c8, 10013f318) + 14
  ffffffff7e1d609c _lwp_start (0, 0, 0, 0, 0, 0)
  ```

  The c++filter command is used to remove the case where the function named called between C/C++ is not displayed properly. When not used, the function name is displayed in a form that is difficult to see, so it is possible to use it. Generally, it exists where the executable file of the path where the compiled is installed is located. (Ex: /opt/SUNwspro/bin/) In the same way as the method of interpreting the result of pstack, it is divided into paragraph units based on lwp# for each thread and interpreted from bottom to top.

## pfiles

---

- Similar to prstat, when checking the CPU occupancy of a thread, it is used as a way to check what part the thread is currently executing.

  ```
  Shell> pfiles -F <process id>
  22951:  /home2/altibase/work/altibase_home/bin/altibase -p boot from admin
  Current rlimit: 65535 file descriptors
  0: S_IFREG mode:0644 dev:118,38 ino:3309572 uid:124 gid:1 size:202128
  O_WRONLY|O_APPEND|O_CREAT|O_LARGEFILE
  /home2/altibase/work/altibase_home/trc/altibase_boot.log
  1: S_IFREG mode:0644 dev:118,38 ino:3309573 uid:124 gid:1 size:1413256
  O_WRONLY|O_APPEND|O_CREAT|O_LARGEFILE
  /home2/altibase/work/altibase_home/trc/altibase_sm.log
  ```

  In the above result, all the files accessed by the process in the order of 0 and 1 along with the currently available file descriptor information are shown. When running pfiles while multiple sessions are connected, all data files, trace logs, transaction log files, and even a list of communication connections are displayed.

  ```
  321: S_IFSOCK mode:0666 dev:329,0 ino:63732 uid:0 gid:0 size:0
  O_RDWR|O_NONBLOCK
  SOCK_STREAM
  SO_REUSEADDR,SO_KEEPALIVE,SO_SNDBUF(65536),SO_RCVBUF(32788),IP_NEXTHOP(0.0.128.20)
  sockname: AF_INET 127.0.0.1  port: 27584
  peername: AF_INET 127.0.0.1  port: 42567
  ```

## System Log

---

- During the technical support, if the user needs to find the cause from outside, SUN should check /var/adm/messages. The file extension means the week the log was recorded, and the log of the week including today is recorded in the messages file.

  ```
  Shell> vi /var/adm/messages
  Feb 24 18:08:24 v880    Corrupt label; wrong magic number
  Feb 24 18:08:24 v880 scsi: [ID 107833 kern.warning] WARNING: /pci@9,700000/fibre-channel@4/fp@0,0/ssd@w210000d023041a42,7 (ssd13):
  Feb 24 18:08:24 v880    Corrupt label; wrong magic number
  Feb 24 18:08:24 v880 scsi: [ID 107833 kern.warning] WARNING: /pci@9,700000/fibre-channel@4/fp@0,0/ssd@w210000d023041a42,7 (ssd13):
  Feb 24 18:08:24 v880    Corrupt label; wrong magic number
  ```

  The system log is difficult to understand clearly unless the user is an expert of each vendor, but when providing technical support dude to a failure, etc., make sure to check if there is any important log at a specific time.

# AIX

---

- Certain commands may not be supported prior to AIX 5.1.

## ps

---

- The same results can be checked as SUN's prstat.

  ```
  Shell> ps -mo THREAD -p <process id>
      USER     PID    PPID       TID S  CP PRI SC    WCHAN        F     TT BND COMMAND
  altibase 1802540       1         - A   0  60 40        *    40001      -   - /home/altibase/altibase_home/bin/altibase -p boot
         -       -       -    860211 S   0  60  1        -   418400      -   - -
         -       -       -   1409101 S   0  60  1        -   410400      -   - -
         -       -       -   1462489 S   0  60  1        -   410400      -  12 -
         -       -       -   1482935 S   0  60  1        -   410400      -   8 -
  ```

  In the above result, the occupancy rate used by threads can be checked with the CP column.

## prostack

---

- The same results can be checked as SUN's pstack.

  ```
  Shell> procstack <process id>
  ---------- tid# 6901809 (pthread ID:    258) ----------
  0x0900000000062a14  write(??, ??, ??) + 0x1c8
  0x00000001000b9a60  cmnSockSend(cmbBlock*,cmnLinkPeer*,int,PDL_Time_Value*,idvStatIndex)() + 0x308
  0x00000001000b8d38  cmnLinkPeerSendTCP(cmnLinkPeer*,cmbBlock*)() + 0x30
  0x000000010007f28c  cmiWriteBlock(cmiProtocolContext*,idBool)() + 0x24c
  0x000000010007ccc0  cmiFlushProtocol(cmiProtocolContext*,idBool)() + 0xa8
  0x00000001000cd838  mmtServiceThread::executeTask()() + 0xc1c
  0x00000001000cbb80  mmtServiceThread::multiplexingAsShared()() + 0x84
  0x00000001000cc594  mmtServiceThread::run()() + 0x4c4
  0x0000000100077bd4  idtBaseThread::staticRunner(void*)() + 0x28
  0x09000000004a44f4  _pthread_body(??) + 0xdc
  ```

  In the same way as the method of interpreting the result of pstack, it is divided into paragraph units based on tid# for each thread and interpreted from bottom to top. In the above result, it can be seen that the transmission part of the communication thread about the result is recorded after a certain query is executed.

## procfiles

---

- The same results can be checked as SUN's pfiles

  ```
  Shell> pfiles -n <process id>
  1802540 : /home/altibase/altibase_home/bin/altibase -p boot from admin
  Current rlimit: 100 file descriptors
  0: S_IFREG mode:0200 dev:53,1 ino:2731329 uid:222 gid:1 rdev:0,0 O_WRONLY | O_APPEND size:451248  name:/home/altibase/altibase_home/trc/altibase_boot.log
  1: S_IFREG mode:0222 dev:53,1 ino:2731337 uid:222 gid:1 rdev:0,0 O_WRONLY | O_APPEND size:3014040  name:/home/altibase/altibase_home/trc/altibase_sm.log
  ```

  -The used file can also be checked by using the -n option.

## System Log

---

- It is used to check the system log if an error has occurred in the operating equipment. Since the log for disk device errors, network device errors, or abnormal termination of processes can be checked, the user must check the system log when to find the cause from outside during the technical support.

  ```
  Shell> errpt -a | more
  ---------------------------------------------------------------------------
  LABEL:          CORE_DUMP
  IDENTIFIER:     C69F5C9B
  Date/Time:       Thu Feb 25 03:59:12 KORST 2010
  Sequence Number: 23893
  Machine Id:      00C76BFD4C00
  Node Id:         aix53-p5
  Class:           S
  Type:            PERM
  Resource Name:   SYSPROC
  Description
  SOFTWARE PROGRAM ABNORMALLY TERMINATED
  Probable Causes
  SOFTWARE PROGRAM
  ```

# HP-UX

---

- Depending on the type of HP CPU, it is classified into PA-RISK/ITANIUM, but some commands may not be supported by PA-RISK equipment.

## CPU usage by thread with glance

---

- In the case of HP, CPU usage for each thread can be checked with a monitoring tool called glance.

  ```
  Run through Shell> glance
  If you press the <s> key, you can enter a specific process id.
  If you press the <G> key, you can check the CPU usage for each thread of the process.
  ```

## pstack

---

- This shows the same results as SUN's pstack.

  ```
  Shell> pstack <process id>
  --------------------------------  lwpid : 3486042   -------------------------------
  0: c000000000446910 : (unknown) () (unknown)
  1: c0000000001a75a0 : (unknown) () (unknown)
  2: c0000000000e1130 : (unknown) () (unknown)
  3: c0000000000e40c0 : (unknown) () (unknown)
  4: 4000000001330fd0 : rpxSender::sleepForNextConnect()() + 0x3b0 (/home/ckh0618/altibase_home/bin/altibase)
  5: 4000000001340cc0 : rpxSender::attemptHandshake(idBool*)() + 0x4c0 (/home/ckh0618/altibase_home/bin/altibase)
  6: 4000000001326f80 : rpxSender::run()() + 0x1a0 (/home/ckh0618/altibase_home/bin/altibase)
  7: 4000000001e108a0 : idtBaseThread::staticRunner(void*)() + 0x60 (/home/ckh0618/altibase_home/bin/altibase)
  8: c0000000000fa220 : (unknown) () (unknown)
  ```

  lwpid means the unique number of the thread. Similarly, paragraphs are separated by lwpid and interpreted from bottom to top. In the above case, the operation to connect the replication Sender Thread with the other party is shown.

## pfiles

---

- This shows the same results as SUN's pfiles.

  ```
  Shell> pfiles <process id>
  0: S_ISREG mode:666 dev:64,65537 ino:8490324 uid:124 gid:20 size:530024 flags = O_WRONLY|O_APPEND|O_LARGEFILE file  = /home/ckh0618/altibase_home/trc/altibase_boot.log
  1: S_ISREG mode:666 dev:64,65537 ino:8490373 uid:124 gid:20 size:8466361 flags = O_WRONLY|O_APPEND|O_LARGEFILE file  = /home/ckh0618/altibase_home/trc/altibase_sm.log
  ```

## System Log

---

- To check the system log in HP, check as follows.

  ```
  Shell> vi /var/adm/syslog/syslog.log
  Feb 24 10:32:07 rx5670 vmunix:     System Console is on the Built-In Serial Interface
  Feb 24 10:32:07 rx5670 vmunix: igelan0: INITIALIZING HP A6794-60001 PCI 1000Base-T at hardware path 0/1/1/0/4/0
  Feb 24 10:32:07 rx5670 vmunix: Logical volume 64, 0x3 configured as ROOT
  Feb 24 10:32:07 rx5670 vmunix: Logical volume 64, 0x2 configured as SWAP
  Feb 24 10:32:07 rx5670 vmunix: Logical volume 64, 0x2 configured as DUM
  ```

# Korean Source Attachments

The Korean source page also references these downloadable source attachments. They are preserved here so the English document set does not lose those references.

- [Korean source attachment 1 (PDF)](https://docs.altibase.com/download/attachments/13436866/ALTIBASE_%EB%AC%B8%EC%A0%9C%EB%B6%84%EC%84%9D%EC%9D%84_%EC%9C%84%ED%95%9C_OS%EB%B3%84_%EC%9C%A0%ED%8B%B8%EB%A6%AC%ED%8B%B0_%EC%82%AC%EC%9A%A9_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1698050117000&api=v2)
