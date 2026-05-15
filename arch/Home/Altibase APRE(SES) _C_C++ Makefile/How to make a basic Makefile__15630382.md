---
title: "How to make a basic Makefile"
page_id: "15630382"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/How+to+make+a+basic+Makefile"
updated_at: "2025-09-23T09:14:35.000+0900"
version: 12
ancestors: ["Home", "Altibase APRE(SES) *C/C++ Makefile"]
labels: []
---

# How to make a basic Makefile
Source: https://docs.altibase.com/display/arch/How+to+make+a+basic+Makefile
Updated: 2025-09-23T09:14:35.000+0900

- [Basic structure of Makefile](#HowtomakeabasicMakefile-BasicstructureofMakefile) - [Example Sources](#HowtomakeabasicMakefile-ExampleSources) - [Running the Precompile](#HowtomakeabasicMakefile-RunningthePrecompile) - [Makefile contents](#HowtomakeabasicMakefile-Makefilecontents) - [Execution](#HowtomakeabasicMakefile-Execution) - [Compiling](#HowtomakeabasicMakefile-Compiling) - [Specifying the header file and library path](#HowtomakeabasicMakefile-Specifyingtheheaderfileandlibrarypath) - [Specifying the basic library for APRE compilation](#HowtomakeabasicMakefile-SpecifyingthebasiclibraryforAPREcompilation) - [Add basic library for APRE](#HowtomakeabasicMakefile-AddbasiclibraryforAPRE) - [Adding the system library](#HowtomakeabasicMakefile-Addingthesystemlibrary) - [Referring to Altibase sample Makefile](#HowtomakeabasicMakefile-ReferringtoAltibasesampleMakefile) - [Using the ldd command](#HowtomakeabasicMakefile-Usingthelddcommand) - [Using the nm command](#HowtomakeabasicMakefile-Usingthenmcommand) - [Using the man page](#HowtomakeabasicMakefile-Usingthemanpage) - [Causes and solutions for bit errors during compilation](#HowtomakeabasicMakefile-Causesandsolutionsforbiterrorsduringcompilation) - [Using the APRE library suitable for compilation mode](#HowtomakeabasicMakefile-UsingtheAPRElibrarysuitableforcompilationmode) - [Downloading 32bit client development tool (Library and Precompiler)](#HowtomakeabasicMakefile-Downloading32bitclientdevelopmenttool(LibraryandPrecompiler)) - [Bit error when compiling](#HowtomakeabasicMakefile-Biterrorwhencompiling) - [How to check the bit in the library](#HowtomakeabasicMakefile-Howtocheckthebitinthelibrary) - [Adding C++ library](#HowtomakeabasicMakefile-AddingC++library) - [Using the C++ compiler](#HowtomakeabasicMakefile-UsingtheC++compiler)

To understand the structure of a Makefile, start with a simple C example. Because the Altibase Makefile specification follows the GNU specification, `gmake` is recommended. This document explains the general rules.

# Basic structure of Makefile

A Makefile is a scripting language that defines the processes that are going on to make an executable file. In this section, we are going to compile the following source.

```
#include <stdio.h>
main()
{
    printf (“hello, world\n”);
}
```

This source can be compiled at the prompt as follows.

```
Shell> cc –o a a.c
```

It can be compiled with make using the simple Makefile script as follows.

```
shell> vi Makefile
a:a.c # User-created protocols and dependencies
	cc -o a a.c # Describes the actual command line to be executed
```

1. `a:a.c` means that `a.c` must be found to create `a`; `make` checks whether it has changed.
2. `cc -o a a.c` is the command to execute when `a.c` exists.
3. `shell> make -f Makefile` runs the Makefile. If the file name is `Makefile`, `-f Makefile` can be omitted.

If there is no change to the same source, the error "make: is up to date" will be output because compilation does not need to be performed.

# Example Sources

The example source uses `$ALTIBASE_HOME/sample/APRE/connect1.sc`, which is included in the sample sources under the Altibase installation directory. This example is based on Altibase 5.3 or later.

This example was written based on the environment compiling based on the GCC compiler in Linux. Therefore, when using other Unix environments and compilers, a part of Makefile must be written differently for the environment.

Some of the sources are as follows.

```
Shell> vi connect1.sc
int main()
{
    char usr[20];
    char pwd[20];
    char opt [200];

    sprintf (usr, “sys”);
    sprintf (pwd, “manager”);
    sprintf (opt, “DSN=127.0.0.1;CONNTYPE=1;PORT_NO=27584”);

    EXEC SQL CONNECT :usr IDENTIFIED BY :pwd USING :opt ;
    if (sqlca.sqlcode != 0)
       printf (“ConnectErr: %d-%s\n”, SQLCODE,sqlca.sqlerrm.sqlerrmc);
```

# Running the Precompile

The APRE extension of Altibase uses "*.sc". Since this file is not in a format that can be directly interpreted by the C/C++ compiler, it must be converted into C/C++ source with the precompiler provided by Altibase.

1. ### Makefile contents

  ```
  connect1.sc:connect1.sc
     apre -t c connect1.sc
  ```
2. ### Execution

  ```
  Shell> make -f Makefile connect1.sc
  ```

  When running after creating the Makefile like this, connect1.c is newly created. (Depending on the extension option, change it to C/C++ according to the user environment.)

# Compiling

Now add a convention to the Makefile to make it the executable connect1.

![Makefile%20flow.png](https://docs.altibase.com/download/attachments/embedded-page/arch/How%20to%20make%20a%20basic%20Makefile/Makefile%20flow.png?api=v2)

Of course, it is okay to use pre-compilation protocols and compile conventions in the connect1 protocol. Here, it will be explained separately. In the above, because the connect1 protocol requires connect1.c in the make step, the protocol for connect1.c is found in the Makefile.

Since there is a corresponding protocol in the Makefile, it operates in the order of precompiling first and then cc compiling. However, when actually compiling, it will get the following error:

```
$ make -f Makefile connect1
apre -t c connect1.sc
-----------------------------------------------------------------
     Altibase C/C++ Precompiler.
     Release Version 6.5.1.3.0
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
cc -o connect1 connect1.c
connect1.c:9:29: error: ulpLibInterface.h: No such file or directory
connect1.c: In function 'main':
connect1.c:68: error: storage size of 'ulpSqlstmt' isn't known
..........................................................

make: *** [connect1] Error 1
```

Refer to the line in bold, there was an error that the header file could not be found. In the Makefile, the path to the header and library that the user used on the source to compile should be specified as described in the next step.

# Specifying the header file and library path

Modify Makefile as follows to refer to Header file and Library.

```
Shell> vi Makefile

ALTI_INCLUDE=${ALTIBASE_HOME}/include
ALTI_LIBRARY=${ALTIBASE_HOME}/lib

connect1.c: connect1.sc
	apre -t c connect1.sc

connect1 : connect1.c
	cc -o connect1 connect1.c -I$(ALTI_INCLUDE) -L$(ALTI_LIBRARY)
```

`ALTI_INCLUDE` and `ALTI_LIBRARY` are environment variables that apply only inside the Makefile, like environment variables set for a user account, and are added to the compiler command line. The next execution result shows a different error.

```
$ make connect1
apre -t c connect1.sc
cc -o connect1 connect1.c -I/altibase_home/include -L/ssd/altibase_home/lib
/tmp/ccREjTkg.o: In function `main':
connect1.c:(.text+0x13a): undefined reference to `ulpGetSqlca'
.............................................................................
.............................................................................
collect2: ld returned 1 exit status
make: *** [connect1] Error 1
```

The above error occurs when the compiler tries to refer to the library in which the functions used in the source are defined, but cannot find it at the compile stage. For headers, it is not necessary to specify every individual header file, but libraries must be specified.

# Specifying the basic library for APRE compilation

Modify the Makefile as follows.

## **Add basic library for APRE**

```
$ vi Makefile
ALTI_INCLUDE=${ALTIBASE_HOME}/include
ALTI_LIBRARY=${ALTIBASE_HOME}/lib
LIBS=-lapre -lodbccli

connect1.c: connect1.sc
	apre -t c connect1.sc

connect1: connect1.c
	cc -o connect1 connect1.c -I$(ALTI_INCLUDE) -L$(ALTI_LIBRARY) $(LIBS)
```

Altibase requires two libraries, `apre` and `odbccli`, when generating binaries with precompilation. These are located in `$ALTIBASE_HOME/lib`. The notation for the library in the Makefile is specified with the `-l` option. When looking at the file, it exists in the form of `libapre.a` or `libapre_sl.so`. In the library name, specify only the name without `lib` and the extension (`.a` or `.so`).

# Adding the system library

When checking the executed result after recompiling with only the basic library added, an error still occurs as follows.

```
$ make connect1
apre -t c connect1.sc
cc -o connect1 connect1.c -I/ssd/altibase_home/include -L/ssd/altibase_home/lib -lapre -lodbccli
/ssd/altibase_home/lib/libapre.a(ulpLibInterface.o): In function `ulpLibInit':
ulpLibInterface.c:(.text+0x77): undefined reference to `pthread_rwlock_init'
/ssd/altibase_home/lib/libapre.a(ulpLibInterface.o): In function `ulpDoEmsql':
ulpLibInterface.c:(.text+0x1e6): undefined reference to `pthread_rwlock_wrlock'
...........................................
...........................................
```

The above error occurs because the thread library for the POSIX thread function used in the APRE library is not found. As with the previously added library, other libraries must be added referenced by APRE to Makefile as the next step.

```
$ vi Makefile
ALTI_INCLUDE=${ALTIBASE_HOME}/include
ALTI_LIBRARY=${ALTIBASE_HOME}/lib
LIBS=-lapre -lodbccli -lpthread

connect1.c: connect1.sc
	apre -t c connect1.sc

connect1: connect1.c
	cc -o connect1 connect1.c -I$(ALTI_INCLUDE) -L$(ALTI_LIBRARY) $(LIBS)
```

Additional system libraries required for compilation and each compilation option differ depending on the OS environment and the type of compiler. For more detailed information, please refer to the description of each compiler in this document.

After checking the list of system libraries required when compiling apre by using the method below, the library can be added to Makefile.

1. How to refer to Altibase's sample Makefile
2. How to use the ldd command
3. How to use the nm command
4. How to refer to the man page

## Referring to Altibase sample Makefile

The list of libraries required for APRE compilation is listed in $ALTIBASE_HOME/install/altibase_env.mk. After referring to it, each library and option can be specified in the user's Makefile.

## Using the ldd command

The use of the ldd command is as follows.

```
$ ldd $ALTIBASE_HOME/bin/apre
        linux-vdso.so.1 =>  (0x00007fff977ff000)
        libdl.so.2 => /lib64/libdl.so.2 (0x000000369c200000)
        libpthread.so.0 => /lib64/libpthread.so.0 (0x000000369ca00000)
        libcrypt.so.1 => /lib64/libcrypt.so.1 (0x00000036a9600000)
        librt.so.1 => /lib64/librt.so.1 (0x000000369d600000)
        libstdc++.so.6 => /usr/lib64/libstdc++.so.6 (0x00000036a1600000)
        libm.so.6 => /lib64/libm.so.6 (0x000000369ce00000)
        libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x000000369fe00000)
        libc.so.6 => /lib64/libc.so.6 (0x000000369c600000)
        /lib64/ld-linux-x86-64.so.2 (0x000000369be00000)
        libfreebl3.so => /lib64/libfreebl3.so (0x00000036a9a00000)
```

## Using the nm command

If the undefined symbol is the `cos` function, run `nm -A /usr/lib/lib* | grep cos` as follows to determine which library reference is required for the undefined symbol.

```
$ nm -A /usr/lib/lib* | grep cos    ( cos is the undefined symbol name )
nm: /usr/lib/libc.so: File format not recognized
nm: /usr/lib/libfreebl3.chk: File format not recognized
nm: /usr/lib/libfreebl3.so: no symbols
/usr/lib/libm.so:00009480 t __acos
/usr/lib/libm.so:000105c0 t __acosf
/usr/lib/libm.so:00009510 t __acosh
/usr/lib/libm.so:00010640 t __acoshf
/usr/lib/libm.so:00017ec0 t __acoshl
/usr/lib/libm.so:00017e40 t __acosl
/usr/lib/libm.so:0000c140 t __cacos
/usr/lib/libm.so:00013050 t __cacosf
```

Since `libm.so` is referenced as above, add `-lm` to the Makefile.

## Using the man page

Using the UNIX man command, some symbols can be found using the following method for the purpose of the symbol and the library referenced by this symbol.

**$ man 3 cos** (`cos` is the undefined symbol name.)

COS(3) Linux Programmer Manual COS(3)

NAME cos, cosf, cosl - cosine function

SYNOPSIS #include <math.h>

**double cos(double x);** float cosf(float x); long double cosl(long double x);

**Link with -lm.**

The man page explains that the `cos` function is included in the math-related library, and that the library option `-lm` must be added when linking.

# Causes and solutions for bit errors during compilation

## Using the APRE library suitable for compilation mode

To make a 64bit program using APRE, a 64bit APRE compiler, a 64bit APRE library, header files, and the compiler-specific 64bit compilation option are required.

Similarly, to make a 32bit program for the APRE, a 32bit APRE compiler, a 32bit APRE library, header file, and a 32bit option must be specified to compile for 32bit.

### Downloading 32bit client development tool (Library and Precompiler)

Download and install the 32-bit client install package for the platform you want to install from the client selection at [http://support.altibase.com/en/product](http://support.altibase.com/en/product).

If the database server package is 64-bit, the 64-bit client development tools are installed with the server package by default. To install 64-bit development tools on a different server, download and install the 64-bit client install package from the client section at [http://support.altibase.com/en/product](http://support.altibase.com/en/product).

**![32bitclient_package.png](https://docs.altibase.com/download/attachments/embedded-page/arch/How%20to%20make%20a%20basic%20Makefile/32bitclient_package.png?api=v2)**

## **Bit error when compiling**

### How to check the bit in the library

If the compile bit and the bit of the linked APRE library do not match, an error occurs during compilation. In this case, check whether the corresponding library bit is 32bit or 64bit. Then, check the bit of the library in the following method.

```
shell> cd $ALTIBASE_HOME/lib # directory where the Altibase APRE library is installed
shell> file libapre_sl.so

libapre_sl.so: ELF 32-bit LSB shared object, Intel 80386, version 1 (GNU/Linux), dynamically linked, not stripped # If the 32bit APRE library is installed in Linux

libapre_sl.so: ELF 64-bit LSB shared object, x86-64, version 1 (GNU/Linux), dynamically linked, not stripped # If the 64bit APRE library is installed in Linux
```

As above, the bit of library can be checked with the "file" command, which is a Unix command, and the messages may be slightly different for each OS, but the bit can be changed with the same message.

**Bit options when compiling**

Bit-related compilation options must be specified for each compiler. The table below shows the 32bit and 64bit compilation options for each compiler. Options may differ depending on the type of CPU supported by the compiler. For other detailed options, please refer to the manual for each compiler.

| OS | SUN | HP | AIX | Linux |
| --- | --- | --- | --- | --- |
| cc compiler 64bit option | -xarch=v9 or "-m64 -xarch=sparc"<br>(when using the SUN Sparc) | +DD64 | -q64 | -m64 |
| cc compiler 32bit option | -xarch=v8plusa (when using the SUN Sparc) | +DD32 | -q32 | -m32 |

# **Adding C++ library**

Up to Altibase version 5.3.3, sesc precompiler is used, and a part of sesc library is built in C++ format. Therefore, in order to compile with a C compiler rather than a C++ compiler, several compatible system libraries are needed in order to refer to them in an interpretable form.

If the C++ related library is not included, an error that cannot find the C++ operator occurs as shown below.

## Error message generated during makefile

```
sesc -t c connect1.sc
-----------------------------------------------------------------
     Altibase C/C++ Precompiler.
     Release Version 5.3.3.38
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------

gcc -o connect1 connect1.c -I/ssd/altibase_home/include -L/ssd/altibase_home/lib -lsesc -lodbccli -lpthread -lm -ldl -lcrypt -lrt

/ssd/altibase_home/lib/libodbccli.a(idvHandlerTimer_aoc.o): In function `idvTimerThread::~idvTimerThread()':
idvHandlerTimer.cpp:(.gnu.linkonce.t._ZN14idvTimerThreadD0Ev+0xc): undefined reference to `operator delete(void*)`
/ssd/altibase_home/lib/libodbccli.a(idvHandlerTimer_aoc.o):(.gnu.linkonce.r._ZTI14idvTimerThread+0x0): undefined reference to `vtable for __cxxabiv1::__si_class_type_info'

...............................
```

To solve the error, add "**-lstdc++**" to the Makefile as follows in the case of gcc compiler to add C++ standard library.

```
$ vi Makefile
ALTI_INCLUDE=${ALTIBASE_HOME}/include
ALTI_LIBRARY=${ALTIBASE_HOME}/lib
LIBS=-lapre -lodbccli -lpthread -lm -lstdc++
```

**...............................**

When using a C compiler, add the C++ library required for each platform. Refer to the table below and add the appropriate library to the Makefile for each compiler.

| Platform | **Library** |
| --- | --- |
| SUN | -lCrun |
| HP | -lstd –lstream –lCsup -lc |
| AIX | -lC |
| LINUX | -lstdc++ -lc |

Starting from Altibase version 5.5.1, the APRE library was rewritten as C source code. Therefore, when compiling with a C compiler, it is not necessary to add a separate C++ library to Makefile.

### Using the C++ compiler

When using a C++ compiler, most of the problems listed above can be avoided, so this case is not explained separately. However, each C++ compiler has its own 64-bit option, so check the option for the compiler being used.
