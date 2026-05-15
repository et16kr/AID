# LLM 참고 문서화를 위한 리뷰 계획

작성일: 2026-05-15

작업공간: `/home/et16/AID`

## 목적

이 문서는 Altibase 한국어/영어 문서 정비 이후, Codex, GPTs, 기타 LLM이 참고하기 쉬운 기술 문서 세트로 만들기 위한 다음 리뷰 계획을 정의한다.

현재 기준으로 한국어 문서에만 있고 영어 문서에 없는 내용은 `KO_EN_DOC_REVIEW_REPORT.md` 검토 범위에서 발견되지 않았다. 다음 리뷰의 중심은 단순 누락 여부가 아니라, 영어 문서가 LLM 참고 문서로 충분히 정확하고 일관되며 검색하기 쉬운지 확인하는 것이다.

## 최종 목표

- 한국어 원문 문서를 기준으로 영어 문서의 의미 누락, 오래된 절차, 잘못된 버전 정보가 없는지 최종 확인한다.
- 영어 문서를 몇 개의 주제별 문서로 취합할 수 있도록 구조와 중복을 정리한다.
- Codex, GPTs, 기타 LLM이 근거 문서로 읽기 쉬운 형태의 영어 기준 문서를 만든다.
- LLM이 영어뿐 아니라 터키어, 아랍어, 독일어, 프랑스어, 태국어, 중국어, 일본어 등 여러 언어로 답변할 때도 제품명, 명령어, SQL, 설정값, 파일 경로, 에러 코드를 정확히 유지할 수 있게 한다.

## 현재 기준 상태

| 항목 | 상태 |
| --- | --- |
| 한국어 기술 문서와 영어 기술 문서 대응 | `DOCK/Home` 51개 기준 대응 확인 |
| 한국어 FAQ와 영어 FAQ 핵심 문서 대응 | `faq/Home` 115개 기준 대응 확인 |
| 문서형 첨부파일 누락 | 누락 0개 |
| 최근 재검토 보고서 | `KO_EN_DOC_REVIEW_REPORT.md` |
| 작업 지침 문서 | `AGENTS.md` |
| 한국어 문서 삭제 여부 | 삭제하지 않음 |

## 리뷰 원칙

- 한국어 문서를 원문 기준으로 본다.
- 한국어 문서와 영어 문서가 의미상 다르면 한국어 문서를 우선한다.
- 영어 문서는 단순 직역보다 자연스러운 기술 영어로 정리한다.
- 명령어, SQL, 에러 코드, 설정값, 파일 경로, 제품명은 번역하지 않고 원문 표기를 보존한다.
- 검토 범위, 수정 내역, 남은 리스크는 보고서로 남긴다.
- 한국어 문서는 리뷰와 추적을 위해 삭제하지 않는다.

## 리뷰 단계

| 단계 | 상태 | 목표 | 산출물 |
| --- | --- | --- | --- |
| R001 | ToDo | 기준 상태 재확인 | 문서 수, 매핑, 첨부파일 누락 여부 확인 |
| R002 | ToDo | 한국어 원문 기준 의미 누락 샘플링 | 고위험 문서별 누락 후보 목록 |
| R003 | ToDo | 영어 문서 품질 리뷰 | 어색한 번역, 중복, 오래된 표현 수정 목록 |
| R004 | ToDo | LLM 참고 문서 구조 설계 | 주제별 통합 문서 목차 |
| R005 | ToDo | 다국어 답변 안정성 리뷰 | 보존해야 할 용어, 명령어, SQL, 에러 코드 목록 |
| R006 | ToDo | 최종 취합 전 승인 리뷰 | 수정 요약, 남은 리스크, 다음 작업 승인 기준 |

## R001 기준 상태 재확인

목표는 이전 검토 이후 문서가 바뀌었는지 확인하고, 한국어 문서 기준으로 영어 문서 대응이 깨지지 않았는지 확인하는 것이다.

확인 항목:

- `DOCK/Home` 한국어 기술 문서 51개가 영어 기술 문서에 대응되는지 확인한다.
- `faq/Home` 한국어 FAQ 115개가 `FAQE/Home` 핵심 문서에 대응되는지 확인한다.
- 한국어 문서의 문서형 첨부파일이 영어 문서에도 보존되어 있는지 확인한다.
- `manifest.json`이 유효한 JSON인지 확인한다.
- Markdown 변경에 trailing whitespace 문제가 없는지 확인한다.

검증 명령:

```bash
python3 -m json.tool manifest.json
git diff --check
find DOCK/Home -type f -name '*.md' | wc -l
find arch/Home -type f -name '*.md' | wc -l
find faq/Home -type f -name '*.md' | wc -l
find FAQE/Home -type f -name '*.md' | wc -l
```

완료 기준:

- 기술 문서 대응 누락 0개
- FAQ 핵심 문서 대응 누락 0개
- 문서형 첨부파일 누락 0개
- JSON 및 diff 검증 통과

## R002 한국어 원문 기준 의미 누락 샘플링

목표는 담당자가 한국어 문서만 수정하고 영어 문서에는 반영하지 않았을 가능성이 높은 영역을 집중적으로 확인하는 것이다.

우선 검토 대상:

- 설치, 패치, 업그레이드 절차
- 지원 OS 및 플랫폼
- 이중화, 백업, 복구
- 보안, 계정, 패스워드 정책
- 성능 튜닝, 파티션, HPT
- 모니터링, 장애 대응, 에러 코드
- 마이그레이션 및 DBMS 변환

확인 항목:

- 버전 기준이 한국어와 영어에서 일치하는지 확인한다.
- 한국어에 추가된 경고, 예외, 제약사항이 영어에 있는지 확인한다.
- 절차 단계, 명령어, SQL 예제가 누락되지 않았는지 확인한다.
- 첨부 문서가 본문 설명과 함께 충분히 연결되어 있는지 확인한다.

완료 기준:

- 차이가 있으면 한국어 기준으로 영어 문서에 반영한다.
- 반영한 문서와 이유를 리뷰 보고서에 기록한다.

## R003 영어 문서 품질 리뷰

목표는 영어 문서가 LLM이 근거로 사용하기에 충분히 명확한지 확인하는 것이다.

확인 항목:

- 자동 번역투 문장을 기술 문서 문장으로 다듬는다.
- 같은 의미의 섹션이 여러 문서에 반복되면 취합 단계에서 병합 후보로 표시한다.
- 제목이 검색 가능한 기술 키워드를 포함하는지 확인한다.
- 절차 문서는 prerequisites, steps, validation, notes 구조로 정리 가능한지 확인한다.
- 에러 문서는 symptom, cause, resolution, related parameters 구조로 정리 가능한지 확인한다.

완료 기준:

- 문서별 품질 이슈 목록을 만든다.
- 바로 고칠 수 있는 문장 품질 문제는 영어 문서에 반영한다.
- 취합 단계에서 처리할 중복은 별도로 표시한다.

## R004 LLM 참고 문서 구조 설계

목표는 정비된 영어 문서를 GPTs/Codex/LLM이 읽기 쉬운 몇 개의 주제별 문서로 묶기 위한 목차를 설계하는 것이다.

초안 주제:

- Installation and Upgrade
- Operation and Administration
- Backup and Recovery
- Replication
- Monitoring and Troubleshooting
- Development and API
- Error Messages
- Migration and Conversion
- Performance Tuning
- Security and User Management

확인 항목:

- 각 주제 문서에 포함될 원본 문서 목록을 정한다.
- 중복되는 FAQ와 기술 문서를 어느 쪽 설명으로 통합할지 정한다.
- LLM 검색을 위해 절 제목과 키워드를 정리한다.
- 원본 문서 출처를 각 절에 남길 방식을 정한다.

완료 기준:

- 주제별 통합 문서 목차가 완성된다.
- 각 목차 항목에 원본 문서 경로가 연결된다.

## R005 다국어 답변 안정성 리뷰

목표는 LLM이 여러 언어로 답변하더라도 변경하면 안 되는 기술 표기가 보존되도록 기준을 만드는 것이다.

보존 대상:

- 제품명: `Altibase`, `ALTIBASE HDB`
- 명령어와 유틸리티: `isql`, `aexport`, `iloader`, `altimon`
- SQL 키워드와 시스템 뷰: `CREATE USER`, `ALTER USER`, `V$VERSION`
- 설정값과 프로퍼티: `TIMED_STATISTICS`, `MEM_MAX_DB_SIZE`, `TRANSACTION_TABLE_SIZE`
- 파일과 경로: `$ALTIBASE_HOME`, `/etc/systemd/logind.conf`
- 에러 코드: `ERR-0109D`, `ERR-11075`, `ERR-91015`

확인 항목:

- 번역하면 안 되는 표기를 용어집으로 분리한다.
- 다국어 답변 시 원문 표기를 유지해야 하는 항목을 문서에 명시한다.
- 제품별, 버전별 조건이 있는 경우 조건을 문장 앞부분에 분명히 둔다.

완료 기준:

- LLM용 용어 보존 규칙이 정리된다.
- 최종 통합 문서에 적용할 용어집 초안이 만들어진다.

## R006 최종 취합 전 승인 리뷰

목표는 영어 문서 취합 작업을 시작해도 되는지 판단하는 것이다.

확인 항목:

- 한국어 기준 누락이 새로 발견되지 않았는지 확인한다.
- 새로 발견된 차이는 모두 영어 문서에 반영했는지 확인한다.
- 취합 대상 주제와 원본 문서 목록이 확정되었는지 확인한다.
- 남은 리스크가 문서화되었는지 확인한다.

완료 기준:

- 리뷰 보고서가 갱신된다.
- 통합 문서 작성으로 넘어갈 수 있다는 승인 기준이 충족된다.

## J013 LLM reference handoff package plan

작성일: 2026-05-16

이 절은 J002-J012에서 정비한 영어 문서를 GPTs, Codex, 기타 LLM 지식 파일로 취합하기 위한 인계 계획이다. 이 단계는 계획 수립만 다루며, 원본 한국어 문서, 원본 영어 문서, `manifest.json`의 문서 본문 메타데이터를 변경하지 않는다.

### 패키지 원칙

- 한국어 원문은 계속 권위 기준으로 유지한다.
- 영어 취합 문서는 `arch/Home`과 한국어 기준 핵심 `FAQE/Home` 문서를 주 입력으로 사용한다.
- 원본 문서는 삭제하거나 이동하지 않는다. 취합 문서는 별도 디렉터리, 예를 들면 `llm-reference/`, 아래 새 파일로 생성한다.
- 각 취합 문서에는 `Source paths` 절을 두고 실제 참조한 영어 원본 경로를 남긴다.
- 한국어 대응 근거가 필요한 경우 `KO_EN_DOC_REVIEW_REPORT.md`의 J002-J012 매핑과 검증 결과를 함께 참조한다.
- 영어-only `FAQE` 추가 문서는 유용할 수 있지만 한국어 기준 커버리지 검증 범위 밖이다. 포함할 경우 해당 절에 `English-only source`로 표시하고 별도 리뷰를 거친다.
- 첨부 파일 URL, 외부 제품 URL, `docs.altibase.com` 원본 URL은 취합 중에도 변경하지 않는다.

### 권장 패키지 구조

| 출력 문서 | 목적 | 주요 영어 source paths |
| --- | --- | --- |
| `01-installation-upgrade-platform.md` | 설치, 패치, 업그레이드, DB 생성, OS별 플랫폼 설정, 설치 장애 대응 | `arch/Home/Altibase Installation Guide__14647632.md`, `arch/Home/Altibase Installation Guide/**`, `arch/Home/Altibase Quick Install & Start for UNIX__16875604.md`, `arch/Home/Troubleshooting Altibase Installation Problems__15138879.md`, `arch/Home/Creating ALTIBASE Database__22643020.md`, `arch/Home/Linux Setup Guide for Altibase__22643022.md`, `arch/Home/Solaris Setup Guide for Altibase__14058290.md`, `arch/Home/Solaris Setup Guide for Altibase/**`, `arch/Home/HPUX Setup Guide for Altibase__14058288.md`, `arch/Home/AIX Setup Guide for Altibase__14058298.md`, `arch/Home/Altibase Docker Guide__14647741.md`, `arch/Home/Altibase Docker Guide/**`, `FAQE/Home/01. Installation, Patch, Upgrade/**` |
| `02-architecture-storage-concepts.md` | Altibase 구조, In-Memory와 Disk DBMS 차이, WAL, 스토리지와 디스크 구성 개념 | `arch/Home/Home/**`, `arch/Home/Disk Configuration Guide for Altibase__14647508.md`, `arch/Home/Disk Configuration Guide for Altibase/**`, `arch/Home/Configuration Guide For Minimizing Disk I_O Contention__22643018.md`, `FAQE/Home/13. General/**`, `FAQE/Home/ALTIBASE HDB Architecture/**` |
| `03-operation-administration.md` | 운영 설정, 시작/종료, 계정과 권한, 세션, 로그 경로, 용량 산정, OS 유틸리티 | `arch/Home/Altibase Configuration File Guide__22642991.md`, `arch/Home/Understanding the Altibase Start_Shut down Process__14909450.md`, `arch/Home/Understanding the Altibase Start_Shut down Process/**`, `arch/Home/System Data Capacity Estimation Guide for Altibase Operations__22643042.md`, `arch/Home/Utility Guide for each OS for Problem Analysis__16875587.md`, `arch/Home/UNIX Memory Management__16875572.md`, `FAQE/Home/02. Operation and Management/**`, `FAQE/Home/ALTIBASE HDB Administration/**` |
| `04-backup-recovery.md` | 백업 정책, cold/online backup, time based recovery, 로그와 복구 절차 | `arch/Home/Considerations for Altibase Backup Policy__14647709.md`, `arch/Home/Considerations for Altibase Backup Policy/**`, `arch/Home/Responding to Failures Guide for Altibase__15138818.md`, `arch/Home/Responding to Failures Guide for Altibase/**`, `FAQE/Home/04. Backup and Recovery/**` |
| `05-replication-ha.md` | 이중화 구성, 제약사항, 충돌, gap 모니터링, HA 운영 주의사항 | `arch/Home/Altibase Replication Configuration Guide__14647672.md`, `arch/Home/Altibase Replication Constraints Guide__22643008.md`, `FAQE/Home/03. Replication/**`, `FAQE/Home/ALTIBASE HDB Replication/**` |
| `06-monitoring-troubleshooting.md` | 모니터링 쿼리, CPU/메모리 증가 분석, 장애 수집 절차, 운영 진단 | `arch/Home/Altibase Monitoring Queries Guide__14058229.md`, `arch/Home/Altibase Monitoring Queries Guide/**`, `arch/Home/Altibase CPU Overload Analysis Guide__14647581.md`, `arch/Home/Altibase CPU Overload Analysis Guide/**`, `arch/Home/Altibase Memory Usage Increase Analysis Guide__14647388.md`, `arch/Home/Altibase Memory Usage Increase Analysis Guide/**`, `arch/Home/Responding to Failures Guide for Altibase__15138818.md`, `arch/Home/Responding to Failures Guide for Altibase/**`, `FAQE/Home/08. Monitoring/**`, `FAQE/Home/ALTIBASE HDB Troubleshooting/**` |
| `07-error-message-reference.md` | 에러 코드별 증상, 원인, 조치, 관련 프로퍼티와 SQL | `FAQE/Home/09. Error Messages/**`, `FAQE/Home/Altibase Error Messages__6979655.md`, `FAQE/Home/Altibase Error Messages/**`, `arch/Home/Altibase Development Guide/4. CLIENT APPLICATION Error Messages__14058547.md`, `arch/Home/Altibase Precompiler Guide/4. Frequently Occurring Error Messages__22643006.md` |
| `08-sql-performance-tuning.md` | SQL, 파티션, HPT, 튜닝, DRDB index, stored procedure 참고 | `arch/Home/Altibase Development Guide__14058519.md`, `arch/Home/Altibase Development Guide/**`, `arch/Home/Altibase SQL Tuning Guide__22643010.md`, `FAQE/Home/05. SQL/**`, `FAQE/Home/06. Stored Procedure/**`, `FAQE/Home/12. Others/**`, `FAQE/Home/ALTIBASE HDB Performance Tuning/**` |
| `09-development-api-integration.md` | APRE, Precompiler, Java, ODBC, ADO.NET, PHP, WAS, Spring/iBATIS/MyBatis/Hibernate, 도구 연동 | `arch/Home/Altibase Developer Training__22642996.md`, `arch/Home/Altibase Precompiler Guide__14647438.md`, `arch/Home/Altibase Precompiler Guide/**`, `arch/Home/APRE_C_C++ New Features & Upgrade Guide__22643052.md`, `arch/Home/Altibase APRE(SES) _C_C++ Makefile__15630378.md`, `arch/Home/Altibase APRE(SES) _C_C++ Makefile/**`, `arch/Home/JAVA Developer's Guide__16875544.md`, `arch/Home/Altibase ODBC Development Guide in Windows Environment__15138911.md`, `arch/Home/Altibase and unixODBC Integration Guide__14647413.md`, `arch/Home/Altibase and unixODBC Integration Guide/**`, `arch/Home/Altibase Window ADO.NET Development Guide__14647565.md`, `arch/Home/Altibase Window ADO.NET Development Guide/**`, `arch/Home/PHP Integration Guide for Altibase__14647305.md`, `arch/Home/PHP Integration Guide for Altibase/**`, `arch/Home/TOMCAT Integration Guide for Altibase__14058489.md`, `arch/Home/TOMCAT Integration Guide for Altibase/**`, `arch/Home/JEUS Integration Guide for Altibase__14058459.md`, `arch/Home/JEUS Integration Guide for Altibase/**`, `arch/Home/JBOSS Integration Guide for Altibase__14647358.md`, `arch/Home/JBOSS Integration Guide for Altibase/**`, `arch/Home/WEBLOGIC Integration Guide for Altibase__14058319.md`, `arch/Home/WEBLOGIC Integration Guide for Altibase/**`, `arch/Home/WebSphere Integration Guide for Altibase__14058343.md`, `arch/Home/Spring Integration Guide for Altibase__14058410.md`, `arch/Home/Spring Integration Guide for Altibase/**`, `arch/Home/iBatis Integration Guide for Altibase__14058303.md`, `arch/Home/iBatis Integration Guide for Altibase/**`, `arch/Home/MyBatis Integration Guide for Altibase__14058349.md`, `arch/Home/MyBatis Integration Guide for Altibase/**`, `arch/Home/Hibernate Integration Guide for Altibase__14058388.md`, `arch/Home/SQuirrel SQL Client Quick Guide for Altibase__14647622.md`, `arch/Home/SQuirrel SQL Client Quick Guide for Altibase/**`, `arch/Home/Altibase GeoServer Integration Guide__22643004.md`, `FAQE/Home/07. Development and API/**`, `FAQE/Home/11. Utilities/**` |
| `10-migration-conversion-tools.md` | Altibase 버전 간 마이그레이션, Oracle/MSSQL 변환, Migration Center, VC 개발 가이드 | `arch/Home/Altibase Data Migration Process Guide__22642994.md`, `arch/Home/Altibase_Oracle Comparison__16875638.md`, `arch/Home/ORACLE to ALTIBASE Conversion Guide__22643038.md`, `arch/Home/Altibase Oracle Conversion Guide__14647316.md`, `arch/Home/Altibase Oracle Conversion Guide/**`, `arch/Home/MSSQL to ALTIBASE Conversion Guide__22643024.md`, `arch/Home/Migration Center User Guide__19955861.md`, `arch/Home/Altibase VC 2008 Development Guide__19333567.md`, `arch/Home/Altibase VC 2010 Development Guide__19334121.md` |
| `11-terminology-and-multilingual-rules.md` | 다국어 답변 시 보존해야 하는 제품명, 명령어, SQL, 프로퍼티, 경로, 에러 코드 규칙 | 이 계획의 `다국어 용어 보존 규칙` 절, `KO_EN_DOC_REVIEW_REPORT.md`, 모든 취합 문서의 `Terminology` 절 |

`FAQE/Home/ALTIBASE HDB*`와 `FAQE/Home/Altibase Error Messages/**` 경로는 영어-only 보조 후보로 취급한다. 이 경로를 실제 취합 문서에 포함할 때는 한국어 기준 핵심 FAQ 검증 범위 밖이라는 점을 `Source paths` 절이나 해당 섹션에 명시한다.

### 취합 문서 작성 템플릿

각 취합 문서는 다음 순서를 기본값으로 사용한다. 주제 특성상 불필요한 절은 생략할 수 있지만, `Source paths`와 `Terminology` 절은 생략하지 않는다.

```markdown
# <Topic title>

## Source paths

- <English source path>
- <English source path>

## Scope and audience

## Key facts

## Procedures

## SQL, commands, and configuration

## Validation and troubleshooting

## Version-specific notes

## Related errors

## Attachments and external references

## Terminology
```

절별 출처가 여러 문서에 걸쳐 있으면 해당 절 아래에 `Sources:` 줄을 추가한다. 예를 들어 백업 복구 문서의 time based recovery 절은 `FAQE/Home/04. Backup and Recovery/**`와 관련 장애 대응 문서 경로를 함께 남긴다.

### 중복 처리 규칙

- 기술 가이드와 FAQ가 같은 주제를 설명하면 기술 가이드를 표준 설명으로 사용하고 FAQ는 운영 절차, 예외, 에러 대응 예시로 병합한다.
- 같은 SQL 또는 명령어가 여러 문서에 반복되면 하나의 canonical 예제로 정리하고, 버전이나 조건이 다른 경우에만 별도 예제로 둔다.
- 에러 메시지는 `07-error-message-reference.md`에 모으고, 다른 문서에서는 관련 에러 코드와 원인 요약만 링크한다.
- `Altibase Development Guide`처럼 여러 주제에 걸치는 문서는 하나의 주 문서에 canonical 내용을 두고 다른 취합 문서에서는 관련 절로 상호 참조한다.
- 한국어 원문과 영어 문서가 다시 달라진 것을 발견하면 취합하지 말고 한국어 기준 영어 문서 보정 작업으로 되돌린다.

### 다국어 용어 보존 규칙

LLM이 터키어, 아랍어, 독일어, 프랑스어, 태국어, 중국어, 일본어 등으로 답변하더라도 다음 표기는 번역하지 않고 원문 그대로 유지하도록 취합 문서에 명시한다.

| 유형 | 보존 예시 | 규칙 |
| --- | --- | --- |
| 제품명 | `Altibase`, `ALTIBASE HDB` | 제품명은 번역하지 않는다. 문장 설명만 요청 언어로 번역한다. |
| 명령어와 유틸리티 | `isql`, `aexport`, `iloader`, `altimon`, `apre`, `sqlcli` | 명령어 이름, 옵션, 출력 예제는 코드 표기로 유지한다. |
| SQL과 객체명 | `CREATE USER`, `ALTER USER`, `ALTER REPLICATION`, `V$VERSION`, `SYS_TABLES_` | SQL 키워드, 메타 테이블, 성능 뷰, 시스템 객체명은 원문을 유지한다. |
| 프로퍼티와 설정값 | `TIMED_STATISTICS`, `MEM_MAX_DB_SIZE`, `TRANSACTION_TABLE_SIZE`, `REPLICATION_MAX_LOGFILE` | 프로퍼티명과 값은 번역하지 않고, 의미 설명만 번역한다. |
| 경로와 환경변수 | `$ALTIBASE_HOME`, `$DOMAIN_HOME`, `/etc/systemd/logind.conf`, `altibase.properties` | 파일명, 디렉터리, 환경변수는 코드 표기로 유지한다. |
| 에러 코드 | `ERR-0109D`, `ERR-11075`, `ERR-4103C`, `ERR-61035`, `ERR-91015` | 에러 코드는 제목과 본문 양쪽에서 원문을 유지한다. |
| 버전과 조건 | `Altibase 7.1.0 or later`, `6.5.1~7.1.0`, `7.3.0 or later` | 버전 조건은 문장 앞부분에 명확히 두고 임의로 단순화하지 않는다. |
| 첨부와 URL | `docs.altibase.com` URL, `.pdf`, `.pptx`, `.zip` 링크 | URL과 파일명은 바꾸지 않는다. 링크 라벨만 필요한 경우 자연스러운 영어로 정리한다. |

다국어 답변을 염두에 둔 문장 작성 규칙은 다음과 같다.

- "it", "this", "that" 같은 대명사보다 제품명, 객체명, 프로퍼티명을 반복해 참조한다.
- 경고, 제한, 버전 조건은 절의 앞부분에 둔다.
- 수치, 단위, 기본값, 재시작 필요 여부를 한 문장 안에서 분리하지 않는다.
- 코드 블록 안의 주석은 영어 기준으로 유지하고, 사용자가 다른 언어로 질문하더라도 코드 자체는 번역하지 않도록 한다.
- 운영 절차는 prerequisites, steps, validation, notes 순서로 작성해 언어가 바뀌어도 단계가 흐려지지 않게 한다.

### 다음 단계 실행 순서

1. `llm-reference/` 같은 별도 출력 디렉터리를 만들고 위 출력 문서 이름으로 빈 골격을 만든다.
2. 각 문서의 `Source paths` 절을 먼저 채운 뒤 내용을 취합한다.
3. 취합 중 발견한 한국어-영어 의미 차이는 통합 문서에서 직접 해결하지 말고 원본 영어 문서 보정 작업으로 기록한다.
4. 문서별로 중복 제거, 용어 보존, 링크 보존, 버전 조건 보존을 self-review한다.
5. 전체 패키지에 대해 `rg` 기반 용어 보존 점검, 빈 Markdown 링크 점검, 첨부 URL 보존 점검, `git diff --check`를 수행한다.
6. 최종 산출물마다 한국어 권위 기준, 영어 source paths, 남은 리스크를 남긴다.

## 보고서 형식

각 리뷰 후 다음 형식으로 보고서를 남긴다.

```markdown
# 리뷰 보고서

검토일:
검토 범위:

## 발견 사항

## 수정한 문서

## 검증 결과

## 남은 리스크

## 다음 작업
```

## 중단 조건

다음 상황에서는 리뷰를 멈추고 사용자 확인을 받는다.

- 한국어 원문과 영어 문서가 서로 다른데 어느 쪽이 최신인지 판단할 수 없는 경우
- 한국어 원문 자체에 오류가 있어 보이지만 외부 근거 없이 수정하기 어려운 경우
- 대량의 영문 재작성이나 문서 구조 변경이 필요해 기존 문서 추적성이 약해질 수 있는 경우
- 원본 문서 삭제 또는 이동이 필요한 경우

## 다음 실행 권장 순서

1. R001 기준 상태 재확인
2. R002 고위험 영역 샘플링
3. R003 영어 품질 리뷰
4. R004 통합 문서 구조 설계
5. R005 다국어 답변 안정성 리뷰
6. R006 최종 취합 전 승인 리뷰
7. J013 LLM reference handoff package plan 기준으로 패키지 골격 작성

이 순서와 J013 인계 계획을 기준으로 완료하면, 이후 작업은 실제 영어 통합 문서 작성과 GPTs/Codex용 최종 문서 패키징으로 넘어갈 수 있다.
