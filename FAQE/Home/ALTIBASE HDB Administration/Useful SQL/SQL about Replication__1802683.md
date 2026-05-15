---
title: "SQL about Replication"
page_id: "1802683"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/SQL+about+Replication"
updated_at: "2011-08-06T10:57:34.000+0900"
version: 8
ancestors: ["Home", "ALTIBASE HDB Administration", "Useful SQL"]
labels: []
---

# SQL about Replication
Source: https://docs.altibase.com/display/FAQE/SQL+about+Replication
Updated: 2011-08-06T10:57:34.000+0900

- [Replication Sender](#SQLaboutReplication-ReplicationSender)
- [Replication Receiver](#SQLaboutReplication-ReplicationReceiver)
- [Replication gap](#SQLaboutReplication-Replicationgap)
- [Replication status](#SQLaboutReplication-Replicationstatus)
- [Log buffer or file status occupied by an unsent XLOG](#SQLaboutReplication-LogbufferorfilestatusoccupiedbyanunsentXLOG)
    - [ALTIBASE HDB V4](#SQLaboutReplication-ALTIBASEHDBV4)
    - [ALTIBASE HDB V5](#SQLaboutReplication-ALTIBASEHDBV5)
- [Replication table list](#SQLaboutReplication-Replicationtablelist)

# Replication Sender

This query returns the replication sender status.

| Column Name | Description |
| --- | --- |
| REP_NAME | the name of replication object |
| REMOTE_IP | the IP address of remote replicated server |
| REMOTE_REP_PORT | the port number of remote replicated server |
| STATUS | the status of replication sender |
| NETWORK | check whether network error or not |
| XSN | XLOG Sequence Number : the final position in a log file from which logs were transmitted by the replication sender |

```
SELECT 	REP_NAME,
        PEER_IP REMOTE_IP,
        PEER_PORT REMOTE_REP_PORT,
        DECODE(STATUS, 0, 'STOP', 1, 'RUN', 2, 'RETRY') AS STATUS,
        DECODE(NET_ERROR_FLAG, 0, 'OK', 'ERROR') AS NETWORK,
        XSN
FROM V$REPSENDER ;
```

# Replication Receiver

| Column Name | Description |
| --- | --- |
| REP_NAME | the name of replication object |
| REMOTE_IP | the IP address of remote replicated server |
| REMOTE_REP_PORT | the port number of remote replicated server |
| APPLY_XSN | applied XLOG Sequence Number : the final position in a log file from which logs were applied by the replication receiver |

```
SELECT 	REP_NAME,
	      PEER_IP REMOTE_IP,
	      PEER_PORT REMOTE_REP_PORT,
	      APPLY_XSN
FROM V$REPRECEIVER ;
```

# Replication gap

| Column Name | Description |
| --- | --- |
| REP_NAME | the name of replication object |
| REMOTE_IP | the IP address of remote replicated server |
| REMOTE_REP_PORT | the port number of remote replicated server |
| APPLY_XSN | applied XLOG Sequence Number : the final position in a log file from which logs were applied by the replication receiver |

```
SELECT 	REP_NAME,
 		    REP_SN,
 		    REP_LAST_SN,
 		    REP_GAP,
 		    READ_FILE_NO,
 		    START_FLAG
FROM    V$REPGAP ;
```

# Replication status

| Column Name | Description |
| --- | --- |
| REP_NAME | the name of replication object |
| REMOTE_IP | the IP address of remote replicated server |
| REP_GAP | the interval between the log record that was most recently written due to a transaction on the local server and the log record that is currently being sent by the replication Sender thread. |
| RESTART_XSN | the XSN from which the Sender thread must begin sending logs when replication is started. |
| SENDER | the sender status |
| RECEIVER | the receiver status |

```
SELECT 	A.REPLICATION_NAME REP_NAME,
        D.HOST_IP REMOTE_IP,
        NVL(TO_CHAR(E.REP_GAP), '-') AS REP_GAP,
        A.XSN RESTART_XSN,
        DECODE(B.PEER_PORT, NULL, 'OFF', 'ON') AS SENDER,
        DECODE(C.PEER_PORT, NULL, 'OFF', 'ON') AS RECEIVER
FROM    SYSTEM_.SYS_REPL_HOSTS_ D ,
        SYSTEM_.SYS_REPLICATIONS_ A LEFT OUTER JOIN
        V$REPSENDER B ON A.REPLICATION_NAME = B.REP_NAME
        LEFT OUTER JOIN V$REPRECEIVER C ON A.REPLICATION_NAME = C.REP_NAME LEFT OUTER JOIN
        (
        	SELECT REP_NAME,
        	       MAX(REP_GAP) REP_GAP
        	FROM   V$REPGAP
        	GROUP BY REP_NAME
         ) E ON A.REPLICATION_NAME = E.REP_NAME
WHERE 	A.REPLICATION_NAME = D.REPLICATION_NAME
ORDER BY REP_NAME ;
```

# Log buffer or file status occupied by an unsent XLOG

This query shows that the logbuffer/logfile status which is occupied by an unsent XLOG.

## ALTIBASE HDB V4

ALTIBASE V4 does not support this feature.

## ALTIBASE HDB V5

```
SELECT 	CASE2((BUFFER_MIN_SN < READ_SN), 'REP BUFFER '||ROUND((BUFFER_MAX_SN-READ_SN)/(BUFFER_MAX_SN-BUFFER_MIN_SN)*100,2)||' % LEFT ', (SELECT TO_CHAR(CUR_WRITE_LF_NO - READ_FILE_NO) FROM    V$LFG, V$REPGAP)) LOGFILE_FOR_REP
FROM 	  V$REPLOGBUFFER ;
```

# Replication table list

The list of tables that participate in a replication.

| Column Name | Description |
| --- | --- |
| REP_NAME | the name of replication object |
| LOCAL_TABLE | the local table name |
| REMOTE_TABLE | the remote table name |

```
SELECT 	REPLICATION_NAME REP_NAME,
        LOCAL_USER_NAME||'.'||LOCAL_TABLE_NAME LOCAL_TABLE,
        REMOTE_USER_NAME||'.'||REMOTE_TABLE_NAME REMOTE_TABLE
FROM    SYSTEM_.SYS_REPL_ITEMS_
ORDER BY 1, 2 ;
```
