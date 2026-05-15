---
title: "Altibase Server Patch Procedure on Unix and Linux"
page_id: "16875922"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Altibase+Server+Patch+Procedure+on+Unix+and+Linux"
updated_at: "2021-04-02T10:40:42.000+0900"
version: 9
ancestors: ["Home", "01. Installation, Patch, Upgrade"]
labels: []
---

# Altibase Server Patch Procedure on Unix and Linux
Source: https://docs.altibase.com/display/FAQE/Altibase+Server+Patch+Procedure+on+Unix+and+Linux
Updated: 2021-04-02T10:40:42.000+0900

- [Overview](#AltibaseServerPatchProcedureonUnixandLinux-Overview) - [Preparation before patching](#AltibaseServerPatchProcedureonUnixandLinux-Preparationbeforepatching) - [Patch Procedure](#AltibaseServerPatchProcedureonUnixandLinux-PatchProcedure) - [1. Check the current version](#AltibaseServerPatchProcedureonUnixandLinux-1.Checkthecurrentversion) - [2. Shutdown Altibase Server **](#AltibaseServerPatchProcedureonUnixandLinux-2.ShutdownAltibaseServer**2ndstepforpatch) - [3. Backup existing installation files](#AltibaseServerPatchProcedureonUnixandLinux-3.Backupexistinginstallationfiles3rdstepforpatch) - [4. Upload patch package and change permissions](#AltibaseServerPatchProcedureonUnixandLinux-4.Uploadpatchpackageandchangepermissions) - [ALTIBASE HDB server version 5.5.1 or later (5.5.1, 6.1.1, 6.3.1, and all versions after 6.3.1)](#AltibaseServerPatchProcedureonUnixandLinux-ALTIBASEHDBserverversion5.5.1orlater(allversionssince5.5.1,6.1.1,6.3.1,and6.3.1)) - [ALTIBASE HDB server versions earlier than 5.5.1 (4.3.9, 5.3.3, and all versions through 5.3.3)](#AltibaseServerPatchProcedureonUnixandLinux-ALTIBASEHDBserverversion5.5.1orearlier(allversionsbelow5.3.3suchas4.3.9,5.3.3,etc.)) - [5. Perform the patch](#AltibaseServerPatchProcedureonUnixandLinux-5.Performthepatch) - [ALTIBASE HDB server version 5.5.1 or later (5.5.1, 6.1.1, 6.3.1, and all versions after 6.3.1)](#AltibaseServerPatchProcedureonUnixandLinux-ALTIBASEHDBserverversion5.5.1orlater(allversionssince5.5.1,6.1.1,6.3.1,and6.3.1).1) - [ALTIBASE HDB server versions earlier than 5.5.1 (4.3.9, 5.3.3, and all versions through 5.3.3)](#AltibaseServerPatchProcedureonUnixandLinux-ALTIBASEHDBserverversion5.5.1orearlier(allversionsbelow5.3.3suchas4.3.9,5.3.3,etc.).1) - [6. Check the patch version](#AltibaseServerPatchProcedureonUnixandLinux-6.Checkthepatchversion) - [7. Copy necessary files from the backup file](#AltibaseServerPatchProcedureonUnixandLinux-7.Copynecessaryfilesfromthebackupfile) - [8. STARTUP ALTIBASE HDB Server **](#AltibaseServerPatchProcedureonUnixandLinux-8.STARTUPALTIBASEHDBServer**8thstepforpatch) - [Precautions](#AltibaseServerPatchProcedureonUnixandLinux-Precautions) - [Check meta version before/after patch](#AltibaseServerPatchProcedureonUnixandLinux-Checkmetaversionbefore/afterpatch) - [When patching from ALTIBASE HDB 4.3.9.1 ~ 4.3.9.50 to 4.3.9.51 ~**](#AltibaseServerPatchProcedureonUnixandLinux-WhenpatchingfromALTIBASEHDB4.3.9.1~4.3.9.50to4.3.9.51~**)

# Overview

---

- Patching means **minor version changes**.
  Altibase server version consists of 4 or 5 digits.
  The first three digits refer to the major version and the last one or two digits refer to the minor version.
  Changing only the last one or two digits without changing the first three digits is called a 'patch', and changing the first three digits is called an 'upgrade'.
- This page describes the procedure for patching Altibase servers in Unix and Linux environments.
- Since the Altibase server patch must be performed after the Altibase server is shut down, service downtime is required.
- Therefore, the user must secure downtime before patching.

# Preparation before patching

---

Check the following before proceeding.

- Can Altibase server downtime be secured? (Confirmed with the client)
- Does the meta version change after patching? (Confirm with Altibase engineer)
- Are there any caveats if the patch version is different from the current version? (Confirm with Altibase engineer)
  Example: In order to patch from HDB 4.3.9.44 to Altibase HDB 4.3.9.233.

# Patch Procedure

---

## 1. Check the current version

---

- Make a note of the version check result below.

  **How to check Altibase server version**

  ```
  $ altibase -v
  ```

## 2. Shutdown Altibase Server ******

---

- Shutdown the Altibase server.

  **How to shutdown Altibase server**

  ```
  $ server stop
  ```

  After the shutdown, check the Altibase server process and service port LISTEN status. When the following two commands are executed, there should be no results to indicate a normal shutdown.

  ```
  $ ps -ef | grep 'altibase -p' | grep -v grep           # To check the Altibase server process
  $ netstat -an | grep 20300                             # To check the service port
  ```

## 3. Backup existing installation files

---

- Back up necessary directories so that problems can be recovered after patching.

  **Example of directory backup**

  ```
  $ cd $ALTIBASE_HOME
  $ cp -Rp bin bin.bak
  $ cp -Rp lib lib.bak
  $ cp -Rp msg msg.bak
  $ cp -Rp conf conf.bak
  $ cp -Rp include include.bak
  ```

  If the size of the $ALTIBASE_HOME directory is not large, the user can make a full backup of the $ALTIBASE_HOME directory as shown below.

  ```
  $ cp -Rp altibase_home altibase_home.bak
  ```

## 4. Upload patch package and change permissions

---

### ALTIBASE HDB server version 5.5.1 or later (5.5.1, 6.1.1, 6.3.1, and all versions after 6.3.1)

- Log in as the ALTIBASE HDB server installation user.
- Upload the patch package to a random path.
- From ALTIBASE HDB server version 5.5.1, the Java-based installer was used, and the package name ends with .run as shown below.
- Grant execute permission to run the package.

  **How to change execution permission**

  ```
  $ chmod +x altibase-HDB-server-6.1.1.3.8-LINUX-X86-64bit-release.run
  ```

### ALTIBASE HDB server versions earlier than 5.5.1 (4.3.9, 5.3.3, and all versions through 5.3.3)

- Log in as the ALTIBASE HDB server installation user.
- Upload the patch package under the $ALTIBASE_HOME directory.
- ALTIBASE HDB Server versions earlier than 5.5.1 provide compressed files.

  ```
  altibase-XEON_LINUX_redhat_Enterprise_release5-64bit-5.3.3.84-release-GCC4.1.2.tgz
  ```

## 5. Perform the patch

---

### ALTIBASE HDB server version 5.5.1 or later (5.5.1, 6.1.1, 6.3.1, and all versions after 6.3.1)

- After executing the executable file as shown below, the subsequent operation proceeds according to the message.

  ```
  $ ./altibase-HDB-server-6.1.1.3.8-LINUX-X86-64bit-release.run
  ```

### ALTIBASE HDB server versions earlier than 5.5.1 (4.3.9, 5.3.3, and all versions through 5.3.3)

- Move to the $ALTIBASE_HOME directory and extract the files as follows.

  ```
  $ cd $ALTIBASE_HOME
  $ gzip -cd altibase-XEON_LINUX_redhat_Enterprise_release5-64bit-5.3.3.84-release-GCC4.1.2.tgz | tar xvf -
  ```

## 6. Check the patch version

---

- After completing the patch execution, check the version to see if the patch is applied.

  **How to check Altibase server version**

  ```
  $ altibase -v
  version 5.3.3.29 X86_64_WRS_LINUX_redhat_Enterprise_release5-64bit-5.3.3.29-release-GCC4.1.1 (xeon-redhat-linux-gnu) Nov 15 2010 17:36:40, binary db version 5.4.1, meta version 5.6.1, cm protocol version 5.6.2, replication protocol version 5.4.1
  ```

## 7. Copy necessary files from the backup file

---

- If the default password (`manager`) of the `sys` user is changed, the `$ALTIBASE_HOME/bin/server`, `is`, and `il` scripts would have changed.
- In this case, copy server, is, and il from the bin directory of the backup directory to $ALTIBASE_HOME/bin.

  ```
  $ cd $ALTIBASE_HOME
  $ cp -p bin.bak/server bin/
  $ cp -p bin.bak/is bin/
  $ cp -p bin.bak/il bin/
  ```

## 8. STARTUP ALTIBASE HDB Server ******

---

- After starting the Altibase server process, check the process and service port listen status.

  ```
  $ server start
  ```

  After shutdown, check the Altibase server process and service port LISTEN status.

  When the following two commands are executed, there should be no results to indicate a normal shutdown.

  ```
  $ ps -ef | grep 'altibase -p' | grep -v grep           # To check the Altibase server process
  altibase 10758 1 0 12:01 ? 00:00:14 /home/altibase/bin/altibase -p boot from admin

  $ netstat -an | grep 20300                             # To check the service port.
  tcp        0      0 0.0.0.0:20300               0.0.0.0:*                   LISTEN
  ```

# Precautions

---

## Check meta version before/after patch

---

- If the meta version changes, the database cannot be reverted to a lower version.
- After patching to a higher version, there may be cases where the user inevitably needs to revert to a lower version. If the meta version is changed, this cannot be done.
- Therefore, if the meta version changes, the user should be aware of this and proceed with the patching, and if necessary, take an offline full backup before the patch.
- Offline full backup targets include data files, log anchor files, log files, and configuration files.

## When patching from ALTIBASE HDB 4.3.9.1 ~ 4.3.9.50 to 4.3.9.51 ~**

---

If the following conditions are satisfied, the replication will not work after patching.

- When patching from ALTIBASE HDB 4.3.9.1 ~ 4.3.9.50 to 4.3.9.51 ~
- Replication environment

**Therefore, if the above conditions are satisfied, the user must follow the procedure below to apply the patch.**

1. Secure the Altibase server downtime
2. Shutdown the Altibase server (Refer to step 2 of the patch procedure)
3. Change the service port Temporarily change the service port during patching to ensure that access to Altibase is blocked.

  ```
  $ cd $ALTIBASE_HOME/conf
  $ vi altibase.properties               # Changed PORT_NO in altibase.properties.
  ```
4. Startup the Altibase server (Refer to step 8 of the patch procedure)
5. Check the replication gap. Make sure it is 0.

  **How to check replication gap**

  ```
  iSQL> SELECT REP_GAP FROM V$REPGAP;
  ```
6. Backup the replicated object creation syntax by performing aexport

  ```
  $ aexport                      # The user can check the syntax for creating a replication object in the SYS_CRT_REP.sql file created after performing aexport.
  ```
7. Drop replication object**

  ```
  -- Check the replication object name
  iSQL> SELECT REPLICATION_NAME FROM SYSTEM_.SYS_REPLICATIONS_;

  -- Stop the replication
  iSQL> ALTER REPLICATION replication_name STOP;

  -- Drop replication object
  iSQL> DROP REPLICATION replication_name;
  ```
8. Perform the checkpoint

  ```
  iSQL> ALTER SYSTEM CHECKPOINT;                   -- Repeat 4 times
  ```
9. Shutdown the Altibase server (Refer to step 2 of the patch procedure)
10. Perform the patch (Refer to steps 3 through 7 of the patch procedure)
11. Add CHECK_LOGFILE property**

  ```
  $ cd $ALTIBASE_HOME/conf
  $ vi altibase.properties               # Save after adding CHECK_LOGFILE = 0 to the last line of altibase.properties file.
  ```
12. Startup the Altibase Server (Refer to step 8 of the patch procedure)
13. Delete CHECK_LOGFILE property**

  ```
  $ cd $ALTIBASE_HOME/conf
  $ vi altibase.properties               # Delete the CHECK_LOGFILE = 0 line added to the end of altibase.properties, then save.
  ```
14. Insert data after creating temporary table This is to use up the log files created in the previous version and create a new log file.

  ```
  CREATE TABLE IMSI_T (C1 INTEGER, C2 INTEGER);

  CREATE OR REPLACE PROCEDURE IMSI_PROC AS V1 INTEGER;
  BEGIN
  FOR V1 IN 1 .. 300000 LOOP
  INSERT INTO IMSI_T VALUES (V1, V1);
  END LOOP;
  END;
  /
  ```

  ```
  iSQL> SELECT CUR_WRITE_LF_NO FROM V$LFG;          -- Check the result (number).
  iSQL> EXEC IMSI_PROC;                             -- Perform insert on the temporary table.
  iSQL> SELECT CUR_WRITE_LF_NO FROM V$LFG;          -- If this value is greater than the value checked above, the step is complete. If it has not changed, run IMSI_PROC again.
  iSQL> DROP PROCEDURE IMSI_PROC;                   -- Drop the temporary table and procedure.
  iSQL> DROP TABLE IMSI_T;
  ```
15. Perform the checkpoint

  ```
  iSQL> ALTER SYSTEM CHECKPOINT;                   -- Repeat 4 times.
  ```
16. Create replication object

  ```
  $ is -f SYS_CRT_REP.sql                          # Execute the created SYS_CRT_REP.sql file after executing aexport.
  ```
17. Start replication

  ```
  -- Check the replication object name
  iSQL> SELECT REPLICATION_NAME FROM SYSTEM_.SYS_REPLICATIONS_;

  -- Start replication
  iSQL> ALTER REPLICATION replication_name START;
  ```
18. Shutdown Altibase server (Refer to step 2 of the patch procedure).
19. Change the service port Change the temporarily changed service port to the original.

  ```
  $ cd $ALTIBASE_HOME/conf
  $ vi altibase.properties               # Changed PORT_NO in altibase.properties.
  ```
20. Startup the Altibase server (Refer to step 8 of the patch procedure)
21. Check the service
