---
title: "How to check the 8-digit errorcode of altibase_qp.log"
page_id: "16876313"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/How+to+check+the+8-digit+errorcode+of+altibase_qp.log"
updated_at: "2021-04-05T10:49:06.000+0900"
version: 3
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# How to check the 8-digit errorcode of altibase_qp.log
Source: https://docs.altibase.com/display/FAQE/How+to+check+the+8-digit+errorcode+of+altibase_qp.log
Updated: 2021-04-05T10:49:06.000+0900

- [Version](#Howtocheckthe8-digiterrorcodeofaltibase_qp.log-Version) - [Symptom](#Howtocheckthe8-digiterrorcodeofaltibase_qp.log-Symptom) - [How to check the 8-digit error code](#Howtocheckthe8-digiterrorcodeofaltibase_qp.log-Howtocheckthe8-digiterrorcode)

# Version

---

Version 6.1.1 or earlier.

In version 6.3.1 or later, it is expressed as a 5-digit error code.

# Symptom

---

Depending on the version of Altibase, the expression method of the error code in $ALTIBASE_HOME/trc/altibase_qp.log is different.

# Example of 6.1.1 version (expressed as an 8-digit error code)

```
[EXEC_DDL_BEGIN : DROP USER ALTITEST CASCADE]
[2013/04/01 11:02:17] [Thread-1105209696] [Level-2]
[EXEC_DDL_END : FAILURE] errorcode 822329545
```

# Example of 6.3.1 version (5 digit error code and error message are output)

```
[EXEC_DDL_BEGIN : DROP USER ALTITEST CASCADE]
[2014/05/21 15:12:48] [Thread-1157658976] [Level-2]
[EXEC_DDL_END : FAILURE] ERR-3103c : Undefined user name. The user specified as the owner of a table or an object was not found in the database.
0001 : DROP USER ALTITEST CASCADE
                ^       ^
```

In version 6.3.1 and later, error codes and messages that can be checked directly from altierr are displayed, so there is no difficulty in checking errors, but in versions below 6.1.1, there are no unknown error codes and error messages, making it difficult to check the contents of errors.

## How to check the 8-digit error code

---

Convert an 8-digit decimal error code to a Hexa value. (Use Windows calculator)

The first 5 digits of the converted number are the error code.

For example, if you convert the error code 822329545 above to Hexa, it becomes 3103C0C9.

Then the actual error code is 3103C.

The error code can be checked by using altierr.

$ altierr 0x3103C 0x3103C ( 200764) qpERR_ABORT_QDR_NOT_EXISTS_USER Undefined user name. The user specified as the owner of a table or an object was not found in the database. <0%s> # *Cause: # - The user specified as the owner of a table or an object was not found in the database. # *Action: # - Please make sure that a user name corresponding to the owner of an object is registered in the database
