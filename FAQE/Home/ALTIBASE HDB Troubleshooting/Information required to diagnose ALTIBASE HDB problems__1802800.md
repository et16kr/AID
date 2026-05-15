---
title: "Information required to diagnose ALTIBASE HDB problems"
page_id: "1802800"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Information+required+to+diagnose+ALTIBASE+HDB+problems"
updated_at: "2011-08-02T13:03:32.000+0900"
version: 13
ancestors: ["Home", "ALTIBASE HDB Troubleshooting"]
labels: []
---

# Information required to diagnose ALTIBASE HDB problems
Source: https://docs.altibase.com/display/FAQE/Information+required+to+diagnose+ALTIBASE+HDB+problems
Updated: 2011-08-02T13:03:32.000+0900

- [About the content](#InformationrequiredtodiagnoseALTIBASEHDBproblems-Aboutthecontent)
- [List of diagnostics information to be gathered](#InformationrequiredtodiagnoseALTIBASEHDBproblems-Listofdiagnosticsinformationtobegathered)
    - [ALTIBASE HDB trace log](#InformationrequiredtodiagnoseALTIBASEHDBproblems-ALTIBASEHDBtracelog)
    - [altibase.properties file](#InformationrequiredtodiagnoseALTIBASEHDBproblems-altibase.propertiesfile)
    - [List of OS Environment variables](#InformationrequiredtodiagnoseALTIBASEHDBproblems-ListofOSEnvironmentvariables)
    - [Kernel value](#InformationrequiredtodiagnoseALTIBASEHDBproblems-Kernelvalue)
    - [OS logs](#InformationrequiredtodiagnoseALTIBASEHDBproblems-OSlogs)
    - [System configuration information](#InformationrequiredtodiagnoseALTIBASEHDBproblems-Systemconfigurationinformation)
    - [ALTIBASE HDB process stack trace](#InformationrequiredtodiagnoseALTIBASEHDBproblems-ALTIBASEHDBprocessstacktrace)
    - [System resource utilization](#InformationrequiredtodiagnoseALTIBASEHDBproblems-Systemresourceutilization)
- [Problem symptoms and required diagnostics information](#InformationrequiredtodiagnoseALTIBASEHDBproblems-Problemsymptomsandrequireddiagnosticsinformation)
    - [Commons](#InformationrequiredtodiagnoseALTIBASEHDBproblems-Commons)
    - [ALTIBASE HDB abnormal shutdown](#InformationrequiredtodiagnoseALTIBASEHDBproblems-ALTIBASEHDBabnormalshutdown)
    - [ALTIBASE HDB hang](#InformationrequiredtodiagnoseALTIBASEHDBproblems-ALTIBASEHDBhang)
    - [ALTIBASE HDB performance degradation](#InformationrequiredtodiagnoseALTIBASEHDBproblems-ALTIBASEHDBperformancedegradation)

# About the content

|  |  |
| --- | --- |
| Purpose | A list of information needed to diagnose ALTIBASE HDB problems. |
| Applies to | HDB versions 4.3.9 or later |
| Prerequisites | Administrator's Manual |

# List of diagnostics information to be gathered

## ALTIBASE HDB trace log

Almost in all cases to analyze problems, the best place to start is ALTIBASE HDB trace logs. The default location of these logs is is $ALTIBASE_HOME/trc folder.

When users have any issues in ALTIBASE HDB environment, they can archive and compress the entire folder structure and send it to Altibase Customer Support service to help to identify the root cause of the problems.

| File Name | Description |
| --- | --- |
| altibase_boot.log | The main trace log. It contains ALTIBASE HDB engine's start-up and shutdown log. |
| altibase_qp.log | The trace of ALTIBASE HDB QP (Query Processing) module. |
| altibase_sm.log | The trace log of ALTIBASE HDB SM (Storage Manage) module. |
| altibase_rp.log | The trace log of ALTIBASE HDB RP (Replication Processor) module. |
| altibase_xa.log | The trace log of ALTIBASE HDB XA module. |

It is advisable to send us all of these files above in order to minimize round-trip times.

## altibase.properties file

altibase.properties file is located in $ALTIBASE_HOME/conf folder.

If any part of this file is altered, it is advisable to send the result of following script along with the log files to Altibase Customer Support .

```
$ is <<EOF
spool out.txt
set linesize 200
select rpad(name,30) name,  value1 from v\$property;
quit;
EOF
```

## List of OS Environment variables

A text file containing the OS specific environment information listed below should also be submitted to Altibase Customer Service.

```
$ env
$ ulimit -a
```

## Kernel value

| OS | command |
| --- | --- |
| HP | # kctune |
| AIX | # vmo -a -F |
|  | # schedo -a -F |
|  | # no -a -F |
| Solaris | # cat /etc/project |
| Linux | # cat /proc/sys/kernel/sem |
|  | # cat /proc/sys/kernel/semall |

## OS logs

| OS | command |
| --- | --- |
| HP | # cat /var/adm/syslog/syslog.log |
| AIX | # errpt -a |
| Solaris | # cat /var/adm/messages |
|  | # dmesg |
| Linux | # cat /var/log/messages |
|  | # dmesg |

## System configuration information

| OS | command |
| --- | --- |
| HP | # machinfo |
| AIX | # prtconf |
| Solaris | # prtconf |
| Linux | # cat /proc/cpuinfo |
|  | # cat /proc/meminfo |

## ALTIBASE HDB process stack trace

The stack trace shows a snapshot of the state of the threads, and it is very useful information to solve the various types of problems - especially, process hanging situations.

| Platforms | Usage |  |
| --- | --- | --- |
| AIX | $ procstack [altibase_pid] | after AIX 6.1, procstack command to ALTIBASE HDB process does not work properly. |
| HPUX | $ pstack [altibase_pid] |  |
| Solaris | $ pstack [altibase_pid] |  |
| Linux | $ pstack [altibase_pid] |  |

## System resource utilization

- vmstat

  ```
  $ vmstat 1 5
  ```

- CPU and memory utilization of ALTIBASE HDB process

  ```
  $ ps -p [altibase_pid] -o pcpu -o vsz
  ```

# Problem symptoms and required diagnostics information

## Commons

- ALTIBASE HDB trace log
- altibase.properties
- OS Environment variable list
   Above information is required to analyze any ALTIBASE HDB problem.

## ALTIBASE HDB abnormal shutdown

- Commons
- OS logs

## ALTIBASE HDB hang

- Commons
- ALTIBASE HDB process stack trace

## ALTIBASE HDB performance degradation

- Commons
- ALTIBASE HDB process stack trace during the system peak time.
