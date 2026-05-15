---
title: "Monitoring Tools for Windows"
page_id: "16876220"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Monitoring+Tools+for+Windows"
updated_at: "2021-04-05T10:01:27.000+0900"
version: 4
ancestors: ["Home", "08. Monitoring"]
labels: []
---

# Monitoring Tools for Windows
Source: https://docs.altibase.com/display/FAQE/Monitoring+Tools+for+Windows
Updated: 2021-04-05T10:01:27.000+0900

- [Overview](#MonitoringToolsforWindows-Overview) - [Version](#MonitoringToolsforWindows-Version) - [Monitoring batch program](#MonitoringToolsforWindows-Monitoringbatchprogram) - [Settings](#MonitoringToolsforWindows-Settings) - [Checking connection information](#MonitoringToolsforWindows-Checkingconnectioninformation) - [Adding monitoring items](#MonitoringToolsforWindows-Addingmonitoringitems) - [Monitoring cycle](#MonitoringToolsforWindows-Monitoringcycle) - [Deleting old log function](#MonitoringToolsforWindows-Deletingoldlogfunction) - [Modifying altimon.vbs file](#MonitoringToolsforWindows-Modifyingaltimon.vbsfile) - [Execution](#MonitoringToolsforWindows-Execution) - [How to run in the foreground](#MonitoringToolsforWindows-Howtorunintheforeground) - [How to execute in background](#MonitoringToolsforWindows-Howtoexecuteinbackground) - [Termination](#MonitoringToolsforWindows-Termination) - [When executing in the foreground](#MonitoringToolsforWindows-Whenexecutingintheforeground) - [When executing in the background](#MonitoringToolsforWindows-Whenexecutinginthebackground) - [Log](#MonitoringToolsforWindows-Log)

# Overview

---

This document describes a monitoring tool for Windows.

# Version

---

- This document is written based on Altibase HDB version 6.3.1
- Both ALTIBASE HDB 5 and ALTIBASE HDB 6 can be used, but some monitoring items may cause a result error.
- If needed, please leave a request at [http://support.altibase.com/en/](http://support.altibase.com/en/) or in a comment section on this page.

# Monitoring batch program

---

Download the compressed file below, place it in a folder, and extract it.

- [altimon_for_windows.zip](https://docs.altibase.com/download/attachments/7340488/altimon_for_windows.zip?version=1&modificationDate=1415946725000&api=v2)

Once it is unzipped, the user will find two folders and two files.

- [altimon.bat](https://docs.altibase.com/download/attachments/7340488/altimon.bat?version=1&modificationDate=1415946725000&api=v2) : Batch program for monitoring
- [altimon.vbs](https://docs.altibase.com/download/attachments/7340488/altimon.vbs?version=1&modificationDate=1415946725000&api=v2) : VB file to run batch program in background
- ALTIMON_SCRIPT folder: There are .sql files containing monitoring queries
- ALTIMON_LOG folder: Save log files

# Settings

---

## Checking connection information

Change the ALTIBASE HDB server connection command in the altimon.bat file to suit your environment.

```
set ISQL="%ALTIBASE_HOME%\bin\isql.exe" -s localhost -u sys -p manager -silent
```

## Adding monitoring items

---

If there are items that the user wants to add other than the basic monitoring items, add a monitoring query to the all.sql file in the ALTIMON_SCRIPT folder.

In the monitoring query, put sysdate in the first column of the SELECT clause and an identifier starting with _MON_ in the second column.

**Example of monitoring query**

```
SELECT TO_CHAR(SYSDATE, 'HH:MI:SS') TIME, '_MON_REP_GAP'
     , REP_NAME
     , REP_SN
     , REP_GAP
  FROM V$REPGAP
 ORDER BY REP_NAME, REP_GAP;
```

## Monitoring cycle

At the end of altimon.bat, change the number after -n in the command below. This number refers to the monitoring cycle.

Modify to suit the environment in seconds.

```
ping -n 60 127.0.0.1 > nul
```

Ex) When set to 5 minutes, -n 60 to -n 300

## Deleting old log function

At the bottom of the altimon.bat file are commands that start with forfiles.

In this command, the /D -30 option means to delete the log 30 days ago, so change the number after the /D option.

```
forfiles /P . /M mon.log* /D -30 /C "cmd /c del @file"
```

## Modifying altimon.vbs file

After downloading the above files, upload them to a folder on the server to be monitored.

Then, modify the path of the second line in the altimon.vbs file to suit your environment.

```
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "C:\Users\Altibase\Desktop\altimon.bat" & Chr(34), 0
Set WshShell = Nothing
```

# Execution

---

## How to run in the foreground

Execute Windows Command Prompt (Execution Window). Go to the folder where the altimon.bat file is located and run the batch program.

**To execute it in a new window**

```
C:\Users\Altibase>start altimon.bat
or
C:\Users\Altibase>start altimon
```

**To execute it in the current window**

```
C:\Users\Altibase>altimon.bat
or
C:\Users\Altibase>altimon
```

The user can also go to the folder where the batch program (altimon.bat) is located in Windows Explorer and double-click the alti_mon.bat file.

If executing the batch program in the foreground, a notification message appears in the execution window as shown below.

![altimon_for_windows.jpeg](https://docs.altibase.com/download/attachments/embedded-page/FAQE/Monitoring%20Tools%20for%20Windows/altimon_for_windows.jpeg?api=v2)

The batch program executed in the foreground is terminated when the open window is closed.

## How to execute in background

Put the attached files in the same folder, open a DOS window, move to the folder, and execute the command below.

```
C> alti_mon.vbs
```

```
C:\Users\Altibase\Desktop>alti_mon.vbs
Microsoft (R) Windows Script Host version 5.8
Copyright (C) Microsoft Corporation 1996-2001. All rights reserved.
```

A batch program executing in the background does not terminate the batch program even if you close an open window. To terminate, you need to use the taskkill command. Refer to the end.

# Termination

---

## When executing in the foreground

Close the execution window where you executed the batch program (altimon.bat) or press Ctrl+c.

## When executing in the background

Execute the Windows command prompt (execution window) and execute the command below.

```
C> taskkill /fi "windowtitle eq ALTIMON FOR WINDOWS"
```

**Example**

```
C:\Users\Altibase\Desktop>taskkill /fi "windowtitle eq ALTIMON FOR WINDOWS"
Success: A shutdown signal was sent to the process (PID 8216).
```

# Log

When executing the batch program, a log file in the form of mon.log.YYYY-MM-DD is created under the ALTIMON_LOG folder.
