---
title: "When server create errors occur after DB name change"
page_id: "16875972"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/When+server+create+errors+occur+after+DB+name+change"
updated_at: "2021-03-03T17:49:21.000+0900"
version: 1
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# When server create errors occur after DB name change
Source: https://docs.altibase.com/display/FAQE/When+server+create+errors+occur+after+DB+name+change
Updated: 2021-03-03T17:49:21.000+0900

# Contents

---

In versions 5.3.3 and earlier, the DB must be created manually.

The following types of tasks can be performed by executing the server command, and the DB can be created with the server create command.

Usage: server { start | stop | kill | status | create db_charset national_charset | restart }

$server create MS949 UTF8

When the first DB is created, the DB NAME is set to mydb, and DB_NAME can be changed in altibase.properties.

#=================================================================

# Fixed Properties # should not be modified after createdb

#=================================================================

**DB_NAME = mydb <-- change to the new DB name**

MEM_DB_DIR = ?/dbs

MEM_DB_DIR = ?/dbs

DEFAULT_DISK_DB_DIR = ?/dbs

When running `server create` after changing `DB_NAME`, the following error occurs.

**$server create MS949 UTF8**

**Connecting to the DB server... Connected.** **TRANSITION TO PHASE : PROCESS** **Command executed successfully.** **FAILURE of createdb.** **Invalid Database Name. Check the properties and retry.** **[ERR-91015 : Communication failure.]**

# Solution

---

This occurs because the DB name is mydb in the $ALTIBASE_HOME/bin/server script file.

```
'create') if [ $# = 3 ]; then rm -f live-altibase.txt; ${ISQL} << EOF > /dev/null spool live-altibase.txt; EOF if [ -f live-altibase.txt ]; then echo " server is running !!!! \n " echo " you must shutdown first before server create " rm -f live-altibase.txt; else ${ADMIN} << EOF startup process; create database mydb INITSIZE=10M noarchivelog character set $2 national character set $3; quit EOF
```

Create the DB after changing this script value to the same `DB_NAME` that was set in `altibase.properties`.
