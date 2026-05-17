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

Additional source read for the R017 wildcard boundary and cross-reference:

- `arch/Home/Altibase Precompiler Guide/4. Frequently Occurring Error Messages__22643006.md` - detailed SQLCODE/error coverage is canonical in `llm-reference/07-troubleshooting-error-messages.md`; this topic keeps the APRE development cross-reference and the high-level error-handling workflow.

## Source coverage notes

This R017 section covers Altibase APRE*C/C++, SES*C/C++ upgrade boundaries, embedded SQL development patterns, APRE host variables, `sqlca`, connection and transaction control, cursor/FAC handling, dynamic SQL, function/procedure calls, `WHENEVER`, failover connection strings, sample-code cautions, APRE/SES Makefile construction, platform-specific C/C++ link options, and attachment preservation.

`arch/Home/Altibase Developer Training__22642996.md` and `arch/Home/APRE_C_C++ New Features & Upgrade Guide__22643052.md` have attachment evidence in `source-stabilization/url-backed-attachments.tsv` and `source-stabilization/legacy-attachments.tsv`. Their document-format attachments and legacy source limitations are recorded in `llm-reference/coverage/attachment-diagram-register.tsv`.

`arch/Home/Altibase Precompiler Guide/4. Frequently Occurring Error Messages__22643006.md` is read in this job because the R017 wildcard source list includes the whole precompiler guide, but detailed error rows were already produced by R013. Use this document for APRE development context and use `llm-reference/07-troubleshooting-error-messages.md` for the full SQLCODE catalog.

The APRE sample program source includes illustrative code copied from the source. Some lines in the source sample are not compile-ready as written, for example `EXC SQL`, `INTEGE`, mixed `error_do`/`Error_do`, and `AUTOCOMMIT = FALSE:`. Preserve those as source sample cautions; when generating new working code, follow the syntax rules and APRE examples in the procedural sections instead of copying the sample blindly.

## Scope and audience

Use this document to answer developer, build engineer, DBA, support, and LLM questions about Altibase embedded SQL development in C and C++: choosing APRE options, writing `.sc` files, compiling APRE output, linking `libapre` and `libodbccli`, selecting platform libraries, diagnosing Makefile errors, handling host variables and NULL indicators, controlling connections and transactions, avoiding fetch-across-commit errors, and upgrading from SES*C/C++ to APRE*C/C++.

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

## Version-specific notes

| Version or boundary | Note |
| --- | --- |
| Altibase 5.1 or later | Plan-Cache internally shares execution plans executed by all sessions. |
| Altibase 5.3 or later | Host variable declaration clause can be omitted depending on `apre` option. |
| Altibase 5.3.3 or later | APRE*C/C++ replaces SES*C/C++; `apre -parse full` can recognize C host variables outside `DECLARE SECTION`; host variable initialization is supported; CTF/STF failover functions are available. |
| Altibase 5.3.3 or earlier | SESC library compatibility may require C++ libraries when compiling with a C compiler. |
| Altibase 5.5.1 or later | APRE library was rewritten in C source code, so a separate C++ library is not needed for APRE itself when compiling with a C compiler. |
| Altibase 6.3.1 or later | FAC can be avoided with `WITH HOLD` cursor behavior in non-auto-commit mode. |
| Altibase 7.3 | APRE New Features & Upgrade Guide basis version. |

## Related errors

Detailed error coverage for APRE/precompiler SQLCODEs is canonical in `llm-reference/07-troubleshooting-error-messages.md` under the precompiler SQLCODE catalog. This topic preserves development actions that prevent or triage those errors:

- Use `sqlca.sqlcode`, `SQLCODE`, and `SQLSTATE` consistently.
- Print `SQLCODE` and `sqlca.sqlerrm.sqlerrmc` in debug logs.
- Check cursor `PREPARE`, `DECLARE`, `OPEN`, `FETCH`, and `CLOSE` order.
- Use `EXEC SQL ALTER SESSION SET STACK SIZE = 4096;` for calculation stack overflow.
- Use `QUERY_TIMEOUT`, `FETCH_TIMEOUT`, and `UTRANS_TIMEOUT` overrides only after considering resource occupancy.
- Check `$ALTIBASE_HOME/trc/altibase_boot.log` for fetch and update-transaction timeout disconnects.

## Attachments and external references

Document-format attachments preserved by R017:

- [Altibase_Developer_Training_v1.pptx](https://docs.altibase.com/download/attachments/22642996/Altibase_Developer_Training_v1.pptx?version=1&modificationDate=1761004797000&api=v2)
- [D33_ALTIBASE5 Developer Training.pdf](https://docs.altibase.com/download/attachments/19333461/D33_ALTIBASE5_%EA%B0%9C%EB%B0%9C%EC%9E%90%EA%B5%90%EC%9C%A1.pdf?version=2&modificationDate=1697612224000&api=v2)
- [Altibase_개발자교육_v1.pptx](https://docs.altibase.com/download/attachments/19333461/Altibase_%EA%B0%9C%EB%B0%9C%EC%9E%90%EA%B5%90%EC%9C%A1_v1.pptx?version=5&modificationDate=1759191535000&api=v2)

Legacy source limitation:

- `APRE_New_Features_업그레이드_가이드.pdf` is a legacy `#` placeholder from the Korean source with no downloadable URL in source. Do not invent a URL.

Embedded APRE New Features screenshots and Makefile screenshots are registered as `not_document_format` in `llm-reference/coverage/attachment-diagram-register.tsv`; the answer-affecting semantics from those screenshots are represented as text and code examples in this document.

External references and source pages:

- `https://docs.altibase.com/display/arch/Altibase+Precompiler+Guide`
- `https://docs.altibase.com/pages/viewpage.action?pageId=15630378`
- `https://docs.altibase.com/pages/viewpage.action?pageId=22643052`
- `http://support.altibase.com`
- `http://support.altibase.com/en/product`

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
