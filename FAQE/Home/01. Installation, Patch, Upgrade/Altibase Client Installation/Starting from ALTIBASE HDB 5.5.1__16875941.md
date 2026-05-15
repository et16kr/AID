---
title: "Starting from ALTIBASE HDB 5.5.1"
page_id: "16875941"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Starting+from+ALTIBASE+HDB+5.5.1"
updated_at: "2021-04-02T10:43:41.000+0900"
version: 2
ancestors: ["Home", "01. Installation, Patch, Upgrade", "Altibase Client Installation"]
labels: []
---

# Starting from ALTIBASE HDB 5.5.1
Source: https://docs.altibase.com/display/FAQE/Starting+from+ALTIBASE+HDB+5.5.1
Updated: 2021-04-02T10:43:41.000+0900

- [OS](#StartingfromALTIBASEHDB5.5.1-OS) - [Download Altibase Client Installation File](#StartingfromALTIBASEHDB5.5.1-DownloadAltibaseClientInstallationFile) - [Upload Altibase Client Installation File](#StartingfromALTIBASEHDB5.5.1-UploadAltibaseClientInstallationFile) - [Change Altibase installation file execution permission](#StartingfromALTIBASEHDB5.5.1-ChangeAltibaseinstallationfileexecutionpermission) - [Start Installation](#StartingfromALTIBASEHDB5.5.1-StartInstallation) - [Check OS user initialization file](#StartingfromALTIBASEHDB5.5.1-CheckOSuserinitializationfile) - [Apply OS user initialization file](#StartingfromALTIBASEHDB5.5.1-ApplyOSuserinitializationfile) - [Installation verification](#StartingfromALTIBASEHDB5.5.1-Installationverification)

# OS

---

- Linux
- HP-UX
- AIX
- Solaris

# Download Altibase Client Installation File

---

- Download the client installation file from [http://support.altibase.com/en/product](http://support.altibase.com/en/product)
- If you do not have the version of the client you want to install, please request it through the Customer Service -> Request Technical Support menu at +82-2-2082-1114 or [http://support.altibase.com/en/](http://support.altibase.com/en/).

# Upload Altibase Client Installation File

---

- Upload the installation file to the server where you want to install the Altibase client.
- Log in as the OS user that will own the installation and upload the installation package to any path.

# Change Altibase installation file execution permission

---

- Altibase client installation files have only read and write permissions as default permissions.
- Execute permission is required to proceed with the installation.
- Add the execution permission as follows.

  **How to change execution permission**

  ```
  $ chmod +x altibase-HDB-client-6.3.1.3.1-LINUX-X86-64bit-release.run
  ```
- After changing the permission, check that the rwxrwx-rx execution permission has been added as shown below.

  **How to change execution permission**

  ```
  $ ls -l altibase-HDB-client-6.3.1.3.1-LINUX-X86-64bit-release.run
  -rwxrwxr-x 1 heejung.lee heejung.lee 20535639 2014-11-28 15:49 altibase-HDB-client-6.3.1.3.1-LINUX-X86-64bit-release.run
  ```

# Start Installation

---

- Execute the installation file as shown below.

  **How to execute installation file**

  ```
  $ ./altibase-HDB-client-6.3.1.3.1-LINUX-X86-64bit-release.run
  ```
- Example of the installation process

  ```
  $ ./altibase-HDB-client-6.3.1.3.1-LINUX-X86-64bit-release.run
  ----------------------------------------------------------------------------
  Welcome to the ALTIBASE HDB Client 6.3.1.3.1 setup wizard.

  ----------------------------------------------------------------------------
  Installation Directory

  Please specify the installation directory for ALTIBASE HDB Client 6.3.1.3.1

  Installation directory [/data/heejung.lee/altibase_home]:    # Enter the directory to install as an absolute path.

  Please select the installation type.

  Installation type

  [1] Patch: patch package install
  [2] Full installation: full package install
  Please choose an option [1] :                                 # Enter 2, then press Enter.

  ----------------------------------------------------------------------------
  ALTIBASE HDB Property setting

  ALTIBASE HDB connection port number (1024-65535)  [20300]:    # Enter the service port of the Altibase server. If using the default, press Enter.

  ----------------------------------------------------------------------------
  Setup is now ready to install ALTIBASE HDB Client 6.3.1.3.1.

  Do you want to continue? [Y/n]:                               # Press Enter to start the installation.

  ----------------------------------------------------------------------------
  Please wait until the setup wizard finishes installing ALTIBASE HDB Client
  6.3.1.3.1.

   Installing
   0% ______________ 50% ______________ 100%
   ########################################Info:
  The following ALTIBASE HDB environment variables were added.

  -- ALTIBASE_HOME=/data/heejung.lee/altibase_home
  -- ALTIBASE_PORT_NO=20300
  -- PATH
  -- LD_LIBRARY_PATH
  -- CLASSPATH

  =========================
  Please perform [re-login]
  or [source .bash_profile]
  or [. .bash_profile]
  ==========================
  Press [Enter] to continue :
  #
  ----------------------------------------------------------------------------
  Setup has finished installing the ALTIBASE HDB Client 6.3.1.3.1 on your client.
  $                                                              # Installation ended.
  ```
- When installation completes normally, the following directories are created under the installation directory.

  **Altibase client directory structure**

  ```
  $ ls -l
  total 132
  drwxr-xr-x 2 heejung.lee heejung.lee  4096 2015-03-09 10:22 APatch
  -rwxr-xr-x 1 heejung.lee heejung.lee   230 2015-03-09 10:22 Uninstall ALTIBASE HDB Client 6.3.1.3.1.desktop
  drwxr-xr-x 2 heejung.lee heejung.lee  4096 2015-03-09 10:22 admin
  drwxr-xr-x 2 heejung.lee heejung.lee  4096 2015-03-09 10:22 audit
  drwxr-xr-x 2 heejung.lee heejung.lee  4096 2015-03-09 10:22 bin
  drwxr-xr-x 2 heejung.lee heejung.lee  4096 2015-03-09 10:22 conf
  drwxr-xr-x 2 heejung.lee heejung.lee  4096 2015-03-09 10:22 include
  drwxr-xr-x 2 heejung.lee heejung.lee  4096 2015-03-09 10:22 install
  drwxr-xr-x 2 heejung.lee heejung.lee  4096 2015-03-09 10:22 lib
  drwxr-xr-x 2 heejung.lee heejung.lee  4096 2015-03-09 10:22 msg
  -rw-rw-rw- 1 heejung.lee heejung.lee 84573 2014-11-28 15:46 report.txt
  drwxr-xr-x 9 heejung.lee heejung.lee  4096 2015-03-09 10:22 sample
  drwxr-xr-x 2 heejung.lee heejung.lee  4096 2015-03-09 10:22 thirdparty
  $
  ```

# Check OS user initialization file

---

- If the above process is successful, the following contents are included in the OS user's configuration file.

  **Example of Bash shell**

  ```
  $ cat ~/.bash_profile

  # ALTIBASE_ENV
  export ALTIBASE_HOME=/data/heejung.lee/altibase_home
  export ALTIBASE_PORT_NO=20300
  export PATH=${ALTIBASE_HOME}/bin:${PATH}
  export LD_LIBRARY_PATH=${ALTIBASE_HOME}/lib:${LD_LIBRARY_PATH}
  export CLASSPATH=${ALTIBASE_HOME}/lib/Altibase.jar:${CLASSPATH}
  ```
- The OS user initialization file name differs by shell:
  `Bourne shell(sh), Korn shell(ksh): .profile`
  `bash shell(bash): .bash_profile` or `.profile`
  `C shell(csh): .login` or `.cshrc`

# Apply OS user initialization file

---

- To apply the environment variables added to the initialization file, proceed as follows.

  ```
  $ . ~/.bash_profile
  ```

  Or

  ```
  $ . ~/.profile
  ```
- Check the environment variable value to confirm that it was applied.

  ```
  $ echo $ALTIBASE_HOME
  /data/heejung.lee/altibase_home
  ```

# Installation verification

---

- Altibase server connection test is performed by using iSQL

  ```
  isql -u DB_user_name -p password -s IP -port service_port
  ```
- Example

  ```
  $ isql -u sys -p manager -s 192.168.1.145 -port 20300
  -----------------------------------------------------------------
       Altibase Client Query utility.
       Release Version 6.3.1.3.1
       Copyright 2000, ALTIBASE Corporation or its subsidiaries.
       All Rights Reserved.
  -----------------------------------------------------------------
  ISQL_CONNECTION = TCP, SERVER = 192.168.1.145, PORT_NO = 20300
  iSQL>
  iSQL> SELECT PRODUCT_VERSION FROM V$VERSION;
  PRODUCT_VERSION
  ----------------------------------------------
  6.3.1.3.8
  1 row selected.
  iSQL>
  ```
