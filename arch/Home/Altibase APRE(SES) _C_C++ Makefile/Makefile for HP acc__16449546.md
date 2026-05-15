---
title: "Makefile for HP acc"
page_id: "16449546"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/Makefile+for+HP+acc"
updated_at: "2025-09-23T09:15:52.000+0900"
version: 7
ancestors: ["Home", "Altibase APRE(SES) *C/C++ Makefile"]
labels: []
---

# Makefile for HP acc
Source: https://docs.altibase.com/display/arch/Makefile+for+HP+acc
Updated: 2025-09-23T09:15:52.000+0900

- [Additional libraries and compile options for APRE compile in HP UX environment](#MakefileforHPacc-AdditionallibrariesandcompileoptionsforAPREcompileinHPUXenvironment) - [Libraries to be added to Makefile](#MakefileforHPacc-LibrariestobeaddedtoMakefile) - [Compile options](#MakefileforHPacc-Compileoptions) - [Example of Simple Makefile](#MakefileforHPacc-ExampleofSimpleMakefile) - [Example of Makefile for 32bit compile](#MakefileforHPacc-ExampleofMakefilefor32bitcompile)

Previously, we discussed how to add the basic APRE library in the "How to make a basic Makefile" chapter. This chapter describes the library and compile options that should be additionally described in Makefile, which acc (C compiler) is used in HP UX environment.

# **Additional libraries and compile options for APRE compile in HP UX environment**

## **Libraries to be added to Makefile**

As previously mentioned, the basic APRE library "-lapre -lodbccli" must be described in Makefile.

When compiling with only the basic library added, there are system libraries referenced by the APRE library and a reference error occurs. Therefore, system libraries used in APRE must be specified in Makefile as follows.

| Library type | Makefile Library | Description |
| --- | --- | --- |
| Posix thread Library | **-lpthread** | Thread library for POSIX thread functions |
| Math related Library | **-lm** | Library for using math functions |
| Dynamic Linking Loader(DL) Library | **-ldld** | Dynamically loaded (DL) library |
| Unwind Express Library | **-lunwind** | Library for APIs that perform stack tracing and stack unwinding on Itanium-based servers |
| C++ Library | **-lstd –lstream –lCsup -lc** | In case of compiling using acc C compiler in Altibase version 5.3.3 or earlier version, specify C++ library |
| Realtime Extensions Library | **-lrt** |  |

## **Compile options**

It is necessary to specify the following options to improve performance and specify the compile bit type.

| Option | Option display | Description |
| --- | --- | --- |
| Multithread Program Compile option | -mt | Designation required when creating a program with multi-thread |
| Instruction Set Architecture (ISA) Designation | +DD64 | Creating 64-bit code for HP-UX on IA64 |
| +DD32 | Creating 32-bit code for HP-UX on IA64 |  |
| Warning option | +vnocompatwarnings | Option to reduce unnecessary warning messages |

Refer to `$ALTIBASE_HOME/install/altibase_env.mk` and `$ALTIBASE_HOME/sample/APRE/Makefile` for optimized compile and link options when compiling APRE.

# **Example of Simple Makefile**

The simplest Makefile that can compile APRE in HP acc environment is completed as follows. In addition, if there is an additional library referenced by the program, the library must be additionally described in Makefile.

```
ALTI_INCLUDE=$(ALTIBASE_HOME)/include
ALTI_LIBRARY=$(ALTIBASE_HOME)/lib
LIBS=-lapre -lodbccli -lpthread -lunwind -lm
LFLAGS=-mt +DD64 -Wl,+vnocompatwarnings -L.

connect1.c: connect1.sc
	$(ALTIBASE_HOME)/bin/apre -t c connect1.sc

connect1: connect1.c
	cc $(LFLAGS) -o connect1 connect1.c -I$(ALTI_INCLUDE) -L$(ALTI_LIBRARY) $(LIBS)

clean:
	rm *.c *.o
```

# **Example of Makefile for 32bit compile**

An example of the APRE Makefile for acc that specifies the 32bit compile option is as follows. Specify "+DD32" as a compile option, and specify the path where the 32bit APRE library is installed in the path referencing the header file and library. In addition, the APRE precompiler also specifies the path to execute 32bit APRE.

```
ALTI_INCLUDE=/alticlient32/include
ALTI_LIBRARY=/alticlient32/lib
LIBS=-lapre -lodbccli -lpthread -lunwind -lm
LFLAGS=-mt +DD32 -Wl,+vnocompatwarnings -L.

connect1.c: connect1.sc
	/alticlient32/bin/apre -t c connect1.sc

connect1: connect1.c
	cc $(LFLAGS) -o connect1 connect1.c -I$(ALTI_INCLUDE) -L$(ALTI_LIBRARY) $(LIBS)

clean:
	rm *.c *.o
```
