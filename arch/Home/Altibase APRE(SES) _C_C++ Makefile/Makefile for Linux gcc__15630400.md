---
title: "Makefile for Linux gcc"
page_id: "15630400"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/Makefile+for+Linux+gcc"
updated_at: "2025-09-23T09:17:14.000+0900"
version: 8
ancestors: ["Home", "Altibase APRE(SES) *C/C++ Makefile"]
labels: []
---

# Makefile for Linux gcc
Source: https://docs.altibase.com/display/arch/Makefile+for+Linux+gcc
Updated: 2025-09-23T09:17:14.000+0900

- [Additional library and compilation options for APRE compilation in Linux environment](#MakefileforLinuxgcc-AdditionallibraryandcompilationoptionsforAPREcompilationinLinuxenvironment) - [Library to be added to Makefile](#MakefileforLinuxgcc-LibrarytobeaddedtoMakefile) - [Compile options](#MakefileforLinuxgcc-Compileoptions) - [Example of Simple Makefile](#MakefileforLinuxgcc-ExampleofSimpleMakefile) - [Example of Makefile for 32bit compile](#MakefileforLinuxgcc-ExampleofMakefilefor32bitcompile)

Previously, we have looked at how to add the basic APRE library. This chapter describes the library and compilation options that must be additionally described in Makefile in the Linux gcc environment.

# Additional library and compilation options for APRE compilation in Linux environment

## **Library to be added to Makefile**

As already explained above, the basic APRE library "-lapre -lodbccli" should be described in Makefile.

When compiling with only the basic library added, there are system libraries referenced by the APRE library and a reference error occurs. Therefore, system libraries used in APRE must be specified in Makefile as follows.

| Library type | Makefile Library | Description |
| --- | --- | --- |
| C++ library | **-lstdc++** | When compiling using gcc in Altibase version 5.3.3 or lower version, specify C++ library |
| Dynamic Linking Loader(DL) Library | **-ldl** | Dynamically loaded (DL) library |
| Math related library | **-lm** | Library for using math functions |
| Posix thread library | **-lpthread** | Thread library for POSIX thread functions |
| Realtime Extensions Library | **-lrt** |  |

## **Compile options**

It is necessary to specify the following options to improve performance and specify the compile bit type.

| Option name | Option display | Description |
| --- | --- | --- |
| 32bit/64bit compilation mode | -m64 | Generate 64-bit code |
| -m32 | Generate 32-bit code |  |

By referring to the $ALTIBASE_HOME/install/altibase_env.mk file and $ALTIBASE_HOME/sample/APRE/Makefile, it can be referred to the optimized compile and link options when compiling APRE.

# **Example of Simple Makefile**

The simplest Makefile that can compile APRE in Linux gcc environment is completed as follows. In addition, if there is an additional library referenced by the program, the library must additionally be described in Makefile.

$ cat Makefile ALTI_INCLUDE=${ALTIBASE_HOME}/include ALTI_LIBRARY=${ALTIBASE_HOME}/lib **-lapre -lodbccli**

SYS_LIBS=******-lpthread -lm -ldl -lcrypt -lstdc++ **-lrt********

connect1.c:[connect1.sc](http://connect1.sc/)

[apre -t c](http://connect1.sc/)[connect1.sc](http://connect1.sc/)

[connect1:connect1.c](http://connect1.sc/)

cc -o connect1 connect1.c -I$(ALTI_INCLUDE) -L$(ALTI_LIBRARY) $(SYS_LIBS)

# **Example of Makefile for 32bit compile**

An example of the APRE Makefile for gcc that specifies the 32bit compile option is as follows. Specify "-m32" as a compile option, and specify the path where 32bit APRE Library is installed in the path referencing the Header file and Library. In addition, the APRE Precompiler specifies the path to run 32bit APRE.

ALTI_INCLUDE=**/alticlient32/include** ALTI_LIBRARY=**/alticlient32/lib** -lapre -lodbccli

SYS_LIBS=**-lpthread -lm -ldl -lc**

connect1.c:[connect1.sc](http://connect1.sc/)

[**/alticlient32/bin/apre** -t c](http://connect1.sc/)[connect1.sc](http://connect1.sc/)

[connect1:connect1.c](http://connect1.sc/)

gcc **-m32** -o connect1 connect1.c -I$(ALTI_INCLUDE) -L$(ALTI_LIBRARY) $(SYS_LIBS)

clean:

rm *.c *.o
