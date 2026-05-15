---
title: "32-bit ODBC installation on 64-bit Windows"
page_id: "22642957"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/32-bit+ODBC+installation+on+64-bit+Windows"
updated_at: "2025-10-20T15:40:42.000+0900"
version: 1
ancestors: ["Home", "07. Development and API", "ODBC"]
labels: []
---

# 32-bit ODBC installation on 64-bit Windows
Source: https://docs.altibase.com/display/FAQE/32-bit+ODBC+installation+on+64-bit+Windows
Updated: 2025-10-20T15:40:42.000+0900

- [Overview](#id-32-bitODBCinstallationon64-bitWindows-Overview) - [Version](#id-32-bitODBCinstallationon64-bitWindows-Version) - [Altibase ODBC installation](#id-32-bitODBCinstallationon64-bitWindows-AltibaseODBCinstallation) - [ODBC Setting](#id-32-bitODBCinstallationon64-bitWindows-ODBCSetting)

# Overview

---

This document describes how to set up 32-bit ODBC driver on Windows Server 2003 64-bit systems.

# Version

---

~ Altibase 6.5.1 (**Note:** Starting from version 7.1, 32-bit ODBC drivers are no longer supported.)

# Altibase ODBC installation

---

1. Download the Windows Altibase 32-bit client installation file or the Altibase 32-bit ODBC installation file.
  Download: [http://support.altibase.com/en/product](http://support.altibase.com/en/product)
  Client installation file name example: altibase-HDB-client-x.x.x.x.x-WINDOWS-X86-32bit-release.exe
  ODBC installation file name example: altibase-HDB-ODBC-x.x.x.x.x-WINDOWS-X86-32bit-release.exe
2. Install the Windows Altibase 32-bit client.
  For the installation method, refer to 2. Product Installation Using Package Installer -> ALTIBASE HDB Client Product Installation in Windows in the Installation Guide manual.
  Manual download: [http://support.altibase.com/en/manual](http://support.altibase.com/en/manual)

# ODBC Setting

---

1. Run the data source manager for 32-bit ODBC.
  Double-click C:\windows\sysWOW64\odbcad32.exe.
  ![image2018-11-7%2017_39_40.png](https://docs.altibase.com/download/attachments/embedded-page/FAQE/32-bit%20ODBC%20installation%20on%2064-bit%20Windows/image2018-11-7%2017_39_40.png?api=v2)
2. Create a new data source
  Click the 'Add' button in the user 'DSN tab' of the ODBC Data Source Administrator window to open the Create New Data Source window.
  Select the Altibase 32-bit ODBC driver and click 'Finish'.
  ![image2018-11-7%2017_42_35.png](https://docs.altibase.com/download/attachments/embedded-page/FAQE/32-bit%20ODBC%20installation%20on%2064-bit%20Windows/image2018-11-7%2017_42_35.png?api=v2)
3. When the 'Altibase Connection Config' window appears, enter the Altibase server connection information.
  ![image2018-11-7%2017_45_52.png](https://docs.altibase.com/download/attachments/embedded-page/FAQE/32-bit%20ODBC%20installation%20on%2064-bit%20Windows/image2018-11-7%2017_45_52.png?api=v2)
  ● Windows DSN Name
  Enter a custom name for the data source.
  ● host (name or IP)
  Enter the IP of the Altibase server.
  ● Port (default 20300)
  Enter the service port of the Altibase server
  Check the value of PORT_NO in the altibase.properties file (Altibase server properties file) or the value of the ALTIBASE_PORT_NO environment variable on the Altibase server.
  ● User
  Enter the database user name.
  ● Password
  Enter the database user password.
  ● Database
  Enter the database name.
  The database name can be checked with SELECT_DB_NAME FROM V$DATABASE;
  ● NLS_USE
  Enter the Altibase server character set.
  The Altibase server character set can be checked with NLS_CHARACTERSET FROM V$NLS_PARAMETERS;
4. Click the Test Connection button to check the connection.
  ![image2018-11-7%2017_54_58.png](https://docs.altibase.com/download/attachments/embedded-page/FAQE/32-bit%20ODBC%20installation%20on%2064-bit%20Windows/image2018-11-7%2017_54_58.png?api=v2)
5. Check the Altibase DSN added to the User DSN tab.
  ![image2018-11-7%2017_56_26.png](https://docs.altibase.com/download/attachments/embedded-page/FAQE/32-bit%20ODBC%20installation%20on%2064-bit%20Windows/image2018-11-7%2017_56_26.png?api=v2)
