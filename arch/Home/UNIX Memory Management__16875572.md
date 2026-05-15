---
title: "UNIX Memory Management"
page_id: "16875572"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/UNIX+Memory+Management"
updated_at: "2025-09-23T09:38:50.000+0900"
version: 7
ancestors: ["Home"]
labels: []
---

# UNIX Memory Management
Source: https://docs.altibase.com/display/arch/UNIX+Memory+Management
Updated: 2025-09-23T09:38:50.000+0900

- [Overview](#UNIXMemoryManagement-Overview) - [Solaris System Administration Techniques](#UNIXMemoryManagement-SolarisSystemAdministrationTechniques) - [Memory Allocation](#UNIXMemoryManagement-MemoryAllocation) - [Insufficient Memory](#UNIXMemoryManagement-InsufficientMemory) - [pmap](#UNIXMemoryManagement-pmap) - [Memory Management Policy for AIX system](#UNIXMemoryManagement-MemoryManagementPolicyforAIXsystem) - [Classification of Memory](#UNIXMemoryManagement-ClassificationofMemory) - [Insufficient Memory](#UNIXMemoryManagement-InsufficientMemory.1) - [svmon](#UNIXMemoryManagement-svmon) - [Memory Management Policy for HP](#UNIXMemoryManagement-MemoryManagementPolicyforHP) - [Allocation of Memory](#UNIXMemoryManagement-AllocationofMemory) - [Insufficient memory](#UNIXMemoryManagement-Insufficientmemory) - [Checking memory usage](#UNIXMemoryManagement-Checkingmemoryusage) - [Memory Management Policy for Linux](#UNIXMemoryManagement-MemoryManagementPolicyforLinux) - [Linux Memory Management](#UNIXMemoryManagement-LinuxMemoryManagement) - [Checking Linux memory](#UNIXMemoryManagement-CheckingLinuxmemory) - [Why doesn't the vsz decrease?](#UNIXMemoryManagement-Whydoesn'tthevszdecrease?)

# Overview

---

This document describes how to manage the memory requested by a process on a UNIX system.

Therefore, for in-depth understanding, please refer to the documents provided by each vendor.

For errors and improvements related to this document, please contact the technical support portal or technical support center.

- Technical support portal: [http://support.altibase.com](http://support.altibase.com/)[/en/](http://support.altibase.com/en/)
- Technical support center: 02-2082-1114

# Solaris System Administration Techniques

---

This section describes the memory management of the Solaris operating system.

## Memory Allocation

---

Solaris allocates memory in the form of reserved. The reserved area exists in the swap area.

In other words, when a process requests 10M, it first allocates 10M to the swap area, and when the process actually accesses the memory, 10M is allocated to the physical memory.

Therefore, Solaris cannot run any process if the swap area is insufficient.

```
-bash-4.0$ /usr/sbin/swap -s
total: 3610640k bytes allocated + 1939792k reserved = 5550432k used, 36742272k available
```

As in the example of the code box above, when looking at the swap information, it can be seen that the swap area is being written even when the actual physical memory is available. This is because Solaris itself has a policy of unconditionally allocating the reserved area to memory requests.

The following shows the change of VSZ/swap area on the code.

|  | Memory Allocation | Reserved(Swap) | VSZ |
| --- | --- | --- | --- |
| 1. Request | P = malloc(100M) | 100M | 0M |
| 2. Actual usage | For (i=0; i<10M;i++)*(p+1) = 1 | 90M | 10M |

Even if it is allocated in the actual code, the memory does not increase immediately. After that, it can be seen that the memory usage increases at the actual access point.

## Insufficient Memory

---

By default, Solaris uses free memory for file cache.

This condition is basically used as a file cache only when the physical memory is more than the value set to lotsfree (1/6 of the total memory).

(Version earlier than 5.1, when free memory is needed, the file cache option had to be given so that it can be selected first, but from version 5.8 or later, the file cache is also stored in free memory by default. Therefore unlike AIX/HP, there is no need for the user to set a separate setting.)

However, it if starts to be kept below lotsfree, the system starts searching memory pages to find pages that are not recently used. (These search numbers appear in the sr part of the vmstat information.)

To keep lotsfree, infrequently accessed pages are loaded into memory and operated to fill the lotsfree level.

This operation is referred to as swap (swapping). (In vmstat, fr means the number of free pages in the memory, but free means that the page in the memory is updated to disk if there is changed information. It shows a phenomenon that the performance is deteriorated.)

## pmap

---

Solaris provides a utility for inquiring about the actual use part of the process as follows.

```
-bash-4.0$ pmap -F 22748
0000000100D22000       8560K rwx--  /home1/hjkim/altibase/5.1.5.72/bin/altibase
000000010157E000     488320K rwx--    [ heap ]
FFFFFFFF72EFE000          8K rw--R    [ stack tid=74 ]
FFFFFFFF730FC000         16K rw--R    [ anon ]
FFFFFFFF732FC000         16K rw--R    [ anon ]
FFFFFFFF73C00000      10240K rw-s-  dev:118,46 ino:45717892
```

The top will be the process memory, and the heap area will be the area where the DB and etc. are located. The meaning of anon refers to an area at the time of initial access to a page with MMAP_PRIVATE mapping. ino and etc. can be seen as the redo log buffer area uploaded by mmp.

# Memory Management Policy for AIX system

---

This section describes the memory management policy for the AIX system.

## Classification of Memory

---

To understand the memory usage of AIX, first, the definition of the classification of memory will be described.

| Classification | Description |
| --- | --- |
| Persistent | Area used for JFS file cache |
| Client | Area used for file cache of CDROM, NFS, JFS2 |
| Computational | Area such as process stack, heap, and share memory |

For a better understand, we are going to explain with the result of svmon. (All results of svmon are page units, and 1 page is basically 4K unless otherwise indicated.)

Shell> svmon –G

size inuse free pin virtual

memory 2031616 1779678 251938 474697 1682009

pg space 4128768 495129

work pers clnt other

pin 404863 0 0 69834

in use 1225427 5 554246

The above results are first described in the table below.

| items (in the red box) | Description |
| --- | --- |
| free | number of pages not in use in physical memory |
| inuse | (Computational + Persistent) number of physical memory pages in actual use |
| pg space | Usage of paging space |
| pin | Number of pages of physical memory that cannot be swapped out |
| size | Number of pages of total physical memory. 1 page is 4,096 bytes, so it is a system with 7936M of memory. |
| virtual | Number of pages created by VMM (Virtual Memory Manager) |

The sum of the pins outside the red text is the same as the capacity of the pins in the red box, and the inuse is also the same. Please note that even if the user is using the same inuse, the user can confirm that some of them are being used as file cache.

## Insufficient Memory

---

Generally, AIX tries to use all of the free memory as file cache.

Therefore, in the case of insufficient memory, it operates as follows. If the amount of memory being used for the file cache is greater than MAXPERM, the memory is unconditionally stolen from the file cache.

If it is between MAXPERM AND MINPERM, it will steal from the side that is judged to have less I/O among the file cache and computational memory.

Therefore, depending on the size of MAXPERM's set value, a part of the memory that has been well used from the perspective of the process may be swapped to the paging space area, causing disk I/O when re-accessing, resulting in jitter in performance.

When using Altibase, it is recommended to set several properties in AIX5.2ML04 or later to eliminate such jitter as possible.

For more detailed information, please refer to "Altibase Environment Configuration Guide for AIX" or the technical document related to performance tuning distributed in AIX.

| Related property | Description |
| --- | --- |
| MAXPERM | Maximum share of physical memory used for file cache (soft limit) |
| MINPERM | Minimum share of physical memory used for file cache |
| NUMPERM | Occupation of the area used as actual file cache (check with vmtune,vmo) |
| MAXCLIENT | Maximum share of the file cache used by NFS, JFS2, etc. |
| stric_maxperm | If set to 1, MAXPERM is maintained |
| lru_file_repage | When set to 0, it is forcibly designated to occur only in file cache such as JFS2 for steals that occur when memory is insufficient. |

## svmon

---

On AIX, the actual memory usage of a process can be checked in detail with svmon.

```
 Shell> svmon -P 356528
-------------------------------------------------------------------------------
Pid   Command       Inuse      Pin     Pgsp  Virtual 64-bit Mthrd  16MB
356528 altibase         37992     8380    59579    96475    Y     Y     N
PageSize      Inuse        Pin       Pgsp    Virtual
s   4 KB      29224       8332      59579      87707
m  64 KB       548          3          0        548
```

Generally, svmon is not the information that provides snapshots and should be viewed as statistical information.

Therefore, the memory usage and the result of svmon, which are checked with a command such as (psv [process id]), may be different.

However, the user needs to carefully pay attention to the pgsp item. The fact that this part is increasing means that there is actually insufficient memory or that the computation memory area has been stolen and swapped, and from the standpoint of ALTIBASE, it is a problem that can cause performance degradation, so the user should check and adjust the file cache setting.

As shown below, The user can also check the actual memory usage by using the ps command.

```
Shell> ps v 356528
PID    TTY STAT  TIME PGIN  SIZE     RSS   LIM  TSIZ   TRS  %CPU  %MEM
356528      - A    29:37  4700  290328  77688    xx  17933  3396    0.1    1.0
```

The analysis problem in the results of ps and svmon is that the sum of the issue part of svmon must match the size of the actual ps result, but in the case of page-out, the ps side is actually displayed larger.

# Memory Management Policy for HP

---

This section describes the memory management of the HP operating system.

## Allocation of Memory

---

HP's memory allocation policy has something to do with what we call arena.

For details, check with malloc with man-page. To the point, the system manages a memory pool (arena) to allocate memory. In the case of the threaded program, memory is allocated with this arena.

If the number of threads increases by a lot, performance can be improved in terms of concurrency by adjusting the number of the arena. (In the case of non-thread, memory is allocated with only one arena.)

```
Shell> export _M_ARENA_OPT=16:8
```

If the environment is configured as above, threads are allocated memory with 16 arenas, which means that if the arena's memory pool becomes insufficient, it will operate in the form of expanding the memory pool in unites of (8*4096 bytes).

(If the expansion unit is too large, the memory may increase rapidly, so many testings are required when setting this environment. The default value is 8:32)

## Insufficient memory

---

Since the swapping policy is not different from other operating systems, separate explanations are omitted.

## Checking memory usage

---

Commonly, it is possible to check with Glance.

|  |
| --- |
| If branching to "m" after running Shell> glance, the overall system memory status can be checked. If "M" is pressed to designate a process after pressing "s", the memory usage type of the process can be checked. |

For versions with pmap, pmap can be used.

```
rx6600:[/] pmap 12379
12379:  /altibase_home/bin/altibase -p boot from admin
OFFSET            VSZ    RSZ     TYPE     PRM  FILE
0                    4K     4K     SD(170)  r-- [nullderef]
4000000000000000  15.1M  11.5M     SC(2)    r-x [text]
6000000000000000   901M   658M    PD       rw- [data]
9fffffff7d67f000     72K    64K       PD       rw- [uarea]
9fffffff7d7af000     72K    64K       PD       rw- [uarea]
```

In HP, the exact memory usages of a process can be checked with the map command. The result is similar to that of Solaris.

HP can adjust the settings for file cache in the same way as AIX. Since these values are related to the overall performance, the recommended value is variable depending on the situation, but in general, it is recommended to set 5%(min)/15%(max).

| Kernel property | Description |
| --- | --- |
| dbc_max_pct | Maximum threshold of memory to be used for file cache |
| dbc_min_pct | Minimum threshold of memory to be used for file cache |

# Memory Management Policy for Linux

---

This section describes the memory management of the Linux operating system.

## Linux Memory Management

---

Linux has a memory usage policy similar to AIX for the file cache part. In other words, it tries to use all the free memory as a file cache. However, starting with kernel 2.6, there is a limit on this part, and the usage of file cache can be limited.

|  |
| --- |
| Shell> cat /proc/sys/vm/swappiness When configuring, use sysctl. |

Basically, it is set to 60(%), and there are some complex arithmetic expressions, but when the physical memory starts to be used beyond the value set in swappiness, swapping starts unconditionally.

This is because the Linux system itself generates swapping in an effort to secure the file cache below the set value.

However, since this part incurs a cost due to swapping that the user wants or does not want, it can worsen the system performance. Although currently, Altibase does not make any special recommendations, it is recommended to set this kernel value to “0” in MySQL and etc.

## Additional conditions to Arena-related matters (when writing)

- This feature was added in red Hat Enterprise Linux 6 to improve performance issues due to memory contention between threads in a multi-threaded application environment.
- The default value is the number of CPU core * MALLOC_ARENA_TEST.
- The default value of MALLOC_ARENA_TEST environment variable
    - 2 for 32-bit
    - 8 for 64-bit
- The MALLOC_ARENA_MAX environment variable operates properly in glibc2.10 or later.

## Checking Linux memory

---

The memory usage of a process can be checked with the top or map command.

# Why doesn't the vsz decrease?

---

Generally, the operating system returns the memory area used by the process to the free area only when the process ends.

In other words, even if a process calls free() on a memory area explicitly allocated by a user, the area is not released immediately.

This is because kernel cost can have a significant performance impact if the memory manager of the operating system expects the process to reuse the freed memory area by the process to remain in the form of a fragment and reconfigured to a free-list of allocable segments.

Therefore, even if the process is free(), the operating system sees a phenomenon in which the size of the VSZ does not decrease with an actual monitoring tool, for the reason described above.

# Korean Source Attachments

The Korean source page also references these downloadable source attachments. They are preserved here so the English document set does not lose those references.

- [Korean source attachment 1 (PDF)](https://docs.altibase.com/download/attachments/13436842/UNIX_Memory_Management.pdf?version=1&modificationDate=1698104488000&api=v2)
