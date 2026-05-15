---
title: "altibase_boot.log - TRY_COUNT, LOCK_COUNT, MISS_COUNT"
page_id: "22642967"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/altibase_boot.log+-+TRY_COUNT%2C+LOCK_COUNT%2C+MISS_COUNT"
updated_at: "2025-10-20T15:46:23.000+0900"
version: 1
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# altibase_boot.log - TRY_COUNT, LOCK_COUNT, MISS_COUNT
Source: https://docs.altibase.com/display/FAQE/altibase_boot.log+-+TRY_COUNT%2C+LOCK_COUNT%2C+MISS_COUNT
Updated: 2025-10-20T15:46:23.000+0900

# - [Overview](#altibase_boot.log-TRY_COUNT,LOCK_COUNT,MISS_COUNT-Overview) - [Situation](#altibase_boot.log-TRY_COUNT,LOCK_COUNT,MISS_COUNT-Situation) - [Cause](#altibase_boot.log-TRY_COUNT,LOCK_COUNT,MISS_COUNT-Cause) - [6.3.1 or earlier](#altibase_boot.log-TRY_COUNT,LOCK_COUNT,MISS_COUNT-6.3.1orearlier) - [6.5.1](#altibase_boot.log-TRY_COUNT,LOCK_COUNT,MISS_COUNT-6.5.1) - [7.1 or later](#altibase_boot.log-TRY_COUNT,LOCK_COUNT,MISS_COUNT-7.1orlater) - [Solution](#altibase_boot.log-TRY_COUNT,LOCK_COUNT,MISS_COUNT-Solution)

# Overview

---

In altibase_boot.log, a large number of messages with the title "reset Mutex Statistics" may be recorded. This document provides a brief description of this message.

# Situation

---

The following message may be repeatedly recorded in altibase_boot.log.

**Message format**

--- reset Mutex Statistics --- TRY_COUNT: 2102048999 LOCK_COUNT: 2147483647 MISS_COUNT: 59144056 ------------------------------

# Cause

---

This message is output when the values of the try_count, lock_count, and miss_count columns of the v$mutex performance view table exceed the maximum value and the values are initialized.This message appears when the values of the `try_count`, `lock_count`, and `miss_count` columns in the performance view table `v$mutex` exceed their maximum limit and are reset.

`v$mutex` records mutex-related information for concurrency control within the database. When the values of these columns continuously increase and exceed the maximum limit, a value overflow occurs. At that point, the values are logged in `altibase_boot.log` and then reset to zero.

Column description

- try_count = number of mutex lock attempts
- lock_count = number of successful mutex locks
- miss_count = number of waits because the mutex lock was not held

### 6.3.1 or earlier

**V$MUTEX table structure**

iSQL> desc v$mutex; [ ATTRIBUTE ] ----------------------------------------------------- NAME TYPE ----------------------------------------------------- NAME VARCHAR(64) **TRY_COUNT INTEGER** // If the integer maximum value (2147483647) is exceeded, it will be logged. LOCK_COUNT INTEGER MISS_COUNT INTEGER SPIN_VALUE INTEGER TOTAL_LOCK_TIME_US BIGINT MAX_LOCK_TIME_US BIGINT

### 6.5.1

**V$MUTEX table structure**

`iSQL> desc v$mutex`

`[ ATTRIBUTE ]`

`------------------------------------------------------------------------------`

`NAME                                     TYPE`

`------------------------------------------------------------------------------`

`NAME                                     VARCHAR(``64``)`

`TRY_COUNT                                BIGINT``// When the BIGINT maximum value (9223372036854775807) is exceeded, the event is logged.`

`LOCK_COUNT                               BIGINT`

`MISS_COUNT                               BIGINT`

`SPIN_VALUE                               INTEGER`

`TOTAL_LOCK_TIME_US                       BIGINT`

`MAX_LOCK_TIME_US                         BIGINT`

### 7.1 or later

**V$MUTEX table structure**

`iSQL> desc v$mutex`

`[ ATTRIBUTE ]`

`------------------------------------------------------------------------------`

`NAME                                     TYPE`

`------------------------------------------------------------------------------`

`NAME                                     VARCHAR(``64``)`

`TRY_COUNT                                BIGINT``// When the BIGINT maximum value (9223372036854775807) is exceeded, the event is logged.`

`LOCK_COUNT                               BIGINT`

`MISS_COUNT                               BIGINT`

`SPIN_VALUE                               INTEGER`

`TOTAL_LOCK_TIME_US                       BIGINT`

`MAX_LOCK_TIME_US                         BIGINT`

`THREAD_ID                                VARCHAR(``64``)``// The ID of the thread that currently holds the lock`

# Solution

---

When the maximum number of columns that can store mutex-related information is reached, the information is recorded in altibase_boot.log, and there is no particular problem or action required.
