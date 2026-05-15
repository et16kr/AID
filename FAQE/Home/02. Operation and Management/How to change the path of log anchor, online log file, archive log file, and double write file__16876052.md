---
title: "How to change the path of log anchor, online log file, archive log file, and double write file"
page_id: "16876052"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/How+to+change+the+path+of+log+anchor%2C+online+log+file%2C+archive+log+file%2C+and+double+write+file"
updated_at: "2021-04-02T17:30:05.000+0900"
version: 3
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# How to change the path of log anchor, online log file, archive log file, and double write file
Source: https://docs.altibase.com/display/FAQE/How+to+change+the+path+of+log+anchor%2C+online+log+file%2C+archive+log+file%2C+and+double+write+file
Updated: 2021-04-02T17:30:05.000+0900

- [Overview](#Howtochangethepathofloganchor,onlinelogfile,archivelogfile,anddoublewritefile-Overview) - [Summary of change procedure](#Howtochangethepathofloganchor,onlinelogfile,archivelogfile,anddoublewritefile-Summaryofchangeprocedure) - [Detailed procedure](#Howtochangethepathofloganchor,onlinelogfile,archivelogfile,anddoublewritefile-Detailedprocedure) - [1. Check the current path setting](#Howtochangethepathofloganchor,onlinelogfile,archivelogfile,anddoublewritefile-1.Checkthecurrentpathsetting1.CurrPath) - [2. Stop the Altibase server](#Howtochangethepathofloganchor,onlinelogfile,archivelogfile,anddoublewritefile-2.StoptheAltibaseserver) - [3. Copy the files and change properties](#Howtochangethepathofloganchor,onlinelogfile,archivelogfile,anddoublewritefile-3.Copythefilesandchangeproperties) - [Log anchor](#Howtochangethepathofloganchor,onlinelogfile,archivelogfile,anddoublewritefile-Loganchor) - [Online log file](#Howtochangethepathofloganchor,onlinelogfile,archivelogfile,anddoublewritefile-Onlinelogfile) - [Archive log file](#Howtochangethepathofloganchor,onlinelogfile,archivelogfile,anddoublewritefile-Archivelogfile) - [Double Write file](#Howtochangethepathofloganchor,onlinelogfile,archivelogfile,anddoublewritefile-DoubleWritefile) - [File type properties and file name format table](#Howtochangethepathofloganchor,onlinelogfile,archivelogfile,anddoublewritefile-Filetypepropertiesandfilenameformattable) - [3. Start the Altibase server](#Howtochangethepathofloganchor,onlinelogfile,archivelogfile,anddoublewritefile-3.StarttheAltibaseserver) - [4. Check the change path](#Howtochangethepathofloganchor,onlinelogfile,archivelogfile,anddoublewritefile-4.Checkthechangepath) - [Reference](#Howtochangethepathofloganchor,onlinelogfile,archivelogfile,anddoublewritefile-Reference)

# Overview

---

This section describes how to change the path of log anchor, online log file, archive log file, and double write file.

In order to change the paths of these files, the Altibase server must be restarted, so be sure to perform it after securing service downtime.

# Summary of change procedure

---

1. Check the current path setting.
2. Stop the Altibase server.
3. Copy files and change properties.
4. Start the Altibase server.
5. Check the change path.

# Detailed procedure

---

## 1. Check the current path setting

---

Refer to the sentence below to check the current path of each property and make a note of it.

```
iSQL> SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME IN ('LOGANCHOR_DIR', 'LOG_DIR', 'DOUBLE_WRITE_DIRECTORY', 'ARCHIVE_DIR');

Example)
iSQL(sysdba)> set linesize 1024
iSQL(sysdba)> set colsize 60
iSQL(sysdba)> SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME IN ('LOGANCHOR_DIR', 'LOG_DIR', 'DOUBLE_WRITE_DIRECTORY', 'ARCHIVE_DIR');
NAME                                                          VALUE1
-------------------------------------------------------------------------------------------------------------------------------
LOG_DIR                                                       /data/eheejung/65166/logs         # Online log file path
LOGANCHOR_DIR                                                 /data/eheejung/65166/logs         # Log anchor file path
ARCHIVE_DIR                                                   /data/eheejung/65166/arch_logs    # Archive log file path
DOUBLE_WRITE_DIRECTORY                                        /data/eheejung/65166/dbs          # Double Write file path
4 rows selected.
```

## 2. Stop the Altibase server

---

Stop the Altibase server.

```
$ server stop
```

## 3. Copy the files and change properties

---

Copy the file which path you want to change to the new path and change the properties of each.

- ### Log anchor

  There are three log anchor files: loganchor0, loganchor1, and loganchor2.
  Copy all three files from the path located in the LOGANCHOR_DIR property to the new path.
  Find the LOGANCHOR_DIR property in the $ALTIBASE_HOME/conf/altibase.properties file and change it to a new path.
- ### Online log file

  The online log file name format is `logfile#`. Copy all files starting with `logfile` from the path located in the `LOG_DIR` property to the new path.

  Find the `LOG_DIR` property in the `$ALTIBASE_HOME/conf/altibase.properties` file and change it to a new path.
- ### Archive log file

  The archive log file name format is `logfile#`. Copy all files starting with `logfile` from the path located in the `ARCHIVE_DIR` property to the new path.
  Find the `ARCHIVE_DIR` property in the `$ALTIBASE_HOME/conf/altibase.properties` file and change it to a new path.
- ### Double Write file

  The Double Write file name format is `*.dwf`. Copy all files ending in `*.dwf` from the path located in the `DOUBLE_WRITE_DIRECTORY` property to the new path.
  Find the `DOUBLE_WRITE_DIRECTORY` property in the `$ALTIBASE_HOME/conf/altibase.properties` file and change it to a new path.
- ### File type properties and file name format table

  | File type | Property | File name format |
  | --- | --- | --- |
  | Log anchor | LOGANCHOR_DIR | loganchor0<br>loganchor1<br>loganchor2 |
  | Online log file | LOG_DIR | logfile*#* |
  | Archive log file | ARCHIVE_DIR | logfile*#* |
  | Double Write file | DOUBLE_WRITE_DIRECTORY | *.dwf |

## 3. Start the Altibase server

---

Start the Altibase server.

```
$ server start
```

## 4. Check the change path

---

1. Check the change path with the SQL statement executed in Check the current path settings.

```
SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME IN ('LOGANCHOR_DIR', 'LOG_DIR', 'DOUBLE_WRITE_DIRECTORY', 'ARCHIVE_DIR');
```

# Reference

---

- [How to change the tablespace data file path](https://aid.altibase.com/display/FAQE/How+to+change+the+tablespace+data+file+path)
