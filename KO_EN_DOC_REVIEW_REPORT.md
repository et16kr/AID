# 한국어-영어 문서 재검토 보고서

검토일: 2026-05-15

작업공간: `/home/et16/AID`

## 요약

한국어 문서를 기준으로 영어 문서를 다시 비교했습니다. 담당자가 오류를 발견한 뒤 한국어 문서만 수정하고 영어 문서는 갱신하지 않았을 가능성을 전제로, 기술 문서 매핑, FAQ 핵심 문서 대응, 문서형 첨부파일, 최근에 차이가 있었던 고위험 항목을 재점검했습니다.

검토 중 실제 차이 2건을 발견하여 영어 문서에 반영했습니다.

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

## 결론

이번 재검토와 갱신 후의 현재 상태에서는, 검토 범위 기준으로 한국어 문서에만 있고 영어 문서에 없는 내용은 발견되지 않았습니다.

다만 이 보고서는 문서 매핑, 첨부파일, 기술 키워드, 변경 위험이 높은 항목을 중심으로 한 재검토 결과입니다. 최종 목표인 Codex, GPTs, LLM 참고 문서로 취합할 때는 영어 문서를 다시 읽기 쉬운 구조로 통합하면서 문장 단위 품질과 용어 일관성을 추가로 다듬는 것이 좋습니다.
