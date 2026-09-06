<!-- source: https://learn.chatgpt.com/ko-KR/docs/enterprise/plugin-management -->

## 시작하기 전에

워크스페이스 관리자는 GitHub에서 플러그인 마켓플레이스를 가져오고 레포지토리의 변경 사항을 반영해 플러그인을 최신 상태로 유지할 수 있습니다. 마켓플레이스는 가져올 플러그인 목록이 담긴 JSON 카탈로그입니다.

마켓플레이스 레포지토리와 여기서 참조하는 다른 모든 레포지토리를 읽을 수 있는 GitHub 계정을 사용하세요. 공개 및 비공개 GitHub 레포지토리를 지원합니다. 가져오기 전에 레포지토리 액세스에 필요한 GitHub 조직 승인을 모두 받으세요.

가져오기 전에 레포지토리 내용을 검토하세요. 새 플러그인은 설치 정책이 **사용 가능으로** 설정되며, 설치 시 인증하도록 구성됩니다. 새 마켓플레이스는 매일 자동으로 동기화하도록 설정됩니다. 가져오기 작업은 유효한 항목을 모두 처리하며, 이후 동기화에서는 레포지토리의 새 플러그인을 모두 자동으로 추가합니다.

## 마켓플레이스 동기화 구성

1. **관리자** \> **플러그인을** 열고 **추가** \> **마켓플레이스 가져오기를** 선택하세요.
2. **소스에** 레포지토리 URL(예: `https://github.com/example/team-plugins`)을 입력하세요. 브랜치나 폴더 URL이 아닌 레포지토리 URL만 사용하세요.
3. 마켓플레이스가 하위 디렉터리에 있다면 **경로에** 해당 디렉터리를 입력하세요. 예를 들어 `team-tools/.agents/plugins/marketplace.json`의 경우 `team-tools`를 입력하세요. 레포지토리 루트를 사용하려면 **경로를** 비워 두세요. 매니페스트 파일 이름은 입력하지 마세요.
4. 필요한 경우 **브랜치, 태그 또는 커밋을** 입력하세요. 비워 두면 레포지토리의 기본 브랜치를 사용합니다. 이후 커밋을 반영하려면 브랜치를 사용하세요. 특정 커밋으로 고정하면 해당 리비전이 유지됩니다.
5. **마켓플레이스 가져오기를** 선택하고, GitHub 액세스 승인 요청이 표시되면 승인하세요. 마켓플레이스 규모가 매우 크면 처음 가져오는 데 최대 1시간이 걸릴 수 있습니다. 이후 매일 수행되는 동기화는 보통 몇 분 정도 걸립니다.
6. **가져오기 결과를** 검토한 다음, 가져온 플러그인을 하나씩 열어 설치 정책과 필요한 앱을 구성하세요.

일일 동기화를 기다리지 않고 업데이트를 요청하려면 **관리자** \> **플러그인** \> **마켓플레이스에서** 해당 마켓플레이스를 열고 **지금 동기화를** 선택하세요.

## 지원 형식

선택한 디렉터리에는 다음 파일 중 하나가 있어야 합니다:

| 파일                               | 형식                                                               |
| ---------------------------------- | -------------------------------------------------------------------- |
| `.agents/plugins/marketplace.json` | `plugins` 배열이 있는 Codex 마켓플레이스.                          |
| `.claude-plugin/marketplace.json`  | `plugins` 배열이 있는 Claude 호환 마켓플레이스.              |
| `.claude-plugin/plugin.json`       | 마켓플레이스 매니페스트가 없을 때 사용하는 독립형 Claude 플러그인. |

마켓플레이스의 항목은 `.codex-plugin/plugin.json` 파일이 있는 네이티브 플러그인, Claude 호환 플러그인, Agent Plugins 1.0 패키지 또는 지원되는 스킬 패키지를 참조할 수 있습니다.

Codex 마켓플레이스에서는 같은 레포지토리에 있는 플러그인에 로컬 경로를 사용하세요:

```json
{
  "name": "team-plugins",
  "interface": {
    "displayName": "Team plugins"
  },
  "plugins": [
    {
      "name": "team-tools",
      "source": {
        "source": "local",
        "path": "./plugins/team-tools"
      }
    }
  ]
}

이 경로는 `.agents/plugins/` 디렉터리가 아닌 선택한 마켓플레이스 루트 기준의 상대 경로입니다.

Claude 호환 마켓플레이스에서는 각 로컬 플러그인에 경로 문자열을 사용할 수 있습니다:

```json
{
  "name": "team-plugins",
  "plugins": [
    {
      "name": "team-tools",
      "source": "./plugins/team-tools"
    }
  ]
}

Codex 마켓플레이스 항목은 GitHub 레포지토리 루트의 플러그인을 위한 `source: "url"` 형식과 GitHub 하위 디렉터리의 플러그인을 위한 `source: "git-subdir"` 형식도 지원합니다. 예를 들면 다음과 같습니다:

```json
{
  "name": "team-tools",
  "source": {
    "source": "git-subdir",
    "url": "https://github.com/example/team-tools.git",
    "path": "./plugins/team-tools",
    "ref": "main"
  }
}

Git 소스에서는 `ref` 또는 40자 전체 커밋 `sha`를 지정할 수 있습니다. 액세스를 승인하는 GitHub 계정은 참조된 모든 레포지토리를 읽을 수 있어야 합니다. 워크스페이스 가져오기 기능은 현재 GitHub 레포지토리만 지원합니다.

## 워크스페이스 액세스 구성

GitHub에서 가져오거나 동기화할 때는 `AVAILABLE`, `INSTALLED_BY_DEFAULT`, `NOT_AVAILABLE`, `ON_INSTALL`, `ON_USE` 등 레포지토리에 정의된 설치 또는 인증 정책을 적용하지 않습니다. 워크스페이스 관리자가 플러그인별로 이러한 설정을 구성합니다. 업데이트를 동기화하거나 기존 플러그인을 GitHub 관리로 전환해도 해당 플러그인의 워크스페이스 정책은 유지됩니다.

**설치 정책에서** 적용 가능한 각 역할에 대해 **사용 가능** 또는 **설치됨을** 선택하세요. 필요한 앱도 활성화되어 있어야 하며, 구성원은 연결된 서비스에 액세스할 수 있어야 합니다. 플러그인을 가져와도 앱 액세스 권한이 부여되거나 구성원의 계정이 연결되지는 않습니다. 역할, 앱, 액션 제어에 관한 내용은 [플러그인 제어](/ko-KR/codex/enterprise/apps-and-connectors)를 참고하세요.

## 기존 플러그인을 GitHub 관리로 전환하기

기존 플러그인의 마켓플레이스 항목에 `pluginId`를 추가하세요:

```json
{
  "name": "team-tools",
  "pluginId": "plugin_0123456789abcdef0123456789abcdef",
  "source": {
    "source": "local",
    "path": "./plugins/team-tools"
  }
}

**관리자** \> **플러그인에서** 해당 플러그인을 열고 URL에서 `/admin/plugins/` 뒤에 있는 ID를 복사하세요. 마켓플레이스 항목의 `name` 및 `source` 옆에 `pluginId`를 넣으세요. 기존 플러그인은 같은 워크스페이스에 있어야 합니다.

이렇게 하면 업로드된 플러그인 등 관리되지 않는 워크스페이스 플러그인이 GitHub 관리로 전환됩니다. 플러그인의 ID, 공유 설정, 워크스페이스 정책은 유지됩니다. 이후 업데이트는 GitHub에서 가져오며, 더 이상 아카이브 업로드로 관리 대상 플러그인을 교체할 수 없습니다. 다른 GitHub 소스에서 이미 관리 중인 플러그인은 이 방식으로 이전할 수 없습니다.

## 데스크톱 전용 플러그인

`mcp.json` 또는 `.mcp.json`에 MCP 서버를 선언한 플러그인을 가져오면 **데스크톱 전용으로** 표시되며, ChatGPT 데스크톱 앱에서만 작동합니다. 여기에는 원격 HTTPS URL을 사용하는 서버도 포함됩니다. 인라인 서버 선언 등 지원되는 다른 MCP 구성 형식에도 같은 제한이 적용됩니다.

## `.app.json`으로 기존 앱 참조하기

플러그인 루트에 `.app.json`을 추가하세요. 파일 이름은 점으로 시작해야 하며, 점이 없는 `app.json`은 지원되지 않습니다.

```json
{
  "apps": {
    "team-tools": {
      "id": "asdk_app_example",
      "required": true
    }
  }
}

`asdk_app_example`을 기존 앱의 ID로 바꾸세요. 지원되는 앱 ID는 `asdk_app_`, `connector_` 또는 `templated_apps_`로 시작합니다. `plugin_...` ID가 아닌 앱 ID를 사용하세요. 예를 들어 `plugin_asdk_app_example`이 포함된 플러그인 URL은 `asdk_app_example` 앱을 나타냅니다.

`team-tools` 키는 이 파일 내에서 참조 이름을 지정합니다. 플러그인이 해당 앱에 의존한다면 `required`를 `true`로 설정하세요. 다른 기존 앱을 참조하려면 항목을 더 추가할 수 있습니다.

네이티브 플러그인의 경우 `.codex-plugin/plugin.json`에서 `apps`를 `./.app.json`으로 설정하세요. 다음은 이 예제의 전체 매니페스트입니다:

```json
{
  "name": "team-tools",
  "version": "1.0.0",
  "description": "Use the team's approved tools.",
  "author": {
    "name": "Example team"
  },
  "apps": "./.app.json",
  "interface": {
    "displayName": "Team tools",
    "shortDescription": "Use approved team tools",
    "longDescription": "Connect to the team's existing app.",
    "developerName": "Example team",
    "category": "Productivity",
    "capabilities": ["Read"]
  }
}

파일은 다음 구조로 배치하세요:

```text
team-plugins/
├── .agents/plugins/marketplace.json
└── plugins/team-tools/
    ├── .codex-plugin/plugin.json
    └── .app.json

이 참조는 앱을 만들거나 권한을 부여하지 않습니다. 관리자는 대상 역할에서 앱을 사용할 수 있도록 설정해야 하며, 구성원은 필요한 인증을 완료해야 합니다. 기존 앱 권한, 액션 제어, 서비스 액세스는 그대로 적용됩니다.

## 플러그인을 최신 상태로 유지하기

새 마켓플레이스는 매일 업데이트를 확인합니다. 자동 동기화를 기다리지 않고 업데이트를 요청하려면 **관리자** \> **플러그인** \> **마켓플레이스를** 열고 해당 마켓플레이스를 선택한 다음 **지금 동기화를** 선택하세요.

동기화를 통해 새 마켓플레이스 항목을 추가하고 기존 플러그인을 업데이트할 수 있습니다. 자동 동기화 시 새 플러그인을 모두 가져오므로 레포지토리 변경 사항을 병합하기 전에 검토하세요.

동기화 후 상태와 저장된 보고서를 검토하세요. **완료 — 오류 N개** 상태는 동기화가 끝났지만 일부 플러그인을 처리하지 못했다는 뜻입니다. 기존 플러그인의 업데이트가 유효하지 않으면 마지막으로 정상 작동한 버전이 유지됩니다. GitHub에서 보고된 문제를 수정한 다음 **지금 동기화를** 선택해 다시 시도하세요.

레포지토리에서 항목을 삭제해도 워크스페이스로 가져온 사본은 삭제되지 않습니다. 해당 사본은 **더 이상 소스에 없음** 상태로 표시됩니다. ChatGPT에서 마켓플레이스를 삭제하면 해당 마켓플레이스에서 가져온 플러그인이 모두 삭제됩니다.

## GitHub 액세스 재연결 또는 변경

**GitHub 액세스를 다시 연결하려면** 먼저 가져오기에 사용한 GitHub 계정이 해당 레포지토리와 참조된 모든 레포지토리에 여전히 액세스할 수 있는지 확인하세요. 그런 다음 처음 마켓플레이스를 가져온 관리자가 ChatGPT에서 GitHub 플러그인을 열고 자신의 계정을 다시 연결해야 합니다. 마켓플레이스 동기화에는 해당 관리자의 GitHub 연결이 사용되기 때문입니다.

**새 소유자에게 이전하려면** 새 워크스페이스 관리자가 **관리자** \> **플러그인** \> **추가** \> **마켓플레이스 가져오기를** 열고, **소스**, **경로**, **브랜치, 태그 또는 커밋에** 동일한 값을 사용해 같은 마켓플레이스를 가져와야 합니다. 이후 동기화에는 새 관리자의 GitHub 연결이 사용됩니다.

다시 연결하거나 소유자를 변경하려는 목적으로 마켓플레이스를 삭제하지 마세요. 삭제하면 가져온 플러그인도 함께 삭제됩니다.
