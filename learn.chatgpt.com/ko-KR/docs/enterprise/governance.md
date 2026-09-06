<!-- source: https://learn.chatgpt.com/ko-KR/docs/enterprise/governance -->

Codex 활동에 대한 거버넌스에는 대화형 분석, 프로그래밍 방식의 보고,
관련 ChatGPT 사용량 제어, 감사 기록이 포함됩니다. 질문에 맞는
도구를 선택하세요. 분석 데이터와 컴플라이언스 데이터는
용도가 서로 다릅니다.

<a id="governance-and-observability"></a>
<a id="ways-to-track-codex-usage"></a>

| 필요한 작업                                          | 먼저 사용할 도구                                                                |
| ------------------------------------------------------- | ------------------------------------------------------------------------- |
| ChatGPT 전반의 도입 현황 파악                      | [워크스페이스 분석](/ko-KR/codex/enterprise/workspace-analytics)              |
| Codex 도입 현황과 활동을 대화형으로 검토        | [Codex 분석](#analytics-dashboard)                                   |
| 집계된 Codex 보고 데이터를 다른 시스템에 로드     | [Analytics API](/ko-KR/codex/enterprise/analytics-api)                          |
| 감사 또는 조사를 위해 기록 내보내기               | [Compliance API](/ko-KR/codex/enterprise/compliance-api)                        |
| 플랜에 따른 ChatGPT 워크스페이스 크레딧 제어 검토 | [ChatGPT 사용량 한도 및 지출 제어](/ko-KR/codex/enterprise/usage-limits) |

## 관리 도구 열기

- 워크스페이스 보고 데이터를 대화형으로 살펴보려면 [워크스페이스 분석](https://chatgpt.com/admin/usage)을 여세요.
  [워크스페이스 분석 가이드](https://help.openai.com/en/articles/10875114-workspace-analytics-for-chatgpt-enterprise-and-edu)에서
  현재 제공되는 역할과 뷰를 설명합니다.
- 정해진 일정에 따라 프로그래밍 방식으로 보고 작업을 수행하려면
  [Codex Analytics API 레퍼런스](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics)를 여세요.
- 감사 및 조사 통합 작업을 하려면 [Admin API 레퍼런스](https://chatgpt.com/public/admin/api-reference)와
  [컴플라이언스 플랫폼 가이드](https://help.openai.com/en/articles/9261474-compliance-api-for-chatgpt-enterprise-edu-and-chatgpt-for-teachers)를
  여세요.

예를 들어 도입 현황을 빠르게 확인하려면 워크스페이스 분석을 사용하세요.
집계된 Codex 보고 데이터를 비즈니스 인텔리전스 시스템에 로드하려면 Analytics API를,
감사 가능한 기록을 SIEM 또는 전자 증거개시 워크플로우로 전송하려면
Compliance API를 사용하세요.

## 분석 대시보드

<a id="dashboard-views"></a>
<a id="data-export"></a>

ChatGPT는 전반적인 도입 및 참여 현황을 파악할 수 있는 워크스페이스 전체 분석을 제공합니다.
Codex 분석은 Codex 활동에 초점을 맞춥니다. 둘 다 대화형 보고
도구이며, 원시 감사 로그가 아닙니다.

두 분석 환경을 비교하고 각 담당자가 관리하는 최신 자료를 찾으려면
[워크스페이스 분석](/ko-KR/codex/enterprise/workspace-analytics)을 참고하세요. [워크스페이스 분석](https://chatgpt.com/admin/usage)을
직접 열 수도 있습니다. 대시보드 라벨이나 다운로드한 보고서 필드를 기반으로
장기적으로 유지할 보고 데이터 규격을 정하지 마세요.
제품이 발전하면서 이러한 라벨과 필드는 바뀔 수 있습니다.

## 관련 ChatGPT 사용량 제어

ChatGPT 워크스페이스 사용량 제어는 분석과 별개이며 기능 사용 권한을
설정하지 않습니다. 플랜에 따라 적용 대상인 Codex 활동에
ChatGPT 워크스페이스 크레딧이 사용될 수 있으며, 한도가 소진되면
적용 대상 기능의 이용이 일시 중지될 수 있습니다. 이러한 제어는 Codex 전체에 적용되는 한도를 설정하거나
Platform API 청구를 관리하지 않습니다.

장기적으로 유지되는 적용 범위와 최신 도움말 센터 자료는
[ChatGPT 사용량 한도 및 지출 제어](/ko-KR/codex/enterprise/usage-limits)에서 확인하세요.

## Analytics API

<a id="what-it-measures"></a>
<a id="endpoints"></a>
<a id="usage"></a>
<a id="code-review-activity"></a>
<a id="user-engagement-with-code-review"></a>
<a id="how-it-works"></a>
<a id="common-use-cases"></a>

집계된 Codex 보고 데이터를 프로그래밍 방식으로 활용하려면 Analytics API를 사용하세요.
데이터 웨어하우스, 비즈니스 인텔리전스 시스템, 대화형 대시보드에 의존하지 않아야 하는
내부 보고에 적합합니다.

API 레퍼런스는 액세스 요구사항, 라우트, 스키마,
필드, 보고 기간, 페이지네이션에 관한 기준 문서입니다.
통합 범위에 대한 개념 설명과 공식 레퍼런스 링크는 [Analytics API](/ko-KR/codex/enterprise/analytics-api)에서
확인하세요.

## Compliance API

<a id="what-it-measures-1"></a>
<a id="what-you-can-export"></a>
<a id="activity-logs"></a>
<a id="metadata-for-audit-and-investigation"></a>
<a id="common-use-cases-1"></a>
<a id="what-it-does-not-provide"></a>

감사 가능한 기록이 필요한 보안, 법무, 거버넌스 워크플로우에는
Compliance API를 사용하세요. 이 API는 도입 현황이나 생산성을 보여 주는 대시보드가 아닙니다.

API 레퍼런스는 이벤트 범위, 스키마, 권한,
필터, 데이터 보존, 요청 처리 방식에 관한 기준 문서입니다.
통합 범위에 대한 개념 설명과 공식 레퍼런스 링크는 [Compliance API](/ko-KR/codex/enterprise/compliance-api)에서
확인하세요.

<a id="recommended-pattern"></a>

이러한 도구의 도입 순서와 검증 방법은
[관리자용 도입 가이드](/ko-KR/codex/enterprise/admin-setup)를 참고하세요.

## 관련 문서

- [관리자용 도입 가이드](/ko-KR/codex/enterprise/admin-setup)
- [워크스페이스 분석](/ko-KR/codex/enterprise/workspace-analytics)
- [Analytics API](/ko-KR/codex/enterprise/analytics-api)
- [Compliance API](/ko-KR/codex/enterprise/compliance-api)
