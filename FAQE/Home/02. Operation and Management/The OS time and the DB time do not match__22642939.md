---
title: "The OS time and the DB time do not match"
page_id: "22642939"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/The+OS+time+and+the+DB+time+do+not+match"
updated_at: "2025-10-20T15:21:06.000+0900"
version: 1
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# The OS time and the DB time do not match
Source: https://docs.altibase.com/display/FAQE/The+OS+time+and+the+DB+time+do+not+match
Updated: 2025-10-20T15:21:06.000+0900

- [Overview](#TheOStimeandtheDBtimedonotmatch-Overview) - [Version](#TheOStimeandtheDBtimedonotmatch-Version) - [Symptoms](#TheOStimeandtheDBtimedonotmatch-Symptoms) - [OS time change](#TheOStimeandtheDBtimedonotmatch-OStimechange) - [Time Zone Change](#TheOStimeandtheDBtimedonotmatch-TimeZoneChange) - [DST (Daylight Saving Time) Application](#TheOStimeandtheDBtimedonotmatch-DST(DaylightSavingTime)Application)

# **Overview**

---

During DB server operation (with Altibase running), if the OS time zone is changed or daylight saving time (DST) is applied, the OS time and the DB (sysdate) time may not match.

In such cases, a DB restart is required to ensure accurate time synchronization.

(Note: This document is based on the Linux OS, and the methods for checking and changing settings may differ for other Unix systems.)

# **Version**

---

All versions of ALTIBASE HDB

# **Symptoms**

---

## OS time change

After changing the OS time, querying the time in Altibase returns the correct result.

| OS Check | Altibase Check |
| --- | --- |
| [root@master ~]# **timedatectl set-time "2025-08-20 12:00:00"**<br>[root@master ~]# timedatectl<br>Local time: Wed **2025-08-20 12:00:02** KST<br>Universal time: Wed 2025-08-20 03:00:02 UTC<br>RTC time: Wed 2025-08-20 03:00:02<br>Time zone: Asia/Seoul (KST, +0900)<br>NTP enabled: n/a<br>NTP synchronized: no<br>RTC in local TZ: no<br>DST active: n/a | iSQL> SELECT TO_CHAR(SYSDATE, 'YYYY-MM-DD HH:MI:SS.SSSSSS') FROM DUAL;<br>TO_CHAR(SYSDATE,'YYYY-MM-DDHH:MI:SS.SSSSSS<br>-----------------------------------------------------------------------------------<br>**2025-08-20 12:00:02**.267024<br>1 row selected |

## Time Zone Change

After changing the time zone, a time discrepancy occurs when querying the time in Altibase → DB restart is required

| OS Check | Altibase Check |
| --- | --- |
| [root@master ~]# **timedatectl set-timezone Europe/Istanbul**<br>[root@master ~]# timedatectl<br>Local time: Wed **2025-08-20 06:01:44** +03<br>Universal time: Wed 2025-08-20 03:01:44 UTC<br>RTC time: Wed 2025-08-20 03:01:45<br>Time zone: Europe/Istanbul (+03, +0300)<br>NTP enabled: n/a<br>NTP synchronized: no<br>RTC in local TZ: no<br>DST active: n/a | iSQL> SELECT TO_CHAR(SYSDATE, 'YYYY-MM-DD HH:MI:SS.SSSSSS') FROM DUAL;<br>TO_CHAR(SYSDATE,'YYYY-MM-DDHH:MI:SS.SSSSSS<br>-----------------------------------------------------------------------------------<br>**2025-08-20 12:01:44**.679908<br>1 row selected. |
|  | Restart Altibase |
| [root@master ~]# timedatectl<br>Local time: Wed **2025-08-20 06:03:30** +03<br>Universal time: Wed 2025-08-20 03:03:30 UTC<br>RTC time: Wed 2025-08-20 03:03:31<br>Time zone: Europe/Istanbul (+03, +0300)<br>NTP enabled: n/a<br>NTP synchronized: no<br>RTC in local TZ: no<br>DST active: n/a | iSQL> SELECT TO_CHAR(SYSDATE, 'YYYY-MM-DD HH:MI:SS.SSSSSS') FROM DUAL;<br>TO_CHAR(SYSDATE,'YYYY-MM-DDHH:MI:SS.SSSSSS<br>-----------------------------------------------------------------------------------<br>**2025-08-20 06:03:30**.983508<br>1 row selected. |

## DST (Daylight Saving Time) Application

After DST (Daylight Saving Time) changes, a time discrepancy occurs when querying the time in Altibase → DB restart is required

| OS Check | Altibase Check |
| --- | --- |
| [root@master ~]# timedatectl<br>Local time: Sun **2025-03-09 03:02:38** CDT<br>Universal time: Sun 2025-03-09 08:02:38 UTC<br>RTC time: Sun 2025-03-09 08:02:39<br>Time zone: CST6CDT (CDT, -0500)<br>NTP enabled: n/a<br>NTP synchronized: no<br>RTC in local TZ: no<br>DST active: yes<br>Last DST change: DST began at<br>Sun 2025-03-09 01:59:59 CST<br>Sun **2025-03-09 03:00:00** CDT<br>Next DST change: DST ends (the clock jumps one hour backwards) at<br>Sun 2025-11-02 01:59:59 CDT<br>Sun 2025-11-02 01:00:00 CST | iSQL> SELECT TO_CHAR(SYSDATE, 'YYYY-MM-DD HH:MI:SS.SSSSSS') FROM DUAL;<br>TO_CHAR(SYSDATE,'YYYY-MM-DDHH:MI:SS.SSSSSS<br>-----------------------------------------------------------------------------------<br>**2025-03-09 02:02:38**.568618<br>1 row selected. |
|  | Restart Altibase |
| [root@master ~]# timedatectl<br>Local time: Sun **2025-03-09 03:03:54** CDT<br>Universal time: Sun 2025-03-09 08:03:54 UTC<br>RTC time: Sun 2025-03-09 08:03:55<br>Time zone: CST6CDT (CDT, -0500)<br>NTP enabled: n/a<br>NTP synchronized: no<br>RTC in local TZ: no<br>DST active: yes<br>Last DST change: DST began at<br>Sun 2025-03-09 01:59:59 CST<br>Sun 2025-03-09 03:00:00 CDT<br>Next DST change: DST ends (the clock jumps one hour backwards) at<br>Sun 2025-11-02 01:59:59 CDT<br>Sun 2025-11-02 01:00:00 CST | iSQL> SELECT TO_CHAR(SYSDATE, 'YYYY-MM-DD HH:MI:SS.SSSSSS') FROM DUAL;<br>TO_CHAR(SYSDATE,'YYYY-MM-DDHH:MI:SS.SSSSSS<br>-----------------------------------------------------------------------------------<br>**2025-03-09 03:03:54**.600136<br>1 row selected. |

※ When performing an incomplete recovery using the until time on a server with DST applied, the time difference must be taken into account.
