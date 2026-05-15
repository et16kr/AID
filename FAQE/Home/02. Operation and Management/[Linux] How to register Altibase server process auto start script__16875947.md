---
title: "[Linux] How to register Altibase server process auto start script"
page_id: "16875947"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/%5BLinux%5D+How+to+register+Altibase+server+process+auto+start+script"
updated_at: "2021-04-02T10:47:28.000+0900"
version: 3
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# [Linux] How to register Altibase server process auto start script
Source: https://docs.altibase.com/display/FAQE/%5BLinux%5D+How+to+register+Altibase+server+process+auto+start+script
Updated: 2021-04-02T10:47:28.000+0900

- [Overview](#overview) - [Version](#version) - [OS](#os) - [Red Hat family v7 or later](#red-hat-family-v7-or-later) - [Red Hat family v6 or earlier](#red-hat-family-v6-or-earlier) - [Sample of autostart script](#sample-of-autostart-script) - [Register the script in /etc/init.d](#register-the-script-in-etcinitd) - [Execute chkconfig](#execute-chkconfig) - [Log](#log)

# Overview

---

This document describes how to automatically start and stop the Altibase database when a Red Hat family Linux server starts or stops. The procedure is divided into Red Hat family v7 or later and v6 or earlier.

# Version

---

Altibase 4 or later

# OS

---

Linux

# Red Hat family v7 or later

---

On Red Hat family v7 or later, check the SELinux state. If SELinux is enabled, change the current mode to permissive according to the operating system policy.

For permanent SELinux state and mode changes, refer to the Red Hat documentation:

- [Changing SELinux states and modes](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html/system_design_guide/changing-selinux-states-and-modes_system-design-guide#changing-selinux-states-and-modes_system-design-guide)

## Create the Altibase auto start and stop service

---

- File name: `altibased.service`
- File path: `/usr/lib/systemd/system`

Create the `altibased.service` file.

```
[root@localhost] # vi altibased.service
```

```
[Unit]
Description=AltibaseAutoStartStop
After=network.target syslog.target

[Service]
Type=forking
User=altibase
Group=altibase
LimitNOFILE=1048576
LimitNPROC=infinity
TimeoutSec=0
KillMode=none

ExecStart=/etc/rc.d/init.d/altibase start
ExecStop=/etc/rc.d/init.d/altibase stop

[Install]
WantedBy=multi-user.target
```

Main items:

| Item | Description |
| --- | --- |
| `Description` | Service description |
| `User` | OS account used to run the service |
| `Group` | Group of the OS account |
| `ExecStart` | File to run when the service starts |
| `ExecStop` | File to run when the service stops |

After creating `altibased.service`, change its file permission to 755.

```
[root@localhost] # chmod 755 altibased.service
```

## Create the file executed by the Altibase service

---

Create the auto start and stop script that is executed by `altibased.service`.

- File name: `altibase`
- File path: `/etc/rc.d/init.d`

```
[root@localhost] # vi altibase
```

Change the Altibase environment file path to match the user environment.

```
#!/bin/bash
# Startup Script for the Altibase Server
# path: /etc/rc.d/init.d/altibase
# chkconfig: 345 90 10
# processname: altibase

. /home/altibase/altibase_home/conf/altibase_user.env

case "$1" in
  start)
    echo "Startup altibase: "
    ${ALTIBASE_HOME}/bin/server start
    ;;
  stop)
    echo "Shutdown altibase: "
    ${ALTIBASE_HOME}/bin/server stop
    ;;
  *)
    echo "Usage: service altibase {start | stop}"
    exit 1
esac
exit 0
```

After creating `altibase`, change its file permission to 755.

```
[root@localhost] # chmod 755 altibase
```

## Create the altibased.service symbolic link

---

The created `altibased.service` service file must exist as a symbolic link in the following location.

```
[root@localhost] # cd /etc/systemd/system/multi-user.target.wants
[root@localhost] # ln -s /usr/lib/systemd/system/altibased.service altibased.service
```

## Register and test altibased.service with systemctl

---

Register `altibased.service` with `systemctl`.

```
[root@localhost] # systemctl enable altibased.service
[root@localhost] # systemctl start altibased.service
[root@localhost] # systemctl stop altibased.service
```

Stop and start the server, then check `$ALTIBASE_HOME/trc` to verify that Altibase stopped and started normally.

## Check the systemctl status

---

```
[root@localhost] # systemctl status altibased.service
```

# Change and check SELinux mode

---

This section describes how to change and check SELinux mode on Red Hat family v7 or later.

## Check SELinux mode

---

```
[root@localhost] # sestatus
SELinux status:                 enabled
SELinuxfs mount:                /sys/fs/selinux
SELinux root directory:         /etc/selinux
Loaded policy name:             targeted
Current mode:                   enforcing
Mode from config file:          enforcing
Policy MLS status:              enabled
Policy deny_unknown status:     allowed
Memory protection checking:     actual (secure)
Max kernel policy version:      31
```

## Temporarily change the SELinux current mode

---

If the SELinux current mode is changed temporarily, it returns to the original state after the OS is restarted. If the current mode is changed only temporarily, the Altibase process does not start automatically after an OS restart.

```
[root@localhost] # setenforce 0
[root@localhost] # setenforce 1
```

## Permanently change the SELinux current mode

---

To permanently change the SELinux current mode, modify the following configuration file.

Change the `SELINUX` item in `/etc/selinux/config` to `permissive`, then restart the OS.

```
[root@localhost] # cd /etc/selinux
[root@localhost] # vi config

# This file controls the state of SELinux on the system.
# SELINUX= can take one of these three values:
#       enforcing - SELinux security policy is enforced.
#       permissive - SELinux prints warnings instead of enforcing.
#       disabled - No SELinux policy is loaded.
#SELINUX=enforcing
SELINUX=permissive
# SELINUXTYPE= can take one of these two values:
#       targeted - Targeted processes are protected,
#       mls - Multi Level Security protection.
```

## Check SELinux status after restarting the OS

---

```
[root@localhost] # sestatus
SELinux status:                 enabled
SELinuxfs mount:                /sys/fs/selinux
SELinux root directory:         /etc/selinux
Loaded policy name:             targeted
Current mode:                   permissive
Mode from config file:          permissive
Policy MLS status:              enabled
Policy deny_unknown status:     allowed
Memory protection checking:     actual (secure)
Max kernel policy version:      31
```

# Red Hat family v6 or earlier

---

On Red Hat family v6 or earlier, use the following procedure to automatically start and stop the Altibase process.

## Sample of autostart script

- [altibased](https://docs.altibase.com/download/attachments/12517478/altibased?version=1&modificationDate=1536132439000&api=v2)

The automatic startup script was written to run in the following situations.

- One Altibase server running on one server
- Installing Altibase server in OS user altibase and have startup/shutdown privileges
- Running in bash shell
- Using the chkconfig utility

This script is a sample file. Depending on the client's OS user's environment settings, it may operate differently than intended, so be sure to test it to check whether it is running properly.

### Register the script in /etc/init.d

Upload the autostart script altibased file to the /etc/init.d directory.

### Change the script

Change the user variable at the top of the script to suit the client's environment.

```
$ vi /etc/init.d/altibased
#!/bin/bash
#
# altibase
#
# chkconfig: 2345 20 80
# description: ALTIBASE process startup
user=altibase                         #  Change to a user with privileges to start/stop Altibase server processes
```

### Change the script execution permission

```
$ chmod +x altibased

$ ls -l altibased
-rwxr-xr-x 1 root root 811 Sep  3 13:50 /etc/init.d/altibased
```

### Execute chkconfig

```
$ chkconfig --add altibased
```

### Check the chkconfig registration

```
$ ls -l /etc/rc.d/rc*.d/K*alti*
$ ls -l /etc/rc.d/rc*.d/S*alti*
```

### Log

The log is set to remain in /var/log/${user}_altibased.log.
