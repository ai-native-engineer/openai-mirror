<!-- source: https://learn.chatgpt.com/ko-KR/docs/enterprise/analytics-api -->

Codex Analytics API는 ChatGPT 워크스페이스의 Codex 사용량과 활동을 집계한
지표를 제공합니다.

[Codex Analytics API 레퍼런스](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics)는 현재 적용되는 접근 요구 사항, 라우트,
요청 및 응답 스키마, 지표, 시간 해석 규칙, 페이지네이션에 관한
공식 기준 문서입니다.

## Analytics API가 적합한 경우

다음과 같은 작업이 필요할 때 Analytics API가 적합합니다:

- 정기적인 Codex 보고를 자동화합니다.
- 집계된 Codex 지표와 조직 내부 데이터를 결합합니다.
- 승인된 사용자 그룹을 위한 통제된 보고 레이어를 구축합니다.
- 통합 기능이 대화형 대시보드에 종속되지 않도록 합니다.

원시 감사 로그를 제공하는 인터페이스는 아닙니다.
워크플로우에 감사 가능한 활동 기록이 필요한 경우
[Compliance API](/ko-KR/codex/enterprise/compliance-api)를 사용하세요.

## 관리 범위 확인

Analytics API 결과는 ChatGPT 워크스페이스 범위로 제한되지만, 요청 인증에는
Platform 조직 API 키를 사용합니다. 키가 속한 조직은 워크스페이스와 연결된
조직과 일치해야 합니다.

현재 적용되는 키 발급 방식, 스코프 요구 사항, 라우트, 스키마, 필드,
시간 해석 규칙, 페이지네이션 동작은 API 레퍼런스를 기준으로 합니다.
이 페이지에서는 해당 명세를 중복해서 설명하지 않습니다.

## 관련 문서

- [워크스페이스 분석](/ko-KR/codex/enterprise/workspace-analytics)
- [관리자용 도입 가이드](/ko-KR/codex/enterprise/admin-setup)
- [거버넌스](/ko-KR/codex/enterprise/governance)
- [Compliance API](/ko-KR/codex/enterprise/compliance-api)
