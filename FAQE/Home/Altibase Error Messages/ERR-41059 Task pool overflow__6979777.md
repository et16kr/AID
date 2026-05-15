---
title: "ERR-41059 Task pool overflow"
page_id: "6979777"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-41059+Task+pool+overflow"
updated_at: "2014-11-19T10:35:27.000+0900"
version: 5
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-41059 Task pool overflow
Source: https://docs.altibase.com/display/FAQE/ERR-41059+Task+pool+overflow
Updated: 2014-11-19T10:35:27.000+0900

- [Version](#ERR-41059Taskpooloverflow-Version)
- [Explanation](#ERR-41059Taskpooloverflow-Explanation)
- [Cause](#ERR-41059Taskpooloverflow-Cause)
- [Action](#ERR-41059Taskpooloverflow-Action)
- [Reference](#ERR-41059Taskpooloverflow-Reference)

## Version

4.3.9 or above

## Explanation

Unable to connect to the database.

If this error message occurs, the existing session or transaction has to be terminated first to fix it.

## Cause

1. The number of new connections has increased.

2. The task was not cleaned up because it was not closed properly after the connection was terminated.

3. Connection fails because the status of all service threads is EXECUTE.

4. A new connection cannot be established because the number of transactions exceeds TRANSACTION_TABLE_SIZE.

## Action

If the server cannot be stopped, either terminate the client or disable was connection.

Otherwise,

1. Increase MAX_CLIENT.

2. View the application source to check that the tasks have been properly closed.

3. Increase TRANSACTION_TABLE_SIZE.

## Reference

1. Check the open files using the ulimit command since the number of sockets may exceed the number permitted for the Altibase account. Increase, if necessary.

```
Ulimit -n 1048576
```

2. Add the following to the /etc/security/limits.conf file.

```
Altibase account soft nofile 1048576
Altibase account hard nofile 1048576
```
