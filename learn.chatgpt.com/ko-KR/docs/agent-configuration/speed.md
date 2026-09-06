<!-- source: https://learn.chatgpt.com/ko-KR/docs/agent-configuration/speed -->

<strong>ChatGPT Work와 Codex는 사용량을 공유합니다.</strong> 두 제품에는 동일한
  요금, 크레딧, 사용량 한도가 적용됩니다. 자세한 내용은
  [Codex 요금](/codex/pricing)을 참조하세요.

## 패스트 모드

Codex에서는 크레딧을 더 많이 사용하는 대신 모델의 속도를 높일 수 있습니다.

GPT-5.6, GPT-5.5, GPT-5.4에서 패스트 모드를 사용하면 모델 속도가 1.5배로 빨라집니다.
GPT-5.6과 GPT-5.5는 표준 모드의 2.5배, GPT-5.4는 표준 모드의 2배에 해당하는 크레딧을 소모합니다.

GPT-6 Astra 패스트 모드가 제공되는 경우, 크레딧은 표준 모드의
2.5배로 소모됩니다. 모델 제공 여부는 [모델](/ko-KR/codex/models)을,
토큰 요금은 [요금](/ko-KR/codex/pricing#token-rates)을 참조하세요.

CLI에서 `/fast on`, `/fast off` 또는 `/fast status` 명령어를 사용해 현재 설정을 변경하거나
확인할 수 있습니다. 또한 `config.toml` 파일에 `service_tier =
"fast"` 설정과 `[features].fast_mode = true` 설정을 함께 추가해 기본값을 저장할 수 있습니다.
ChatGPT로 로그인하면 ChatGPT 데스크톱 앱, Codex CLI 및 IDE 확장에서
패스트 모드를 사용할 수 있습니다. 패스트 모드는 ChatGPT 크레딧 기능입니다. API 키를 사용하면
Codex에 API 토큰 요금이 대신 적용되며, ChatGPT 크레딧 소모 배수는
적용되지 않습니다. API Priority 처리에는 별도의 요율이 적용되며, GPT-5.6의 경우
표준 API 토큰 요율의 2배입니다.

## Codex-Spark

GPT-5.3-Codex-Spark는 거의 즉각적인 응답으로 실시간 코딩 반복 작업을 수행하도록 최적화된 별도의 Codex 모델로, 빠르지만 작업 수행 능력은 비교적 제한적입니다. 패스트 모드는 지원 모델의 속도를 높이는 대신 크레딧 소모율이 증가하지만, Codex-Spark는 별도로 선택하는 모델이며 자체 사용량 한도가 적용됩니다.

연구 프리뷰 기간에는 Codex-Spark가 ChatGPT Pro 구독자에게만 제공됩니다.
