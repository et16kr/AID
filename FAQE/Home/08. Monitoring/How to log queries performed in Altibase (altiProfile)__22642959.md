---
title: "How to log queries performed in Altibase (altiProfile)?"
page_id: "22642959"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=22642959"
updated_at: "2025-10-20T15:42:03.000+0900"
version: 1
ancestors: ["Home", "08. Monitoring"]
labels: []
---

# How to log queries performed in Altibase (altiProfile)?
Source: https://docs.altibase.com/pages/viewpage.action?pageId=22642959
Updated: 2025-10-20T15:42:03.000+0900

- [Overview](#HowtologqueriesperformedinAltibase(altiProfile)?-Overview) - [Profiling related properties](#HowtologqueriesperformedinAltibase(altiProfile)?-Profilingrelatedproperties) - [How to start and stop profiling](#HowtologqueriesperformedinAltibase(altiProfile)?-Howtostartandstopprofiling) - [How to analyze the results](#HowtologqueriesperformedinAltibase(altiProfile)?-Howtoanalyzetheresults) - [Precautions](#HowtologqueriesperformedinAltibase(altiProfile)?-Precautions)

# Overview

---

All SQL statements executed on the Altibase server can be traced.

It is possible by setting/disabling Altibase properties, and in addition to SQL statements, it is possible to trace execution time, index/disk access information, PLAN information, session information, and ALTIBASE HDB system information.

This chapter describes how to profile Altibase and check the results.

# Profiling related properties

---

| Property Name | Description |  |
| --- | --- | --- |
| QUERY_PROF_FLAG | Set the level for collecting and recording server status and operation details<br>\| Value \| Name \| Description \|<br>\| --- \| --- \| --- \|<br>\| 0 \|  \| Do not record (default) \|<br>\| 1 \| [STATEMENT] \| Each time an SQL statement is executed, outputs the executed SQL, execution time, execution info, index, and disk access info.<br>To display execution time correctly, the `TIMED_STATISTICS` property must be set to 1. \|<br>\| 2 \| [BIND] \| Each time a prepared SQL statement is executed, outputs the Bind Parameter values (only if variable binding info exists). \|<br>\| 4 \| [PLAN] \| Each time an SQL statement is executed, outputs the execution plan. \|<br>\| 8 \| [SESSION STAT] \| Outputs session info every 3 seconds (V$SESSTAT information). \|<br>\| 16 \| [SYSTEM STAT] \| Outputs system info every 3 seconds (V$SYSSTAT information). \|<br>\| 32 \| [MEMORY STAT] \| Outputs memory info every 3 seconds (V$MEMSTAT information). \|<br>By combining these `QUERY_PROF_FLAG` values, various server status information and operation details can be collected.<br>For example, setting it to 7 (1 + 2 + 4) will output statement and execution time, bound variable values, and SQL execution plan info every time an SQL statement is executed.<br>Setting it to 63 (1 + 2 + 4 + 8 + 16 + 32) will output all possible information:<br>on each SQL execution, the `[STATEMENT]`, `[BIND]`, and `[PLAN]` information will be output in sequence,<br>and every 3 seconds, the system info `[SESSION STAT]`, `[SYSTEM STAT]`, and `[MEMORY STAT]` will be output to show Altibase status. |  |
| Value | Name | Description |
| 0 |  | Do not record (default) |
| 1 | [STATEMENT] | Each time an SQL statement is executed, outputs the executed SQL, execution time, execution info, index, and disk access info.<br>To display execution time correctly, the `TIMED_STATISTICS` property must be set to 1. |
| 2 | [BIND] | Each time a prepared SQL statement is executed, outputs the Bind Parameter values (only if variable binding info exists). |
| 4 | [PLAN] | Each time an SQL statement is executed, outputs the execution plan. |
| 8 | [SESSION STAT] | Outputs session info every 3 seconds (V$SESSTAT information). |
| 16 | [SYSTEM STAT] | Outputs system info every 3 seconds (V$SYSSTAT information). |
| 32 | [MEMORY STAT] | Outputs memory info every 3 seconds (V$MEMSTAT information). |
| QUERY_PROF_LOG_DIR | Directory path where the operations performed and server status information are stored in Altibase<br>Default: $ALTIBASE_HOME/trc<br>This path can be changed during Altibase operation using the ALTER SYSTEM statement. |  |

# How to start and stop profiling

---

- Start profiling Record information on all SQL statements executed after the next command is executed in the log file.

  ALTER SYSTEM SET QUERY_PROF_FLAG = *value*;

  ALTER SYSTEM SET TIMED_STATISTICS = 1;

  Value: Refer to the description of the QUERY_PROF_FLAG property above.

  TIMED_STATISTICS: In version 5.1.5 or later, to check the execution time of an SQL statement, this property value should be set to 1 (default is 0). (In versions earlier that, there is no corresponding property, and you can check the execution time of all SQL statements by default.)
- Stop profiling To stop profiling, execute the following command:

  ALTER SYSTEM SET QUERY_PROF_FLAG = 0;

# How to analyze the results

---

When profiling starts, a log file is created in the format $ALTIBASE_HOME/trc/**alti#time-#number.prof.** (By default, files are created in the format: $ALTIBASE_HOME/trc/alti#timestamp-#sequence.prof)

Since the log file is in binary format, it must be converted to a text file using the altiProfile command. The method is as follows.

When there is a single profile file:

`$ altiProfile alti-#timestamp-#sequence.prof > #sequence.out`

When there are multiple profile files:

$ altiProfile *.prof > #sequence.out

Since the log file conversion result is output to stdout, it is recommended to save it as a file as in the example above.

The following is a description of the contents of the converted result.

- When QUERY_PROF_FLAG = 1 is set

**Output format**

[STATEMENT] Record time (session_ID/SQL statement_ID/transaction_ID)

SQL statement

User information :

Time it took to execute

Execution information: Success/failure status and number of success/failures

Index access information

Disk access information

**Example**

```
[STATEMENT] 2025/07/16 09:45:05(2/131076/129940)
  SQL
     => [UPDATE EMPLOYEES SET DNO = ?, EMP_TEL = ? WHERE ENO = ?]

  User Info
     User    ID     = 2
     Client PID     = 30017
     Client Type    = [CLI-64LE]
     Client AppInfo = [isql]

  Elapsed Time
     Total =            0 sec      618 usec
     SoftP =            0 sec       55 usec
     Parse =            0 sec        0 usec
     Valid =            0 sec        0 usec
     Optim =            0 sec        0 usec
     Execu =            0 sec      563 usec
     Fetch =            0 sec        0 usec

  Query Execute Info
     EXECUTE Result =                    4 (0:failure, 1:rebuild, 2:retry, 3:queue empty, 4:success)
     Optimizer Mode =                    0
     Cost      Mode =                    0
     Used Memory    =                    0
     SUCCESS   SUM  =                    1
     FAILURE   SUM  =                    0
     PROCESSED ROW  =                    1

  XA Info
     XA Flag        =                    0 (0:Non-XA, 1:XA)

  Result Set Info
     FETCH Result   =                    2 (0:failure, 1:success, 2:no result set)

  Index Access Info
     Memory Full  Scan Count  =                    0
     Memory Index Scan Count  =                    1
     Disk   Full  Scan Count  =                    0
     Disk   Index Scan Count  =                    0

  Disk Access Info
     READ   DATA PAGE  =                    0
     WRITE  DATA PAGE  =                    0
     GET    DATA PAGE  =                    0
     CREATE DATA PAGE  =                    0
     READ   UNDO PAGE  =                    0
     WRITE  UNDO PAGE  =                    0
     GET    UNDO PAGE  =                    0
     CREATE UNDO PAGE  =                    0
```

- When QUERY_PROF_FLAG = 3 is set (i.e., QUERY_PROF_FLAG = 1 + 2): Both the executed SQL statement and the bind variable values for prepared SQL statements are output.

**Example**

```
[BIND] 2025/07/16 09:45:05 (2/131076/129940/01)
    [(_integer ) 3001]                          ==>  Bind 변수 값
[BIND] 2025/07/16 09:45:05 (2/131076/129940/02)
    [(_char    ) (11)                           ==>  Bind 변수 값
    00000000 01011111111]
[BIND] 2025/07/16 09:45:05 (2/131076/129940/03)
    [(_integer ) 1]                             ==>  Bind 변수 값
```

- When QUERY_PROF_FLAG = 7 is set (i.e., QUERY_PROF_FLAG = 1 + 2 + 4): It outputs the SQL statement, the bind variable values, and the execution plan generated for the SQL execution.

**Example**

```
[PLAN] 2025/07/16 09:45:05(2/131076/129940)
[------------------------------------------------------------
UPDATE ( TABLE: SYS.EMPLOYEES )
 SCAN ( TABLE: SYS.EMPLOYEES, INDEX: SYS.__SYS_IDX_ID_143, RANGE SCAN, ACCESS: 1, COST: 0.01 )
------------------------------------------------------------
]
```

- When QUERY_PROF_FLAG = 15 is set (i.e., QUERY_PROF_FLAG = 1 + 2 + 4 + 8): Session information for all sessions currently created on the server is recorded as shown below. The output is equivalent to the result of executing: SELECT * FROM v$sesstat ORDER BY sid, seqnum;

[SESSION STAT] Record time (Session_ID)

Field name = value

**Example**

```
[SESSION STAT] 2025/07/16 10:05:23 (1)
     logon current                             =          1
     logon cumulative                          =          1
     data page read                            =          0
     data page write                           =          0
     data page gets                            =          0
     data page fix                             =          0
     data page create                          =          0
     undo page read                            =          0
     undo page write                           =          0
     undo page gets                            =          0
     undo page fix                             =          0
     undo page create                          =          0
     base time in second                       =          0
     query timeout                             =          0
     ddl timeout                               =          0
     idle timeout                              =          0
     fetch timeout                             =          0
     utrans timeout                            =          0
     session terminated                        =          0
     ddl sync timeout                          =          0
     statement rebuild count                   =          0
     unique violation count                    =          0
     update retry count                        =          0
     delete retry count                        =          0
     lock row retry count                      =          0
     session commit                            =          0
     session rollback                          =          0
     fetch success count                       =          0
     fetch failure count                       =          0
     execute success count                     =          5
     execute success count : insert            =          0
     execute success count : update            =          0
     execute success count : delete            =          0
     execute success count : select            =          0
     rep_execute success count : insert        =          0
     rep_execute success count : update        =          1
     rep_execute success count : delete        =          0
     execute failure count                     =          0
     prepare success count                     =          4
     prepare failure count                     =          0
     rebuild count                             =          0
     write redo log count                      =          1
     write redo log bytes                      =        272
     read socket count                         =          6
     write socket count                        =          7
     byte received via inet                    =        677
     byte sent via inet                        =        620
     byte received via unix domain             =          0
     byte sent via unix domain                 =          0
     semop count for receiving via ipc         =          0
     semop count for sending via ipc           =          0
     memory table cursor full scan count       =          0
     memory table cursor index scan count      =          1
     memory table cursor GRID scan count       =          0
     disk table cursor full scan count         =          0
     disk table cursor index scan count        =          0
     disk table cursor GRID scan count         =          0
     lock acquired count                       =          3
     lock released count                       =          0
     service thread created count              =          0
     memory table access count                 =          1
     missing ppco x-trylatch count             =          0
     read IB count                             =          0
     write IB count                            =          0
     byte received via IB                      =          0
     byte sent via IB                          =          0
     elapsed time: query parse                 =        407
     elapsed time: query validate              =          0
     elapsed time: query optimize              =          0
     elapsed time: query execute               =   66497143
     elapsed time: query fetch                 =          0
     elapsed time: soft prepare                =        155
     elapsed time: analyze values in DML(disk)  =          0
     elapsed time: record lock validation in DML(disk)  =          0
     elapsed time: allocate data slot in DML(disk)  =          0
     elapsed time: write undo record in DML(disk)  =          0
     elapsed time: allocate tss in dml(disk)   =          0
     elapsed time: allocate undopage in dml(disk)  =          0
     elapsed time: index operation in dml(disk)  =          0
     elapsed time: create page(disk)           =          0
     elapsed time: get page(disk)              =          0
     elapsed time: fix page(disk)              =          0
     elapsed time: logical aging by tx in dml(disk)  =          0
     elapsed time: phyical aging by tx in dml(disk)  =          0
     elapsed time: replace(plan cache)         =          0
     elapsed time: victim free in replace(plan cache)  =          0
     elapsed time: hard rebuild                =          0
     elapsed time: soft rebuild                =          0
     elapsed time: add hard-prepared plan to plan cache  =          0
     elapsed time: add hard-rebuild plan to plan cache  =          0
     elapsed time: search time for parent PCO  =         42
     elapsed time: creation time for parent PCO  =          0
     elapsed time: search time for child PCO   =          0
     elapsed time: creation time for child PCO  =          0
     elapsed time: validation time for child PCO  =         23
     elapsed time: creation time for new child PCO by rebuild at execution   =          0
     elapsed time: creation time for new child PCO by rebuild at soft prepare  =          0
     elapsed time: hard prepare time           =        510
     elapsed time: matching time for child PCO  =         33
     elapsed time: waiting time for hard prepare  =          0
     elapsed time: moving time from cold region to hot region.  =          0
     elapsed time: waiting time for parent PCO  when choosing plan cache replacement victim.  =          0
     elapsed time: privilege checking time during soft prepare.  =          9
     elapsed time: copying logs to replication log buffer (sender side)  =          0
     elapsed time: sender(s) waiting for new logs  =          0
     elapsed time: sender(s) reading logs from replication log buffer  =          0
     elapsed time: sender(s) reading logs from log file(s)  =          0
     elapsed time: sender(s) checking whether logs are useful  =          0
     elapsed time: sender(s) analyzing logs    =          0
     elapsed time: sender(s) sending xlogs to receiver(s)  =          0
     elapsed time: sender(s) receiving ACK from receiver(s)  =          0
     elapsed time: sender(s) setting ACKed value  =          0
     elapsed time: receiver(s) receiving xlogs from sender(s)  =          0
     elapsed time: receiver(s) performing endian conversion  =          0
     elapsed time: receiver(s) beginning transaction(s)  =          0
     elapsed time: receiver(s) committing transaction(s)  =          0
     elapsed time: receiver(s) aborting transaction(s)  =          0
     elapsed time: receiver(s) opening table cursor(s)  =          0
     elapsed time: receiver(s) closing table cursor(s)  =          0
     elapsed time: receiver(s) inserting rows  =          0
     elapsed time: receiver(s) updating rows   =          0
     elapsed time: receiver(s) deleting rows   =          0
     elapsed time: receiver(s) opening lob cursor(s)  =          0
     elapsed time: receiver(s) preparing to write LOB(s)  =          0
     elapsed time: receiver(s) writing LOB piece(s)  =          0
     elapsed time: receiver(s) finish writing LOBs  =          0
     elapsed time: receiver(s) closing LOB cursor(s)  =          0
     elapsed time: receiver(s) comparing images to check for conflicts  =          0
     elapsed time: receiver(s) sending ACK     =          0
     elapsed time: receiver(s) trim LOB(s)     =          0
     elapsed time: task schedule               =          0
     max     time: task schedule               =          0
```

- When QUERY_PROF_FLAG = 31 is set (i.e., QUERY_PROF_FLAG = 1 + 2 + 4 + 8 + 16):
  Comprehensive information about the overall Altibase system is output.
  This output is equivalent to the result of executing: SELECT * FROM v$sysstat ORDER BY seqnum;
  .

**Example**

```
[SYSTEM STAT] 2025/07/16 10:15:26 (0)
     logon current                             =          1
     logon cumulative                          =         12
     data page read                            =          4
     data page write                           =          0
     data page gets                            =      13390
     data page fix                             =        735
     data page create                          =      27754
     undo page read                            =          0
     undo page write                           =          0
     undo page gets                            =          0
     undo page fix                             =          0
     undo page create                          =          0
     base time in second                       = 1752628526
     query timeout                             =          0
     ddl timeout                               =          0
     idle timeout                              =          0
     fetch timeout                             =          0
     utrans timeout                            =          2
     session terminated                        =          0
     ddl sync timeout                          =          0
     statement rebuild count                   =          0
     unique violation count                    =          0
     update retry count                        =          0
     delete retry count                        =          0
     lock row retry count                      =          0
     session commit                            =         85
     session rollback                          =         11
     fetch success count                       =         57
     fetch failure count                       =          0
     execute success count                     =        158
     execute success count : insert            =          0
     execute success count : update            =          0
     execute success count : delete            =          0
     execute success count : select            =         57
     rep_execute success count : insert        =          0
     rep_execute success count : update        =         20
     rep_execute success count : delete        =          0
     execute failure count                     =         12
     prepare success count                     =        135
     prepare failure count                     =         23
     rebuild count                             =          0
     write redo log count                      =      31862
     write redo log bytes                      =    4552687
     read socket count                         =        230
     write socket count                        =        596
     byte received via inet                    =      95951
     byte sent via inet                        =     173741
     byte received via unix domain             =        140
     byte sent via unix domain                 =       9237
     semop count for receiving via ipc         =          0
     semop count for sending via ipc           =          0
     memory table cursor full scan count       =        439
     memory table cursor index scan count      =       8337
     memory table cursor GRID scan count       =          0
     disk table cursor full scan count         =         18
     disk table cursor index scan count        =          0
     disk table cursor GRID scan count         =          0
     lock acquired count                       =       8436
     lock released count                       =       2489
     service thread created count              =         25
     memory table access count                 =      13918
     missing ppco x-trylatch count             =          0
     read IB count                             =          0
     write IB count                            =          0
     byte received via IB                      =          0
     byte sent via IB                          =          0
     elapsed time: query parse                 =      19280
     elapsed time: query validate              =      11934
     elapsed time: query optimize              =       5714
     elapsed time: query execute               = 3199359716
     elapsed time: query fetch                 =       4968
     elapsed time: soft prepare                =       4675
     elapsed time: analyze values in DML(disk)  =          0
     elapsed time: record lock validation in DML(disk)  =          0
     elapsed time: allocate data slot in DML(disk)  =          0
     elapsed time: write undo record in DML(disk)  =          0
     elapsed time: allocate tss in dml(disk)   =          0
     elapsed time: allocate undopage in dml(disk)  =          0
     elapsed time: index operation in dml(disk)  =          0
     elapsed time: create page(disk)           =          0
     elapsed time: get page(disk)              =          0
     elapsed time: fix page(disk)              =          0
     elapsed time: logical aging by tx in dml(disk)  =          0
     elapsed time: phyical aging by tx in dml(disk)  =          0
     elapsed time: replace(plan cache)         =          0
     elapsed time: victim free in replace(plan cache)  =          0
     elapsed time: hard rebuild                =          0
     elapsed time: soft rebuild                =          0
     elapsed time: add hard-prepared plan to plan cache  =         71
     elapsed time: add hard-rebuild plan to plan cache  =          0
     elapsed time: search time for parent PCO  =        451
     elapsed time: creation time for parent PCO  =        279
     elapsed time: search time for child PCO   =          0
     elapsed time: creation time for child PCO  =         34
     elapsed time: validation time for child PCO  =       2247
     elapsed time: creation time for new child PCO by rebuild at execution   =          0
     elapsed time: creation time for new child PCO by rebuild at soft prepare  =          0
     elapsed time: hard prepare time           =      39568
     elapsed time: matching time for child PCO  =        400
     elapsed time: waiting time for hard prepare  =          0
     elapsed time: moving time from cold region to hot region.  =          0
     elapsed time: waiting time for parent PCO  when choosing plan cache replacement victim.  =          0
     elapsed time: privilege checking time during soft prepare.  =        219
     elapsed time: copying logs to replication log buffer (sender side)  =          0
     elapsed time: sender(s) waiting for new logs  =          0
     elapsed time: sender(s) reading logs from replication log buffer  =          0
     elapsed time: sender(s) reading logs from log file(s)  =          0
     elapsed time: sender(s) checking whether logs are useful  =          0
     elapsed time: sender(s) analyzing logs    =          0
     elapsed time: sender(s) sending xlogs to receiver(s)  =          0
     elapsed time: sender(s) receiving ACK from receiver(s)  =          0
     elapsed time: sender(s) setting ACKed value  =          0
     elapsed time: receiver(s) receiving xlogs from sender(s)  =          0
     elapsed time: receiver(s) performing endian conversion  =          0
     elapsed time: receiver(s) beginning transaction(s)  =          0
     elapsed time: receiver(s) committing transaction(s)  =          0
     elapsed time: receiver(s) aborting transaction(s)  =          0
     elapsed time: receiver(s) opening table cursor(s)  =          0
     elapsed time: receiver(s) closing table cursor(s)  =          0
     elapsed time: receiver(s) inserting rows  =          0
     elapsed time: receiver(s) updating rows   =          0
     elapsed time: receiver(s) deleting rows   =          0
     elapsed time: receiver(s) opening lob cursor(s)  =          0
     elapsed time: receiver(s) preparing to write LOB(s)  =          0
     elapsed time: receiver(s) writing LOB piece(s)  =          0
     elapsed time: receiver(s) finish writing LOBs  =          0
     elapsed time: receiver(s) closing LOB cursor(s)  =          0
     elapsed time: receiver(s) comparing images to check for conflicts  =          0
     elapsed time: receiver(s) sending ACK     =          0
     elapsed time: receiver(s) trim LOB(s)     =          0
     elapsed time: task schedule               =          0
     max     time: task schedule               =          0
```

- When QUERY_PROF_FLAG = 63 is set (i.e., QUERY_PROF_FLAG = 1 + 2 + 4 + 8 + 16 + 32): It outputs the memory usage by each Altibase module at that point in time. The output is equivalent to the result of executing: SELECT * FROM v$memstat ORDER BY seqnum;

**Output format**

[MEMORY STAT] recording time

Module name: (Current amount of memory used / number of unit memory / maximum amount of memory used)

**Example**

```
[MEMORY STAT] 2025/07/16 10:25:59
   Main_Module_DirectAttach : (0/ 0/ 0)
   Main_Module_Channel : (0/ 0/ 0)
   Main_Module_CDBC_MAIN : (0/ 0/ 0)
   Main_Module_CDBC_QP : (0/ 0/ 0)
   Main_Module_CDBC_STATE_MEMPOOL : (0/ 0/ 0)
   Main_Module_CDBC_CURSORDATA_MEMPOOL : (0/ 0/ 0)
   Main_Module_CDBC_CONDITIONBUF_MEMPOOL : (0/ 0/ 0)
   Main_Module_Distributed : (0/ 0/ 0)
   Main_Module_Thread : (0/ 0/ 0)
   Main_Module_Queue : (0/ 0/ 0)
   Main_Module_Utility : (0/ 0/ 0)
   SQL_Plan_Cache_Control : (0/ 0/ 0)
   GIS_DataType : (0/ 0/ 0)
   GIS_Disk_Index : (0/ 0/ 0)
   GIS_Function : (0/ 0/ 0)
   GIS_TEMP_MEMORY : (0/ 0/ 0)
   Query_Common : (0/ 0/ 0)
   Query_Meta : (0/ 0/ 0)
   Query_DML : (0/ 0/ 0)
   Query_Sequence : (0/ 0/ 0)
   Query_PSM_Concurrent_Execute : (0/ 0/ 0)
   Replication_Common : (0/ 0/ 0)
   Replication_Control : (0/ 0/ 0)
   Replication_Data : (0/ 0/ 0)
   Replication_Met : (0/ 0/ 0)
   Replication_Network : (0/ 0/ 0)
   Replication_Recovery : (0/ 0/ 0)
   Replication_Storage : (0/ 0/ 0)
   Replication_Executor : (0/ 0/ 0)
   Replication_Sender : (0/ 0/ 0)
   Replication_Receiver : (0/ 0/ 0)
   Replication_Sync : (0/ 0/ 0)
   Replication_Module_Property : (0/ 0/ 0)
   Query_PSM_Node : (0/ 0/ 0)
   Query_PSM_Execute : (0/ 0/ 0)
   Query_Prepare : (0/ 0/ 0)
   Query_PSM_Varray : (0/ 0/ 0)
   Query_Execute : (0/ 0/ 0)
   Query_Binding : (0/ 0/ 0)
   Query_Transaction : (0/ 0/ 0)
   Query_Conversion : (0/ 0/ 0)
   Query_Execute_Cache : (0/ 0/ 0)
   Query_Result_Cache : (0/ 0/ 0)
   Query_PSM_Internal_Execute : (0/ 0/ 0)
   Mathematics : (0/ 0/ 0)
   Storage_Disk_Buffer : (0/ 0/ 0)
   Storage_Disk_Collection : (0/ 0/ 0)
   Storage_Disk_Datafile : (0/ 0/ 0)
   Storage_Disk_SecondaryBuffer : (0/ 0/ 0)
   Storage_Tablespace : (0/ 0/ 0)
   Storage_DataPort : (0/ 0/ 0)
   Storage_Disk_Index : (0/ 0/ 0)
   Storage_Disk_Page : (0/ 0/ 0)
   Storage_Disk_Recovery : (0/ 0/ 0)
   Storage_Global_Memory_Manager : (0/ 0/ 0)
   Storage_Memory_Ager : (0/ 0/ 0)
   Storage_Memory_Logical_Ager : (0/ 0/ 0)
   Storage_Memory_Collection : (0/ 0/ 0)
   Storage_Memory_Interface : (0/ 0/ 0)
   Storage_Memory_Locking : (0/ 0/ 0)
   Storage_Memory_Manager : (0/ 0/ 0)
   Storage_Memory_Index : (0/ 0/ 0)
   Fixed_Table : (0/ 0/ 0)
   Storage_Memory_Page : (0/ 0/ 0)
   Storage_Memory_Recovery : (0/ 0/ 0)
   Storage_Memory_Recovery_Chkpt_Thread : (0/ 0/ 0)
   Storage_Memory_Recovery_LFG_Thread : (0/ 0/ 0)
   Storage_Memory_Recovery_Archive_Thread : (0/ 0/ 0)
   Storage_Memory_Utility : (0/ 0/ 0)
   Storage_Memory_Transaction : (0/ 0/ 0)
   Volatile_Log_Buffer : (0/ 0/ 0)
   Volatile_Memory_Manager : (0/ 0/ 0)
   Volatile_Memory_Page : (0/ 0/ 0)
   Temp_Memory : (0/ 0/ 0)
   Transaction_Table : (0/ 0/ 0)
   Legacy_Transaction_Manager : (0/ 0/ 0)
   Transaction_OID_List : (0/ 0/ 0)
   Transaction_Private_Buffer : (0/ 0/ 0)
   Transaction_Segment_Table : (0/ 0/ 0)
   Transaction_DiskPage_Touched_List : (0/ 0/ 0)
   Transaction_Table_Info : (0/ 0/ 0)
   Index_Memory : (0/ 0/ 0)
   LOG_Memory : (0/ 0/ 0)
   InMemoryRecovery_Memory : (0/ 0/ 0)
   CatalogCache_Memory : (0/ 0/ 0)
   OS_Independent : (0/ 0/ 0)
   Utility_Module : (0/ 0/ 0)
   Async_IO_Manager : (0/ 0/ 0)
   Mutex : (0/ 0/ 0)
   Clock_Manager : (0/ 0/ 0)
   Timer_Manager : (0/ 0/ 0)
   Profile_Manager : (0/ 0/ 0)
   Socket_Manager : (0/ 0/ 0)
   External_Procedure : (0/ 0/ 0)
   External_Procedure_Agent : (0/ 0/ 0)
   Audit_Manager : (0/ 0/ 0)
   Altiwrap : (0/ 0/ 0)
   Process_ThreadInfo : (0/ 0/ 0)
   CM_Buffer : (0/ 0/ 0)
   CM_NetworkInterface : (0/ 0/ 0)
   CM_Multiplexing : (0/ 0/ 0)
   CM_DataType : (0/ 0/ 0)
   CM_Interface : (0/ 0/ 0)
   Database_Link : (0/ 0/ 0)
   Dynamic Module Loader : (0/ 0/ 0)
   Tablespace_Free_Extent_Pool : (0/ 0/ 0)
   Condition_Variable : (0/ 0/ 0)
   WATCHDOG : (0/ 0/ 0)
   Latch : (0/ 0/ 0)
   Thread_Stack : (0/ 0/ 0)
   Remote_Call_Server : (0/ 0/ 0)
   Remote_Call_Client : (0/ 0/ 0)
   Query_Common_Remote_Call : (0/ 0/ 0)
   IDU_MEM_OTHER : (0/ 0/ 0)
   MMAP : (0/ 0/ 0)
   SYSTEM : (0/ 0/ 0)
   Shared Meta : (0/ 0/ 0)
   RESERVED : (0/ 0/ 0)
```

- Using the -stat option of altiProfile, you can output statistical information about executed SQL statements.
  The -stat option supports two types: query and session.
  This information is useful for identifying SQL statements that may require tuning.
  The session option includes SESSION ID information in addition to the statistics provided by the query option.

- When the -stat option is used, the profiling output is generated in two file formats: .txt and .csv.

When using the query option:

$ altiProfile -stat query *.prof > #sequence.out

When using the session option:

$ altiProfile -stat session *.prof > #sequence.out

**예제**

```
$ altiProfile -stat query alti-1752630730-0.prof
### Processing [alti-1752630730-0.prof]...
100% [====================]
### Writing CSV File [alti-prof-stat-1752631027.csv]...
### Writing TEXT File [alti-prof-stat-1752631027.txt]...
### Successfully done.
$ ls -la  ==> Statistical Information Output Files
-rw-rw-rw- 1 alti0 alti0     747 Jul 16 10:57 alti-prof-stat-1752631027.csv
-rw-rw-rw- 1 alti0 alti0    1241 Jul 16 10:57 alti-prof-stat-1752631027.txt
$ cat alti-prof-stat-1752631027.txt
  COUNT      AVG          TOTAL         MIN         MAX    SUCCESS  FAIL   QUERY
===========================================================================================================
     4     3.959910    15.839640     0.002116     7.665345     4     0    EXEC PROC1(3001, '01046585724', 1)
     7     2.262010    15.834073     0.000159     7.663861     7     0    UPDATE EMPLOYEES SET DNO = ?, EMP_TEL = ? WHERE ENO = ?
     9     0.620658     5.585918     0.000081     5.584472     9     0    UPDATE EMPLOYEES SET DNO = :v1, EMP_TEL = :v2 WHERE ENO = :v3
    10     0.000352     0.003520     0.000088     0.002201    10     0    select * from SYS.CUSTOMERS
     8     0.000364     0.002911     0.000149     0.001264     8     0    commit
     1     0.002279     0.002279     0.002279     0.002279     1     0    ALTER SYSTEM SET QUERY_PROF_FLAG = 7
    12     0.000153     0.001840     0.000072     0.000454    12     0    select * from SYS.DEPARTMENTS
     6     0.000249     0.001492     0.000059     0.000880     6     0    select * from ALTITEST.ORDERS
===========================================================================================================
[TOTAL] Count(Query): 57  Avg(Time): 0.653889  Sum(Time): 37.2717

$ altiProfile -stat session alti-1752630730-0.prof
### Processing [alti-1752630730-0.prof]...
100% [====================]
### Writing CSV File [alti-prof-stat-1752631158.csv]...
### Writing TEXT File [alti-prof-stat-1752631158.txt]...
### Successfully done.
$ ls -la
-rw-rw-rw- 1 alti0 alti0    2319 Jul 16 10:59 alti-prof-stat-1752631158.txt
-rw-rw-rw- 1 alti0 alti0    1393 Jul 16 10:59 alti-prof-stat-1752631158.csv
$ cat alti-prof-stat-1752631158.txt
SESSION    COUNT      AVG          TOTAL         MIN         MAX    SUCCESS  FAIL   QUERY
===========================================================================================================
     1       5     1.117055     5.585273     0.000166     5.584472     5     0    UPDATE EMPLOYEES SET DNO = :v1, EMP_TEL = :v2 WHERE ENO = :v3
     1       2     2.114851     4.229702     0.002116     4.227586     2     0    EXEC PROC1(3001, '01046585724', 1)
     1       3     1.408920     4.226760     0.000335     4.225859     3     0    UPDATE EMPLOYEES SET DNO = ?, EMP_TEL = ? WHERE ENO = ?
     1       5     0.000562     0.002812     0.000112     0.002201     5     0    select * from SYS.CUSTOMERS
     1       1     0.002279     0.002279     0.002279     0.002279     1     0    ALTER SYSTEM SET QUERY_PROF_FLAG = 7
     1       6     0.000367     0.002201     0.000149     0.001264     6     0    commit
     1       4     0.000332     0.001328     0.000115     0.000880     4     0    select * from ALTITEST.ORDERS
     1       6     0.000175     0.001049     0.000082     0.000454     6     0    select * from SYS.DEPARTMENTS
===========================================================================================================
[SUB-TOTAL] Count(Query): 32  Avg(Time): 0.439106  Sum(Time): 14.0514
     2       2     5.804969    11.609938     3.944593     7.665345     2     0    EXEC PROC1(3001, '01046585724', 1)
     2       4     2.901828    11.607313     0.000159     7.663861     4     0    UPDATE EMPLOYEES SET DNO = ?, EMP_TEL = ? WHERE ENO = ?
     2       6     0.000132     0.000791     0.000072     0.000229     6     0    select * from SYS.DEPARTMENTS
     2       2     0.000355     0.000710     0.000261     0.000449     2     0    commit
     2       5     0.000142     0.000708     0.000088     0.000186     5     0    select * from SYS.CUSTOMERS
     2       4     0.000161     0.000645     0.000081     0.000305     4     0    UPDATE EMPLOYEES SET DNO = :v1, EMP_TEL = :v2 WHERE ENO = :v3
     2       2     0.000082     0.000164     0.000059     0.000105     2     0    select * from ALTITEST.ORDERS
===========================================================================================================
[SUB-TOTAL] Count(Query): 25  Avg(Time): 0.928811  Sum(Time): 23.2203
```

# Precautions

---

When profiling is enabled, execution information for all SQL statements executed in the Altibase server is recorded in the log file, and the Altibase status is profiled every 3 seconds according to the setting, which can affect Altibase performance as well as the load on the system.

In addition, there is a possibility that a disk pool may occur due to high disk usage due to log recording by profiling.

Therefore, it is not recommended to enable profiling on operation servers by default.

It is recommended to use it for a short time during testing, performance analysis, and tuning. When profiling, be sure to monitor the disk usage together and stop it appropriately.
