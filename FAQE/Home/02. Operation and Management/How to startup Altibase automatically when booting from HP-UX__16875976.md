---
title: "How to startup Altibase automatically when booting from HP-UX"
page_id: "16875976"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/How+to+startup+Altibase+automatically+when+booting+from+HP-UX"
updated_at: "2021-04-02T11:26:31.000+0900"
version: 3
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# How to startup Altibase automatically when booting from HP-UX
Source: https://docs.altibase.com/display/FAQE/How+to+startup+Altibase+automatically+when+booting+from+HP-UX
Updated: 2021-04-02T11:26:31.000+0900

- [Overview](#HowtostartupAltibaseautomaticallywhenbootingfromHP-UX-Overview) - [What is HP-UX Startup Script?](#HowtostartupAltibaseautomaticallywhenbootingfromHP-UX-WhatisHP-UXStartupScript?) - [How to write a script for automatic startup/stop of Altibase](#HowtostartupAltibaseautomaticallywhenbootingfromHP-UX-Howtowriteascriptforautomaticstartup/stopofAltibase) - [STEP 1](#HowtostartupAltibaseautomaticallywhenbootingfromHP-UX-STEP1) - [STEP 2](#HowtostartupAltibaseautomaticallywhenbootingfromHP-UX-STEP2) - [STEP 3](#HowtostartupAltibaseautomaticallywhenbootingfromHP-UX-STEP3) - [STEP 4](#HowtostartupAltibaseautomaticallywhenbootingfromHP-UX-STEP4) - [STEP 5](#HowtostartupAltibaseautomaticallywhenbootingfromHP-UX-STEP5) - [STEP 6](#HowtostartupAltibaseautomaticallywhenbootingfromHP-UX-STEP6) - [STEP 7](#HowtostartupAltibaseautomaticallywhenbootingfromHP-UX-STEP7)

# Overview

---

This section describes how to automatically startup Altibase when booting from HP-UX.

# What is HP-UX Startup Script?

---

In HP-UX, script files that are executed during system boot/shutdown are managed as follows.

1. The actual script files that are executed at boot time exist in the /sbin/init.d directory.
2. The configuration files for the above script files are in the /etc/rc.config.d directory. Each rc script has one configuration file and sets the definitions and values of variables necessary for script execution.
3. Script files that are executed at boot time exist in the /sbin/rc*.d directory, and these files are symbolic links to the files in the /sbin/init.d directory.

# How to write a script for automatic startup/stop of Altibase

---

- ## STEP 1

  ---

  Create the **/etc/rc.config.d/altibase_conf**file.

  As described above, in this file, variables necessary for starting/shutdown of Altibase are defined and values are set.

  The contents of this file are shown below.

  ```
  ALTIBASE_HOME=/altibase/altibase_home; export ALTIBASE_HOME
  PATH=$ALTIBASE_HOME/bin:/usr/bin:/sbin; export PATH
  ALTIBASE_OWNER=altibase
  START_ALTIBASE=1
  ```

  If the user does not want to automatically start Altibase when booting HP-UX, set the value of START_ALTIBASE to 0. And if ALTIBASE_OWNER or ALTIBASE_HOME is changed, modify the altibase_conf file must be also modified.
- ## STEP 2

  ---

  Create the **/sbin/init.d/alti_start** file. This file is a script that actually starts up Altibase by using the Altibase startup command.

  #!/sbin/sh

  if [ -f /etc/rc.config.d/altibase_conf ] ; then

  . /etc/rc.config.d/altibase_conf

  fi

  ADMIN="${ALTIBASE_HOME}/bin/isql -u sys -p manager -sysdba -noprompt"

  ${ADMIN} << EOF

  startup

  quit

  EOF
- ## STEP 3

  ---

  Create the **/sbin/init.d/alti_stop** file.This file is a script that actually shuts down Altibase by using the Altibase shutdown command.

  #!/sbin/sh

  if [ -f /etc/rc.config.d/altibase_conf ] ; then

  . /etc/rc.config.d/altibase_conf

  fi

  ADMIN="${ALTIBASE_HOME}/bin/isql -u sys -p manager -sysdba -noprompt"

  FUNC_CHECK_ISQL_CONN()

  {

  case $ISQL_CONNECTION in

  [Ii][Pp][Cc])

  unset ISQL_CONNECTION

  ;;

  *)

  ;;

  esac

  }

  # Permit sysdba via IPC

  FUNC_CHECK_ISQL_CONN

  ${ADMIN} << EOF > /dev/null

  ALTER SYSTEM SET CHECKPOINT_BULK_WRITE_PAGE_COUNT = 0;

  ALTER SYSTEM SET CHECKPOINT_BULK_WRITE_SLEEP_SEC = 0;

  ALTER SYSTEM SET CHECKPOINT_BULK_WRITE_SLEEP_USEC = 0;

  quit;

  EOF

  killCheckServer > ${ALTIBASE_HOME}/trc/killCheckServer.log 2>&1

  ${ADMIN} << EOF

  shutdown immediate;

  quit;

  EOF
- ## STEP 4

  ---

  Create the **/sbin/init.d/altibase** file. This file can be created by copying the /sbin/init.d/template file, which is actually the file that the Start/Stop script will create symbolic links later on.

  #!/sbin/sh

  #

  # @(#)B.11.11_LR

  #

  # NOTE: This script is not configurable! Any changes made to this

  # script will be overwritten when you upgrade to the next

  # release of HP-UX.

  #

  # WARNING: Changing this script in any way may lead to a system that

  # is unbootable. Do not modify this script.

  #

  rval=0

  # Check the exit value of a command run by this script. If non-zero, the

  # exit code is echoed to the log file and the return value of this script

  # is set to indicate failure.

  set_return() {

  x=$?

  if [ $x -ne 0 ]; then

  echo "EXIT CODE: $x"

  rval=1 # script FAILed

  fi

  }

  # Kill the named process(es).

  # $1=

  killproc() {

  pid=`ps -el | awk '( ($NF ~ /'"$1"'/) && ($4 != mypid) && ($5 != mypid) )

  { print $4 }' mypid=$$ `

  if [ "X$pid" != "X" ]; then

  if kill "$pid"; then

  echo "$1 stopped"

  else

  rval=1

  echo "Unable to stop $1"

  fi

  fi

  }

  case $1 in

  'start_msg')

  # Emit a _short_ message relating to running this script with

  # the "start" argument; this message appears as part of the checklist.

  echo "Starting the Altibase Database"

  ;;

  'stop_msg')

  # Emit a _short_ message relating to running this script with

  # the "stop" argument; this message appears as part of the checklist.

  echo "Stopping the Altibase Database"

  ;;

  'start')

  # source the system configuration variables

  if [ -f /etc/rc.config.d/altibase_conf ] ; then

  . /etc/rc.config.d/altibase_conf

  else

  echo "ERROR: /etc/rc.config defaults file MISSING"

  fi

  # Check to see if this script is allowed to run...

  if [ "$START_ALTIBASE" != 1 ]; then

  rval=2

  else

  # Execute the commands to start your subsystem

  su - $ALTIBASE_OWNER -c "/sbin/init.d/alti_start"

  fi

  ;;

  'stop')

  # source the system configuration variables

  if [ -f /etc/rc.config.d/altibase_conf ] ; then

  . /etc/rc.config.d/altibase_conf

  else

  echo "ERROR: /etc/rc.config defaults file MISSING"

  fi

  # Check to see if this script is allowed to run...

  if [ "$START_ALTIBASE" != 1 ]; then

  rval=2

  else

  su - $ALTIBASE_OWNER -c "/sbin/init.d/alti_stop"

  # Execute the commands to stop your subsystem

  fi

  ;;

  *)

  echo "usage: $0 {start|stop|start_msg|stop_msg}"

  rval=1

  ;;

  esac
- ## STEP 5

  ---

  Create Symbolic Link of Startup Script and Shutdown Script in /sbin/rc2.d directory.

  # cd /sbin/rc2.d

  # ln -s /sbin/init.d/altibase S955altibase

  # ln -s /sbin/init.d/altibase K955altibase
- ## STEP 6

  ---

  Modify the execution permission so that each script can be executed normally.

  # cd /sbin/rc2.d

  # chmod 755 S955altibase

  # chmod 755 K955altibase

  # cd /sbin/init.d

  # chmod 755 *alti*
- ## STEP 7

  ---

  Test to see if it works properly. At this time, the test must be performed under the root account.

  # su - root

  # /sbin/init.d/altibase
