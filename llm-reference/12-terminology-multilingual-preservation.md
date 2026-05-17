# Terminology and Multilingual Preservation

## Source paths

- `llm-reference/README.md`
- `llm-reference/source-index.md`
- `llm-reference/00-source-classification.md`
- `llm-reference/01-installation-upgrade-platform.md`
- `llm-reference/02-architecture-storage-concepts.md`
- `llm-reference/03-operation-administration-security.md`
- `llm-reference/04-backup-recovery.md`
- `llm-reference/05-replication-ha.md`
- `llm-reference/06-monitoring-diagnostics.md`
- `llm-reference/07-troubleshooting-error-messages.md`
- `llm-reference/08-sql-performance-tuning.md`
- `llm-reference/09-development-client-api.md`
- `llm-reference/10-application-framework-integration.md`
- `llm-reference/11-migration-conversion-tools.md`
- `LLM_REFERENCE_REVIEW_PLAN.md`
- `KO_EN_DOC_REVIEW_REPORT.md`
- `PASS2_KO_EN_DOC_REVIEW_REPORT.md`
- `source-stabilization/validation-report.md`
- `source-stabilization/source-classification.tsv`
- `source-stabilization/legacy-attachments.tsv`
- `source-stabilization/url-backed-attachments.tsv`
- `llm-reference/coverage/semantic-unit-coverage.tsv`
- `llm-reference/coverage/attachment-diagram-register.tsv`
- `llm-reference/coverage/omissions-and-risks.tsv`

## Source coverage notes

This guide consolidates the `Terminology` sections and source-classification rules from completed `llm-reference/` topic documents. It does not replace the topic documents; it defines the cross-topic preservation rules an LLM must apply when answering in English, Turkish, Arabic, German, French, Thai, Chinese, Japanese, or another user-requested language.

`source-stabilization/source-classification.tsv` classifies the Phase 3 source set as `Korean-source-verified`, `Link-validated Korean-source-verified`, or `English-only source`. English-only auxiliary material must keep an explicit `English-only source` or `english_only_auxiliary` label and must not be described as Korean-source-verified.

`source-stabilization/legacy-attachments.tsv`, `source-stabilization/url-backed-attachments.tsv`, and `llm-reference/coverage/attachment-diagram-register.tsv` define attachment and diagram boundaries. URL-backed source links are preserved as source evidence. Legacy labels without downloadable URLs remain labels only. Unavailable diagrams are recorded and are not reconstructed.

The protected identifier catalog below is a cross-topic glossary. If a topic document contains an additional code-formatted identifier that is not repeated here, apply the same category rule: preserve the exact identifier and translate only the explanatory prose around it.

## Scope and audience

Use this guide when generating or reviewing multilingual Altibase answers from the LLM reference package. It is for answer authors, reviewers, prompt builders, and retrieval workflows that need stable references for commands, SQL, configuration, paths, product names, error codes, APIs, version conditions, attachments, and source labels.

This guide covers translation boundaries, not new Altibase behavior. For procedure details, SQL examples, command syntax, failure analysis, and version-specific operational instructions, use the topic document named in the source path or cross-reference.

## Key facts

- Translate explanatory prose into the user's language, but keep exact technical identifiers in source form.
- Preserve case, punctuation, underscores, dollar signs, slashes, dots, hyphens, parentheses, quotes, percent signs, and wildcard markers when they are part of an identifier, command, SQL literal, path, filename, URL, error code, class name, or output string.
- Keep product names such as `Altibase`, `ALTIBASE`, `ALTIBASE HDB`, and source-specific capitalization exactly as written in the cited document.
- Keep SQL keywords, system views, performance views, metadata tables, properties, environment variables, command names, filenames, paths, Java/.NET/C/C++ identifiers, error codes, and attachment filenames untranslated.
- Put version, OS, license, restart, mode, default-value, output, and failure-condition constraints near the beginning of a sentence so they survive translation.
- Do not collapse source variants. If two source documents give different version boundaries, filenames, values, or examples, keep the source-specific condition instead of normalizing one answer.
- Do not invent missing attachment URLs. For legacy `#` labels, use the wording `no downloadable URL in source`.
- Do not reconstruct unavailable diagrams. Use `diagram_unavailable` and rely on preserved surrounding text.
- Korean filenames, encoded URLs, and Korean sample data are identifiers when they come from the source. Preserve them exactly and translate only the explanation.
- English-only auxiliary source labels are evidence labels, not product features. Preserve `English-only source` and `english_only_auxiliary` exactly.

## Procedures

### Answer in a non-English language

1. Identify the topic document and source classification before answering.
2. Keep every exact identifier in code formatting or as source text.
3. Translate the surrounding explanation into the user's requested language.
4. Place version and platform conditions before the instruction they limit.
5. Keep command blocks, SQL blocks, code samples, output samples, filenames, paths, URLs, and attachment names unchanged.
6. If the answer cites English-only auxiliary material, state `English-only source` near that source-specific claim.
7. If the answer cites a legacy attachment label, state `no downloadable URL in source`.
8. If a diagram is unavailable, state that the source records `diagram_unavailable`; do not infer the visual contents.

### Review a translated answer

1. Scan for translated identifiers that should remain exact, especially uppercase properties, `V$` views, `SYSTEM_.` tables, paths, error codes, class names, and utility names.
2. Check that no source-specific version boundary was softened into a broad statement.
3. Check that `Korean-source-verified`, `Link-validated Korean-source-verified`, and `English-only source` labels are not mixed.
4. Check attachment text against the register before presenting a URL, filename, or legacy label.
5. Check source-variation risks in `llm-reference/coverage/omissions-and-risks.tsv` before reconciling conflicting values.

## SQL, commands, and configuration

### Protected identifier glossary

#### Product names and feature names

Preserve these names exactly:

- `Altibase`
- `ALTIBASE`
- `ALTIBASE HDB`
- `Altibase HDB`
- `Altibase Package Installer`
- `APatch`
- `iSQL`
- `iLoader`
- `iloader`
- `aexport`
- `altiProfile`
- `altimon`
- `Migration Center`
- `MigrationCenter`
- `AdminCenter2`
- `GeoServer`
- `SQuirrel SQL Client`
- `Hybrid Partitioned Table (HPT)`
- `Write Ahead Logging`
- `WAL`
- `MVCC`
- `MVCC Garbage Data`
- `Direct I/O`
- `Buffered I/O`
- `Page Change Tracking`
- `Off-Line Replicator`
- `Parallel Applier`
- `HA`
- `Fail-over`
- `Connection Time Fail-Over`
- `Service Time Fail-Over`
- `CTF`
- `STF`
- `FAC`
- `PBT`
- `DB to DB`
- `DB to File`
- `Reconcile`
- `PL/SQL Converter Tool`
- `Schema = User`
- `Local XA`
- `XA`
- `DBCP`
- `JNDI`
- `SqlMap`
- `Mapper`
- `SessionFactory`
- `LobLocator`
- `AltibaseDialect`

#### Commands, utilities, and shell tools

Keep command names, options, and output examples unchanged:

- Altibase and package utilities: `isql`, `iSQL`, `aexport`, `iloader`, `altimon`, `altiProfile`, `altierr`, `apre`, `sesc`, `sqlcli`, `server create`, `server start`, `server stop`, `server kill`, `altibase -v`, `run_is.sh`, `run_il_out.sh`, `run_il_in.sh`, `run_is_refresh_mview.sh`, `run_is_index.sh`, `run_is_fk.sh`, `run_is_repl.sh`, `run_is_job.sh`, `run_is_alt_tbl.sh`.
- Build and development tools: `make`, `gmake`, `ldd`, `nm`, `man`, `file`, `cc`, `gcc`, `g++`, `xlc_r`, `odbcinst -j`, `dltest`.
- Operating-system commands: `chmod`, `uname -a`, `ifconfig -a`, `/sbin/ifconfig -a`, `netstat -an`, `ps -ef`, `gzip -cd`, `tar xvf`, `regedit.exe`, `rpm -q glibc`, `cpupower`, `tuned-adm`, `udevadm`, `sysctl`, `ipcs`, `ulimit`, `projadd`, `projmod`, `kctune`, `swlist`, `smit`, `smitty chtz_user`, `vmo`, `lsdev`, `instfix`, `pstack`, `procstack`, `dbx`, `gdb`, `svmon`, `glance`, `vmstat`, `free -m`, `top`, `df -k`, `bdf`, `errpt -a`, `iostat`, `dd`, `sed`, `vi`, `tail -f`.
- Docker commands: `docker pull`, `docker images`, `docker build`, `docker run`, `docker network create`, `docker network ls`, `docker inspect`, `docker stop`, `docker ps`, `docker rm`.
- Windows and GUI executables: `migcenter.bat`, `migcenter.sh`, `startup.bat`, `squirrel-sql.jar`, `AdminCenter.exe`, `C:\windows\sysWOW64\odbcad32.exe`.

#### SQL statements, clauses, keywords, and objects

Keep SQL syntax, SQL object names, and source aliases unchanged:

- Startup and shutdown: `startup process`, `startup control`, `startup service`, `STARTUP PROCESS`, `STARTUP CONTROL`, `STARTUP META`, `STARTUP SERVICE`, `STARTUP`, `shutdown abort`, `shutdown immediate`, `shutdown normal`, `SHUTDOWN ABORT`, `SHUTDOWN IMMEDIATE`, `SHUTDOWN NORMAL`, `CONTROL`, `META`, `SERVICE`, `PROCESS`.
- Database and tablespace operations: `create database`, `CREATE DATABASE`, `alter database archivelog`, `drop database`, `CREATE USER`, `ALTER USER`, `DROP USER`, `CREATE MEMORY TABLESPACE`, `CREATE DISK TABLESPACE`, `DROP TABLESPACE`, `ALTER TABLESPACE`, `ALTER SYSTEM CHECKPOINT`, `ALTER SYSTEM`, `ALTER SESSION`, `SESSION CLOSE`.
- Replication DDL: `CREATE REPLICATION`, `ALTER REPLICATION`, `DROP REPLICATION`, `ALTER REPLICATION replication_name START`, `ALTER REPLICATION replication_name STOP`, `ALTER REPLICATION replication_name SYNC ONLY TABLE user_name.table_name`, `ALTER SESSION SET REPLICATION = FALSE`, `CREATE EAGER REPLICATION`, `CREATE REPLICATION rep1 OPTIONS OFFLINE '/data1/logfiles'`, `ALTER REPLICATION rep1 START WITH OFFLINE`.
- SQL and performance clauses: `EXPLAIN PLAN`, `FULL SCAN`, `INDEX SCAN`, `ACCESS`, `KEY`, `FILTER`, `LIMIT`, `PREPARE`, `BIND`, `EXECUTE`, `FETCH`, `SELECT FOR UPDATE`, `WHERE CURRENT OF`, `ROWNUM`, `CONNECT_BY_ISCYCLE`, `WITH READ ONLY`, `WITH CHECK OPTION`, `JOIN UPDATE`, `MERGE`, `GO`, `Commit;`.
- Stored procedure and PSM terms: `Stored Procedure`, `Stored Function`, `Dynamic SQL/DDL`, `SQL%ROWCOUNT`, `showProcedures`, `showProcBody`, `ALL_CRT_PROC.sql`, `user_name_procedure_name_CRT.sql`, `TYPESET`, `REF CURSOR`, `DBMS_OUTPUT.NEW_LINE`, `PUT`, `PUT_LINE`, `PRINT`, `PRINTLN`, `UTL_FILE`.
- Oracle, MSSQL, and conversion terms: `CHAR`, `VARCHAR`, `VARCHAR2`, `NCHAR`, `NVARCHAR`, `NVARCHAR2`, `NUMBER(38)`, `BINARY_FLOAT`, `BINARY_DOUBLE`, `REAL`, `DOUBLE`, `LONG`, `NCLOB`, `CLOB`, `RAW`, `LONG RAW`, `BFILE`, `BLOB`, `DATE`, `TIMESTAMP`, `SDO_GEOMETRY`, `GEOMETRY`, `ROWID`, `UROWID`, `ANY*`, `XMLType`, `FILESTREAM`, `COLLATE`, `IDENTITY`, `ROWGUIDCOL`, `dbo`, `REMOTE_TABLE`, `REMOTE_EXECUTE_IMMEDIATE`.
- SQL functions that must remain exact when cited: `ABS`, `ACOS`, `ASIN`, `ATAN`, `ATAN2`, `BITAND`, `CEIL`, `COS`, `COSH`, `EXP`, `FLOOR`, `LN`, `LOG`, `MOD`, `POWER`, `ROUND`, `SIGN`, `SIN`, `SINH`, `SQRT`, `TAN`, `TANH`, `TRUNC`, `NANVL`, `WIDTH_BUCKET`, `ISNUMERIC`, `NUMAND`, `NUMOR`, `NUMSHIFT`, `NUMXOR`, `RAND`, `RANDOM`, `CHR`, `CONCAT`, `INITCAP`, `LOWER`, `LPAD`, `LTRIM`, `NCHR`, `REGEXP_REPLACE`, `REGEXP_SUBSTR`, `REPLACE`, `REPLACE2`, `RPAD`, `RTRIM`, `SUBSTR`, `TRANSLATE`, `TRIM`, `UPPER`, `CHOSUNG`, `DIGEST`, `DIGITS`, `RANDOM_STRING`, `REPLICATE`, `REVERSE_STR`, `SIZEOF`, `STUFF`, `ADD_MONTHS`, `CURRENT_DATE`, `CURRENT_TIMESTAMP`, `DB_TIMEZONE`, `DBTIMEZONE`, `EXTRACT`, `DATEPART`, `LAST_DAY`, `MONTHS_BETWEEN`, `NEXT_DAY`, `SESSION_TIMEZONE`, `SESSIONTIMEZONE`, `SYSDATE`, `SYSTIMESTAMP`, `DATEADD`, `DATEDIFF`, `DATENAME`, `UNIX_DATE`, `UNIX_TIMESTAMP`, `CONV_TIMEZONE`.

#### System views, performance views, and metadata tables

Preserve exact capitalization, prefixes, and punctuation:

- Dynamic views: `V$VERSION`, `V$PROPERTY`, `V$SESSION`, `V$STATEMENT`, `v$statement`, `V$SQLTEXT`, `V$PLANTEXT`, `V$SERVICE_THREAD`, `V$TRANSACTION`, `V$MEMGC`, `V$LOCK`, `V$LOCK_WAIT`, `V$LOCK_STATEMENT`, `V$TABLESPACES`, `V$MEM_TABLESPACES`, `V$VOL_TABLESPACES`, `V$DATAFILES`, `V$SEGMENT`, `V$MEMTBL_INFO`, `V$DISKTBL_INFO`, `V$INDEX`, `V$LFG`, `v$lfg`, `V$ARCHIVE`, `v$archive`, `V$DATABASE`, `V$BUFFPOOL_STAT`, `V$REPSENDER`, `V$REPGAP`, `V$REPRECEIVER`, `V$REPSENDER_TRANSTBL`, `V$REPRECEIVER_TRANSTBL`, `V$SYSSTAT`, `V$SESSTAT`, `V$NLS_PARAMETERS`, `V$MEMSTAT`, `V$FILESTAT`, `V$MUTEX`, `V$SYSTEM_EVENT`.
- Fixed tables: `X$SEGMENT`, `X$TEMPTABLE_STATS`, `X$DATAFILES`, `X$REPRECEIVER`.
- Metadata tables: `SYSTEM_.SYS_USERS_`, `SYSTEM_.SYS_TABLES_`, `SYSTEM_.SYS_COLUMNS_`, `SYSTEM_.SYS_CONSTRAINTS_`, `SYSTEM_.SYS_CONSTRAINT_COLUMNS`, `SYSTEM_.SYS_INDICES_`, `SYSTEM_.SYS_REPLICATIONS_`, `SYSTEM_.SYS_REPL_HOSTS_`, `SYSTEM_.SYS_REPL_ITEMS_`, `SYSTEM_.SYS_TBS_USERS_`, `SYSTEM_.SYS_PRIVILEGES_`, `SYSTEM_.SYS_GRANT_SYSTEM_`, `SYSTEM_.SYS_GRANT_OBJECT_`, `SYSTEM_.SYS_VIEWS_`, `SYSTEM_.SYS_VIEW_PARSE_`, `SYSTEM_.SYS_PROCEDURES_`, `SYSTEM_.SYS_PROC_PARSE_`, `SYSTEM_.SYS_JOBS_`.

#### Properties, environment variables, and OS settings

Keep property names, environment variables, and setting values exact:

- Core server properties: `DB_NAME`, `PORT_NO`, `MEM_MAX_DB_SIZE`, `BUFFER_AREA_SIZE`, `MEM_DB_DIR`, `DEFAULT_DISK_DB_DIR`, `LOGANCHOR_DIR`, `LOG_DIR`, `ARCHIVE_DIR`, `ARCH_DIR`, `CHECK_LOGFILE`, `STARTUP_SHM_CHUNK_SIZE`, `EXPAND_CHUNK_PAGE_COUNT`, `REPLICATION_PORT_NO`, `IPC_PORT_NO`, `IPC_CHANNEL_COUNT`, `IPC_FILEPATH`, `IPCDA`, `ISQL_CONNECTION=IPC`, `AUTO_COMMIT`, `AUTOCOMMIT`.
- Timeout and session properties: `CONNECTION_TIMEOUT`, `TIMEOUT`, `QUERY_TIMEOUT`, `FETCH_TIMEOUT`, `IDLE_TIMEOUT`, `UTRANS_TIMEOUT`, `UTRANS_TIME`, `DDL_LOCK_TIMEOUT`, `REPLICATION_LOCK_TIMEOUT`, `TRANSACTION_TABLE_SIZE`, `MAX_CLIENT`, `JOB_SCHEDULER_ENABLE`, `JOB_THREAD_COUNT`, `JOB_THREAD_QUEUE_SIZE`.
- Memory, storage, and work-area properties: `VOLATILE_MAX_DB_SIZE`, `TRX_UPDATE_MAX_LOGSIZE`, `LOCK_ESCALATION_MEMORY_SIZE`, `TEMP_MAX_PAGE_COUNT`, `TOTAL_WA_SIZE`, `SORT_AREA_SIZE`, `HASH_AREA_SIZE`, `EXECUTE_STMT_MEMORY_MAXIMUM`, `PREPARE_STMT_MEMORY_MAXIMUM`, `DIRECT_IO_ENABLED`, `DATABASE_IO_TYPE`, `LOG_IO_TYPE`, `COMMIT_WRITE_WAIT_MODE`, `LOG_BUFFER_TYPE`, `HOT_LIST_PCT`, `BUFFER_POOL_SIZE`, `SQL_PLAN_CACHE_SIZE`, `SQL_PLAN_CACHE_BUCKET_CNT`, `SQL_PLAN_CACHE_HOT_REGION_LRU_RATIO`, `SQL_PLAN_CACHE_PREPARED_EXECUTION_CONTEXT_CNT`.
- Performance and diagnostic properties: `TIMED_STATISTICS`, `QUERY_PROF_FLAG`, `QUERY_PROF_LOG_DIR`, `TRCLOG_PREDICATE`, `TRCLOG_DETAIL_PREDICATE`, `PREPARE_LOG_FILE_COUNT`, `MULTIPLEXING_THREAD_COUNT`, `MULTIPLEXING_MAX_THREAD_COUNT`, `MULTIPLEXING_POLL_TIMEOUT`, `CHECKPOINT_BULK_WRITE_PAGE_COUNT`, `CHECKPOINT_BULK_WRITE_SLEEP_SEC`, `CHECKPOINT_BULK_WRITE_SLEEP_USEC`, `CHECKPOINT_BULK_SYNC_PAGE_COUNT`, `AGER_WAIT_MINIMUM`, `AGER_WAIT_MAXIMUM`, `TEMP_TBS_MEMORY`, `PVO`, `PLAN-CACHE`.
- Replication properties: `REPLICATION_ALLOW_DUPLICATE_HOSTS`, `REPLICATION_MAX_LOGFILE`, `REPLICATION_SENDER_START_AFTER_GIVING_UP`, `REPLICATION_UPDATE_REPLACE`, `REPLICATION_INSERT_REPLACE`, `REPLICATION_TIMESTAMP_RESOLUTION`, `REPLICATION_GAP_UNIT`, `RP_MSGLOG_FLAG`, `Replication_ddl_enable`, `REPLICATION_DDL_ENABLE`.
- Security and privilege properties: `FAILED_LOGIN_ATTEMPTS`, `PASSWORD_LOCK_TIME`, `PASSWORD_VERIFY_FUNCTION`, `PASSWORD_LIFE_TIME`, `PASSWORD_GRACE_TIME`, `REMOTE_SYSDBA_ENABLE`, `ACCESS_LIST`, `TRC_ACCESS_PERMISSION`.
- Character-set variables: `ALTIBASE_NLS_USE`, `DATA_NLS_USE`, `NLS_USE`, `NLS_CHARACTERSET`, `NLS_NCHAR_CHARACTERSET`, `client_nls`, `LANG`, `chcp 65001`.
- Utility and export variables: `ILO_DATEFORM`, `ILOADER_FIELD_TERM`, `ILOADER_ROW_TERM`, `ALTIBASE_JDBC_TRCLOG_DISABLE`, `ODBCINI`, `ODBCSYSINI`, `ISQL_BUFFER_SIZE`.
- Environment variables and shell paths: `ALTIBASE_HOME`, `$ALTIBASE_HOME`, `$ALTIBASE_PID`, `ALTIBASE_PORT_NO`, `PATH`, `LD_LIBRARY_PATH`, `LD_LIBRARY_PATH_64`, `SHLIB_PATH`, `CLASSPATH`, `DISPLAY`, `GEOSERVER_HOME`, `GEOSERVER_DATA_DIR`, `$DOMAIN_HOME`.
- Linux and UNIX OS settings: `CPUfreq Governor`, `RemoveIPC`, `vm.swappiness`, `vm.force_cgroup_v2_swappiness`, `memory.swappiness`, `transparent_hugepage`, `transparent_hugepage.defrag`, `vm.max_map_count`, `kernel.shmmni`, `kernel.shmmax`, `kernel.sem`, `shmmax`, `shmmni`, `shmseg`, `semmsl`, `semmns`, `semopm`, `semmni`, `semmap`, `semmnu`, `semume`, `semvmx`, `dbc_min_pct`, `dbc_max_pct`, `filecache_min`, `filecache_max`, `maxdsiz`, `maxdsiz_64bit`, `max_thread_proc`, `maxfiles`, `nproc`, `maxusers`, `minperm`, `lru_file_repage`, `strict_maxclient`, `PTHREAD_FORCE_SCOPE_SYSTEM`, `PERF_ENABLE`, `PTHREAD_FAST_SHARED_OBJECTS`, `PTHREAD_DISABLE_HANDOFF`, `_M_ARENA_OPTS`, `_M_ARENA_OPT`, `PTHREAD_SHARED_MUTEX_OLDSPIN`, `AIXTHREAD_MNRATIO`, `AIXTHREAD_SCOPE`, `AIXTHREAD_MUTEX_DEBUG`, `AIXTHREAD_RWLOCK_DEBUG`, `AIXTHREAD_COND_DEBUG`, `SPINLOOPTIME`, `YIELDLOOPTIME`, `MALLOCMULTIHEAP`, `AIXTHREAD_MUTEX_FAST`, `MALLOC_ARENA_MAX`, `MALOC_ARENA_MAX`, `MALLOC_ARENA_TEST`.

#### Paths, filenames, scripts, and logs

Preserve exact paths and filenames:

- Installation paths: `$ALTIBASE_HOME`, `$ALTIBASE_HOME/APatch`, `$ALTIBASE_HOME/bin`, `$ALTIBASE_HOME/include`, `$ALTIBASE_HOME/lib`, `$ALTIBASE_HOME/conf/altibase.properties`, `$ALTIBASE_HOME/conf/altibase_user.env`, `$ALTIBASE_HOME/conf/license`, `$ALTIBASE_HOME/install/pre_install.sh`, `$ALTIBASE_HOME/install/post_install.sh`, `$ALTIBASE_HOME/install/altibase_env.mk`, `$ALTIBASE_HOME/packages`, `$ALTIBASE_HOME/packages/catproc.sql`, `$ALTIBASE_HOME/sample/APRE`, `$ALTIBASE_HOME/msg/manual.txt`, `$ALTIBASE_HOME/conf/glogin.sql`.
- Data and log paths: `$ALTIBASE_HOME/dbs`, `$ALTIBASE_HOME/logs`, `$ALTIBASE_HOME/arch_logs`, `$ALTIBASE_HOME/trc`, `/ALTIBASE_REDO_LOG`, `/ALTIBASE_MEMORY_DATA`, `/ALTIBASE_DISK_DATA`, `/ALTIBASE_DISK_INDEX`, `/ALTIBASE_DISK_UNDO`, `SYS_TBS_DISK_UNDO`, `dwfile0.dwf`, `dwfile1.dwf`.
- Log files: `$ALTIBASE_HOME/trc/altibase_boot.log`, `altibase_boot.log`, `altibase_cm.log`, `altibase_dk.log`, `altibase_dump.log`, `altibase_error.log`, `altibase_ipc.log`, `altibase_ipcda.log`, `altibase_job.log`, `altibase_lb.log`, `altibase_mm.log`, `altibase_qp.log`, `altibase_rp.log`, `altibase_rp_conflict.log`, `altibase_sm.log`, `altibase_snmp.log`, `altibase_xa.log`, `killCheckServer.log`, `jdbc.trc`, `jdbc.trc.lck`.
- OS paths: `/etc/systemd/logind.conf`, `/etc/sysctl.conf`, `/etc/sysctl.d/99-sysctl.conf`, `/etc/security/limits.conf`, `/etc/system`, `/etc/default/grub`, `/etc/grub.conf`, `/etc/rc.d/rc.local`, `/etc/udev/rules.d/99-cpufreq.rules`, `/home/altibase/docker-entrypoint.sh`, `/home/altibase/set_altibase.env`, `/home/altibase/altibase_home`, `/var/adm/messages.*`.
- Migration and loader files: `.fmt`, `.dat`, `.log`, `.bad`, `ALL_CRT_*`, `ALL_CRT_TBS.sql`, `dbms_metadata.sql`, `dbms_metadata.plb`, `altibase_spatial_ref_sys.sql`, `download.d.out`.
- Development source and generated files: `.sc`, `.c`, `.cpp`, `connect1.sc`, `connect1.c`, `connect1.cpp`, `Testsample.sc`, `altibase_env.mk`, `Makefile`, `db.php`, `odbc.ini`, `odbcinst.ini`.

#### Roles, internal terms, and output fields

Keep Altibase roles, internal components, monitoring IDs, and output aliases stable:

- Replication and HA roles: `Sender`, `Receiver`, `Apply XSN`, `SN`, `XSN`, `APPLY_XSN`, `REP_GAP`, `REP_GAP_SIZE`, `GIVE_UP_TIME`, `restart_xsn`, `sender`, `receiver`, `xLog`, `redo log`, `Before Value`, `After Value`, `Asynchronous(Lazy)`, `Synchronous mode (Eager)`, `Lazy`, `Eager`, `Active/Standby`, `Active/Active`, `Cross Active-Active`.
- Query and storage internals: `Query Processor (QP)`, `Storage Manager (SM)`, `LogSyncThread`, `checkpoint`, `dirty page`, `memory table`, `disk table`, `Flush List`, `LRU`, `BufferReplace`, `undo tablespace`, `Ager`, `FMS`, `TMS`, `Freelist Managed Segment`, `Tree Managed Segment`, `PCTUSED`, `PCTFREE`.
- Monitoring IDs: `ST01` through `ST10`, `SV01`, `SV02`, `TL01`, `LO01`, `LO02`, `GC01`, `GC02`, `MS01`, `MS02`, `TS01` through `TS14`, `DB01`, `OB01` through `OB20`, `PV01` through `PV05`, `CT01` through `CT04`, and `RP01` through `RP06`.
- OS diagnostic fields: `RX-ERR`, `RX-DRP`, `RX-OVR`, `TX-ERR`, `TX-DRP`, `TX-OVR`, `si`, `so`, `sr`, `fr`, `LWP`, `CP`, `tid#`, `lwpid`, `pgsp`, `VSZ`, `STATUS`, `NET_ERROR_FLAG`, `TOTAL(M)`, `ALLOC(M)`, `USED(M)`, `USAGE(%)`, `ADD_OID_CNT`, `GC_OID_CNT`, `MINMEMSCNINTXS`, `MEMORY_VIEW_SCN`, `MIN_MEMORY_LOB_VIEW_SCN`.
- Query phase terms: `Parsing`, `Validating`, `Optimizing`, `Executing`, `Parse Tree`, `Checked Parse Tree`, `Plan Tree`.

#### Error codes, messages, SQL status, and network status

Keep error codes, SQL statuses, errno names, and message text exact when cited:

- Installation and startup errors: `ERR-910FB`, `ERR-91015`, `ERR-91003`, `ERR-9100B`, `ERR-0103C`, `No valid license present!`, `idp checkRange() Error`, `idp convertFromString() Error`, `idp insertBySrc() Error`, `Failed to mmap log file`, `Memory [iduMemMgr :: malloc] failed.`, `Failed to create a thread object.`, `resource temporarily unavailable`, `Too many open files`, `altibase.service start operation timed out. Terminating.`
- Korean-source-verified FAQ errors: `ERR-0109D`, `ERR-11030`, `ERR-11036`, `ERR-11049`, `ERR-1105D`, `ERR-11075`, `ERR-11118`, `ERR-11183`, `ERR-11184`, `ERR-21010`, `ERR-21011`, `ERR-311E0`, `ERR-31283`, `ERR-4103C`, `ERR-41059`, `ERR-4109C`, `ERR-410D2`, `ERR-5102E`, `ERR-71018`, `ERR-71019`, `ERR-7101D`, `ERR-91015`, `ERR-31386`.
- Replication errors: `ERR-11058`, `ERR-61000`, `ERR-61001`, `ERR-61012`, `ERR-61022`, `ERR-61023`, `ERR-61035`, `ERR-61036`, `ERR-6103a`, `ERR-61047`, `ERR-61048`, `ERR-6104b`, `ERR-6100D`, `ERR-610CF`, `ERR-610D2`, `ERR-610a0`, `ERR-610f7`, `ERR-61100`, `ERR-6110C`, `ERR-61113`.
- English-only catalog and troubleshooting errors: `ERR-0001c`, `ERR-01067`, `ERR-0106B`, `ERR-1051`, `ERR-11009`, `ERR-11025`, `ERR-11027`, `ERR-11035`, `ERR-110F0`, `ERR-11107`, `ERR-11123`, `ERR-11136`, `ERR-201436`, `ERR-410D5`, `ERR-51024`, `ERR-51039`, `ERR-51043`, `ERR-5104D`, `ERR-5104F`, `ERR-5105A`, `ERR-51067`, `ERR-51192`, `ERR-71015`, `ERR-91013`, `ERR-91020`, `ERR-9102B`, `ERR-9103D`, `ERR-91044`, `ERR-A100C`, `ERR-A1013`.
- SQL and client statuses: `SQLCODE`, `sqlca.sqlcode`, `SQLSTATE`, `sqlca.sqlerrm.sqlerrmc`, `sqlca.sqlerrd[2]`, `SQL_SUCCESS`, `SQL_NO_DATA`, `SQL_SUCCESS_WITH_INFO`, `08F01`, `ES_08FO01`, `SQLLEN`, `SQLULEN`, `SQLFreeStmt`, `SQL_CLOSE`, `SQL_DROP`, `SQL_UNBIND`, `SQL_RESET_PARAMS`, `SQLBindCol()`, `SQLBindParameter()`.
- Network and OS statuses: `ECONNRESET`, `ETIMEDOUT`, `errno`, `RST packet`, `L4 switch`, `firewall`, `localtime_r()`, `sysdate()`, `TZ`, `KORST-9`, `Asia/Seoul`, `CM_PROTOCOL`, `cm protocol version`.

#### Java, JDBC, ODBC, .NET, C, and C++ identifiers

Keep programming identifiers exact and do not turn them into prose:

- APRE and Embedded SQL: `APRE*C/C++`, `SES*C/C++`, `APRE`, `SES`, `Precompiler of Embedded SQL`, `EXEC SQL`, `DECLARE SECTION`, `ARGUMENT SECTION`, `CONNECT`, `DISCONNECT`, `FREE`, `AUTOCOMMIT`, `COMMIT`, `ROLLBACK`, `DECLARE CURSOR`, `WITH HOLD`, `WHENEVER`, `SQLERROR`, `NOT FOUND`, `-parse none`, `-parse partial`, `-parse full`, `-t c`, `-t cpp`, `-I`, `-D`, `-keyword`, `-unsafe_null`, `-n`.
- Libraries and link flags: `libapre.a`, `libapre_sl.so`, `libodbccli_sl.so`, `libsesc.a`, `libsesc_sl.so`, `-lapre`, `-lodbccli`, `-lsesc`, `-lpthread`, `-lpthreads`, `-lm`, `-ldl`, `-lcrypt`, `-lrt`, `-lstdc++`, `-lC`, `-lCrun`, `-ldemangle`, `-lsocket`, `-lnsl`, `-lunwind`.
- JDBC identifiers: `Altibase.jar`, `Altibase5.jar`, `Altibase6_5.jar`, `Altibase7_3.jar`, `Altibase.jdbc.driver.AltibaseDriver`, `Altibase5.jdbc.driver.AltibaseDriver`, `Altibase7_3.jdbc.driver.AltibaseDriver`, `AltibaseConnectionPoolDataSource`, `ABPoolingDataSource`, `AltibaseXADataSource`, `ABXADataSource`, `AltibaseXAResource`, `ABXAResource`, `PreparedStatement`, `CallableStatement`, `ResultSet`, `DriverManager.getConnection`, `setAutoCommit(false)`, `executeBatch()`, `setFetchSize()`, `setObject(parameterIndex, null, SQLType.NULL)`, `setNull(parameterIndex, null)`.
- JDBC URLs and failover keys: `jdbc:Altibase://ip_address:port_no/db_name`, `jdbc:Altibase://<host>:<port>/<database>`, `jdbc:Altibase_5.6.2://`, `AlternateServer`, `AlternateServers`, `FailOver_Source`, `HealthCheckDuration`, `V$SESSION.FAILOVER_SOURCE`, `SessionFailOver`, `LoadBalance`, `ConnectionRetryCount`, `ConnectionRetryDelay`.
- ODBC and unixODBC identifiers: `ODBC`, `Unix ODBC`, `ALTIBASE_HDB_ODBC_64bit`, `windows.h`, `sql.h`, `sqlext.h`, `afxdb.h`, `odbc32.lib`, `LongDataCompat`, `libaltibase_odbc-64bit-ul32.so`, `libaltibase_odbc-64bit-ul64.so`, `libaltibase_odbc.so`, `BUILD_LEGACY_64_BIT_MODE`, `BUILD_REAL_64_BIT_MODE`.
- ADO.NET identifiers: `ADO.NET`, `Altibase.Data.AltibaseClient.dll`, `odbccli_sl.dll`, `Altibase.Data.AltibaseClient`, `AltibaseConnection`, `AltibaseCommand`, `AltibaseDataReader`, `AltibaseDataAdapter`, `AltibaseTransaction`, `DataSet`, `DTC`, `XA transaction`, `altiadonetX.X.X_32/64bit.zip`, `altiadonetX.X.X.X_32bit.zip`, `altiadonetX.X.X.X_64bit.zip`, `%ALTIBASE_HOME%/lib`, `System.BadImageFormatException`, `System.DllNotFoundException`.
- PHP and framework identifiers: `PHP`, `PERL`, `resource`, `HashTable`, `odbc_connect`, `odbc_exec`, `odbc_prepare`, `odbc_execute`, `odbc_do`, `odbc_fetch_row`, `odbc_result`, `odbc_close`, `memory_limit`, `odbc.defaultbinmode`, `odbc.defaultlrl`, `Spring+iBatis`, `DataSourceTransactionManager`, `TransactionTemplate`, `transactionTemplate.execute()`, `doInTransaction()`, `<tx:advice>`, `TransactionProxyFactoryBean`, `@Transactional(propagation=Propagation.REQUIRED)`, `DefaultAutoCommit`, `SetAutoCommitAllowed`, `AltibaseClobStringTypeHandler`, `org.hibernate.dialect.AltibaseDialect`.

#### Version, platform, and mode conditions

Keep version labels and platform conditions exact. Do not simplify ranges unless the topic document names a canonical duplicate target.

- Product versions: `Altibase 4.3.9`, `Altibase 5.1`, `Altibase 5.3`, `Altibase 5.3.3`, `Altibase 5.5.1`, `Altibase 6.1.1`, `Altibase 6.3.1`, `Altibase 6.5.1`, `Altibase 7`, `Altibase 7.1.0`, `Altibase 7.3`, `Altibase 7.3.0`, `ALTIBASE HDB 4.3.9.x`, `ALTIBASE HDB 5.1.5.x`, `ALTIBASE HDB 5.3.x`, `ALTIBASE HDB V4`, `ALTIBASE HDB V5`, `ALTIBASE HDB 6.3`.
- Patch and compatibility boundaries: `4.3.9.1` through `4.3.9.50`, `4.3.9.51 or later`, `5.1.5.72`, `5.1.5.9.3`, `6.1.1.6.1`, `6.5.1.4.5`, `7.1.0.0.8`, `7.1.0.7.2`, `7.3.0 or later`.
- OS and platform labels: `Oracle Linux 8`, `Red Hat Enterprise Linux 8`, `CentOS 8`, `Rocky Linux 8`, `Ubuntu 18`, `Ubuntu 16`, `Ubuntu 12`, `POWER7`, `POWER8(LE)`, `AIX 5.2 ML03`, `AIX 6.1`, `HPUX 11.23`, `HPUX 11.31`, `Sun OS 5.8`, `Sun OS 5.10`, `RHEL 6`, `RHEL 7`, `RHEL 8`.
- Modes and defaults: `Noarchivelog`, `Archivelog`, `ARCHIVE_MODE`, `RESETLOGS`, `AUTOEXTEND`, `OFF`, `ON`, `RUN(1)`, `STOP(0)`, `RETRY(2)`, `1 MB`, `64 KB`, `32 KB`, `10485760` bytes.

#### Attachments, URLs, and source labels

Keep these labels and rules exact:

- Source classification labels: `Korean-source-verified`, `Link-validated Korean-source-verified`, `English-only source`, `Legacy attachment label only`, `Diagram unavailable`.
- Coverage statuses: `covered`, `covered_by_canonical_duplicate`, `source_index_only`, `legacy_attachment_label_only`, `diagram_unavailable`, `not_document_format`, `english_only_auxiliary`, `recheck_required`, `preserved_url`, `legacy_no_downloadable_url`, `accepted_source_limitation`, `accepted_english_only_auxiliary`.
- Document-format extensions: `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.zip`.
- Non-document-format examples that still remain exact when cited: `.txt`, `.bat`, `.vbs`, `.tar`, `.conf`, `.jar`, `.png`, `.jpg`, `.jpeg`.
- Source domains and links: `docs.altibase.com`, `support.altibase.com`, `support.altibase.com/en/`, `support.altibase.com/en/product`, `manual.altibase.com`, `github.com/ALTIBASE/Documents`, `docs.docker.com`, `hub.docker.com/r/altibase/altibase`, `squirrel-sql.sourceforge.net`, `www.unixodbc.org`.
- Legacy labels and filenames without downloadable URLs: `ALTIBASE_개발가이드.pdf`, `ALTIBASE_개발가이드_5.3.pdf`, `ALTIBASE_Oracle_변환_가이드.pdf`, `ORACLE_to_ALTIBASE_변환_가이드_5.5.pdf`, `APRE_New_Features_업그레이드_가이드.pdf`, `ALTIBASE_MSSQL_변환가이드.pdf`, `total_memory_tablespaces_usage.txt`, `ALTIMON USER GUIDE`.
- URL-backed attachment filenames to preserve exactly include `202312_Altibase_설정_파일_가이드.pdf`, `201003_ALTIBASE_설정_파일_가이드.pdf`, `ALTIBASE_버전별_DB_생성_가이드.pdf`, `ALTIBASE_Quick_Install_Start_for_UNIX.pdf`, `ALTIBASE_설치_시_발생할_수_있는_문제상황과_조치.pdf`, `ALTIBASE_TOMCAT연동_가이드.pdf`, `ALTIBASE_JEUS_연동_가이드.pdf`, `Altibase_개발자교육_v1.pptx`, `D68_Altibase_SQL_Tuning_Guide.pdf`, `ALTIBASE_VC_2008_개발가이드.zip`, `ALTIBASE_ORACLE_비교자료.pdf`, `ALTIBASE_VC_2010_개발가이드.zip`, `Migration Center User Guide 7.12.pdf`, `GeoServer Importer Extension.zip`, `LobSpringIbatisSample.zip`, `altimon_for_windows.zip`, `ALTIMON_USER_GUIDE.pdf`, and `AdminCenter2.zip`.

#### Korean sample data and source-preserved output strings

Preserve sample data and source output strings exactly, even when they contain Korean text or source-level typos:

- `US7ASII_한글테스트합니다`
- `"한글 데이터입니다"`
- `STAUS` when cited as the source-preserved monitoring alias
- `ls --l run_il_out.sh` when cited as a source-preserved command example
- `tail -f download.d.out` when cited as a source-preserved command example
- `./configure -prefix=/home/wonsik/ODBC_HOME --enable-gui=no --enable-threads=yes` when cited as the source-preserved unixODBC configure command

## Validation and troubleshooting

### Multilingual self-review checklist

- Product and feature names remain in original case.
- Commands and SQL examples are not translated.
- `V$`, `X$`, and `SYSTEM_.` object names remain exact.
- Properties and environment variables remain exact.
- Paths retain `$`, `/`, `.`, `_`, and case.
- Error codes remain exact and include the original message when message text is answer-critical.
- Version, platform, restart, license, backup mode, and failure-condition variants are retained.
- English-only auxiliary material is labeled as `English-only source` or `english_only_auxiliary`.
- Legacy labels use `no downloadable URL in source`.
- Diagrams with missing exports are labeled `diagram_unavailable`.
- Korean filenames and sample data are preserved exactly.

### Common translation failures to reject

| Failure | Correct handling |
| --- | --- |
| Translating `Sender` and `Receiver` as generic sender/receiver roles without source context | Keep `Sender` and `Receiver` exact and explain their replication roles in the requested language. |
| Translating `MEM_MAX_DB_SIZE`, `TRANSACTION_TABLE_SIZE`, or `REPLICATION_MAX_LOGFILE` | Keep the property exact and translate only its meaning. |
| Translating `V$SESSION` or `SYSTEM_.SYS_TABLES_` | Keep SQL object names exact. |
| Replacing `$ALTIBASE_HOME` with a localized phrase for installation directory | Keep `$ALTIBASE_HOME`; explain it as the Altibase installation home. |
| Changing `ERR-91015` into localized words only | Keep `ERR-91015` and message text, then explain symptom/cause/action. |
| Turning a Korean attachment filename into a translated English filename | Keep the original filename; optionally add a translated description after it. |
| Presenting an English-only page as Korean-source-verified | Label the claim `English-only source`. |
| Inventing a link for `ALTIBASE_개발가이드.pdf` or `total_memory_tablespaces_usage.txt` | Preserve the label and state `no downloadable URL in source`. |

## Version-specific notes

- Current conversion guidance and legacy Altibase HDB 6.3 conversion guidance can differ. Keep current and legacy source contexts separate.
- Replication gap behavior differs before Altibase `7` and from Altibase `7` onward. Keep `REP_GAP`, `REP_GAP_SIZE`, and `REPLICATION_GAP_UNIT` with the relevant version condition.
- Cursor fetch-across-commit sources preserve different buffer-size details. Keep values tied to the cited source instead of normalizing them.
- CPU optimizer-statistics wording has source-specific version variants. Preserve each scoped wording.
- AIX `PTHREAD_FORCE_SCOPE_SYSTEM` is required by the source, but the source does not provide an exact example value. Do not invent one.
- Disk DB sizing source values include an index header length variation. Preserve the source limitation when exact sizing depends on that value.
- `TRANSACTION_TABLE_SIZE` change behavior, client/server compatibility, and APRE/JDBC/ODBC driver names are version-sensitive. Keep the exact version condition attached to the answer.
- ALTIBASE HDB 5.5.1 or later uses the Java-based `.run` installer, while earlier versions use compressed patch files such as `.tgz`.
- `Altibase 7.3 or later` migration can require installing `DBMS_METADATA` from `$ALTIBASE_HOME/packages` before `aexport` metadata extraction.

## Related errors

The error-code catalog in `llm-reference/07-troubleshooting-error-messages.md` owns detailed cause and action guidance. This guide owns preservation rules:

- Preserve `ERR-` prefixes, uppercase hex digits, embedded decimal codes, underscores, parentheses, and source message text.
- Preserve related properties in the same sentence when they are part of the resolution, for example `MEM_MAX_DB_SIZE`, `TRX_UPDATE_MAX_LOGSIZE`, `TEMP_MAX_PAGE_COUNT`, `TOTAL_WA_SIZE`, `SORT_AREA_SIZE`, `HASH_AREA_SIZE`, `MAX_CLIENT`, `TRANSACTION_TABLE_SIZE`, and `REPLICATION_MAX_LOGFILE`.
- Preserve related files and paths in the same sentence when they are diagnostic evidence, for example `$ALTIBASE_HOME/trc/altibase_boot.log`, `altibase_qp.log`, `altibase_rp.log`, `altibase_error.log`, and `$ALTIBASE_HOME/conf/altibase.properties`.
- Preserve OS errno names and platform-specific numeric mappings when cited, such as `ECONNRESET`, `ETIMEDOUT`, Linux `104`, AIX `73`, HP-UX `232`, SUN `131`, and Windows `10054`.

## Attachments and external references

Attachment and URL preservation is part of answer correctness, not formatting cleanup.

- Preserve original source URLs exactly when the source provides a URL.
- Preserve original filenames exactly, including Korean characters and URL-encoded characters.
- Do not convert a legacy hash label into a downloadable URL.
- For a legacy label, write `no downloadable URL in source`.
- For non-document-format artifacts such as `.txt`, `.bat`, `.vbs`, `.tar`, `.conf`, `.jar`, `.png`, `.jpg`, or screenshots, keep the artifact label exact but do not promote it to the document-format attachment gate.
- For unavailable Gliffy or diagram placeholders, write `diagram_unavailable` and do not describe the unseen diagram.
- Keep `docs.altibase.com` download URLs, `support.altibase.com` product/manual links, GitHub manual links, Docker links, SourceForge links, and manual references unchanged.

## Terminology

- `identifier`: A product name, command, SQL object, property, environment variable, path, filename, URL, error code, class name, method name, option, output alias, or sample literal that must remain exact.
- `translation boundary`: The point where explanatory prose may be translated but exact source identifiers must not change.
- `source classification`: Evidence label such as `Korean-source-verified`, `Link-validated Korean-source-verified`, or `English-only source`.
- `legacy attachment label`: A source label that looks like an attachment but has no downloadable URL in the source.
- `diagram_unavailable`: A source limitation where diagram content is unavailable and must not be reconstructed.
- `not_document_format`: An attachment or artifact outside the `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, and `.zip` preservation gate.
- `source variation`: A preserved source-specific difference in version, value, filename, mode, output, or failure condition.
- `multilingual answer stability`: The requirement that answers remain technically identical even when explanatory language changes.
