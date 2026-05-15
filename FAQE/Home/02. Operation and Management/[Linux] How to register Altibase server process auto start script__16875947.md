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

- [Overview](#id-[Linux]HowtoregisterAltibaseserverprocessautostartscript-Overview) - [Version](#id-[Linux]HowtoregisterAltibaseserverprocessautostartscript-Version) - [OS](#id-[Linux]HowtoregisterAltibaseserverprocessautostartscript-OS) - [How to register](#id-[Linux]HowtoregisterAltibaseserverprocessautostartscript-Howtoregister) - [Sample of autostart script](#id-[Linux]HowtoregisterAltibaseserverprocessautostartscript-Sampleofautostartscript) - [Register the script in /etc/init.d](#id-[Linux]HowtoregisterAltibaseserverprocessautostartscript-Registerthescriptin/etc/init.d) - [Change the script](#id-[Linux]HowtoregisterAltibaseserverprocessautostartscript-Changethescript) - [Change the script execution permission](#id-[Linux]HowtoregisterAltibaseserverprocessautostartscript-Changethescriptexecutionpermission) - [Execute chkconfig](#id-[Linux]HowtoregisterAltibaseserverprocessautostartscript-Executechkconfig) - [Check the chkconfig registration](#id-[Linux]HowtoregisterAltibaseserverprocessautostartscript-Checkthechkconfigregistration) - [Log](#id-[Linux]HowtoregisterAltibaseserverprocessautostartscript-Log)

# Overview

---

This section describes how to automatically start the Altibase server process when booting the OS on the Linux server.

# Version

---

Altibase 4 or later

# OS

---

Linux

# How to register

---

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
