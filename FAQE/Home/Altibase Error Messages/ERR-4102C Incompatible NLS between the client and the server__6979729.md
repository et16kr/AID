---
title: "ERR-4102C Incompatible NLS between the client and the server"
page_id: "6979729"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-4102C+Incompatible+NLS+between+the+client+and+the+server"
updated_at: "2014-11-19T16:54:28.000+0900"
version: 10
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-4102C Incompatible NLS between the client and the server
Source: https://docs.altibase.com/display/FAQE/ERR-4102C+Incompatible+NLS+between+the+client+and+the+server
Updated: 2014-11-19T16:54:28.000+0900

- [Version](#ERR-4102CIncompatibleNLSbetweentheclientandtheserver-Version)
- [Explanation](#ERR-4102CIncompatibleNLSbetweentheclientandtheserver-Explanation)
- [Cause](#ERR-4102CIncompatibleNLSbetweentheclientandtheserver-Cause)
- [Action](#ERR-4102CIncompatibleNLSbetweentheclientandtheserver-Action)
- [Reference](#ERR-4102CIncompatibleNLSbetweentheclientandtheserver-Reference)
    - [1. Check the Character Set](#ERR-4102CIncompatibleNLSbetweentheclientandtheserver-1.ChecktheCharacterSet)
    - [2. How to set the environmental variables](#ERR-4102CIncompatibleNLSbetweentheclientandtheserver-2.Howtosettheenvironmentalvariables)

## Version

5.3.3 or below

## Explanation

Unable to connect to the client.

## Cause

This error occurs if the character sets for Altibase and the client differ.

## Action

Set the NLS value of the client to the same value as the Altibase server. You can also set the character set by using the environmental variable called ALTIBASE_NLS_USE from iSQL.

## Reference

##### 1. Check the Character Set

```
iSQL> SELECT nls_use, nls_characterset FROM v$nls_parameters;
NLS_USE                                   NLS_CHARACTERSET
---------------------------------------------------------------------------------------
US7ASCII                                  MS949
```

(NLS_USE : Client Character Set, NLS_CHARACTERSET : DB Character Set)

##### 2. How to set the environmental variables

Execute the following command from the client shell.

```
$export ALTIBASE_NLS_USE=MS949
```
