---
title: "How to check the number of records affected by DML within the stored procedure"
page_id: "16876157"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/How+to+check+the+number+of+records+affected+by+DML+within+the+stored+procedure"
updated_at: "2021-03-18T14:59:03.000+0900"
version: 1
ancestors: ["Home", "06. Stored Procedure"]
labels: []
---

# How to check the number of records affected by DML within the stored procedure
Source: https://docs.altibase.com/display/FAQE/How+to+check+the+number+of+records+affected+by+DML+within+the+stored+procedure
Updated: 2021-03-18T14:59:03.000+0900

Use SQL%ROWCOUNT to find out how many records were affected by DML.

**Example**

```
CREATE OR REPLACE PROCEDURE proc1
AS
  v1 INTEGER;
BEGIN
  DELETE FROM MEM_T LIMIT 10 ;
  v1 := SQL%ROWCOUNT;
  PRINTLN(v1);
END;
/

Ex)

iSQL> exec proc1;
10
Execute success.
```

IE users

Copying the procedure creation statement in IE may create a blank space, so please use the attached file if necessary. SP_DML_RECORD_COUNT.txt
