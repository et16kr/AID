---
title: "Makefile for AIX xlc"
page_id: "16252935"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/Makefile+for+AIX+xlc"
updated_at: "2025-09-23T09:15:23.000+0900"
version: 9
ancestors: ["Home", "Altibase APRE(SES) *C/C++ Makefile"]
labels: []
---

# Makefile for AIX xlc
Source: https://docs.altibase.com/display/arch/Makefile+for+AIX+xlc
Updated: 2025-09-23T09:15:23.000+0900

- [Library and compile options for APRE compile in AIX environment](#MakefileforAIXxlc-LibraryandcompileoptionsforAPREcompileinAIXenvironment) - [Library to be added to Makefile](#MakefileforAIXxlc-LibrarytobeaddedtoMakefile) - [Compile Options](#MakefileforAIXxlc-CompileOptions) - [Example of simple Makefile](#MakefileforAIXxlc-ExampleofsimpleMakefile) - [Example of Makefile for 32-bit compile](#MakefileforAIXxlc-ExampleofMakefilefor32-bitcompile) - [Example of Makefile using APRE Shared Library(libapre_sl.so)](#MakefileforAIXxlc-ExampleofMakefileusingAPRESharedLibrary(libapre_sl.so)) - [Example of Makefile for Shared library build using APRE source](#MakefileforAIXxlc-ExampleofMakefileforSharedlibrarybuildusingAPREsource) - [Considerations when building shared library](#MakefileforAIXxlc-Considerationswhenbuildingsharedlibrary)

Previously, we discussed how to add the basic APRE library in the "How to make a basic Makefile" chapter. This chapter describes the library and compile options that must be additionally described in Makefile in the environment in which the AIX xlc compiler is used.

# Library and compile options for APRE compile in AIX environment

## Library to be added to Makefile

As previously explained, the basic APRE library `-lapre -lodbccli` should be specified in the Makefile.

When compiling only with the basic library added, there are system libraries referenced by the APRE library and a reference error occurs. Therefore, system libraries used in APRE must be specified in Makefile as follows.

| Library type | Makefile added library name | Description |
| --- | --- | --- |
| Thread library | **-lpthreads** | Thread library for POSIX thread function |
| Math related library | **-lm** | Library for using math function |
| C++ library | **-lC** | Add when compiling using the C compiler in version 5.3.3 or earlier |

## Compile Options

It is necessary to specify the following options to improve performance and specify the compile bit type.

| Option | Option display | Description |
| --- | --- | --- |
| Option to specify the maximum memory segment size | -bmaxdata | When compiling a 32bit program, specify the maximum usable memory segment size (default 256M) |
| Option to specify the 32bit/64 compile mode | -q32 | When compiling a 32bit program |
| Option to specify the 32bit/64 compile mode | -q64 | When compiling a 64bit program |
| Compiler optimization mode | -O2 | Use compiler optimization level 2 |
| Option to use inline functions | -qinline | Enable inline functions instead of function calls to improve performance |
| Option for runtime linking | -brtl | Runtime linking option; set this when using a shared library |
| Option for symbol export | -bexpall | Export global symbols when creating a shared library |

Refer to `$ALTIBASE_HOME/install/altibase_env.mk` and `$ALTIBASE_HOME/sample/APRE/Makefile` for optimized compile and link options for APRE.

# Example of simple Makefile

The simplest Makefile that can compile APRE in an AIX xlc environment is as follows. If the program references additional libraries, add those libraries to the Makefile.

```makefile
ALTI_INCLUDE=$(ALTIBASE_HOME)/include
ALTI_LIBRARY=$(ALTIBASE_HOME)/lib
LIBS=-lapre -lodbccli -lpthreads -lm
LFLAGS=-O2 -qinline -q64 # 64bit compile mode

connect1.c:connect1.sc
	$(ALTIBASE_HOME)/bin/apre -t c connect1.sc

connect1:connect1.c
	cc $(LFLAGS) -o connect1 connect1.c -I$(ALTI_INCLUDE) -L$(ALTI_LIBRARY) $(LIBS)

clean:
	rm *.c *.o
```

# Example of Makefile for 32-bit compile

An example of Makefile for 32bit compile is as follows. Specify "-q32" as a compile option, and specify the path where 32bit APRE library is installed in the path referencing the Header file and Library. In addition, the APRE Precompiler also specifies the path to execute 32bit APRE. If necessary, increase the memory segment to be used in the program, such as "-bmaxdata:0x80000000". In case of "bmaxdata:0x80000000", it can be used up to 2G.

```makefile
ALTI_INCLUDE=/alticlient32/include
ALTI_LIBRARY=/alticlient32/lib
LIBS=-lapre -lodbccli -lpthreads -lm
LFLAGS=-O2 -qinline -q32 -bmaxdata:0x80000000 -L. # 32bit compile mode, setting the maximum memory segment size

connect1.c:connect1.sc
	/alticlient32/bin/apre -t c connect1.sc

connect1:connect1.c
	cc $(LFLAGS) -o connect1 connect1.c -I$(ALTI_INCLUDE) -L$(ALTI_LIBRARY) $(LIBS)

clean:
	rm *.c *.o
```

# Example of Makefile using APRE Shared Library (`libapre_sl.so`)

In `$ALTIBASE_HOME/lib`, `libapre_sl.so` and `libodbccli_sl.so` are provided as shared libraries in addition to `libapre.a`, which is a static library.

Using a shared library has the following advantages compared to using a static library:

- Can reduce the size of the executable file.
- After loading the library into memory, it can be shared, reducing the memory usage of the program
- When the used library is changed, only the library needs to be replaced and there is no need to recompile the executable file.

The following is an example Makefile that uses a shared library with the xlc compiler on AIX. To use runtime linking, add `-brtl` as a link option and add the APRE shared libraries.

```makefile
ALTI_INCLUDE=$(ALTIBASE_HOME)/include
ALTI_LIBRARY=$(ALTIBASE_HOME)/lib
LIBS=-lapre_sl -lodbccli_sl -lc -lpthreads -lm
LFLAGS=-O2 -brtl -qinline -q64 # 64bit compile mode

connect1.c:connect1.sc
	$(ALTIBASE_HOME)/bin/apre -t c connect1.sc

connect1:connect1.c
	cc $(LFLAGS) -o connect1 connect1.c -I$(ALTI_INCLUDE) -L$(ALTI_LIBRARY) $(LIBS)

clean:
	rm *.c *.o
```

# Example of Makefile for Shared library build using APRE source

If necessary, there is a case that a shared library consisting of a function that searches DB with APRE must be created and used by calling it from a program. The example below is an example of Makefile for creating a shared library with APRE.

First, write a C source for creating a library as follows.

**connect1.sc**

```
/* connect1.sc */
int contest_db();
int contest_db()
{
    /* declare host variables */
    EXEC SQL BEGIN DECLARE SECTION;
    char usr[10];
    char pwd[10];
    char conn_opt1[100];
    char conn_opt2[100];
    char conn_opt3[100];
    EXEC SQL END DECLARE SECTION;
    .................
    EXEC SQL CONNECT :usr IDENTIFIED BY :pwd USING :conn_opt3;
    ....
}
```

The Makefile for creating `libconn_sl.so`, which will be called by a program using `connect1.sc`, is as follows.

**Example of Makefile for shared library build**

```makefile
ALTI_INCLUDE=$(ALTIBASE_HOME)/include
ALTI_LIBRARY=$(ALTIBASE_HOME)/lib
LIBS=-lc -lpthreads -lm # -lapre_sl -lodbccli_sl must be linked when building an executable file.
LFLAGS=-O2 -lc -q64 # 64bit compile mode

SHLLIB=libconn_sl.so
OBJS=connect1.o

all: $(SHLLIB)

$(SHLLIB):$(OBJS)
	xlc_r -G -o $(SHLLIB) $(OBJS) -b64 -bexpall -I$(ALTI_INCLUDE) -L$(ALTI_LIBRARY) $(LIBS)

connect1.o:connect1.c
	xlc_r $(LFLAGS) -c connect1.c -I$(ALTI_INCLUDE) -L$(ALTI_LIBRARY) $(LIBS)

connect1.c:connect1.sc
	$(ALTIBASE_HOME)/bin/apre -t c connect1.sc

clean:
	rm *.o
```

### Example of Makefile that compiles the program used by calling Shared Library made with APRE function

First, create "alticonn.h" as a header file for APRE shared library.

**alticonn.h**

```
/* alticonn.h */
 int contest_db();
```

The user program calls `contest_db()` registered in `libconn_sl.so`. The source of the user program is as follows.

**test.c**

```
 /* test.c */
#include "alticonn.h"
extern int contest_db();
int main()
{
  contest_db();
}
```

### Example of Makefile for Execution Program Build

The Makefile to compile the user program that calls the `contest_db()` function registered in `libconn_sl.so` is as follows.

```makefile
ALTI_INCLUDE=$(ALTIBASE_HOME)/include
ALTI_LIBRARY=$(ALTIBASE_HOME)/lib
LIBS=-lapre_sl -lodbccli_sl -lc -lpthreads -lm
LFLAGS=-O2 -brtl -qinline -q64 # 64bit compile mode

INC_ALL=-I. -I$(ALTI_INCLUDE)
LIB_ALL=-L. -L$(ALTI_LIBRARY)

all:test

test:
	xlc_r $(LFLAGS) -o test test.c $(INC_ALL) $(LIB_ALL) -lconn_sl $(LIBS)

clean:
	rm *.c *.o
```

## Considerations when building shared library

In AIX, when creating and using more than one shared library, do not add `-lapre_sl` and `-lodbccli_sl` when building a shared library.

In AIX shared libraries, the global variables in the `apre_sl` and `odbccli_sl` libraries are recognized as different variables, so shared libraries cannot share them. Therefore, when creating a shared library, do not link the APRE libraries (`apre_sl`, `odbccli_sl`); link the APRE libraries when creating the executable binary.

For example, if the connection-related shared library is `con.so` and the select-related shared library is `sel.so`, and a binary is built and executed, an error occurs because `sel.so` cannot refer to the connection-related object in `con.so`. To prevent this error, add `apre_sl` and `odbccli_sl` as links only when creating an executable binary.
