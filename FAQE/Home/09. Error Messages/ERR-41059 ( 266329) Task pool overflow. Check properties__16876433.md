---
title: "ERR-41059 ( 266329) Task pool overflow. Check properties."
page_id: "16876433"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876433"
updated_at: "2021-04-05T13:23:04.000+0900"
version: 4
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# ERR-41059 ( 266329) Task pool overflow. Check properties.
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876433
Updated: 2021-04-05T13:23:04.000+0900

- [Version](#ERR-41059(266329)Taskpooloverflow.Checkproperties.-Version) - [Symptom](#ERR-41059(266329)Taskpooloverflow.Checkproperties.-Symptom) - [Cause](#ERR-41059(266329)Taskpooloverflow.Checkproperties.-Cause) - [When the number of new connections increases](#ERR-41059(266329)Taskpooloverflow.Checkproperties.-Whenthenumberofnewconnectionsincreases) - [When all service threads are in EXECUTE state and a new connection occurs](#ERR-41059(266329)Taskpooloverflow.Checkproperties.-WhenallservicethreadsareinEXECUTEstateandanewconnectionoccurs) - [When a new connection occurs while the number of transactions reaches TRANSACTION_TABLE_SIZE](#ERR-41059(266329)Taskpooloverflow.Checkproperties.-WhenanewconnectionoccurswhilethenumberoftransactionsreachesTRANSACTION_TABLE_SIZE) - [How to check](#ERR-41059(266329)Taskpooloverflow.Checkproperties.-Howtocheck) - [Checklist](#ERR-41059(266329)Taskpooloverflow.Checkproperties.-Checklist) - [How to check MAX_CLIENT setting value](#ERR-41059(266329)Taskpooloverflow.Checkproperties.-HowtocheckMAX_CLIENTsettingvalue) - [How to check the number of sessions](#ERR-41059(266329)Taskpooloverflow.Checkproperties.-Howtocheckthenumberofsessions) - [How to check the number of tasks](#ERR-41059(266329)Taskpooloverflow.Checkproperties.-Howtocheckthenumberoftasks) - [Solution](#ERR-41059(266329)Taskpooloverflow.Checkproperties.-Solution) - [Change MAX_CLIENT property](#ERR-41059(266329)Taskpooloverflow.Checkproperties.-ChangeMAX_CLIENTproperty) - [Review application](#ERR-41059(266329)Taskpooloverflow.Checkproperties.-Reviewapplication)

# Version

---

Altibase HDB 5 or later

# Symptom

---

When a new connection attempt from the client to the Altibase server fails with the following error message,

```
[ERR-91015 : Communication failure.]
```

The following error message can be seen in the altibase_boot.log of the Altibase server.

```
ERR-41059(errno=16) Task pool overflow. Check properties.
Dispatcher failed callback
```

# Cause

---

**This occurs when the number of tasks created in the Altibase server reaches MAX_CLIENT.**

Task is an object created when a new connection is made to the Altibase server. The maximum number of simultaneous creations is affected by the value of the Altibase server property MAX_CLIENT.

When the number of currently created tasks reaches MAX_CLIENT and a new task object cannot be created, a task pool overflow message appears.

MAX_CLIENT also refers to the maximum number of sessions that can be connected at the same time, but the task is affected by the same properties because it is eventually mapped to a session.

The following are possible causes.

## When the number of new connections increases

---

This can happen when the number of new connections increases and the number of tasks exceeds MAX_CLIENT.

## When all service threads are in EXECUTE state and a new connection occurs

---

If a new connection fails while all service threads are in EXECUTE state, the connection remains in the form of a task in the Altibase server. Therefore, even if the connection fails for this reason, the number of tasks increases as a new connection occurs.

When the connection fails as shown below,

```
$ is -silent
[ERR-5104D : Connection timeout.]
```

If the number of tasks exceeds MAX_CLIENT, the connection failure error message changes as follows.

```
$ is -silent
[ERR-91015 : Communication failure.]
```

## When a new connection occurs while the number of transactions reaches TRANSACTION_TABLE_SIZE

---

If a new connection fails while the number of concurrent transactions reaches TRANSACTION_TABLE_SIZE, the connection remains in the form of a task in the Altibase server. Therefore, even if the connection fails for this reason, the number of tasks increases as a new connection occurs.

When the connection fails as shown below,

```
$ is -silent
[ERR-5104D : Connection timeout.]
```

If the number of tasks exceeds MAX_CLIENT, the connection failure error message changes as follows.

```
$ is -silent
[ERR-91015 : Communication failure.]
```

In this case, the following message appears in altibase_boot.log.

```
TRANSACTION_TABLE_SIZE is full !!
 Current TRANSACTION_TABLE_SIZE is 1024
 Please check TRANSACTION_TABLE_SIZE
```

## How to check

---

### Checklist

To find the cause of the task pool overflow, the following items must be checked.

- **MAX_CLIENT property setting value**
- **Number of sessions connected to Altibase server**
  If the number of sessions connected to the Altibase server is equal to MAX_CLIENT, it is caused by increased sessions. If it is less than MAX_CLIENT, check the number of tasks.
- **Number of tasks created in Altibase server**
  If the number of sessions is less than MAX_CLIENT and the number of tasks is equal to or greater than MAX_CLIENT, you can suspect the cause below.

1. When all service threads are in EXECUTE state and a new connection occurs and the task is increased.
2. When the number of transactions reaches TRANSACTION_TABLE_SIZE and a new connection occurs and the task increases

- **$ALTIBASE_HOME/trc/altibase_boot.log**
  If the number of transactions exceeds TRANSACTION_TABLE_SIZE, the message TRANSACTION_TABLE_SIZE is full is left.

### How to check MAX_CLIENT setting value

Task pool overflow occurs when the number of tasks exceeds the value of the MAX_CLIENT property, so check the value of this property first.

- **When iSQL connection is possible**

  ```
  iSQL> set linesize 1024;
  iSQL> set colsize 30;
  iSQL> SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME = 'MAX_CLIENT';
  NAME                            VALUE1
  -------------------------------------------------------------------
  MAX_CLIENT                      1000
  1 row selected
  ```
- **When iSQL connection is not possible**

  ```
  $ grep MAX_CLIENT $ALTIBASE_HOME/conf/altibase.properties
  ```

### How to check the number of sessions

- **When iSQL connection is possible**

  If iSQL access is available, the number of sessions can be checked with the performance view, and through this, you can infer the cause of task pool overflow to some extent. If the current number of sessions is compared with the MAX_CLIENT value, and the value is the same, the increase in sessions is the cause. If the current number of sessions is less than MAX_CLIENT, it could be due to two other things than the session growth.

  **How to check the number of sessions**

  ```
  $ export ISQL_CONNECTION = IPC
  $ is -silent -sysdba
  iSQL> SELECT COUNT(*) FROM V$SESSION;                                    -- Check the current number of sessions
  COUNT
  -----------------------
  1000
  1 row selected.
  ```
- **When iSQL connection is not possible**

  If it is difficult to connect to iSQL, the number of sessions must be checked with the information on the OS. Depending on the client's connection method, there are two ways to check it. In the case of connecting using both TCP and IPC methods, the user can add up the results and compare them with MAX_CLIENT to determine whether the increase in sessions or other parts are the causes.

  **When the client connects with TCP**

  ```
  $ netstat -an | grep 20300 | grep ESTA | wc -l                   # Compare the result to MAX_CLIENT

  Or
  $ lsof -p pid                                                    # Compare the number of socket files open by the Altibase server with MAX_CLIENT.
  ```

  **When the client connects with IPC**

  ```
  # Linux
  $ ipcs -m | grep -i -e nattch -e eheejung
  key        shmid      owner      perms      bytes      nattch     status
  0x00003ed0 458761     altibase   666        131104     1

  # HP-UX, AIX
  $ ipcs -ma | grep -e NATTCH -e eheejung
  T         ID     KEY        MODE        OWNER     GROUP   CREATOR    CGROUP NATTCH      SEGSZ  CPID  LPID   ATIME    DTIME    CTIME
  m    7438362 0x00003353 --rw-rw-rw-  altibase     users  altibase     users      1     655480 13139 12411 17:57:48 no-entry 10:22:18

  # SunOS
  $ ipcs -ma | /usr/xpg4/bin/grep -e NATTCH -e beadskin
  T         ID      KEY        MODE        OWNER    GROUP  CREATOR   CGROUP NATTCH      SEGSZ  CPID  LPID   ATIME    DTIME    CTIME
  m          9   0x3863     --rw-rw-rw- altibase    other altibase    other      1     983576 14435 14435 17:31:35 no-entry 17:31:35
  ```

### How to check the number of tasks

- **When iSQL connection is possible**

  If the number of sessions is less than MAX_CLIENT, other causes should be investigated. Check the number of tasks with the command below and compare the number of tasks with MAX_CLIENT. The value of logon current means the number of tasks created and can be greater than the number of sessions.

  ```
  iSQL> SELECT NAME, VALUE FROM V$SYSSTAT WHERE NAME = 'logon current';
  ```

  If the number of sessions is less than MAX_CLIENT and the value of logon current is equal to or greater than MAX_CLIENT, there are two possible causes:
  - All service threads are in EXECUTE state and new connections increase the task count.
  - TRANSACTION_TABLE_SIZE has been reached and new connections increase the task count.

- **When iSQL connection is not possible**

  The number of created tasks can be checked by the logon current value of v$sysstat. However, if a task pool overflow occurs, you may not be able to execute the above statement because a new connection cannot be established. In this case, the number of tasks must be checked with the number of open files in the Altibase server process with the lsof command.

  **Example of executing lsof in Linux**

  ```
   $ lsof -p PID | grep -e IPv4 -e sock | grep -v LISTEN
  altibase 7494 eheejung   38u  IPv4           40725257                 TCP localhost:21109->localhost:36248 (ESTABLISHED)     # Sessions in which the connection was established normally, included in the task.
  altibase 7494 eheejung   39u  IPv4           40725262                 TCP localhost:21109->localhost:36249 (ESTABLISHED)
  altibase 7494 eheejung   40u  sock                0,4            40726084 can't identify protocol                            # All service threads are in EXECUTE state or
  altibase 7494 eheejung   41u  sock                0,4            40726576 can't identify protocol                            # When connection fails due to exceeding TRANSACTION_TABLE_SIZE
  altibase 7494 eheejung   42u  sock                0,4            40726604 can't identify protocol                            # Remaining task
  ```

  On Solaris, the pfiles command can be used instead of lsof.

  ```
  $ pfiles PID | grep sock

          sockname: AF_INET 0.0.0.0  port: 21109                   # LISTEN
          sockname: AF_INET 127.0.0.1  port: 21109                 # A session in which the connection was established normally, and this is also included in the task.
          sockname: AF_INET 127.0.0.1  port: 21109
          sockname: AF_INET 127.0.0.1  port: 21109
          sockname: AF_INET 127.0.0.1  port: 21109
          sockname: AF_INET 0.0.0.0  port: 0                       # If all service threads are in EXECUTE state or the connection fails due to exceeding TRANSACTION_TABLE_SIZE, the remaining tasks.
          sockname: AF_INET 0.0.0.0  port: 0
          sockname: AF_INET 0.0.0.0  port: 0
  ```

# Solution

---

## Change MAX_CLIENT property

---

If there are many actual simultaneous connection sessions, you need to change MAX_CLIENT.

When the number of simultaneous connection sessions increases, the number of concurrent transactions increases, and in the case of Unix/Linux systems, the number of open files increases.

Therefore, if you change MAX_CLIENT larger than the existing value, the following values must be changed as well.

- TRANSACTION_TABLE_SIZE
- max open files

Refer to "[Notes/Considerations when increasing the number of concurrent connection sessions (MAX_CLIENT)](https://docs.altibase.com/pages/viewpage.action?pageId=16876028)"

## Review application

---

If the application has the following characteristics, it is necessary to check again.

Unless the above processing is inevitable due to the nature of the service, consider changing the session to end immediately after the transaction is completed.

- Continuously opening new connections
- Maintaining unnecessarily connected sessions even though they no longer need to be connected
