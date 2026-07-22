---
name: openai-mirror
description: "이 repo의 OpenAI 공개 자료 미러를 증분 갱신하거나 전량 재수집하고, 생성물을 검증해 로컬 커밋한다. openai.com, OpenAI Academy, 개발자 문서, Help Center, Model Spec, OpenAI YouTube 자막, OpenAI 소유 PDF를 수집한다. Use when 'OpenAI 미러 갱신/재생성', '누락 페이지 복구', 'Academy/YouTube/PDF 재수집', 'openai-mirror'를 요청할 때. Do NOT use for OpenAI API/제품 사용 질문(openai-docs), 저장된 미러 검색, 단일 URL 크롤(crawl), Anthropic/Claude 미러."
---

# OpenAI Mirror

이 repo의 생성기와 발행 절차다. 생성물은 직접 수정하지 않고 수집기를 고쳐 다시 생성한다.

## 작업 라우팅

| 작업 | 먼저 읽을 것 |
|---|---|
| 증분/전량 갱신, 검증, commit, push | `references/publishing.md` |
| 부분 수집, 누락 복구, 수집기 수정 | `references/crawl-notes.md`와 대상 스크립트의 `--help` |

일반 갱신은 `publishing.md`의 로컬 commit까지 완료한다. public push와 삭제 반영은 그 문서의 승인 게이트를 따른다.

## 불변 규칙

- 최신 상태만 제자리 갱신하고 이력은 git에 둔다.
- `_yt-cache/`는 gitignored 작업 캐시이며 발행하지 않는다.
- 외부 인용 PDF는 제외하고 OpenAI 소유 PDF만 원본으로 미러한다.
