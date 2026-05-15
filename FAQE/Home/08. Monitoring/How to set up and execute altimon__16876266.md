---
title: "How to set up and execute altimon"
page_id: "16876266"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/How+to+set+up+and+execute+altimon"
updated_at: "2021-04-05T10:34:21.000+0900"
version: 2
ancestors: ["Home", "08. Monitoring"]
labels: []
---

# How to set up and execute altimon
Source: https://docs.altibase.com/display/FAQE/How+to+set+up+and+execute+altimon
Updated: 2021-04-05T10:34:21.000+0900

- [What is ALTIMON?](#what-is-altimon) - [ALTIMON USER GUIDE](#altimon-user-guide) - [ALTIMON execution and configuration files](#altimon-execution-and-configuration-files) - [Uploading ALTIMON file](#uploading-altimon-file) - [Copying ALTIMON execution file](#copying-altimon-execution-file) - [Copying ALTIMON configuration file](#copying-altimon-configuration-file) - [Things to be changed in the ALTIMON configuration file](#things-to-be-changed-in-the-altimon-configuration-file) - [Executing ALTIMON](#executing-altimon) - [Check Altibase Log](#check-altibase-log)

# What is ALTIMON?

---

ALTIMON is a monitoring program that periodically checks the operating status of the ALTIBASE HDB server, and helps to track the cause of the failure by checking the ALTIBASE HDB server status when a failure occurs.

This page briefly explains how to set up and run ALTIMON.

For more details regarding ALTIMON, please refer to ALTIMON USER GUIDE.

ALTIMON USER GUIDE

---

- [ALTIMON_USER_GUIDE.pdf](https://docs.altibase.com/download/attachments/6979592/ALTIMON_USER_GUIDE.pdf?version=2&modificationDate=1422495172000&api=v2)

# ALTIMON execution and configuration files

---

### ALTIMON execution file

|  | Linux | SunOS Sparc | SunOS x86 | HP-UX IA | AIX |
| --- | --- | --- | --- | --- | --- |
| Altibase 6.3.1 | [altimon_linux_631.tar](https://docs.altibase.com/download/attachments/6979592/altimon_linux_631.tar?version=4&modificationDate=1606700918000&api=v2) |  |  |  |  |
| Altibase 6.1.1 | [altimon_linux_611.tar](https://docs.altibase.com/download/attachments/6979592/altimon_linux_611.tar?version=3&modificationDate=1606701256000&api=v2) |  |  |  |  |
| Altibase 4.3.9 |  |  | [altimon_sunos_x86_439.tar](https://docs.altibase.com/download/attachments/6979592/altimon_sunos_x86_439.tar?version=1&modificationDate=1606701556000&api=v2) |  |  |

### ALTIMON installation file

- Linux : [altimon_linux_611.tar](https://docs.altibase.com/download/attachments/6979592/altimon_linux_611.tar?version=3&modificationDate=1606701256000&api=v2)
- HP-UX IA : [altimon_linux.tar](https://docs.altibase.com/download/attachments/6979592/altimon_linux.tar?version=2&modificationDate=1606699755000&api=v2)
- HP-UX PA-RISC
- SunOS Sparc : [altimon_hpux_ia64.tar](https://docs.altibase.com/download/attachments/6979592/altimon_hpux_ia64.tar?version=2&modificationDate=1606699773000&api=v2)
- SunOS x86 :
- AIX : [altimon_sunos_sparc.tar](https://docs.altibase.com/download/attachments/6979592/altimon_sunos_sparc.tar?version=2&modificationDate=1606699785000&api=v2)
- Altibase does not provide an ALTIMON package for Windows. For Windows, refer to the [Monitoring Tools for Windows](https://docs.altibase.com/display/FAQE/Monitoring+Tools+for+Windows) page.

### ALTIMON configuration file

- Altibase version 6.3.1 : [altimon.conf.631](https://docs.altibase.com/download/attachments/6979592/altimon.conf?version=1&modificationDate=1527654613000&api=v2)
- ALTIBASE HDB version 5.1.5 : [altimon.conf.5.1.5](https://docs.altibase.com/download/attachments/6979592/altimon.conf.5.1.5?version=1&modificationDate=1445845022000&api=v2)
- ALTIBASE HDB version 4.3.9 :

# Uploading ALTIMON file

---

Upload the attachment (altimon.tar) to any directory on the system running the Altibase server process.

Extract the attachment.

```
$ tar xvf altimon.tar
```

Once it is extracted, 'altimon' directory will be created.

```
$ ls -l altimon
total 8336
drwxr-xr-x    2 eheejung staff           256 Dec 30 15:26 ACTION_LOG
drwxr-xr-x    2 eheejung staff           256 Dec 30 15:26 ACTION_SCRIPT
-rw-r--r--    1 eheejung staff           318 Dec 30 11:23 Makefile
-rwxr-xr-x    1 eheejung staff       3991619 Dec 30 15:10 altimon            // execution file
-rw-r--r--    1 eheejung staff         18120 Dec 30 11:23 altimon.conf       // configuration file
-rw-r--r--    1 eheejung staff         78141 Dec 30 11:23 altimon.cpp
-rw-r--r--    1 eheejung staff        166311 Dec 30 15:10 altimon.o
drwxr-xr-x    2 eheejung staff           256 Dec 30 15:26 log
```

# Copying ALTIMON execution file

---

Copy the ALTIMON executable file to the $ALTIBASE_HOME/bin directory.

```
 $ cp -p altimon $ALTIBASE_HOME/bin/
```

# Copying ALTIMON configuration file

---

Copy the ALTIMON configuration file to the `$ALTIBASE_HOME/conf/` directory.

```
$ cp -p altimon.conf $ALTIBASE_HOME/conf/
```

# Things to be changed in the ALTIMON configuration file

---

In the ALTIMON configuration file ($ALTIBASE_HOME/conf/altimon.conf), in the Connection Group section and ALTIMON PROPERTY section, change the comment section below to suit your environment.

For time-related queries, including LONG_RUN_QUERY, to run correctly, the TIMED_STATISTICS property must be set to 1.

```
#########################################
## Connection Group
#########################################
<CONNECTION_INFO>
    <DB_IP>        127.0.0.1 </DB_IP>
    <SYS_PASSWD>   manager     </SYS_PASSWD>               # Enter sys account password
    <PORT_NO>      20300       </PORT_NO>                  # Enter the Altibase server service port
    <NLS_USE>      US7ASCII    </NLS_USE>                  # Enter database server character set iSQL> select NLS_CHARACTERSET from v$nls_parameters; Can be checked.
</CONNECTION_INFO>

#########################################
## ALTIMON PROPERTY
#########################################
<ALTIMON_PROPERTY>
    <DATE_FORMAT>   1    </DATE_FORMAT>
    <SLEEP_TIME>    300  </SLEEP_TIME>                                       # If a problem occurs, change it to suit your environment so that the situation at that time can be logged. The unit is seconds.
    <LOG_FILE>      /home/altibase/altimon/log/altimon.log </LOG_FILE>       # Change the log file path to suit the environment. Enter it as an absolute path, leave the file name as it is, and change only the path.
    <LOG_DIR>       /home/altibase/altimon/log </LOG_DIR>                    # Enter the log file path again as an absolute path to suit the environment.
    <LIFE_CYCLE>    3    </LIFE_CYCLE>                                       # Log file retention period, in daily units. Change it to suit the environment.
    <LOGGING_LV>    2    </LOGGING_LV>
    <ALARM_FILE>    /home/altibase/altimon/log/alarm.log   </ALARM_FILE>     # Change the alarm log file path to suit your environment. Enter it as an absolute path, leave the filename as it is, and change only the path.
    <DB_SAVE>       OFF   </DB_SAVE>
    <LISTEN_PORT>   22300 </LISTEN_PORT>
</ALTIMON_PROPERTY>
```

From the settings below, the path $HOME/altimon/ACTION_SCRIPT/ will continue to be used.

If the altimon directory is located differently from the one below, please change it.

If altimon.tar is placed in the $HOME directory and untar it, the user does not need to change the settings below.

```
#########################################
## PROCESS CHECK PROPERTY
#########################################
<OS_QUERY_GROUP_SET>
    <CPU_USAGE> 80 </CPU_USAGE>
    <CPU_ACT>                                        # From this setting, the path $HOME/altimon/ACTION_SCRIPT/ will continue to be used. If the altimon directory is located differently from the one below, it will be changed.
       is -silent -f $HOME/altimon/ACTION_SCRIPT/cpu_act.sql -o $HOME/altimon/ACTION_LOG/cpu_act.log.`date +%Y%m%d_%H%M%S`
    </CPU_ACT>
    <MEM_USAGE> 100000000 </MEM_USAGE>
    <MEM_ACT>
       is -silent -f $HOME/altimon/ACTION_SCRIPT/mem_act.sql -o $HOME/altimon/ACTION_LOG/mem_act.log.`date +%Y%m%d_%H%M%S`
    </MEM_ACT>
    <DISK_CHK_ENABLE> ON </DISK_CHK_ENABLE>
    <DISK1>  /home       </DISK1>                    # Please modify the file system to be monitored.
    <DISK1_USAGE> 90     </DISK1_USAGE>              # Enter the file system usage threshold. The unit is %.
    <DISK2>  /home1   </DISK2>
    <DISK2_USAGE> 90     </DISK2_USAGE>
    <DISK_ACT>
    </DISK_ACT>
</OS_QUERY_GROUP_SET>
```

# Executing ALTIMON

---

After setting the environment variable, execute ALTIMON.

```
$ export UNIX95=1             (For Bourne Shell, Korn Shell, Bash Shell)
Or
$ setenv UNIX95 1             ( For C Shell)
```

For AIX, it also sets the NMON environment variable.

```
$ export NMON=t              (For Bourne Shell, Korn Shell, Bash Shell)
Or
$ setenv NMON t              ( For C Shell)
```

Execute altimon.

```
$ altimon start
```

# Check Altibase Log

---

altimon.log is saved in the following path set in $ALTIBASE_HOME/conf/altimon.conf.

The log of the day is altimon.log, and the last log is changed to altimon.log_MMDD.

```
<LOG_FILE>      /home/eheejung/altimon/log/altimon.log </LOG_FILE>
```

The ALTIMON log of the date of failure can be sent from the above path.
