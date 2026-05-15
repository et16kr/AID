---
title: "Cannot insert new records after deleting bulk records"
page_id: "2557870"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Cannot+insert+new+records+after+deleting+bulk+records"
updated_at: "2011-08-16T12:12:28.000+0900"
version: 30
ancestors: ["Home", "ALTIBASE HDB Troubleshooting"]
labels: []
---

# Cannot insert new records after deleting bulk records
Source: https://docs.altibase.com/display/FAQE/Cannot+insert+new+records+after+deleting+bulk+records
Updated: 2011-08-16T12:12:28.000+0900

## Problem Abstract

Disk Tablespace gets full and data cannot be inserted anymore.

This problem was reported by an ALTIBASE HDB customer. In this document, we will reference the reported case while examining the causes of the problem and the possible resolution options.

## Background

### FMS (Freelist Managed Segment)

ALTIBASE HDB 5.3.3 manages disk pages with FMS technique.

Unknown macro: {gliffy}

In FMS technique, used and available pages are added to the head of the freelist. Although the pages are added to the freelist, they are not usable until the Ager cleans them.

ALTIBASE HDB has to allocate a new page to insert data, if all pages at the header are not aged. By default, only 5 pages are searched to allocate the space for the new data. ALTIBASE HDB can search more than 5 pages by modifying the ALTIBASE HDB provided properties. However, the performance can be degraded if the value gets bigger.

### Tablespace

Unless specified otherwise, ALTIBASE HDB stores data and Index in the same Tablespace, and they are managed in a Segment unit. Each Segment requests a page to the Tablespace if it needs more space to store data or Index.

Unknown macro: {gliffy}

## Cause of the Problem

There are three possible causes for the issue.

### Inefficient page usage

ALTIBASE HDB provides two properties - PCTUSED and PCTFREE for controlling the page usage.

PCTFREE: the amount of space kept free on each page for the update statement - versioning. The value specified by PCTFREE indicates the percentage of space kept free in order to allow existing records to be updated.

PCTUSED: once the page gets full, it does not return to the insert-able state until the amount of space gets smaller than the value specified on this value.

If the page usage is as follows, ALTIBASE HDB cannot reuse the existing pages, but allocates a new page for the new data being inserted.

Unknown macro: {gliffy}

Since the value of properties are already changed - PCTUSED = 80, this is not the case at this time.

This problem can occur on any disk database. To avoid this issue, DBA must perform reorganization on tables.

### Bulk insert and delete operations

ALTIBASE HDB cleans the page for only **committed data** . Therefore, it cannot work on pages with bulk insert/delete operations. By default, ALTIBASE HDB searches the first 5 available pages from the head of the freelist when it needs space for the operation. Under bulk operations, many pages are added to the head of the freelist; however, they are not available pages. Therefore, ALTIBASE HDB allocates a new page for the next bulk insert operation.

Since the Tablespace is full, ALTIBASE HDB cannot allocate the page and returns an error message.

According to the test case we got from the customer, this was not the issue in their case.

### Index Segment full

A page returns to the reusable state once it gets aged. A page allocated to the Index Segment gets aged when the 'SPLIT' operation is occurred. However, once the Index Segment and the Tablespace are full, the Index Segment cannot allocate a page from the Tablespace; therefore, 'SPLIT' operation fails.

Since ALTIBASE HDB cannot allocate a page to the Index Segment, the error message is returned.

## Solutions

### 1. Upgrade to 5.5.1

ALTIBASE HDB 5.5.1 uses TMS (Tree Managed Segment) technique for the page. This issue does not occur frequently with 5.5.1 as it does with 5.3.3 - this technique is also used by other database vendors such as Oracle.

However, an upgrade was not an option for the customer reporting the problem.

### 2. Commit frequently

The use of the Ager more frequently can help avoiding this problem. Thus it is recommended that the commit is performed more frequently in the bulk operations.

### 3. Seperate Tablespace

We noticed that the customer was using LOB data type. LOB data accelerates the problem since storing LOB data takes a lot of pages. Therefore, separating the Tablespace will reduce the possibility of the symptom.

It is recommended to separate the Tablespace - one for data and another for Index. In this way, the users can easily monitor the usage of the Tablespaces and prevent the problem in advance.

If the usage of Data and Index Tablespace are near 100%, then DBA may add datafile to prevent the Tablespace full situation.

Furthermore, it is recommended that the tables are refreshed periodically. ALTIBASE HDB does not support a reorganize function that is supported by some other database solutions such as Oracle. However the steps listed below can be used a a workaround for achieving the same re-org results:

1. export data 2. truncate tables 3. import data

This will gather the data distributed all over the pages and stack them from the first page.

Unknown macro: {gliffy}
