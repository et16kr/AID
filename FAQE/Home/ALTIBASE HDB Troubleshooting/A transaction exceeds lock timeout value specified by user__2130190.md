---
title: "A transaction exceeds lock timeout value specified by user"
page_id: "2130190"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/A+transaction+exceeds+lock+timeout+value+specified+by+user"
updated_at: "2011-08-03T17:40:37.000+0900"
version: 9
ancestors: ["Home", "ALTIBASE HDB Troubleshooting"]
labels: []
---

# A transaction exceeds lock timeout value specified by user
Source: https://docs.altibase.com/display/FAQE/A+transaction+exceeds+lock+timeout+value+specified+by+user
Updated: 2011-08-03T17:40:37.000+0900

- [What is this error?](#Atransactionexceedslocktimeoutvaluespecifiedbyuser-Whatisthiserror?)
- [How to confirm this condition?](#Atransactionexceedslocktimeoutvaluespecifiedbyuser-Howtoconfirmthiscondition?)
- [How to resolve this case?](#Atransactionexceedslocktimeoutvaluespecifiedbyuser-Howtoresolvethiscase?)

# What is this error?

```
Session-1
iSQL> AUTOCOMMIT OFF;
iSQL> UPDATE T1 SET C1 = C1 + 1;

Session-2
iSQL> DROP INDEX IDX33; (IDX33 is relate with T1 table)
[ERR-11075 : The transaction exceeds lock timeout specified by user.]
```

This error occurs when a session executing a DDL tries to put a lock on a table is already locked by other session. This error can also occur when a replication transaction tries to put a lock on a table that is already locked by a local transaction. (In this case, you can find the error message in $ALTIBASE_HOME/trc/altibase_rp.log)

# How to confirm this condition?

Users will need to validate to make sure that in fact there is a lock on the target table by another session. To learn more about how to check session conditions, [please review this content.](http://aid.altibase.com/display/arch/Miscellaneous+queries#Miscellaneousqueries-Lock%26TransactionInformation)

# How to resolve this case?

There are two ways to resolve this problem. First, terminate session that has a lock on the target table. ([See this page.](http://aid.altibase.com/display/arch/How+to+terminate+a+session)) Second option is simply to wait for a while. Lock can be unlocked when users explicitly execute a commit or rollback.
