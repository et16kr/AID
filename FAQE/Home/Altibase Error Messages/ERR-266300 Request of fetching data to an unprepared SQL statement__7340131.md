---
title: "ERR-266300 Request of fetching data to an unprepared SQL statement"
page_id: "7340131"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-266300+Request+of+fetching+data+to+an+unprepared+SQL+statement"
updated_at: "2014-10-29T11:08:29.000+0900"
version: 5
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-266300 Request of fetching data to an unprepared SQL statement
Source: https://docs.altibase.com/display/FAQE/ERR-266300+Request+of+fetching+data+to+an+unprepared+SQL+statement
Updated: 2014-10-29T11:08:29.000+0900

- [Version](#ERR-266300RequestoffetchingdatatoanunpreparedSQLstatement-Version)
- [Explanation](#ERR-266300RequestoffetchingdatatoanunpreparedSQLstatement-Explanation)
- [Cause](#ERR-266300RequestoffetchingdatatoanunpreparedSQLstatement-Cause)
- [Action](#ERR-266300RequestoffetchingdatatoanunpreparedSQLstatement-Action)
- [Reference](#ERR-266300RequestoffetchingdatatoanunpreparedSQLstatement-Reference)

## Version

6.3.1 or above

## Explanation

Unable to fetch.

## Cause

This error occurs when the database is running in non-autocommit mode and the COMMIT statement is executed before a fetch operation has completed.

If the fetch operation continues (using the open cursor) after the COMMIT statement has been executed, the cursor becomes invalid and the fetch operation fails.

## Action

1. Run the database in autocommit mode.

2. When running in non-autocommit mode, complete the fetch operation and then execute CLOSE CURSOR. Afterwards, execute COMMIT.

3. Use two or more multiple connections and execute the FETCH and COMMIT statements separately.

## Reference

N/A
