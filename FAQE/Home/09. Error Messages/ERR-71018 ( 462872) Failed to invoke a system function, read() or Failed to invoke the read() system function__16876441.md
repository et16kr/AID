---
title: "ERR-71018 ( 462872) Failed to invoke a system function, read() or Failed to invoke the read() system function"
page_id: "16876441"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-71018+%28+462872%29+Failed+to+invoke+a+system+function%2C+read%28%29+or+Failed+to+invoke+the+read%28%29+system+function"
updated_at: "2021-03-30T15:25:18.000+0900"
version: 1
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# ERR-71018 ( 462872) Failed to invoke a system function, read() or Failed to invoke the read() system function
Source: https://docs.altibase.com/display/FAQE/ERR-71018+%28+462872%29+Failed+to+invoke+a+system+function%2C+read%28%29+or+Failed+to+invoke+the+read%28%29+system+function
Updated: 2021-03-30T15:25:18.000+0900

- [Overview](#ERR-71018(462872)Failedtoinvokeasystemfunction,read()orFailedtoinvoketheread()systemfunction-Overview) - [Type of error message](#ERR-71018(462872)Failedtoinvokeasystemfunction,read()orFailedtoinvoketheread()systemfunction-Typeoferrormessage) - [ALTIBASE HDB 4 ~ ALTIBASE HDB 5.3.3](#ERR-71018(462872)Failedtoinvokeasystemfunction,read()orFailedtoinvoketheread()systemfunction-ALTIBASEHDB4~ALTIBASEHDB5.3.3) - [ALTIBASE HDB 5.5.1 ~ later version](#ERR-71018(462872)Failedtoinvokeasystemfunction,read()orFailedtoinvoketheread()systemfunction-ALTIBASEHDB5.5.1~laterversion) - [Explanation of error messages](#ERR-71018(462872)Failedtoinvokeasystemfunction,read()orFailedtoinvoketheread()systemfunction-Explanationoferrormessages) - [Cause](#ERR-71018(462872)Failedtoinvokeasystemfunction,read()orFailedtoinvoketheread()systemfunction-Cause) - [Major error code](#ERR-71018(462872)Failedtoinvokeasystemfunction,read()orFailedtoinvoketheread()systemfunction-Majorerrorcode) - [Major occurrence case](#ERR-71018(462872)Failedtoinvokeasystemfunction,read()orFailedtoinvoketheread()systemfunction-Majoroccurrencecase) - [Solution](#ERR-71018(462872)Failedtoinvokeasystemfunction,read()orFailedtoinvoketheread()systemfunction-Solution) - [Reference](#ERR-71018(462872)Failedtoinvokeasystemfunction,read()orFailedtoinvoketheread()systemfunction-Reference)

# Overview

---

When connecting to the DB using the TCP connection type When the DB client program does not close the DB connection (session close) normally, related error messages are recorded in altibase_boot.log.

This document describes the type and cause of the message.

# Type of error message

---

Error messages are recorded in all versions of ALTIBASE HDB, and error messages vary slightly depending on the ALTIBASE HDB version.

### ALTIBASE HDB 4 ~ ALTIBASE HDB 5.3.3

ERR-71018(errno=238) Failed to invoke a system function, read()

ERR-71019(errno=104) Failed to invoke a system function, write()

### ALTIBASE HDB 5.5.1 ~ later version

ERR-71018(errno=238) Failed to invoke the read() system function

ERR-71019(errno=104) Failed to invoke the write() system function

# Explanation of error messages

---

The Altibase server has a 'session manager thread' that monitors the connection between the client and the Altibase server.

In general, when a client process terminates abnormally, the session connected with that client can immediately detect its status. However, when the work inside the Altibase server, which is not related to the session work, is being performed for a long time, the session cannot check the connection status between the client and the Altibase server. So, a 'session management thread' is placed to periodically monitor the connection status of the session.

ERR-71018(errno=113) Failed to invoke a system function, read() ERR-71019(errno=104) Failed to invoke a system function, write()

The above error codes (ERR-71018,71019) are messages indicating that this thread has detected that the connection with the client has been disconnected and that the session has been cleaned up.

Error code ERR-71018 means its waiting for the client's request, Error code ERR-71019 means that it has detected that the connection has been lost while responding to the client.

# Cause

---

The cause of the disconnection can be inferred through the system error code errno.

ERR-71018(errno=113) Failed to invoke a system function, read()

ERR-71019(errno=104) Failed to invoke a system function, write()

Among the above error messages, errno=113 and errno=104 represent system error codes.

### Major error code

The mainly occurring errors are as follows.

- ECONNRESET

  This error code sets ECONNRESET to errno when the Altibase server receives an RST packet from the client. The RST packet is when the client announces that the connection is no longer valid.

  | OS | System error code |
  | --- | --- |
  | Linux | 104 |
  | AIX | 73 |
  | HP-UX | 232 |
  | SUN | 131 |
  | Windows | 10054 |
- ETIMEDOUT

  In TCP communication, if there is no response to the session, the OS tries to retransmit the packet several times to check the connection status. If there is no response during the set time, ETIMEDOUT occurs.

  | OS | System error code |
  | --- | --- |
  | Linux | 110 |
  | AIX | 78 |
  | HP-UX | 238 |
  | SUN | 145 |
  | Windows | 10060 |

  To check system error code

  For Linux, error codes are defined in the /usr/include/asm-x86_64/errno.h file.

  In the case of AIX, error codes are defined in the /usr/include/errno.h file.

  If there is a header file (errno.h) defined for the error code in other OS, the meaning of the error code can be checked by referring to the file.

### Major occurrence case

This can often occur in situations where the TCP session connected between the DB client and the DB server is forcibly terminated.

- L4, when idle TCP session is forcibly organized by firewall
- LAN card, mechanical error of other network equipment
- Abnormal termination or restart of DB client program

# Solution

---

There is no action that the Altibase server can take as a message indicating that the Altibase server has detected that the connection to the client has been lost and has cleaned up the fine lines.

# Reference

---

In a replication environment, the same error message may occur in altibase_rp.log. This occurs when the redundant sender detects that the receiver is shutting down during replication log transmission.
