---
title: "ERR-3109F REPL sender failure to handshake with peer server"
page_id: "6979813"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-3109F+REPL+sender+failure+to+handshake+with+peer+server"
updated_at: "2014-10-27T15:35:22.000+0900"
version: 9
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-3109F REPL sender failure to handshake with peer server
Source: https://docs.altibase.com/display/FAQE/ERR-3109F+REPL+sender+failure+to+handshake+with+peer+server
Updated: 2014-10-27T15:35:22.000+0900

- [Version](#ERR-3109FREPLsenderfailuretohandshakewithpeerserver-Version)
- [Explanation](#ERR-3109FREPLsenderfailuretohandshakewithpeerserver-Explanation)
- [Cause](#ERR-3109FREPLsenderfailuretohandshakewithpeerserver-Cause)
- [Action](#ERR-3109FREPLsenderfailuretohandshakewithpeerserver-Action)
- [Reference](#ERR-3109FREPLsenderfailuretohandshakewithpeerserver-Reference)

## Version

All versions

## Explanation

Unable to create replication object.

## Cause

This error occurs if the replication target table schema is different.

## Action

1. Check whether the replication target tables have equal schemas.

2. If different, match them with the same schemas.

3. Re-create the replication object.

## Reference

N/A
