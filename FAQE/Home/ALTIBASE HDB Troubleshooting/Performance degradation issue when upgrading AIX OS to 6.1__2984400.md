---
title: "Performance degradation issue when upgrading AIX OS to 6.1"
page_id: "2984400"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Performance+degradation+issue+when+upgrading+AIX+OS+to+6.1"
updated_at: "2011-11-10T18:36:42.000+0900"
version: 3
ancestors: ["Home", "ALTIBASE HDB Troubleshooting"]
labels: []
---

# Performance degradation issue when upgrading AIX OS to 6.1
Source: https://docs.altibase.com/display/FAQE/Performance+degradation+issue+when+upgrading+AIX+OS+to+6.1
Updated: 2011-11-10T18:36:42.000+0900

- [Symptom](#PerformancedegradationissuewhenupgradingAIXOSto6.1-Symptom)
- [Analysis](#PerformancedegradationissuewhenupgradingAIXOSto6.1-Analysis)
- [Solution](#PerformancedegradationissuewhenupgradingAIXOSto6.1-Solution)

# Symptom

The performance of ALTIBASE HDB is dramatically degraded after upgrading AIX OS from version 5.3 to version 6.1.

# Analysis

1. Observed a state of Service Thread of ALTIBASE HDB by using "procstack" utility of AIX.

2. Found out that built-in function - sysdate() - of ALTIBASE HDB was causing the performace degradation.

3. sysdate() function of ALTIBASE HDB triggers a system-call to "localtime_r()" and it causes the performance degradation. We confirmed the difference between AIX 5.3 and 6.1 with an AIX support engineer.

```
0x0000000000003428  _check_lock() + 0x8
0x0900000000a85598  _global_lock_common(??, ??, ??) + 0x2b8
0x0900000000011410  _rec_mutex_lock(??) + 0xd0
0x0900000000049284  localtime_tz_r(??, ??, ??) + 0x384
0x000000010000dbec  PDL_OS::localtime_r(const long*,tm*)() + 0xc
0x00000001000b54dc  qtc::sysdate(qcTemplate*)() + 0xbc
0x0000000100476b8c  qmx::executeInsertValues(qcStatement*)() + 0x90c
0x000000010058903c  mmcStmtType::executeDML(mmcSession*,mmcSessionInfo*,mmcStmtType*,unsigned int*,long*)() + 0x19c
0x0000000100584398  mmcStmtType::execute(unsigned int*,long*,mmcSessionInfo*)() + 0x98
0x00000001005c00c4  mmtTaskThread::doPrepareExecute(mmcStmtType*,long long,void*,unsigned long long,void*,unsigned long long)() + 0x444
0x00000001005c1fc4  mmtTaskThread::executeArray(unsigned int)() + 0x484
0x00000001005c29ac  mmtTaskThread::executeProtocol()() + 0x72c
0x000000010059ef60  mmtTaskThread::processProtocol(idBool*,idBool*)() + 0x780
0x000000010059f678  mmtTaskThread::runShared()() + 0x198
0x00000001005a04a0  mmtTaskThread::run()() + 0x400
0x0000000100035924  idtBaseThread::staticRunner(void*)() + 0x44
0x0900000000a86d50  _pthread_body(??) + 0xf0
```

# Solution

Performance bottleneck occurs depending on the setting of TimeZone in AIX 6.1. To work around this AIX issue, the default TimeZone setting has to be changed to Local TimeZone based on Posix standard.

```
Shell Prompt> echo $TZ
Asia/Seoul <- Olson time zone (X)
KORST-9 <- Posix time zone (O)

- Modify Time zone
Shell Prompt> smitty chtz_user
```
