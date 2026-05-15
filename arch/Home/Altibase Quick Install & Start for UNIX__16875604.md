---
title: "Altibase Quick Install & Start for UNIX"
page_id: "16875604"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16875604"
updated_at: "2021-02-22T16:30:44.000+0900"
version: 17
ancestors: ["Home"]
labels: []
---

# Altibase Quick Install & Start for UNIX
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16875604
Updated: 2021-02-22T16:30:44.000+0900

- [Overview](#AltibaseQuickInstall&StartforUNIX-Overview) - [Preparation](#AltibaseQuickInstall&StartforUNIX-Preparation) - [Altibase package installation and DB creation procedure](#AltibaseQuickInstall&StartforUNIX-AltibasepackageinstallationandDBcreationprocedure) - [How to download and install Altibase Package](#AltibaseQuickInstall&StartforUNIX-HowtodownloadandinstallAltibasePackage) - [Altibase directory components](#AltibaseQuickInstall&StartforUNIX-Altibasedirectorycomponents) - [Notes/Considerations on installation related to Altibase package](#AltibaseQuickInstall&StartforUNIX-Notes/ConsiderationsoninstallationrelatedtoAltibasepackage) - [Description of Altibase Database Creation](#AltibaseQuickInstall&StartforUNIX-DescriptionofAltibaseDatabaseCreation) - [Starting Altibase](#AltibaseQuickInstall&StartforUNIX-StartingAltibase) - [Shutting Altibase Down](#AltibaseQuickInstall&StartforUNIX-ShuttingAltibaseDown) - [Altibase Shutdown Procedure](#AltibaseQuickInstall&StartforUNIX-AltibaseShutdownProcedure) - [Explanation of Starting and Shutting Down Altibase](#AltibaseQuickInstall&StartforUNIX-ExplanationofStartingandShuttingDownAltibase) - [Use-Cases of Altibase](#AltibaseQuickInstall&StartforUNIX-Use-CasesofAltibase) - [iSQL commands](#AltibaseQuickInstall&StartforUNIX-iSQLcommands) - [Creating and Deleting DB user account](#AltibaseQuickInstall&StartforUNIX-CreatingandDeletingDBuseraccount) - [Creating and Deleting Tablespace account](#AltibaseQuickInstall&StartforUNIX-CreatingandDeletingTablespaceaccount) - [Creating and Deleting Tables](#AltibaseQuickInstall&StartforUNIX-CreatingandDeletingTables)

# Overview

---

This document describes how to install and start/stop Altibase.

The content to be referred after the basic installation is provided as a separate document and URL, so please refer to it.

For errors and improvements related to this document, please contact the technical support portal or technical support center.

- Technical support portal: [http://support.altibase.com](http://support.altibase.com/)
- Technical support center: 02-2082-1114

# Preparation

---

1. The OS user account for installing the Altibase package on the server must be created.
2. Download the Altibase package installer from support.altibase.com/en/ and upload the file to the system.
3. Check the Altibase version, OS type, OS bit information, and MAC address information. Then obtain a temporary license from support.altibase.com/en/ or contact the Altibase sales department to confirm the contract status and issue a formal license.

Access the Altibase package installer file from the URL described below, sign up for the membership, log in, and download the package.

Users can download the package from http://support.altibase.com/en/ or from Altibase.

Since the OS information, compile bit, and product version information are described in the package, request or download an appropriate product package.

```
http://support.altibase.com/en/
```

Example of Altibase package file name (Example of package file description of 6.5.1.XX, 7.1.0.XX based on Altibase package file for Linux)

```
altibase-HDB-server-6.5.1.X.X-LINUX-X86-64bit-release.run
altibase-server-7.1.0.X.X-LINUX-X86-64bit-release.run
```

# Altibase package installation and DB creation procedure

---

This section describes how to create DB of versions supported according to Altibase's End of Service (EOS) policy.

As of this document , the latest Altibase version is 'Altibase ver. 7' and'Altibase ver. earlier than 6' are for EOS.

Since Altibase cannot be operated until the DB is created, the DB must be created as follows before starting.

## How to download and install Altibase Package

---

- Grant the execution permission to the Altibase package file.

  ```
  $ ls -al
  -rw-r--r--  1 altibase dba 74639019 Jul 30 14:46 altibase-HDB-server-6.5.1.7.1-LINUX-X86-64bit-release.run

  $ chmod 744 altibase-HDB-server-6.5.1.7.1-LINUX-X86-64bit-release.run

  $ ls -al
  -rwxr--r--  1 altibase dba 74639019 Jul 30 14:46 altibase-HDB-server-6.5.1.7.1-LINUX-X86-64bit-release.run
  ```
- Execute the Altibase package and set the absolute path where the Altibase engine will be installed.

  ```
  $ ./altibase-HDB-server-6.5.1.7.1-LINUX-X86-64bit-release.run
  ----------------------------------------------------------------------------
  Welcome to the ALTIBASE HDB Server 6.5.1.7.1 setup wizard.
  ----------------------------------------------------------------------------
  Installation Directory

  Please specify the installation directory for ALTIBASE HDB Server 6.5.1.7.1

  Installation directory [/home/altibase/]: /home/altibase/altibase_home (After entering the set value, press Enter)
  ```
- Decide how to create DB. (Default = 1) * Full package installation and patch selection option. Altibase package default installation selects Full option.

  ```
  Please select the installation type.

  Installation type

  [1] Full installation: full package install
  [2] Patch: patch package install
  Please choose an option [1] : 1 (After entering the set value, press Enter)
  ```
- The user can check the kernel configuration guide. (The user can also check through pre_install.sh in the install directory under the installation path.)

  ```
  ----------------------------------------------------------------------------
  Pre-Installation Requirements for ALTIBASE HDB
  It is first necessary to set your system environment to ensure that ALTIBASE HDB
  will run properly. Before installing ALTIBASE HDB, the kernel parameter values
  must be set using the root user account. The kernel parameter values may be
  modified after installation; however, they must be set prior to starting
  ALTIBASE HDB.

  Please refer to the installation manual and pre_install.sh script file.
  (pre_install.sh: '$Altibase_install_dir'/install/pre_install.sh)

  ================ LINUX ================
  [ How to modify kernel parameter values ]

  echo 512 32000 512 512 > /proc/sys/kernel/sem
  echo 872415232 > /proc/sys/kernel/shmall

  # shmall
  If it is desired to use ALTIBASE HDB in shared memory mode, the value of
  'shmall' must be set. This value determines the maximum size of an Altibase
  database.

  Press [Enter] to continue :
  These values must be set in order for ALTIBASE HDB to operate properly.
  They must be set such that they are suitable for the system configuration.
  =====================================

  Press [Enter] to continue : (Insert Enter)
  ```
- Determine the DB name. (Default = mydb) * When changing the DB name, it is necessary to reconfigure the DB.

  ```
  ----------------------------------------------------------------------------
  ALTIBASE HDB Property Settings
  Step 1: Basic Database Operation Properties
  Database name [mydb] : mydb (After entering the set value, press Enter)
  ```
- Set the DB PORT. (Default = 20300)

  ```
  ALTIBASE HDB connection port number (1024-65535)      [20300] : 20300 (After entering the set value, press Enter)
  ```
- Determine the MEM_MAX_DB_SIZE value. (Default = 2G) * MEM_MAX_DB_SIZE refers to the 'maximum value' of data to be stored in memory, and refers to the limit value, not-pre-allocated.

  ```
  Maximum size of memory database

  - MIN value: 16M (K = kB, M = MB, G = GB) [2G] : 2G (After entering the set value, press Enter)
  ```
- Determine the total memory size of the buffer pool. (Default = 128M)

  BUFFER_AREA_SIZE refers to the'maximum value' of the memory size to be used as a buffer area in relation to the disk table, and refers to the total value allocated in advance.

  ```
  Buffer area size for caching disk-based database pages
  - MIN value: 1M (K = kB, M = MB, G = GB) [128M] : 128M (After entering the set value, press Enter)
  ```
- Decide whether to create DB. (Default = YES)

  ```
  Do you want to create a database after the installation process is complete?
  [1] YES
  [2] NO
  Please choose an option [1] : 1 (After entering the set value, press Enter)
  ```
- Determine the initial database size of the DB. (Default = 10M)

  ```
  ALTIBASE HDB Property Settings
  Step 2: Database Creation Properties
  Initial database size
  - 4M-4G (K = kB,M = MB,G = GB) [10M] : 10M (After entering the set value, press Enter)
  ```
- Determine the DB archive/no archive settings. (Default = No archivelog)

  ```
  Database archive logging mode
  [1] No archivelog
  [2] Archivelog
  Please choose an option [1] : 1 (After entering the set value, press Enter)
  ```
- Determine the DB character set setting. (Default = UTF8)

  ```
  Database character set
  [1] UTF-8
  [2] MS949
  [3] US7ASCII
  [4] KO16KSC5601
  [5] BIG5
  [6] GB231280
  [7] MS936
  [8] SHIFT-JIS
  [9] EUC-JP
  [10] MS932
  Please choose an option [1] : 1 (After entering the set value, press Enter)
  ```
- Determine the DB's National Character Set setting (Default = UTF8)

  ```
  National character set
  [1] UTF-8
  [2] UTF-16
  Please choose an option [1] : 1 (After entering the set value, press Enter)
  ```
- Set the DB data file (disk tablespace data file, memory tablespace checkpoint image file), archive log file, log file, and log anchor file path. * The path can be set to the path to be set, and the default value is set to the dbs, arch_logs, logs path of the directory where the Altibase engine is installed.

  ```
  ALTIBASE HDB Property Settings
  Step 3: Set Database Directories
  Default disk database directory [/home/altibase/altibase_home/dbs] : /home/altibase/altibase_home/dbs (After entering the set value, press Enter)
  Memory database directory [/home/altibase/altibase_home/dbs] : /home/altibase/altibase_home/dbs (After entering the set value, press Enter)
  Archive log directory [/home/altibase/altibase_home/arch_logs] : /home/altibase/altibase_home/arch_logs (After entering the set value, press Enter)
  Transaction log directory [/home/altibase/altibase_home/logs] : /home/altibase/altibase_home/logs (After entering the set value, press Enter)
  [Log Anchor file directories ]
  ALTIBASE HDB maintains three sets of log anchor files. These files contain
  important information
  about the database. By default, they are located in the "logs" folder.
  The location can be changed here or by modifying the contents of the ALTIBASE
  HDB properties file,
  which is named "altibase.properties".
  Directory 1. [/home/altibase/altibase_home/logs] : /home/altibase/altibase_home/logs (After entering the set value, press Enter)
  Directory 2. [/home/altibase/altibase_home/logs] : /home/altibase/altibase_home/logs (After entering the set value, press Enter)
  Directory 3. [/home/altibase/altibase_home/logs] : /home/altibase/altibase_home/logs (After entering the set value, press Enter)
  ```
- Show the property value to which the DB default setting is applied.

  ```
  Property Review
  Please check your property settings.

  To change these properties after installation is complete,
  please modify the following file:
    /home/altibase/altibase_home/conf/altibase.properties.
  1. ALTIBASE HDB Property Settings:
      Step 1: Basic Database Operation Properties
      1) Database name:
           [mydb]
      2) ALTIBASE HDB connection port number (1024-65535):
           [20300]
      3) Maximum size of memory database:
           [2G]
      4) Buffer area size for caching disk-based database pages:
           [128M]
  2. ALTIBASE HDB Property Settings:
  Press [Enter] to continue : (Insert Enter)
      Step 2: Database Creation Properties
      1) Initial database size
           [10M]
      2) Database archive logging mode
           [noarchivelog]
      3) Database character set
           [UTF8]
      4) National character set
           [UTF8]
  3. ALTIBASE HDB Property Settings:
      Step 3: Set Database Directories
      The database will not operate properly if any of these directories are
  removed.
      1) Disk database directory:
           [/home/altibase/altibase_home/dbs]
  Press [Enter] to continue : (Insert Enter)
      2) Memory database directory:
           [/home/altibase/altibase_home/dbs]
      3) Archive log directory:
           [/home/altibase/altibase_home/arch_logs]
      4) Transaction log directory:
           [/home/altibase/altibase_home/logs]
      5) Log Anchor file directories:
           Directory 1:
           [/home/altibase/altibase_home/logs]
           Directory 2:
           [/home/altibase/altibase_home/logs]
           Directory 3:
           [/home/altibase/altibase_home/logs]
  Press [Enter] to continue : (Insert Enter)
  ```
- Install the package to proceed with DB creation.

  ```
  Setup is now ready to install ALTIBASE HDB Server 6.5.1.7.1.
  Do you want to continue? [Y/n]: Y (Enter after Yes to proceed)
  ----------------------------------------------------------------------------
  Please wait until the setup wizard finishes installing ALTIBASE HDB Server
  6.5.1.7.1.
   Installing
   0% ______________ 50% ______________ 100%
   #########################################
  ```
- Enter the issued license after completing the package installation to create the DB. (Default = 1)

  ```
  ALTIBASE HDB License
  If a license has not been issued or if it has expired,
  ALTIBASE HDB services will not start.
  If this is the case, Please visit   http://support.altibase.com
  Choose an option for ALTIBASE HDB license registration.
  [1] I will input a license key.
  [2] I will select a license file.
  [3] I want to register an ALTIBASE HDB license later.
  Please choose an option [1] : 1 (After entering the set value, press Enter)
  ----------------------------------------------------------------------------
  ALTIBASE HDB License
  Please enter your ALTIBASE HDB license key.
   []: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX (Insert the issued license and press Enter)
  ```
- Proceed to create DB. (Data file, checkpoint image file, log file, log anchor file required for DB configuration based on the above property setting value)

  ```
  ALTIBASE HDB Quick Setting Guide
  [  Installation complete  ]
  Please refer to the file listed below to verify the ALTIBASE HDB version.
      /home/altibase/altibase_home/APatch/patchinfo
  [ Quick Guide to Making Settings in ALTIBASE HDB ]
  1. Set kernel variables using the root user account.
      run the '/home/altibase/altibase_home/install/pre_install.sh' file
      - This script helps you make kernel parameter settings.
  ================ LINUX ================
  [ How to modify kernel parameter values ]
  echo 512 32000 512 512 > /proc/sys/kernel/sem
  echo 872415232 > /proc/sys/kernel/shmall
  # shmall
  If it is desired to use ALTIBASE HDB in shared memory mode, the value of
  'shmall' must be set. This value determines the maximum size of an Altibase
  database.
  Press [Enter] to continue : (Insert Enter)
  These values must be set in order for ALTIBASE HDB to operate properly.
  They must be set such that they are suitable for the system configuration.
  =====================================
  2. Provide a license.
      Please rename and locate the license file as shown below.
      /home/altibase/altibase_home/conf/license
      If no license file has been issued or if the license file has expired,
      ALTIBASE HDB services will not start.
      In this case, please visit http://support.altibase.com
  3. Configure user environment variables (using the user account with which
  ALTIBASE HDB was installed).
      Run the '/home/altibase/altibase_home/install/post_install.sh' file
      under the account with which ALTIBASE HDB was installed.
  Press [Enter] to continue : (Insert Enter)
      This script performs necessary post-installation configuration.
      1) Create the ALTIBASE HDB user environment file and apply it to the user
  profile.
           (/home/altibase/altibase_home/conf/altibase_user.env)
      2) Create a database.
           If you selected 'YES' in response to the question about whether to
  create
           a database after installation, at "ALTIBASE HDB Property setting step
  1",
           a database will be automatically created.
           If you selected 'NO' in response to this question,
           you need to create a database manually.
           shell> server create [DB Character Set] [National Character Set]
  4. Start up and shut down the server
      shell> server start
      shell> server stop
  Press [Enter] to continue : (Insert Enter)
  5. Connect to the database using iSQL
      shell> isql -s 127.0.0.1 -u SYS -p MANAGER
  Press [Enter] to continue : (Insert Enter)
  Would you like to launch 'post_install.sh' now ?
   - This will create the ALTIBASE HDB database. [Y/n]: Y (Enter after Yes to proceed)
  Result
  -----------------------------------------------------------------
       Altibase Client Query utility.
       Release Version 6.5.1.7.1
       Copyright 2000, ALTIBASE Corporation or its subsidiaries.
       All Rights Reserved.
  -----------------------------------------------------------------
  ISQL_CONNECTION = UNIX, SERVER = localhost
  [ERR-910FB : Connected to idle instance]
  Connecting to the DB server.... Connected.
  TRANSITION TO PHASE : PROCESS
  Command executed successfully.
  DB Info (Page Size     = 32768)
          (Page Count    = 257)
          (Total DB Size = 8421376)
          (DB File Size  = 1073741824)
          Creating MMDB FILES     [SUCCESS]
          Creating Catalog Tables [SUCCESS]
  Press [Enter] to continue :
          Creating DRDB FILES     [SUCCESS]
    [SM] Rebuilding Indices [Total Count:0]  [SUCCESS]
  DB Writing Completed. All Done.
  Create success.
  Press [Enter] to continue : (Insert Enter)
  ----------------------------------------------------------------------------
  Setup has finished installing the ALTIBASE HDB Server 6.5.1.7.1 on your host.
  Info: [Linux Env.]
          Target : /home/altibase/altibase_home/conf/altibase_user.env
          created  ----------------------- Altibase environment setup file.
          added    ----------------------- ALTIBASE_HOME
          added    ----------------------- PATH
          added    ----------------------- LD_LIBRARY_PATH
          added    ----------------------- CLASSPATH
          export ----------------------- 'altibase_user.env'
          into '/home/altibase/.bash_profile'

  ==============================================
  Please perform [re-login]
  or [source /home/altibase/.bash_profile]
  or [. /home/altibase/.bash_profile]
  ==============================================
  Press [Enter] to continue : (Insert Enter)
  ```
- When the DB creation is completed, the configuration value is applied to the altibase.properties file in the directory called conf in the Altibase engine path. ($ALTIBASE_HOME/conf/altibase.properties)

  ```
  $ vi $ALTIBASE_HOME/conf/altibase.properties
  ========================= omitted =========================
  DB_NAME             =  mydb
  ========================= omitted =========================
  MEM_DB_DIR          = ?/dbs # Memory DB Directory     (This is the $ALTIBASE_HOME/dbs area and is the path to save the checkpoint image file of the standard memory tablespace. The default can be checked with ?/dbs.)
  ========================= omitted =========================
  DEFAULT_DISK_DB_DIR = ?/dbs # Disk   DB Directory     (This is the $ALTIBASE_HOME/dbs area and the path to save data files of the basic disk tablespace. The default can be checked with ?/dbs.)
  ========================= omitted =========================
  LOGANCHOR_DIR       = ?/logs # LOGANCHOR_DIR1         (This is the ALTIBASE_HOME/logs area and the path to save the log anchor file (the first of the three files). The default can be checked with ?/logs.)
  LOGANCHOR_DIR       = ?/logs # LOGANCHOR_DIR2         (This is the ALTIBASE_HOME/logs area and the path to save the log anchor file (the second file out of three). The default can be checked with ?/logs.)
  LOGANCHOR_DIR       = ?/logs # LOGANCHOR_DIR3         (This is the ALTIBASE_HOME/logs area and the path to save the log anchor file (the third file out of three). The default can be checked with ?/logs.)
  ========================= omitted =========================
  LOG_DIR             = ?/logs # LOG_DIR                (This is the $ALTIBASE_HOME/logs area and the path to save log files. The default can be checked with ?/logs.)
  ========================= omitted =========================
  ARCHIVE_DIR         =  ?/arch_logs # ARCHIVE_DIR      (This is the $ALTIBASE_HOME/arch_logs area and the path to save archive log files. The default can be checked ?/arch_logs.)
  ========================= omitted =========================
  MEM_MAX_DB_SIZE     = 2G # MEM_MAX_DB_SIZE
  ========================= omitted =========================
  BUFFER_AREA_SIZE    = 128M # BUFFER_AREA_SIZE
  ========================= omitted =========================
  PORT_NO             = 20300 # PORT_NO
  ========================= omitted =========================
  ```
- When the DB creation is completed normally, data files, checkpoint image files, log anchor files, and log files should be created in the dbs and logs directories as follows.

  ```
  $ ls -al $ALTIBASE_HOME/dbs

  SYS_TBS_MEM_DATA-0-0
  SYS_TBS_MEM_DATA-1-0
  SYS_TBS_MEM_DIC-0-0
  SYS_TBS_MEM_DIC-1-0
  dwfile-1.dwf
  dwfile0.dwf
  dwfile1.dwf
  system001.dbf
  temp001.dbf
  undo001.dbf

  $ ls -al $ALTIBASE_HOME/logs
  loganchor0
  loganchor1
  loganchor2
  logfile0
  logfile1
  logfile2
  logfile3
  logfile4
  logfile5
  ```
- When the DB creation is completed normally, $ALTIBASE_HOME and PATH are automatically set in the environment variable for the OS user account that installed the Altibase package.

  ```
  $ vi .bash_profile
  # .bash_profile
  # Get the aliases and functions
  if [ -f ~/.bashrc ]; then
          . ~/.bashrc
  fi
  # User specific environment and startup programs
  PATH=$PATH:$HOME/bin
  export PATH

  # ALTIBASE_ENV
  . /home/altibase/altibase_home/conf/altibase_user.env

  $ vi altibase_user.env
  ALTIBASE_HOME=/home/altibase/altibase_home;export ALTIBASE_HOME
  PATH=${ALTIBASE_HOME}/bin:${PATH};export PATH
  LD_LIBRARY_PATH=${ALTIBASE_HOME}/lib:${LD_LIBRARY_PATH};export LD_LIBRARY_PATH
  CLASSPATH=${ALTIBASE_HOME}/lib/Altibase.jar:${CLASSPATH};export CLASSPATH
  ```

## Altibase directory components

---

When the Altibase package is installed, the following directory is created.

This section is about basic installation and operation, and describes only the main directories that the user will check after installation. (Refer to the manual for details.)

|  |  |
| --- | --- |
| **Directory** | **Description** |
| admin | Example SQL and View creation file directory for easy viewing of Altibase performance view |
| bin | Altibase execution file, utility (execution file) directory |
| include | Header file directory provided for Altibase application development |
| install | [altibase_env.mk](http://altibase_env.mk) file and README file directory containing examples of macro settings for makefiles for Altibase application development. |
| lib | Library directory provided for Altibase application development |
| sample | Example program source (CLI, APRE, JDBC, C/C++, etc.) directory that provided Altibase application as a sample |
| trc | Trace log file location where Altibase operation status information is recorded |
| conf | Location of the Altibase configuration files (altibase.properties, aexport.properties), the property example file (sample), and the license file location directory |
| logs | Altibase log anchor file and default path where log files are created |
| dbs | Default path where Altibase data files are created |
| arch_logs | Backup directory to back up log files for Altibase recovery |
| altiComp | Utility directory that resolves data inconsistency caused by failures during replication operation between Altibase databases |
| msg | Directory containing files containing Altibase error messages |

# Notes/Considerations on installation related to Altibase package

---

- Altibase does not officially offer a 32-bit package.
  However, Altibase provides package products for the development and integration of client products (client-server).
  The client product starts with the name "altibase-HDB-client-6.5.1.x.x" before the package name.
  Since the product package includes compiler information, when using gcc/g++ as an example, check the version of the compiler in advance.
- For information on whether to use the Altibase client package and the available versions, additional information can be provided from technical inquiries at 02-2082-1114 or [support.altibase.com](http://support.altibase.com).

# Description of Altibase Database Creation

---

The following document describes how to create the Altibase database in detail.

[Creating ALTIBASE Database](https://docs.altibase.com/display/arch/Creating+ALTIBASE+Database)

# Starting Altibase

---

The normal startup is possible only when the basic installation and DB creation of the Altibase package are completed as above.

This section explains how the user can start the DB.

- When the installation and DB creation of the Altibase package is completed, execute the environment variable file in the installed OS user account to start.
- Since the environment variable file is different for each OS type, check if $ALTIBASE_HOME and PAHT are properly configured in the environment variable for the corresponding version.
- For Linux, for example, execute the environment file after checking whether $ALTIBASE_HOME and PATH are properly set in the environment variable file. (Run $.$HOME/.bash_profile or source $HOME/.bash_profile)

```
$ server start
-----------------------------------------------------------------
     Altibase Client Query utility.
     Release Version 6.5.1.7.1
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
ISQL_CONNECTION = UNIX, SERVER = localhost
[ERR-910FB : Connected to idle instance]
Connecting to the DB server.... Connected.

TRANSITION TO PHASE : PROCESS
TRANSITION TO PHASE : CONTROL

TRANSITION TO PHASE : META
  [SM] Recovery Phase - 1 : Preparing Database
                          : Dynamic Memory Version => Parallel Loading
  [SM] Recovery Phase - 2 : Loading Database
  [SM] Recovery Phase - 3 : Skipping Recovery & Starting Threads...
                            Refining Disk Table
  [SM] Refine Memory Table : ........................................................................... [SUCCESS]
  [SM] Rebuilding Indices [Total Count:137] ............................................................ [SUCCESS]

TRANSITION TO PHASE : SERVICE
  [CM] Listener started : TCP on port 20300 [IPV4]
  [CM] Listener started : UNIX
  [CM] Listener started : IPC
  [RP] Initialization : [PASS]
--- STARTUP Process SUCCESS ---
Command executed successfully.
```

- In addition to the above method, Altibase can be started by connecting to iSQL and executing the "startup service" command.

  ```
  $ isql -sysdba
  -----------------------------------------------------------------
       Altibase Client Query utility.
       Release Version 6.5.1.7.1
       Copyright 2000, ALTIBASE Corporation or its subsidiaries.
       All Rights Reserved.
  -----------------------------------------------------------------
  Write UserID : SYS                       (Enter user "SYS")
  Write Password : MANAGER                 (Enter the default password "MANAGER")
  ISQL_CONNECTION = UNIX, SERVER = localhost
  [ERR-910FB : Connected to idle instance]
  iSQL(sysdba)> startup service;
  Connecting to the DB server.... Connected.

  TRANSITION TO PHASE : PROCESS

  TRANSITION TO PHASE : CONTROL

  TRANSITION TO PHASE : META
    [SM] Recovery Phase - 1 : Preparing Database
                            : Dynamic Memory Version => Parallel Loading
    [SM] Recovery Phase - 2 : Loading Database
    [SM] Recovery Phase - 3 : Starting Recovery
                              Initializing Active Transaction List
                              Redo
                              Refine Disk Table..
                              Undo
    [SM] Refine Memory Table : ........................................................................... [SUCCESS]
    [SM] Rebuilding Indices [Total Count:137] ............................................................ [SUCCESS]

  TRANSITION TO PHASE : SERVICE
    [CM] Listener started : TCP on port 20300 [IPV4]
    [CM] Listener started : UNIX
    [CM] Listener started : IPC
    [RP] Initialization : [PASS]
  --- STARTUP Process SUCCESS ---
  Command executed successfully.
  ```
- Example of failure to start Altibase

  ```
  1) If $ALTIBASE_HOME is set in the environment variable, PATH is not set or the environment variable file is not executed
   $ server start
  -bash: server: command not found

  $ isql -sysdba
  [ISQL]ERROR: Could not SQLConnect

  2) If DB is not created
  $ server start
  -----------------------------------------------------------------
       Altibase Client Query utility.
       Release Version 6.5.1.7.1
       Copyright 2000, ALTIBASE Corporation or its subsidiaries.
       All Rights Reserved.
  -----------------------------------------------------------------
  ISQL_CONNECTION = UNIX, SERVER = localhost
  [ERR-910FB : Connected to idle instance]
  Connecting to the DB server.... Connected.

  TRANSITION TO PHASE : PROCESS

  TRANSITION TO PHASE : CONTROL
  [FAILURE] The log anchor file does not exist or is not valid.
  Startup Failed....
  [ERR-91015 : Communication failure.]

  3) If a license is not entered
  $ server start
  -----------------------------------------------------------------
       Altibase Client Query utility.
       Release Version 6.5.1.7.1
       Copyright 2000, ALTIBASE Corporation or its subsidiaries.
       All Rights Reserved.
  -----------------------------------------------------------------
  ISQL_CONNECTION = UNIX, SERVER = localhost
  [ERR-910FB : Connected to idle instance]
  Connecting to the DB server...............................Startup Failure. Check Your Environment.

  $ vi $ALTIBASE_HOME/trc/altibase_boot.log (Trace logs are recored in the $ALTIBASE_HOME/trc directory, and the log on failure can be checked in altibase_boot.log.)
  ========================= omitted =========================
  [2019/09/01 02:03:35 6][PID:108941][Thread-140685391135488][LWP-108941]
  No valid license present!
  ========================= omitted =========================
  ```

# Shutting Altibase Down

---

If the Altibase installation is completed and started normally, this section describes how to shut down the DB by the user.

## Altibase Shutdown Procedure

---

- Altibase can be stopped by executing the "server stop" command in the prompt window of the OS account. (This is provided to execute commands with a shell script called "server" so that users can easily terminate them.)

  ```
   $ server stop
  -----------------------------------------------------------------
       Altibase Client Query utility.
       Release Version 6.5.1.7.1
       Copyright 2000, ALTIBASE Corporation or its subsidiaries.
       All Rights Reserved.
  -----------------------------------------------------------------
  ISQL_CONNECTION = UNIX, SERVER = localhost
  Ok..Shutdown Proceeding....

  TRANSITION TO PHASE : Shutdown Altibase
    [RP] Finalization : PASS
  shutdown immediate success.
  ```
- In addition to the above method, Altibase can be stopped by connecting to iSQL and executing the "shutdown immediate" command. (When executing the shutdown command, options can be shut down with abort, immediate, or normal.

  ```
  $ isql -sysdba
  -----------------------------------------------------------------
       Altibase Client Query utility.
       Release Version 6.5.1.7.1
       Copyright 2000, ALTIBASE Corporation or its subsidiaries.
       All Rights Reserved.
  -----------------------------------------------------------------
  Write UserID : SYS                       (Enter "SYS")
  Write Password : MANAGER                 (Enter the default password "MANAGER")

  iSQL(sysdba)> shutdown abort;

  iSQL(sysdba)> shutdown immediate;

  iSQL(sysdba)> shutdown normal;
  ```

  * When the above shutdown is in progress, it can be shutdown(stopped) in three ways. please refer to the description below.

  | Option | Description |
  | --- | --- |
  | abort | All the connected sessions (clients) are forcibly terminated and immediately stop running. Since Altibase is stopped, it is immediately shut down without a normal shutdown process. (After running, data recovery is performed and there is no problem.) |
  | immediate | All the connected sessions (clients) are forcibly terminated and stopped with a normal shutdown process. |
  | normal | After waiting for all the connected sessions (clients) to be terminated normally, it is stopped through a normal shutdown process. |

  If the "normal" option is used, it has to wait for the session (client) to terminate. If the Altibase is stopped without knowing this reason, it may be taken as a. mistake as if the shutdown process is not in progress.

# Explanation of Starting and Shutting Down Altibase

---

- Details on starting and stopping Altibase are described in detail in the URL below.
- [Understanding the Altibase Start/Shut down Process](https://docs.altibase.com/pages/viewpage.action?pageId=13434993)

# Use-Cases of Altibase

---

- This chapter describes how to create a DB user, create a tablespace, and create a table simply as an example.
- Altibase complies with the SQL92 standard, so there is no significant difference in statements from other DBMSs.
- For more detailed information on SQL statements, refer to the manual provided by Altibase. (Go to Altibase.com or github.com/ALTIBASE to access and download the manual)

## iSQL commands

---

- Altibase provides a utility program for users to use SQL statements in terminals and applications. * When the DB is created, only the user with DBA authority called "SYS" exists, so only $ALTIBASE_HOME/bin/is can be executed and accessed. ("is" is provided as a shell script made for easy access and use of iSQL.)

  ```
  $ is
  -----------------------------------------------------------------
       Altibase Client Query utility.
       Release Version 6.5.1.7.1
       Copyright 2000, ALTIBASE Corporation or its subsidiaries.
       All Rights Reserved.
  -----------------------------------------------------------------
  ISQL_CONNECTION = TCP, SERVER = localhost, PORT_NO = 20300
  iSQL> select sysdate from dual;
  SYSDATE
  ---------------
  01-SEP-2019
  1 row selected.

  $ isql -s 127.0.0.1 -u sys -p manager -port 20300
  -----------------------------------------------------------------
       Altibase Client Query utility.
       Release Version 6.5.1.7.1
       Copyright 2000, ALTIBASE Corporation or its subsidiaries.
       All Rights Reserved.
  -----------------------------------------------------------------
  ISQL_CONNECTION = TCP, SERVER = 127.0.0.1, PORT_NO = 20300
  iSQL> select sysdate from dual;
  SYSDATE
  ---------------
  01-SEP-2019
  1 row selected.
  ```
- Each input option is as follows.

  | Input option | Description |
  | --- | --- |
  | -u | Enter the DB user's account name. |
  | -p | Enter the DB user's password. |
  | -s | Enter the network IP address of the server where the target DB to be accessed is located, or 127.0.0.1 for the local server. |
  | -port | Enter the PORT_NO set in the target DB to be connected. (PORT_NO can be checked in the $ALTIBASE_HOME/conf/altibase.properties file) |
- If the DB character set is not set to US7ASCII, the character set specified when creating the DB must be set as an environment variable. * When the DB was created, if the character set is set to MS949 as an example, the session (client) that connects to the input and output of Korean data should also be set and applied to the character set of ALTIBASE_NLS_USE with MS949.

  ```
  Example)
  $ server create MS949 UTF8
  -> When the character set of Altibase is set and configured to MS949

  $ is
  -----------------------------------------------------------------
       Altibase Client Query utility.
       Release Version 6.5.1.7.1
       Copyright 2000, ALTIBASE Corporation or its subsidiaries.
       All Rights Reserved.
  -----------------------------------------------------------------
  ISQL_CONNECTION = TCP, SERVER = localhost, PORT_NO = 20300
  iSQL> create table test (c1 varchar(100));
  Create success.
  iSQL> insert into test values ('Altibase');
  1 row inserted.
  iSQL> insert into test values ('알티베이스');
  1 row inserted.
  -> Save Altibase's character set by inputting random Korean data in MS949

  $ is
  -----------------------------------------------------------------
       Altibase Client Query utility.
       Release Version 6.5.1.7.1
       Copyright 2000, ALTIBASE Corporation or its subsidiaries.
       All Rights Reserved.
  -----------------------------------------------------------------
  ISQL_CONNECTION = TCP, SERVER = localhost, PORT_NO = 20300
  iSQL> set vertical on;
  iSQL> select * from v$nls_parameters;
  SESSION_ID                : 1
  NLS_USE                   : US7ASCII          (In the case of a connected session, check that it is connected with the US7ASCII charset.)
  NLS_CHARACTERSET          : MS949             (Check that Altibase charset is set to MS949)
  NLS_NCHAR_CHARACTERSET    : UTF8
  NLS_COMP                  : BINARY
  NLS_NCHAR_CONV_EXCP       : FALSE
  NLS_NCHAR_LITERAL_REPLACE : FALSE
  1 row selected.

  iSQL> select * from test;
  C1
  ----------------------------------
  Altibase
  ?????
  2 rows selected.
  -> When retrieving Korean data in a session connected with US7ASCII, the input "알티베이스" data may be broken and displayed as ?????

  $ export ALTIBASE_NLS_USE=MS949
  -> For sessions connected to Altibase, environment variables are dynamically set and applied so that they can be accessed with the MS949 charset.
   (ALTIBASE_NLS_USE setting)
  -> Save and execute export ALTIBASE_NLS_USE=MS949 in the environment variable.
  -> Only when the character set is explicitly specified in the environment variable is handled correctly in input/output of Korean characters.
  -> Even if the above environment variable is set, there may be a case in which the Korean language is displayed as a broken font. In that case, the environment of the currently used and connected terminal must be set so that Korean language can be used.

  $ is
  -----------------------------------------------------------------
       Altibase Client Query utility.
       Release Version 6.5.1.7.1
       Copyright 2000, ALTIBASE Corporation or its subsidiaries.
       All Rights Reserved.
  -----------------------------------------------------------------
  ISQL_CONNECTION = TCP, SERVER = localhost, PORT_NO = 20300
  iSQL> set vertical on;
  iSQL> select * from v$nls_parameters;
  SESSION_ID                : 1
  NLS_USE                   : MS949            (In the case of the connected session, it was US7ASCII in the above situation, but it is confirmed that it is connected by setting and applying the same value as the Altibase DB charset with MS949.)
  NLS_CHARACTERSET          : MS949            (Check that Altibase charset is set to MS949)
  NLS_NCHAR_CHARACTERSET    : UTF8
  NLS_COMP                  : BINARY
  NLS_NCHAR_CONV_EXCP       : FALSE
  NLS_NCHAR_LITERAL_REPLACE : FALSE
  1 row selected.

  iSQL> select * from test;
  C1
  ----------------------------------
  Altibase
  알티베이스
  2 rows selected.
  -> Check that when Korean data is retrieved from the session connected with the same settings as the Altibase DB character set, it is displayed normally.
  ```

## Creating and Deleting DB user account

---

- In Altibase, a user with DBA authority called "SYS" account is created. New user accounts can be created by logging in with this account. * In this part, commands for creating and deleting new users are explained as follows.

  ```
  1) Example of creation
  iSQL> CREATE USER new_user IDENTIFIED BY new_user_password DEFAULT TABLESPACE SYS_TBS_DISK_DATA ACCESS SYS_TBS_MEM_DATA ON;
  Create success.

  2) Example of deletion
  iSQL> DROP USER new_user CASCADE;
  Drop success.
  ```
- Each input part used is as follows.

  | Input | Description |
  | --- | --- |
  | After CREATE USER | Describe the name of a new user to be used in Altibase. |
  | After IDENTIFIED BY | Describe to designate the user's password (password). |
  | After DEFAULT TABLESPACE | Users can create it without describing it from this part. However, it is a clause that specifies the accessible tablespace and can be changed through the “ALTER USER” statement. |
  | ACCESS ~ ON | Authorize access to the tablespace described between ACCESS and ON. |

## Creating and Deleting Tablespace account

---

- Altibase HDB (Hybrid DBMS) can use both memory tablespaces and disk tablespaces. * In this part commands for creating and deleting user memory tablespaces and user disk tablespaces are explained as follows.

  ```
  1) Example of creating user memory tablespace
  iSQL> CREATE MEMORY TABLESPACE new_tbs_mem SIZE 1G AUTOEXTEND ON NEXT 128M MAXSIZE 2G;
  Create success.
  -> If the user executes the example as above, a checkpoint image file called “$ALTIBASE_HOME/dbs/NEW_TBS_MEM-X-X” is created, and the size increases in units of 128M starting from the initial 1G, and is automatically expanded to 2G and set as a usable space.

  2) Example of creating user disk tablespace
  iSQL> CREATE DISK TABLESPACE new_tbs_disk DATAFILE 'new_tbs.dbf' SIZE 1G AUTOEXTEND ON NEXT 128M MAXSIZE 2G;
  Create success.
  -> If the user executes the example as above, a data file called “$ALTIBASE_HOME/dbs/new_tbs.dbf” is created. The tablespace starts from 1G and increases in 128M increments, and automatically expands to 2G and is set as a usable space.
  -> In the case of creating the disk tablespace, it is possible to use CREATE TABLESPACE by omitting CREATE DISK TABLESPACE or DISK.

  3) Example of deleting/dropping
  iSQL> DROP TABLESPACE new_tbs_disk INCLUDING CONTENTS AND DATAFILES;
  Drop success.
  -> This statement deletes not only the tablespace, but also objects and data files.
     If it is not deleted normally, access to the tablespace and sessions (clients) in use exist. The user can retrieve for and clean up the sessions (clients) and execute the delete statement again.
  ```

## Creating and Deleting Tables

---

- Altibase HDB (Hybrid DBMS) can use both memory tablespaces and disk tablespaces, so memory tables and disk tables can be created as well. * In this part, commands that create and delete memory tables and disk tables are explained as follows.

  ```
  1) How to query memory tablespaces and disk tablespaces
  iSQL> select type, name from v$tablespaces;
  TYPE        NAME
  ---------------------------------------------------------
  0           SYS_TBS_MEM_DIC
  1           SYS_TBS_MEM_DATA                  (Memory tablespace created by default)
  3           SYS_TBS_DISK_DATA                 (Disk tablespace created by default)
  7           SYS_TBS_DISK_UNDO
  5           SYS_TBS_DISK_TEMP
  5 rows selected.

  1) Example of creating a memory table
  iSQL> create table mem_tbl (c1 int, c2 varchar(100), c3 char(100));
  Create success.

  iSQL> desc mem_tbl;
  [ TABLESPACE : SYS_TBS_MEM_DATA ]             (Memory table created by default)
  [ ATTRIBUTE ]
  ------------------------------------------------------------------------------
  NAME                                     TYPE                        IS NULL
  ------------------------------------------------------------------------------
  C1                                       INTEGER         FIXED
  C2                                       VARCHAR(100)    FIXED
  C3                                       CHAR(100)       FIXED
  MEM_TBL has no index
  MEM_TBL has no primary key
  -> Altibase uses a memory tablespace by default if a tablespace is not specified when creating a table and is created as a memory table.

  3) Example of creating a disk table
  iSQL> create table disk_tbl (c1 int, c2 varchar(100), c3 char(100)) tablespace SYS_TBS_DISK_DATA;
  Create success.

  iSQL> desc disk_tbl;
  [ TABLESPACE : SYS_TBS_DISK_DATA ]            (Disk tablespace created by default)
  [ ATTRIBUTE ]
  ------------------------------------------------------------------------------
  NAME                                     TYPE                        IS NULL
  ------------------------------------------------------------------------------
  C1                                       INTEGER
  C2                                       VARCHAR(100)
  C3                                       CHAR(100)
  DISK_TBL has no index
  DISK_TBL has no primary key
  -> Altibase uses the disk tablespace when a disk tablespace is specified when creating a table and is created as a disk table.

  4) Example of deleting/dropping tables
  iSQL> drop table mem_tbl;
  Drop success.

  iSQL> drop table disk_tbl;
  Drop success.
  -> Memory tables and disk tables can both be dropped in the same way.
  ```

# Korean Source Attachments

The Korean source page also references these downloadable source attachments. They are preserved here so the English document set does not lose those references.

- [Korean source attachment 1 (PDF)](https://docs.altibase.com/download/attachments/13436834/ALTIBASE_Quick_Install_Start_for_UNIX.pdf?version=1&modificationDate=1697762511000&api=v2)
