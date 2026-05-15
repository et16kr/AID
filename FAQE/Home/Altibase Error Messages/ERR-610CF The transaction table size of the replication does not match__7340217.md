---
title: "ERR-610CF The transaction table size of the replication does not match"
page_id: "7340217"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-610CF+The+transaction+table+size+of+the+replication+does+not+match"
updated_at: "2014-11-20T14:59:50.000+0900"
version: 7
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-610CF The transaction table size of the replication does not match
Source: https://docs.altibase.com/display/FAQE/ERR-610CF+The+transaction+table+size+of+the+replication+does+not+match
Updated: 2014-11-20T14:59:50.000+0900

- [Version](#ERR-610CFThetransactiontablesizeofthereplicationdoesnotmatch-Version)
- [Explanation](#ERR-610CFThetransactiontablesizeofthereplicationdoesnotmatch-Explanation)
- [Cause](#ERR-610CFThetransactiontablesizeofthereplicationdoesnotmatch-Cause)
- [Action](#ERR-610CFThetransactiontablesizeofthereplicationdoesnotmatch-Action)
- [Reference](#ERR-610CFThetransactiontablesizeofthereplicationdoesnotmatch-Reference)

## Version

4.3.9 or above

## Explanation

Unable to start replication.

## Cause

The TRANSACTION_TABLE_SIZE property for both local and remote servers is different.

## Action

Set an identical value for TRANSACTION_TABLE_SIZE on both servers. Change it from the altibase.properties file located in $ALTIBASE_HOME/conf/ directory, then restart the server.

## Reference

1. TRANSACTION_TABLE_SIZE can be changed without recreating the database from Altibase versions 5.1.5.9.3 or above.

2. If TRANSACTION_TABLE_SIZE is changed, older versions need to restart the server.
