---
title: "Hangul is broken when using php"
page_id: "16876191"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Hangul+is+broken+when+using+php"
updated_at: "2021-04-05T09:55:48.000+0900"
version: 3
ancestors: ["Home", "07. Development and API", "PHP"]
labels: []
---

# Hangul is broken when using php
Source: https://docs.altibase.com/display/FAQE/Hangul+is+broken+when+using+php
Updated: 2021-04-05T09:55:48.000+0900

- [Situation](#Hangulisbrokenwhenusingphp-Situation) - [PHP execution structure](#Hangulisbrokenwhenusingphp-PHPexecutionstructure) - [Main Cause](#Hangulisbrokenwhenusingphp-MainCause) - [Setting NLS_USE in ODBC settings](#Hangulisbrokenwhenusingphp-SettingNLS_USEinODBCsettings) - [Korean language support code setting in terminal window](#Hangulisbrokenwhenusingphp-Koreanlanguagesupportcodesettinginterminalwindow) - [Setting the maximum length set for a variable in PHP config](#Hangulisbrokenwhenusingphp-SettingthemaximumlengthsetforavariableinPHPconfig)

# Situation

---

When searching Korean on a web page using PHP, Korean characters may be broken.

This document describes the causes and solutions for this situation.

# PHP execution structure

---

ALTIBASE HDB can be accessed through ODBC APIs from PHP pages by using the ODBC driver manager unixODBC ([http://www.unixodbc.org/](http://www.unixodbc.org/)) and the ODBC driver provided by Altibase.

For information on how to connect Altibase and PHP, refer to [PHP Integration Guide for Altibase](https://aid.altibase.com/display/arch/PHP+Integration+Guide+for+Altibase).

![php%E1%84%92%E1%85%A9%E1%84%8E%E1%85%AE%E1%86%AF%E1%84%89%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5.png](https://docs.altibase.com/download/attachments/embedded-page/FAQE/Hangul%20is%20broken%20when%20using%20php/php%E1%84%92%E1%85%A9%E1%84%8E%E1%85%AE%E1%86%AF%E1%84%89%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A5.png?api=v2)

# Main Cause

---

Broken Hangul output can be caused by configuration problems in several places, such as the web server configuration, PHP configuration, or unixODBC configuration. First, check that DB results containing Hangul are displayed normally through unixODBC.

Use the `$UNIXODBC_HOME/bin/isql` utility provided by unixODBC to execute a query on the DB and check whether query results containing Korean characters are displayed normally, and then check the PHP settings.

After that, the last step is to check the web server setting or web page setting to make sure there is no problem with the character set setting related to Korean.

# Setting NLS_USE in ODBC settings

---

In the unixODBC `odbc.ini` file, the `NLS_USE` setting specifies the client character set used for the DB connection. If this value does not match the DB character set, Korean output may be corrupted.

This property must be set to the same value as the DB character set.

Contents set in the odbc.ini file

```ini
[Altiodbc]

Driver = /home/omegaman/altibase_home/lib/libaltibase_odbc-64bit-ul64.so

Description = altibase odbc

User = SYS

Password = MANAGER

ServerType = altibase

Server = 127.0.0.1

User = SYS

Port = 21038

**NLS_USE = MS949**

Database = mydb

FetchBufferSize = 64

ReadOnly = no

TraceFile = /tmp/odbc.log

Trace = 1
```

## Korean language support code setting in terminal window

---

Even though data is normally imported from the DB, if the terminal window that outputs it does not support the output of the Korean character set, the Korean language may not be displayed properly.

If the DB character set is set to UTF8, the code page (chcp command) must be set so that Unicode can be displayed in the window command window. Otherwise, Korean characters will not be displayed normally.

```text
C:\Users\omegaman>isql -s 192.168.1.35 -port 20416

iSQL> set vertical on;

iSQL> select nls_use, nls_characterset from v$nls_parameters;

NLS_USE : US7ASCII

NLS_CHARACTERSET : UTF8

iSQL> exit;

C:\Users\Altibase>chcp 65001 <-- The console character must be set to Unicode (65001) as the character set of the DB is UTF8, which is unicode.

Active code page: 65001
```

When a terminal access program such as Secure CRT outputs UTF8 Korean characters, Unicode-related session settings must also be configured correctly for Korean characters to display normally.

![secureCRT%E1%84%86%E1%85%AE%E1%86%AB%E1%84%8C%E1%85%A1%E1%84%89%E1%85%A5%E1%86%AF%E1%84%8C%E1%85%A5%E1%86%BC.png](https://docs.altibase.com/download/attachments/embedded-page/FAQE/Hangul%20is%20broken%20when%20using%20php/secureCRT%E1%84%86%E1%85%AE%E1%86%AB%E1%84%8C%E1%85%A1%E1%84%89%E1%85%A5%E1%86%AF%E1%84%8C%E1%85%A5%E1%86%BC.png?api=v2)

# Setting the maximum length set for a variable in PHP config

---

If the php program is running, varchar or clob data with large data may be broken or the same data may appear repeatedly. If **there is a problem with data output from a specific part**, the user should look at the odbc configuration part.

If it happens as above, change the odbc.defaultlrl value in php.ini so that all data can be included.

For example, if the column is varchar(65536), data may be output incorrectly by default odbc.defaultlrl = 4096.

If it is changed to **odbc.defaultlrl = 65536**, data up to 64 KBytes can be output normally.

Generally, php.ini is under /etc, but this may vary depending on the configuration.
