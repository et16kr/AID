---
title: "Maximum Capacity Specifications for Altibase"
page_id: "16875989"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Maximum+Capacity+Specifications+for+Altibase"
updated_at: "2021-04-02T11:26:53.000+0900"
version: 2
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# Maximum Capacity Specifications for Altibase
Source: https://docs.altibase.com/display/FAQE/Maximum+Capacity+Specifications+for+Altibase
Updated: 2021-04-02T11:26:53.000+0900

| Altibase Database Engine Object | Maximum sizes / Numbers Altibase |
| --- | --- |
| Identifier length | 40 bytes |
| Tablespaces per database | 64 * 1,024 |
| Datafiles per tablespace | 1,023 |
| Datafile size | 32 gigabytes (64bit standard) |
| Users per database | 2,147,483,638 |
| Tables per database | 2,097,151 |
| Indexes per table | 64 |
| Columns per table | 1,024 |
| Columns per index | 32 |
| Rows per table | Limited by available storage OR maxrows |
| Partitions per partitioned table or index | 2,147,483,638 |
| Constraints per database | 2,147,483,638 |
| Replications per database | 6.1.1 or earlier : 32<br>6.3.1 or later : Set to REPLICATION_MAX_COUNT property |
| Tables per replication | 2147483647 |
