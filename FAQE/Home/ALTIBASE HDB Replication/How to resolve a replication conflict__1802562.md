---
title: "How to resolve a replication conflict?"
page_id: "1802562"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=1802562"
updated_at: "2011-08-06T10:47:53.000+0900"
version: 100
ancestors: ["Home", "ALTIBASE HDB Replication"]
labels: []
---

# How to resolve a replication conflict?
Source: https://docs.altibase.com/pages/viewpage.action?pageId=1802562
Updated: 2011-08-06T10:47:53.000+0900

- [Replication conflict resolution in ALTIBASE HDB](#Howtoresolveareplicationconflict?-ReplicationconflictresolutioninALTIBASEHDB)
    - [Eager mode Replication](#Howtoresolveareplicationconflict?-EagermodeReplication)
          - [Overview](#Howtoresolveareplicationconflict?-Overview)
          - [How to configure this mode?](#Howtoresolveareplicationconflict?-Howtoconfigurethismode?)
          - [Considerations](#Howtoresolveareplicationconflict?-Considerations)
    - [User-oriented scheme (REPLICATION_UPDATE_REPLACE property)](#Howtoresolveareplicationconflict?-User-orientedscheme(REPLICATION_UPDATE_REPLACEproperty))
          - [Overview](#Howtoresolveareplicationconflict?-Overview.1)
          - [How to configure this scheme?](#Howtoresolveareplicationconflict?-Howtoconfigurethisscheme?)
          - [Considerations](#Howtoresolveareplicationconflict?-Considerations.1)
    - [Time Stamp scheme](#Howtoresolveareplicationconflict?-TimeStampscheme)
          - [Overview](#Howtoresolveareplicationconflict?-Overview.2)
          - [How to configure this scheme?](#Howtoresolveareplicationconflict?-Howtoconfigurethisscheme?.1)
          - [Considerations](#Howtoresolveareplicationconflict?-Considerations.2)
- [Summary](#Howtoresolveareplicationconflict?-Summary)

# Replication conflict resolution in ALTIBASE HDB

We explained that a replication conflict is caused by either network delays or irregular sequence of transactions. In a typical conflict situation, a Receiver cannot decide which record is correct between the current value and the before value in Xlog. To help users to deal with such replication conflicts, ALTIBASE HDB provides a few different conflict resolution schemes, such as user-oriented scheme, a master-scheme and a time stamp based scheme.

## Eager mode Replication

### Overview

> Diagram note: The source export did not include this Confluence Gliffy diagram, and no diagram image URL is available in this repository.

| Steps | Description |
| --- | --- |
| 1 | Local Transaction takes place and waits until the step #5 |
| 2 | Sender creates XLog |
| 3 | Sender sends XLog to Receiver |
| 4,5 | Receiver applies and returns the result back to Sender |
| 6 | Return errorCode to the application |

We already explained about the typical flow of [Eager mode Replication.](http://aid.altibase.com/x/BYEb) Here is a typical flow for in case of a replication conflict: the transaction in the local server cannot be completed until the Sender receives an ACK from the Receiver in the remote server. The Receiver checks whether any conflict has occurred in the remote server. If the transaction fails due to a conflict in the remote server, the Receiver sends an ACK containing the error information related to the conflict back to Sender. In this case, the transaction in the local server will also fail.

### How to configure this mode?

User can specify the mode when creating a replication object as shown below:

```
CREATE EAGER REPLICATION WITH '' ...
```

### Considerations

Performance of Eager mode replication is always slower than that of Lazy mode. If your priority is high performance, Eager mode replication is not a good choice.

## User-oriented scheme (REPLICATION_UPDATE_REPLACE property)

### Overview

> Diagram note: The source export did not include this Confluence Gliffy diagram, and no diagram image URL is available in this repository.

| Steps | Description |
| --- | --- |
| 1,2 | Local Transaction completes without waiting for an ACK from Receiver |
| 3 | Sender creates XLog |
| 3 | Sender sends XLog to Receiver |
| 4 | Receiver applies XLog regardless of a replication conflict |

REPLICATION_UPDATE_REPLACE is one of properties in ALTIBASE HDB. When it is turn on, Receiver does not check for a conflict any more. It simply overwrites the existing record even if there is a replication conflict. In the above diagram, the conflict has occurred because the existing value ("30") is different from the before-value ("10") of XLog. When user uses this method, the existing data in the remote server is modified to "20".

### How to configure this scheme?

Set the value of REPLICATION_UPDATE_REPLACE property to "1" in $ALTIBASE_HOME/conf/altibase.properties so that Receiver does not check for any conflict.

### Considerations

Network delays can introduce mismatches for last values.

## Time Stamp scheme

### Overview

> Diagram note: The source export did not include this Confluence Gliffy diagram, and no diagram image URL is available in this repository.

This method is similar to REPLICATION_UPDATE_REPLACE method, however, Receiver compares the timestamp value of an existing record with the timestamp value of XLog when Receiver applies XLog to the remote server. If the timestamp value of XLog is bigger than the existing record, XLog will be applied, otherwise, the replication transaction will be dropped. In the above diagram, since the timestamp value (11:01) of XLog is smaller than the timestamp value (11:02) of the existing data, the replication transaction can not be applied to the remote server. On the other hand, if XLog of Node B has been sent to Node A, the existing data would be replaced with the XLog from Node B since timestamp value of Node B is bigger than that of Node B.

### How to configure this scheme?

1. Add a timestamp column to the table.
2. set REPLICATION_TIMESTAMP_RESOLUTION value to "1" in $ALTIBASE_HOME/conf/altibase.properties.

### Considerations

Since the size of timestamp data type is 8 bytes, the size of the record will be increased by 8 bytes.

System clocks should be synchronized across the servers to ensure accuracy of the operation.

# Summary

Users should know that these methods do not guarantee the data consistency perfectly, they only allow users to control the behavior of Receiver when replication conflicts occur.

For more information, please refer to [reference manual](http://atc.altibase.com/sub09/551b/html/Replication/ch02s03.html#N10570)
