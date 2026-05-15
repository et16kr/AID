---
title: "How to create a user (CREATE USER) and change a password (ALTER USER)"
page_id: "16876036"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16876036"
updated_at: "2021-04-02T17:21:25.000+0900"
version: 2
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# How to create a user (CREATE USER) and change a password (ALTER USER)
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16876036
Updated: 2021-04-02T17:21:25.000+0900

**- [Overview](#Howtocreateauser(CREATEUSER)andchangeapassword(ALTERUSER)-Overview) - [Applicable versions](#Howtocreateauser(CREATEUSER)andchangeapassword(ALTERUSER)-Applicableversions) - [How to create a user and change a password](#Howtocreateauser(CREATEUSER)andchangeapassword(ALTERUSER)-Howtocreateauserandchangeapassword) - [How to change SYS user](#Howtocreateauser(CREATEUSER)andchangeapassword(ALTERUSER)-HowtochangeSYSuser) - [Reference Manual](#Howtocreateauser(CREATEUSER)andchangeapassword(ALTERUSER)-ReferenceManual)**

# Overview

---

In addition to the system user SYS user, general users can be created using the create user statement, and after creating the user, the user's password can be changed using the alter user statement.

# Applicable versions

---

- This document is written based on ALTIBASE HDB 6.3.1.
- If you need additional inquiries or updates, please leave a request post at [http://support.altibase.com/en/](http://support.altibase.com/en/) or make a comment on this page.

# How to create a user and change a password

---

```
-- Create
CREATE USER user_name IDENTIFIED BY password;
-- Change
ALTER USER user_name IDENTIFIED BY change_password;
-- Delete
DROP USER user_name;
DROP USER user_name CASCADE;
```

# How to change SYS user

---

The SYS user plays a special role as the database administrator.

Therefore, additional work is required when changing the password, please check through the following link:

[How to change sys user password](https://docs.altibase.com/display/FAQE/How+to+change+sys+user+password)

# Reference Manual

---

ALTIBASE SQL User's Manual
