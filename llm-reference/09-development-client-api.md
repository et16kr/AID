# Development and Client API

## Source paths

R017 source paths covered:

- `arch/Home/Altibase Developer Training__22642996.md`
- `arch/Home/Altibase Precompiler Guide__14647438.md`
- `arch/Home/Altibase Precompiler Guide/1. Considerations for ALTIBASE Development__14647447.md`
- `arch/Home/Altibase Precompiler Guide/2. How to use APRE__14647451.md`
- `arch/Home/Altibase Precompiler Guide/3. APRE Sample Program__14647488.md`
- `arch/Home/Altibase Precompiler Guide/5. Considerations when converting from other DBMSs__14647506.md`
- `arch/Home/APRE_C_C++ New Features & Upgrade Guide__22643052.md`
- `arch/Home/Altibase APRE(SES) _C_C++ Makefile__15630378.md`
- `arch/Home/Altibase APRE(SES) _C_C++ Makefile/How to make a basic Makefile__15630382.md`
- `arch/Home/Altibase APRE(SES) _C_C++ Makefile/Makefile for AIX xlc__16252935.md`
- `arch/Home/Altibase APRE(SES) _C_C++ Makefile/Makefile for HP acc__16449546.md`
- `arch/Home/Altibase APRE(SES) _C_C++ Makefile/Makefile for Linux gcc__15630400.md`
- `arch/Home/Altibase APRE(SES) _C_C++ Makefile/Makefile for SUN(Solaris) cc__16678920.md`
- `arch/Home/Altibase APRE(SES) _C_C++ Makefile/Notes_Considerations__16678933.md`

R018 source paths covered:

- `arch/Home/JAVA Developer's Guide__16875544.md`
- `arch/Home/Altibase ODBC Development Guide in Windows Environment__15138911.md`
- `arch/Home/Altibase and unixODBC Integration Guide__14647413.md`
- `arch/Home/Altibase and unixODBC Integration Guide/1. unixODBC Manager Installation__14647417.md`
- `arch/Home/Altibase and unixODBC Integration Guide/2. Integrating unixODBC Manager__14647432.md`
- `arch/Home/Altibase Window ADO.NET Development Guide__14647565.md`
- `arch/Home/Altibase Window ADO.NET Development Guide/1. ADO.NET Settings__14647569.md`
- `arch/Home/Altibase Window ADO.NET Development Guide/2. ADO.NET Development Guide__14647573.md`
- `arch/Home/Altibase Window ADO.NET Development Guide/3. Frequent Error Messages__14647579.md`
- `arch/Home/PHP Integration Guide for Altibase__14647305.md`
- `arch/Home/PHP Integration Guide for Altibase/1. ALTIBASE HDB PHP Module Reference__14647310.md`
- `arch/Home/PHP Integration Guide for Altibase/2. ODBC Manger Installation for PHP Integration__14647312.md`
- `arch/Home/PHP Integration Guide for Altibase/3. PHP Functions for ODBC Connection__14647314.md`
- `FAQE/Home/07. Development and API/Connection disconnection, error codes, and error messages in each case (APRE_C_C++, SQLCLI)__16876167.md`
- `FAQE/Home/07. Development and API/How to manage Spring+iBatis transaction__16876194.md`
- `FAQE/Home/07. Development and API/JDBC/How to change the jdbc.trc file creation location__16876175.md`
- `FAQE/Home/07. Development and API/JDBC/How to use Fail-Over in Altibase JDBC__16876173.md`
- `FAQE/Home/07. Development and API/JDBC/Simultaneous connections to different Altibase versions via JDBC__22642951.md`
- `FAQE/Home/07. Development and API/ODBC/32-bit ODBC installation on 64-bit Windows__22642957.md`
- `FAQE/Home/07. Development and API/ODBC/Integrating with unix_odbc__16876187.md`
- `FAQE/Home/07. Development and API/ODBC/ODBC function, SQLFreeStmt__16876183.md`
- `FAQE/Home/07. Development and API/PHP/Hangul is broken when using php__16876191.md`

Additional source read for the R017 wildcard boundary and cross-reference:

- `arch/Home/Altibase Precompiler Guide/4. Frequently Occurring Error Messages__22643006.md` - detailed SQLCODE/error coverage is canonical in `llm-reference/07-troubleshooting-error-messages.md`; this topic keeps the APRE development cross-reference and the high-level error-handling workflow.

## Source coverage notes

This R017 section covers Altibase APRE*C/C++, SES*C/C++ upgrade boundaries, embedded SQL development patterns, APRE host variables, `sqlca`, connection and transaction control, cursor/FAC handling, dynamic SQL, function/procedure calls, `WHENEVER`, failover connection strings, sample-code cautions, APRE/SES Makefile construction, platform-specific C/C++ link options, and attachment preservation.

`arch/Home/Altibase Developer Training__22642996.md` and `arch/Home/APRE_C_C++ New Features & Upgrade Guide__22643052.md` have attachment evidence in `source-stabilization/url-backed-attachments.tsv` and `source-stabilization/legacy-attachments.tsv`. Their document-format attachments and legacy source limitations are recorded in `llm-reference/coverage/attachment-diagram-register.tsv`.

`arch/Home/Altibase Precompiler Guide/4. Frequently Occurring Error Messages__22643006.md` is read in this job because the R017 wildcard source list includes the whole precompiler guide, but detailed error rows were already produced by R013. Use this document for APRE development context and use `llm-reference/07-troubleshooting-error-messages.md` for the full SQLCODE catalog.

The APRE sample program source includes illustrative code copied from the source. Some lines in the source sample are not compile-ready as written, for example `EXC SQL`, `INTEGE`, mixed `error_do`/`Error_do`, and `AUTOCOMMIT = FALSE:`. Preserve those as source sample cautions; when generating new working code, follow the syntax rules and APRE examples in the procedural sections instead of copying the sample blindly.

The R018 source set covers Java/JDBC, JDBC failover and tracing FAQs, Windows ODBC, unixODBC and SQLLEN/bitness details, ADO.NET, PHP through ODBC, PHP Hangul output troubleshooting, Spring+iBatis LOB transaction handling, and APRE/SQLCLI connection-disconnect error states. R018 document-format attachments and embedded images are registered in `llm-reference/coverage/attachment-diagram-register.tsv`; embedded screenshots are source evidence only and are recorded as `not_document_format`.

`FAQE/Home/07. Development and API/How to manage Spring+iBatis transaction__16876194.md` is owned by R018 because it is a development/API FAQ, even though broader framework integration is covered separately in `llm-reference/10-application-framework-integration.md` by R019. This document preserves the transaction and LOB-specific answerability from the FAQ.

## Scope and audience

Use this document to answer developer, build engineer, DBA, support, and LLM questions about Altibase embedded SQL development in C and C++: choosing APRE options, writing `.sc` files, compiling APRE output, linking `libapre` and `libodbccli`, selecting platform libraries, diagnosing Makefile errors, handling host variables and NULL indicators, controlling connections and transactions, avoiding fetch-across-commit errors, and upgrading from SES*C/C++ to APRE*C/C++.

Also use this document for Java/JDBC driver setup, connection URLs, connection pools, XA, failover, simultaneous driver-version connections, JDBC trace behavior, ODBC DSN setup on Windows and Unix, unixODBC compilation and SQLLEN compatibility, ADO.NET DLL/reference setup and classes, PHP ODBC setup, PHP character-set troubleshooting, and development/API FAQ error-state variants.

When answering in another language, keep product names, command names, compiler options, SQL keywords, file names, library names, paths, connection-string keys, error codes, and sample identifiers exactly as written.

## Key facts

### APRE and SES terminology

`APRE*C/C++` is the Altibase C/C++ precompiler for embedded SQL in Altibase 5.3.3 or later. `SES*C/C++` is the older embedded SQL precompiler for Altibase 5.1.5 or earlier. The APRE executable is `apre`; source files normally use the `.sc` extension and are precompiled into C or C++ source before normal compilation.

The parent precompiler guide is based on Altibase version 6 or later and Linux `2.6.32-504.el6.x86_64`. The APRE New Features & Upgrade Guide is based on APRE*C/C++ for Altibase 7.3. The Makefile guide examples use Altibase version 6 or later, Linux `2.6.32-504.el6.x86_64`, and GCC `4.4.7 20120313 (Red Hat 4.4.7-11)`.

The development training page is a basic programming guide and preserves these downloadable documents:

- Altibase v7 or later training document: [Altibase_Developer_Training_v1.pptx](https://docs.altibase.com/download/attachments/22642996/Altibase_Developer_Training_v1.pptx?version=1&modificationDate=1761004797000&api=v2)
- Legacy Altibase v5 training document: [D33_ALTIBASE5 Developer Training.pdf](https://docs.altibase.com/download/attachments/19333461/D33_ALTIBASE5_%EA%B0%9C%EB%B0%9C%EC%9E%90%EA%B5%90%EC%9C%A1.pdf?version=2&modificationDate=1697612224000&api=v2)
- Korean source training PPTX: [Altibase_개발자교육_v1.pptx](https://docs.altibase.com/download/attachments/19333461/Altibase_%EA%B0%9C%EB%B0%9C%EC%9E%90%EA%B5%90%EC%9C%A1_v1.pptx?version=5&modificationDate=1759191535000&api=v2)

### APRE source and generated files

Precompile `.sc` source with `apre`. Use `-t cpp` to generate C++ source and `-t c` when a C compiler needs C output.

```bash
apre -mt -t cpp connect1.sc
```

When the command succeeds, the generated file appears in the current directory and the prompt returns without an error. The source example says `sample.cpp`; for `connect1.sc` with `-t cpp`, expect a generated C++ source such as `connect1.cpp`.

Header files are under `$ALTIBASE_HOME/include`, and libraries are under `$ALTIBASE_HOME/lib`. Basic APRE linking uses:

```text
-lapre -lodbccli
```

The Makefile guide says Altibase Makefile usage follows the GNU specification and recommends `gmake`.

### APRE host variables and `sqlca`

Before Altibase 5.3.3, host variables had to be declared between `EXEC SQL BEGIN DECLARE SECTION` and `EXEC SQL END DECLARE SECTION`. Starting with Altibase 5.3.3 or later, APRE can recognize normal variables as host variables through the `apre -parse full` option.

For character host variables, include an extra byte for NULL padding. For a database column declared as `CHAR(10)`, declare the host variable in a form such as:

```c
char C1[10 + 1];
```

The precompile `-n` option can omit the extra byte, but then user code must control the clear length of the `char` host variable.

ALTIBASE precompilers use `?` as parameter markers and `:` before host variables in embedded SQL source:

```c
sprintf("delete from sample_table where column1 = ?");
EXEC SQL SELECT CAST(:H_INT AS INTEGER) + Column1 INTO :H_Out FROM T1;
```

`sqlca` is available without a separate declaration. Use `sqlca.sqlcode` to decide success or failure and log `SQLCODE` for debugging. Error code values are defined in `$ALTIBASE_HOME/msg/manual.txt`.

| Identifier | Meaning |
| --- | --- |
| `sqlca.sqlcode` | Error code used to determine SQL success or failure |
| `SQLCODE` | Altibase internal error code, for example `-69720` |
| `SQLSTATE` | CLI-standard character error code, for example `08S01` |
| `sqlca.sqlerrm.sqlerrmc` | Error message text |
| `sqlca.sqlerrd[2]` | DML processed-row count; for SELECT with host-variable arrays, number of array entries fetched in the current fetch |

Predefined values include:

| Error value | Code | Meaning |
| --- | ---: | --- |
| `SES_DUPKEY_ERR` | `-69720` | Duplicate index value |
| `SQL_ERROR` | `-1` | SQL processing error |
| `SQL_INVALID_HANDLE` | `-2` | Internal object required for SQL processing has an error |
| `SQL_NO_DATA` | `100` | No target data |
| `SQL_SUCCESS` | `0` | Processing succeeded |
| `SQL_SUCCESS_WITH_INFO` | `1` | Processing succeeded with user-confirmation information |

### Connections, threads, and transaction control

Altibase does not use a separate listener configuration for APRE connections; the source connects directly to an internal DBMS thread by specifying server IP and port in the connection option.

```c
sprintf(usr, "sys");
sprintf(pwd, "manager");
sprintf(opt, "DSN=127.0.0.1;PORT_NO=20300;CONNTYPE=1");
EXEC SQL CONNECT :usr IDENTIFIED BY :pwd USING :opt;
```

`CONNTYPE` selects the connection method:

| Value | Method | Use and restriction |
| --- | --- | --- |
| `CONNTYPE=1` | TCP/IP | Program and DBMS communicate over TCP/IP. |
| `CONNTYPE=2` | Unix domain | Local-only; recommended when the program is on the same server and lower communication cost is required. |
| `CONNTYPE=3` | IPC | Local-only; requires `IPC_CHANNEL_COUNT` in `$ALTIBASE_HOME/conf/altibase.properties` to be at least `1`, requires DB restart, and requires sufficient IPC-related kernel settings. |

ALTIBASE does not guarantee inter-thread protection for connection objects. Use one connection per thread or implement concurrency control when multiple threads access one connection. Without this, errors can include:

```text
Invalid request to process the SQL statement
Communication link failure (EXEC->PREP)
Communication link failure (PREP->EXEC)
Communication link failure (EXEC->INVL)
Connection does not exist
```

Name connections explicitly with `EXEC SQL AT` when needed:

```sql
EXEC SQL AT CONN1 CONNECT ...
EXEC SQL AT :ConnName CONNECT ...
```

Disconnect forms are:

```sql
EXEC SQL DISCONNECT;
EXEC SQL AT CONN1 DISCONNECT;
EXEC SQL AT :ConnName DISCONNECT;
```

If abnormal connection termination occurs, run `EXEC SQL FREE` before reconnecting. `DISCONNECT` in non-auto-commit mode commits the immediately preceding normally processed transaction unless the application explicitly rolls it back first.

Commit and rollback forms include:

```sql
EXEC SQL COMMIT;
EXEC SQL ROLLBACK;
EXEC SQL AT CONN1 COMMIT;
EXEC SQL AT :ConnName COMMIT;
```

Altibase basically operates in auto-commit mode unless configuration is changed. To use non-auto-commit mode, set `AUTO_COMMIT = 0` in `$ALTIBASE_HOME/conf/altibase.properties` or run:

```sql
EXEC SQL AUTOCOMMIT OFF;
```

After switching to non-auto-commit mode, perform explicit `COMMIT` or `ROLLBACK`.

Starting with Altibase version 5, explicit commit or rollback is not needed for ordinary `SELECT` statements. LOB handling is different: access LOB data in non-auto-commit mode and explicitly commit or roll back afterward. If auto-commit is used for LOB access, source examples include:

```text
Connection is in autocommit mode. One can not operate on LOB datas with autocommit mode on
LobLocator can not span the transaction 34734145
```

Failure to commit or roll back after LOB access can keep locks and cause resource failure.

### Cursor and FAC behavior

The normal cursor order is:

```text
PREPARE -> DECLARE -> OPEN -> FETCH -> CLOSE
```

For static cursor code, declare, open, fetch until `SQL_NO_DATA`, and then close:

```c
EXEC SQL DECLARE CURSOR1 CURSOR FOR SELECT C1, C2 FROM TEST1 WHERE C1 >= :H_Condition;
EXEC SQL OPEN CURSOR1;
EXEC SQL FETCH CURSOR1 INTO :O_C1, :O_C2;
EXEC SQL CLOSE CURSOR1;
```

Altibase follows the ANSI rule for fetch-across-commit behavior. In non-auto-commit mode, committing or rolling back while fetching can close the opened cursor internally. If a change transaction must occur during fetch, use auto-commit, use a separate connection object, or use `WITH HOLD` where supported.

FAC error variants from the source:

| Version | Error code | Message |
| --- | --- | --- |
| Altibase 4.3.9 | `ERR-4103C` | `Request of fetching data to an unprepared SQL statement.` |
| Altibase 5.3.3 through 6.1.1 | `100` | No message listed in the source table. |
| Altibase 6.3.1 or later | `ERR-410D2` | `Request of fetching data to an unprepared SQL statement.` |

Starting with Altibase 6.3.1 or later, a cursor declared with `WITH HOLD` remains open after `COMMIT` or `ROLLBACK` if the session is in non-auto-commit mode:

```sql
EXEC SQL AUTOCOMMIT OFF;
EXEC SQL DECLARE CURSOR1 CURSOR WITH HOLD FOR SELECT * FROM DEPARTMENT;
```

When using a separate connection inside a fetch loop, consider the transaction boundary. If the business rule requires all-or-nothing processing in one transaction, place commit/rollback outside the fetch loop.

### Dynamic SQL, functions, procedures, and `WHENEVER`

Dynamic SQL uses a separate `char*` variable and `PREPARE` when the table name, column list, or search condition is not fixed.

```c
sprintf(sql_text, "insert into test_table values (?, ?)");
EXEC SQL PREPARE STMT1 FROM :sql_text;
EXEC SQL EXECUTE STMT1 USING :H_var1, :H_var2;
```

Starting with Altibase 5.1 or later, execution plans executed by all sessions are shared internally in the Plan-Cache. Dynamic SQL that changes the query string every time cannot reuse an existing Plan-Cache entry and is slower than static SQL because it repeatedly runs prepare/execute processing.

Built-in or user-created functions can be called in `SELECT`:

```sql
EXEC SQL SELECT TO_CHAR(SYSDATE, 'yyyy-mm-dd hh:mi:ss') INTO :H_day FROM dual;
EXEC SQL SELECT user_func(1, 2) INTO :H_value FROM dual;
```

When a function returns `CHAR` or `VARCHAR`, specify the returned length. If omitted, only 1 byte is returned and `Invalid length of the data type` can occur.

Procedures use an embedded block:

```sql
EXEC SQL EXECUTE
BEGIN
       user_proc(:in_param1 in, :in_param2 out);
END;
END-EXEC;
```

`WHENEVER` must be declared before the embedded SQL statement it controls. Conditions and actions include:

| Condition | Meaning |
| --- | --- |
| `NOT FOUND` | `sqlca.sqlcode` is `SQL_NO_DATA` |
| `SQLERROR` | `sqlca.sqlcode` is `SQL_ERROR` |

| Action | Meaning |
| --- | --- |
| `CONTINUE` | Ignore the error and continue |
| `DO user_function` | Execute a user-defined function |
| `DO BREAK` | Exit the loop; valid only inside a loop |
| `DO CONTINUE` | Continue from the top of the loop; valid only inside a loop |
| `GOTO Label` | Jump to a user label |
| `STOP` | Disconnect and close the program |

Examples:

```sql
EXEC SQL WHENEVER SQLERROR DO user_function();
EXEC SQL WHENEVER SQLERROR STOP;
EXEC SQL WHENEVER SQLERROR GOTO ERROR_ROUTINE;
EXEC SQL WHENEVER SQLERROR CONTINUE;
```

### Failover and current connection checks

Altibase does not provide an active call that returns the connection-object status. Detect connection termination by checking `SQLSTATE` after executing a query. The user-code failover example checks `08001`, `08S01`, and `08003`, runs `EXEC SQL FREE`, and then reconnects to the opposite server.

Starting with Altibase 5.3.3 or later, Altibase provides CTF (`Connection Time Failover`) and STF (`Service Time FailOver`). CTF applies when the program first attempts to connect. STF applies to a connection failure while executing a query after connection. These functions do not support transaction failover; application business logic must be retried.

Example connection-string keys:

```text
DSN=127.0.0.1;
AlternateServers=(128.0.0.1:20300,128.0.0.2:20301);
ConnectionRetryCount=3;
ConnectionRetryDelay=10;
SessionFailOver=on;
LoadBalance=off
```

| Item | Meaning |
| --- | --- |
| `AlternateServers` | Target failover servers in `IP:PORT` form, separated by commas, in order. |
| `ConnectionRetryCount` | Number of connection attempts for one target server. |
| `ConnectionRetryDelay` | Sleep interval in seconds before retry. |
| `SessionFailOver` | Whether to connect automatically to a listed alternate server when an SQL error occurs during service time. |
| `LoadBalance` | If `on`, randomly selects the initial server from `DSN` and `AlternateServers`; if `off`, uses `DSN` first and then the alternate list order. |

If an error occurs at cursor open and reprocessing is required, close and release the cursor before reprocessing:

```sql
EXEC SQL CLOSE RELEASE CURSOR1;
```

### APRE new features and option behavior

APRE*C/C++ adds or improves:

- Partial C Preprocessor support for macro processing.
- C Parser support for host variable declarations.
- Library rewrite to relax host variable declaration and usage restrictions.
- `DECLARE STATEMENT`.
- Function calls in `WHENEVER`.
- Changed or added `apre` command options.
- Changed error-message output.
- `RETURNING INTO`.
- `FREE` is no longer supported; use `DISCONNECT` instead.

The partial C preprocessor handles macros such as `#include`, `#define`, `#if`, `#ifdef`, `#ifndef`, `#endif`, `#else`, and `#elif`.

The C Parser allows host variable declarations outside `DECLARE SECTION` only when the source is C. C++-style source can have parsing errors in `-parse full`; for C++-style source, declare host variables inside `DECLARE SECTION` and use `-parse partial` or `-parse none`.

Host variable improvements include:

- Assigning an initial value while declaring a host variable.
- Defining a structure after `typedef`, or in the reverse order.
- Addressing array elements of array-type host variables in embedded SQL.
- Using pointer host variables for data types other than `char*` and `struct*`.
- Using output host variables without `:` in the `INTO` clause of a `SELECT`.
- Using a non-array input host variable with embedded SQL containing a `FOR` clause.
- Using a union type host variable.

`DECLARE STATEMENT` lets SQL statement or PL/SQL block identifiers be declared for use by other embedded SQL statements:

```sql
EXEC SQL DECLARE my_statement STATEMENT;
EXEC SQL DECLARE emp_cursore CURSOR FOR my_statement;
EXEC SQL PREPARE my_statement FROM :my_string;
```

APRE option changes and additions:

| Option | Meaning |
| --- | --- |
| `-I` | New name for SES*C/C++ `-include`; specifies the path of included source files during precompile and is equivalent to `EXEC SQL OPTION (INCLUDE=library_path)`. |
| `-D` | Declares a macro during preprocessing, like `#define` in source. |
| `-keyword` | Shows reserved keywords. |
| `-parse none` | Processes internal SQL only; behaves like SES*C/C++; does not process `#include` header files. |
| `-parse partial` | Processes internal SQL and macros; this is the APRE*C/C++ default. |
| `-parse full` | Processes internal SQL, macros, external declarations, and host variables; C++-style source cannot recognize host variables outside `DECLARE SECTION`. |

Examples:

```bash
apre -t cpp -I$APP_HOME/include/main tmp.sc
apre -DALTIBASE -DOTHER_DBMS -t cpp tmp.sc
apre -keyword
apre -t c -parse none main.sc
```

If the cause of an APRE error is not clear during SES-to-APRE migration, try `-parse none` to precompile in the same style as SES*C/C++ and isolate macro-processing effects.

### SES-to-APRE upgrade facts

The upgrade guide records these name changes:

| Classification | SES*C/C++ | APRE*C/C++ | Path |
| --- | --- | --- | --- |
| Execution file | `sesc` | `apre` | `$ALTIBASE_HOME/bin` |
| Header file | `ses.h` | `ulpLibInterface.h` | `$ALTIBASE_HOME/include` |
| Library file | `libsesc.a` | `libapre.a` | `$ALTIBASE_HOME/lib` |
| Shared library | `libsesc_sl.so` | `libapre_sl.so` | `$ALTIBASE_HOME/lib` |
| Link option | `-lsesc` | `-lapre` | Not path-specific |
| Include option | `-include` | `-include` or `-I` | Not path-specific |

The changes are backward compatible, but the source recommends changing the execution file name and link option to the APRE*C/C++ style for maintenance. It is also recommended to change `-include` to `-I`.

APRE requires a semicolon terminator for `EXEC SQL BEGIN/END DECLARE/ARGUMENT SECTION`. Missing the terminator can produce:

```text
[ERR-302L : EXEC SQL END DECLARE SECTION is not exist.]
```

Binary type names changed from `SES_CLOB`, `SES_BLOB`, `SES_BINARY`, `SES_BYTES`, and `SES_NIBBLE` to `APRE_CLOB`, `APRE_BLOB`, `APRE_BINARY`, `APRE_BYTES`, and `APRE_NIBBLE`. The old names remain usable for backward compatibility.

Do not use the precompiler library interface directly. The source says this internal interface changes frequently, arbitrary direct use of related macros, structures, and functions is prohibited, and Altibase is not responsible for future errors caused by such use.

### APRE sample programs

Sample APRE sources are under:

```text
$ALTIBASE_HOME/sample/APRE
```

The sample categories include:

| Category | Sample source names |
| --- | --- |
| Cursor usage | `cursor1.sc`, `cursor2.sc` |
| DB connection | `connect1.sc`, `connect2.sc` |
| DML usage | `select.sc`, `insert.sc`, `delete.sc`, `update.sc` |
| Dynamic SQL | `dynamic1.sc`, `dynamic2.sc`, `dynamic3.sc` |
| Failover | `Fail-Over/FailOverSample.sc` |
| LOB usage | `BLOB/blobSample.sc`, `CLOB/clobSample.sc` |
| Multi-connection | `mc1.sc`, `mc2.sc` |
| PSM/function | `ps1m.sc`, `psm2.sc` |
| Thread development | `mt1.sc`, `mt2.sc` |
| Host variables | `arrays1.sc`, `arrays2.sc`, `pointer.sc`, `date.sc`, `varchar.sc`, `binary.sc` |

The source sample combines separate-connection and cursor-fetch ideas: one connection fetches from `TABLE_A`, and a second named connection performs updates against `TABLE_B`. Treat that sample as an illustration of the separate-connection pattern, not as a clean compile-ready source without review.

### Conversion from other DBMS precompiler code

When converting from another DBMS:

| Area | Altibase guidance |
| --- | --- |
| `CONNECT`/`DISCONNECT` | Use `EXEC SQL CONNECT [AT :con_name] :usr IDENTIFIED BY :pwd USING :opt;`. |
| Function arguments | Use `EXEC SQL BEGIN ARGUMENT SECTION` or copy argument values into host variables declared in `DECLARE SECTION`. |
| Error codes | `sqlca.sqlcode`, `SQLCODE`, and `SQLSTATE` are available without separate declaration; convert DBMS-specific error-code handling appropriately. |
| Host variables | Altibase 5.3 or later can omit the declaration clause depending on the `apre` option; Altibase 5.3.3 or later supports host variable initialization. |
| Header paths | Use `EXEC SQL INCLUDE "../user_header.h";` or `EXEC SQL OPTION (INCLUDE=/absolute/path/); EXEC SQL INCLUDE user_header.h;`. |
| Header host variables | Use conditional declaration such as `#ifdef SESC_DECLARE`. |
| Omitted `INTO` clause in `SELECT` | Not supported. |
| `SET TRANSACTION ...` | Not supported. |

### Java and JDBC driver setup

The Java developer guide is based on Altibase version 6.5.1, JRE or JDK version 1.5, and Eclipse. The source states that Java applications need an Altibase JDBC driver under `$ALTIBASE_HOME/lib`.

| Driver file | Use |
| --- | --- |
| `Altibase.jar` | General JDBC driver for Altibase DB integration or multiple Altibase servers of the same version. |
| `Altibase6_5.jar` | JDBC driver used when integrating Altibase version 5 or earlier. |
| `Altibase5.jar` | Additional driver in older multi-version examples; driver class `Altibase5.jdbc.driver.AltibaseDriver`. |
| `Altibase7_3.jar` | Additional driver in the 2025 FAQ for simultaneous Altibase 7.1 and 7.3 connections; driver class `Altibase7_3.jdbc.driver.AltibaseDriver`. |

Check JDBC driver compatibility by comparing the JDBC driver's CMP value with the server cm protocol version:

```bash
java -jar Altibase.jar
altibase -v
```

Example JDBC driver output from the source:

```text
JDBC Driver Info : Altibase Ver = 6.5.1.5.10 for JavaVM v1.4, CMP:7.1.3, Sep  6 2018 09:17:52
```

Example server output includes `cm protocol version 7.1.3`. The source recommends using the latest Altibase JDBC driver file of the same or later version than the Altibase DB server version.

To make `Altibase.jar` visible to Java:

- Add `$ALTIBASE_HOME/lib/Altibase.jar` to `CLASSPATH`, for example in `.profile` or `.bash_profile`.
- Place `Altibase.jar` in `$JAVA_HOME/jre/lib/ext` or `$JRE_HOME/lib/ext`.
- Run Java with `-cp` or `-classpath`, for example `java -classpath $ALTIBASE_HOME/lib/Altibase.jar HelloApp`.
- In Eclipse, edit the installed JRE and add `$ALTIBASE_HOME/lib/Altibase.jar` as an external JAR.

### JDBC connection, pool, XA, and failover facts

The JDBC driver class is:

```java
Class.forName("Altibase.jdbc.driver.AltibaseDriver");
```

The normal JDBC URL form is:

```text
jdbc:Altibase://ip_address:port_no/db_name
```

`port_no` is the Altibase port defined by `PORT_NO` in `$ALTIBASE_HOME/conf/altibase.properties`, and `db_name` is the DB name from `DB_NAME` in `$ALTIBASE_HOME/conf/altibase.properties`. The DB name can be checked with:

```sql
SELECT DB_NAME FROM V$DATABASE;
```

Connection properties can be passed through `java.util.Properties` or appended to the URL as query parameters:

```java
String db_url1 = "jdbc:Altibase://192.168.1.111:20300/mydb";
Properties props1 = new Properties();
props1.put("user", "sys");
props1.put("password", "manager");
Connection altibaseConnection1 = DriverManager.getConnection(db_url1, props1);
```

```java
String db_url1 = "jdbc:Altibase://192.168.1.111:20300/mydb?user=sys&password=manager";
Connection altibaseConnection1 = DriverManager.getConnection(db_url1);
```

JDBC connection properties from the source include:

| Property name | Description | Default value |
| --- | --- | --- |
| `portNumber` | DB `PORT_NO` | `20300` |
| `databaseName` | DB name | `JDBC` |
| `user` | DB user name | `SYS` |
| `password` | DB password | `MANAGER` |
| `serverName` | DB server IP | `localhost` |
| `connType` | Connection type: `1` TCP/IP, `3` IPC | `1` |

For connection pools, Altibase 6.3.1 or later uses `AltibaseConnectionPoolDataSource`; Altibase 6.1.1 uses `ABPoolingDataSource`. Both are in the `Altibase.jdbc.driver` package. Pool properties include `url`, `user`, `password`, `maxPoolSize`, `minPoolSize`, `initialPoolSize`, `maxIdleTime`, and `propertyCycle`.

For XA distributed transactions, Altibase 6.3.1 or later uses `AltibaseXADataSource` and `AltibaseXAResource`. Altibase 6.1.1 uses `ABXADataSource` and `ABXAResource`. The sample flow gets an `XAConnection`, gets the physical `Connection`, and then gets the `XAResource`.

Starting from Altibase 5.3.3, JDBC failover properties can be defined in the URL:

```text
jdbc:Altibase://192.168.1.1111:20300/mydb?alternateservers=(192.168.1.1111:20300,192.168.1.222:20300)&connectionretrycount=3&connectionretrydelay=3&sessionfailover=off&loadbalance=off
```

The JDBC failover FAQ says failover connection-property names are case insensitive and adds these details:

| Property | Meaning |
| --- | --- |
| `AlternateServer` or `alternateservers` | Alternate servers in `(IP1:Port1, IP2:Port2,...)` format. |
| `ConnectionRetryCount` | Number of connection retries to the same server. |
| `ConnectionRetryDelay` | Wait time in seconds before retrying the same server. |
| `LoadBalance` | `ON` randomly tries primary and alternate servers; `OFF` tries the primary first, then alternates in listed order. |
| `SessionFailOver` | `ON` means CTF plus STF; `OFF` means only CTF. The Java guide says Altibase recommends CTF. |
| `FailOver_Source` | Description of the failover source stored in `V$SESSION.FAILOVER_SOURCE`. |
| `HealthCheckDuration` | Seconds before a failed server is added back to the available-server list. |

CTF is `Connection Time Fail-Over`, when failure is detected during connection and another available node is tried. STF is `Service Time Fail-Over`, when failure is detected during service after the DBMS had already connected. For STF, the application must prepare the statement again and continue from the statement-preparation stage. To check failover success, use exception handling: `SQLException.getSQLState()` returns `08F01` for Altibase 6.3.1 or later, and `ES_08FO01` for Altibase 6.1.1 or earlier.

### JDBC simultaneous version connections and traces

Starting from Altibase version 5 or later, additional JDBC driver files allow one Java application to connect to different Altibase versions at the same time. In the older Java guide, load `Altibase5.jdbc.driver.AltibaseDriver` first, then `Altibase.jdbc.driver.AltibaseDriver`. In the 2025 FAQ based on Altibase 7.3, use `Altibase7_3.jar` from the 7.3 `$ALTIBASE_HOME/lib` and `Altibase.jar` from the 7.1 `$ALTIBASE_HOME/lib`:

```java
Class.forName("Altibase7_3.jdbc.driver.AltibaseDriver");
Class.forName("Altibase.jdbc.driver.AltibaseDriver");
String db_url1 = "jdbc:Altibase://192.168.1.111:20300/mydb";
String db_url2 = "jdbc:Altibase://192.168.1.222:20300/mydb";
```

Check the 7.3 additional driver with:

```bash
java -jar Altibase7_3.jar
```

Expected form:

```text
Altibase 7.3.0.1.0 with CMP 7.1.8 for JDBC 4.2 compiled with JDK 8
```

For IBM Java 1.6, the Java guide says `DriverManager` handles exceptions immediately without retrying. Include the cm protocol version in the connection string:

```java
String db_url1 = "jdbc:Altibase_5.6.2://192.168.1.111:20300/mydb";
String db_url2 = "jdbc:Altibase_4.5.1://192.168.1.222:20300/mydb";
```

The `jdbc.trc` FAQ says `jdbc.trc` is created from ALTIBASE HDB 5.5.1 or later when the JDBC driver is initialized. If failover is in the connection URL, it records failover event traces. If failover is not configured or does not occur, the file remains 0 bytes or at its initial size. Concurrent Java program executions create files such as `jdbc.trc`, `jdbc.trc.lck`, `jdbc.trc.1`, `jdbc.trc.1.lck`, `jdbc.trc.2`, and `jdbc.trc.2.lck`. Multiple connection objects in one Java program share the same `jdbc.trc`.

If `ALTIBASE_HOME` is set on the client, `jdbc.trc` is created under `$ALTIBASE_HOME/trc`; otherwise it is created where the Java program is executed. If write permission is missing, the application can fail with:

```text
java.io.IOException: Couldn't get lock for /opt/altibase-HDB-server-6.1.1/trc/jdbc.trc
```

The FAQ's version-specific trace controls are:

| ALTIBASE HDB version | Trace creation control |
| --- | --- |
| 6.1.1.1.3 or earlier | Not available. |
| 6.1.1.1.4 through 6.1.1.1.7 | Run Java with `java -DALTIBASE_JDBC_TRCLOG_DISABLE=true`. |
| 6.1.1.1.8 or later | Run Java with `java -DALTIBASE_JDBC_TRCLOG_DISABLE=true` or set `export ALTIBASE_JDBC_TRCLOG_DISABLE=true` for the Java execution user. |

### Java development cautions and procedures/functions

Use `PreparedStatement` for bind-execute statements that insert many rows or repeatedly select by a parameter. Use `executeBatch()` for bulk DML so rows are sent to the server as an array instead of one network round trip per `executeUpdate()`.

Use `setFetchSize()` to control how many records are fetched from the DB server at once, but avoid unnecessarily large values because client memory increases in proportion to fetch size. The source example says records of 5000 bytes with `setFetchSize(1000)` instead of `setFetchSize(10)` increase memory use by about `5000 * (1000 - 10) = 4950K bytes`.

Always close `Connection`, `Statement`, and `ResultSet` objects. Unclosed `Statement` and `PreparedStatement` objects keep prepared SQL contents on the DB server and increase memory use.

For NULLs in `PreparedStatement`, use `setObject(parameterIndex, null, SQLType.NULL)` or `setNull(parameterIndex, null)` as recorded in the source. Altibase does not support `setObject(parameterIndex, null)`.

JDBC LOB processing requires `autocommit` off. Because JDBC defaults to autocommit on, call `setAutoCommit(false)` on the `Connection` before LOB processing. If autocommit remains on, the source records this error or an unwanted null return:

```text
Connection is in autocommit mode. One can not operate on LOB datas with autocommit mode on
```

LOB examples are under `$ALTIBASE_HOME/sample/JDBC/CLOB` and `$ALTIBASE_HOME/sample/JDBC/BLOB`.

Stored procedure and function call forms are:

```text
{ call procedure_name(?,?,....) }
{ call ? := function_name(?,?,....) }
```

The Java REF CURSOR example defines a `TYPESET`, opens the cursor in a procedure, calls it with `prepareCall`, passes the SQL text, executes, then reads `getResultSet()`.

### Windows ODBC development

The Windows ODBC guide is based on Altibase version 6.5.1 and Windows 10. Windows ODBC is provided only up to Altibase version 6.5.1 and is not provided starting from Altibase version 7.1.0.

Download Windows ODBC files from `http://support.altibase.com` under Downloads -> Products. For older versions not available on the website, contact `support@altibase.com`. First-time installation uses the Windows Client package.

Register an Altibase ODBC driver through Start -> Control Panel -> Management Tools -> ODBC Data Source (64-bit) -> Add, select `ALTIBASE_HDB_ODBC_64bit`, and enter connection settings. The Altibase DB server must be running before using Test Connection.

| DSN field | Meaning | Example |
| --- | --- | --- |
| Windows DSN Name | DSN display name | `SERVER1` |
| Host (name or IP) | Altibase DB server host | `192.168.1.35` |
| Port | Altibase DB server port | `20300` |
| User | DB account | `sys` |
| Password | DB account password | `manager` |
| DB Name | `DB_NAME` created at DB creation time | `mydb` |
| `NLS_USE` | DB character set | `MS949` |

ODBC applications on Windows generally require headers such as `windows.h`, `sql.h`, `sqlext.h`, and `afxdb.h`, and libraries such as `odbc32.lib`. Source conversion is normally not needed; change the connection part to use the Altibase ODBC connection string:

```text
DRIVER=ALTIBASE_HDB_ODBC_64bit;user=sys;password=manager; Server=127.0.0.1;PORT=20300;NLS_USE=MS949;LongDataCompat=on
```

Set `LongDataCompat=on` when using large data such as BLOB. ODBC LOB processing should run in non-auto-commit mode. The Windows ODBC source shows C# BLOB insert using `OdbcTransaction tx = cn.BeginTransaction()`, parameter binding with `OdbcType.Binary`, and `tx.Commit()`. For BLOB select, it uses `SELECT binary_length(C2), C2 FROM T1`, `OdbcDataReader.GetBytes`, and writes the byte array to `c:\test.dat`.

The 32-bit ODBC FAQ covers Windows Server 2003 64-bit systems and applies through Altibase 6.5.1. Starting from version 7.1, 32-bit ODBC drivers are no longer supported. To configure 32-bit ODBC on 64-bit Windows, install the 32-bit client or ODBC package, run `C:\windows\sysWOW64\odbcad32.exe`, create a data source, and enter server connection information. Check the server port from `PORT_NO` in `altibase.properties` or the server-side `ALTIBASE_PORT_NO` environment variable. Check database name and character set with:

```sql
SELECT DB_NAME FROM V$DATABASE;
SELECT NLS_CHARACTERSET FROM V$NLS_PARAMETERS;
```

### unixODBC integration and SQLLEN compatibility

The unixODBC integration guide is based on Altibase 6.3.1, Linux `2.6.32-504.el6.x86_64`, and unixODBC 2.3.2. It assumes native compilers. Installing unixODBC and preparing its build environment are generally user responsibilities, so Altibase does not generally provide technical support for that part.

The Altibase Unix ODBC driver file name includes `ul32` or `ul64`, but that does not mean the file's 32-bit or 64-bit ELF bitness. It indicates SQLLEN size: `ul32` uses SQLLEN 4 bytes, and `ul64` uses SQLLEN 8 bytes. The actual file bitness is shown by `file`, for example:

```bash
file $ALTIBASE_HOME/lib/libaltibase_odbc*
```

The unixODBC manager bit type and the ODBC driver bit type must match. If unixODBC is compiled 64-bit, use a 64-bit Altibase ODBC driver. If unixODBC is compiled 32-bit, use the 32-bit Altibase ODBC driver from the Altibase 32-bit client package.

The guide strongly recommends SQLLEN and SQLULEN as 32-bit by setting:

```bash
export CFLAGS=-DBUILD_LEGACY_64_BIT_MODE=1
```

If SQLLEN/SQLULEN are 64-bit, value-transfer errors can occur between unixODBC and Altibase. In PHP or Python, values transferred through functions such as `SQLColAttribute` may be calculated incorrectly, and `SQLfetch()` or `SQLMoreResult()` can intermittently return incorrect values when the application and unixODBC manager disagree on SQLLEN size.

Build environment variables used to select bitness include `CFLAGS`, `LDFLAGS`, `CC`, and `CXX`. On 64-bit Linux, a source example for 32-bit unixODBC with SQLLEN 4 bytes is:

```bash
export CFLAGS="-m32 -DBUILD_LEGACY_64_BIT_MODE=1"
export LDFLAGS=-m32
export CXXFLAGS=-m32
```

Platform examples from the source:

| Platform | Compiler and bitness notes |
| --- | --- |
| AIX | `OBJECT_MODE=64`, `/usr/vac/bin/xlc`, `/usr/vacpp/bin/xlC_r`, `-q64`; compiler paths can vary. |
| HP | `/opt/aCC/bin/aCC`, `+DD64`, and for 64-bit builds add `+DD64 -DBUILD_REAL_64_BIT_MODE` to `CFLAGS`. |
| SUN | `/opt/SUNWspro/bin/cc`, `/opt/SUNWspro/bin/CC`, `/opt/SUNWspro/bin/CC` for `LD`, `-xarch=v9`; set `/usr/lib/64` and `/usr/ucblib/sparv9` in `LD_LIBRARY_PATH_64`. |

The source install flow is:

```bash
mkdir install
cd install
gzip -dc unixODBC*.gz | tar xvf -
./configure --prefix=/home/unixODBC --disable-gui --enable-threads=yes
make
make install
cd /home/unixODBC/bin
./dltest $ALTIBASE_HOME/lib/libaltibase_odbc-64bit-ul32.so
```

Use `--enable-threads=yes`; if thread support is disabled, `isql` can fail with:

```text
./isql: symbol lookup error: /home/altibase_home/lib/libaltibase_odbc-64bit-ul64.so: undefined symbol: pthread_sigmask
```

Set `ODBCINI` to the target `odbc.ini` path and define an Altibase DSN. Important settings include `Driver`, `UserName`, `Password`, `Server`, `User`, `Port`, `Database`, `FetchBufferSize`, `ReadOnly`, `LongDataCompat`, `TraceFile`, and `Trace`. Use `LongDataCompat=ON` for LOB data.

Use `odbcinst -j` to check SQLLEN/SQLULEN:

```bash
/home/unixODBC/bin/odbcinst -j
```

If `SQLLEN = 4byte/32bit`, use `libaltibase_odbc-64bit-ul32.so`. If `SQLLEN = 8byte/64bit`, use `libaltibase_odbc-64bit-ul64.so`. Test the DSN with:

```bash
cd /home/unixODBC/bin
./isql Altiodbc
```

On AIX, if `libodbcinst.so` is not found in `LIBRARY_PATH`, check whether `libodbcinst.so.1` exists in the compiled source directory, create a symbolic link to `libodbcinst.so.1`, and place it in `LD_LIBRARY_PATH`. On SUN, set the unixODBC manager library path in `LD_LIBRARY_PATH_64`.

To enable unixODBC trace logging, create `odbcinst.ini` in the same directory as `odbc.ini`, use the DSN name `[ODBC]`, and set:

```ini
[ODBC]
TraceFile = /home/unixODBC/bin/trace.log
Trace = Yes
```

### ADO.NET development

The Windows ADO.NET guide is based on Altibase 6.5.1, Windows 7, and Visual Studio 2010 C#. It recommends reading the Application Program Interface User's Manual for detailed ADO.NET interface instructions.

Altibase provides .NET Framework Data Provider components. The source names these ADO.NET classes and roles:

| Class | Role |
| --- | --- |
| `Connection` | Connectivity to data sources |
| `Command` | Query the connected DB |
| `DataReader` | Read records from the connected DB |
| `DataAdapter` | Fill data in the `DataSet` object |

Requirements:

- Use .NET Framework 2.0 or later with the .NET Data Provider included in the Altibase HDB package.
- Use Entity Framework with .NET Framework 3.5 SP1 or later.
- Install the Altibase CLI library because the Altibase HDB .NET Data Provider connects through it.
- Install the DTC system service for distributed transactions and enable the `XA transaction` option in DTC settings.

Download `altiadonetX.X.X_32/64bit.zip` from `http://support.altibase.com` under Downloads -> Products -> LIBRARY. Use the same version as the server package from the CLIENT section when version matching matters. The source records `altiadonet6.5.1.2_64/32.zip` as the latest uploaded file at the time it was written.

After installing the Windows Client package or extracting the compressed file, verify that `Altibase.Data.AltibaseClient.dll` and `odbccli_sl.dll` exist under `%ALTIBASE_HOME%/lib`. Add `Altibase.Data.AltibaseClient.dll` as a Visual Studio reference. `odbccli_sl.dll` must be either in the same folder as the executable or in a directory listed in `PATH`; rerun Visual Studio after changing `PATH`.

The ADO.NET connection string example is:

```text
DSN=192.168.1.35;uid=sys;pwd=manager;NLS_USE=MS949;PORT=20300
```

ADO.NET code examples use:

- `AltibaseConnection` for opening a connection.
- `AltibaseCommand` and `AltibaseDataReader` for `Select to_char(sysdate, 'yyyy-mm-dd hh:mi:ss') from dual`.
- `AltibaseDataAdapter` with `INSERT INTO T1 VALUES (?, ?)` and `DataTable`/`DataRow`.
- `AltibaseTransaction` with `BeginTransaction()`, `Commit()`, and `Rollback()`.

Use the ADO.NET DLL that matches the Visual Studio compilation bit type. If Visual Studio builds 32-bit, use `altiadonetX.X.X.X_32bit.zip`; if it builds 64-bit, use `altiadonetX.X.X.X_64bit.zip`.

### PHP through ODBC

The PHP integration guide says Altibase integrates with PHP by using ODBC functions. PHP-supported data types listed by the source are `resource`, `int`, `bool`, `double`, `float`, `string`, `array`, and `HashTable`. The port number of the Altibase server and the port number in `db.php` of the Altibase sample program must match.

For Unix/Linux PHP integration:

1. Download unixODBC from `http://www.unixodbc.org`.
2. Compile it with a configured prefix, then run `make` and `make install`.
3. Set `ODBCSYSINI` to the Altibase installation account's home directory, for example `export ODBCSYSINI=~`.
4. Add the unixODBC driver-manager library path through `LD_LIBRARY_PATH`, `LD_LIBRARY_PATH_64`, or `SHLIB_PATH` depending on platform and bitness.
5. Create `odbc.ini` and `odbcinst.ini` under the `ODBCSYSINI` path. The source states `odbcinst.ini` is a 0-byte file in this setup.
6. In `odbc.ini`, define the DSN, Altibase ODBC driver path, server IP, and port.

Example `odbc.ini`:

```ini
[Altibase]
Driver = /home/altibase/altibase_home/lib/libaltibase_odbc.so
Server = 127.0.0.1
Port = 20300
```

For PHP/PERL through unixODBC, the FAQ adds:

```bash
export CFLAGS=-DBUILD_LEGACY_64_BIT_MODE=1
export ODBCINI=/path/to/odbc.ini
export LD_LIBRARY_PATH=$APACHE_HOME/modules:/path/to/unixODBC/lib:/path/to/php/lib
```

Check that `SQLLEN` and `SQLULEN` are 4 with `odbcinst -j`; if they are 8, they are 64-bit. Add `LongDataCompat=ON` to `odbc.ini` for LOB data. The PHP configure example includes `--with-unixODBC=/user/web/odbc` and then `make` and `make install`. The source `php.ini` settings are:

```ini
memory_limit=-1
odbc.defaultbinmode=1
odbc.defaultlrl=1048576
```

In Windows, ODBC Manager is installed by default, and the Altibase ODBC driver is automatically registered when Altibase is installed.

Altibase supports standard ODBC, so PHP can use standard ODBC functions such as `odbc_connect`, `odbc_exec`, `odbc_prepare`, `odbc_execute`, `odbc_do`, `odbc_fetch_row`, `odbc_result`, and `odbc_close`.

### Spring+iBatis transaction handling for Altibase LOBs

The Spring+iBatis FAQ lists two broad transaction styles:

| Style | Source options |
| --- | --- |
| BMT, explicit transaction management | Use `DataSourceTransactionManager` directly or use `TransactionTemplate`. |
| CMT, declarative transaction management | Use `<tx:advice>`, `TransactionProxyFactoryBean`, or `@Transactional`. |

The common `applicationContext.xml` data source uses `org.apache.commons.dbcp.BasicDataSource`, driver `Altibase.jdbc.driver.AltibaseDriver`, URL `jdbc:Altibase://192.168.1.82:20300/mydb`, username `sys`, password `manager`, and pool settings `maxActive`, `maxIdle`, and `maxWait`.

When directly using `DataSourceTransactionManager`, there is no additional configuration, but commit and rollback are handled in source code and `setAutoCommit(false)` must be called. The FAQ explicitly notes that `setAutoCommit(false)` must be called when selecting BLOB data.

When using `TransactionTemplate`, define a `transactionTemplate` bean and use functions such as `transactionTemplate.execute()` and `doInTransaction()` in source code. The FAQ notes that Oracle code may not have handled BLOB transactions explicitly, but Altibase code must use these transaction functions for BLOB data.

For declarative transaction management through `<tx:advice>`, `TransactionProxyFactoryBean`, or `@Transactional`, the FAQ examples configure `SqlMapClientFactoryBean`, `defaultLobHandler`, and:

```xml
<prop key="DefaultAutoCommit">false</prop>
<prop key="SetAutoCommitAllowed">true</prop>
```

Classes that require transactions under annotation style need `@Transactional(propagation=Propagation.REQUIRED)`. If `AltibaseClobStringTypeHandler` recommended by the standard framework is applied, an error can occur when `CLOB` is 0 bytes; the FAQ says normal query results can be obtained by adding the annotation without using `TypeHandler`.

The source preserves downloadable sample code:

- [LobSpringIbatisSample.zip](https://docs.altibase.com/download/attachments/9109742/LobSpringIbatisSample.zip?version=1&modificationDate=1447388295000&api=v2)

### PHP Hangul output troubleshooting

When Korean characters are broken on a PHP web page, first check whether query results containing Hangul display normally through unixODBC by using the `$UNIXODBC_HOME/bin/isql` utility. Then check PHP settings, and finally check web server or web page character-set settings.

In `odbc.ini`, set `NLS_USE` to the same value as the DB character set. Example:

```ini
NLS_USE = MS949
```

For UTF8 databases, the Windows console code page must support Unicode:

```text
chcp 65001
```

Terminal clients such as Secure CRT also need Unicode-related session settings for UTF8 Korean output.

If large `varchar` or `clob` data is broken or repeated from a specific point, adjust `odbc.defaultlrl` in `php.ini`. The FAQ example says default `odbc.defaultlrl = 4096` can truncate or corrupt output for `varchar(65536)`, and setting `odbc.defaultlrl = 65536` allows output up to 64 KBytes. `php.ini` is generally under `/etc`, but the path can vary by configuration.

## Procedures

### Precompile and build a simple APRE program

1. Start with `.sc` source such as `$ALTIBASE_HOME/sample/APRE/connect1.sc`.
2. Precompile it to C or C++ source:

```makefile
connect1.c: connect1.sc
	apre -t c connect1.sc
```

3. Add include and library paths:

```makefile
ALTI_INCLUDE=${ALTIBASE_HOME}/include
ALTI_LIBRARY=${ALTIBASE_HOME}/lib
```

4. Link APRE and ODBC CLI libraries:

```makefile
LIBS=-lapre -lodbccli
```

5. Add platform system libraries when unresolved symbol errors occur. On Linux, the guide shows:

```makefile
SYS_LIBS=-lpthread -lm -ldl -lcrypt -lstdc++ -lrt
```

6. Run `make` or `gmake`, depending on the platform and local standard.

### Diagnose missing headers and libraries

If compilation reports `ulpLibInterface.h: No such file or directory`, add `$ALTIBASE_HOME/include` through `-I$(ALTI_INCLUDE)`.

If link reports undefined references such as `ulpGetSqlca`, add `$ALTIBASE_HOME/lib` through `-L$(ALTI_LIBRARY)` and link `-lapre -lodbccli`.

If APRE library internals report unresolved POSIX thread symbols such as `pthread_rwlock_init` or `pthread_rwlock_wrlock`, add the platform thread library, for example `-lpthread` on Linux/HP-UX, `-lpthreads` on AIX, or `-lpthread`/`-lthread` on Solaris.

To find additional system libraries:

- Check `$ALTIBASE_HOME/install/altibase_env.mk`.
- Check `$ALTIBASE_HOME/sample/APRE/Makefile`.
- Run `ldd $ALTIBASE_HOME/bin/apre` to inspect shared-library dependencies.
- Use `nm -A /usr/lib/lib* | grep symbol_name` for unresolved symbols.
- Use `man 3 function_name`; for example, `man 3 cos` explains that `cos` links with `-lm`.

### Handle 32-bit and 64-bit build mismatches

Use a 64-bit APRE compiler, 64-bit APRE library, 64-bit headers, and compiler-specific 64-bit options for 64-bit programs. Use the corresponding 32-bit client development tools, library, headers, and 32-bit options for 32-bit programs.

If the database server package is 64-bit, 64-bit client development tools are installed with the server package by default. To install 32-bit or separate 64-bit client development tools, download the appropriate client install package from:

```text
http://support.altibase.com/en/product
```

Check library bitness with:

```bash
cd $ALTIBASE_HOME/lib
file libapre_sl.so
```

Example output meanings:

```text
ELF 32-bit LSB shared object ... # 32-bit APRE library on Linux
ELF 64-bit LSB shared object ... # 64-bit APRE library on Linux
```

Compiler bit options from the source:

| OS/compiler | 64-bit option | 32-bit option |
| --- | --- | --- |
| Solaris `cc` on SPARC | `-xarch=v9` or `-m64 -xarch=sparc` | `-xarch=v8plusa` |
| HP-UX `cc` | `+DD64` | `+DD32` |
| AIX `cc` | `-q64` | `-q32` |
| Linux `gcc` | `-m64` | `-m32` |

### Upgrade SES*C/C++ build files to APRE*C/C++

1. Change precompile command names from `sesc` to `apre`.
2. Change link options from `-lsesc` to `-lapre`.
3. Change library references from `libsesc.a` or `libsesc_sl.so` to `libapre.a` or `libapre_sl.so`.
4. Update include references from `ses.h` to `ulpLibInterface.h` where direct header references exist.
5. Prefer `-I` instead of the older `-include` option.
6. If APRE reports unclear syntax or macro-processing errors, retry with `-parse none` to isolate differences from SES behavior.
7. Remove any user code that directly calls or depends on the precompiler library interface.

### Build on Linux with `gcc`

Use basic APRE libraries plus Linux system libraries:

```makefile
ALTI_INCLUDE=${ALTIBASE_HOME}/include
ALTI_LIBRARY=${ALTIBASE_HOME}/lib
LIBS=-lapre -lodbccli
SYS_LIBS=-lpthread -lm -ldl -lcrypt -lstdc++ -lrt

connect1.c: connect1.sc
	apre -t c connect1.sc

connect1: connect1.c
	cc -o connect1 connect1.c -I$(ALTI_INCLUDE) -L$(ALTI_LIBRARY) $(LIBS) $(SYS_LIBS)
```

For 32-bit Linux, use the 32-bit client paths, run the 32-bit `apre`, and compile with `-m32`:

```makefile
ALTI_INCLUDE=/alticlient32/include
ALTI_LIBRARY=/alticlient32/lib
LIBS=-lapre -lodbccli
SYS_LIBS=-lpthread -lm -ldl -lc

connect1.c: connect1.sc
	/alticlient32/bin/apre -t c connect1.sc

connect1: connect1.c
	gcc -m32 -o connect1 connect1.c -I$(ALTI_INCLUDE) -L$(ALTI_LIBRARY) $(LIBS) $(SYS_LIBS)
```

### Build on HP-UX with `acc`

HP-UX `acc` libraries include:

| Library | Purpose |
| --- | --- |
| `-lpthread` | POSIX thread functions |
| `-lm` | Math functions |
| `-ldld` | Dynamic loaded library |
| `-lunwind` | Stack tracing and unwinding APIs on Itanium-based servers |
| `-lstd -lstream -lCsup -lc` | C++ compatibility libraries for Altibase 5.3.3 or earlier when compiling with `acc` |
| `-lrt` | Realtime extensions |

The source examples use `-mt`, `+DD64` or `+DD32`, and `-Wl,+vnocompatwarnings`.

### Build on AIX with `xlc`

AIX `xlc` libraries include:

| Library | Purpose |
| --- | --- |
| `-lpthreads` | POSIX thread functions |
| `-lm` | Math functions |
| `-lC` | C++ compatibility library for Altibase 5.3.3 or earlier when compiling with the C compiler |

Compile/link options include `-bmaxdata`, `-q32`, `-q64`, `-O2`, `-qinline`, `-brtl`, and `-bexpall`.

Simple 64-bit example:

```makefile
ALTI_INCLUDE=$(ALTIBASE_HOME)/include
ALTI_LIBRARY=$(ALTIBASE_HOME)/lib
LIBS=-lapre -lodbccli -lpthreads -lm
LFLAGS=-O2 -qinline -q64

connect1.c:connect1.sc
	$(ALTIBASE_HOME)/bin/apre -t c connect1.sc

connect1:connect1.c
	cc $(LFLAGS) -o connect1 connect1.c -I$(ALTI_INCLUDE) -L$(ALTI_LIBRARY) $(LIBS)
```

For AIX 32-bit, use 32-bit client paths, `/alticlient32/bin/apre`, `-q32`, and optionally `-bmaxdata:0x80000000`; the source says `0x80000000` allows up to 2 GB.

When building AIX shared libraries that use APRE functions, do not link `-lapre_sl` and `-lodbccli_sl` into the shared library itself. Link APRE shared libraries only when creating the executable binary. Otherwise, global variables in `apre_sl` and `odbccli_sl` can be recognized as different variables across shared libraries, and a library such as `sel.so` may be unable to refer to the connection-related object in `con.so`.

### Build on Solaris with `cc`

Solaris `cc` libraries include:

| Library | Purpose |
| --- | --- |
| `-lpthread` or `-lthread` | POSIX thread functions |
| `-lm` | Math functions |
| `-ldl` | Dynamic loaded library |
| `-lnsl` | Networking Services functions |
| `-lsocket` | Socket functions |
| `-lCrun -ldemangle` | C++ compatibility libraries for Altibase 5.3.3 or earlier when compiling with `cc` |
| `-lrt` | Realtime extensions |

Compile options include `-mt`, `-xarch=amd64`, `-xarch=sse2a`, `-xarch=v9`, `-xarch=v8plus`, and `-fast`.

The source 64-bit Solaris x86 example includes:

```makefile
LIBS=-lapre -lodbccli -lthread -lposix4 -ldl -lkvm -lkstat -lsocket -lnsl -lgen -lC -lCrun -ldemangle -lm
LFLAGS=-fast -mt -xarch=amd64 -L/opt/SUNWspro/lib/amd64 -L/usr/lib/amd64
```

For 32-bit Solaris x86, use 32-bit client paths, `/alticlient32/bin/apre`, and `-xarch=sse2a`.

### Decide whether to add C++ compatibility libraries

Up to Altibase 5.3.3, `sesc` was used and part of the SESC library was built in C++ format. When compiling with a C compiler rather than a C++ compiler, add platform C++ compatibility libraries if C++ operator or vtable references cannot be resolved.

The source table lists:

| Platform | C++ compatibility libraries |
| --- | --- |
| SUN | `-lCrun` |
| HP | `-lstd -lstream -lCsup -lc` |
| AIX | `-lC` |
| Linux | `-lstdc++ -lc` |

Starting with Altibase 5.5.1, the APRE library was rewritten in C source code. When compiling with a C compiler, a separate C++ library is not required for APRE itself. When using a C++ compiler, most of these compatibility issues can be avoided, but compiler-specific 64-bit options still need to be checked.

### Configure a Java/JDBC client

1. Verify that the desired driver file, such as `Altibase.jar` or an additional version-specific JAR, exists under `$ALTIBASE_HOME/lib`.
2. Check compatibility:

```bash
java -jar Altibase.jar
altibase -v
```

3. Compare the driver's CMP value with the server cm protocol version.
4. Add the JAR to `CLASSPATH`, place it under `$JAVA_HOME/jre/lib/ext` or `$JRE_HOME/lib/ext`, pass it with `java -classpath`, or add it to Eclipse as an external JAR.
5. Load the driver class:

```java
Class.forName("Altibase.jdbc.driver.AltibaseDriver");
```

6. Build a URL in `jdbc:Altibase://ip_address:port_no/db_name` form and pass `user` and `password` as properties or URL query parameters.
7. For LOB work, call `setAutoCommit(false)` before using CLOB or BLOB data.
8. Close all `Connection`, `Statement`, `PreparedStatement`, and `ResultSet` resources when done.

### Configure JDBC failover

1. Add alternate servers and failover properties to the JDBC URL.
2. Choose `SessionFailOver=off` for CTF only, or `SessionFailOver=on` for CTF plus STF.
3. If STF is enabled, catch `SQLException`, check `getSQLState()`, and prepare statements again after successful failover.
4. Treat `08F01` as the Altibase 6.3.1-or-later STF success code and `ES_08FO01` as the Altibase 6.1.1-or-earlier STF success code.
5. Use `FailOver_Source` if the server-side `V$SESSION.FAILOVER_SOURCE` value is needed for operations or diagnostics.
6. Use `HealthCheckDuration` to control how long a failed server stays out of the JDBC available-server list.

### Configure simultaneous JDBC connections to different Altibase versions

1. Place the base `Altibase.jar` and the additional version-specific JAR under the relevant `$ALTIBASE_HOME/lib` directories.
2. For Altibase 7.1 and 7.3 simultaneous connections, use `Altibase.jar` from 7.1 and `Altibase7_3.jar` from 7.3.
3. Load the version-specific driver class and the normal driver class separately:

```java
Class.forName("Altibase7_3.jdbc.driver.AltibaseDriver");
Class.forName("Altibase.jdbc.driver.AltibaseDriver");
```

4. In older Altibase 5 examples, load `Altibase5.jdbc.driver.AltibaseDriver` before `Altibase.jdbc.driver.AltibaseDriver`.
5. In IBM Java 1.6, include the cm protocol version in each URL, for example `jdbc:Altibase_5.6.2://...`.

### Configure Windows ODBC

1. Confirm that the target Altibase version supports Windows ODBC. Windows ODBC is supported only through Altibase 6.5.1.
2. Download the Windows ODBC files or Windows Client package from `http://support.altibase.com`; use `support@altibase.com` for older unavailable versions.
3. For 64-bit DSNs, open ODBC Data Source (64-bit). For 32-bit DSNs on 64-bit Windows, run `C:\windows\sysWOW64\odbcad32.exe`.
4. Add an Altibase driver, for example `ALTIBASE_HDB_ODBC_64bit`.
5. Enter DSN name, host, port, user, password, database name, and `NLS_USE`.
6. Use Test Connection while the Altibase DB server is running.
7. In application connection strings, set `LongDataCompat=on` when using large data such as BLOB.
8. For ODBC LOB insert or select, begin a transaction and commit after successful work.

### Build and configure unixODBC

1. Download unixODBC source from `http://www.unixodbc.org`.
2. Check the Altibase ODBC driver file bitness:

```bash
file $ALTIBASE_HOME/lib/libaltibase_odbc*
```

3. Decide unixODBC bitness and SQLLEN size. Prefer SQLLEN 4 bytes with:

```bash
export CFLAGS=-DBUILD_LEGACY_64_BIT_MODE=1
```

4. For 32-bit unixODBC on 64-bit Linux, also set `-m32` in `CFLAGS`, `LDFLAGS`, and `CXXFLAGS`.
5. Configure and build:

```bash
./configure --prefix=/home/unixODBC --disable-gui --enable-threads=yes
make
make install
```

6. Verify that the Altibase ODBC driver loads:

```bash
cd /home/unixODBC/bin
./dltest $ALTIBASE_HOME/lib/libaltibase_odbc-64bit-ul32.so
```

7. Set `ODBCINI` to the `odbc.ini` path and configure the DSN.
8. Check SQLLEN/SQLULEN with `odbcinst -j`.
9. Test the DSN:

```bash
./isql Altiodbc
```

10. Enable trace logging in `odbcinst.ini` only when diagnostic output is needed.

### Configure ADO.NET

1. Download the correct `altiadonetX.X.X_32/64bit.zip` from the Altibase support site, preferably matching the server/client version.
2. Verify that `Altibase.Data.AltibaseClient.dll` and `odbccli_sl.dll` exist under `%ALTIBASE_HOME%/lib`.
3. Add `Altibase.Data.AltibaseClient.dll` as a Visual Studio reference.
4. Put `odbccli_sl.dll` in the application executable folder or add its directory to `PATH`.
5. Restart Visual Studio after changing `PATH`.
6. Match the ADO.NET DLL bit type with the Visual Studio build target. Use the 32-bit DLL for 32-bit builds and the 64-bit DLL for 64-bit builds.
7. For distributed transactions, install DTC and enable `XA transaction` in DTC settings.

### Configure PHP through ODBC

1. Install and configure unixODBC or use Windows ODBC Manager.
2. On Unix/Linux, set `ODBCSYSINI`, create `odbc.ini`, and create a 0-byte `odbcinst.ini` in that path when following the PHP guide's setup.
3. Add the unixODBC driver-manager library directory to `LD_LIBRARY_PATH`, `LD_LIBRARY_PATH_64`, or `SHLIB_PATH`.
4. Define the Altibase DSN and driver path in `odbc.ini`.
5. For PHP/PERL, set `CFLAGS=-DBUILD_LEGACY_64_BIT_MODE=1`, `ODBCINI`, and `LD_LIBRARY_PATH`.
6. Confirm `SQLLEN` and `SQLULEN` are 4 with `odbcinst -j`.
7. Add `LongDataCompat=ON` to process LOB data.
8. Compile PHP with `--with-unixODBC=/path/to/unixODBC`, then run `make` and `make install`.
9. Set `memory_limit=-1`, `odbc.defaultbinmode=1`, and `odbc.defaultlrl=1048576` in `php.ini` when following the source FAQ.

## SQL, commands, and configuration

### APRE command and option catalog

| Command or option | Use |
| --- | --- |
| `apre -mt -t cpp connect1.sc` | Precompile `connect1.sc` to C++ source with multithread option. |
| `apre -t c connect1.sc` | Precompile `connect1.sc` to C source. |
| `apre -unsafe_null -t cpp file.sc` | Allow NULL host-variable handling without indicator variables. |
| `apre -t cpp -I$APP_HOME/include/main tmp.sc` | Precompile with include path. |
| `apre -DALTIBASE -DOTHER_DBMS -t cpp tmp.sc` | Define macros during preprocessing. |
| `apre -keyword` | Print reserved keywords. |
| `apre -t c -parse none main.sc` | Precompile like SES*C/C++, without macro/header processing. |
| `apre -parse full` | Use full parsing so C host variables can be recognized outside `DECLARE SECTION`. |

### Embedded SQL fragments

```sql
EXEC SQL BEGIN DECLARE SECTION;
EXEC SQL END DECLARE SECTION;
EXEC SQL CONNECT :usr IDENTIFIED BY :pwd USING :opt;
EXEC SQL AT CONN1 CONNECT :usr IDENTIFIED BY :pwd USING :opt;
EXEC SQL DISCONNECT;
EXEC SQL FREE;
EXEC SQL AUTOCOMMIT OFF;
EXEC SQL COMMIT;
EXEC SQL ROLLBACK;
EXEC SQL DECLARE CURSOR1 CURSOR FOR SELECT C1, C2 FROM TEST1 WHERE C1 >= :H_Condition;
EXEC SQL DECLARE CURSOR1 CURSOR WITH HOLD FOR SELECT * FROM DEPARTMENT;
EXEC SQL PREPARE STMT1 FROM :sql_text;
EXEC SQL EXECUTE STMT1 USING :H_var1, :H_var2;
EXEC SQL CLOSE RELEASE CURSOR1;
```

### Build paths and files

| Identifier | Meaning |
| --- | --- |
| `$ALTIBASE_HOME/bin/apre` | APRE executable path. |
| `$ALTIBASE_HOME/include` | Altibase header directory. |
| `$ALTIBASE_HOME/lib` | Altibase library directory. |
| `$ALTIBASE_HOME/install/altibase_env.mk` | Source for optimized APRE compiler/link options and library lists. |
| `$ALTIBASE_HOME/sample/APRE/Makefile` | Sample APRE Makefile. |
| `$ALTIBASE_HOME/sample/APRE` | APRE sample source tree. |
| `$ALTIBASE_HOME/conf/altibase.properties` | Property file containing `AUTO_COMMIT`, `IPC_CHANNEL_COUNT`, and timeout-related server settings. |
| `$ALTIBASE_HOME/msg/manual.txt` | Error-code reference for `SQLCODE`. |
| `$ALTIBASE_HOME/trc/altibase_boot.log` | Log to check timeout-related disconnect messages. |

### Connection-string keys

| Key | Meaning |
| --- | --- |
| `DSN` | Server address or data source name in source examples. |
| `PORT_NO` | Altibase connection port. |
| `CONNTYPE` | Connection method selector: `1`, `2`, or `3`. |
| `AlternateServers` | Failover target servers in `IP:PORT` form. |
| `ConnectionRetryCount` | Retry count per target server. |
| `ConnectionRetryDelay` | Delay in seconds between retries. |
| `SessionFailOver` | Enables or disables STF behavior. |
| `LoadBalance` | Selects random initial target when `on`; preserves `DSN` first when `off`. |

### Java and JDBC commands, URLs, and SQL

```bash
java -jar Altibase.jar
java -jar Altibase7_3.jar
altibase -v
java -classpath $ALTIBASE_HOME/lib/Altibase.jar HelloApp
java -DALTIBASE_JDBC_TRCLOG_DISABLE=true ClassFileName
export ALTIBASE_JDBC_TRCLOG_DISABLE=true
```

```text
jdbc:Altibase://ip_address:port_no/db_name
jdbc:Altibase://192.168.1.111:20300/mydb?user=sys&password=manager
jdbc:Altibase://127.0.0.1:20300/mydb?AlternateServers=(128.1.3.52:20300,128.1.3.53:20300)&ConnectionRetryCount=3&ConnectionRetryDelay=10&SessionFailOver=on&LoadBalance=off
jdbc:Altibase_5.6.2://192.168.1.111:20300/mydb
```

```sql
SELECT DB_NAME FROM V$DATABASE;
SELECT NLS_CHARACTERSET FROM V$NLS_PARAMETERS;
CREATE OR REPLACE TYPESET my_type AS TYPE my_cur IS REF CURSOR; END;
```

```java
Class.forName("Altibase.jdbc.driver.AltibaseDriver");
Class.forName("Altibase5.jdbc.driver.AltibaseDriver");
Class.forName("Altibase7_3.jdbc.driver.AltibaseDriver");
Connection altibaseConnection1 = DriverManager.getConnection(db_url1, props1);
CallableStatement altibaseStatement1 = altibaseConnection1.prepareCall("{call sum_proc(?,?,?)}");
```

### Windows ODBC and unixODBC configuration

```text
DRIVER=ALTIBASE_HDB_ODBC_64bit;user=sys;password=manager; Server=127.0.0.1;PORT=20300;NLS_USE=MS949;LongDataCompat=on
C:\windows\sysWOW64\odbcad32.exe
```

```bash
file $ALTIBASE_HOME/lib/libaltibase_odbc*
export CFLAGS=-DBUILD_LEGACY_64_BIT_MODE=1
export CFLAGS="-m32 -DBUILD_LEGACY_64_BIT_MODE=1"
export LDFLAGS=-m32
export CXXFLAGS=-m32
./configure --prefix=/home/unixODBC --disable-gui --enable-threads=yes
make
make install
./dltest $ALTIBASE_HOME/lib/libaltibase_odbc-64bit-ul32.so
export ODBCINI=/home/unixODBC/etc/odbc.ini
/home/unixODBC/bin/odbcinst -j
./isql Altiodbc
```

```ini
[ODBC Data Sources]
Altiodbc = Altibase ODBC Driver

[Altiodbc]
Driver = /altibase_home/lib/libaltibase_odbc-64bit-ul32.so
Description = Sample Altibase DSN
UserName = SYS
Password = MANAGER
ServerType = Altibase
Server = 127.0.0.1
User = SYS
Port = 20300
Database = mydb
FetchBufferSize = 64
ReadOnly = no
LongDataCompat=ON
TraceFile = /tmp/odbc.trace
Trace = 1
```

```ini
[ODBC]
TraceFile = /home/unixODBC/bin/trace.log
Trace = Yes
```

ODBC function options from the SQLFreeStmt FAQ:

| Option | Meaning |
| --- | --- |
| `SQL_CLOSE` | Close the cursor associated with the statement handle and discard pending results; the cursor can be reopened by executing SELECT again. |
| `SQL_DROP` | Release statement-handle resources and invalidate the handle; closes an open cursor and discards pending results. |
| `SQL_UNBIND` | Release columns bound by prior `SQLBindCol()` calls. |
| `SQL_RESET_PARAMS` | Release parameters set by prior `SQLBindParameter()` calls. |

Use `SQLFreeStmt(stmt, SQL_DROP)` only when the statement handle will not be reused. Use `SQLFreeStmt(stmt, SQL_CLOSE)` when all rows were not fetched and the existing statement handle should be reused without `SQLAllocStmt()`.

### ADO.NET and PHP identifiers

```text
Altibase.Data.AltibaseClient.dll
odbccli_sl.dll
%ALTIBASE_HOME%/lib
DSN=192.168.1.35;uid=sys;pwd=manager;NLS_USE=MS949;PORT=20300
altiadonetX.X.X_32/64bit.zip
altiadonetX.X.X.X_32bit.zip
altiadonetX.X.X.X_64bit.zip
```

ADO.NET classes and methods from the source include `AltibaseConnection`, `AltibaseCommand`, `AltibaseDataReader`, `AltibaseDataAdapter`, `AltibaseTransaction`, `BeginTransaction()`, `Commit()`, and `Rollback()`.

```bash
export ODBCSYSINI=~
export LD_LIBRARY_PATH=/usr/local/odbcDriverManager32/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH_64=/usr/local/odbcDriverManager64/lib:$LD_LIBRARY_PATH_64
export ODBCINI=/path/to/odbc.ini
export LD_LIBRARY_PATH=$APACHE_HOME/modules:/path/to/unixODBC/lib:/path/to/php/lib
chcp 65001
```

```ini
memory_limit=-1
odbc.defaultbinmode=1
odbc.defaultlrl=1048576
odbc.defaultlrl=65536
```

PHP ODBC functions preserved from source samples include `odbc_connect`, `odbc_exec`, `odbc_prepare`, `odbc_execute`, `odbc_do`, `odbc_fetch_row`, `odbc_result`, and `odbc_close`.

### Error and timeout SQL

```sql
EXEC SQL ALTER SESSION SET STACK SIZE = 4096;
EXEC SQL ALTER SESSION SET QUERY_TIMEOUT = 0;
EXEC SQL ALTER SESSION SET FETCH_TIMEOUT = 0;
EXEC SQL ALTER SESSION SET UTRANS_TIMEOUT = 0;
```

`0` disables the corresponding timeout, but the transaction or query can continue occupying DBMS resources until it finishes.

## Validation and troubleshooting

### APRE development checks

- Check every `EXEC SQL` stage for errors, especially cursor `PREPARE` or `DECLARE`; otherwise a later `OPEN` or `FETCH` can only report that the statement or cursor does not exist.
- For threaded programs, ensure each thread uses its own connection or protect shared connection objects.
- For character host variables, include NULL padding or use `-n` only when the application controls clear length.
- For `NULL` results, use `NVL`, an indicator variable, or `apre -unsafe_null`.
- For LOB access, use non-auto-commit mode and explicitly commit or roll back.
- For FAC symptoms, check whether commit/rollback occurred during fetch, then use auto-commit, a separate connection, or `WITH HOLD` on Altibase 6.3.1 or later.
- For C++-style source with host variables outside `DECLARE SECTION`, avoid `-parse full`; declare host variables inside `DECLARE SECTION` and use `-parse partial` or `-parse none`.
- When C/C++ compile options such as `-D` or `-I` are used in the compiler stage, pass equivalent options to APRE precompile when they affect preprocessing.

### Makefile problem checklist

When compilation fails, check:

1. Whether the correct APRE library is being used for the compiler.
2. Whether the Makefile has path, typo, or variable-name errors.
3. Whether library/object bitness differs.
4. Whether the required vendor library is linked.
5. Whether the required system library is linked.
6. Whether C/C++ compatibility libraries are needed.

### Common source-level errors

The full SQLCODE catalog is in `llm-reference/07-troubleshooting-error-messages.md`. APRE development answers should still preserve these source-level mappings:

| Symptom or message | Key action |
| --- | --- |
| `Connection does not exist. (SQLCODE=-2)` | Check connection creation, connection names in `EXEC SQL AT`, thread connection control, and timeout disconnects. |
| `String data right truncated. (SQLCODE=1)` | Increase DB host variable size to data length plus 1 byte. |
| `Invalid size of data to bind to a host variable ...` | Check host variable length, memory corruption, and thread concurrency on one connection. |
| `Calculation stack overflow` | Run `EXEC SQL ALTER SESSION SET STACK SIZE = 4096;`; default is `1024`. |
| `Indicator variable required but not supplied` | Use `NVL`, an indicator variable, or `apre -unsafe_null`. |
| `Client's query exceeded in the execution time limitation` | Tune the query or set `QUERY_TIMEOUT = 0` after evaluating resource risk. |
| `Communication link failure` | Check `$ALTIBASE_HOME/trc/altibase_boot.log` for fetch or update transaction timeout, and investigate L4/firewall network timeouts through PBT when no DB log remains. |

### Source sample caution

When using `Testsample.sc` from the APRE sample-program source, treat it as a pattern for separate-connection cursor updates. Before compiling, review source spellings and syntax carefully because the exported source sample contains obvious non-compilable tokens such as `EXC SQL`, `INTEGE`, inconsistent function capitalization, and `AUTOCOMMIT = FALSE:`.

### JDBC validation and error handling

- If a JDBC connection fails with `Communication link failure`, check whether the DB is running, connection properties are correct, the `Altibase.jar` version is compatible with the server, or service-time timeout disconnected the session.
- If a `Communication link failure` occurs during service, check whether a timeout occurred and review `$ALTIBASE_HOME/trc/altibase_boot.log`.
- For `No suitable driver`, check whether the JDBC driver is incorrect for the target Altibase version and reset the Altibase JDBC driver.
- For `Client unable to establish connection`, check whether the Altibase server is running.
- Timeout categories from the Java guide:

| Category | Client message | Server log message | Result |
| --- | --- | --- | --- |
| `QUERY_TIMEOUT` | `Client's query exceeded in the execution time limitation` | `[Notify : Query Timeout] Query Canceled by Server` | Roll back the statement and return an error. |
| `FETCH_TIMEOUT` | `Communication link failure.` | `[Notify : Fetch Timeout] Session Closed by Server` | Roll back the statement and close the session. |
| `IDLE_TIMEOUT` | `Communication link failure.` | `[Notify : Idle Timeout] Session Closed by Server` | Roll back the statement and close the session. |
| `UTRANS_TIMEOUT` | `The session has been closed by server.` | `[Notify : UTrans Timeout] Session Closed by Server` | Roll back the statement and close the session. |

- For `Invalid descriptor index`, check whether `setXXX()` was called with more values than the bind variables in `PreparedStatement`.
- For `Optional feature not implemented`, check JDBC API support in the JDBC manual.
- For `jdbc.trc` lock errors, grant write permission to `$ALTIBASE_HOME/trc` or set `ALTIBASE_HOME` to a suitable client-side location. Use `ALTIBASE_JDBC_TRCLOG_DISABLE=true` where supported when the source FAQ's trace-disable behavior is acceptable.

### APRE, SQLCLI, and ODBC connection-disconnect states

The development/API FAQ for APRE*C/C++ and SQLCLI says these cases can leave an application without a valid connection:

1. The application is not connected.
2. A communication socket error or server-side disconnection occurred.
3. The application did not detect a previously disconnected connection.
4. A timeout disconnected the session. `QUERY_TIMEOUT` does not disconnect, but `FETCH_TIMEOUT`, `UTRANS_TIMEOUT`, and `IDLE_TIMEOUT` do.
5. The DB server shut down.
6. Connect failed because the DB server is shut down.

APRE*C/C++ can inspect `sqlca.sqlcode`, `sqlca.sqlerrm.sqlerrmc`, `SQLCODE`, and `SQLSTATE`. SQLCLI can inspect `state`, `err`, and `msg` by calling `SQLError(env,dbc,stmt,state,err,msg,msgMax,msgLength)`.

Conclusion mappings from the FAQ:

| Situation | SQLSTATE | SQLCODE or errno |
| --- | --- | --- |
| Connection failure | `08001` | The source conclusion says `SQLCODE [1(0x01)]` and `errno [32770(0x050032)]`; connection-failure examples show APRE `SQLCODE [-327730] [50032]` and SQLCLI/ODBC `error number (err) [327730] in Hex(50032)`. |
| Execute without connection or after the connection has already disconnected | `08003` | `331830(0x051036)` |
| Socket disconnection, timeout disconnection, or server shutdown | `08S01` | `331843(0x051043)` |

Preserve the source-specific numeric variants for connection failure when citing this FAQ; do not normalize `1`, `32770`, `-327730`, or `327730` without source confirmation.

### Windows ODBC, unixODBC, ADO.NET, and PHP checks

- For Windows ODBC, use the ODBC administrator that matches driver bitness. Use `C:\windows\sysWOW64\odbcad32.exe` for 32-bit ODBC on 64-bit Windows.
- For 32-bit Windows ODBC setup, confirm `PORT_NO` in `altibase.properties` or `ALTIBASE_PORT_NO`, and confirm `DB_NAME` and `NLS_CHARACTERSET` through SQL.
- For unixODBC, confirm three independent dimensions: unixODBC executable bitness, Altibase ODBC driver ELF bitness, and SQLLEN/SQLULEN size.
- If `isql` fails with `undefined symbol: pthread_sigmask`, rebuild unixODBC with thread support enabled.
- If AIX cannot find `libodbcinst.so`, check `libodbcinst.so.1`, create the needed symbolic link, and place it in `LD_LIBRARY_PATH`.
- On SUN, ensure the unixODBC manager library path is in `LD_LIBRARY_PATH_64`.
- For ADO.NET `System.BadImageFormatException`, use an ADO.NET DLL that matches Visual Studio's compilation bit type.
- For ADO.NET `System.DllNotFoundException` involving `odbccli_sl.dll`, copy `odbccli_sl.dll` beside the executable or add its directory to `PATH`.
- For PHP Hangul corruption, validate with unixODBC `isql` before changing PHP or web settings, match `NLS_USE` to the DB character set, set terminal Unicode support when DB character set is UTF8, and increase `odbc.defaultlrl` when large varchar or clob output breaks at a specific point.

## Version-specific notes

| Version or boundary | Note |
| --- | --- |
| Altibase 5 or later | Additional JDBC driver files can allow simultaneous application connections to later and earlier Altibase versions. |
| Altibase 5.1 or later | Plan-Cache internally shares execution plans executed by all sessions. |
| Altibase 5.3 or later | Host variable declaration clause can be omitted depending on `apre` option. |
| Altibase 5.3.3 or later | APRE*C/C++ replaces SES*C/C++; `apre -parse full` can recognize C host variables outside `DECLARE SECTION`; host variable initialization is supported; CTF/STF failover functions are available; JDBC failover properties can be defined in the connection URL. |
| Altibase 5.3.3 or earlier | SESC library compatibility may require C++ libraries when compiling with a C compiler. |
| ALTIBASE HDB 5.5.1 or later | `jdbc.trc` is created for JDBC-related traces when the JDBC driver initializes. |
| Altibase 5.5.1 or later | APRE library was rewritten in C source code, so a separate C++ library is not needed for APRE itself when compiling with a C compiler. |
| Altibase 6.1.1 | Java connection-pool examples use `ABPoolingDataSource`; XA examples use `ABXADataSource` and `ABXAResource`. |
| Altibase 6.1.1 or earlier | JDBC STF success can be identified by `SQLException.getSQLState()` returning `ES_08FO01`. |
| ALTIBASE HDB 6.1.1.1.3 or earlier | The `jdbc.trc` FAQ says trace creation location change or disable control is not available. |
| ALTIBASE HDB 6.1.1.1.4 through 6.1.1.1.7 | Run Java with `java -DALTIBASE_JDBC_TRCLOG_DISABLE=true` for the FAQ's trace-control behavior. |
| ALTIBASE HDB 6.1.1.1.8 or later | Use `java -DALTIBASE_JDBC_TRCLOG_DISABLE=true` or `export ALTIBASE_JDBC_TRCLOG_DISABLE=true`. |
| Altibase 6.3.1 | unixODBC integration guide basis version; SQLFreeStmt FAQ basis version; APRE/SQLCLI disconnection FAQ basis version. |
| Altibase 6.3.1 or later | FAC can be avoided with `WITH HOLD` cursor behavior in non-auto-commit mode. |
| Altibase 6.3.1 or later | Java connection-pool examples use `AltibaseConnectionPoolDataSource`; XA examples use `AltibaseXADataSource` and `AltibaseXAResource`; JDBC STF success can be identified by `SQLException.getSQLState()` returning `08F01`. |
| Altibase 6.5.1 | Java guide basis version; Windows ODBC guide basis version; ADO.NET guide basis version. |
| Through Altibase 6.5.1 | Windows ODBC and 32-bit ODBC on 64-bit Windows are supported through this version. |
| Starting from Altibase 7.1 | Windows ODBC and 32-bit ODBC drivers are no longer supported. |
| Altibase 7.3 | APRE New Features & Upgrade Guide basis version. |
| Altibase 7.3 | Simultaneous JDBC connection FAQ basis version; additional driver file is `Altibase7_3.jar`. |
| .NET Framework 2.0 or later | Recommended for the .NET Data Provider included in the Altibase HDB package. |
| .NET Framework 3.5 SP1 or later | Required by the ADO.NET source for Entity Framework use. |

## Related errors

Detailed error coverage for APRE/precompiler SQLCODEs is canonical in `llm-reference/07-troubleshooting-error-messages.md` under the precompiler SQLCODE catalog. This topic preserves development actions that prevent or triage those errors:

- Use `sqlca.sqlcode`, `SQLCODE`, and `SQLSTATE` consistently.
- Print `SQLCODE` and `sqlca.sqlerrm.sqlerrmc` in debug logs.
- Check cursor `PREPARE`, `DECLARE`, `OPEN`, `FETCH`, and `CLOSE` order.
- Use `EXEC SQL ALTER SESSION SET STACK SIZE = 4096;` for calculation stack overflow.
- Use `QUERY_TIMEOUT`, `FETCH_TIMEOUT`, and `UTRANS_TIMEOUT` overrides only after considering resource occupancy.
- Check `$ALTIBASE_HOME/trc/altibase_boot.log` for fetch and update-transaction timeout disconnects.

R018 Java/JDBC, ODBC, ADO.NET, and PHP sources add these client API errors and states:

| Error or state | Source context | Action |
| --- | --- | --- |
| `Communication link failure` | JDBC, APRE, SQLCLI/ODBC | Check DB/server availability, connection properties, compatible driver version, timeout disconnection, socket/network errors, and `$ALTIBASE_HOME/trc/altibase_boot.log`. |
| `No suitable driver` | JDBC | Reset or replace the Altibase JDBC driver for the target Altibase version. |
| `Client unable to establish connection` | JDBC, APRE, SQLCLI/ODBC | Check whether the Altibase server is running and whether connection settings are valid. |
| `Invalid descriptor index` | JDBC | Match `setXXX()` calls to the number of bind variables in `PreparedStatement`. |
| `Optional feature not implemented` | JDBC | Check JDBC manual/API support. |
| `java.io.IOException: Couldn't get lock for .../jdbc.trc` | JDBC trace | Grant write permission or use an appropriate `ALTIBASE_HOME`; disable JDBC trace where the FAQ's version-specific setting supports it. |
| `SQLSTATE 08001` | APRE/SQLCLI connection failure | Treat as connection failure. |
| `SQLSTATE 08003` | APRE/SQLCLI execute without a valid connection | Detect disconnected connections before reuse. |
| `SQLSTATE 08S01` | APRE/SQLCLI socket, timeout, or server-shutdown disconnection | Reconnect or fail over after diagnosing timeout or network/server shutdown cause. |
| `SQLSTATE 08F01` | JDBC STF success in Altibase 6.3.1 or later | Prepare statements again and continue application logic after failover. |
| `SQLSTATE ES_08FO01` | JDBC STF success in Altibase 6.1.1 or earlier | Prepare statements again and continue application logic after failover. |
| `undefined symbol: pthread_sigmask` | unixODBC `isql` test | Rebuild unixODBC with `--enable-threads=yes`. |
| `System.BadImageFormatException` | ADO.NET | Use the ADO.NET DLL matching the Visual Studio compilation bit type. |
| `System.DllNotFoundException` for `odbccli_sl.dll` | ADO.NET | Put `odbccli_sl.dll` beside the executable or add its directory to `PATH`. |
| `Connection is in autocommit mode. One can not operate on LOB datas with autocommit mode on` | JDBC, ODBC, Spring+iBatis LOB handling | Turn autocommit off or manage the LOB operation inside an explicit transaction. |

## Attachments and external references

Document-format attachments preserved by R017:

- [Altibase_Developer_Training_v1.pptx](https://docs.altibase.com/download/attachments/22642996/Altibase_Developer_Training_v1.pptx?version=1&modificationDate=1761004797000&api=v2)
- [D33_ALTIBASE5 Developer Training.pdf](https://docs.altibase.com/download/attachments/19333461/D33_ALTIBASE5_%EA%B0%9C%EB%B0%9C%EC%9E%90%EA%B5%90%EC%9C%A1.pdf?version=2&modificationDate=1697612224000&api=v2)
- [Altibase_개발자교육_v1.pptx](https://docs.altibase.com/download/attachments/19333461/Altibase_%EA%B0%9C%EB%B0%9C%EC%9E%90%EA%B5%90%EC%9C%A1_v1.pptx?version=5&modificationDate=1759191535000&api=v2)

Document-format attachments preserved by R018:

- [JAVA_개발가이드.pdf](https://docs.altibase.com/download/attachments/14057500/JAVA_%EA%B0%9C%EB%B0%9C%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1698304337000&api=v2)
- [ALTIBASE_Windows_ODBC_개발가이드.pdf](https://docs.altibase.com/download/attachments/13436856/ALTIBASE_Windows_ODBC_%EA%B0%9C%EB%B0%9C%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1698199482000&api=v2)
- [ALTIBASE_Windows_AOD.NET_개발가이드.pdf](https://docs.altibase.com/download/attachments/11698513/ALTIBASE_Windows_AOD.NET_%EA%B0%9C%EB%B0%9C%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1698127982000&api=v2)
- [LobSpringIbatisSample.zip](https://docs.altibase.com/download/attachments/9109742/LobSpringIbatisSample.zip?version=1&modificationDate=1447388295000&api=v2)

Legacy source limitation:

- `APRE_New_Features_업그레이드_가이드.pdf` is a legacy `#` placeholder from the Korean source with no downloadable URL in source. Do not invent a URL.

Embedded APRE New Features screenshots and Makefile screenshots are registered as `not_document_format` in `llm-reference/coverage/attachment-diagram-register.tsv`; the answer-affecting semantics from those screenshots are represented as text and code examples in this document.

Embedded R018 screenshots for Java classpath/Eclipse setup, Windows ODBC setup, unixODBC download, ADO.NET Visual Studio setup, 32-bit Windows ODBC setup, and PHP Hangul terminal/session settings are registered as `not_document_format`; the procedural semantics are represented in text above.

External references and source pages:

- `https://docs.altibase.com/display/arch/Altibase+Precompiler+Guide`
- `https://docs.altibase.com/pages/viewpage.action?pageId=15630378`
- `https://docs.altibase.com/pages/viewpage.action?pageId=22643052`
- `https://docs.altibase.com/display/arch/JAVA+Developer%27s+Guide`
- `https://docs.altibase.com/display/arch/Altibase+ODBC+Development+Guide+in+Windows+Environment`
- `https://docs.altibase.com/display/arch/Altibase+and+unixODBC+Integration+Guide`
- `https://docs.altibase.com/display/arch/Altibase+Window+ADO.NET+Development+Guide`
- `https://docs.altibase.com/display/arch/PHP+Integration+Guide+for+Altibase`
- `https://docs.altibase.com/display/FAQE/How+to+use+Fail-Over+in+Altibase+JDBC`
- `https://docs.altibase.com/display/FAQE/How+to+change+the+jdbc.trc+file+creation+location`
- `https://docs.altibase.com/display/FAQE/Simultaneous+connections+to+different+Altibase+versions+via+JDBC`
- `https://docs.altibase.com/display/FAQE/32-bit+ODBC+installation+on+64-bit+Windows`
- `https://docs.altibase.com/display/FAQE/Integrating+with+unix_odbc`
- `https://docs.altibase.com/display/FAQE/ODBC+function%2C+SQLFreeStmt`
- `https://docs.altibase.com/display/FAQE/Hangul+is+broken+when+using+php`
- `http://support.altibase.com`
- `http://support.altibase.com/en/product`
- `http://support.altibase.com/en/manual`
- `http://www.unixodbc.org`
- `http://php.morva.net/manual/kr/index.php`

## Terminology

Keep these identifiers untranslated in multilingual answers:

- Product and precompiler names: `Altibase`, `ALTIBASE`, `APRE*C/C++`, `SES*C/C++`, `APRE`, `SES`, `Precompiler of Embedded SQL`.
- Executables and commands: `apre`, `sesc`, `make`, `gmake`, `ldd`, `nm`, `man`, `file`, `cc`, `gcc`, `g++`, `xlc_r`.
- Source and generated files: `.sc`, `.c`, `.cpp`, `connect1.sc`, `connect1.c`, `connect1.cpp`, `Testsample.sc`, `altibase_env.mk`, `Makefile`.
- Libraries: `libapre.a`, `libapre_sl.so`, `libodbccli_sl.so`, `libsesc.a`, `libsesc_sl.so`, `-lapre`, `-lodbccli`, `-lsesc`, `-lpthread`, `-lpthreads`, `-lm`, `-ldl`, `-lcrypt`, `-lrt`, `-lstdc++`, `-lC`, `-lCrun`, `-ldemangle`, `-lsocket`, `-lnsl`, `-lunwind`.
- Embedded SQL and variables: `EXEC SQL`, `DECLARE SECTION`, `ARGUMENT SECTION`, `CONNECT`, `DISCONNECT`, `FREE`, `AUTOCOMMIT`, `COMMIT`, `ROLLBACK`, `DECLARE CURSOR`, `WITH HOLD`, `PREPARE`, `EXECUTE`, `WHENEVER`, `SQLERROR`, `NOT FOUND`, `sqlca.sqlcode`, `SQLCODE`, `SQLSTATE`, `sqlca.sqlerrm.sqlerrmc`, `sqlca.sqlerrd[2]`.
- Properties and connection keys: `AUTO_COMMIT`, `IPC_CHANNEL_COUNT`, `CONNTYPE`, `DSN`, `PORT_NO`, `AlternateServers`, `ConnectionRetryCount`, `ConnectionRetryDelay`, `SessionFailOver`, `LoadBalance`, `QUERY_TIMEOUT`, `FETCH_TIMEOUT`, `UTRANS_TIMEOUT`.
- Paths: `$ALTIBASE_HOME/bin`, `$ALTIBASE_HOME/include`, `$ALTIBASE_HOME/lib`, `$ALTIBASE_HOME/install/altibase_env.mk`, `$ALTIBASE_HOME/sample/APRE`, `$ALTIBASE_HOME/conf/altibase.properties`, `$ALTIBASE_HOME/msg/manual.txt`, `$ALTIBASE_HOME/trc/altibase_boot.log`.
- Version labels and modes: `Altibase 5.1`, `5.3`, `5.3.3`, `5.5.1`, `6.3.1`, `7.3`, `CTF`, `STF`, `FAC`, `PBT`, `-parse none`, `-parse partial`, `-parse full`, `-t c`, `-t cpp`, `-I`, `-D`, `-keyword`, `-unsafe_null`, `-n`.
- Java/JDBC identifiers: `Altibase.jar`, `Altibase5.jar`, `Altibase6_5.jar`, `Altibase7_3.jar`, `Altibase.jdbc.driver.AltibaseDriver`, `Altibase5.jdbc.driver.AltibaseDriver`, `Altibase7_3.jdbc.driver.AltibaseDriver`, `AltibaseConnectionPoolDataSource`, `ABPoolingDataSource`, `AltibaseXADataSource`, `ABXADataSource`, `AltibaseXAResource`, `ABXAResource`, `PreparedStatement`, `CallableStatement`, `ResultSet`, `DriverManager.getConnection`, `setAutoCommit(false)`, `executeBatch()`, `setFetchSize()`, `setObject(parameterIndex, null, SQLType.NULL)`, `setNull(parameterIndex, null)`.
- JDBC URLs and trace identifiers: `jdbc:Altibase://ip_address:port_no/db_name`, `jdbc:Altibase_5.6.2://`, `AlternateServer`, `FailOver_Source`, `HealthCheckDuration`, `V$SESSION.FAILOVER_SOURCE`, `jdbc.trc`, `jdbc.trc.lck`, `ALTIBASE_JDBC_TRCLOG_DISABLE`, `08F01`, `ES_08FO01`.
- ODBC and unixODBC identifiers: `ALTIBASE_HDB_ODBC_64bit`, `C:\windows\sysWOW64\odbcad32.exe`, `windows.h`, `sql.h`, `sqlext.h`, `afxdb.h`, `odbc32.lib`, `LongDataCompat`, `libaltibase_odbc-64bit-ul32.so`, `libaltibase_odbc-64bit-ul64.so`, `libaltibase_odbc.so`, `SQLLEN`, `SQLULEN`, `BUILD_LEGACY_64_BIT_MODE`, `BUILD_REAL_64_BIT_MODE`, `ODBCINI`, `ODBCSYSINI`, `odbc.ini`, `odbcinst.ini`, `odbcinst -j`, `isql`, `dltest`, `SQLFreeStmt`, `SQL_CLOSE`, `SQL_DROP`, `SQL_UNBIND`, `SQL_RESET_PARAMS`, `SQLBindCol()`, `SQLBindParameter()`.
- ADO.NET identifiers: `Altibase.Data.AltibaseClient.dll`, `odbccli_sl.dll`, `Altibase.Data.AltibaseClient`, `AltibaseConnection`, `AltibaseCommand`, `AltibaseDataReader`, `AltibaseDataAdapter`, `AltibaseTransaction`, `DataSet`, `DTC`, `XA transaction`, `altiadonetX.X.X_32/64bit.zip`, `altiadonetX.X.X.X_32bit.zip`, `altiadonetX.X.X.X_64bit.zip`, `%ALTIBASE_HOME%/lib`, `PATH`, `System.BadImageFormatException`, `System.DllNotFoundException`.
- PHP and Spring identifiers: `PHP`, `PERL`, `resource`, `HashTable`, `db.php`, `odbc_connect`, `odbc_exec`, `odbc_prepare`, `odbc_execute`, `odbc_do`, `odbc_fetch_row`, `odbc_result`, `odbc_close`, `memory_limit`, `odbc.defaultbinmode`, `odbc.defaultlrl`, `NLS_USE`, `chcp 65001`, `Spring+iBatis`, `DataSourceTransactionManager`, `TransactionTemplate`, `transactionTemplate.execute()`, `doInTransaction()`, `<tx:advice>`, `TransactionProxyFactoryBean`, `@Transactional(propagation=Propagation.REQUIRED)`, `DefaultAutoCommit`, `SetAutoCommitAllowed`, `AltibaseClobStringTypeHandler`, `LobSpringIbatisSample.zip`.
