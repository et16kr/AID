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

DB connection termination messages occur when an Altibase client program connects to the Altibase server through TCP and does not close the DB connection (session close) normally. In this case, related error messages are recorded in the Altibase server trace log file, altibase_boot.log.

This document describes the types and causes of these error messages.

# Type of error message

---

The error messages recorded differ slightly depending on the Altibase version.

### ALTIBASE HDB 4 ~ ALTIBASE HDB 5.3.3

- ERR-71018(errno=238) Failed to invoke a system function, read()
- ERR-71019(errno=104) Failed to invoke a system function, write()

### ALTIBASE HDB 5.5.1 or later

- ERR-71018(errno=238) Failed to invoke the read() system function
- ERR-71019(errno=104) Failed to invoke the write() system function

# Explanation of error messages

---

The Altibase server **session manager thread** periodically checks the connection status between the client and the Altibase server. These messages indicate that the session manager thread detected a disconnected client connection and cleaned up the corresponding session.

The session manager thread performs the following roles:

1. **Detect abnormal client termination**
   When a client process terminates abnormally, the connected session detects the status and closes the session.
2. **Check connection status during internal server work**
   Even when the Altibase server is performing internal work and cannot check connection status in real time, the session manager thread checks it periodically.

#### Error message meaning

- **ERR-71018**
  Indicates that the connection was lost while waiting for a client request. (`read()` call failure)
- **ERR-71019**
  Indicates that the connection was lost while sending a response to the client. (`write()` call failure)

# Cause

---

The cause of the error can be inferred from the **system error code (errno)**.

- ERR-71018(errno=113) Failed to invoke a system function, read()
- ERR-71019(errno=104) Failed to invoke a system function, write()

### Major error code

The major system error codes are as follows.

#### 1. ECONNRESET

- This occurs when the client sends an **RST packet**, which indicates that the connection is no longer valid.
- When the Altibase server receives an RST packet from the client, it sets errno to **ECONNRESET**.

**System error code**

- Linux: 104
- AIX: 73
- HP-UX: 232
- SUN: 131
- Windows: 10054

#### 2. ETIMEDOUT

- This occurs when there is no response from the client during TCP communication.
- The OS retransmits packets to check connection status, and if there is no response within the configured time, **ETIMEDOUT** occurs.

**System error code**

- Linux: 110
- AIX: 78
- HP-UX: 238
- SUN: 145
- Windows: 10060

#### Reference material

- Linux: /usr/include/asm-x86_64/errno.h
- AIX: /usr/include/errno.h
- Other OS: refer to the errno.h header file

### Major occurrence case

TCP session termination errors often occur in the following situations:

#### 1. Network environment issue

- An **idle TCP session** is forcibly cleaned up by an L4 switch or firewall.
- Mechanical failure of a LAN card or other network equipment.

#### 2. DB client issue

- Abnormal termination or restart of the DB client program.

# Solution

---

This message indicates that the Altibase server detected that the connection to the client was lost and cleaned up the session. No additional action is required on the server side.

# Reference

---

- In a replication environment, a similar error message may be recorded in altibase_rp.log.
- This occurs when the **replication Sender** detects that the **Receiver** has stopped while sending replication logs.
