<!-- source: https://learn.chatgpt.com/ko-KR/docs/third-party/slack -->

Slack 채널과 스레드에서 Codex를 사용해 코딩 작업을 시작하세요. 프롬프트와 함께 `@Codex`를 멘션하면 Codex가 클라우드 채팅을 만들고 결과를 답글로 게시합니다.

<div class="not-prose max-w-3xl mr-auto">
  
    
      
    
  
</div>

<br />

## Slack 앱 설정하기

1. [Codex 클라우드 채팅](/ko-KR/codex/cloud)을 설정하세요. Plus, Pro, Business, 엔터프라이즈 또는 Edu 요금제([ChatGPT 요금](https://chatgpt.com/pricing) 참조), 연결된 GitHub 계정, 하나 이상의 [환경](/ko-KR/codex/environments/cloud-environment)이 필요합니다.
2. [Codex 설정](https://chatgpt.com/codex/settings/connectors)으로 이동해 워크스페이스에 Slack 앱을 설치하세요. Slack 워크스페이스 정책에 따라 관리자의 설치 승인이 필요할 수 있습니다.
3. 채널에 `@Codex`를 추가하세요. 아직 추가하지 않았다면 멘션할 때 Slack에서 앱을 추가하라는 메시지가 표시됩니다.

<a id="start-a-task"></a>

## 채팅 시작하기

1. 채널이나 스레드에서 프롬프트와 함께 `@Codex`를 멘션하세요. Codex는 스레드의 이전 메시지를 참조할 수 있으므로 대개 컨텍스트를 다시 설명하지 않아도 됩니다.
2. (선택 사항) 프롬프트에 환경이나 레포지토리를 지정하세요. 예: `@Codex fix the above in openai/codex`.
3. Codex가 반응(👀)을 남기고 채팅 링크가 포함된 답글을 보낼 때까지 기다리세요. 작업이 완료되면 Codex가 결과를 게시하고, 설정에 따라 스레드에 답변도 게시합니다.

### Codex가 환경과 레포지토리를 선택하는 방식

- Codex는 접근 권한이 있는 환경을 검토하여 요청에 가장 적합한 환경을 선택합니다. 요청이 모호하면 가장 최근에 사용한 환경을 대신 선택합니다.
- 채팅은 해당 환경의 레포지토리 맵에 첫 번째로 나열된 레포지토리의 기본 브랜치를 대상으로 실행됩니다. 다른 레포지토리를 기본값으로 사용하거나 레포지토리를 더 추가하려면 Codex에서 레포지토리 맵을 업데이트하세요.
- 적합한 환경이나 레포지토리가 없으면 Codex는 문제를 해결한 뒤 다시 시도하는 방법을 Slack 답글로 안내합니다.

### 엔터프라이즈 데이터 제어

기본적으로 Codex는 스레드에 답변을 게시하며, 답변에는 작업이 실행된 환경의 정보가 포함될 수 있습니다.
이를 방지하려면 엔터프라이즈 관리자가 [ChatGPT 워크스페이스 설정](https://chatgpt.com/admin/settings)에서 **작업 완료 시 Codex Slack 앱의 답변 게시 허용을** 선택 해제하면 됩니다. 관리자가 답변 게시를 끄면 Codex는 채팅 링크만 답글로 보냅니다.

### 데이터 사용, 개인정보 보호 및 보안

`@Codex`를 멘션하면 Codex는 요청을 파악하고 채팅을 만들기 위해 메시지와 스레드 기록을 수신합니다.
데이터는 OpenAI의 [개인정보 보호 정책](https://openai.com/privacy), [이용약관](https://openai.com/terms/) 및 기타 관련 [정책](https://openai.com/policies)에 따라 처리됩니다.
보안에 대한 자세한 내용은 Codex의 [보안 문서](/ko-KR/codex/agent-approvals-security)를 참조하세요.

Codex는 실수할 수 있는 대규모 언어 모델을 사용합니다. 답변과 diff를 항상 검토하세요.

### 팁 및 문제 해결

- **연결 누락**: Codex가 Slack 또는 GitHub 연결을 확인할 수 없으면 다시 연결할 수 있는 링크가 포함된 답글을 보냅니다.
- **예상치 않은 환경 선택**: 스레드에서 원하는 환경을 지정해 답글을 작성한 다음(예: `Please run this in openai/openai (applied)`), `@Codex`를 다시 멘션하세요.
- **길거나 복잡한 스레드**: Codex가 스레드 앞부분에 묻혀 있는 컨텍스트를 놓치지 않도록 가장 최근 메시지에 핵심 내용을 요약하세요.
- **워크스페이스에 게시**: 일부 엔터프라이즈 워크스페이스에서는 최종 답변 게시를 제한합니다. 이 경우 채팅 링크를 열어 진행 상황과 결과를 확인하세요.
- **추가 도움말**: [OpenAI 도움말 센터](https://help.openai.com/)를 참조하세요.
