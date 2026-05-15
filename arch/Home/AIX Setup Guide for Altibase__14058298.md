---
title: "AIX Setup Guide for Altibase"
page_id: "14058298"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/AIX+Setup+Guide+for+Altibase"
updated_at: "2025-09-23T08:45:51.000+0900"
version: 9
ancestors: ["Home"]
labels: []
---

# AIX Setup Guide for Altibase
Source: https://docs.altibase.com/display/arch/AIX+Setup+Guide+for+Altibase
Updated: 2025-09-23T08:45:51.000+0900

- [Overview](#AIXSetupGuideforAltibase-Overview) - [Kernel Parameters](#AIXSetupGuideforAltibase-KernelParameters) - [User Settings](#AIXSetupGuideforAltibase-UserSettings) - [Summary](#AIXSetupGuideforAltibase-Summary) - [Enclosure](#AIXSetupGuideforAltibase-Enclosure)

## Overview

This document provides guides for setting appropriate values and various user environment settings of kernel parameters for installing and operating Altibase in the AIX (Advanced Interactive eXecutive) Operating System.

This document covers only operating system items that must be set before Altibase is installed. For Altibase property configuration, refer to the separate document "Altibase Configuration File Guide".

This document is based on AIX 5.x and does not cover AIX 4.3 or earlier versions, as they are no longer supported by Altibase.

## Kernel Parameters

When operating Altibase on the AIX OS, it describes the types of kernel parameters that need to be changed, and why the settings need to be changed, and introduces how to change the kernel parameters.

For details related to each kernel parameter, refer to the guide provided by IBM.

### Posix AIO

Posix AIO is an AIX kernel parameter that allows a process to handle disk I/O and application operations concurrently, improving performance.

If the corresponding kernel parameter is not set, Altibase cannot be used, so it must be set in advance.

However, starting from AIX 6.1, the default value of Posix AIO is `Available`, so it does not need to be set separately.

### File Cache

This kernel parameter is not mandatory to change. However, proper file cache settings are recommended because they suppress swap-out events on memory areas used by Altibase and minimize cases where OS-layer Disk I/O delay caused by swapping leads to Altibase performance degradation.

For reference, AIX 5.2 ML03 or earlier does not have the related parameters, and AIX 6.1 or later does not require special changes. Depending on the operating system version, this section may not apply.

File cache is a kind of system buffer managed at the operating system level to solve the bottleneck caused by the speed difference between main memory and auxiliary memory. These file caches are managed by unique policies of each operating system, but commonly have a direct correlation with the swap policy.

Swapping itself is useful because it allows applications or data files larger than main memory to be handled. However, on systems running long-resident applications such as a DBMS, OS-layer Disk I/O delay caused by swapping can make DBMS response times irregular or delayed. Therefore, file cache behavior must be considered according to system usage.

Therefore, in order to guarantee Altibase's consistent response time, it is recommended to set the file cache and swap-related kernel parameters in advance so that swap does not occur as much as possible.

### Configuration on AIX

The default memory manager of AIX is to convert unused memory areas to file cache as much as possible.

In this state, if an additional memory allocation request occurs and there is insufficient free memory, AIX swaps out memory being used by a process or less frequently accessed file cache areas, and then allocates the requested memory.

For a long-resident memory process such as Altibase, infrequently accessed data areas can unintentionally be swapped out to disk by the operating system, and that memory area can then be used as file cache.

If a transaction accesses the swapped-out area, performance can become inconsistent.

In this way, the process by which the memory manager acquires the memory requested by the process or the file cache in order to allocate additional memory is called stealing. The stealing target can be specified by the file cache-related kernel parameter lru_file_repage.

Generally, three kernel parameters are changed as well as lru_file_repage.

| Kernel Parameter | Recommended Value | Remark |
| --- | --- | --- |
| minperm | 10% | - |
| lru_file_repage | 0 | Supported in AIX 5.2 ML5, AIX 5.3 ML2 or later |
| strict_maxclient | 0 | Supported in AIX 5.2 ML4 or later |

When set as above, stealing occurs only in the file cache when the file cache share compared to the total memory is used above minperm.

Since this setting can be checked during AIX operation, if performance or other problems occur, it is recommended to change it in consultation with AIX engineers.

### Resource Limitations

In the case of AIX, some resource limit items are set through kernel parameter changes rather than by using ulimit in the user configuration file.

Altibase is a single-process, multi-thread-based application program, so if the system does not have any application programs other than Altibase, there is no need to specifically consider the number of process limits per user. In some cases, it may be necessary to appropriately expand the limit on the number of processes per user by predicting the number.

The relevant kernel parameters are as follows.

| Kernel Parameter | Description | Recommended Value |
| --- | --- | --- |
| Maximum number of PROCESSES allowed per user | The number of processes that can be created per user | More than the number of processes that can be running simultaneously |

### How to Change

To change kernel parameters related to file cache, use the virtual memory kernel utility vmo. For other changes, use the system kernel utility smit.

Generally, the user needs to connect to the root account, and it is recommended to restart the system after changing to properly apply even the kernel parameters applied in real-time.

#### Posix AIO

After running smit, move through "Devices", "Asynchronous I/O", and "Posix Asynchronous I/O", then change the "Defined" state of "Configure Defined Asynchronous I/O" to "Available".

However, if only this process is performed, the following process must be performed as the previous Posix AIO setting may be reset when the system is restarted.

After running smit, move the items in the order of “Devices”, “Asynchronous I / O”, “Posix Asynchronous I / O”, and “Change / Show Characteristics of Asynchronous I / O”, change the item of “STATE to be configured at system restart” to Available.

The current configuration of AIO-related kernel parameter can be checked as follows.

###### Check AIO related kernel parameter settings

```
# lsdev –C | grep aio
aio0         Available               Asynchronous I/O (Legacy)
posix_aio0  Available               Posix Asynchronous I/O
```

##### File Cache

The change method is as follows.

###### How to change file cache

```
# vmo -p -o minperm%=10
# vmo -p -o lru_file_repage=0
# vmo -p -o strict_maxclient=0
```

The confirmation method is as follows.

###### How to check file cache

```
# vmo –L
```

##### Resource Limitation

After running smit, move to "System Environments", "Change/Show Characteristics of Operating System", and change the "Maximum number of PROCESSES allowed per user" value to the number of processes that can be run simultaneously.

## User Settings

This describes resource limits, environment variables, and various environment settings of user accounts in the system for operating Altibase in the AIX OS.

For instructions and specifics related to configuration, refer to the guide provided by IBM.

### Resource Limitations

In the UNIX operating system, logical limits are set for available resources on a user account basis. Among the resource limit items, the items that need to be expanded for stable service operation as follows.

| Classification | Description | Recommended Value |
| --- | --- | --- |
| data seg size(data) | The maximum size of one process data area | unlimited |
| file size (fsize) | The maximum size of files that can be created | unlimited |
| open files (nofiles) | The maximum number of files that can be accessed simultaneously by one process | unlimited |
| max memory size (rss) | The maximum size of available memory | unlimited |
| virtual memory (memory) | The maximum size of available virtual memory | unlimited |
| max user process | The number of processes that can be created per user | unlimited |

This setting is intended to prevent problems caused by logical limits when the memory or datafile area used by a specific user expands, even though enough physical resources are available. This setting has no effect on other processes. It is recommended to set the maximum value allowed by the operating system, preferably `unlimited`.

For example, open files includes not only files accessed by the process but also communication sockets. If Altibase is operated in an environment where this value is limited to 10, more than 10 concurrent sessions are impossible. Considering the files used by Altibase itself, there may be no available session capacity.

To change these values, edit the environment configuration file using the `ulimit` command, edit the system resource configuration file, or use the kernel-related utilities provided by the operating system.

### Hard-Limit & Soft-Limit

Resource limit values are divided into the concept of hard-limit and soft-limit. The hard-limit means the maximum value of kernel-level resource limit that cannot be changed except the system administrator account (root), and the soft-limit means that the current user account can change up to the hard-limit. (refer to the ulimit -S/-H option for details.)

The soft-limit is effective while the user maintains a session by accessing it, and changes are immediately reflected. However, when other sessions of the same user account are connected, the existing soft-limit is reflected, so the ulimit command is often added to the user account configuration file.

However, this method may not be intended due to the global hard-limit, so it is recommended to systematically apply it through editing system-wide resource configuration files rather than applying user account units using environment configuration files.

For reference, the system configuration file related to the user resource limit in AIX is /etc/security/limits.

### Environment Variables

#### Setting for Multi-Threaded Applications

Separate environment variables need to be set for Altibase, a multi-thread based application program. For reference, this document mentions only representative ones, but it should be noted that all environment variables related to multi-threads supported by AIX need to be considered.

The following items are recommended environment variables to prevent performance degradation in multi-threaded SMP systems. Altibase can run without these environment variables, but they must be set because failures of unknown cause may occur later.

Among these settings, `PTHREAD_FORCE_SCOPE_SYSTEM`, an environment variable related to the MxN thread model, must also be set.

| Environment Variable | Description |
| --- | --- |
| AIXTHREAD_MNRATIO | The number of k kernel threads for processing n user threads |
| AIXTHREAD_SCOPE | Sets the thread model to 1:1 |
| PTHREAD_FORCE_SCOPE_SYSTEM | Environment variable related to the MxN thread model |
| AIXTHREAD_MUTEX_DEBUG | Set to remove the overhead of the pthread library due to the mutex / condition variable in use / read/write lock management used by the debugger. |
| AIXTHREAD_RWLOCK_DEBUG |  |
| AIXTHREAD_COND_DEBUG |  |
| SPINLOOPTIME | The number of attempts to acquire a lock in the state of CPU resource acquisition |
| YIELDLOOPTIME | The number of times to yield CPU resources while holding lock |
| MALLOCMULTIHEAP | Sets up in a multi-threaded environment that uses a lot of malloc |
| AIXTHREAD_MUTEX_FAST | This is an option to change the internal mutex_locking operation method of the operating system. If mutex_contention is severe, set it to ON to improve performance. It is provided in AIX 5.2 and later. |

More information on environmental variables can be found on the IBM website.

## Summary

For stable operation of Altibase on the AIX operating system, kernel parameter settings and user environment settings must be performed in advance. If the setting is not performed properly, it should be noted that the problem can be caused by each limit value even though the system has sufficient resources.

### Setting Examples

#### Kernel Parameters

Refer to the table below and set the appropriate kernel parameters. For reference, in AIX, some of the resource limit items are adjusted by changing kernel parameters.

| Classification | Kernel Parameter | Recommended Value | Remark |
| --- | --- | --- | --- |
| Posix AIO | Configure Defined Asynchronous I/O | Available | Required before AIX 6.1 |
| File Cache | lru_file_repage | 0 | Consider before AIX 6.1 (`lru_file_repage` is required) |
| File Cache | strict_maxclient | 0 |  |
| File Cache | minperm | 10 |  |
| Resource limitation | The maximum number of PROCESSES allowed per user | More than the number of processes that can be running simultaneously | Corresponds to max user process |

#### User Resource Limits

Refer to the table below, if possible, set it to unlimited.

| Classification | Description | Recommended Value |
| --- | --- | --- |
| data seg size(data) | The maximum size of the process data area | unlimited |
| file size (fsize) | The maximum size of the created file | unlimited |
| open files (nofiles) | The maximum number of files that can be accessed by one process at the same time | unlimited |
| max memory size (rss) | The maximum size of available memory | unlimited |
| max user process | The number of processes that can be created per user | Maximum number of PROCESSES allowed per user |

#### User Environment Variables

For sh, bash, and ksh, the following example shows how to set required environment variables in the environment configuration file. For csh, declare them with a shell command such as `setenv` instead of `export`.

###### User Environment Variable Setting Examples

```
#For Multi-Threaded Application
AIXTHREAD_MNRATIO=1:1; export AIXTHREAD_MNRATIO
AIXTHREAD_SCOPE=S; export AIXTHREAD_SCOPE
AIXTHREAD_MUTEX_DEBUG= OFF; export AIXTHREAD_MUTEX_DEBUG
AIXTHREAD_RWLOCK_DEBUG=OFF; export AIXTHREAD_RWLOCK_DEBUG
AIXTHREAD_COND_DEBUG = OFF; export AIXTHREAD_COND_DEBUG
SPINLOOPTIME = 1000; export SPINLOOPTIME
YIELDLOOPTIME = 50; export YIELDLOOPTIME
MALLOCMULTIHEAP=1; export MALLOCMULTIHEAP

# For Resource Limitation
ulimit –d unlimited  #data segment size, data
ulimit –f unlimited  #file size, fsize
ulimit –n unlimited  #file descriptor(open files), nofiles
ulimit –m unlimited  #max memory size, rss
```

For reference, in ksh, an error can occur when defining one environment variable by using another environment variable that has not already been defined.

## Enclosure

### AIX Memory Related Patches

There is a bug that can cause a memory leak in the heapmin function provided by the AIX platform.

Related IBM official document is as follows.

[http://www-01.ibm.com/support/docview.wss?uid=swg1IV28577](http://www-01.ibm.com/support/docview.wss?uid=swg1IV28577)

As a measure of this, the user must patch or upgrade to the AIX native compiler where AIX bug IV28577 is resolved.

Use the following command to check whether the patch is applied.

###### Check heapmin Related Patch

```
-bash-3.2$ instfix -i | grep IV28577
All filesets for IV28577 were found.
```

If the patch is not applied, no value is displayed. In that case, ask an AIX engineer to perform the patch or upgrade.

In addition, it is recommended to apply the latest patch to avoid various problems known in AIX.

### Limit of the Number of IPC Channels

Among the semaphore parameters of AIX, the semume value basically limits the number of semaphore undo entries. It is automatically set in AIX and set to 1024, and cannot be changed by the user.

Altibase uses undo entries to ensure resources between IPC connections, and from Altibase 5.1.5.72 or later, undo entries for each IPC channel have been changed from the previous two to use three.

Since the semume (number of undo entry resources) is fixed at 1024, Altibase uses 2 or 3 undo entries per IPC channel based on version 5.1.5.72, so the maximum number of IPC channels that can be used is limited.

Therefore, the maximum number of IPC channels that can be used for each version is as follows:

- In versions earlier than 5.1.5.72, up to 512 IPC channels (= 1024 / 2) can be used.
- In version 5.1.5.72 or later, up to 341 IPC channels (= 1024 / 3) can be used.
