---
title: "How to check the privileges granted to an object"
page_id: "16876153"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/How+to+check+the+privileges+granted+to+an+object"
updated_at: "2021-03-18T14:55:00.000+0900"
version: 1
ancestors: ["Home", "05. SQL"]
labels: []
---

# How to check the privileges granted to an object
Source: https://docs.altibase.com/display/FAQE/How+to+check+the+privileges+granted+to+an+object
Updated: 2021-03-18T14:55:00.000+0900

- [Overview](#Howtochecktheprivilegesgrantedtoanobject-Overview) - [Version](#Howtochecktheprivilegesgrantedtoanobject-Version) - [How to check](#Howtochecktheprivilegesgrantedtoanobject-Howtocheck)

# Overview

---

DB users can grant privileges to objects using the grant statement. the user can search the relationship of object authority between DB users granted to the entire DB by using a query.

# Version

---

Available in all versions of ALTIBASE HDB 4.3.9 or later

# How to check

---

It can be searched with the query below.

```
SELECT a.user_name grantee,                                     -- User grantee
       c.user_name grantor,                                     -- User grantor
       f.user_name object_owner,                                -- Owner of the object
       e.table_name object_name,                                -- Name of object
       e.table_type object_type,                                -- Type of object
       replace(d.priv_name, '_', ' ') priv_name,                -- Name of privilege
       decode(b.with_grant_option, 0, 'NO', 'YES') grantable    -- Whether it is possible to re-grant the rights to the object
  FROM system_.sys_users_ a,
       system_.sys_grant_object_ b,
       system_.sys_users_ c,
       system_.sys_privileges_ d,
       system_.sys_tables_ e,
       system_.sys_users_ f
 WHERE c.user_name <> 'SYSTEM_'
   and b.grantee_id = a.user_id
   and b.grantor_id = c.user_id
   and b.priv_id = d.priv_id
   and b.obj_id = e.table_id
   and e.user_id = f.user_id
 ORDER BY grantee,
       grantor,
       object_owner,
       object_type,
       object_name,
       priv_name ;
```

**Example**

iSQL> create user user1 identified by user1;

iSQL> create user user2 identified by user2;

iSQL> connect user1/user1;

iSQL> create table user1_t1 ( c1 integer );

iSQL> grant select on user1_t1 to user2;

iSQL> grant insert on user1_t1 to user2;

GRANTEE GRANTOR OBJECT_OWNER OBJECT_NAME OBJECT_TYPE PRIV_NAME GRANTABLE --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- USER2 USER1 USER1 USER1_T1 T INSERT NO USER2 USER1 USER1 USER1_T1 T SELECT NO 2 rows selected.
