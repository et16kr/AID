# 한국어-영어 문서 재검토 보고서

검토일: 2026-05-15

작업공간: `/home/et16/AID`

## 요약

한국어 문서를 기준으로 영어 문서를 다시 비교했습니다. 담당자가 오류를 발견한 뒤 한국어 문서만 수정하고 영어 문서는 갱신하지 않았을 가능성을 전제로, 기술 문서 매핑, FAQ 핵심 문서 대응, 문서형 첨부파일, 최근에 차이가 있었던 고위험 항목을 재점검했습니다.

이전 재검토에서는 실제 차이 2건을 발견하여 영어 문서에 반영했습니다.

- 한국어 원문: `DOCK/Home/36. Altibase 개발가이드__7341274.md`
- 영어 갱신 대상: `arch/Home/Altibase Development Guide/1. Considerations when Designing__22642998.md`
- 반영 내용:
  - `Hybrid Partitioned Table (HPT)`를 사용하여 하나의 논리 테이블을 메모리 파티션과 디스크 파티션으로 구성할 수 있다는 설명을 추가했습니다.
  - 파티션 테이블 제한 설명의 기준 버전을 `6.3.1`에서 한국어 원문 기준인 `7.3.0`으로 갱신했습니다.
  - 파티션 키 없이 전체 파티션 테이블을 조회할 때 성능 저하가 발생할 수 있다는 설명을 한국어 원문 기준으로 정리했습니다.
- 한국어 원문: `DOCK/Home/68. Altibase GeoServer 연동가이드__14058194.md`
- 영어 갱신 대상: `arch/Home/Altibase GeoServer Integration Guide__22643004.md`
- 반영 내용:
  - 공간정보 Import 절의 GeoServer importer plug-in ZIP 다운로드 링크를 영어 문서에 보존했습니다.
  - 해당 절의 문장을 자연스러운 기술 영어로 정리하고 Windows 경로를 코드 표기로 명확히 했습니다.

이 반영 후, J002부터 J009까지 범위별 본문과 첨부 링크를 갱신했습니다. J010에서는 문서형 첨부와 중요 출처 링크를 전체 범위에서 다시 대조하여 영어 문서의 누락되거나 깨진 참조 링크를 보정했습니다. 한국어 문서는 삭제하지 않았습니다.

## J002 설치 및 플랫폼 설정 문서 추가 검토

J002에서는 한국어 `DOCK`의 설치, 플랫폼 설정, 데이터베이스 생성, 빠른 시작, 설치 문제 해결, Linux/Unix 설정 문서를 영어 `arch` 문서와 재비교했습니다. 한국어 원문을 기준으로 본문 절, 명령어, SQL 예제, 설정값, 주의사항, 첨부 문서 링크, 외부 참조 링크를 확인했습니다.

비교 및 갱신 범위는 다음과 같습니다.

| 한국어 기준 | 영어 갱신 문서 |
| --- | --- |
| `DOCK/Home/20. Altibase 설정 파일 가이드__13437165.md` | `arch/Home/Altibase Configuration File Guide__22642991.md` |
| `DOCK/Home/21. Altibase 디스크I_O 병목을 고려한 볼륨구성 가이드__11698408.md` | `arch/Home/Configuration Guide For Minimizing Disk I_O Contention__22643018.md` |
| `DOCK/Home/22. Altibase 운영을 위한 Solaris 설정 가이드__11698415.md` | `arch/Home/Solaris Setup Guide for Altibase/*` |
| `DOCK/Home/23. Altibase 운영을 위한 HPUX 설정 가이드__14057733.md` | `arch/Home/HPUX Setup Guide for Altibase__14058288.md` |
| `DOCK/Home/24. Altibase 운영을 위한 AIX 설정 가이드__13436846.md` | `arch/Home/AIX Setup Guide for Altibase__14058298.md` |
| `DOCK/Home/25. Altibase 데이터베이스 생성 가이드__13436812.md` | `arch/Home/Creating ALTIBASE Database__22643020.md` |
| `DOCK/Home/31. Altibase 설치가이드__11698403.md` | `arch/Home/Altibase Installation Guide/*` |
| `DOCK/Home/41. Altibase Quick Install & Start for UNIX__13436834.md` | `arch/Home/Altibase Quick Install & Start for UNIX__16875604.md` |
| `DOCK/Home/42. Altibase 설치 시 발생할 수 있는 문제상황과 조치__13437056.md` | `arch/Home/Troubleshooting Altibase Installation Problems__15138879.md` |
| `DOCK/Home/57. Altibase 운영을 위한 Linux 설정 가이드__13436485.md` | `arch/Home/Linux Setup Guide for Altibase__22643022.md` |

주요 반영 내용은 다음과 같습니다.

- 설정 파일 가이드의 기본값, 버전 기준, 변경 불가 속성, `DIRECT_IO_ENABLED`, `REPLICATION_PORT_NO`, `MEM_DB_DIR`, `DEFAULT_DISK_DB_DIR`, 관련 한국어 원문 링크를 보정했습니다.
- 디스크 I/O 가이드의 그림 링크, 예제 조건, Direct I/O 그림 참조, 파일시스템 표기를 한국어 원문 기준으로 정리했습니다.
- Solaris, HPUX, AIX 설정 가이드의 커널 파라미터 값, 사용자 제한 설명, 환경변수 설명, 오탈자 및 깨진 문장을 수정했습니다.
- 데이터베이스 생성 가이드의 `UTF8` 생성 예제, `isql -sysdba` 명령 블록, 구버전 첨부 가이드 설명을 보정했습니다.
- 설치 가이드의 APatch 디렉터리 예제, 지원 OS 표, 라이선스 안내, post-install 절차, `Noarchivelog`/`Archivelog` 표기, 경로 예제를 보정했습니다.
- Quick Install & Start, 설치 문제 해결 문서의 명령 출력 블록, 기본 패스워드 표기, 시작/종료 참조 링크, 설치 문제 해결 버전 범위와 속성 파일명을 수정했습니다.
- Linux 설정 가이드의 손상된 TOC와 한국어 잔여 문구를 제거하고, `swappiness`, THP, semaphore, locale, 요약 표, Red Hat swap 링크, Symantec SEP 주의사항, `References` 절을 한국어 원문 기준으로 갱신했습니다.
- J002 한국어 원문 문서의 문서형 첨부 URL이 대응 영어 문서에 보존되어 있는지 확인했고 누락은 없었습니다.

## J003 운영 및 관리 문서 추가 검토

J003에서는 한국어 `DOCK`의 설정, 장애 대응, 시작/종료, 시스템 리소스 용량 산정, 문제 분석용 OS 유틸리티, UNIX 메모리 관리, 모니터링 쿼리, CPU 과부하 분석, 메모리 사용량 증가 분석 문서를 영어 `arch` 문서와 재비교했습니다. 한국어 원문을 기준으로 본문 절, 명령어, SQL, 설정값, 주의사항, 첨부 문서 링크를 확인했습니다.

비교 및 갱신 범위는 다음과 같습니다.

| 한국어 기준 | 영어 갱신 문서 |
| --- | --- |
| `DOCK/Home/20. Altibase 설정 파일 가이드__13437165.md` | `arch/Home/Altibase Configuration File Guide__22642991.md` |
| `DOCK/Home/26. Altibase 기본적인 장애대응 절차__13435879.md` | `arch/Home/Responding to Failures Guide for Altibase/*` |
| `DOCK/Home/43. Altibase STARTUP _ STOP 과정의 이해__13434993.md` | `arch/Home/Understanding the Altibase Start_Shut down Process/*` |
| `DOCK/Home/45. Altibase 운영을 위한 시스템 리소스 용량산정 가이드__14057887.md` | `arch/Home/System Data Capacity Estimation Guide for Altibase Operations__22643042.md` |
| `DOCK/Home/47. 문제분석을 위한 OS별 유틸리티 사용 가이드__13436866.md` | `arch/Home/Utility Guide for each OS for Problem Analysis__16875587.md` |
| `DOCK/Home/48. UNIX Memory Management__13436842.md` | `arch/Home/UNIX Memory Management__16875572.md` |
| `DOCK/Home/59. Altibase 모니터링 쿼리 가이드__10060431.md` | `arch/Home/Altibase Monitoring Queries Guide/*` |
| `DOCK/Home/62. Altibase CPU 과부하 현상에 대한 분석가이드__11698396.md` | `arch/Home/Altibase CPU Overload Analysis Guide/*` |
| `DOCK/Home/63. Altibase Memory 사용량 증가 분석가이드__11698518.md` | `arch/Home/Altibase Memory Usage Increase Analysis Guide/*` |

주요 반영 내용은 다음과 같습니다.

- 한국어 모니터링 쿼리 가이드의 `[ST01]`, `[TS01]`, `[OB01]`, `[RP01]` 등 쿼리 식별자를 대응 영어 분할 문서의 제목에 복원했습니다.
- 시스템 리소스 용량 산정 문서에 남아 있던 한국어 표 행과 `1000개` 표현을 제거하거나 영어로 정리했습니다.
- 장애 대응 문서에서 `ulimit -n`, `$ALTIBASE_HOME/conf/altibase.properties`, `Garbage Data`, 이중화 갭 설명, `REP_GAP` 계산 설명을 한국어 원문 의미에 맞게 보정했습니다.
- 시작/종료 문서에서 `altibase.properties`, Altibase 프로세스 중복 구동 방지, `V$OBSOLETE_BACKUP_INFO`, META 단계 설명, ABORT 설명의 오역과 오탈자를 수정했습니다.
- OS 유틸리티 문서에서 AIX `procstack` 표기와 시스템 로그 설명을 한국어 원문 의미에 맞게 수정했습니다.
- CPU 과부하 및 메모리 사용량 증가 분석 문서의 OS 환경변수 영향, 프로파일링, `Query_Binding`, GC aging, Altibase 프로세스 메모리 설명을 자연스러운 기술 영어로 정리했습니다.
- J003 한국어 원문 문서의 문서형 첨부 URL이 대응 영어 문서에 보존되어 있는지 확인했고 누락은 없었습니다.

## J004 이중화, 백업 및 복구 문서 추가 검토

J004에서는 한국어 `DOCK`의 이중화 구성, 이중화 제약사항, 백업 정책, 장애 대응, STARTUP/STOP 복구 관련 절을 영어 `arch` 문서와 재비교했습니다. 한국어 원문을 기준으로 본문 절, 명령어, SQL, 설정값, 에러 코드, 주의사항, 첨부 문서 링크를 확인했습니다.

비교 및 갱신 범위는 다음과 같습니다.

| 한국어 기준 | 영어 갱신 문서 |
| --- | --- |
| `DOCK/Home/26. Altibase 기본적인 장애대응 절차__13435879.md` | `arch/Home/Responding to Failures Guide for Altibase/*` |
| `DOCK/Home/27. Altibase 이중화 구성 가이드__13828098.md` | `arch/Home/Altibase Replication Configuration Guide__14647672.md` |
| `DOCK/Home/43. Altibase STARTUP _ STOP 과정의 이해__13434993.md` | `arch/Home/Understanding the Altibase Start_Shut down Process/*` |
| `DOCK/Home/49. Altibase 이중화 제약사항 가이드__19333729.md` | `arch/Home/Altibase Replication Constraints Guide__22643008.md` |
| `DOCK/Home/50. Altibase 백업정책 결정을 위한 고려사항__14057586.md` | `arch/Home/Considerations for Altibase Backup Policy/*` |

주요 반영 내용은 다음과 같습니다.

- 이중화 구성 가이드의 기준 버전을 한국어 원문 기준인 `Altibase 7.1.0` 이상으로 보정하고, 디스크 공유 미지원, Lazy/Eager 동작, Off-Line Replicator, HA Standby 종료 상태, N-way 이중화, `REPLICATION_MAX_LOGFILE`, 대량 변경 작업, Parallel Applier의 DML 처리 설명을 정리했습니다.
- 이중화 제약사항 가이드에서 비이중화 컬럼, 파티션드 테이블, DDL 제약 조건의 구조를 한국어 원문 의미에 맞게 정리하고, UPDATE Conflict 표에서 누락된 `ERR-61035` 메시지를 복원했습니다.
- `RP_MSGLOG_FLAG`, `$ALTIBASE_HOME/trc/altibase_rp_conflict.log`, `REPLICATION_UPDATE_REPLACE` 등 번역하면 안 되는 설정값과 경로를 코드 표기로 명확히 했습니다.
- 백업 정책 문서의 복구 시점, 복구 시간, 백업 시간, 트랜잭션 영향, 백업 종류별 비교 표를 한국어 원문 관계에 맞게 재구성하여 온라인 백업, 오프라인 백업, 논리 백업, 증분 백업의 차이가 명확히 보이도록 했습니다.
- 장애 대응 및 STARTUP/STOP 문서에서 이중화 Sender 수, `REP_GAP` 의미, 충돌 SQL 추적, 선택별 복구, `kill -9` 표기를 정리했습니다.
- J004 한국어 원문 문서의 문서형 첨부 URL이 대응 영어 문서에 보존되어 있는지 확인했고 누락은 없었습니다.

## J005 개발 및 API 연동 문서 추가 검토

J005에서는 한국어 `DOCK`의 개발자 교육, Precompiler, APRE, Java, ODBC, ADO.NET, Spring, iBATIS, MyBatis, Hibernate, PHP, WAS 연동 문서를 영어 `arch` 문서와 재비교했습니다. 한국어 원문을 기준으로 본문 절, 명령어, 코드 예제, 설정값, 오류 메시지, 주의사항, 첨부 문서 링크를 확인했습니다.

비교 및 갱신 범위는 다음과 같습니다.

| 한국어 기준 | 영어 갱신 문서 |
| --- | --- |
| `DOCK/Home/28. Altibase TOMCAT 연동가이드__7341030.md` | `arch/Home/TOMCAT Integration Guide for Altibase/*` |
| `DOCK/Home/29. Altibase JEUS 연동가이드__7341028.md` | `arch/Home/JEUS Integration Guide for Altibase/*` |
| `DOCK/Home/30. Altibase JBoss 연동가이드__13437492.md` | `arch/Home/JBOSS Integration Guide for Altibase/*` |
| `DOCK/Home/32. Altibase와 unixODBC 연동 가이드__11698379.md` | `arch/Home/Altibase and unixODBC Integration Guide/*` |
| `DOCK/Home/33. Altibase 개발자교육__19333461.md` | `arch/Home/Altibase Developer Training__22642996.md` |
| `DOCK/Home/34. Altibase Precompiler 가이드__11698385.md` | `arch/Home/Altibase Precompiler Guide/*` |
| `DOCK/Home/35. Altibase APRE(SES) _C_C++ Makefile__11698493.md` | `arch/Home/Altibase APRE(SES) _C_C++ Makefile/*` |
| `DOCK/Home/44. APRE_C_C++ New Features & 업그레이드 가이드__13435760.md` | `arch/Home/APRE_C_C++ New Features & Upgrade Guide__22643052.md` |
| `DOCK/Home/51. Altibase window ADO.NET 개발 가이드__11698513.md` | `arch/Home/Altibase Window ADO.NET Development Guide/*` |
| `DOCK/Home/52. Altibase WebSphere 연동 가이드__13435602.md` | `arch/Home/WebSphere Integration Guide for Altibase__14058343.md` |
| `DOCK/Home/53. Windows 환경의 Altibase ODBC 개발 가이드__13436856.md` | `arch/Home/Altibase ODBC Development Guide in Windows Environment__15138911.md` |
| `DOCK/Home/54. Altibase Spring 연동 가이드__7340945.md` | `arch/Home/Spring Integration Guide for Altibase/*` |
| `DOCK/Home/55. Altibase iBATIS 연동가이드__7340053.md` | `arch/Home/iBatis Integration Guide for Altibase/*` |
| `DOCK/Home/56. JAVA 개발 가이드__14057500.md` | `arch/Home/JAVA Developer's Guide__16875544.md` |
| `DOCK/Home/58. Altibase Hibernate 연동가이드__14057878.md` | `arch/Home/Hibernate Integration Guide for Altibase__14058388.md` |
| `DOCK/Home/60. Altibase WebLogic 연동가이드__7340101.md` | `arch/Home/WEBLOGIC Integration Guide for Altibase/*` |
| `DOCK/Home/64. Altibase MyBatis 연동 가이드__7340818.md` | `arch/Home/MyBatis Integration Guide for Altibase/*` |
| `DOCK/Home/66. Altibase PHP 연동가이드__7341461.md` | `arch/Home/PHP Integration Guide for Altibase/*` |

주요 반영 내용은 다음과 같습니다.

- APRE New Features 문서에서 이미지로만 남아 있던 `-I`, `-D`, `-keyword`, `-parse`, `ERR-302L` 예제를 텍스트와 코드 블록으로 복원하고 `APRE*C/C++`, `$ALTIBASE_HOME` 표기를 보정했습니다.
- ADO.NET 개발 가이드의 C# 예제를 fenced code block으로 정리하고 `AltibaseDataAdapter`, `AltibaseTransaction`, `Altibase ADO.NET` 표기를 보정했습니다.
- MyBatis 연동 문서의 한국어 주석, 표 헤더, 예제 설명, 깨진 `Altibase` 주석을 영어로 정리하고 `jdbc:Altibase://IP:port_no/db_name` URL 형식을 코드 표기로 명확히 했습니다.
- JBoss, Java, WebLogic, TOMCAT, PHP, Precompiler, APRE Makefile 문서에 남아 있던 한국어 잔여 문구와 오탈자를 영어 기술 문서 표현으로 정리했습니다.
- J005 한국어 원문 문서의 문서형 첨부 URL이 대응 영어 문서에 보존되어 있는지 확인했고 누락은 없었습니다.

## J006 SQL, 튜닝, 마이그레이션, 변환 및 도구 문서 추가 검토

J006에서는 한국어 `DOCK`의 Altibase 개발가이드, SQL 튜닝, Oracle/MSSQL 변환, Altibase 버전 간 마이그레이션, Docker, GeoServer, SQuirrel SQL Client, VC 2008/2010, Migration Center 문서를 영어 `arch` 문서와 재비교했습니다. 한국어 원문을 기준으로 본문 절, 명령어, SQL, 설정값, 주의사항, 첨부 문서 링크를 확인했습니다.

비교 및 갱신 범위는 다음과 같습니다.

| 한국어 기준 | 영어 갱신 문서 |
| --- | --- |
| `DOCK/Home/36. Altibase 개발가이드__7341274.md` | `arch/Home/Altibase Development Guide/*` |
| `DOCK/Home/37. Altibase SQL 튜닝 가이드__19333563.md` | `arch/Home/Altibase SQL Tuning Guide__22643010.md` |
| `DOCK/Home/38. Altibase VC 2008 개발가이드__19333567.md` | `arch/Home/Altibase VC 2008 Development Guide__19333567.md` |
| `DOCK/Home/39. Altibase, Oracle 비교 자료__14058137.md` | `arch/Home/Altibase_Oracle Comparison__16875638.md` |
| `DOCK/Home/40. Oracle to Altibase 변환가이드__7341605.md` | `arch/Home/ORACLE to ALTIBASE Conversion Guide__22643038.md` |
| `DOCK/Home/46. Altibase 버전 간 마이그레이션 가이드__19333688.md` | `arch/Home/Altibase Data Migration Process Guide__22642994.md` |
| `DOCK/Home/61. Altibase VC 2010 개발가이드__19334121.md` | `arch/Home/Altibase VC 2010 Development Guide__19334121.md` |
| `DOCK/Home/65. MSSQL to Altibase 변환가이드__7341431.md` | `arch/Home/MSSQL to ALTIBASE Conversion Guide__22643024.md` |
| `DOCK/Home/67. Altibase 도커 가이드__14057660.md` | `arch/Home/Altibase Docker Guide/*` |
| `DOCK/Home/68. Altibase GeoServer 연동가이드__14058194.md` | `arch/Home/Altibase GeoServer Integration Guide__22643004.md` |
| `DOCK/Home/69. Altibase를 위한 SQuirrel SQL Client Quick 가이드__12255259.md` | `arch/Home/SQuirrel SQL Client Quick Guide for Altibase/*` |
| `DOCK/Home/70. Migration Center 사용자 가이드__19955861.md` | `arch/Home/Migration Center User Guide__19955861.md` |

주요 반영 내용은 다음과 같습니다.

- Oracle 변환 가이드에서 한국어가 남아 있던 Overview, 표 헤더, `COLUMN DEFINITION` 절, `WHERE CURRENT OF` 예제 주석, 검증 표를 영어로 정리하고, `PROCEDURE/FUNCTION` 데이터 타입 최대 크기 표를 한국어 원문 의미에 맞게 복원했습니다.
- Oracle 변환 가이드의 MigrationCenter 다운로드 안내, support portal 링크, Migration Center manual 링크를 한국어 원문 기준으로 영어 문서에 반영했습니다.
- 개발가이드와 Oracle/MSSQL 변환 가이드의 구버전 PDF placeholder는 한국어 원문에 실제 다운로드 URL이 없으므로, 영어 문서에 "downloadable URL 없는 legacy document placeholder"로 기록했습니다.
- Altibase 버전 간 마이그레이션 문서의 캐릭터셋 확인 문구, `...중략...`, `합계`, `.fmt`/`.dat` 파일 수 확인 주석, `iloader` 성능 옵션 주석에 남아 있던 한국어를 영어로 정리했습니다.
- Docker 문서에서 `docker build`, `docker run`, `docker network`, `docker ps`, `isql` 명령과 출력이 한 줄로 붙어 있던 부분을 한국어 원문 구조에 맞게 분리하고, 중복된 이중화 추가 노드 절을 제거했습니다.
- GeoServer 문서의 레이어 미리보기 절, SQuirrel 문서의 JDBC driver registration 제목 및 tab 설명, Development Guide trace/error 절의 한국어 잔여 문구를 영어로 정리했습니다.
- J006 한국어 원문 문서의 URL-backed 문서형 첨부 URL 6개가 대응 영어 문서에 보존되어 있는지 확인했고 누락은 없었습니다.

## J007 FAQ 설치, 운영 및 관리 문서 추가 검토

J007에서는 한국어 `faq`의 `01. 설치, 패치, 업그레이드` 4개 문서와 `02. 운영 및 관리` 28개 문서를 영어 `FAQE`의 대응 핵심 카테고리 문서와 재비교했습니다. 한국어 원문을 기준으로 본문 절, 명령어, SQL, 설정값, 운영 절차, 주의사항, 문서형 첨부 링크를 확인했습니다.

비교 및 갱신 범위는 다음과 같습니다.

| 한국어 기준 | 영어 갱신 문서 |
| --- | --- |
| `faq/Home/01. 설치, 패치, 업그레이드/*` | `FAQE/Home/01. Installation, Patch, Upgrade/*` |
| `faq/Home/02. 운영 및 관리/*` | `FAQE/Home/02. Operation and Management/*` |

주요 반영 내용은 다음과 같습니다.

- Linux 자동 시작 FAQ에서 Red Hat 계열 v6 이하용 `altibased` 스크립트 본문과 `chkconfig` 등록 절차를 한국어 원문 기준으로 영어 문서에 복원했습니다.
- Solaris/HP-UX 자동 시작 FAQ의 깨진 표 내보내기 형태, `Unknown macro`, 잘못된 `PATH` 링크를 검색 가능한 쉘 코드 블록으로 정리했습니다.
- `MEM_MAX_DB_SIZE` FAQ에 대상 버전, 재구동 필요 조건, 체크포인트 이미지 파일 크기 관련 startup 오류와 조치, 관련 링크를 한국어 원문 기준으로 추가했습니다.
- `TRANSACTION_TABLE_SIZE` FAQ에 오프라인 변경 가능 버전의 의미, `V$MEMSTAT` 메모리 사용량 상세 표, `BUG-31862` 참고 링크를 반영했습니다.
- IPC 설정, 로그앵커/온라인 로그/아카이브 로그/Double Write 파일 경로 변경, 테이블스페이스 데이터 파일 경로 변경 문서의 SQL, 프로퍼티명, 주석, 표 헤더, 운영 절차 설명을 한국어 원문 의미에 맞게 보정했습니다.
- `JOB` 객체 생성 FAQ에 JOB interval이 프로시저 수행 시간보다 길어야 한다는 주의사항을 복원하고, 깨진 매뉴얼 링크를 정리했습니다.
- 보안 점검, 컬럼 변경, SYS 패스워드 변경, OS/DB 시간 불일치, 클라이언트 설치 FAQ의 한국어 잔여 문구, 오탈자, 잘못된 링크를 영어 기술 문서 표현으로 정리했습니다.
- J007 한국어 원문 범위의 URL-backed 문서형 첨부 URL은 0개였고, 대응 영어 문서에서 문서형 첨부 누락은 없었습니다.

## J008 FAQ 이중화, 백업, SQL, Stored Procedures 및 개발/API 문서 추가 검토

J008에서는 한국어 `faq`의 `03. 이중화` 8개 문서, `04. 백업 및 복구` 7개 문서, `05. SQL` 2개 문서, `06. Stored Procedures` 2개 문서, `07. 개발 및 API` 9개 문서를 영어 `FAQE`의 대응 핵심 카테고리 문서와 재비교했습니다. 한국어 원문을 기준으로 본문 절, 명령어, SQL, 설정값, 에러 코드, JDBC/ODBC/PHP 예제, 주의사항, 문서형 첨부 링크를 확인했습니다.

비교 및 갱신 범위는 다음과 같습니다.

| 한국어 기준 | 영어 갱신 문서 |
| --- | --- |
| `faq/Home/03. 이중화/*` | `FAQE/Home/03. Replication/*` |
| `faq/Home/04. 백업 및 복구/*` | `FAQE/Home/04. Backup and Recovery/*` |
| `faq/Home/05. SQL/*` | `FAQE/Home/05. SQL/*` |
| `faq/Home/06. Stored Procedures/*` | `FAQE/Home/06. Stored Procedure/*` |
| `faq/Home/07. 개발 및 API/*` | `FAQE/Home/07. Development and API/*` |

주요 반영 내용은 다음과 같습니다.

- 이중화 대상 테이블 추가/삭제 FAQ에서 누락되어 있던 `ALTER REPLICATION replication_name ADD TABLE FROM user_name.table_name TO user_name.table_name;` 구문을 복원하고, 삭제 구문의 `DROP TABLE FROM ... TO ...` 형식을 한국어 원문 기준으로 수정했습니다.
- 이중화 모니터링 FAQ의 `NET_ERROR_FLAG`, `XSN`, Altibase 7 미만 `REP_GAP` 설명과 Altibase 7 이상 `rep_name` 설명에 남아 있던 한국어 문장을 영어로 정리했습니다.
- 이중화 GIVE-UP FAQ의 `REPLICATION_MAX_LOGFILE` 설명, `GIVE_UP_TIME` 확인 표, 이중화 객체 생성/삭제 FAQ의 포트 `LISTEN` 확인 주의사항과 에러 메시지 조치 설명을 한국어 원문 의미에 맞게 보정했습니다.
- `aexport`/`iloader`, Cold Backup, Online Backup, Time Based Recovery FAQ의 환경변수, 로그 확인 명령, `run_il_in.sh`, `RESETLOGS`, `LOGANCHOR_DIR`, 작은따옴표 등 명령/예제 표기를 검색 가능한 영어 문장과 코드로 정리했습니다.
- Stored Procedure FAQ의 `SP_DML_RECORD_COUNT.txt` 첨부 링크를 보존하고, `SYSTEM_.SYS_PROCEDURES_`, `SYSTEM_.SYS_PROC_PARSE_`, `aexport -object user_name.procedure_name` 관련 설명의 한국어 잔여 문구를 제거했습니다.
- JDBC Fail-Over FAQ에서 한국어 원문에 있는 CTF/STF 성공 여부 확인 기준(`08F01`, `ES_08FO01`)을 복원하고, 한 줄로 뭉개진 Java 샘플을 코드 블록으로 정리했습니다.
- ODBC/PHP 개발 FAQ에서 `SELECT DB_NAME FROM V$DATABASE`, `SELECT NLS_CHARACTERSET FROM V$NLS_PARAMETERS`, `SQLFreeStmt`, `ALTIBASE_JDBC_TRCLOG_DISABLE`, unixODBC 라이브러리 경로, PHP `odbc.ini` 예제를 한국어 원문 의미에 맞게 보정했습니다.
- J008 한국어 원문 범위의 URL-backed 문서형 첨부 3개(PDF 2개, ZIP 1개)가 대응 영어 문서에 보존되어 있음을 확인했고, Stored Procedure 예제 텍스트 첨부 1개도 영어 문서에 링크로 보존했습니다.

## J009 FAQ 모니터링, 에러 메시지, 유틸리티, 기타 및 일반 문서 추가 검토

J009에서는 한국어 `faq`의 `08. 모니터링` 19개 문서, `09. 에러메시지` 29개 문서, `11. 유틸리티` 2개 문서, `12. 기타` 2개 문서, `13. 일반` 3개 문서를 영어 `FAQE`의 대응 핵심 카테고리 문서와 재비교했습니다. 한국어 원문을 기준으로 본문 절, 명령어, SQL, 설정값, 에러 코드, 운영 예제, 첨부 문서 링크를 확인했습니다.

비교 및 갱신 범위는 다음과 같습니다.

| 한국어 기준 | 영어 갱신 문서 |
| --- | --- |
| `faq/Home/08. 모니터링/*` | `FAQE/Home/08. Monitoring/*` |
| `faq/Home/09. 에러메시지/*` | `FAQE/Home/09. Error Messages/*` |
| `faq/Home/11. 유틸리티/*` | `FAQE/Home/11. Utilities/*` |
| `faq/Home/12. 기타/*` | `FAQE/Home/12. Others/*` |
| `faq/Home/13. 일반/*` | `FAQE/Home/13. General/*` |

주요 반영 내용은 다음과 같습니다.

- `altiProfile`, 디스크 테이블스페이스, 언두 테이블스페이스 FAQ에 남아 있던 한국어 SQL 주석, `예제`, `단위: 초`, `Bind 변수 값` 등 잔여 문구를 검색 가능한 영어로 정리했습니다.
- 디스크 테이블 및 인덱스 사용량 FAQ에서 Confluence export 오류로 남아 있던 `Error rendering macro 'code'` 문구를 제거하고, 한국어 원문 기준의 `Disk table count query` 제목을 복원했습니다.
- `[Notify : Fetch Timeout]`, `ERR-4103C`, `ERR-410D2`, `ERR-11075`, `ERR-21010`, `ERR-91015` 등 에러 FAQ의 한국어 잔여 문구, 커서 의사코드, 버전별 참조 링크, 매뉴얼 링크를 영어 문서 기준으로 보정했습니다.
- `ALTIMON_USER_GUIDE.pdf`, `altimon_for_windows.zip`, `AdminCenter2.zip`, HP-UX 설정 가이드 PDF 등 J009 범위의 URL-backed 문서형 첨부 4개가 대응 영어 문서에 보존되어 있음을 확인했습니다.
- 대용량 DRDB Index 구축 FAQ에서 `BUFFER_AREA_SIZE`, `SORT_AREA_SIZE`, `DISK_INDEX_BUILD_SORT_AREA_SIZE`, `DISK_INDEX_BUILD_MERGE_PAGE_COUNT`, `INDEX_BUILD_THREAD_COUNT` 설명을 한국어 원문 의미에 맞게 정리하고 버전 `6.5.1~7.1.0`, `7.3.0 or later` 기준을 명확히 했습니다.
- 일반 FAQ에서 Altibase 제공 인터페이스 표, In-Memory DBMS와 Disk-based DBMS 차이, WAL 및 장애 관리 설명을 자연스러운 영어 기술 문장으로 정리했습니다.

## J010 문서형 첨부 및 출처 링크 전체 대조

J010에서는 전체 한국어 기술 문서와 FAQ의 문서형 첨부 링크 및 중요 출처 링크를 영어 대응 문서와 다시 대조했습니다. 대상 확장자는 `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.zip`이며, GeoServer importer plug-in처럼 URL 경로에 `.zip/download`가 포함된 외부 ZIP도 문서형 출처 링크로 함께 확인했습니다.

주요 반영 내용은 다음과 같습니다.

- 한국어 기술 문서의 URL-backed 문서형 링크 42개(문서 첨부 41개와 GeoServer importer ZIP 1개)와 한국어 FAQ의 URL-backed 문서형 첨부 7개가 영어 대응 문서에 보존되어 있음을 확인했습니다.
- GeoServer 연동 가이드에서 한국어 원문에 있던 OpenJDK, Oracle JRE, GeoServer download, Altibase spatial driver, JTS, `altibase_spatial_ref_sys.sql`, OGC, OSGeo 출처 링크를 영어 문서에 복원했습니다.
- WebSphere 연동 가이드의 IBM Installation Manager 다운로드 URL이 공백으로 깨져 있던 문제를 한국어 원문 URL 기준으로 보정했습니다.
- APRE Makefile, Windows ODBC, 장애 대응 참고 문서, 이중화 DDL FAQ, Oracle 변환, Migration Center 문서의 영어 지원/매뉴얼/제품 다운로드 링크를 보정했습니다.
- APRE Makefile 문서에는 한국어 원문에 있는 64-bit client development tool 다운로드 안내를 영어로 추가했습니다.

검토 중 한국어 GeoServer 문서의 `GeoServer Documentation` 링크가 Red Hat Enterprise Linux CPU governor 페이지를 가리키는 것을 확인했습니다. 이 링크는 라벨과 URL이 일치하지 않아 영어 문서에는 전파하지 않았고, 수동 검토 리스크로 남겼습니다.

## 검토 범위

| 구분 | 한국어 기준 문서 | 영어 대상 문서 | 결과 |
| --- | ---: | ---: | --- |
| 기술 문서 | `DOCK/Home`: 51개 Markdown | `arch/Home`: 181개 Markdown, 그중 한국어 대응 상위 문서 51개 | 51개 모두 영어 대응 문서 확인 |
| FAQ 핵심 문서 | `faq/Home`: 115개 Markdown | `FAQE/Home`: 한국어 FAQ에 대응하는 핵심 문서 115개 | 115개 모두 영어 대응 문서 확인 |
| 문서형 첨부파일 및 외부 ZIP 출처 | 한국어 기술 문서 URL-backed 링크 42개, 한국어 FAQ URL-backed 링크 7개 | 대응 영어 문서 | 누락 0개 |

## 검토 방법

- `DOCK/Home`의 한국어 기술 문서 51개를 `arch/Home`의 영어 문서와 다시 매핑했습니다.
- 영어 기술 문서가 하위 문서로 분리된 경우, 상위 문서와 하위 문서 내용을 함께 묶어 한국어 원문과 비교했습니다.
- `faq/Home`의 한국어 FAQ 115개를 `FAQE/Home`의 대응 핵심 카테고리 115개와 다시 비교했습니다.
- `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.zip` 형식의 한국어 원문 첨부파일 링크가 대응 영어 문서에 보존되어 있는지 확인했습니다.
- 이전 검토에서 차이가 있었던 항목과 오류 가능성이 높은 항목을 별도로 확인했습니다.
  - HPT 및 파티션 테이블 버전 기준
  - Linux 자동 시작 및 SELinux 안내
  - PUBLIC SYNONYM 보안 점검 항목
  - ALTIMON 설정 및 `TIMED_STATISTICS` 안내
  - 한국어 원문 첨부파일 링크 보존 여부

## 이번 검토에서 갱신한 문서

| 한국어 기준 | 영어 갱신 문서 | 조치 |
| --- | --- | --- |
| `DOCK/Home/36. Altibase 개발가이드__7341274.md` | `arch/Home/Altibase Development Guide/1. Considerations when Designing__22642998.md` | HPT 설명 추가, 파티션 테이블 기준 버전 `7.3.0`으로 갱신 |
| `DOCK/Home/68. Altibase GeoServer 연동가이드__14058194.md` | `arch/Home/Altibase GeoServer Integration Guide__22643004.md` | importer plug-in ZIP 다운로드 링크 보존 및 문장 정리 |

변경된 영어 문서의 메타데이터를 맞추기 위해 `manifest.json`의 해당 문서 `body_chars`, `word_count`도 갱신했습니다.

## 재검토 결과

| 점검 항목 | 결과 |
| --- | ---: |
| 한국어 기술 문서의 영어 대응 문서 | 51 / 51 |
| 누락된 기술 문서 대응 경로 | 0 |
| 한국어 FAQ 핵심 문서의 영어 대응 문서 | 115 / 115 |
| FAQ 카테고리별 문서 수 불일치 | 0 |
| 한국어 기술 문서의 URL-backed 문서형 링크 | 42 |
| 영어 기술 문서에서 누락된 한국어 첨부파일 | 0 |
| 한국어 FAQ의 문서형 첨부파일 | 7 |
| 영어 FAQ에서 누락된 한국어 첨부파일 | 0 |
| 고위험 항목 표본 점검 | 5 / 5 통과 |

## 이전 반영 사항 유지 확인

이전 검토에서 영어 문서에 추가하거나 정리했던 다음 항목도 유지되어 있음을 확인했습니다.

- 한국어에만 있던 기술 문서의 영어 문서 생성:
  - `Altibase VC 2008 Development Guide`
  - `Altibase VC 2010 Development Guide`
  - `Migration Center User Guide`
- 한국어 원문의 PDF/PPTX/ZIP 등 문서형 첨부파일 링크가 대응 영어 문서에 보존됨
- FAQ 갱신 항목 유지:
  - Red Hat 계열 v7 이상 Linux 자동 시작, `systemd`, SELinux 안내
  - ALTIMON 사용자 가이드, 설정 파일 복사, `TIMED_STATISTICS` 요구사항
  - PUBLIC SYNONYM 관련 보안 점검과 PRIVATE SYNONYM 안내
  - 사용자 패스워드 길이 제약의 `16byte` 기준
  - 인터페이스 지원 버전 및 SQL 튜닝 지원 안내
  - Spring+iBatis `TypeHandler` 설명과 샘플 첨부파일 링크

## 검증

| 검증 항목 | 결과 |
| --- | --- |
| `python3 -m json.tool manifest.json` | 통과 |
| `git diff --check` | 통과 |
| Markdown 문서 수 | `DOCK/Home` 51개, `arch/Home` 181개, `faq/Home` 115개, `FAQE/Home` 241개 |
| 문서형 첨부 URL 추가 대조 | GeoServer importer plug-in ZIP 링크 보존 후 통과 |
| J002 문서형 첨부 URL 대조 | 설치/플랫폼 범위 10개 URL 확인, 누락 0개 |
| J002 갱신 문서 stale-string grep | 알려진 오탈자, 깨진 명령어, 오래된 링크 패턴 재검출 0건 |
| J002 manifest 메타데이터 대조 | 갱신된 `arch` 문서 14개 확인, 불일치 0건 |
| J003 문서형 첨부 URL 대조 | 운영/관리 범위 9개 문서형 URL 확인, 누락 0개 |
| J003 모니터링 쿼리 ID 대조 | `SS`, `ST`, `SV`, `TL`, `LO`, `GC`, `MS`, `TS`, `DB`, `OB`, `PV`, `CT`, `RP` 계열 72개 제목 ID 확인, 누락 0개 |
| J003 갱신 문서 stale-string grep | 한국어 잔여 문구, 알려진 오탈자, 잘못된 명령/경로 패턴 재검출 0건 |
| J003 manifest 메타데이터 대조 | 갱신된 `arch` 문서 확인, 불일치 0건 |
| J004 문서형 첨부 URL 대조 | 이중화/백업/복구 범위 3개 문서형 URL 확인, 누락 0개 |
| J004 이중화/백업 핵심 항목 grep | `Altibase 7.1.0`, `ERR-61035`, `RP_MSGLOG_FLAG`, `REP_GAP`, `Page Change Tracking`, `kill -9` 확인 |
| J004 갱신 문서 stale-string grep | 알려진 오탈자, 누락 에러 메시지, 잘못된 복구/백업 표 헤더 패턴 재검출 0건 |
| J004 manifest 메타데이터 대조 | 갱신된 `arch` 문서 확인, 불일치 0건 |
| J005 문서형 첨부 URL 대조 | 개발/API 연동 범위 17개 문서형 URL 확인, 누락 0개 |
| J005 개발/API 핵심 항목 grep | `apre -DALTIBASE`, `ERR-302L`, `AltibaseDataAdapter`, `AltibaseTransaction`, `jdbc:Altibase://IP:port_no/db_name`, `ODBC Manager`, `JDBC driver file` 확인 |
| J005 갱신 문서 stale-string grep | 한국어 잔여 문구, 깨진 `Altibase` 주석, 알려진 오탈자 패턴 재검출 0건 |
| J005 manifest 메타데이터 대조 | 갱신된 `arch` 문서 확인, 불일치 0건 |
| J006 문서형 첨부 URL 대조 | SQL/튜닝/마이그레이션/변환/도구 범위 6개 URL 확인, 누락 0개 |
| J006 핵심 항목 grep | `MigrationCenter can be downloaded`, `PSM_PARAM_AND_RETURN_WITHOUT_PRECISION_ENABLE`, `docker build [OPTIONS]`, `docker run [OPTIONS]`, `Altibase JDBC Driver Registration`, `Layer Preview` 확인 |
| J006 갱신 문서 stale-string grep | 한국어 잔여 문구, Docker 명령/출력 결합 패턴 재검출 0건 (`Registeration`은 원본 source URL과 이미지 경로에만 보존) |
| J006 manifest 메타데이터 대조 | 갱신된 `arch` 문서 11개 확인, 불일치 0건 |
| J007 FAQ 대응 문서 대조 | 설치/패치/업그레이드 4개, 운영/관리 28개 대응 확인, 누락 0개 |
| J007 문서형 첨부 URL 대조 | 설치/운영 FAQ 범위 URL-backed 문서형 첨부 0개 확인, 누락 0개 |
| J007 핵심 항목 grep | `altibased`, `MEM_MAX_DB_SIZE`, `SYS_TBS_MEM_DATA`, `V$MEMSTAT`, `LOG_DIR`, `ARCHIVE_DIR`, `Restart Altibase` 확인 |
| J007 갱신 문서 stale-string grep | 한국어 잔여 문구, `Unknown macro`, 깨진 `PATH` 링크, 알려진 오탈자 패턴 재검출 0건 |
| J007 manifest 메타데이터 대조 | 갱신된 `FAQE` 문서 16개 확인, 불일치 0건 |
| J008 FAQ 대응 문서 대조 | 이중화 8개, 백업/복구 7개, SQL 2개, Stored Procedures 2개, 개발/API 9개 대응 확인, 누락 0개 |
| J008 문서형 첨부 URL 대조 | 범위 내 URL-backed 문서형 첨부 3개 및 텍스트 샘플 첨부 1개 확인, 누락 0개 |
| J008 핵심 항목 grep | `ALTER REPLICATION replication_name ADD TABLE`, `DROP TABLE FROM`, `REPLICATION_MAX_LOGFILE`, `SP_DML_RECORD_COUNT.txt`, `08F01`, `ES_08FO01`, `SELECT DB_NAME FROM V$DATABASE`, `SQLLEN Size` 확인 |
| J008 갱신 문서 stale-string grep | 한국어 잔여 문구, 깨진 `libaltibase_odbc` 링크, `SELECT_DB_NAME`, `run_il_int.sh`, `Error rendering macro`, `thㅅ`, 비ASCII 인용부호 패턴 재검출 0건 |
| J008 manifest 메타데이터 대조 | 갱신된 `FAQE` 문서 확인, 불일치 0건 |
| J009 FAQ 대응 문서 대조 | 모니터링 19개, 에러 메시지 29개, 유틸리티 2개, 기타 2개, 일반 3개 대응 확인, 누락 0개 |
| J009 문서형 첨부 URL 대조 | 범위 내 URL-backed 문서형 첨부 4개 확인, 누락 0개 |
| J009 핵심 항목 grep | `Bind variable value`, `Disk table count query`, `UTRANS_TIMEOUT`, `FETCH CURSOR`, `DISK_INDEX_BUILD_SORT_AREA_SIZE`, `ADO.NET`, `TPC-C`, `WAL` 확인 |
| J009 갱신 문서 stale-string grep | 한국어 잔여 문구, `Error rendering macro`, `WIndows`, `Characterstic`, `Disability`, 깨진 manual link 패턴 재검출 0건 |
| J009 manifest 메타데이터 대조 | 갱신된 `FAQE` 문서 확인, 불일치 0건 |
| J010 문서형 첨부 URL 전체 대조 | 기술 문서 42개, FAQ 7개 URL-backed 문서형 링크 확인, 누락 0개 |
| J010 출처 링크 보정 grep | GeoServer 외부 출처 링크, IBM Installation Manager URL, 영어 support/manual/product 링크 확인 |
| J010 manifest 메타데이터 대조 | 갱신된 `arch`/`FAQE` 문서 8개 확인, 불일치 0건 |

## 결론

이번 재검토와 갱신 후의 현재 상태에서는, 검토 범위 기준으로 한국어 문서의 URL-backed 문서형 첨부 및 확인한 중요 출처 링크가 영어 대응 문서에 보존되어 있습니다.

다만 이 보고서는 문서 매핑, 첨부파일, 기술 키워드, 변경 위험이 높은 항목을 중심으로 한 재검토 결과입니다. 최종 목표인 Codex, GPTs, LLM 참고 문서로 취합할 때는 영어 문서를 다시 읽기 쉬운 구조로 통합하면서 문장 단위 품질과 용어 일관성을 추가로 다듬는 것이 좋습니다.
