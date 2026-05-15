---
title: "Data download using iloader"
page_id: "16876147"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Data+download+using+iloader"
updated_at: "2021-04-05T09:39:28.000+0900"
version: 2
ancestors: ["Home", "04. Backup and Recovery", "Using aexport and iloader"]
labels: []
---

# Data download using iloader
Source: https://docs.altibase.com/display/FAQE/Data+download+using+iloader
Updated: 2021-04-05T09:39:28.000+0900

- [Preparation for iloader](#Datadownloadusingiloader-Preparationforiloader) - [Performing backup](#Datadownloadusingiloader-Performingbackup) - [Download data for all tables in the database](#Datadownloadusingiloader-Downloaddataforalltablesinthedatabase) - [Downloading data of a table belonging to a specific user](#Datadownloadusingiloader-Downloadingdataofatablebelongingtoaspecificuser) - [Downloading data for a specific table](#Datadownloadusingiloader-Downloadingdataforaspecifictable) - [Check the data download result](#Datadownloadusingiloader-Checkthedatadownloadresult) - [Check the run_il_out.sh execution log](#Datadownloadusingiloader-Checktherun_il_out.shexecutionlog) - [Check log by table](#Datadownloadusingiloader-Checklogbytable) - [Data download file](#Datadownloadusingiloader-Datadownloadfile)

# Preparation for iloader

---

Before executing the iloader, be sure to check the following environment variables before proceeding.

ALTIBASE_NLS_USE is required to prevent the breakdown of Korean data, and ILO_DATEFORM should be set to prevent duplication when a date type column has a unique value.

- ALTIBASE_NLS_USE
- ILO_DATEFORM

In the session of executing the iloader, it is applied by setting it with the export command as shown below or adding it to the user environment configuration file (.bash_profile or .profile) and logging out and logging in.

**How to set environment variables**

**How to set environment variables**

```
$ export ALTIBASE_NLS_USE= Database server character set
$ export ILO_DATEFORM='YYYY/MM/DD HH:MI:SS.SSSSSS'
```

**How to set environment variables**

```
$ echo $ALTIBASE_NLS_USE
$ echo $ILO_DATEFORM
```

The ALTIBASE HDB server character set can be checked with the following sentence: NLS_CHARACTERSET is the ALTIBASE server's character set and NLS_USE is the client's character set. Hangul data is not broken only when these two are set identically.

Error rendering macro 'code': Invalid value specified for parameter 'firstline'

```
iSQL> set linesize 1024;
iSQL> set colsize 20;
iSQL> select NLS_USE, NLS_CHARACTERSET from v$nls_parameters;
NLS_USE               NLS_CHARACTERSET
-----------------------------------------------
MS949                 MS949
1 row selected.
```

# Performing backup

---

Use run_il_out.sh to backup table data.

```
$ ls --l run_il_out.sh
rw-rw-rw 1 eheejung eheejung 633 Nov 1 11:00 run_il_out.sh
```

## Download data for all tables in the database

run_il_out.sh must be a file created after entering UserID as sys when executing aexport. Run run_il_out.sh.

**Example**

```
$ sh run_il_out.sh | tee download.out                   # If done in the foreground, closing the terminal window will terminate the execution.
or
$ nohup sh run_il_out.sh &                              # If you do it in the background, closing the terminal window does not terminate the execution.
$ mv nohup.out download.out                             # You can connect again and check the progress with the download.out file.
```

## Downloading data of a table belonging to a specific user

In order to back up only tables owned by a specific user, use run_il_out.sh that aexport-ed to that user.

```
$ aexport
-----------------------------------------------------------------
     Altibase Export Script Utility.
     Release Version 6.3.1.2.7
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
Write Server Name (default:localhost) :
Write UserID : altitest
Write Password :
...Omitted...

$ cat run_il_out.sh
iloader -s localhost -u ALTITEST -p ALTITEST formout -f ALTITEST_ORDERS.fmt -T ORDERS

iloader -s localhost -u ALTITEST -p ALTITEST out -f ALTITEST_ORDERS.fmt -d ALTITEST_ORDERS.dat -log ALTITEST_ORDERS.log
```

If aexport is executed by sys, it can extract only the user from run_il_out.sh and execute it.

**Ex) When the user name is altitest**

```
$ grep "\-f ALTITEST_" run_il_out.sh > altitest_il_out.sh    # Extract only the iloader command corresponding to the altitest user from run_il_out.sh and saves it in another file.

$ sh altitest_il_out.sh | tee download.out                   # If done in the foreground, closing the terminal window will terminate the execution.
or
$ nohup sh altitest_il_out.sh &                              # If you do it in the background, closing the terminal window does not terminate the execution.
$ mv nohup.out download.out                                  # It can connect again and check the progress with the download.out file.
```

## Downloading data for a specific table

In order to download only specific tables, extract only the tables you want from run_il_out.sh and back them up.

**Ex) Extracting the SYS user's ORDERS tables**

```
$ grep 'SYS_ORDERS.fmt' run_il_out.sh
iloader -s localhost -u SYS -p MANAGER formout -f SYS_ORDERS.fmt -T ORDERS
iloader -s localhost -u SYS -p MANAGER out -f SYS_ORDERS.fmt -d SYS_ORDERS.dat -log SYS_ORDERS.log
```

Execute iloader formout and iloader out commands in sequence.

**Ex) Backup of the SYS user's ORDERS table**

```
[heejung.lee@63127 /data/heejung.lee/work/631_aexport]$iloader -s localhost -u SYS -p MANAGER formout -f SYS_ORDERS.fmt -T ORDERS            # Create iloader form file
-----------------------------------------------------------------
     Altibase Data Load/Download utility.
     Release Version 6.3.1.2.7
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
ISQL_CONNECTION : TCP
[heejung.lee@63127 /data/heejung.lee/work/631_aexport]$
[heejung.lee@63127 /data/heejung.lee/work/631_aexport]$ls -l SYS_ORDERS.fmt                                                                   # Check whether iloader form file is created
-rw-rw-rw- 1 heejung.lee heejung.lee 210 2014-11-19 15:28 SYS_ORDERS.fmt
[heejung.lee@63127 /data/heejung.lee/work/631_aexport]$
[heejung.lee@63127 /data/heejung.lee/work/631_aexport]$iloader -s localhost -u SYS -p MANAGER out -f SYS_ORDERS.fmt -d SYS_ORDERS.dat -log SYS_ORDERS.log        # Perform data download
-----------------------------------------------------------------
     Altibase Data Load/Download utility.
     Release Version 6.3.1.2.7
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
ISQL_CONNECTION : TCP
DATE FORMAT : YYYY/MM/DD HH:MI:SS:SSSSSS
DATA_NLS_USE: MS949

     Total 30 record download(ORDERS)

     DOWNLOAD : 2.3150 msec
```

If there are many tables or a lot of data, monitor download.out to see if it is shutting down.

**Data download performance log monitoring**

```
$ tail -f download.d.out
```

## Check the data download result

### Check the run_il_out.sh execution log

The run_il_out.sh run log is the file specified in the tee command.

```
$ sh run_il_out.sh | tee download.out
```

Check whether an error has occurred in the specified file as follows.

```
$ grep –i err- download.out
[ERR-311F4 : Invalid column name                  # If something starts with ERR- like this, it means that an error has occurred.
                                                  # Actions are required according to the situation, so if it is difficult to take action directly after checking the error, contact us.
```

### Check log by table

When run_il_out.sh is executed, log files in the form of DBUSER_TABLENAME.log are created. (Eg, ALTITEST_ORDERS.log in the altitest user's orders table) In these files, check for errors with the command below.

```
$ cat run_il_out.sh | grep fmt | wc -l                                            # Check the number of tables in the database
106

$ ls -l *.fmt | wc -l                                                             # Check the number of tables to be backed up by the number of *.fmt files.
106

$ cat *.log | grep 'Error Row Count' |  awk -F: '{print $2}' | wc -l              # If the number of Error Row Count occurrences is different from the number of .fmt files, it means that an error occurred in a specific table by the number of differences.
106                                                                               # Open the run_il_out.sh execution log (download.out) and search by table name to check.
```

```
 $ cat *.log | grep 'Error Row Count' |  awk -F: '{print $2}' | sort -u            # If the result is only 0, there is no download failure in DBUSER_TABLENAME.log.
0                                                                                 # If there is a non-zero result, the user need to look for that table and find the cause with the .log and .bad files.
```

### Data download file

The backup file created by running run_il_out.sh is created in USERNAME_TABLENAME.dat format.

```
$ ls -l *.dat
-rw-rw-rw- 1 heejung.lee heejung.lee 12457 2014-11-19 15:03 ALTITEST_ORDERS.dat

$ ls -l *.dat | wc -l                                                             # Tthe backup result can be checked once again by comparing the number of backup files with the number of tables.

$ ls -l ALTITEST_ORDERS*                                                          # .Dat, .fmt, .log files are created for each table.
-rw-rw-rw- 1 heejung.lee heejung.lee   0 2014-11-19 15:03 ALTITEST_ORDERS.dat
-rw-rw-rw- 1 heejung.lee heejung.lee 210 2014-11-19 15:03 ALTITEST_ORDERS.fmt
-rw-rw-rw- 1 heejung.lee heejung.lee 169 2014-11-19 15:03 ALTITEST_ORDERS.log
```
