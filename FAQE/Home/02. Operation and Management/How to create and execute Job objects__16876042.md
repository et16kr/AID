---
title: "How to create and execute Job objects"
page_id: "16876042"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/How+to+create+and+execute+Job+objects"
updated_at: "2021-04-02T17:27:07.000+0900"
version: 2
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# How to create and execute Job objects
Source: https://docs.altibase.com/display/FAQE/How+to+create+and+execute+Job+objects
Updated: 2021-04-02T17:27:07.000+0900

**- [Overview](#HowtocreateandexecuteJobobjects-Overview) - [Version](#HowtocreateandexecuteJobobjects-Version) - [How to use](#HowtocreateandexecuteJobobjects-Howtouse) - [Enabling the task scheduler function (Altibase Server Property Settings)](#HowtocreateandexecuteJobobjects-Enablingthetaskschedulerfunction(AltibaseServerPropertySettings)) - [Creating the procedure](#HowtocreateandexecuteJobobjects-Creatingtheprocedure) - [Creating the Job object](#HowtocreateandexecuteJobobjects-CreatingtheJobobject) - [Enabling the job object](#HowtocreateandexecuteJobobjects-Enablingthejobobject) - [Check the Job object and execution result](#HowtocreateandexecuteJobobjects-ChecktheJobobjectandexecutionresult) - [Related Properties](#HowtocreateandexecuteJobobjects-RelatedProperties) - [JOB_SCHEDULER_ENABLE](#HowtocreateandexecuteJobobjects-JOB_SCHEDULER_ENABLE) - [JOB_THREAD_COUNT](#HowtocreateandexecuteJobobjects-JOB_THREAD_COUNT) - [JOB_THREAD_QUEUE_SIZE](#HowtocreateandexecuteJobobjects-JOB_THREAD_QUEUE_SIZE) - [Reference](#HowtocreateandexecuteJobobjects-Reference)**

# Overview

---

This document describes how to create and execute Job objects, and how to monitor them.

# Version

---

Altibase version 6.3.1 or later

# How to use

---

To create a Job object and operate normally, the user must proceed in the following order.

1. Enable the task scheduler function
2. Create the procedure to register in the Job object
3. Create the Job object
4. Enable the Job object (only performed on Altibase 6.5.1 or later. Altibase 6.3.1 is not applicable)
5. Check the Job object and execution result

### Enabling the task scheduler function (Altibase Server Property Settings)

---

If the user is using the Job object for the first time, the job scheduler function must be enabled by changing the following Altibase server properties.

The job scheduler performs a procedure according to the settings registered in the job object.

- JOB_SCHEDULER_ENABLE : Task Scheduler Enable settings
- JOB_THREAD_COUNT : Number of threads to execute Job object

Both of the above properties must be set to 1 to use the task scheduler. The default value is 0, so be sure to check if the user is using Task Scheduler for the first time.

The JOB_SCHEDULER_ENABLE property can be changed even when the Altibase server is running, but to change the value of the JOB_THREAD_COUNT property, the Altibase server must be restarted.

Therefore, when using the task scheduler for the first time, change the properties according to the procedure below.

1. Stop the Altibase server

```
$ server stop
```

2. Find the JOB_SCHEDULER_ENABLE and JOB_THREAD_COUNT properties in the altibase.properties file, change the value to 1, and save.

**Example of Unix/Linux**

```
$ cd $ALTIBASE_HOME/conf
$ vi altibase.properties
```

3. Start the Altibase server

```
$ server start
```

4. Check the property setting value

```
SELECT NAME, MEMORY_VALUE1 FROM X$PROPERTY WHERE NAME IN ('JOB_SCHEDULER_ENABLE', 'JOB_THREAD_COUNT');
```

### Creating the procedure

---

Create a procedure to be registered in the Job object and check if the procedure is executed normally.

The reason for checking whether the procedure is normally executed is to exclude the possibility of a procedure problem if the Job object does not operate as set by the job scheduler.

### Creating the Job object

---

Create a JOB object.

The stored procedure to be executed, execution time, and execution cycle can be set in the JOB object. For the statement of creating a JOB object, refer to the SQL Reference manual. (Manual download page: [http://support.altibase.com/en/manual](http://support.altibase.com/en/manual) or [https://github.com/ALTIBASE/Documents/tree/master/Manuals/](https://github.com/ALTIBASE/Documents/tree/master/Manuals/Altibase_7.1/eng))

```
CREATE JOB job1
EXEC proc1
START sysdate
END sysdate + 3
INTERVAL 1 HOUR;
```

### Enabling the job object

---

This operation is an added procedure with the addition of a function to enable/disable a specific JOB in Altibase version 6.5.1.

In Altibase version 6.3.1, when creating a JOB object, it becomes 'enabled' immediately, but from Altibase 6.5.1, if the ENABLE option is not used in the CREATE JOB statement, it is 'disabled'.

Therefore, starting from Altibase version 6.5.1, after creating a Job object, in order to make the Job run, it must be changed to the enabled state.

The change method is as follows.

**Altibase 6.5.1 or later**

```
ALTER JOB job_name SET ENABLE;
```

Starting from Altibase version 6.5.1, it is also possible to set it to "Enabled" immediately when creating a Job object.

```
CREATE JOB job1
EXEC proc1
START sysdate
END sysdate + 3
INTERVAL 1 HOUR
ENABLE;
```

### Check the Job object and execution result

---

The user can check the job object information and job execution result with the query below.

```
-- JOB_NAME  : Name of Job object
-- PROC_NAME : Name of the procedure registered in the Job object
-- INTERVAL, INTERVAL_TYPE : Performance cycle
-- STATE : Check whether Job object is executed. If ING, the user can see that the procedure registered in the Job object is being executed.
-- EXEC_COUNT : Number of times the job object was executed after creation
-- ERROR_CODE : Error code when the procedure registered in the Job object fails
-- START_TIME, END_TIME : Time when the Job object was first executed / Time when it was finished
-- LAST_EXEC_TIME : Last time the Job object was performed
SELECT JOB_NAME
     , DECODE(IS_ENABLE, 'T', 'ENABLE', 'F', 'DISABLE') IS_ENABLE                  -- Delete then use it in Altibase 6.3.1
     , EXEC_QUERY PROC_NAME
     , INTERVAL
     , RPAD(DECODE(INTERVAL_TYPE, 'YY', 'YEARLY', 'MM', 'MONTHLY', 'DD', 'DAILY', 'HH', 'HOURLY', 'MI', 'MINUTELY'), 13) INTERVAL_TYPE
     , RPAD(DECODE(STATE, 0, '-', 1, 'ING'), 5) STATE
     , RPAD(EXEC_COUNT, 10) EXEC_COUNT
     , RPAD(ERROR_CODE, 10) ERROR_CODE
     , TO_CHAR(SYSDATE, 'YYYY-MM-DD HH:MI:SS') SYSDATE
     , TO_CHAR(START_TIME, 'YYYY-MM-DD HH:MI:SS') START_TIME
     , TO_CHAR(END_TIME, 'YYYY-MM-DD HH:MI:SS') END_TIME
     , TO_CHAR(LAST_EXEC_TIME, 'YYYY-MM-DD HH:MI:SS') LAST_EXEC_TIME
  FROM SYSTEM_.SYS_JOBS_;
```

**Example results**

```
JOB_NAME              IS_ENABLE  PROC_NAME             INTERVAL    INTERVAL_TYPE         STATE       EXEC_COUNT            ERROR_CODE            SYSDATE               START_TIME            END_TIME              LAST_EXEC_TIME
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
JOB2                  DISABLE  PROC                  1           MINUTELY              -           0                                           2016-08-30 14:15:06   2016-08-30 10:08:22   2016-09-02 10:08:22
JOB1                  ENABLE   PROC                  1           MINUTELY              -           43                                          2016-08-30 14:15:06   2016-08-30 10:11:00                         2016-08-30 14:15:00
2 rows selected.
```

How to check the error message corresponding to the error code

The error message corresponding to the error code can be checked by using the altierr utility.

$altierr 0x31129

0x31129 (201001) qpERR_ABORT_QSV_NOT_EXIST_PROC_SQLTEXT Procedure or function not found : <0%s>. # *Cause: The specified procedure or function name was not found in the database. # *Action: Verify that the procedure or function exists.

# Related Properties

---

## JOB_SCHEDULER_ENABLE

---

##### Property description

- This property is to enable or disable the task scheduler function.
- The default value is 0, which disables the task scheduler.

##### How to change the set value

- It can be changed by using ALTER SYSTEM.

  ```
  ALTER SYSTEM SET JOB_SCHEDULER_ENABLE = 1;           -- Enable the job scheduler function

  Or,
  ALTER SYSTEM SET JOB_SCHEDULER_ENABLE = 0;           -- Disable the job scheduler fucntion
  ```

##### How to check the set value

- The JOB_SCHEDULER_ENABLE set value can be checked with the query below.

  ```
  SELECT NAME, MEMORY_VALUE1 FROM X$PROPERTY WHERE NAME = 'JOB_SCHEDULER_ENABLE';
  ```

## JOB_THREAD_COUNT

---

##### Property description

- This property configures the number of threads to process a job.
- The default value is 0. When the Altibase server is started, the thread for executing the task scheduler is not started.
- If JOB_THREAD_COUNT is set to a value other than 0, JobScheduler threads and JobThread threads as many as JOB_THREAD_COUNT are started.
- Job is not executed by the service thread, but are processed by a thread called JobThread. So, if the user wants the job to be executed by the job scheduler, this property must be set.
- Change this property value requires restarting the Altibase server.

##### How to change the set value

- Stop the Altibase server.
- Find JOB_THREAD_COUNT in $ALTIBASE_HOME/conf/altibase.properties, change the value, and save.
- Start the Altibase server.

##### How to check the set value

- The JOB_THREAD_COUNT set value can be checked with the query below.

  ```
  SELECT NAME, MEMORY_VALUE1 FROM X$PROPERTY WHERE NAME = 'JOB_THREAD_COUNT';
  ```

## JOB_THREAD_QUEUE_SIZE

---

##### Property description

- This property sets the number of queues to process multiple job objects are executed at the same time.
  For example, when 4 job objects are executed at the same time by the job scheduler, they are processed in the following order according to the number of JOB_THREAD_COUNT and JOB_THREAD_QUEUE_SIZE.

  - JOB_THREAD_COUNT = 4, JOB_THREAD_QUEUE_SIZE = 1: 4 can be executed at the same time
  - JOB_THREAD_COUNT = 2, JOB_THREAD_QUEUE_SIZE = 2: Two are executed at the same time, and the other two are executed consecutively.
  - JOB_THREAD_COUNT = 1 ,JOB_THREAD_QUEUE_SIZE = 4: 1 is executed at the same time and the remaining 3 are executed consecutively.
- The default and minimum values are set large enough to 64, so there is no need for users to set them arbitrarily.
- To change the value of this property with the Read-Only attribute, the Altibase server must be stopped.

##### How to change the set value

- Stop the Altibase server.
- Save after changing JOB_THREAD_QUEUE_SIZE in $ALTIBASE_HOME/conf/altibase.properties.
- Start the Altibase server.

##### How to check the set value

- The JOB_THREAD_QUEUE_SIZE set value can be checked with the query below.

  ```
  SELECT NAME, MEMORY_VALUE1 FROM X$PROPERTY WHERE NAME = 'JOB_THREAD_QUEUE_SIZE';
  ```

# Reference

---

The following are manuals for the description of the task scheduler.

- Administrator's Manual> 5. Database Objects and Permissions> Job
- SQL Reference> 3. Data Definition Language> ALTER JOB /
- SQL Reference> 3. Data Definition Language> CREATE JOB
- SQL Reference> 3. Data Definition Language> DROP JOB
- General Reference> 2. ALTIBASE HDB Properties> Other Properties
- General Reference> 3. Data Dictionary> SYS_JOBS_

- Manual Download Page: [http://support.altibase](http://support.altibase)[.com/en/manual](http://support.altibase.com/en/manual) or [https://github.com/ALTIBASE/Documents/tree/master/Manuals/](https://github.com/ALTIBASE/Documents/tree/master/Manuals/Altibase_7.1/eng)
