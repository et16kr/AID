---
title: "Makefile for SUN(Solaris) cc"
page_id: "16678920"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/Makefile+for+SUN%28Solaris%29+cc"
updated_at: "2025-09-23T09:17:42.000+0900"
version: 6
ancestors: ["Home", "Altibase APRE(SES) *C/C++ Makefile"]
labels: []
---

# Makefile for SUN(Solaris) cc
Source: https://docs.altibase.com/display/arch/Makefile+for+SUN%28Solaris%29+cc
Updated: 2025-09-23T09:17:42.000+0900

- [Library and Compile Options for APRE compile in SUN (Solaris) environment.](#MakefileforSUN(Solaris)cc-LibraryandCompileOptionsforAPREcompileinSUN(Solaris)environment.) - [Library to be added to Makefile](#MakefileforSUN(Solaris)cc-LibrarytobeaddedtoMakefile) - [Compile options](#MakefileforSUN(Solaris)cc-Compileoptions) - [Example of simple Makefile](#MakefileforSUN(Solaris)cc-ExampleofsimpleMakefile) - [Example of Makefile for 32bit compile](#MakefileforSUN(Solaris)cc-ExampleofMakefilefor32bitcompile)

Previously, we discussed how to add the basic APRE library in the "How to make a basic Makefile" chapter. This chapter describes the library and compile options that should be additionally described in Makefile, which in the SUN (Solaris) cc compiler is used.

# Library and Compile Options for APRE compile in SUN (Solaris) environment.

## **Library to be added to Makefile**

As previously mentioned, the basic APRE library "-lapre -lodbccli" must be described in Makefile.

When compiling with only the basic library added, there are system libraries referenced by the APRE library and a reference error occurs. Therefore, system libraries used in APRE must be specified in Makefile as follows.

| Library type | Makefile Library | Description |
| --- | --- | --- |
| Thread Library | **+Makefile or -lthread** | Thread library for POSIX thread functions |
| Math related Library | **-lm** | Library for using math functions |
| Dynamic Linking Loader (DL) Library | **-ldl** | Dynamically loaded (DL) Library |
| Networking Services Library | **-lnsl** | Library for using Networking Services functions |
| Sockets Library | **-lsocket** | Library for using Sockets functions |
| C++ Library | -lCrun -ldemangle | When compiling using cc in Altibase version 5.3.3 or lower version, specify C++ library |
| Realtime Extensions Library to be added | **-lrt** |  |

## **Compile options**

It is necessary to specify the following options to improve performance and specify the compile bit type.

| Option | Option display | Description |
| --- | --- | --- |
| Multithread program compile option | -mt | Need to specify when creating a program in multi-thread |
| Instruction Set Architecture (ISA) | -xarch=amd64 | When compiling 64bit program on AMD cpu (X86) platform |
| -xarch=sse2a | When compiling 32bit program on AMD cpu (X86) platform |  |
| -xarch=v9 | When compiling 64bit program on SUN sparc cpu platform |  |
| -xarch=v8plus | When compiling 32bit porgram on SUN sparc cpu platform |  |
| Performance option | -fast | Option for improving Runtime performance |

By referring to the $ALTIBASE_HOME/install/[altibase_env.mk](http://altibase_env.mk) file and $ALTIBASE_HOME/sample/APRE/Makefile, it can be referred to the optimized compile and link options when compiling APRE.

# Example of simple Makefile

The simplest Makefile that can compile APRE in SUN X86 cc environment is completed as follows. In addition, if there is an additional library referenced by the program, the library must additionally be described in Makefile. Depending on the platform type, the options for specifying the memory model (32bit/64bit) may vary, so refer to the compile option table described above and set it according to the platform type.

ALTI_INCLUDE=/altibase_home/include ALTI_LIBRARY=/altibase_home/lib LIBS=**-lapre -lodbccli -lthread -lposix4 -ldl -lkvm -lkstat -lsocket -lnsl -lgen -lC -lCrun -ldemangle -lm** LFLAGS=**-fast -mt -xarch=amd64** -L/opt/SUNWspro/lib/amd64 -L/usr/lib/amd64

connect1.c:[connect1.sc](http://connect1.sc/)

[/altibase_home/bin/apre -t c](http://connect1.sc/)[connect1.sc](http://connect1.sc/)

[connect1:connect1.c](http://connect1.sc/)

/opt/SUNWspro/bin/cc $(LFLAGS) -o connect1 connect1.c -I$(ALTI_INCLUDE) -L$(ALTI_LIBRARY) $(LIBS)

clean:

rm *.c *.o

# **Example of Makefile for 32bit compile**

An example of APRE Makefile for SUN X86 cc specifying the 32bit compile option is as follows. Specify "-xarch=sse2a" as a compile coption, and specify the path where the 32bit APRE library is installed in the path referencing the Header file and library. In addition, APRE precompiler also specifeis the path to execute 32bit APRE.

ALTI_INCLUDE=**/alticlient32/include** ALTI_LIBRARY=**/alticlient32/lib** LIBS=**-lapre -lodbccli -lpthread -lrt -ldl -lkvm -lkstat -lsocket -lnsl -lgen -lm**

LFLAGS=**-fast -mt -xarch=sse2a** -L/opt/SUNWspro/lib/amd64 -L/usr/lib/amd64

connect1.c:[connect1.sc](http://connect1.sc/)

[**/alticlient32/bin/apre** -t c](http://connect1.sc/)[connect1.sc](http://connect1.sc/)

[connect1:connect1.c](http://connect1.sc/)

/opt/SUNWspro/bin/cc $(LFLAGS) -o connect1 connect1.c -I$(ALTI_INCLUDE) -L$(ALTI_LIBRARY) $(LIBS)

clean:

rm *.c *.o
