<!-- source: https://learn.chatgpt.com/ko-KR/docs/third-party/linear -->

Linear에서 Codex를 사용해 이슈 작업을 위임하세요. 이슈를 Codex에 할당하거나 댓글에서 `@Codex`를 멘션하면 Codex가 클라우드 채팅을 만들고 진행 상황과 결과를 답글로 알려줍니다.

Linear의 Codex는 유료 플랜에서 사용할 수 있습니다([요금](/ko-KR/codex/pricing) 참조).

엔터프라이즈 플랜을 사용 중이라면 ChatGPT 워크스페이스 관리자에게 [워크스페이스 설정](https://chatgpt.com/admin/settings)에서 Codex 클라우드 채팅을 켜고 [커넥터 설정](https://chatgpt.com/admin/ca)에서 **Codex for Linear를** 활성화해 달라고 요청하세요.

## Linear 연동 설정

1. [Codex 클라우드 채팅](/ko-KR/codex/cloud)을 설정하려면 [Codex](https://chatgpt.com/codex)에서 GitHub를 연결하고 Codex가 작업할 레포지토리용 [환경](/ko-KR/codex/environments/cloud-environment)을 만드세요.
2. [Codex 설정](https://chatgpt.com/codex/settings/connectors)으로 이동해 워크스페이스에 **Codex for Linear를** 설치하세요.
3. Linear 이슈의 댓글 스레드에서 `@Codex`를 멘션해 Linear 계정을 연결하세요.

## Codex에 작업 위임

다음 두 가지 방법으로 작업을 위임할 수 있습니다:

### Codex에 이슈 할당

연동을 설치한 후에는 팀원에게 할당할 때와 같은 방식으로 이슈를 Codex에 할당할 수 있습니다. Codex가 작업을 시작하고 진행 상황을 이슈에 게시합니다.

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

### 댓글에서 `@Codex`를 멘션하기

댓글 스레드에서 `@Codex`를 멘션해 작업을 위임하거나 질문할 수도 있습니다. Codex가 답변하면 같은 스레드에 후속 댓글을 남겨 동일한 채팅을 이어갈 수 있습니다.

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

Codex는 이슈 작업을 시작하면 작업할 [환경과 레포지토리를 선택합니다](#how-codex-chooses-an-environment-and-repo).
특정 레포지토리를 지정하려면 댓글에 해당 레포지토리를 포함하세요. 예: `@Codex fix this in openai/codex`.

진행 상황을 확인하려면:

- 이슈에서 **활동을** 열어 진행 상황 업데이트를 확인하세요.
- 자세한 진행 상황을 확인하려면 채팅 링크를 여세요.

Codex가 작업을 완료하면 요약과 완료된 채팅 링크를 게시하므로 이를 통해 Pull Request를 만들 수 있습니다.

### Codex가 환경과 레포지토리를 선택하는 방식

- Linear는 이슈 컨텍스트를 바탕으로 레포지토리를 제안합니다. Codex는 해당 제안과 가장 잘 맞는 환경을 선택합니다. 요청이 모호하면 가장 최근에 사용한 환경을 대신 선택합니다.
- 채팅은 해당 환경의 레포지토리 맵에 첫 번째로 나열된 레포지토리의 기본 브랜치를 기준으로 실행됩니다. 기본 레포지토리를 변경하거나 레포지토리를 추가해야 한다면 Codex에서 레포지토리 맵을 업데이트하세요.
- 적합한 환경이나 레포지토리가 없으면 Codex가 Linear에 답글을 게시해 다시 시도하기 전에 문제를 해결하는 방법을 안내합니다.

## Codex에 이슈 자동 할당

트리아지 규칙을 사용해 이슈를 Codex에 자동으로 할당할 수 있습니다:

1. Linear에서 **설정으로** 이동하세요.
2. **내 팀에서** 팀을 선택하세요.
3. 워크플로우 설정에서 **트리아지를** 열고 활성화하세요.
4. **트리아지 규칙에서** 규칙을 만들고 **위임** \> **Codex를** 선택하세요(원하는 다른 속성도 함께 설정하세요).

Linear는 트리아지로 들어온 새 이슈를 Codex에 자동으로 할당합니다.
트리아지 규칙을 사용하면 Codex는 이슈 작성자의 계정으로 채팅을 실행합니다.

<div class="not-prose max-w-3xl mr-auto my-4">
  
    
      
    
  
</div>

## 데이터 사용, 개인정보 보호 및 보안

`@Codex`를 멘션하거나 이슈를 Codex에 할당하면 Codex는 요청을 파악하고 채팅을 만들기 위해 이슈 내용을 전달받습니다.
데이터는 OpenAI의 [개인정보 보호 정책](https://openai.com/privacy), [이용약관](https://openai.com/terms/) 및 그 밖에 적용되는 [정책](https://openai.com/policies)에 따라 처리됩니다.
보안에 대한 자세한 내용은 [Codex 보안 문서](/ko-KR/codex/agent-approvals-security)를 참조하세요.

Codex는 실수할 수 있는 대규모 언어 모델을 사용합니다. 답변과 diff를 항상 검토하세요.

## 팁 및 문제 해결

- **연결 누락**: Codex가 Linear 연결을 확인할 수 없으면 이슈에 계정 연결 링크가 포함된 답글을 게시합니다.
- **예기치 않은 환경 선택**: 원하는 환경을 지정해 스레드에 답글을 남기세요(예: `@Codex please run this in openai/codex`).
- **잘못된 코드 영역**: 이슈에 컨텍스트를 더 추가하거나 `@Codex` 댓글에 명확한 지침을 작성하세요.
- **추가 도움말**: [OpenAI 도움말 센터](https://help.openai.com/)를 참조하세요.

<a id="connect-linear-for-local-tasks-mcp"></a>

## 로컬 작업을 위한 Linear 연결(MCP)

ChatGPT 데스크톱 앱, Codex CLI 또는 IDE 확장을 사용해 로컬에서 Linear 이슈에 액세스하려면 Linear Model Context Protocol (MCP) 서버를 구성하세요.

자세한 내용은 [Linear MCP 문서](https://linear.app/integrations/codex-mcp)를 확인하세요.

IDE 확장과 CLI는 동일한 구성을 공유하므로 어느 것을 사용하든 MCP 서버 설정 단계는 같습니다.

### CLI 사용(권장)

CLI가 설치되어 있다면 다음 명령을 실행하세요:

```bash
codex mcp add linear --url https://mcp.linear.app/mcp

이 명령을 실행하면 Linear 계정으로 로그인하고 해당 계정을 Codex에 연결하라는 메시지가 표시됩니다.

### 수동 구성

1. 편집기에서 `~/.codex/config.toml` 파일을 여세요.
2. 다음을 추가하세요:

```toml
[mcp_servers.linear]
url = "https://mcp.linear.app/mcp"

3. 로그인하려면 `codex mcp login linear` 명령을 실행하세요.
