---
title: "Building a Large-Scale DRDB Index"
page_id: "22642978"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Building+a+Large-Scale+DRDB+Index"
updated_at: "2025-10-20T15:54:13.000+0900"
version: 1
ancestors: ["Home", "12. Others"]
labels: []
---

# Building a Large-Scale DRDB Index
Source: https://docs.altibase.com/display/FAQE/Building+a+Large-Scale+DRDB+Index
Updated: 2025-10-20T15:54:13.000+0900

# Overview

---

Indexing involves reading, sorting, and storing data.

Therefore, running indexes in parallel can actually degrade performance due to excessive disk I/O and buffer misses.

By configuring the properties as shown below, you can reduce I/O and buffer misses, optimize the sorting process, and ultimately shorten the build time for large-scale disk-based indexes.

# Solution

---

## **Version 6.5.1~7.1.0**

---

1. `BUFFER_AREA_SIZE` (unit: bytes): larger values are generally better.
2. `SORT_AREA_SIZE` (unit: bytes): number of physical cores in the system * 20 MB.
3. `DISK_INDEX_BUILD_MERGE_PAGE_COUNT` (unit: pages): 1% of `BUFFER_AREA_SIZE` is recommended, but consider `DISK_INDEX_BUILD_MERGE_PAGE_COUNT` as described in consideration 3.
4. `INDEX_BUILD_THREAD_COUNT` (unit: cores): number of physical cores in the hardware.

**Considerations**

---

1. `BUFFER_AREA_SIZE`

- The larger the value, the longer the STARTUP time will be.

2. `SORT_AREA_SIZE`

- When building a single index, memory usage is at least the size of SORT_AREA_SIZE. If two indexes are built in parallel, memory usage doubles to SORT_AREA_SIZE × 2.
   SORT_AREA_SIZE is also a shared property with disk temp tables, so changing it affects the operation of disk temp tables.

3. `DISK_INDEX_BUILD_MERGE_PAGE_COUNT`

- The unit of the property is the number of pages, while the unit of BUFFER_AREA_SIZE is bytes.
- If the property value is large but the index size is small, performance may actually degrade.
- Index build performance may degrade if the following condition is met:
  `DISK_INDEX_BUILD_MERGE_PAGE_COUNT > (index key length * number of records) / SORT_AREA_SIZE`

## **Version 7.3.0 or later**

---

1. `BUFFER_AREA_SIZE` (unit: bytes): larger values are generally better.
2. `DISK_INDEX_BUILD_SORT_AREA_SIZE` (unit: bytes): number of physical cores in the system * 20 MB.
3. `DISK_INDEX_BUILD_MERGE_PAGE_COUNT` (unit: pages): 1% of `BUFFER_AREA_SIZE`.
4. `INDEX_BUILD_THREAD_COUNT` (unit: cores): number of physical cores in the hardware.

**Considerations**

---

1. `BUFFER_AREA_SIZE`

- The larger the value, the longer the STARTUP time will be.

2. `DISK_INDEX_BUILD_SORT_AREA_SIZE`

- When building a single index, at least the amount of memory equal to DISK_INDEX_BUILD_SORT_AREA_SIZE is used. If two indexes are built in parallel, memory usage doubles to DISK_INDEX_BUILD_SORT_AREA_SIZE × 2.
   (SORT_AREA_SIZE is not used.)

3. `DISK_INDEX_BUILD_MERGE_PAGE_COUNT`

- The unit of the property is the number of pages, while the unit of BUFFER_AREA_SIZE is bytes.
- The following issue does not occur in version 7.3.0 or later:
  - If the property value is large but the index size is small, performance may actually degrade.
  - Index build performance may degrade if the following condition is met:
    `DISK_INDEX_BUILD_MERGE_PAGE_COUNT > (index key length * number of records) / SORT_AREA_SIZE`
