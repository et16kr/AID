---
title: "ERR-5102E Invalid cursor state"
page_id: "7340159"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-5102E+Invalid+cursor+state"
updated_at: "2014-10-28T11:16:54.000+0900"
version: 13
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-5102E Invalid cursor state
Source: https://docs.altibase.com/display/FAQE/ERR-5102E+Invalid+cursor+state
Updated: 2014-10-28T11:16:54.000+0900

- [Version](#ERR-5102EInvalidcursorstate-Version)
- [Explanation](#ERR-5102EInvalidcursorstate-Explanation)
- [Cause](#ERR-5102EInvalidcursorstate-Cause)
- [Action](#ERR-5102EInvalidcursorstate-Action)
- [Reference](#ERR-5102EInvalidcursorstate-Reference)

## Version

5.1.1 or above.

## Explanation

Unable to use cursor or execute the SELECT statement using cursors in the application.

## Cause

This error can occur:

- when trying to open the cursor without closing the cursor that has been used.
- when trying to fetch the committed cursor.
- if the application's cursor calling order is incorrect.
- due to a concurrency control issue if a single connection is shared in a multithreaded environment.

## Action

Sometimes, when the user program is found to be a thread, there is a possibility of handling an invalid cursor from its own thread because concurrency control of the connection object is not performed properly. Thus, the CLOSE CURSOR clause has to be used whenever finishing using a cursor to resolve the problem.

DECLARE CURSOR

OPEN CURSOR

FETCH CURSOR

/*** CLOSE CURSOR ***/ This clause is missing in most of the cases.

1. Fix CURSOR DECLARE/OPEN/FETCH/CLOSE errors.

2. If the connection is being shared in a multithreaded environment, output thread numbers to check the cursor calling order.

3. If thread concurrency cannot be controlled in the application, give each thread a connection.

## Reference

This error can occur after a version upgrade to ALTIBASE HDB 5.1.1 or above.
