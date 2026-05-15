---
title: "How to change replication object IP"
page_id: "16876079"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/How+to+change+replication+object+IP"
updated_at: "2021-03-16T18:13:58.000+0900"
version: 1
ancestors: ["Home", "03. Replication"]
labels: []
---

# How to change replication object IP
Source: https://docs.altibase.com/display/FAQE/How+to+change+replication+object+IP
Updated: 2021-03-16T18:13:58.000+0900

- [Overview](#HowtochangereplicationobjectIP-Overview) - [Procedure](#HowtochangereplicationobjectIP-Procedure)

# Overview

---

This is a procedure guide for changing the registered IP to another IP when creating a replication object.

# Procedure

---

**1. Stop the replication object to be changed.**

```
ALTER REPLICATION replication_name STOP;
```

**2. Add new IP**

```
ALTER REPLICATION replication_name ADD HOST 'new_ip_address', replication_port;
```

**3. Remove exist IP**

```
ALTER REPLICATION replication_name DROP HOST 'old_ip_address', replication_port;
```

**4. Start replication object**

```
ALTER REPLICATION replication_name START;
```

**5. Check the host information of the replication object**

```
SELECT REPLICATION_NAME, HOST_IP, PORT_NO FROM SYSTEM_.SYS_REPL_HOSTS_ ORDER BY HOST_NO
```
