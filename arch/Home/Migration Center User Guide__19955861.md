---
title: "Migration Center User Guide"
page_id: "19955861"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=19955861"
updated_at: "2023-12-04T10:22:49.000+0900"
version: 2
ancestors: ["Home"]
labels: []
translated_from_space_key: "DOCK"
---

# Migration Center User Guide
Source: https://docs.altibase.com/pages/viewpage.action?pageId=19955861
Updated: 2023-12-04T10:22:49.000+0900

- [Overview](#overview) - [Benefits](#benefits) - [Requirements](#requirements) - [JDBC Drivers](#jdbc-drivers) - [Precautions](#precautions) - [Getting Started](#getting-started) - [Interface](#interface) - [GUI User Guide](#gui-user-guide) - [Supported Conversion Objects](#supported-conversion-objects)

# Overview

---

Migration Center is a DBMS migration tool that directly or indirectly copies generally compatible DBMS objects and data between DBMS products.

Altibase Migration Center helps migrate objects and data from other databases to Altibase, and from Altibase to Oracle DB.

Migration Center lets users perform DB migration work in GUI mode with mouse operations, and it also supports a command-line interface (CLI) mode.

The test environment for this document is Migration Center 7.12.

For errors and improvement requests related to this document, contact the technical support portal or the technical support center.

- Technical support portal: [http://support.altibase.com](http://support.altibase.com/) > Technical Knowledge > Q&A
- Technical support center: 02-2082-1114

This document is provided for informational purposes and may be changed without prior notice. It may contain errors, and Altibase assumes no express or implied liability for merchantability or fitness for a particular purpose.

The schedule for developing or releasing features and functions of Altibase products described in this document is at Altibase's discretion.

Altibase may hold patent rights, trademark rights, copyrights, or other intellectual property rights related to this document.

## Benefits

---

Migration Center provides the following benefits.

1. Source DB objects can be migrated easily to the target DB.
2. Source DB data can be copied directly to Altibase through JDBC.
3. Data can be exported to external files and imported into Altibase DB with iLoader.
4. Parallel execution options can shorten the migration process.
5. Data migration load can be balanced automatically across multiple threads.
6. Data processed by each thread can also be divided manually.
7. Data type mapping is provided for different data types between databases.
8. Both default type mapping and user-defined data type mapping are supported.
9. Both GUI mode and CLI mode are supported.
10. Users can edit DDL SQL statements used for DB object migration.

## Requirements

---

Migration Center has the following system requirements.

| Category | Mode | Requirement |
| --- | --- | --- |
| Hardware | GUI mode | CPU: 800 MHz or higher<br>Memory: 512 MB or higher<br>Disk: at least 150 MB free<br>Screen resolution: 1024 x 768 or higher |
| Hardware | CLI mode | CPU: 800 MHz or higher<br>Memory: 512 MB or higher<br>Disk: at least 150 MB free |
| Software | All modes | Oracle or IBM Java 8 or later JRE |

Migration Center supports the following DBMS combinations.

| Target DB | Source DB |
| --- | --- |
| Altibase DB V6.5.1 or later | Altibase DB V4.3.9 or later<br>Oracle V9i to 11g<br>MS-SQL V2005 to 2012<br>MySQL V5.0 to 5.7<br>Informix V11.50<br>TimesTen V7.0 and 11.2<br>CUBRID V8.4.1 to 9.3.5, ISO-8859 and UTF-8 character sets<br>Tibero V4sp1 to 6.0<br>PostgreSQL 9.5.3 |
| Oracle 10g to 11g | Altibase DB V4.3.9 or later |

## JDBC Drivers

---

Migration Center uses JDBC drivers for database connections, so users must prepare JDBC drivers that match the source and target databases.

For user convenience, Migration Center includes some JDBC drivers for selected databases. MS-SQL, MySQL, Informix, and TimesTen drivers must be obtained directly by the user because of legal restrictions.

TimesTen supports only Type 2 drivers, so migration must be performed on a host where the TimesTen Client Package is installed.

### JDBC Driver Download URLs

---

The Oracle JDBC driver is distributed with Migration Center. MS-SQL 2005 is not supported under the Microsoft Support Lifecycle policy, and no download URL is provided. Use the JDBC driver included with the MS-SQL product used by the customer.

| Database | JDBC download URL | Notes |
| --- | --- | --- |
| Tibero | [https://technet.tmaxsoft.com/](https://technet.tmaxsoft.com/) |  |
| CUBRID | [http://www.cubrid.org/?mid=downloads&item=jdbc_driver](http://www.cubrid.org/?mid=downloads&item=jdbc_driver) |  |
| TimesTen | [http://www.oracle.com/technetwork/database/database-technologies/timesten/downloads/index.html](http://www.oracle.com/technetwork/database/database-technologies/timesten/downloads/index.html) |  |
| Informix | [http://www14.software.ibm.com/webapp/download/search.jsp?go=y&rs=ifxjdbc](http://www14.software.ibm.com/webapp/download/search.jsp?go=y&rs=ifxjdbc) |  |
| MySQL | [http://dev.mysql.com/downloads/connector/j/](http://dev.mysql.com/downloads/connector/j/) |  |
| MS-SQL | [Download Microsoft JDBC Driver for SQL Server](https://docs.microsoft.com/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server?view=sql-server-2017)<br>[Microsoft JDBC Driver for SQL Server Support Matrix](https://docs.microsoft.com/en-us/sql/connect/jdbc/microsoft-jdbc-driver-for-sql-server-support-matrix?view=sql-server-2017) | MS-SQL 2008, 2008 SP1, and 2012 JDBC drivers can be downloaded from the URL.<br>JDBC 6.0 and JRE 8 are recommended for Migration Center.<br>The MS-SQL JDBC driver requires JRE 7 or later, so on Linux the `JAVA_HOME` environment variable must point to JRE 7 or later.<br>To use a JDBC driver version other than JDBC 6.0, check the SQL Server Support Matrix and use a compatible JRE. |
| PostgreSQL | [https://jdbc.postgresql.org/download/](https://jdbc.postgresql.org/download/) |  |

## Precautions

---

Check the following precautions before using Migration Center.

1. Migration Center performs migration with a 1:1 mapping between the source DB and target DB.
2. Source DB components are extracted.
3. Based on the extracted source DB components, prepare the target DB users, tablespaces, and data capacity.
4. Apply the extracted source DB components to the target DB.
5. For performance-sensitive migration, if the migration target table is configured as a memory table, physical memory and disk must be prepared according to the data size.
6. Columns with a LOB data type and a `NOT NULL` constraint are not migrated.
7. It is recommended that the source DB and target DB use the same character set and national character set.
8. For large data migrations, configure the environment in GUI mode and complete the Build and Reconcile steps, then run the Run step in CLI mode for better performance.
9. If the source DB user is composed of multiple DBs or schemas, Migration Center cannot connect to the source DB. If the source has a multi-DB or multi-schema structure, it is best to ask the customer to change it to a 1:1 mapping between DB user and DB or schema. If this is not possible, migration must be performed manually.
10. PSM conversion is performed only for Oracle source databases. Tibero is migrated without PSM changes. Other DBMS products do not migrate PSM; they only collect PSM information for manual conversion.

# Getting Started

---

This section describes how to download, install, and remove Migration Center.

## Installation and Removal

---

1. Download Migration Center from [http://support.altibase.com/en/product](http://support.altibase.com/en/product).
2. To install Migration Center, unzip the downloaded package to any directory.
3. To remove Migration Center, delete the Migration Center directory.
4. To run Migration Center on Windows, execute `migcenter.bat` from the installation directory.
5. To run Migration Center on Linux, execute `migcenter.sh`.

## Migration Center Concepts

---

### Terms

| Term | Description |
| --- | --- |
| Project | A Migration Center project is the basic work unit that describes every aspect of a migration. A project includes what to migrate, where to migrate from and to, which type of database or data file is involved, and how database objects and table data should be migrated. |

### Basic Process

Migration consists of five steps: Prepare, Build, Reconcile, Run, and Data Validation.

| Step | Description |
| --- | --- |
| Prepare | This is the implicit stage for the actual migration project. The final state is an open project with all database connections configured. |
| Build | Migration Center performs an initial investigation of the current state of the source and target databases. It collects database object information through database connections and stores the information in the project directory. Because this information is used in later stages, it must reflect the latest state. If metadata changes in the source database before the Run step, rerun the full process from Build through Run so the changes are included. |
| Reconcile | Migration Center constructs the full migration plan for the current state. This step mainly reconciles differences in data types, tablespaces, and similar items between source and target database systems. Users can edit the `SELECT` statements used for extracting data from the source database and the DDL statements to be executed on the target database. If migration options are changed, processing must resume from this step. |
| Run | Migration Center executes the plan produced in the Reconcile step. Schema and data are migrated directly or indirectly. If Migration Type is `DB to DB`, Migration Center creates database objects in the target database and then copies data from the source database to the target database. If Migration Type is `DB to File`, SQL script files are generated during migration, but the basic process is the same. |
| Data Validation | If Build was performed by `Build User`, all tables with primary keys are checked for data consistency. If Build was performed by `Build Table`, migrated tables with primary keys are checked. Data that differs from the source is saved in CSV format and can be applied to the target database through the `FILESYNC` menu or command. To reduce validation time, data sampling is used by default. To validate all data instead of sample data, set `Data Sampling` to `No` in Data Validation Options. |

# Interface

---

Migration Center provides GUI mode and CLI mode. Detailed usage for each mode is provided in the GUI mode quick guide and CLI mode quick guide.

## Starting Migration Center

---

Unzip `MigrationCenter7.12.zip` to any folder. Run `migcenter.bat` from the Migration Center directory on Windows, or run `migcenter.sh` on Linux.

## User Interface

---

The Migration Center GUI mode screen is organized into four windows.

## Menus and Icons

---

| Menu | Description |
| --- | --- |
| Database > Add Database Connection | Registers the source DBMS and target DBMS for migration. A shortcut icon is provided in the upper-left area of Migration Center. |
| Database > Database Connection List | Shows the list of registered DBMS connections. |
| Database > Exit | Exits Migration Center. |
| Project > Create Project | Creates a new project for object and data migration. A shortcut icon is provided in the upper-left area. |
| Project > Open Project | Opens an existing project. |
| Project > Connect | Connects to the databases used by the project. The same function is available by right-clicking a project in the Project pane and selecting `Connect`. |
| Project > Disconnect | Disconnects the databases used by the project. The same function is available by right-clicking a project and selecting `Disconnect`. |
| Project > Close | Closes the project. The same function is available by right-clicking a project and selecting `Close`. |
| Migration > Build User | Migrates all objects and data owned by a DB user. The shortcut icon lets users select `Build User`; the same function is available by right-clicking a project and selecting `Build User`. |
| Migration > Build Table | Migrates all tables and data owned by a DB user. The shortcut icon lets users select `Build Table`; the same function is available from the project context menu. |
| Migration > Reconcile | Enabled after the Build step completes. It reconciles target objects. The same function is available from the shortcut icon or by right-clicking a project and selecting `Reconcile`. |
| Migration > Run | Enabled after the Reconcile step completes. It runs migration. The same function is available from the shortcut icon or by right-clicking a project and selecting `Run`. |
| Migration > Data Validation | Enabled after the Reconcile step completes. It validates migrated data. The same function is available from the project context menu. |
| Migration > Migration Options | Configures basic options used by the migration project. If Migration Options are changed, processing must restart from the Reconcile step. The same function is available from the project context menu. |
| Report > Build Report | Enabled after project Build completes. The same function is available from the project context menu. |
| Report > Reconcile Report | Enabled after project Reconcile completes. The same function is available from the project context menu. |
| Report > Run Report | Enabled after project Run completes. The same function is available from the project context menu. |
| Report > Data Validation Report | Enabled after project Data Validation completes. The same function is available from the project context menu. |

## Migration Center Utility

---

| Utility | Description |
| --- | --- |
| PSM Converter for File | Converts Oracle PL/SQL to Altibase PSM. It reads a SQL file containing Oracle PL/SQL syntax, converts it to Altibase PSM, and writes the result to a predefined SQL file. The output is provided with an HTML report file. Internally, this utility is the same as the PSM Converter used in the migration Reconcile step. Run it from `Tools > PSM Converter for File`. |
| Generate Migration Error Report | Collects troubleshooting information for Migration Center problems. After opening a project, run this tool to collect log files, revision numbers, and other trace information into a ZIP file. Send the ZIP file to the Altibase customer service portal with customer registration information. Run it from `Tools > Generate Migration Error Report`. |

# GUI User Guide

---

This section describes migration in GUI mode.

## Migration Flow

---

GUI mode migration proceeds in this order.

1. Start Migration Center.
2. Prepare the project.
3. Register source and target DB connections.
4. Create the project.
5. Open the project.
6. Connect the source and target DBs.
7. Configure Migration Options.
8. Build the project.
9. Reconcile the project.
10. Run the project.
11. Validate the project.

## Registering DBMS Connections

---

Register the source DBMS and target DBMS by selecting `Database > Add Database Connection` or by clicking the Add Database Connection icon.

## Entering DBMS Information

---

The DBMS types that can be registered are Oracle, Altibase, MS-SQL, MySQL, Informix, TimesTen, CUBRID, Tibero, and PostgreSQL.

| DBMS | Required or available fields |
| --- | --- |
| Oracle | DB type, connection name, server IP, port, DB user name, password, Oracle SID, IP protocol, connection test, connection registration, cancel. The Oracle JDBC driver bundled with Migration Center is used. |
| Altibase | DB type, connection name, server IP, port, DB user name, password, JDBC driver file, Altibase DB name, client character set, IP protocol, optional JDBC driver properties, connection test, connection registration, cancel. |
| MS-SQL | DB type, connection name, server IP, port, DB user name, password, JDBC driver file, MS-SQL DB name, IP protocol, optional JDBC driver properties, connection test, connection registration, cancel. |
| MySQL | DB type, connection name, server IP, port, DB user name, password, JDBC driver file, MySQL DB name, IP protocol, optional JDBC driver properties, connection test, connection registration, cancel. |
| Informix | DB type, connection name, server IP, port, DB user name, password, JDBC driver file, Informix DB name, Informix server name, IP protocol, optional JDBC driver properties, connection test, connection registration, cancel. |
| TimesTen | DB type, connection name, server IP, port, DB user name, password, connection type (`client` or `direct`), JDBC driver file, server DSN information, IP protocol, optional JDBC driver properties, connection test, connection registration, cancel. |
| CUBRID | DB type, connection name, server IP, port, DB user name, password, JDBC driver file, CUBRID DB name, optional JDBC driver properties, connection test, connection registration, cancel. |
| Tibero | DB type, connection name, server IP, port, DB user name, password, JDBC driver file, Tibero DB name, connection test, connection registration, cancel. |
| PostgreSQL | DB type, connection name, server IP, port, DB user name, password, JDBC driver file, DB name, DB schema, IP protocol, optional JDBC driver properties, connection test, connection registration, cancel. |

## DBMS Connection List

---

The DBMS connection list shows registered DBMS connections. Users can register a new DBMS, copy a selected DBMS, change input information for a selected DBMS, delete a selected DBMS, and close the list window.

## Creating a Project

---

A project must be created before objects and data can be migrated. Select `Project > Create Project` or click the Create Project icon to open the project creation window.

Project creation requires the project name, project location, source DBMS, and target DBMS. By default, projects are created in the Migration Center `projects` folder. Users can create the project or cancel project creation.

## Opening a Project

---

Open a previously created project by selecting `Project > Open Project`. Migration Center can open only one project for migration at a time.

## Connecting Project Databases

---

To migrate objects and data, open the project and connect the project databases. Select `Project > Connect`, or right-click the project in the Project pane and select `Connect`.

After connection, the Project pane changes to the DB-connected state, the information pane changes from the Prepare step to the Build step, and the full DB connection success log is displayed.

## Migration Options

---

Migration Options are basic settings that affect migration. The two basic migration types are `DB to DB` and `DB to File`. Open Migration Options from `Migration > Migration Options`, or right-click the project in the Project pane and select `Migration Options`.

### DB to DB

---

In `DB to DB` migration, objects and table data from the source DB are migrated directly to the target DB.

| Option | Description |
| --- | --- |
| Execution Thread | Sets the maximum number of threads for data migration. The default is the number of logical CPUs on the Migration Center host multiplied by 3. A value from 1 to logical CPUs multiplied by 3 is recommended. |
| Migration Target | Selects the migration target. `Object & Data` migrates database objects and table data. `Object` migrates only database objects; data must be migrated separately later. |
| Foreign Key Migration | Includes foreign key constraints in the migration target. The default is `No`. |
| PSM Migration | Includes PSM objects such as stored procedures, stored functions, materialized views, views, type sets, and triggers. The default is `Yes`. |
| Drop Existing Objects | Recreates database objects before migration. `Yes` drops and creates target objects. `No` migrates without dropping database objects. The default is `No`. |
| Keep Partition Table | Keeps partitioned tables. `Yes` creates the same partitioned table as the source DBMS when conversion is possible, and requires additional work in `5. Partitioned Table Conversion` during Reconcile. `No` creates a non-partitioned table. The default is `No`. |
| Use Double-quoted Identifier | Specifies whether to use double quotes for database object names. The default is `No`. |
| Remove FORCE from View DDL | Specifies whether to remove the `FORCE` keyword from view creation statements. The default is `Yes`. |
| Postfix for reserved word | Specifies a suffix to add when a source database object name conflicts with an Altibase reserved word. The default is `_POC`. |
| Batch Execution | Enables JDBC batch input for performance. The default is `Yes`. |
| Batch Size | Specifies the batch size when JDBC batch input is used. The default is `10000`. |
| Batch LOB type | Specifies whether to batch process `BLOB` and `CLOB` data types. `Yes` allows batch processing, but memory exhaustion can occur depending on LOB size. An exception can also occur in TimesTen because it does not support batch processing. `No` disallows batch processing. The default is `No`. |
| Log Insert-failed Data | Writes rows that failed to insert during data migration to a log file. This option is enabled only when `Batch Execution` is `No`. The default is `No`. |
| File Encoding | Specifies the character set used when failed records are written to a file. This option is enabled only when `Log Insert-failed Data` is `Yes`. The default is `UTF8`. |
| Operation | Selects the Data Validation operation. `DIFF` checks data differences between source and target databases. `FILESYNC` applies the CSV file generated by `DIFF` to the target database. |
| Write to CSV | Specifies whether to write mismatched data to CSV. |
| Include LOB | Specifies whether to include LOB data when mismatched data is written to CSV. |
| Data Sampling | Specifies whether to use data sampling. `Yes` validates sample data to reduce validation time. `No` validates all data. The default is `Yes`. |
| Percent Sampling (exact counting) | Specifies the sampling percentage for a table. This option is used when `Exact Counting Method` is selected in the Build step. |
| Record Count Sampling (approximate counting) | Specifies the number of records sampled from a table. This option is used when `Approximate Counting Method` is selected in the Build step. |

### DB to File

---

In `DB to File` migration, source DB objects and table data are saved separately as SQL script files, form files, and CSV data files. The saved files are migrated to the target DB by using iSQL and iLoader.

| Option | Description |
| --- | --- |
| Execution Thread | Sets the maximum number of threads for data migration. The default is the number of logical CPUs on the Migration Center host multiplied by 3. A value from 1 to logical CPUs multiplied by 3 is recommended. |
| Migration Target | Selects the migration target. `Object & Data` migrates database objects and table data. `Object` migrates only database objects; data must be migrated separately later. |
| Foreign Key Migration | Includes foreign key constraints in the migration target. |
| PSM Migration | Includes PSM objects such as stored procedures, stored functions, materialized views, views, type sets, and triggers. |
| Keep Partition Table | Keeps partitioned tables. `Yes` creates the same partitioned table as the source DBMS when conversion is possible and requires additional work in Reconcile. `No` creates a non-partitioned table. The default is `No`. |
| Use Double-quoted Identifier | Specifies whether to use double quotes for database object names. |
| Remove FORCE from View DDL | Specifies whether to remove the `FORCE` keyword from view creation statements. |
| Postfix for reserved word | Specifies a suffix to add when a source database object name conflicts with an Altibase reserved word. |
| File Encoding | Specifies the character set used for generated scripts and data files. |

## Running Migration

---

Migration with Migration Center consists of three main phases after preparation: Build, Reconcile, and Run. Data Validation is performed after Run when needed.

### User Migration: Build User Step

---

To migrate all objects and data included in a DB user, select `Build User` in the Build step. Depending on Migration Options, objects only or objects and data are migrated by DB user.

The Build User dialog supports two counting methods. `Approximate counting method` retrieves table record counts by referring to source DBMS statistics, so accuracy depends on the statistics. `Exact counting method` executes the `COUNT` function against every table in the source DBMS to obtain accurate table record counts.

When the Build step completes, Migration Center creates a Build Report for the source DB. The Build Report shows information collected from the source DB and target DB.

### User Migration: Reconcile Step

---

The Reconcile step prepares the migration by adjusting how objects are migrated between the source and target DBs. Users can change default settings while performing migration by DB user.

The Reconcile step includes the following adjustment screens.

| Reconcile screen | Description |
| --- | --- |
| Data Type Mapping | Maps source and target DBMS data types. Select the data type to change, click `Change`, choose the target data type, and optionally set precision and scale for numeric types. Users can reset changes, proceed to the next step, or cancel Reconcile. |
| PSM Data Type Mapping | Maps source and target DBMS PSM data types. The workflow is the same as Data Type Mapping, with an additional option to return to the previous step. |
| Tablespace to Tablespace Mapping | Maps source and target DBMS tablespaces. If no tablespace is selected, the default tablespace is used. The destination default tablespace must be usable by the target DBMS DB user. Mapped tablespaces must be created in the target DBMS before migration. |
| Object to Tablespace Mapping | Changes the tablespace of tables and indexes by drag and drop. |
| Partitioned Table Conversion | Changes partitioned table configuration. Users can select a partitioned table, change the partition type, set the partition key, delete or edit selected partitions, and add partition definitions. It is recommended not to change partition type during migration. List and range partitioned tables in Altibase DB must have a default partition. If `Keep Partitioned Table` is `No`, partitioned tables are migrated as normal tables. |
| Select Editing | Edits the `SELECT` statement used to extract data from source DBMS tables. Users can double-click hints and `WHERE` conditions to insert them, reset changes, return to the previous step, or continue. |
| DDL Editing | Converts preceding PSM-related content, displays object scripts, selects object types and objects, edits scripts, and saves changed scripts. The Save button is enabled only when Destination DDL content has changed. |

The Reconcile step produces a Reconcile Report.

### User Migration: Run Step

---

The Run step copies source DB objects to the target DB or to external files according to Migration Options.

After the Run step completes, execution results are generated in `RunReport4Summary.html`, and detailed information about failed objects is written to `RunReport4Missing.html`.

### Table Migration: Build Table Step

---

`Build Table` migrates only selected table objects and data. As with Build User, users can choose approximate counting based on source DBMS statistics or exact counting with `COUNT` against all source tables.

The table selection window allows users to search table names by keyword, list all tables when no keyword is entered, select tables individually, select all listed tables, add selected tables to the migration list, add more tables later, remove selected tables from the selected table list, build selected tables, and create a Build Report.

### Table Migration: Reconcile Step

---

The Reconcile step for table-level migration adjusts how selected table objects are migrated between the source and target DBs. It uses the same configuration as DB user-level migration. Refer to the DB user-level Reconcile section for details.

### Table Migration: Run Step

---

The table-level Run step copies selected source DB objects to the target DB or to external files according to Migration Options. After completion, `RunReport4Summary.html` contains execution results and `RunReport4Missing.html` contains detailed information about failed objects.

### Data Validation Step

---

The Data Validation step checks whether the data migration performed in the Run step was completed correctly. After validation completes, Migration Center provides a validation report so users can perform follow-up actions. The report lists source and target DB information, validated tables, matching rows, and mismatched rows.

### CLI Mode

---

Migration Center supports both GUI mode and CLI mode. It is generally recommended to configure the migration in GUI mode. For better data migration performance, configure migration through Reconcile in GUI mode, then execute the Run step in CLI mode.

To run CLI mode after GUI configuration:

1. Run Migration Center in GUI mode through the Reconcile step.
2. Upload the full Migration Center folder from GUI mode to any directory on the Linux server.
3. Execute the uploaded migration project with CLI.
4. Run the CLI Run step with:

```sh
./migcenter.sh run [project_path]
```

`[project_path]` must be the absolute path to the project.

# Supported Conversion Objects

---

Migration object support differs by Build method. Objects from source DBMS products that are not supported by Migration Center must be converted manually.

In the Build step, object creation statements are recorded in `SrcDbObj_Create.sql` and `BuildReport4Unsupported.html`; users can refer to these files during conversion work.

## Altibase to Altibase

---

| Object type | Build User | Build Table | Notes |
| --- | --- | --- | --- |
| Table | O | O | Comments specified on tables and columns are also migrated. |
| Primary key constraint | O | O |  |
| Unique constraint | O | O |  |
| Check constraint | O | O |  |
| Foreign key constraint | O | O |  |
| Index | O | O |  |
| Sequence | O | X |  |
| Queue | O | X |  |
| Private synonym | Partial | X | Synonyms that reference objects in other schemas are also migrated. |
| Procedure | Partial | X | The original DDL is executed without separate conversion. |
| Function | Partial | X |  |
| Package | Partial | X |  |
| View | Partial | X |  |
| Materialized view | Partial | X |  |
| Trigger | Partial | X |  |

## Altibase to Oracle

---

| Object type | Build User | Build Table | Notes |
| --- | --- | --- | --- |
| Table | O | O |  |
| Primary key constraint | O | O |  |
| Unique constraint | O | O |  |
| Check constraint | O | O |  |
| Foreign key constraint | O | O |  |
| Index | O | O |  |
| Sequence | O | X |  |
| Queue | X | X | Automatically excluded during Build because no object can be converted. |
| Private synonym | Partial | X | Synonyms that reference objects in other schemas are also migrated. |
| Procedure | Partial | X | The original DDL is executed without separate conversion. |
| Function | Partial | X |  |
| Package | Partial | X |  |
| View | Partial | X |  |
| Materialized view | Partial | X | The original DDL is executed without separate conversion. The base table must have a primary key for migration. |
| Trigger | Partial | X | The original DDL is executed without separate conversion. |

## CUBRID to Altibase

---

| Object type | Build User | Build Table | Notes |
| --- | --- | --- | --- |
| Table | O | O | Comments specified on tables and columns are also migrated. |
| Primary key constraint | O | O |  |
| Unique constraint | O | O |  |
| Foreign key constraint | O | O |  |
| Index | O | O | CUBRID reverse indexes and prefix length indexes are not supported by Altibase. Reverse indexes store key values in reverse order and are not supported. Prefix length indexes index only part of a key value and are replaced with normal Altibase indexes during migration. |
| `auto_increment` | O | O | Migrated as a sequence. |
| Serial | O | X |  |
| Procedure | X | X | Object creation statements collected from the source database during Build are recorded in `SrcDbObj_Create.sql` and `BuildReport4Unsupported.html`. |
| Function | X | X |  |
| View | X | X |  |
| Trigger | X | X |  |

## Informix to Altibase

---

| Object type | Build User | Build Table | Notes |
| --- | --- | --- | --- |
| Table | O | O | Comments specified on tables and columns are also migrated. |
| Primary key constraint | O | O |  |
| Unique constraint | O | O |  |
| Foreign key constraint | O | O |  |
| Index | O | O |  |
| Serial column type | O | O | Migrated as a sequence. |
| Sequence | O | X |  |
| Private synonym | Partial | X | Only synonyms that reference objects in the same schema are migrated. |
| Procedure | X | X | Object creation statements collected from the source database during Build are recorded in `SrcDbObj_Create.sql` and `BuildReport4Unsupported.html`. |
| Function | X | X |  |
| View | X | X |  |
| Trigger | X | X |  |

## MySQL to Altibase

---

| Object type | Build User | Build Table | Notes |
| --- | --- | --- | --- |
| Table | O | O | Comments specified on tables and columns are also migrated. |
| Primary key constraint | O | O |  |
| Unique constraint | O | O |  |
| Check constraint | O | O |  |
| Foreign key constraint | O | O |  |
| Index | O | O |  |
| `auto_increment` column attribute | O | O | Migrated as a sequence. |
| Procedure | X | X | Object creation statements collected from the source database during Build are recorded in `SrcDbObj_Create.sql` and `BuildReport4Unsupported.html`. |
| Function | X | X |  |
| View | X | X |  |
| Trigger | X | X |  |

## Oracle to Altibase

---

| Object type | Build User | Build Table | Notes |
| --- | --- | --- | --- |
| Table | O | O | To migrate temporary tables, a volatile tablespace must exist in Altibase because Altibase temporary tables can be created only in volatile tablespaces. Comments specified on tables and columns are also migrated. |
| Primary key constraint | O | O |  |
| Unique constraint | O | O |  |
| Check constraint | O | O |  |
| Foreign key constraint | O | O |  |
| Index | O | O |  |
| Sequence | O | X |  |
| Private synonym | Partial | X | Only synonyms that reference objects in the same schema are migrated. |
| Procedure | Partial | X | Migration Center converts and attempts to migrate object creation statements according to rules defined in the PSM converter. |
| Function | Partial | X |  |
| Package | Partial | X |  |
| View | Partial | X |  |
| Materialized view | Partial | X |  |
| Trigger | Partial | X |  |

## MSSQL to Altibase

---

| Object type | Build User | Build Table | Notes |
| --- | --- | --- | --- |
| Table | O | O | Comments specified on tables and columns are also migrated. |
| Primary key constraint | O | O |  |
| Unique constraint | O | O |  |
| Check constraint | O | O |  |
| Foreign key constraint | O | O |  |
| Index | O | O |  |
| Identity column attribute | O | O | Migrated as a sequence. |
| Sequence | O | X | SQL Server 2012 is supported. |
| Private synonym | Partial | X | Only synonyms that reference objects in the same schema are migrated. |
| Procedure | X | X | Object creation statements collected from the source database during Build are recorded in `SrcDbObj_Create.sql` and `BuildReport4Unsupported.html`. |
| Function | X | X |  |
| View | X | X |  |
| Trigger | X | X |  |

## TimesTen to Altibase

---

| Object type | Build User | Build Table | Notes |
| --- | --- | --- | --- |
| Table | O | O | To migrate temporary tables to Altibase, a volatile tablespace must exist in Altibase because Altibase temporary tables can be created only in volatile tablespaces. Comments specified on tables and columns are also migrated. |
| Primary key constraint | O | O |  |
| Unique constraint | O | O |  |
| Foreign key constraint | O | O |  |
| Index | O | O | TimesTen indexes do not provide information about sort order (`ASC` or `DESC`) or size. Therefore, index order is migrated as the default value `ASC`, and size is not displayed. Among the three TimesTen index types, hash and range indexes are converted to Altibase B-tree indexes, while bitmap indexes are not supported. If an index column has a primary key or unique constraint, the index is excluded from migration because Altibase does not allow it; check the Missing tab in the Build Report. |
| Sequence | O | X |  |
| Private synonym | Partial | X | Only synonyms that reference objects in the same schema are migrated. |
| Procedure | Partial | X | TimesTen 11.2 is supported. |
| Function | Partial | X |  |
| Package | Partial | X |  |
| View | Partial | X |  |
| Materialized view | Partial | X |  |
| Trigger | Partial | X |  |

## Tibero to Altibase

---

| Object type | Build User | Build Table | Notes |
| --- | --- | --- | --- |
| Table | O | O | To migrate Tibero temporary tables to Altibase, a volatile tablespace must exist in Altibase because Altibase temporary tables can be created only in volatile tablespaces. Comments specified on tables and columns are also migrated. |
| Primary key constraint | O | O |  |
| Unique constraint | O | O |  |
| Check constraint | O | O |  |
| Foreign key constraint | O | O |  |
| Index | O | O | Indexes automatically created on Tibero LOB type columns are not migrated because Altibase does not support them. |
| Sequence | O | X |  |
| Private synonym | Partial | X | Only synonyms that reference objects in the same schema are migrated. |
| Procedure | Partial | X | Migration Center converts and attempts to migrate object creation statements according to rules defined in the PSM converter. |
| Function | Partial | X |  |
| Package | Partial | X |  |
| View | Partial | X |  |
| Materialized view | Partial | X |  |
| Trigger | Partial | X |  |

Tibero procedures, functions, views, materialized views, and triggers are migrated by using a third-party SQL parser for Oracle. Therefore, Tibero-specific syntax that is not compatible with Oracle syntax can cause parsing errors during conversion. In that case, users must manually convert the syntax.

## PostgreSQL to Altibase

---

| Object type | Build User | Build Table | Notes |
| --- | --- | --- | --- |
| Table | O | O | Comments specified on columns are also migrated. PostgreSQL tables can have up to 1,600 columns while Altibase supports up to 1,024 columns, so review this before migration. |
| Primary key constraint | O | O |  |
| Unique constraint | O | O |  |
| Check constraint | O | O |  |
| Foreign key constraint | O | O | `CASCADE`, `NO ACTION`, and `SET NULL` options are migrated with the same option. `RESTRICT` behaves the same as no foreign key option in Altibase, so this option is removed during migration. `SET DEFAULT` is not supported in Altibase, so it is converted to `SET NULL` during migration. |
| Index | O | O | Among PostgreSQL index types, only B-tree and R-tree indexes supported by Altibase are migrated. |
| Sequence | O | X | The PostgreSQL default sequence maximum value `9223372036854775807` is forcibly converted to the Altibase default maximum value `9223372036854775806`. If the PostgreSQL sequence cache size is 1, the `CACHE` clause is removed and the sequence is created with the Altibase default cache size 20. User-created sequences explicitly selected in `Build Table` are excluded from migration, but sequences created for serial data type columns in migration target tables are migrated with the table. |
| Function | X | X | Not supported for migration. Object creation statements collected from PostgreSQL during Build are recorded in `SrcDbObj_Create.sql` and `BuildReport4Unsupported.html`. |
| View | X | X |  |
| Materialized view | X | X |  |
| Trigger | X | X |  |

Objects in PostgreSQL that are not listed in the table, such as exclusion constraints, types, and enums, have no corresponding Altibase object and are excluded from migration.

Original downloadable document: [Migration_Center_사용자가이드.pdf](https://docs.altibase.com/download/attachments/19955861/Migration_Center_%EC%82%AC%EC%9A%A9%EC%9E%90%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=2&modificationDate=1701652961000&api=v2)
