---
title: "make Cannot find a rule to create target connect1.o from dependencies."
page_id: "7340239"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=7340239"
updated_at: "2014-12-11T17:37:17.000+0900"
version: 8
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# make Cannot find a rule to create target connect1.o from dependencies.
Source: https://docs.altibase.com/pages/viewpage.action?pageId=7340239
Updated: 2014-12-11T17:37:17.000+0900

- [Version](#makeCannotfindaruletocreatetargetconnect1.ofromdependencies.-Version)
- [Explanation](#makeCannotfindaruletocreatetargetconnect1.ofromdependencies.-Explanation)
- [Cause](#makeCannotfindaruletocreatetargetconnect1.ofromdependencies.-Cause)
- [Action](#makeCannotfindaruletocreatetargetconnect1.ofromdependencies.-Action)
- [Reference](#makeCannotfindaruletocreatetargetconnect1.ofromdependencies.-Reference)

## Version

All versions

## Explanation

This error occurs if a source file is compiled using the Make utility of a sample source.

```
$ cd $ALTIBASE_HOME/sample/APRE
$ make connect1
make: Cannot find a rule to create target connect1.o from dependencies.
Stop.
```

## Cause

The Makefile in the $ALTIBASE_HOME/sample directory was created based on the GNU Make. Thus, this error occurs if Make is executed in the $ALTIBASE_HOME/sample directory. In a platform such as Linux, this error does not occur as the GNU Make is installed by default.

## Action

Change it to GNU Make (install, if necessary) then re-execute Make.

## Reference

Information about GNU Make can be checked as below:

```
$ make -v

GNU Make 3.81

Copyright (C) 2006 Free Software Foundation, Inc.

This is free software; see the source for copying conditions.

There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A

PARTICULAR PURPOSE.

This program built for rs6000-ibm-aix
```
