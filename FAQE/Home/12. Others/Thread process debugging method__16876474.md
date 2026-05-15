---
title: "Thread process debugging method"
page_id: "16876474"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Thread+process+debugging+method"
updated_at: "2021-04-05T13:30:06.000+0900"
version: 3
ancestors: ["Home", "12. Others"]
labels: []
---

# Thread process debugging method
Source: https://docs.altibase.com/display/FAQE/Thread+process+debugging+method
Updated: 2021-04-05T13:30:06.000+0900

- [Overview](#Threadprocessdebuggingmethod-Overview) - [Using pstack](#Threadprocessdebuggingmethod-Usingpstack) - [How to use](#Threadprocessdebuggingmethod-Howtouse) - [Example](#Threadprocessdebuggingmethod-Example) - [Using dbx](#Threadprocessdebuggingmethod-Usingdbx) - [How to use](#Threadprocessdebuggingmethod-Howtouse.1) - [Example](#Threadprocessdebuggingmethod-Example.1) - [Using gdb](#Threadprocessdebuggingmethod-Usinggdb) - [How to use](#Threadprocessdebuggingmethod-Howtouse.2) - [Example](#Threadprocessdebuggingmethod-Example.2)

# Overview

---

When a process on Unix consumes excessive CPU or hangs, the process debugging utilities provided by each Unix OS can help identify the cause by analyzing the currently running call stack.

Unix process debugging methods differ by utility and by Unix variant, so commands are often confused. This document explains simple commands for viewing each thread stack.

# Using pstack

---

`pstack` is provided by Sun, several other Unix variants, and Linux. It is useful for viewing the call stack of a running process by thread, and can be used when a database hang occurs.

## How to use

---

- Linux:

  ```
  shell> pstack processid
  ```

- Sun:

  ```
  shell> pstack -F processid
  ```

## Example

---

**Example**

```
[omegaman@as48-x64 ~]$ uname -a
Linux as48-x64 2.6.9-89.ELsmp #1 SMP Mon Apr 20 10:33:05 EDT 2009 x86_64 x86_64 x86_64 GNU/Linux
[omegaman@as48-x64 ~]$
[omegaman@as48-x64 ~]$ whereis pstack
pstack: /usr/bin/pstack /usr/share/man/man1/pstack.1.gz
[omegaman@as48-x64 ~]$ ps -ef | grep altibase | grep omegaman
omegaman 16745 16454  0 13:55 pts/2    00:00:00 grep altibase
omegaman 22978     1  0 Dec04 ?        00:00:07 /home/omegaman/altibase_home/bin/altibase -p boot from admin
[omegaman@as48-x64 ~]$ pstack 22978      :22978 is  a process id of altibase
Thread 41 (Thread 1084229984 (LWP 22979)):
#0  0x00000039070c2f56 in __select_nocancel () from /lib64/tls/libc.so.6
#1  0x0000000000f40f4b in idvClockThread::run ()
#2  0x0000000000ef797c in idtBaseThread::staticRunner ()
#3  0x0000003907706137 in start_thread () from /lib64/tls/libpthread.so.0
#4  0x00000039070c9f03 in clone () from /lib64/tls/libc.so.6
Thread 40 (Thread 1094719840 (LWP 22980)):
```

# Using dbx

---

`dbx` is provided by AIX, HP, and Sun. You can check call stack information for a running process with the `dbx` command, and you can also check the stack for each thread in a core file.

This section describes the method used on AIX as an example.

## How to use

---

1. Check the process ID of the process in question: `shell> ps -eafl | grep altibase`
2. Attach to the process: `shell> dbx -a <pid of altibase process>`
3. View all thread information: `(dbx) thread`
4. View only individual thread information: `(dbx) thread current <thread number>` and `(dbx) where`
5. Detach: `(dbx) detach`

  Always execute the detach command to release the connected process. If you exit without detaching, the target process may also be terminated.
6. Exit: `(dbx) quit`

## Example

---

```
$ dbx -a 421920 Waiting to attach to process 421920 ... Successfully attached to altibase. warning: Directory containing altibase could not be determined. Apply 'use' command to initialize source path.

Type 'help' for help. reading symbolic information ...warning: no source compiled with -g

stopped in _event_sleep at 0x9000000004b6a84 ($t6) 0x9000000004b6a84 (_event_sleep+0xe8) e8410028 ld r2,0x28(r1) (dbx) where _event_sleep(??, ??, ??, ??, ??, ??) at 0x9000000004b6a84 _event_wait(??, ??) at 0x9000000004b6f5c _cond_wait_local(??, ??, ??) at 0x9000000004c305c _cond_wait(??, ??, ??) at 0x9000000004c3628 pthread_cond_timedwait(??, ??, ??) at 0x9000000004c3e38 run()() at 0x100187228 staticRunner(void*)() at 0x10007ea70 (dbx) list no source file (dbx) detach
```

# Using gdb

---

If `gdb` (GNU debugger) is installed, stack information for each thread can be checked by using `gdb`.

## How to use

---

1. Attach `gdb` to the target process: `shell> $gdb $ALTIBASE_HOME/bin/altibase process-id`
2. Print information for each thread: `(gdb) info threads`
3. Print the stack trace of all threads: `(gdb) thread apply all bt`
4. Switch to a specific thread: `(gdb) t 1` switches to thread 1.
5. Print the current thread's stack: `(gdb) bt`
6. Quit: `(gdb) quit`

## Example

---

```
$gdb $ALTIBASE_HOME/bin/altibase 34567 gdb> info threads 42 Thread 31 (LWP 4) 0x329614 in _poll () 41 Thread 30 0x300cf8 in _lwp_sema_wait () 40 Thread 29 0x300cf8 in _lwp_sema_wait () 39 Thread 28 (LWP 29) 0x329614 in _poll () 38 Thread 27 (LWP 28) 0x329614 in _poll () 37 Thread 26 (LWP 27) 0x329614 in _poll () 36 Thread 25 (LWP 26) 0x329614 in _poll () 5 LWP 28 0x329614 in _poll () 4 LWP 29 0x329614 in _poll () 3 LWP 30 0x300cf8 in _lwp_sema_wait () * 2 Thread 1 (LWP 1) 0x329614 in _poll () 1 LWP 1 0x329614 in _poll ()  gdb> thread apply all bt; Output stack trace of all threads Thread 2 (Thread 1 (LWP 1)): #0 0x329614 in _poll () #1 0x2f2548 in select_large_fdset () #2 0x286908 in __1cKidcManagerGselect6FpnGfd_set_pnOPDL_Time_Value__i_ () #3 0x978d8 in __1cMmmtThreadMgrIDispatch6M_nGIDE_RC__ () #4 0x945f4 in __1cGmmiMgrIMainLoop6F_nGIDE_RC__ () #5 0x929e0 in main ()  Thread 1 (LWP 1 ): #0 0x329614 in _poll () #1 0x2f2548 in select_large_fdset () #2 0x286908 in __1cKidcManagerGselect6FpnGfd_set_pnOPDL_Time_Value__i_ () #3 0x978d8 in __1cMmmtThreadMgrIDispatch6M_nGIDE_RC__ () ---Type to continue, or q to quit--- #4 0x945f4 in __1cGmmiMgrIMainLoop6F_nGIDE_RC__ () #5 0x929e0 in main () #0 0x329614 in _poll ()  gdb> t 1 ; Switch to thread 1 gdb> bt ; Output stack gdb> quit
```
