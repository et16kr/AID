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

이 반영 후, 현재 검토 범위에서는 한국어 문서에는 있지만 영어 문서에 없는 누락 내용은 추가로 발견되지 않았습니다. 한국어 문서는 삭제하지 않았습니다.

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

## 검토 범위

| 구분 | 한국어 기준 문서 | 영어 대상 문서 | 결과 |
| --- | ---: | ---: | --- |
| 기술 문서 | `DOCK/Home`: 51개 Markdown | `arch/Home`: 181개 Markdown, 그중 한국어 대응 상위 문서 51개 | 51개 모두 영어 대응 문서 확인 |
| FAQ 핵심 문서 | `faq/Home`: 115개 Markdown | `FAQE/Home`: 한국어 FAQ에 대응하는 핵심 문서 115개 | 115개 모두 영어 대응 문서 확인 |
| 문서형 첨부파일 | 한국어 기술 문서 41개, 한국어 FAQ 7개 | 대응 영어 문서 | 누락 0개 |

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
| 한국어 기술 문서의 문서형 첨부파일 | 41 |
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

## 결론

이번 재검토와 갱신 후의 현재 상태에서는, 검토 범위 기준으로 한국어 문서에만 있고 영어 문서에 없는 내용은 발견되지 않았습니다.

다만 이 보고서는 문서 매핑, 첨부파일, 기술 키워드, 변경 위험이 높은 항목을 중심으로 한 재검토 결과입니다. 최종 목표인 Codex, GPTs, LLM 참고 문서로 취합할 때는 영어 문서를 다시 읽기 쉬운 구조로 통합하면서 문장 단위 품질과 용어 일관성을 추가로 다듬는 것이 좋습니다.
