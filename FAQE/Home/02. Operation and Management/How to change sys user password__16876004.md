---
title: "How to change sys user password"
page_id: "16876004"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/How+to+change+sys+user+password"
updated_at: "2023-05-25T21:42:54.000+0900"
version: 5
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# How to change sys user password
Source: https://docs.altibase.com/display/FAQE/How+to+change+sys+user+password
Updated: 2023-05-25T21:42:54.000+0900

- [Overview](#Howtochangesysuserpassword-Overview) - [Version](#Howtochangesysuserpassword-Version) - [Procedure](#Howtochangesysuserpassword-Procedure) - [1. Execute the alter user command](#Howtochangesysuserpassword-1.Executethealterusercommand) - [2. Execute altipasswrd](#Howtochangesysuserpassword-2.Executealtipasswrd) - [3. Modify the script containing the sys password](#Howtochangesysuserpassword-3.Modifythescriptcontainingthesyspassword) - [Solution](#Howtochangesysuserpassword-Solution) - [What to do if an "Invalid password" error occurs when starting the server](#Howtochangesysuserpassword-Whattodoifan"Invalidpassword"erroroccurswhenstartingtheserver)

# Overview

---

This document explains the procedure for changing the password of the sys account.

# Version

---

ALTIBASE HDB version 4 or later

# Procedure

---

To change the password for the sys account, follow the three steps below.

## 1. Execute the alter user command

---

Connect to the Altibase server as the sys user and change the password with the alter user command.

```
ALTER USER sys IDENTIFIED BY "new_password";
```

## 2. Execute altipasswrd

---

Execute while the Altibase server is online.

**Example of executing altipasswd**

```
$ altipasswd
Previous Password : old_password
New Password : new_password
Retype New Password : new_password
```

altipasswd is...

- When the ALTIBASE HDB server is in shutdown stage, it checks the sys account password by referring to the syspassword file.
- Executing altipasswd changes the syspassword file. This file is located under the $ALTIBASE_HOME/conf directory.

## 3. Modify the script containing the sys password

The three scripts below contain the sys password.

So, when changing the sys password, these scripts also need to be modified.

- **server script** Change the password after the -p option in the $ALTIBASE_HOME/bin/server script to the new password.

  ```
  $ cd $ALTIBASE_HOME/bin
  $ vi server
  ADMIN="${ALTIBASE_HOME}/bin/isql -u sys -p manager -sysdba -noprompt"
  ISQL="${ALTIBASE_HOME}/bin/isql -s localhost -u sys -p manager -silent"
  ```
- **is script** Change the password after the -p option in the $ALTIBASE_HOME/bin/is script to the new password.

  ```
  $ cd $ALTIBASE_HOME/bin
  $ vi is
  ${ALTIBASE_HOME}/bin/isql -s localhost -u sys -p manager $*
  ```
- **il script** Change the password after the -p option in the $ALTIBASE_HOME/bin/il script to the new password.

  ```
  $ cd $ALTIBASE_HOME/bin
  $ vi il
  ${ALTIBASE_HOME}/bin/iloader -S localhost -U SYS -P MANAGER $*
  ```

# Solution

---

## What to do if an "Invalid password" error occurs when starting the server

a. Open the $ALTIBASE_HOME/bin/server script and check if the password has been modified in the lower part.

ADMIN="${ALTIBASE_HOME}/bin/isql -u sys -p manager -sysdba -noprompt"

ISQL="${ALTIBASE_HOME}/bin/isql -s localhost -u sys -p manager -silent"

b. If an invalid password error occurs even though the above is applied with the changed password, it is possible that the sys password was changed only with the alter user command and altipasswd was not executed.

In this case, execute altipasswd, apply the changed password, and then try to start the server.
