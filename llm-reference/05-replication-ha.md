# Replication and High Availability

## Source paths

R010 source paths covered in this revision:

- `arch/Home/Altibase Replication Configuration Guide__14647672.md`
- `arch/Home/Altibase Replication Constraints Guide__22643008.md`
- `FAQE/Home/03. Replication/Causes and Solutions of Replication Conflicts__16876059.md`
- `FAQE/Home/03. Replication/DDL operation on the table for Altibase replication__22642943.md`
- `FAQE/Home/03. Replication/How to add_delete replication target table__16876094.md`
- `FAQE/Home/03. Replication/How to change replication object IP__16876079.md`
- `FAQE/Home/03. Replication/How to create multiple replication objects with the same IP__16876063.md`
- `FAQE/Home/03. Replication/How to create_delete replication objects__16876082.md`
- `FAQE/Home/03. Replication/Replication give-up__22642945.md`
- `FAQE/Home/03. Replication/Replication monitoring query__22642947.md`

## Source coverage notes

This document covers the R010 topic: Altibase replication design, high availability, Sender and Receiver behavior, Lazy and Eager replication modes, Off-Line Replicator use, HA solution cautions, N-way replication, replication setup, target-table changes, DDL handling, constraints, conflict handling, gap monitoring, GIVE-UP behavior, and every Korean-source-verified replication FAQ variant in `FAQE/Home/03. Replication/**`.

The replication configuration guide and seven replication FAQ pages are classified as `Korean-source-verified` in `llm-reference/coverage/source-inventory.tsv`. The replication constraints guide and `FAQE/Home/03. Replication/How to create_delete replication objects__16876082.md` are classified as `Link-validated Korean-source-verified` because Phase 2 validated the Korean-source attachment URLs.

No English-only auxiliary source is used in this R010 revision.

The source set preserves three URL-backed PDF attachments: one Korean-source replication constraints PDF in the architecture constraints guide and two replication guide PDFs in the create/delete replication objects FAQ. Embedded diagrams and screenshots are registered as `not_document_format`; this topic preserves the surrounding technical meaning without reconstructing image pixels.

R009 already covers replication-related first-response checks from the failure-response guide, including `V$REPGAP`, retained online log risk, and trace-log triage during failures. This R010 document owns the dedicated replication setup, HA, constraints, conflict, GIVE-UP, and monitoring FAQ coverage.

## Scope and audience

Use this document to answer DBA, SRE, platform, support, and LLM questions about designing and operating Altibase replication and HA. It is written for answer generation that needs exact Altibase identifiers, SQL, properties, paths, version conditions, source limitations, and failure modes.

When answering in another language, keep product names, commands, SQL, system views, property names, paths, error codes, log filenames, attachment filenames, and source URLs exactly as written.

## Key facts

Altibase HA guidance compares disk sharing, network replication, and HA solution switching. Altibase does not support the disk-sharing method as a built-in high-availability approach; its replication architecture uses network-based data synchronization between independent databases.

A node is a server connected through one or more networks and configured to provide the user's service. Fail-over means transferring service to a healthy node when a failure occurs between nodes, with only minimal service downtime.

High availability design has two source-defined goals:

| Goal | Meaning |
| --- | --- |
| Performance | Compared with a single-node system, the HA design should not cause significant performance degradation. |
| Continuous service | In any failure type, service should resume with minimal downtime. |

The disk-sharing method uses a shared DB on shared disk, a master node that controls buffer-cache synchronization, and shared-disk access by all nodes. The source says this can be best for data integrity, but it can degrade performance through master-node communication and buffer-access waits, require high-speed buffer-replication equipment between all nodes, and make shared-disk failure an entire-system failure.

Altibase network replication lets each node own a separate database and transmit transaction logs over the network. The replication configuration guide says this can maintain at least about `90%` of single-system performance because only network log transmission is added. The tradeoff is that the transaction time on the local node and the apply time on the peer node can differ, so 100% consistency across nodes cannot be guaranteed by network replication alone.

Altibase replication is transaction-log based:

1. A committed local change writes redo log through the storage manager.
2. The local Sender reads that transaction log and converts it to xLog.
3. The Sender sends xLog through the network to the peer node.
4. The peer Receiver analyzes the xLog and applies it to its database through the Applier.

Every table included in a replication configuration must have a primary key. A replication object can include multiple tables, and multiple networks can be configured for replication stability.

The Sender creates xLog from change transaction logs:

| Transaction | Sender log contents |
| --- | --- |
| `INSERT` | Table, column value |
| `UPDATE` | Table, primary key, before value, after value |
| `DELETE` | Table, primary key |

The xLog carries enough information to find the table, primary key, and column on the receiving node and to compare the current receiver-side value against the transmitted before value.

The Sender uses Lazy mode by default. Lazy mode does not wait for the peer node to apply the transaction, so local change processing is not blocked by replication. Eager mode waits until the transaction is applied on the peer node.

The Receiver sends received xLog to the Applier. Because the xLog came from a transaction log already processed by QueryProcessor on the peer node, the Applier requests storage-manager processing without separate QueryProcessor validation. Before applying a change, the receiving node checks that the xLog before value matches the current local value.

After applying data, the Receiver sends an acknowledgment to the peer Sender. The Sender records both the log position being sent and the retransmission position to use after transmission failure or peer-node failure. When network communication is restored, the Sender reconnects to the Receiver and resumes from the recorded retransmission position.

Replication can introduce two broad problem categories:

| Problem | Source meaning |
| --- | --- |
| Data conflict | Two or more nodes change the same primary key to different values, or an xLog cannot be applied because the receiving row state differs. |
| Data transmission gap | Local transaction logs are generated faster than xLog can be transmitted and applied on the peer node. |

Conflict types from the source set:

| Conflict type | Condition |
| --- | --- |
| `Dup Conflict` or `INSERT Conflict` | A row with the same primary key already exists on the receiving node. |
| `Update Conflict` | The target row does not exist, or the current receiver-side value does not match the transmitted before value. |
| `Not Found Conflict` or `DELETE Conflict` | A row needed for `UPDATE` or `DELETE` by primary key does not exist on the receiving node. |

The safest conflict-prevention design is to avoid `INSERT`, `UPDATE`, and `DELETE` on the same key value from both servers. The source examples recommend separating primary key ranges, such as odd sequence values on one server and even sequence values on the other, or using one node for changes and another for retrieval only.

Altibase provides conflict-related options, but they do not remove the need for conflict-aware service design:

| Method or property | Source behavior |
| --- | --- |
| `REPLICATION_UPDATE_REPLACE=1` | Apply a received `UPDATE` even when the transmitted before value differs from the receiver's current value. |
| `REPLICATION_INSERT_REPLACE=1` | For same-key insert conflict, delete the existing row and insert the received row. |
| User-oriented scheme | Insert and delete conflicts are not reflected and conflict errors are logged; update reflection follows `REPLICATION_UPDATE_REPLACE`. |
| Master / Slave scheme | Master ignores insert/update/delete conflicts; Slave deletes existing data and inserts for insert conflict, applies update conflict unconditionally, and ignores delete conflict. |
| Timestamp-based scheme | With `REPLICATION_TIMESTAMP_RESOLUTION=1`, a timestamp column in every replicated table is used so the latest value wins; both servers must have synchronized time. |

The configuration guide also names the Master / Slave method and TimeStamp method as Altibase conflict-handling functions. Choose the method based on service design, not as a substitute for preventing same-primary-key writes.

Replication gap is the unsent or unapplied log backlog between local transaction log generation and peer apply progress. If a Sender cannot send local transaction logs, Altibase keeps the logs required for replication. If that condition persists, online log files can accumulate and fill the disk.

`REPLICATION_MAX_LOGFILE` can limit how many redo log files replication retains. If retained redo logs exceed the configured threshold, replication GIVE-UP can delete redo logs required for incomplete replication to avoid Active Server disk-full failure. This prevents disk-full escalation but can create data inconsistency and requires follow-up consistency work.

Off-Line Replicator is available from Altibase `v5.3`. When an active server fails before transmitting all logs, the healthy server can create an Off-Line Replicator to read the failed node's transaction log files directly and apply missing data locally. To use it, either configure shared disk equipment so every node can write its own transaction logs to disk shared with the failed server, or copy the failed server's logs by FTP or an equivalent transfer method before apply.

An HA solution configuration has one service node and one standby node. The HA solution periodically checks the service node and switches shared disk access to the standby node on failure. In this configuration:

1. Altibase on the standby node cannot be running; it must be shut down.
2. After switchover, Altibase must start up. Memory DB usage and large in-flight work increase startup and recovery time.
3. Shared disk normally contains transaction log files and data files.
4. Each node keeps its own Altibase engine, trace log files, license, and property file.

Because the HA solution pattern described in the source does not use network replication during switchover, data conflict and replication gap do not need to be considered for that switchover. This is distinct from an Active/Standby replication configuration where both Altibase engines are running from the service perspective.

Lazy mode and Eager mode have different answer implications:

| Mode | Source meaning | Use when |
| --- | --- | --- |
| Lazy | The sending node does not wait for xLog transmission or peer apply progress. | The workload can tolerate temporary replication delay and needs better local performance. |
| Eager | The sending node first applies locally, sends xLog, and waits for the peer apply result. | The workload cannot tolerate replication delay and can accept lower performance. |

Lazy/Eager mode can be specified per session, so different task classes can use different modes. The source example assigns account balance or deposit work to Eager mode and login-time information to Lazy mode. Unlike Lazy mode, Eager mode also fails the local transaction when a conflict occurs.

An Active/Standby replication design that handles all services on one side and uses Off-Line Replicator before service switch can solve the source-described data inconsistency and delay problem:

| Situation | Node A | Node B |
| --- | --- | --- |
| Normal service | Processes all services. | Receives replication logs only and remains standby from the service perspective. |
| Failure occurs | Fails and requires recovery. | Applies Node A transaction logs not yet received with Off-Line Replicator, then starts service. |
| Node A recovery | Receives all replication logs from Node B after the failure to match data. | Automatically detects Node A recovery and transmits logs after the failure through replication. |

Altibase supports N-way replication. One node can connect to up to `32` peer nodes. In three-or-more-node designs, each node must have a Sender and Receiver for each target connection. For example, node A must have replication objects for A-B and A-C, and node B needs B-A and B-C objects for normal synchronization among A-B-C. Plan network-card expansion before deploying N-way replication.

Parallel Applier improves replication performance by creating multiple appliers in the storage manager. It distributes xLog from the Sender to appliers by transaction unit and executes DML in parallel. It is suitable for workloads with long transactions. If many replicated transactions are short, performance can decrease because commit synchronization happens frequently.

Sequence replication lets a remote server and local server use the same sequence after fail-over, preserving application source compatibility. It replicates the cache start value so sequence values do not overlap. Altibase replication supports only tables, so Altibase internally creates a table for sequence replication.

Sequence replication constraints from the constraints guide:

- Sequence replication is not supported in Active-Active environments.
- Larger sequence cache sizes improve generation speed.
- During failover, a gap equivalent to the cache size can occur on the remote server.
- When recreating replication or modifying sequences, all servers must apply changes consistently.
- The guide recommends incrementing sequences by `2`, with one server using odd values and the other using even values. In 4-way replication, design the sequence together with a server-specific unique ID.

Core replication configuration constraints:

| Area | Constraint |
| --- | --- |
| Primary key | All replicated tables require primary keys. Primary key values must not be updated. |
| LOB | LOB columns cannot be used as primary keys or unique keys. |
| Column metadata | Column definitions, primary keys, and `NOT NULL` constraints must match on both sides. If column counts or definitions differ, replication setup can succeed, but synchronization occurs only for matching columns. |
| xLog size | Memory tables have no size limit on generated xLog; for disk tables, one row's xLog must be less than `128 KB`. |
| Connections | A maximum of `32` replication connections can be established per database. |
| Character set | From Altibase `v5.3.3`, replication target databases must have the same character set and national character set to connect. |
| Non-replicated columns | During replicated `INSERT`, unmatched columns become `NULL`; a unique index that combines replicated and non-replicated columns can allow creation but fail at runtime. |
| Partitioned tables | Partitioning method must match. Range/list partition criteria must be identical. Hash partition count must match. |
| DDL | By default, DDL is not allowed while replication is running. Selected DDL can run during replication if `Replication_ddl_enable` is set to `1`. |

DDL statements permitted by the constraints guide when `Replication_ddl_enable = 1`:

- `ADD/DROP Column`
- `ALTER Column`
- `TRUNCATE Table/Partition`
- `CREATE/DROP Index`
- `CREATE/DROP Trigger`

Altibase does not support full Active-Active replication where the same data, tables, or rows are written actively on both nodes at the same time. Use Cross Active-Active, workload separation, or primary-key separation to avoid conflicts.

If a primary key value must change in a replication environment, implement it as delete of the existing record followed by insert of a new one.

When memory and disk tables are in the same replication object, slower disk-table transaction processing can delay the whole replication apply path. If the workload does not require strict apply ordering between memory and disk tables, separate them into memory-table and disk-table replication objects.

Use a dedicated replication line separate from the service network. The replication configuration guide recommends bandwidth of `1G` or higher and two or more dedicated LAN cards for replication stability.

## Procedures

### Design replication and HA before creating objects

1. Decide whether the service needs Active/Active, Cross Active-Active, Active/Standby replication, or an HA solution using shared disk.
2. Identify which data can be changed by which node. Prevent same-primary-key changes from multiple nodes unless a source-supported conflict method is explicitly part of the design.
3. Decide Lazy or Eager mode by workload. Use Eager only where the workload requires no replication delay and can accept the performance cost.
4. If using Active/Standby replication and failure switchover, design how Off-Line Replicator will access the failed node's transaction logs.
5. Confirm every replicated table has a primary key and that peer tables have matching column definitions, primary key, and `NOT NULL` constraints.
6. Check character set and national character set compatibility for Altibase `v5.3.3` or later.
7. Separate memory-table and disk-table replication objects when apply ordering between them is not important.
8. Size log disk capacity for the expected failure-recovery window. Do not rely on GIVE-UP as routine operation.
9. Use a dedicated replication network, preferably `1G` or higher, and consider multiple dedicated LAN cards.

### Enable the replication function

Replication is disabled when `REPLICATION_PORT_NO` is `0`. Check it:

```sql
SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME = 'REPLICATION_PORT_NO';
```

Before assigning a replication port, verify that the target server is not already listening on it:

```bash
netstat -an | grep 30300 | grep LISTEN
```

If `LISTEN` appears, the port is already used and cannot be used as the replication port.

Edit `$ALTIBASE_HOME/conf/altibase.properties` on each replication target server:

```bash
cd $ALTIBASE_HOME/conf
vi altibase.properties
```

Set the port:

```text
REPLICATION_PORT_NO = 30300
```

Restart Altibase because enabling replication requires a server restart:

```bash
server restart
```

If application access must be blocked while creating replication objects, the FAQ says to change the Altibase service port and restart:

```bash
export ALTIBASE_PORT_NO=20400
server restart
```

After startup, verify the replication port and property:

```bash
netstat -an | grep 30300 | grep LISTEN
```

```sql
SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME = 'REPLICATION_PORT_NO';
```

### Create replication objects

Replication objects are created with `CREATE REPLICATION`. They define replication mode, remote server information, and replication target tables. Two servers to be replicated are paired, and each paired server must create a replication object with the same object name.

Syntax shape from the FAQ:

```sql
CREATE REPLICATION replication_name
WITH remote_host_ip, remote_replication_port_no
FROM user_name.table_name TO user_name.table_name,
FROM ...
;
```

For two target servers A and B:

- Server A: `192.168.1.112`, replication port `25524`
- Server B: `192.168.1.113`, replication port `35524`
- Replication object: `REP1`
- Target tables: `sys.employees`, `sys.departments`

Create on server A:

```sql
CREATE REPLICATION rep1 WITH '192.168.1.113', 35524
FROM sys.employees TO sys.employees,
FROM sys.departments TO sys.departments;
```

Create on server B:

```sql
CREATE REPLICATION rep1 WITH '192.168.1.112', 25524
FROM sys.employees TO sys.employees,
FROM sys.departments TO sys.departments;
```

Check host and table metadata:

```sql
SELECT REPLICATION_NAME, HOST_IP, PORT_NO FROM SYSTEM_.SYS_REPL_HOSTS_;
SELECT REPLICATION_NAME, LOCAL_USER_NAME, LOCAL_TABLE_NAME FROM SYSTEM_.SYS_REPL_ITEMS_;
```

For three target servers A, B, and C:

- A synchronizes with B and C.
- B synchronizes with A and C.
- C synchronizes with A and B.
- Objects are `REP_A_B`, `REP_B_C`, and `REP_C_A`.
- A is `192.168.1.112:30300`, B is `192.168.1.113:30300`, and C is `192.168.1.114:30300`.

Create on server A:

```sql
CREATE REPLICATION rep_a_b WITH '192.168.1.113', 30300 FROM sys.employees TO sys.employees, FROM sys.departments TO sys.departments;
CREATE REPLICATION rep_c_a WITH '192.168.1.114', 30300 FROM sys.employees TO sys.employees, FROM sys.departments TO sys.departments;
```

Create on server B:

```sql
CREATE REPLICATION rep_a_b WITH '192.168.1.112', 30300 FROM sys.employees TO sys.employees, FROM sys.departments TO sys.departments;
CREATE REPLICATION rep_b_c WITH '192.168.1.114', 30300 FROM sys.employees TO sys.employees, FROM sys.departments TO sys.departments;
```

Create on server C:

```sql
CREATE REPLICATION rep_c_a WITH '192.168.1.112', 30300 FROM sys.employees TO sys.employees, FROM sys.departments TO sys.departments;
CREATE REPLICATION rep_b_c WITH '192.168.1.113', 30300 FROM sys.employees TO sys.employees, FROM sys.departments TO sys.departments;
```

Check each server with:

```sql
SELECT REPLICATION_NAME, HOST_IP, PORT_NO FROM SYSTEM_.SYS_REPL_HOSTS_;
SELECT REPLICATION_NAME, LOCAL_USER_NAME, LOCAL_TABLE_NAME FROM SYSTEM_.SYS_REPL_ITEMS_;
```

### Start replication and verify sender and receiver

Starting replication starts data synchronization. The server that executes `ALTER REPLICATION ... START` runs the Sender thread, and the paired remote server runs the Receiver thread. The server where change transactions occur is the active server. If both paired servers perform changes and synchronize in both directions, both become active servers.

Start the Sender:

```sql
ALTER REPLICATION replication_name START;
```

Check the replication object start status:

```sql
SELECT REPLICATION_NAME, DECODE(IS_STARTED, 0, 'STOPPED', 1, 'STARTED') IS_STARTED
  FROM SYSTEM_.SYS_REPLICATIONS_;
```

Check Sender status:

```sql
SELECT REP_NAME, DECODE(STATUS, 0, 'STOP', 1, 'START', STATUS) STATUS
  FROM V$REPSENDER;
```

Check Receiver status:

```sql
select REP_NAME, MY_IP, MY_PORT FROM V$REPRECEIVER;
```

### Delete a replication object

Stop replication first:

```sql
ALTER REPLICATION replication_name STOP;
```

Drop the replication object:

```sql
DROP REPLICATION replication_name;
```

### Add a replication target table

This FAQ applies to Altibase `4.3.9` or later.

Stop the replication object on the server where the Sender thread is running. This stops the local Sender and remote Receiver:

```sql
ALTER REPLICATION replication_name STOP;
```

Verify the running status:

```sql
SELECT REPLICATION_NAME, DECODE(IS_STARTED, 0, 'STOPPED', 1, 'STARTED') IS_STARTED
  FROM SYSTEM_.SYS_REPLICATIONS_;
```

Add the target table on each replication target server:

```sql
ALTER REPLICATION replication_name ADD TABLE FROM user_name.table_name TO user_name.table_name;
```

Check the target table list:

```sql
SELECT REPLICATION_NAME, LOCAL_USER_NAME, LOCAL_TABLE_NAME
  FROM SYSTEM_.SYS_REPL_ITEMS_;
```

If the peer table data does not match, truncate one side and run `SYNC` from the server that has the correct data:

```sql
ALTER REPLICATION replication_name SYNC ONLY TABLE user_name.table_name;
```

If the data already matches, start replication:

```sql
ALTER REPLICATION replication_name START;
```

### Delete a replication target table

Stop the replication object:

```sql
ALTER REPLICATION replication_name STOP;
```

Remove the table from the replication object on each replication target server:

```sql
ALTER REPLICATION replication_name DROP TABLE FROM user_name.table_name TO user_name.table_name;
```

Check the target table list:

```sql
SELECT REPLICATION_NAME, LOCAL_USER_NAME, LOCAL_TABLE_NAME
  FROM SYSTEM_.SYS_REPL_ITEMS_;
```

Start replication again:

```sql
ALTER REPLICATION replication_name START;
```

### Change a replication object's IP address

Stop the replication object:

```sql
ALTER REPLICATION replication_name STOP;
```

Add the new host IP and replication port:

```sql
ALTER REPLICATION replication_name ADD HOST 'new_ip_address', replication_port;
```

Remove the existing host IP and replication port:

```sql
ALTER REPLICATION replication_name DROP HOST 'old_ip_address', replication_port;
```

Start replication:

```sql
ALTER REPLICATION replication_name START;
```

Check host metadata:

```sql
SELECT REPLICATION_NAME, HOST_IP, PORT_NO
  FROM SYSTEM_.SYS_REPL_HOSTS_
 ORDER BY HOST_NO;
```

### Create multiple replication objects with the same IP and port

Before Altibase `6.5.1`, creating multiple replication objects with the same remote IP and port can fail:

```sql
CREATE REPLICATION REP1 WITH '192.168.1.145', 30300 FROM ALTITEST.REP_TEST_T TO ALTITEST.REP_TEST_T;
CREATE REPLICATION REP2 WITH '192.168.1.145', 30300 FROM ALTITEST.REP_TEST_T2 TO ALTITEST.REP_TEST_T2;
```

Source error:

```text
[ERR-6110C : Replication hosts already exist.]
```

From Altibase `6.5.1`, use `REPLICATION_ALLOW_DUPLICATE_HOSTS` to allow different replication objects to use the same host information.

Check the property:

```sql
set linesize 1024
set colsize 60
SELECT NAME, VALUE1 FROM V$PROPERTY WHERE NAME = 'REPLICATION_ALLOW_DUPLICATE_HOSTS';
```

If it is `0`, change it to `1`:

```sql
ALTER SYSTEM SET REPLICATION_ALLOW_DUPLICATE_HOSTS = 1;
```

Persist it:

```bash
cd $ALTIBASE_HOME/conf
vi altibase.properties
```

```text
REPLICATION_ALLOW_DUPLICATE_HOSTS     = 1
```

Then create the objects:

```sql
CREATE REPLICATION REP1 WITH '192.168.1.145', 30300 FROM ALTITEST.REP_TEST_T TO ALTITEST.REP_TEST_T;
CREATE REPLICATION REP2 WITH '192.168.1.145', 30300 FROM ALTITEST.REP_TEST_T2 TO ALTITEST.REP_TEST_T2;
```

### Perform DDL on a replicated table during service outage

DDL operations are not replicated because DDL-like operations are not sent through the replication log. Each node needs a separate DDL operation method.

When all services accessing the database can be stopped for a period:

1. Stop the service or otherwise prevent transactions. To block service reliably, the FAQ says the DB may be stopped, the service port changed, and the DB started again before work.
2. Check connected sessions and running statements:

```sql
select count(*) from v$session;
select count(*) from v$statement where execute_flag =1 ;
```

3. Check the replication object containing the target table:

```sql
select REPLICATION_NAME, LOCAL_USER_NAME, LOCAL_TABLE_NAME
  from SYSTEM_.SYS_REPL_ITEMS_;
```

4. Check that all target-node replication gaps are `0` on the DB where the Sender is running:

```sql
SELECT rep_name, rep_gap FROM v$repgap;
```

5. Stop the target replication object:

```sql
ALTER REPLICATION rep_name STOP;
```

6. Remove the target table from the replication object:

```sql
ALTER REPLICATION rep_name DROP TABLE FROM user_name.table_name TO user_name.table_name;
```

7. Perform the DDL operation:

```sql
ALTER TABLE t1 ADD COLUMN ( c1 INTEGER);
```

8. Add the table back to the replication object:

```sql
ALTER REPLICATION rep_name ADD TABLE FROM user_name.table_name TO user_name.table_name;
```

9. Start replication:

```sql
ALTER REPLICATION rep_name START;
```

10. Restart service. If the DB service port was changed, restore the service port and restart the database before checking DB status.

For an uninterrupted-service environment, the FAQ says more steps and extra caution are required, often working one node at a time while the DB operates. Use the manual for the target Altibase version and get Altibase Technical Support guidance.

### Handle bulk changes in replicated environments

Replication sends transaction-log-based changes, not the SQL text. Bulk changes can produce a large transaction-log volume and delay reflection on peer nodes.

Use one of the source-recommended approaches:

1. Divide the work into small batches by using a `LIMIT` clause.
2. Run the same change on all nodes after setting the session not to replicate its logs:

```sql
ALTER SESSION SET REPLICATION = FALSE;
```

Use the second approach only when the same change is applied on all relevant nodes and the operational design permits the session's changes not to be sent through replication.

## SQL, commands, and configuration

Replication setup and operation depends on these exact properties, views, logs, and SQL forms:

| Identifier | Type | Source use |
| --- | --- | --- |
| `REPLICATION_PORT_NO` | Property | Enables replication and defines the port used between replication threads. Default `0` disables replication. Restart required after changing in `altibase.properties`. |
| `REPLICATION_ALLOW_DUPLICATE_HOSTS` | Property | From Altibase `6.5.1`, allows different replication objects to use the same host information when set to `1`. |
| `REPLICATION_MAX_LOGFILE` | Property | Limits the number of redo log files replication can retain before GIVE-UP. Unit is number of redo log files. |
| `REPLICATION_SENDER_START_AFTER_GIVING_UP` | Property | Controls whether replication restarts after GIVE-UP; default is `1`. |
| `REPLICATION_UPDATE_REPLACE` | Property | Applies a received `UPDATE` even when before-image values differ when set to `1`. |
| `REPLICATION_INSERT_REPLACE` | Property | For insert conflict, delete then insert when set to `1`; do not insert and log conflict when set to `0`. |
| `REPLICATION_TIMESTAMP_RESOLUTION` | Property | Timestamp-based conflict resolution uses value `1` and requires timestamp columns on all replicated tables. |
| `Replication_ddl_enable` | Property name as written in source | Allows selected DDL during running replication when set to `1`. |
| `REPLICATION_GAP_UNIT` | Property | Unit used to display `REP_GAP` in Altibase version 7 and later; default unit is `1 MB`. |
| `RP_MSGLOG_FLAG` | Property | With value `6`, outputs conflicting table and SQL information to `$ALTIBASE_HOME/trc/altibase_rp_conflict.log`. |

Replication metadata and monitoring views:

| Identifier | Use |
| --- | --- |
| `SYSTEM_.SYS_REPLICATIONS_` | Replication object metadata including `REPLICATION_NAME`, `IS_STARTED`, `XSN`, and `GIVE_UP_TIME`. |
| `SYSTEM_.SYS_REPL_HOSTS_` | Registered host IP and port for replication objects. |
| `SYSTEM_.SYS_REPL_ITEMS_` | Replication object target table metadata. |
| `V$PROPERTY` | Property value checks, including `REPLICATION_PORT_NO` and `REPLICATION_ALLOW_DUPLICATE_HOSTS`. |
| `V$REPSENDER` | Sender status, peer IP/port, network status, replication mode, and `XSN`. |
| `V$REPRECEIVER` | Receiver status and peer/local IP and port. |
| `X$REPRECEIVER` | Receiver detail query source used by the monitoring FAQ for `APPLY_XSN`. |
| `V$REPGAP` | Replication gap monitoring. |
| `V$SESSION` | Session-count check before DDL work. |
| `V$STATEMENT` | Running statement check before DDL work. |

Set `RP_MSGLOG_FLAG`:

```sql
alter system set RP_MSGLOG_FLAG = 6 ;
```

Check overall replication status:

```sql
set linesize 1024
set colsize 20
SELECT a.replication_name rep_name
     , d.host_ip || decode(d.host_ip, b.peer_ip, ' (*)', NULL) peer_ip
     , nvl(to_char(e.rep_gap), '-') as rep_gap
     , a.xsn restart_xsn
     , decode(b.peer_port, NULL, 'OFF', 'ON') as sender
     , decode(c.peer_port, NULL, 'OFF', 'ON') as receiver
  FROM system_.sys_repl_hosts_ d
     , system_.sys_replications_ a
       left outer join v$repsender b on a.replication_name = b.rep_name
       left outer join v$repreceiver c on a.replication_name = c.rep_name
       left outer join
       (select rep_name, max(rep_gap) rep_gap from v$repgap group by rep_name) e
       on a.replication_name = e.rep_name
 WHERE a.replication_name = d.replication_name
 ORDER BY rep_name;
```

`restart_xsn` is the serial number reflected by the remote server and the retransmission start point when replication restarts. `sender` and `receiver` show whether the Sender and Receiver are running.

Check Sender information:

```sql
set linesize 1024
set colsize 20
SELECT trim(REP_NAME) as REP_NAME
     , decode(START_FLAG, 0, 'Normal',
                          1, 'Quick',
                          2, 'Sync',
                          3, 'Sync Only') as START_FLAG
     , decode(net_error_flag, 0, 'OK', 'Error') as NET_ERROR_FLAG
     , decode(STATUS, 0, 'Stop', 1, 'Run', 2, 'Retry') as STATUS
     , peer_ip
     , peer_port
     , XSN
  FROM V$REPSENDER;
```

Important Sender columns:

| Column | Meaning |
| --- | --- |
| `rep_name` | Replication object name. |
| `peer_ip` | Remote server IP address. |
| `peer_port` | Remote server replication port. |
| `STATUS` | `STOP(0)`, `RUN(1)`, or `RETRY(2)`; `1` is normal. |
| `repl_mode` | Sender replication mode: Lazy or Eager. |
| `NET_ERROR_FLAG` | Network error state; `0` is normal, `1` is error. |
| `XSN` | Last redo log serial number sent by the Sender; same as `REP_SN` in `V$REPGAP`. |

Check Receiver information:

```sql
set linesize 1024
set colsize 20
SELECT trim(REP_NAME)
     , trim(MY_IP)
     , trim(PEER_IP)
     , MY_PORT
     , PEER_PORT
     , apply_xsn
  FROM X$REPRECEIVER;
```

Important Receiver columns:

| Column | Meaning |
| --- | --- |
| `peer_ip` | Remote server IP address. |
| `peer_port` | Remote server replication port. |
| `apply_xsn` | Serial number currently being applied by the Receiver. |

Check replication gap on Altibase versions earlier than `7`:

```sql
set linesize 1024
set colsize 20
select rep_name
     , rep_gap
  from v$repgap;
```

For versions earlier than `7`, `REP_GAP` is the interval between `REP_LAST_SN` and `REP_SN`, meaning:

```text
rep_gap = rep_last_sn - rep_sn
```

Check replication gap on Altibase version `7` and later:

```sql
set linesize 1024
set colsize 20
select rep_name
     , rep_gap
     , rep_gap_size
  from v$repgap;
```

From Altibase version `7`, `REP_GAP_SIZE` shows the replication gap in bytes, and `REP_GAP` displays the gap in the unit configured by `REPLICATION_GAP_UNIT`:

```text
REP_GAP = CEIL(REP_GAP_SIZE / REPLICATION_GAP_UNIT)
```

Default unit is megabytes because `REPLICATION_GAP_UNIT` defaults to `1 MB`.

## Validation and troubleshooting

### Validate replication setup

After enabling replication and creating objects, validate:

1. `REPLICATION_PORT_NO` is nonzero on every target server.
2. `netstat -an | grep <port> | grep LISTEN` shows the expected replication port on each server.
3. `SYSTEM_.SYS_REPL_HOSTS_` lists the expected remote IP and port.
4. `SYSTEM_.SYS_REPL_ITEMS_` lists every replicated table.
5. `SYSTEM_.SYS_REPLICATIONS_` shows the expected `IS_STARTED` state.
6. `V$REPSENDER` has `STATUS` `1` or `Run` for the active Sender.
7. `V$REPRECEIVER` or `X$REPRECEIVER` shows Receiver activity on the paired server.
8. `V$REPGAP` is stable and near zero for normal steady-state operation.

### Investigate replication gap growth

When replication gap increases significantly, check:

- Network status, including maintenance, failures, or IP/port blocking by firewalls.
- Remote system status, including hardware failure or remote database shutdown.
- Whether bulk DML operations are running.
- Whether a Sender remains stopped after it started at least once.
- Whether log disk capacity is sufficient for the expected recovery window.

If the Sender remains stopped, Altibase retains the logs that the Sender must send. Without monitoring, transaction logs can continue to increase and cause disk-full failure.

### Interpret and respond to GIVE-UP

GIVE-UP applies to ALTIBASE HDB version `6.1.1` and later.

Redo log cleanup occurs during checkpoint. Redo log files cannot be deleted when:

1. They are referenced by ongoing transactions.
2. They are no longer used by active transactions but are required for replication because transfer to the Standby Server has not completed.
3. They are referenced by CLR, or Compensation Log Record, generated during transaction rollback.

If retained redo log files exceed `REPLICATION_MAX_LOGFILE`, Altibase can delete redo logs even though the Standby Server has not completed synchronization. This is replication GIVE-UP. It avoids disk full on the Active Server but can create data inconsistency between Active and Standby servers.

Set the retention threshold in `$ALTIBASE_HOME/conf/altibase.properties`:

```text
REPLICATION_MAX_LOGFILE = 400
```

The unit is the number of redo log files. In this example, more than `400` redo log files retained by replication can trigger GIVE-UP at checkpoint.

`REPLICATION_SENDER_START_AFTER_GIVING_UP` controls what happens after GIVE-UP:

```text
REPLICATION_SENDER_START_AFTER_GIVING_UP = 1  (default)
```

| Value | Behavior |
| --- | --- |
| `0` | `IS_STARTED` in `SYS_REPLICATIONS_` changes to `0`; the restart SN, the `XSN` column in `SYS_REPLICATIONS_`, is initialized to `-1`; replication stops; redo log growth due to replication no longer increases while stopped. |
| `1` | The restart SN updates to the last or largest SN of the current log file and replication resumes from that current point forward. |

Check whether GIVE-UP occurred:

```sql
set vertical on;
select replication_name, is_started, give_up_time
  from SYSTEM_.SYS_REPLICATIONS_;
```

Columns:

| Column | Meaning |
| --- | --- |
| `REPLICATION_NAME` | Replication name. |
| `IS_STARTED` | Whether replication has started: `1` means start and `0` means stop. |
| `GIVE_UP_TIME` | Most recent date and time when replication GIVE-UP occurred. |

### Troubleshoot conflicts

Replication conflicts are logged in trace files. The conflict FAQ examples reference `$ALTIBASE_HOME/trc/altibase_rp.log`. The constraints guide says `RP_MSGLOG_FLAG` writes conflicting table and SQL information to `$ALTIBASE_HOME/trc/altibase_rp_conflict.log`. Preserve the applicable filename when answering from a specific source or version.

Conflict symptoms and examples:

| Conflict | Source condition | Source error examples |
| --- | --- | --- |
| Insert conflict | Same primary key already exists on the receiver. | `ERR-11058(errno=0) The row already exists in a unique index.` |
| Update conflict | Target primary key does not exist or before-image differs. | `ERR-61000(errno=0) The received record is not found in the database.`; `ERR-61035(errno=0) [Receiver] An update conflict encountered.` |
| Delete conflict | Target primary key does not exist on the receiver. | `ERR-610f7(errno=16) [Receiver] Unable to find record in executeDelete() function` |

The conflict FAQ gives this update conflict example:

```text
ERR-610f7(errno=16) [Receiver] Unable to find record in executeUpdate() function
ERR-61000(errno=16) The received record is not found in the database.
UPDATE TEST SET C2 = 20150428 WHERE C1 =1231232 ;
```

The delete conflict example:

```text
ERR-610f7(errno=16) [Receiver] Unable to find record in executeDelete() function
DELETE FROM TEST WHERE C1 = 21987744;
```

A valid insert conflict can occur in business logic that first attempts insert and then updates when duplicate-key SQLCODE is returned:

```text
INSERT INTO TABLE
If (SQLCODE == SQL_DUP_ERROR)
{
UPDATE TABLE ~
}
```

Because rollback information from the failed local insert is recorded in redo log and transmitted, the remote side can log an insert conflict. If the same transaction rolls back remotely, this can be safely ignored, but the source recommends reviewing the application and changing the pattern when possible:

```text
UPDATE TABLE
If (SQLCODE == SQL_NO_DATA)
{
INSERT INTO TABLE
}
```

### Troubleshoot replication object creation and start errors

`ERR-61023`:

```text
ERR-61023 : Replication is disabled
```

Cause: `CREATE REPLICATION` was executed while replication is disabled. Check `REPLICATION_PORT_NO`, set it to a nonzero port in `$ALTIBASE_HOME/conf/altibase.properties`, and restart Altibase.

`ERR-61113`:

```text
ERR-61113 : A replicated table must have a primary key. (user_name.table_name)
```

Cause: the target table in the `FROM` clause does not have a primary key. Create a primary key on the table shown in the error message, then execute `CREATE REPLICATION` again.

`ERR-6100D`:

```text
ERR-6100D : [Sender] Failed to handshake with the peer server (Handshake Process Error)
```

Cause: `ALTER REPLICATION replication_name START` could not handshake with the peer. Check whether the remote server IP and replication port in the `WITH` clause are correct and reachable.

`ERR-6110C`:

```text
ERR-6110C : Replication hosts already exist.
```

Cause: multiple replication objects use the same remote IP and port while duplicate hosts are not allowed. From Altibase `6.5.1`, set `REPLICATION_ALLOW_DUPLICATE_HOSTS = 1` when that design is required.

## Version-specific notes

| Version condition | Source meaning |
| --- | --- |
| Altibase `7.1.0` or later | Basis for the replication configuration guide. |
| Altibase `v5.3` or later | Off-Line Replicator is available. |
| Altibase `v5.3.3` or later | Replication target databases must have the same character set and national character set to connect. |
| Altibase `4.3.9` or later | Replication object create/delete and add/delete target table FAQ procedures apply. |
| Altibase `6.5.1` or later | `REPLICATION_ALLOW_DUPLICATE_HOSTS` permits different replication objects with the same host information. |
| ALTIBASE HDB `6.1.1` and above | Replication GIVE-UP FAQ applies. |
| Earlier than Altibase `7` | `V$REPGAP.REP_GAP` means the interval between `REP_LAST_SN` and `REP_SN`. |
| Altibase `7` and above | `V$REPGAP` includes `REP_GAP_SIZE`; `REP_GAP` is calculated by `REPLICATION_GAP_UNIT`. |

DDL support differs by Altibase version. For DDL statements related to replication, use the manual for the specific target version and the support manual page at `http://support.altibase.com/en/manual`.

## Related errors

| Error | Source context | Action basis |
| --- | --- | --- |
| `ERR-11058(errno=0) The row already exists in a unique index.` | Insert conflict. | Prevent same-key insert across nodes or apply the selected conflict scheme. |
| `ERR-61000(errno=0) The received record is not found in the database.` | Delete or update conflict when target row does not exist. | Check whether peer data diverged and review application write ownership. |
| `ERR-61035(errno=0) [Receiver] An update conflict encountered.` | Update conflict when before-image does not match. | Use service design to prevent conflicts; use `REPLICATION_UPDATE_REPLACE=1` only when business logic allows forced update. |
| `ERR-610f7(errno=16) [Receiver] Unable to find record in executeUpdate() function` | Conflict FAQ update example. | Inspect conflict log and source SQL. |
| `ERR-610f7(errno=16) [Receiver] Unable to find record in executeDelete() function` | Conflict FAQ delete example. | Inspect conflict log and source SQL. |
| `ERR-61023 : Replication is disabled` | `CREATE REPLICATION` while `REPLICATION_PORT_NO` is `0`. | Set `REPLICATION_PORT_NO`, restart, and retry. |
| `ERR-61113 : A replicated table must have a primary key. (user_name.table_name)` | `CREATE REPLICATION` for a table without a primary key. | Create a primary key and retry. |
| `ERR-6100D : [Sender] Failed to handshake with the peer server (Handshake Process Error)` | `ALTER REPLICATION ... START` could not connect to peer. | Check `WITH` IP and port reachability. |
| `ERR-6110C : Replication hosts already exist.` | Duplicate remote host information while duplicate hosts are not allowed. | From `6.5.1`, set `REPLICATION_ALLOW_DUPLICATE_HOSTS=1` if the design requires it. |

## Attachments and external references

Preserved document-format attachments:

- `arch/Home/Altibase Replication Constraints Guide__22643008.md`: `https://docs.altibase.com/download/attachments/19333729/ALTIBASE_%EC%9D%B4%EC%A4%91%ED%99%94_%EC%A0%9C%EC%95%BD%EC%82%AC%ED%95%AD_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1698111415000&api=v2`
- `FAQE/Home/03. Replication/How to create_delete replication objects__16876082.md`: `https://docs.altibase.com/download/attachments/13008990/D24_ALTIBASE_%ED%9A%A8%EC%9C%A8%EC%A0%81%EC%9D%B8_%EC%9D%B4%EC%A4%91%ED%99%94_%EA%B0%80%EC%9D%B4%EB%93%9C1.pdf?version=1&modificationDate=1544508306000&api=v2`
- `FAQE/Home/03. Replication/How to create_delete replication objects__16876082.md`: `https://docs.altibase.com/download/attachments/13008990/D67_ALTIBASE_%EC%9D%B4%EC%A4%91%ED%99%94_%EC%A0%9C%EC%95%BD%EC%82%AC%ED%95%AD_%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1544508306000&api=v2`

Embedded diagrams and screenshots are retained in the source files and registered as `not_document_format` in `llm-reference/coverage/attachment-diagram-register.tsv`. The consolidated topic covers the technical meaning around those images without reconstructing their visual contents.

Important source URLs and external references:

- `https://docs.altibase.com/display/arch/Altibase+Replication+Configuration+Guide`
- `https://docs.altibase.com/display/arch/Altibase+Replication+Constraints+Guide`
- `https://docs.altibase.com/display/FAQE/Causes+and+Solutions+of+Replication+Conflicts`
- `https://docs.altibase.com/display/FAQE/DDL+operation+on+the+table+for+Altibase+replication`
- `https://docs.altibase.com/pages/viewpage.action?pageId=16876094`
- `https://docs.altibase.com/display/FAQE/How+to+change+replication+object+IP`
- `https://docs.altibase.com/display/FAQE/How+to+create+multiple+replication+objects+with+the+same+IP`
- `https://docs.altibase.com/pages/viewpage.action?pageId=16876082`
- `https://docs.altibase.com/display/FAQE/Replication+give-up`
- `https://docs.altibase.com/display/FAQE/Replication+monitoring+query`
- Altibase support portal: `http://support.altibase.com` and `http://support.altibase.com/en/`
- Manual page: `http://support.altibase.com/en/manual`
- GitHub manuals: `https://github.com/ALTIBASE/Documents/tree/master/Manuals/Altibase_7.1/eng`

## Terminology

Keep these terms and identifiers stable in multilingual answers:

- Product and feature names: `Altibase`, `ALTIBASE HDB`, `Replication`, `Off-Line Replicator`, `Parallel Applier`, `HA`, `Fail-over`, `Lazy`, `Eager`, `Cross Active-Active`, `Active/Standby`, `Active/Active`.
- SQL and replication DDL: `CREATE REPLICATION`, `ALTER REPLICATION`, `DROP REPLICATION`, `ALTER REPLICATION replication_name START`, `ALTER REPLICATION replication_name STOP`, `ALTER REPLICATION replication_name SYNC ONLY TABLE user_name.table_name`, `ALTER SESSION SET REPLICATION = FALSE`.
- Properties: `REPLICATION_PORT_NO`, `REPLICATION_ALLOW_DUPLICATE_HOSTS`, `REPLICATION_MAX_LOGFILE`, `REPLICATION_SENDER_START_AFTER_GIVING_UP`, `REPLICATION_UPDATE_REPLACE`, `REPLICATION_INSERT_REPLACE`, `REPLICATION_TIMESTAMP_RESOLUTION`, `REPLICATION_GAP_UNIT`, `RP_MSGLOG_FLAG`, `Replication_ddl_enable`.
- Views and metadata tables: `V$PROPERTY`, `V$REPSENDER`, `V$REPRECEIVER`, `X$REPRECEIVER`, `V$REPGAP`, `V$SESSION`, `V$STATEMENT`, `SYSTEM_.SYS_REPLICATIONS_`, `SYSTEM_.SYS_REPL_HOSTS_`, `SYSTEM_.SYS_REPL_ITEMS_`.
- Logs and paths: `$ALTIBASE_HOME/conf/altibase.properties`, `$ALTIBASE_HOME/trc/altibase_rp.log`, `$ALTIBASE_HOME/trc/altibase_rp_conflict.log`.
- Error codes: `ERR-11058`, `ERR-61000`, `ERR-61035`, `ERR-610f7`, `ERR-61023`, `ERR-61113`, `ERR-6100D`, `ERR-6110C`.
- Exact data-sync vocabulary: `xLog`, `redo log`, `Before Value`, `After Value`, `XSN`, `APPLY_XSN`, `REP_GAP`, `REP_GAP_SIZE`, `REPLICATION_GAP_UNIT`, `GIVE_UP_TIME`.
