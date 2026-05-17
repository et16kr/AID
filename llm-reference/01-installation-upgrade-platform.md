# Installation, Upgrade, and Platform

## Source paths

R004 source paths covered in this revision:

- `arch/Home/Altibase Installation Guide__14647632.md`
- `arch/Home/Altibase Installation Guide/1. Altibase HDB package installer__14647639.md`
- `arch/Home/Altibase Installation Guide/2. Product Installation using the Package Installer__14647653.md`
- `arch/Home/Altibase Installation Guide/3. License Key Request__14647666.md`
- `arch/Home/Altibase Quick Install & Start for UNIX__16875604.md`
- `arch/Home/Troubleshooting Altibase Installation Problems__15138879.md`
- `arch/Home/Creating ALTIBASE Database__22643020.md`
- `FAQE/Home/01. Installation, Patch, Upgrade/What Platforms (OS) Altibase HDB supports__16875920.md`
- `FAQE/Home/01. Installation, Patch, Upgrade/Altibase Server Patch Procedure on Unix and Linux__16875922.md`
- `FAQE/Home/01. Installation, Patch, Upgrade/Altibase Client Installation/Starting from ALTIBASE HDB 5.5.1__16875941.md`
- `FAQE/Home/01. Installation, Patch, Upgrade/What to do when installing Altibase on Windows, and it says _It has already been installed__16875943.md`

R005 source paths covered in this revision:

- `arch/Home/Linux Setup Guide for Altibase__22643022.md`
- `arch/Home/Solaris Setup Guide for Altibase__14058290.md`
- `arch/Home/Solaris Setup Guide for Altibase/1. Kernel Parameters__22643040.md`
- `arch/Home/Solaris Setup Guide for Altibase/2. User Settings__14058294.md`
- `arch/Home/Solaris Setup Guide for Altibase/3. Summary__14058296.md`
- `arch/Home/HPUX Setup Guide for Altibase__14058288.md`
- `arch/Home/AIX Setup Guide for Altibase__14058298.md`
- `arch/Home/Altibase Docker Guide__14647741.md`
- `arch/Home/Altibase Docker Guide/1. Overview of Docker__14647745.md`
- `arch/Home/Altibase Docker Guide/2. Docker Installation__14647748.md`
- `arch/Home/Altibase Docker Guide/3. Altibase Docker Image__14647754.md`
- `arch/Home/Altibase Docker Guide/4. Creating Altibase Service Container__14647760.md`
- `arch/Home/Altibase Docker Guide/5. Stopping_Deleting Altibase Service Container__14909445.md`

## Source coverage notes

This document covers the R004 and R005 portions of `llm-reference/01-installation-upgrade-platform.md`. R004 covers installation, patching, database creation, startup validation, installation troubleshooting, and the installation FAQ set. R005 adds OS prerequisites and platform setup for Linux, Solaris, HPUX, and AIX, plus Docker image and service-container operation.

All R004 and R005 source files are classified as `Korean-source-verified` or `Link-validated Korean-source-verified` in `llm-reference/coverage/source-inventory.tsv`. Five URL-backed PDF attachments from Korean source pages are preserved in the English source set and registered in `llm-reference/coverage/attachment-diagram-register.tsv`: three from R004 and two Linux setup PDFs from R005. Embedded PNG/JPG installer, registry, and Docker conceptual images are treated as non-document-format source artifacts; this document preserves their procedural meaning without reconstructing the images.

No English-only auxiliary source is used in the R004 or R005 consolidation.

## Scope and audience

Use this document to answer Altibase installation, patch, license, database creation, startup, shutdown, installation-failure, OS-prerequisite, platform-setup, and Docker-container questions. It is written for DBAs, platform engineers, and support engineers who need exact commands, paths, properties, version boundaries, kernel/resource settings, and failure symptoms.

When answering in another language, keep product names, commands, SQL, property names, file paths, error codes, version strings, and package filenames exactly as written.

## Key facts

Altibase installation packages are downloaded from the Altibase support portal, such as `http://support.altibase.com/en/`, and are selected by product type, version, OS, CPU, and bitness. Example server packages include `altibase-HDB-server-6.5.1.X.X-LINUX-X86-64bit-release.run` and `altibase-server-7.1.0.X.X-LINUX-X86-64bit-release.run`. Example client packages include `altibase-HDB-client-6.3.1.3.1-LINUX-X86-64bit-release.run`.

The Altibase Package Installer is Java-based. It installs server products, client libraries, and tools. Server packages include client components, but client-only packages are separate and are used for client-server development and integration. Altibase does not officially provide a 32-bit server package; 32-bit client packages can be provided for client integration.

The package installer creates an Altibase home directory and an `APatch` directory. Default home directory patterns are:

```text
$HOME/altibase-HDB-server-<version>
$HOME/altibase-HDB-client-<version>
```

`$ALTIBASE_HOME/APatch` stores installed product and patch metadata, installer logs, uninstall executables, and rollback backup directories. Typical files include `altibase_base_install.log`, `patchinfo`, `pkg_patch_0_0_0_0.txt`, `pkg_patch_0_0_0_10.txt`, `uninstall-p0_0_0_0`, `uninstall-p0_0_0_10`, and `rollback-p0_0_0_10`.

`patchinfo` records the installed product signature, patch version, OS information, OS patch information, compiler information, and Java information. `pkg_patch_<installed version>.txt` records source-code repository revision information for a patch. `altibase_base_install.log` records actions during the most recent installation.

For patch installation, the package installer backs up files that it patches under `$ALTIBASE_HOME/APatch`. It does not back up data files, log files, or files created after product installation. On HP platforms, automatic backup and rollback are not supported for installer patching; manually back up data and log files.

General server installation requirements in the package installer guide are:

| Requirement | Value |
| --- | --- |
| Memory | 64-bit OS requires at least 1 GB; 2 GB or more is recommended. |
| CPU | 1 CPU or more; 2 CPUs or more are recommended. |
| Disk | Account for `$ALTIBASE_HOME/APatch` patch backups and rollback files. |
| Network | Use a dedicated line when using replication. |

The package installer guide is based on Altibase v7.1.0 on Linux `2.6.32-504.el6.x86_64`. The Quick Install guide uses examples from Altibase 6.5.1 and 7.1.0 package naming. The database creation guide is based on Altibase 7.1.0 or later and states that versions earlier than Altibase ver. 6 were EOS targets at the time of writing.

The Linux setup guide is based on Altibase 5.5.1 or later and Red Hat Enterprise Linux 6 or later. It treats glibc version as the compatibility check basis regardless of Linux distribution type or kernel version. The main recommended Linux settings are `CPUfreq Governor=performance`, `RemoveIPC=no`, `vm.swappiness=1`, `THP=never`, `max_map_count=2147483647`, `kernel.shmmni=4096`, `kernel.shmmax=2147483648`, and `kernel.sem=2000 32000 512 5029`.

The Solaris setup guide is based on Altibase 6 or later and Sun OS 5.8 through 5.10. Solaris 5.10 and earlier can use `/etc/system` settings; Solaris 5.10 also supports project-based shared-memory and semaphore settings with `projadd` and `projmod`.

The HPUX setup guide covers Hewlett Packard Unix platform prerequisites, including IPC shared memory, semaphores, file cache, data-segment and process limits, user resource limits, HPUX-specific library paths, multi-thread environment variables, and required pthread patch checks.

The AIX setup guide is based on AIX 5.x and explicitly does not cover AIX 4.3 or earlier because those versions are no longer supported by Altibase. AIX prerequisites include Posix AIO, file-cache tuning for applicable AIX levels, process limits, user resource limits, multi-thread environment variables, AIX native compiler patch `IV28577`, and version-dependent IPC channel limits.

The Docker guide is based on Altibase 7.1.1 or later and Docker 19.03.2 or later. Docker itself requires Linux kernel version 3.10.X or later. Docker commands normally require root privileges; if a non-root user needs to run Docker without `sudo`, add that user to the `docker` group.

## Procedures

### Server Package Installation

Before installation, create an OS user account to own the Altibase installation. Download the correct package for the target version, OS, CPU, and bitness. Check OS information with `uname -a` on Unix/Linux, and obtain a license using the target host MAC address.

Grant execute permission to the `.run` package:

```bash
chmod +x altibase-server-7.1.0.0.0-LINUX-X86-64bit-release.run
chmod 744 altibase-HDB-server-6.5.1.7.1-LINUX-X86-64bit-release.run
```

Run the installer:

```bash
./altibase-server-7.1.0.0.0-LINUX-X86-64bit-release.run
./altibase-HDB-server-6.5.1.7.1-LINUX-X86-64bit-release.run
```

The installer first checks the OS name, OS version, and OS mode, such as 64-bit or 32-bit. If this pre-check does not match the package, installation stops.

The installer can run in GUI mode or interactive text mode. GUI mode is used when `DISPLAY` is set. Text mode is used when `DISPLAY` is not set. If an incorrect `DISPLAY` IP or port causes a hang-like condition, unset `DISPLAY` or run the package with `-mode text`.

Select the installation directory and package installation type. `Full Installation` installs the product. `Patch Installation` patches an existing installation. If the chosen directory already contains an Altibase product, choose another directory or uninstall the existing product first.

The installer property stage has three steps:

| Step | Settings |
| --- | --- |
| Basic Database Operation Properties | Database name, connection port number, maximum memory database size, buffer area size, and whether to generate a database creation SQL script. |
| Database Creation Properties | Initial database size, `Noarchivelog` or `Archivelog`, database character set, and national character set. |
| Database Directories | Default disk database directory, memory database directory, archive log directory, transaction log directory, and three log anchor directories. |

Important defaults and prompts include:

| Setting | Default or example | Meaning |
| --- | --- | --- |
| Database name | `mydb` | Changing the DB name later requires database recreation. |
| Connection port | `20300` | Valid installer prompt range is `1024-65535`. |
| `MEM_MAX_DB_SIZE` | `2G` | Maximum value of data stored in memory; it is a limit, not pre-allocated memory. |
| `BUFFER_AREA_SIZE` | `128M` | Memory pre-allocated as disk table buffer area. |
| Initial database size | `10M` | Installer prompt range in the Quick Install example is `4M-4G`. |
| Archive logging | `noarchivelog` | Select `Archivelog` only when archive log management and disk capacity are planned. |
| Database character set | `UTF8` | Other source-listed options include `MS949`, `US7ASCII`, `KO16KSC5601`, `BIG5`, `GB231280`, `MS936`, `SHIFTJIS`, `MS932`, and `EUCJP`. |
| National character set | `UTF8` or `UTF16` | Used for `NVARCHAR` and `NVARCHAR2`. |

If a property was not included in the installer step, or a Step 1 or Step 3 value must be changed after installation, edit:

```text
$ALTIBASE_HOME/conf/altibase.properties
```

After property review, proceed with product installation. The installer updates `altibase.properties`, creates `$ALTIBASE_HOME/conf/altibase_user.env`, and adds the environment file execution command to the user shell profile, such as `.bashrc`, `.bash_profile`, or `.profile`.

License registration has three modes:

- Manually enter the license key.
- Select the license key file.
- Register the license later by copying the license file to `$ALTIBASE_HOME/conf/license`.

If a license is not registered during installation, the installer does not ask whether to create a database in the next step. Copy the license later with:

```bash
cp license $ALTIBASE_HOME/conf/
```

The installer Quick Setup Guide exposes these files:

| File | Purpose |
| --- | --- |
| `$ALTIBASE_HOME/install/pre_install.sh` | Minimum essential system kernel parameter guidance. |
| `$ALTIBASE_HOME/install/post_install.sh` | Database creation SQL script when database properties were entered. |
| `$ALTIBASE_HOME/packages/catproc.sql` | SQL script for using PSM. |

The package installer can create the database and run `catproc.sql` when the Quick Setup checkbox is selected. If it is not selected, manually create the database and run the PSM script later.

Post-installation steps are:

1. Set kernel parameters manually if they were not set during installation; refer to `$ALTIBASE_HOME/install/pre_install.sh`.
2. Re-login or run the shell profile, for example `source ~/.bash_profile`.
3. If the database was not created during installation, run `$ALTIBASE_HOME/install/post_install.sh dbcreate` when database properties were entered, or run `server create utf8 utf8` when they were not.
4. If PSM was not configured during installation, run `catproc.sql`.

```bash
sh post_install.sh dbcreate
server create utf8 utf8
isql -s 127.0.0.1 -u sys -p manager -silent -f ${ALTIBASE_HOME}/packages/catproc.sql
```

### License Request and MAC Address Collection

Altibase is commercial software. A license certificate contains a license key suitable for the installation host. For purchase, contact `sales@altibase.com`. License issuance requires the OS MAC address.

Use these commands and formatting rules to collect the MAC address:

| OS | Command | Input rule |
| --- | --- | --- |
| Linux | `ifconfig -a` or `/sbin/ifconfig -a` | Enter the 12 digits from `HWaddr`, excluding colons. |
| Solaris | `ifconfig -a` as root | Enter the 12 digits from `ether`, excluding colons. |
| AIX | `lscfg -vp` or `lscfg -vpl` | Enter the 12 digits from `Network Address`. |
| HP-UX | `lanscan` or `/usr/sbin/lanscan` | Enter the 12 digits from `Address`, excluding `0x`. |
| Windows | `ipconfig /all` | Enter the 12 digits from `Physical Address`, excluding hyphens. |

### Database Creation

Altibase cannot be operated until the database is created. Check `DB_NAME` before creation:

```bash
cat $ALTIBASE_HOME/conf/altibase.properties | grep DB_NAME
```

If `DB_NAME` is not `mydb`, edit `$ALTIBASE_HOME/bin/server` so the `create database mydb` command uses the configured `DB_NAME`.

Create the database through the server script:

```bash
server create UTF8 UTF16
```

The syntax is:

```text
server create <database character set> <national character set>
```

Alternatively, create the database with `isql` in `sysdba` mode:

```sql
startup process;
create database mydb INITSIZE=10M noarchivelog character set UTF8 national character set UTF16;
exit;
```

The database character set stores database text data. Source-listed database character sets are `US7ASCII`, `KO16KSC5601`, `MS949`, `BIG5`, `GB231280`, `UTF8`, `SHIFTJIS`, and `EUCJP`. The national character set is Unicode-based and is stored in `NVARCHAR` and `NVARCHAR2`; source-listed values are `UTF8` and `UTF16`.

`DB_NAME` is fixed at database creation. To change it, recreate the database and migrate data. Choose the initial database name carefully.

Archive log mode is set in the control stage. To change from no-archive-log mode to archive-log mode:

```bash
server stop
isql -u sys -p manager -sysdba
```

```sql
startup control;
alter database archivelog;
startup service;
exit;
```

In archive log mode, Altibase copies log files to the configured archive log directory and does not delete them arbitrarily. Secure enough archive log directory space for the backup cycle and expected log volume.

To drop a database, first check files that will be removed:

```sql
select name, checkpoint_path from v$tablespaces a, v$mem_tablespace_checkpoint_paths b where a.id = b.space_id;
select a.name, b.name from v$tablespaces a, v$datafiles b where a.id = b.spaceid;
```

```bash
cat $ALTIBASE_HOME/conf/altibase.properties | grep ^LOG | grep DIR
```

Then enter the process stage and drop the database:

```sql
startup process;
drop database mydb;
exit;
```

The drop operation checks `loganchor0`, `loganchor1`, and `loganchor2`, then removes DB files, log files, and log anchor files.

### Startup, Shutdown, and Startup Validation

Before startup, the Altibase package must be installed, the database must be created, and environment variables must be applied for the installation OS user. On Linux, run the profile, for example:

```bash
source $HOME/.bash_profile
```

Start Altibase with:

```bash
server start
```

Successful startup transitions through `PROCESS`, `CONTROL`, `META`, and `SERVICE`, then shows listener initialization such as:

```text
[CM] Listener started : TCP on port 20300 [IPV4]
[CM] Listener started : UNIX
[CM] Listener started : IPC
[RP] Initialization : [PASS]
--- STARTUP Process SUCCESS ---
Command executed successfully.
```

Altibase can also be started from `iSQL`:

```bash
isql -sysdba
```

```sql
startup service;
```

Common startup validation failures are:

| Symptom | Evidence | Required action |
| --- | --- | --- |
| `server` command not found | `-bash: server: command not found` | Apply the environment file so `$ALTIBASE_HOME/bin` is in `PATH`. |
| `isql` cannot connect | `[ISQL]ERROR: Could not SQLConnect` | Check environment variables and database startup state. |
| Database not created | `[FAILURE] The log anchor file does not exist or is not valid.` and `ERR-91015` | Create the database first. |
| License missing or invalid | `No valid license present!` in `$ALTIBASE_HOME/trc/altibase_boot.log` | Place a valid `license` file under `$ALTIBASE_HOME/conf`. |

Stop Altibase with:

```bash
server stop
```

Altibase can also be stopped from `iSQL`:

```sql
shutdown abort;
shutdown immediate;
shutdown normal;
```

Shutdown options differ:

| Option | Behavior |
| --- | --- |
| `abort` | Forcibly terminates connected sessions and stops immediately without normal shutdown processing. Recovery is performed on next startup. |
| `immediate` | Forcibly terminates connected sessions and stops through normal shutdown processing. |
| `normal` | Waits for all connected sessions to terminate normally, then stops through normal shutdown processing. This wait can be mistaken for a hung shutdown. |

### Client Installation from ALTIBASE HDB 5.5.1

The client installation FAQ covers Linux, HP-UX, AIX, and Solaris. Download the client installation file from `http://support.altibase.com/en/product`. If the desired client version is not available, request it through the support menu, `+82-2-2082-1114`, or `http://support.altibase.com/en/`.

Upload the client installer as the OS user that will own the installation. Add execute permission:

```bash
chmod +x altibase-HDB-client-6.3.1.3.1-LINUX-X86-64bit-release.run
ls -l altibase-HDB-client-6.3.1.3.1-LINUX-X86-64bit-release.run
```

Run the client installer:

```bash
./altibase-HDB-client-6.3.1.3.1-LINUX-X86-64bit-release.run
```

In the source example, select `Full installation` by entering `2` when the prompt offers:

```text
[1] Patch: patch package install
[2] Full installation: full package install
```

Enter the target server service port when prompted for `ALTIBASE HDB connection port number (1024-65535) [20300]`. After successful installation, the installer adds environment variables:

```bash
export ALTIBASE_HOME=/data/heejung.lee/altibase_home
export ALTIBASE_PORT_NO=20300
export PATH=${ALTIBASE_HOME}/bin:${PATH}
export LD_LIBRARY_PATH=${ALTIBASE_HOME}/lib:${LD_LIBRARY_PATH}
export CLASSPATH=${ALTIBASE_HOME}/lib/Altibase.jar:${CLASSPATH}
```

Shell initialization files differ by shell:

| Shell | Initialization file |
| --- | --- |
| Bourne shell or Korn shell | `.profile` |
| bash | `.bash_profile` or `.profile` |
| C shell | `.login` or `.cshrc` |

Apply the environment:

```bash
. ~/.bash_profile
. ~/.profile
echo $ALTIBASE_HOME
```

Verify client installation by connecting with `iSQL` and querying the server version:

```bash
isql -u DB_user_name -p password -s IP -port service_port
isql -u sys -p manager -s 192.168.1.145 -port 20300
```

```sql
SELECT PRODUCT_VERSION FROM V$VERSION;
```

### Patch Procedure on Unix and Linux

A patch is a minor version change. In Altibase server version numbers, the first three digits are the major version and the last one or two digits are the minor version. Changing only the last one or two digits is a patch; changing the first three digits is an upgrade.

Server patching requires service downtime because Altibase must be shut down. Before patching, confirm:

- Downtime is secured with the client.
- Whether the meta version changes after patching.
- Caveats when the patch version differs from the current version, such as patching from HDB 4.3.9.44 to Altibase HDB 4.3.9.233.

Basic patch steps:

1. Check the current version:

```bash
altibase -v
```

2. Shut down Altibase:

```bash
server stop
```

3. Confirm no server process and no service port listener remain. The following commands should return no result after a normal shutdown:

```bash
ps -ef | grep 'altibase -p' | grep -v grep
netstat -an | grep 20300
```

4. Back up installation directories:

```bash
cd $ALTIBASE_HOME
cp -Rp bin bin.bak
cp -Rp lib lib.bak
cp -Rp msg msg.bak
cp -Rp conf conf.bak
cp -Rp include include.bak
```

If `$ALTIBASE_HOME` is not large, make a full home backup:

```bash
cp -Rp altibase_home altibase_home.bak
```

5. For ALTIBASE HDB server 5.5.1 or later, upload the `.run` patch package to any path and grant execute permission:

```bash
chmod +x altibase-HDB-server-6.1.1.3.8-LINUX-X86-64bit-release.run
./altibase-HDB-server-6.1.1.3.8-LINUX-X86-64bit-release.run
```

6. For ALTIBASE HDB versions earlier than 5.5.1, upload the compressed patch package under `$ALTIBASE_HOME`, then extract it:

```bash
cd $ALTIBASE_HOME
gzip -cd altibase-XEON_LINUX_redhat_Enterprise_release5-64bit-5.3.3.84-release-GCC4.1.2.tgz | tar xvf -
```

7. Check the patch version:

```bash
altibase -v
```

8. If the default `sys` password `manager` was changed, restore changed helper scripts from the backup:

```bash
cd $ALTIBASE_HOME
cp -p bin.bak/server bin/
cp -p bin.bak/is bin/
cp -p bin.bak/il bin/
```

9. Start Altibase and validate process and port listener:

```bash
server start
ps -ef | grep 'altibase -p' | grep -v grep
netstat -an | grep 20300
```

If the meta version changes, the database cannot be reverted to a lower version after patching. If downgrade may be needed, take an offline full backup before patching. Offline full backup targets include data files, log anchor files, log files, and configuration files.

Special patch case: If patching from ALTIBASE HDB `4.3.9.1` through `4.3.9.50` to `4.3.9.51` or later in a replication environment, replication will not work after patching unless the special procedure is followed. The procedure is:

1. Secure downtime and stop Altibase.
2. Temporarily change `PORT_NO` in `$ALTIBASE_HOME/conf/altibase.properties` to block client access.
3. Start Altibase.
4. Confirm the replication gap is `0`.
5. Run `aexport` and save the replication object creation syntax from `SYS_CRT_REP.sql`.
6. Stop and drop replication objects.
7. Run `ALTER SYSTEM CHECKPOINT` four times.
8. Stop Altibase and perform the patch.
9. Add `CHECK_LOGFILE = 0` to the end of `altibase.properties`.
10. Start Altibase, then remove `CHECK_LOGFILE = 0`.
11. Create `IMSI_T` and `IMSI_PROC`, execute enough inserts to move `CUR_WRITE_LF_NO` in `V$LFG`, then drop the temporary procedure and table.
12. Run `ALTER SYSTEM CHECKPOINT` four times.
13. Recreate replication objects from `SYS_CRT_REP.sql`.
14. Start replication.
15. Stop Altibase, restore the original service port, start Altibase, and check service.

Core commands and SQL for this special procedure include:

```sql
CREATE TABLE IMSI_T (C1 INTEGER, C2 INTEGER);

CREATE OR REPLACE PROCEDURE IMSI_PROC AS V1 INTEGER;
BEGIN
FOR V1 IN 1 .. 300000 LOOP
INSERT INTO IMSI_T VALUES (V1, V1);
END LOOP;
END;
/
```

```sql
SELECT REP_GAP FROM V$REPGAP;
SELECT REPLICATION_NAME FROM SYSTEM_.SYS_REPLICATIONS_;
ALTER REPLICATION replication_name STOP;
DROP REPLICATION replication_name;
ALTER SYSTEM CHECKPOINT;
SELECT CUR_WRITE_LF_NO FROM V$LFG;
EXEC IMSI_PROC;
ALTER REPLICATION replication_name START;
```

```bash
aexport
is -f SYS_CRT_REP.sql
```

### Windows Reinstall Registry Cleanup

If repeated installation and uninstallation on Windows leaves stale registry data, full package installation can report that Altibase is already installed, and patch installation can report that patching cannot be done.

Run `regedit.exe` from Windows Start, Run. Delete the stale registry entry:

```text
Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Altibase Corp.,
```

After deleting this registry item, run the Altibase installation again.

### Basic Post-Install SQL Use Cases

Altibase provides the `iSQL` utility. When a database is first created, only the DBA account `SYS` exists. The source notes that `$ALTIBASE_HOME/bin/is` is provided as a shell script for easier access to `iSQL`.

Connect through local defaults or explicit TCP settings:

```bash
is
isql -s 127.0.0.1 -u sys -p manager -port 20300
```

Important `isql` options:

| Option | Description |
| --- | --- |
| `-u` | Database user account name. |
| `-p` | Database user password. |
| `-s` | Server network IP address, or `127.0.0.1` for local server. |
| `-port` | Target `PORT_NO` from `$ALTIBASE_HOME/conf/altibase.properties`. |

If the database character set is not `US7ASCII`, set the client session character set with `ALTIBASE_NLS_USE`. For example, if the database was created with `MS949`, set:

```bash
export ALTIBASE_NLS_USE=MS949
```

Use `V$NLS_PARAMETERS` to verify session and database character-set settings:

```sql
set vertical on;
select * from v$nls_parameters;
```

If a session uses `US7ASCII` against `MS949` data, the source sample value `알티베이스` can display as `?????`. After setting `ALTIBASE_NLS_USE=MS949`, the same sample value displays correctly.

Create and drop users:

```sql
CREATE USER new_user IDENTIFIED BY new_user_password DEFAULT TABLESPACE SYS_TBS_DISK_DATA ACCESS SYS_TBS_MEM_DATA ON;
DROP USER new_user CASCADE;
```

Create and drop tablespaces:

```sql
CREATE MEMORY TABLESPACE new_tbs_mem SIZE 1G AUTOEXTEND ON NEXT 128M MAXSIZE 2G;
CREATE DISK TABLESPACE new_tbs_disk DATAFILE 'new_tbs.dbf' SIZE 1G AUTOEXTEND ON NEXT 128M MAXSIZE 2G;
DROP TABLESPACE new_tbs_disk INCLUDING CONTENTS AND DATAFILES;
```

A memory tablespace example creates checkpoint image files such as `$ALTIBASE_HOME/dbs/NEW_TBS_MEM-X-X`. A disk tablespace example creates a data file such as `$ALTIBASE_HOME/dbs/new_tbs.dbf`. When dropping a tablespace, if the drop does not complete normally, active sessions or objects may still be using the tablespace; clean them up and run the drop again.

Query default tablespaces, create memory and disk tables, inspect them, and drop them:

```sql
select type, name from v$tablespaces;
create table mem_tbl (c1 int, c2 varchar(100), c3 char(100));
desc mem_tbl;
create table disk_tbl (c1 int, c2 varchar(100), c3 char(100)) tablespace SYS_TBS_DISK_DATA;
desc disk_tbl;
drop table mem_tbl;
drop table disk_tbl;
```

If no tablespace is specified, Altibase creates a memory table in `SYS_TBS_MEM_DATA`. If `tablespace SYS_TBS_DISK_DATA` is specified, Altibase creates a disk table.

### Linux OS Prerequisites

Check glibc with:

```bash
rpm -q glibc
```

For CPU frequency governor, confirm the current setting and driver status:

```bash
cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor | sort -u
cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor
lsmod | grep cpufreq
cpupower frequency-info | grep driver
cpupower frequency-info --policy
grep MHz /proc/cpuinfo | sort -u
```

If no CPUfreq driver is installed, governor tuning is not required. Otherwise set the governor to `performance`. Temporary changes can use either governor directives or `cpupower`:

```bash
echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor
cpupower frequency-set -g performance
```

For persistent RHEL 6 settings, add the same `echo performance` line to `/etc/rc.local`. For RHEL 7 or later, create or modify `/etc/udev/rules.d/99-cpufreq.rules`:

```text
ACTION=="add", SUBSYSTEM=="cpu", KERNEL=="cpu[0-9]*", ATTR{cpufreq/scaling_governor}="performance"
```

Reload the rule:

```bash
sudo udevadm control --reload-rules
sudo udevadm trigger --subsystem-match=cpu
```

If `tuned` is active on RHEL 7 or later, check the current profile and either include `throughput-performance` in the active profile or switch to `throughput-performance` or `latency-performance`:

```bash
tuned-adm active
cd /usr/lib/tuned/virtual-guest
vi tuned.conf
tuned-adm profile 'profile_name'
tuned-adm profile throughput-performance
```

For `RemoveIPC`, confirm and persist `RemoveIPC=no` in `/etc/systemd/logind.conf`:

```bash
grep RemoveIPC /etc/systemd/logind.conf
vi /etc/systemd/logind.conf
systemctl restart systemd-logind.service
```

`RemoveIPC` has no immediate-change command in the Linux source. Restart the OS or restart `systemd-logind.service` after editing the file.

For `swappiness`, check `vm.swappiness` and set it to `1`:

```bash
cat /proc/sys/vm/swappiness
sysctl vm.swappiness
sysctl -w vm.swappiness=1
```

Persist `vm.swappiness = 1` in `/etc/sysctl.conf` or `/etc/sysctl.d/99-sysctl.conf`. On RHEL 8, also verify `vm.force_cgroup_v2_swappiness`; if it is supported, set it to `1` in both sysctl files. If it is not supported, verify every `memory.swappiness` value under `/sys/fs/cgroup/memory` and change all values to `1` through an OS-vendor-supported workaround.

```bash
sysctl vm.force_cgroup_v2_swappiness
find /sys/fs/cgroup/memory -name memory.swappiness -exec cat {} \; | sort -u
```

For THP, verify `enabled`, `defrag`, `/proc/meminfo`, and boot loader state:

```bash
cat /sys/kernel/mm/redhat_transparent_hugepage/enabled
cat /sys/kernel/mm/redhat_transparent_hugepage/defrag
cat /sys/kernel/mm/transparent_hugepage/enabled
cat /sys/kernel/mm/transparent_hugepage/defrag
grep -i huge /proc/meminfo
cat /proc/cmdline
```

The recommended THP output is `always madvise [never]`; all huge-page counters except `Hugepagesize` should be `0`; boot options should include `transparent_hugepage=never` and `transparent_hugepage.defrag=never`.

Temporary THP disable commands are:

```bash
echo never > /sys/kernel/mm/redhat_transparent_hugepage/enabled
echo never > /sys/kernel/mm/redhat_transparent_hugepage/defrag
echo never > /sys/kernel/mm/transparent_hugepage/enabled
echo never > /sys/kernel/mm/transparent_hugepage/defrag
```

For persistent THP settings, edit `/etc/grub.conf` on RHEL 6 or `/etc/default/grub` on RHEL 7 or later, add `transparent_hugepage=never transparent_hugepage.defrag=never`, regenerate GRUB, and reboot:

```bash
vi /etc/grub.conf
vi /etc/default/grub
grub2-mkconfig -o /boot/grub2/grub.cfg
grub2-mkconfig -o /boot/efi/EFI/redhat/grub.cfg
```

RHEL 6 can also use `/etc/rc.d/rc.local`, and RHEL 7 or later can use a `tuned` `[vm]` setting of `transparent_hugepage=never`.

For `max_map_count`, check and set `2147483647`:

```bash
cat /proc/sys/vm/max_map_count
sysctl -a | grep max_map_count
sysctl -w vm.max_map_count=2147483647
```

Persist `vm.max_map_count = 2147483647` in `/etc/sysctl.conf`, or on RHEL 6 add `echo 2147483647 > /proc/sys/vm/max_map_count` to `/etc/rc.d/rc.local`. RHEL 7 or later can also use a `tuned` `[sysctl]` setting.

For Linux shared memory and semaphore checks:

```bash
ipcs -m -l
ipcs -s -l
sysctl -a | grep -e kernel.shmmax -e kernel.shmmni -e kernel.sem
```

Temporary shared-memory and semaphore settings are:

```bash
echo 4096 > /proc/sys/kernel/shmmni
echo 2147483648 > /proc/sys/kernel/shmmax
echo 2000 32000 512 5029 > /proc/sys/kernel/sem
```

Persist them in `/etc/sysctl.conf`:

```text
kernel.shmmni = 4096
kernel.shmmax = 2147483648
kernel.sem = 2000        32000   512     5029
```

For Linux OS user resource limits, add the recommended `ulimit` commands to the Altibase OS user's `.bash_profile`, apply the file, and restart Altibase so the process inherits the new settings:

```bash
ulimit -d  unlimited
ulimit -f  unlimited
ulimit -n  1048576
ulimit -m  unlimited
ulimit -v  unlimited
ulimit -u  unlimited
. ~/.bash_profile
ulimit -a
ulimit -Ha
cat /proc/`ps -ef | grep 'altibase -p' | grep -v grep | awk '{print $2}'`/limits
```

If applying the profile reports `cannot modify limit`, root must raise the hard limit in `/etc/security/limits.conf`:

```text
altibase         -     nofile          1048576
altibase         -     nproc           unlimited
```

For Linux character-set environment variables, query the server character set and set `ALTIBASE_NLS_USE` and `LANG` in `.bash_profile`:

```sql
SELECT NLS_CHARACTERSET FROM V$NLS_PARAMETERS;
```

```bash
export ALTIBASE_NLS_USE=UTF8
export LANG=ko_KR.utf8
. ~/.bash_profile
```

The source mapping is `MS949 -> ALTIBASE_NLS_USE=MS949, LANG=ko_KR.euckr`, `KO16KSC5601 -> ALTIBASE_NLS_USE=KO16KSC5601, LANG=ko_KR.euckr`, and `UTF8 -> ALTIBASE_NLS_USE=UTF8, LANG=ko_KR.utf8`.

### Solaris OS Prerequisites

For Solaris, set shared memory and semaphore parameters before Altibase installation. Solaris 5.10 or earlier can use `/etc/system`:

```text
set shmsys:shminfo_shmmin = 1
set shmsys:shminfo_shmmax = 2147483649
set shmsys:shminfo_shmmni = 500
set shmsys:shminfo_shmseg = 200
set semsys:seminfo_semmns = 8192
set semsys:seminfo_semmni = 5029
set semsys:seminfo_semmsl = 2000
set semsys:seminfo_semmap = 5024
set semsys:seminfo_semmnu = 1024
set semsys:seminfo_semopm = 512
set semsys:seminfo_semume = 512
```

Restart the system after editing `/etc/system`. Solaris 5.10 can also use project-based settings:

```bash
projadd -U altibase -K "project.max-sem-ids=(priv,5029,deny)" user.altibase
projmod -a -K "project.max-shm-memory=(priv, maximum physical memory, deny)" user.altibase
projmod -a -K "process.max-sem-nsems=(priv,2000,deny)" user.altibase
projmod -a -K "process.max-sem-ops=(priv,512,deny)" user.altibase
projmod -a -K "project.max-shm-ids=(priv,1024,deny)" user.altibase
projmod -a -K "project.max-msg-messages=(priv,100,deny)" user.altibase
projmod -a -K "project.max-msg-ids=(priv,100,deny)" user.altibase
projmod -a -K "process.max-msg-qbytes=(priv,1048576,deny)" user.altibase
projadd -l
```

Set `project.max-shm-memory` to the maximum physical memory value. For Solaris user setup, set resource limits as high as possible, preferably `unlimited`, and configure `ALTIBASE_HOME`, `PATH`, `LD_LIBRARY_PATH`, and `LD_LIBRARY_PATH_64`. If the DB character set is not `US7ASCII` in Altibase 5.3 or later, set `ALTIBASE_NLS_USE`; also align the terminal font with the database character set.

```bash
ALTIBASE_HOME=/ALTIBASE; export ALTIBASE_HOME
PATH=$ALTIBASE_HOME/bin:$PATH; export PATH
ALTIBASE_NLS_USE=MS949; export ALTIBASE_NLS_USE
LD_LIBRARY_PATH=$ALTIBASE_HOME/lib:$LD_LIBRARY_PATH; export LD_LIBRARY_PATH
LD_LIBRARY_PATH_64=$ALTIBASE_HOME/lib:$LD_LIBRARY_PATH_64; export LD_LIBRARY_PATH_64
ulimit -d unlimited
ulimit -f unlimited
ulimit -n unlimited
ulimit -v unlimited
```

### HPUX OS Prerequisites

On HPUX, use `kctune` on HPUX 11.23 or later, `kmtune` on HPUX 11.11, or `sam` for kernel changes. Root access is generally required, and a system restart is recommended after kernel parameter changes.

Shared-memory changes:

```bash
kctune shmmni=500
kctune shmseg=200
```

Semaphore changes:

```bash
kctune semmns=8192
kctune semmni=5029
kctune semmnu=1024
kctune semume=512
```

File-cache changes:

```bash
kctune dbc_min_pct=5
kctune dbc_max_pct=10
kctune filecache_min=5%
kctune filecache_max=10%
```

For `dbc_max_pct`, HP recommends `20%` for systems with 8 GB or less physical memory and `10%` for systems with 8 GB or more. HPUX 11.31 renames `dbc_min_pct` to `filecache_min` and `dbc_max_pct` to `filecache_max`.

Resource-limit kernel changes:

```bash
kctune maxdsiz=2147483648
kctune maxdsiz_64bit=4396972765184
kctune max_thread_proc=600
kctune maxfiles=2048
kctune nproc=6142
```

For HPUX versions earlier than 11.23, do not set `nproc` directly; set `maxusers=124` instead. For HPUX user setup, raise user limits as high as possible and set `ALTIBASE_HOME`, `PATH`, `LD_LIBRARY_PATH`, and `SHLIB_PATH`. `SHLIB_PATH` is required when linking dynamic libraries in 32-bit mode.

HPUX multi-threaded Altibase environments must consider all HP-supported multi-thread environment variables. The source calls out `PTHREAD_FORCE_SCOPE_SYSTEM`, `PERF_ENABLE`, `PTHREAD_FAST_SHARED_OBJECTS`, and `PTHREAD_DISABLE_HANDOFF`; starting from HPUX 11.31, `PERF_ENABLE` behavior is included in `PTHREAD_FORCE_SCOPE_SYSTEM`. It also calls out `_M_ARENA_OPTS=x:y`, where `x` is the number of arenas per process with range `1-64` and default `8`, and `y` is the arena expansion unit in memory pages with range `1-4096` and default `32`.

```bash
export _M_ARENA_OPTS=24:64
swlist -l patch | grep pthread
```

The `pthread library cumulative patch`, such as `PHCO_38955`, directly affects performance. Apply the latest HPUX patches to avoid known platform issues. If `PHCO_33675` or `PHCO_34718` is present on HPUX 11.23, set `PTHREAD_SHARED_MUTEX_OLDSPIN=1` to restore performance degraded by longer-held shared mutexes.

### AIX OS Prerequisites

On AIX, enable Posix AIO before Altibase installation unless AIX 6.1 or later already has Posix AIO in `Available` state. Use `smit` to change `Configure Defined Asynchronous I/O` to `Available`, then set `STATE to be configured at system restart` to `Available`. Check the result with:

```bash
lsdev -C | grep aio
```

For AIX file-cache tuning, use `vmo`:

```bash
vmo -p -o minperm%=10
vmo -p -o lru_file_repage=0
vmo -p -o strict_maxclient=0
vmo -L
```

`lru_file_repage=0` is supported on AIX 5.2 ML5 and AIX 5.3 ML2 or later. `strict_maxclient=0` is supported on AIX 5.2 ML4 or later. AIX 5.2 ML03 or earlier does not have the related file-cache parameters, and AIX 6.1 or later does not require special changes for this section.

For process limits, use `smit`, then `System Environments`, then `Change/Show Characteristics of Operating System`, and set `Maximum number of PROCESSES allowed per user` higher than the number of processes that can run simultaneously. AIX user resource limits should be set to `unlimited` where possible; the system configuration file for user resource limits is `/etc/security/limits`.

For AIX multi-threaded Altibase environments, set representative variables such as `AIXTHREAD_MNRATIO`, `AIXTHREAD_SCOPE`, `PTHREAD_FORCE_SCOPE_SYSTEM`, `AIXTHREAD_MUTEX_DEBUG`, `AIXTHREAD_RWLOCK_DEBUG`, `AIXTHREAD_COND_DEBUG`, `SPINLOOPTIME`, `YIELDLOOPTIME`, `MALLOCMULTIHEAP`, and `AIXTHREAD_MUTEX_FAST`. The source requires `PTHREAD_FORCE_SCOPE_SYSTEM` because it relates to the MxN thread model, but it does not provide an exact example value.

```bash
AIXTHREAD_MNRATIO=1:1; export AIXTHREAD_MNRATIO
AIXTHREAD_SCOPE=S; export AIXTHREAD_SCOPE
AIXTHREAD_MUTEX_DEBUG=OFF; export AIXTHREAD_MUTEX_DEBUG
AIXTHREAD_RWLOCK_DEBUG=OFF; export AIXTHREAD_RWLOCK_DEBUG
AIXTHREAD_COND_DEBUG=OFF; export AIXTHREAD_COND_DEBUG
SPINLOOPTIME=1000; export SPINLOOPTIME
YIELDLOOPTIME=50; export YIELDLOOPTIME
MALLOCMULTIHEAP=1; export MALLOCMULTIHEAP
ulimit -d unlimited
ulimit -f unlimited
ulimit -n unlimited
ulimit -m unlimited
```

Check the AIX `IV28577` heapmin-related patch or upgrade to an AIX native compiler version where it is resolved:

```bash
instfix -i | grep IV28577
```

If no output appears, ask an AIX engineer to apply the patch or upgrade. The source also records an IPC channel limit: AIX fixes `semume` at `1024`; versions earlier than Altibase `5.1.5.72` use two undo entries per IPC channel, so up to `512` IPC channels can be used, while Altibase `5.1.5.72` or later uses three undo entries per IPC channel, so up to `341` IPC channels can be used.

### Docker Image and Container Operation

Install Docker on Ubuntu or CentOS with the Docker-provided scripts, or use the Docker installation page for other platforms:

```bash
sudo wget -qO- http://get.docker.com/ | sh
curl -fsSL https://get.docker.com/ | sudo sh
docker version
```

Download the Altibase-provided image from Docker Hub:

```bash
docker pull altibase/altibase
docker images
```

To create a custom Altibase Docker image, install Altibase first, then place `Dockerfile`, `set_altibase.env`, `docker-entrypoint.sh`, and `altibase_home` in the build context. The source Dockerfile uses `ubuntu:18.04`, adjusts `nofile`, `nproc`, `vm.swappiness`, and `kernel.sem`, copies the Altibase home and scripts, exposes `20300`, `30300`, and `30310`, and runs `/home/altibase/docker-entrypoint.sh` as the entrypoint.

```dockerfile
FROM ubuntu:18.04
MAINTAINER ALTIBASE

RUN sed -e '56 i\root\t\t soft\t nofile\t\t 1048576 \nroot\t\t hard\t nofile\t\t 1048576 \nroot\t\t soft\t nproc\t\t unlimited \nroot\t\t hard\t nproc\t\t unlimited \n' -i /etc/security/limits.conf; \
echo "vm.swappiness = 1" >> /etc/sysctl.conf; \
echo "kernel.sem = 20000 32000 512 5029" >> /etc/sysctl.conf;

WORKDIR /home/altibase
COPY set_altibase.env /home/altibase
COPY docker-entrypoint.sh /home/altibase
COPY ./altibase_home /home/altibase/altibase_home
EXPOSE 20300 30300 30310
ENTRYPOINT ["/bin/bash", "/home/altibase/docker-entrypoint.sh"]
```

Build the image:

```bash
docker build -t altitest:0.0 ./
```

The source `docker-entrypoint.sh` supports `MODE=daemon`, `MODE=isql`, `MODE=shell`, and `MODE=replication`. If `USER_ID` is not set, it defaults to `sys`; if `USER_PASSWD` is not set, it defaults to `manager`. If `$ALTIBASE_HOME/dbs/system001.dbf` is absent, the script creates `mydb` with `DB_SIZE`, `DB_CHARSET`, and `NATIONAL_CHARSET`. `set_replication_port_no` edits `REPLICATION_PORT_NO` in `altibase.properties` using `MASTER_REP_PORT` or `SLAVE_REP_PORT`.

Important `set_altibase.env` values from the source include `ALTIBASE_HOME=/home/altibase/altibase_home`, `ALTIBASE_NLS_USE=MS949`, `ALTIBASE_PORT_NO=20300`, `ALTIBASE_MSG=${HOME}/altimsg`, `ALTIBASE_LINKER_SQLLEN_SIZE=4`, `DB_SIZE=10`, `DB_CHARSET=MS949`, `NATIONAL_CHARSET=UTF8`, `LD_LIBRARY_PATH_64=${LD_LIBRARY_PATH}`, `SHLIB_PATH=${LD_LIBRARY_PATH}`, and `CLASSPATH=.:${ALTIBASE_HOME}/lib/Altibase.jar:${CLASSPATH}`. The source script uses the identifier `MALOC_ARENA_MAX=4` exactly as written.

Create a service container:

```bash
docker run -it -e MODE=shell --name altibase_test altitest:0.0 bash
```

`MODE=daemon` runs Altibase as a daemon and keeps a terminal, `MODE=isql` runs Altibase and keeps an `isql` connection inside the container, `MODE=shell` runs Altibase and keeps a shell inside the container, and `MODE=replication` is used only when creating additional nodes for a replication connection. Do not use `MODE=replication` for the master node.

To preserve data outside the container layer, bind host directories as volumes:

```bash
docker run -it --name altibase_test \
--privileged \
-v ~/work/ALTIBASE_DBS:/home/altibase/altibase_home/dbs \
-v ~/work/ALTIBASE_LOGS:/home/altibase/altibase_home/logs \
altitest:0.0 /bin/bash
```

For replication between containers, first create and inspect a bridge network:

```bash
docker network create --driver bridge isolated_network
docker network ls
docker inspect isolated_network
```

Create the master container on that network:

```bash
docker run -it \
--net=isolated_network \
--hostname=master \
-e MODE=shell \
-e MASTER_REP_PORT=30300 \
--name altitest_master altitest:0.0 /bin/bash
```

Create the additional replication node on the same network:

```bash
docker run -it \
--net=isolated_network \
--hostname=slave \
-e MODE=replication \
-e MASTER_HOST_NAME=master -e MASTER_DB_PORT=20300 -e MASTER_REP_PORT=30300 \
-e SLAVE_HOST_NAME=slave -e SLAVE_REP_PORT=30310 \
--name altitest_slave altitest:0.0 /bin/bash altibase
```

Connect from inside the container with:

```bash
isql -s localhost -u sys -p manager
```

Connect from outside the container by finding the container IP with `docker ps` and `docker inspect`, then using `isql -s`:

```bash
docker ps
docker inspect altibase_test
isql -s 172.17.0.3 -u sys -p manager
```

Stop and remove a service container:

```bash
docker stop altibase_test
docker ps
docker ps -a
docker rm altibase_test
```

## SQL, commands, and configuration

### Important Paths

| Path | Meaning |
| --- | --- |
| `$ALTIBASE_HOME` | Altibase installation home. |
| `$ALTIBASE_HOME/APatch` | Installer patch metadata, rollback backups, and uninstall/rollback executables. |
| `$ALTIBASE_HOME/APatch/patchinfo` | Product signature, patch version, OS, compiler, and Java metadata. |
| `$ALTIBASE_HOME/APatch/pkg_patch_<version>.txt` | Source revision metadata for each installed patch. |
| `$ALTIBASE_HOME/APatch/altibase_base_install.log` | Most recent installation action log. |
| `$ALTIBASE_HOME/APatch/rollback-p<version>` | Patch rollback backup directory. |
| `$ALTIBASE_HOME/bin` | Altibase executable and utility scripts, including `server`, `is`, `il`, `isql`, and `altibase`. |
| `$ALTIBASE_HOME/conf` | `altibase.properties`, `aexport.properties`, samples, and `license`. |
| `$ALTIBASE_HOME/conf/altibase.properties` | Main server configuration file. |
| `$ALTIBASE_HOME/conf/altibase_user.env` | User environment file created by the installer. |
| `$ALTIBASE_HOME/dbs` | Default data file and memory checkpoint image directory. |
| `$ALTIBASE_HOME/logs` | Default log anchor and log file directory. |
| `$ALTIBASE_HOME/arch_logs` | Default archive log directory. |
| `$ALTIBASE_HOME/trc` | Trace log directory. |
| `$ALTIBASE_HOME/trc/altibase_boot.log` | Startup failure trace log used for license and boot errors. |
| `$ALTIBASE_HOME/install/pre_install.sh` | Kernel parameter guidance script. |
| `$ALTIBASE_HOME/install/post_install.sh` | Post-install database creation and environment setup script. |
| `$ALTIBASE_HOME/packages/catproc.sql` | PSM setup script. |
| `$ALTIBASE_HOME/lib/Altibase.jar` | JDBC classpath component in installer-created client/server environments. |

### Important Properties and Environment Variables

| Identifier | Meaning |
| --- | --- |
| `DB_NAME` | Database name fixed at database creation. |
| `PORT_NO` | Altibase service port. |
| `MEM_MAX_DB_SIZE` | Maximum memory database data size; a limit, not pre-allocated memory. |
| `BUFFER_AREA_SIZE` | Pre-allocated disk table buffer area size. |
| `MEM_DB_DIR` | Memory DB checkpoint image directory. |
| `DEFAULT_DISK_DB_DIR` | Default disk tablespace data file directory. |
| `LOGANCHOR_DIR` | Log anchor file directory; three log anchor files are maintained. |
| `LOG_DIR` | Transaction log file directory. |
| `ARCHIVE_DIR` | Archive log file directory. |
| `CHECK_LOGFILE` | Temporary patch workaround property for the `4.3.9.1` to `4.3.9.50` replication patch case; add `CHECK_LOGFILE = 0` only for the documented step and remove it afterward. |
| `ALTIBASE_HOME` | OS environment variable pointing to the Altibase installation home. |
| `ALTIBASE_PORT_NO` | Client environment variable for default service port. |
| `PATH` | Must include `$ALTIBASE_HOME/bin`. |
| `LD_LIBRARY_PATH` | Must include `$ALTIBASE_HOME/lib` on Unix/Linux-style environments. |
| `CLASSPATH` | Must include `$ALTIBASE_HOME/lib/Altibase.jar`. |
| `ALTIBASE_NLS_USE` | Client session character set, such as `MS949`. |
| `DISPLAY` | Controls GUI installer mode; unset it or use `-mode text` if bad display settings cause a hang-like condition. |

### Directory Components After Server Installation

| Directory | Description |
| --- | --- |
| `admin` | Example SQL and view creation files for Altibase performance views. |
| `bin` | Execution files and utilities. |
| `include` | Header files for Altibase application development. |
| `install` | `altibase_env.mk` and README examples for application makefile macro settings. |
| `lib` | Libraries for Altibase application development. |
| `sample` | Sample source programs for CLI, APRE, JDBC, C/C++, and related interfaces. |
| `trc` | Trace log files for Altibase operation status. |
| `conf` | Configuration files, examples, and license file location. |
| `logs` | Default log anchor and log file path. |
| `dbs` | Default data file path. |
| `arch_logs` | Archive log backup directory for recovery. |
| `altiComp` | Utility directory for resolving replication inconsistency after failures. |
| `msg` | Altibase error message files. |

### Platform Settings Summary

| Platform | Setting group | Exact settings preserved from source |
| --- | --- | --- |
| Linux | CPU and memory policy | `CPUfreq Governor=performance`, `RemoveIPC=no`, `vm.swappiness=1`, `vm.force_cgroup_v2_swappiness=1` where supported on RHEL 8, `THP=never`, `transparent_hugepage.defrag=never`, `vm.max_map_count=2147483647`. |
| Linux | IPC | `kernel.shmmni=4096`, `kernel.shmmax=2147483648`, `kernel.sem=2000 32000 512 5029`. |
| Linux | OS user limits | `ulimit -d unlimited`, `ulimit -f unlimited`, `ulimit -n 1048576`, `ulimit -m unlimited`, `ulimit -v unlimited`, `ulimit -u unlimited`. |
| Linux | Character set environment | `MS949 -> ALTIBASE_NLS_USE=MS949, LANG=ko_KR.euckr`; `KO16KSC5601 -> ALTIBASE_NLS_USE=KO16KSC5601, LANG=ko_KR.euckr`; `UTF8 -> ALTIBASE_NLS_USE=UTF8, LANG=ko_KR.utf8`. |
| Solaris | Shared memory | `shmmax=2G+1`, `shmmni=500`, `shmseg=200`; when using memory DB in shared memory, `shmmax` must exceed `STARTUP_SHM_CHUNK_SIZE` and `shmmni` must have headroom for `EXPAND_CHUNK_PAGE_COUNT * 32K` segments. |
| Solaris | Semaphores | `semmns=8192`, `semmni=5029`, `semmsl=2000`, `semmap=5024`, `semmnu=1024`, `semopm=512`, `semume=512`, `semvmx=32767`. |
| Solaris | Environment | `ALTIBASE_HOME`, `PATH=$ALTIBASE_HOME/bin:$PATH`, `ALTIBASE_NLS_USE`, `LD_LIBRARY_PATH`, `LD_LIBRARY_PATH_64`; terminal font should match the DB character set. |
| HPUX | Shared memory and semaphores | `shmmni=500`, `shmseg=200`, `semmns=8192`, `semmni=5029`, `semmnu=1024`, `semume=512`; `semmsl=2000`, `semvmx=32767` are preserved as recommended values. |
| HPUX | File cache and resource limits | `dbc_min_pct=5`, `dbc_max_pct=5~20%`, `filecache_min=5%`, `filecache_max=10%`, `maxdsiz=2147483648`, `maxdsiz_64bit=4396972765184`, `max_thread_proc=600`, `maxfiles=2048`, `nproc=6142`, `maxusers=124` before HPUX 11.23. |
| HPUX | Multi-thread environment | `PTHREAD_FORCE_SCOPE_SYSTEM`, `PERF_ENABLE`, `PTHREAD_FAST_SHARED_OBJECTS`, `PTHREAD_DISABLE_HANDOFF`, `_M_ARENA_OPTS`, and `PTHREAD_SHARED_MUTEX_OLDSPIN=1` when `PHCO_33675` or `PHCO_34718` exists on HPUX 11.23. |
| AIX | AIO and file cache | Posix AIO `Available`; `minperm%=10`, `lru_file_repage=0`, `strict_maxclient=0`. |
| AIX | Resource and thread environment | `Maximum number of PROCESSES allowed per user` higher than concurrent process needs; `AIXTHREAD_MNRATIO=1:1`, `AIXTHREAD_SCOPE=S`, `PTHREAD_FORCE_SCOPE_SYSTEM`, `AIXTHREAD_MUTEX_DEBUG=OFF`, `AIXTHREAD_RWLOCK_DEBUG=OFF`, `AIXTHREAD_COND_DEBUG=OFF`, `SPINLOOPTIME=1000`, `YIELDLOOPTIME=50`, `MALLOCMULTIHEAP=1`. |
| Docker | Build/container settings | Dockerfile `kernel.sem = 20000 32000 512 5029`, exposed ports `20300 30300 30310`, entrypoint `/home/altibase/docker-entrypoint.sh`, modes `daemon`, `isql`, `shell`, `replication`, and image tag example `altitest:0.0`. |

### Docker Environment and Modes

| Identifier | Meaning |
| --- | --- |
| `MODE=daemon` | Run Altibase as a daemon and keep the terminal. |
| `MODE=isql` | Start Altibase and keep an `isql` session inside the container. |
| `MODE=shell` | Start Altibase and keep a shell inside the container. |
| `MODE=replication` | Create an additional replication node; do not use for the master node. |
| `USER_ID` / `USER_PASSWD` | Defaults to `sys` / `manager` when not supplied. |
| `FILE` | Optional script executed by `is` or `isql` during container startup. |
| `MASTER_REP_PORT` / `SLAVE_REP_PORT` | Values used by `set_replication_port_no` to rewrite `REPLICATION_PORT_NO`. |
| `MASTER_HOST_NAME`, `MASTER_DB_PORT`, `SLAVE_HOST_NAME` | Replication container topology variables. |
| `DB_SIZE`, `DB_CHARSET`, `NATIONAL_CHARSET` | Inputs to `CREATE DATABASE mydb INITSIZE=${DB_SIZE}M NOARCHIVELOG CHARACTER SET ${DB_CHARSET} NATIONAL CHARACTER SET ${NATIONAL_CHARSET}`. |
| `MALOC_ARENA_MAX` | Source Docker environment identifier preserved exactly as written. |

## Validation and troubleshooting

### Installation and Startup Troubleshooting

The troubleshooting source applies to Altibase version 6.5 or later. For unlisted problems, send occurrence conditions and trace logs from the `trc` directory under the Altibase installation path to `support@altibase.com`.

| Problem | Symptom or evidence | Cause | Resolution |
| --- | --- | --- | --- |
| Unable to interpret binary | `cannot execute binary file` when running a package such as `altibase-HDB-server-6.5.1.6.8-LINUX-POWERPC-64bit-release.run` | Package CPU does not match the target device CPU, or other binary/library compatibility issue. | Reinstall with the package matching the target CPU. Use `altibase -v` to check an installed executable. |
| Environment variable not registered | `[ERR-91003 : Environment (ALTIBASE_HOME) does not exists.` | `ALTIBASE_HOME` is not set. | Register the Altibase installation path in `ALTIBASE_HOME`. |
| User file privilege problem | `[ERR-9100B : Privilege error for sysdba user account.]` | `sysdba` access is being attempted by a user other than the Altibase installation owner. | Retry as the installation owner or change ownership of all files under the installation path to the current user. |
| Missing `altibase.properties` | `idp readConf() Error : Open File [/hdb_home/651/conf/altibase.properties] Error.` | The configuration file is missing from `$ALTIBASE_HOME/conf`. | Create or update `altibase.properties` from `altibase.properties.sample`. |
| Missing license file | `Commencing Server as Community Edition`, `DISK_MAX_DB_SIZE(Unlimited) exceeded limit 8192M`, `[FAILURE] License invalid or expired.`, `ERR-91015` | No license file exists under `$ALTIBASE_HOME/conf`. | Create `$ALTIBASE_HOME/conf/license` from the issued Altibase license. |
| Invalid license | `Invalid or expired license in License File(/hdb_home/651/conf/license)` and `ERR-91015` | Host ID or MAC address differs from the information used for license issuance. | Reissue the license for the target device information. |
| Expired license | Same invalid or expired license startup failure. | License has expired. | Apply for and issue a new license from the support portal. |
| Property value out of range | `idp checkRange() Error : Property [property_name] [current_value] Overflowed the Value Range.(min_value~max_value)` | Property value exceeds allowed range. | Correct the property to a valid value. |
| Property conversion failure | `idp convertFromString() Error : The property [property_name] value [current_value] is not convertable.` | Property value cannot be converted to the expected data type. | Correct the property data type and value. |
| Duplicate property | `idp insertBySrc() Error : Property [property_name] Can't Store Multiple Values.` | Same property appears more than once when only one value is allowed. | Remove or consolidate duplicate property entries. |
| Writing file error | `ERR-0103C : Unable to invoke create() function on [/ALTIBASE/altibase_home/dbs/dwfile0.dwf]` during `createdb` | Disk free space is insufficient or directory privileges are missing. | Check disk free space and directory privileges. |
| Database creation skipped | `[FAILURE] The log anchor file does not exist or it is not valid.` and `ERR-91015` | Database was not created before service startup. | Perform the database creation procedure. |
| Listener port bind failure | `[CM] Listener failed : TCP on port 20300 [IPV4]`, `[FAILURE] Unable to bind the socket.`, `ERR-91015` | Altibase cannot bind the service TCP port, commonly because another application owns it. | Find the port owner and either change that application or change the Altibase `PORT_NO`. |
| Replication port bind failure | `[RP] Initialization : FAIL`, `[Receiver] Failed to listen to a replication socket (Port No:30300)`, `ERR-91015` | Altibase cannot bind the replication port. | Find the port owner and either change that application or change the Altibase replication port. |

### Startup Validation Commands

Use these commands after patching or startup:

```bash
ps -ef | grep 'altibase -p' | grep -v grep
netstat -an | grep 20300
altibase -v
```

After shutdown, `ps -ef | grep 'altibase -p' | grep -v grep` and `netstat -an | grep 20300` should return no result. After startup, they should show the Altibase process and a `LISTEN` entry on the service port.

### Platform Setup Troubleshooting

| Platform | Symptom or condition | Source-backed action |
| --- | --- | --- |
| Linux | `Failed to mmap log file ( errno=ENOMEM(12), Not enough memory` in `altibase_boot.log`, or application error `Memory [iduMemMgr :: malloc] failed.` | Check `vm.max_map_count`; for terabyte-scale memory tables, set `vm.max_map_count=2147483647`. |
| Linux | `Failed to create a thread object.` or `resource temporarily unavailable` | Check `ulimit -u` and hard-limit settings; raise max user processes to `unlimited` where possible. |
| Linux | `Too many open files` | Check `ulimit -n`, process limits, and `/etc/security/limits.conf`; set open files to `1048576` where the source recommends it. |
| Linux | Swap sizing is being planned for very large RHEL systems | The source notes that the old two-times-memory swap rule is not practical for terabyte-scale memory, and that systems with more than 140 logical processors or more than 3 TB RAM should use at least 100 GB swap. |
| Linux | RHEL 7 or later `systemd` service terminates Altibase during OS boot while recovery is still loading the database | Set `TimeoutStartSec` or `TimeoutSec` high enough for the operating environment, or set it to `0` to disable timeout; review `TimeoutStopSec` similarly. |
| Linux | SYS-area CPU usage increases on Red Hat Enterprise Linux 7 with Symantec Endpoint Protection for Linux | The source records a June 2020 case where CPU increased with more Altibase sessions because of `select()` and `write()` system calls; Broadcom had not identified the cause, and the antivirus program was changed as the resolution. |
| Solaris | Memory DB is loaded into shared memory and startup or expansion needs more segments | Ensure `shmmax > STARTUP_SHM_CHUNK_SIZE` and give `shmmni` enough headroom for segments of size `EXPAND_CHUNK_PAGE_COUNT * 32K`. |
| HPUX | Multi-thread performance degrades after `PHCO_33675` or `PHCO_34718` on HPUX 11.23 | Set `PTHREAD_SHARED_MUTEX_OLDSPIN=1` and review the HP patch level. |
| AIX | `instfix -i \| grep IV28577` returns no output | Ask an AIX engineer to patch or upgrade to an AIX native compiler where AIX bug `IV28577` is resolved. |
| AIX | IPC channel count must be estimated | Because AIX fixes `semume=1024`, versions earlier than Altibase `5.1.5.72` can use up to `512` IPC channels, and Altibase `5.1.5.72` or later can use up to `341` IPC channels. |
| Docker | Container data disappears after deleting a container | Use bind-mounted volumes such as `-v ~/work/ALTIBASE_DBS:/home/altibase/altibase_home/dbs` and `-v ~/work/ALTIBASE_LOGS:/home/altibase/altibase_home/logs`; container-layer changes are deleted with the container. |
| Docker | External clients cannot connect because the target IP is unknown | Run `docker ps` and `docker inspect <container>` and use the container `IPAddress` with `isql -s`. |

## Version-specific notes

### Package Installer Support Table

The installation guide lists package installer support as follows:

| OS | CPU | Version | Server bit | Client bit |
| --- | --- | --- | --- | --- |
| AIX | PowerPC | 6.1 tl03 or later | 64-bit | 64-bit, 32-bit |
| HP-UX | IA64 | 11.31 or later | 64-bit | 64-bit, 32-bit |
| SUN | SPARC | 2.8 or later | 64-bit | 64-bit, 32-bit |
| Linux | x86, x86-64 with GNU glibc 2.12 or later | Red Hat 6.0 or later | 64-bit | 64-bit, 32-bit |
| Windows | x86, x86-64 | Windows 2008, Windows 2012, Windows 7, Windows 8 | 64-bit | 64-bit, 32-bit |

SUN and Windows packages are not supported from Altibase 7.1 or later.

### FAQ Platform Support for 6.5.1

| OS | CPU | Version | Server bit | Client bit |
| --- | --- | --- | --- | --- |
| AIX | PowerPC | 6.1 tl03 or later | 64-bit | 64-bit, 32-bit |
| HP-UX | IA64 | 11.31 or later | 64-bit | 64-bit, 32-bit |
| Linux | x86, x86-64 with GNU glibc 2.12 or later | Ubuntu 12, 13; Redhat 6, 7; CentOS 6, 7; Fedora 7 through 21; openSUSE 12; Oracle Linux 6.5, 6.6, 7.1 | 64-bit | 64-bit, 32-bit |
| SUN | SPARC | 2.10 or later | 64-bit | 64-bit, 32-bit |
| Windows | x86, x86-64 | Windows 2008, Windows 2012, Windows 7, Windows 8 | 64-bit | 64-bit, 32-bit |

### FAQ Platform Support for 6.3.1

| OS | CPU | Version | Server bit | Client bit |
| --- | --- | --- | --- | --- |
| AIX | PowerPC | 5.3 tl1 or later | 64-bit | 64-bit, 32-bit |
| HP-UX | PA-RISC | 11.11 or later | 64-bit | 64-bit, 32-bit |
| HP-UX | IA64 | 11.23 or later | Not specified in source row | Not specified in source row |
| Linux | x86, x86-64 with GNU glibc 2.3.4 or later | Ubuntu 8 through 13; Redhat 4 through 7; CentOS 4 through 7; Fedora 7 through 21; openSUSE 9 through 12; Oracle Linux 6.5, 6.6, 7.1 | 64-bit | 64-bit, 32-bit |
| SUN | SPARC | 2.8 or later | 64-bit | 64-bit, 32-bit |
| SUN | i86PC | 2.10 or later | Not specified in source row | Not specified in source row |
| Windows | x86, x86-64 | Windows 2008, Windows 2012, Windows 7, Windows 8 | 64-bit | 64-bit, 32-bit |

### FAQ Platform Support for 6.1.1

| OS | CPU | Version | Server bit | Client bit |
| --- | --- | --- | --- | --- |
| AIX | PowerPC | 5.3 tl1 or later | 64-bit | 64-bit, 32-bit |
| HP-UX | PA-RISC | 11.00 or later | 64-bit | 64-bit, 32-bit |
| HP-UX | IA64 | 11.23 or later | Not specified in source row | Not specified in source row |
| Linux | x86, x86-64 with GNU glibc 2.3.4 or later | Ubuntu 8 through 13; Redhat 4 through 7; CentOS 4 through 7; Fedora 7 through 21; openSUSE 9 through 12; Oracle Linux 6.5, 6.6, 7.1 | 64-bit | 64-bit, 32-bit |
| SUN | SPARC | 2.8 or later | 64-bit | 64-bit, 32-bit |
| SUN | i86PC | 2.10 or later | Not specified in source row | Not specified in source row |
| Windows | x86, x86-64 | Windows 2003, Windows 2008, Windows 2012, Windows 7, Windows 8 | 64-bit | 64-bit, 32-bit |

Altibase HDB 6 and later JDBC versions are compatible with JDK 1.4 and later.

### Patch Version Boundaries

For patch installation, use the 5.5.1 boundary:

- ALTIBASE HDB 5.5.1 or later uses the Java-based `.run` installer.
- Versions earlier than 5.5.1, such as 4.3.9 and 5.3.3, use compressed patch files such as `.tgz`.

The special replication patch procedure applies only when both conditions are true:

- Patching from ALTIBASE HDB `4.3.9.1` through `4.3.9.50` to `4.3.9.51` or later.
- The database is in a replication environment.

### Linux glibc Compatibility from Linux Setup Guide

The Linux setup guide checks compatibility by glibc version rather than distribution name or kernel version.

| Altibase version | OS family or CPU condition | glibc range | Note |
| --- | --- | --- | --- |
| Altibase v7.3.0 | Oracle Linux 8 / Red Hat Enterprise Linux 8 / CentOS 8 / Rocky Linux 8 | `2.12 ~ 2.33` |  |
| Altibase v7.3.0 | Oracle Linux 7 / Red Hat Enterprise Linux 7 / CentOS 7 | `2.12 ~ 2.33` |  |
| Altibase v7.3.0 | Oracle Linux 6 / Red Hat Enterprise Linux 6 / CentOS 6 | `2.12 ~ 2.33` |  |
| Altibase v7.3.0 | Ubuntu 18 | `2.27 ~ 2.33` |  |
| Altibase v7.3.0 | Ubuntu 16 | `2.23 ~ 2.33` |  |
| Altibase v7.3.0 | Ubuntu 12 | `2.17 ~ 2.33` |  |
| Altibase v7.3.0 | POWER7 with Red Hat Enterprise Linux 6.5 | `2.12 ~ 2.33` |  |
| Altibase v7.3.0 | POWER8(LE) with Red Hat Enterprise Linux 7.2 | `2.17 ~ 2.33` |  |
| Altibase v7.1.0 | Oracle Linux 8 / Red Hat Enterprise Linux 8 / CentOS 8 / Rocky Linux 8 | `2.12 ~ 2.33` |  |
| Altibase v7.1.0 | Oracle Linux 7 / Red Hat Enterprise Linux 7 / CentOS 7 | `2.12 ~ 2.33` |  |
| Altibase v7.1.0 | Oracle Linux 6 / Red Hat Enterprise Linux 6 / CentOS 6 | `2.12 ~ 2.33` |  |
| Altibase v7.1.0 | Ubuntu 18 | `2.27 ~ 2.33` | Altibase `7.1.0.7.2` or higher |
| Altibase v7.1.0 | Ubuntu 16 | `2.23 ~ 2.33` | Altibase `7.1.0.7.2` or higher |
| Altibase v7.1.0 | Ubuntu 12 | `2.17 ~ 2.33` |  |
| Altibase v7.1.0 | POWER7 with Red Hat Enterprise Linux 6.5 | `2.12 ~ 2.33` |  |
| Altibase v7.1.0 | POWER8(LE) with Red Hat Enterprise Linux 7.2 | `2.17 ~ 2.33` | Altibase `7.1.0.0.8` or higher |
| Altibase v6.5.1 | Oracle Linux 8 / Red Hat Enterprise Linux 8 / CentOS 8 / Rocky Linux 8 | `2.12 ~ 2.33` |  |
| Altibase v6.5.1 | Oracle Linux 7 / Red Hat Enterprise Linux 7 / CentOS 7 | `2.12 ~ 2.33` |  |
| Altibase v6.5.1 | Oracle Linux 6 / Red Hat Enterprise Linux 6 / CentOS 6 | `2.12 ~ 2.33` |  |
| Altibase v6.5.1 | Ubuntu 12 | `2.17 ~ 2.33` |  |
| Altibase v6.5.1 | POWER8 with Red Hat Enterprise Linux 7.1 | `2.12 ~ 2.33` |  |
| Altibase v6.5.1 | POWER7 with Red Hat Enterprise Linux 6.5 | `2.12 ~ 2.33` |  |
| Altibase v6.5.1 | POWER8(LE) with Red Hat Enterprise Linux 7.6 | `2.17 ~ 2.33` | Altibase `6.5.1.4.5` or higher |
| Altibase v6.5.1 | POWER8(LE) with Red Hat Enterprise Linux 7.2 | `2.17 ~ 2.33` | Altibase `6.5.1.4.5` or higher |
| Altibase v6.3.1 | Source row has no OS version | `2.3.4 ~ 2.20` |  |
| Altibase v6.1.1 | Source row has no OS version | `2.3.4 ~ 2.20` |  |
| Altibase v5.5.1 | Source row has no OS version | `2.3.4 ~ 2.20` |  |

### Platform Setup Version Boundaries

| Platform | Version-specific condition |
| --- | --- |
| Linux | R005 Linux setup is based on Altibase 5.5.1 or later and Red Hat Enterprise Linux 6 or later. `RemoveIPC` applies to Red Hat Enterprise Linux 7.2 and later. RHEL 8 requires additional `vm.force_cgroup_v2_swappiness` or cgroup `memory.swappiness` checks. RHEL 6 examples use `/etc/rc.local`; RHEL 7 or later examples use `udev`, `tuned`, and GRUB2 paths. |
| Solaris | R005 Solaris setup is based on Altibase 6 or later and Sun OS 5.8 through 5.10. Solaris 5.10 or below can use `/etc/system`; Solaris 5.10 or later can use `projadd` and `projmod`. |
| HPUX | `maxusers` is needed only earlier than HPUX 11.23; HPUX 11.31 renames `dbc_min_pct` and `dbc_max_pct` to `filecache_min` and `filecache_max`. `PERF_ENABLE` is needed for HPUX 11.23 only because HPUX 11.31 includes the behavior in `PTHREAD_FORCE_SCOPE_SYSTEM`. |
| AIX | R005 AIX setup is based on AIX 5.x and excludes AIX 4.3 or earlier. Posix AIO is already `Available` by default starting in AIX 6.1. File-cache settings do not apply to AIX 5.2 ML03 or earlier and do not require special changes on AIX 6.1 or later. |
| Docker | R005 Docker setup is based on Altibase 7.1.1 or later, Docker 19.03.2 or later, and Docker kernel requirement 3.10.X or later. |

## Related errors

| Error or message | Context | Action |
| --- | --- | --- |
| `ERR-910FB : Connected to idle instance` | Expected while connecting to an idle instance during database creation or startup. | Continue startup or database creation. |
| `ERR-91015 : Communication failure.` | Common wrapper error for startup failures such as missing database files, license failure, listener bind failure, or replication port bind failure. | Read the preceding failure message and check `$ALTIBASE_HOME/trc/altibase_boot.log` when startup fails. |
| `ERR-91003 : Environment (ALTIBASE_HOME) does not exists.` | `ALTIBASE_HOME` is not registered for `sysdba` connection. | Set `ALTIBASE_HOME` to the installation path and apply the shell profile. |
| `ERR-9100B : Privilege error for sysdba user account.` | `sysdba` connection attempted by the wrong OS user. | Use the installation owner or correct ownership under the installation path. |
| `ERR-0103C : Unable to invoke create() function on [/ALTIBASE/altibase_home/dbs/dwfile0.dwf]` | Database creation cannot write a file. | Check disk free space and directory privileges. |
| `idp checkRange() Error` | Property value out of range. | Correct the property value to the allowed range. |
| `idp convertFromString() Error` | Property value cannot be converted. | Correct the value format or data type. |
| `idp insertBySrc() Error` | Duplicate single-valued property. | Remove duplicate property entries. |
| `No valid license present!` | Startup failure recorded in `altibase_boot.log`. | Install or reissue the license file. |
| `Failed to mmap log file ( errno=ENOMEM(12), Not enough memory` | Linux `max_map_count` can block memory allocation for very large memory tables. | Set `vm.max_map_count=2147483647` and restart as needed. |
| `Memory [iduMemMgr :: malloc] failed.` | Application-visible memory allocation failure tied to Linux memory-map or memory availability constraints. | Check `max_map_count`, memory, and Linux resource settings. |
| `Failed to create a thread object.` | OS user process/thread limit is insufficient. | Raise `ulimit -u` and hard-limit settings. |
| `resource temporarily unavailable` | OS user process/thread limit is insufficient. | Raise `ulimit -u` and hard-limit settings. |
| `Too many open files` | OS user open-file limit is insufficient. | Raise `ulimit -n` and hard-limit settings. |
| `altibase.service start operation timed out. Terminating.` | Linux `systemd` timed out Altibase startup while recovery was still running. | Increase `TimeoutStartSec` or `TimeoutSec`, or set timeout to `0`. |

## Attachments and external references

Preserved PDF attachments from Korean source pages:

- `ALTIBASE_버전별_DB_생성_가이드.pdf`: `https://docs.altibase.com/download/attachments/13436812/ALTIBASE_%EB%B2%84%EC%A0%84%EB%B3%84_DB_%EC%83%9D%EC%84%B1_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=2&modificationDate=1758150003000&api=v2`
- `ALTIBASE_Quick_Install_Start_for_UNIX.pdf`: `https://docs.altibase.com/download/attachments/13436834/ALTIBASE_Quick_Install_Start_for_UNIX.pdf?version=1&modificationDate=1697762511000&api=v2`
- `ALTIBASE_설치_시_발생할_수_있는_문제상황과_조치.pdf`: `https://docs.altibase.com/download/attachments/13437056/ALTIBASE_%EC%84%A4%EC%B9%98_%EC%8B%9C_%EB%B0%9C%EC%83%9D%ED%95%A0_%EC%88%98_%EC%9E%88%EB%8A%94_%EB%AC%B8%EC%A0%9C%EC%83%81%ED%99%A9%EA%B3%BC_%EC%A1%B0%EC%B9%98.pdf?version=1&modificationDate=1697764061000&api=v2`
- `Altibase_운영을_위한_Linux_설정_가이드_2019.pdf`: `https://docs.altibase.com/download/attachments/13436485/Altibase_%EC%9A%B4%EC%98%81%EC%9D%84_%EC%9C%84%ED%95%9C_Linux_%EC%84%A4%EC%A0%95_%EA%B0%80%EC%9D%B4%EB%93%9C_2019.pdf?version=1&modificationDate=1584944731000&api=v2`
- `ALTIBASE_운영을_위한_Linux_설정_가이드.pdf`: `https://docs.altibase.com/download/attachments/13436485/ALTIBASE_%EC%9A%B4%EC%98%81%EC%9D%84_%EC%9C%84%ED%95%9C_Linux_%EC%84%A4%EC%A0%95_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1698366100000&api=v2`

External references and contact points preserved from R004 sources:

- Altibase support portal: `http://support.altibase.com`
- Altibase English support portal: `http://support.altibase.com/en/`
- Product download page: `http://support.altibase.com/en/product`
- Technical support email for unlisted installation problems: `support@altibase.com`
- Sales contact for license purchase: `sales@altibase.com`
- Technical support center phone number in the source: `02-2082-1114`
- Client installation support phone number in the FAQ source: `+82-2-2082-1114`
- Database creation guide source URL: `https://docs.altibase.com/display/arch/Creating+ALTIBASE+Database`
- Start and shutdown process source URL: `https://docs.altibase.com/pages/viewpage.action?pageId=13434993`
- Linux setup guide source URL: `https://docs.altibase.com/display/arch/Linux+Setup+Guide+for+Altibase`
- Solaris setup guide source URL: `https://docs.altibase.com/display/arch/Solaris+Setup+Guide+for+Altibase`
- HPUX setup guide source URL: `https://docs.altibase.com/display/arch/HPUX+Setup+Guide+for+Altibase`
- AIX setup guide source URL: `https://docs.altibase.com/display/arch/AIX+Setup+Guide+for+Altibase`
- Docker guide source URL: `https://docs.altibase.com/display/arch/Altibase+Docker+Guide`
- Docker container overview reference: `https://www.docker.com/resources/what-container`
- Docker image/container layers reference: `https://docs.docker.com/v17.09/engine/userguide/storagedriver/imagesandcontainers/#container-and-layers`
- Docker installation page: `https://docs.docker.com/install/`
- Docker Hub Altibase image: `https://hub.docker.com/r/altibase/altibase`
- Docker build reference: `https://docs.docker.com/engine/reference/commandline/build/`
- Docker run reference: `https://docs.docker.com/engine/reference/run/`
- Docker documentation: `https://docs.docker.com/`
- Altibase Docker configuration reference in source: `http://support.altibase.com/fileDownload.do?gubun=wp&no=20`
- Altibase 7.1 English Replication Manual reference in source: `https://github.com/ALTIBASE/Documents/blob/master/Manuals/Altibase_7.1/eng/Replication%20Manual.md`
- Altibase 7.1 English manual root reference in source: `https://github.com/ALTIBASE/Documents/blob/master/Manuals/Altibase_7.1/eng/README.md`
- IBM AIX `IV28577` reference: `http://www-01.ibm.com/support/docview.wss?uid=swg1IV28577`

Embedded PNG installer, Windows registry, and Docker JPG screenshots remain in the source Markdown files as non-document-format image references. Do not infer additional procedural content from those images beyond the text preserved here.

## Terminology

Preserve these exact terms and identifiers:

- Product names: `Altibase`, `ALTIBASE HDB`, `Altibase Package Installer`, `iSQL`, `APatch`.
- Commands and utilities: `chmod`, `uname -a`, `server create`, `server start`, `server stop`, `isql`, `is`, `il`, `altibase -v`, `aexport`, `netstat -an`, `ps -ef`, `gzip -cd`, `tar xvf`, `regedit.exe`, `rpm -q glibc`, `cpupower`, `tuned-adm`, `udevadm`, `sysctl`, `ipcs`, `ulimit`, `projadd`, `projmod`, `kctune`, `swlist`, `smit`, `vmo`, `lsdev`, `instfix`, `docker pull`, `docker images`, `docker build`, `docker run`, `docker network create`, `docker network ls`, `docker inspect`, `docker stop`, `docker ps`, `docker rm`.
- SQL and views: `startup process`, `startup control`, `startup service`, `create database`, `alter database archivelog`, `drop database`, `shutdown abort`, `shutdown immediate`, `shutdown normal`, `CREATE USER`, `DROP USER`, `CREATE MEMORY TABLESPACE`, `CREATE DISK TABLESPACE`, `DROP TABLESPACE`, `ALTER SYSTEM CHECKPOINT`, `DROP REPLICATION`, `V$VERSION`, `V$TABLESPACES`, `V$MEM_TABLESPACE_CHECKPOINT_PATHS`, `V$DATAFILES`, `V$NLS_PARAMETERS`, `V$REPGAP`, `SYSTEM_.SYS_REPLICATIONS_`, `V$LFG`.
- Properties and environment variables: `DB_NAME`, `PORT_NO`, `MEM_MAX_DB_SIZE`, `BUFFER_AREA_SIZE`, `MEM_DB_DIR`, `DEFAULT_DISK_DB_DIR`, `LOGANCHOR_DIR`, `LOG_DIR`, `ARCHIVE_DIR`, `CHECK_LOGFILE`, `STARTUP_SHM_CHUNK_SIZE`, `EXPAND_CHUNK_PAGE_COUNT`, `REPLICATION_PORT_NO`, `ALTIBASE_HOME`, `ALTIBASE_PORT_NO`, `PATH`, `LD_LIBRARY_PATH`, `LD_LIBRARY_PATH_64`, `SHLIB_PATH`, `CLASSPATH`, `ALTIBASE_NLS_USE`, `LANG`, `DISPLAY`, `MALOC_ARENA_MAX`, `MALLOC_ARENA_MAX`, `PTHREAD_FORCE_SCOPE_SYSTEM`, `PERF_ENABLE`, `PTHREAD_FAST_SHARED_OBJECTS`, `PTHREAD_DISABLE_HANDOFF`, `_M_ARENA_OPTS`, `PTHREAD_SHARED_MUTEX_OLDSPIN`, `AIXTHREAD_MNRATIO`, `AIXTHREAD_SCOPE`, `AIXTHREAD_MUTEX_DEBUG`, `AIXTHREAD_RWLOCK_DEBUG`, `AIXTHREAD_COND_DEBUG`, `SPINLOOPTIME`, `YIELDLOOPTIME`, `MALLOCMULTIHEAP`, `AIXTHREAD_MUTEX_FAST`, `MODE`, `USER_ID`, `USER_PASSWD`, `FILE`, `MASTER_REP_PORT`, `SLAVE_REP_PORT`, `MASTER_HOST_NAME`, `MASTER_DB_PORT`, `SLAVE_HOST_NAME`, `DB_SIZE`, `DB_CHARSET`, `NATIONAL_CHARSET`.
- Kernel parameters and OS settings: `CPUfreq Governor`, `RemoveIPC`, `vm.swappiness`, `vm.force_cgroup_v2_swappiness`, `memory.swappiness`, `transparent_hugepage`, `transparent_hugepage.defrag`, `vm.max_map_count`, `kernel.shmmni`, `kernel.shmmax`, `kernel.sem`, `shmmax`, `shmmni`, `shmseg`, `semmsl`, `semmns`, `semopm`, `semmni`, `semmap`, `semmnu`, `semume`, `semvmx`, `dbc_min_pct`, `dbc_max_pct`, `filecache_min`, `filecache_max`, `maxdsiz`, `maxdsiz_64bit`, `max_thread_proc`, `maxfiles`, `nproc`, `maxusers`, `minperm`, `lru_file_repage`, `strict_maxclient`.
- Paths: `$ALTIBASE_HOME`, `$ALTIBASE_HOME/APatch`, `$ALTIBASE_HOME/conf/altibase.properties`, `$ALTIBASE_HOME/conf/altibase_user.env`, `$ALTIBASE_HOME/conf/license`, `$ALTIBASE_HOME/install/pre_install.sh`, `$ALTIBASE_HOME/install/post_install.sh`, `$ALTIBASE_HOME/packages/catproc.sql`, `$ALTIBASE_HOME/trc/altibase_boot.log`, `$ALTIBASE_HOME/dbs`, `$ALTIBASE_HOME/logs`, `$ALTIBASE_HOME/arch_logs`, `/etc/systemd/logind.conf`, `/etc/sysctl.conf`, `/etc/sysctl.d/99-sysctl.conf`, `/etc/security/limits.conf`, `/etc/system`, `/etc/default/grub`, `/etc/grub.conf`, `/etc/rc.d/rc.local`, `/etc/udev/rules.d/99-cpufreq.rules`, `/home/altibase/docker-entrypoint.sh`, `/home/altibase/set_altibase.env`, `/home/altibase/altibase_home`.
- Error codes and messages: `ERR-910FB`, `ERR-91015`, `ERR-91003`, `ERR-9100B`, `ERR-0103C`, `No valid license present!`, `idp checkRange() Error`, `idp convertFromString() Error`, `idp insertBySrc() Error`, `Failed to mmap log file`, `Memory [iduMemMgr :: malloc] failed.`, `Failed to create a thread object.`, `resource temporarily unavailable`, `Too many open files`, `altibase.service start operation timed out. Terminating.`
