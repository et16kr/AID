---
title: "Create database object and upload data"
page_id: "16876145"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Create+database+object+and+upload+data"
updated_at: "2021-04-05T09:41:14.000+0900"
version: 2
ancestors: ["Home", "04. Backup and Recovery", "Using aexport and iloader"]
labels: []
---

# Create database object and upload data
Source: https://docs.altibase.com/display/FAQE/Create+database+object+and+upload+data
Updated: 2021-04-05T09:41:14.000+0900

- [Database object and data upload procedure](#Createdatabaseobjectanduploaddata-Databaseobjectanddatauploadprocedure) - [Preparation before uploading data](#Createdatabaseobjectanduploaddata-Preparationbeforeuploadingdata) - [Creating database object](#Createdatabaseobjectanduploaddata-Creatingdatabaseobject) - [Uploading data](#Createdatabaseobjectanduploaddata-Uploadingdata) - [Checking the data upload result](#Createdatabaseobjectanduploaddata-Checkingthedatauploadresult) - [Checking the .sh running log](#Createdatabaseobjectanduploaddata-Checkingthe.shrunninglog) - [Checking log files for each table](#Createdatabaseobjectanduploaddata-Checkinglogfilesforeachtable)

# Database object and data upload procedure

---

In order to restore all database objects and data, execute the following .sh files created when aexport is executed in order.

Execute steps 2 through 8 in order.

```
1. run_il_out.sh            : [faq: iloader formout, data-out script ]         # This is a script for backing up data, so it is excluded from this step.
2. run_is.sh                : [faq: isql table-schema script ]
3. run_il_in.sh             : [faq: iloader data-in script ]
4. run_is_refresh_mview.sh  : [faq: isql materialized view refresh script ]
5. run_is_index.sh          : [faq: isql table-index script ]
6. run_is_fk.sh             : [faq: isql table-foreign key script ]
7. run_is_repl.sh           : [faq: isql replication script ]
8. run_is_job.sh            : [faq: isql job script ]
```

Each file contains `isql` commands that execute `.sql` files containing object creation statements.

```
$ cat run_is.sh
isql -s localhost -u SYS -p MANAGER -f ALL_CRT_TBS.sql
isql -s localhost -u SYS -p MANAGER -f ALL_CRT_USER.sql
isql -s localhost -u SYS -p MANAGER -f ALL_CRT_SYN.sql
isql -s localhost -u SYS -p MANAGER -f ALL_CRT_DIR.sql
isql -s localhost -u SYS -p MANAGER -f ALL_CRT_TBL.sql
isql -s localhost -u SYS -p MANAGER -f ALL_CRT_SEQ.sql
isql -s localhost -u SYS -p MANAGER -f ALL_CRT_LIB.sql
isql -s localhost -u SYS -p MANAGER -f ALL_CRT_VIEW_PROC.sql
isql -s localhost -u SYS -p MANAGER -f ALL_CRT_LINK.sql
```

# Preparation before uploading data

---

Before restoring data, be sure to check the following environment variables before proceeding.

`ALTIBASE_NLS_USE` is required to prevent Korean character data from being corrupted, and `ILO_DATEFORM` should be set to prevent duplicate values when a date-type column has unique values.

- ALTIBASE_NLS_USE
- ILO_DATEFORM

In the session where `iloader` is executed, set these variables with the `export` command as shown below. Alternatively, add them to the user environment file (`.bash_profile` or `.profile`) so they remain applied after logout and login.

**How to set environment variables**

```
$ export ALTIBASE_NLS_USE=database_server_character_set
$ export ILO_DATEFORM='YYYY/MM/DD HH:MI:SS.SSSSSS'
```

**How to check environment variables**

```
$ echo $ALTIBASE_NLS_USE
$ echo $ILO_DATEFORM
```

The ALTIBASE HDB server character set can be checked with the following statement. `NLS_CHARACTERSET` is the Altibase server character set, and `NLS_USE` is the client character set. Korean character data is preserved only when these two values are set identically.

**How to check the ALTIBASE server character set-Available from ALTIBASE HDB version 5**

```
iSQL> set linesize 1024;
iSQL> set colsize 20;
iSQL> select NLS_USE, NLS_CHARACTERSET from v$nls_parameters;
NLS_USE               NLS_CHARACTERSET
-----------------------------------------------
MS949                 MS949
1 row selected.
```

# Creating database object

---

When running the .sh file, the user should leave a log file to check for errors.

**Ex) Logging when running .sh**

```
$ sh run_is.sh | tee run_is.log

or

$ nohup sh run_is.sh &
$ mv nohup.out run_is.log
```

# Uploading data

---

Data upload is performed using `run_il_in.sh`. To upload only tables owned by a specific user or only a specific table, extract only the required commands from `run_il_in.sh` as follows.

**Ex) In case of uploading only table owned by ALTITEST user**

```
$ grep "\-f ALTITEST_" run_il_in.sh > altitest_il_in.sh    # Extract only the iloader command corresponding to the altitest user from run_il_in.sh and save it in another file.

$ sh altitest_il_in.sh | tee upload.out                    # If done in the foreground, closing the terminal window will terminate the execution.
Or,
$ nohup sh altitest_il_in.sh &                             # If you do it in the background, closing the terminal window does not terminate the execution.
$ mv nohup.out upload.out                                  # You can connect again and check the progress with the upload.out file.
```

**Ex) In case of uploading the SYS user's ORDERS table**

```
$ grep 'SYS_ORDERS.fmt' run_il_in.sh
iloader -s localhost -u SYS -p MANAGER in -f SYS_ORDERS.fmt -d SYS_ORDERS.dat -log SYS_ORDERS.log -bad SYS_ORDERS.bad
```

If there are many tables or a large amount of data, monitor `upload.out` to check whether the upload has finished.

**Data upload execution log monitoring**

```
$ tail -f upload.out
```

# Checking the data upload result

---

### Checking the .sh running log

Leave a log whenever each `.sh` file is executed, then check the log after execution to confirm whether it completed normally.

**Ex) Checking errors**

```
$ grep -i err- run_is.log
```

### Checking log files for each table

Execute the following commands to check if there is an error when uploading data.

```
$ grep -i err- upload.out                                                 # Check whether an error has occurred in the result of running the run_il_in.sh script.
[ERR-311F4 : Invalid column name                                          # If something starts with ERR- like this, it means that an error has occurred.
$ ls -l *.fmt|wc -l                                                       # Check the number of tables
$ ls -l *.log|wc -l                                                       # Check the number of log files created by running run_il_in.sh

$ cat *.log | grep 'Error Row Count' |  awk -F: '{print $2}' | wc -l      # This count should match both counts above. If it differs, errors occurred for the difference in count.

$ cat *.log | grep 'Error Row Count' |  awk -F: '{print $2}' | sort -u    # If this result is 0, nothing has failed when performing the upload.
0
```
