---
title: "Can PUBLIC SYNONYM be dropped?"
page_id: "16875993"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16875993"
updated_at: "2021-03-11T15:51:08.000+0900"
version: 1
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# Can PUBLIC SYNONYM be dropped?
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16875993
Updated: 2021-03-11T15:51:08.000+0900

- [Impact of dropping PUBLIC SYNONYM](#CanPUBLICSYNONYMbedropped?-ImpactofdroppingPUBLICSYNONYM) - [How to drop PUBLIC SYNONYM](#CanPUBLICSYNONYMbedropped?-HowtodropPUBLICSYNONYM) - [How to create PUBLIC SYNONYM](#CanPUBLICSYNONYMbedropped?-HowtocreatePUBLICSYNONYM)

---

# Impact of dropping PUBLIC SYNONYM

---

Even if PUBLIC SYNONYM is all dropped, it does not affect the operation of the Altibase server.

# How to drop PUBLIC SYNONYM

---

PUBLIC SYNONYM is created when a database is created to provide convenience to DB users. Dropping it is not recommended because PUBLIC SYNONYM is used by common queries such as dual table lookups and is frequently used in procedures such as print and println.

However, if it needs to be dropped, the DROP statement can be used as follows.

Please drop it after checking whether PUBLIC SYNONYM is used in the application.

**DROP PUBLIC SYNONYM statement**

DROP PUBLIC SYNONYM *SYNONYM_NAME*;

**Example of dropping PRINTLN**

DROP PUBLIC SYNONYM *PRINTLN*;

# How to create PUBLIC SYNONYM

If a dropped PUBLIC SYNONYM is needed, create it as follows.

**CREATE PUBLIC SYNONYM statement**

CREATE PUBLIC SYNONYM *SYNONYM_NAME* FOR SYSTEM_.*OBJECT_NAME*;

**Example of creating PRINTLN**

CREATE PUBLIC SYNONYM *PRINTLN* FOR SYSTEM_.*PRINTLN*;
