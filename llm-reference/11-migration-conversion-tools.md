# Migration, Conversion, and Tools

## Source paths

- `arch/Home/Altibase Data Migration Process Guide__22642994.md`
- `arch/Home/Altibase_Oracle Comparison__16875638.md`
- `arch/Home/ORACLE to ALTIBASE Conversion Guide__22643038.md`
- `arch/Home/Altibase Oracle Conversion Guide__14647316.md`
- `arch/Home/Altibase Oracle Conversion Guide/1. Environment Configuration__14647318.md`
- `arch/Home/Altibase Oracle Conversion Guide/2. Environment Setting__14647320.md`
- `arch/Home/Altibase Oracle Conversion Guide/2. Environment Setting/2-1 Object Conversion__14647322.md`
- `arch/Home/Altibase Oracle Conversion Guide/2. Environment Setting/2-2 SQL Conversion__14647324.md`
- `arch/Home/Altibase Oracle Conversion Guide/2. Environment Setting/2-3 Stored Procedure _ Function Conversion__14647326.md`
- `arch/Home/Altibase Oracle Conversion Guide/3. Conversion Procedure__14647349.md`
- `arch/Home/MSSQL to ALTIBASE Conversion Guide__22643024.md`
- `arch/Home/Migration Center User Guide__19955861.md`
- `arch/Home/Altibase VC 2008 Development Guide__19333567.md`
- `arch/Home/Altibase VC 2010 Development Guide__19334121.md`
- `arch/Home/Altibase GeoServer Integration Guide__22643004.md`
- `arch/Home/SQuirrel SQL Client Quick Guide for Altibase__14647622.md`
- `arch/Home/SQuirrel SQL Client Quick Guide for Altibase/1. SQuirrel SQL Client Installation__14647626.md`
- `arch/Home/SQuirrel SQL Client Quick Guide for Altibase/2. Altibase JDBC Driver Registeration__14647628.md`
- `arch/Home/SQuirrel SQL Client Quick Guide for Altibase/3. Integration with Altibase__14647630.md`
- `FAQE/Home/11. Utilities/AdminCenter2 execution file__16876465.md`
- `FAQE/Home/11. Utilities/iLoader/An error occurs when uploading a DOS format data file to iloader__16876469.md`

## Source coverage notes

This topic consolidates R020-owned source material for Altibase-to-Altibase migration, Oracle and Microsoft SQL Server conversion, Migration Center 7.12, VC guide attachments, GeoServer integration, SQuirrel SQL Client setup, AdminCenter2, and iLoader utility troubleshooting. The source documents include both current conversion guides and legacy Altibase HDB 6.3 material; version boundaries are retained instead of normalized.

Korean-source-backed document attachments are preserved when the source provides a downloadable URL. Legacy `#` attachment labels are recorded without synthetic URLs. Embedded screenshots and UI images remain in the source files and are not reconstructed in this consolidated reference.

## Scope and audience

Use this reference for DBA, migration engineer, application conversion, and support answers about:

- Moving data between Altibase versions, servers, or logical backup/restore targets with `aexport`, `iloader`, and `iSQL`.
- Converting Oracle 12c databases to Altibase 7.1 or later, plus reading legacy Oracle 9i-11g to ALTIBASE HDB 6.3 guidance.
- Converting Microsoft SQL Server 2016 databases to Altibase 7.1 or later.
- Operating Migration Center 7.12 in GUI and CLI modes.
- Integrating Altibase with GeoServer and SQuirrel SQL Client.
- Handling legacy utilities such as AdminCenter2 and iLoader DOS-format input.

Product names, commands, SQL, configuration properties, paths, class names, error codes, attachment filenames, and URLs must remain exact in generated answers.

## Key facts

### Source version baselines

| Area | Source baseline | Answering rule |
| --- | --- | --- |
| Altibase data migration | Altibase-to-Altibase version upgrade, server migration, and logical backup/recovery | Use `aexport` for object DDL and generated extraction/loading scripts, then `iloader` for table data. |
| Oracle comparison | Altibase 7.1 or later compared with Oracle 12c | Preserve architecture, object, SQL, datatype, API, and function differences. |
| Current Oracle conversion | Oracle 12c to Altibase 7.1 or later | Use current rules for datatypes, objects, PSM, Migration Center, and validation. |
| Legacy Oracle conversion | Oracle 9i-11g to ALTIBASE HDB 6.3 | Label as legacy; keep differences such as trigger, temporary table, and package limitations. |
| MSSQL conversion | SQL Server 2016 to Altibase 7.1 or later | Map SQL Server schemas to Altibase users and manually convert unsupported syntax. |
| Migration Center | Migration Center 7.12 | Supports GUI and CLI migration between supported DBMSs; GUI Reconcile precedes CLI `run`. |
| VC 2008 guide | Altibase v5 | Documented as a preserved ZIP attachment for Visual C++ 2008 development. |
| VC 2010 guide | Altibase v5 | Documented as a preserved PDF attachment for Visual C++ 2010 development. |
| GeoServer | Altibase 7.1.0 or later, GeoServer 2.16.2 or later | Requires GeoTools Altibase JDBC module, `Altibase.jar`, and spatial metadata setup. |
| SQuirrel SQL Client | Altibase 6 or later, SQuirrel SQL Client 3.7.1 | Register the Altibase JDBC driver and create an alias with a JDBC URL. |
| AdminCenter2 | Up to ALTIBASE HDB v4 only | For HDB 5 and later, the FAQ points users to Ware Valley Orange for Altibase. |
| iLoader DOS-format FAQ | ALTIBASE HDB 5.5.1 adds `%r%n` row separator handling | Convert CRLF files or set row terminator to avoid `ERR-9102B`. |

### Tool roles

| Tool | Role |
| --- | --- |
| `aexport` | Generates object DDL SQL and scripts such as `run_il_out.sh`, `run_is.sh`, `run_il_in.sh`, and index/FK/replication/job scripts. |
| `iloader` / `iLoader` | Extracts and loads table data using `.fmt`, `.dat`, `.log`, and `.bad` files. |
| `iSQL` / `isql` | Executes object creation, verification SQL, and package installation SQL. |
| Migration Center | Migrates compatible objects and data from supported source DBMSs to Altibase, and from Altibase to Oracle. |
| PL/SQL Converter Tool | Converts Oracle PL/SQL file datatype and syntax surfaces; business logic remains manually verified. |
| SQuirrel SQL Client | Java SQL client configured through the Altibase JDBC driver. |
| GeoServer | GIS server integration using Altibase JDBC and spatial metadata. |
| AdminCenter2 | Legacy GUI administration utility for ALTIBASE HDB v4 and earlier. |

## Procedures

### Migrate Altibase data with aexport and iloader

Use the Altibase Data Migration Process Guide when the requirement is an Altibase version upgrade, server migration, or logical backup/recovery.

1. Perform a preliminary check.
   - Stop services or otherwise ensure there is no DML or DDL during extraction.
   - Prepare a working directory with at least twice the data size.
   - Record source object and row counts before extraction.
   - For Altibase 7.3 or later, install `DBMS_METADATA` from `$ALTIBASE_HOME/packages` with `dbms_metadata.sql` and `dbms_metadata.plb` if `aexport` needs metadata extraction.
   - Query `V$NLS_PARAMETERS` and set `ALTIBASE_NLS_USE` to the server `NLS_CHARACTERSET`.
2. Adjust delimiter properties before running `aexport` to reduce data delimiter conflicts:

```properties
ILOADER_FIELD_TERM=^C_c^
ILOADER_ROW_TERM=^R_r^%n
```

3. Run `aexport` from a working directory. It generates scripts and SQL files including:
   - `run_il_out.sh`
   - `run_is.sh`
   - `run_il_in.sh`
   - `run_is_refresh_mview.sh`
   - `run_is_index.sh`
   - `run_is_fk.sh`
   - `run_is_repl.sh`
   - `run_is_job.sh`
   - `run_is_alt_tbl.sh`
   - `ALL_CRT_*` SQL files
4. Extract data.

```bash
time sh run_il_out.sh | tee download.out
nohup sh run_il_out.sh > download.out 2>&1 &
grep -i err- download.out
grep -i 'error row count' *.log
```

5. Configure the target Altibase instance.
   - Check source settings from `V$DATABASE`, `V$NLS_PARAMETERS`, `V$LOG`, and `V$PROPERTY`.
   - If source and target are on the same server, stop the source before copying or backing up `$ALTIBASE_HOME`, disk data, memory checkpoint image, log anchor, and transaction logs.
   - Edit target paths in `ALL_CRT_TBS.sql`.
   - Change generated script connection addresses when needed:

```bash
sed -i 's/-s localhost/-s 192.168.1.145/g' *.sh
sh run_is.sh | tee run_is.out
grep -i err- run_is.out
```

6. Load data.

```bash
time sh run_il_in.sh | tee upload.out
nohup sh run_il_in.sh > upload.out 2>&1 &
grep -i err- upload.out
grep -i 'Error Row Count' *.log
ls -l *.bad | awk '{print $5}' | sort -u
find ./ -type f -name "*.bad" ! -size 0
```

For performance-sensitive loads, the source recommends adding `iloader` options such as:

```bash
-array 1000 -commit 100
```

7. Verify follow-up scripts and counts.
   - `.fmt` and `.dat` file counts must match table counts.
   - `Error Row Count` must be 0.
   - `.bad` files must be size 0.
   - Run materialized view refresh, index, FK, replication, job, and alter-table scripts as applicable.

### Convert Oracle databases to Altibase

For current Oracle conversion, use the `ORACLE to ALTIBASE Conversion Guide` baseline: Oracle 12c to Altibase 7.1 or later.

1. Analyze the environment.
   - Record Oracle version.
   - Record source and target OS and hardware specifications.
   - Record target Altibase version.
   - Analyze source Oracle physical memory and swap.
   - Review business logic, batch jobs, and application dependency areas.
2. Convert datatypes and DDL.
   - Convert Oracle character, numeric, LOB, raw, date, and spatial types to Altibase equivalents.
   - Remove unsupported Oracle object clauses rather than carrying them into target DDL.
   - Convert tablespaces, tables, indexes, views, triggers, sequences, synonyms, and constraints according to the conversion tables below.
3. Convert SQL and PSM.
   - Convert Oracle-specific functions, `ROWNUM` usage, cursor update logic, packages, and utility package calls.
   - Validate autocommit and transaction behavior because Altibase stored procedure execution under autocommit is one transaction and internal `COMMIT`/`ROLLBACK` is ignored.
4. Use Migration Center for compatible data movement.
   - Create users and tablespaces on the target before mapping.
   - Add database connections, create a project, connect, build users/tables, reconcile mappings, run migration, and validate data.
   - Use the PL/SQL Converter Tool for Oracle PL/SQL file syntax and datatype conversion; manually verify business logic.
5. Validate the migrated database.
   - Use application verification plans.
   - Review Migration Center reports.
   - Compare record counts, sums, key queries, and any critical business outputs.
   - Manually review unsupported Oracle features and nonstandard source syntax.

### Convert Microsoft SQL Server databases to Altibase

Use the `MSSQL to ALTIBASE Conversion Guide` baseline: SQL Server 2016 to Altibase 7.1 or later.

1. Map schemas to users.
   - SQL Server schemas are independent from users and default to `dbo`.
   - Altibase uses `Schema = User`.
   - Convert each source schema to an Altibase user and avoid object-name conflicts.
   - Break schema-level grants down into object-level grants when needed.
2. Convert data types and objects.
   - Convert SQL Server text, binary, numeric, date/time, identity, and sequence features.
   - Convert SQL Server databases and filegroups into Altibase memory or disk tablespaces.
   - Remove unsupported clauses such as `FILESTREAM`, `COLLATE`, `IDENTITY`, `ROWGUIDCOL`, filtered index clauses, and unsupported compression/index options.
3. Convert SQL and procedures.
   - Replace SQL Server batch terminator `GO` with semicolon-based execution and explicit `Commit;` when preserving default autocommit behavior.
   - Replace temporary table syntax, `IF`/`WHILE`, variable declaration, parameter markers, procedure calls, and result-set cursor handling with Altibase PSM syntax.
   - Replace identity columns with sequence-based defaults.
4. Convert DB link and join-update patterns.
   - Use `REMOTE_TABLE(dblink_name, query)` for remote SELECT.
   - Use `REMOTE_EXECUTE_IMMEDIATE(dblink_name, query)` for remote DML.
   - Use `JOIN UPDATE` only when each joined table has a primary key or unique constraint; otherwise consider `MERGE`.
5. Validate data and unsupported features manually.

### Use Migration Center

Migration Center 7.12 can migrate compatible object definitions and data from supported source DBMSs to Altibase, and from Altibase to Oracle. It supports DB-to-DB migration and DB-to-File script/data generation.

1. Verify requirements.
   - GUI: CPU 800 MHz or faster, memory 512 MB or more, disk 150 MB or more, display 1024x768.
   - CLI: CPU 800 MHz or faster, memory 512 MB or more, disk 150 MB or more.
   - Java: Oracle or IBM Java 8 or later.
2. Install.
   - Download from `http://support.altibase.com/en/product`.
   - Unzip the package.
   - Start with `migcenter.bat` on Windows or `migcenter.sh` on Linux.
   - Remove by deleting the installation directory.
3. Prepare source and target.
   - Migration Center assumes a 1:1 source-target mapping.
   - Prepare target users, tablespaces, and capacity.
   - Ensure source and target character set and national character set compatibility.
   - For memory tables, size physical memory and disk capacity.
   - Do not expect LOB columns with `NOT NULL` to migrate.
4. Run the GUI flow.
   - Register source and target DBMS connection profiles.
   - Create or open a project.
   - Connect.
   - Set migration options.
   - Build users and tables.
   - Reconcile data type, PSM datatype, tablespace, table-to-tablespace, partition, SELECT, and DDL mappings.
   - Run migration.
   - Run data validation.
5. For large migrations, build and reconcile in the GUI, then move the complete project folder to Linux and run:

```bash
./migcenter.sh run [project_path]
```

`[project_path]` must be an absolute path.

### Configure GeoServer with Altibase

1. Install Java Runtime Environment 8 or later.
2. Install GeoServer 2.16.2 stable, for example under `C:\Program Files\GeoServer`.
3. Set `GEOSERVER_HOME` and `GEOSERVER_DATA_DIR`.
4. Copy required libraries into `C:\Program Files\GeoServer\webapps\geoserver\WEB-INF\lib`:
   - `gt-jdbc-altibase-21-SNAPSHOT.jar`
   - `jts-1.14.jar`
   - Altibase `Altibase.jar`
5. Install Altibase spatial metadata objects because the spatial module is not installed by default:

```bash
is -f $ALTIBASE_HOME/thirdparty/ArcGIS/geometry_columns.sql
```

6. Insert spatial reference metadata for SRID 4326 using the source-provided `altibase_spatial_ref_sys.sql` reference.
7. Start GeoServer with `startup.bat` and open `http://localhost:8080/geoserver`.
8. Login with the default account from the guide: username `admin`, password `geoserver`.
9. Add an Altibase data store. Important fields:
   - `dbtype`: `altibase`
   - host and port, with default port `20300`
   - database, with default database `mydb`
   - user and password
   - schema is not managed in the guide
   - `preparedStatements` is optional and is not checked in the source flow
10. Register the layer, set the coordinate system, and calculate bounds.
11. For spatial file import, install the GeoServer importer plugin ZIP into `WEB-INF/lib`, restart, choose Import Data, then select the workspace/store and spatial file.

Validate imported data from Altibase:

```sql
SELECT "fid", "emd_cd", "emd_eng_nm", ASTEXT("the_geom")
FROM "SEOUL_43260"
LIMIT 3;
```

GeoServer-created table and column names can be case-sensitive; use double quotes for lowercase names in Altibase SQL.

### Configure SQuirrel SQL Client

1. Use SQuirrel SQL Client 3.7.1 standard for the guide baseline. The source notes that SQuirrel 3.9.1 requires Java 1.8 or later.
2. Run `squirrel-sql.jar`.
3. In Drivers, create a new driver entry:
   - Name: `Altibase`
   - Example URL: `jdbc:Altibase://<host>:<port>/<database>`
   - Extra Class Path: add the Altibase JDBC driver JAR.
   - List Drivers and select `Altibase.jdbc.driver.AltibaseDriver`.
4. In Aliases, create an alias:
   - Name: user-defined alias name
   - Driver: registered Altibase driver
   - URL: Altibase JDBC URL
   - User Name and Password
5. Test the alias, connect, and use the Objects and SQL tabs.

### Use AdminCenter2

The AdminCenter2 FAQ is legacy utility coverage.

- AdminCenter2 is the last version of that tool.
- It supports only ALTIBASE HDB v4 and earlier.
- For HDB 5 and later, the FAQ recommends Ware Valley Orange for Altibase.
- Maintenance and support for AdminCenter2 ended.
- Download `AdminCenter2.zip`, unzip it, and run `AdminCenter.exe`.
- The JDBC driver is `$ALTIBASE_HOME/lib/Altibase.jar`.
- The manual is available from the application menu through Help > Help Contents.
- A separate Korean AdminCenter2 version is not provided.

### Fix iLoader DOS-format uploads

If a DOS CRLF data file is loaded on Unix/Linux, `iloader` can raise:

```text
ERR-9102B : Token value length overflow.
```

The cause is that the default row terminator uses `%n` LF, while the file contains CRLF. In `vi`, the file can show `^M`; the `file` command can show `[DOS]`.

Fix options:

- Convert on Windows with an editor such as UltraEdit: File > Convert > `DOS->UNIX`.
- Convert on Unix/Linux:

```bash
dos2unix SYS_T.dat
sed 's/^M//g' SYS_T.dat > SYS_T.dat.1
```

In the `sed` command, enter `^M` as `Ctrl+v` then `m`.

For ALTIBASE HDB 5.5.1 and later, specify a CRLF row separator:

```bash
iloader ... -t "|" -r "%r%n"
```

## SQL, commands, and configuration

### Altibase migration checks

Record row counts before and after extraction/loading. The source gives a query-generation pattern against the system catalog:

```sql
SELECT 'SELECT COUNT(*) FROM ' || USER_NAME || '.' || TABLE_NAME || ';'
  FROM SYSTEM_.SYS_USERS_ U, SYSTEM_.SYS_TABLES_ T
 WHERE U.USER_ID NOT IN (0, 1)
   AND U.USER_ID = T.USER_ID
   AND TABLE_TYPE = 'T'
 ORDER BY USER_NAME, TABLE_NAME;
```

Use source settings from:

```sql
SELECT * FROM V$DATABASE;
SELECT * FROM V$NLS_PARAMETERS;
SELECT * FROM V$LOG;
SELECT NAME, VALUE1 FROM V$PROPERTY;
```

Set the client character set to match server `NLS_CHARACTERSET`:

```bash
export ALTIBASE_NLS_USE=<server NLS_CHARACTERSET>
```

### Oracle datatype conversion highlights

| Oracle | Altibase rule |
| --- | --- |
| `CHAR`, `VARCHAR2` | `CHAR`, `VARCHAR`; Altibase `VARCHAR` max is 32000. |
| `NCHAR`, `NVARCHAR2` | Convert within Altibase national character size limits. |
| `NUMBER(38)` integer use | Prefer native integer-family Altibase types where appropriate. |
| `BINARY_FLOAT`, `BINARY_DOUBLE` | `REAL`, `DOUBLE`. |
| `LONG`, `NCLOB` | `CLOB`. |
| `RAW`, `LONG RAW`, `BFILE` | `BLOB`. |
| `DATE`, `TIMESTAMP` | Convert to Altibase date/time support; interval and time-zone timestamp variants are unsupported. |
| `SDO_GEOMETRY` | `GEOMETRY`, default size 32000 and up to 100 MB. |
| `ROWID`, `UROWID`, `ANY*`, XML/URI/media types | Unsupported; redesign or manual conversion required. |

### Oracle object conversion highlights

| Object area | Altibase conversion rule |
| --- | --- |
| Tablespaces | Convert Oracle data tablespaces to Altibase memory or disk tablespaces. Remove `BIGFILE`, `SMALLFILE`, `MINIMUM EXTENT`, `BLOCKSIZE`, default storage, `FLASHBACK`, `TABLESPACE GROUP`, and unsupported extent clauses. |
| Undo | Altibase manages undo with system tablespace behavior; use `SYS_TBS_DISK_UNDO` datafile add/resize operations when needed. |
| Tables | Convert regular tables; object/XML tables are unsupported. Remove `SORT`, `REF`, `ORGANIZATION`, `CLUSTER`, unsupported composite partitioning, and unsupported validation clauses. |
| Constraints | Primary key, unique, check, and foreign key are supported. `ON DELETE CASCADE` is supported; current conversion source says `ON DELETE SET NULL` is unsupported. |
| Table storage | Convert `INITIAL` to `INITEXTENTS`, `NEXT` to `NEXTEXTENTS`; remove `PCTINCREASE`, `FREELISTS`, `FREELIST`, `OPTIMAL`, and `BUFFER POOL`. |
| LOB storage | Preserve only supported `TABLESPACE` and `LOGGING`/`NOLOGGING` surfaces; remove unsupported storage, chunk, retention, freepool, cache, and storage-in-row clauses. |
| Partitioning | Range, list, and hash partitioning are supported; composite partitioning is not. |
| Indexes | Current source supports B-tree, R-tree, and function-based indexes; bitmap, cluster, reverse, and global partitioned indexes are unsupported. |
| Views | `CREATE OR REPLACE VIEW` is supported; remove unsupported XMLType/object view and `WITH CHECK OPTION` surfaces. Current source says views are updatable unless `WITH READ ONLY` is specified. |
| Triggers | Current source supports `BEFORE`, `AFTER`, and `INSTEAD OF`; DDL triggers are not supported. Replication-reflected changes do not fire triggers. `OLD` and `NEW` cannot be aliases. |
| Sequences | Remove `ORDER`, `NOORDER`, `KEEP`, `NOKEEP`, `SESSION`, and `GLOBAL`; preserve Altibase min/max range limits. |
| Synonyms | Remove `EDITIONABLE` and `NONEDITIONABLE`. |
| ALTER TABLE | Add or alter only one constraint at a time. Avoid pre-created indexes on primary-key or unique columns because Altibase creates the supporting index internally. |

Legacy ALTIBASE HDB 6.3 Oracle conversion sources differ in some areas: they record no package support, no `INSTEAD OF` trigger support, no LOB-column trigger target, temporary table limitations, and `TYPESET` use for `REF CURSOR`. When answering, label those as legacy 6.3 guidance.

### Oracle SQL and function conversion highlights

Preserve these Oracle-to-Altibase function categories:

- Numeric functions commonly supported or mapped: `ABS`, `ACOS`, `ASIN`, `ATAN`, `ATAN2`, `BITAND`, `CEIL`, `COS`, `COSH`, `EXP`, `FLOOR`, `LN`, `LOG`, `MOD`, `POWER`, `ROUND`, `SIGN`, `SIN`, `SINH`, `SQRT`, `TAN`, `TANH`, `TRUNC`.
- Oracle numeric functions not supported in the comparison source include `NANVL` and `WIDTH_BUCKET`.
- Altibase-only numeric functions in the comparison include `ISNUMERIC`, `NUMAND`, `NUMOR`, `NUMSHIFT`, `NUMXOR`, `RAND`, and `RANDOM`.
- Character functions commonly supported or mapped: `CHR`, `CONCAT`, `INITCAP`, `LOWER`, `LPAD`, `LTRIM`, `NCHR`, `REGEXP_REPLACE`, `REGEXP_SUBSTR`, `REPLACE`, `RPAD`, `RTRIM`, `SUBSTR`, `TRANSLATE`, `TRIM`, `UPPER`.
- Oracle `REPLACE` may map to Altibase `REPLACE2` in the comparison table.
- Oracle NLS-specific character functions such as `NLS_INITCAP`, `NLS_LOWER`, `NLS_UPPER`, `NLSSORT`, plus `SOUNDEX` and `TREAT`, are not supported in the comparison.
- Altibase-only character functions include `CHOSUNG`, `DIGEST`, `DIGITS`, `RANDOM_STRING`, `REPLICATE`, `REVERSE_STR`, `SIZEOF`, and `STUFF`.
- Datetime mappings include `ADD_MONTHS`, `CURRENT_DATE`, `CURRENT_TIMESTAMP`, `DBTIMEZONE` to `DB_TIMEZONE`, `EXTRACT` to `DATEPART`/`EXTRACT`, `LAST_DAY`, `MONTHS_BETWEEN`, `NEXT_DAY`, `SESSIONTIMEZONE` to `SESSION_TIMEZONE`, `SYSDATE`, `SYSTIMESTAMP`, `ROUND`, and `TRUNC`.
- Unsupported or redesign-required datetime areas include `FROM_TZ`, `LOCALTIMESTAMP`, `NEW_TIME`, intervals, and time-zone timestamp functions.
- Altibase datetime functions include `DATEADD`, `DATEDIFF`, `DATENAME`, `UNIX_DATE`, `UNIX_TIMESTAMP`, and `CONV_TIMEZONE`.

SQL feature differences to retain:

- `ROWNUM` is not supported in DML.
- `WHERE CURRENT OF` is not supported; convert cursor updates to explicit primary-key updates.
- Oracle hierarchical query support exists, but `CONNECT_BY_ISCYCLE` is not supported in the comparison source.
- `SELECT FOR UPDATE` is supported without join.
- Parallel SELECT is not supported; parallel INSERT and parallel index build are supported.

### Oracle PSM conversion configuration

Altibase stored procedure and function conversion must preserve precision and transaction differences.

Under autocommit, Altibase processes a procedure as a single transaction, ignores internal `COMMIT` and `ROLLBACK`, and automatically commits after execution. In non-autocommit mode, Oracle and Altibase behavior is aligned by the source.

Relevant precision properties:

```properties
PSM_PARAM_AND_RETURN_WITHOUT_PRECISION_ENABLE=1
PSM_CHAR_DEFAULT_PRECISION=32767
PSM_NCHAR_UTF16_DEFAULT_PRECISION=16383
PSM_NCHAR_UTF8_DEFAULT_PRECISION=10921
PSM_VARCHAR_DEFAULT_PRECISION=32767
PSM_NVARCHAR_UTF16_DEFAULT_PRECISION=16383
PSM_NVARCHAR_UTF8_DEFAULT_PRECISION=10921
LOB_OBJECT_BUFFER_SIZE=32000
```

If `PSM_PARAM_AND_RETURN_WITHOUT_PRECISION_ENABLE=0`, omitted precision for `CHAR`, `NCHAR`, `NVARCHAR`, and `VARCHAR` becomes 1.

Package and utility mapping examples:

- `DBMS_OUTPUT.NEW_LINE`, `PUT`, and `PUT_LINE` map to Altibase package procedures; `PUT` and `PUT_LINE` can also be represented as `PRINT` and `PRINTLN`.
- `UTL_FILE` mappings include `FOPEN`, `FCLOSE`, `FCLOSE_ALL`, `FCOPY`, `FFLUSH`, `FREMOVE`, `FRENAME`, `GET_LINE`, `IS_OPEN`, `NEW_LINE`, `PUT`, and `PUT_LINE`.
- Unsupported `UTL_FILE` procedures include `FGETATTR`, `FGETPOS`, `FOPEN_NCHAR`, `FSEEK`, `GET_LINE_NCHAR`, `GET_RAW`, `PUT_LINE_NCHAR`, `PUT_NCHAR`, `PUTF`, `PUTF_NCHAR`, and `PUT_RAW`.
- `DBMS_RANDOM.SEED`, `STRING`, `VALUE`, `INITIALIZE`, and `RANDOM` are supported or mappable; `NORMAL` and `TERMINATE` are unsupported.

Legacy 6.3 source notes that omitted parameter or return size can raise:

```text
ERR-2100D : Invalid length of the data type
```

### MSSQL datatype and object conversion highlights

| SQL Server | Altibase rule |
| --- | --- |
| `CHAR`, `VARCHAR` | Convert up to Altibase 32000-byte limit. |
| `CHAR(MAX)`, `VARCHAR(MAX)`, `TEXT`, `NTEXT` | `CLOB`. |
| `NCHAR`, `NVARCHAR` | Convert within Altibase national character limits; `MAX` forms map to `CLOB`. |
| `BINARY` | `BYTE`. |
| `VARBINARY(MAX)`, `IMAGE` | `BLOB`. |
| `TINYINT` | `SMALLINT`. |
| `MONEY`, `SMALLMONEY` | `DECIMAL(p,s)` with appropriate precision and scale. |
| `DATETIMEOFFSET` | Unsupported; use `DATE` only when time-zone information is excluded. |
| `DATETIME2`, `SMALLDATETIME`, `DATETIME`, `TIME` | `DATE` with precision caveats. |

Object conversion reminders:

- SQL Server database/file options map to Altibase tablespace and datafile options where applicable.
- `FILENAME`, `SIZE`, `MAXSIZE`, and `FILEGROWTH` map into Altibase datafile sizing and `AUTOEXTEND ON NEXT` behavior.
- Unsupported database options include `FILESTREAM`, `DEFAULT_FULLTEXT_LANGUAGE`, `DEFAULT_LANGUAGE`, `NESTED_TRIGGERS`, `TRANSFORM_NOISE_WORDS`, `TWO_DIGIT_YEAR_CUTOFF`, `DB_CHAINING`, and `TRUSTWORTHY`.
- Table conversion removes `FILESTREAM`, `COLLATE`, `IDENTITY`, `ROWGUIDCOL`, XML collection options, clustered/nonclustered inline clauses, computed columns, and unsupported index options.
- `DATA_COMPRESSION` maps to `COMPRESS(column_name)` where applicable.
- `partition_scheme` maps to `PARTITION BY RANGE`, `PARTITION BY HASH`, or `PARTITION BY LIST`.
- Index conversion supports B-tree and R-tree. Bitmap, cluster, reverse, and global partitioned indexes are unsupported in the MSSQL guide.

Create users with the Altibase schema-user model:

```sql
CREATE USER user_name IDENTIFIED BY 'password'
DEFAULT TABLESPACE = tablespace_name;
```

### MSSQL SQL and procedure conversion highlights

Preserve these conversion rules:

- `CAST` and `CONVERT` generally map to Altibase `CAST`; Altibase `CONVERT` is a different function surface.
- `PARSE` and `TRY_CAST` map only where `CAST` semantics are acceptable; `TRY_CONVERT` and `TRY_PARSE` are unsupported.
- `COUNT_BIG` maps to `COUNT`, `STDEV` maps to `STDDEV`, and `VAR` maps to `VARIANCE`.
- Ranking functions `DENSE_RANK`, `NTILE`, `RANK`, and `ROW_NUMBER` are supported.
- `CURRENT_TIMESTAMP`, `DATENAME`, `DATEPART`, `DATEADD`, `DATEDIFF`, `LAST_DAY`-style `EOMONTH` conversion, `SYSDATE`, Unix time functions, and `CONV_TIMEZONE` cover most date mapping needs.
- `CHOOSE` is unsupported; `IIF` maps to `case2`.
- String mappings include `CHARINDEX`/`PATINDEX` to `INSTR`/`POSITION`, `LEFT` and `RIGHT` to `SUBSTR`/`SUBSTRING`, `LEN` to `LENGTH`, `REVERSE` to `REVERSE_STR`, `SPACE` to `LPAD`/`RPAD`, and `STR` to `TO_CHAR`.
- Concatenation `+` maps to `||`.
- Remainder `%` maps to `MOD`.
- `ISNULL` maps to `NVL`.
- `CEILING` maps to `CEIL`.

Procedure conversion rules:

- Remove `@` from variables and parameters.
- Use `IN`, `OUT`, or `IN OUT`.
- Put a function return type after `RETURN`.
- Place declarations between `AS` and `BEGIN`.
- Terminate declarations with semicolons.
- Use `:=` or `SET` for assignment.
- Use `IF ... THEN`, `ELSIF`, and `END IF`.
- Use `TYPESET` and `REF CURSOR` patterns for result sets.
- Use `BEGIN ... EXCEPTION ... END` with `OTHERS` and `SQL%ROWCOUNT` as needed.
- Call stored procedures with parentheses.

### Migration Center connection and option details

Supported source-to-target combinations from the Migration Center guide include:

- Target Altibase DB V6.5.1 or later from Altibase 4.3.9 or later.
- Oracle 9i-11g to Altibase.
- MS-SQL 2005-2012 to Altibase.
- MySQL 5.0-5.7 to Altibase.
- Informix 11.50 to Altibase.
- TimesTen 7.0/11.2 to Altibase.
- CUBRID 8.4.1-9.3.5 with ISO-8859 or UTF-8 to Altibase.
- Tibero 4sp1-6.0 to Altibase.
- PostgreSQL 9.5.3 to Altibase.
- Altibase 4.3.9 or later to Oracle 10g-11g.

JDBC driver notes:

- Oracle JDBC driver is bundled.
- MS-SQL, MySQL, Informix, TimesTen, and other third-party drivers may need to be obtained separately.
- TimesTen requires a Type 2 client installation.
- The source says the MS-SQL 2005 driver URL is unavailable; use the driver included with the product when needed.
- For MS-SQL JDBC 6.0 with Migration Center, Java 8 is recommended; on Linux, set `JAVA_HOME` as required by the driver.

Important DB-to-DB options:

| Option | Source default or rule |
| --- | --- |
| Execution Thread | Default is logical CPUs * 3; recommended range is 1 through logical CPUs * 3. |
| Migration Target | Object and Data, or Object. |
| FK | Default `No`. |
| PSM | Default `Yes`. |
| Drop Existing Objects | Default `No`. |
| Keep Partition | Default `No`; if `Yes`, reconcile partition conversion carefully. |
| Double-quoted identifier | Default `No`. |
| Remove FORCE | Default `Yes`. |
| Reserved word postfix | `_POC`. |
| Batch Execution | Default `Yes`. |
| Batch Size | `10000`. |
| Batch LOB | Default `No`; source warns about memory and TimesTen behavior. |
| Log Insert-failed Data | Enabled only when Batch Execution is `No`; default `No`. |
| File Encoding | Default `UTF8` when failed data is logged. |
| Validation Operation | `DIFF` or `FILESYNC`. |
| Data Sampling | Default `Yes`; choose `No` for full validation. |

Migration reports and outputs:

- `SrcDbObj_Create.sql`
- `BuildReport4Unsupported.html`
- `RunReport4Summary.html`
- `RunReport4Missing.html`
- Data Validation CSV output

Supported-object caveats that affect answers:

- Oracle temporary tables require a volatile tablespace target.
- Tibero PSM conversion uses a third-party Oracle parser and can fail on Tibero-specific syntax.
- TimesTen hash/range indexes become B-tree; bitmap indexes are unsupported; indexes on primary-key or unique columns can be excluded because Altibase disallows duplicate supporting indexes.
- PostgreSQL has up to 1600 columns, while Altibase supports up to 1024 columns per table.
- PostgreSQL foreign key `RESTRICT` is removed and `SET DEFAULT` converts to `SET NULL`.
- PostgreSQL default sequence max value `9223372036854775807` is forced to Altibase `9223372036854775806`.
- PostgreSQL sequence cache 1 removes `CACHE` and uses Altibase default 20.
- PostgreSQL functions, views, materialized views, triggers, exclusion constraints, types, and enums are unsupported in the Migration Center matrix.

## Validation and troubleshooting

### Altibase migration validation

Use all of these checks when answering a data migration validation question:

- Source count SQL before extraction.
- Generated `.fmt` and `.dat` counts after extraction.
- `grep -i err- download.out`
- `grep -i 'error row count' *.log`
- `grep -i err- run_is.out`
- `grep -i err- upload.out`
- `Error Row Count` in `iloader` logs must be 0.
- `.bad` files must exist only as zero-byte files.
- Follow-up object scripts must be run and checked as applicable.

`ERR-9102B : Token value length overflow` can occur during data migration when a token exceeds the expected length or when DOS CRLF row terminators conflict with Unix/Linux `iloader` row terminator handling.

### Oracle conversion validation

- Check unsupported object lists before migration.
- Review generated DDL for unsupported Oracle clauses.
- Verify package, procedure, and function behavior under Altibase transaction semantics.
- Convert `WHERE CURRENT OF` to primary-key-based updates.
- Treat legacy 6.3 notes as source-version-specific, not current Altibase 7.1 guidance.
- Use Migration Center reports and application verification plans to confirm converted data and logic.

### MSSQL conversion validation

- Confirm schema-to-user mapping and object grants.
- Check identity-to-sequence conversion.
- Review `GO`, `IF`, `WHILE`, parameter, variable, and result-set conversion.
- Confirm date/time conversion when `DATETIMEOFFSET` or time-zone semantics exist.
- Confirm DB link usage and join-update key requirements.

### Migration Center validation

- If source metadata changes after Build and before Run, rerun Build through Run.
- If options change after Reconcile, restart from Reconcile.
- For full validation, set Data Sampling to `No`.
- `FILESYNC` is available as a validation operation.
- CSV diff output may be written for validation review.

### GeoServer validation

- Confirm `geometry_columns.sql` was installed.
- Confirm `spatial_ref_sys` includes SRID 4326 when using the sample flow.
- Confirm the Altibase data store uses `dbtype=altibase` and correct host, port, database, user, and password.
- Use the layer preview.
- Query Altibase with quoted identifiers when GeoServer created lowercase names.

### SQuirrel validation

- Use List Drivers to confirm `Altibase.jdbc.driver.AltibaseDriver`.
- Test the alias before connecting.
- Confirm the Objects tab and SQL tab are available after connection.

### AdminCenter2 validation

Do not recommend AdminCenter2 for HDB 5 or later. Its maintenance and support ended, and the FAQ points HDB 5 or later users to Orange for Altibase.

## Version-specific notes

- Altibase 7.3 or later: `DBMS_METADATA` package installation from `$ALTIBASE_HOME/packages` can be needed for `aexport` metadata extraction.
- Altibase 7.1 or later: current Oracle 12c and SQL Server 2016 conversion guides target this baseline.
- ALTIBASE HDB 6.3: legacy Oracle conversion guide baseline; preserve older limitations separately.
- ALTIBASE HDB 5.5.1: iLoader supports the `%r%n` row terminator pattern for DOS CRLF files.
- Altibase v5: VC 2008 and VC 2010 development guide attachments apply to this baseline.
- Altibase 6 or later: SQuirrel SQL Client quick guide baseline.
- Altibase 7.1.0 or later and GeoServer 2.16.2 or later: GeoServer integration guide baseline.
- ALTIBASE HDB v4 or earlier: AdminCenter2 support boundary.

## Related errors

| Error or exception | Source context | Required answer detail |
| --- | --- | --- |
| `ERR-9102B : Token value length overflow` | `iloader` migration and DOS-format FAQ | Check delimiter/row terminator, token length, `.bad` file contents, and DOS CRLF conversion. |
| `ERR-2100D : Invalid length of the data type` | Legacy Oracle PSM conversion | Occurs when `CHAR`/`VARCHAR` parameter or return types omit size under legacy behavior. |
| `CURSOR_ALREADY_OPEN` | Oracle/MSSQL PSM exception mapping | Altibase decimal `201062`, hex `31166`. |
| `DUP_VAL_ON_INDEX` | Oracle/MSSQL PSM exception mapping | Altibase decimal `201063`, hex `31167`. |
| `INVALID_CURSOR` | Oracle/MSSQL PSM exception mapping | Altibase decimal `201064`, hex `31168`. |
| `INVALID_NUMBER` | Oracle/MSSQL PSM exception mapping | Altibase decimal `201065`, hex `31169`. |
| `NO_DATA_FOUND` | Oracle/MSSQL PSM exception mapping | Altibase decimal `201066`, hex `3116A`. |
| `PROGRAM_ERROR` | Oracle/MSSQL PSM exception mapping | Altibase decimal `201067`, hex `3116B`. |
| `STORAGE_ERROR` | Oracle/MSSQL PSM exception mapping | Altibase decimal `201068`, hex `3116C`. |
| `TIMEOUT_ON_RESOURCE` | Oracle/MSSQL PSM exception mapping | Altibase decimal `201069`, hex `3116D`. |
| `TOO_MANY_ROWS` | Oracle/MSSQL PSM exception mapping | Altibase decimal `201070`, hex `3116E`. |
| `VALUE_ERROR` | Oracle/MSSQL PSM exception mapping | Altibase decimal `201071`, hex `3116F`. |
| `ZERO_DIVIDE` | Oracle/MSSQL PSM exception mapping | Altibase decimal `201072`, hex `31170`. |
| `INVALID_PATH` | MSSQL conversion file exception mapping | Altibase decimal `201237`, hex `31215`. |
| `INVALID_MODE` | MSSQL conversion file exception mapping | Altibase decimal `201235`, hex `31213`. |
| `INVALID_FILEHANDLE` | MSSQL conversion file exception mapping | Altibase decimal `201238`, hex `31216`. |
| `INVALID_OPERATION` | MSSQL conversion file exception mapping | Altibase decimal `201239`, hex `31217`. |
| `READ_ERROR` | MSSQL conversion file exception mapping | Altibase decimal `201242`, hex `3121A`. |
| `WRITE_ERROR` | MSSQL conversion file exception mapping | Altibase decimal `201243`, hex `3121B`. |
| `ACCESS_DENIED` | MSSQL conversion file exception mapping | Altibase decimal `201236`, hex `31214`. |
| `DELETE_FAILED` | MSSQL conversion file exception mapping | Altibase decimal `201240`, hex `31218`. |
| `RENAME_FAILED` | MSSQL conversion file exception mapping | Altibase decimal `201241`, hex `31219`. |

## Attachments and external references

### Preserved URL-backed attachments

- `ALTIBASE_ORACLE_비교자료.pdf`: `https://docs.altibase.com/download/attachments/14058137/ALTIBASE_ORACLE_%EB%B9%84%EA%B5%90%EC%9E%90%EB%A3%8C.pdf?version=1&modificationDate=1697697201000&api=v2`
- `Migration_Center_사용자가이드.pdf`: `https://docs.altibase.com/download/attachments/19955861/Migration_Center_%EC%82%AC%EC%9A%A9%EC%9E%90%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=2&modificationDate=1701652961000&api=v2`
- `ALTIBASE_VC_2008_개발가이드.zip`: `https://docs.altibase.com/download/attachments/19333567/ALTIBASE_VC_2008_%EA%B0%9C%EB%B0%9C%EA%B0%80%EC%9D%B4%EB%93%9C.zip?version=1&modificationDate=1697696674000&api=v2`
- `ALTIBASE_VC_2010_개발가이드.pdf`: `https://docs.altibase.com/download/attachments/19334121/ALTIBASE_VC_2010_%EA%B0%9C%EB%B0%9C%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1698738784000&api=v2`
- GeoServer importer plugin ZIP: `https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.2/extensions/geoserver-2.16.2-importer-plugin.zip/download`
- `AdminCenter2.zip`: `https://docs.altibase.com/download/attachments/8454900/AdminCenter2.zip?version=1&modificationDate=1424835455000&api=v2`

### Legacy attachment labels without downloadable URLs

- `ALTIBASE_Oracle_변환_가이드.pdf`: no downloadable URL in source.
- `ORACLE_to_ALTIBASE_변환_가이드_5.5.pdf`: no downloadable URL in source.
- `ALTIBASE_MSSQL_변환가이드.pdf`: no downloadable URL in source.

### Manual and support links

- Altibase support product downloads: `http://support.altibase.com/en/product`
- Altibase 7.3 Utilities Manual: `https://manual.altibase.com/7.3/en/tools/util/copyright/`
- Altibase 7.3 iLoader User's Manual: `https://manual.altibase.com/7.3/en/tools/iloader/copyright/`
- Migration Center manual: `https://manual.altibase.com/7.1/external-tools/migration-center/copyright/`
- Altibase DB Link manual: `https://manual.altibase.com/7.3/en/admin/dblink/copyright/`
- Altibase 7.3 Getting Started: `https://manual.altibase.com/7.3/en/start-here/getting-started/copyright/`
- Altibase 7.3 Spatial SQL Reference: `https://manual.altibase.com/7.3/en/ref/spatial-sql/copyright/`
- Ware Valley Orange for Altibase: `http://www.warevalley.com`
- SQuirrel SQL Client 3.7.1 standard JAR: `https://jaist.dl.sourceforge.net/project/squirrel-sql/1-stable/3.7.1/squirrel-sql-3.7.1-standard.jar`
- SQuirrel SQL installation page: `http://squirrel-sql.sourceforge.net/#installation`

## Terminology

- `aexport`: Altibase export utility that produces object DDL and `iloader`/`iSQL` helper scripts.
- `iloader` / `iLoader`: Altibase data unload/load utility; preserve exact row terminator options such as `%n` and `%r%n`.
- `iSQL` / `isql`: Altibase SQL execution tool used for object creation, package installation, and verification queries.
- `Migration Center` / `MigrationCenter`: Altibase GUI/CLI migration tool; keep source spelling when citing UI or manual names.
- `DB to DB`: Migration Center mode that directly creates target objects and copies data.
- `DB to File`: Migration Center mode that creates SQL scripts and data files.
- `Reconcile`: Migration Center phase for editing datatype, tablespace, partition, SELECT, and DDL mappings.
- `PL/SQL Converter Tool`: Migration Center-adjacent tool for Oracle PL/SQL file syntax and datatype conversion.
- `Schema = User`: Altibase model that affects SQL Server schema conversion.
- `TYPESET`: Altibase construct used by legacy conversion guidance for `REF CURSOR` result sets.
- `REMOTE_TABLE` and `REMOTE_EXECUTE_IMMEDIATE`: Altibase DB Link functions for remote SELECT and DML.
- `GeoServer`: GIS server integrated through Altibase JDBC and spatial metadata.
- `SQuirrel SQL Client`: Java SQL client configured with `Altibase.jdbc.driver.AltibaseDriver`.
- `AdminCenter2`: legacy Altibase GUI utility for ALTIBASE HDB v4 and earlier.
