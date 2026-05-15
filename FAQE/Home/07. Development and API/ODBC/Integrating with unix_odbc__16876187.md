---
title: "Integrating with unix_odbc"
page_id: "16876187"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Integrating+with+unix_odbc"
updated_at: "2021-04-05T09:55:03.000+0900"
version: 2
ancestors: ["Home", "07. Development and API", "ODBC"]
labels: []
---

# Integrating with unix_odbc
Source: https://docs.altibase.com/display/FAQE/Integrating+with+unix_odbc
Updated: 2021-04-05T09:55:03.000+0900

- [Overview](#Integratingwithunix_odbc-Overview) - [Version](#Integratingwithunix_odbc-Version) - [UNIX ODBC type and URL](#Integratingwithunix_odbc-UNIXODBCtypeandURL) - [INSTALL](#Integratingwithunix_odbc-INSTALL) - [PHP, PERL Integration](#Integratingwithunix_odbc-PHP,PERLIntegration) - [PHP Integration Guide](#Integratingwithunix_odbc-PHPIntegrationGuide)

# Overview

---

This document is for integrating Altibase with UNIX_ODBC.

# Version

---

All the versions of ALTIBASE HDB

# UNIX ODBC type and URL

---

unix_odbc is an open source project, and unixODBC is mainly used.

1. unixODBC can be downloaded from the link below:
  - [http://unixodbc.org/](http://unixodbc.org/)

# INSTALL

---

```sh
$ mkdir $HOME/ODBC_HOME
$ gzip -d unixODBC-2.3.2.tar.gz
$ tar -xvf unixODBC-2.3.2.tar
$ cd unixODBC-2.3.2
$ cd $ALTIBASE_HOME/lib
$ file libaltibase_odbc-64bit-ul64.so
libaltibase_odbc-64bit-ul64.so: ELF 64-bit LSB shared object, AMD x86-64, version 1 (SYSV), not stripped

$ ./configure --prefix=/home/wonsik/ODBC_HOME --enable-gui=no --enable-threads=yes
```

Option descriptions:

- `prefix`: the path where unixODBC is installed.
- `enable-gui`: whether to build the GUI ODBC Administrator.
- `enable-threads`: the default is `yes` if thread support is found on the machine. Modern Linux systems have pthread support in glibc, so it is usually best to leave this enabled.

If the enable-threads option is set to no, the following error may occur when testing the connection with isql.

```sh
$ ./isql Altiodbc
./isql: symbol lookup error: /home/wonsik/altibase_home/lib/libaltibase_odbc-64bit-ul64.so: undefined symbol: pthread_sigmask
```

```sh
$ make
$ make install
$ cd ODBC_HOME
$ dltest $ALTIBASE_HOME/lib/libaltibase_odbc-64bit-ul64.so
SUCCESS: Loaded /home/wonsik/altibase_home/lib/libaltibase_odbc-64bit-ul64.so
```

```ini
$ cat odbc.ini
[ODBC Data Sources]
Altiodbc = Altibase ODBC Driver

[Altiodbc]
Driver = /home/wonsik/altibase_home/lib/libaltibase_odbc-64bit-ul64.so
Description = Sample Altibase DSN
UserName = SYS
Password = MANAGER
ServerType = Altibase
Server = 127.0.0.1
User = SYS
Port = 40501
Database = mydb
FetchBufferSize = 64
ReadOnly = no
TraceFile = /home/wonsik/ODBC_HOME/odbc.trace
Trace = 0
```

Trace option means 1 (debug), 0 (normal)

```sh
$ export ODBCINI=/home/wonsik/odbc.ini
$ cd $HOME/ODBC_HOME/bin
$ odbc_config --ulen
-DSIZEOF_SQLULEN=8

$ ./isql Altiodbc
+---------------------------------------+
| Connected! |
| |
| sql-statement |
| help [tablename] |
| quit |
| |
+---------------------------------------+
SQL>
```

# PHP, PERL Integration

---

PHP, PERL, etc. support unix_odbc, so it can be integrated with Altibase in the above way.

# PHP Integration Guide

---

1. Setting related environment variables

  Be sure to set the following variables in advance.

  ```sh
  export CFLAGS=-DBUILD_LEGACY_64_BIT_MODE=1
  export ODBCINI=/path/to/odbc.ini
  export LD_LIBRARY_PATH=$APACHE_HOME/modules:/path/to/unixODBC/lib:/path/to/php/lib
  ```
2. Check SQLLEN, SQLULEN

  Move to the `bin` directory of the unixODBC installation path and use the `odbcinst` command to check whether the `SQLLEN` and `SQLULEN` sizes are 4.

  If the value is 4, it is set to 32-bit. If the value is 8, it is set to 64-bit.

  ```sh
  $ ./odbcinst -j

  unixODBC 2.3.2

  DRIVERS............: /home/altibase/phptest/unixodbc/etc/odbcinst.ini

  SYSTEM DATA SOURCES: /home/altibase/phptest/unixodbc/etc/odbc.ini

  FILE DATA SOURCES..: /home/altibase/phptest/unixodbc/etc/ODBCDataSources

  USER DATA SOURCES..: /home/altibase/phptest/unixodbc/etc/odbc.ini

  SQLULEN Size.......: 4

  SQLLEN Size........: 4 <--- If 4, 32-bit. If 8, 64-bit.

  SQLSETPOSIROW Size.: 2
  ```
3. Modify unixODBC's odbc.ini file

  LOB data can be processed by adding `LongDataCompat=ON` to the `odbc.ini` file.
4. PHP compilation and installation operation

  ```sh
  $> ./configure \
      --prefix=/user/web/php \
      --with-config-file-path=/user/web/php/conf \
      --with-apxs2=/user/web/apache2/bin/apxs \
      --with-unixODBC=/user/web/odbc \
      --with-mcrypt \
      --with-mhash \
      --with-openssl \
      --with-kerberos \
      --with-curl \
      --enable-dom \
      --with-iconv=/usr/local \
      --with-xmlrpc \
      --enable-libxml \
      --with-libxml-dir=/usr/lib64 \
      --with-gd \
      --with-freetype-dir=/usr \
      --with-jpeg-dir=/usr/lib64 \
      --with-png-dir=/usr/lib64 \
      --with-zlib-dir=/usr/lib64 \
      --enable-mbstring \
      --enable-shmop \
      --enable-sockets \
      --enable-sigchild \
      --enable-soap \
      --enable-zip \
      --enable-ftp \
      --enable-sysvmsg \
      --enable-sysvsem \
      --enable-sysvshm \
      --with-regex=php \
      --with-pcre-regex \
      --enable-mbregex \
      --enable-dba=shared \
      --enable-mod-charset \
      --with-xml \
      --with-pcre \
      --with-gdbm \
      --with-dbm
  $> make
  $> make install
  ```
5. php.ini settings

  ```ini
  memory_limit=-1
  odbc.defaultbinmode=1
  odbc.defaultlrl=1048576
  ```
