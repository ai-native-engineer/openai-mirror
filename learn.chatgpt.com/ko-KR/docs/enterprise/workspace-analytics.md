<!-- source: https://learn.chatgpt.com/ko-KR/docs/enterprise/workspace-analytics -->

워크스페이스 전반의 도입 현황을 파악하려면 ChatGPT 워크스페이스 분석을 사용하세요. Codex 중심의
보고에는 Codex 분석을 사용하세요. 집계 데이터를 프로그래밍 방식으로 조회하려면 Analytics API를,
감사 가능한 기록이 필요하면 Compliance API를 사용하세요.

이러한 보고 수단은 제품 접근 권한을 부여하거나 런타임 정책을 설정하지 않습니다. 관리 범위는
[역할 및 워크스페이스 권한](/ko-KR/codex/enterprise/roles-and-workspace-permissions)을
참조하세요.

## 보고 수단 선택

| 보고 수단                     | 용도                                                    | 명세 출처                                                                                                         |
| --------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| ChatGPT 워크스페이스 분석 | 워크스페이스 전반의 도입 및 참여 현황에 대한 대화형 보고 | [워크스페이스 분석 도움말 센터 안내](https://help.openai.com/en/articles/10875114)                               |
| Codex 분석             | Codex 도입 및 활동에 중점을 둔 대화형 보고  | 인증 후 이용할 수 있는 [Codex 분석 대시보드](https://admin.openai.com/analytics/codex)                                |
| Analytics API               | 프로그래밍 방식의 Codex 집계 보고                      | [Codex Analytics API 레퍼런스](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics) |
| Compliance API              | 감사, 보안, 법무 및 조사 기록             | [Admin API 레퍼런스](https://chatgpt.com/public/admin/api-reference)                                              |

## ChatGPT 워크스페이스 분석 검토

ChatGPT 워크스페이스 분석에서는 지원되는 워크스페이스 기능 전반의 도입 및
참여 현황을 대화형으로 확인할 수 있습니다. 제공 여부, 역할, 대시보드
섹션, 데이터 최신성, 개인정보 보호 처리 방식, 내보내기 형식은 변경될 수 있습니다. 현재 지원 범위와 절차는
[ChatGPT Enterprise 및 Edu용 워크스페이스 분석](https://help.openai.com/en/articles/10875114)에서
확인하세요.

다운로드한 보고서는 개인을 식별할 수 있는 조직 데이터로 취급하세요.
내보낸 보고서가 집계 대시보드와 동일한 개인정보 보호 특성을 지닌다고
가정하지 말고 조직의 접근, 저장 및 보존 정책을
적용하세요.

## Codex 분석 검토

인증 후 이용할 수 있는 [Codex 분석 대시보드](https://admin.openai.com/analytics/codex)는
Codex 보고에 중점을 둡니다. 안정적인 스키마 명세로 간주하지 말고
대화형 탐색에 사용하세요. 대시보드의 카테고리, 필드, 필터 및 내보내기 형식은
이 페이지와 별개로 변경될 수 있습니다.

자동화된 보고에는 [Analytics API](/ko-KR/codex/enterprise/analytics-api)를
사용하고 해당 API 레퍼런스의 지침을 따르세요. 감사 가능한 기록에는
[Compliance API](/ko-KR/codex/enterprise/compliance-api)를 사용하세요.

## 보고 데이터 해석

다음 구분을 염두에 두세요:

- ChatGPT 워크스페이스 분석과 Codex 분석은 다루는 제품
범위가 서로 다릅니다.
- 집계 분석 데이터와 감사 기록은 용도가 서로 다르며 각각 별도의
명세가 적용됩니다.
- 분석은 활동 현황을 보여줄 뿐이며, 접근 권한을 부여하거나 런타임
권한을 변경하지 않습니다.
- [ChatGPT 사용 한도 및 지출 제어](/ko-KR/codex/enterprise/usage-limits)는
  플랜에 따라 달라지는 별도의 워크스페이스 제한 사항입니다.
