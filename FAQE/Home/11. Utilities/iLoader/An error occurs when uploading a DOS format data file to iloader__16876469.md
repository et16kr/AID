---
title: "An error occurs when uploading a DOS format data file to iloader."
page_id: "16876469"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876469"
updated_at: "2021-04-05T13:29:22.000+0900"
version: 2
ancestors: ["Home", "11. Utilities", "iLoader"]
labels: []
---

# An error occurs when uploading a DOS format data file to iloader.
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876469
Updated: 2021-04-05T13:29:22.000+0900

- [Overview](#AnerroroccurswhenuploadingaDOSformatdatafiletoiloader.-Overview) - [How to remove](#AnerroroccurswhenuploadingaDOSformatdatafiletoiloader.-Howtoremove) - [On Windows](#AnerroroccurswhenuploadingaDOSformatdatafiletoiloader.-OnWindows) - [On Linux/Unix](#AnerroroccurswhenuploadingaDOSformatdatafiletoiloader.-OnLinux/Unix) - [Convert to a UNIX-format file using dos2unix](#AnerroroccurswhenuploadingaDOSformatdatafiletoiloader.-ConverttoaUNIX-formatfileusingdos2unix) - [Remove ^M using sed](#AnerroroccurswhenuploadingaDOSformatdatafiletoiloader.-Remove^Musingsed) - [Starting from ALTIBASE HDB 5.5.1 ...](#AnerroroccurswhenuploadingaDOSformatdatafiletoiloader.-StartingfromALTIBASEHDB5.5.1...)

# Overview

---

To upload a DOS-format data file to `iloader` on a Unix/Linux server, convert the file by using an editor or `dos2unix`.

If `iloader` is executed without conversion, the following error may occur.

```
ERR-9102B : Token value length overflow.
```

In DOS-format files, the row termination code is CR (Carriage Return) + LF (Line Feed).

When `iloader` parses the data file, it recognizes `%n` (LF) as a row terminator. Therefore, a parsing error can occur when uploading a DOS-format data file.

When a DOS-format file is opened with `vi` on Linux/Unix, `^M` is attached to the line ends, or the file appears as follows:

"SYS_T.dat" [DOS] 225L, 33822C

# How to remove

---

## On Windows

---

- In Windows, it can be converted using an editing program.
- Ex) In UltraEdit, select File -> Convert ->'DOS->UNIX' and save

## On Linux/Unix

---

### Convert to a UNIX-format file using dos2unix

- The `dos2unix` command converts DOS/MAC files to UNIX format.

  **Example**

  ```
  $ dos2unix SYS_T.dat
  dos2unix: converting file SYS_T.dat to UNIX format ...
  ```

  **File type comparison before and after dos2unix execution**

  ```
  $ file SYS_T.dat
  SYS_T.dat: ISO-8859 text, with very long lines, with CRLF line terminators           # DOS format file

  $ dos2unix SYS_T.dat
  dos2unix: converting file SYS_T.dat to UNIX format ...

  $ file SYS_T.dat
  SYS_T.dat: ISO-8859 text, with very long lines                                       # UNIX format file
  ```

### Remove ^M using sed

- Use the file from which `sed` removed `^M` as the `iloader` data file.
- `^M` must be entered as Ctrl+v+m.

  **Example**

  ```
  $ sed 's/^M//g' SYS_T.dat > SYS_T.dat.1
  ```

## Starting from ALTIBASE HDB 5.5.1 ...

---

From ALTIBASE HDB 5.5.1, a file can be uploaded without conversion or modification by using `%r%n`, which means CR+LF, as the record separator.

**Example**

```
$ file SYS_T.txt
SYS_T.txt: ISO-8859 text, with CRLF, LF line terminators

$ iloader -s 127.0.0.1 -u sys -p manager in -f SYS_T.fmt -d SYS_T.txt -log SYS_T.log -bad SYS_T.bad -t "|" -r "%r%n"
-----------------------------------------------------------------
     Altibase Data Load/Download utility.
     Release Version 5.5.1.4.10
     Copyright 2000, ALTIBASE Corporation or its subsidiaries.
     All Rights Reserved.
-----------------------------------------------------------------
ISQL_CONNECTION : TCP
DATA_NLS_USE: MS949
UPLOAD : 13.5710 msec

     Load Count  : 2(T)
```
