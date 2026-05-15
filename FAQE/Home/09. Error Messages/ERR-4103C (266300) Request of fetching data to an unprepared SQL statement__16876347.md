---
title: "ERR-4103C (266300) Request of fetching data to an unprepared SQL statement."
page_id: "16876347"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876347"
updated_at: "2021-04-05T10:57:01.000+0900"
version: 3
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# ERR-4103C (266300) Request of fetching data to an unprepared SQL statement.
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876347
Updated: 2021-04-05T10:57:01.000+0900

- [Overview](#ERR-4103C(266300)RequestoffetchingdatatoanunpreparedSQLstatement.-Overview) - [Version](#ERR-4103C(266300)RequestoffetchingdatatoanunpreparedSQLstatement.-Version) - [Symptom](#ERR-4103C(266300)RequestoffetchingdatatoanunpreparedSQLstatement.-Symptom) - [Cause](#ERR-4103C(266300)RequestoffetchingdatatoanunpreparedSQLstatement.-Cause) - [When COMMIT/ROLLBACK is performed in the OPEN CURSOR state](#ERR-4103C(266300)RequestoffetchingdatatoanunpreparedSQLstatement.-WhenCOMMIT/ROLLBACKisperformedintheOPENCURSORstate) - [Solution](#ERR-4103C(266300)RequestoffetchingdatatoanunpreparedSQLstatement.-Solution) - [When COMMIT/ROLLBACK is performed in the OPEN CURSOR state](#ERR-4103C(266300)RequestoffetchingdatatoanunpreparedSQLstatement.-WhenCOMMIT/ROLLBACKisperformedintheOPENCURSORstate.1) - [1. Separation of fetch session and change DML session](#ERR-4103C(266300)RequestoffetchingdatatoanunpreparedSQLstatement.-1.SeparationoffetchsessionandchangeDMLsession) - [2. Declare a cursor only enough to be stored in the communication buffer, and then repetitively open the cursor](#ERR-4103C(266300)RequestoffetchingdatatoanunpreparedSQLstatement.-2.Declareacursoronlyenoughtobestoredinthecommunicationbuffer,andthenrepetitivelyopenthecursor) - [Reference](#ERR-4103C(266300)RequestoffetchingdatatoanunpreparedSQLstatement.-Reference) - [Differences by version](#ERR-4103C(266300)RequestoffetchingdatatoanunpreparedSQLstatement.-Differencesbyversion)

# Overview

---

This document describes an error that occurs during the record fetch process by using a cursor to process a select statement that returns multiple records.

# Version

---

Altibase 4.3.9

# Symptom

---

To process a query statement that returns multiple records, a CURSOR must be used in the following process.

1. DECLARE CURSOR
2. OPEN CURSOR
3. FETCH CURSOR
4. CLOSE/RELEASE CURSOR

Although the cursor is used as above, the 3. FETCH process proceeds to some extent in the CURSOR FETCH stage, and the `ERR-4103C (266300) Request of fetching data to an unprepared SQL statement.` error occurs even though there are still records to be fetched at some point.

Below is an example where an error occurs when using the cursor and the result of the error.

**Example of using cursor-SESC**

```

DECLARE CURSOR

OPEN CURSOR

/* fetch cursor in loop */
/* To retrieve all records that meet the conditions, the FETCH CURSOR statement is repeatedly executed until the execution result is SQL_NO_DATA. */
while(1)
{
    FETCH CURSOR ;

    if (sqlca.sqlcode == SQL_SUCCESS)
    {
        ...
    }
    else if (sqlca.sqlcode == SQL_NO_DATA)
    {
        ...
    }
    else
    {
        /* Even though there are records to be fetched at some point after fetching to some extent, the error 'ERR-4103C (266300) Request of fetching data to an unprepared SQL statement.' occurs.*/
        printf("Error : [%d] %s\n", SQLCODE, sqlca.sqlerrm.sqlerrmc);
        break;
    }
}
```

**Example of error occurrence result**

```
$ ./cursor1
<CURSOR 1>
[Success declare cursor]

[Success open cursor]

[Fetch Cursor]
------------------------------------------------------------------
DNO      DNAME                          DEP_LOCATION       MGR_NO
------------------------------------------------------------------
1     BUSINESS DEPT                  Seoul              100
2     BUSINESS DEPT                  Seoul              100
...Omitted...
908     BUSINESS DEPT                  Seoul              100
909     BUSINESS DEPT                  Seoul              100

Error : [-266300] Request of fetching data to an unprepared SQL statement.      /* Error occurred while performing fetch */
------------------------------------------------------------------
[Close Cursor]
------------------------------------------------------------------
Success close cursor
```

# Cause

---

## When COMMIT/ROLLBACK is performed in the OPEN CURSOR state

---

Altibase complies with the ANSI standard and is configured not to support the fetch across commit method by default. Therefore, if COMMIT or ROLLBACK is performed after opening the cursor, the cursor is forcibly closed according to the ANSI standard.

Fetch across commit is a method that performs COMMIT while fetching unit records after opening a cursor, which is not recommended by the ANSI standard.

For this reason, if an application performs COMMIT or ROLLBACK after opening the cursor, this error may occur.

The reason an error occurs while performing FETCH to some extent is that the first large amount of records is stored in the communication buffer during FETCH. An error occurs when fetching all the records in the communication buffer and fetching the next certain amount of records into the communication buffer.

The following is an example of creating an application that may cause an error by performing COMMIT or ROLLBACK in the cursor OPEN state.

```
non-autocommit mode

DECLARE CURSOR

OPEN CURSOR

while(1)
{
    FETCH CURSOR ;

    if (sqlca.sqlcode == SQL_SUCCESS) {

       /* Execute change DML */

       /* Perform COMMIT or ROLLBACK */

    }
    else if (sqlca.sqlcode == SQL_NO_DATA) {
       ...
    }
    else {
      /* An error occurs at this stage when all the records in the first communication buffer are processed and then placed in the second communication buffer. */
       ...
    }
}
```

# Solution

---

## When COMMIT/ROLLBACK is performed in the OPEN CURSOR state

---

Here are two solutions to deal with this error.

- Separate fetch and change DML operations using multiple connections
- Open the cursor repeatedly after declaring the cursor only enough to be contained in the communication buffer

All of the above solutions require application changes.

### 1. Separation of fetch session and change DML session

By using multiple connections within one application, COMMIT or ROLLBACK does not affect the cursor.

- Create a session that uses a cursor and a session that executes modified DML statements. It is described by defining it as CONN1 and CONN2, respectively.
- Whenever cursor FETCH is executed in the session using the cursor (CONN1), change DML is executed in CONN2 and COMMIT or ROLLBACK is executed.
- The session (CONN2) that executes the modified DML statement is set to non-autocommit mode.

The following is an example of creating an application that reflects this action.

```
/* Session for FETCH */
EXEC SQL AT conn1 CONNECT;

/* Session for performing change DML */
EXEC SQL AT conn2 CONNECT;

EXEC SQL AT conn2 AUTOCOMMIT OFF;

/* Declare cursor in CONN1, perform OPEN, FETCH */
EXEC SQL AT conn1 DECLARE cursor;
EXEC SQL AT conn1 OPEN cursor;
while (1)
{
    /* Perform FETCH on conn1 */
    EXEC SQL AT conn1 FETCH cursor

    if (sqlca.sqlcode == SQL_SUCCESS) {

          /* Change DML and COMMIT or ROLLBACK in conn2 */
          EXEC SQL AT conn2 INSERT or UPDATE or DELETE ;

          /* check sqlca.sqlcode */
          if (sqlca.sqlcode == SQL_SUCCESS) {
             ...
          }
          else {
             ...
          }

          /* The commit or rollback performed in conn2 does not affect the cursor use of conn1. */
          EXEC SQL AT conn2 commit or rollback;

          /* check sqlca.sqlcode */
          if (sqlca.sqlcode == SQL_SUCCESS) {
              ...
          }
          else {
              ...
          }
    }
    else if (sqlca.sqlcode == SQL_NO_DATA)  {
        ...
    }
    else    {
        ...
    }
}
```

### 2. Declare a cursor only enough to be stored in the communication buffer, and then repetitively open the cursor

After calculating the number of records enough to put in the communication buffer with one FETCH, declare the cursor using the LIMIT clause.

The communication buffer size of Altibase version 4.3.9 is 64K. Since the number of records in the communication buffer depends on the record size, the last value of the LIMIT clause varies depending on the operating environment.

Specify the number of records to be stored in the communication buffer in the LIMIT clause, and open the cursor again and use it while changing the start value of the LIMIT clause before opening the cursor.

The following is an example of creating an application that reflects this action.

```
/* The cursor is declared using the LIMIT clause. n is the last record value to be returned in the LIMIT clause and must be defined according to the operating environment. The number of records in the communication buffer depends on the record size. */
DECLARE CURSOR
         SELECT ~
           FROM ~
          WHERE ~
          LIMIT :s_start, n;

/* Declare the starting value used in the LIMIT clause. */
s_start = 1;

while(1)
{
    /* Cursor open is repeated until all records meeting the conditions are fetched. */
    OPEN CURSOR

        while(1)
        {
            FETCH CURSOR ;

            if (sqlca.sqlcode == SQL_SUCCESS) {

               /* Execute change DML */
            }
            else if (sqlca.sqlcode == SQL_NO_DATA) {
               ...
            }
            else {
               ...
            }
        }

        /* Perform COMMIT or ROLLBACK */

       /* Specify the starting value of the LIMIT clause. n is an example. */
       s_start = s_start + n ;

}

CLOSE CURSOR OR CLOSE RELEASE CURSOR
```

# Reference

---

## Differences by version

---

Depending on the Altibase version, the error messages that occur in the same situation may be different.

The difference in error messages that occurs when COMMIT/ROLLBACK is executed among FETCHs in a non-autocommit environment is as follows.

| Version | Error code | Error message | Reference page |
| --- | --- | --- | --- |
| Altibase 4.3.9 | ERR-4103C | Request of fetching data to an unprepared SQL statement. |  |
| Altibase 5.3.3 ~ 6.1.1 | 100 | Not found data | [Not found data](https://docs.altibase.com/pages/viewpage.action?pageId=16876451) |
| Altibase 6.3.1 or later | ERR-410D2 | Fetch out of sequence. | [ERR-410D2 (266450) Fetch out of sequence](https://docs.altibase.com/pages/viewpage.action?pageId=16876332) |
