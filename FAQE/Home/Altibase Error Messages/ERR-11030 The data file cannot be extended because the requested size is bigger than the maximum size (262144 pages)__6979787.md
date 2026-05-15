---
title: "ERR-11030 The data file cannot be extended because the requested size is bigger than the maximum size (262144 pages)"
page_id: "6979787"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=6979787"
updated_at: "2014-11-20T14:00:21.000+0900"
version: 11
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-11030 The data file cannot be extended because the requested size is bigger than the maximum size (262144 pages)
Source: https://docs.altibase.com/pages/viewpage.action?pageId=6979787
Updated: 2014-11-20T14:00:21.000+0900

- [Version](#ERR-11030Thedatafilecannotbeextendedbecausetherequestedsizeisbiggerthanthemaximumsize(262144pages)-Version)
- [Explanation](#ERR-11030Thedatafilecannotbeextendedbecausetherequestedsizeisbiggerthanthemaximumsize(262144pages)-Explanation)
- [Cause](#ERR-11030Thedatafilecannotbeextendedbecausetherequestedsizeisbiggerthanthemaximumsize(262144pages)-Cause)
- [Action](#ERR-11030Thedatafilecannotbeextendedbecausetherequestedsizeisbiggerthanthemaximumsize(262144pages)-Action)
    - [1. Change the AUTOEXTEND option](#ERR-11030Thedatafilecannotbeextendedbecausetherequestedsizeisbiggerthanthemaximumsize(262144pages)-1.ChangetheAUTOEXTENDoption)
    - [2. Change the datafile size](#ERR-11030Thedatafilecannotbeextendedbecausetherequestedsizeisbiggerthanthemaximumsize(262144pages)-2.Changethedatafilesize)
    - [3. Increase SYS_UNDO_FILE_MAX_SIZE](#ERR-11030Thedatafilecannotbeextendedbecausetherequestedsizeisbiggerthanthemaximumsize(262144pages)-3.IncreaseSYS_UNDO_FILE_MAX_SIZE)
- [Reference](#ERR-11030Thedatafilecannotbeextendedbecausetherequestedsizeisbiggerthanthemaximumsize(262144pages)-Reference)

## Version

4.3.9 or above

## Explanation

1. Unable to change the datafile size of the disk tablespace.

2. Unable to resize the undo tablespace datafile.

## Cause

1. The user has attempted to change the size of a datafile that has the AUTOEXTEND option OFF to a value bigger than the maximum size.

2. The value of the undo tablespace datafile to be resized exceeded SYS_UNO_FILE_MAX_SIZE.

## Action

Set the AUTOEXTEND option of datafile to ON and follow the steps as below to change the datafile size.

##### 1. Change the AUTOEXTEND option

```
iSQL>ALTER TABLESPACE DISK_USER_TBS
   2 ALTER DATAFILE '/home/altibase_home/dbs/user.dbf' AUTOEXTEND ON;
Alter success.
```

##### 2. Change the datafile size

```
iSQL> ALTER TABLESPACE DISK_USER_TBS
   2  ALTER DATAFILE '/home/altibase_home/dbs/user.dbf' SIZE 100M;
Alter success.
```

##### 3. Increase SYS_UNDO_FILE_MAX_SIZE

Change SYS_UNDO_FILE_MAX_SIZE from $ALTIBASE_HOME/conf/altibase.properties to the desired size (in bytes) and recreate the database.

## Reference

In order to change this property, the database has to be recreated.

Hence, if you want to increase the undospace size, it is easier to use the ALTER TABLESPACE command to add a datafile.
