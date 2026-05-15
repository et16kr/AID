---
title: "Automatic altibase startup during OS booting in Solaris"
page_id: "16875996"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Automatic+altibase+startup+during+OS+booting+in+Solaris"
updated_at: "2021-04-02T15:17:56.000+0900"
version: 7
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# Automatic altibase startup during OS booting in Solaris
Source: https://docs.altibase.com/display/FAQE/Automatic+altibase+startup+during+OS+booting+in+Solaris
Updated: 2021-04-02T15:17:56.000+0900

- [Overview](#AutomaticaltibasestartupduringOSbootinginSolaris-Overview) - [How to automatically startup Altibase](#AutomaticaltibasestartupduringOSbootinginSolaris-HowtoautomaticallystartupAltibase) - [Steps](#AutomaticaltibasestartupduringOSbootinginSolaris-Steps) - [STEP 1](#AutomaticaltibasestartupduringOSbootinginSolaris-STEP1) - [STEP2](#AutomaticaltibasestartupduringOSbootinginSolaris-STEP2) - [STEP3](#AutomaticaltibasestartupduringOSbootinginSolaris-STEP3) - [STEP4](#AutomaticaltibasestartupduringOSbootinginSolaris-STEP4) - [STEP5](#AutomaticaltibasestartupduringOSbootinginSolaris-STEP5) - [STEP6](#AutomaticaltibasestartupduringOSbootinginSolaris-STEP6) - [STEP7](#AutomaticaltibasestartupduringOSbootinginSolaris-STEP7)

# Overview

---

This document describes how to write a script that automatically starts up the Altibase server when booting in Sun Solaris.

# How to automatically startup Altibase

---

Solaris provides an rc script that is related to the run level. These scripts reside in the /sbin directory and are symlinked to the rc scripts in the /etc directory.

The /sbin/rc# scripts exist under the /etc/rc#.d directory with matching names, which contains scripts to start and stop system processes for run levels.

File names in this directory start with K and S, K* scripts are used to kill processes, and S* scripts are used to start processes. These files are run in alphanumeric order.

In the /etc/init.d directory there are actual run control files that start or kill processes, which are hard-linked to the etc/rc#.d directory.

# Steps

---

### STEP 1

Create the /etc/alti-conf.d/alti.conf file. In this file, variables necessary for automatic operation are defined and set. The contents of this file are as follows.

| ALTIBASE_HOME=/home/altibase/altibase_home ; export ALTIBASE_HOME PATH=$ALTIBASE_HOME/[bin:/usr/bin:/sbin](http://bin/usr/bin:/sbin) ; export PATH ALTIBASE_OWNER=altibase START_ALTIBASE=1 |
| --- |

If the user does not want to run the file automatically, set the value of START_ALTIBASE to 0. And when ALTIBASE_OWNER or ALTIBASE_HOME is changed, the value in this file must be modified.

### STEP2

Create the /etc/init.d/alti_start file. In this script, it is a script that actually starts up the DBMS by using the Altibase startup command.

| #!/sbin/sh if [ -f /etc/alti-conf.d/alti.conf ] ; then . /etc/alti-conf.d/alti.conf Fi<br>{*}ADMIN="$<br> <br>Unknown macro: {ALTIBASE_HOME}<br> <br>/bin/isql -s 127.0.0.1 -u sys -p manager -sysdba"*<br>*$<br> <br>Unknown macro: {ADMIN}<br> <br><<EOF{*}<br>startup quit EOF |
| --- |

### STEP3

Create the /etc/init.d/alti_stop file.

In this script, it is a script that actually stops the DBMS by using the Altibase command.

| #!/sbin/sh if [ -f /etc/alti-conf.d/alti.conf ] ; then . /etc/alti-conf.d/alti.conf fi<br>ADMIN="$<br> <br>Unknown macro: {ALTIBASE_HOME}<br> <br>/bin/isql -s 127.0.0.1 -u sys -p manager -sysdba"<br>*$<br> <br>Unknown macro: {ADMIN}<br> <br><<EOF{*}<br>shutdown immediate quit EOF |
| --- |

### STEP4

Create the /etc/init.d/altibase file.

This file is actually the file that the startup script or stop script will create a symbolic link later on. The contents of this file are as follows.

| #!/sbin/sh # # Copyright (c) 1997, 2001 by Sun Microsystems, Inc. # All rights reserved. # #ident "@(#)altibase 1.0 04/08/17" case $1 in 'start') # source the system configuration variables if [ -f /etc/alti-conf.d/alti.conf ] ; then . /etc/alti-conf.d/alti.conf else echo "ERROR: /etc/alti-conf.d/alti.conf defaults file MISSING" fi # Check to see if this script is allowed to run... if [ "$START_ALTIBASE" != 1 ]; then exit 2 else # Execute the commands to start your subsystem su - $ALTIBASE_OWNER -c "/etc/init.d/alti_start" fi ;; 'stop') # source the system configuration variables if [ -f /etc/alti-conf.d/alti.conf ] ; then . /etc/alti-conf.d/alti.conf else echo "ERROR: /etc/alti-conf.d/alti.conf defaults file MISSING" fi # Check to see if this script is allowed to run... if [ "$START_ALTIBASE" != 1 ]; then exit 2 else su - $ALTIBASE_OWNER -c "/etc/init.d/alti_stop" # Execute the commands to stop your subsystem fi ;; *)<br>{*}echo "usage: $0<br> <br>Unknown macro: {start\|stop}<br> <br>"*<br>exit 1 ;; esac exit 0 |
| --- |

### STEP5

Create a Hard Link of Startup Script and Shutdown Script in /etc/rc3.d Directory.

| #cd /etc/rc3.d # ln /etc/init.d/altibase S955altibase |
| --- |

### STEP6

Set the execution authority so that each script can be executed normally.

| #cd /etc/rc3.d # chmod 755 S955altibase #cd /etc/init.d # chmod 755 *alti* |
| --- |

### STEP7

Test to see if it operates normally. At this time, the test should be performed under the root account.

| # /etc/init.d/altibase <start:stop> |
| --- |
