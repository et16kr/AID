---
title: "How to check the history of adding datafiles"
page_id: "16875969"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/How+to+check+the+history+of+adding+datafiles"
updated_at: "2021-03-03T17:36:59.000+0900"
version: 1
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# How to check the history of adding datafiles
Source: https://docs.altibase.com/display/FAQE/How+to+check+the+history+of+adding+datafiles
Updated: 2021-03-03T17:36:59.000+0900

- [How to check](#Howtocheckthehistoryofaddingdatafiles-Howtocheck) - [Version](#Howtocheckthehistoryofaddingdatafiles-Version) - [How to change properties](#Howtocheckthehistoryofaddingdatafiles-Howtochangeproperties) - [How to use the ALTER SYSTEM command](#Howtocheckthehistoryofaddingdatafiles-HowtousetheALTERSYSTEMcommand) - [How to reflect in the altibase.properties file](#Howtocheckthehistoryofaddingdatafiles-Howtoreflectinthealtibase.propertiesfile) - [How to check logs](#Howtocheckthehistoryofaddingdatafiles-Howtochecklogs)

# How to check

---

Data file addition or change time information is not recorded in a separate performance view or v$datafiles. However, if the QP_MSGLOG_FLAG property is set to record DDL statements, DDL statements are recorded in $ALTIBASE_HOME/trc/altibase_qp.log, so this file can be opened, and the changes can be checked in the datafile.

# Version

---

This is supported by Altibase HDB version 4.3.9 or later.

# How to change properties

---

Change the setting value of QP_MSGLOG_FLAG so that DDL can be logged in altibase_qp.log. One of the following two methods can be used to change the method.

## How to use the ALTER SYSTEM command

If the user changes it by using this method, the value of the property can be changed without restarting the server. When the server is restarted, the default value is restored. To keep the changed value even after the server is restarted, the property change value must be applied in the $ALTIBASE_HOME/conf/altibase.properties file.

iSQL> alter system set qp_msglog_flag=2;

Alter success

## How to reflect in the altibase.properties file

---

1) Add the following line in the $ALTIBASE_HOME/conf/altibase.properties file.

|  |
| --- |
| QP_MSGLOG_FLAG = 2 # 2: DDL logging |

2) Restart the ALTIBASE process.

shell> server restart

3) Check if the changed value has been applied.

iSQL> select name, value1 from v$property where name='QP_MSGLOG_FLAG';

Starting from Altibase HDB version 5.1.5.33 or later, the default value of QP_MSGLOG_FLAG is 2, so all DDLs are written to altibase_qp.log by default.

# How to check logs

---

When a data file is added with the alter tablespace ~ add datafiles statement, the following log is displayed in altibase_qp.log.

|  |
| --- |
| [2013/11/27 14:10:57] [Thread-1094719840] [Level-2] [EXEC_DDL_BEGIN : alter tablespace TEST_TBS add DATAFILE '/altibase_home_533/dbs/test02.dbf'] [2013/11/27 14:10:58] [Thread-1094719840] [Level-2] [EXEC_DDL_END : SUCCESS] |

If the user uses the following syntax, the following will be the result.

|  |
| --- |
| shell> $awk '/DATAFILE/ {print last " : " $0}{last=$0}' altibase_qp.log \| grep -i 'add' [2013/11/27 14:10:57] [Thread-1094719840] [Level-2] : **[EXEC_DDL_BEGIN : alter tablespace TEST_TBS add DATAFILE '/altibase_home_533/dbs/test02.dbf']** |

However, since it is a method of grep-ing the trace log file, the history that is old enough to be deleted from the log file cannot be found.
