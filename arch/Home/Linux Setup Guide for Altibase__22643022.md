---
title: "Linux Setup Guide for Altibase"
page_id: "22643022"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/Linux+Setup+Guide+for+Altibase"
updated_at: "2025-10-21T09:27:03.000+0900"
version: 1
ancestors: ["Home"]
labels: []
---

# Linux Setup Guide for Altibase
Source: https://docs.altibase.com/display/arch/Linux+Setup+Guide+for+Altibase
Updated: 2025-10-21T09:27:03.000+0900

- [Overview](#overview)
- [Linux Compatibility](#linux-compatibility)
- [Kernel Parameters](#kernel-parameters)
- [How to Change Kernel Parameters](#how-to-change-kernel-parameters)
- [User Setting](#user-setting)
- [Summary](#summary)
- [Others](#others)
- [References](#references)

---

## Overview

This document provides a guide for setting kernel parameters and OS user configuration for the stable operation of the Altibase server on the Linux system.

This document is based on the version below:

- Altibase 5.5.1 or later
- Red Hat Enterprise Linux 6 or later

## Linux Compatibility

---

Linux has many distribution types, but the Altibase compatibility check is based on glibc version regardless of the distribution type and kernel version.

### glibc Compatibility Version

Starting from Altibase 5.5.1, the compatibility is checked based on the glibc version.

The glibc versions with guaranteed compatibility for each Altibase server version are as follows.

| Altibase Version | OS Version | glibc Version |
| --- | --- | --- |
| Altibase v7.3.0 | Oracle Linux 8 / Red Hat Enterprise Linux 8 / CentOS 8 / Rocky Linux 8 | 2.12 ~ 2.33 |
| Oracle Linux 7 / Red Hat Enterprise Linux 7 / CentOS 7 | 2.12 ~ 2.33 |  |
| Oracle Linux 6 / Red Hat Enterprise Linux 6 / CentOS 6 | 2.12 ~ 2.33 |  |
| Ubuntu 18 | 2.27 ~ 2.33 |  |
| Ubuntu 16 | 2.23 ~ 2.33 |  |
| Ubuntu 12 | 2.17 ~ 2.33 |  |
| POWER7 w/Red Hat Enterprise Linux 6.5 | 2.12 ~ 2.33 |  |
| POWER8(LE) w/Red Hat Enterprise Linux 7.2 | 2.17 ~ 2.33 |  |
| Altibase v7.1.0 | Oracle Linux 8 / Red Hat Enterprise Linux 8 / CentOS 8 / Rocky Linux 8 | 2.12 ~ 2.33 |
| Oracle Linux 7 / Red Hat Enterprise Linux 7 / CentOS 7 | 2.12 ~ 2.33 |  |
| Oracle Linux 6 / Red Hat Enterprise Linux 6 / CentOS 6 | 2.12 ~ 2.33 |  |
| Ubuntu 18 | 2.27 ~ 2.33 Altibase 7.1.0.7.2 or higher |  |
| Ubuntu 16 | 2.23 ~ 2.33 Altibase 7.1.0.7.2 or higher |  |
| Ubuntu 12 | 2.17 ~ 2.33 |  |
| POWER7 w/Red Hat Enterprise Linux 6.5 | 2.12 ~ 2.33 |  |
| POWER8(LE) w/Red Hat Enterprise Linux 7.2 | 2.17 ~ 2.33 Altibase 7.1.0.0.8 or higher |  |
| Altibase v6.5.1 | Oracle Linux 8 / Red Hat Enterprise Linux 8 / CentOS 8 / Rocky Linux 8 | 2.12 ~ 2.33 |
| Oracle Linux 7 / Red Hat Enterprise Linux 7 / CentOS 7 | 2.12 ~ 2.33 |  |
| Oracle Linux 6 / Red Hat Enterprise Linux 6 / CentOS 6 | 2.12 ~ 2.33 |  |
| Ubuntu 12 | 2.17 ~ 2.33 |  |
| POWER8 w/Red Hat Enterprise Linux 7.1 | 2.12 ~ 2.33 |  |
| POWER7 w/Red Hat Enterprise Linux 6.5 | 2.12 ~ 2.33 |  |
| POWER8(LE) w/Red Hat Enterprise Linux 7.6 | 2.17 ~ 2.33 Altibase 6.5.1.4.5 or higher |  |
| POWER8(LE) w/Red Hat Enterprise Linux 7.2 | 2.17 ~ 2.33 Altibase 6.5.1.4.5 or higher |  |
| Altibase v6.3.1 |  | 2.3.4 ~ 2.20 |
| Altibase v6.1.1 |  | 2.3.4 ~ 2.20 |
| Altibase v5.5.1 |  | 2.3.4 ~ 2.20 |

### glibc Recommended Version

Use the glibc version recommended for the Altibase version.

In the previous version of glibc, there was a bug in which a system call (malloc/free) function could cause deadlock due to a race condition.

### How to Check the glibc Version

How to check the glibc version is as follows.

```
$ rpm -q glibc
```

## Kernel Parameters

---

This section describes the types of kernel parameters, recommended values, and recommended reasons for configuring Altibase in Linux to operate stably.

The recommended parameter types are as follows:

- CPU frequency Governor
- RemoveIPC
- swappiness
- THP
- max_map_count
- Shared memory
- Semaphore

### CPU Frequency Governor

Altibase server is a system that absolutely requires maximum processing performance and shortest response time, so CPU clock speed should always be kept at the highest level.

Linux keeps pace with green IT (environmentally friendly computing) and efficiently minimizes power consumption of the system as the core of power management and provides CPUfreq Governor for this.

The default setting of OnDemand Governor in RHEL 6 has a case where the Altibase server performance cannot guarantee consistency due to the delay due to frequency change. Therefore, it is recommended to set it to 'performance' or disable this function itself.

| Kernel Parameter | Description | Recommended Value |
| --- | --- | --- |
| CPU frequency Governor (CPUfreq Governor) | This is a performance adjuster that adjusts CPU frequency change rules, etc. for power management in Linux. The default value of RHEL 6 is OnDemand, the CPU operates at the highest clock frequency when the system load is high, and operates at the lowest frequency when the system is idle. | performance |

### RemoveIPC

RemoveIPC is an option added in RHEL 7.2. It is a Linux property that removes the System V IPC and POSIX IPC objects when the OS user terminates the session.

In the case of the default setting 'yes', cases of abnormal termination of the Altibase server and applications due to forced semaphore allocation and return in the Altibase environment using IPC have been reported. Even in an environment that does not use IPC, 'no' is recommended because there have also been reported that affects system performance due to RemoveIPC-related actions and system calls occurring in the kernel.

| Kernel Parameter | Description | Recommended Value |
| --- | --- | --- |
| RemoveIPC | Removes all IPC resources when the OS user logs out. The root user and system user are not affected by this setting. The default value is 'yes'. | no |

### Swappiness

This is a recommended kernel parameter to minimize the effect of disk I/O on the performance of the Altibase server when swapping occurs.

Swapping refers to the operation (swap out) of moving out the physical memory area, which is less frequently used, into the swap area in a situation where the physical memory is insufficient. The swap is to use the disk as a memory and when the swap out occurs, the system performance decreases due to DISK I/O.

Therefore, it is important to properly set the swappiness to maintain the stable and consistent performance of the Altibase server.

| Kernel Parameter | Description | Recommended Value |
| --- | --- | --- |
| swappiness | A low value makes the kernel use page-cache pages as much as possible, and a high value makes the kernel prefer to swap out less frequently used physical memory pages (cold pages). | 1 |

- Disabling swappiness completely increases the likelihood that the Altibase server process will be killed abnormally by the OOM Killer in low memory situations.
- Recommendation '1' is a setting to minimize swapping without disabling swappiness.
- The page cache is a memory area managed by Linux to improve file I/O performance.

### THP(Transparent Huge Pages)

THP is a setting adopted by Linux for managing a large amount of memory. It is a setting to automate the function of expanding a memory page of 4096 bytes in units of 2MB or 1GB.

However, in the Altibase operating environment, cases of performance issues due to memory allocation delays and fragmentation have been reported, so deactivation is recommended.

| Kernel Parameter | Description | Recommended Value |
| --- | --- | --- |
| THP(transparent_hugepage) | This automates the function to expand the memory page unit managed by the kernel from the existing 4K to 2M or 1G. The default value is 'always'. | never |

### max_map_count

When operating a terabyte unit memory table, memory allocation may fail due to the max_map_count parameter limitation. It is recommended to set it to a sufficiently large value because it can seriously affect the operation of Altibase such as transaction failure.

| Kernel Parameter | Description | Recommended Value |
| --- | --- | --- |
| max_map_count | This is the maximum number of memory map areas that a process can use. In most cases, the default value 65530 is suitable, but if the user needs to map more than this file to the application, the user should increase this value. | 2147483647 |

- If memory allocation fails due to this parameter limitation,

    - The following message may be left in the Altibase trace log altibase_boot.log.

          - Failed to mmap log file ( errno=ENOMEM(12), Not enough memory
    - In the application, an error such as Memory [iduMemMgr :: malloc] failed. may occur.

### Shared Memory

This is a kernel parameter required when multiple applications need to exchange information with each other on one server.

- When the communication method between Altibase server and client is IPC or IPCDA type
- Two or more Altibase applications communicate over IPC

The OS provides a resource called IPC (Inter Process Communication). Among various IPC resources, the memory area used by two or more processes to exchange information is called shared memory. The shared memory can be set by the user by dividing it into one or more areas by specifying a unit, and this is called a segment.

For example, a user can set up a shared memory with one segment at 10 MB or a shared memory of 100 MB by organizing 10 segments with 10 MB. Therefore, it is necessary to set the segment-related kernel parameters such as the maximum size or number of segments.

Shared memory related parameters provided by Linux and recommended values from Altibase are as follows.

| Kernel Parameter | Description | Recommended Value |
| --- | --- | --- |
| shmmni | The maximum number of shared memory segments that can be created. The default value is 4096. | 4096 |
| shmmax | The maximum size of one shared memory segment, in bytes. For x86 systems, the minimum setting is 268435456 bytes (256MB) and for 64-bit systems it is 2147483648 bytes (2GB). | 2147483648 |

### Semaphore

This is a kernel parameter required to implement synchronization between processes when the communication method between the Altibase server and the client is IPC or IPCDA type.

Semaphore is a resource provided by the OS to restrict access to shared resources in IPC. Since the shared memory is used as a communication buffer in the IPC or IPCDA communication method, semaphore operation is used to control read/write concurrency for this resource. Depending on the semaphore operation, the process can be in waiting or in progress state. Since semaphore operations occur simultaneously, it is necessary to set the number of semaphores and the appropriate kernel parameters for the operations.

Semaphore-related parameters provided by Linux and recommended values from Altibase are as follows.

| Kernel Parameter | Description | Recommended Value |
| --- | --- | --- |
| semmsl | The maximum number of semaphores in a set of semaphores and must be logically equal to or less than semmns. If set too large, several semaphore IDs can monopolize the entire system semaphore | 2000 |
| semmns | The maximum number of semaphores in the operating system, and 16 bytes of kernel memory are allocated per one. | 32000 |
| semopm | The maximum number of operations handled by the semop system call. | 512 |
| semmni | The maximum number of semaphore sets can be set within 65535, and 84 bytes of kernel memory are allocated per set. | 5029 |

## How to Change Kernel Parameters

---

Let's learn how to check and change the settings of each kernel parameter.

### CPU frequency Governor

It is recommended that the CPU frequency governor is set as performance.

#### How to Check Set Value

Normally, it is checked with the cat command. If the cpupowerutils package is installed, it can also be checked with the cpupower command.

##### 1. cat command

###### CPU frequency governor setting confirmation method and output example - cat

```
$ cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor | sort -u
performance
```

If CPUfreq driver is not installed, the following output may be displayed. In this case, it is not necessary to consider the CPU frequency governor setting.

```
$ cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
cat: /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor: There is no such file or directory
```

**How to check whether the CPUfreq governor driver is installed**

###### Red Hat Enterprise Linux 6

```
$ lsmod | grep cpufreq
acpi_cpufreq            7699  0
freq_table              4936  1 acpi_cpufreq
mperf                   1557  1 acpi_cpufreq

# Or

$ cpupower frequency-info | grep driver
 driver: acpi-cpufreq

# If CPUfreq driver is not installed, the output result is as follows.
# lsmod output does not appear.
$ lsmod | grep cpufreq
$ cpupower frequency-info | grep driver
 no or unknown cpufreq driver is active on this CPU
```

###### Red Hat Enterprise Linux 7

```
$ cpupower frequency-info | grep driver
  driver: intel_pstate
```

##### 2. cpupower command

How to check CPU frequency governor settings - cpupower

```
# Statements and output examples
# The output may differ depending on the cpupower command version
$ cpupower frequency-info --policy
analyzing CPU 0:
  current policy: frequency should be within 1.20 GHz and 3.60 GHz.
                  The governor "performance" may decide which speed to use
                  within this range.

# Output result when CPUfreq driver is not installed
$ cpupower frequency-info --policy
analyzing CPU 0:
  Unable to determine current policy
```

##### 3. How to check clock speed per CPU core

Check if the clock speed of all CPU cores is set with the following command.

```
$ grep MHz /proc/cpuinfo | sort -u
```

#### How to Change the Settings

##### Change Immediately

Settings using the governor directive and the cpupower command can be changed while online, but initialized when the OS is restarted.

###### Governor directives using the cat command

```
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
```

###### cpupower

```
$ cpupower frequency-set -g performance
```

##### Permanent Application

This is a way to keep the settings even after restarting the OS.

###### 1. rc.local: Applicable only on RHEL 6

Add the following line to the `/etc/rc.local` file:

```
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
```

**2. Using udev rules: For RHEL 7 and above**

Create or modify the file `/etc/udev/rules.d/99-cpufreq.rules`:

```
vi /etc/udev/rules.d/99-cpufreq.rules
```

Add the following:

```
ACTION=="add", SUBSYSTEM=="cpu", KERNEL=="cpu[0-9]*", ATTR{cpufreq/scaling_governor}="performance"
```

udevadm reload:

```
sudo udevadm control --reload-rules
sudo udevadm trigger --subsystem-match=cpu
```

**3. Using tuned : RHEL 7 and above**

On RHEL 7 or later, a tuned profile configuration may be required.

Check the active tuned profile:

If the tuned service is stopped or there is no active profile, this step is not necessary. If tuned is active, check the current profile and apply the appropriate configuration.

```
$ tuned-adm active
```

Example:

```
Current active profile: virtual-guest
```

Changing the profile configuration: Example when the currently active profile is the virtual-guest profile

```
$ cd /usr/lib/tuned/virtual-guest
$ vi tuned.conf
```

[main] Add the following to the session:

Using built-in Linux profiles like throughput-performance or latency-performance can have the following effects:

- The CPUfreq governor is set to performance.
- The CPU clock speed is fixed to the maximum.

```
[main]
include=throughput-performance
```

Apply changed profile:

```
$ tuned-adm profile 'profile_name'
```

Alternatively, change the active profile to throughput-performance or latency-performance.

```
 $ tuned-adm profile throughput-performance
```

### RemoveIPC

RemoveIPC applies to Red Hat Enterprise Linux 7.2 and later, and the recommended value is 'no'.

#### How to Check Set Value

Make sure RemoveIPC = no is set in the logind.conf file.

Check RemoveIPC settings

```
$ grep RemoveIPC /etc/systemd/logind.conf
RemoveIPC=no
```

#### How to Change the Settings

**Red Hat Enterprise Linux 7**

###### **Change Immediate**

RemoveIPC does not provide a way to change immediately on Linux

###### **Permanent Application**

Open the /etc/systemd/logind.conf file with an editor and change RemoveIPC = no.

How to change RemoveIPC

```
$ vi /etc/systemd/logind.conf

#  This file is part of systemd.
...
[Login]
...
RemoveIPC=no
```

Restart the OS or execute the following command to apply the changes.

Apply after changing RemoveIPC

```
$ systemctl restart systemd-logind.service
```

### swappiness

You can check the value of vm.swappiness in the following two ways.

**1. checking /proc/sys/vm/swappiness file**

```
$ cat /proc/sys/vm/swappiness
```

example:

```
1
```

**2. using sysctl comman**

```
$ sysctl vm.swappiness
```

example:

```
vm.swappiness = 1
```

**3. Additional check for RHEL 8: Verify the vm.force_cgroup_v2_swappiness parameter**

In a cgroup v1 environment on RHEL 8, the vm.swappiness setting has little effect on swap behavior, which may lead to unexpected swapping. To prevent this, an additional configuration recommended by Red Hat should be verified.

(Reference: [https://access.redhat.com/solutions/6785021](https://access.redhat.com/solutions/6785021))

Use the sysctl command to check the value of the parameter. The recommended value is 1.

```
$ sysctl vm.force_cgroup_v2_swappiness
```

example:

```
vm.force_cgroup_v2_swappiness = 1
```

If the following result appears, it means the system does not support the vm.force_cgroup_v2_swappiness parameter, so you need to check setting number 4.

```
sysctl: cannot stat /proc/sys/vm/force_cgroup_v2_swappiness: No such file or directory
```

**4. Additional check for RHEL 8 (vm.force_cgroup_v2_swappiness parameter not supported):memory.swappiness value of each cgroup**

On RHEL 8 systems that do not support vm.force_cgroup_v2_swappiness, you need to verify the memory.swappiness value for each cgroup. All values should be set to 1.

```
$ find /sys/fs/cgroup/memory -name memory.swappiness -exec cat {} \; | sort -u
```

example:

```
1
```

If a value other than 1 appears as shown below, you need to change the memory.swappiness value of all cgroups to 1.

```
1
60
```

### How to change the swappiness setting

#### **Change Immediate**

This method applies immediately, but the setting will be reset when the OS is rebooted.

```
$ sysctl -w vm.swappiness=1
```

#### Permanent Application

The following method ensures the setting is retained even after rebooting the OS. To fully apply the configuration, the OS must be restarted.

**1. Modify the default sysctl.conf file**

```
vi /etc/sysctl.conf
```

Add the following setting or modify the existing value.

```
vm.swappiness = 1
```

**2. Create /etc/sysctl.d/99-sysctl.conf or modify the existing file.**

```
vi /etc/sysctl.d/99-sysctl.conf
```

Add the following setting or modify the existing value.

```
vm.swappiness = 1
```

**3. Additional setting for RHEL 8: vm.force_cgroup_v2_swappiness = 1**

Add the following to both /etc/sysctl.d/99-sysctl.conf and /etc/sysctl.conf.

```
vm.force_cgroup_v2_swappiness = 1
```

**4. Additional setting for RHEL 8 (vm.force_cgroup_v2_swappiness parameter not supported): Change the memory.swappiness value of each cgroup to 1**

Support for the vm.force_cgroup_v2_swappiness parameter in RHEL 8 may vary depending on the version. For unsupported versions, it is recommended to contact the OS vendor for guidance on Workaround #2 described on the following page.

- [Red Hat Solution: 6785021](https://access.redhat.com/solutions/6785021)

**5. Using tuned: RHEL 7 and above**

On RHEL 7 or later, configuring a tuned profile may be necessary.

Check the active tuned profile:

If the tuned service is stopped or there is no active profile, this step is not required. If tuned is active, check the current profile and apply the appropriate settings..

```
$ tuned-adm active
```

example:

```
Current active profile: throughput-performance
```

Changing the profile configuration: Example when the currently active profile is throughput-performance

```
$ cd /usr/lib/tuned/throughput-performance
$ vi tuned.conf
```

If there is a vm.swappiness setting in the [sysctl] session, modify it; if not, leave it as is.

```
[sysctl]
vm.swappiness=1
```

If vm.force_cgroup_v2_swappiness is supported on RHEL 8, also add the following setting to the [sysctl] session.

```
[sysctl]
vm.force_cgroup_v2_swappiness=1
```

Apply the changed profile:

```
$ tuned-adm profile 'profile_name'
```

### THP

Check the current settings, and if the recommended configuration is not applied, refer to the guide below to make the changes.

#### Check THP settings

Verify the following three items to confirm that THP is disabled.

**1. Check the current status of THP**

**Red Hat Enterprise Linux 6**

```
$ cat /sys/kernel/mm/redhat_transparent_hugepage/enabled
$ cat /sys/kernel/mm/redhat_transparent_hugepage/defrag
```

**Red Hat Enterprise Linux 7 and above**

```
$ cat /sys/kernel/mm/transparent_hugepage/enabled
$ cat /sys/kernel/mm/transparent_hugepage/defrag
```

**Recommended settings: never**

```
always madvise [never]
```

The values enclosed in brackets ([]) in the output indicate the current settings.

**2. Check /proc/meminfo**

```
$ grep -i huge /proc/meminfo
```

Example output: All values except Hugepagesize should be 0.

```
AnonHugePages:         0 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
```

**3. Check the boot loader settings**

```
$ cat /proc/cmdline
```

Example output: Verify that transparent_hugepage=never and transparent_hugepage.defrag=never are present.

```
BOOT_IMAGE=/vmlinuz-3.10.0-862.el7.x86_64 root=/dev/mapper/centos-root ro crashkernel=auto rd.lvm.lv=centos/root rd.lvm.lv=centos/swap rhgb quiet transparent_hugepage=never transparent_hugepage.defrag=never
```

#### How to change THP settings

To fully disable THP (Transparent Huge Pages), it is recommended to also change the defrag setting. If defrag is set to always, even with THP disabled, the kernel may still try to defragment fragmented memory when allocating large pages, which can cause unnecessary CPU usage and performance degradation.

#### Temporary application

The commands below will stop creating and using new THP. Previously created THP will not be released, and to completely remove them, you need to reboot the OS with THP disabled.

**Red Hat Enterprise Linux 6**

```
$ echo never > /sys/kernel/mm/redhat_transparent_hugepage/enabled
$ echo never > /sys/kernel/mm/redhat_transparent_hugepage/defrag
```

**Red Hat Enterprise Linux 7 and above**

```
$ echo never > /sys/kernel/mm/transparent_hugepage/enabled
$ echo never > /sys/kernel/mm/transparent_hugepage/defrag
```

#### Permanent application

The following settings are for maintaining the configuration even after rebooting the OS. To fully apply the changes, the OS must be restarted.

**1. modify GRUB settings**

**modify grub.conf :**

**Red Hat Enterprise Linux 6 (/etc/grub.conf 수정)**

```
$ vi /etc/grub.conf
```

RHEL 6 modification example: Add transparent_hugepage=never transparent_hugepage.defrag=never to the end of the kernel line.

```
           # kernel 마지막 부분에 transparent_hugepage=never를 추가한다.
        kernel /vmlinuz-2.6.32-504.el6.x86_64 ro root=/dev/mapper/vg_os-lv_os rd_NO_LUKS LANG=en_US.UTF-8 rd_NO_MD SYSFONT=latarcyrheb-sun16 crashkernel=auto rd_LVM_LV=vg_os/lv_os  KEYBOARDTYPE=pc KEYTABLE=us rd_NO_DM rhgb quiet transparent_hugepage=never
        initrd /initramfs-2.6.32-504.el6.x86_64.img
```

**Red Hat Enterprise Linux 7 and above (modify /etc/default/grub.conf)**

```
$ vi /etc/default/grub
```

RHEL 7 and later modification example: Add transparent_hugepage=never transparent_hugepage.defrag=never at the end of the GRUB_CMDLINE_LINUX entry.

```
   # Add transparent_hugepage=never at the end of the GRUB_CMDLINE_LINUX entry.
GRUB_CMDLINE_LINUX="nomodeset crashkernel=auto rd.lvm.lv=vg_os/lv_root rd.lvm.lv=vg_os/lv_swap rhgb quiet transparent_hugepage=never transparent_hugepage.defrag=never"
GRUB_DISABLE_RECOVERY="true"
```

**Regenerate the GRUB configuration file::**

**- BIOS-based systems:**

```
 $ grub2-mkconfig -o /boot/grub2/grub.cfg
```

**- UEFI-based systems:**

```
$ grub2-mkconfig -o /boot/efi/EFI/redhat/grub.cfg
```

**OS reboot:**

Reboot the OS to apply the changes.

**2. Add rc.local configuration (RHEL 6 only)**

```
$ vi /etc/rc.d/rc.local
```

Add the following content at the end of the file.

```
if test −f /sys/kernel/mm/transparent_hugepage/enabled; then
echo never > /sys/kernel/mm/transparent_hugepage/enabled
fi
if test −f /sys/kernel/mm/transparent_hugepage/defrag; then
echo never > /sys/kernel/mm/transparent_hugepage/defrag
fi
```

##### 3. Using tuned: RHEL 7 and above

On RHEL 7 or later, configuring a tuned profile may be necessary.

Check the active tuned profile:

If the tuned service is stopped or there is no active profile, this step is not needed. If tuned is active, check the current profile and apply the settings.

```
$ tuned-adm active
```

example:

```
Current active profile: throughput-performance
```

Changing the profile configuration: Example when the currently active profile is throughput-performance

```
$ cd /usr/lib/tuned/throughput-performance
$ vi tuned.conf
```

If there is a transparent_hugepage setting in the [vml] session, modify it; if not, leave it as is.

```
[vm]
transparent_hugepage=never
```

Apply the changed profile:

```
$ tuned-adm profile 'profile_name'
```

Restart the OS to confirm the changes. The OS reboot can be done once after all kernel parameter changes are made.

### max_map_count

Check the current settings, and if the recommended configuration is not applied, refer to the guide below to make the necessary changes.

**1. Using cat**

```
$ cat /proc/sys/vm/max_map_count
```

**2. Using sysctl**

```
$ sysctl -a | grep max_map_count
```

#### How to change the max_map_count setting

#### **Temporary application**

Use the sysctl command. This setting applies immediately but will reset after the OS is restarted..

```
$ sysctl -w vm.max_map_count=2147483647
```

#### **Permanent application**

The following method ensures the setting is retained even after rebooting the OS. To fully apply the configuration, the OS must be restarted.

**1. Modify the default sysctl.conf file**

```
$ vi /etc/sysctl.conf
```

Add vm.max_map_count = 2147483647 or modify the existing value.

```
vm.max_map_count = 2147483647
```

**2. Add rc.local configuration (RHEL 6 only)**

```
$ vi /etc/rc.d/rc.local
```

Add the following content at the end of the file.

```
echo 2147483647 > /proc/sys/vm/max_map_count
```

##### 3. Using tuned: RHEL 7 and above

On RHEL 7 or later, configuring a tuned profile may be necessary.

Check the active tuned profile:

If the tuned service is stopped or there is no active profile, this step is not required. If tuned is active, check the current profile and apply the appropriate settings.

```
$ tuned-adm active
```

example:

```
Current active profile: throughput-performance
```

Changing the profile configuration: Example when the currently active profile is throughput-performance

```
$ cd /usr/lib/tuned/throughput-performance
$ vi tuned.conf
```

If there is a max_map_count setting in the [sysctl] session, modify it; if not, leave it as is.

```
[sysctl]
vm.max_map_count=2147483647
```

Apply the changed profile.

```
$ tuned-adm profile 'profile_name'
```

Restart the OS to verify the changes. You can perform the OS reboot once after all kernel parameter changes are completed.

### Shared Memory and Semaphore

#### How to Check Set Value

###### ipcs command

How to check shared memory and semaphore 1 - Using ipcs command

```
# Check shared memory kernel parameter settings
$ ipcs -m -l
------ Shared Memory Limits --------
max number of segments = 4096                         # shmmni (Recommended: 4096)
max seg size (kbytes) = 2097152                       # shmmax (Recommended: 2097152)
max total shared memory (kbytes) = 137438953472
min seg size (bytes) = 1

# Check the semaphore kernel parameter settings
$ ipcs -s -l
------ Semaphore Limits --------
max number of arrays = 5029                           # semmni (Recommended: 5029)
max semaphores per array = 2000                       # semmsl (Recommended: 2000)
max semaphores system wide = 32000                    # semmns (Recommended: 32000)
max ops per semop call = 512                          # semopm (Recommended: 512)
semaphore max value = 32767
```

###### sysctl command

How to check shared memory and semaphore 2 - Using sysctl command

```
# Examples of statements and results
$ sysctl -a | grep -e kernel.shmmax -e kernel.shmmni -e kernel.sem
kernel.shmmax = 2147483648
kernel.shmmni = 4096
kernel.sem = 2000        32000   512     5029
```

#### How to Change the Settings

##### Change Immediately

Use the echo command.

Immediate change shared memory and semaphores

```
# Shared Memory Settings
echo 4096 > /proc/sys/kernel/shmmni
echo 2147483648 > /proc/sys/kernel/shmmax

# Semaphore settings
echo 2000 32000 512 5029 > /proc/sys/kernel/sem
```

##### Permanent Application

Add to /etc/sysctl.conf file.

Shared memory and semaphore permanent application - /etc/sysctl.conf

```
$ vi /etc/sysctl.conf
kernel.shmmni = 4096
kernel.shmmax = 2147483648
kernel.sem = 2000        32000   512     5029
```

Restart the OS to see the changes. Restarting the OS may be performed at once after all kernel parameters are changed.

## User Setting

---

This section describes the user settings required to install and operate the Altibase server on Linux. A user is an OS user, and is a user who installs the Altibase server and runs the Altibase server process.

The user login configuration file in the bash shell is .bash_profile. The user configuration file differs depending on the shell, but it is described based on the Linux default shell because it is a bash shell.

The user setting is divided into the following two categories:

- Resource limitation
- Environment variable

### Resource Limitation

Linux provides settings to limit system resources such as CPU, memory, and files. Proper configuration is necessary because the purpose of preventing a specific user from monopolizing system resources, or the limitation of file creation or memory allocation, has a fatal effect on the operation of the Altibase server.

The resource items and recommended values in the Altibase server operating environment are as follows.

| ulimit command | Items in limits.conf | Description | Recommended Value |
| --- | --- | --- | --- |
| data seg size (kbytes, -d) | data | The maximum memory size of the process data area | unlimited |
| file size (blocks, -f) | fsize | The maximum size of files that can be created | unlimited |
| open files (-n) | nofile | The maximum number of open file descriptors a process can open | 1048576 |
| max memory size (kbytes, -m) | rss | The maximum amount of available memory | unlimited |
| virtual memory (kbytes, -v) | as | The maximum amount of virtual memory available | unlimited |
| max user processes (-u) | nproc | The maximum number of processes (including threads) that the user can run | unlimited |

### Related Error Message

This is an error message caused by resource limitations. If the following message is checked while operating the Altibase server, it is necessary to check the resource limit settings.

- Insufficient max user processes

    - Failed to create a thread object.
    - resource temporarily unavailable
- Insufficient open files

    - Too many open files

### View and Change Resource Settings

Resource limits are set for each user, but apply individually to user processes.

To reflect the changed resource limit settings to the Altibase server, the Altibase server must be restarted.

#### How to Check Set Value

This command checks the resource limit setting value.

```
$ ulimit -a        # If -S or -H option is not specified, -S (Soft-Limit) is output.

$ ulimit -Ha       # Output the Hard-Limit setting value.
```

Check the resource limit set in the Altibase server process with the following command.

```
$ cat /proc/`ps -ef | grep 'altibase -p' | grep -v grep | awk '{print $2}'`/limits
```

If the desired settings are not applied to the Altibase server process, the Altibase server must be restarted.

### How to Change the Settings

##### Execute ulimit command

ulimit is a command to set resource limits. The ulimit configuration command is added to the .bash_profile of the configuration file of the OS user who installs and runs the Altibase server.

User resource limit setting example - added to .bash_profile

```
#For Resource Limitation
ulimit -d  unlimited  # data segment size
ulimit -f  unlimited  # file size
ulimit -n  1048576    # file descriptor(open files)
ulimit -m  unlimited  # max memory size(rss)
ulimit -v  unlimited  # virtual memory
ulimit -u  unlimited  # user process
```

##### Apply the configuration file (.bash_profile)

Apply ulimit setting with the following command.

```
. ~/.bash_profile
```

When applying the configuration file, the following error may occur.

```
-bash: ulimit: open files: cannot modify limit: Command not accepted
-bash: ulimit: max user processes: cannot modify limit: Command not accepted
```

This is an error caused by Hard-Limit.

###### Hard-Limit & Soft-Limit

System resource limits include Hard-Limit and Soft-Limit. Hard-Limit means the maximum resource limit setting value that can be set by the OS general user, and Soft-Limit means the resource limit value set by the user.

If Hard-Limit is smaller than the value that user wants to set as ulimit, 'cannot modify limit' error occurs.

How to check Hard-Limit

```
$ ulimit -H -u -n    # The -H option means Hard-Limit.
max user processes              (-u) 1024
open files                      (-n) 4096
```

##### Change /etc/security/limits.conf

Hard-Limit changes require root privileges. Add the following setting to the limits.conf file and save it.

Hard-Limit configuration example - OS user name is altibase

```
#<domain>      <type>  <item>         <value>
altibase         -     nofile          1048576
altibase         -     nproc           unlimited
```

Log in as the OS user and perform step 2 again.

### Environment Variables

This is an environment variable to be set after installing the Altibase server.

| Classification | Environment Variable | Description | Setting Value |
| --- | --- | --- | --- |
| Required (Auto Setting) | ALTIBASE_HOME | Specifies the path where Altibase is installed | Depends on the environment |
| Required (Auto Setting) | PATH | Finds the location Altibase's utilities and shell scripts | $ALTIBASE_HOME/bin |
| Required (Auto Setting) | LD_LIBRARY_PATH | Finds the location of the Altibase dynamic library | $ALTIBASE_HOME/lib |
| Required (Auto Setting) | CLASSPATH | Finds the location of the Java Class file | $ALTIBASE_HOME/lib |
| Required (Manual Setting) | ALTIBASE_NLS_USE | Sets the Altibase client character set. Set the same as the Altibase server character set. | Same as Altibase server character set |
| Required (Manual Setting) | LANG | Defines the user's system locale | It is affected by the Altibase server character set. |
| Select (Manual Setting) | MALLOC_ARENA_MAX | - A feature added in Red Hat Enterprise Linux 6 to improve performance issues due to memory contention between threads in a multi-threaded application environment.<br>- The default is the number of CPU cores * MALLOC_ARENA_TEST.<br>- The default value of MALLOC_ARENA_TEST environment: 2 for 32-bit, 8 for 64-bit.<br>- The MALLOC_ARENA_MAX environment variable works properly in glibc2.10 or later. | - |

- Environment variable MALLOC_ARENA_MAX

    - This environment variable is optional.
    - In general, consider keeping the default value and setting it smaller than the default value if a memory issue is found.
    - Since this environment variable affects the performance and memory usage of the Altibase server process according to the set value, it is difficult to recommend the same value collectively.
    - The default value of this environment variable is influenced by the number of CPU cores. As the number of CPU cores increases, the VSZ of the Altibase server process may increase excessively.

#### How to Set Environment Variables

##### How to Check the Set Value

Check if the required environment variables are set correctly.

###### env command

The env result prints all environment variables set for the session.

```
$ env
```

###### echo command

The specified environment variable settings are output. If the value is not output, it means that the environment variable is not set.

```
# This is an example of checking the ALTIBASE_HOME environment variable setting value using the echo command.
$ echo $ALTIBASE_HOME
```

##### How to Change the Settings

This is a method of setting the ALTIBASE_NLS_USE and LANG environment variables that must be manually set among the required environment variables.

###### Check the Altibase server character set

```
iSQL> SELECT NLS_CHARACTERSET FROM V$NLS_PARAMETERS;
```

###### Set environment variables in .bash_profile file

Environment variables are set in units of OS user sessions. Therefore, it must be added to the user configuration file .bash_profile to be applied every time an OS user connects.

The table below shows the ALTIBASE_NLS_USE and LANG environment variable settings according to the Altibase server character set.

| Altibase Server Character Set | ALTIBASE_NLS_USE | LANG |
| --- | --- | --- |
| MS949 | MS949 | ko_KR.euckr |
| KO16KSC5601 | KO16KSC5601 | ko_KR.euckr |
| UTF8 | UTF8 | ko_KR.utf8 |

Refer to the table above and add environment variables to the user configuration file .bash_profile.

Environment variable setting example - added to .bash_profile

```
# This is an example when the Altibase server character set is UTF8.
# Add the following contents to .bash_profile and save.
export ALTIBASE_NLS_USE=UTF8
export LANG=ko_KR.utf8
```

###### Apply to the configuration file .bash_profile

Apply the environment variable added with the following command.

```
. ~/.bash_profile
```

## Summary

---

| Category | Recommendation setting | How to check |  |  |
| --- | --- | --- | --- | --- |
| **Kernel Parameter** | CPU frequency Governor | performance | cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor \| sort -u |  |
| CPU core clock speed is fixed at maximum | grep MHz /proc/cpuinfo \| sort -u |  |  |  |
| RemoveIPC | no | grep RemoveIPC /etc/systemd/logind.conf |  |  |
| swappiness | 1 | cat /proc/sys/vm/swappiness or sysctl -a \| grep swappiness |  |  |
| THP | never | cat /sys/kernel/mm/transparent_hugepage/enabled<br>cat /sys/kernel/mm/transparent_hugepage/defrag |  |  |
| All 0 besides Hugepagesize | grep -i huge /proc/meminfo |  |  |  |
| Including transparent_hugepage=never | cat /proc/cmdline |  |  |  |
| max_map_count | 2147483647 | cat /proc/sys/vm/max_map_count |  |  |
| **Shared Memory** | shmmni | 4096 | ipcs -m -l<br>sysctl -a \| grep -e kernel.shmmax -e kernel.shmmni |  |
| shmmax | 2147483648 |  |  |  |
| Semaphore | semmsl | 2000 | ipcs -s -l<br>sysctl -a \| grep kernel.sem |  |
| semmns | 32000 |  |  |  |
| semopm |  | 512 |  |  |
| semmni | 5029 |  |  |  |
| OS User Resource Limitation | data seg size | (kbytes, -d) | unlimited | ulimit -a |
| file size | (blocks, -f) | unlimited |  |  |
| open files | (-n) | 1048576 |  |  |
| max memory size | (kbytes, -m) | unlimited |  |  |
| virtual memory | (kbytes, -v) | unlimited |  |  |
| max user processes | (-u) | unlimited |  |  |
| OS User Environment Variable | ALTIBASE_HOME |  | Altibase installation path (absolute path) | env |
| PATH |  | $ALTIBASE_HOME/bin |  |  |
| LD_LIBRARY_PATH |  | $ALTIBASE_HOME/lib |  |  |
| CLASSPATH |  | $ALTIBASE_HOME/lib |  |  |
| ALTIBASE_NLS_USE |  | Same as Altibase server character set |  |  |
| LANG |  | Based on Altibase server character set |  |  |

## Others

---

### Red Hat Enterprise Linux Recommended Swap Size

Red Hat Linux recommends the following for Swap sizing.

- In the past, twice as much swap space as physical memory was recommended, but today with terabytes of memory, the previous recommendation is not practical.
- For systems with more than 140 logical processors or systems with more than 3 TB of RAM, a minimum swap space of 100 GB is recommended.

For details, refer to the Red Hat CUSTOMER PORTAL page.

- [What is the recommended swap size for Red Hat Enterprise Linux?](https://access.redhat.com/ko/solutions/744483)

### Force termination of Altibase server process by timeout setting when registering Altibase startup service with systemd

Note for Linux distributions using RHEL 7 or higher or systemd.

If there is a timeout setting in the systemd service configuration file, there may be a phenomenon in which the Altibase server process is forcibly terminated by the OS while the Altibase server process is running during the OS boot process.

- TimeoutStartSec or TimeoutSec

  In this case, the following message is left in the system log (messages).

Jun 3 07:25:26 r-sky-ex altibase: [SM] Recovery Phase - 2 : Loading Database

Jun 3 07:26:53 r-sky-ex systemd: altibase.service start operation timed out. Terminating. Jun 3 07:26:53 r-sky-ex systemd: Failed to start altibase 7.1. Jun 3 07:26:53 r-sky-ex systemd: Unit altibase.service entered failed state. Jun 3 07:26:53 r-sky-ex systemd: altibase.service failed.

The time it takes to run the Altibase server process may take a long time depending on the situation.
- Memory data and memory index is large or
- When Restart Recovery is in progress while Altibase is running

TimeoutStartSec or TimeoutSec setting value must be set enough according to the operating environment or set to 0 (timeout disabled).

Similarly, there is a TimeoutStopSec setting.

Please refer to 'man systemd.service' for more details.

### SYS area CPU usage increase on servers where Symantec Endpoint Protection (SEP) for Linux is installed

It has been found that the CPU usage of the SYS area of the Altibase server process is increased by the Symantec Endpoint Protection process.

As a result of vtune analysis, as the number of Altibase sessions increases, the CPU usage of the SYS area increases significantly by system calls select() and write().

There is a case where the cause was not identified by Broadcom, and the vaccine program was changed. (As of June 2020)

The server environment where the symptoms are reported is as follows.

- Red Hat Enterprise Linux 7
- Symantec Endpoint Protection(SEP) for Linux

# References

---

### Linux Compatibility

- [Altibase 7.1 Korean manuals - Installation Guide#OS-Patch](https://github.com/ALTIBASE/Documents/blob/master/Manuals/Altibase_7.1/kor/Installation.md#os-patch)
- [Bug 1244002 - NFS and Fuse mounts hang while running IO - Malloc/free deadlock](https://bugzilla.redhat.com/show_bug.cgi?id=1244002)
- [Which platforms (OS) does Altibase HDB support?](https://docs.altibase.com/pages/viewpage.action?pageId=9110736)

### CPU Frequency Governor

- [Red Hat Enterprise Linux 6 Power Management Guide - 3.2. Using CPUfreq Governors](https://access.redhat.com/documentation/ko-kr/red_hat_enterprise_linux/6/html/power_management_guide/cpufreq_governors)
- [Red Hat Enterprise Linux 6 Power Management Guide - 2.5.2. Tuned-adm](https://access.redhat.com/documentation/ko-kr/red_hat_enterprise_linux/6/html/power_management_guide/tuned-adm)
- [Red Hat Enterprise Linux 6 Performance Tuning Guide - 7.2. File System Performance Profiles](https://access.redhat.com/documentation/ko-kr/red_hat_enterprise_linux/6/html/performance_tuning_guide/ch07s02)
- [Red Hat Enterprise Linux 6 Power Management Guide - CPUfreq Setup](https://access.redhat.com/documentation/ko-kr/red_hat_enterprise_linux/6/html-single/power_management_guide/index#cpufreq_setup)
- [Red Hat Enterprise Linux 7 Power Management Guide - CPUfreq Drivers](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html-single/power_management_guide/index#cpufreq_drivers)
- [Red Hat Enterprise Linux 6 Power Management Guide](https://access.redhat.com/documentation/ko-kr/red_hat_enterprise_linux/6/html-single/power_management_guide/index)
- [Red Hat Enterprise Linux 7 Performance Tuning Guide](https://access.redhat.com/documentation/ko-kr/red_hat_enterprise_linux/7/html-single/performance_tuning_guide/index)
- [RHEL7: How to get started with CPU governor](https://www.certdepot.net/rhel7-get-started-cpu-governor/)

### RemoveIPC

- [logind.conf(5) - Linux manual page - man7.org](http://man7.org/linux/man-pages/man5/logind.conf.5.html)
- [Daemons using IPC terminate unexpectedly after update to Red Hat Enterprise Linux 7.2](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/7.2_release_notes/known-issues-installation_and_booting)
- [Database Installation and Operation Fails if RemoveIPC=yes Is Configured for systemd - Oracle Docs](https://docs.oracle.com/cd/E52668_01/E67200/html/section-t51_kcn_f5.html)
- [IBM Db2 servers might crash when RemoveIPC for Red Hat Enterprise Linux 7.2 is set to yes](https://www.ibm.com/support/knowledgecenter/en/SS5R93_5.3.2/com.ibm.spectrum.sc.doc/fqz0_r_tbs_db2_rhel72.html)

### Swappiness

- [Wikipedia - Paging#Swappiness](https://en.wikipedia.org/wiki/Paging#Swappiness)
- [Wikipedia - Page cache](https://en.wikipedia.org/wiki/Page_cache)
- [Wikipedia - Talk:Swappiness](https://en.wikipedia.org/wiki/Talk%3ASwappiness)
- [Recommended swap size for Red Hat Enterprise Linux](https://access.redhat.com/ko/solutions/744483)
- [Red Hat Enterprise Linux 7 Performance Tuning Guide - 4.3. Configuration Tools](https://access.redhat.com/documentation/ko-kr/red_hat_enterprise_linux/7/html/performance_tuning_guide/sect-red_hat_enterprise_linux-performance_tuning_guide-memory-configuration_tools)

### THP

- [Red Hat Enterprise Linux - Huge Pages and Transparent Huge Pages](https://access.redhat.com/documentation/ko-kr/red_hat_enterprise_linux/6/html/performance_tuning_guide/s-memory-transhuge)
- [System hang due to THP (Transparent Huge Page)](https://support.hpe.com/hpsc/doc/public/display?docId=mmr_kc-0111835)
- [How to use, monitor, and disable transparent hugepages in Red Hat Enterprise Linux 6 and 7?](https://access.redhat.com/solutions/46111)
- [Disabling Transparent HugePages - Oracle Docs](https://docs.oracle.com/en/database/oracle/oracle-database/18/ladbi/disabling-transparent-hugepages.html#GUID-02E9147D-D565-4AF8-B12A-8E6E9F74BEEA)
- [Transparent Huge Pages on Linux - SAP Help Portal](https://help.sap.com/viewer/bed8c14f9f024763b0777aa72b5436f6/2.0.04/en-US/8049ba0c8df2454dbbf8dc7caf636021.html)
- [Transparent hugepages are not disabled on Red Hat Enterprise Linux 6](https://access.redhat.com/ja/solutions/1315213)
- [Disable transparent hugepages (THP) on Red Hat Enterprise Linux 7](https://access.redhat.com/ja/solutions/1565043)
- [CentOS / RHEL 6: How to disable Transparent Huge Pages (THP)](https://www.thegeekdiary.com/centos-rhel-6-how-to-disable-transparent-huge-pages-thp/)
- [CentOS / RHEL 7: How to disable Transparent Huge Pages (THP)](https://www.thegeekdiary.com/centos-rhel-7-how-to-disable-transparent-huge-pages-thp/)

### max_map_count

- [Linux kernel sysctl vm documentation](https://www.kernel.org/doc/Documentation/sysctl/vm.txt)
- [Red Hat Enterprise Linux 7 Performance Tuning Guide - 7.5. Configuring System Memory Capacity](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/performance_tuning_guide/sect-red_hat_enterprise_linux-performance_tuning_guide-configuration_tools-configuring_system_memory_capacity)
- [Additional OS validations required for SAP Applications on RHEL 7](https://blogs.sap.com/2018/11/29/additional-os-validations-required-for-sap-applications-on-rhel-7./)

### Shared Memory and Semaphore

- IPCDA is a communication method supported from Altibase 7.
- [Altibase 7.1 Korean manuals - Administrator's Manual 2#Server-client communication](https://github.com/ALTIBASE/Documents/blob/master/Manuals/Altibase_7.1/kor/Admin_2.md#%ED%86%B5%EC%8B%A0-%EB%B0%A9%EB%B2%95)
- [Altibase 7.1 Korean manuals - Installation Guide#OS-specific kernel parameter settings](https://github.com/ALTIBASE/Documents/blob/master/Manuals/Altibase_7.1/kor/Installation.md#os%EB%B3%84-%EC%BB%A4%EB%84%90-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0-%EC%84%A4%EC%A0%95)

### Locale

- [ArchWiki - Locale](https://wiki.archlinux.org/index.php/Locale_(%ED%95%9C%EA%B5%AD%EC%96%B4))

### MALLOC_ARENA_MAX

- [Red Hat Enterprise Linux 6.0 Release Notes - Compiler and Tools](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/6.0_release_notes/compiler)
- [Linux glibc 2.10 / RHEL 6 malloc may show excessive virtual memory usage](https://www.ibm.com/developerworks/community/blogs/kevgrig/entry/linux_glibc_2_10_rhel_6_malloc_may_show_excessive_virtual_memory_usage?lang=en)
- [Presto issue 8993](https://github.com/prestodb/presto/issues/8993)

# Korean Source Attachments

The Korean source page also references these downloadable source attachments. They are preserved here so the English document set does not lose those references.

- [Korean source attachment 1 (PDF)](https://docs.altibase.com/download/attachments/13436485/Altibase_%EC%9A%B4%EC%98%81%EC%9D%84_%EC%9C%84%ED%95%9C_Linux_%EC%84%A4%EC%A0%95_%EA%B0%80%EC%9D%B4%EB%93%9C_2019.pdf?version=1&modificationDate=1584944731000&api=v2)
- [Korean source attachment 2 (PDF)](https://docs.altibase.com/download/attachments/13436485/ALTIBASE_%EC%9A%B4%EC%98%81%EC%9D%84_%EC%9C%84%ED%95%9C_Linux_%EC%84%A4%EC%A0%95_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1698366100000&api=v2)
