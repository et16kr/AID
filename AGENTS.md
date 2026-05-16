# 작업 지침: Altibase 문서 정비 및 GPT/Codex용 기술문서화

이 저장소의 현재 작업 목표는 Altibase 한국어/영문 문서를 정비한 뒤, Codex, GPTs, 기타 LLM이 참고하기 쉬운 기술문서 세트로 재구성하는 것이다.

## 최종 목표

- 한국어 원문 문서를 기준으로 영문 문서를 최신화한다.
- 영문 문서를 정리해 몇 개의 큰 주제별 문서로 취합한다.
- 취합한 영문 문서를 GPTs 지식 파일, Codex 참고 문서, 기타 LLM용 참조 문서로 읽기 쉬운 형태로 갱신한다.
- 최종 산출물은 사람이 검토하기 쉽고, LLM이 검색/참조하기 쉬운 기술문서 세트여야 한다.
- 최종 문서는 LLM이 참고하여 영어뿐 아니라 터키어, 아랍어, 독일어, 프랑스어, 태국어, 중국어, 일본어 등 여러 언어로 정확하게 답변할 수 있는 기준 지식이 되어야 한다.

## 현재 작업의 핵심 원칙

- 한국어 문서를 원문 기준으로 본다.
- 한국어 문서에만 있는 내용, 수정사항, 최신 절차, 첨부 링크가 있으면 대응되는 영문 문서에 영어로 반영한다.
- 한국어 문서는 리뷰와 추적을 위해 삭제하지 않는다.
- 기존 사용자의 변경사항을 되돌리지 않는다.
- 단순히 파일 수만 맞추지 말고, 내용 차이와 첨부 문서 참조까지 확인한다.
- 영문 문서를 수정할 때는 한국어 문서의 의미를 보존하되, 자연스러운 기술 영어로 작성한다.
- 검증 결과와 판단 근거는 리뷰 보고서로 남긴다.

## 현재 판단: LLM 취합 스크립트 실행 시점

- `.codex-jobs/llm-reference-consolidation/` workflow는 필요하므로 보존한다.
- 이 workflow는 최종 LLM 참고 문서 취합용이며, 영문 source 문서 완성 전에 먼저 실행하지 않는다.
- 먼저 한국어 원문 기준으로 `arch/`와 `FAQE/` 영문 source 문서의 누락, 미번역, 잘못된 절차, 오래된 버전 정보, 첨부 링크 누락을 충분히 보강한다.
- 영문 source 문서가 안정화된 뒤에 `llm-reference/` 취합 workflow를 실행한다.
- 이유: 취합 문서를 먼저 만들면 이후 영문 source 문서 보강 사항을 `llm-reference/`에 다시 반영해야 하므로 재작업과 추적성 저하가 발생한다.
- 따라서 현재 우선순위는 `KO -> EN source 문서 완성`이고, `llm-reference/` 생성은 그 다음 단계이다.

## 단계별 완료 판단 기준

1. `KO -> EN 완전성 보강` 완료 기준
   - `DOCK/Home` 51개 기술 문서와 `faq/Home` 115개 FAQ가 대응 영문 문서와 다시 연결되어 있다.
   - 절차, SQL, 명령어, 설정값, 경고, 버전 조건, 첨부 링크를 확인했다는 문서별 기록이 있다.
   - 한국어 원문에만 있고 영어에 없는 항목은 `arch/` 또는 `FAQE/`에 반영되어 있다.
   - 반영하지 않은 항목은 반영 불가 사유와 남은 리스크로 기록되어 있다.
   - URL-backed 문서형 첨부 누락은 0개이고, unresolved KO/EN 의미 차이는 0개이다.

2. `영문 source 문서 안정화` 완료 기준
   - 잔여 한글은 첨부 파일명, URL, 한글 데이터 예제처럼 의도된 항목으로만 분류되어 있다.
   - 빈 Markdown 링크, `Error rendering macro`, `Unknown macro`, `unknown-macro` 잔여 패턴이 없다.
   - legacy `#` 첨부 라벨은 모두 목록화되어 있고 `no downloadable URL in source`로 처리되어 있다.
   - 영어-only `FAQE` 문서는 Korean-source-verified로 오인되지 않게 분류되어 있다.
   - 수정된 문서는 `manifest.json` 메타데이터가 갱신되어 있고, 기본 검증 명령이 통과한다.

3. `LLM 취합 스크립트 실행` 완료 기준
   - `.codex-jobs/llm-reference-consolidation/jobs.tsv`의 모든 job이 `Done`이다.
   - `llm-reference/` 아래 예상 Markdown 산출물이 모두 존재한다.
   - 각 취합 문서에 `Source paths`와 `Terminology` 절이 있다.
   - 사용한 source path는 실제 파일 또는 디렉터리로 존재한다.
   - 영어-only source, legacy attachment, diagram unavailable 같은 리스크 라벨이 필요한 곳에 표시되어 있다.
   - 최종 build report와 handoff 문서가 있고, 검증 명령이 통과하며 작업 트리가 clean 상태이다.

## 현재까지 진행된 작업

- 한국어 기술 문서 `DOCK`와 영문 기술 문서 `arch`의 대응 관계를 점검했다.
- 한국어 FAQ `faq`와 영문 FAQ `FAQE`의 핵심 카테고리 대응 관계를 점검했다.
- 한국어에만 있던 기술 문서 3개를 영문 문서로 추가했다.
  - `Altibase VC 2008 Development Guide`
  - `Altibase VC 2010 Development Guide`
  - `Migration Center User Guide`
- 한국어 문서에만 있던 PDF/PPTX/ZIP 등 첨부 문서 참조를 영문 문서에 보존했다.
- 한국어 FAQ에만 있거나 최신 한국어 문서에만 반영된 내용을 일부 영문 FAQ에 반영했다.
- 리뷰 보고서 문서로 `KO_EN_DOC_REVIEW_REPORT.md`를 생성했다.

## 앞으로 할 일

1. 한국어 문서 기준 재비교
   - `DOCK` 대 `arch`, `faq` 대 `FAQE`를 다시 비교한다.
   - 한국어 문서가 더 최신이거나 영문 문서와 의미상 다른 부분을 찾는다.
   - 단순 제목/파일 대응뿐 아니라 본문 절, 명령어, SQL, 설정값, 주의사항, 첨부 링크를 확인한다.

2. 영문 문서 개선
   - 차이가 있으면 한국어 문서를 기준으로 영문 문서를 갱신한다.
   - 한국어 원문에서만 수정된 오류, 절차, 버전 정보, 경고, 예외사항을 영문 문서에 반영한다.
   - 첨부 파일 링크는 가능하면 원문 `docs.altibase.com` URL을 보존한다.

3. 리뷰 보고서 갱신
   - 어떤 문서를 비교했는지 기록한다.
   - 어떤 차이를 발견했는지 기록한다.
   - 영문 문서에 반영한 내용을 기록한다.
   - 남은 리스크나 수동 검토가 필요한 부분이 있으면 명확히 적는다.

4. 영문 문서 취합
   - 이 단계는 영문 source 문서가 한국어 원문 기준으로 충분히 보강된 뒤에 진행한다.
   - `.codex-jobs/llm-reference-consolidation/` workflow는 이 단계에서 실행한다.
   - 정비가 끝난 영문 문서를 GPTs/Codex용으로 읽기 쉬운 몇 개의 문서로 묶는다.
   - 예시 주제:
     - Installation and Upgrade
     - Operation and Administration
     - Backup and Recovery
     - Replication
     - Monitoring and Troubleshooting
     - Development and API
     - Error Messages
     - Migration and Conversion
   - 각 취합 문서는 중복을 줄이고, 검색 가능한 제목과 명확한 절 구조를 사용한다.

5. Codex/GPTs/LLM용 최종 문서화
   - LLM이 답변 근거를 찾기 쉽도록 절 제목, 키워드, 명령어, SQL 예제를 정리한다.
   - 긴 문서는 요약, 절차, 주의사항, 관련 링크를 분리한다.
   - 문서마다 출처 또는 원본 대응 문서를 남긴다.
   - 최종 문서는 GPTs 지식 파일, Codex 참고 문서, 기타 LLM 참조 문서로 바로 넣을 수 있는 형태를 목표로 한다.
   - 문서는 영어를 기준 참조 언어로 정리하되, LLM이 사용자의 요청 언어에 맞춰 터키어, 아랍어, 독일어, 프랑스어, 태국어, 중국어, 일본어 등으로 답변할 수 있도록 의미가 명확해야 한다.
   - 다국어 답변 시 오역이 생기기 쉬운 제품명, 명령어, SQL, 설정값, 파일 경로, 에러 코드는 원문 표기를 유지할 수 있도록 문서에 명확히 남긴다.

## 비교 시 우선 확인할 항목

- 버전 정보
- 지원 OS 및 플랫폼
- 설치, 패치, 업그레이드 절차
- 운영 명령어와 설정 파일 경로
- SQL 예제와 시스템 뷰 이름
- 에러 코드, 원인, 조치 방법
- 이중화/백업/복구 관련 주의사항
- 보안, 계정, 패스워드 정책
- 첨부 PDF/PPTX/ZIP 링크
- 한국어 문서에만 있는 경고, 예외, 참고 문서

## 검증 방법

작업 후 가능한 범위에서 다음을 확인한다.

```bash
python3 -m json.tool manifest.json
git diff --check
find DOCK -type f -name '*.md' | wc -l
find faq -type f -name '*.md' | wc -l
find arch -type f -name '*.md' | wc -l
find FAQE -type f -name '*.md' | wc -l
```

첨부 문서 누락 여부도 다시 확인한다.

- 한국어 기술 문서의 문서형 첨부가 영문 기술 문서에 보존되어 있는지 확인한다.
- 한국어 FAQ의 문서형 첨부가 영문 FAQ에 보존되어 있는지 확인한다.
- 대상 확장자: `.pdf`, `.ppt`, `.pptx`, `.doc`, `.docx`, `.xls`, `.xlsx`, `.zip`

## 산출물

- 갱신된 영문 Markdown 문서
- 갱신된 `manifest.json`
- 리뷰 보고서 Markdown 문서
- 향후 Codex/GPTs/LLM용으로 취합된 영문 기술문서
- 다국어 답변 생성을 지원할 수 있는 명확한 기준 참조 문서

## 주의사항

- 한국어 문서는 삭제하지 않는다.
- 사용자가 명시적으로 요청하기 전까지 문서 취합 단계에서 원본 영문 문서를 제거하지 않는다.
- 한국어 원문과 영문 문서가 다르면 한국어 원문을 우선한다.
- 자동 번역처럼 보이는 문장은 기술 문서로 자연스럽게 다듬는다.
- 리뷰 보고서는 과장 없이, 확인한 범위와 남은 리스크를 분리해 쓴다.
