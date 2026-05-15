# J001 Baseline Inventory and Mapping

Review date: 2026-05-15

Workspace: `/home/et16/AID`

## Requirement Boundary

J001 is limited to baseline inventory before content review. This job confirms the current repository state, document counts, Korean-English technical document mappings, FAQ category mappings, and attachment coverage. It does not change Korean source documents, English target documents, or `manifest.json`.

Korean documents remain authoritative for later jobs. If a later content-review job finds a Korean-English difference, the English document must be updated from the Korean source unless a stop condition applies.

## Initial Git State

Before J001 edits, the only dirty tracked file was `.codex-jobs/ko-en-doc-coverage/jobs.tsv`, where the workflow runner had changed J001 from `ToDo` to `Progress`. The only untracked files were workflow runtime files under `.codex-jobs/ko-en-doc-coverage/.runtime/` and `.codex-jobs/ko-en-doc-coverage/logs/`.

No project documentation files under `DOCK/`, `arch/`, `faq/`, `FAQE/`, or `manifest.json` were dirty before editing.

## Design Note

This job adds this baseline note under the workflow directory and a workflow-local `.gitignore` for `.runtime/` and `logs/`. This keeps generated execution artifacts out of future project handoffs while preserving the tracked workflow files and job evidence.

No product-document structure, Korean-English mapping behavior, or Markdown source format changes are introduced by this job.

## Document Counts

| Set | Current Markdown count | Manifest `page_count` | Result |
| --- | ---: | ---: | --- |
| `DOCK/Home` | 51 | 51 | Matches |
| `arch/Home` | 181 | 181 | Matches |
| `faq/Home` | 115 | 115 | Matches |
| `FAQE/Home` | 241 | 241 | Matches |

## Technical Document Mapping

All 51 Korean technical documents under `DOCK/Home` have a corresponding English target root under `arch/Home`. When the English target is split into child pages, later content-review jobs must compare the Korean source against the English parent page plus its child-page directory.

| Korean source | English target root |
| --- | --- |
| `DOCK/Home/20. Altibase 설정 파일 가이드__13437165.md` | `arch/Home/Altibase Configuration File Guide__22642991.md` |
| `DOCK/Home/21. Altibase 디스크I_O 병목을 고려한 볼륨구성 가이드__11698408.md` | `arch/Home/Configuration Guide For Minimizing Disk I_O Contention__22643018.md` |
| `DOCK/Home/22. Altibase 운영을 위한 Solaris 설정 가이드__11698415.md` | `arch/Home/Solaris Setup Guide for Altibase__14058290.md` |
| `DOCK/Home/23. Altibase 운영을 위한 HPUX 설정 가이드__14057733.md` | `arch/Home/HPUX Setup Guide for Altibase__14058288.md` |
| `DOCK/Home/24. Altibase 운영을 위한 AIX 설정 가이드__13436846.md` | `arch/Home/AIX Setup Guide for Altibase__14058298.md` |
| `DOCK/Home/25. Altibase 데이터베이스 생성 가이드__13436812.md` | `arch/Home/Creating ALTIBASE Database__22643020.md` |
| `DOCK/Home/26. Altibase 기본적인 장애대응 절차__13435879.md` | `arch/Home/Responding to Failures Guide for Altibase__15138818.md` |
| `DOCK/Home/27. Altibase 이중화 구성 가이드__13828098.md` | `arch/Home/Altibase Replication Configuration Guide__14647672.md` |
| `DOCK/Home/28. Altibase TOMCAT 연동가이드__7341030.md` | `arch/Home/TOMCAT Integration Guide for Altibase__14058489.md` |
| `DOCK/Home/29. Altibase JEUS 연동가이드__7341028.md` | `arch/Home/JEUS Integration Guide for Altibase__14058459.md` |
| `DOCK/Home/30. Altibase JBoss 연동가이드__13437492.md` | `arch/Home/JBOSS Integration Guide for Altibase__14647358.md` |
| `DOCK/Home/31. Altibase 설치가이드__11698403.md` | `arch/Home/Altibase Installation Guide__14647632.md` |
| `DOCK/Home/32. Altibase와 unixODBC 연동 가이드__11698379.md` | `arch/Home/Altibase and unixODBC Integration Guide__14647413.md` |
| `DOCK/Home/33. Altibase 개발자교육__19333461.md` | `arch/Home/Altibase Developer Training__22642996.md` |
| `DOCK/Home/34. Altibase Precompiler 가이드__11698385.md` | `arch/Home/Altibase Precompiler Guide__14647438.md` |
| `DOCK/Home/35. Altibase APRE(SES) _C_C++ Makefile__11698493.md` | `arch/Home/Altibase APRE(SES) _C_C++ Makefile__15630378.md` |
| `DOCK/Home/36. Altibase 개발가이드__7341274.md` | `arch/Home/Altibase Development Guide__14058519.md` |
| `DOCK/Home/37. Altibase SQL 튜닝 가이드__19333563.md` | `arch/Home/Altibase SQL Tuning Guide__22643010.md` |
| `DOCK/Home/38. Altibase VC 2008 개발가이드__19333567.md` | `arch/Home/Altibase VC 2008 Development Guide__19333567.md` |
| `DOCK/Home/39. Altibase, Oracle 비교 자료__14058137.md` | `arch/Home/Altibase_Oracle Comparison__16875638.md` |
| `DOCK/Home/40. Oracle to Altibase 변환가이드__7341605.md` | `arch/Home/ORACLE to ALTIBASE Conversion Guide__22643038.md` |
| `DOCK/Home/41. Altibase Quick Install & Start for UNIX__13436834.md` | `arch/Home/Altibase Quick Install & Start for UNIX__16875604.md` |
| `DOCK/Home/42. Altibase 설치 시 발생할 수 있는 문제상황과 조치__13437056.md` | `arch/Home/Troubleshooting Altibase Installation Problems__15138879.md` |
| `DOCK/Home/43. Altibase STARTUP _ STOP 과정의 이해__13434993.md` | `arch/Home/Understanding the Altibase Start_Shut down Process__14909450.md` |
| `DOCK/Home/44. APRE_C_C++ New Features & 업그레이드 가이드__13435760.md` | `arch/Home/APRE_C_C++ New Features & Upgrade Guide__22643052.md` |
| `DOCK/Home/45. Altibase 운영을 위한 시스템 리소스 용량산정 가이드__14057887.md` | `arch/Home/System Data Capacity Estimation Guide for Altibase Operations__22643042.md` |
| `DOCK/Home/46. Altibase 버전 간 마이그레이션 가이드__19333688.md` | `arch/Home/Altibase Data Migration Process Guide__22642994.md` |
| `DOCK/Home/47. 문제분석을 위한 OS별 유틸리티 사용 가이드__13436866.md` | `arch/Home/Utility Guide for each OS for Problem Analysis__16875587.md` |
| `DOCK/Home/48. UNIX Memory Management__13436842.md` | `arch/Home/UNIX Memory Management__16875572.md` |
| `DOCK/Home/49. Altibase 이중화 제약사항 가이드__19333729.md` | `arch/Home/Altibase Replication Constraints Guide__22643008.md` |
| `DOCK/Home/50. Altibase 백업정책 결정을 위한 고려사항__14057586.md` | `arch/Home/Considerations for Altibase Backup Policy__14647709.md` |
| `DOCK/Home/51. Altibase window ADO.NET 개발 가이드__11698513.md` | `arch/Home/Altibase Window ADO.NET Development Guide__14647565.md` |
| `DOCK/Home/52. Altibase WebSphere 연동 가이드__13435602.md` | `arch/Home/WebSphere Integration Guide for Altibase__14058343.md` |
| `DOCK/Home/53. Windows 환경의 Altibase ODBC 개발 가이드__13436856.md` | `arch/Home/Altibase ODBC Development Guide in Windows Environment__15138911.md` |
| `DOCK/Home/54. Altibase Spring 연동 가이드__7340945.md` | `arch/Home/Spring Integration Guide for Altibase__14058410.md` |
| `DOCK/Home/55. Altibase iBATIS 연동가이드__7340053.md` | `arch/Home/iBatis Integration Guide for Altibase__14058303.md` |
| `DOCK/Home/56. JAVA 개발 가이드__14057500.md` | `arch/Home/JAVA Developer's Guide__16875544.md` |
| `DOCK/Home/57. Altibase 운영을 위한 Linux 설정 가이드__13436485.md` | `arch/Home/Linux Setup Guide for Altibase__22643022.md` |
| `DOCK/Home/58. Altibase Hibernate 연동가이드__14057878.md` | `arch/Home/Hibernate Integration Guide for Altibase__14058388.md` |
| `DOCK/Home/59. Altibase 모니터링 쿼리 가이드__10060431.md` | `arch/Home/Altibase Monitoring Queries Guide__14058229.md` |
| `DOCK/Home/60. Altibase WebLogic 연동가이드__7340101.md` | `arch/Home/WEBLOGIC Integration Guide for Altibase__14058319.md` |
| `DOCK/Home/61. Altibase VC 2010 개발가이드__19334121.md` | `arch/Home/Altibase VC 2010 Development Guide__19334121.md` |
| `DOCK/Home/62. Altibase CPU 과부하 현상에 대한 분석가이드__11698396.md` | `arch/Home/Altibase CPU Overload Analysis Guide__14647581.md` |
| `DOCK/Home/63. Altibase Memory 사용량 증가 분석가이드__11698518.md` | `arch/Home/Altibase Memory Usage Increase Analysis Guide__14647388.md` |
| `DOCK/Home/64. Altibase MyBatis 연동 가이드__7340818.md` | `arch/Home/MyBatis Integration Guide for Altibase__14058349.md` |
| `DOCK/Home/65. MSSQL to Altibase 변환가이드__7341431.md` | `arch/Home/MSSQL to ALTIBASE Conversion Guide__22643024.md` |
| `DOCK/Home/66. Altibase PHP 연동가이드__7341461.md` | `arch/Home/PHP Integration Guide for Altibase__14647305.md` |
| `DOCK/Home/67. Altibase 도커 가이드__14057660.md` | `arch/Home/Altibase Docker Guide__14647741.md` |
| `DOCK/Home/68. Altibase GeoServer 연동가이드__14058194.md` | `arch/Home/Altibase GeoServer Integration Guide__22643004.md` |
| `DOCK/Home/69. Altibase를 위한 SQuirrel SQL Client Quick 가이드__12255259.md` | `arch/Home/SQuirrel SQL Client Quick Guide for Altibase__14647622.md` |
| `DOCK/Home/70. Migration Center 사용자 가이드__19955861.md` | `arch/Home/Migration Center User Guide__19955861.md` |

## FAQ Category Mapping

All 12 Korean FAQ categories have a corresponding English core category under `FAQE/Home`. Recursive Markdown counts match by category.

| Korean category | Count | English category | Count | Result |
| --- | ---: | --- | ---: | --- |
| `faq/Home/01. 설치, 패치, 업그레이드` | 4 | `FAQE/Home/01. Installation, Patch, Upgrade` | 4 | Matches |
| `faq/Home/02. 운영 및 관리` | 28 | `FAQE/Home/02. Operation and Management` | 28 | Matches |
| `faq/Home/03. 이중화` | 8 | `FAQE/Home/03. Replication` | 8 | Matches |
| `faq/Home/04. 백업 및 복구` | 7 | `FAQE/Home/04. Backup and Recovery` | 7 | Matches |
| `faq/Home/05. SQL` | 2 | `FAQE/Home/05. SQL` | 2 | Matches |
| `faq/Home/06. Stored Procedures` | 2 | `FAQE/Home/06. Stored Procedure` | 2 | Matches |
| `faq/Home/07. 개발 및 API` | 9 | `FAQE/Home/07. Development and API` | 9 | Matches |
| `faq/Home/08. 모니터링` | 19 | `FAQE/Home/08. Monitoring` | 19 | Matches |
| `faq/Home/09. 에러메시지` | 29 | `FAQE/Home/09. Error Messages` | 29 | Matches |
| `faq/Home/11. 유틸리티` | 2 | `FAQE/Home/11. Utilities` | 2 | Matches |
| `faq/Home/12. 기타` | 2 | `FAQE/Home/12. Others` | 2 | Matches |
| `faq/Home/13. 일반` | 3 | `FAQE/Home/13. General` | 3 | Matches |

English-only FAQE extras under `ALTIBASE HDB Administration`, `ALTIBASE HDB Architecture`, `ALTIBASE HDB Performance Tuning`, `ALTIBASE HDB Replication`, `ALTIBASE HDB Troubleshooting`, and `Altibase Error Messages` remain outside the Korean-source core coverage count.

## Attachment Inventory

The attachment check covered URL-backed document-format links with extensions `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, and `.zip`.

| Source set | URL-backed attachment links | Source files containing links | English coverage result |
| --- | ---: | ---: | --- |
| Korean technical docs, `docs.altibase.com/download/attachments` | 41 | 32 | Missing 0 |
| Korean technical docs, GeoServer SourceForge importer ZIP | 1 | 1 | Missing 0 |
| Korean FAQ docs, `docs.altibase.com/download/attachments` | 7 | 6 | Missing 0 |

The check found six legacy Korean technical attachment labels whose Markdown URL is `#`, so there is no source URL to preserve:

- `DOCK/Home/36. Altibase 개발가이드__7341274.md`: `ALTIBASE_개발가이드.pdf`, `ALTIBASE_개발가이드_5.3.pdf`
- `DOCK/Home/40. Oracle to Altibase 변환가이드__7341605.md`: `ALTIBASE_Oracle_변환_가이드.pdf`, `ORACLE_to_ALTIBASE_변환_가이드_5.5.pdf`
- `DOCK/Home/44. APRE_C_C++ New Features & 업그레이드 가이드__13435760.md`: `APRE_New_Features_업그레이드_가이드.pdf`
- `DOCK/Home/65. MSSQL to Altibase 변환가이드__7341431.md`: `ALTIBASE_MSSQL_변환가이드.pdf`

These placeholder labels are not counted as missing URL-backed attachments. Later content-review jobs should keep their context in mind, but there is no actual URL in the Korean source for an English document to preserve.

## Baseline Result

- Technical mapping: 51 / 51 Korean technical documents have English targets.
- FAQ category mapping: 12 / 12 Korean FAQ categories have English core category targets.
- FAQ core document counts: 115 Korean FAQ documents and 115 English core FAQ documents across matching categories.
- URL-backed attachment coverage: 49 / 49 Korean links are present in the mapped English target content.
- Korean source documents were not deleted or modified.
- English target documents were not modified in J001.

## Validation Evidence

The following checks passed for J001:

- `python3 -m json.tool manifest.json`
- `git diff --check`
- `find DOCK -type f -name '*.md' | wc -l`: 51
- `find faq -type f -name '*.md' | wc -l`: 115
- `find arch -type f -name '*.md' | wc -l`: 181
- `find FAQE -type f -name '*.md' | wc -l`: 241
- `find DOCK/Home -type f -name '*.md' | wc -l`: 51
- `find arch/Home -type f -name '*.md' | wc -l`: 181
- `find faq/Home -type f -name '*.md' | wc -l`: 115
- `find FAQE/Home -type f -name '*.md' | wc -l`: 241
- `bash -n .codex-jobs/ko-en-doc-coverage/run_all.sh`
- `bash -n .codex-jobs/ko-en-doc-coverage/run-all.sh`
- Note-driven mapping and attachment validation: 51 technical mappings, 12 FAQ category mappings, 49 URL-backed attachment links, missing 0.

## Remaining Risk

J001 confirms inventory and mapping only. It does not prove sentence-level content equivalence. Jobs J002 through J012 still need to compare Korean source content against English targets by scope, including split English parent/child page sets, commands, SQL, settings, version statements, warnings, and notes.
